"""Enrollment Manager — database models and business logic."""

from __future__ import annotations

import sys
from datetime import UTC, date, datetime
from pathlib import Path

# Ensure sibling packages (readiness_tracker, etc.) are importable
_apps_dir = str(Path(__file__).resolve().parent.parent)
if _apps_dir not in sys.path:
    sys.path.insert(0, _apps_dir)

from sqlalchemy import (
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
    create_engine,
    event,
    func,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Session,
    relationship,
    sessionmaker,
)

# ---------------------------------------------------------------------------
# Database path — sits next to this file; *.db is gitignored
# ---------------------------------------------------------------------------
DB_PATH = Path(__file__).parent / "enrollment_manager.db"
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
# Course catalog — imported from readiness_tracker (single source of truth)
# ---------------------------------------------------------------------------
from readiness_tracker.db import COURSE_CATALOG  # noqa: E402


# ---------------------------------------------------------------------------
# ORM models
# ---------------------------------------------------------------------------
class TrainingClass(Base):
    """A scheduled training class (one offering of a course)."""
    __tablename__ = "training_classes"

    class_id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(String(10), nullable=False)
    class_name = Column(String(100), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    location = Column(String(100), nullable=False)
    max_seats = Column(Integer, nullable=False)
    instructor_name = Column(String(100), nullable=True)
    status = Column(String(20), nullable=False, default="SCHEDULED")  # SCHEDULED/IN_PROGRESS/COMPLETED/CANCELLED
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))

    enrollments = relationship(
        "Enrollment", back_populates="training_class", cascade="all, delete-orphan"
    )
    waitlist_entries = relationship(
        "WaitlistEntry", back_populates="training_class", cascade="all, delete-orphan"
    )


class Enrollment(Base):
    """A student enrolled in a training class."""
    __tablename__ = "enrollments"
    __table_args__ = (
        UniqueConstraint("class_id", "dodid", name="uq_class_student"),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    class_id = Column(Integer, ForeignKey("training_classes.class_id"), nullable=False)
    dodid = Column(String(10), nullable=False, index=True)
    last_name = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    rank = Column(String(10), nullable=False)
    unit = Column(String(50), nullable=False)
    enrollment_date = Column(Date, nullable=False)
    status = Column(String(20), nullable=False, default="ENROLLED")  # ENROLLED/WAITLISTED/DROPPED/COMPLETED/NO_SHOW
    seat_number = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))

    training_class = relationship("TrainingClass", back_populates="enrollments")


class WaitlistEntry(Base):
    """A student waiting for a seat in a training class."""
    __tablename__ = "waitlist_entries"

    id = Column(Integer, primary_key=True, autoincrement=True)
    class_id = Column(Integer, ForeignKey("training_classes.class_id"), nullable=False)
    dodid = Column(String(10), nullable=False, index=True)
    last_name = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    rank = Column(String(10), nullable=False)
    unit = Column(String(50), nullable=False)
    request_date = Column(Date, nullable=False)
    priority = Column(Integer, default=0)  # higher = more priority
    status = Column(String(20), nullable=False, default="WAITING")  # WAITING/PROMOTED/EXPIRED
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))

    training_class = relationship("TrainingClass", back_populates="waitlist_entries")


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


# ---------------------------------------------------------------------------
# Business logic
# ---------------------------------------------------------------------------
def get_class_roster(class_id: int, db: Session) -> list[Enrollment]:
    """Return all enrolled students for a class, ordered by seat number."""
    return (
        db.query(Enrollment)
        .filter(Enrollment.class_id == class_id, Enrollment.status == "ENROLLED")
        .order_by(Enrollment.seat_number)
        .all()
    )


def get_class_availability(class_id: int, db: Session) -> dict:
    """Return seat availability for a class.

    Returns dict with max_seats, enrolled_count, seats_remaining, and fill_pct.
    """
    tc = db.query(TrainingClass).filter(TrainingClass.class_id == class_id).first()
    if not tc:
        return {"max_seats": 0, "enrolled_count": 0, "seats_remaining": 0, "fill_pct": 0.0}

    enrolled_count = (
        db.query(Enrollment)
        .filter(Enrollment.class_id == class_id, Enrollment.status == "ENROLLED")
        .count()
    )
    waitlist_count = (
        db.query(WaitlistEntry)
        .filter(WaitlistEntry.class_id == class_id, WaitlistEntry.status == "WAITING")
        .count()
    )
    seats_remaining = max(0, tc.max_seats - enrolled_count)
    fill_pct = round(enrolled_count / tc.max_seats * 100, 1) if tc.max_seats else 0.0

    return {
        "class_id": class_id,
        "class_name": tc.class_name,
        "max_seats": tc.max_seats,
        "enrolled_count": enrolled_count,
        "seats_remaining": seats_remaining,
        "waitlist_count": waitlist_count,
        "fill_pct": fill_pct,
    }


def enroll_student(
    class_id: int,
    dodid: str,
    last_name: str,
    first_name: str,
    rank: str,
    unit: str,
    db: Session,
) -> dict:
    """Enroll a student in a class. Auto-waitlist if class is full.

    Returns dict with status ('enrolled' or 'waitlisted') and the record.
    """
    tc = db.query(TrainingClass).filter(TrainingClass.class_id == class_id).first()
    if not tc:
        raise ValueError(f"Training class {class_id} not found")

    if tc.status == "CANCELLED":
        raise ValueError(f"Class {class_id} is cancelled")

    # Check if student is already enrolled
    existing = (
        db.query(Enrollment)
        .filter(Enrollment.class_id == class_id, Enrollment.dodid == dodid)
        .first()
    )
    if existing:
        raise ValueError(f"Student {dodid} already enrolled in class {class_id}")

    # Check if student is already on the waitlist
    existing_waitlist = (
        db.query(WaitlistEntry)
        .filter(
            WaitlistEntry.class_id == class_id,
            WaitlistEntry.dodid == dodid,
            WaitlistEntry.status == "WAITING",
        )
        .first()
    )
    if existing_waitlist:
        raise ValueError(f"Student {dodid} already on waitlist for class {class_id}")

    enrolled_count = (
        db.query(Enrollment)
        .filter(Enrollment.class_id == class_id, Enrollment.status == "ENROLLED")
        .count()
    )

    if enrolled_count < tc.max_seats:
        # Seat available — enroll directly
        seat_num = enrolled_count + 1
        enrollment = Enrollment(
            class_id=class_id,
            dodid=dodid,
            last_name=last_name.strip().upper(),
            first_name=first_name.strip().upper(),
            rank=rank.strip().upper(),
            unit=unit.strip().upper(),
            enrollment_date=date.today(),
            status="ENROLLED",
            seat_number=seat_num,
        )
        db.add(enrollment)
        db.commit()
        db.refresh(enrollment)
        return {"status": "enrolled", "record": enrollment}
    else:
        # Class full — add to waitlist
        waitlist_entry = WaitlistEntry(
            class_id=class_id,
            dodid=dodid,
            last_name=last_name.strip().upper(),
            first_name=first_name.strip().upper(),
            rank=rank.strip().upper(),
            unit=unit.strip().upper(),
            request_date=date.today(),
            priority=0,
            status="WAITING",
        )
        db.add(waitlist_entry)
        db.commit()
        db.refresh(waitlist_entry)
        return {"status": "waitlisted", "record": waitlist_entry}


def promote_waitlist(class_id: int, db: Session) -> list[dict]:
    """Move top waitlisted students to enrolled when seats are available.

    Promotes by priority (desc), then by request_date (asc — FIFO).
    Returns list of promoted students.
    """
    availability = get_class_availability(class_id, db)
    seats_open = availability["seats_remaining"]
    if seats_open <= 0:
        return []

    # Get waiting entries sorted by priority desc, then request_date asc
    waiting = (
        db.query(WaitlistEntry)
        .filter(WaitlistEntry.class_id == class_id, WaitlistEntry.status == "WAITING")
        .order_by(WaitlistEntry.priority.desc(), WaitlistEntry.request_date.asc())
        .limit(seats_open)
        .all()
    )

    promoted = []
    current_enrolled = (
        db.query(Enrollment)
        .filter(Enrollment.class_id == class_id, Enrollment.status == "ENROLLED")
        .count()
    )

    for entry in waiting:
        current_enrolled += 1
        enrollment = Enrollment(
            class_id=class_id,
            dodid=entry.dodid,
            last_name=entry.last_name,
            first_name=entry.first_name,
            rank=entry.rank,
            unit=entry.unit,
            enrollment_date=date.today(),
            status="ENROLLED",
            seat_number=current_enrolled,
        )
        db.add(enrollment)
        entry.status = "PROMOTED"
        promoted.append({
            "dodid": entry.dodid,
            "last_name": entry.last_name,
            "first_name": entry.first_name,
            "rank": entry.rank,
        })

    db.commit()
    return promoted


def get_enrollment_stats(db: Session) -> dict:
    """Overall enrollment statistics across all classes.

    Returns total_classes, total_enrolled, total_waitlisted, avg_fill_rate.
    """
    total_classes = db.query(TrainingClass).count()
    active_classes = (
        db.query(TrainingClass)
        .filter(TrainingClass.status.in_(["SCHEDULED", "IN_PROGRESS"]))
        .count()
    )
    total_enrolled = (
        db.query(Enrollment)
        .filter(Enrollment.status == "ENROLLED")
        .count()
    )
    total_waitlisted = (
        db.query(WaitlistEntry)
        .filter(WaitlistEntry.status == "WAITING")
        .count()
    )

    # Calculate average fill rate for active/scheduled classes
    active = (
        db.query(TrainingClass)
        .filter(TrainingClass.status.in_(["SCHEDULED", "IN_PROGRESS"]))
        .all()
    )
    fill_rates = []
    for tc in active:
        enrolled = (
            db.query(Enrollment)
            .filter(Enrollment.class_id == tc.class_id, Enrollment.status == "ENROLLED")
            .count()
        )
        if tc.max_seats > 0:
            fill_rates.append(enrolled / tc.max_seats * 100)

    avg_fill_rate = round(sum(fill_rates) / len(fill_rates), 1) if fill_rates else 0.0

    return {
        "total_classes": total_classes,
        "active_classes": active_classes,
        "total_enrolled": total_enrolled,
        "total_waitlisted": total_waitlisted,
        "avg_fill_rate": avg_fill_rate,
    }


def get_student_enrollments(dodid: str, db: Session) -> list[dict]:
    """Return all classes a student is enrolled in."""
    enrollments = (
        db.query(Enrollment)
        .filter(Enrollment.dodid == dodid)
        .all()
    )
    results = []
    for e in enrollments:
        tc = db.query(TrainingClass).filter(TrainingClass.class_id == e.class_id).first()
        results.append({
            "enrollment_id": e.id,
            "class_id": e.class_id,
            "class_name": tc.class_name if tc else "Unknown",
            "course_id": tc.course_id if tc else "Unknown",
            "start_date": tc.start_date.isoformat() if tc else "",
            "end_date": tc.end_date.isoformat() if tc else "",
            "location": tc.location if tc else "",
            "enrollment_status": e.status,
            "seat_number": e.seat_number,
        })
    return results
