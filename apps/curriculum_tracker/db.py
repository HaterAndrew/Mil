"""Curriculum Tracker — database models and business logic.

Tracks curriculum document versions, review cycles, and content freshness
across the maven_training/ corpus. Supports the CURRICULUM_MAINTENANCE_SOP.
"""

from __future__ import annotations

import hashlib
import os
from datetime import UTC, date, datetime, timedelta
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

# ---------------------------------------------------------------------------
# Database path — sits next to this file; *.db is gitignored
# ---------------------------------------------------------------------------
DB_PATH = Path(__file__).parent / "curriculum_tracker.db"
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
class Document(Base):
    __tablename__ = "documents"

    doc_id = Column(Integer, primary_key=True, autoincrement=True)
    file_path = Column(String(500), unique=True, nullable=False)
    doc_type = Column(String(30), nullable=False)  # TM/SYLLABUS/EXERCISE/EXAM/DOCTRINE/ADMIN
    course_id = Column(String(10), nullable=True)  # which TM it belongs to
    title = Column(String(200), nullable=False)
    current_version = Column(String(20), default="1.0")
    last_modified = Column(DateTime, nullable=True)
    file_hash = Column(String(64), nullable=True)  # SHA-256
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))

    reviews = relationship(
        "ReviewCycle", back_populates="document", cascade="all, delete-orphan"
    )
    changes = relationship(
        "ChangeLog", back_populates="document", cascade="all, delete-orphan"
    )


class ReviewCycle(Base):
    __tablename__ = "review_cycles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    doc_id = Column(Integer, ForeignKey("documents.doc_id"), nullable=False, index=True)
    review_type = Column(String(30), nullable=False)  # SCHEDULED/AD_HOC/POST_EXERCISE
    reviewer_name = Column(String(100), nullable=False)
    review_date = Column(Date, nullable=False)
    status = Column(String(30), nullable=False)  # APPROVED/CHANGES_REQUIRED/IN_REVIEW/OVERDUE
    notes = Column(Text, nullable=True)
    next_review_date = Column(Date, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))

    document = relationship("Document", back_populates="reviews")


class ChangeLog(Base):
    __tablename__ = "change_log"

    id = Column(Integer, primary_key=True, autoincrement=True)
    doc_id = Column(Integer, ForeignKey("documents.doc_id"), nullable=False, index=True)
    change_date = Column(DateTime, nullable=False)
    previous_hash = Column(String(64), nullable=True)
    new_hash = Column(String(64), nullable=True)
    change_summary = Column(Text, nullable=True)
    changed_by = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))

    document = relationship("Document", back_populates="changes")


# ---------------------------------------------------------------------------
# Doc type classification — maps path fragments to doc_type
# ---------------------------------------------------------------------------
DOC_TYPE_MAP: dict[str, str] = {
    "tm/": "TM",
    "syllabi/": "SYLLABUS",
    "exercises/EX": "EXERCISE",
    "exercises/exams/": "EXAM",
    "doctrine/": "DOCTRINE",
    "training_management/": "ADMIN",
    "quick_reference/": "DOCTRINE",
    "standards/": "ADMIN",
    "source_material/": "ADMIN",
}


def _classify_doc_type(rel_path: str) -> str:
    """Determine doc_type from the relative file path."""
    for pattern, doc_type in DOC_TYPE_MAP.items():
        if pattern in rel_path:
            return doc_type
    return "ADMIN"


def _extract_course_id(rel_path: str) -> str | None:
    """Extract the TM course ID from a file path (e.g., TM_40G -> TM-40G)."""
    # Match patterns like TM_10, TM_20, TM_30, TM_40A, TM_50G, etc.
    import re
    match = re.search(r"TM[_-](\d{2}[A-Z]?)", rel_path, re.IGNORECASE)
    if match:
        suffix = match.group(1).upper()
        return f"TM-{suffix}"
    # Check for syllabus references (e.g., SYLLABUS_TM10)
    match = re.search(r"SYLLABUS[_-]TM(\d{2}[A-Z]?)", rel_path, re.IGNORECASE)
    if match:
        suffix = match.group(1).upper()
        return f"TM-{suffix}"
    return None


def _extract_title(file_path: str) -> str:
    """Derive a human-readable title from the file name."""
    name = Path(file_path).stem
    # Replace underscores with spaces, title-case
    return name.replace("_", " ").strip()


def _compute_sha256(filepath: str) -> str:
    """Compute SHA-256 hash of file contents."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


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
def scan_directory(base_path: str, db: Session) -> dict[str, int]:
    """Walk maven_training/, hash .md files, upsert Documents, log changes.

    Returns counts: {"new": N, "changed": N, "unchanged": N}.
    """
    base = Path(base_path)
    if not base.exists():
        return {"new": 0, "changed": 0, "unchanged": 0}

    counts = {"new": 0, "changed": 0, "unchanged": 0}

    for root, _dirs, files in os.walk(base):
        for fname in files:
            if not fname.endswith(".md"):
                continue

            full_path = os.path.join(root, fname)
            # Store path relative to repo root for portability
            rel_path = os.path.relpath(full_path, base.parent)
            file_hash = _compute_sha256(full_path)
            mod_time = datetime.fromtimestamp(
                os.path.getmtime(full_path), tz=UTC
            )

            existing = (
                db.query(Document)
                .filter(Document.file_path == rel_path)
                .first()
            )

            if existing is None:
                # New document
                doc = Document(
                    file_path=rel_path,
                    doc_type=_classify_doc_type(rel_path),
                    course_id=_extract_course_id(rel_path),
                    title=_extract_title(fname),
                    file_hash=file_hash,
                    last_modified=mod_time,
                )
                db.add(doc)
                db.flush()  # get doc_id

                # Initial changelog entry
                db.add(ChangeLog(
                    doc_id=doc.doc_id,
                    change_date=mod_time,
                    previous_hash=None,
                    new_hash=file_hash,
                    change_summary="Initial scan — document discovered",
                ))
                counts["new"] += 1

            elif existing.file_hash != file_hash:
                # Changed document
                db.add(ChangeLog(
                    doc_id=existing.doc_id,
                    change_date=mod_time,
                    previous_hash=existing.file_hash,
                    new_hash=file_hash,
                    change_summary="Content changed since last scan",
                ))
                existing.file_hash = file_hash
                existing.last_modified = mod_time
                counts["changed"] += 1

            else:
                counts["unchanged"] += 1

    db.commit()
    return counts


def get_stale_documents(days: int, db: Session) -> list[Document]:
    """Return documents not reviewed in the last N days."""
    cutoff = datetime.now(UTC) - timedelta(days=days)

    # Subquery: latest review date per doc
    from sqlalchemy import case

    # Documents with no reviews, or whose latest review is older than cutoff
    reviewed_docs = (
        db.query(
            ReviewCycle.doc_id,
            func.max(ReviewCycle.review_date).label("latest_review"),
        )
        .group_by(ReviewCycle.doc_id)
        .subquery()
    )

    # Docs never reviewed
    never_reviewed = (
        db.query(Document)
        .outerjoin(ReviewCycle, Document.doc_id == ReviewCycle.doc_id)
        .filter(ReviewCycle.id.is_(None))
        .all()
    )

    # Docs whose latest review is before the cutoff
    stale_reviewed = (
        db.query(Document)
        .join(reviewed_docs, Document.doc_id == reviewed_docs.c.doc_id)
        .filter(reviewed_docs.c.latest_review < cutoff.date())
        .all()
    )

    # Combine and deduplicate
    seen = set()
    result = []
    for doc in never_reviewed + stale_reviewed:
        if doc.doc_id not in seen:
            seen.add(doc.doc_id)
            result.append(doc)

    return result


def get_overdue_reviews(db: Session) -> list[ReviewCycle]:
    """Return reviews past their next_review_date that haven't been completed."""
    today = date.today()
    return (
        db.query(ReviewCycle)
        .filter(
            ReviewCycle.next_review_date.isnot(None),
            ReviewCycle.next_review_date < today,
            ReviewCycle.status.in_(["IN_REVIEW", "OVERDUE"]),
        )
        .all()
    )


def get_document_history(doc_id: int, db: Session) -> list[ChangeLog]:
    """Return all changelog entries for a given document, newest first."""
    return (
        db.query(ChangeLog)
        .filter(ChangeLog.doc_id == doc_id)
        .order_by(ChangeLog.change_date.desc())
        .all()
    )


def get_review_summary(db: Session) -> dict[str, int]:
    """Count reviews by status: APPROVED, CHANGES_REQUIRED, IN_REVIEW, OVERDUE."""
    rows = (
        db.query(ReviewCycle.status, func.count(ReviewCycle.id))
        .group_by(ReviewCycle.status)
        .all()
    )
    result = {"APPROVED": 0, "CHANGES_REQUIRED": 0, "IN_REVIEW": 0, "OVERDUE": 0}
    for status, count in rows:
        result[status] = count
    return result


def get_freshness_report(db: Session) -> list[dict]:
    """For each doc_type, compute avg days since last review.

    Returns list of dicts: {"doc_type", "doc_count", "avg_days_since_review",
    "never_reviewed"}.
    """
    today = date.today()
    docs = db.query(Document).all()

    # Group by doc_type
    type_groups: dict[str, list[Document]] = {}
    for doc in docs:
        type_groups.setdefault(doc.doc_type, []).append(doc)

    results = []
    for doc_type, group_docs in sorted(type_groups.items()):
        days_list = []
        never_reviewed = 0

        for doc in group_docs:
            # Find latest review for this doc
            latest = (
                db.query(func.max(ReviewCycle.review_date))
                .filter(ReviewCycle.doc_id == doc.doc_id)
                .scalar()
            )
            if latest:
                delta = (today - latest).days
                days_list.append(delta)
            else:
                never_reviewed += 1

        avg_days = round(sum(days_list) / len(days_list), 1) if days_list else None

        results.append({
            "doc_type": doc_type,
            "doc_count": len(group_docs),
            "avg_days_since_review": avg_days,
            "never_reviewed": never_reviewed,
        })

    return results
