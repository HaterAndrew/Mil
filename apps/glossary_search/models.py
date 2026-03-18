"""Pydantic V2 models for the Glossary Search application."""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class TermCategory(str, Enum):
    """Classification categories for indexed terms."""

    GLOSSARY = "GLOSSARY"
    DOCTRINE = "DOCTRINE"
    ACRONYM = "ACRONYM"
    CONCEPT = "CONCEPT"


class TermEntry(BaseModel):
    """A single glossary/doctrine term with its definition and provenance."""

    id: int = 0
    term: str
    definition: str
    source_file: str
    source_line: int
    category: TermCategory

    model_config = {"from_attributes": True}


class SearchQuery(BaseModel):
    """Inbound search request parameters."""

    query: str = Field(..., min_length=1, description="Search string")
    category: Optional[TermCategory] = Field(
        default=None, description="Filter by category"
    )
    limit: int = Field(default=20, ge=1, le=200, description="Max results")


class SearchResult(BaseModel):
    """Search response payload."""

    query: str
    total_hits: int
    results: list[TermEntry]
    search_time_ms: float


class CategoryCount(BaseModel):
    """Term count for a single category."""

    category: str
    count: int


class IndexStats(BaseModel):
    """Aggregate statistics about the indexed corpus."""

    total_terms: int
    by_category: list[CategoryCount]
    source_files: int
