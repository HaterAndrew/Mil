"""Shared API key authentication for Maven Training micro-apps.

Uses X-API-Key header checked against the API_KEY environment variable.
When API_KEY is not set, auth is disabled with a warning (dev mode).
Set API_KEY in production to enforce authentication.
The /health endpoint is always exempt from authentication.
"""

from __future__ import annotations

import hmac
import logging
import os

from fastapi import HTTPException, Request, status

logger = logging.getLogger(__name__)

_API_KEY: str | None = os.environ.get("API_KEY")

if not _API_KEY:
    logger.warning(
        "API_KEY not set — authentication disabled. "
        "Set API_KEY environment variable to enforce auth in production."
    )


async def verify_api_key(request: Request) -> None:
    """FastAPI dependency that enforces X-API-Key header authentication.

    Usage::

        @app.post("/things", dependencies=[Depends(verify_api_key)])
        def create_thing(...): ...

    Skips auth when:
    - AUTH_DISABLED=true (explicit dev mode)
    - Request path is /health
    """
    # Auth disabled when no API_KEY configured
    if not _API_KEY:
        return

    # Exempt health checks
    if request.url.path.rstrip("/") == "/health":
        return

    provided = request.headers.get("X-API-Key", "")
    if not provided or not hmac.compare_digest(provided, _API_KEY):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )
