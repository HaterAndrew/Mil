"""Tests for the MTT Scheduler."""

from __future__ import annotations

import pytest


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def create_event(client, **overrides):
    payload = {
        "name": "SL 2 MTT Wiesbaden",
        "course_id": "SL 2",
        "location": "Clay Kaserne",
        "start_date": "2026-04-01",
        "end_date": "2026-04-03",
        "max_capacity": 20,
        **overrides,
    }
    resp = client.post("/events", json=payload)
    assert resp.status_code == 201
    return resp.json()


def create_instructor(client, **overrides):
    payload = {
        "name": "SMITH",
        "rank": "SFC",
        "unit": "2-1 BN",
        "qualifications": ["SL 2", "SL 3"],
        "available_from": "2026-01-01",
        "available_to": "2026-12-31",
        **overrides,
    }
    resp = client.post("/instructors", json=payload)
    assert resp.status_code == 201
    return resp.json()


def create_venue(client, **overrides):
    payload = {
        "name": "Bldg 1042 Lab",
        "location": "Clay Kaserne",
        "capacity": 30,
        "has_network": True,
        "has_sipr": False,
        **overrides,
    }
    resp = client.post("/venues", json=payload)
    assert resp.status_code == 201
    return resp.json()


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------
class TestHealth:
    def test_health(self, mtt_client):
        resp = mtt_client.get("/health")
        assert resp.status_code == 200
        assert resp.json()["status"] == "ok"


# ---------------------------------------------------------------------------
# Events CRUD
# ---------------------------------------------------------------------------
class TestEvents:
    def test_create_event(self, mtt_client):
        data = create_event(mtt_client)
        assert data["name"] == "SL 2 MTT Wiesbaden"
        assert data["status"] == "PLANNED"
        assert data["enrolled_count"] == 0

    def test_list_events(self, mtt_client):
        create_event(mtt_client, name="Event A")
        create_event(mtt_client, name="Event B")
        resp = mtt_client.get("/events")
        assert resp.status_code == 200
        assert len(resp.json()) == 2

    def test_list_events_by_status(self, mtt_client):
        create_event(mtt_client)
        resp = mtt_client.get("/events", params={"status": "PLANNED"})
        assert len(resp.json()) == 1
        resp = mtt_client.get("/events", params={"status": "COMPLETE"})
        assert len(resp.json()) == 0

    def test_get_event_404(self, mtt_client):
        resp = mtt_client.get("/events/999")
        assert resp.status_code == 404

    def test_update_event(self, mtt_client):
        ev = create_event(mtt_client)
        payload = {
            "name": "Updated Event",
            "course_id": "SL 3",
            "location": "Grafenwoehr",
            "start_date": "2026-05-01",
            "end_date": "2026-05-03",
            "max_capacity": 25,
        }
        resp = mtt_client.put(f"/events/{ev['id']}", json=payload)
        assert resp.status_code == 200
        assert resp.json()["name"] == "Updated Event"

    def test_update_event_status(self, mtt_client):
        ev = create_event(mtt_client)
        resp = mtt_client.patch(f"/events/{ev['id']}/status", params={"status": "ACTIVE"})
        assert resp.status_code == 200
        assert resp.json()["status"] == "ACTIVE"

    def test_invalid_status(self, mtt_client):
        ev = create_event(mtt_client)
        resp = mtt_client.patch(f"/events/{ev['id']}/status", params={"status": "INVALID"})
        assert resp.status_code == 422


# ---------------------------------------------------------------------------
# Instructors
# ---------------------------------------------------------------------------
class TestInstructors:
    def test_create_instructor(self, mtt_client):
        data = create_instructor(mtt_client)
        assert data["name"] == "SMITH"
        assert data["rank"] == "SFC"

    def test_list_instructors(self, mtt_client):
        create_instructor(mtt_client, name="Alpha")
        create_instructor(mtt_client, name="Bravo")
        resp = mtt_client.get("/instructors")
        assert len(resp.json()) == 2

    def test_get_instructor_404(self, mtt_client):
        resp = mtt_client.get("/instructors/999")
        assert resp.status_code == 404

    def test_delete_instructor(self, mtt_client):
        inst = create_instructor(mtt_client)
        resp = mtt_client.delete(f"/instructors/{inst['id']}")
        assert resp.status_code == 204


# ---------------------------------------------------------------------------
# Instructor assignment
# ---------------------------------------------------------------------------
class TestAssignment:
    def test_assign_instructor_to_event(self, mtt_client):
        ev = create_event(mtt_client)
        inst = create_instructor(mtt_client)
        resp = mtt_client.post(f"/events/{ev['id']}/instructors/{inst['id']}")
        assert resp.status_code == 200

    def test_duplicate_assignment_409(self, mtt_client):
        ev = create_event(mtt_client)
        inst = create_instructor(mtt_client)
        mtt_client.post(f"/events/{ev['id']}/instructors/{inst['id']}")
        resp = mtt_client.post(f"/events/{ev['id']}/instructors/{inst['id']}")
        assert resp.status_code == 409

    def test_unassign_instructor(self, mtt_client):
        ev = create_event(mtt_client)
        inst = create_instructor(mtt_client)
        mtt_client.post(f"/events/{ev['id']}/instructors/{inst['id']}")
        resp = mtt_client.delete(f"/events/{ev['id']}/instructors/{inst['id']}")
        assert resp.status_code == 200

    def test_unassign_not_assigned_404(self, mtt_client):
        ev = create_event(mtt_client)
        inst = create_instructor(mtt_client)
        resp = mtt_client.delete(f"/events/{ev['id']}/instructors/{inst['id']}")
        assert resp.status_code == 404


# ---------------------------------------------------------------------------
# Enrollments
# ---------------------------------------------------------------------------
class TestEnrollments:
    def test_enroll_soldier(self, mtt_client):
        ev = create_event(mtt_client)
        resp = mtt_client.post("/enrollments", json={
            "event_id": ev["id"],
            "dodid": "1234567890",
            "soldier_name": "DOE JOHN",
            "soldier_rank": "SPC",
            "soldier_unit": "2-1 BN",
        })
        assert resp.status_code == 201
        assert resp.json()["status"] == "ENROLLED"

    def test_duplicate_enrollment_409(self, mtt_client):
        ev = create_event(mtt_client)
        enroll_payload = {
            "event_id": ev["id"],
            "dodid": "1234567890",
            "soldier_name": "DOE JOHN",
            "soldier_rank": "SPC",
            "soldier_unit": "2-1 BN",
        }
        mtt_client.post("/enrollments", json=enroll_payload)
        resp = mtt_client.post("/enrollments", json=enroll_payload)
        assert resp.status_code == 409

    def test_over_capacity_422(self, mtt_client):
        ev = create_event(mtt_client, max_capacity=1)
        mtt_client.post("/enrollments", json={
            "event_id": ev["id"],
            "dodid": "1111111111",
            "soldier_name": "A",
            "soldier_rank": "PVT",
            "soldier_unit": "1BN",
        })
        resp = mtt_client.post("/enrollments", json={
            "event_id": ev["id"],
            "dodid": "2222222222",
            "soldier_name": "B",
            "soldier_rank": "PVT",
            "soldier_unit": "1BN",
        })
        assert resp.status_code == 422


# ---------------------------------------------------------------------------
# Venues
# ---------------------------------------------------------------------------
class TestVenues:
    def test_create_venue(self, mtt_client):
        data = create_venue(mtt_client)
        assert data["name"] == "Bldg 1042 Lab"
        assert data["has_network"] is True

    def test_list_venues(self, mtt_client):
        create_venue(mtt_client, name="Venue A")
        create_venue(mtt_client, name="Venue B")
        resp = mtt_client.get("/venues")
        assert len(resp.json()) == 2

    def test_delete_venue_with_events_409(self, mtt_client):
        venue = create_venue(mtt_client)
        create_event(mtt_client, venue_id=venue["id"])
        resp = mtt_client.delete(f"/venues/{venue['id']}")
        assert resp.status_code == 409

    def test_delete_unused_venue(self, mtt_client):
        venue = create_venue(mtt_client)
        resp = mtt_client.delete(f"/venues/{venue['id']}")
        assert resp.status_code == 204


# ---------------------------------------------------------------------------
# Analytics
# ---------------------------------------------------------------------------
class TestAnalytics:
    def test_calendar_empty(self, mtt_client):
        resp = mtt_client.get("/calendar")
        assert resp.status_code == 200
        assert resp.json() == []

    def test_calendar_with_event(self, mtt_client):
        create_event(mtt_client)
        resp = mtt_client.get("/calendar")
        data = resp.json()
        assert len(data) == 1
        assert data[0]["course_id"] == "SL 2"

    def test_conflicts_none(self, mtt_client):
        resp = mtt_client.get("/conflicts")
        assert resp.status_code == 200
        assert resp.json() == []

    def test_utilization(self, mtt_client):
        create_event(mtt_client)
        resp = mtt_client.get("/utilization")
        assert resp.status_code == 200
        assert len(resp.json()) == 1
        assert resp.json()[0]["fill_pct"] == 0.0
