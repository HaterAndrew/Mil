"""SharePoint Sync — FastAPI application."""

from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import Response
from shared.auth import verify_api_key
from shared.factory import create_app
from sqlalchemy.orm import Session

from .db import get_db, init_db
from .models import (
    FileDiff,
    SharePointVariant,
    SyncRecordCreate,
    SyncRecordResponse,
    SyncStatus,
)
from .sync_engine import (
    SOURCE_ROOT,
    build_sync_package,
    compare_states,
    compute_file_hashes,
    generate_sync_manifest,
    get_sharepoint_variants,
    get_sync_history,
    load_sync_state,
    record_sync,
)


# ---------------------------------------------------------------------------
# App lifecycle
# ---------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = create_app(title="SharePoint Sync", version="1.0.0", lifespan=lifespan)


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------
@app.get("/health")
def health():
    return {"status": "ok"}


# ---------------------------------------------------------------------------
# Sync status
# ---------------------------------------------------------------------------
@app.get("/status", response_model=SyncStatus)
def sync_status(db: Session = Depends(get_db)):
    """Return current sync state comparing local files to last baseline."""
    current = compute_file_hashes(SOURCE_ROOT)
    last = load_sync_state(db)
    diff = compare_states(current, last)

    total_changed = len(diff["added"]) + len(diff["modified"]) + len(diff["deleted"])

    return SyncStatus(
        total_files=len(current),
        added=len(diff["added"]),
        modified=len(diff["modified"]),
        deleted=len(diff["deleted"]),
        unchanged=len(diff["unchanged"]),
        in_sync=(total_changed == 0),
    )


# ---------------------------------------------------------------------------
# Diff
# ---------------------------------------------------------------------------
@app.get("/diff", response_model=FileDiff)
def get_diff(db: Session = Depends(get_db)):
    """Return categorized file diff since last sync."""
    current = compute_file_hashes(SOURCE_ROOT)
    last = load_sync_state(db)
    diff = compare_states(current, last)

    return FileDiff(**diff)


# ---------------------------------------------------------------------------
# Record sync
# ---------------------------------------------------------------------------
@app.post("/sync", response_model=SyncRecordResponse, status_code=201, dependencies=[Depends(verify_api_key)])
def create_sync(payload: SyncRecordCreate, db: Session = Depends(get_db)):
    """Record current file state as the new sync baseline."""
    current = compute_file_hashes(SOURCE_ROOT)
    last = load_sync_state(db)
    diff = compare_states(current, last)

    rec = record_sync(db, current, notes=payload.notes, diff=diff)
    return SyncRecordResponse.model_validate(rec)


# ---------------------------------------------------------------------------
# Sync history
# ---------------------------------------------------------------------------
@app.get("/history")
def list_history(db: Session = Depends(get_db)):
    """Return all past sync records, newest first."""
    return get_sync_history(db)


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------
@app.get("/manifest")
def get_manifest(db: Session = Depends(get_db)):
    """Generate a markdown manifest of current changes."""
    current = compute_file_hashes(SOURCE_ROOT)
    last = load_sync_state(db)
    diff = compare_states(current, last)

    return {"manifest": generate_sync_manifest(diff)}


# ---------------------------------------------------------------------------
# Package generation
# ---------------------------------------------------------------------------
@app.get("/package/changes")
def download_changes_package(db: Session = Depends(get_db)):
    """Build and download a ZIP of added/modified files only."""
    current = compute_file_hashes(SOURCE_ROOT)
    last = load_sync_state(db)
    diff = compare_states(current, last)

    total_changed = len(diff["added"]) + len(diff["modified"])
    if total_changed == 0:
        raise HTTPException(status_code=404, detail="No changes to package")

    zip_bytes = build_sync_package(SOURCE_ROOT, diff, include_all=False)
    return Response(
        content=zip_bytes,
        media_type="application/zip",
        headers={"Content-Disposition": "attachment; filename=sharepoint_sync_changes.zip"},
    )


@app.get("/package/full")
def download_full_package(db: Session = Depends(get_db)):
    """Build and download a ZIP of all current files."""
    current = compute_file_hashes(SOURCE_ROOT)
    last = load_sync_state(db)
    diff = compare_states(current, last)

    zip_bytes = build_sync_package(SOURCE_ROOT, diff, include_all=True)
    return Response(
        content=zip_bytes,
        media_type="application/zip",
        headers={"Content-Disposition": "attachment; filename=sharepoint_sync_full.zip"},
    )


# ---------------------------------------------------------------------------
# SharePoint variants
# ---------------------------------------------------------------------------
@app.get("/variants", response_model=list[SharePointVariant])
def list_variants():
    """Find files with _sharepoint suffix and their standard counterparts."""
    raw = get_sharepoint_variants()
    results = []
    for v in raw:
        sp_exists = v["sharepoint_exists"] == "True"
        std_exists = v["standard_exists"] == "True"

        if not sp_exists or not std_exists:
            status = "MISSING"
        else:
            status = "OK"

        results.append(SharePointVariant(
            sharepoint_path=v["sharepoint_path"],
            standard_path=v["standard_path"],
            sharepoint_exists=sp_exists,
            standard_exists=std_exists,
            status=status,
        ))
    return results
