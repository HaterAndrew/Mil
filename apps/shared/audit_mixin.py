"""Audit trail mixin for SQLAlchemy models."""
from datetime import UTC, datetime

from sqlalchemy import Column, DateTime, String


class AuditMixin:
    """Adds created_at, updated_at, created_by, updated_by to any model."""
    created_at = Column(DateTime, default=lambda: datetime.now(UTC), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(UTC),
                        onupdate=lambda: datetime.now(UTC), nullable=True)
    created_by = Column(String, default="system", nullable=False)
    updated_by = Column(String, nullable=True)
