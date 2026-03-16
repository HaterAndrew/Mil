"""Training Readiness Tracker — FastAPI application."""

from __future__ import annotations

import csv
import io
from contextlib import asynccontextmanager
from datetime import date

from fastapi import Depends, FastAPI, File, HTTPException, Query, UploadFile, status
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from .db import (
    ALL_COURSES,
    PREREQ_CHAIN,
    Completion,
    Trainee,
    check_eligibility,
    get_db,
    get_next_recommended,
    get_unit_rollup,
    init_db,
)
from .models import (
    CompletionCreate,
    CompletionResponse,
    EligibilityCheck,
    TraineeCreate,
    TraineeListItem,
    TraineeResponse,
    UnitRollup,
    UploadResult,
)


# ---------------------------------------------------------------------------
# App lifecycle
# ---------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Training Readiness Tracker",
    description="Track soldier/unit completion across the MSS TM prereq chain.",
    version="1.0.0",
    lifespan=lifespan,
)


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------
@app.get("/health")
def health():
    return {"status": "ok"}


# ---------------------------------------------------------------------------
# Trainees
# ---------------------------------------------------------------------------
@app.post("/trainees", response_model=TraineeResponse, status_code=status.HTTP_201_CREATED)
def create_trainee(payload: TraineeCreate, db: Session = Depends(get_db)):
    existing = db.query(Trainee).filter(Trainee.dodid == payload.dodid).first()
    if existing:
        raise HTTPException(status_code=409, detail=f"Trainee {payload.dodid} already exists")
    trainee = Trainee(**payload.model_dump())
    db.add(trainee)
    db.commit()
    db.refresh(trainee)
    resp = TraineeResponse.model_validate(trainee)
    resp.next_recommended = get_next_recommended(trainee.dodid, db)
    return resp


@app.get("/trainees", response_model=list[TraineeListItem])
def list_trainees(
    unit: str | None = None,
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    q = db.query(Trainee)
    if unit:
        q = q.filter(Trainee.unit == unit)
    trainees = q.order_by(Trainee.last_name).offset(offset).limit(limit).all()
    result = []
    for t in trainees:
        item = TraineeListItem.model_validate(t)
        item.completion_count = len([c for c in t.completions if c.result == "GO"])
        result.append(item)
    return result


@app.get("/trainees/{dodid}", response_model=TraineeResponse)
def get_trainee(dodid: str, db: Session = Depends(get_db)):
    trainee = db.query(Trainee).filter(Trainee.dodid == dodid).first()
    if not trainee:
        raise HTTPException(status_code=404, detail=f"Trainee {dodid} not found")
    resp = TraineeResponse.model_validate(trainee)
    resp.eligible_courses = [
        c for c in ALL_COURSES if check_eligibility(dodid, c, db)[0]
    ]
    resp.next_recommended = get_next_recommended(dodid, db)
    return resp


# ---------------------------------------------------------------------------
# Completions
# ---------------------------------------------------------------------------
@app.post("/completions", response_model=CompletionResponse, status_code=status.HTTP_201_CREATED)
def record_completion(payload: CompletionCreate, db: Session = Depends(get_db)):
    # Verify trainee exists
    trainee = db.query(Trainee).filter(Trainee.dodid == payload.dodid).first()
    if not trainee:
        raise HTTPException(status_code=404, detail=f"Trainee {payload.dodid} not found")

    # Verify course exists
    if payload.course_id not in PREREQ_CHAIN:
        raise HTTPException(status_code=422, detail=f"Unknown course: {payload.course_id}")

    # Hard prereq enforcement — only for GO results
    if payload.result == "GO":
        eligible, missing = check_eligibility(payload.dodid, payload.course_id, db)
        if not eligible:
            raise HTTPException(
                status_code=422,
                detail=f"Prereqs not met for {payload.course_id}. Missing: {', '.join(missing)}",
            )

    # Check for existing completion and update if exists
    existing = (
        db.query(Completion)
        .filter(Completion.dodid == payload.dodid, Completion.course_id == payload.course_id)
        .first()
    )
    if existing:
        existing.result = payload.result
        existing.evaluation_date = payload.evaluation_date
        existing.evaluator_name = payload.evaluator_name
        db.commit()
        db.refresh(existing)
        return CompletionResponse.model_validate(existing)

    comp = Completion(**payload.model_dump())
    db.add(comp)
    db.commit()
    db.refresh(comp)
    return CompletionResponse.model_validate(comp)


@app.get("/completions", response_model=list[CompletionResponse])
def list_completions(
    dodid: str | None = None,
    course_id: str | None = None,
    db: Session = Depends(get_db),
):
    q = db.query(Completion)
    if dodid:
        q = q.filter(Completion.dodid == dodid)
    if course_id:
        q = q.filter(Completion.course_id == course_id)
    return [CompletionResponse.model_validate(c) for c in q.all()]


# ---------------------------------------------------------------------------
# Eligibility
# ---------------------------------------------------------------------------
@app.get("/eligibility/{dodid}/{course_id}", response_model=EligibilityCheck)
def check_trainee_eligibility(dodid: str, course_id: str, db: Session = Depends(get_db)):
    eligible, missing = check_eligibility(dodid, course_id, db)
    return EligibilityCheck(
        dodid=dodid,
        target_course=course_id,
        eligible=eligible,
        missing_prereqs=missing,
    )


# ---------------------------------------------------------------------------
# Unit rollup
# ---------------------------------------------------------------------------
@app.get("/rollup", response_model=list[UnitRollup])
def rollup_all(db: Session = Depends(get_db)):
    return get_unit_rollup(db)


@app.get("/rollup/{unit}", response_model=UnitRollup)
def rollup_unit(unit: str, db: Session = Depends(get_db)):
    results = get_unit_rollup(db, unit=unit)
    if not results:
        raise HTTPException(status_code=404, detail=f"No trainees found for unit: {unit}")
    return results[0]


# ---------------------------------------------------------------------------
# CSV upload — roster
# ---------------------------------------------------------------------------
@app.post("/upload/roster", response_model=UploadResult)
async def upload_roster(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """Upload a CSV roster. Expected columns: dodid, last_name, first_name, rank, unit, mos."""
    content = await file.read()
    text = content.decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(text))

    accepted, rejected = 0, 0
    errors: list[str] = []

    for i, row in enumerate(reader, start=2):  # row 1 is header
        try:
            dodid = row.get("dodid", "").strip()
            if not dodid or len(dodid) != 10 or not dodid.isdigit():
                raise ValueError(f"Invalid DODID: '{dodid}'")

            existing = db.query(Trainee).filter(Trainee.dodid == dodid).first()
            if existing:
                # Update fields
                existing.last_name = row.get("last_name", "").strip().upper()
                existing.first_name = row.get("first_name", "").strip().upper()
                existing.rank = row.get("rank", "").strip().upper()
                existing.unit = row.get("unit", "").strip().upper()
                existing.mos = row.get("mos", "").strip().upper() or None
            else:
                trainee = Trainee(
                    dodid=dodid,
                    last_name=row.get("last_name", "").strip().upper(),
                    first_name=row.get("first_name", "").strip().upper(),
                    rank=row.get("rank", "").strip().upper(),
                    unit=row.get("unit", "").strip().upper(),
                    mos=row.get("mos", "").strip().upper() or None,
                )
                db.add(trainee)
            accepted += 1
        except Exception as e:
            rejected += 1
            errors.append(f"Row {i}: {e}")

    db.commit()
    return UploadResult(accepted=accepted, rejected=rejected, errors=errors)


# ---------------------------------------------------------------------------
# CSV upload — completions
# ---------------------------------------------------------------------------
@app.post("/upload/completions", response_model=UploadResult)
async def upload_completions(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """Upload completions CSV. Columns: dodid, course_id, result, evaluation_date, evaluator_name."""
    content = await file.read()
    text = content.decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(text))

    accepted, rejected = 0, 0
    errors: list[str] = []

    for i, row in enumerate(reader, start=2):
        try:
            dodid = row.get("dodid", "").strip()
            course_id = row.get("course_id", "").strip().upper()
            result = row.get("result", "").strip().upper()
            eval_date_str = row.get("evaluation_date", "").strip()
            evaluator = row.get("evaluator_name", "").strip() or None

            if not dodid or not course_id or result not in ("GO", "NO_GO"):
                raise ValueError(f"Invalid data: dodid={dodid}, course={course_id}, result={result}")

            if course_id not in PREREQ_CHAIN:
                raise ValueError(f"Unknown course: {course_id}")

            # Verify trainee exists
            trainee = db.query(Trainee).filter(Trainee.dodid == dodid).first()
            if not trainee:
                raise ValueError(f"Trainee {dodid} not found")

            # Parse date
            eval_date = date.fromisoformat(eval_date_str)

            # Prereq check for GO results
            if result == "GO":
                eligible, missing = check_eligibility(dodid, course_id, db)
                if not eligible:
                    raise ValueError(f"Prereqs not met for {course_id}: missing {', '.join(missing)}")

            # Upsert
            existing = (
                db.query(Completion)
                .filter(Completion.dodid == dodid, Completion.course_id == course_id)
                .first()
            )
            if existing:
                existing.result = result
                existing.evaluation_date = eval_date
                existing.evaluator_name = evaluator
            else:
                db.add(Completion(
                    dodid=dodid,
                    course_id=course_id,
                    result=result,
                    evaluation_date=eval_date,
                    evaluator_name=evaluator,
                ))
            accepted += 1
        except Exception as e:
            rejected += 1
            errors.append(f"Row {i}: {e}")

    db.commit()
    return UploadResult(accepted=accepted, rejected=rejected, errors=errors)


# ---------------------------------------------------------------------------
# Export
# ---------------------------------------------------------------------------
@app.get("/export/csv")
def export_csv(
    unit: str | None = None,
    db: Session = Depends(get_db),
):
    """Export completions as a downloadable CSV."""
    q = db.query(Completion).join(Trainee)
    if unit:
        q = q.filter(Trainee.unit == unit)

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["dodid", "last_name", "first_name", "rank", "unit", "mos",
                      "course_id", "result", "evaluation_date", "evaluator_name"])

    for comp in q.all():
        t = comp.trainee
        writer.writerow([
            t.dodid, t.last_name, t.first_name, t.rank, t.unit, t.mos or "",
            comp.course_id, comp.result, comp.evaluation_date.isoformat(),
            comp.evaluator_name or "",
        ])

    output.seek(0)
    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=readiness_export.csv"},
    )
