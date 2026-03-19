"""Lessons Learned Pipeline — database models and business logic."""

from __future__ import annotations

from collections import Counter
from datetime import UTC, date, datetime
from pathlib import Path

from sqlalchemy import (
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
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
DB_PATH = Path(__file__).parent / "lessons_learned.db"
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
class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    source_type = Column(String(30), nullable=False)  # AAR/EXERCISE/FIELD_OBSERVATION/STUDENT_FEEDBACK/INSTRUCTOR_NOTE
    source_reference = Column(String(200), nullable=True)  # e.g., "AAR-2026-042"
    submitted_by = Column(String(100), nullable=False)
    submit_date = Column(Date, nullable=False)
    status = Column(String(20), nullable=False, default="NEW")  # NEW/VALIDATED/ACTIONABLE/IMPLEMENTED/ARCHIVED
    priority = Column(String(10), nullable=False, default="MEDIUM")  # HIGH/MEDIUM/LOW
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))

    tags = relationship("LessonTag", back_populates="lesson", cascade="all, delete-orphan")
    action_items = relationship("ActionItem", back_populates="lesson", cascade="all, delete-orphan")
    comments = relationship("LessonComment", back_populates="lesson", cascade="all, delete-orphan")


class LessonTag(Base):
    __tablename__ = "lesson_tags"
    __table_args__ = (
        UniqueConstraint("lesson_id", "tag_type", "tag_value", name="uq_lesson_tag"),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"), nullable=False)
    tag_type = Column(String(30), nullable=False)  # TTP_CATEGORY/ECHELON/WFF/DOCTRINE_REF/COURSE_ID/KEYWORD
    tag_value = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))

    lesson = relationship("Lesson", back_populates="tags")


class ActionItem(Base):
    __tablename__ = "action_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"), nullable=False)
    description = Column(Text, nullable=False)
    assigned_to = Column(String(100), nullable=True)
    due_date = Column(Date, nullable=True)
    status = Column(String(20), nullable=False, default="OPEN")  # OPEN/IN_PROGRESS/COMPLETED/CANCELLED
    completed_date = Column(Date, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))

    lesson = relationship("Lesson", back_populates="action_items")


class LessonComment(Base):
    __tablename__ = "lesson_comments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"), nullable=False)
    author = Column(String(100), nullable=False)
    comment_text = Column(Text, nullable=False)
    comment_date = Column(DateTime, nullable=False, default=lambda: datetime.now(UTC))
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))

    lesson = relationship("Lesson", back_populates="comments")


# ---------------------------------------------------------------------------
# Tag taxonomy constants (TM-40K syllabus alignment)
# ---------------------------------------------------------------------------
SOURCE_TYPES = ["AAR", "EXERCISE", "FIELD_OBSERVATION", "STUDENT_FEEDBACK", "INSTRUCTOR_NOTE"]

STATUSES = ["NEW", "VALIDATED", "ACTIONABLE", "IMPLEMENTED", "ARCHIVED"]

PRIORITIES = ["HIGH", "MEDIUM", "LOW"]

TAG_TYPES = ["TTP_CATEGORY", "ECHELON", "WFF", "DOCTRINE_REF", "COURSE_ID", "KEYWORD"]

TTP_CATEGORIES = [
    "Data Collection",
    "Data Processing",
    "Visualization",
    "Analysis",
    "Dissemination",
    "Platform Administration",
    "Integration",
    "Quality Control",
]

ECHELONS = [
    "Squad",
    "Platoon",
    "Company",
    "Battalion",
    "Brigade",
    "Division",
    "Corps",
    "Theater",
]

WFF_CATEGORIES = [
    "Intelligence",
    "Fires",
    "Movement & Maneuver",
    "Sustainment",
    "Protection",
    "Mission Command",
    "Cross-Functional",
]

DOCTRINE_REFS = [
    "ADP 2-0",    # Intelligence
    "ADP 3-0",    # Operations
    "ADP 3-09",   # Fires
    "ADP 3-19",   # Fires (TASS)
    "ADP 3-37",   # Protection
    "ADP 3-90",   # Offense & Defense
    "ADP 4-0",    # Sustainment
    "ADP 5-0",    # The Operations Process
    "ADP 6-0",    # Mission Command
    "ADP 6-22",   # Army Leadership
    "ADRP 1-02",  # Terms & Symbols
    "ATP 2-01.3", # Intelligence Preparation of the Battlefield
]

ACTION_STATUSES = ["OPEN", "IN_PROGRESS", "COMPLETED", "CANCELLED"]


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
def get_lessons_by_tag(tag_type: str, tag_value: str, db: Session) -> list[Lesson]:
    """Filter lessons by a specific tag type and value."""
    return (
        db.query(Lesson)
        .join(LessonTag)
        .filter(LessonTag.tag_type == tag_type, LessonTag.tag_value == tag_value)
        .order_by(Lesson.submit_date.desc())
        .all()
    )


def get_tag_frequency(tag_type: str, db: Session) -> list[dict]:
    """Count of lessons per tag value for a given tag type.

    Returns list of dicts: {tag_value, count}.
    """
    rows = (
        db.query(LessonTag.tag_value, func.count(LessonTag.lesson_id))
        .filter(LessonTag.tag_type == tag_type)
        .group_by(LessonTag.tag_value)
        .order_by(func.count(LessonTag.lesson_id).desc())
        .all()
    )
    return [{"tag_value": row[0], "count": row[1]} for row in rows]


def get_trend_analysis(db: Session) -> list[dict]:
    """Lessons submitted per month, broken down by source type.

    Returns list of dicts: {month, source_type, count}.
    """
    lessons = db.query(Lesson).order_by(Lesson.submit_date).all()

    # Bucket by (year-month, source_type)
    buckets: dict[tuple[str, str], int] = {}
    for lesson in lessons:
        key = (lesson.submit_date.strftime("%Y-%m"), lesson.source_type)
        buckets[key] = buckets.get(key, 0) + 1

    return [
        {"month": k[0], "source_type": k[1], "count": v}
        for k, v in sorted(buckets.items())
    ]


def get_action_item_status(db: Session) -> dict[str, int]:
    """Count of action items by status."""
    rows = (
        db.query(ActionItem.status, func.count(ActionItem.id))
        .group_by(ActionItem.status)
        .all()
    )
    return {row[0]: row[1] for row in rows}


def get_cross_reference(tag_type_a: str, tag_type_b: str, db: Session) -> list[dict]:
    """Co-occurrence matrix between two tag types.

    Returns list of dicts: {tag_a, tag_b, count} for every pair that co-occurs
    on at least one lesson.
    """
    # Get all lessons that have both tag types
    lessons_with_a = (
        db.query(LessonTag.lesson_id, LessonTag.tag_value)
        .filter(LessonTag.tag_type == tag_type_a)
        .all()
    )
    lessons_with_b = (
        db.query(LessonTag.lesson_id, LessonTag.tag_value)
        .filter(LessonTag.tag_type == tag_type_b)
        .all()
    )

    # Build lookup: lesson_id -> set of tag values for each type
    a_map: dict[int, set[str]] = {}
    for lesson_id, tag_value in lessons_with_a:
        a_map.setdefault(lesson_id, set()).add(tag_value)

    b_map: dict[int, set[str]] = {}
    for lesson_id, tag_value in lessons_with_b:
        b_map.setdefault(lesson_id, set()).add(tag_value)

    # Count co-occurrences
    pairs: Counter[tuple[str, str]] = Counter()
    for lesson_id in set(a_map.keys()) & set(b_map.keys()):
        for a_val in a_map[lesson_id]:
            for b_val in b_map[lesson_id]:
                pairs[(a_val, b_val)] += 1

    return [
        {"tag_a": k[0], "tag_b": k[1], "count": v}
        for k, v in sorted(pairs.items())
    ]


def get_pipeline_stats(db: Session) -> dict:
    """Aggregate pipeline statistics.

    Returns dict with: total_lessons, by_status, by_priority, by_source_type.
    """
    total = db.query(Lesson).count()

    status_rows = (
        db.query(Lesson.status, func.count(Lesson.id))
        .group_by(Lesson.status)
        .all()
    )
    by_status = {row[0]: row[1] for row in status_rows}

    priority_rows = (
        db.query(Lesson.priority, func.count(Lesson.id))
        .group_by(Lesson.priority)
        .all()
    )
    by_priority = {row[0]: row[1] for row in priority_rows}

    source_rows = (
        db.query(Lesson.source_type, func.count(Lesson.id))
        .group_by(Lesson.source_type)
        .all()
    )
    by_source_type = {row[0]: row[1] for row in source_rows}

    return {
        "total_lessons": total,
        "by_status": by_status,
        "by_priority": by_priority,
        "by_source_type": by_source_type,
    }
