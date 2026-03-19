"""Tests for the Cross-Reference Validator.

The /scan endpoint runs validators against markdown files. We test with
temporary markdown files to exercise the scan pipeline without needing
the full maven_training corpus.
"""

from __future__ import annotations

import os


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------
class TestHealth:
    def test_health(self, xref_client):
        resp = xref_client.get("/health")
        assert resp.status_code == 200
        assert resp.json()["status"] == "ok"


# ---------------------------------------------------------------------------
# Scan history
# ---------------------------------------------------------------------------
class TestScans:
    def test_scans_empty(self, xref_client):
        resp = xref_client.get("/scans")
        assert resp.status_code == 200
        assert resp.json() == []

    def test_scan_not_found(self, xref_client):
        resp = xref_client.get("/scan/9999")
        assert resp.status_code == 404


# ---------------------------------------------------------------------------
# Issues
# ---------------------------------------------------------------------------
class TestIssues:
    def test_issues_empty(self, xref_client):
        resp = xref_client.get("/issues")
        assert resp.status_code == 200
        assert resp.json() == []


# ---------------------------------------------------------------------------
# Scan with temp markdown files
# ---------------------------------------------------------------------------
class TestScanExecution:
    def test_scan_clean_files(self, xref_client, tmp_path):
        """Scan a directory with a simple, valid markdown file."""
        md_file = tmp_path / "test_doc.md"
        md_file.write_text("# Chapter 1\n\nSome content.\n\n# Chapter 2\n\nMore content.\n")

        resp = xref_client.post("/scan", json={
            "root_path": str(tmp_path),
            "patterns": ["*.md"],
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["total_files"] >= 1
        assert "issues" in data

    def test_scan_broken_link(self, xref_client, tmp_path):
        """Scan detects a broken internal link."""
        md_file = tmp_path / "test_doc.md"
        md_file.write_text(
            "# Overview\n\n"
            "See [details](nonexistent_file.md) for more info.\n"
        )

        resp = xref_client.post("/scan", json={
            "root_path": str(tmp_path),
            "patterns": ["*.md"],
        })
        assert resp.status_code == 200
        data = resp.json()
        # Should find the broken link
        broken = [i for i in data["issues"] if i["issue_type"] == "BROKEN_LINK"]
        assert len(broken) >= 1

    def test_scan_persists_history(self, xref_client, tmp_path):
        """Scan results are saved and retrievable via history."""
        md_file = tmp_path / "test.md"
        md_file.write_text("# Test\n\nValid content.\n")

        xref_client.post("/scan", json={
            "root_path": str(tmp_path),
            "patterns": ["*.md"],
        })

        resp = xref_client.get("/scans")
        assert len(resp.json()) == 1

        scan_id = resp.json()[0]["scan_id"]
        resp = xref_client.get(f"/scan/{scan_id}")
        assert resp.status_code == 200
        assert resp.json()["scan_id"] == scan_id
