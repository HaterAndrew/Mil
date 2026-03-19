"""Instructor Certification Manager — database models and business logic."""

from __future__ import annotations

import sys
from datetime import UTC, date, datetime, timedelta
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
    create_engine,
    event,
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
DB_PATH = Path(__file__).parent / "instructor_manager.db"
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
class Instructor(Base):
    __tablename__ = "instructors"

    instructor_id = Column(String(10), primary_key=True)
    last_name = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    rank = Column(String(10), nullable=False)
    unit = Column(String(50), nullable=False)
    mos = Column(String(10), nullable=False)
    email = Column(String(100), nullable=True)
    phone = Column(String(20), nullable=True)
    status = Column(String(10), nullable=False, default="ACTIVE")  # ACTIVE/INACTIVE/TDY
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))

    certifications = relationship(
        "Certification", back_populates="instructor", cascade="all, delete-orphan"
    )
    teaching_history = relationship(
        "TeachingHistory", back_populates="instructor", cascade="all, delete-orphan"
    )


class Certification(Base):
    __tablename__ = "certifications"

    id = Column(Integer, primary_key=True, autoincrement=True)
    instructor_id = Column(
        String(10), ForeignKey("instructors.instructor_id"), nullable=False
    )
    course_id = Column(String(10), nullable=False)
    certified_date = Column(Date, nullable=False)
    expiration_date = Column(Date, nullable=False)
    certifying_authority = Column(String(100), nullable=True)
    status = Column(String(10), nullable=False, default="CURRENT")  # CURRENT/EXPIRED/PENDING
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))

    instructor = relationship("Instructor", back_populates="certifications")


class TeachingHistory(Base):
    __tablename__ = "teaching_history"

    id = Column(Integer, primary_key=True, autoincrement=True)
    instructor_id = Column(
        String(10), ForeignKey("instructors.instructor_id"), nullable=False
    )
    course_id = Column(String(10), nullable=False)
    event_date = Column(Date, nullable=False)
    location = Column(String(100), nullable=True)
    students_count = Column(Integer, nullable=True)
    rating = Column(String(20), nullable=True)  # EXCELLENT/SATISFACTORY/NEEDS_IMPROVEMENT
    notes = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))

    instructor = relationship("Instructor", back_populates="teaching_history")


# ---------------------------------------------------------------------------
# Course catalog — imported from readiness_tracker (single source of truth)
# ---------------------------------------------------------------------------
from readiness_tracker.db import COURSE_CATALOG, ALL_COURSES  # noqa: E402


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


def get_instructor_certifications(instructor_id: str, db: Session) -> list[Certification]:
    """Return all certifications for a given instructor."""
    return (
        db.query(Certification)
        .filter(Certification.instructor_id == instructor_id)
        .order_by(Certification.expiration_date)
        .all()
    )


def get_certified_instructors(course_id: str, db: Session) -> list[Instructor]:
    """Return instructors with a CURRENT certification for a given course."""
    return (
        db.query(Instructor)
        .join(Certification)
        .filter(
            Certification.course_id == course_id,
            Certification.status == "CURRENT",
        )
        .all()
    )


def get_expiring_certifications(days_ahead: int, db: Session) -> list[dict]:
    """Return certifications expiring within *days_ahead* days.

    Includes instructor details for display. Only considers CURRENT certs.
    """
    cutoff = date.today() + timedelta(days=days_ahead)
    rows = (
        db.query(Certification)
        .join(Instructor)
        .filter(
            Certification.status == "CURRENT",
            Certification.expiration_date <= cutoff,
            Certification.expiration_date >= date.today(),
        )
        .order_by(Certification.expiration_date)
        .all()
    )
    results = []
    for cert in rows:
        days_left = (cert.expiration_date - date.today()).days
        results.append({
            "cert_id": cert.id,
            "instructor_id": cert.instructor_id,
            "rank": cert.instructor.rank,
            "last_name": cert.instructor.last_name,
            "first_name": cert.instructor.first_name,
            "unit": cert.instructor.unit,
            "course_id": cert.course_id,
            "course_name": COURSE_CATALOG.get(cert.course_id, (cert.course_id, 0))[0],
            "expiration_date": cert.expiration_date.isoformat(),
            "days_remaining": days_left,
            # RAG: RED <30d, AMBER <60d, GREEN >=60d
            "rag": "RED" if days_left < 30 else ("AMBER" if days_left < 60 else "GREEN"),
        })
    return results


def get_instructor_load(db: Session) -> list[dict]:
    """Count teaching events per instructor in the last 90 days.

    Returns list sorted by event count descending for workload analysis.
    """
    cutoff = date.today() - timedelta(days=90)
    instructors = db.query(Instructor).filter(Instructor.status == "ACTIVE").all()

    results = []
    for inst in instructors:
        recent_events = [
            h for h in inst.teaching_history if h.event_date >= cutoff
        ]
        results.append({
            "instructor_id": inst.instructor_id,
            "rank": inst.rank,
            "last_name": inst.last_name,
            "first_name": inst.first_name,
            "unit": inst.unit,
            "event_count": len(recent_events),
            # Flag overloaded instructors (>5 events in 90 days)
            "overloaded": len(recent_events) > 5,
        })
    return sorted(results, key=lambda x: x["event_count"], reverse=True)


def get_coverage_matrix(db: Session) -> list[dict]:
    """For each course, count the number of CURRENT certified instructors.

    Used for gap analysis — courses with 0 instructors are critical gaps.
    RAG: GREEN >=3, AMBER >=1, RED = 0.
    """
    results = []
    for course_id, (course_name, hours) in COURSE_CATALOG.items():
        count = (
            db.query(Certification)
            .filter(
                Certification.course_id == course_id,
                Certification.status == "CURRENT",
            )
            .count()
        )
        if count >= 3:
            rag = "GREEN"
        elif count >= 1:
            rag = "AMBER"
        else:
            rag = "RED"

        results.append({
            "course_id": course_id,
            "course_name": course_name,
            "hours": hours,
            "certified_count": count,
            "rag": rag,
        })
    return results
