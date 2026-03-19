"""Pydantic V2 models for the Offline Package Builder."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Package request / response
# ---------------------------------------------------------------------------
class PackageRequest(BaseModel):
    """Payload for building an offline package."""

    selected_tms: list[str] = Field(..., min_length=1, description="TM identifiers to include")
    include_syllabi: bool = Field(True, description="Include matching syllabi")
    include_exercises: bool = Field(True, description="Include matching exercises and exams")
    include_pdfs: bool = Field(True, description="Include PDF versions")
    include_doctrine: bool = Field(False, description="Include doctrine publications")
    include_quick_ref: bool = Field(False, description="Include quick reference files")


class PackageRecord(BaseModel):
    """Stored record of a previously built package."""

    id: int
    created_at: datetime
    selected_tms: list[str]
    total_items: int
    size_kb: int
    include_pdfs: bool
    notes: str | None = None

    model_config = {"from_attributes": True}


class PackageSummary(BaseModel):
    """Preview of what a package will contain before building."""

    selected_tms: list[str]
    auto_included_prereqs: dict[str, list[str]]
    all_tms: list[str]
    estimated_size_kb: int
    item_counts: dict[str, int]


class InventoryCategory(BaseModel):
    """Summary of available content in one category."""

    category: str
    item_count: int
    total_size_kb: int
    items: list[str]


class InventoryResponse(BaseModel):
    """Full content inventory across all categories."""

    categories: list[InventoryCategory]
    total_items: int
    total_size_kb: int
