"""Progress Tracker — database models and business logic.

Tracks individual soldier training milestones, flags stalled/overdue
progression, and generates printable training records.
"""

from __future__ import annotations

import sys
from datetime import UTC, date, datetime, timedelta
from pathlib import Path

# Ensure sibling packages (readiness_tracker, etc.) are importable
_apps_dir = str(Path(__file__).resolve().parent.parent)
if _apps_dir not in sys.path:
    sys.path.insert(0, _apps_dir)

from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    Integer,
    String,
    Text,
    create_engine,
    event,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Session,
    sessionmaker,
)

# Import shared prereq chain and catalog from readiness_tracker
from readiness_tracker.db import (
    COURSE_CATALOG,
    PREREQ_CHAIN,
    SessionLocal as ReadinessSessionLocal,
    Trainee,
    Completion,
    check_eligibility,
)

# ---------------------------------------------------------------------------
# Database path — sits next to this file; *.db is gitignored
# ---------------------------------------------------------------------------
DB_PATH = Path(__file__).parent / "progress_tracker.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


@event.listens_for(engine, "connect")
def _set_sqlite_pragmas(dbapi_conn, _connection_record):
    cursor = dbapi_conn.cursor()
    cursor.execute("PRAGMA journal_mode=WAL")
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


class Base(DeclarativeBase):
    pass


# ---------------------------------------------------------------------------
# ORM models
# ---------------------------------------------------------------------------
class Milestone(Base):
    __tablename__ = "milestones"

    id = Column(Integer, primary_key=True, autoincrement=True)
    dodid = Column(String(10), nullable=False, index=True)
    course_id = Column(String(10), nullable=False)
    target_date = Column(Date, nullable=False)
    status = Column(String(20), nullable=False, default="ON_TRACK")
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))


class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, autoincrement=True)
    dodid = Column(String(10), nullable=False, index=True)
    target_course = Column(String(10), nullable=False)
    target_date = Column(Date, nullable=False)
    achieved = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def get_db():
    """Yield a DB session; auto-close on exit."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Create tables if they don't exist."""
    Base.metadata.create_all(bind=engine)


def _compute_status(target_date: date) -> tuple[str, int]:
    """Determine milestone status and days remaining from target_date.

    Returns (status, days_remaining).
    - OVERDUE: target_date is past
    - AT_RISK: target_date is within 14 days
    - ON_TRACK: target_date is > 14 days away
    """
    today = date.today()
    delta = (target_date - today).days
    if delta < 0:
        return "OVERDUE", delta
    elif delta <= 14:
        return "AT_RISK", delta
    else:
        return "ON_TRACK", delta


# ---------------------------------------------------------------------------
# Business logic
# ---------------------------------------------------------------------------
def get_soldier_timeline(dodid: str, db: Session) -> list[dict]:
    """Return milestone + status data for one soldier, sorted by target_date."""
    milestones = (
        db.query(Milestone)
        .filter(Milestone.dodid == dodid)
        .order_by(Milestone.target_date)
        .all()
    )
    results = []
    for m in milestones:
        if m.status == "COMPLETE":
            status = "COMPLETE"
            days_remaining = 0
        else:
            status, days_remaining = _compute_status(m.target_date)
        results.append({
            "id": m.id,
            "dodid": m.dodid,
            "course_id": m.course_id,
            "course_name": COURSE_CATALOG.get(m.course_id, (m.course_id, 0))[0],
            "target_date": m.target_date,
            "status": status,
            "days_remaining": days_remaining,
            "notes": m.notes,
            "created_at": m.created_at,
        })
    return results


def flag_overdue(db: Session) -> int:
    """Scan all non-COMPLETE milestones, update status based on target_date vs today.

    Returns count of milestones updated.
    """
    milestones = (
        db.query(Milestone)
        .filter(Milestone.status != "COMPLETE")
        .all()
    )
    updated = 0
    for m in milestones:
        new_status, _ = _compute_status(m.target_date)
        if m.status != new_status:
            m.status = new_status
            updated += 1
    db.commit()
    return updated


def get_all_overdue(db: Session) -> list[dict]:
    """Return all overdue milestones with soldier info from readiness_tracker."""
    # First flag/update statuses
    flag_overdue(db)

    overdue = (
        db.query(Milestone)
        .filter(Milestone.status == "OVERDUE")
        .order_by(Milestone.target_date)
        .all()
    )

    # Look up soldier info from readiness_tracker DB
    rt_db = ReadinessSessionLocal()
    try:
        results = []
        for m in overdue:
            trainee = rt_db.query(Trainee).filter(Trainee.dodid == m.dodid).first()
            name = f"{trainee.last_name}, {trainee.first_name}" if trainee else m.dodid
            rank = trainee.rank if trainee else ""
            unit = trainee.unit if trainee else ""
            _, days_remaining = _compute_status(m.target_date)
            results.append({
                "id": m.id,
                "dodid": m.dodid,
                "name": name,
                "rank": rank,
                "unit": unit,
                "course_id": m.course_id,
                "course_name": COURSE_CATALOG.get(m.course_id, (m.course_id, 0))[0],
                "target_date": m.target_date,
                "days_overdue": abs(days_remaining),
            })
        return results
    finally:
        rt_db.close()


def get_stalled_soldiers(db: Session, days: int = 30) -> list[dict]:
    """Find soldiers with no new milestone completions in N days.

    Cross-references readiness_tracker for soldier info and last completion date.
    """
    rt_db = ReadinessSessionLocal()
    try:
        # Get all trainees
        trainees = rt_db.query(Trainee).all()
        cutoff = date.today() - timedelta(days=days)
        stalled = []

        for t in trainees:
            # Find latest GO completion date
            completions = [
                c for c in t.completions
                if c.result == "GO"
            ]
            if not completions:
                # Never completed anything — stalled from day one
                stalled.append({
                    "dodid": t.dodid,
                    "name": f"{t.last_name}, {t.first_name}",
                    "rank": t.rank,
                    "unit": t.unit,
                    "last_completion_date": None,
                    "days_since_activity": 999,
                    "furthest_course": None,
                })
                continue

            latest = max(completions, key=lambda c: c.evaluation_date)
            if latest.evaluation_date < cutoff:
                go_courses = sorted(
                    [c.course_id for c in completions],
                )
                days_since = (date.today() - latest.evaluation_date).days
                stalled.append({
                    "dodid": t.dodid,
                    "name": f"{t.last_name}, {t.first_name}",
                    "rank": t.rank,
                    "unit": t.unit,
                    "last_completion_date": latest.evaluation_date,
                    "days_since_activity": days_since,
                    "furthest_course": go_courses[-1] if go_courses else None,
                })

        # Sort by most stalled first
        stalled.sort(key=lambda x: x["days_since_activity"], reverse=True)
        return stalled
    finally:
        rt_db.close()


def generate_training_record(dodid: str, db: Session) -> dict | None:
    """Compile full training record for a soldier (printable format).

    Combines milestone data from this DB with soldier info from readiness_tracker.
    """
    rt_db = ReadinessSessionLocal()
    try:
        trainee = rt_db.query(Trainee).filter(Trainee.dodid == dodid).first()
        if not trainee:
            return None

        milestones = get_soldier_timeline(dodid, db)

        # Compute overall status and percent complete
        total = len(milestones)
        if total == 0:
            return {
                "dodid": dodid,
                "name": f"{trainee.last_name}, {trainee.first_name}",
                "rank": trainee.rank,
                "unit": trainee.unit,
                "milestones": [],
                "overall_status": "ON_TRACK",
                "pct_complete": 0.0,
                "completions": [],
            }

        complete_count = sum(1 for m in milestones if m["status"] == "COMPLETE")
        overdue_count = sum(1 for m in milestones if m["status"] == "OVERDUE")
        at_risk_count = sum(1 for m in milestones if m["status"] == "AT_RISK")

        pct = round(complete_count / total * 100, 1)

        if overdue_count > 0:
            overall = "OVERDUE"
        elif at_risk_count > 0:
            overall = "AT_RISK"
        elif complete_count == total:
            overall = "COMPLETE"
        else:
            overall = "ON_TRACK"

        # Get completion history from readiness_tracker
        completions = []
        for c in trainee.completions:
            completions.append({
                "course_id": c.course_id,
                "course_name": COURSE_CATALOG.get(c.course_id, (c.course_id, 0))[0],
                "result": c.result,
                "evaluation_date": c.evaluation_date,
                "evaluator_name": c.evaluator_name or "",
            })

        return {
            "dodid": dodid,
            "name": f"{trainee.last_name}, {trainee.first_name}",
            "rank": trainee.rank,
            "unit": trainee.unit,
            "mos": trainee.mos or "",
            "milestones": milestones,
            "overall_status": overall,
            "pct_complete": pct,
            "completions": completions,
        }
    finally:
        rt_db.close()


def get_soldier_goals(dodid: str, db: Session) -> list[dict]:
    """Return all goals for a soldier with eligibility info."""
    goals = (
        db.query(Goal)
        .filter(Goal.dodid == dodid)
        .order_by(Goal.target_date)
        .all()
    )

    rt_db = ReadinessSessionLocal()
    try:
        results = []
        for g in goals:
            eligible, missing = check_eligibility(g.dodid, g.target_course, rt_db)
            results.append({
                "id": g.id,
                "dodid": g.dodid,
                "target_course": g.target_course,
                "course_name": COURSE_CATALOG.get(g.target_course, (g.target_course, 0))[0],
                "target_date": g.target_date,
                "achieved": g.achieved,
                "eligible": eligible,
                "missing_prereqs": missing,
                "created_at": g.created_at,
            })
        return results
    finally:
        rt_db.close()
