"""Tests for the Training Metrics Executive Dashboard.

Note: The /metrics endpoint calls collect_all_metrics() which imports from
all other app DBs. We test snapshot CRUD directly and mock the cross-app
aggregation for endpoint tests.
"""

from __future__ import annotations

from unittest.mock import patch


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------
class TestHealth:
    def test_health(self, metrics_client):
        resp = metrics_client.get("/health")
        assert resp.status_code == 200
        assert resp.json()["status"] == "ok"


# ---------------------------------------------------------------------------
# Snapshots — CRUD against the local DB
# ---------------------------------------------------------------------------
MOCK_METRICS = {
    "total_trainees": 50,
    "funnel": [],
    "unit_summary": [],
    "bottleneck_top3": [],
    "exam_pass_rate": 82.5,
    "exam_sessions_count": 10,
    "total_aars": 5,
    "top_issues": [],
    "overdue_milestones": 2,
    "upcoming_events": 3,
    "active_alerts": 0,
    "expiring_certs": 1,
    "coverage_gaps": 0,
    "fill_rate": 75.0,
    "waitlisted_count": 4,
    "overdue_reviews": 0,
    "stale_docs": 2,
    "open_action_items": 3,
    "lessons_this_month": 1,
    "risks": [],
    "executive_summary": {
        "readiness_score": 72.0,
        "on_track": "Training on track.",
        "at_risk": "No significant risks.",
        "what_changed": "3 MTT events scheduled.",
        "decision_required": "No decisions required.",
        "rag": "GREEN",
    },
}


class TestSnapshots:
    @patch("training_metrics.api.collect_all_metrics", return_value=MOCK_METRICS)
    def test_create_snapshot(self, mock_collect, metrics_client):
        resp = metrics_client.post("/snapshots", json={
            "report_type": "WEEKLY",
            "generated_by": "MAJ SMITH",
            "notes": "End-of-week snapshot",
        })
        assert resp.status_code == 201
        data = resp.json()
        assert data["report_type"] == "WEEKLY"
        assert data["generated_by"] == "MAJ SMITH"
        assert "data_json" in data

    @patch("training_metrics.api.collect_all_metrics", return_value=MOCK_METRICS)
    def test_list_snapshots(self, mock_collect, metrics_client):
        metrics_client.post("/snapshots", json={
            "report_type": "WEEKLY", "generated_by": "SYSTEM",
        })
        metrics_client.post("/snapshots", json={
            "report_type": "MONTHLY", "generated_by": "SYSTEM",
        })
        resp = metrics_client.get("/snapshots")
        assert resp.status_code == 200
        assert len(resp.json()) == 2

    @patch("training_metrics.api.collect_all_metrics", return_value=MOCK_METRICS)
    def test_latest_snapshot(self, mock_collect, metrics_client):
        metrics_client.post("/snapshots", json={
            "report_type": "WEEKLY", "generated_by": "SYSTEM",
        })
        resp = metrics_client.get("/snapshots/latest", params={"type": "WEEKLY"})
        assert resp.status_code == 200
        assert resp.json()["report_type"] == "WEEKLY"

    def test_latest_snapshot_404(self, metrics_client):
        resp = metrics_client.get("/snapshots/latest", params={"type": "QUARTERLY"})
        assert resp.status_code == 404


# ---------------------------------------------------------------------------
# Live metrics endpoint (mocked)
# ---------------------------------------------------------------------------
class TestMetrics:
    @patch("training_metrics.api.collect_all_metrics", return_value=MOCK_METRICS)
    def test_get_metrics(self, mock_collect, metrics_client):
        resp = metrics_client.get("/metrics")
        assert resp.status_code == 200
        data = resp.json()
        assert data["total_trainees"] == 50
        assert data["exam_pass_rate"] == 82.5
        assert data["executive_summary"]["rag"] == "GREEN"


# ---------------------------------------------------------------------------
# Briefing export (mocked)
# ---------------------------------------------------------------------------
class TestBriefing:
    @patch("training_metrics.api.collect_all_metrics", return_value=MOCK_METRICS)
    def test_export_briefing(self, mock_collect, metrics_client):
        resp = metrics_client.get("/export/briefing")
        assert resp.status_code == 200
        text = resp.json()["briefing"]
        assert "BOTTOM LINE UP FRONT" in text
        assert "GREEN" in text
