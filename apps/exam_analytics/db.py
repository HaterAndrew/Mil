"""Exam Analytics Dashboard — database models and analytics helpers."""

from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

from sqlalchemy import (
    Column,
    Date,
    DateTime,
    Float,
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
# Database
# ---------------------------------------------------------------------------
DB_PATH = Path(__file__).parent / "exam_analytics.db"
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
# Constants — exam structure (uniform across all courses)
# ---------------------------------------------------------------------------
EXAM_STRUCTURE = {
    "mc_count": 15,
    "mc_points": 2,
    "sa_count": 5,
    "sa_points": 6,
    "total_questions": 20,
    "total_possible": 60,
    "passing_percent": 70.0,
    "passing_score": 42,
}


# ---------------------------------------------------------------------------
# ORM models
# ---------------------------------------------------------------------------
class ExamSession(Base):
    __tablename__ = "exam_sessions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(String(10), nullable=False)   # e.g., "TM-40G"
    form_type = Column(String(4), nullable=False)     # PRE or POST
    administration_date = Column(Date, nullable=False)
    cohort_label = Column(String(100), nullable=False) # e.g., "TM-40G FY26 Q2"
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))

    results = relationship("ExamResult", back_populates="session", cascade="all, delete-orphan")


class ExamResult(Base):
    __tablename__ = "exam_results"
    __table_args__ = (
        UniqueConstraint("session_id", "trainee_id", name="uq_session_trainee"),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(Integer, ForeignKey("exam_sessions.id"), nullable=False)
    trainee_id = Column(String(100), nullable=False)  # DODID or name
    total_score = Column(Integer, nullable=False)
    total_possible = Column(Integer, nullable=False, default=60)
    score_percent = Column(Float, nullable=False)
    result = Column(String(10), nullable=False)  # PASS, FAIL, DIAGNOSTIC
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))

    session = relationship("ExamSession", back_populates="results")
    question_scores = relationship(
        "QuestionScore", back_populates="exam_result", cascade="all, delete-orphan"
    )


class QuestionScore(Base):
    __tablename__ = "question_scores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    result_id = Column(Integer, ForeignKey("exam_results.id"), nullable=False)
    question_number = Column(Integer, nullable=False)   # 1–20
    question_type = Column(String(2), nullable=False)    # MC or SA
    points_possible = Column(Integer, nullable=False)    # 2 for MC, 6 for SA
    points_awarded = Column(Integer, nullable=False)

    exam_result = relationship("ExamResult", back_populates="question_scores")


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


def compute_gain_scores(
    pre_session_id: int,
    post_session_id: int,
    db: Session,
) -> list[dict]:
    """Match trainees between PRE and POST sessions, compute gain scores."""
    pre_results = (
        db.query(ExamResult)
        .filter(ExamResult.session_id == pre_session_id)
        .all()
    )
    post_results = (
        db.query(ExamResult)
        .filter(ExamResult.session_id == post_session_id)
        .all()
    )

    post_by_trainee = {r.trainee_id: r for r in post_results}
    gains = []

    for pre in pre_results:
        post = post_by_trainee.get(pre.trainee_id)
        if not post:
            continue

        absolute = post.score_percent - pre.score_percent
        # Normalized gain: (post - pre) / (100 - pre); handle ceiling
        if pre.score_percent >= 100.0:
            normalized = 0.0
        else:
            normalized = (post.score_percent - pre.score_percent) / (100.0 - pre.score_percent) * 100.0

        gains.append({
            "trainee_id": pre.trainee_id,
            "pre_percent": round(pre.score_percent, 1),
            "post_percent": round(post.score_percent, 1),
            "absolute_gain": round(absolute, 1),
            "normalized_gain": round(normalized, 1),
        })

    return gains


def question_difficulty(session_id: int, db: Session) -> list[dict]:
    """Per-question difficulty analysis for a session."""
    results = (
        db.query(ExamResult)
        .filter(ExamResult.session_id == session_id)
        .all()
    )

    if not results:
        return []

    # Aggregate scores per question
    q_totals: dict[int, list[tuple[int, int]]] = {}  # qnum -> [(awarded, possible)]
    q_types: dict[int, str] = {}

    for r in results:
        for qs in r.question_scores:
            q_totals.setdefault(qs.question_number, []).append(
                (qs.points_awarded, qs.points_possible)
            )
            q_types[qs.question_number] = qs.question_type

    difficulty = []
    for qnum in sorted(q_totals.keys()):
        scores = q_totals[qnum]
        total_awarded = sum(s[0] for s in scores)
        total_possible = sum(s[1] for s in scores)
        avg_pct = (total_awarded / total_possible * 100.0) if total_possible else 0.0

        # For MC: percent who got full marks
        if q_types[qnum] == "MC":
            full_marks = sum(1 for s in scores if s[0] == s[1])
            pct_correct = full_marks / len(scores) * 100.0 if scores else 0.0
        else:
            pct_correct = avg_pct

        difficulty.append({
            "question_number": qnum,
            "question_type": q_types[qnum],
            "percent_correct": round(pct_correct, 1),
            "avg_points": round(total_awarded / len(scores), 2) if scores else 0,
            "num_responses": len(scores),
        })

    return difficulty


def cohort_summary(session_id: int, db: Session) -> dict | None:
    """Summary statistics for an exam session."""
    session = db.query(ExamSession).filter(ExamSession.id == session_id).first()
    if not session:
        return None

    results = session.results
    if not results:
        return {
            "session_id": session.id,
            "course_id": session.course_id,
            "form_type": session.form_type,
            "cohort_label": session.cohort_label,
            "num_students": 0,
            "avg_score": 0,
            "median_score": 0,
            "pass_rate": 0,
            "min_score": 0,
            "max_score": 0,
        }

    scores = sorted([r.score_percent for r in results])
    n = len(scores)
    median = scores[n // 2] if n % 2 else (scores[n // 2 - 1] + scores[n // 2]) / 2
    passing = sum(1 for r in results if r.result == "PASS")

    return {
        "session_id": session.id,
        "course_id": session.course_id,
        "form_type": session.form_type,
        "cohort_label": session.cohort_label,
        "num_students": n,
        "avg_score": round(sum(scores) / n, 1),
        "median_score": round(median, 1),
        "pass_rate": round(passing / n * 100, 1) if n else 0,
        "min_score": round(scores[0], 1),
        "max_score": round(scores[-1], 1),
    }


def item_discrimination(session_id: int, db: Session) -> list[dict]:
    """Point-biserial correlation for each question.

    Measures how well each question discriminates between high and low performers.
    High discrimination (> 0.3) = good question; low (< 0.1) = poor question.
    """
    results = (
        db.query(ExamResult)
        .filter(ExamResult.session_id == session_id)
        .all()
    )
    if len(results) < 3:
        return []

    # Split into top/bottom halves by total score
    sorted_results = sorted(results, key=lambda r: r.total_score)
    mid = len(sorted_results) // 2
    bottom_ids = {r.id for r in sorted_results[:mid]}
    top_ids = {r.id for r in sorted_results[mid:]}

    # Per-question analysis
    q_data: dict[int, dict] = {}
    for r in results:
        group = "top" if r.id in top_ids else "bottom"
        for qs in r.question_scores:
            qn = qs.question_number
            if qn not in q_data:
                q_data[qn] = {"type": qs.question_type, "possible": qs.points_possible,
                              "top_scores": [], "bottom_scores": [], "all_scores": []}
            q_data[qn][f"{group}_scores"].append(qs.points_awarded)
            q_data[qn]["all_scores"].append(qs.points_awarded)

    disc_results = []
    for qnum in sorted(q_data.keys()):
        d = q_data[qnum]
        top_avg = sum(d["top_scores"]) / len(d["top_scores"]) if d["top_scores"] else 0
        bottom_avg = sum(d["bottom_scores"]) / len(d["bottom_scores"]) if d["bottom_scores"] else 0
        # Discrimination index: (top_avg - bottom_avg) / points_possible
        disc_index = (top_avg - bottom_avg) / d["possible"] if d["possible"] else 0

        # Quality classification
        if disc_index >= 0.3:
            quality = "GOOD"
        elif disc_index >= 0.2:
            quality = "ACCEPTABLE"
        elif disc_index >= 0.1:
            quality = "MARGINAL"
        else:
            quality = "POOR"

        disc_results.append({
            "question_number": qnum,
            "question_type": d["type"],
            "discrimination_index": round(disc_index, 3),
            "top_avg": round(top_avg, 2),
            "bottom_avg": round(bottom_avg, 2),
            "quality": quality,
        })

    return disc_results


def cross_cohort_comparison(db: Session, course_id: str | None = None) -> list[dict]:
    """Compare cohort performance across sessions for the same course."""
    query = db.query(ExamSession)
    if course_id:
        query = query.filter(ExamSession.course_id == course_id)

    sessions = query.order_by(ExamSession.administration_date).all()
    comparisons = []

    for session in sessions:
        if not session.results:
            continue
        scores = [r.score_percent for r in session.results]
        n = len(scores)
        avg = sum(scores) / n
        passing = sum(1 for r in session.results if r.result == "PASS")
        sorted_scores = sorted(scores)
        median = sorted_scores[n // 2] if n % 2 else (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2

        # Standard deviation
        variance = sum((s - avg) ** 2 for s in scores) / n if n > 0 else 0
        std_dev = variance ** 0.5

        comparisons.append({
            "session_id": session.id,
            "course_id": session.course_id,
            "form_type": session.form_type,
            "cohort_label": session.cohort_label,
            "date": session.administration_date.isoformat(),
            "n_students": n,
            "avg_score": round(avg, 1),
            "median_score": round(median, 1),
            "std_dev": round(std_dev, 1),
            "pass_rate": round(passing / n * 100, 1) if n else 0,
            "min_score": round(sorted_scores[0], 1),
            "max_score": round(sorted_scores[-1], 1),
        })

    return comparisons


def question_improvement(
    pre_session_id: int, post_session_id: int, db: Session
) -> list[dict]:
    """Compare question-level performance between PRE and POST sessions.

    Shows which questions improved most — identifies where the training
    had the biggest impact.
    """
    pre_diff = question_difficulty(pre_session_id, db)
    post_diff = question_difficulty(post_session_id, db)

    if not pre_diff or not post_diff:
        return []

    pre_map = {q["question_number"]: q for q in pre_diff}
    post_map = {q["question_number"]: q for q in post_diff}

    results = []
    for qnum in sorted(set(pre_map.keys()) & set(post_map.keys())):
        pre_pct = pre_map[qnum]["percent_correct"]
        post_pct = post_map[qnum]["percent_correct"]
        improvement = post_pct - pre_pct

        results.append({
            "question_number": qnum,
            "question_type": pre_map[qnum]["question_type"],
            "pre_percent": pre_pct,
            "post_percent": post_pct,
            "improvement": round(improvement, 1),
        })

    return sorted(results, key=lambda x: x["improvement"], reverse=True)
