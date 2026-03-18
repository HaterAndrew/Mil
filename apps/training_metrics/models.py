"""Pydantic V2 request/response models for the Training Metrics Executive Dashboard."""

from __future__ import annotations

from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Snapshot CRUD
# ---------------------------------------------------------------------------
class SnapshotCreate(BaseModel):
    report_type: Literal["WEEKLY", "MONTHLY", "QUARTERLY"] = "WEEKLY"
    generated_by: str = Field(..., min_length=1, max_length=100)
    notes: str | None = None


class SnapshotResponse(BaseModel):
    id: int
    report_date: date
    report_type: str
    generated_by: str
    data_json: str  # raw JSON blob — consumers parse as needed
    notes: str | None = None
    created_at: datetime
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Risk items surfaced by auto-scan
# ---------------------------------------------------------------------------
class RiskItem(BaseModel):
    description: str
    severity: Literal["HIGH", "MEDIUM", "LOW"]
    source_app: str
    recommended_action: str


# ---------------------------------------------------------------------------
# Executive summary — the four CG questions
# ---------------------------------------------------------------------------
class ExecutiveSummary(BaseModel):
    readiness_score: float = Field(..., ge=0, le=100, description="Weighted avg of key metrics")
    on_track: str
    at_risk: str
    what_changed: str
    decision_required: str
    rag: Literal["GREEN", "AMBER", "RED"]


# ---------------------------------------------------------------------------
# Full metrics bundle returned by /metrics
# ---------------------------------------------------------------------------
class MetricsBundle(BaseModel):
    """Aggregated KPIs from all MSS Training apps."""

    # Readiness tracker
    total_trainees: int = 0
    funnel: list[dict] = []
    unit_summary: list[dict] = []
    bottleneck_top3: list[dict] = []

    # Exam analytics
    exam_pass_rate: float | None = None
    exam_sessions_count: int = 0

    # AAR aggregator
    total_aars: int = 0
    top_issues: list[dict] = []

    # Progress tracker
    overdue_milestones: int = 0

    # MTT scheduler
    upcoming_events: int = 0

    # Data quality
    active_alerts: int = 0

    # Instructor manager (optional)
    expiring_certs: int = 0
    coverage_gaps: int = 0

    # Enrollment manager (optional)
    fill_rate: float | None = None
    waitlisted_count: int = 0

    # Curriculum tracker (optional)
    overdue_reviews: int = 0
    stale_docs: int = 0

    # Lessons learned (optional)
    open_action_items: int = 0
    lessons_this_month: int = 0

    # Computed
    risks: list[RiskItem] = []
    executive_summary: ExecutiveSummary | None = None
