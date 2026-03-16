# AAR Aggregator

Ingest After-Action Reviews, aggregate trends by WFF category, and flag recurring issues.

## Quick Start

```bash
# From repo root

# 1. Seed demo data
python -m apps.aar_aggregator.seed

# 2. Start API (port 8003)
uvicorn apps.aar_aggregator.api:app --reload --port 8003

# 3. Start dashboard (port 8503) — in a separate terminal
streamlit run apps/aar_aggregator/dashboard.py --server.port 8503
```

## API Docs

With the API running: http://localhost:8003/docs

## Input Methods

1. **Web form** — structured entry matching AAR template Sections 1–10
2. **File upload** — upload .txt/.md files; parsed and previewed before saving

## WFF Categories

Improve items are categorized by Warfighting Function:
- INTELLIGENCE
- FIRES
- MOVEMENT_MANEUVER
- SUSTAINMENT
- PROTECTION
- MISSION_COMMAND

## Recurring Issues

Problems appearing in 2+ AARs are automatically flagged. This surfaces systemic issues
that need attention beyond a single training event.
