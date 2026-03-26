# FOUNDRY BOOTCAMP — EVALUATOR AND COORDINATOR PACKAGE
## Maven Smart System (MSS) — USAREUR-AF

| | |
|---|---|
| **Document** | FBC Evaluator/Coordinator Package |
| **Proponent** | USAREUR-AF C2DAO Training Division |
| **Applies To** | Bootcamp evaluators, SME support staff, C2DAO event coordinators |

---

## 1. EVALUATOR ROLE

The evaluator is the single point of accountability for Go/No-Go determinations. One evaluator per bootcamp event. The evaluator:

- Reviews each participant's Project Brief before Day 1 (submitted with enrollment)
- Conducts Day 5 product demo reviews
- Makes the Go/No-Go determination per the standards in FBC_GUIDE.md Chapter 5
- Completes the Evaluation Record (Appendix A) for each participant
- Forwards completed records to C2DAO Training Division for filing

The evaluator does not provide platform instruction during the bootcamp. If a participant needs instruction rather than consultation, the evaluator flags this to the SME and, if warranted, documents a No-Go with a SL 3 redirect recommendation.

---

## 2. SME SUPPORT ROLE

SME ratio: 1 SME per ≤8 participants. For larger bootcamp cohorts (9–16 participants), two SMEs.

SME duties:
- Available throughout build days for 1:1 consultation
- Runs or co-runs daily standup
- Escalates blockers to the evaluator when scope changes are needed
- Documents any projects that surface SL 4 requirements during the bootcamp (see Section 3)

SME does not: instruct, build participant products, approve scope changes without evaluator coordination.

---

## 3. SCOPE ESCALATION PROCEDURE

When a participant's project turns out to require work beyond SL 2/30 scope (Python, TypeScript, OSDK, or code-level transforms), the SME and evaluator jointly:

1. Notify the participant on the day the code requirement surfaces
2. Assess whether a no-code alternative can meet the validated problem statement
   - If yes: redirect to no-code approach, document the change in the evaluation record
   - If no: issue a partial credit note — participant receives documentation credit for the Project Brief and Handoff Package, but No-Go on functional product; recommend appropriate SL 4 track for enrollment
3. Document in the evaluation record: what was built, what could not be completed, what SL 4 track is recommended

---

## 4. DAY 1 IN-BRIEF AGENDA (coordinator-led, 60 min)

| Time | Item |
|---|---|
| 0800–0810 | Welcome, logistics (bathrooms, comms, emergency procedures) |
| 0810–0825 | Bootcamp structure overview: goals, schedule, standup cadence, evaluation standard |
| 0825–0840 | Governance refresher: naming conventions, branching, what requires data steward coordination |
| 0840–0855 | Environment check: each participant confirms access, data available, workspace loads |
| 0855–0900 | SME introductions; open questions; build begins |

The in-brief is not a platform training block. Keep it under 60 minutes. If a participant's environment does not load during the check, the SME works with them 1:1 while the in-brief continues. If the issue is not resolved by 1000, the coordinator contacts C2DAO for access resolution.

---

## 5. DAY 5 DEMO / PEER REVIEW FORMAT

Each participant gets 15 minutes:
- 10 min: live demonstration of their product
- 5 min: Q&A from evaluator and peers

Evaluator notes completion status against Go standards during the demo. Go/No-Go is determined after all demos are complete.

After demos, evaluator conducts 1:1 evaluations as needed before 1200.

---

## 6. GO/NO-GO DETERMINATION

Go when all four standards are met (see FBC_GUIDE.md Chapter 5):

| Standard | Notes |
|---|---|
| Functional product | Live demo, evaluator-operated — not a recorded video |
| Documentation | Check naming standards during demo; description field present |
| Handoff package | Review submitted package before 1200 on Day 5 |
| Governance | Confirm branch exists; check branch review status; confirm promotion plan is documented |

**Partial Go** is not a formal evaluation outcome — it is either Go or No-Go. Use the evaluation record notes to document what was completed and what remains for the post-bootcamp period.

---

## 7. POST-SPRINT FOLLOW-UP (coordinator)

Within 5 duty days of bootcamp close:
- [ ] Evaluation records filed with C2DAO Training Division
- [ ] Go participants notified in writing; unit Training NCO/Officer copied
- [ ] No-Go participants counseled; remediation plan documented (re-bootcamp or SL 3 redirect)
- [ ] Any products requiring data steward coordination flagged to the unit Data Steward
- [ ] Bootcamp after-action report drafted (see Appendix B)

---

## APPENDIX A — EVALUATION RECORD

```
FOUNDRY BOOTCAMP — EVALUATION RECORD
Evaluator: [Name, Rank]
Bootcamp: [Quarter/Year]

PARTICIPANT: [Name, Rank, Unit, MOS]
Project: [Project name and one-sentence description]

EVALUATION (circle):

Functional product:          GO / NO-GO
Documentation:               GO / NO-GO
Handoff package:             GO / NO-GO
Governance:                  GO / NO-GO

OVERALL:                     GO / NO-GO

NOTES:
[Observations, partial completions, scope escalations, SL 4 recommendations]

Evaluator signature: _________________ Date: _________
```

---

## APPENDIX B — AFTER-ACTION REPORT TEMPLATE

```
FOUNDRY BOOTCAMP — AFTER-ACTION REPORT
Bootcamp: [Quarter/Year]
Coordinator: [Name]
Evaluator: [Name]

PARTICIPANTS: [Total enrolled / Total completed (Go) / Total No-Go]

PRODUCTS BUILT:
[List each product, participant, and Go/No-Go outcome]

SCOPE ESCALATIONS (SL 4 redirects):
[List any projects that surfaced code requirements and recommended tracks]

SME OBSERVATIONS:
[Common blockers, governance issues, platform gaps seen across cohort]

COORDINATION ISSUES:
[Access problems, environment issues, data access delays]

RECOMMENDED IMPROVEMENTS:
[Changes to Project Brief criteria, pre-bootcamp checklist, Day 1 agenda, etc.]

Submitted to C2DAO Training Division: [Date]
```

---

*USAREUR-AF Operational Data Team*
*Foundry Bootcamp (FBC) Evaluator/Coordinator Package | Version 1.0 | March 2026*
