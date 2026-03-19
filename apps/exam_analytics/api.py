"""Exam Analytics Dashboard — FastAPI application."""

from __future__ import annotations

import csv
import io
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, File, HTTPException, Query, UploadFile, status
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from .db import (
    EXAM_STRUCTURE,
    ExamResult,
    ExamSession,
    QuestionScore,
    cohort_summary,
    compute_gain_scores,
    get_db,
    init_db,
    question_difficulty,
)
from .models import (
    CohortSummary,
    ExamResultCreate,
    ExamResultResponse,
    ExamSessionCreate,
    ExamSessionResponse,
    GainScoreResponse,
    QuestionDifficulty,
    UploadResult,
)


# ---------------------------------------------------------------------------
# App
# ---------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Exam Analytics Dashboard",
    description="Analyze pre/post exam results, gain scores, and question difficulty.",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/health")
def health():
    return {"status": "ok"}


# ---------------------------------------------------------------------------
# Sessions
# ---------------------------------------------------------------------------
@app.post("/sessions", response_model=ExamSessionResponse, status_code=status.HTTP_201_CREATED)
def create_session(payload: ExamSessionCreate, db: Session = Depends(get_db)):
    session = ExamSession(**payload.model_dump())
    db.add(session)
    db.commit()
    db.refresh(session)
    return ExamSessionResponse.model_validate(session)


@app.get("/sessions", response_model=list[ExamSessionResponse])
def list_sessions(
    course_id: str | None = None,
    form_type: str | None = None,
    db: Session = Depends(get_db),
):
    q = db.query(ExamSession)
    if course_id:
        q = q.filter(ExamSession.course_id == course_id)
    if form_type:
        q = q.filter(ExamSession.form_type == form_type.upper())
    return [ExamSessionResponse.model_validate(s) for s in q.order_by(ExamSession.administration_date.desc()).all()]


@app.get("/sessions/{session_id}", response_model=ExamSessionResponse)
def get_session(session_id: int, db: Session = Depends(get_db)):
    session = db.query(ExamSession).filter(ExamSession.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return ExamSessionResponse.model_validate(session)


# ---------------------------------------------------------------------------
# Results
# ---------------------------------------------------------------------------
@app.post("/results/{session_id}", response_model=ExamResultResponse, status_code=status.HTTP_201_CREATED)
def record_result(session_id: int, payload: ExamResultCreate, db: Session = Depends(get_db)):
    session = db.query(ExamSession).filter(ExamSession.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    result = ExamResult(
        session_id=session_id,
        trainee_id=payload.trainee_id,
        total_score=payload.total_score,
        total_possible=payload.total_possible,
        score_percent=payload.score_percent,
        result=payload.result,
    )
    db.add(result)
    db.flush()

    for qs in payload.question_scores:
        db.add(QuestionScore(
            result_id=result.id,
            **qs.model_dump(),
        ))

    db.commit()
    db.refresh(result)
    return ExamResultResponse.model_validate(result)


@app.get("/results/{session_id}", response_model=list[ExamResultResponse])
def list_results(session_id: int, db: Session = Depends(get_db)):
    results = db.query(ExamResult).filter(ExamResult.session_id == session_id).all()
    return [ExamResultResponse.model_validate(r) for r in results]


# ---------------------------------------------------------------------------
# CSV upload — exam results
# ---------------------------------------------------------------------------
@app.post("/upload/results/{session_id}", response_model=UploadResult)
async def upload_results(
    session_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    """Upload exam results CSV.

    Expected columns: trainee_id, q1, q2, ..., q20
    q1–q15 = MC (0 or 2 pts), q16–q20 = SA (0–6 pts).
    """
    session = db.query(ExamSession).filter(ExamSession.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    content = await file.read()
    text = content.decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(text))

    mc_pts = EXAM_STRUCTURE["mc_points"]
    sa_pts = EXAM_STRUCTURE["sa_points"]
    total_possible = EXAM_STRUCTURE["total_possible"]
    passing_score = EXAM_STRUCTURE["passing_score"]

    accepted, rejected = 0, 0
    errors: list[str] = []

    for i, row in enumerate(reader, start=2):
        try:
            trainee_id = row.get("trainee_id", "").strip()
            if not trainee_id:
                raise ValueError("Missing trainee_id")

            total_score = 0
            question_scores: list[QuestionScore] = []

            for qnum in range(1, 21):
                col = f"q{qnum}"
                raw = row.get(col, "").strip()
                if raw == "":
                    raise ValueError(f"Missing {col}")
                pts = int(raw)

                if qnum <= 15:
                    q_type = "MC"
                    q_possible = mc_pts
                    if pts not in (0, mc_pts):
                        raise ValueError(f"{col}: MC score must be 0 or {mc_pts}, got {pts}")
                else:
                    q_type = "SA"
                    q_possible = sa_pts
                    if pts < 0 or pts > sa_pts:
                        raise ValueError(f"{col}: SA score must be 0–{sa_pts}, got {pts}")

                total_score += pts
                question_scores.append(QuestionScore(
                    question_number=qnum,
                    question_type=q_type,
                    points_possible=q_possible,
                    points_awarded=pts,
                ))

            score_pct = round(total_score / total_possible * 100, 1)

            # Determine result
            if session.form_type == "PRE":
                result_str = "DIAGNOSTIC"
            elif total_score >= passing_score:
                result_str = "PASS"
            else:
                result_str = "FAIL"

            exam_result = ExamResult(
                session_id=session_id,
                trainee_id=trainee_id,
                total_score=total_score,
                total_possible=total_possible,
                score_percent=score_pct,
                result=result_str,
            )
            db.add(exam_result)
            db.flush()

            for qs in question_scores:
                qs.result_id = exam_result.id
                db.add(qs)

            accepted += 1
        except Exception as e:
            rejected += 1
            errors.append(f"Row {i}: {e}")

    db.commit()
    return UploadResult(accepted=accepted, rejected=rejected, errors=errors)


# ---------------------------------------------------------------------------
# Analytics
# ---------------------------------------------------------------------------
@app.get("/sessions/{session_id}/summary", response_model=CohortSummary)
def session_summary(session_id: int, db: Session = Depends(get_db)):
    summary = cohort_summary(session_id, db)
    if summary is None:
        raise HTTPException(status_code=404, detail="Session not found")
    return summary


@app.get("/sessions/{session_id}/questions", response_model=list[QuestionDifficulty])
def session_questions(session_id: int, db: Session = Depends(get_db)):
    return question_difficulty(session_id, db)


@app.get("/gain-scores", response_model=list[GainScoreResponse])
def gain_scores(
    pre_session_id: int = Query(...),
    post_session_id: int = Query(...),
    low_gain_threshold: float = Query(5.0, description="Flag trainees with normalized gain below this"),
    db: Session = Depends(get_db),
):
    gains = compute_gain_scores(pre_session_id, post_session_id, db)
    return gains


@app.get("/gain-scores/flagged", response_model=list[GainScoreResponse])
def flagged_gain_scores(
    pre_session_id: int = Query(...),
    post_session_id: int = Query(...),
    threshold: float = Query(5.0),
    db: Session = Depends(get_db),
):
    """Return only trainees with normalized gain below threshold."""
    gains = compute_gain_scores(pre_session_id, post_session_id, db)
    return [g for g in gains if g["normalized_gain"] < threshold]


# ---------------------------------------------------------------------------
# Export
# ---------------------------------------------------------------------------
@app.get("/export/csv/{session_id}")
def export_session_csv(session_id: int, db: Session = Depends(get_db)):
    session = db.query(ExamSession).filter(ExamSession.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    output = io.StringIO()
    writer = csv.writer(output)

    header = ["trainee_id", "total_score", "total_possible", "score_percent", "result"]
    header += [f"q{i}" for i in range(1, 21)]
    writer.writerow(header)

    for r in session.results:
        q_scores = {qs.question_number: qs.points_awarded for qs in r.question_scores}
        row = [r.trainee_id, r.total_score, r.total_possible, r.score_percent, r.result]
        row += [q_scores.get(i, "") for i in range(1, 21)]
        writer.writerow(row)

    output.seek(0)
    filename = f"exam_{session.course_id}_{session.form_type}_{session.cohort_label}.csv"
    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )
