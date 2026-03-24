"""Training Readiness Tracker — database models and business logic."""

from __future__ import annotations

from contextlib import contextmanager
from datetime import UTC, date, datetime
from pathlib import Path

from sqlalchemy import (
    CheckConstraint,
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
    text,
)
from sqlalchemy.orm import (
    Session,
    relationship,
)

from shared.audit_mixin import AuditMixin
from shared.database import Base, create_app_engine, create_session_factory

# ---------------------------------------------------------------------------
# Database path — sits next to this file; *.db is gitignored
# ---------------------------------------------------------------------------
DB_PATH = Path(__file__).parent / "readiness_tracker.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_app_engine("readiness_tracker")

SessionLocal = create_session_factory(engine)


# ---------------------------------------------------------------------------
# ORM models
# ---------------------------------------------------------------------------
class Trainee(Base, AuditMixin):
    __tablename__ = "trainees"

    dodid = Column(String(10), primary_key=True)
    last_name = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    rank = Column(String(10), nullable=False)
    unit = Column(String(50), nullable=False)
    mos = Column(String(10), nullable=True)

    completions = relationship(
        "Completion", back_populates="trainee", cascade="all, delete-orphan"
    )


class Course(Base):
    __tablename__ = "courses"

    course_id = Column(String(10), primary_key=True)
    name = Column(String(100), nullable=False)
    hours = Column(Integer, nullable=False)


class Completion(Base, AuditMixin):
    __tablename__ = "completions"
    __table_args__ = (
        UniqueConstraint("dodid", "course_id", name="uq_trainee_course"),
        CheckConstraint("result IN ('GO', 'NO_GO')", name="ck_completion_result"),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    dodid = Column(String(10), ForeignKey("trainees.dodid"), nullable=False, index=True)
    course_id = Column(String(10), ForeignKey("courses.course_id"), nullable=False, index=True)
    result = Column(String(5), nullable=False)  # GO or NO_GO
    evaluation_date = Column(Date, nullable=False)
    evaluator_name = Column(String(100), nullable=True)

    trainee = relationship("Trainee", back_populates="completions")


# ---------------------------------------------------------------------------
# Prereq chain — authoritative source of truth
# ---------------------------------------------------------------------------
PREREQ_CHAIN: dict[str, list[str]] = {
    "TM-10": [],
    "TM-20": ["TM-10"],
    "TM-30": ["TM-20"],
    "FBC": ["TM-20"],  # parallel track; does NOT grant TM-30 credit
    # WFF tracks (A–F) — all require TM-30
    "TM-40A": ["TM-30"],
    "TM-40B": ["TM-30"],
    "TM-40C": ["TM-30"],
    "TM-40D": ["TM-30"],
    "TM-40E": ["TM-30"],
    "TM-40F": ["TM-30"],
    # Specialist tracks (G–O) — all require TM-30
    "TM-40G": ["TM-30"],
    "TM-40H": ["TM-30"],
    "TM-40M": ["TM-30"],
    "TM-40J": ["TM-30"],
    "TM-40K": ["TM-30"],
    "TM-40L": ["TM-30"],
    "TM-40N": ["TM-30"],
    "TM-40O": ["TM-30"],
    # Advanced specialist (G–O only — NO TM-50A through TM-50F)
    "TM-50G": ["TM-40G"],
    "TM-50H": ["TM-40H"],
    "TM-50M": ["TM-40M"],
    "TM-50J": ["TM-40J"],
    "TM-50K": ["TM-40K"],
    "TM-50L": ["TM-40L"],
    "TM-50N": ["TM-40N"],
    "TM-50O": ["TM-40O"],
}

ALL_COURSES = list(PREREQ_CHAIN.keys())

# Course metadata (name, hours)
COURSE_CATALOG: dict[str, tuple[str, int]] = {
    "TM-10": ("Maven User", 8),
    "TM-20": ("Builder", 40),
    "TM-30": ("Advanced Builder", 40),
    "FBC": ("Foundry Bootcamp", 40),
    "TM-40A": ("Intelligence WFF", 24),
    "TM-40B": ("Fires WFF", 24),
    "TM-40C": ("Movement & Maneuver WFF", 24),
    "TM-40D": ("Sustainment WFF", 24),
    "TM-40E": ("Protection WFF", 24),
    "TM-40F": ("Mission Command WFF", 24),
    "TM-40G": ("ORSA", 40),
    "TM-40H": ("AI Engineer", 40),
    "TM-40M": ("ML Engineer", 40),
    "TM-40J": ("Program Manager", 24),
    "TM-40K": ("Knowledge Manager", 24),
    "TM-40L": ("Software Engineer", 40),
    "TM-40N": ("UI/UX Designer", 24),
    "TM-40O": ("Platform Engineer", 40),
    "TM-50G": ("Advanced ORSA", 40),
    "TM-50H": ("Advanced AI Engineer", 40),
    "TM-50M": ("Advanced ML Engineer", 40),
    "TM-50J": ("Advanced Program Manager", 40),
    "TM-50K": ("Advanced Knowledge Manager", 40),
    "TM-50L": ("Advanced Software Engineer", 40),
    "TM-50N": ("Advanced UI/UX Designer", 40),
    "TM-50O": ("Advanced Platform Engineer", 40),
}


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
    """Create tables and seed the courses catalog."""
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        existing = db.query(Course).count()
        if existing == 0:
            for cid, (name, hours) in COURSE_CATALOG.items():
                db.add(Course(course_id=cid, name=name, hours=hours))
            db.commit()
    finally:
        db.close()


def get_go_courses(dodid: str, db: Session) -> set[str]:
    """Return the set of course_ids where the trainee has a GO result."""
    rows = (
        db.query(Completion.course_id)
        .filter(Completion.dodid == dodid, Completion.result == "GO")
        .all()
    )
    return {r.course_id for r in rows}


def check_eligibility(
    dodid: str, target_course: str, db: Session
) -> tuple[bool, list[str]]:
    """Check whether *dodid* can take *target_course*.

    Returns (eligible, list_of_missing_prereqs).
    """
    if target_course not in PREREQ_CHAIN:
        return False, [f"Unknown course: {target_course}"]

    prereqs = PREREQ_CHAIN[target_course]
    if not prereqs:
        return True, []

    completed = get_go_courses(dodid, db)
    missing = [p for p in prereqs if p not in completed]
    return (len(missing) == 0), missing


def get_next_recommended(dodid: str, db: Session) -> list[str]:
    """Return courses the trainee is eligible for but hasn't completed (GO)."""
    completed = get_go_courses(dodid, db)
    recommended: list[str] = []
    for course_id, prereqs in PREREQ_CHAIN.items():
        if course_id in completed:
            continue
        if all(p in completed for p in prereqs):
            recommended.append(course_id)
    return recommended


def get_unit_rollup(db: Session, unit: str | None = None) -> list[dict]:
    """Aggregate completion counts per unit.

    If *unit* is provided, returns a single-element list for that unit.
    Otherwise returns all units.
    """
    query = db.query(Trainee)
    if unit:
        query = query.filter(Trainee.unit == unit)
    trainees = query.all()

    # Group trainees by unit
    units: dict[str, list[Trainee]] = {}
    for t in trainees:
        units.setdefault(t.unit, []).append(t)

    results = []
    for unit_name, members in sorted(units.items()):
        counts: dict[str, int] = {c: 0 for c in ALL_COURSES}
        for member in members:
            for comp in member.completions:
                if comp.result == "GO" and comp.course_id in counts:
                    counts[comp.course_id] += 1
        results.append(
            {
                "unit": unit_name,
                "total_trainees": len(members),
                "course_counts": counts,
            }
        )
    return results


# ---------------------------------------------------------------------------
# Advanced analytics
# ---------------------------------------------------------------------------

# Course tier classification for RAG heatmap
COURSE_TIERS = {
    "Foundation": ["TM-10", "TM-20", "TM-30"],
    "WFF (A-F)": ["TM-40A", "TM-40B", "TM-40C", "TM-40D", "TM-40E", "TM-40F"],
    "Specialist (G-O)": ["TM-40G", "TM-40H", "TM-40M", "TM-40J", "TM-40K", "TM-40L", "TM-40N", "TM-40O"],
    "Advanced (50)": ["TM-50G", "TM-50H", "TM-50J", "TM-50K", "TM-50L", "TM-50M", "TM-50N", "TM-50O"],
}


def get_rag_heatmap_data(db: Session) -> list[dict]:
    """Build RAG heatmap data: rows = units, columns = courses, cells = % complete.

    Returns list of dicts with keys: unit, course_id, total, go_count, pct, rag.
    RAG logic: GREEN >= 80%, AMBER >= 50%, RED < 50%.
    """
    trainees = db.query(Trainee).all()
    # Group by unit
    unit_members: dict[str, list[Trainee]] = {}
    for t in trainees:
        unit_members.setdefault(t.unit, []).append(t)

    results = []
    for unit_name, members in sorted(unit_members.items()):
        total = len(members)
        # Get all GO completions for this unit
        go_set: dict[str, set[str]] = {}  # course_id -> set of dodids with GO
        for m in members:
            for c in m.completions:
                if c.result == "GO":
                    go_set.setdefault(c.course_id, set()).add(m.dodid)

        for course_id in ALL_COURSES:
            if course_id == "FBC":
                continue
            go_count = len(go_set.get(course_id, set()))
            pct = round(go_count / total * 100, 1) if total else 0
            if pct >= 80:
                rag = "GREEN"
            elif pct >= 50:
                rag = "AMBER"
            else:
                rag = "RED"

            results.append({
                "unit": unit_name,
                "course_id": course_id,
                "total": total,
                "go_count": go_count,
                "pct": pct,
                "rag": rag,
            })
    return results


def get_bottleneck_analysis(db: Session) -> list[dict]:
    """Identify where soldiers are getting stuck in the prereq chain.

    For each course, counts how many soldiers have completed the prereqs
    but haven't completed (GO) this course yet. High numbers = bottleneck.
    """
    trainees = db.query(Trainee).all()

    # Build completion map per trainee
    trainee_go: dict[str, set[str]] = {}
    for t in trainees:
        trainee_go[t.dodid] = {c.course_id for c in t.completions if c.result == "GO"}

    results = []
    for course_id, prereqs in PREREQ_CHAIN.items():
        if course_id == "FBC":
            continue
        eligible_not_done = 0
        completed = 0
        for dodid, go_courses in trainee_go.items():
            has_prereqs = all(p in go_courses for p in prereqs)
            has_course = course_id in go_courses
            if has_course:
                completed += 1
            elif has_prereqs:
                eligible_not_done += 1

        results.append({
            "course_id": course_id,
            "completed": completed,
            "eligible_not_done": eligible_not_done,
            "total_trainees": len(trainees),
        })

    return results


def get_training_velocity(db: Session) -> list[dict]:
    """Count completions (GO) per month for velocity/throughput tracking."""
    completions = (
        db.query(Completion)
        .filter(Completion.result == "GO")
        .order_by(Completion.evaluation_date)
        .all()
    )

    buckets: dict[str, int] = {}
    for c in completions:
        key = c.evaluation_date.strftime("%Y-%m")
        buckets[key] = buckets.get(key, 0) + 1

    return [{"month": k, "completions": v} for k, v in sorted(buckets.items())]


def get_funnel_data(db: Session) -> list[dict]:
    """Training funnel: how many soldiers have reached each stage.

    Returns cumulative "at least completed X" counts in prereq chain order.
    """
    trainees = db.query(Trainee).all()
    total = len(trainees)

    trainee_go: dict[str, set[str]] = {}
    for t in trainees:
        trainee_go[t.dodid] = {c.course_id for c in t.completions if c.result == "GO"}

    # Foundation funnel stages
    stages = [
        ("TM-10", "TM-10: Maven User"),
        ("TM-20", "TM-20: Builder"),
        ("TM-30", "TM-30: Advanced Builder"),
    ]

    results = []
    for course_id, label in stages:
        count = sum(1 for go_courses in trainee_go.values() if course_id in go_courses)
        results.append({
            "stage": label,
            "count": count,
            "total": total,
            "pct": round(count / total * 100, 1) if total else 0,
        })

    # Any TM-40 completion
    tm40_count = sum(
        1 for go_courses in trainee_go.values()
        if any(c.startswith("TM-40") for c in go_courses)
    )
    results.append({
        "stage": "TM-40: Any Specialization",
        "count": tm40_count,
        "total": total,
        "pct": round(tm40_count / total * 100, 1) if total else 0,
    })

    # Any TM-50 completion
    tm50_count = sum(
        1 for go_courses in trainee_go.values()
        if any(c.startswith("TM-50") for c in go_courses)
    )
    results.append({
        "stage": "TM-50: Advanced",
        "count": tm50_count,
        "total": total,
        "pct": round(tm50_count / total * 100, 1) if total else 0,
    })

    return results


def get_unit_summary(db: Session) -> list[dict]:
    """Per-unit summary: total trainees, avg courses completed, furthest course."""
    trainees = db.query(Trainee).all()
    unit_members: dict[str, list[Trainee]] = {}
    for t in trainees:
        unit_members.setdefault(t.unit, []).append(t)

    results = []
    for unit_name, members in sorted(unit_members.items()):
        go_counts = []
        for m in members:
            go_counts.append(len([c for c in m.completions if c.result == "GO"]))

        avg_courses = sum(go_counts) / len(go_counts) if go_counts else 0
        max_courses = max(go_counts) if go_counts else 0

        results.append({
            "unit": unit_name,
            "total_trainees": len(members),
            "avg_courses": round(avg_courses, 1),
            "max_courses": max_courses,
            "zero_courses": sum(1 for c in go_counts if c == 0),
        })

    return results
