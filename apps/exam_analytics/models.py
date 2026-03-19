"""Pydantic V2 models for the Exam Analytics Dashboard."""

from __future__ import annotations

from datetime import date
from typing import Literal

from pydantic import BaseModel, Field, field_validator, model_validator


# ---------------------------------------------------------------------------
# Exam session
# ---------------------------------------------------------------------------
class ExamSessionCreate(BaseModel):
    course_id: str = Field(..., pattern=r"^TM-\d{2}[A-HJ-O]?$")
    form_type: Literal["PRE", "POST"]
    administration_date: date
    cohort_label: str = Field(..., min_length=1, max_length=100)


class ExamSessionResponse(ExamSessionCreate):
    id: int
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Question score
# ---------------------------------------------------------------------------
class QuestionScoreCreate(BaseModel):
    question_number: int = Field(..., ge=1, le=20)
    question_type: Literal["MC", "SA"]
    points_possible: int
    points_awarded: int = Field(..., ge=0)

    @model_validator(mode="after")
    def validate_points(self):
        if self.question_type == "MC" and self.points_possible != 2:
            raise ValueError("MC questions must have 2 points possible")
        if self.question_type == "SA" and self.points_possible != 6:
            raise ValueError("SA questions must have 6 points possible")
        if self.points_awarded > self.points_possible:
            raise ValueError(
                f"Points awarded ({self.points_awarded}) cannot exceed "
                f"points possible ({self.points_possible})"
            )
        return self


class QuestionScoreResponse(QuestionScoreCreate):
    id: int
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Exam result
# ---------------------------------------------------------------------------
class ExamResultCreate(BaseModel):
    trainee_id: str = Field(..., min_length=1, max_length=100)
    total_score: int = Field(..., ge=0)
    total_possible: int = Field(60, ge=1)
    score_percent: float = Field(..., ge=0, le=100)
    result: Literal["PASS", "FAIL", "DIAGNOSTIC"]
    question_scores: list[QuestionScoreCreate] = []

    @model_validator(mode="after")
    def validate_score_consistency(self):
        if self.total_score > self.total_possible:
            raise ValueError("total_score cannot exceed total_possible")
        return self


class ExamResultResponse(BaseModel):
    id: int
    trainee_id: str
    total_score: int
    total_possible: int
    score_percent: float
    result: str
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Analytics responses
# ---------------------------------------------------------------------------
class GainScoreResponse(BaseModel):
    trainee_id: str
    pre_percent: float
    post_percent: float
    absolute_gain: float
    normalized_gain: float


class QuestionDifficulty(BaseModel):
    question_number: int
    question_type: str
    percent_correct: float
    avg_points: float
    num_responses: int


class CohortSummary(BaseModel):
    session_id: int
    course_id: str
    form_type: str
    cohort_label: str
    num_students: int
    avg_score: float
    median_score: float
    pass_rate: float
    min_score: float
    max_score: float


# ---------------------------------------------------------------------------
# Upload
# ---------------------------------------------------------------------------
class UploadResult(BaseModel):
    accepted: int
    rejected: int
    errors: list[str] = []
