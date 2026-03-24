"""Instructor Certification Manager — FastAPI application."""

from __future__ import annotations

import csv
import io
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, Query, status
from fastapi.responses import StreamingResponse
from shared.auth import verify_api_key
from shared.factory import create_app
from sqlalchemy.orm import Session

from .db import (
    COURSE_CATALOG,
    Certification,
    Instructor,
    TeachingHistory,
    get_coverage_matrix,
    get_db,
    get_expiring_certifications,
    init_db,
)
from .models import (
    CertificationCreate,
    CertificationResponse,
    CoverageReport,
    ExpirationAlert,
    InstructorCreate,
    InstructorResponse,
    TeachingHistoryCreate,
    TeachingHistoryResponse,
)


# ---------------------------------------------------------------------------
# App lifecycle
# ---------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = create_app(title="Instructor Certification Manager", version="1.0.0", lifespan=lifespan)


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------
@app.get("/health")
def health():
    return {"status": "ok"}


# ---------------------------------------------------------------------------
# Instructors
# ---------------------------------------------------------------------------
@app.post(
    "/instructors", response_model=InstructorResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(verify_api_key)],
)
def create_instructor(payload: InstructorCreate, db: Session = Depends(get_db)):
    existing = db.query(Instructor).filter(Instructor.instructor_id == payload.instructor_id).first()
    if existing:
        raise HTTPException(status_code=409, detail=f"Instructor {payload.instructor_id} already exists")
    instructor = Instructor(**payload.model_dump())
    db.add(instructor)
    db.commit()
    db.refresh(instructor)
    return InstructorResponse.model_validate(instructor)


@app.get("/instructors", response_model=list[InstructorResponse], dependencies=[Depends(verify_api_key)])
def list_instructors(
    unit: str | None = None,
    status_filter: str | None = Query(None, alias="status"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    q = db.query(Instructor)
    if unit:
        q = q.filter(Instructor.unit == unit)
    if status_filter:
        q = q.filter(Instructor.status == status_filter.upper())
    instructors = q.order_by(Instructor.last_name).offset(offset).limit(limit).all()
    return [InstructorResponse.model_validate(i) for i in instructors]


@app.get("/instructors/{instructor_id}", response_model=InstructorResponse, dependencies=[Depends(verify_api_key)])
def get_instructor(instructor_id: str, db: Session = Depends(get_db)):
    instructor = db.query(Instructor).filter(Instructor.instructor_id == instructor_id).first()
    if not instructor:
        raise HTTPException(status_code=404, detail=f"Instructor {instructor_id} not found")
    return InstructorResponse.model_validate(instructor)


# ---------------------------------------------------------------------------
# Certifications
# ---------------------------------------------------------------------------
@app.post(
    "/certifications", response_model=CertificationResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(verify_api_key)],
)
def create_certification(payload: CertificationCreate, db: Session = Depends(get_db)):
    # Verify instructor exists
    instructor = db.query(Instructor).filter(Instructor.instructor_id == payload.instructor_id).first()
    if not instructor:
        raise HTTPException(status_code=404, detail=f"Instructor {payload.instructor_id} not found")

    # Verify course is valid
    if payload.course_id not in COURSE_CATALOG:
        raise HTTPException(status_code=422, detail=f"Unknown course: {payload.course_id}")

    cert = Certification(**payload.model_dump())
    db.add(cert)
    db.commit()
    db.refresh(cert)
    return CertificationResponse.model_validate(cert)


@app.get("/certifications", response_model=list[CertificationResponse], dependencies=[Depends(verify_api_key)])
def list_certifications(
    instructor_id: str | None = None,
    course_id: str | None = None,
    db: Session = Depends(get_db),
):
    q = db.query(Certification)
    if instructor_id:
        q = q.filter(Certification.instructor_id == instructor_id)
    if course_id:
        q = q.filter(Certification.course_id == course_id)
    return [CertificationResponse.model_validate(c) for c in q.all()]


@app.get("/certifications/expiring", response_model=list[ExpirationAlert], dependencies=[Depends(verify_api_key)])
def expiring_certifications(
    days: int = Query(30, ge=1, le=365),
    db: Session = Depends(get_db),
):
    """Return certifications expiring within the specified number of days."""
    return get_expiring_certifications(days, db)


# ---------------------------------------------------------------------------
# Teaching History
# ---------------------------------------------------------------------------
@app.post(
    "/teaching-history", response_model=TeachingHistoryResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(verify_api_key)],
)
def record_teaching(payload: TeachingHistoryCreate, db: Session = Depends(get_db)):
    # Verify instructor exists
    instructor = db.query(Instructor).filter(Instructor.instructor_id == payload.instructor_id).first()
    if not instructor:
        raise HTTPException(status_code=404, detail=f"Instructor {payload.instructor_id} not found")

    record = TeachingHistory(**payload.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    return TeachingHistoryResponse.model_validate(record)


# ---------------------------------------------------------------------------
# Coverage matrix
# ---------------------------------------------------------------------------
@app.get("/coverage", response_model=list[CoverageReport])
def coverage_matrix(db: Session = Depends(get_db)):
    """Course coverage matrix — how many CURRENT certified instructors per course."""
    return get_coverage_matrix(db)


# ---------------------------------------------------------------------------
# Export
# ---------------------------------------------------------------------------
@app.get("/export/csv", dependencies=[Depends(verify_api_key)])
def export_csv(db: Session = Depends(get_db)):
    """Export all instructor certifications as a downloadable CSV."""
    certs = (
        db.query(Certification)
        .join(Instructor)
        .order_by(Instructor.last_name, Certification.course_id)
        .all()
    )

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow([
        "instructor_id", "rank", "last_name", "first_name", "unit", "mos",
        "course_id", "certified_date", "expiration_date", "status", "certifying_authority",
    ])

    for cert in certs:
        inst = cert.instructor
        writer.writerow([
            inst.instructor_id, inst.rank, inst.last_name, inst.first_name,
            inst.unit, inst.mos,
            cert.course_id, cert.certified_date.isoformat(),
            cert.expiration_date.isoformat(), cert.status,
            cert.certifying_authority or "",
        ])

    output.seek(0)
    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=instructor_certifications.csv"},
    )
