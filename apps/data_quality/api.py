"""FastAPI backend for the Data Quality Monitor."""

from __future__ import annotations

from contextlib import asynccontextmanager
from datetime import datetime, timezone
from typing import Optional

from fastapi import FastAPI, HTTPException, Query
from sqlalchemy import desc, func

from shared.middleware import SecurityHeadersMiddleware

from .db import (
    AlertRow,
    MetricRow,
    PipelineRow,
    acknowledge_alert,
    evaluate_metric,
    get_active_alerts,
    get_all_health,
    get_db,
    get_metric_trend,
    get_pipeline_health,
    init_db,
)
from .models import (
    AlertOut,
    AlertSeverity,
    MetricCreate,
    MetricResponse,
    MetricStatus,
    MetricType,
    PipelineCreate,
    PipelineHealth,
    PipelineResponse,
    PipelineStatus,
)


# ---------------------------------------------------------------------------
# App lifespan — initialize DB on startup
# ---------------------------------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Data Quality Monitor API",
    description="Track pipeline health, data quality metrics, and anomaly alerts.",
    version="1.0.0",
    lifespan=lifespan,
)
app.add_middleware(SecurityHeadersMiddleware)


# ---------------------------------------------------------------------------
# Pipeline CRUD
# ---------------------------------------------------------------------------

@app.post("/pipelines", response_model=PipelineResponse, status_code=201)
def create_pipeline(payload: PipelineCreate):
    """Register a new data pipeline."""
    with get_db() as db:
        existing = db.query(PipelineRow).filter(PipelineRow.name == payload.name).first()
        if existing:
            raise HTTPException(409, f"Pipeline '{payload.name}' already exists")
        row = PipelineRow(**payload.model_dump())
        db.add(row)
        db.flush()
        db.refresh(row)
        return row


@app.get("/pipelines", response_model=list[PipelineResponse])
def list_pipelines():
    """List all registered pipelines."""
    with get_db() as db:
        return db.query(PipelineRow).order_by(PipelineRow.name).all()


@app.get("/pipelines/{pipeline_id}", response_model=PipelineResponse)
def get_pipeline(pipeline_id: int):
    """Get a single pipeline by ID."""
    with get_db() as db:
        row = db.query(PipelineRow).filter(PipelineRow.id == pipeline_id).first()
        if not row:
            raise HTTPException(404, "Pipeline not found")
        return row


@app.put("/pipelines/{pipeline_id}", response_model=PipelineResponse)
def update_pipeline(pipeline_id: int, payload: PipelineCreate):
    """Update an existing pipeline registration."""
    with get_db() as db:
        row = db.query(PipelineRow).filter(PipelineRow.id == pipeline_id).first()
        if not row:
            raise HTTPException(404, "Pipeline not found")
        for field, val in payload.model_dump().items():
            setattr(row, field, val)
        db.flush()
        db.refresh(row)
        return row


@app.delete("/pipelines/{pipeline_id}", status_code=204)
def delete_pipeline(pipeline_id: int):
    """Remove a pipeline and all associated data."""
    with get_db() as db:
        row = db.query(PipelineRow).filter(PipelineRow.id == pipeline_id).first()
        if not row:
            raise HTTPException(404, "Pipeline not found")
        db.delete(row)


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------

@app.post("/metrics", response_model=MetricResponse, status_code=201)
def record_metric(payload: MetricCreate):
    """Record a metric observation for a pipeline.

    Automatically evaluates the metric against its threshold, creates an
    alert when the result is FAIL, and updates the parent pipeline status.
    """
    with get_db() as db:
        pipe = db.query(PipelineRow).filter(PipelineRow.id == payload.pipeline_id).first()
        if not pipe:
            raise HTTPException(404, "Pipeline not found")

        status = evaluate_metric(payload.value, payload.threshold, payload.metric_type)
        ts = payload.timestamp or datetime.now(timezone.utc)

        row = MetricRow(
            pipeline_id=payload.pipeline_id,
            metric_type=payload.metric_type,
            value=payload.value,
            threshold=payload.threshold,
            status=status.value,
            timestamp=ts,
        )
        db.add(row)

        # Update pipeline last_run / last_success / status
        pipe.status = _derive_pipeline_status(db, pipe.id, status).value
        # Use raw SQL attributes so we don't trigger validation
        pipe.last_run = ts  # type: ignore[assignment]
        if status == MetricStatus.PASS:
            pipe.last_success = ts  # type: ignore[assignment]

        # Generate alert on FAIL
        if status == MetricStatus.FAIL:
            severity = (
                AlertSeverity.CRITICAL.value
                if payload.metric_type in (MetricType.COMPLETENESS, MetricType.ACCURACY)
                else AlertSeverity.WARNING.value
            )
            alert = AlertRow(
                pipeline_id=payload.pipeline_id,
                metric_type=payload.metric_type,
                value=payload.value,
                threshold=payload.threshold,
                severity=severity,
                timestamp=ts,
            )
            db.add(alert)

        db.flush()
        db.refresh(row)
        return row


def _derive_pipeline_status(db, pipeline_id: int, latest: MetricStatus) -> PipelineStatus:
    """Derive overall pipeline status considering latest observation."""
    if latest == MetricStatus.FAIL:
        return PipelineStatus.FAILED
    if latest == MetricStatus.WARN:
        return PipelineStatus.DEGRADED
    # If latest is PASS, check whether any other recent metric is degraded
    from datetime import timedelta
    cutoff = datetime.now(timezone.utc) - timedelta(hours=24)
    recent_fail = (
        db.query(MetricRow)
        .filter(
            MetricRow.pipeline_id == pipeline_id,
            MetricRow.timestamp >= cutoff,
            MetricRow.status == MetricStatus.FAIL.value,
        )
        .first()
    )
    if recent_fail:
        return PipelineStatus.FAILED
    recent_warn = (
        db.query(MetricRow)
        .filter(
            MetricRow.pipeline_id == pipeline_id,
            MetricRow.timestamp >= cutoff,
            MetricRow.status == MetricStatus.WARN.value,
        )
        .first()
    )
    if recent_warn:
        return PipelineStatus.DEGRADED
    return PipelineStatus.HEALTHY


@app.get("/metrics/{pipeline_id}", response_model=list[MetricResponse])
def get_metrics(
    pipeline_id: int,
    type: Optional[MetricType] = Query(None, alias="type"),
    days: int = Query(30, ge=1, le=365),
):
    """Retrieve metric history for a pipeline, optionally filtered by type."""
    with get_db() as db:
        pipe = db.query(PipelineRow).filter(PipelineRow.id == pipeline_id).first()
        if not pipe:
            raise HTTPException(404, "Pipeline not found")
        rows = get_metric_trend(db, pipeline_id, type.value if type else None, days)
        if type:
            # get_metric_trend already filters by type when non-None
            return rows
        # If no type filter, return all types for this pipeline
        from datetime import timedelta
        cutoff = datetime.now(timezone.utc) - timedelta(days=days)
        return (
            db.query(MetricRow)
            .filter(MetricRow.pipeline_id == pipeline_id, MetricRow.timestamp >= cutoff)
            .order_by(MetricRow.timestamp)
            .all()
        )


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------

@app.get("/health", response_model=list[PipelineHealth])
def all_health():
    """Health summary for all pipelines."""
    with get_db() as db:
        return get_all_health(db)


@app.get("/health/{pipeline_id}", response_model=PipelineHealth)
def pipeline_health(pipeline_id: int):
    """Health summary for a single pipeline."""
    with get_db() as db:
        h = get_pipeline_health(db, pipeline_id)
        if not h:
            raise HTTPException(404, "Pipeline not found")
        return h


# ---------------------------------------------------------------------------
# Alerts
# ---------------------------------------------------------------------------

@app.get("/alerts", response_model=list[AlertOut])
def list_alerts(
    severity: Optional[AlertSeverity] = Query(None),
    pipeline_id: Optional[int] = Query(None),
):
    """Active (unacknowledged) alerts, optionally filtered."""
    with get_db() as db:
        return get_active_alerts(
            db,
            severity=severity.value if severity else None,
            pipeline_id=pipeline_id,
        )


@app.post("/alerts/{alert_id}/ack", response_model=AlertOut)
def ack_alert(alert_id: int, ack_by: str = Query("operator")):
    """Acknowledge an alert."""
    with get_db() as db:
        alert = acknowledge_alert(db, alert_id, ack_by)
        if not alert:
            raise HTTPException(404, "Alert not found")
        db.flush()
        db.refresh(alert)
        pipe = db.query(PipelineRow).filter(PipelineRow.id == alert.pipeline_id).first()
        return {
            "id": alert.id,
            "pipeline_id": alert.pipeline_id,
            "pipeline_name": pipe.name if pipe else "Unknown",
            "metric_type": alert.metric_type,
            "value": alert.value,
            "threshold": alert.threshold,
            "severity": alert.severity,
            "timestamp": alert.timestamp,
            "acknowledged": alert.acknowledged,
        }


# ---------------------------------------------------------------------------
# Dashboard aggregate stats
# ---------------------------------------------------------------------------

@app.get("/dashboard-stats")
def dashboard_stats():
    """Aggregate KPIs for the Streamlit dashboard header."""
    with get_db() as db:
        total_pipes = db.query(func.count(PipelineRow.id)).scalar() or 0
        healthy = (
            db.query(func.count(PipelineRow.id))
            .filter(PipelineRow.status == PipelineStatus.HEALTHY.value)
            .scalar()
            or 0
        )
        degraded = (
            db.query(func.count(PipelineRow.id))
            .filter(PipelineRow.status == PipelineStatus.DEGRADED.value)
            .scalar()
            or 0
        )
        failed = (
            db.query(func.count(PipelineRow.id))
            .filter(PipelineRow.status == PipelineStatus.FAILED.value)
            .scalar()
            or 0
        )
        active_alerts = (
            db.query(func.count(AlertRow.id))
            .filter(AlertRow.acknowledged == False)  # noqa: E712
            .scalar()
            or 0
        )
        critical_alerts = (
            db.query(func.count(AlertRow.id))
            .filter(
                AlertRow.acknowledged == False,  # noqa: E712
                AlertRow.severity == AlertSeverity.CRITICAL.value,
            )
            .scalar()
            or 0
        )

        return {
            "total_pipelines": total_pipes,
            "healthy": healthy,
            "degraded": degraded,
            "failed": failed,
            "active_alerts": active_alerts,
            "critical_alerts": critical_alerts,
            "health_pct": round((healthy / total_pipes) * 100, 1) if total_pipes else 0.0,
        }
