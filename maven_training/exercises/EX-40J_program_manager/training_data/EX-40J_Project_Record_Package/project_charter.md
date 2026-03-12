# EX-40J TRAINING — Project Charter
## LOGSTAT Aggregation Pipeline
**Classification:** UNCLASSIFIED // TRAINING USE ONLY

---

## Project Overview

Automate daily aggregation of logistics status (LOGSTAT) reports from three battalion-level source systems into a single theater-level dashboard on MSS. Currently, S4 staff manually compile LOGSTATs each morning — estimated 2.5 hours/day.

## Scope

| Phase | Description |
|-------|-------------|
| Ingest | 3 source APIs (BSB, FSB, CSSB logistics systems) |
| Transform | Normalize equipment class codes; compute availability percentages |
| Load | Write to theater LOGSTAT dataset on MSS |
| Visualize | Automated dashboard refresh; G4 Viewer access |

## Stakeholders

| Role | Person/Organization |
|------|---------------------|
| Sponsor | G4 (COL Harrington) |
| Product Owner | S4 OIC (CPT Delacroix) |
| Technical Lead | Data team PM (participant role) |
| End Users | G4 staff, G3 planners |
| Platform | MSS data team (API access approval required) |

## Success Criteria

1. Daily LOGSTAT dashboard available by 0600 without manual intervention
2. Data latency < 2 hours from source system update
3. UAT passed by G4 staff
4. G3-directed delivery date: D+14 (Week 8 of project)

## Out of Scope

- Real-time push (batch daily is acceptable)
- Source system modifications
- Historical backfill beyond 90 days

## Constraints

| Constraint | Detail |
|------------|--------|
| Access | No direct database access to source systems — API only |
| Platform | MSS tenant provisioning required before ingestion build can begin |
| Deadline | G3-directed deadline is fixed; no scope relief available |
