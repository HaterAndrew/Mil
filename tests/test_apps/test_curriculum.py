"""Tests for the Curriculum Tracker."""

from __future__ import annotations

from datetime import date, datetime, timezone

from curriculum_tracker.db import Document, ReviewCycle, ChangeLog


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def seed_documents(curriculum_db):
    """Insert documents directly into the test DB."""
    session = curriculum_db()
    docs = [
        Document(
            file_path="tm/TM_10/overview.md",
            doc_type="TM",
            course_id="SL 1",
            title="SL 1 Overview",
            current_version="1.0",
            last_modified=datetime(2026, 1, 15, tzinfo=timezone.utc),
            file_hash="abc123",
        ),
        Document(
            file_path="tm/TM_20/overview.md",
            doc_type="TM",
            course_id="SL 2",
            title="SL 2 Overview",
            current_version="1.1",
            last_modified=datetime(2026, 2, 1, tzinfo=timezone.utc),
            file_hash="def456",
        ),
        Document(
            file_path="syllabi/TM_30_syllabus.md",
            doc_type="SYLLABUS",
            course_id="SL 3",
            title="SL 3 Syllabus",
            current_version="2.0",
            last_modified=datetime(2025, 6, 1, tzinfo=timezone.utc),
            file_hash="ghi789",
        ),
    ]
    session.add_all(docs)
    session.commit()
    session.close()


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------
class TestHealth:
    def test_health(self, curriculum_client):
        resp = curriculum_client.get("/health")
        assert resp.status_code == 200
        assert resp.json()["status"] == "ok"


# ---------------------------------------------------------------------------
# Documents
# ---------------------------------------------------------------------------
class TestDocuments:
    def test_list_documents(self, curriculum_client, curriculum_db):
        seed_documents(curriculum_db)
        resp = curriculum_client.get("/documents")
        assert resp.status_code == 200
        assert len(resp.json()) == 3

    def test_list_by_doc_type(self, curriculum_client, curriculum_db):
        seed_documents(curriculum_db)
        resp = curriculum_client.get("/documents", params={"doc_type": "TM"})
        assert len(resp.json()) == 2
        resp = curriculum_client.get("/documents", params={"doc_type": "SYLLABUS"})
        assert len(resp.json()) == 1

    def test_list_by_course_id(self, curriculum_client, curriculum_db):
        seed_documents(curriculum_db)
        resp = curriculum_client.get("/documents", params={"course_id": "SL 1"})
        assert len(resp.json()) == 1
        assert resp.json()[0]["course_id"] == "SL 1"

    def test_get_document(self, curriculum_client, curriculum_db):
        seed_documents(curriculum_db)
        docs = curriculum_client.get("/documents").json()
        doc_id = docs[0]["doc_id"]
        resp = curriculum_client.get(f"/documents/{doc_id}")
        assert resp.status_code == 200
        assert resp.json()["doc_id"] == doc_id

    def test_get_document_404(self, curriculum_client, curriculum_db):
        resp = curriculum_client.get("/documents/9999")
        assert resp.status_code == 404

    def test_stale_documents(self, curriculum_client, curriculum_db):
        seed_documents(curriculum_db)
        # SL 3 syllabus was modified 2025-06-01, should be stale at 90-day threshold
        resp = curriculum_client.get("/documents/stale", params={"days": 90})
        assert resp.status_code == 200
        paths = [d["file_path"] for d in resp.json()]
        assert "syllabi/TM_30_syllabus.md" in paths


# ---------------------------------------------------------------------------
# Reviews
# ---------------------------------------------------------------------------
class TestReviews:
    def test_create_review(self, curriculum_client, curriculum_db):
        seed_documents(curriculum_db)
        docs = curriculum_client.get("/documents").json()
        doc_id = docs[0]["doc_id"]
        resp = curriculum_client.post("/reviews", json={
            "doc_id": doc_id,
            "review_type": "SCHEDULED",
            "reviewer_name": "MAJ SMITH",
            "review_date": "2026-03-15",
            "status": "APPROVED",
            "notes": "Looks good",
        })
        assert resp.status_code == 201
        assert resp.json()["status"] == "APPROVED"

    def test_duplicate_review(self, curriculum_client, curriculum_db):
        seed_documents(curriculum_db)
        docs = curriculum_client.get("/documents").json()
        doc_id = docs[0]["doc_id"]
        payload = {
            "doc_id": doc_id,
            "review_type": "SCHEDULED",
            "reviewer_name": "MAJ SMITH",
            "review_date": "2026-03-15",
            "status": "APPROVED",
        }
        curriculum_client.post("/reviews", json=payload)
        resp = curriculum_client.post("/reviews", json=payload)
        assert resp.status_code == 409

    def test_review_doc_not_found(self, curriculum_client, curriculum_db):
        resp = curriculum_client.post("/reviews", json={
            "doc_id": 9999,
            "review_type": "SCHEDULED",
            "reviewer_name": "MAJ SMITH",
            "review_date": "2026-03-15",
            "status": "APPROVED",
        })
        assert resp.status_code == 404

    def test_list_reviews(self, curriculum_client, curriculum_db):
        seed_documents(curriculum_db)
        docs = curriculum_client.get("/documents").json()
        doc_id = docs[0]["doc_id"]
        curriculum_client.post("/reviews", json={
            "doc_id": doc_id,
            "review_type": "SCHEDULED",
            "reviewer_name": "MAJ SMITH",
            "review_date": "2026-03-10",
            "status": "APPROVED",
        })
        curriculum_client.post("/reviews", json={
            "doc_id": doc_id,
            "review_type": "AD_HOC",
            "reviewer_name": "CPT JONES",
            "review_date": "2026-03-12",
            "status": "IN_REVIEW",
        })
        resp = curriculum_client.get("/reviews")
        assert resp.status_code == 200
        assert len(resp.json()) == 2

    def test_list_reviews_by_status(self, curriculum_client, curriculum_db):
        seed_documents(curriculum_db)
        docs = curriculum_client.get("/documents").json()
        doc_id = docs[0]["doc_id"]
        curriculum_client.post("/reviews", json={
            "doc_id": doc_id,
            "review_type": "SCHEDULED",
            "reviewer_name": "MAJ SMITH",
            "review_date": "2026-03-10",
            "status": "APPROVED",
        })
        resp = curriculum_client.get("/reviews", params={"status": "APPROVED"})
        assert len(resp.json()) == 1
        resp = curriculum_client.get("/reviews", params={"status": "IN_REVIEW"})
        assert len(resp.json()) == 0


# ---------------------------------------------------------------------------
# Document history
# ---------------------------------------------------------------------------
class TestHistory:
    def test_document_history(self, curriculum_client, curriculum_db):
        seed_documents(curriculum_db)
        docs = curriculum_client.get("/documents").json()
        doc_id = docs[0]["doc_id"]

        # Seed a changelog entry
        session = curriculum_db()
        session.add(ChangeLog(
            doc_id=doc_id,
            change_date=datetime(2026, 3, 1, tzinfo=timezone.utc),
            previous_hash="old_hash",
            new_hash="abc123",
            change_summary="Updated content",
            changed_by="auto-scan",
        ))
        session.commit()
        session.close()

        resp = curriculum_client.get(f"/documents/{doc_id}/history")
        assert resp.status_code == 200
        assert len(resp.json()) == 1

    def test_history_404(self, curriculum_client, curriculum_db):
        resp = curriculum_client.get("/documents/9999/history")
        assert resp.status_code == 404


# ---------------------------------------------------------------------------
# Reports
# ---------------------------------------------------------------------------
class TestReports:
    def test_summary(self, curriculum_client, curriculum_db):
        seed_documents(curriculum_db)
        docs = curriculum_client.get("/documents").json()
        curriculum_client.post("/reviews", json={
            "doc_id": docs[0]["doc_id"],
            "review_type": "SCHEDULED",
            "reviewer_name": "MAJ SMITH",
            "review_date": "2026-03-10",
            "status": "APPROVED",
        })
        resp = curriculum_client.get("/summary")
        assert resp.status_code == 200
        data = resp.json()
        assert data["approved"] == 1

    def test_freshness(self, curriculum_client, curriculum_db):
        seed_documents(curriculum_db)
        resp = curriculum_client.get("/freshness")
        assert resp.status_code == 200
        assert isinstance(resp.json(), list)


# ---------------------------------------------------------------------------
# Export
# ---------------------------------------------------------------------------
class TestExport:
    def test_csv_export(self, curriculum_client, curriculum_db):
        seed_documents(curriculum_db)
        resp = curriculum_client.get("/export/csv")
        assert resp.status_code == 200
        assert "text/csv" in resp.headers["content-type"]
        assert "SL 1" in resp.text
