"""Pydantic V2 request/response models for the Curriculum Tracker."""

from __future__ import annotations

from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Document
# ---------------------------------------------------------------------------
class DocumentResponse(BaseModel):
    doc_id: int
    file_path: str
    doc_type: str
    course_id: str | None = None
    title: str
    current_version: str
    last_modified: datetime | None = None
    file_hash: str | None = None
    created_at: datetime | None = None
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Review Cycle
# ---------------------------------------------------------------------------
class ReviewCycleCreate(BaseModel):
    doc_id: int
    review_type: Literal["SCHEDULED", "AD_HOC", "POST_EXERCISE"]
    reviewer_name: str = Field(..., min_length=1, max_length=100)
    review_date: date
    status: Literal["APPROVED", "CHANGES_REQUIRED", "IN_REVIEW", "OVERDUE"]
    notes: str | None = None
    next_review_date: date | None = None


class ReviewCycleResponse(BaseModel):
    id: int
    doc_id: int
    review_type: str
    reviewer_name: str
    review_date: date
    status: str
    notes: str | None = None
    next_review_date: date | None = None
    created_at: datetime | None = None
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Change Log
# ---------------------------------------------------------------------------
class ChangeLogResponse(BaseModel):
    id: int
    doc_id: int
    change_date: datetime
    previous_hash: str | None = None
    new_hash: str | None = None
    change_summary: str | None = None
    changed_by: str | None = None
    created_at: datetime | None = None
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Reports
# ---------------------------------------------------------------------------
class FreshnessReport(BaseModel):
    doc_type: str
    doc_count: int
    avg_days_since_review: float | None = None
    never_reviewed: int = 0


class ReviewSummary(BaseModel):
    approved: int = 0
    changes_required: int = 0
    in_review: int = 0
    overdue: int = 0


class ScanResult(BaseModel):
    new: int = 0
    changed: int = 0
    unchanged: int = 0
