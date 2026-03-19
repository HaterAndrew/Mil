"""Cross-Reference Validator — FastAPI application."""

from __future__ import annotations

import threading
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Query

from .db import (
    get_filtered_issues,
    get_scan_history,
    get_scan_result,
    init_db,
    run_full_scan,
)
from .models import (
    ScanHistoryItem,
    ScanRequest,
    ScanResult,
    ValidationIssue,
)

# Prevent concurrent scans from corrupting the database
_scan_lock = threading.Lock()


# ---------------------------------------------------------------------------
# App lifecycle
# ---------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Cross-Reference Validator",
    description=(
        "Scans the maven_training documentation corpus and validates "
        "cross-references, internal links, chapter references, and "
        "prereq chain consistency."
    ),
    version="1.0.0",
    lifespan=lifespan,
)


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------
@app.get("/health")
def health():
    return {"status": "ok"}


# ---------------------------------------------------------------------------
# Scan operations
# ---------------------------------------------------------------------------
@app.post("/scan", response_model=ScanResult)
def trigger_scan(request: ScanRequest | None = None):
    """Trigger a new cross-reference validation scan.

    Accepts an optional root_path override. Defaults to the maven_training
    directory.
    """
    if request is None:
        request = ScanRequest()
    if not _scan_lock.acquire(blocking=False):
        raise HTTPException(status_code=409, detail="A scan is already in progress")
    try:
        result = run_full_scan(request.root_path, request.patterns)
    finally:
        _scan_lock.release()
    return result


@app.get("/scan/{scan_id}", response_model=ScanResult)
def get_scan(scan_id: int):
    """Retrieve full results for a specific scan."""
    result = get_scan_result(scan_id)
    if result is None:
        raise HTTPException(status_code=404, detail=f"Scan {scan_id} not found")
    return result


@app.get("/scans", response_model=list[ScanHistoryItem])
def list_scans():
    """List all past scans, most recent first."""
    return get_scan_history()


@app.get("/issues", response_model=list[ValidationIssue])
def list_issues(
    type: str | None = Query(None, description="Filter by issue type (e.g., BROKEN_LINK)"),
    severity: str | None = Query(None, description="Filter by severity (ERROR, WARNING, INFO)"),
    scan_id: int | None = Query(None, description="Scan ID (defaults to latest)"),
):
    """Return filtered issues from a scan (defaults to latest)."""
    return get_filtered_issues(
        scan_id=scan_id,
        issue_type=type,
        severity=severity,
    )
