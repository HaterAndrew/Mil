"""Tests for the Instructor Certification Manager."""

from __future__ import annotations

from datetime import date, timedelta


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def create_instructor(client, instructor_id="INS001", **overrides):
    payload = {
        "instructor_id": instructor_id,
        "last_name": "JONES",
        "first_name": "SARAH",
        "rank": "SFC",
        "unit": "2-1 BN",
        "mos": "17C",
        **overrides,
    }
    resp = client.post("/instructors", json=payload)
    assert resp.status_code == 201
    return resp.json()


def create_cert(client, instructor_id="INS001", course_id="SL 1", **overrides):
    today = date.today()
    payload = {
        "instructor_id": instructor_id,
        "course_id": course_id,
        "certified_date": (today - timedelta(days=180)).isoformat(),
        "expiration_date": (today + timedelta(days=180)).isoformat(),
        **overrides,
    }
    resp = client.post("/certifications", json=payload)
    assert resp.status_code == 201
    return resp.json()


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------
class TestHealth:
    def test_health(self, instructor_client):
        resp = instructor_client.get("/health")
        assert resp.status_code == 200
        assert resp.json()["status"] == "ok"


# ---------------------------------------------------------------------------
# Instructors
# ---------------------------------------------------------------------------
class TestInstructors:
    def test_create_instructor(self, instructor_client):
        data = create_instructor(instructor_client)
        assert data["instructor_id"] == "INS001"
        assert data["last_name"] == "JONES"

    def test_duplicate_instructor_409(self, instructor_client):
        create_instructor(instructor_client)
        resp = instructor_client.post("/instructors", json={
            "instructor_id": "INS001",
            "last_name": "X", "first_name": "Y",
            "rank": "PVT", "unit": "1-1 BN", "mos": "25B",
        })
        assert resp.status_code == 409

    def test_list_instructors(self, instructor_client):
        create_instructor(instructor_client, instructor_id="INS001")
        create_instructor(instructor_client, instructor_id="INS002")
        resp = instructor_client.get("/instructors")
        assert len(resp.json()) == 2

    def test_list_by_unit(self, instructor_client):
        create_instructor(instructor_client, instructor_id="INS001", unit="2-1 BN")
        create_instructor(instructor_client, instructor_id="INS002", unit="3-2 BN")
        resp = instructor_client.get("/instructors", params={"unit": "2-1 BN"})
        assert len(resp.json()) == 1

    def test_get_instructor_404(self, instructor_client):
        resp = instructor_client.get("/instructors/NONEXIST")
        assert resp.status_code == 404


# ---------------------------------------------------------------------------
# Certifications
# ---------------------------------------------------------------------------
class TestCertifications:
    def test_create_certification(self, instructor_client):
        create_instructor(instructor_client)
        data = create_cert(instructor_client)
        assert data["course_id"] == "SL 1"
        assert data["status"] == "CURRENT"

    def test_cert_requires_instructor(self, instructor_client):
        resp = instructor_client.post("/certifications", json={
            "instructor_id": "NONEXIST",
            "course_id": "SL 1",
            "certified_date": "2026-01-01",
            "expiration_date": "2027-01-01",
        })
        assert resp.status_code == 404

    def test_cert_validates_course(self, instructor_client):
        create_instructor(instructor_client)
        resp = instructor_client.post("/certifications", json={
            "instructor_id": "INS001",
            "course_id": "FAKE-99",
            "certified_date": "2026-01-01",
            "expiration_date": "2027-01-01",
        })
        assert resp.status_code == 422

    def test_list_certifications(self, instructor_client):
        create_instructor(instructor_client)
        create_cert(instructor_client, course_id="SL 1")
        create_cert(instructor_client, course_id="SL 2")
        resp = instructor_client.get("/certifications")
        assert len(resp.json()) == 2

    def test_filter_by_instructor(self, instructor_client):
        create_instructor(instructor_client, instructor_id="INS001")
        create_instructor(instructor_client, instructor_id="INS002")
        create_cert(instructor_client, instructor_id="INS001")
        create_cert(instructor_client, instructor_id="INS002")
        resp = instructor_client.get("/certifications", params={"instructor_id": "INS001"})
        assert len(resp.json()) == 1


# ---------------------------------------------------------------------------
# Expiring certifications
# ---------------------------------------------------------------------------
class TestExpiring:
    def test_expiring_within_window(self, instructor_client):
        create_instructor(instructor_client)
        today = date.today()
        create_cert(
            instructor_client,
            expiration_date=(today + timedelta(days=15)).isoformat(),
        )
        resp = instructor_client.get("/certifications/expiring", params={"days": 30})
        assert resp.status_code == 200
        data = resp.json()
        assert len(data) == 1
        assert data[0]["rag"] == "RED"  # <30 days

    def test_not_expiring_outside_window(self, instructor_client):
        create_instructor(instructor_client)
        today = date.today()
        create_cert(
            instructor_client,
            expiration_date=(today + timedelta(days=365)).isoformat(),
        )
        resp = instructor_client.get("/certifications/expiring", params={"days": 30})
        assert len(resp.json()) == 0


# ---------------------------------------------------------------------------
# Teaching history
# ---------------------------------------------------------------------------
class TestTeachingHistory:
    def test_record_teaching(self, instructor_client):
        create_instructor(instructor_client)
        resp = instructor_client.post("/teaching-history", json={
            "instructor_id": "INS001",
            "course_id": "SL 1",
            "event_date": "2026-03-01",
            "location": "Clay Kaserne",
            "students_count": 15,
            "rating": "EXCELLENT",
        })
        assert resp.status_code == 201

    def test_teaching_requires_instructor(self, instructor_client):
        resp = instructor_client.post("/teaching-history", json={
            "instructor_id": "NONEXIST",
            "course_id": "SL 1",
            "event_date": "2026-03-01",
        })
        assert resp.status_code == 404


# ---------------------------------------------------------------------------
# Coverage matrix
# ---------------------------------------------------------------------------
class TestCoverage:
    def test_coverage_matrix(self, instructor_client):
        create_instructor(instructor_client)
        create_cert(instructor_client, course_id="SL 1")
        resp = instructor_client.get("/coverage")
        assert resp.status_code == 200
        data = resp.json()
        # Should have an entry for SL 1 with count >= 1
        tm10 = [c for c in data if c["course_id"] == "SL 1"]
        assert len(tm10) == 1
        assert tm10[0]["certified_count"] >= 1


# ---------------------------------------------------------------------------
# Export
# ---------------------------------------------------------------------------
class TestExport:
    def test_csv_export(self, instructor_client):
        create_instructor(instructor_client)
        create_cert(instructor_client)
        resp = instructor_client.get("/export/csv")
        assert resp.status_code == 200
        assert "text/csv" in resp.headers["content-type"]
        assert "INS001" in resp.text
