"""Offline Package Builder — database models and session management.

Tracks package build history for audit and re-download purposes.
"""

from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
    Text,
    create_engine,
    event,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    sessionmaker,
)
from sqlalchemy.types import JSON

# ---------------------------------------------------------------------------
# Database path — sits next to this file; *.db is gitignored
# ---------------------------------------------------------------------------
DB_PATH = Path(__file__).parent / "offline_packager.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


@event.listens_for(engine, "connect")
def _set_sqlite_pragmas(dbapi_conn, _connection_record):
    cursor = dbapi_conn.cursor()
    cursor.execute("PRAGMA journal_mode=WAL")
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


class Base(DeclarativeBase):
    pass


# ---------------------------------------------------------------------------
# ORM model
# ---------------------------------------------------------------------------
class PackageRecord(Base):
    """Tracks each offline package build."""

    __tablename__ = "package_records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False, default=lambda: datetime.now(UTC))
    selected_tms = Column(JSON, nullable=False)  # ["SL 1", "SL 2", ...]
    all_tms = Column(JSON, nullable=False)        # includes auto-resolved prereqs
    total_items = Column(Integer, nullable=False, default=0)
    size_kb = Column(Integer, nullable=False, default=0)
    include_pdfs = Column(Boolean, nullable=False, default=True)
    notes = Column(Text, nullable=True)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def get_db():
    """Yield a DB session; auto-close on exit."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Create tables if they don't exist."""
    Base.metadata.create_all(bind=engine)
