"""Alembic env.py — per-app migration support.

Each app has its own SQLAlchemy Base and DB file.  Select the target app
via the APP environment variable:

    APP=mtt_scheduler alembic revision --autogenerate -m "add venue notes"
    APP=mtt_scheduler alembic upgrade head
    APP=enrollment_manager alembic check

If APP is not set, lists available apps and exits.
"""

from __future__ import annotations

import importlib
import os
import sys
from logging.config import fileConfig
from pathlib import Path

from sqlalchemy import engine_from_config, pool

from alembic import context

# ---------------------------------------------------------------------------
# Ensure apps/ directory is on sys.path
# ---------------------------------------------------------------------------
_REPO_ROOT = Path(__file__).resolve().parent.parent
_APPS_DIR = _REPO_ROOT / "apps"
for p in [str(_REPO_ROOT), str(_APPS_DIR)]:
    if p not in sys.path:
        sys.path.insert(0, p)


# ---------------------------------------------------------------------------
# App registry — maps APP env var to (db_module, db_path)
# ---------------------------------------------------------------------------
APP_REGISTRY: dict[str, str] = {
    "mtt_scheduler":      "mtt_scheduler.db",
    "enrollment_manager": "enrollment_manager.db",
    "instructor_manager": "instructor_manager.db",
    "lessons_learned":    "lessons_learned.db",
    "training_metrics":   "training_metrics.db",
    "curriculum_tracker": "curriculum_tracker.db",
    "offline_packager":   "offline_packager.db",
    "sharepoint_sync":    "sharepoint_sync.db",
    "xref_validator":     "xref_validator.db",
    "progress_tracker":   "progress_tracker.db",
    "glossary_search":    "glossary_search.db",
    "aar_aggregator":     "aar_aggregator.db",
    "data_quality":       "data_quality.db",
    "readiness_tracker":  "readiness_tracker.db",
    "exam_analytics":     "exam_analytics.db",
}


def _get_app_metadata():
    """Import the selected app's Base and return its metadata."""
    app_name = os.environ.get("APP", "")

    if not app_name:
        apps = ", ".join(sorted(APP_REGISTRY))
        raise SystemExit(
            f"ERROR: Set APP env var to select target app.\n"
            f"Available: {apps}\n"
            f"Example: APP=mtt_scheduler alembic revision --autogenerate -m 'desc'"
        )

    if app_name not in APP_REGISTRY:
        raise SystemExit(f"ERROR: Unknown app '{app_name}'. Available: {', '.join(sorted(APP_REGISTRY))}")

    mod_path = APP_REGISTRY[app_name]
    mod = importlib.import_module(mod_path)
    return mod.Base.metadata


# ---------------------------------------------------------------------------
# Alembic configuration
# ---------------------------------------------------------------------------
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = _get_app_metadata()


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        render_as_batch=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            render_as_batch=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
