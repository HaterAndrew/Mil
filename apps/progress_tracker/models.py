"""Pydantic V2 request/response models for the Progress Tracker."""

from __future__ import annotations

from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, Field, field_validator


# ---------------------------------------------------------------------------
# Status enum values
# ---------------------------------------------------------------------------
MilestoneStatus = Literal["ON_TRACK", "AT_RISK", "OVERDUE", "COMPLETE"]


# ---------------------------------------------------------------------------
# Milestones
# ---------------------------------------------------------------------------
class MilestoneCreate(BaseModel):
    dodid: str = Field(..., min_length=10, max_length=10, pattern=r"^\d{10}$")
    course_id: str = Field(..., pattern=r"^(TM-\d{2}[A-HJ-O]?|FBC)$")
    target_date: date
    notes: str | None = Field(None, max_length=500)


class MilestoneResponse(BaseModel):
    id: int
    dodid: str
    course_id: str
    target_date: date
    status: MilestoneStatus
    notes: str | None = None
    days_remaining: int
    created_at: datetime | None = None
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Training Record
# ---------------------------------------------------------------------------
class MilestoneRecordItem(BaseModel):
    course_id: str
    course_name: str
    target_date: date
    status: MilestoneStatus
    days_remaining: int
    notes: str | None = None


class TrainingRecordOut(BaseModel):
    dodid: str
    name: str
    rank: str
    unit: str
    milestones: list[MilestoneRecordItem] = []
    overall_status: MilestoneStatus
    pct_complete: float


# ---------------------------------------------------------------------------
# Goals
# ---------------------------------------------------------------------------
class GoalCreate(BaseModel):
    dodid: str = Field(..., min_length=10, max_length=10, pattern=r"^\d{10}$")
    target_course: str = Field(..., pattern=r"^(TM-\d{2}[A-HJ-O]?|FBC)$")
    target_date: date


class GoalResponse(BaseModel):
    id: int
    dodid: str
    target_course: str
    target_date: date
    achieved: bool
    eligible: bool
    missing_prereqs: list[str] = []
    created_at: datetime | None = None
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Stalled soldier summary
# ---------------------------------------------------------------------------
class StalledSoldier(BaseModel):
    dodid: str
    name: str
    rank: str
    unit: str
    last_completion_date: date | None = None
    days_since_activity: int
    furthest_course: str | None = None
