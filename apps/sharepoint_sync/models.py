"""Pydantic V2 models for the SharePoint Sync API."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Sync status / diff
# ---------------------------------------------------------------------------
class SyncStatus(BaseModel):
    """Current sync state summary."""

    total_files: int
    added: int
    modified: int
    deleted: int
    unchanged: int
    in_sync: bool


class FileDiff(BaseModel):
    """Categorized file lists from a diff comparison."""

    added: list[str] = []
    modified: list[str] = []
    deleted: list[str] = []
    unchanged: list[str] = []


# ---------------------------------------------------------------------------
# Sync records
# ---------------------------------------------------------------------------
class SyncRecordCreate(BaseModel):
    """Payload for recording a new sync baseline."""

    notes: str = Field("", max_length=500, description="Optional sync notes")


class SyncRecordResponse(BaseModel):
    """Stored sync record returned by the API."""

    id: int
    timestamp: datetime
    total_files: int
    added: int
    modified: int
    deleted: int
    notes: str | None = None

    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# SharePoint variants
# ---------------------------------------------------------------------------
class SharePointVariant(BaseModel):
    """A file with _sharepoint suffix and its standard counterpart."""

    sharepoint_path: str
    standard_path: str
    sharepoint_exists: bool
    standard_exists: bool
    status: str = "OK"  # OK, STALE, MISSING
