"""MTT Scheduler — database models and business logic."""

from __future__ import annotations

import json
from datetime import UTC, date, datetime
from pathlib import Path

from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Table,
    Text,
    create_engine,
    event,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Session,
    relationship,
    sessionmaker,
)

import sys
from pathlib import Path as _Path
_apps_dir = str(_Path(__file__).resolve().parent.parent)
if _apps_dir not in sys.path:
    sys.path.insert(0, _apps_dir)

from shared.audit_mixin import AuditMixin

# ---------------------------------------------------------------------------
# Database path — sits next to this file; *.db is gitignored
# ---------------------------------------------------------------------------
DB_PATH = Path(__file__).parent / "mtt_scheduler.db"
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
# Association table: many-to-many between events and instructors
# ---------------------------------------------------------------------------
event_instructors = Table(
    "event_instructors",
    Base.metadata,
    Column("event_id", Integer, ForeignKey("events.id"), primary_key=True),
    Column("instructor_id", Integer, ForeignKey("instructors.id"), primary_key=True),
)


# ---------------------------------------------------------------------------
# ORM models
# ---------------------------------------------------------------------------
class Event(Base, AuditMixin):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    course_id = Column(String(10), nullable=False)
    location = Column(String(100), nullable=False)
    venue_id = Column(Integer, ForeignKey("venues.id"), nullable=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    max_capacity = Column(Integer, nullable=False)
    status = Column(String(20), nullable=False, default="PLANNED")
    notes = Column(Text, nullable=True)

    venue = relationship("Venue", back_populates="events")
    instructors = relationship(
        "Instructor", secondary=event_instructors, back_populates="events"
    )
    enrollments = relationship(
        "Enrollment", back_populates="event", cascade="all, delete-orphan"
    )


class Instructor(Base):
    __tablename__ = "instructors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    rank = Column(String(10), nullable=False)
    unit = Column(String(50), nullable=False)
    qualifications = Column(Text, nullable=True)  # JSON-encoded list
    available_from = Column(Date, nullable=False)
    available_to = Column(Date, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))

    events = relationship(
        "Event", secondary=event_instructors, back_populates="instructors"
    )

    def get_qualifications(self) -> list[str]:
        """Decode qualifications from JSON text."""
        if not self.qualifications:
            return []
        try:
            return json.loads(self.qualifications)
        except (json.JSONDecodeError, TypeError):
            return []

    def set_qualifications(self, quals: list[str]) -> None:
        """Encode qualifications to JSON text."""
        self.qualifications = json.dumps(quals)


class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    dodid = Column(String(10), nullable=False)
    soldier_name = Column(String(100), nullable=False)
    soldier_rank = Column(String(10), nullable=False)
    soldier_unit = Column(String(50), nullable=False)
    status = Column(String(20), nullable=False, default="ENROLLED")
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))

    event = relationship("Event", back_populates="enrollments")


class Venue(Base):
    __tablename__ = "venues"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    location = Column(String(100), nullable=False)
    capacity = Column(Integer, nullable=False)
    has_network = Column(Boolean, default=False)
    has_sipr = Column(Boolean, default=False)
    notes = Column(Text, nullable=True)

    events = relationship("Event", back_populates="venue")


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
    """Create all tables if they don't exist."""
    Base.metadata.create_all(bind=engine)


# ---------------------------------------------------------------------------
# Business logic
# ---------------------------------------------------------------------------
def get_calendar_data(
    db: Session,
    start: date | None = None,
    end: date | None = None,
) -> list[dict]:
    """Return events formatted for timeline/calendar display.

    Optionally filter by date range.
    """
    q = db.query(Event)
    if start:
        q = q.filter(Event.end_date >= start)
    if end:
        q = q.filter(Event.start_date <= end)
    q = q.order_by(Event.start_date)

    results = []
    for ev in q.all():
        enrolled = len([e for e in ev.enrollments if e.status != "DROPPED"])
        instructor_names = [f"{i.rank} {i.name}" for i in ev.instructors]
        venue_name = ev.venue.name if ev.venue else "TBD"
        results.append({
            "id": ev.id,
            "name": ev.name,
            "course_id": ev.course_id,
            "location": ev.location,
            "venue": venue_name,
            "start_date": ev.start_date.isoformat(),
            "end_date": ev.end_date.isoformat(),
            "status": ev.status,
            "max_capacity": ev.max_capacity,
            "enrolled": enrolled,
            "fill_pct": round(enrolled / ev.max_capacity * 100, 1) if ev.max_capacity else 0,
            "instructors": instructor_names,
        })
    return results


def check_instructor_conflicts(db: Session) -> list[dict]:
    """Find scheduling overlaps where an instructor is assigned to
    multiple events with overlapping date ranges.
    """
    instructors = db.query(Instructor).all()
    conflicts = []

    for inst in instructors:
        assigned = sorted(inst.events, key=lambda e: e.start_date)
        for i in range(len(assigned)):
            for j in range(i + 1, len(assigned)):
                ev1 = assigned[i]
                ev2 = assigned[j]
                # Check for date overlap
                if ev1.end_date >= ev2.start_date and ev1.start_date <= ev2.end_date:
                    # Calculate overlap period
                    overlap_start = max(ev1.start_date, ev2.start_date)
                    overlap_end = min(ev1.end_date, ev2.end_date)
                    conflicts.append({
                        "instructor_name": f"{inst.rank} {inst.name}",
                        "instructor_id": inst.id,
                        "event1": ev1.name,
                        "event1_id": ev1.id,
                        "event2": ev2.name,
                        "event2_id": ev2.id,
                        "overlap_dates": f"{overlap_start.isoformat()} to {overlap_end.isoformat()}",
                    })
    return conflicts


def get_capacity_utilization(db: Session) -> list[dict]:
    """Return enrollment fill percentage for each event."""
    events = db.query(Event).order_by(Event.start_date).all()
    results = []
    for ev in events:
        enrolled = len([e for e in ev.enrollments if e.status != "DROPPED"])
        results.append({
            "id": ev.id,
            "name": ev.name,
            "course_id": ev.course_id,
            "location": ev.location,
            "status": ev.status,
            "max_capacity": ev.max_capacity,
            "enrolled": enrolled,
            "fill_pct": round(enrolled / ev.max_capacity * 100, 1) if ev.max_capacity else 0,
            "available": ev.max_capacity - enrolled,
        })
    return results


def get_location_summary(db: Session) -> list[dict]:
    """Return count of events per location with status breakdown."""
    events = db.query(Event).all()

    # Group by location
    loc_data: dict[str, dict] = {}
    for ev in events:
        loc = ev.location
        if loc not in loc_data:
            loc_data[loc] = {
                "location": loc,
                "total_events": 0,
                "planned": 0,
                "active": 0,
                "complete": 0,
                "cancelled": 0,
                "total_capacity": 0,
                "total_enrolled": 0,
            }
        loc_data[loc]["total_events"] += 1
        loc_data[loc][ev.status.lower()] += 1
        loc_data[loc]["total_capacity"] += ev.max_capacity
        enrolled = len([e for e in ev.enrollments if e.status != "DROPPED"])
        loc_data[loc]["total_enrolled"] += enrolled

    return sorted(loc_data.values(), key=lambda x: x["total_events"], reverse=True)
