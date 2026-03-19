"""Tests for the Lessons Learned Pipeline."""

from __future__ import annotations


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def create_lesson(client, **overrides):
    payload = {
        "title": "Improve MSS data export workflow",
        "description": "Soldiers found the CSV export confusing during FTX. Recommend adding column headers.",
        "source_type": "FIELD_OBSERVATION",
        "source_reference": "FTX-2026-003",
        "submitted_by": "SFC JONES",
        "submit_date": "2026-03-01",
        "priority": "MEDIUM",
        **overrides,
    }
    resp = client.post("/lessons", json=payload)
    assert resp.status_code == 201
    return resp.json()


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------
class TestHealth:
    def test_health(self, lessons_client):
        resp = lessons_client.get("/health")
        assert resp.status_code == 200
        assert resp.json()["status"] == "ok"


# ---------------------------------------------------------------------------
# Lessons CRUD
# ---------------------------------------------------------------------------
class TestLessons:
    def test_create_lesson(self, lessons_client):
        data = create_lesson(lessons_client)
        assert data["title"] == "Improve MSS data export workflow"
        assert data["status"] == "NEW"

    def test_list_lessons(self, lessons_client):
        create_lesson(lessons_client, title="Lesson A")
        create_lesson(lessons_client, title="Lesson B")
        resp = lessons_client.get("/lessons")
        assert len(resp.json()) == 2

    def test_list_by_status(self, lessons_client):
        create_lesson(lessons_client)
        resp = lessons_client.get("/lessons", params={"status": "NEW"})
        assert len(resp.json()) == 1
        resp = lessons_client.get("/lessons", params={"status": "ARCHIVED"})
        assert len(resp.json()) == 0

    def test_list_by_priority(self, lessons_client):
        create_lesson(lessons_client, priority="HIGH")
        create_lesson(lessons_client, priority="LOW")
        resp = lessons_client.get("/lessons", params={"priority": "HIGH"})
        assert len(resp.json()) == 1

    def test_list_by_source_type(self, lessons_client):
        create_lesson(lessons_client, source_type="AAR")
        create_lesson(lessons_client, source_type="EXERCISE")
        resp = lessons_client.get("/lessons", params={"source_type": "AAR"})
        assert len(resp.json()) == 1

    def test_get_lesson_404(self, lessons_client):
        resp = lessons_client.get("/lessons/999")
        assert resp.status_code == 404


# ---------------------------------------------------------------------------
# Tags
# ---------------------------------------------------------------------------
class TestTags:
    def test_add_tag(self, lessons_client):
        lesson = create_lesson(lessons_client)
        resp = lessons_client.post(f"/lessons/{lesson['id']}/tags", json={
            "tag_type": "WFF",
            "tag_value": "Intelligence",
        })
        assert resp.status_code == 201
        assert resp.json()["tag_type"] == "WFF"

    def test_duplicate_tag_409(self, lessons_client):
        lesson = create_lesson(lessons_client)
        tag = {"tag_type": "WFF", "tag_value": "Intelligence"}
        lessons_client.post(f"/lessons/{lesson['id']}/tags", json=tag)
        resp = lessons_client.post(f"/lessons/{lesson['id']}/tags", json=tag)
        assert resp.status_code == 409

    def test_list_tags(self, lessons_client):
        lesson = create_lesson(lessons_client)
        lessons_client.post(f"/lessons/{lesson['id']}/tags", json={
            "tag_type": "WFF", "tag_value": "Intelligence",
        })
        lessons_client.post(f"/lessons/{lesson['id']}/tags", json={
            "tag_type": "ECHELON", "tag_value": "Battalion",
        })
        resp = lessons_client.get(f"/lessons/{lesson['id']}/tags")
        assert len(resp.json()) == 2

    def test_tag_on_nonexistent_lesson_404(self, lessons_client):
        resp = lessons_client.post("/lessons/999/tags", json={
            "tag_type": "WFF", "tag_value": "Fires",
        })
        assert resp.status_code == 404


# ---------------------------------------------------------------------------
# Action Items
# ---------------------------------------------------------------------------
class TestActions:
    def test_add_action(self, lessons_client):
        lesson = create_lesson(lessons_client)
        resp = lessons_client.post(f"/lessons/{lesson['id']}/actions", json={
            "description": "Update export template",
            "assigned_to": "SPC DOE",
            "due_date": "2026-04-01",
        })
        assert resp.status_code == 201
        assert resp.json()["status"] == "OPEN"

    def test_list_actions(self, lessons_client):
        lesson = create_lesson(lessons_client)
        lessons_client.post(f"/lessons/{lesson['id']}/actions", json={
            "description": "Action 1",
        })
        lessons_client.post(f"/lessons/{lesson['id']}/actions", json={
            "description": "Action 2",
        })
        resp = lessons_client.get(f"/lessons/{lesson['id']}/actions")
        assert len(resp.json()) == 2


# ---------------------------------------------------------------------------
# Comments
# ---------------------------------------------------------------------------
class TestComments:
    def test_add_comment(self, lessons_client):
        lesson = create_lesson(lessons_client)
        resp = lessons_client.post(f"/lessons/{lesson['id']}/comments", json={
            "author": "MAJ SMITH",
            "comment_text": "Good observation. Adding to next cycle.",
        })
        assert resp.status_code == 201
        assert resp.json()["author"] == "MAJ SMITH"


# ---------------------------------------------------------------------------
# Analytics
# ---------------------------------------------------------------------------
class TestAnalytics:
    def test_tag_frequency(self, lessons_client):
        lesson = create_lesson(lessons_client)
        lessons_client.post(f"/lessons/{lesson['id']}/tags", json={
            "tag_type": "WFF", "tag_value": "Intelligence",
        })
        resp = lessons_client.get("/tags/frequency", params={"tag_type": "WFF"})
        assert resp.status_code == 200
        data = resp.json()
        assert len(data) == 1
        assert data[0]["tag_value"] == "Intelligence"

    def test_trend_analysis(self, lessons_client):
        create_lesson(lessons_client)
        resp = lessons_client.get("/analysis/trend")
        assert resp.status_code == 200

    def test_cross_reference(self, lessons_client):
        lesson = create_lesson(lessons_client)
        lessons_client.post(f"/lessons/{lesson['id']}/tags", json={
            "tag_type": "WFF", "tag_value": "Intelligence",
        })
        lessons_client.post(f"/lessons/{lesson['id']}/tags", json={
            "tag_type": "ECHELON", "tag_value": "Battalion",
        })
        resp = lessons_client.get("/analysis/cross-reference", params={
            "type_a": "WFF", "type_b": "ECHELON",
        })
        assert resp.status_code == 200
        data = resp.json()
        assert len(data) == 1
        assert data[0]["tag_a"] == "Intelligence"
        assert data[0]["tag_b"] == "Battalion"


# ---------------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------------
class TestStats:
    def test_pipeline_stats(self, lessons_client):
        create_lesson(lessons_client)
        resp = lessons_client.get("/stats")
        assert resp.status_code == 200
        data = resp.json()
        assert data["total_lessons"] == 1
        assert data["by_status"]["NEW"] == 1


# ---------------------------------------------------------------------------
# Export
# ---------------------------------------------------------------------------
class TestExport:
    def test_csv_export(self, lessons_client):
        create_lesson(lessons_client)
        resp = lessons_client.get("/export/csv")
        assert resp.status_code == 200
        assert "text/csv" in resp.headers["content-type"]
        assert "Improve MSS" in resp.text
