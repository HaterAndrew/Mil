"""MTT Scheduler — Pydantic V2 request/response models."""

from __future__ import annotations

from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, Field, field_validator


# ---------------------------------------------------------------------------
# Events
# ---------------------------------------------------------------------------
class EventCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    course_id: str = Field(..., min_length=1, max_length=10)
    location: str = Field(..., min_length=1, max_length=100)
    start_date: date
    end_date: date
    max_capacity: int = Field(..., ge=1, le=200)
    venue_id: int | None = None
    notes: str | None = None

    @field_validator("end_date")
    @classmethod
    def end_after_start(cls, v: date, info) -> date:
        start = info.data.get("start_date")
        if start and v < start:
            msg = "end_date must be on or after start_date"
            raise ValueError(msg)
        return v


class EventResponse(BaseModel):
    id: int
    name: str
    course_id: str
    location: str
    start_date: date
    end_date: date
    max_capacity: int
    status: Literal["PLANNED", "ACTIVE", "COMPLETE", "CANCELLED"]
    venue_id: int | None = None
    notes: str | None = None
    enrolled_count: int = 0
    created_at: datetime | None = None
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Instructors
# ---------------------------------------------------------------------------
class InstructorCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    rank: str = Field(..., min_length=1, max_length=10)
    unit: str = Field(..., min_length=1, max_length=50)
    qualifications: list[str] = Field(default_factory=list)
    available_from: date
    available_to: date

    @field_validator("name", "rank", "unit")
    @classmethod
    def strip_and_upper(cls, v: str) -> str:
        return v.strip().upper()


class InstructorResponse(BaseModel):
    id: int
    name: str
    rank: str
    unit: str
    qualifications: list[str] = []
    available_from: date
    available_to: date
    assigned_events: int = 0
    created_at: datetime | None = None
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Enrollments
# ---------------------------------------------------------------------------
class EnrollmentCreate(BaseModel):
    event_id: int
    dodid: str = Field(..., min_length=10, max_length=10, pattern=r"^\d{10}$")
    soldier_name: str = Field(..., min_length=1, max_length=100)
    soldier_rank: str = Field(..., min_length=1, max_length=10)
    soldier_unit: str = Field(..., min_length=1, max_length=50)

    @field_validator("soldier_name", "soldier_rank", "soldier_unit")
    @classmethod
    def strip_and_upper(cls, v: str) -> str:
        return v.strip().upper()


class EnrollmentResponse(BaseModel):
    id: int
    event_id: int
    dodid: str
    soldier_name: str
    soldier_rank: str
    soldier_unit: str
    status: Literal["ENROLLED", "COMPLETE", "NO_SHOW", "DROPPED"]
    created_at: datetime | None = None
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Venues
# ---------------------------------------------------------------------------
class VenueCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    location: str = Field(..., min_length=1, max_length=100)
    capacity: int = Field(..., ge=1, le=500)
    has_network: bool = False
    has_sipr: bool = False
    notes: str | None = None


class VenueResponse(BaseModel):
    id: int
    name: str
    location: str
    capacity: int
    has_network: bool
    has_sipr: bool
    notes: str | None = None
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Schedule Conflict
# ---------------------------------------------------------------------------
class ScheduleConflict(BaseModel):
    instructor_name: str
    event1: str
    event2: str
    overlap_dates: str
