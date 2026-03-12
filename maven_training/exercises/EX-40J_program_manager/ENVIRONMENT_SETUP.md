# ENVIRONMENT SETUP — EX-40J Program Manager (Technical)

## Environment Type
MSS training instance with project tracking access. No special platform capabilities required beyond standard access.

## Required Access
- Training accounts: Viewer access to the EX-40J synthetic project record
- Evaluator account: Full access to project record (to verify participant answers)

## Pre-Load Instructions

### 1. Synthetic Project Record
Pre-load the EX-40J project record into the training environment:
- File: `EX-40J_Project_Record_Package/` (from training data package)
- Contents:
  - `pipeline_definition.md` — describes the LOGSTAT aggregation pipeline (what it does, tech stack, source systems)
  - `milestone_tracker.md` — 8-week project plan with weeks 1-6 marked; week 4 milestone missed
  - `open_tickets.md` — 4 open tickets including the rate-limit blocker (Ticket #EX40J-007)
  - `project_charter.md` — original scope, stakeholders, success criteria

### 2. Project Record Design (key facts evaluator must know)
- Current week: 6 of 8
- Missed milestone: Week 4 — "API integration complete" (delayed, not scope-changed)
- Blocker: Source system API rate-limited to 100 requests/hour; pipeline needs ~2,000/hour
- Downstream affected milestone: Week 7 — "UAT with end-user" (depends on integration)
- Commander approval needed: Yes — the schedule slip affects a G3-directed delivery date
- Workaround exists (evaluator knowledge only): batch processing with overnight run can work within rate limits — engineer has not proposed this yet

### 3. Evaluator Scenario Card (Task 4 — Retro)
See the evaluator role-play guidance in the EVALUATOR NOTES section of EXERCISE.md.

## Environment URL
```
[Insert training MSS tenant URL here — or provide as local files if MSS not required for this exercise]
```

## Notes
- This exercise has lower platform dependency than other TM-40 exercises
- The synthetic project record can be distributed as printed documents if the training environment is unavailable
- Do not reveal the rate-limit workaround to participants before Task 4
