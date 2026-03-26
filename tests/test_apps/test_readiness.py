"""Tests for the Training Readiness Tracker."""

from __future__ import annotations

import io
import pytest


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def create_trainee(client, dodid="1234567890", **overrides):
    payload = {
        "dodid": dodid,
        "last_name": "KELLY",
        "first_name": "JAMES",
        "rank": "SGT",
        "unit": "2-1 BN",
        "mos": "17C",
        **overrides,
    }
    resp = client.post("/trainees", json=payload)
    assert resp.status_code == 201
    return resp.json()


def record_go(client, dodid, course_id, eval_date="2026-01-15"):
    payload = {
        "dodid": dodid,
        "course_id": course_id,
        "result": "GO",
        "evaluation_date": eval_date,
        "evaluator_name": "MAJ SMITH",
    }
    return client.post("/completions", json=payload)


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------
class TestHealth:
    def test_health(self, readiness_client):
        resp = readiness_client.get("/health")
        assert resp.status_code == 200
        assert resp.json()["status"] == "ok"


# ---------------------------------------------------------------------------
# Trainees
# ---------------------------------------------------------------------------
class TestTrainees:
    def test_create_trainee(self, readiness_client):
        data = create_trainee(readiness_client)
        assert data["dodid"] == "1234567890"
        assert data["last_name"] == "KELLY"

    def test_duplicate_trainee_409(self, readiness_client):
        create_trainee(readiness_client)
        resp = readiness_client.post("/trainees", json={
            "dodid": "1234567890", "last_name": "X", "first_name": "Y",
            "rank": "PVT", "unit": "1-1 BN",
        })
        assert resp.status_code == 409

    def test_list_trainees(self, readiness_client):
        create_trainee(readiness_client, dodid="1111111111")
        create_trainee(readiness_client, dodid="2222222222", unit="3-2 BN")
        resp = readiness_client.get("/trainees")
        assert resp.status_code == 200
        assert len(resp.json()) == 2

    def test_list_trainees_by_unit(self, readiness_client):
        create_trainee(readiness_client, dodid="1111111111", unit="2-1 BN")
        create_trainee(readiness_client, dodid="2222222222", unit="3-2 BN")
        resp = readiness_client.get("/trainees", params={"unit": "2-1 BN"})
        assert len(resp.json()) == 1

    def test_get_trainee_404(self, readiness_client):
        resp = readiness_client.get("/trainees/9999999999")
        assert resp.status_code == 404

    def test_get_trainee_with_recommendations(self, readiness_client):
        create_trainee(readiness_client)
        resp = readiness_client.get("/trainees/1234567890")
        assert resp.status_code == 200
        data = resp.json()
        # New trainee should be recommended SL 1
        assert "SL 1" in data["next_recommended"]


# ---------------------------------------------------------------------------
# Prereq Chain — the critical business logic
# ---------------------------------------------------------------------------
class TestPrereqChain:
    @pytest.mark.parametrize("course,prereqs", [
        ("SL 2", ["SL 1"]),
        ("SL 3", ["SL 2"]),
        ("SL 4A", ["SL 3"]),
        ("SL 4G", ["SL 3"]),
        ("SL 4L", ["SL 3"]),
        ("SL 5G", ["SL 4G"]),
        ("SL 5L", ["SL 4L"]),
        ("FBC", ["SL 2"]),
    ])
    def test_prereq_blocks_without_completion(self, readiness_client, course, prereqs):
        """Cannot record GO without prereqs met."""
        create_trainee(readiness_client)
        resp = record_go(readiness_client, "1234567890", course)
        assert resp.status_code == 422
        detail = resp.json()["detail"]
        for prereq in prereqs:
            assert prereq in detail

    def test_tm10_has_no_prereqs(self, readiness_client):
        create_trainee(readiness_client)
        resp = record_go(readiness_client, "1234567890", "SL 1")
        assert resp.status_code == 201

    def test_full_chain_tm10_to_tm40g(self, readiness_client):
        """Walk the full chain: SL 1 → SL 2 → SL 3 → SL 4G."""
        create_trainee(readiness_client)
        assert record_go(readiness_client, "1234567890", "SL 1").status_code == 201
        assert record_go(readiness_client, "1234567890", "SL 2").status_code == 201
        assert record_go(readiness_client, "1234567890", "SL 3").status_code == 201
        assert record_go(readiness_client, "1234567890", "SL 4G").status_code == 201

    def test_full_chain_to_tm50g(self, readiness_client):
        """Walk chain to advanced: SL 1 → SL 2 → SL 3 → SL 4G → SL 5G."""
        create_trainee(readiness_client)
        for course in ["SL 1", "SL 2", "SL 3", "SL 4G"]:
            assert record_go(readiness_client, "1234567890", course).status_code == 201
        assert record_go(readiness_client, "1234567890", "SL 5G").status_code == 201

    def test_fbc_does_not_grant_tm30(self, readiness_client):
        """FBC completion does NOT satisfy SL 3 prereq for SL 4."""
        create_trainee(readiness_client)
        assert record_go(readiness_client, "1234567890", "SL 1").status_code == 201
        assert record_go(readiness_client, "1234567890", "SL 2").status_code == 201
        assert record_go(readiness_client, "1234567890", "FBC").status_code == 201
        # SL 4G requires SL 3, not FBC
        resp = record_go(readiness_client, "1234567890", "SL 4G")
        assert resp.status_code == 422
        assert "SL 3" in resp.json()["detail"]

    def test_no_go_does_not_satisfy_prereq(self, readiness_client):
        """NO_GO result should not count as prereq completion."""
        create_trainee(readiness_client)
        # Record SL 1 as NO_GO
        resp = readiness_client.post("/completions", json={
            "dodid": "1234567890", "course_id": "SL 1",
            "result": "NO_GO", "evaluation_date": "2026-01-15",
        })
        assert resp.status_code == 201
        # SL 2 should still be blocked
        resp = record_go(readiness_client, "1234567890", "SL 2")
        assert resp.status_code == 422

    def test_unknown_course_rejected(self, readiness_client):
        """SL 5A through SL 5F do not exist."""
        create_trainee(readiness_client)
        resp = record_go(readiness_client, "1234567890", "SL 5A")
        assert resp.status_code == 422


# ---------------------------------------------------------------------------
# Eligibility endpoint
# ---------------------------------------------------------------------------
class TestEligibility:
    def test_eligible_for_tm10(self, readiness_client):
        create_trainee(readiness_client)
        resp = readiness_client.get("/eligibility/1234567890/SL 1")
        assert resp.status_code == 200
        assert resp.json()["eligible"] is True

    def test_not_eligible_for_tm20(self, readiness_client):
        create_trainee(readiness_client)
        resp = readiness_client.get("/eligibility/1234567890/SL 2")
        data = resp.json()
        assert data["eligible"] is False
        assert "SL 1" in data["missing_prereqs"]


# ---------------------------------------------------------------------------
# Unit rollup
# ---------------------------------------------------------------------------
class TestRollup:
    def test_rollup_counts(self, readiness_client):
        create_trainee(readiness_client, dodid="1111111111", unit="2-1 BN")
        create_trainee(readiness_client, dodid="2222222222", unit="2-1 BN")
        record_go(readiness_client, "1111111111", "SL 1")
        record_go(readiness_client, "2222222222", "SL 1")
        record_go(readiness_client, "1111111111", "SL 2")

        resp = readiness_client.get("/rollup/2-1 BN")
        assert resp.status_code == 200
        data = resp.json()
        assert data["total_trainees"] == 2
        assert data["course_counts"]["SL 1"] == 2
        assert data["course_counts"]["SL 2"] == 1


# ---------------------------------------------------------------------------
# CSV Upload
# ---------------------------------------------------------------------------
class TestCSVUpload:
    def test_roster_upload(self, readiness_client):
        csv_content = "dodid,last_name,first_name,rank,unit,mos\n1111111111,DOE,JOHN,SPC,1-1 BN,25B\n"
        resp = readiness_client.post(
            "/upload/roster",
            files={"file": ("roster.csv", csv_content.encode(), "text/csv")},
        )
        assert resp.status_code == 200
        assert resp.json()["accepted"] == 1

        # Verify trainee was created
        resp = readiness_client.get("/trainees/1111111111")
        assert resp.status_code == 200
        assert resp.json()["last_name"] == "DOE"

    def test_completions_upload_with_prereq_check(self, readiness_client):
        create_trainee(readiness_client, dodid="1111111111")
        record_go(readiness_client, "1111111111", "SL 1")

        # SL 2 should succeed (prereq SL 1 met), SL 3 should fail (prereq SL 2 not met)
        csv_content = (
            "dodid,course_id,result,evaluation_date,evaluator_name\n"
            "1111111111,SL 2,GO,2026-02-01,MAJ SMITH\n"
            "1111111111,SL 3,GO,2026-02-15,MAJ SMITH\n"
        )
        resp = readiness_client.post(
            "/upload/completions",
            files={"file": ("comps.csv", csv_content.encode(), "text/csv")},
        )
        assert resp.status_code == 200
        data = resp.json()
        assert data["accepted"] == 1
        assert data["rejected"] == 1


# ---------------------------------------------------------------------------
# Export
# ---------------------------------------------------------------------------
class TestExport:
    def test_csv_export(self, readiness_client):
        create_trainee(readiness_client)
        record_go(readiness_client, "1234567890", "SL 1")
        resp = readiness_client.get("/export/csv")
        assert resp.status_code == 200
        assert "text/csv" in resp.headers["content-type"]
        assert "SL 1" in resp.text
