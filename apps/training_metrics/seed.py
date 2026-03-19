"""Seed historical snapshots for the Training Metrics Executive Dashboard.

Generates 3-4 weekly snapshots with realistic aggregated data. Calls
collect_all_metrics() if other app DBs exist, otherwise falls back to
synthetic snapshot data.
"""

from __future__ import annotations

import json
import random
from datetime import date, timedelta

from .db import ReportSnapshot, SessionLocal, init_db, collect_all_metrics


def _synthetic_snapshot(report_date: date, week_offset: int) -> dict:
    """Generate a realistic synthetic metrics snapshot for a given week.

    week_offset: 0 = most recent, 1 = one week ago, etc.
    Trends show gradual improvement over time.
    """
    # Base values — improve slightly each week (offset 3 is oldest)
    base_trainees = 60
    base_pass_rate = 72.0 + (3 - week_offset) * 2.5
    base_overdue = max(0, 8 - (3 - week_offset))
    base_alerts = max(0, 4 - (3 - week_offset))
    base_events = random.randint(3, 7)
    base_aars = 12 + (3 - week_offset) * 3

    # Funnel data — more soldiers progress each week
    tm10_pct = min(95, 82 + (3 - week_offset) * 3)
    tm20_pct = min(85, 65 + (3 - week_offset) * 4)
    tm30_pct = min(70, 45 + (3 - week_offset) * 5)
    tm40_pct = min(55, 30 + (3 - week_offset) * 4)
    tm50_pct = min(30, 10 + (3 - week_offset) * 3)

    funnel = [
        {"stage": "TM-10: Maven User", "count": int(base_trainees * tm10_pct / 100),
         "total": base_trainees, "pct": tm10_pct},
        {"stage": "TM-20: Builder", "count": int(base_trainees * tm20_pct / 100),
         "total": base_trainees, "pct": tm20_pct},
        {"stage": "TM-30: Advanced Builder", "count": int(base_trainees * tm30_pct / 100),
         "total": base_trainees, "pct": tm30_pct},
        {"stage": "TM-40: Any Specialization", "count": int(base_trainees * tm40_pct / 100),
         "total": base_trainees, "pct": tm40_pct},
        {"stage": "TM-50: Advanced", "count": int(base_trainees * tm50_pct / 100),
         "total": base_trainees, "pct": tm50_pct},
    ]

    # Unit summary
    units = ["1-1 IN BN", "2-1 IN BN", "3-1 FA BN", "BSB 1BCT", "BEB 1BCT"]
    unit_summary = []
    for unit in units:
        unit_trainees = random.randint(10, 14)
        avg_courses = round(random.uniform(2.0, 5.0), 1)
        unit_summary.append({
            "unit": unit,
            "total_trainees": unit_trainees,
            "avg_courses": avg_courses,
            "max_courses": random.randint(5, 8),
            "zero_courses": random.randint(0, 3),
        })

    # Bottleneck top 3
    bottleneck_courses = ["TM-20", "TM-30", "TM-40A"]
    bottleneck_top3 = [
        {
            "course_id": c,
            "completed": random.randint(15, 35),
            "eligible_not_done": max(0, random.randint(5, 18) - (3 - week_offset) * 2),
            "total_trainees": base_trainees,
        }
        for c in bottleneck_courses
    ]

    # Risk items — fewer as weeks progress
    risks = []
    if base_overdue >= 5:
        risks.append({
            "description": f"{base_overdue} training milestones overdue",
            "severity": "HIGH" if base_overdue >= 8 else "MEDIUM",
            "source_app": "Progress Tracker",
            "recommended_action": "Identify root causes; adjust timelines or allocate resources",
        })
    if base_alerts > 2:
        risks.append({
            "description": f"{base_alerts} active data quality alerts",
            "severity": "MEDIUM",
            "source_app": "Data Quality Monitor",
            "recommended_action": "Investigate and resolve data quality issues",
        })
    if random.random() > 0.5 + (3 - week_offset) * 0.1:
        risks.append({
            "description": "2 instructor certifications expiring within 30 days",
            "severity": "MEDIUM",
            "source_app": "Instructor Manager",
            "recommended_action": "Schedule recertification sessions",
        })

    # Executive summary
    readiness_score = round(min(100, 55 + (3 - week_offset) * 7 + random.uniform(-3, 3)), 1)
    if readiness_score >= 70:
        rag = "GREEN"
    elif readiness_score >= 50:
        rag = "AMBER"
    else:
        rag = "RED"

    executive_summary = {
        "readiness_score": readiness_score,
        "on_track": (
            f"Training program {'is on track' if rag == 'GREEN' else 'requires attention'}. "
            f"{base_trainees} trainees in pipeline, readiness score {readiness_score}%."
        ),
        "at_risk": (
            f"{len([r for r in risks if r['severity'] == 'HIGH'])} HIGH-severity risks. "
            + (risks[0]["description"] if risks else "No critical issues.")
        ),
        "what_changed": (
            f"{base_events} MTT events scheduled. "
            f"{random.randint(1, 4)} new lessons learned this month."
        ),
        "decision_required": (
            "Review and mitigate HIGH-severity risks."
            if any(r["severity"] == "HIGH" for r in risks)
            else "No immediate decisions required."
        ),
        "rag": rag,
    }

    return {
        "total_trainees": base_trainees,
        "funnel": funnel,
        "unit_summary": unit_summary,
        "bottleneck_top3": bottleneck_top3,
        "exam_pass_rate": round(base_pass_rate, 1),
        "exam_sessions_count": random.randint(8, 15),
        "total_aars": base_aars,
        "top_issues": [
            {"issue": "Insufficient lab time for TM-30", "count": random.randint(3, 7)},
            {"issue": "Network connectivity during exercises", "count": random.randint(2, 5)},
        ],
        "overdue_milestones": base_overdue,
        "upcoming_events": base_events,
        "active_alerts": base_alerts,
        "expiring_certs": random.randint(0, 3),
        "coverage_gaps": random.randint(0, 2),
        "fill_rate": round(random.uniform(0.72, 0.95), 2),
        "waitlisted_count": random.randint(3, 12),
        "overdue_reviews": random.randint(0, 4),
        "stale_docs": random.randint(2, 8),
        "open_action_items": random.randint(2, 8),
        "lessons_this_month": random.randint(1, 5),
        "risks": risks,
        "executive_summary": executive_summary,
    }


def seed():
    """Insert 4 weekly historical snapshots."""
    init_db()
    db = SessionLocal()
    try:
        if db.query(ReportSnapshot).count() > 0:
            print("DB already has snapshots -- skipping seed.")
            return

        random.seed(42)

        # Try to collect live metrics for the most recent snapshot
        live_data = None
        try:
            live_data = collect_all_metrics()
            # Only use live data if it has real content
            if live_data.get("total_trainees", 0) == 0:
                live_data = None
        except Exception:
            live_data = None

        today = date.today()
        snapshots_created = 0

        for week_offset in range(3, -1, -1):  # 3 weeks ago -> this week
            report_date = today - timedelta(weeks=week_offset)

            if week_offset == 0 and live_data:
                # Use live data for the most recent snapshot
                data = live_data
            else:
                # Use synthetic data for historical snapshots
                data = _synthetic_snapshot(report_date, week_offset)

            snapshot = ReportSnapshot(
                report_date=report_date,
                report_type="WEEKLY",
                generated_by="SYSTEM (seed)",
                data_json=json.dumps(data, default=str),
                notes=f"Week of {report_date.isoformat()} — {'live' if week_offset == 0 and live_data else 'synthetic'} data",
            )
            db.add(snapshot)
            snapshots_created += 1

        db.commit()
        print(f"Seeded {snapshots_created} weekly snapshots.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
