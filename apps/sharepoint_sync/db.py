"""SharePoint Sync — database models and session management."""

from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    create_engine,
    event,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    relationship,
    sessionmaker,
)

# ---------------------------------------------------------------------------
# Database
# ---------------------------------------------------------------------------
DB_PATH = Path(__file__).parent / "sharepoint_sync.db"
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
# ORM models
# ---------------------------------------------------------------------------
class SyncRecord(Base):
    """Tracks each sync event — when content was packaged/deployed."""

    __tablename__ = "sync_records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, nullable=False, default=lambda: datetime.now(UTC))
    total_files = Column(Integer, nullable=False, default=0)
    added = Column(Integer, nullable=False, default=0)
    modified = Column(Integer, nullable=False, default=0)
    deleted = Column(Integer, nullable=False, default=0)
    notes = Column(Text, nullable=True)

    file_states = relationship(
        "FileState", back_populates="sync_record", cascade="all, delete-orphan"
    )


class FileState(Base):
    """Per-file hash snapshot tied to a sync record."""

    __tablename__ = "file_states"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sync_id = Column(Integer, ForeignKey("sync_records.id"), nullable=False)
    file_path = Column(String(500), nullable=False)
    file_hash = Column(String(64), nullable=False)
    status = Column(String(20), nullable=False)  # ADDED, MODIFIED, DELETED, UNCHANGED

    sync_record = relationship("SyncRecord", back_populates="file_states")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def get_db():
    """Yield a database session; closes on exit."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Create all tables if they don't exist."""
    Base.metadata.create_all(bind=engine)
