# BUILDER SPRINT — STANDARD OPERATING PROCEDURE
## Maven Smart System (MSS) — USAREUR-AF
### C2DAO Training Division

| | |
|---|---|
| **Document** | Builder Sprint SOP |
| **Designation** | BSP-SOP-001 |
| **Proponent** | USAREUR-AF C2DAO Training Division |
| **Effective Date** | March 2026 |
| **Cadence** | Quarterly (4 events per FY) |
| **Applies To** | Unit Training NCOs/Officers, MSS Administrators, Evaluators, SME Support Staff |

---

## OVERVIEW

The Builder Sprint (BSP) is a quarterly 5-day supervised build event. It operates **outside the TM-10 through TM-50 training sequence** — it is not a TM course, does not grant TM credit, and has no place in the TM prereq chain. It is a separate, optional program for personnel who hold TM-20 qualification and have a validated operational problem to build.

**BSP is not a substitute for TM-30.** Personnel who need structured instruction on advanced platform skills should enroll in TM-30. BSP assumes participants already operate at TM-20 level.

---

## ANNUAL SCHEDULE

Sprints are held quarterly. C2DAO publishes the annual BSP calendar each October alongside the Annual Training Schedule.

| Sprint | Target Quarter |
|---|---|
| BSP-1 | Q2 FY (January–March) |
| BSP-2 | Q3 FY (April–June) |
| BSP-3 | Q4 FY (July–September) |
| BSP-4 | Q1 FY (October–December) |

Specific dates are published 90+ days in advance. Units plan Project Brief submissions around the enrollment deadline (T-21 days before Day 1).

---

## PHASE 1 — ENROLLMENT AND PROJECT VALIDATION

### Step 1: Unit Identifies Candidate

Unit commander or Training NCO/Officer identifies a TM-20 qualified soldier or civilian with an operational problem suitable for BSP. Confirm:

- TM-10 and TM-20 Go evaluations on file
- An operational problem that produces a tangible Foundry product
- No code required (Python, TypeScript, OSDK) — if yes, route to TM-40 specialist enrollment instead
- Data access can be confirmed before sprint Day 1

### Step 2: Project Brief Preparation

Candidate prepares a Project Brief using the template in BSP_GUIDE.md Appendix A. The brief must include:

- Problem statement (2–5 sentences)
- Output type and description
- Named end user
- Data sources with access confirmation status
- Scope statement (in scope / out of scope for the 5-day sprint)
- Supervisor signature

### Step 3: Unit Submits Enrollment Request

Unit Training NCO/Officer submits to C2DAO Training Division:

- Enrollment Request (standard enrollment form — CAD Appendix A)
- Project Brief (BSP_GUIDE.md Appendix A)
- TM-10 and TM-20 Go records

**Enrollment deadline:** T-21 days before sprint Day 1.

### Step 4: C2DAO Project Review

C2DAO Training Division reviews the Project Brief within 5 duty days of receipt:

| Review criterion | Pass condition |
|---|---|
| TM-20 prereq verified | Go records on file |
| Problem statement clear | Specific output and named consumer |
| Scope feasible | Prototype achievable in 5 days at TM-20/30 skill level |
| Data access confirmed | All sources listed as CONFIRMED by candidate |
| No code requirements | No Python/TypeScript/OSDK work in scope |

If the brief fails any criterion, C2DAO returns it with specific feedback for revision. Revised briefs may be resubmitted up to T-14 days.

**Enrollment is confirmed upon Project Brief approval.** Confirmation is sent in writing to the unit Training NCO/Officer and candidate.

---

## PHASE 2 — PRE-SPRINT COORDINATION

### Step 5: Access Provisioning

Upon enrollment confirmation, the C2DAO coordinator submits an access provisioning request to the MSS Administrator:

- Sprint workspace creation (`BSP_[YYYYQQ]_SPRINT`) in MSS Training Environment
- Participant sub-projects created per approved project list
- Editor role granted to each participant for their sub-project
- Branch pre-configured per naming standard

Lead time: 7 duty days minimum. Confirm access provisioned no later than T-5 days.

### Step 6: Participant Access Confirmation

Each participant confirms access by T-5 days:

- [ ] MSS Training Environment accessible
- [ ] Sprint workspace and sub-project accessible
- [ ] All project data sources accessible
- [ ] Branch created and visible

Participants who cannot confirm by T-5 days must notify the coordinator immediately. Unresolved access by T-2 days may result in enrollment deferral to the next sprint cycle.

### Step 7: SME Pre-Brief

Coordinator provides the SME(s) with the participant project list and sprint schedule by T-2 days. See ENVIRONMENT_SETUP.md for SME pre-brief contents.

---

## PHASE 3 — SPRINT EXECUTION

C2DAO coordinator and evaluator are responsible for executing the sprint per SPRINT_PACKAGE.md. Key checkpoints:

| Day | Coordinator Actions |
|---|---|
| Day 1 | In-brief complete; environment check complete; all participants building by 0900 |
| Days 2–4 | Standup conducted 0800; blockers logged; scope escalations documented if applicable |
| Day 5 | All demos complete by 1200; Go/No-Go determinations made; out-brief complete by 1500 |

---

## PHASE 4 — POST-SPRINT ADMINISTRATION

Within 5 duty days of sprint close:

| Action | Responsible |
|---|---|
| Evaluation records completed and filed | Evaluator → C2DAO Training Division |
| Go notifications sent to participants and unit Training NCOs/Officers | C2DAO Training Division |
| No-Go counseling and remediation documentation | Evaluator + Coordinator |
| TM-40 redirect recommendations forwarded to unit Training NCOs/Officers | Evaluator |
| Sprint after-action report submitted | Coordinator |
| Production promotion coordination for any sprint products ready for promotion | Coordinator + unit Data Steward |

---

## CAPACITY AND QUOTA

| Parameter | Standard |
|---|---|
| Cohort size | 4–16 participants per sprint cycle |
| Minimum viable cohort | 4 participants (below 4, defer to next cycle unless C2DAO directs otherwise) |
| Maximum per sprint | 16 participants (above 16, split into two parallel cohort tracks) |
| SME ratio | 1 SME per ≤8 participants |
| Evaluator | 1 per sprint (may serve as lead SME if qualified) |

---

## WAIVERS

**Waiver of TM-20 prereq:** Not granted. TM-20 is the floor. Personnel without TM-20 Go on file are not eligible for BSP and should be enrolled in TM-20 first.

**Waiver of Project Brief:** Not granted. BSP without a validated project is a TM-30 equivalency request — that is a different program. Route to TM-30 enrollment.

**Waiver of T-14 day brief deadline:** May be granted at C2DAO discretion for cases where a validated operational problem emerges after the normal deadline. Requires evaluator confirmation that the project meets all scope criteria and data access is confirmed. Late briefs accepted no later than T-5 days.

---

## RELATIONSHIP TO TM SERIES

| Question | Answer |
|---|---|
| Does BSP count toward TM-30 credit? | No |
| Does BSP unlock TM-40 enrollment? | No |
| Does BSP appear in a training record? | Yes — as a separate event type; not as a TM course completion |
| Can a TM-30 graduate attend BSP? | Yes — TM-30 graduates with a validated project may attend |
| Can a TM-40 graduate attend BSP? | Yes — any TM-20+ qualified builder with a validated project may attend |

---

## DOCUMENT REFERENCES

| Document | Location |
|---|---|
| BSP Participant Guide | maven_training/builder_sprint/BSP_GUIDE.md |
| BSP Evaluator/Coordinator Package | maven_training/builder_sprint/SPRINT_PACKAGE.md |
| BSP Environment Setup | maven_training/builder_sprint/ENVIRONMENT_SETUP.md |
| Enrollment Request Form (standard) | training_management/CAD_MSS.md Appendix A |
| Project Brief template | BSP_GUIDE.md Appendix A |
| Handoff Package template | BSP_GUIDE.md Appendix B |

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*Builder Sprint SOP (BSP-SOP-001) | Version 1.0 | March 2026*
