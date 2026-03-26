"""Enrollment Manager — FastAPI application."""

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
    Enrollment,
    TrainingClass,
    WaitlistEntry,
    enroll_student,
    get_class_availability,
    get_class_roster,
    get_db,
    get_enrollment_stats,
    get_student_enrollments,
    init_db,
    promote_waitlist,
)
from .models import (
    BatchStatusUpdate,
    ClassAvailability,
    CourseDistribution,
    EnrollmentCreate,
    EnrollmentResponse,
    EnrollmentStats,
    TrainingClassCreate,
    TrainingClassResponse,
    WaitlistResponse,
)


# ---------------------------------------------------------------------------
# App lifecycle
# ---------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = create_app(
    title="Enrollment Manager",
    description="Manage class enrollment, seat allocation, and waitlists for MSS Training.",
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
# Training Classes
# ---------------------------------------------------------------------------
@app.post("/classes", response_model=TrainingClassResponse, status_code=status.HTTP_201_CREATED,
           dependencies=[Depends(verify_api_key)])
def create_class(payload: TrainingClassCreate, db: Session = Depends(get_db)):
    tc = TrainingClass(**payload.model_dump())
    db.add(tc)
    db.commit()
    db.refresh(tc)
    return TrainingClassResponse.model_validate(tc)


@app.get("/classes", response_model=list[TrainingClassResponse])
def list_classes(
    status_filter: str | None = Query(None, alias="status"),
    course_id: str | None = None,
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    q = db.query(TrainingClass)
    if status_filter:
        q = q.filter(TrainingClass.status == status_filter.upper())
    if course_id:
        q = q.filter(TrainingClass.course_id == course_id)
    classes = q.order_by(TrainingClass.start_date).offset(offset).limit(limit).all()
    return [TrainingClassResponse.model_validate(tc) for tc in classes]


@app.get("/classes/{class_id}", response_model=TrainingClassResponse)
def get_class(class_id: int, db: Session = Depends(get_db)):
    tc = db.query(TrainingClass).filter(TrainingClass.class_id == class_id).first()
    if not tc:
        raise HTTPException(status_code=404, detail=f"Class {class_id} not found")
    return TrainingClassResponse.model_validate(tc)


# ---------------------------------------------------------------------------
# Enrollment
# ---------------------------------------------------------------------------
@app.post("/classes/{class_id}/enroll", response_model=dict, dependencies=[Depends(verify_api_key)])
def enroll(class_id: int, payload: EnrollmentCreate, db: Session = Depends(get_db)):
    """Enroll a student. Auto-waitlists if class is full."""
    try:
        result = enroll_student(
            class_id=class_id,
            dodid=payload.dodid,
            last_name=payload.last_name,
            first_name=payload.first_name,
            rank=payload.rank,
            unit=payload.unit,
            db=db,
        )
        return {"status": result["status"], "message": f"Student {payload.dodid} {result['status']}"}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))


@app.get("/classes/{class_id}/roster", response_model=list[EnrollmentResponse], dependencies=[Depends(verify_api_key)])
def class_roster(class_id: int, db: Session = Depends(get_db)):
    roster = get_class_roster(class_id, db)
    return [EnrollmentResponse.model_validate(e) for e in roster]


# ---------------------------------------------------------------------------
# Availability
# ---------------------------------------------------------------------------
@app.get("/classes/{class_id}/availability", response_model=ClassAvailability)
def class_availability(class_id: int, db: Session = Depends(get_db)):
    avail = get_class_availability(class_id, db)
    if avail["max_seats"] == 0:
        raise HTTPException(status_code=404, detail=f"Class {class_id} not found")
    return ClassAvailability(**avail)


# ---------------------------------------------------------------------------
# Waitlist
# ---------------------------------------------------------------------------
@app.post("/classes/{class_id}/promote-waitlist", dependencies=[Depends(verify_api_key)])
def promote(class_id: int, db: Session = Depends(get_db)):
    """Promote top waitlisted students to enrolled when seats are available."""
    promoted = promote_waitlist(class_id, db)
    return {"promoted_count": len(promoted), "promoted": promoted}


@app.get("/classes/{class_id}/waitlist", response_model=list[WaitlistResponse], dependencies=[Depends(verify_api_key)])
def class_waitlist(class_id: int, db: Session = Depends(get_db)):
    entries = (
        db.query(WaitlistEntry)
        .filter(WaitlistEntry.class_id == class_id, WaitlistEntry.status == "WAITING")
        .order_by(WaitlistEntry.priority.desc(), WaitlistEntry.request_date.asc())
        .all()
    )
    return [WaitlistResponse.model_validate(e) for e in entries]


# ---------------------------------------------------------------------------
# Student lookup
# ---------------------------------------------------------------------------
@app.get("/students/{dodid}/enrollments", dependencies=[Depends(verify_api_key)])
def student_enrollments(dodid: str, db: Session = Depends(get_db)):
    return get_student_enrollments(dodid, db)


# ---------------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------------
@app.get("/stats", response_model=EnrollmentStats)
def stats(db: Session = Depends(get_db)):
    return EnrollmentStats(**get_enrollment_stats(db))


# ---------------------------------------------------------------------------
# Batch status update
# ---------------------------------------------------------------------------
@app.patch("/classes/{class_id}/batch-status", dependencies=[Depends(verify_api_key)])
def batch_status_update(class_id: int, payload: BatchStatusUpdate, db: Session = Depends(get_db)):
    """Update enrollment status for multiple students at once (drop, complete, no-show)."""
    tc = db.query(TrainingClass).filter(TrainingClass.class_id == class_id).first()
    if not tc:
        raise HTTPException(status_code=404, detail=f"Class {class_id} not found")

    updated = []
    not_found = []
    for dodid in payload.dodids:
        enrollment = (
            db.query(Enrollment)
            .filter(Enrollment.class_id == class_id, Enrollment.dodid == dodid)
            .first()
        )
        if enrollment:
            enrollment.status = payload.new_status
            updated.append(dodid)
        else:
            not_found.append(dodid)

    db.commit()
    return {
        "updated_count": len(updated),
        "updated": updated,
        "not_found": not_found,
    }


# ---------------------------------------------------------------------------
# Course distribution analytics
# ---------------------------------------------------------------------------
@app.get("/analytics/course-distribution", response_model=list[CourseDistribution])
def course_distribution(db: Session = Depends(get_db)):
    """Enrollment distribution grouped by course_id."""
    courses = db.query(TrainingClass.course_id).distinct().all()
    results = []
    for (course_id,) in courses:
        classes = db.query(TrainingClass).filter(TrainingClass.course_id == course_id).all()
        total_enrolled = 0
        total_waitlisted = 0
        fill_rates = []
        locations = set()
        for tc in classes:
            enrolled = (
                db.query(Enrollment)
                .filter(Enrollment.class_id == tc.class_id, Enrollment.status == "ENROLLED")
                .count()
            )
            waitlisted = (
                db.query(WaitlistEntry)
                .filter(WaitlistEntry.class_id == tc.class_id, WaitlistEntry.status == "WAITING")
                .count()
            )
            total_enrolled += enrolled
            total_waitlisted += waitlisted
            if tc.max_seats > 0:
                fill_rates.append(enrolled / tc.max_seats * 100)
            locations.add(tc.location)

        avg_fill = round(sum(fill_rates) / len(fill_rates), 1) if fill_rates else 0.0
        results.append(CourseDistribution(
            course_id=course_id,
            total_classes=len(classes),
            total_enrolled=total_enrolled,
            total_waitlisted=total_waitlisted,
            avg_fill_rate=avg_fill,
            locations=sorted(locations),
        ))

    return sorted(results, key=lambda r: r.course_id)


# ---------------------------------------------------------------------------
# Export
# ---------------------------------------------------------------------------
@app.get("/export/csv", dependencies=[Depends(verify_api_key)])
def export_csv(db: Session = Depends(get_db)):
    """Export all enrollments as a downloadable CSV."""
    enrollments = (
        db.query(Enrollment)
        .join(TrainingClass)
        .order_by(TrainingClass.start_date, Enrollment.seat_number)
        .all()
    )

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow([
        "class_id", "course_id", "class_name", "start_date", "location",
        "dodid", "last_name", "first_name", "rank", "unit",
        "enrollment_status", "seat_number", "enrollment_date",
    ])

    for e in enrollments:
        tc = e.training_class
        writer.writerow([
            tc.class_id, tc.course_id, tc.class_name,
            tc.start_date.isoformat(), tc.location,
            e.dodid, e.last_name, e.first_name, e.rank, e.unit,
            e.status, e.seat_number or "", e.enrollment_date.isoformat(),
        ])

    output.seek(0)
    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=enrollment_export.csv"},
    )
