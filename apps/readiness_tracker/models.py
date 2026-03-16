"""Pydantic V2 request/response models for the Training Readiness Tracker."""

from __future__ import annotations

from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, Field, field_validator


# ---------------------------------------------------------------------------
# Trainee
# ---------------------------------------------------------------------------
class TraineeCreate(BaseModel):
    dodid: str = Field(..., min_length=10, max_length=10, pattern=r"^\d{10}$")
    last_name: str = Field(..., min_length=1, max_length=50)
    first_name: str = Field(..., min_length=1, max_length=50)
    rank: str = Field(..., min_length=1, max_length=10)
    unit: str = Field(..., min_length=1, max_length=50)
    mos: str | None = Field(None, max_length=10)

    @field_validator("last_name", "first_name", "rank", "unit")
    @classmethod
    def strip_and_upper(cls, v: str) -> str:
        return v.strip().upper()


class CompletionOut(BaseModel):
    id: int
    course_id: str
    result: str
    evaluation_date: date
    evaluator_name: str | None = None
    model_config = {"from_attributes": True}


class TraineeResponse(BaseModel):
    dodid: str
    last_name: str
    first_name: str
    rank: str
    unit: str
    mos: str | None = None
    completions: list[CompletionOut] = []
    eligible_courses: list[str] = []
    next_recommended: list[str] = []
    model_config = {"from_attributes": True}


class TraineeListItem(BaseModel):
    dodid: str
    last_name: str
    first_name: str
    rank: str
    unit: str
    mos: str | None = None
    completion_count: int = 0
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Completion
# ---------------------------------------------------------------------------
class CompletionCreate(BaseModel):
    dodid: str = Field(..., pattern=r"^\d{10}$")
    course_id: str = Field(..., pattern=r"^(TM-\d{2}[A-L]?|BSP)$")
    result: Literal["GO", "NO_GO"]
    evaluation_date: date
    evaluator_name: str | None = None


class CompletionResponse(CompletionCreate):
    id: int
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Eligibility
# ---------------------------------------------------------------------------
class EligibilityCheck(BaseModel):
    dodid: str
    target_course: str
    eligible: bool
    missing_prereqs: list[str]


# ---------------------------------------------------------------------------
# Unit rollup
# ---------------------------------------------------------------------------
class UnitRollup(BaseModel):
    unit: str
    total_trainees: int
    course_counts: dict[str, int]


# ---------------------------------------------------------------------------
# CSV upload results
# ---------------------------------------------------------------------------
class UploadResult(BaseModel):
    accepted: int
    rejected: int
    errors: list[str] = []
