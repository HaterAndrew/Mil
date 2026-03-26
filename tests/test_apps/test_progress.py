"""Tests for the Progress Tracker.

Note: Endpoints that cross-reference readiness_tracker (/stalled, /overdue,
/record, /goals) are tested with mocks since they open separate DB sessions.
"""

from __future__ import annotations

from datetime import date, timedelta
from unittest.mock import patch


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------
class TestHealth:
    def test_health(self, progress_client):
        resp = progress_client.get("/health")
        assert resp.status_code == 200
        assert resp.json()["status"] == "ok"


# ---------------------------------------------------------------------------
# Milestones
# ---------------------------------------------------------------------------
class TestMilestones:
    def test_create_milestone(self, progress_client):
        future = (date.today() + timedelta(days=60)).isoformat()
        resp = progress_client.post("/milestones", json={
            "dodid": "1234567890",
            "course_id": "SL 2",
            "target_date": future,
        })
        assert resp.status_code == 201
        data = resp.json()
        assert data["dodid"] == "1234567890"
        assert data["course_id"] == "SL 2"
        assert data["status"] == "ON_TRACK"
        assert data["days_remaining"] > 14

    def test_create_milestone_at_risk(self, progress_client):
        """Milestone within 14 days should be AT_RISK."""
        soon = (date.today() + timedelta(days=7)).isoformat()
        resp = progress_client.post("/milestones", json={
            "dodid": "1234567890",
            "course_id": "SL 1",
            "target_date": soon,
        })
        assert resp.status_code == 201
        assert resp.json()["status"] == "AT_RISK"

    def test_create_milestone_overdue(self, progress_client):
        """Milestone in the past should be OVERDUE."""
        past = (date.today() - timedelta(days=5)).isoformat()
        resp = progress_client.post("/milestones", json={
            "dodid": "1234567890",
            "course_id": "SL 1",
            "target_date": past,
        })
        assert resp.status_code == 201
        assert resp.json()["status"] == "OVERDUE"

    def test_get_milestones(self, progress_client):
        future = (date.today() + timedelta(days=30)).isoformat()
        progress_client.post("/milestones", json={
            "dodid": "1234567890",
            "course_id": "SL 1",
            "target_date": future,
        })
        progress_client.post("/milestones", json={
            "dodid": "1234567890",
            "course_id": "SL 2",
            "target_date": future,
        })

        resp = progress_client.get("/milestones/1234567890")
        assert resp.status_code == 200
        assert len(resp.json()) == 2

    def test_get_milestones_empty(self, progress_client):
        resp = progress_client.get("/milestones/9999999999")
        assert resp.status_code == 200
        assert resp.json() == []

    def test_milestone_with_notes(self, progress_client):
        future = (date.today() + timedelta(days=60)).isoformat()
        resp = progress_client.post("/milestones", json={
            "dodid": "1234567890",
            "course_id": "SL 3",
            "target_date": future,
            "notes": "Priority enrollment requested",
        })
        assert resp.status_code == 201
        assert resp.json()["notes"] == "Priority enrollment requested"


# ---------------------------------------------------------------------------
# Goals (mocked readiness_tracker)
# ---------------------------------------------------------------------------
class TestGoals:
    @patch("readiness_tracker.db.check_eligibility", return_value=(True, []))
    @patch("readiness_tracker.db.SessionLocal")
    def test_create_goal(self, mock_rt_session, mock_eligibility, progress_client):
        mock_rt_session.return_value.close = lambda: None
        future = (date.today() + timedelta(days=90)).isoformat()
        resp = progress_client.post("/goals", json={
            "dodid": "1234567890",
            "target_course": "SL 3",
            "target_date": future,
        })
        assert resp.status_code == 201
        data = resp.json()
        assert data["target_course"] == "SL 3"
        assert data["eligible"] is True
        assert data["missing_prereqs"] == []

    @patch("readiness_tracker.db.check_eligibility", return_value=(False, ["SL 1", "SL 2"]))
    @patch("readiness_tracker.db.SessionLocal")
    def test_create_goal_not_eligible(self, mock_rt_session, mock_eligibility, progress_client):
        mock_rt_session.return_value.close = lambda: None
        future = (date.today() + timedelta(days=90)).isoformat()
        resp = progress_client.post("/goals", json={
            "dodid": "1234567890",
            "target_course": "SL 4G",
            "target_date": future,
        })
        assert resp.status_code == 201
        data = resp.json()
        assert data["eligible"] is False
        assert "SL 1" in data["missing_prereqs"]
