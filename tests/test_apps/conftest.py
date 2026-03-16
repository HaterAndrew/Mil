"""Shared test fixtures for the apps test suite."""

from __future__ import annotations

import pytest
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

# ---------------------------------------------------------------------------
# Readiness Tracker fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def readiness_db(tmp_path):
    """Create a temp SQLite DB for readiness tracker tests."""
    from apps.readiness_tracker import db as rt_db

    db_path = tmp_path / "test_readiness.db"
    url = f"sqlite:///{db_path}"
    test_engine = create_engine(url, connect_args={"check_same_thread": False})

    @event.listens_for(test_engine, "connect")
    def _pragmas(dbapi_conn, _rec):
        cur = dbapi_conn.cursor()
        cur.execute("PRAGMA journal_mode=WAL")
        cur.execute("PRAGMA foreign_keys=ON")
        cur.close()

    test_session = sessionmaker(bind=test_engine, autocommit=False, autoflush=False)

    # Patch the module's engine and session
    original_engine = rt_db.engine
    original_session = rt_db.SessionLocal

    rt_db.engine = test_engine
    rt_db.SessionLocal = test_session

    rt_db.Base.metadata.create_all(bind=test_engine)
    rt_db.init_db()

    yield test_session

    rt_db.engine = original_engine
    rt_db.SessionLocal = original_session


@pytest.fixture
def readiness_client(readiness_db):
    """TestClient for readiness tracker API using temp DB."""
    from fastapi.testclient import TestClient
    from apps.readiness_tracker.api import app
    from apps.readiness_tracker import db as rt_db

    def override_get_db():
        db = readiness_db()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[rt_db.get_db] = override_get_db
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


# ---------------------------------------------------------------------------
# Exam Analytics fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def exam_db(tmp_path):
    """Create a temp SQLite DB for exam analytics tests."""
    from apps.exam_analytics import db as ea_db

    db_path = tmp_path / "test_exam.db"
    url = f"sqlite:///{db_path}"
    test_engine = create_engine(url, connect_args={"check_same_thread": False})

    @event.listens_for(test_engine, "connect")
    def _pragmas(dbapi_conn, _rec):
        cur = dbapi_conn.cursor()
        cur.execute("PRAGMA journal_mode=WAL")
        cur.execute("PRAGMA foreign_keys=ON")
        cur.close()

    test_session = sessionmaker(bind=test_engine, autocommit=False, autoflush=False)

    original_engine = ea_db.engine
    original_session = ea_db.SessionLocal

    ea_db.engine = test_engine
    ea_db.SessionLocal = test_session

    ea_db.Base.metadata.create_all(bind=test_engine)

    yield test_session

    ea_db.engine = original_engine
    ea_db.SessionLocal = original_session


@pytest.fixture
def exam_client(exam_db):
    """TestClient for exam analytics API using temp DB."""
    from fastapi.testclient import TestClient
    from apps.exam_analytics.api import app
    from apps.exam_analytics import db as ea_db

    def override_get_db():
        db = exam_db()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[ea_db.get_db] = override_get_db
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


# ---------------------------------------------------------------------------
# AAR Aggregator fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def aar_db(tmp_path):
    """Create a temp SQLite DB for AAR aggregator tests."""
    from apps.aar_aggregator import db as aar_mod

    db_path = tmp_path / "test_aar.db"
    url = f"sqlite:///{db_path}"
    test_engine = create_engine(url, connect_args={"check_same_thread": False})

    @event.listens_for(test_engine, "connect")
    def _pragmas(dbapi_conn, _rec):
        cur = dbapi_conn.cursor()
        cur.execute("PRAGMA journal_mode=WAL")
        cur.execute("PRAGMA foreign_keys=ON")
        cur.close()

    test_session = sessionmaker(bind=test_engine, autocommit=False, autoflush=False)

    original_engine = aar_mod.engine
    original_session = aar_mod.SessionLocal

    aar_mod.engine = test_engine
    aar_mod.SessionLocal = test_session

    aar_mod.Base.metadata.create_all(bind=test_engine)

    yield test_session

    aar_mod.engine = original_engine
    aar_mod.SessionLocal = original_session


@pytest.fixture
def aar_client(aar_db):
    """TestClient for AAR aggregator API using temp DB."""
    from fastapi.testclient import TestClient
    from apps.aar_aggregator.api import app
    from apps.aar_aggregator import db as aar_mod

    def override_get_db():
        db = aar_db()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[aar_mod.get_db] = override_get_db
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()
