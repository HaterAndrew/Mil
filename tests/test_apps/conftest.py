"""Shared test fixtures for the apps test suite."""

from __future__ import annotations

import pytest
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker


# ---------------------------------------------------------------------------
# Fixture factory — eliminates boilerplate for adding new app test fixtures.
#
# IMPORTANT: Import paths must use the short form (e.g. 'mtt_scheduler.db')
# matching how app code imports sibling packages, NOT the long form
# (e.g. 'apps.mtt_scheduler.db'). The root conftest adds apps/ to sys.path,
# so both resolve to the same file — but Python treats them as distinct
# modules, causing duplicate class registration on shared SQLAlchemy Bases.
# ---------------------------------------------------------------------------
def _make_db_fixture(db_module_import_path: str, has_init_db: bool = False):
    """Return a pytest fixture that creates a temp SQLite DB for an app module."""
    @pytest.fixture
    def _db(tmp_path):
        import importlib
        db_mod = importlib.import_module(db_module_import_path)

        db_path = tmp_path / "test.db"
        url = f"sqlite:///{db_path}"
        test_engine = create_engine(url, connect_args={"check_same_thread": False})

        @event.listens_for(test_engine, "connect")
        def _pragmas(dbapi_conn, _rec):
            cur = dbapi_conn.cursor()
            cur.execute("PRAGMA journal_mode=WAL")
            cur.execute("PRAGMA foreign_keys=ON")
            cur.close()

        test_session = sessionmaker(bind=test_engine, autocommit=False, autoflush=False)

        original_engine = db_mod.engine
        original_session = db_mod.SessionLocal

        db_mod.engine = test_engine
        db_mod.SessionLocal = test_session

        db_mod.Base.metadata.create_all(bind=test_engine)
        if has_init_db:
            db_mod.init_db()

        yield test_session

        db_mod.engine = original_engine
        db_mod.SessionLocal = original_session

    return _db


def _make_client_fixture(db_fixture_name: str, api_import_path: str, db_module_import_path: str):
    """Return a pytest fixture that creates a TestClient for an app's FastAPI."""
    @pytest.fixture
    def _client(request):
        import importlib
        from fastapi.testclient import TestClient

        db_session_factory = request.getfixturevalue(db_fixture_name)
        api_mod = importlib.import_module(api_import_path)
        db_mod = importlib.import_module(db_module_import_path)

        def override_get_db():
            db = db_session_factory()
            try:
                yield db
            finally:
                db.close()

        api_mod.app.dependency_overrides[db_mod.get_db] = override_get_db
        client = TestClient(api_mod.app)
        yield client
        api_mod.app.dependency_overrides.clear()

    return _client

# ---------------------------------------------------------------------------
# Readiness Tracker fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def readiness_db(tmp_path):
    """Create a temp SQLite DB for readiness tracker tests."""
    from readiness_tracker import db as rt_db

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
    from readiness_tracker.api import app
    from readiness_tracker import db as rt_db

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
    from exam_analytics import db as ea_db

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
    from exam_analytics.api import app
    from exam_analytics import db as ea_db

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
    from aar_aggregator import db as aar_mod

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
    from aar_aggregator.api import app
    from aar_aggregator import db as aar_mod

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


# ---------------------------------------------------------------------------
# MTT Scheduler fixtures
# ---------------------------------------------------------------------------
mtt_db = _make_db_fixture("mtt_scheduler.db")
mtt_client = _make_client_fixture("mtt_db", "mtt_scheduler.api", "mtt_scheduler.db")


# ---------------------------------------------------------------------------
# Enrollment Manager fixtures
# ---------------------------------------------------------------------------
enrollment_db = _make_db_fixture("enrollment_manager.db")
enrollment_client = _make_client_fixture(
    "enrollment_db", "enrollment_manager.api", "enrollment_manager.db"
)


# ---------------------------------------------------------------------------
# Instructor Manager fixtures
# ---------------------------------------------------------------------------
instructor_db = _make_db_fixture("instructor_manager.db")
instructor_client = _make_client_fixture(
    "instructor_db", "instructor_manager.api", "instructor_manager.db"
)


# ---------------------------------------------------------------------------
# Lessons Learned fixtures
# ---------------------------------------------------------------------------
lessons_db = _make_db_fixture("lessons_learned.db")
lessons_client = _make_client_fixture(
    "lessons_db", "lessons_learned.api", "lessons_learned.db"
)


# ---------------------------------------------------------------------------
# Training Metrics fixtures
# ---------------------------------------------------------------------------
metrics_db = _make_db_fixture("training_metrics.db")
metrics_client = _make_client_fixture(
    "metrics_db", "training_metrics.api", "training_metrics.db"
)


# ---------------------------------------------------------------------------
# Glossary Search fixtures — non-standard: lazy engine singleton
# ---------------------------------------------------------------------------
@pytest.fixture
def glossary_db(tmp_path):
    """Create a temp SQLite DB for glossary search tests."""
    from glossary_search import db as gs_db

    db_path = tmp_path / "test_glossary.db"
    url = f"sqlite:///{db_path}"
    test_engine = create_engine(url, connect_args={"check_same_thread": False})
    test_session_factory = sessionmaker(bind=test_engine, autocommit=False, autoflush=False)

    original_engine = gs_db._engine
    original_session = gs_db._SessionLocal

    gs_db._engine = test_engine
    gs_db._SessionLocal = test_session_factory

    gs_db.Base.metadata.create_all(bind=test_engine)

    yield test_session_factory

    gs_db._engine = original_engine
    gs_db._SessionLocal = original_session


@pytest.fixture
def glossary_client(glossary_db):
    """TestClient for glossary search API using temp DB."""
    from fastapi.testclient import TestClient
    from glossary_search.api import app

    client = TestClient(app)
    yield client


# ---------------------------------------------------------------------------
# Curriculum Tracker fixtures
# ---------------------------------------------------------------------------
curriculum_db = _make_db_fixture("curriculum_tracker.db")
curriculum_client = _make_client_fixture(
    "curriculum_db", "curriculum_tracker.api", "curriculum_tracker.db"
)


# ---------------------------------------------------------------------------
# Data Quality fixtures — non-standard: contextmanager get_db, _engine/_SessionLocal
# ---------------------------------------------------------------------------
@pytest.fixture
def dq_db(tmp_path):
    """Create a temp SQLite DB for data quality tests."""
    from data_quality import db as dq_mod

    db_path = tmp_path / "test_dq.db"
    url = f"sqlite:///{db_path}"
    test_engine = create_engine(url, connect_args={"check_same_thread": False})

    @event.listens_for(test_engine, "connect")
    def _pragmas(dbapi_conn, _rec):
        cur = dbapi_conn.cursor()
        cur.execute("PRAGMA journal_mode=WAL")
        cur.execute("PRAGMA foreign_keys=ON")
        cur.close()

    test_session_factory = sessionmaker(
        bind=test_engine, autocommit=False, autoflush=False, expire_on_commit=False,
    )

    original_engine = dq_mod._engine
    original_session = dq_mod._SessionLocal

    dq_mod._engine = test_engine
    dq_mod._SessionLocal = test_session_factory

    dq_mod.Base.metadata.create_all(bind=test_engine)

    yield test_session_factory

    dq_mod._engine = original_engine
    dq_mod._SessionLocal = original_session


@pytest.fixture
def dq_client(dq_db):
    """TestClient for data quality API using temp DB."""
    from fastapi.testclient import TestClient
    from data_quality.api import app

    client = TestClient(app)
    yield client


# ---------------------------------------------------------------------------
# Offline Packager fixtures
# ---------------------------------------------------------------------------
packager_db = _make_db_fixture("offline_packager.db")
packager_client = _make_client_fixture(
    "packager_db", "offline_packager.api", "offline_packager.db"
)


# ---------------------------------------------------------------------------
# SharePoint Sync fixtures
# ---------------------------------------------------------------------------
sync_db = _make_db_fixture("sharepoint_sync.db")
sync_client = _make_client_fixture(
    "sync_db", "sharepoint_sync.api", "sharepoint_sync.db"
)


# ---------------------------------------------------------------------------
# XRef Validator fixtures
# ---------------------------------------------------------------------------
xref_db = _make_db_fixture("xref_validator.db")
xref_client = _make_client_fixture(
    "xref_db", "xref_validator.api", "xref_validator.db"
)


# ---------------------------------------------------------------------------
# Progress Tracker fixtures
# ---------------------------------------------------------------------------
progress_db = _make_db_fixture("progress_tracker.db")
progress_client = _make_client_fixture(
    "progress_db", "progress_tracker.api", "progress_tracker.db"
)
