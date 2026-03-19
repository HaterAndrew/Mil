"""
Shared pytest fixtures for sitrep_tracker tests.
Uses an in-memory SQLite DB so tests are isolated and leave no files on disk.
"""
import os
import sys
import pytest

# Allow imports from sitrep_tracker/ and apps/ without installing packages
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "sitrep_tracker"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "apps"))


@pytest.fixture(autouse=True)
def in_memory_db(monkeypatch, tmp_path):
    """Point DB_PATH to a temp file for every test; init the schema fresh."""
    import db as db_module
    from pathlib import Path

    test_db = tmp_path / "test_sitrep.db"
    monkeypatch.setattr(db_module, "DB_PATH", test_db)
    db_module.init_db()
    yield test_db
