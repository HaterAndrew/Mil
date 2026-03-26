"""Tests for the Offline Package Builder.

Note: Endpoints that scan the maven_training filesystem (/inventory, /preview,
/packages POST) are not tested here — they require the full corpus directory.
We test health and package history (DB-backed).
"""

from __future__ import annotations

from offline_packager.db import PackageRecord


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------
class TestHealth:
    def test_health(self, packager_client):
        resp = packager_client.get("/health")
        assert resp.status_code == 200
        assert resp.json()["status"] == "ok"


# ---------------------------------------------------------------------------
# Package history
# ---------------------------------------------------------------------------
class TestPackages:
    def test_list_packages_empty(self, packager_client):
        resp = packager_client.get("/packages")
        assert resp.status_code == 200
        assert resp.json() == []

    def test_list_packages_with_records(self, packager_client, packager_db):
        """Seed package records directly and verify list endpoint."""
        session = packager_db()
        session.add(PackageRecord(
            selected_tms=["SL 1", "SL 2"],
            all_tms=["SL 1", "SL 2"],
            total_items=25,
            size_kb=1024,
            include_pdfs=True,
            notes="Test package",
        ))
        session.add(PackageRecord(
            selected_tms=["SL 3"],
            all_tms=["SL 1", "SL 2", "SL 3"],
            total_items=40,
            size_kb=2048,
            include_pdfs=False,
        ))
        session.commit()
        session.close()

        resp = packager_client.get("/packages")
        assert resp.status_code == 200
        data = resp.json()
        assert len(data) == 2

    def test_list_packages_with_limit(self, packager_client, packager_db):
        session = packager_db()
        for i in range(5):
            session.add(PackageRecord(
                selected_tms=[f"SL {i}"],
                all_tms=[f"SL {i}"],
                total_items=10,
                size_kb=100,
            ))
        session.commit()
        session.close()

        resp = packager_client.get("/packages", params={"limit": 3})
        assert resp.status_code == 200
        assert len(resp.json()) == 3
