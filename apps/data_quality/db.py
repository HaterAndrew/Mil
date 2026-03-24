"""SQLAlchemy ORM, tables, and business logic for the Data Quality Monitor."""

from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Generator, Optional

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    create_engine,
    desc,
    func,
)
from sqlalchemy.orm import Session, declarative_base, relationship, sessionmaker

import sys
from pathlib import Path as _Path
_apps_dir = str(_Path(__file__).resolve().parent.parent)
if _apps_dir not in sys.path:
    sys.path.insert(0, _apps_dir)

from shared.audit_mixin import AuditMixin

from .models import (
    AlertSeverity,
    MetricStatus,
    MetricType,
    PipelineHealth,
    PipelineStatus,
)

# ---------------------------------------------------------------------------
# Database path & engine
# ---------------------------------------------------------------------------
DB_PATH = Path(__file__).parent / "data_quality.db"
_engine = create_engine(f"sqlite:///{DB_PATH}", echo=False)
_SessionLocal = sessionmaker(bind=_engine)

Base = declarative_base()


# ---------------------------------------------------------------------------
# ORM tables
# ---------------------------------------------------------------------------

class PipelineRow(Base, AuditMixin):
    __tablename__ = "pipelines"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, default="")
    owner = Column(String(100), nullable=False)
    schedule = Column(String(50), nullable=False)
    source_system = Column(String(100), nullable=False)
    target_system = Column(String(100), nullable=False)
    status = Column(String(20), default=PipelineStatus.UNKNOWN.value)
    last_run = Column(DateTime, nullable=True)
    last_success = Column(DateTime, nullable=True)

    metrics = relationship("MetricRow", back_populates="pipeline", cascade="all, delete-orphan")
    alerts = relationship("AlertRow", back_populates="pipeline", cascade="all, delete-orphan")


class MetricRow(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True, autoincrement=True)
    pipeline_id = Column(Integer, ForeignKey("pipelines.id"), nullable=False)
    metric_type = Column(String(20), nullable=False)
    value = Column(Float, nullable=False)
    threshold = Column(Float, nullable=False)
    status = Column(String(10), nullable=False)
    timestamp = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))

    pipeline = relationship("PipelineRow", back_populates="metrics")


class AlertRow(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    pipeline_id = Column(Integer, ForeignKey("pipelines.id"), nullable=False)
    metric_type = Column(String(20), nullable=False)
    value = Column(Float, nullable=False)
    threshold = Column(Float, nullable=False)
    severity = Column(String(20), nullable=False)
    timestamp = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    acknowledged = Column(Boolean, default=False)
    ack_by = Column(String(100), nullable=True)
    ack_at = Column(DateTime, nullable=True)

    pipeline = relationship("PipelineRow", back_populates="alerts")


# ---------------------------------------------------------------------------
# Lifecycle helpers
# ---------------------------------------------------------------------------

def init_db() -> None:
    """Create all tables if they don't exist."""
    Base.metadata.create_all(_engine)


@contextmanager
def get_db() -> Generator[Session, None, None]:
    """Yield a scoped session, committing on success, rolling back on error."""
    session = _SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


# ---------------------------------------------------------------------------
# Metric evaluation logic
# ---------------------------------------------------------------------------

def evaluate_metric(value: float, threshold: float, metric_type: str) -> MetricStatus:
    """Determine PASS / WARN / FAIL for a given metric observation.

    Rules vary by metric type to account for directionality:
      - COMPLETENESS: higher is better (>= threshold = PASS)
      - TIMELINESS:   lower is better  (<= threshold = PASS)
      - FRESHNESS:    lower is better  (<= threshold hours = PASS)
      - VOLUME:       band check       (0.8x–1.5x threshold = healthy)
      - ACCURACY:     higher is better  (>= threshold = PASS)
    """
    mt = metric_type.upper()

    if mt == MetricType.COMPLETENESS.value:
        if value >= threshold:
            return MetricStatus.PASS
        if value >= threshold * 0.9:
            return MetricStatus.WARN
        return MetricStatus.FAIL

    if mt == MetricType.TIMELINESS.value:
        if value <= threshold:
            return MetricStatus.PASS
        if value <= threshold * 1.2:
            return MetricStatus.WARN
        return MetricStatus.FAIL

    if mt == MetricType.FRESHNESS.value:
        if value <= threshold:
            return MetricStatus.PASS
        return MetricStatus.FAIL

    if mt == MetricType.VOLUME.value:
        if value < threshold * 0.5:
            return MetricStatus.FAIL
        if value < threshold * 0.8 or value > threshold * 1.5:
            return MetricStatus.WARN
        return MetricStatus.PASS

    if mt == MetricType.ACCURACY.value:
        if value >= threshold:
            return MetricStatus.PASS
        return MetricStatus.FAIL

    # Fallback for unknown metric types
    return MetricStatus.WARN


# ---------------------------------------------------------------------------
# Query helpers
# ---------------------------------------------------------------------------

def get_pipeline_health(session: Session, pipeline_id: int) -> Optional[PipelineHealth]:
    """Aggregate recent metrics for a single pipeline into a health summary."""
    pipe = session.query(PipelineRow).filter(PipelineRow.id == pipeline_id).first()
    if not pipe:
        return None

    # Look at the most recent 30 days of metrics
    cutoff = datetime.now(timezone.utc) - timedelta(days=30)
    recent = (
        session.query(MetricRow)
        .filter(MetricRow.pipeline_id == pipeline_id, MetricRow.timestamp >= cutoff)
        .order_by(desc(MetricRow.timestamp))
        .all()
    )

    # Build per-metric-type summary (latest value)
    metrics_summary: dict = {}
    seen_types: set[str] = set()
    for m in recent:
        if m.metric_type not in seen_types:
            seen_types.add(m.metric_type)
            metrics_summary[m.metric_type] = {
                "value": m.value,
                "threshold": m.threshold,
                "status": m.status,
            }

    # Uptime: fraction of metric observations that passed
    total = len(recent)
    passed = sum(1 for m in recent if m.status == MetricStatus.PASS.value)
    uptime_pct = round((passed / total) * 100, 1) if total else 0.0

    # Average latency: use TIMELINESS values as proxy (ms)
    timeliness_vals = [m.value for m in recent if m.metric_type == MetricType.TIMELINESS.value]
    avg_latency = round(sum(timeliness_vals) / len(timeliness_vals), 1) if timeliness_vals else 0.0

    # Determine overall status from per-type statuses
    statuses = [v["status"] for v in metrics_summary.values()]
    if any(s == MetricStatus.FAIL.value for s in statuses):
        overall = PipelineStatus.FAILED
    elif any(s == MetricStatus.WARN.value for s in statuses):
        overall = PipelineStatus.DEGRADED
    elif statuses:
        overall = PipelineStatus.HEALTHY
    else:
        overall = PipelineStatus.UNKNOWN

    return PipelineHealth(
        pipeline_id=pipe.id,
        name=pipe.name,
        overall_status=overall,
        metrics_summary=metrics_summary,
        uptime_pct=uptime_pct,
        avg_latency_ms=avg_latency,
    )


def get_all_health(session: Session) -> list[PipelineHealth]:
    """Return health summaries for every registered pipeline."""
    pipes = session.query(PipelineRow).order_by(PipelineRow.name).all()
    results: list[PipelineHealth] = []
    for p in pipes:
        h = get_pipeline_health(session, p.id)
        if h:
            results.append(h)
    return results


def get_metric_trend(
    session: Session,
    pipeline_id: int,
    metric_type: str,
    days: int = 30,
) -> list[MetricRow]:
    """Return time-ordered metric observations for charting."""
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    return (
        session.query(MetricRow)
        .filter(
            MetricRow.pipeline_id == pipeline_id,
            MetricRow.metric_type == metric_type,
            MetricRow.timestamp >= cutoff,
        )
        .order_by(MetricRow.timestamp)
        .all()
    )


def get_active_alerts(
    session: Session,
    severity: Optional[str] = None,
    pipeline_id: Optional[int] = None,
) -> list[dict]:
    """Return unacknowledged alerts, optionally filtered."""
    q = (
        session.query(AlertRow, PipelineRow.name)
        .join(PipelineRow, AlertRow.pipeline_id == PipelineRow.id)
        .filter(AlertRow.acknowledged == False)  # noqa: E712
    )
    if severity:
        q = q.filter(AlertRow.severity == severity)
    if pipeline_id:
        q = q.filter(AlertRow.pipeline_id == pipeline_id)

    q = q.order_by(desc(AlertRow.timestamp))
    results = []
    for alert, pipe_name in q.all():
        results.append({
            "id": alert.id,
            "pipeline_id": alert.pipeline_id,
            "pipeline_name": pipe_name,
            "metric_type": alert.metric_type,
            "value": alert.value,
            "threshold": alert.threshold,
            "severity": alert.severity,
            "timestamp": alert.timestamp,
            "acknowledged": alert.acknowledged,
        })
    return results


def acknowledge_alert(session: Session, alert_id: int, ack_by: str) -> Optional[AlertRow]:
    """Mark an alert as acknowledged."""
    alert = session.query(AlertRow).filter(AlertRow.id == alert_id).first()
    if not alert:
        return None
    alert.acknowledged = True
    alert.ack_by = ack_by
    alert.ack_at = datetime.now(timezone.utc)
    return alert
