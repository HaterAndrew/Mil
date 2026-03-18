# Data Quality Monitor

Pipeline health monitoring, quality metrics tracking, and anomaly alerting for the USAREUR-AF operational data team.

## Quick Start

```bash
# From repo root

# 1. Seed demo data
python -m apps.data_quality.seed

# 2. Start API (port 8010)
uvicorn apps.data_quality.api:app --host 0.0.0.0 --port 8010

# 3. Start dashboard (port 8510)
streamlit run apps/data_quality/dashboard.py --server.port 8510
```

## Architecture

| File | Purpose |
|------|---------|
| `models.py` | Pydantic V2 schemas (Pipeline, Metric, Alert, Health) |
| `db.py` | SQLAlchemy ORM, tables, metric evaluation, query helpers |
| `api.py` | FastAPI REST endpoints (CRUD, metrics, health, alerts) |
| `dashboard.py` | Streamlit UI with 6 views |
| `seed.py` | Deterministic demo data (6 pipelines, 90 days history, 15 alerts) |

## Dashboard Views

- **Pipeline Overview** — grid of pipeline cards with RAG status and sparklines
- **Pipeline Detail** — per-pipeline metric trends, alerts, metadata
- **Alert Center** — active alerts with severity badges, acknowledge workflow
- **Metric Trends** — multi-pipeline comparison charts by metric type
- **Quality Scorecard** — summary table, cells colored by PASS/WARN/FAIL
- **Pipeline Manager** — register and view pipeline configurations

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `/pipelines` | Register pipeline |
| GET | `/pipelines` | List all pipelines |
| GET | `/pipelines/{id}` | Get single pipeline |
| PUT | `/pipelines/{id}` | Update pipeline |
| DELETE | `/pipelines/{id}` | Remove pipeline |
| POST | `/metrics` | Record metric observation |
| GET | `/metrics/{pipeline_id}` | Metric history (filter by type, days) |
| GET | `/health` | All pipelines health summary |
| GET | `/health/{pipeline_id}` | Single pipeline health |
| GET | `/alerts` | Active alerts (filter by severity, pipeline) |
| POST | `/alerts/{id}/ack` | Acknowledge alert |
| GET | `/dashboard-stats` | Aggregate KPIs |

## Metric Evaluation Rules

| Type | PASS | WARN | FAIL |
|------|------|------|------|
| COMPLETENESS | >= threshold | >= threshold * 0.9 | below |
| TIMELINESS | <= threshold | <= threshold * 1.2 | above |
| FRESHNESS | <= threshold (hrs) | — | above |
| VOLUME | 0.8x–1.5x threshold | outside band | < 0.5x threshold |
| ACCURACY | >= threshold | — | below |

## Demo Pipelines

1. **MSS Roster Sync** — IPPS-A to Foundry (healthy)
2. **Training Completion ETL** — DTMS to Foundry (healthy)
3. **SITREP Aggregation** — CPOF to Foundry (degraded)
4. **Personnel Data Feed** — eMILPO to Foundry (healthy)
5. **Equipment Readiness Pipeline** — GCSS-Army to Foundry (degraded)
6. **Intelligence Fusion Feed** — DCGS-A to Foundry (failed)
