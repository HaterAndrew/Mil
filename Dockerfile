# ============================================================
# Dockerfile — MSS Training Analytics Portal (Streamlit)
# Multi-stage build: builder → runtime
# ============================================================

# ---------------------------------------------------------------------------
# Stage 1: builder — install dependencies in a venv
# ---------------------------------------------------------------------------
FROM python:3.11-slim AS builder

WORKDIR /build

COPY requirements.txt .
RUN python -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip \
    && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# ---------------------------------------------------------------------------
# Stage 2: runtime — minimal final image
# ---------------------------------------------------------------------------
FROM python:3.11-slim AS runtime

RUN groupadd -r appuser && useradd -r -g appuser -m appuser

WORKDIR /app

# Copy venv from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy application source
COPY --chown=appuser:appuser apps/ ./apps/
COPY --chown=appuser:appuser maven_training/ ./maven_training/
COPY --chown=appuser:appuser scripts/ ./scripts/

# Create data directory for SQLite DBs (writable by appuser)
RUN mkdir -p /data && chown appuser:appuser /data

USER appuser

ENV STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_ADDRESS=0.0.0.0 \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

EXPOSE 8501

HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8501/_stcore/health')"

CMD ["streamlit", "run", "apps/portal.py"]
