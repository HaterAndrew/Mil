"""Training Metrics Executive Dashboard — FastAPI application."""

from __future__ import annotations

from contextlib import asynccontextmanager
from datetime import date

from fastapi import Depends, FastAPI, HTTPException, Query
from shared.auth import verify_api_key
from shared.factory import create_app
from sqlalchemy.orm import Session

from .db import (
    collect_all_metrics,
    get_db,
    get_latest_snapshot,
    get_snapshot_history,
    init_db,
    save_snapshot,
)
from .models import (
    MetricsBundle,
    SnapshotCreate,
    SnapshotResponse,
)


# ---------------------------------------------------------------------------
# App lifecycle
# ---------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = create_app(title="Training Metrics Executive Dashboard", version="1.0.0", lifespan=lifespan)


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------
@app.get("/health")
def health():
    return {"status": "ok"}


# ---------------------------------------------------------------------------
# Live aggregated metrics
# ---------------------------------------------------------------------------
@app.get("/metrics", response_model=MetricsBundle)
def get_metrics():
    """Collect current metrics from all app DBs and return aggregated bundle."""
    data = collect_all_metrics()
    return MetricsBundle(**data)


# ---------------------------------------------------------------------------
# Snapshots — save / list / latest
# ---------------------------------------------------------------------------
@app.post("/snapshots", response_model=SnapshotResponse, status_code=201, dependencies=[Depends(verify_api_key)])
def create_snapshot(payload: SnapshotCreate, db: Session = Depends(get_db)):
    """Capture a point-in-time snapshot of all metrics."""
    data = collect_all_metrics()
    snapshot = save_snapshot(
        report_type=payload.report_type,
        generated_by=payload.generated_by,
        data=data,
        db=db,
        notes=payload.notes,
    )
    return snapshot


@app.get("/snapshots", response_model=list[SnapshotResponse])
def list_snapshots(db: Session = Depends(get_db)):
    """Return all snapshots ordered by date descending."""
    return get_snapshot_history(db)


@app.get("/snapshots/latest", response_model=SnapshotResponse)
def latest_snapshot(
    type: str = Query("WEEKLY", description="WEEKLY, MONTHLY, or QUARTERLY"),
    db: Session = Depends(get_db),
):
    """Return the most recent snapshot of the given type."""
    snapshot = get_latest_snapshot(type.upper(), db)
    if not snapshot:
        raise HTTPException(status_code=404, detail=f"No {type} snapshot found")
    return snapshot


# ---------------------------------------------------------------------------
# Briefing export — BLUF format
# ---------------------------------------------------------------------------
@app.get("/export/briefing", dependencies=[Depends(verify_api_key)])
def export_briefing():
    """Generate a text-based executive briefing in BLUF format."""
    data = collect_all_metrics()
    summary = data.get("executive_summary", {})
    risks = data.get("risks", [])

    lines = []
    lines.append("=" * 72)
    lines.append("MSS TRAINING EXECUTIVE BRIEFING")
    lines.append(f"Date: {date.today().isoformat()}")
    lines.append(f"Classification: CUI")
    lines.append("=" * 72)
    lines.append("")

    # BLUF — Bottom Line Up Front
    lines.append("BOTTOM LINE UP FRONT (BLUF)")
    lines.append("-" * 40)
    rag = summary.get("rag", "N/A")
    score = summary.get("readiness_score", 0)
    lines.append(f"Overall Readiness: {rag} ({score}%)")
    lines.append(f"  {summary.get('on_track', 'No data available.')}")
    lines.append("")

    # The four CG questions
    lines.append("1. ARE WE ON TRACK?")
    lines.append(f"   {summary.get('on_track', 'No data.')}")
    lines.append("")

    lines.append("2. WHAT'S AT RISK?")
    lines.append(f"   {summary.get('at_risk', 'No risks identified.')}")
    lines.append("")

    lines.append("3. WHAT CHANGED?")
    lines.append(f"   {summary.get('what_changed', 'No changes.')}")
    lines.append("")

    lines.append("4. WHAT DO YOU NEED FROM ME?")
    lines.append(f"   {summary.get('decision_required', 'No decisions required.')}")
    lines.append("")

    # Key metrics
    lines.append("KEY METRICS")
    lines.append("-" * 40)
    lines.append(f"  Total Trainees:      {data.get('total_trainees', 0)}")
    lines.append(f"  Exam Pass Rate:      {data.get('exam_pass_rate', 'N/A')}%")
    lines.append(f"  Upcoming Events:     {data.get('upcoming_events', 0)}")
    lines.append(f"  Overdue Milestones:  {data.get('overdue_milestones', 0)}")
    lines.append(f"  Active Alerts:       {data.get('active_alerts', 0)}")
    lines.append(f"  Open Action Items:   {data.get('open_action_items', 0)}")
    lines.append(f"  Expiring Certs:      {data.get('expiring_certs', 0)}")
    lines.append(f"  Waitlisted Students: {data.get('waitlisted_count', 0)}")
    lines.append("")

    # Risk register
    if risks:
        lines.append("RISK REGISTER")
        lines.append("-" * 40)
        for i, r in enumerate(risks, 1):
            lines.append(f"  {i}. [{r['severity']}] {r['description']}")
            lines.append(f"     Source: {r['source_app']}")
            lines.append(f"     Action: {r['recommended_action']}")
            lines.append("")

    lines.append("=" * 72)
    lines.append("END OF BRIEFING")
    lines.append("=" * 72)

    return {"briefing": "\n".join(lines)}
