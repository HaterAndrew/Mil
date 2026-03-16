"""Pydantic V2 models for the AAR Aggregator."""

from __future__ import annotations

from datetime import date
from typing import Literal

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Child item models
# ---------------------------------------------------------------------------
class ImproveItemCreate(BaseModel):
    problem: str = Field(..., min_length=1)
    proposed_fix: str | None = None
    owner: str | None = None
    priority: Literal["H", "M", "L"] = "M"
    category: Literal[
        "INTELLIGENCE", "FIRES", "MOVEMENT_MANEUVER",
        "SUSTAINMENT", "PROTECTION", "MISSION_COMMAND",
    ] | None = None


class ImproveItemOut(ImproveItemCreate):
    id: int
    aar_id: int
    model_config = {"from_attributes": True}


class StudentEvalCreate(BaseModel):
    trainee_name: str = Field(..., min_length=1)
    tm_level: str = Field(..., pattern=r"^TM-\d{2}[A-L]?$")
    result: Literal["GO", "NO_GO"]
    notes: str | None = None


class StudentEvalOut(StudentEvalCreate):
    id: int
    model_config = {"from_attributes": True}


class DiscrepancyCreate(BaseModel):
    document: str = Field(..., min_length=1)
    section_page: str = Field(..., min_length=1)
    issue_description: str = Field(..., min_length=1)
    severity: Literal["H", "M", "L"]


class DiscrepancyOut(DiscrepancyCreate):
    id: int
    model_config = {"from_attributes": True}


class EnvIssueCreate(BaseModel):
    issue: str = Field(..., min_length=1)
    impact: str = Field(..., min_length=1)
    resolution: str | None = None


class EnvIssueOut(EnvIssueCreate):
    id: int
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# AAR
# ---------------------------------------------------------------------------
class AARCreate(BaseModel):
    date: date
    tm_levels: list[str] = Field(..., min_length=1)
    exercises: list[str] = []
    location: str = Field(..., min_length=1)
    student_count: int = Field(..., gt=0)
    instructor_names: list[str] = Field(..., min_length=1)
    planned_objectives: str = Field(..., min_length=1)
    actual_execution: str = Field(..., min_length=1)
    sustains: list[str] = Field(..., min_length=1)
    improves: list[ImproveItemCreate] = []
    evaluations: list[StudentEvalCreate] = []
    discrepancies: list[DiscrepancyCreate] = []
    env_issues: list[EnvIssueCreate] = []
    instructor_recommendations: str | None = None
    submitted_by: str = Field(..., min_length=1)


class AARSummary(BaseModel):
    id: int
    date: date
    tm_levels: list[str]
    location: str
    student_count: int
    submitted_by: str
    sustain_count: int = 0
    improve_count: int = 0
    model_config = {"from_attributes": True}


class AARDetail(BaseModel):
    id: int
    date: date
    tm_levels: list[str]
    exercises: list[str]
    location: str
    student_count: int
    instructor_names: list[str]
    planned_objectives: str
    actual_execution: str
    instructor_recommendations: str | None
    submitted_by: str
    sustains: list[str]
    improves: list[ImproveItemOut]
    evaluations: list[StudentEvalOut]
    discrepancies: list[DiscrepancyOut]
    env_issues: list[EnvIssueOut]
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Analytics
# ---------------------------------------------------------------------------
class RecurringIssue(BaseModel):
    problem: str
    count: int
    aar_ids: list[int]
    dates: list[str | None]
    category: str | None
    priority: str | None


class TrendByCategory(BaseModel):
    category: str
    count: int


class MonthlyTrend(BaseModel):
    month: str
    improve_count: int


# ---------------------------------------------------------------------------
# Upload
# ---------------------------------------------------------------------------
class ParsedAARPreview(BaseModel):
    """Preview of a parsed AAR file — for human review before saving."""
    parsed: dict
    warnings: list[str] = []
