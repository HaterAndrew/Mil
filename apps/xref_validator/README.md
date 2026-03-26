# Cross-Reference Validator

Scans the `maven_training/` documentation corpus and validates all cross-references, internal links, chapter references, and prereq chain consistency. Surfaces broken links, stale references, and inconsistencies.

## Validators

| Validator | What it checks |
|---|---|
| **Markdown Links** | Every `[text](target)` link — verifies the target file exists on disk |
| **Chapter Refs** | `Chapter N` / `Ch N` references — confirms a matching heading exists in the document |
| **TM Refs** | All `TM-XX` references — validates against the known course catalog (flags TM-50A–F, old TM-40A=ORSA) |
| **Prereq Consistency** | Prereq statements in docs — checks alignment with the authoritative prereq chain |

## Authoritative Prereq Chain

```
SL 1 → SL 2 → SL 3 → ALL SL 4 (A–L)
                    → FBC (parallel track off SL 2)

SL 4G → SL 5G    SL 4H → SL 5H    SL 4M → SL 5M
SL 4J → SL 5J    SL 4K → SL 5K    SL 4L → SL 5L

NOTE: SL 5A through SL 5F do NOT exist.
```

## Quick Start

```bash
# From the repo root (apps/ parent)
cd apps/

# Seed the database with an initial scan
python -m xref_validator.seed

# Start the API (port 8006)
uvicorn xref_validator.api:app --port 8006 --reload

# Start the dashboard (port 8506)
streamlit run xref_validator/dashboard.py --server.port 8506
```

## API Endpoints

| Method | Path | Description |
|---|---|---|
| `POST` | `/scan` | Trigger a new validation scan |
| `GET` | `/scan/{scan_id}` | Get full scan results |
| `GET` | `/scans` | List scan history |
| `GET` | `/issues?type=BROKEN_LINK&severity=ERROR` | Filtered issues from latest scan |
| `GET` | `/health` | Health check |

## Dashboard Pages

- **Run Scan** — Execute a scan with progress feedback and results summary
- **Issues Browser** — Filter and browse issues by type, severity, and file path
- **Trend Analysis** — Chart issue counts over time from scan history
- **Prereq Audit** — Visual prereq chain diagram with pass/fail indicators
- **Scan History** — Table of past scans with drill-down to full results

## Architecture

```
xref_validator/
├── __init__.py        Empty package marker
├── models.py          Pydantic V2 request/response models
├── db.py              SQLAlchemy ORM + all scan/validation logic
├── api.py             FastAPI application (port 8006)
├── dashboard.py       Streamlit dashboard (port 8506)
├── seed.py            Initial scan seeder
└── README.md          This file
```

## Ports

| Service | Port |
|---|---|
| Dashboard (Streamlit) | 8506 |
| API (FastAPI) | 8006 |
