"""Pydantic V2 request/response models for the Enrollment Manager."""

from __future__ import annotations

from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, Field, field_validator


# ---------------------------------------------------------------------------
# Training Class
# ---------------------------------------------------------------------------
class TrainingClassCreate(BaseModel):
    course_id: str = Field(..., min_length=1, max_length=10)
    class_name: str = Field(..., min_length=1, max_length=100)
    start_date: date
    end_date: date
    location: str = Field(..., min_length=1, max_length=100)
    max_seats: int = Field(..., gt=0, le=200)
    instructor_name: str | None = Field(None, max_length=100)
    status: Literal["SCHEDULED", "IN_PROGRESS", "COMPLETED", "CANCELLED"] = "SCHEDULED"

    @field_validator("class_name", "location")
    @classmethod
    def strip_whitespace(cls, v: str) -> str:
        return v.strip()


class TrainingClassResponse(BaseModel):
    class_id: int
    course_id: str
    class_name: str
    start_date: date
    end_date: date
    location: str
    max_seats: int
    instructor_name: str | None = None
    status: str
    created_at: datetime | None = None
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Enrollment
# ---------------------------------------------------------------------------
class EnrollmentCreate(BaseModel):
    dodid: str = Field(..., min_length=10, max_length=10, pattern=r"^\d{10}$")
    last_name: str = Field(..., min_length=1, max_length=50)
    first_name: str = Field(..., min_length=1, max_length=50)
    rank: str = Field(..., min_length=1, max_length=10)
    unit: str = Field(..., min_length=1, max_length=50)

    @field_validator("last_name", "first_name", "rank", "unit")
    @classmethod
    def strip_and_upper(cls, v: str) -> str:
        return v.strip().upper()


class EnrollmentResponse(BaseModel):
    id: int
    class_id: int
    dodid: str
    last_name: str
    first_name: str
    rank: str
    unit: str
    enrollment_date: date
    status: str
    seat_number: int | None = None
    created_at: datetime | None = None
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Waitlist
# ---------------------------------------------------------------------------
class WaitlistResponse(BaseModel):
    id: int
    class_id: int
    dodid: str
    last_name: str
    first_name: str
    rank: str
    unit: str
    request_date: date
    priority: int
    status: str
    created_at: datetime | None = None
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Availability & Stats
# ---------------------------------------------------------------------------
class ClassAvailability(BaseModel):
    class_id: int
    class_name: str
    max_seats: int
    enrolled_count: int
    seats_remaining: int
    waitlist_count: int
    fill_pct: float


class EnrollmentStats(BaseModel):
    total_classes: int
    active_classes: int
    total_enrolled: int
    total_waitlisted: int
    avg_fill_rate: float


# ---------------------------------------------------------------------------
# Batch operations
# ---------------------------------------------------------------------------
class BatchStatusUpdate(BaseModel):
    dodids: list[str] = Field(..., min_length=1)
    new_status: Literal["DROPPED", "COMPLETED", "NO_SHOW"] = Field(...)

    @field_validator("dodids")
    @classmethod
    def validate_dodids(cls, v: list[str]) -> list[str]:
        for d in v:
            if not d.isdigit() or len(d) != 10:
                raise ValueError(f"Invalid DODID: {d}")
        return v


# ---------------------------------------------------------------------------
# Course distribution
# ---------------------------------------------------------------------------
class CourseDistribution(BaseModel):
    course_id: str
    total_classes: int
    total_enrolled: int
    total_waitlisted: int
    avg_fill_rate: float
    locations: list[str]
