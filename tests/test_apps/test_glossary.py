"""Tests for the Glossary Search API."""

from __future__ import annotations

from glossary_search.db import Term


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def seed_terms(glossary_db):
    """Insert a few terms directly into the test DB."""
    session = glossary_db()
    terms = [
        Term(term="OPDATA", definition="Operational Data", source_file="GLOSSARY.md",
             source_line=1, category="ACRONYM"),
        Term(term="AOR", definition="Area of Responsibility", source_file="GLOSSARY.md",
             source_line=10, category="ACRONYM"),
        Term(term="Data Pipeline", definition="A series of processing steps that move data from source to target.",
             source_file="DATA_LITERACY.md", source_line=42, category="CONCEPT"),
        Term(term="SITREP", definition="Situation Report — periodic update on current conditions.",
             source_file="GLOSSARY.md", source_line=20, category="ACRONYM"),
    ]
    session.add_all(terms)
    session.commit()
    session.close()


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------
class TestHealth:
    def test_health(self, glossary_client, glossary_db):
        resp = glossary_client.get("/health")
        assert resp.status_code == 200
        assert resp.json()["status"] == "ok"


# ---------------------------------------------------------------------------
# Search
# ---------------------------------------------------------------------------
class TestSearch:
    def test_search_by_term(self, glossary_client, glossary_db):
        seed_terms(glossary_db)
        resp = glossary_client.get("/search", params={"q": "OPDATA"})
        assert resp.status_code == 200
        data = resp.json()
        assert data["total_hits"] >= 1
        assert any(r["term"] == "OPDATA" for r in data["results"])

    def test_search_by_definition(self, glossary_client, glossary_db):
        seed_terms(glossary_db)
        resp = glossary_client.get("/search", params={"q": "processing steps"})
        data = resp.json()
        assert data["total_hits"] >= 1

    def test_search_with_category_filter(self, glossary_client, glossary_db):
        seed_terms(glossary_db)
        resp = glossary_client.get("/search", params={"q": "data", "category": "CONCEPT"})
        data = resp.json()
        # Should find "Data Pipeline" but not acronyms
        for r in data["results"]:
            assert r["category"] == "CONCEPT"

    def test_search_no_results(self, glossary_client, glossary_db):
        seed_terms(glossary_db)
        resp = glossary_client.get("/search", params={"q": "xyznonexistent"})
        assert resp.json()["total_hits"] == 0


# ---------------------------------------------------------------------------
# Terms listing
# ---------------------------------------------------------------------------
class TestTerms:
    def test_list_all(self, glossary_client, glossary_db):
        seed_terms(glossary_db)
        resp = glossary_client.get("/terms")
        assert resp.status_code == 200
        assert len(resp.json()) == 4

    def test_list_by_category(self, glossary_client, glossary_db):
        seed_terms(glossary_db)
        resp = glossary_client.get("/terms", params={"category": "ACRONYM"})
        data = resp.json()
        assert len(data) == 3
        assert all(t["category"] == "ACRONYM" for t in data)

    def test_get_term_by_id(self, glossary_client, glossary_db):
        seed_terms(glossary_db)
        # Get all terms, then fetch one by id
        all_terms = glossary_client.get("/terms").json()
        term_id = all_terms[0]["id"]
        resp = glossary_client.get(f"/terms/{term_id}")
        assert resp.status_code == 200
        assert resp.json()["id"] == term_id

    def test_get_term_404(self, glossary_client, glossary_db):
        resp = glossary_client.get("/terms/9999")
        assert resp.status_code == 404


# ---------------------------------------------------------------------------
# Categories
# ---------------------------------------------------------------------------
class TestCategories:
    def test_list_categories(self, glossary_client, glossary_db):
        seed_terms(glossary_db)
        resp = glossary_client.get("/categories")
        assert resp.status_code == 200
        data = resp.json()
        cats = {c["category"] for c in data}
        assert "ACRONYM" in cats
        assert "CONCEPT" in cats


# ---------------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------------
class TestStats:
    def test_index_stats(self, glossary_client, glossary_db):
        seed_terms(glossary_db)
        resp = glossary_client.get("/stats")
        assert resp.status_code == 200
        data = resp.json()
        assert data["total_terms"] == 4
        assert data["source_files"] == 2
