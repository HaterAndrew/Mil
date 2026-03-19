"""Pydantic V2 request/response models for the Lessons Learned Pipeline."""

from __future__ import annotations

from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Lesson
# ---------------------------------------------------------------------------
class LessonCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: str = Field(..., min_length=1)
    source_type: Literal["AAR", "EXERCISE", "FIELD_OBSERVATION", "STUDENT_FEEDBACK", "INSTRUCTOR_NOTE"]
    source_reference: str | None = Field(None, max_length=200)
    submitted_by: str = Field(..., min_length=1, max_length=100)
    submit_date: date
    status: Literal["NEW", "VALIDATED", "ACTIONABLE", "IMPLEMENTED", "ARCHIVED"] = "NEW"
    priority: Literal["HIGH", "MEDIUM", "LOW"] = "MEDIUM"


class LessonResponse(BaseModel):
    id: int
    title: str
    description: str
    source_type: str
    source_reference: str | None = None
    submitted_by: str
    submit_date: date
    status: str
    priority: str
    created_at: datetime | None = None
    tags: list[LessonTagOut] = []
    action_items: list[ActionItemResponse] = []
    comments: list[CommentOut] = []
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Tags
# ---------------------------------------------------------------------------
class LessonTagCreate(BaseModel):
    tag_type: Literal["TTP_CATEGORY", "ECHELON", "WFF", "DOCTRINE_REF", "COURSE_ID", "KEYWORD"]
    tag_value: str = Field(..., min_length=1, max_length=100)


class LessonTagOut(BaseModel):
    id: int
    tag_type: str
    tag_value: str
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Action Items
# ---------------------------------------------------------------------------
class ActionItemCreate(BaseModel):
    description: str = Field(..., min_length=1)
    assigned_to: str | None = Field(None, max_length=100)
    due_date: date | None = None
    status: Literal["OPEN", "IN_PROGRESS", "COMPLETED", "CANCELLED"] = "OPEN"


class ActionItemResponse(BaseModel):
    id: int
    lesson_id: int
    description: str
    assigned_to: str | None = None
    due_date: date | None = None
    status: str
    completed_date: date | None = None
    created_at: datetime | None = None
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Comments
# ---------------------------------------------------------------------------
class CommentCreate(BaseModel):
    author: str = Field(..., min_length=1, max_length=100)
    comment_text: str = Field(..., min_length=1)


class CommentOut(BaseModel):
    id: int
    author: str
    comment_text: str
    comment_date: datetime
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Analytics responses
# ---------------------------------------------------------------------------
class TagFrequency(BaseModel):
    tag_value: str
    count: int


class PipelineStats(BaseModel):
    total_lessons: int
    by_status: dict[str, int] = {}
    by_priority: dict[str, int] = {}
    by_source_type: dict[str, int] = {}


class CrossReference(BaseModel):
    tag_a: str
    tag_b: str
    count: int


# ---------------------------------------------------------------------------
# Forward reference resolution (LessonResponse uses nested models)
# ---------------------------------------------------------------------------
LessonResponse.model_rebuild()
