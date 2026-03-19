"""AAR Aggregator — database models, file parser, and analytics helpers."""

from __future__ import annotations

import enum
import re
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
from sqlalchemy.types import JSON

# ---------------------------------------------------------------------------
# Database
# ---------------------------------------------------------------------------
DB_PATH = Path(__file__).parent / "aar_aggregator.db"
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
# WFF categories
# ---------------------------------------------------------------------------
class WFFCategory(str, enum.Enum):
    INTELLIGENCE = "INTELLIGENCE"
    FIRES = "FIRES"
    MOVEMENT_MANEUVER = "MOVEMENT_MANEUVER"
    SUSTAINMENT = "SUSTAINMENT"
    PROTECTION = "PROTECTION"
    MISSION_COMMAND = "MISSION_COMMAND"


WFF_VALUES = [c.value for c in WFFCategory]


# ---------------------------------------------------------------------------
# ORM models
# ---------------------------------------------------------------------------
class AAR(Base):
    __tablename__ = "aars"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    tm_levels = Column(JSON, nullable=False)          # ["TM-10", "TM-20"]
    exercises = Column(JSON, nullable=True)            # ["EX_10"]
    location = Column(String(200), nullable=False)
    student_count = Column(Integer, nullable=False)
    instructor_names = Column(JSON, nullable=False)    # ["MAJ SMITH"]
    planned_objectives = Column(Text, nullable=False)
    actual_execution = Column(Text, nullable=False)
    instructor_recommendations = Column(Text, nullable=True)
    submitted_by = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))

    sustains = relationship("SustainItem", back_populates="aar", cascade="all, delete-orphan")
    improves = relationship("ImproveItem", back_populates="aar", cascade="all, delete-orphan")
    evaluations = relationship("StudentEvaluation", back_populates="aar", cascade="all, delete-orphan")
    discrepancies = relationship("CurriculumDiscrepancy", back_populates="aar", cascade="all, delete-orphan")
    env_issues = relationship("EnvironmentIssue", back_populates="aar", cascade="all, delete-orphan")


class SustainItem(Base):
    __tablename__ = "sustain_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    aar_id = Column(Integer, ForeignKey("aars.id"), nullable=False)
    item_text = Column(Text, nullable=False)

    aar = relationship("AAR", back_populates="sustains")


class ImproveItem(Base):
    __tablename__ = "improve_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    aar_id = Column(Integer, ForeignKey("aars.id"), nullable=False)
    problem = Column(Text, nullable=False)
    proposed_fix = Column(Text, nullable=True)
    owner = Column(String(100), nullable=True)
    priority = Column(String(1), nullable=False)   # H, M, L
    category = Column(String(20), nullable=True)    # WFF category

    aar = relationship("AAR", back_populates="improves")


class StudentEvaluation(Base):
    __tablename__ = "student_evaluations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    aar_id = Column(Integer, ForeignKey("aars.id"), nullable=False)
    trainee_name = Column(String(100), nullable=False)
    tm_level = Column(String(10), nullable=False)
    result = Column(String(5), nullable=False)  # GO or NO_GO
    notes = Column(Text, nullable=True)

    aar = relationship("AAR", back_populates="evaluations")


class CurriculumDiscrepancy(Base):
    __tablename__ = "curriculum_discrepancies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    aar_id = Column(Integer, ForeignKey("aars.id"), nullable=False)
    document = Column(String(200), nullable=False)
    section_page = Column(String(100), nullable=False)
    issue_description = Column(Text, nullable=False)
    severity = Column(String(1), nullable=False)  # H, M, L

    aar = relationship("AAR", back_populates="discrepancies")


class EnvironmentIssue(Base):
    __tablename__ = "environment_issues"

    id = Column(Integer, primary_key=True, autoincrement=True)
    aar_id = Column(Integer, ForeignKey("aars.id"), nullable=False)
    issue = Column(Text, nullable=False)
    impact = Column(Text, nullable=False)
    resolution = Column(Text, nullable=True)

    aar = relationship("AAR", back_populates="env_issues")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    Base.metadata.create_all(bind=engine)


def find_recurring_issues(
    db: Session,
    min_count: int = 2,
    date_from: date | None = None,
    date_to: date | None = None,
) -> list[dict]:
    """Find improve_item problems that recur across multiple AARs."""
    query = db.query(ImproveItem).join(AAR)
    if date_from:
        query = query.filter(AAR.date >= date_from)
    if date_to:
        query = query.filter(AAR.date <= date_to)

    items = query.all()

    # Normalize and group by lowercased problem text
    groups: dict[str, list[dict]] = {}
    for item in items:
        key = item.problem.strip().lower()
        groups.setdefault(key, []).append({
            "aar_id": item.aar_id,
            "problem": item.problem,
            "category": item.category,
            "priority": item.priority,
            "date": item.aar.date.isoformat() if item.aar else None,
        })

    recurring = []
    for key, occurrences in groups.items():
        if len(occurrences) >= min_count:
            recurring.append({
                "problem": occurrences[0]["problem"],
                "count": len(occurrences),
                "aar_ids": [o["aar_id"] for o in occurrences],
                "dates": [o["date"] for o in occurrences],
                "category": occurrences[0].get("category"),
                "priority": occurrences[0].get("priority"),
            })

    return sorted(recurring, key=lambda x: x["count"], reverse=True)


def trend_by_category(
    db: Session,
    date_from: date | None = None,
    date_to: date | None = None,
) -> dict[str, int]:
    """Count improve items by WFF category within date range."""
    query = db.query(ImproveItem.category, func.count(ImproveItem.id)).join(AAR)
    if date_from:
        query = query.filter(AAR.date >= date_from)
    if date_to:
        query = query.filter(AAR.date <= date_to)

    rows = query.group_by(ImproveItem.category).all()
    return {cat or "UNCATEGORIZED": cnt for cat, cnt in rows}


def trend_over_time(
    db: Session,
    date_from: date | None = None,
    date_to: date | None = None,
) -> list[dict]:
    """Count improve items bucketed by month."""
    query = db.query(AAR).options()
    if date_from:
        query = query.filter(AAR.date >= date_from)
    if date_to:
        query = query.filter(AAR.date <= date_to)

    aars = query.order_by(AAR.date).all()

    # Bucket by year-month
    buckets: dict[str, int] = {}
    for aar in aars:
        key = aar.date.strftime("%Y-%m")
        buckets[key] = buckets.get(key, 0) + len(aar.improves)

    return [{"month": k, "improve_count": v} for k, v in sorted(buckets.items())]


def priority_matrix(db: Session) -> list[dict]:
    """Build a frequency-vs-severity priority matrix for improve items.

    Groups problems, counts frequency, and maps severity. Useful for
    identifying which issues need immediate attention (high freq + high severity).
    """
    items = db.query(ImproveItem).join(AAR).all()

    # Group by normalized problem text
    groups: dict[str, dict] = {}
    for item in items:
        key = item.problem.strip().lower()
        if key not in groups:
            groups[key] = {
                "problem": item.problem,
                "count": 0,
                "priorities": [],
                "categories": [],
                "aar_ids": [],
            }
        groups[key]["count"] += 1
        groups[key]["priorities"].append(item.priority)
        if item.category:
            groups[key]["categories"].append(item.category)
        groups[key]["aar_ids"].append(item.aar_id)

    results = []
    for key, data in groups.items():
        # Severity score: H=3, M=2, L=1; take the max
        severity_map = {"H": 3, "M": 2, "L": 1}
        max_severity = max(severity_map.get(p, 1) for p in data["priorities"])
        dominant_priority = {3: "H", 2: "M", 1: "L"}[max_severity]

        results.append({
            "problem": data["problem"],
            "frequency": data["count"],
            "severity_score": max_severity,
            "priority": dominant_priority,
            "category": data["categories"][0] if data["categories"] else None,
            "aar_ids": list(set(data["aar_ids"])),
        })

    return sorted(results, key=lambda x: (x["severity_score"] * x["frequency"]), reverse=True)


def keyword_frequency(db: Session, top_n: int = 20) -> list[dict]:
    """Extract most frequent keywords from improve item problem descriptions.

    Filters out common stop words to surface meaningful terms.
    """
    stop_words = {
        "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
        "of", "with", "by", "is", "was", "are", "were", "been", "be", "have",
        "has", "had", "do", "does", "did", "will", "would", "could", "should",
        "may", "might", "must", "shall", "can", "need", "not", "no", "all",
        "it", "its", "this", "that", "these", "those", "from", "into", "out",
        "up", "down", "off", "over", "under", "again", "further", "then",
        "once", "here", "there", "when", "where", "why", "how", "each",
        "few", "more", "most", "other", "some", "such", "than", "too",
        "very", "just", "about", "above", "after", "before", "between",
        "during", "through", "while", "so", "if", "as", "until",
    }

    items = db.query(ImproveItem).all()
    word_counts: Counter = Counter()

    for item in items:
        words = re.findall(r'[a-z]+', item.problem.lower())
        meaningful = [w for w in words if w not in stop_words and len(w) > 2]
        word_counts.update(meaningful)

    return [{"word": word, "count": count}
            for word, count in word_counts.most_common(top_n)]


def go_nogo_trend(db: Session) -> list[dict]:
    """Track GO/NO_GO pass rates from student evaluations over time."""
    aars = db.query(AAR).order_by(AAR.date).all()

    results = []
    for aar in aars:
        if not aar.evaluations:
            continue
        total = len(aar.evaluations)
        go = sum(1 for e in aar.evaluations if e.result == "GO")
        nogo = total - go

        results.append({
            "aar_id": aar.id,
            "date": aar.date.isoformat(),
            "tm_level": aar.tm_levels[0] if aar.tm_levels else "Unknown",
            "total_evaluated": total,
            "go_count": go,
            "nogo_count": nogo,
            "go_rate": round(go / total * 100, 1) if total else 0,
        })

    return results


def category_cooccurrence(db: Session) -> list[dict]:
    """Find which WFF categories co-occur within the same AARs.

    Reveals correlated problem areas — e.g., MISSION_COMMAND issues
    often appear alongside PROTECTION issues.
    """
    aars = db.query(AAR).all()

    pair_counts: Counter = Counter()
    for aar in aars:
        categories = set()
        for item in aar.improves:
            if item.category:
                categories.add(item.category)

        # Generate all pairs
        cat_list = sorted(categories)
        for i in range(len(cat_list)):
            for j in range(i + 1, len(cat_list)):
                pair_counts[(cat_list[i], cat_list[j])] += 1

    results = []
    for (cat_a, cat_b), count in pair_counts.most_common():
        if count >= 1:
            results.append({
                "category_a": cat_a,
                "category_b": cat_b,
                "co_occurrences": count,
            })

    return results


def aar_summary_stats(db: Session) -> dict:
    """High-level summary stats across all AARs."""
    aars = db.query(AAR).all()
    if not aars:
        return {"total_aars": 0}

    total_students = sum(a.student_count for a in aars)
    total_sustains = sum(len(a.sustains) for a in aars)
    total_improves = sum(len(a.improves) for a in aars)
    total_evals = sum(len(a.evaluations) for a in aars)
    total_discs = sum(len(a.discrepancies) for a in aars)

    go_count = sum(1 for a in aars for e in a.evaluations if e.result == "GO")
    total_eval = sum(len(a.evaluations) for a in aars)
    overall_go_rate = round(go_count / total_eval * 100, 1) if total_eval else 0

    # TM level breakdown
    tm_counts: Counter = Counter()
    for a in aars:
        for tm in a.tm_levels:
            tm_counts[tm] += 1

    return {
        "total_aars": len(aars),
        "total_students_trained": total_students,
        "total_sustains": total_sustains,
        "total_improves": total_improves,
        "total_evaluations": total_evals,
        "total_discrepancies": total_discs,
        "overall_go_rate": overall_go_rate,
        "tm_level_counts": dict(tm_counts.most_common()),
        "date_range": {
            "earliest": min(a.date for a in aars).isoformat(),
            "latest": max(a.date for a in aars).isoformat(),
        },
    }


# ---------------------------------------------------------------------------
# File parser — AAR template format
# ---------------------------------------------------------------------------
def parse_aar_file(content: str) -> dict:
    """Parse a markdown AAR file matching the template structure.

    Returns a dict suitable for creating an AAR via the API.
    This is best-effort — human review is expected before saving.
    """
    lines = content.splitlines()
    sections: dict[str, list[str]] = {}
    current_section = "HEADER"

    # Section header patterns
    section_patterns = [
        (r"(?i)section\s*1.*event\s*detail", "EVENT_DETAILS"),
        (r"(?i)section\s*2.*planned", "PLANNED"),
        (r"(?i)section\s*3.*happened", "HAPPENED"),
        (r"(?i)section\s*4.*sustain", "SUSTAIN"),
        (r"(?i)section\s*5.*improve", "IMPROVE"),
        (r"(?i)section\s*6.*go.?no.?go", "EVALUATIONS"),
        (r"(?i)section\s*7.*discrepan", "DISCREPANCIES"),
        (r"(?i)section\s*8.*environment", "ENVIRONMENT"),
        (r"(?i)section\s*9.*recommend", "RECOMMENDATIONS"),
        (r"(?i)section\s*10.*sign", "SIGNOFF"),
    ]

    for line in lines:
        stripped = line.strip()
        # Check if line is a section header
        matched = False
        for pattern, section_name in section_patterns:
            if re.search(pattern, stripped):
                current_section = section_name
                sections.setdefault(current_section, [])
                matched = True
                break
        if not matched and stripped:
            sections.setdefault(current_section, []).append(stripped)

    def extract_field(section_lines: list[str], field: str) -> str:
        """Extract a field value like 'Date: 2026-01-15'."""
        for line in section_lines:
            if line.lower().startswith(field.lower()):
                return line.split(":", 1)[-1].strip()
        return ""

    def extract_list_items(section_lines: list[str]) -> list[str]:
        """Extract bullet/numbered items."""
        items = []
        for line in section_lines:
            cleaned = re.sub(r"^[\-\*\d\.]+\s*", "", line).strip()
            if cleaned:
                items.append(cleaned)
        return items

    # Build result
    event_lines = sections.get("EVENT_DETAILS", [])
    date_str = extract_field(event_lines, "date")

    # Try to parse TM levels
    tm_levels = []
    for line in event_lines:
        found = re.findall(r"TM-\d{2}[A-L]?", line, re.IGNORECASE)
        tm_levels.extend(found)
    tm_levels = list(set(tm_levels)) or ["TM-10"]

    # Exercises
    exercises = []
    for line in event_lines:
        found = re.findall(r"EX_\d{2}[A-LM]?", line, re.IGNORECASE)
        exercises.extend(found)
    exercises = list(set(exercises))

    location = extract_field(event_lines, "location") or "Unknown"

    student_count_str = extract_field(event_lines, "number of student") or extract_field(event_lines, "students")
    try:
        student_count = int(re.search(r"\d+", student_count_str).group()) if student_count_str else 1
    except (AttributeError, ValueError):
        student_count = 1

    instructor_str = extract_field(event_lines, "instructor")
    instructor_names = [n.strip() for n in instructor_str.split(",") if n.strip()] if instructor_str else ["Unknown"]

    planned = "\n".join(sections.get("PLANNED", ["No objectives recorded."]))
    happened = "\n".join(sections.get("HAPPENED", ["No execution details recorded."]))

    sustains = extract_list_items(sections.get("SUSTAIN", []))
    if not sustains:
        sustains = ["No sustain items recorded."]

    # Parse improve items
    improve_lines = sections.get("IMPROVE", [])
    improves = []
    for line in improve_lines:
        cleaned = re.sub(r"^[\-\*\d\.]+\s*", "", line).strip()
        if cleaned:
            improves.append({
                "problem": cleaned,
                "proposed_fix": None,
                "owner": None,
                "priority": "M",
                "category": None,
            })

    recommendations = "\n".join(sections.get("RECOMMENDATIONS", [""]))

    # Sign-off
    signoff = sections.get("SIGNOFF", [])
    submitted_by = extract_field(signoff, "instructor") or extract_field(signoff, "submitted") or "Unknown"

    result = {
        "date": date_str or datetime.now(UTC).strftime("%Y-%m-%d"),
        "tm_levels": tm_levels,
        "exercises": exercises,
        "location": location,
        "student_count": student_count,
        "instructor_names": instructor_names,
        "planned_objectives": planned,
        "actual_execution": happened,
        "sustains": sustains,
        "improves": improves,
        "evaluations": [],
        "discrepancies": [],
        "env_issues": [],
        "instructor_recommendations": recommendations or None,
        "submitted_by": submitted_by,
    }

    return result
