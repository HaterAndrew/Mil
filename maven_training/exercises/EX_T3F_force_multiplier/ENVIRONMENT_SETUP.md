# ENVIRONMENT SETUP — EX_T3F MSC FORCE MULTIPLIER
## USAREUR-AF Operational Data Team — C2DAO

---

## Requirements

| Component | Requirement |
|---|---|
| **MSS Access** | All candidates must have active MSS accounts with Builder-level access |
| **Classroom** | Projector, instructor workstation, 1 workstation per candidate |
| **Materials** | TM-10 lesson plans, TM-10 exercise packet, TM-10 pre/post tests (student version), T&EO scoring sheets |
| **Pre-staged Failures** | 5 environment failures configured for Day 2 practice + 3 additional for Day 3 exam |
| **Role-Play Scripts** | Go/No-Go practicum scenarios (1 per candidate, mix of Go and No-Go outcomes) |

---

## Pre-Staged Environment Failures

### Day 2 Practice (Block 10) — All 5 Failures

| # | Failure | Setup Instructions |
|---|---|---|
| 1 | CAC auth failure | Configure one workstation to reject CAC (clear cache, expired test cert). Reset after use. |
| 2 | Expired account | Create a test account with expired status. |
| 3 | Wrong environment | Set bookmark to production URL on one workstation. |
| 4 | Missing project access | Remove one test account from training project membership. |
| 5 | Stale training data | Set synthetic data dates to 6+ months ago. |

### Day 3 Exam (Block 14) — 3 of 5 Failures

Select 3 failures from the set of 5 for the exam. Where possible, use different specific instances than the Day 2 practice (e.g., different workstation for CAC failure, different account for expired status).

---

## Go/No-Go Practicum Scenarios (Block 13)

Prepare 1 scenario per candidate. Each scenario specifies:
- Which T&EO (TM10-01 through TM10-06)
- What the role-player does (specific actions, including any errors)
- The correct overall Go/No-Go result

**Scenario mix:** At least 1 Go scenario and at least 1 No-Go scenario across the class. No two candidates receive the same T&EO.

| Example | T&EO | Role-Player Action | Correct Result |
|---|---|---|---|
| A | TM10-02 | Completes all steps correctly | Go |
| B | TM10-06 | Applies wrong classification marking | No-Go (critical item) |
| C | TM10-03 | Completes 4 of 5 non-critical, all critical passed | Go (if T&EO threshold is 4 of 5) |
| D | TM10-04 | Asks evaluator "what should I click?" during eval | Void — evaluator must identify that assistance invalidates the eval |

---

## Instructor Preparation

- [ ] Confirm all candidate accounts active in MSS Training Environment
- [ ] Configure Day 2 practice failures (all 5)
- [ ] Configure Day 3 exam failures (3 of 5, different instances from Day 2 where possible)
- [ ] Prepare Go/No-Go practicum scenarios (1 per candidate)
- [ ] Train role-players on their scenarios
- [ ] Print T&EO scoring sheets (multiple copies per candidate for practice + exam)
- [ ] Print TM-10 lesson plans for teach-back
- [ ] Print mock pre-test packets for Block 5 (Day 1)
- [ ] Prepare sample Unit Training Status Report (completed example for Block 6)
- [ ] Prepare the 15-topic sorting exercise for Block 2 (TM-20 scope)
- [ ] Prepare 4 borderline scenarios for Block 8 (Go/No-Go decision exercise)
- [ ] Prepare 6 escalation scenarios for Block 11
- [ ] Secure exam answer keys in instructor binder

---

*USAREUR-AF Operational Data Team*
*Environment Setup — EX_T3F | Version 1.0 | March 2026*
