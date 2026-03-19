"""Tests for the Enrollment Manager."""

from __future__ import annotations


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def create_class(client, **overrides):
    payload = {
        "course_id": "TM-20",
        "class_name": "TM-20 Cycle 1",
        "start_date": "2026-04-01",
        "end_date": "2026-04-03",
        "location": "Clay Kaserne",
        "max_seats": 20,
        **overrides,
    }
    resp = client.post("/classes", json=payload)
    assert resp.status_code == 201
    return resp.json()


def enroll(client, class_id, dodid="1234567890", **overrides):
    payload = {
        "dodid": dodid,
        "last_name": "DOE",
        "first_name": "JOHN",
        "rank": "SPC",
        "unit": "2-1 BN",
        **overrides,
    }
    return client.post(f"/classes/{class_id}/enroll", json=payload)


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------
class TestHealth:
    def test_health(self, enrollment_client):
        resp = enrollment_client.get("/health")
        assert resp.status_code == 200
        assert resp.json()["status"] == "ok"


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------
class TestClasses:
    def test_create_class(self, enrollment_client):
        data = create_class(enrollment_client)
        assert data["course_id"] == "TM-20"
        assert data["status"] == "SCHEDULED"

    def test_list_classes(self, enrollment_client):
        create_class(enrollment_client, class_name="A")
        create_class(enrollment_client, class_name="B")
        resp = enrollment_client.get("/classes")
        assert len(resp.json()) == 2

    def test_list_by_status(self, enrollment_client):
        create_class(enrollment_client)
        resp = enrollment_client.get("/classes", params={"status": "SCHEDULED"})
        assert len(resp.json()) == 1
        resp = enrollment_client.get("/classes", params={"status": "COMPLETED"})
        assert len(resp.json()) == 0

    def test_get_class_404(self, enrollment_client):
        resp = enrollment_client.get("/classes/999")
        assert resp.status_code == 404


# ---------------------------------------------------------------------------
# Enrollment
# ---------------------------------------------------------------------------
class TestEnrollment:
    def test_enroll_student(self, enrollment_client):
        tc = create_class(enrollment_client)
        resp = enroll(enrollment_client, tc["class_id"])
        assert resp.status_code == 200
        assert resp.json()["status"] == "enrolled"

    def test_duplicate_enrollment(self, enrollment_client):
        tc = create_class(enrollment_client)
        enroll(enrollment_client, tc["class_id"])
        resp = enroll(enrollment_client, tc["class_id"])
        assert resp.status_code == 422

    def test_auto_waitlist_when_full(self, enrollment_client):
        tc = create_class(enrollment_client, max_seats=1)
        resp1 = enroll(enrollment_client, tc["class_id"], dodid="1111111111")
        assert resp1.json()["status"] == "enrolled"
        resp2 = enroll(enrollment_client, tc["class_id"], dodid="2222222222")
        assert resp2.json()["status"] == "waitlisted"


# ---------------------------------------------------------------------------
# Roster & availability
# ---------------------------------------------------------------------------
class TestRoster:
    def test_roster(self, enrollment_client):
        tc = create_class(enrollment_client)
        enroll(enrollment_client, tc["class_id"])
        resp = enrollment_client.get(f"/classes/{tc['class_id']}/roster")
        assert resp.status_code == 200
        assert len(resp.json()) == 1

    def test_availability(self, enrollment_client):
        tc = create_class(enrollment_client, max_seats=5)
        enroll(enrollment_client, tc["class_id"])
        resp = enrollment_client.get(f"/classes/{tc['class_id']}/availability")
        data = resp.json()
        assert data["max_seats"] == 5
        assert data["enrolled_count"] == 1
        assert data["seats_remaining"] == 4

    def test_availability_404(self, enrollment_client):
        resp = enrollment_client.get("/classes/999/availability")
        assert resp.status_code == 404


# ---------------------------------------------------------------------------
# Waitlist promotion
# ---------------------------------------------------------------------------
class TestWaitlist:
    def test_promote_waitlist_no_seats(self, enrollment_client):
        """Promote returns 0 when no seats are available."""
        tc = create_class(enrollment_client, max_seats=1)
        enroll(enrollment_client, tc["class_id"], dodid="1111111111")
        enroll(enrollment_client, tc["class_id"], dodid="2222222222")  # waitlisted
        resp = enrollment_client.post(f"/classes/{tc['class_id']}/promote-waitlist")
        assert resp.status_code == 200
        assert resp.json()["promoted_count"] == 0

    def test_promote_waitlist_with_seats(self, enrollment_db, enrollment_client):
        """Promote moves waitlisted student to enrolled when seat freed via DB."""
        from enrollment_manager.db import Enrollment

        tc = create_class(enrollment_client, max_seats=1)
        enroll(enrollment_client, tc["class_id"], dodid="1111111111")
        enroll(enrollment_client, tc["class_id"], dodid="2222222222")  # waitlisted

        # Drop enrollment directly in DB to free a seat
        db = enrollment_db()
        e = db.query(Enrollment).filter(Enrollment.dodid == "1111111111").first()
        e.status = "DROPPED"
        db.commit()
        db.close()

        resp = enrollment_client.post(f"/classes/{tc['class_id']}/promote-waitlist")
        assert resp.status_code == 200
        assert resp.json()["promoted_count"] == 1

    def test_waitlist_list(self, enrollment_client):
        tc = create_class(enrollment_client, max_seats=1)
        enroll(enrollment_client, tc["class_id"], dodid="1111111111")
        enroll(enrollment_client, tc["class_id"], dodid="2222222222")
        resp = enrollment_client.get(f"/classes/{tc['class_id']}/waitlist")
        assert resp.status_code == 200
        assert len(resp.json()) == 1


# ---------------------------------------------------------------------------
# Stats & student lookup
# ---------------------------------------------------------------------------
class TestStats:
    def test_enrollment_stats(self, enrollment_client):
        tc = create_class(enrollment_client)
        enroll(enrollment_client, tc["class_id"])
        resp = enrollment_client.get("/stats")
        assert resp.status_code == 200
        data = resp.json()
        assert data["total_classes"] == 1
        assert data["total_enrolled"] == 1

    def test_student_enrollments(self, enrollment_client):
        tc = create_class(enrollment_client)
        enroll(enrollment_client, tc["class_id"])
        resp = enrollment_client.get("/students/1234567890/enrollments")
        assert resp.status_code == 200
        assert len(resp.json()) == 1


# ---------------------------------------------------------------------------
# Export
# ---------------------------------------------------------------------------
class TestExport:
    def test_csv_export(self, enrollment_client):
        tc = create_class(enrollment_client)
        enroll(enrollment_client, tc["class_id"])
        resp = enrollment_client.get("/export/csv")
        assert resp.status_code == 200
        assert "text/csv" in resp.headers["content-type"]
        assert "DOE" in resp.text
