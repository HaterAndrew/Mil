"""SharePoint Sync — seed initial baseline.

Scans maven_training/ and records the current state as the first sync
baseline.  Safe to re-run — will create a new baseline each time.

Usage: python -m apps.sharepoint_sync.seed
"""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure repo root is on sys.path
_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from apps.sharepoint_sync.db import SessionLocal, init_db
from apps.sharepoint_sync.sync_engine import (
    SOURCE_ROOT,
    compute_file_hashes,
    record_sync,
)


def main() -> None:
    """Scan maven_training/ and record the initial sync baseline."""
    init_db()

    if not SOURCE_ROOT.is_dir():
        print(f"WARNING: Source directory not found: {SOURCE_ROOT}")
        print("Creating empty baseline — re-run after content is available.")
        hashes: dict[str, str] = {}
    else:
        print(f"Scanning {SOURCE_ROOT} ...")
        hashes = compute_file_hashes(SOURCE_ROOT)
        print(f"Found {len(hashes):,} files.")

    # Record as initial baseline (all files marked UNCHANGED since this
    # is the first sync — no prior state to diff against)
    db = SessionLocal()
    try:
        rec = record_sync(
            db,
            hashes,
            notes="Initial baseline — seeded by seed.py",
            diff=None,  # No diff for first sync; all UNCHANGED
        )
        print(
            f"Baseline recorded (ID: {rec.id}) — "
            f"{rec.total_files} files at {rec.timestamp:%Y-%m-%d %H:%M:%S} UTC."
        )
    finally:
        db.close()

    print("Done.")


if __name__ == "__main__":
    main()
