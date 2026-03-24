"""Offline Package Builder — FastAPI application."""

from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.responses import Response
from shared.auth import verify_api_key
from shared.factory import create_app
from sqlalchemy.orm import Session

from .db import PackageRecord as PackageRecordRow
from .db import get_db, init_db
from .models import (
    InventoryCategory,
    InventoryResponse,
    PackageRecord,
    PackageRequest,
    PackageSummary,
)
from .packager import (
    PREREQ_CHAIN,
    build_package,
    discover_content,
    estimate_size,
    get_all_tms_with_prereqs,
    resolve_dependencies,
)

# Default root path for maven_training content
_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
MAVEN_TRAINING_PATH = _REPO_ROOT / "maven_training"


# ---------------------------------------------------------------------------
# App lifecycle
# ---------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = create_app(title="Offline Package Builder", version="1.0.0", lifespan=lifespan)


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------
@app.get("/health")
def health():
    return {"status": "ok"}


# ---------------------------------------------------------------------------
# Inventory
# ---------------------------------------------------------------------------
@app.get("/inventory", response_model=InventoryResponse)
def get_inventory():
    """Return full content inventory of the maven_training corpus."""
    if not MAVEN_TRAINING_PATH.is_dir():
        raise HTTPException(status_code=503, detail="maven_training directory not found")

    inv = discover_content(MAVEN_TRAINING_PATH)
    categories = []
    total_items = 0
    total_kb = 0

    for cat_name, items in inv.items():
        cat_kb = sum(meta.get("size_kb", 0) for meta in items.values())
        categories.append(InventoryCategory(
            category=cat_name,
            item_count=len(items),
            total_size_kb=cat_kb,
            items=sorted(items.keys()),
        ))
        total_items += len(items)
        total_kb += cat_kb

    return InventoryResponse(
        categories=categories,
        total_items=total_items,
        total_size_kb=total_kb,
    )


# ---------------------------------------------------------------------------
# Preview
# ---------------------------------------------------------------------------
@app.post("/preview", response_model=PackageSummary, dependencies=[Depends(verify_api_key)])
def preview_package(request: PackageRequest):
    """Preview what a package will contain without building it."""
    if not MAVEN_TRAINING_PATH.is_dir():
        raise HTTPException(status_code=503, detail="maven_training directory not found")

    # Validate TM identifiers
    for tm in request.selected_tms:
        if tm not in PREREQ_CHAIN:
            raise HTTPException(status_code=422, detail=f"Unknown TM identifier: {tm}")

    auto_included = resolve_dependencies(request.selected_tms)
    all_tms = get_all_tms_with_prereqs(request.selected_tms)

    inventory = discover_content(MAVEN_TRAINING_PATH)

    # Build selection dict matching what build_package expects
    selection = _build_selection(all_tms, inventory, request)
    est_kb = estimate_size(inventory, selection, request.include_pdfs)

    item_counts = {cat: len(items) for cat, items in selection.items()}

    return PackageSummary(
        selected_tms=request.selected_tms,
        auto_included_prereqs=auto_included,
        all_tms=all_tms,
        estimated_size_kb=est_kb,
        item_counts=item_counts,
    )


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------
@app.post("/packages", status_code=201, dependencies=[Depends(verify_api_key)])
def build(request: PackageRequest, db: Session = Depends(get_db)):
    """Build an offline package and return it as a ZIP download."""
    if not MAVEN_TRAINING_PATH.is_dir():
        raise HTTPException(status_code=503, detail="maven_training directory not found")

    for tm in request.selected_tms:
        if tm not in PREREQ_CHAIN:
            raise HTTPException(status_code=422, detail=f"Unknown TM identifier: {tm}")

    auto_included = resolve_dependencies(request.selected_tms)
    all_tms = get_all_tms_with_prereqs(request.selected_tms)
    inventory = discover_content(MAVEN_TRAINING_PATH)
    selection = _build_selection(all_tms, inventory, request)

    zip_bytes = build_package(
        selected=selection,
        inventory=inventory,
        auto_included=auto_included,
        include_pdfs=request.include_pdfs,
        root_path=MAVEN_TRAINING_PATH,
    )

    total_items = sum(len(v) for v in selection.values())
    size_kb = len(zip_bytes) // 1024

    # Record build in DB
    record = PackageRecordRow(
        selected_tms=request.selected_tms,
        all_tms=all_tms,
        total_items=total_items,
        size_kb=size_kb,
        include_pdfs=request.include_pdfs,
    )
    db.add(record)
    db.commit()

    return Response(
        content=zip_bytes,
        media_type="application/zip",
        headers={"Content-Disposition": "attachment; filename=mss_offline_package.zip"},
    )


# ---------------------------------------------------------------------------
# History
# ---------------------------------------------------------------------------
@app.get("/packages", response_model=list[PackageRecord])
def list_packages(
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
):
    """List previously built packages."""
    rows = (
        db.query(PackageRecordRow)
        .order_by(PackageRecordRow.created_at.desc())
        .limit(limit)
        .all()
    )
    return [PackageRecord.model_validate(r) for r in rows]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _build_selection(
    all_tms: list[str],
    inventory: dict,
    request: PackageRequest,
) -> dict[str, list[str]]:
    """Build the selection dict for the packager from a request."""
    selection: dict[str, list[str]] = {
        "tm": [tm for tm in all_tms if tm in inventory.get("tm", {})],
        "syllabi": sorted(inventory.get("syllabi", {}).keys()) if request.include_syllabi else [],
        "exercises": sorted(inventory.get("exercises", {}).keys()) if request.include_exercises else [],
        "exams": sorted(inventory.get("exams", {}).keys()) if request.include_exercises else [],
        "doctrine": sorted(inventory.get("doctrine", {}).keys()) if request.include_doctrine else [],
        "quick_reference": sorted(inventory.get("quick_reference", {}).keys()) if request.include_quick_ref else [],
        "pdf": sorted(inventory.get("pdf", {}).keys()) if request.include_pdfs else [],
    }
    return selection
