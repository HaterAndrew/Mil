"""AAR Aggregator — FastAPI application."""

from __future__ import annotations

from contextlib import asynccontextmanager
from datetime import date

from fastapi import Depends, FastAPI, File, HTTPException, Query, UploadFile, status
from sqlalchemy.orm import Session

from .db import (
    AAR,
    CurriculumDiscrepancy,
    EnvironmentIssue,
    ImproveItem,
    StudentEvaluation,
    SustainItem,
    find_recurring_issues,
    get_db,
    init_db,
    parse_aar_file,
    trend_by_category,
    trend_over_time,
)
from .models import (
    AARCreate,
    AARDetail,
    AARSummary,
    DiscrepancyOut,
    ImproveItemOut,
    MonthlyTrend,
    ParsedAARPreview,
    RecurringIssue,
    TrendByCategory,
)


# ---------------------------------------------------------------------------
# App
# ---------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="AAR Aggregator",
    description="Ingest AARs, aggregate trends, and flag recurring issues.",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/health")
def health():
    return {"status": "ok"}


# ---------------------------------------------------------------------------
# AAR CRUD
# ---------------------------------------------------------------------------
@app.post("/aars", response_model=AARSummary, status_code=status.HTTP_201_CREATED)
def create_aar(payload: AARCreate, db: Session = Depends(get_db)):
    aar = AAR(
        date=payload.date,
        tm_levels=payload.tm_levels,
        exercises=payload.exercises,
        location=payload.location,
        student_count=payload.student_count,
        instructor_names=payload.instructor_names,
        planned_objectives=payload.planned_objectives,
        actual_execution=payload.actual_execution,
        instructor_recommendations=payload.instructor_recommendations,
        submitted_by=payload.submitted_by,
    )
    db.add(aar)
    db.flush()

    # Sustain items
    for text in payload.sustains:
        db.add(SustainItem(aar_id=aar.id, item_text=text))

    # Improve items
    for item in payload.improves:
        db.add(ImproveItem(aar_id=aar.id, **item.model_dump()))

    # Student evaluations
    for ev in payload.evaluations:
        db.add(StudentEvaluation(aar_id=aar.id, **ev.model_dump()))

    # Curriculum discrepancies
    for disc in payload.discrepancies:
        db.add(CurriculumDiscrepancy(aar_id=aar.id, **disc.model_dump()))

    # Environment issues
    for env in payload.env_issues:
        db.add(EnvironmentIssue(aar_id=aar.id, **env.model_dump()))

    db.commit()
    db.refresh(aar)

    return AARSummary(
        id=aar.id,
        date=aar.date,
        tm_levels=aar.tm_levels,
        location=aar.location,
        student_count=aar.student_count,
        submitted_by=aar.submitted_by,
        sustain_count=len(aar.sustains),
        improve_count=len(aar.improves),
    )


@app.get("/aars", response_model=list[AARSummary])
def list_aars(
    date_from: date | None = None,
    date_to: date | None = None,
    tm_level: str | None = None,
    db: Session = Depends(get_db),
):
    q = db.query(AAR)
    if date_from:
        q = q.filter(AAR.date >= date_from)
    if date_to:
        q = q.filter(AAR.date <= date_to)
    aars = q.order_by(AAR.date.desc()).all()

    results = []
    for aar in aars:
        if tm_level and tm_level not in (aar.tm_levels or []):
            continue
        results.append(AARSummary(
            id=aar.id,
            date=aar.date,
            tm_levels=aar.tm_levels,
            location=aar.location,
            student_count=aar.student_count,
            submitted_by=aar.submitted_by,
            sustain_count=len(aar.sustains),
            improve_count=len(aar.improves),
        ))
    return results


@app.get("/aars/{aar_id}", response_model=AARDetail)
def get_aar(aar_id: int, db: Session = Depends(get_db)):
    aar = db.query(AAR).filter(AAR.id == aar_id).first()
    if not aar:
        raise HTTPException(status_code=404, detail="AAR not found")

    return AARDetail(
        id=aar.id,
        date=aar.date,
        tm_levels=aar.tm_levels or [],
        exercises=aar.exercises or [],
        location=aar.location,
        student_count=aar.student_count,
        instructor_names=aar.instructor_names or [],
        planned_objectives=aar.planned_objectives,
        actual_execution=aar.actual_execution,
        instructor_recommendations=aar.instructor_recommendations,
        submitted_by=aar.submitted_by,
        sustains=[s.item_text for s in aar.sustains],
        improves=[ImproveItemOut.model_validate(i) for i in aar.improves],
        evaluations=aar.evaluations,
        discrepancies=aar.discrepancies,
        env_issues=aar.env_issues,
    )


@app.delete("/aars/{aar_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_aar(aar_id: int, db: Session = Depends(get_db)):
    aar = db.query(AAR).filter(AAR.id == aar_id).first()
    if not aar:
        raise HTTPException(status_code=404, detail="AAR not found")
    db.delete(aar)
    db.commit()


# ---------------------------------------------------------------------------
# File upload + parse
# ---------------------------------------------------------------------------
@app.post("/upload/parse", response_model=ParsedAARPreview)
async def upload_parse(file: UploadFile = File(...)):
    """Parse an uploaded AAR file and return preview for review."""
    # AAR files are typically <100 KB; reject anything over 5 MB
    content = await file.read()
    if len(content) > 5 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File too large (5 MB max)")
    text = content.decode("utf-8-sig")
    parsed = parse_aar_file(text)

    warnings = []
    if parsed.get("student_count", 0) <= 1:
        warnings.append("Student count defaulted to 1 — verify in original document")
    if parsed.get("location") == "Unknown":
        warnings.append("Could not extract location from file")
    if not parsed.get("improves"):
        warnings.append("No improve items found — check Section 5 formatting")

    return ParsedAARPreview(parsed=parsed, warnings=warnings)


@app.post("/upload/confirm", response_model=AARSummary, status_code=status.HTTP_201_CREATED)
def upload_confirm(payload: AARCreate, db: Session = Depends(get_db)):
    """Save a previously parsed (and possibly edited) AAR."""
    return create_aar(payload, db)


# ---------------------------------------------------------------------------
# Trends
# ---------------------------------------------------------------------------
@app.get("/trends/category", response_model=list[TrendByCategory])
def trends_category(
    date_from: date | None = None,
    date_to: date | None = None,
    db: Session = Depends(get_db),
):
    cats = trend_by_category(db, date_from, date_to)
    return [TrendByCategory(category=k, count=v) for k, v in sorted(cats.items(), key=lambda x: -x[1])]


@app.get("/trends/recurring", response_model=list[RecurringIssue])
def trends_recurring(
    min_count: int = Query(2, ge=2),
    date_from: date | None = None,
    date_to: date | None = None,
    db: Session = Depends(get_db),
):
    return find_recurring_issues(db, min_count, date_from, date_to)


@app.get("/trends/over-time", response_model=list[MonthlyTrend])
def trends_over_time(
    date_from: date | None = None,
    date_to: date | None = None,
    db: Session = Depends(get_db),
):
    return trend_over_time(db, date_from, date_to)


# ---------------------------------------------------------------------------
# Discrepancies
# ---------------------------------------------------------------------------
@app.get("/discrepancies", response_model=list[DiscrepancyOut])
def list_discrepancies(
    severity: str | None = None,
    db: Session = Depends(get_db),
):
    q = db.query(CurriculumDiscrepancy)
    if severity:
        q = q.filter(CurriculumDiscrepancy.severity == severity.upper())
    return [DiscrepancyOut.model_validate(d) for d in q.all()]
