"""MTT Scheduler — FastAPI application."""

from __future__ import annotations

from contextlib import asynccontextmanager
from datetime import date

from fastapi import Depends, FastAPI, HTTPException, Query, status
from sqlalchemy.orm import Session

from .db import (
    Enrollment,
    Event,
    Instructor,
    Venue,
    check_instructor_conflicts,
    event_instructors,
    get_calendar_data,
    get_capacity_utilization,
    get_db,
    get_location_summary,
    init_db,
)
from .models import (
    EnrollmentCreate,
    EnrollmentResponse,
    EventCreate,
    EventResponse,
    InstructorCreate,
    InstructorResponse,
    ScheduleConflict,
    VenueCreate,
    VenueResponse,
)


# ---------------------------------------------------------------------------
# App lifecycle
# ---------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="MTT Scheduler",
    description="Mobile Training Team scheduling for USAREUR-AF theater-wide MSS training events.",
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
# Events CRUD
# ---------------------------------------------------------------------------
@app.post("/events", response_model=EventResponse, status_code=status.HTTP_201_CREATED)
def create_event(payload: EventCreate, db: Session = Depends(get_db)):
    ev = Event(
        name=payload.name,
        course_id=payload.course_id,
        location=payload.location,
        venue_id=payload.venue_id,
        start_date=payload.start_date,
        end_date=payload.end_date,
        max_capacity=payload.max_capacity,
        status="PLANNED",
        notes=payload.notes,
    )
    db.add(ev)
    db.commit()
    db.refresh(ev)
    resp = EventResponse.model_validate(ev)
    resp.enrolled_count = 0
    return resp


@app.get("/events", response_model=list[EventResponse])
def list_events(
    status_filter: str | None = Query(None, alias="status"),
    location: str | None = None,
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    q = db.query(Event)
    if status_filter:
        q = q.filter(Event.status == status_filter.upper())
    if location:
        q = q.filter(Event.location.ilike(f"%{location}%"))
    events = q.order_by(Event.start_date).offset(offset).limit(limit).all()

    results = []
    for ev in events:
        resp = EventResponse.model_validate(ev)
        resp.enrolled_count = len([e for e in ev.enrollments if e.status != "DROPPED"])
        results.append(resp)
    return results


@app.get("/events/{event_id}", response_model=EventResponse)
def get_event(event_id: int, db: Session = Depends(get_db)):
    ev = db.query(Event).filter(Event.id == event_id).first()
    if not ev:
        raise HTTPException(status_code=404, detail=f"Event {event_id} not found")
    resp = EventResponse.model_validate(ev)
    resp.enrolled_count = len([e for e in ev.enrollments if e.status != "DROPPED"])
    return resp


@app.put("/events/{event_id}", response_model=EventResponse)
def update_event(event_id: int, payload: EventCreate, db: Session = Depends(get_db)):
    ev = db.query(Event).filter(Event.id == event_id).first()
    if not ev:
        raise HTTPException(status_code=404, detail=f"Event {event_id} not found")
    ev.name = payload.name
    ev.course_id = payload.course_id
    ev.location = payload.location
    ev.venue_id = payload.venue_id
    ev.start_date = payload.start_date
    ev.end_date = payload.end_date
    ev.max_capacity = payload.max_capacity
    ev.notes = payload.notes
    db.commit()
    db.refresh(ev)
    resp = EventResponse.model_validate(ev)
    resp.enrolled_count = len([e for e in ev.enrollments if e.status != "DROPPED"])
    return resp


@app.patch("/events/{event_id}/status")
def update_event_status(
    event_id: int,
    new_status: str = Query(..., alias="status"),
    db: Session = Depends(get_db),
):
    valid = {"PLANNED", "ACTIVE", "COMPLETE", "CANCELLED"}
    if new_status.upper() not in valid:
        raise HTTPException(status_code=422, detail=f"Invalid status. Must be one of: {valid}")
    ev = db.query(Event).filter(Event.id == event_id).first()
    if not ev:
        raise HTTPException(status_code=404, detail=f"Event {event_id} not found")
    ev.status = new_status.upper()
    db.commit()
    return {"id": ev.id, "status": ev.status}


@app.post("/events/{event_id}/instructors/{instructor_id}")
def assign_instructor(event_id: int, instructor_id: int, db: Session = Depends(get_db)):
    ev = db.query(Event).filter(Event.id == event_id).first()
    if not ev:
        raise HTTPException(status_code=404, detail=f"Event {event_id} not found")
    inst = db.query(Instructor).filter(Instructor.id == instructor_id).first()
    if not inst:
        raise HTTPException(status_code=404, detail=f"Instructor {instructor_id} not found")
    if inst in ev.instructors:
        raise HTTPException(status_code=409, detail="Instructor already assigned to this event")
    # Validate instructor availability window covers the event dates
    if inst.available_from and inst.available_to:
        if ev.start_date < inst.available_from or ev.end_date > inst.available_to:
            raise HTTPException(
                status_code=422,
                detail=(
                    f"Instructor {inst.name} is available "
                    f"{inst.available_from.isoformat()}–{inst.available_to.isoformat()}, "
                    f"but event runs {ev.start_date.isoformat()}–{ev.end_date.isoformat()}"
                ),
            )
    ev.instructors.append(inst)
    db.commit()
    return {"detail": f"Instructor {inst.name} assigned to event {ev.name}"}


@app.delete("/events/{event_id}/instructors/{instructor_id}")
def unassign_instructor(event_id: int, instructor_id: int, db: Session = Depends(get_db)):
    ev = db.query(Event).filter(Event.id == event_id).first()
    if not ev:
        raise HTTPException(status_code=404, detail=f"Event {event_id} not found")
    inst = db.query(Instructor).filter(Instructor.id == instructor_id).first()
    if not inst:
        raise HTTPException(status_code=404, detail=f"Instructor {instructor_id} not found")
    if inst not in ev.instructors:
        raise HTTPException(status_code=404, detail="Instructor not assigned to this event")
    ev.instructors.remove(inst)
    db.commit()
    return {"detail": f"Instructor {inst.name} removed from event {ev.name}"}


# ---------------------------------------------------------------------------
# Instructors CRUD
# ---------------------------------------------------------------------------
@app.post("/instructors", response_model=InstructorResponse, status_code=status.HTTP_201_CREATED)
def create_instructor(payload: InstructorCreate, db: Session = Depends(get_db)):
    inst = Instructor(
        name=payload.name,
        rank=payload.rank,
        unit=payload.unit,
        available_from=payload.available_from,
        available_to=payload.available_to,
    )
    inst.set_qualifications(payload.qualifications)
    db.add(inst)
    db.commit()
    db.refresh(inst)
    resp = InstructorResponse.model_validate(inst)
    resp.qualifications = inst.get_qualifications()
    resp.assigned_events = len(inst.events)
    return resp


@app.get("/instructors", response_model=list[InstructorResponse])
def list_instructors(db: Session = Depends(get_db)):
    instructors = db.query(Instructor).order_by(Instructor.name).all()
    results = []
    for inst in instructors:
        resp = InstructorResponse.model_validate(inst)
        resp.qualifications = inst.get_qualifications()
        resp.assigned_events = len(inst.events)
        results.append(resp)
    return results


@app.get("/instructors/{instructor_id}", response_model=InstructorResponse)
def get_instructor(instructor_id: int, db: Session = Depends(get_db)):
    inst = db.query(Instructor).filter(Instructor.id == instructor_id).first()
    if not inst:
        raise HTTPException(status_code=404, detail=f"Instructor {instructor_id} not found")
    resp = InstructorResponse.model_validate(inst)
    resp.qualifications = inst.get_qualifications()
    resp.assigned_events = len(inst.events)
    return resp


@app.delete("/instructors/{instructor_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_instructor(instructor_id: int, db: Session = Depends(get_db)):
    inst = db.query(Instructor).filter(Instructor.id == instructor_id).first()
    if not inst:
        raise HTTPException(status_code=404, detail=f"Instructor {instructor_id} not found")
    db.delete(inst)
    db.commit()


# ---------------------------------------------------------------------------
# Enrollments CRUD
# ---------------------------------------------------------------------------
@app.post("/enrollments", response_model=EnrollmentResponse, status_code=status.HTTP_201_CREATED)
def create_enrollment(payload: EnrollmentCreate, db: Session = Depends(get_db)):
    ev = db.query(Event).filter(Event.id == payload.event_id).first()
    if not ev:
        raise HTTPException(status_code=404, detail=f"Event {payload.event_id} not found")

    # Check capacity
    active_enrolled = len([e for e in ev.enrollments if e.status not in ("DROPPED",)])
    if active_enrolled >= ev.max_capacity:
        raise HTTPException(status_code=422, detail="Event is at max capacity")

    # Check for duplicate enrollment
    existing = (
        db.query(Enrollment)
        .filter(
            Enrollment.event_id == payload.event_id,
            Enrollment.dodid == payload.dodid,
            Enrollment.status != "DROPPED",
        )
        .first()
    )
    if existing:
        raise HTTPException(status_code=409, detail="Soldier already enrolled in this event")

    enrollment = Enrollment(
        event_id=payload.event_id,
        dodid=payload.dodid,
        soldier_name=payload.soldier_name,
        soldier_rank=payload.soldier_rank,
        soldier_unit=payload.soldier_unit,
        status="ENROLLED",
    )
    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)
    return EnrollmentResponse.model_validate(enrollment)


@app.get("/enrollments", response_model=list[EnrollmentResponse])
def list_enrollments(
    event_id: int | None = None,
    dodid: str | None = None,
    db: Session = Depends(get_db),
):
    q = db.query(Enrollment)
    if event_id:
        q = q.filter(Enrollment.event_id == event_id)
    if dodid:
        q = q.filter(Enrollment.dodid == dodid)
    return [EnrollmentResponse.model_validate(e) for e in q.all()]


@app.patch("/enrollments/{enrollment_id}/status")
def update_enrollment_status(
    enrollment_id: int,
    new_status: str = Query(..., alias="status"),
    db: Session = Depends(get_db),
):
    valid = {"ENROLLED", "COMPLETE", "NO_SHOW", "DROPPED"}
    if new_status.upper() not in valid:
        raise HTTPException(status_code=422, detail=f"Invalid status. Must be one of: {valid}")
    enrollment = db.query(Enrollment).filter(Enrollment.id == enrollment_id).first()
    if not enrollment:
        raise HTTPException(status_code=404, detail=f"Enrollment {enrollment_id} not found")
    enrollment.status = new_status.upper()
    db.commit()
    return {"id": enrollment.id, "status": enrollment.status}


# ---------------------------------------------------------------------------
# Venues CRUD
# ---------------------------------------------------------------------------
@app.post("/venues", response_model=VenueResponse, status_code=status.HTTP_201_CREATED)
def create_venue(payload: VenueCreate, db: Session = Depends(get_db)):
    venue = Venue(**payload.model_dump())
    db.add(venue)
    db.commit()
    db.refresh(venue)
    return VenueResponse.model_validate(venue)


@app.get("/venues", response_model=list[VenueResponse])
def list_venues(db: Session = Depends(get_db)):
    return [VenueResponse.model_validate(v) for v in db.query(Venue).order_by(Venue.name).all()]


@app.get("/venues/{venue_id}", response_model=VenueResponse)
def get_venue(venue_id: int, db: Session = Depends(get_db)):
    venue = db.query(Venue).filter(Venue.id == venue_id).first()
    if not venue:
        raise HTTPException(status_code=404, detail=f"Venue {venue_id} not found")
    return VenueResponse.model_validate(venue)


@app.delete("/venues/{venue_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_venue(venue_id: int, db: Session = Depends(get_db)):
    venue = db.query(Venue).filter(Venue.id == venue_id).first()
    if not venue:
        raise HTTPException(status_code=404, detail=f"Venue {venue_id} not found")
    # Check if venue is in use
    if venue.events:
        raise HTTPException(status_code=409, detail="Cannot delete venue with assigned events")
    db.delete(venue)
    db.commit()


# ---------------------------------------------------------------------------
# Analytics endpoints
# ---------------------------------------------------------------------------
@app.get("/calendar")
def calendar(
    start: date | None = None,
    end: date | None = None,
    db: Session = Depends(get_db),
):
    return get_calendar_data(db, start=start, end=end)


@app.get("/conflicts", response_model=list[ScheduleConflict])
def conflicts(db: Session = Depends(get_db)):
    raw = check_instructor_conflicts(db)
    return [
        ScheduleConflict(
            instructor_name=c["instructor_name"],
            event1=c["event1"],
            event2=c["event2"],
            overlap_dates=c["overlap_dates"],
        )
        for c in raw
    ]


@app.get("/utilization")
def utilization(db: Session = Depends(get_db)):
    return get_capacity_utilization(db)
