"""Pydantic V2 models for the Data Quality Monitor."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

class PipelineStatus(str, Enum):
    HEALTHY = "HEALTHY"
    DEGRADED = "DEGRADED"
    FAILED = "FAILED"
    UNKNOWN = "UNKNOWN"


class MetricType(str, Enum):
    COMPLETENESS = "COMPLETENESS"
    TIMELINESS = "TIMELINESS"
    ACCURACY = "ACCURACY"
    FRESHNESS = "FRESHNESS"
    VOLUME = "VOLUME"


class MetricStatus(str, Enum):
    PASS = "PASS"
    WARN = "WARN"
    FAIL = "FAIL"


class AlertSeverity(str, Enum):
    CRITICAL = "CRITICAL"
    WARNING = "WARNING"
    INFO = "INFO"


# ---------------------------------------------------------------------------
# Pipeline models
# ---------------------------------------------------------------------------

class PipelineCreate(BaseModel):
    """Payload for creating a new pipeline registration."""
    name: str = Field(..., max_length=100, description="Pipeline display name")
    description: str = Field("", description="Free-text description")
    owner: str = Field(..., max_length=100, description="Responsible POC")
    schedule: str = Field(..., max_length=50, description="Run schedule, e.g. 'daily 0600Z'")
    source_system: str = Field(..., max_length=100, description="Upstream system name")
    target_system: str = Field(..., max_length=100, description="Downstream system name")


class PipelineResponse(PipelineCreate):
    """Full pipeline record returned by the API."""
    id: int
    status: PipelineStatus = PipelineStatus.UNKNOWN
    last_run: Optional[datetime] = None
    last_success: Optional[datetime] = None

    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Metric models
# ---------------------------------------------------------------------------

class MetricCreate(BaseModel):
    """Payload for recording a metric observation."""
    pipeline_id: int
    metric_type: MetricType
    value: float = Field(..., description="Observed metric value")
    threshold: float = Field(..., description="Pass/fail threshold")
    timestamp: Optional[datetime] = Field(
        default=None,
        description="Observation time; defaults to server time if omitted",
    )


class MetricResponse(BaseModel):
    """Metric record with computed status."""
    id: int
    pipeline_id: int
    metric_type: MetricType
    value: float
    threshold: float
    status: MetricStatus
    timestamp: datetime

    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Alert models
# ---------------------------------------------------------------------------

class AlertOut(BaseModel):
    """Active alert returned by the API."""
    id: int
    pipeline_id: int
    pipeline_name: str
    metric_type: MetricType
    value: float
    threshold: float
    severity: AlertSeverity
    timestamp: datetime
    acknowledged: bool = False

    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Health / dashboard models
# ---------------------------------------------------------------------------

class PipelineHealth(BaseModel):
    """Aggregated health summary for a single pipeline."""
    pipeline_id: int
    name: str
    overall_status: PipelineStatus
    metrics_summary: dict  # metric_type -> {value, threshold, status}
    uptime_pct: float
    avg_latency_ms: float
