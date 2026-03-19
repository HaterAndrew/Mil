"""Tests for the AAR Aggregator."""

from __future__ import annotations

import pytest

from apps.aar_aggregator.db import parse_aar_file


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
SAMPLE_AAR = {
    "date": "2026-01-27",
    "tm_levels": ["TM-10"],
    "exercises": ["EX_10"],
    "location": "MSS sandbox",
    "student_count": 12,
    "instructor_names": ["MAJ SMITH"],
    "planned_objectives": "Complete TM-10 ELOs.",
    "actual_execution": "All objectives completed on time.",
    "sustains": ["Dashboard walkthrough was effective", "Printed reference cards helped"],
    "improves": [
        {
            "problem": "Environment access delayed start",
            "proposed_fix": "Pre-provision accounts",
            "owner": "C2DAO",
            "priority": "H",
            "category": "MISSION_COMMAND",
        }
    ],
    "evaluations": [
        {"trainee_name": "SGT JONES", "tm_level": "TM-10", "result": "GO", "notes": None}
    ],
    "discrepancies": [
        {
            "document": "TM-10 Section 2.1",
            "section_page": "p. 8",
            "issue_description": "Screenshot outdated",
            "severity": "M",
        }
    ],
    "env_issues": [
        {"issue": "Login delay", "impact": "30 min lost", "resolution": "Coordinated with C2DAO"}
    ],
    "instructor_recommendations": "Add 15-min buffer.",
    "submitted_by": "MAJ SMITH",
}


def create_aar(client, overrides: dict | None = None):
    payload = {**SAMPLE_AAR, **(overrides or {})}
    resp = client.post("/aars", json=payload)
    assert resp.status_code == 201
    return resp.json()


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------
class TestHealth:
    def test_health(self, aar_client):
        resp = aar_client.get("/health")
        assert resp.status_code == 200


# ---------------------------------------------------------------------------
# AAR CRUD
# ---------------------------------------------------------------------------
class TestAARCrud:
    def test_create_aar_with_nested_items(self, aar_client):
        data = create_aar(aar_client)
        assert data["id"] >= 1
        assert data["sustain_count"] == 2
        assert data["improve_count"] == 1

    def test_get_aar_detail(self, aar_client):
        created = create_aar(aar_client)
        resp = aar_client.get(f"/aars/{created['id']}")
        assert resp.status_code == 200
        detail = resp.json()
        assert detail["location"] == "MSS sandbox"
        assert len(detail["sustains"]) == 2
        assert len(detail["improves"]) == 1
        assert len(detail["evaluations"]) == 1
        assert len(detail["discrepancies"]) == 1
        assert len(detail["env_issues"]) == 1

    def test_list_aars(self, aar_client):
        create_aar(aar_client)
        create_aar(aar_client, {"date": "2026-02-15", "location": "Live instance"})
        resp = aar_client.get("/aars")
        assert len(resp.json()) == 2

    def test_list_aars_date_filter(self, aar_client):
        create_aar(aar_client, {"date": "2026-01-15"})
        create_aar(aar_client, {"date": "2026-03-15"})
        resp = aar_client.get("/aars", params={"date_from": "2026-02-01"})
        assert len(resp.json()) == 1

    def test_delete_aar_cascades(self, aar_client):
        created = create_aar(aar_client)
        aar_id = created["id"]

        # Verify it exists
        assert aar_client.get(f"/aars/{aar_id}").status_code == 200

        # Delete
        resp = aar_client.delete(f"/aars/{aar_id}")
        assert resp.status_code == 204

        # Verify gone
        assert aar_client.get(f"/aars/{aar_id}").status_code == 404

    def test_get_nonexistent_aar(self, aar_client):
        assert aar_client.get("/aars/9999").status_code == 404


# ---------------------------------------------------------------------------
# Recurring Issues
# ---------------------------------------------------------------------------
class TestRecurringIssues:
    def test_recurring_issues_detected(self, aar_client):
        """Same problem in 2 AARs should be flagged."""
        same_problem = [{
            "problem": "Environment access delayed start",
            "priority": "H",
            "category": "MISSION_COMMAND",
        }]
        create_aar(aar_client, {"date": "2026-01-15", "improves": same_problem})
        create_aar(aar_client, {"date": "2026-02-15", "improves": same_problem})

        resp = aar_client.get("/trends/recurring", params={"min_count": 2})
        assert resp.status_code == 200
        recurring = resp.json()
        assert len(recurring) >= 1
        assert recurring[0]["count"] >= 2

    def test_no_recurring_with_different_problems(self, aar_client):
        create_aar(aar_client, {"improves": [{"problem": "Problem A", "priority": "M"}]})
        create_aar(aar_client, {"improves": [{"problem": "Problem B", "priority": "M"}]})

        resp = aar_client.get("/trends/recurring", params={"min_count": 2})
        assert len(resp.json()) == 0


# ---------------------------------------------------------------------------
# Trends
# ---------------------------------------------------------------------------
class TestTrends:
    def test_trend_by_category(self, aar_client):
        create_aar(aar_client)
        resp = aar_client.get("/trends/category")
        assert resp.status_code == 200
        cats = resp.json()
        assert any(c["category"] == "MISSION_COMMAND" for c in cats)

    def test_trend_over_time(self, aar_client):
        create_aar(aar_client, {"date": "2026-01-15"})
        create_aar(aar_client, {"date": "2026-02-15"})
        resp = aar_client.get("/trends/over-time")
        assert resp.status_code == 200
        months = resp.json()
        assert len(months) >= 1


# ---------------------------------------------------------------------------
# Discrepancies
# ---------------------------------------------------------------------------
class TestDiscrepancies:
    def test_list_discrepancies(self, aar_client):
        create_aar(aar_client)
        resp = aar_client.get("/discrepancies")
        assert resp.status_code == 200
        assert len(resp.json()) >= 1

    def test_filter_by_severity(self, aar_client):
        create_aar(aar_client)
        resp = aar_client.get("/discrepancies", params={"severity": "M"})
        discs = resp.json()
        assert all(d["severity"] == "M" for d in discs)


# ---------------------------------------------------------------------------
# File parser
# ---------------------------------------------------------------------------
class TestFileParser:
    def test_parse_aar_template(self):
        content = """# After-Action Review

## Section 1 — Event Details
Date: 2026-01-27
TM Levels: TM-10
Exercises: EX_10
Location: MSS sandbox
Number of Students: 12
Instructors: MAJ SMITH, SGT KELLY

## Section 2 — What Was Planned
Complete all TM-10 ELOs.

## Section 3 — What Actually Happened
All objectives completed on schedule.

## Section 4 — Sustain
- Dashboard walkthrough well received
- Reference cards helped

## Section 5 — Improve
- Environment access delayed start

## Section 9 — Instructor Recommendations
Add 15-minute buffer for access setup.

## Section 10 — Sign-Off
Instructor: MAJ SMITH
"""
        result = parse_aar_file(content)
        assert result["date"] == "2026-01-27"
        assert "TM-10" in result["tm_levels"]
        assert result["location"] == "MSS sandbox"
        assert result["student_count"] == 12
        assert len(result["sustains"]) == 2
        assert len(result["improves"]) >= 1

    def test_parse_minimal_file(self):
        content = """## Section 2 — What Was Planned
Some objectives.

## Section 3 — What Actually Happened
Did the thing.

## Section 4 — Sustain
- It worked
"""
        result = parse_aar_file(content)
        assert "planned_objectives" in result
        assert len(result["sustains"]) >= 1


# ---------------------------------------------------------------------------
# File upload endpoint
# ---------------------------------------------------------------------------
class TestFileUpload:
    def test_upload_parse(self, aar_client):
        content = """## Section 1 — Event Details
Date: 2026-03-01
TM Levels: TM-30
Location: Live training
Number of Students: 6
Instructors: CW3 DAVIS

## Section 2 — What Was Planned
Build pipelines.

## Section 3 — What Actually Happened
All objectives met.

## Section 4 — Sustain
- Good discussion on governance

## Section 5 — Improve
- Need more time for governance module

## Section 10 — Sign-Off
Instructor: CW3 DAVIS
"""
        resp = aar_client.post(
            "/upload/parse",
            files={"file": ("aar.md", content.encode(), "text/plain")},
        )
        assert resp.status_code == 200
        data = resp.json()
        assert "parsed" in data
        assert data["parsed"]["date"] == "2026-03-01"


# ---------------------------------------------------------------------------
# WFF category validation
# ---------------------------------------------------------------------------
class TestValidation:
    def test_invalid_category_rejected(self, aar_client):
        bad_payload = {**SAMPLE_AAR}
        bad_payload["improves"] = [{
            "problem": "Test",
            "priority": "H",
            "category": "INVALID_CATEGORY",
        }]
        resp = aar_client.post("/aars", json=bad_payload)
        assert resp.status_code == 422
