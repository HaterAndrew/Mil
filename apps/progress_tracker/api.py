"""Progress Tracker — FastAPI application."""

from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, Query, status
from shared.auth import verify_api_key
from shared.factory import create_app
from sqlalchemy.orm import Session

from .db import (
    Goal,
    Milestone,
    generate_training_record,
    get_all_overdue,
    get_db,
    get_soldier_goals,
    get_soldier_timeline,
    get_stalled_soldiers,
    init_db,
)
from .models import (
    GoalCreate,
    GoalResponse,
    MilestoneCreate,
    MilestoneRecordItem,
    MilestoneResponse,
    StalledSoldier,
    TrainingRecordOut,
)


# ---------------------------------------------------------------------------
# App lifecycle
# ---------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = create_app(title="Progress Tracker", version="1.0.0", lifespan=lifespan)


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------
@app.get("/health")
def health():
    return {"status": "ok"}


# ---------------------------------------------------------------------------
# Milestones
# ---------------------------------------------------------------------------
@app.post(
    "/milestones", response_model=MilestoneResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(verify_api_key)],
)
def create_milestone(payload: MilestoneCreate, db: Session = Depends(get_db)):
    milestone = Milestone(
        dodid=payload.dodid,
        course_id=payload.course_id,
        target_date=payload.target_date,
        notes=payload.notes,
        status="ON_TRACK",
    )
    db.add(milestone)
    db.commit()
    db.refresh(milestone)

    # Compute live status for response
    from .db import _compute_status
    ms_status, days_remaining = _compute_status(milestone.target_date)
    return MilestoneResponse(
        id=milestone.id,
        dodid=milestone.dodid,
        course_id=milestone.course_id,
        target_date=milestone.target_date,
        status=ms_status,
        notes=milestone.notes,
        days_remaining=days_remaining,
        created_at=milestone.created_at,
    )


@app.get("/milestones/{dodid}", response_model=list[MilestoneResponse])
def get_milestones(dodid: str, db: Session = Depends(get_db)):
    timeline = get_soldier_timeline(dodid, db)
    return [
        MilestoneResponse(
            id=m["id"],
            dodid=m["dodid"],
            course_id=m["course_id"],
            target_date=m["target_date"],
            status=m["status"],
            notes=m["notes"],
            days_remaining=m["days_remaining"],
            created_at=m["created_at"],
        )
        for m in timeline
    ]


# ---------------------------------------------------------------------------
# Stalled soldiers
# ---------------------------------------------------------------------------
@app.get("/stalled", response_model=list[StalledSoldier])
def stalled(days: int = Query(30, ge=1, le=365), db: Session = Depends(get_db)):
    return get_stalled_soldiers(db, days=days)


# ---------------------------------------------------------------------------
# Overdue milestones
# ---------------------------------------------------------------------------
@app.get("/overdue")
def overdue(db: Session = Depends(get_db)):
    return get_all_overdue(db)


# ---------------------------------------------------------------------------
# Training record
# ---------------------------------------------------------------------------
@app.get("/record/{dodid}", response_model=TrainingRecordOut)
def training_record(dodid: str, db: Session = Depends(get_db)):
    record = generate_training_record(dodid, db)
    if not record:
        raise HTTPException(status_code=404, detail=f"Trainee {dodid} not found")

    milestones = [
        MilestoneRecordItem(
            course_id=m["course_id"],
            course_name=m["course_name"],
            target_date=m["target_date"],
            status=m["status"],
            days_remaining=m["days_remaining"],
            notes=m.get("notes"),
        )
        for m in record["milestones"]
    ]

    return TrainingRecordOut(
        dodid=record["dodid"],
        name=record["name"],
        rank=record["rank"],
        unit=record["unit"],
        milestones=milestones,
        overall_status=record["overall_status"],
        pct_complete=record["pct_complete"],
    )


# ---------------------------------------------------------------------------
# Goals
# ---------------------------------------------------------------------------
@app.post(
    "/goals", response_model=GoalResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(verify_api_key)],
)
def create_goal(payload: GoalCreate, db: Session = Depends(get_db)):
    goal = Goal(
        dodid=payload.dodid,
        target_course=payload.target_course,
        target_date=payload.target_date,
    )
    db.add(goal)
    db.commit()
    db.refresh(goal)

    # Check eligibility via readiness_tracker
    from readiness_tracker.db import SessionLocal as RTSession
    from readiness_tracker.db import check_eligibility
    rt_db = RTSession()
    try:
        eligible, missing = check_eligibility(goal.dodid, goal.target_course, rt_db)
    finally:
        rt_db.close()

    return GoalResponse(
        id=goal.id,
        dodid=goal.dodid,
        target_course=goal.target_course,
        target_date=goal.target_date,
        achieved=goal.achieved,
        eligible=eligible,
        missing_prereqs=missing,
        created_at=goal.created_at,
    )


@app.get("/goals/{dodid}", response_model=list[GoalResponse])
def get_goals(dodid: str, db: Session = Depends(get_db)):
    goals = get_soldier_goals(dodid, db)
    return [
        GoalResponse(
            id=g["id"],
            dodid=g["dodid"],
            target_course=g["target_course"],
            target_date=g["target_date"],
            achieved=g["achieved"],
            eligible=g["eligible"],
            missing_prereqs=g["missing_prereqs"],
            created_at=g["created_at"],
        )
        for g in goals
    ]
