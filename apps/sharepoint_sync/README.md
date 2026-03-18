# SharePoint Sync Dashboard

Tracks sync state between local `maven_training/` content and deployed
environments (Cloudflare Pages + SharePoint).  Generates deployment
packages and maintains a history of what was synced and when.

## Quick Start

```bash
# From repo root
# 1. Seed initial baseline
python -m apps.sharepoint_sync.seed

# 2. Launch dashboard
streamlit run apps/sharepoint_sync/dashboard.py --server.port 8509
```

## Features

| View | Description |
|---|---|
| **Sync Status** | Current diff vs last baseline — files added/modified/deleted |
| **File Diff Browser** | Expandable directory tree with status badges and filters |
| **SharePoint Variants** | Side-by-side check of `_sharepoint` files vs standard versions |
| **Generate Package** | Build ZIP of changes-only or full content for deployment |
| **Record Sync** | Mark current state as the new baseline after deploying |
| **Sync History** | Table of all past sync events with stats |

## Architecture

- **`sync_engine.py`** — SHA-256 hashing, diff computation, ZIP generation
- **`db.py`** — SQLAlchemy models (`sync_records`, `file_states`)
- **`dashboard.py`** — Streamlit UI (port 8509, dashboard-only)
- **`seed.py`** — Initial baseline seeder

## Dual-Deployment Workflow

1. Make changes to `maven_training/` content
2. Open dashboard — review what changed in **Sync Status**
3. Check **SharePoint Variants** for stale `_sharepoint` files
4. Use **Generate Package** to build a deployment ZIP
5. Deploy to Cloudflare Pages (git push) and SharePoint (upload ZIP)
6. **Record Sync** to mark the new baseline

## Database

SQLite at `apps/sharepoint_sync/sharepoint_sync.db` (auto-created).
Two tables: `sync_records` (event log) and `file_states` (per-file hashes).
