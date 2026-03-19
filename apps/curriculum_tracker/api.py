"""Curriculum Tracker — FastAPI application.

Provides REST endpoints for document tracking, review management,
and corpus freshness reporting.
"""

from __future__ import annotations

import csv
import io
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import Depends, FastAPI, HTTPException, Query, status
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from .db import (
    Document,
    ReviewCycle,
    ChangeLog,
    get_db,
    get_document_history,
    get_freshness_report,
    get_overdue_reviews,
    get_review_summary,
    get_stale_documents,
    init_db,
    scan_directory,
)
from .models import (
    ChangeLogResponse,
    DocumentResponse,
    FreshnessReport,
    ReviewCycleCreate,
    ReviewCycleResponse,
    ReviewSummary,
    ScanResult,
)

# Default scan target — maven_training/ relative to repo root
_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
MAVEN_TRAINING_PATH = str(_REPO_ROOT / "maven_training")


# ---------------------------------------------------------------------------
# App lifecycle
# ---------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Curriculum Tracker",
    description="Track curriculum document versions, review cycles, and content freshness.",
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
# Scan
# ---------------------------------------------------------------------------
@app.post("/scan", response_model=ScanResult)
def trigger_scan(db: Session = Depends(get_db)):
    """Scan maven_training/ directory, hash .md files, upsert documents."""
    counts = scan_directory(MAVEN_TRAINING_PATH, db)
    return ScanResult(**counts)


# ---------------------------------------------------------------------------
# Documents
# ---------------------------------------------------------------------------
@app.get("/documents", response_model=list[DocumentResponse])
def list_documents(
    doc_type: str | None = None,
    course_id: str | None = None,
    limit: int = Query(200, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    q = db.query(Document)
    if doc_type:
        q = q.filter(Document.doc_type == doc_type.upper())
    if course_id:
        q = q.filter(Document.course_id == course_id.upper())
    docs = q.order_by(Document.file_path).offset(offset).limit(limit).all()
    return [DocumentResponse.model_validate(d) for d in docs]


@app.get("/documents/stale", response_model=list[DocumentResponse])
def stale_documents(
    days: int = Query(90, ge=1),
    db: Session = Depends(get_db),
):
    """Return documents not reviewed in the last N days."""
    docs = get_stale_documents(days, db)
    return [DocumentResponse.model_validate(d) for d in docs]


@app.get("/documents/{doc_id}", response_model=DocumentResponse)
def get_document(doc_id: int, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.doc_id == doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail=f"Document {doc_id} not found")
    return DocumentResponse.model_validate(doc)


# ---------------------------------------------------------------------------
# Reviews
# ---------------------------------------------------------------------------
@app.post("/reviews", response_model=ReviewCycleResponse, status_code=status.HTTP_201_CREATED)
def create_review(payload: ReviewCycleCreate, db: Session = Depends(get_db)):
    # Verify document exists
    doc = db.query(Document).filter(Document.doc_id == payload.doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail=f"Document {payload.doc_id} not found")

    # Check for duplicate review (same doc, same date, same reviewer)
    existing = (
        db.query(ReviewCycle)
        .filter(
            ReviewCycle.doc_id == payload.doc_id,
            ReviewCycle.review_date == payload.review_date,
            ReviewCycle.reviewer_name == payload.reviewer_name,
        )
        .first()
    )
    if existing:
        raise HTTPException(
            status_code=409,
            detail=f"Review already exists for doc {payload.doc_id} "
                   f"by {payload.reviewer_name} on {payload.review_date}",
        )

    review = ReviewCycle(**payload.model_dump())
    db.add(review)
    db.commit()
    db.refresh(review)
    return ReviewCycleResponse.model_validate(review)


@app.get("/reviews", response_model=list[ReviewCycleResponse])
def list_reviews(
    doc_id: int | None = None,
    status_filter: str | None = Query(None, alias="status"),
    db: Session = Depends(get_db),
):
    q = db.query(ReviewCycle)
    if doc_id:
        q = q.filter(ReviewCycle.doc_id == doc_id)
    if status_filter:
        q = q.filter(ReviewCycle.status == status_filter.upper())
    return [ReviewCycleResponse.model_validate(r) for r in q.order_by(ReviewCycle.review_date.desc()).all()]


@app.get("/reviews/overdue", response_model=list[ReviewCycleResponse])
def overdue_reviews(db: Session = Depends(get_db)):
    reviews = get_overdue_reviews(db)
    return [ReviewCycleResponse.model_validate(r) for r in reviews]


# ---------------------------------------------------------------------------
# Document history
# ---------------------------------------------------------------------------
@app.get("/documents/{doc_id}/history", response_model=list[ChangeLogResponse])
def document_history(doc_id: int, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.doc_id == doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail=f"Document {doc_id} not found")
    entries = get_document_history(doc_id, db)
    return [ChangeLogResponse.model_validate(e) for e in entries]


# ---------------------------------------------------------------------------
# Reports
# ---------------------------------------------------------------------------
@app.get("/freshness", response_model=list[FreshnessReport])
def freshness_report(db: Session = Depends(get_db)):
    return [FreshnessReport(**r) for r in get_freshness_report(db)]


@app.get("/summary", response_model=ReviewSummary)
def review_summary(db: Session = Depends(get_db)):
    counts = get_review_summary(db)
    return ReviewSummary(
        approved=counts.get("APPROVED", 0),
        changes_required=counts.get("CHANGES_REQUIRED", 0),
        in_review=counts.get("IN_REVIEW", 0),
        overdue=counts.get("OVERDUE", 0),
    )


# ---------------------------------------------------------------------------
# Export
# ---------------------------------------------------------------------------
@app.get("/export/csv")
def export_csv(
    doc_type: str | None = None,
    db: Session = Depends(get_db),
):
    """Export documents and their latest review status as CSV."""
    q = db.query(Document)
    if doc_type:
        q = q.filter(Document.doc_type == doc_type.upper())

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow([
        "doc_id", "file_path", "doc_type", "course_id", "title",
        "current_version", "last_modified", "file_hash",
        "latest_review_date", "latest_review_status", "reviewer",
    ])

    for doc in q.order_by(Document.file_path).all():
        # Get latest review
        latest_review = (
            db.query(ReviewCycle)
            .filter(ReviewCycle.doc_id == doc.doc_id)
            .order_by(ReviewCycle.review_date.desc())
            .first()
        )
        writer.writerow([
            doc.doc_id,
            doc.file_path,
            doc.doc_type,
            doc.course_id or "",
            doc.title,
            doc.current_version,
            doc.last_modified.isoformat() if doc.last_modified else "",
            doc.file_hash or "",
            latest_review.review_date.isoformat() if latest_review else "",
            latest_review.status if latest_review else "",
            latest_review.reviewer_name if latest_review else "",
        ])

    output.seek(0)
    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=curriculum_export.csv"},
    )
