"""Cross-Reference Validator — seed script.

Runs an initial scan against the maven_training directory to populate the
database with real validation results. Falls back to a mock scan result
if the corpus directory does not exist.
"""

from __future__ import annotations

import sys
from datetime import UTC, datetime
from pathlib import Path

# Ensure package is importable
_app_dir = Path(__file__).resolve().parent
if str(_app_dir.parent) not in sys.path:
    sys.path.insert(0, str(_app_dir.parent))

from xref_validator.db import (
    SessionLocal,
    ScanRecord,
    IssueRecord,
    init_db,
    run_full_scan,
)
from xref_validator.models import MAVEN_TRAINING_DEFAULT


def seed():
    """Execute an initial scan and print summary."""
    init_db()

    root = Path(MAVEN_TRAINING_DEFAULT)

    if root.is_dir():
        print(f"[SEED] Scanning real corpus at: {root}")
        try:
            result = run_full_scan(str(root))
            print(f"[SEED] Scan complete — ID: {result.scan_id}")
            print(f"[SEED]   Files scanned : {result.total_files}")
            print(f"[SEED]   Issues found  : {result.issues_found}")
            if result.summary_by_type:
                print("[SEED]   By type:")
                for itype, count in sorted(result.summary_by_type.items()):
                    print(f"[SEED]     {itype}: {count}")
            if result.summary_by_severity:
                print("[SEED]   By severity:")
                for sev, count in sorted(result.summary_by_severity.items()):
                    print(f"[SEED]     {sev}: {count}")
            return
        except Exception as exc:
            print(f"[SEED] Scan failed: {exc}")
            print("[SEED] Falling back to mock data.")

    # Fallback: create a mock scan record so the dashboard has something
    print("[SEED] Corpus not found — creating mock scan result.")
    db = SessionLocal()
    try:
        scan = ScanRecord(
            timestamp=datetime.now(UTC),
            root_path=str(root),
            total_files=0,
            issues_found=2,
        )
        db.add(scan)
        db.flush()

        db.add(IssueRecord(
            scan_id=scan.id,
            file_path="(mock) example/README.md",
            line_number=10,
            issue_type="BROKEN_LINK",
            severity="ERROR",
            description="Mock issue: broken link to ../nonexistent.md",
            suggested_fix="This is a placeholder — run a real scan against the corpus.",
        ))
        db.add(IssueRecord(
            scan_id=scan.id,
            file_path="(mock) example/TM_50A.md",
            line_number=1,
            issue_type="STALE_REF",
            severity="ERROR",
            description="Mock issue: SL 5A does not exist (stale reference)",
            suggested_fix="SL 5 is only G through L. Remove or update.",
        ))

        db.commit()
        print(f"[SEED] Mock scan created — ID: {scan.id}, 2 mock issues.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
