"""Generate demo data for the Offline Package Builder.

Seeds a few historical package records so the dashboard and API
have data to display immediately.

Run: python -m apps.offline_packager.seed
"""

from __future__ import annotations

import random
from datetime import UTC, datetime, timedelta

from .db import PackageRecord, init_db, SessionLocal

# Deterministic for reproducibility
random.seed(42)

# Sample package configs that might have been built
SAMPLE_PACKAGES = [
    {
        "selected_tms": ["TM-10", "TM-20", "TM-30"],
        "all_tms": ["TM-10", "TM-20", "TM-30"],
        "total_items": 45,
        "size_kb": 2800,
        "include_pdfs": True,
        "notes": "Foundation package for MTT at Grafenwoehr",
    },
    {
        "selected_tms": ["TM-40A", "TM-40B", "TM-40C"],
        "all_tms": ["TM-10", "TM-20", "TM-30", "TM-40A", "TM-40B", "TM-40C"],
        "total_items": 92,
        "size_kb": 5400,
        "include_pdfs": True,
        "notes": "WFF tracks for 2ID deployment support",
    },
    {
        "selected_tms": ["TM-40G", "TM-40H"],
        "all_tms": ["TM-10", "TM-20", "TM-30", "TM-40G", "TM-40H"],
        "total_items": 78,
        "size_kb": 4200,
        "include_pdfs": False,
        "notes": "Specialist tracks — no PDFs to reduce size for BGAN transfer",
    },
    {
        "selected_tms": ["TM-50G"],
        "all_tms": ["TM-10", "TM-20", "TM-30", "TM-40G", "TM-50G"],
        "total_items": 85,
        "size_kb": 4800,
        "include_pdfs": True,
        "notes": "Advanced ORSA package for SHAPE exercise",
    },
]


def seed() -> None:
    """Populate the database with sample package records."""
    init_db()
    db = SessionLocal()
    try:
        # Clear for idempotent re-seeding
        db.query(PackageRecord).delete()
        db.flush()

        now = datetime.now(UTC)
        for i, pkg in enumerate(SAMPLE_PACKAGES):
            record = PackageRecord(
                created_at=now - timedelta(days=random.randint(1, 14), hours=random.randint(0, 12)),
                **pkg,
            )
            db.add(record)

        db.commit()
        print(f"Seeded {len(SAMPLE_PACKAGES)} package records.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
