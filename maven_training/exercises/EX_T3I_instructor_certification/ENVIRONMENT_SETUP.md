# ENVIRONMENT SETUP — EX_T3I INSTRUCTOR CERTIFICATION
## USAREUR-AF Operational Data Team — C2DAO

---

## Requirements

| Component | Requirement |
|---|---|
| **MSS Access** | Instructor-level account with Builder access + training environment admin |
| **Classroom** | Projector, instructor workstation, 1 workstation per candidate |
| **Accounts** | All candidates verified in MSS Training Environment before Day 1 |
| **Materials** | Published lesson plans for TM-10, TM-20, TM-30 (for microteaching block selection) |
| **Pre-staged Failures** | 6 environment failures configured per Block 9 (Day 2) — see setup procedures below |
| **Recorded Performances** | 5 pre-recorded trainee performances for calibration exercises (2 for Block 10, 3 for Block 19) |
| **Role-Play Scripts** | Prepared role-play scenarios for Blocks 12 (facilitation), 14 (error management), 15 (evaluator discipline), 21 (No-Go counseling) |

---

## Pre-Staged Environment Failures (Block 9)

Set up the following failures before Day 2:

| # | Failure | Setup Instructions |
|---|---|---|
| 1 | CAC auth failure | On one workstation: configure browser to reject CAC certificates (clear trusted root store or use an expired test cert). Reset after candidate resolves. |
| 2 | Expired account | Create a training account with an expired status. Candidate must identify the expired state and contact the correct POC. |
| 3 | Wrong environment | Set the default bookmark on one workstation to the production URL instead of the training URL. |
| 4 | Missing project access | Remove one training account from the training project membership. Candidate must diagnose and escalate. |
| 5 | Stale training data | Set the synthetic data loader to populate data with dates 6+ months old. Candidate must identify staleness and re-run the loader. |
| 6 | Pipeline schema change | Modify 1 column name in a source dataset used by a training pipeline. Pipeline will fail with a "column not found" error. |

---

## Recorded Trainee Performances

Prepare 5 screen-recorded trainee performances before the course:

| # | Used In | Performance Quality | Scenario |
|---|---|---|---|
| 1 | Block 10 (Day 2) | Clear Go | TM-20 pipeline building — all measures met cleanly |
| 2 | Block 10 (Day 2) | Borderline | TM-20 pipeline building — correct output but governance metadata incomplete |
| 3 | Block 19 (Day 4) | Clear Go | TM-10 practical exercise — all measures met |
| 4 | Block 19 (Day 4) | Clear No-Go | TM-10 practical exercise — classification marking error (critical item) |
| 5 | Block 19 (Day 4) | Borderline | TM-10 practical exercise — 4 of 5 non-critical passed, all critical passed |

If video recording is not feasible, prepare detailed written scenario descriptions with specific performance details for each measure.

---

## Instructor Preparation

- [ ] Confirm all candidate accounts active in MSS Training Environment
- [ ] Configure 6 pre-staged failures on designated workstations
- [ ] Prepare or verify 5 recorded performances
- [ ] Print T&EO scoring sheets for calibration exercises (5 copies per candidate)
- [ ] Print Instructor Observation Report forms for microteaching (1 per candidate)
- [ ] Print written exam packets (student version — no answer key distributed)
- [ ] Secure answer key in instructor binder
- [ ] Prepare role-play scripts for facilitation, error management, and No-Go counseling blocks
- [ ] Verify projector and instructor workstation connectivity
- [ ] Review lesson plans for TM-10, TM-20, TM-30 to assign microteaching blocks if needed

---

*USAREUR-AF Operational Data Team*
*Environment Setup — EX_T3I | Version 1.0 | March 2026*
