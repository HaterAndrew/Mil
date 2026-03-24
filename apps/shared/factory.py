"""Shared FastAPI app factory for Maven Training micro-apps.

Centralizes boilerplate: security headers, CORS, and common config
so individual apps don't copy-paste the same setup.
"""

from __future__ import annotations

import os
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from shared.middleware import SecurityHeadersMiddleware

# Default CORS origins for local development
_DEFAULT_ORIGINS = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8501",
    "http://127.0.0.1",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8501",
]


def create_app(
    title: str,
    version: str = "1.0.0",
    lifespan: Any = None,
    description: str = "",
) -> FastAPI:
    """Create a configured FastAPI instance with standard middleware.

    Args:
        title: Application title shown in OpenAPI docs.
        version: Semantic version string.
        lifespan: Async context manager for startup/shutdown lifecycle.
        description: Optional description for OpenAPI docs.

    Returns:
        A FastAPI app with SecurityHeaders and CORS middleware applied.
    """
    # Disable interactive API docs in production
    enable_docs = os.environ.get("AUTH_DISABLED", "").lower() == "true"

    app = FastAPI(
        title=title,
        description=description,
        version=version,
        lifespan=lifespan,
        docs_url="/docs" if enable_docs else None,
        redoc_url="/redoc" if enable_docs else None,
        openapi_url="/openapi.json" if enable_docs else None,
    )

    # Security headers (X-Content-Type-Options, X-Frame-Options, etc.)
    app.add_middleware(SecurityHeadersMiddleware)

    # CORS — configurable via CORS_ORIGINS env var (comma-separated)
    origins_env = os.environ.get("CORS_ORIGINS")
    if origins_env:
        origins = [o.strip() for o in origins_env.split(",") if o.strip()]
    else:
        origins = _DEFAULT_ORIGINS

    # Reject wildcard origins when credentials are enabled
    if "*" in origins:
        origins = _DEFAULT_ORIGINS

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
        allow_headers=["Content-Type", "X-API-Key", "Authorization"],
    )

    return app
