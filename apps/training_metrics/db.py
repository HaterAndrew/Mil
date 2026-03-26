"""Training Metrics Executive Dashboard — database models and aggregation logic.

This app has a minimal local DB for storing dashboard snapshots/report history.
All training data is read from other app databases via their public functions.
"""

from __future__ import annotations

import json
import logging
from contextlib import contextmanager

logger = logging.getLogger(__name__)
from datetime import UTC, date, datetime
from pathlib import Path

from sqlalchemy import (
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

# ---------------------------------------------------------------------------
# Database path — sits next to this file; *.db is gitignored
# ---------------------------------------------------------------------------
DB_PATH = Path(__file__).parent / "training_metrics.db"
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
# ORM model — snapshot history
# ---------------------------------------------------------------------------
class ReportSnapshot(Base):
    __tablename__ = "report_snapshots"

    id = Column(Integer, primary_key=True, autoincrement=True)
    report_date = Column(Date, nullable=False, default=lambda: date.today())
    report_type = Column(String(30), nullable=False)  # WEEKLY / MONTHLY / QUARTERLY
    generated_by = Column(String(100), nullable=False)
    data_json = Column(Text, nullable=False)  # JSON blob of all KPIs at snapshot time
    notes = Column(Text, nullable=True)
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


def save_snapshot(
    report_type: str,
    generated_by: str,
    data: dict,
    db: Session,
    notes: str | None = None,
) -> ReportSnapshot:
    """Persist a point-in-time metrics snapshot."""
    snapshot = ReportSnapshot(
        report_date=date.today(),
        report_type=report_type,
        generated_by=generated_by,
        data_json=json.dumps(data, default=str),
        notes=notes,
    )
    db.add(snapshot)
    db.commit()
    db.refresh(snapshot)
    return snapshot


def get_latest_snapshot(report_type: str, db: Session) -> ReportSnapshot | None:
    """Return the most recent snapshot of the given type."""
    return (
        db.query(ReportSnapshot)
        .filter(ReportSnapshot.report_type == report_type)
        .order_by(ReportSnapshot.report_date.desc(), ReportSnapshot.id.desc())
        .first()
    )


def get_snapshot_history(db: Session) -> list[ReportSnapshot]:
    """Return all snapshots ordered by date descending."""
    return (
        db.query(ReportSnapshot)
        .order_by(ReportSnapshot.report_date.desc(), ReportSnapshot.id.desc())
        .all()
    )


# ---------------------------------------------------------------------------
# Cross-app aggregation — THE KEY FUNCTION
# ---------------------------------------------------------------------------
def collect_all_metrics() -> dict:
    """Import data from all other MSS Training app DBs and aggregate.

    Every external import is wrapped in try/except so the dashboard works
    even if some apps aren't seeded or available.
    """
    metrics: dict = {}

    # ----- Readiness Tracker -----
    try:
        from readiness_tracker.db import (
            SessionLocal as RT_Session,
            get_bottleneck_analysis,
            get_funnel_data,
            get_unit_summary,
            init_db as rt_init,
            Trainee,
        )
        rt_init()
        db = RT_Session()
        try:
            metrics["total_trainees"] = db.query(Trainee).count()
            metrics["funnel"] = get_funnel_data(db)
            metrics["unit_summary"] = get_unit_summary(db)

            # Top 3 bottlenecks (courses with most eligible-not-done)
            bottlenecks = get_bottleneck_analysis(db)
            top3 = sorted(bottlenecks, key=lambda x: x["eligible_not_done"], reverse=True)[:3]
            metrics["bottleneck_top3"] = top3
        finally:
            db.close()
    except Exception:
        logger.warning("Failed to load readiness_tracker metrics", exc_info=True)
        metrics.setdefault("total_trainees", 0)
        metrics.setdefault("funnel", [])
        metrics.setdefault("unit_summary", [])
        metrics.setdefault("bottleneck_top3", [])

    # ----- Exam Analytics -----
    try:
        from exam_analytics.db import (
            SessionLocal as EA_Session,
            ExamSession,
            ExamResult,
            cross_cohort_comparison,
            init_db as ea_init,
        )
        ea_init()
        db = EA_Session()
        try:
            sessions_count = db.query(ExamSession).count()
            metrics["exam_sessions_count"] = sessions_count

            # Compute overall pass rate from cross-cohort data
            cohorts = cross_cohort_comparison(db)
            if cohorts:
                total_pass = sum(c.get("pass_rate", 0) * c.get("n_students", 0) / 100 for c in cohorts)
                total_take = sum(c.get("n_students", 0) for c in cohorts)
                metrics["exam_pass_rate"] = round(total_pass / total_take * 100, 1) if total_take else None
            else:
                metrics["exam_pass_rate"] = None
        finally:
            db.close()
    except Exception:
        logger.warning("Failed to load exam_analytics metrics", exc_info=True)
        metrics.setdefault("exam_sessions_count", 0)
        metrics.setdefault("exam_pass_rate", None)

    # ----- AAR Aggregator -----
    try:
        from aar_aggregator.db import (
            SessionLocal as AAR_Session,
            AAR,
            find_recurring_issues,
            init_db as aar_init,
        )
        aar_init()
        db = AAR_Session()
        try:
            metrics["total_aars"] = db.query(AAR).count()
            recurring = find_recurring_issues(db=db, min_count=2)
            # Take top 5 recurring issues
            metrics["top_issues"] = recurring[:5] if recurring else []
        finally:
            db.close()
    except Exception:
        logger.warning("Failed to load aar_aggregator metrics", exc_info=True)
        metrics.setdefault("total_aars", 0)
        metrics.setdefault("top_issues", [])

    # ----- Progress Tracker -----
    try:
        from progress_tracker.db import (
            SessionLocal as PT_Session,
            get_all_overdue,
            init_db as pt_init,
        )
        pt_init()
        db = PT_Session()
        try:
            overdue = get_all_overdue(db)
            metrics["overdue_milestones"] = len(overdue)
        finally:
            db.close()
    except Exception:
        logger.warning("Failed to load progress_tracker metrics", exc_info=True)
        metrics.setdefault("overdue_milestones", 0)

    # ----- MTT Scheduler -----
    try:
        from mtt_scheduler.db import (
            SessionLocal as MTT_Session,
            Event,
            init_db as mtt_init,
        )
        mtt_init()
        db = MTT_Session()
        try:
            # Count events from today forward
            upcoming = (
                db.query(Event)
                .filter(Event.start_date >= date.today())
                .count()
            )
            metrics["upcoming_events"] = upcoming
        finally:
            db.close()
    except Exception:
        logger.warning("Failed to load mtt_scheduler metrics", exc_info=True)
        metrics.setdefault("upcoming_events", 0)

    # ----- Data Quality -----
    try:
        from data_quality.db import (
            SessionLocal as DQ_Session,
            get_active_alerts,
            init_db as dq_init,
        )
        dq_init()
        db = DQ_Session()
        try:
            alerts = get_active_alerts(session=db)
            metrics["active_alerts"] = len(alerts)
        finally:
            db.close()
    except Exception:
        logger.warning("Failed to load data_quality metrics", exc_info=True)
        metrics.setdefault("active_alerts", 0)

    # ----- Instructor Manager (optional — may not exist yet) -----
    try:
        from instructor_manager.db import (
            SessionLocal as IM_Session,
            get_expiring_certifications,
            get_coverage_matrix,
            init_db as im_init,
        )
        im_init()
        db = IM_Session()
        try:
            expiring = get_expiring_certifications(days_ahead=30, db=db)
            metrics["expiring_certs"] = len(expiring)

            coverage = get_coverage_matrix(db)
            # Count courses with zero certified instructors
            gaps = sum(1 for c in coverage if c.get("certified_count", 0) == 0)
            metrics["coverage_gaps"] = gaps
        finally:
            db.close()
    except Exception:
        logger.warning("Failed to load instructor_manager metrics", exc_info=True)
        metrics.setdefault("expiring_certs", 0)
        metrics.setdefault("coverage_gaps", 0)

    # ----- Enrollment Manager (optional — may not exist yet) -----
    try:
        from enrollment_manager.db import (
            SessionLocal as EM_Session,
            get_enrollment_stats,
            init_db as em_init,
        )
        em_init()
        db = EM_Session()
        try:
            stats = get_enrollment_stats(db)
            metrics["fill_rate"] = stats.get("avg_fill_rate")
            metrics["waitlisted_count"] = stats.get("total_waitlisted", 0)
        finally:
            db.close()
    except Exception:
        logger.warning("Failed to load enrollment_manager metrics", exc_info=True)
        metrics.setdefault("fill_rate", None)
        metrics.setdefault("waitlisted_count", 0)

    # ----- Curriculum Tracker (optional — may not exist yet) -----
    try:
        from curriculum_tracker.db import (
            SessionLocal as CT_Session,
            get_overdue_reviews,
            get_stale_documents,
            init_db as ct_init,
        )
        ct_init()
        db = CT_Session()
        try:
            overdue_reviews = get_overdue_reviews(db)
            metrics["overdue_reviews"] = len(overdue_reviews)

            stale = get_stale_documents(days=90, db=db)
            metrics["stale_docs"] = len(stale)
        finally:
            db.close()
    except Exception:
        logger.warning("Failed to load curriculum_tracker metrics", exc_info=True)
        metrics.setdefault("overdue_reviews", 0)
        metrics.setdefault("stale_docs", 0)

    # ----- Lessons Learned (optional — may not exist yet) -----
    try:
        from lessons_learned.db import (  # type: ignore[import-not-found]
            SessionLocal as LL_Session,
            Lesson,
            ActionItem,
            init_db as ll_init,
        )
        ll_init()
        db = LL_Session()
        try:
            open_items = db.query(ActionItem).filter(ActionItem.status == "OPEN").count()
            metrics["open_action_items"] = open_items

            # Lessons submitted this month
            month_start = date.today().replace(day=1)
            this_month = db.query(Lesson).filter(Lesson.submit_date >= month_start).count()
            metrics["lessons_this_month"] = this_month
        finally:
            db.close()
    except Exception:
        logger.warning("Failed to load lessons_learned metrics", exc_info=True)
        metrics.setdefault("open_action_items", 0)
        metrics.setdefault("lessons_this_month", 0)

    # ----- Compute risks from collected metrics -----
    metrics["risks"] = _compute_risks(metrics)

    # ----- Compute executive summary -----
    metrics["executive_summary"] = _compute_executive_summary(metrics)

    return metrics


def _compute_risks(metrics: dict) -> list[dict]:
    """Auto-generate risk items from the aggregated metrics."""
    risks = []

    # Expiring instructor certs
    if metrics.get("expiring_certs", 0) > 0:
        severity = "HIGH" if metrics["expiring_certs"] >= 5 else "MEDIUM"
        risks.append({
            "description": f"{metrics['expiring_certs']} instructor certifications expiring within 30 days",
            "severity": severity,
            "source_app": "Instructor Manager",
            "recommended_action": "Schedule recertification sessions; prioritize courses with single-instructor coverage",
        })

    # Coverage gaps
    if metrics.get("coverage_gaps", 0) > 0:
        risks.append({
            "description": f"{metrics['coverage_gaps']} courses have zero certified instructors",
            "severity": "HIGH",
            "source_app": "Instructor Manager",
            "recommended_action": "Cross-train instructors or recruit SMEs for uncovered courses",
        })

    # High waitlist
    if metrics.get("waitlisted_count", 0) >= 10:
        risks.append({
            "description": f"{metrics['waitlisted_count']} students on waitlists across active classes",
            "severity": "MEDIUM",
            "source_app": "Enrollment Manager",
            "recommended_action": "Consider adding class sections or increasing capacity",
        })

    # Overdue curriculum reviews
    if metrics.get("overdue_reviews", 0) > 0:
        severity = "HIGH" if metrics["overdue_reviews"] >= 5 else "MEDIUM"
        risks.append({
            "description": f"{metrics['overdue_reviews']} curriculum documents overdue for review",
            "severity": severity,
            "source_app": "Curriculum Tracker",
            "recommended_action": "Assign reviewers and set deadlines for overdue documents",
        })

    # Stale documents
    if metrics.get("stale_docs", 0) >= 10:
        risks.append({
            "description": f"{metrics['stale_docs']} documents not updated in 90+ days",
            "severity": "LOW",
            "source_app": "Curriculum Tracker",
            "recommended_action": "Review stale documents for accuracy; update or archive as needed",
        })

    # Open action items from lessons learned
    if metrics.get("open_action_items", 0) >= 5:
        severity = "HIGH" if metrics["open_action_items"] >= 10 else "MEDIUM"
        risks.append({
            "description": f"{metrics['open_action_items']} open action items from lessons learned",
            "severity": severity,
            "source_app": "Lessons Learned",
            "recommended_action": "Review and assign owners for all open action items",
        })

    # Overdue milestones
    if metrics.get("overdue_milestones", 0) > 0:
        severity = "HIGH" if metrics["overdue_milestones"] >= 10 else "MEDIUM"
        risks.append({
            "description": f"{metrics['overdue_milestones']} training milestones overdue",
            "severity": severity,
            "source_app": "Progress Tracker",
            "recommended_action": "Identify root causes for delays; adjust timelines or allocate resources",
        })

    # Active data quality alerts
    if metrics.get("active_alerts", 0) > 0:
        severity = "HIGH" if metrics["active_alerts"] >= 5 else "LOW"
        risks.append({
            "description": f"{metrics['active_alerts']} active data quality alerts",
            "severity": severity,
            "source_app": "Data Quality Monitor",
            "recommended_action": "Investigate and resolve data quality issues; check pipeline health",
        })

    # Training bottlenecks
    bottleneck_top3 = metrics.get("bottleneck_top3", [])
    for bn in bottleneck_top3:
        if bn.get("eligible_not_done", 0) >= 10:
            risks.append({
                "description": (
                    f"{bn['course_id']}: {bn['eligible_not_done']} soldiers eligible but not enrolled"
                ),
                "severity": "MEDIUM",
                "source_app": "Readiness Tracker",
                "recommended_action": f"Schedule {bn['course_id']} class or MTT to clear backlog",
            })

    # Sort: HIGH first, then MEDIUM, then LOW
    severity_order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    risks.sort(key=lambda r: severity_order.get(r["severity"], 3))

    return risks


def _compute_executive_summary(metrics: dict) -> dict:
    """Compute the four CG answers and an overall readiness score.

    Readiness score is a weighted average:
      - Training funnel progression: 30%
      - Exam pass rate: 20%
      - Overdue milestones (inverse): 15%
      - Active alerts (inverse): 10%
      - Instructor coverage: 15%
      - Risk count (inverse): 10%
    """
    scores = []

    # Funnel progression — what % of trainees have completed at least SL 3
    funnel = metrics.get("funnel", [])
    total_trainees = metrics.get("total_trainees", 0)
    if funnel and total_trainees > 0:
        # Find SL 3 stage
        tm30_pct = 0
        for stage in funnel:
            if "SL 3" in stage.get("stage", ""):
                tm30_pct = stage.get("pct", 0)
                break
        scores.append(("funnel", tm30_pct, 0.30))
    else:
        scores.append(("funnel", 0, 0.30))

    # Exam pass rate
    pass_rate = metrics.get("exam_pass_rate")
    if pass_rate is not None:
        scores.append(("exams", pass_rate, 0.20))
    else:
        scores.append(("exams", 50, 0.20))  # neutral if no data

    # Overdue milestones — fewer is better; score = 100 - (overdue * 5), min 0
    overdue = metrics.get("overdue_milestones", 0)
    overdue_score = max(0, 100 - overdue * 5)
    scores.append(("overdue", overdue_score, 0.15))

    # Active alerts — fewer is better
    alerts = metrics.get("active_alerts", 0)
    alert_score = max(0, 100 - alerts * 10)
    scores.append(("alerts", alert_score, 0.10))

    # Instructor coverage — % of courses with at least one certified instructor
    coverage_gaps = metrics.get("coverage_gaps", 0)
    # Assume ~20 courses total; each gap costs 5%
    coverage_score = max(0, 100 - coverage_gaps * 5)
    scores.append(("coverage", coverage_score, 0.15))

    # Risk count — fewer is better
    risk_count = len(metrics.get("risks", []))
    risk_score = max(0, 100 - risk_count * 8)
    scores.append(("risks", risk_score, 0.10))

    # Weighted average
    readiness_score = sum(s * w for _, s, w in scores)
    readiness_score = round(min(100, max(0, readiness_score)), 1)

    # RAG determination
    if readiness_score >= 70:
        rag = "GREEN"
    elif readiness_score >= 50:
        rag = "AMBER"
    else:
        rag = "RED"

    # Generate the four CG answers
    high_risks = [r for r in metrics.get("risks", []) if r["severity"] == "HIGH"]
    medium_risks = [r for r in metrics.get("risks", []) if r["severity"] == "MEDIUM"]

    # On Track
    if rag == "GREEN":
        on_track = (
            f"Training program is on track. {total_trainees} trainees in pipeline, "
            f"readiness score {readiness_score}%."
        )
    elif rag == "AMBER":
        on_track = (
            f"Training program requires attention. {total_trainees} trainees in pipeline, "
            f"readiness score {readiness_score}%. See risk register for details."
        )
    else:
        on_track = (
            f"Training program at risk. {total_trainees} trainees in pipeline, "
            f"readiness score {readiness_score}%. Immediate action required."
        )

    # At Risk
    if high_risks:
        at_risk = f"{len(high_risks)} HIGH-severity risks identified: " + "; ".join(
            r["description"] for r in high_risks[:3]
        )
    elif medium_risks:
        at_risk = f"{len(medium_risks)} MEDIUM-severity risks. No critical issues."
    else:
        at_risk = "No significant risks identified."

    # What Changed (based on available data)
    changes = []
    if metrics.get("upcoming_events", 0) > 0:
        changes.append(f"{metrics['upcoming_events']} MTT events scheduled")
    if metrics.get("lessons_this_month", 0) > 0:
        changes.append(f"{metrics['lessons_this_month']} new lessons learned this month")
    if metrics.get("total_aars", 0) > 0:
        changes.append(f"{metrics['total_aars']} AARs on file")
    what_changed = ". ".join(changes) if changes else "No significant changes since last report."

    # Decision Required
    decisions = []
    if high_risks:
        decisions.append("Review and mitigate HIGH-severity risks")
    if metrics.get("overdue_milestones", 0) >= 10:
        decisions.append("Approve timeline extensions or resource reallocation for overdue milestones")
    if metrics.get("coverage_gaps", 0) > 0:
        decisions.append(f"Approve instructor cross-training for {metrics['coverage_gaps']} uncovered courses")
    if metrics.get("waitlisted_count", 0) >= 15:
        decisions.append("Approve additional class sections to clear waitlist backlog")
    decision_required = ". ".join(decisions) if decisions else "No immediate decisions required."

    return {
        "readiness_score": readiness_score,
        "on_track": on_track,
        "at_risk": at_risk,
        "what_changed": what_changed,
        "decision_required": decision_required,
        "rag": rag,
    }
