"""Pydantic V2 request/response models for the Instructor Certification Manager."""

from __future__ import annotations

from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, Field, field_validator


# ---------------------------------------------------------------------------
# Instructor
# ---------------------------------------------------------------------------
class InstructorCreate(BaseModel):
    instructor_id: str = Field(..., min_length=1, max_length=10)
    last_name: str = Field(..., min_length=1, max_length=50)
    first_name: str = Field(..., min_length=1, max_length=50)
    rank: str = Field(..., min_length=1, max_length=10)
    unit: str = Field(..., min_length=1, max_length=50)
    mos: str = Field(..., min_length=1, max_length=10)
    email: str | None = Field(None, max_length=100)
    phone: str | None = Field(None, max_length=20)
    status: Literal["ACTIVE", "INACTIVE", "TDY"] = "ACTIVE"

    @field_validator("last_name", "first_name", "rank", "unit", "mos")
    @classmethod
    def strip_and_upper(cls, v: str) -> str:
        return v.strip().upper()


class InstructorResponse(BaseModel):
    instructor_id: str
    last_name: str
    first_name: str
    rank: str
    unit: str
    mos: str
    email: str | None = None
    phone: str | None = None
    status: str
    created_at: datetime | None = None
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Certification
# ---------------------------------------------------------------------------
class CertificationCreate(BaseModel):
    instructor_id: str = Field(..., min_length=1, max_length=10)
    course_id: str = Field(..., min_length=1, max_length=10)
    certified_date: date
    expiration_date: date
    certifying_authority: str | None = Field(None, max_length=100)
    status: Literal["CURRENT", "EXPIRED", "PENDING"] = "CURRENT"


class CertificationResponse(BaseModel):
    id: int
    instructor_id: str
    course_id: str
    certified_date: date
    expiration_date: date
    certifying_authority: str | None = None
    status: str
    created_at: datetime | None = None
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Teaching History
# ---------------------------------------------------------------------------
class TeachingHistoryCreate(BaseModel):
    instructor_id: str = Field(..., min_length=1, max_length=10)
    course_id: str = Field(..., min_length=1, max_length=10)
    event_date: date
    location: str | None = Field(None, max_length=100)
    students_count: int | None = Field(None, ge=0)
    rating: Literal["EXCELLENT", "SATISFACTORY", "NEEDS_IMPROVEMENT"] | None = None
    notes: str | None = Field(None, max_length=500)


class TeachingHistoryResponse(BaseModel):
    id: int
    instructor_id: str
    course_id: str
    event_date: date
    location: str | None = None
    students_count: int | None = None
    rating: str | None = None
    notes: str | None = None
    created_at: datetime | None = None
    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Coverage report
# ---------------------------------------------------------------------------
class CoverageReport(BaseModel):
    course_id: str
    course_name: str
    hours: int
    certified_count: int
    rag: Literal["GREEN", "AMBER", "RED"]


# ---------------------------------------------------------------------------
# Expiration alert
# ---------------------------------------------------------------------------
class ExpirationAlert(BaseModel):
    cert_id: int
    instructor_id: str
    rank: str
    last_name: str
    first_name: str
    unit: str
    course_id: str
    course_name: str
    expiration_date: str
    days_remaining: int
    rag: Literal["GREEN", "AMBER", "RED"]
