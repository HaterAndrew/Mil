"""Tests for the SharePoint Sync API.

Note: Most endpoints call compute_file_hashes(SOURCE_ROOT) which requires the
actual maven_training directory. We test health and history (DB-backed only).
Filesystem-dependent endpoints are tested via mocking.
"""

from __future__ import annotations

from unittest.mock import patch

from sharepoint_sync.db import SyncRecord, FileState


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------
class TestHealth:
    def test_health(self, sync_client):
        resp = sync_client.get("/health")
        assert resp.status_code == 200
        assert resp.json()["status"] == "ok"


# ---------------------------------------------------------------------------
# History
# ---------------------------------------------------------------------------
class TestHistory:
    def test_history_empty(self, sync_client):
        resp = sync_client.get("/history")
        assert resp.status_code == 200
        assert resp.json() == []

    def test_history_with_records(self, sync_client, sync_db):
        """Seed sync records directly and verify history endpoint."""
        session = sync_db()
        rec = SyncRecord(total_files=10, added=3, modified=2, deleted=1, notes="Initial sync")
        session.add(rec)
        session.commit()
        session.refresh(rec)

        # Add file states
        session.add(FileState(
            sync_id=rec.id, file_path="tm/TM_10/overview.md",
            file_hash="abc123", status="ADDED",
        ))
        session.add(FileState(
            sync_id=rec.id, file_path="tm/TM_20/overview.md",
            file_hash="def456", status="UNCHANGED",
        ))
        session.commit()
        session.close()

        resp = sync_client.get("/history")
        assert resp.status_code == 200
        data = resp.json()
        assert len(data) == 1


# ---------------------------------------------------------------------------
# Status (mocked filesystem)
# ---------------------------------------------------------------------------
class TestStatus:
    @patch("sharepoint_sync.api.compute_file_hashes", return_value={
        "tm/TM_10/overview.md": "abc123",
        "tm/TM_20/overview.md": "def456",
    })
    def test_status_no_baseline(self, mock_hashes, sync_client):
        """With no prior sync, all files show as added."""
        resp = sync_client.get("/status")
        assert resp.status_code == 200
        data = resp.json()
        assert data["total_files"] == 2
        assert data["added"] == 2
        assert data["in_sync"] is False

    @patch("sharepoint_sync.api.compute_file_hashes", return_value={
        "tm/TM_10/overview.md": "abc123",
    })
    def test_sync_then_status(self, mock_hashes, sync_client):
        """After a sync, same hashes should show in_sync."""
        sync_client.post("/sync", json={"notes": "baseline"})

        resp = sync_client.get("/status")
        assert resp.status_code == 200
        data = resp.json()
        assert data["in_sync"] is True
        assert data["added"] == 0


# ---------------------------------------------------------------------------
# Manifest (mocked filesystem)
# ---------------------------------------------------------------------------
class TestManifest:
    @patch("sharepoint_sync.api.compute_file_hashes", return_value={
        "tm/TM_10/overview.md": "abc123",
    })
    def test_manifest(self, mock_hashes, sync_client):
        resp = sync_client.get("/manifest")
        assert resp.status_code == 200
        assert "manifest" in resp.json()
