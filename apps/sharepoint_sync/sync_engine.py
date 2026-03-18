"""SharePoint Sync — core sync logic.

Compares local maven_training/ content against the last recorded sync
state, generates diff manifests, and builds deployment packages (ZIP).
"""

from __future__ import annotations

import hashlib
import io
import zipfile
from datetime import UTC, datetime
from pathlib import Path

from sqlalchemy.orm import Session

from .db import FileState, SyncRecord, init_db

# Default source directory for maven_training content
SOURCE_ROOT = Path(__file__).resolve().parent.parent.parent / "maven_training"

# ---------------------------------------------------------------------------
# File extensions to skip (binary blobs, temp files, caches)
# ---------------------------------------------------------------------------
_SKIP_DIRS = {".git", "__pycache__", ".venv", "node_modules", ".tox", ".mypy_cache"}


def compute_file_hashes(root_path: Path | str) -> dict[str, str]:
    """Walk *root_path*, compute SHA-256 for each file.

    Returns a dict mapping relative file paths (POSIX-style) to their
    hex-digest hash.  Skips hidden directories and common cache folders.
    """
    root = Path(root_path).resolve()
    hashes: dict[str, str] = {}

    if not root.is_dir():
        return hashes

    for file_path in sorted(root.rglob("*")):
        # Skip directories themselves and unwanted subtrees
        if file_path.is_dir():
            continue
        if any(part in _SKIP_DIRS or part.startswith(".") for part in file_path.relative_to(root).parts):
            continue

        rel = file_path.relative_to(root).as_posix()
        try:
            sha = hashlib.sha256(file_path.read_bytes()).hexdigest()
            hashes[rel] = sha
        except (OSError, PermissionError):
            # Skip files we can't read
            continue

    return hashes


def load_sync_state(db: Session) -> dict[str, str]:
    """Load the most recent sync state from the database.

    Returns a dict mapping relative file paths to their SHA-256 hashes
    as of the last recorded sync.  Returns empty dict if no sync exists.
    """
    latest = (
        db.query(SyncRecord)
        .order_by(SyncRecord.timestamp.desc())
        .first()
    )
    if not latest:
        return {}

    states = (
        db.query(FileState)
        .filter(FileState.sync_id == latest.id)
        .filter(FileState.status != "DELETED")
        .all()
    )
    return {fs.file_path: fs.file_hash for fs in states}


def compare_states(
    current_hashes: dict[str, str],
    last_sync_hashes: dict[str, str],
) -> dict[str, list[str]]:
    """Compare current file hashes against the last sync baseline.

    Returns dict with keys: added, modified, deleted, unchanged — each
    a sorted list of relative file paths.
    """
    current_keys = set(current_hashes.keys())
    last_keys = set(last_sync_hashes.keys())

    added = sorted(current_keys - last_keys)
    deleted = sorted(last_keys - current_keys)

    modified = []
    unchanged = []
    for path in sorted(current_keys & last_keys):
        if current_hashes[path] != last_sync_hashes[path]:
            modified.append(path)
        else:
            unchanged.append(path)

    return {
        "added": added,
        "modified": modified,
        "deleted": deleted,
        "unchanged": unchanged,
    }


def generate_sync_manifest(diff: dict[str, list[str]]) -> str:
    """Create a markdown manifest summarizing changes since last sync."""
    lines = [
        "# SharePoint Sync Manifest",
        f"Generated: {datetime.now(UTC):%Y-%m-%d %H:%M:%S} UTC",
        "",
        "## Summary",
        f"- **Added:** {len(diff['added'])}",
        f"- **Modified:** {len(diff['modified'])}",
        f"- **Deleted:** {len(diff['deleted'])}",
        f"- **Unchanged:** {len(diff['unchanged'])}",
        "",
    ]

    if diff["added"]:
        lines.append("## Added Files")
        for f in diff["added"]:
            lines.append(f"- `{f}`")
        lines.append("")

    if diff["modified"]:
        lines.append("## Modified Files")
        for f in diff["modified"]:
            lines.append(f"- `{f}`")
        lines.append("")

    if diff["deleted"]:
        lines.append("## Deleted Files")
        for f in diff["deleted"]:
            lines.append(f"- ~~`{f}`~~")
        lines.append("")

    return "\n".join(lines)


def build_sync_package(
    root_path: Path | str,
    diff: dict[str, list[str]],
    include_all: bool = False,
) -> bytes:
    """Build a ZIP containing files for deployment.

    If *include_all* is False (default), only added and modified files
    are included.  If True, all current files are packaged.

    The ZIP also includes a SYNC_MANIFEST.md at the root level.
    """
    root = Path(root_path).resolve()
    buf = io.BytesIO()

    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        # Determine which files to include
        if include_all:
            files_to_pack = diff["added"] + diff["modified"] + diff["unchanged"]
        else:
            files_to_pack = diff["added"] + diff["modified"]

        for rel_path in sorted(files_to_pack):
            full_path = root / rel_path
            if full_path.is_file():
                zf.write(full_path, rel_path)

        # Include manifest
        manifest = generate_sync_manifest(diff)
        zf.writestr("SYNC_MANIFEST.md", manifest)

    return buf.getvalue()


def record_sync(
    db: Session,
    current_hashes: dict[str, str],
    notes: str = "",
    diff: dict[str, list[str]] | None = None,
) -> SyncRecord:
    """Save the current file state as the new sync baseline.

    Creates a SyncRecord and associated FileState rows for every file.
    If *diff* is provided, file statuses are set accordingly; otherwise
    all files are marked UNCHANGED (useful for initial baseline).
    """
    init_db()

    # Build status lookup from diff
    status_map: dict[str, str] = {}
    if diff:
        for path in diff.get("added", []):
            status_map[path] = "ADDED"
        for path in diff.get("modified", []):
            status_map[path] = "MODIFIED"
        for path in diff.get("deleted", []):
            status_map[path] = "DELETED"
        for path in diff.get("unchanged", []):
            status_map[path] = "UNCHANGED"

    record = SyncRecord(
        timestamp=datetime.now(UTC),
        total_files=len(current_hashes),
        added=len(diff["added"]) if diff else 0,
        modified=len(diff["modified"]) if diff else 0,
        deleted=len(diff["deleted"]) if diff else 0,
        notes=notes or None,
    )
    db.add(record)
    db.flush()  # get record.id

    # Add file states for all current files
    for path, sha in current_hashes.items():
        fs = FileState(
            sync_id=record.id,
            file_path=path,
            file_hash=sha,
            status=status_map.get(path, "UNCHANGED"),
        )
        db.add(fs)

    # Record deleted files (hash from last sync, marked DELETED)
    if diff:
        last_state = load_sync_state(db)
        for path in diff.get("deleted", []):
            fs = FileState(
                sync_id=record.id,
                file_path=path,
                file_hash=last_state.get(path, ""),
                status="DELETED",
            )
            db.add(fs)

    db.commit()
    db.refresh(record)
    return record


def get_sharepoint_variants() -> list[dict[str, str]]:
    """Find files with _sharepoint suffix and their standard counterparts.

    Scans SOURCE_ROOT for files matching *_sharepoint.* and pairs them
    with the corresponding standard version (same name without _sharepoint).

    Returns list of dicts with keys: sharepoint_path, standard_path,
    sharepoint_exists, standard_exists (all relative to SOURCE_ROOT).
    """
    root = SOURCE_ROOT.resolve()
    if not root.is_dir():
        return []

    variants: list[dict[str, str]] = []
    for sp_file in sorted(root.rglob("*_sharepoint.*")):
        if sp_file.is_dir():
            continue

        rel_sp = sp_file.relative_to(root).as_posix()

        # Derive standard version path: remove _sharepoint from stem
        stem = sp_file.stem.replace("_sharepoint", "")
        standard_file = sp_file.parent / f"{stem}{sp_file.suffix}"
        rel_std = standard_file.relative_to(root).as_posix()

        variants.append({
            "sharepoint_path": rel_sp,
            "standard_path": rel_std,
            "sharepoint_exists": str(sp_file.is_file()),
            "standard_exists": str(standard_file.is_file()),
        })

    return variants


def get_sync_history(db: Session) -> list[dict]:
    """Return all past sync records, newest first."""
    records = (
        db.query(SyncRecord)
        .order_by(SyncRecord.timestamp.desc())
        .all()
    )
    return [
        {
            "id": r.id,
            "timestamp": r.timestamp.strftime("%Y-%m-%d %H:%M:%S") if r.timestamp else "",
            "total_files": r.total_files,
            "added": r.added,
            "modified": r.modified,
            "deleted": r.deleted,
            "notes": r.notes or "",
        }
        for r in records
    ]
