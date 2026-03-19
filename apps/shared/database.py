"""Shared database utilities for all Maven Training micro-apps."""
import logging
from pathlib import Path
from sqlalchemy import create_engine, event
from sqlalchemy.orm import DeclarativeBase, sessionmaker

logger = logging.getLogger(__name__)

class Base(DeclarativeBase):
    pass

def create_app_engine(app_name: str, db_dir: Path | None = None):
    """Create a SQLite engine for the named app with WAL mode and FK enforcement."""
    if db_dir is None:
        db_dir = Path(__file__).resolve().parent.parent / app_name
    db_path = db_dir / f"{app_name}.db"
    engine = create_engine(
        f"sqlite:///{db_path}",
        connect_args={"check_same_thread": False},
    )

    @event.listens_for(engine, "connect")
    def _set_sqlite_pragma(dbapi_conn, connection_record):
        cursor = dbapi_conn.cursor()
        cursor.execute("PRAGMA journal_mode=WAL")
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

    return engine

def create_session_factory(engine):
    """Create a SessionLocal factory bound to the given engine."""
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db(SessionLocal):
    """Dependency generator for FastAPI endpoints."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
