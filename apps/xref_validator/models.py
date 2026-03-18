"""Cross-Reference Validator — Pydantic V2 request/response models."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------
class IssueType(str, Enum):
    BROKEN_LINK = "BROKEN_LINK"
    STALE_REF = "STALE_REF"
    MISSING_FILE = "MISSING_FILE"
    PREREQ_MISMATCH = "PREREQ_MISMATCH"
    CHAPTER_REF_ERROR = "CHAPTER_REF_ERROR"


class Severity(str, Enum):
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"


# ---------------------------------------------------------------------------
# Scan request
# ---------------------------------------------------------------------------
import os

MAVEN_TRAINING_DEFAULT = os.environ.get(
    "MAVEN_TRAINING_ROOT",
    str(Path(__file__).resolve().parent.parent.parent / "maven_training"),
)


class ScanRequest(BaseModel):
    """Parameters for a cross-reference validation scan."""

    root_path: str = Field(
        default=MAVEN_TRAINING_DEFAULT,
        description="Root directory of the documentation corpus to scan.",
    )
    patterns: list[str] = Field(
        default=["**/*.md", "**/*.html"],
        description="Glob patterns for files to include in the scan.",
    )


# ---------------------------------------------------------------------------
# Validation issue
# ---------------------------------------------------------------------------
class ValidationIssue(BaseModel):
    """A single cross-reference problem found during scanning."""

    file_path: str
    line_number: int
    issue_type: IssueType
    severity: Severity
    description: str
    suggested_fix: str = ""


# ---------------------------------------------------------------------------
# Scan result
# ---------------------------------------------------------------------------
class ScanResult(BaseModel):
    """Full results of a completed scan."""

    scan_id: int
    timestamp: datetime
    total_files: int
    issues_found: int
    issues: list[ValidationIssue] = []
    summary_by_type: dict[str, int] = {}
    summary_by_severity: dict[str, int] = {}


class ScanHistoryItem(BaseModel):
    """Lightweight scan record for history listings."""

    scan_id: int
    timestamp: datetime
    total_files: int
    issues_found: int
