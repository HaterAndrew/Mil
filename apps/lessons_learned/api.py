"""Lessons Learned Pipeline — FastAPI application."""

from __future__ import annotations

import csv
import io
from contextlib import asynccontextmanager
from datetime import UTC, datetime

from fastapi import Depends, FastAPI, HTTPException, Query, status
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from shared.middleware import SecurityHeadersMiddleware

from .db import (
    ActionItem,
    Lesson,
    LessonComment,
    LessonTag,
    SessionLocal,
    get_action_item_status,
    get_cross_reference,
    get_db,
    get_lessons_by_tag,
    get_pipeline_stats,
    get_tag_frequency,
    get_trend_analysis,
    init_db,
)
from .models import (
    ActionItemCreate,
    ActionItemResponse,
    CommentCreate,
    CommentOut,
    CrossReference,
    LessonCreate,
    LessonResponse,
    LessonTagCreate,
    LessonTagOut,
    PipelineStats,
    TagFrequency,
)


# ---------------------------------------------------------------------------
# App lifecycle
# ---------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Lessons Learned Pipeline",
    description="Structured lessons-learned pipeline with full tagging taxonomy (TM-40K).",
    version="1.0.0",
    lifespan=lifespan,
)
app.add_middleware(SecurityHeadersMiddleware)


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------
@app.get("/health")
def health():
    return {"status": "ok"}


# ---------------------------------------------------------------------------
# Lessons
# ---------------------------------------------------------------------------
@app.post("/lessons", response_model=LessonResponse, status_code=status.HTTP_201_CREATED)
def create_lesson(payload: LessonCreate, db: Session = Depends(get_db)):
    lesson = Lesson(**payload.model_dump())
    db.add(lesson)
    db.commit()
    db.refresh(lesson)
    return LessonResponse.model_validate(lesson)


@app.get("/lessons", response_model=list[LessonResponse])
def list_lessons(
    status_filter: str | None = Query(None, alias="status"),
    priority: str | None = None,
    source_type: str | None = None,
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    q = db.query(Lesson)
    if status_filter:
        q = q.filter(Lesson.status == status_filter.upper())
    if priority:
        q = q.filter(Lesson.priority == priority.upper())
    if source_type:
        q = q.filter(Lesson.source_type == source_type.upper())
    lessons = q.order_by(Lesson.submit_date.desc()).offset(offset).limit(limit).all()
    return [LessonResponse.model_validate(l) for l in lessons]


@app.get("/lessons/{lesson_id}", response_model=LessonResponse)
def get_lesson(lesson_id: int, db: Session = Depends(get_db)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail=f"Lesson {lesson_id} not found")
    return LessonResponse.model_validate(lesson)


# ---------------------------------------------------------------------------
# Tags
# ---------------------------------------------------------------------------
@app.post("/lessons/{lesson_id}/tags", response_model=LessonTagOut, status_code=status.HTTP_201_CREATED)
def add_tag(lesson_id: int, payload: LessonTagCreate, db: Session = Depends(get_db)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail=f"Lesson {lesson_id} not found")

    # Check for duplicate
    existing = (
        db.query(LessonTag)
        .filter(
            LessonTag.lesson_id == lesson_id,
            LessonTag.tag_type == payload.tag_type,
            LessonTag.tag_value == payload.tag_value,
        )
        .first()
    )
    if existing:
        raise HTTPException(status_code=409, detail="Tag already exists on this lesson")

    tag = LessonTag(lesson_id=lesson_id, **payload.model_dump())
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return LessonTagOut.model_validate(tag)


@app.get("/lessons/{lesson_id}/tags", response_model=list[LessonTagOut])
def list_tags(lesson_id: int, db: Session = Depends(get_db)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail=f"Lesson {lesson_id} not found")
    return [LessonTagOut.model_validate(t) for t in lesson.tags]


# ---------------------------------------------------------------------------
# Action Items
# ---------------------------------------------------------------------------
@app.post("/lessons/{lesson_id}/actions", response_model=ActionItemResponse, status_code=status.HTTP_201_CREATED)
def add_action(lesson_id: int, payload: ActionItemCreate, db: Session = Depends(get_db)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail=f"Lesson {lesson_id} not found")

    action = ActionItem(lesson_id=lesson_id, **payload.model_dump())
    db.add(action)
    db.commit()
    db.refresh(action)
    return ActionItemResponse.model_validate(action)


@app.get("/lessons/{lesson_id}/actions", response_model=list[ActionItemResponse])
def list_actions(lesson_id: int, db: Session = Depends(get_db)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail=f"Lesson {lesson_id} not found")
    return [ActionItemResponse.model_validate(a) for a in lesson.action_items]


# ---------------------------------------------------------------------------
# Comments
# ---------------------------------------------------------------------------
@app.post("/lessons/{lesson_id}/comments", response_model=CommentOut, status_code=status.HTTP_201_CREATED)
def add_comment(lesson_id: int, payload: CommentCreate, db: Session = Depends(get_db)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail=f"Lesson {lesson_id} not found")

    comment = LessonComment(
        lesson_id=lesson_id,
        author=payload.author,
        comment_text=payload.comment_text,
        comment_date=datetime.now(UTC),
    )
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return CommentOut.model_validate(comment)


# ---------------------------------------------------------------------------
# Tag analytics
# ---------------------------------------------------------------------------
@app.get("/tags/frequency", response_model=list[TagFrequency])
def tag_frequency(tag_type: str = Query(...), db: Session = Depends(get_db)):
    results = get_tag_frequency(tag_type.upper(), db)
    return [TagFrequency(**r) for r in results]


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------
@app.get("/analysis/trend")
def trend_analysis(db: Session = Depends(get_db)):
    return get_trend_analysis(db)


@app.get("/analysis/cross-reference", response_model=list[CrossReference])
def cross_reference(
    type_a: str = Query(...),
    type_b: str = Query(...),
    db: Session = Depends(get_db),
):
    results = get_cross_reference(type_a.upper(), type_b.upper(), db)
    return [CrossReference(**r) for r in results]


# ---------------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------------
@app.get("/stats", response_model=PipelineStats)
def pipeline_stats(db: Session = Depends(get_db)):
    return PipelineStats(**get_pipeline_stats(db))


# ---------------------------------------------------------------------------
# Export
# ---------------------------------------------------------------------------
@app.get("/export/csv")
def export_csv(db: Session = Depends(get_db)):
    """Export all lessons with tags as a downloadable CSV."""
    lessons = db.query(Lesson).order_by(Lesson.submit_date.desc()).all()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow([
        "id", "title", "description", "source_type", "source_reference",
        "submitted_by", "submit_date", "status", "priority",
        "tags",
    ])

    for lesson in lessons:
        # Flatten tags into a semicolon-separated string
        tag_str = "; ".join(f"{t.tag_type}:{t.tag_value}" for t in lesson.tags)
        writer.writerow([
            lesson.id, lesson.title, lesson.description, lesson.source_type,
            lesson.source_reference or "", lesson.submitted_by,
            lesson.submit_date.isoformat(), lesson.status, lesson.priority,
            tag_str,
        ])

    output.seek(0)
    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=lessons_learned_export.csv"},
    )
