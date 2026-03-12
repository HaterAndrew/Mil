# EX-40J TRAINING — Pipeline Definition
## LOGSTAT Aggregation Pipeline — Technical Description
**Classification:** UNCLASSIFIED // TRAINING USE ONLY

## What It Does

Ingests daily logistics status (LOGSTAT) data from three battalion-level source systems, normalizes to a common schema, and loads it into the theater LOGSTAT dataset on MSS for G4 dashboard consumption.

## Tech Stack

| Component | Technology |
|-----------|------------|
| Platform | MSS (Maven Smart System) Python Transforms |
| Ingestion | REST API calls to BSB, FSB, CSSB logistics systems |
| Transform | Python (pandas) — normalization, null handling, deduplication |
| Load | Foundry Output dataset (overwrite daily) |
| Visualization | Workshop dashboard (G4 Viewer access) |

## Source Systems

| System | Owner | API Type | Auth | Rate Limit |
|--------|-------|----------|------|------------|
| BSB Logistics API | BSB S4 | REST/JSON | API Key | 10,000 req/hr |
| FSB Logistics API | FSB S4 | REST/JSON | API Key | **100 req/hr ← BLOCKER** |
| CSSB Logistics API | CSSB S4 | REST/JSON | API Key | **100 req/hr ← BLOCKER** |

## Output Schema

| Field | Type | Description |
|-------|------|-------------|
| `report_date` | DATE | Date of LOGSTAT report |
| `battalion` | STRING | Unit identifier |
| `equipment_class` | STRING | Normalized equipment category |
| `equipment_total` | INT | Total equipment in class |
| `equipment_available` | INT | Available (not NMC) |
| `availability_pct` | FLOAT | available / total × 100 |
| `source_system` | STRING | Which API provided this record |
| `ingested_at` | TIMESTAMP | Pipeline run timestamp |

## Run Schedule

| Parameter | Value |
|-----------|-------|
| Trigger | Daily at 0400 local (to produce dashboard ready by 0600) |
| Scheduler | MSS scheduler |
| Retry | 2 attempts on failure, then alert to data team |

## Known Issues

See open tickets: #EX40J-004, #EX40J-007 (critical), #EX40J-011, #EX40J-015
