# ENVIRONMENT SETUP — EX_40J Program Manager (Technical)

**Track:** EX_40J — Program Manager (Technical) (TM-40J) | **Prerequisite:** TM-30 REQUIRED | **Continuation:** TM-50J — Advanced Program Manager
**Companion exams:** EXAM_TM40J_PRE (administer before exercise), EXAM_TM40J_POST (administer after exercise)
**Training data:** `training_data/EX_40J_project_record_package/` — milestone_tracker.md, open_tickets.md, pipeline_definition.md, project_charter.md

## Environment Type

MSS training instance with project tracking access. No special platform capabilities required beyond standard access.

## Required Access

| Account | Access |
|---------|--------|
| Training accounts | Viewer access to the EX_40J synthetic project record |
| Evaluator account | Full access to project record (to verify participant answers) |

## Pre-Load Instructions

### 1. Synthetic Project Record

Pre-load the EX_40J project record into the training environment:

| Item | Details |
|------|---------|
| Package | `EX_40J_project_record_package/` (from training data package) |
| `pipeline_definition.md` | Describes the LOGSTAT aggregation pipeline (what it does, tech stack, source systems) |
| `milestone_tracker.md` | 8-week project plan with weeks 1–6 marked; week 4 milestone missed |
| `open_tickets.md` | 4 open tickets including the rate-limit blocker (Ticket #EX40J-007) |
| `project_charter.md` | Original scope, stakeholders, success criteria |

### 2. Key Facts — Evaluator Must Know

| Fact | Value |
|------|-------|
| Current week | 6 of 8 |
| Missed milestone | Week 4 — "API integration complete" (delayed, not scope-changed) |
| Blocker | Source system API rate-limited to 100 requests/hour; pipeline needs ~2,000/hour |
| Downstream affected milestone | Week 7 — "UAT with end-user" (depends on integration) |
| Commander approval needed | Yes — the schedule slip affects a G3-directed delivery date |
| Workaround (evaluator only) | Batch processing with overnight run can work within rate limits — engineer has not proposed this yet |

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
