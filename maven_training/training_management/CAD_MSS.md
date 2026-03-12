# COURSE ADMINISTRATIVE DATA
## Maven Smart System (MSS) Training Program
### USAREUR-AF Operational Data Team — C2DAO

---

| | |
|---|---|
| **Document** | Course Administrative Data (CAD) |
| **Program** | Maven Smart System (MSS) Training |
| **Proponent** | USAREUR-AF C2DAO |
| **Effective Date** | March 2026 |
| **Applies To** | All trainees enrolled in TM-10 through TM-40F |
| **Classification** | UNCLASSIFIED |

---

## SECTION 1 — PROGRAM OVERVIEW AND ADMINISTRATION

### 1-1. What This Document Covers

This Course Administrative Data document governs all administrative requirements for MSS training. It answers the questions instructors cannot answer during labs: what to bring, what happens if you miss a day, what happens if you fail, how to request a seat, and what the rules are. Read it before Day 1.

### 1-2. Training Proponent

**USAREUR-AF C2DAO** is the proponent for all MSS training. Questions about course content, access provisioning, schedule, and evaluation disputes go to C2DAO. Your unit MSS Administrator handles account provisioning for standard access (TM-10/20). C2DAO handles elevated access (TM-30 AIP, TM-40 Code Workspace, TM-40F OSDK).

**C2DAO Training POC:** Contact via your unit MSS Administrator or G6/G9 data team.

### 1-3. Training Environment

All training is conducted in the **MSS Training Environment** — a Foundry instance separate from production MSS. Training datasets are synthetic; they do not contain actual operational data. Do not attempt to access the production MSS environment during training.

### 1-4. Class Schedule

| Course | Typical Cadence | Maximum Class Size | Minimum Class Size |
|---|---|---|---|
| TM-10 | Monthly or as-needed | 20 students | 4 students |
| TM-20 | Quarterly | 12 students | 4 students |
| TM-30 | Quarterly | 8 students | 3 students |
| TM-40A/B/C/F | Semi-annual or on demand | 6 students | 2 students |
| TM-40D/E | Quarterly | 8 students | 3 students |

Classes below the minimum size threshold are typically consolidated with a subsequent iteration. Contact C2DAO Training POC for current schedule.

---

## SECTION 2 — ENROLLMENT AND PREREQUISITES

### 2-1. How to Request a Seat

1. Complete the **Enrollment Request Form** (Appendix A).
2. Submit to your unit Training NCO/Officer, who forwards to your unit MSS Administrator.
3. The MSS Administrator submits to C2DAO Training POC.
4. C2DAO confirms enrollment and notifies the student and unit training coordinator.

Seats are allocated by unit quota. Units with unfilled quotas may be reassigned at 10 days prior to course start.

### 2-2. Prerequisite Verification

Prerequisites are verified by C2DAO before a seat is confirmed. Do not assume enrollment is complete until you receive confirmation from C2DAO or your unit Training NCO.

| Course | Prerequisites (all must be verified as Go) |
|---|---|
| TM-10 | None. All personnel eligible. |
| TM-20 | TM-10 Go on file |
| TM-30 | TM-10 and TM-20 Go on file |
| TM-40A | TM-10, TM-20, TM-30 Go on file; quantitative background (statistics, linear algebra); Python or R proficiency |
| TM-40B | TM-10, TM-20, TM-30 Go on file; Python proficiency; Data Literacy Technical Reference read |
| TM-40C | TM-10, TM-20, TM-30 Go on file; Python proficiency (pandas, scikit-learn, PyTorch or equivalent) |
| TM-40D | TM-10, TM-20 Go on file; TM-30 recommended but not required |
| TM-40E | TM-10, TM-20 Go on file; TM-30 recommended but not required |
| TM-40F | TM-10, TM-20, TM-30 Go on file; TypeScript or Python proficiency; REST API familiarity |

Prerequisites marked as recommendations carry a strong advisory: trainees without TM-30 attending TM-40D or TM-40E consistently underperform on the evaluation. Units should not enroll personnel who do not meet the recommended prerequisites without C2DAO approval.

### 2-3. Technical Prerequisite Verification (Specialist Tracks)

For TM-40A, TM-40B, TM-40C, and TM-40F, trainees must verify the required access level is active **before Day 1**. Enrollment requires confirmation of:

- Code Workspace running provided test script (TM-40A, TM-40C)
- AIP Logic authoring access active (TM-40B)
- GPU-enabled Code Workspace running provided test script (TM-40C)
- OSDK developer access and developer token working (TM-40F)

If access is not confirmed before Day 1, the seat may be forfeited. Do not arrive expecting to resolve access issues on Day 1 morning — this disrupts the class and the issue typically cannot be resolved same-day.

---

## SECTION 3 — REPORTING INSTRUCTIONS AND DAY 1 PREPARATION

### 3-1. Reporting

Report on Day 1 NLT 15 minutes before the scheduled start time. Training starts at 0800 unless a different time is published for a specific iteration. Report to the designated MSS Training Room.

Trainees should have the following ready on Day 1:
- [ ] CAC and PIV PIN — know your PIV PIN before you arrive. This is tested on Day 1 of TM-10. It is also a source of delay that holds up the entire class.
- [ ] Network connectivity to MSS Training Environment confirmed on the MSS-connected workstation
- [ ] Account active in the MSS Training Environment (test login before Day 1)
- [ ] Required pre-course reading completed (see course syllabus)
- [ ] For TM-40F: configured laptop (Node.js LTS, TypeScript, IDE) brought to training

### 3-2. Day-Before Checklist

The day before Day 1:
- [ ] Log in to the MSS Training Environment and confirm your access level matches what is required
- [ ] Review the course syllabus to confirm you have completed pre-course reading
- [ ] Check that any elevated access (Builder, Editor, Code Workspace, OSDK) is active
- [ ] For TM-40C/40F: run the provided test script on your workspace/environment; if it fails, contact C2DAO **today**, not tomorrow

If access issues exist and cannot be resolved before Day 1, notify your unit MSS Administrator and the C2DAO Training POC immediately. Do not wait until the morning of class.

### 3-3. What to Bring

- Government-issued workstation with CAC reader and network connectivity to MSS
- Printed or digital copy of the relevant TM (provided by C2DAO before course)
- Printed course syllabus
- Note-taking materials
- For TM-40F: personal laptop configured per the pre-course checklist (external IDE permitted and recommended)

---

## SECTION 4 — ACADEMIC POLICIES

### 4-1. Attendance

Attendance at all scheduled blocks of instruction is required. A trainee who misses more than **10% of scheduled instructional hours** for any course may be administratively withdrawn and rescheduled to a future iteration.

| Course | Max Missed Hours (10% threshold) |
|---|---|
| TM-10 (8 hrs) | 0 hours — no absences permitted for a 1-day course |
| TM-20 (40 hrs) | 4 hours |
| TM-30 (40 hrs) | 4 hours |
| TM-40A/B/C/F (40 hrs) | 4 hours |
| TM-40D/E (24 hrs) | 2.4 hours (effectively 0 — contact C2DAO if you must miss any time) |

An absence does not automatically excuse a trainee from evaluation. A trainee who misses instruction may still be required to demonstrate proficiency on all tasks at evaluation. Missed instruction that covers evaluated tasks places the full burden of self-remediation on the trainee before the evaluation.

**No absence from TM-40B Block 1 (AI Safety Seminar)** is permitted under any circumstances. This block cannot be made up independently. A trainee who misses the AI Safety Seminar must attend the full TM-40B course at a future iteration.

### 4-2. Tardiness

Tardiness disrupts labs and other trainees. More than 15 minutes late to any block counts as an absence for that block. Repeat tardiness (3+ instances) is grounds for administrative withdrawal.

### 4-3. Make-Up Policy

If a trainee misses instruction due to a documented duty requirement (training exercise, assigned mission, medical):
1. The trainee notifies the instructor and unit Training NCO on the same duty day.
2. The instructor identifies whether the missed block is an evaluated task.
3. The trainee completes self-study of the missed material using the relevant TM and lesson plan outline.
4. The instructor determines whether a make-up lab is feasible within the course timeline. If not, the trainee may require rescheduling.

Make-up labs are not automatically provided. They are at instructor discretion and subject to training environment availability.

### 4-4. Academic Integrity

MSS training evaluations are individual assessments. On all evaluated practical exercises:

- **No assistance from other trainees** during the evaluation period
- **No access to the internet**, other training resources, or completed examples from prior trainees
- Reference to the relevant TM and course syllabus is **permitted** (open-book)
- Reference to instructor-provided reference cards is **permitted**
- The evaluator may ask the trainee to explain their design decisions — this is a standard evaluation procedure, not a challenge

Violation of academic integrity standards results in automatic No-Go and is reported to the trainee's commander.

### 4-5. Conduct

Conduct during training reflects Army standards. Trainees are expected to:
- Actively engage with labs and discussions
- Ask questions when lost — passively watching and not asking is the most common cause of failed evaluations
- Support other trainees' learning (but not during evaluations)
- Comply with all MSS Training Environment access controls — do not attempt to access data, projects, or tools outside the scope of the current lab

---

## SECTION 5 — EVALUATION AND GO/NO-GO STANDARDS

### 5-1. How Evaluations Work

Each course ends with a practical exercise. The evaluation:
- Is conducted in the MSS Training Environment
- Uses scenario materials provided by the instructor at the start of the evaluation period
- Is observed by the instructor (evaluator) who documents performance
- Is Go/No-Go — there is no partial credit; each task either meets standard or it does not
- Is open TM — trainees may reference the relevant TM and course syllabus during the evaluation
- Requires tasks to be completed **independently** — the evaluator observes but does not assist

The evaluator may ask questions during the evaluation to verify understanding (e.g., "What classification marking applies to this dataset?" or "Why did you configure this Action with Editor-only access?"). These questions are part of the evaluation.

### 5-2. Go Standard

A trainee receives **Go** when:
1. All evaluated tasks are completed to standard without instructor assistance
2. No hard No-Go items are violated (see Section 5-3)
3. The minimum task threshold is met (see course syllabus — typically all tasks, or a stated minimum such as "5 of 6")

### 5-3. No-Go Standard

A trainee receives **No-Go** when:
1. A hard No-Go item is violated (automatic No-Go; remaining tasks still evaluated for feedback)
2. The minimum task threshold is not met within the allotted evaluation time
3. The trainee requests instructor assistance during the evaluation (automatically fails the task requiring assistance)

**Hard No-Go items result in automatic No-Go regardless of all other performance.** See POI Chapter 5 for the full hard No-Go item list.

### 5-4. Evaluation Time

Trainees have the full scheduled evaluation period. The evaluator does not extend the evaluation period. If time runs out before all tasks are completed, uncompleted tasks are marked No-Go.

### 5-5. Evaluation Documentation

The evaluator documents the evaluation outcome on the Individual Training Record (Appendix B). Results are provided to the trainee and recorded in the Unit Training Status Matrix within 2 duty days.

---

## SECTION 6 — NO-GO AND REMEDIATION POLICY

### 6-1. Receiving a No-Go

A No-Go result is not a permanent record of failure — it is a signal that more training time is required before the trainee is certified. The purpose of the Go/No-Go standard is operational: an MSS product built by a trainee who cannot independently meet the standard creates data quality and governance risk for the unit.

### 6-2. Immediate Actions on No-Go

Within 1 duty day of a No-Go result:
1. The evaluator provides a written debrief identifying each failed task and the reason for No-Go
2. The instructor and trainee complete a counseling documenting: failed tasks, recommended remediation plan, re-evaluation date
3. The unit Training NCO is notified
4. For TM-40A/B/C/F: the trainee's commander is notified

### 6-3. Remediation Training Requirements

| Course | Minimum Remediation Hours | Method |
|---|---|---|
| TM-10 | 2 hours | Self-study with TM + supervised lab with instructor |
| TM-20, TM-40D, TM-40E | 4 hours | Supervised lab on failed tasks; build from scratch on a different dataset |
| TM-30, TM-40A, TM-40B, TM-40C, TM-40F | 8 hours | Full-day supervised lab; rebuilding failed components |

Remediation focuses on the specific failed tasks, not a repeat of the entire course. However, the re-evaluation covers all course tasks — not just the previously failed ones.

### 6-4. Re-Evaluation

Re-evaluation uses a different practical exercise scenario (different dataset and scenario context) but the same task structure. The trainee must demonstrate the same competencies, not simply memorize the prior scenario.

Re-evaluation is scheduled within **10 duty days** of the No-Go result. If the trainee's duty schedule prevents re-evaluation within 10 days, the timeline may be extended with C2DAO approval — but re-evaluation must occur within the same course iteration window where possible.

### 6-5. Second No-Go

A trainee who receives No-Go on both the initial evaluation and the first re-evaluation requires:
1. Written request to C2DAO Training POC from the trainee's commander for a second re-evaluation
2. C2DAO review and approval before scheduling
3. Additional remediation as directed by C2DAO (typically requires re-attending a future course iteration in full)

This policy protects the unit from certifying personnel who have not demonstrated competency. A second No-Go is uncommon; when it occurs, it typically indicates a prerequisite gap, not a performance issue. C2DAO will assess whether the prerequisite progression was appropriate.

### 6-6. No-Go Record

No-Go results, remediation completion, and re-evaluation results are all documented on the Individual Training Record. No-Go records are not adverse — they document the training process. A trainee who received No-Go once and passed re-evaluation is certified to the same standard as one who passed on the first attempt.

---

## SECTION 7 — SYSTEM ACCESS AND EQUIPMENT REQUIREMENTS

### 7-1. Standard Access Levels

| Access Level | Description | Who Provisions | Lead Time |
|---|---|---|---|
| Viewer (TM-10) | Can view data, dashboards, Workshop apps, Contour, Quiver, AIP; cannot build or modify | Unit MSS Administrator | 5 duty days |
| Builder (TM-20, 40D, 40E) | Can create projects, ingest data, build pipelines, Object Types, Actions, Workshop apps | Unit MSS Administrator | 5 duty days |
| Editor (TM-30) | Can edit and promote production data products; includes Builder capabilities | Unit MSS Administrator | 7 duty days |
| AIP Logic Configuration (TM-30, 40E) | Can configure AIP Logic workflows; cannot author | C2DAO or designated admin | 7 duty days |
| AIP Logic Authoring (TM-40B) | Can author and modify AIP Logic workflows | C2DAO only | 7–10 duty days |
| Agent Studio (TM-40B) | Can configure and test Agent Studio agents | C2DAO only | 7–10 duty days |
| Code Workspace (TM-40A) | CPU-allocated Code Workspace for Python/R analysis | C2DAO only | 7–10 duty days |
| GPU Code Workspace (TM-40C) | GPU-enabled Code Workspace for model training | C2DAO only | 10+ duty days |
| OSDK Developer (TM-40F) | OSDK developer token; access to specific Object Types for development | C2DAO only | 10+ duty days |

### 7-2. Access Troubleshooting

**Permission denied / 403 error:** You have the wrong access level. Contact your unit MSS Administrator. Do not escalate to C2DAO for standard access issues.

**Cannot create project / no Create button:** Your account has Viewer access, not Builder. Request Builder access from unit MSS Administrator. Allow 5 duty days.

**AIP Logic / Code Workspace not appearing:** These features require elevated access provisioned by C2DAO. Contact C2DAO Training POC.

**Login fails entirely (not 403):** CAC issue or PIV PIN problem. Contact your G6 S6 or unit IT support — this is not an MSS issue.

**"Test account cannot see my Workshop application":** Your application's visibility settings are not set correctly. See TM-20 Chapter 6. This is a common lab step; fix it before the evaluation.

### 7-3. Lost or Compromised Credentials

If you believe your MSS account credentials have been compromised, or if you observe another user accessing accounts or data they should not have access to, immediately notify your unit MSS Administrator and C2DAO. Do not attempt to investigate independently.

---

## SECTION 8 — DATA HANDLING AND CLASSIFICATION

### 8-1. Training Environment Data

Training data is synthetic. However, trainees must apply the same classification habits in the Training Environment as they would in production. If you are uncertain whether a dataset is synthetic or operational, treat it as operational until confirmed.

### 8-2. Classification Markings

All MSS data products must carry classification markings. In the Training Environment, all provided datasets are marked UNCLASSIFIED. Trainees must:
- Confirm the marking of any dataset before using it in a lab or exercise
- Apply the correct marking to any product they build
- Not export or save data from the Training Environment outside of approved local development directories

### 8-3. Export Controls

Even in the Training Environment, exporting data to external storage, emailing datasets, or saving to personal cloud storage is prohibited. If you need a copy of training data for an exercise, use the MSS export procedure to a designated training output location — do not copy-paste data into personal tools.

### 8-4. Sensitive Architecture Details

Do not include system architecture specifics (Foundry endpoint URLs, dataset paths, API keys, token values) in commit messages, screenshots, or communications outside the training environment.

---

## SECTION 9 — STUDENT RIGHTS AND RESPONSIBILITIES

### 9-1. Trainee Rights

- Receive a pre-course syllabus and required reading list at least 5 duty days before training
- Receive a written debrief of any No-Go evaluation within 1 duty day
- Request a review of an evaluation outcome within 3 duty days of receiving results — submit a written request to C2DAO Training POC
- Expect a training environment that functions correctly; if equipment or access issues prevent completing a lab, the issue is documented and the lab is not counted against the trainee

### 9-2. Trainee Responsibilities

- Complete pre-course reading before Day 1
- Arrive with required access confirmed and working
- Actively participate in labs and discussions — passive observation does not meet the standard
- Complete evening reading assignments — trainees who arrive unprepared for the next day's lab consistently underperform
- Flag access or environment issues to the instructor on the same day they occur
- Maintain data discipline: apply correct classification, do not export training data outside approved locations, do not share other trainees' work during evaluations

### 9-3. Complaints and Concerns

Trainees with complaints about instructor conduct, evaluation fairness, or training environment issues should:
1. First, attempt to resolve with the instructor directly
2. If unresolved, submit a written complaint to C2DAO Training POC within 5 duty days
3. C2DAO will review and respond within 10 duty days

---

## APPENDIX A — ENROLLMENT REQUEST FORM

```
=========================================================
MSS TRAINING ENROLLMENT REQUEST
=========================================================
Date of Request:         _________________________________
Trainee Name:            _________________________________
Rank/Grade:              _________________________________
Unit:                    _________________________________
MOS/Branch:              _________________________________
DSN:                     _________________________________
Email (NIPR):            _________________________________

REQUESTED COURSE
Course:                  _________________________________
Preferred Course Date:   _________________________________
Alternate Date:          _________________________________

PREREQUISITES (attach Go evaluation records)
TM-10 Go Date:           _________ (required for TM-20+)
TM-20 Go Date:           _________ (required for TM-30+)
TM-30 Go Date:           _________ (required for TM-40A/B/C/F)

TECHNICAL PREREQUISITES (TM-40 specialist tracks only)
[ ] Code Workspace provisioned and test script passing (TM-40A/C)
[ ] AIP Logic authoring access confirmed (TM-40B)
[ ] GPU Code Workspace provisioned and test script passing (TM-40C)
[ ] OSDK developer token active (TM-40F)

Unit Training NCO/Officer:  _______________________________
Signature:               _________________________________
Date:                    _________________________________

=========================================================
FOR C2DAO USE ONLY
Enrollment confirmed:    [ ] Yes  [ ] No
Class date assigned:     _________________________________
Access provisioning req: _________________________________
Confirmed by:            _________________________________
Date:                    _________________________________
=========================================================
```

---

## APPENDIX B — INDIVIDUAL TRAINING RECORD

```
=========================================================
MSS INDIVIDUAL TRAINING RECORD
=========================================================
Trainee Name:            _________________________________
Rank/Grade:              _________________________________
Unit:                    _________________________________
MOS/Branch:              _________________________________
Date of Arrival USAREUR-AF: _____________________________

=========================================================
COURSE COMPLETION RECORD
=========================================================

TM-10 | MAVEN USER (1 day)
  Attended:     ___________________________________________
  Evaluator:    ___________________________________________
  Result:       [ ] GO     [ ] NO-GO
  Re-eval Date: ___________________________________________
  Re-eval Result: [ ] GO   [ ] NO-GO  [ ] N/A
  Certified Date: ___________________________________________

TM-20 | BUILDER (5 days)
  Attended:     ___________________________________________
  Evaluator:    ___________________________________________
  Result:       [ ] GO     [ ] NO-GO
  Re-eval Date: ___________________________________________
  Re-eval Result: [ ] GO   [ ] NO-GO  [ ] N/A
  Certified Date: ___________________________________________

TM-30 | ADVANCED BUILDER (5 days)
  Attended:     ___________________________________________
  Evaluator:    ___________________________________________
  Result:       [ ] GO     [ ] NO-GO
  Re-eval Date: ___________________________________________
  Re-eval Result: [ ] GO   [ ] NO-GO  [ ] N/A
  Certified Date: ___________________________________________

TM-40 SPECIALIST TRACK (circle):  40A  40B  40C  40D  40E  40F
  Attended:     ___________________________________________
  Evaluator:    ___________________________________________
  Result:       [ ] GO     [ ] NO-GO
  Re-eval Date: ___________________________________________
  Re-eval Result: [ ] GO   [ ] NO-GO  [ ] N/A
  Certified Date: ___________________________________________

=========================================================
REMEDIATION RECORD (attach counseling if applicable)
=========================================================
Course:     ________________  Date:  ___________________
Failed Tasks: _____________________________________________
Remediation Hours Completed:  ___________________________
Remediation Instructor:  ________________________________
Re-eval Scheduled:  _____________________________________

=========================================================
SUSTAINMENT TRAINING RECORD
=========================================================
Annual TM-10 refresher:
  Date:  _________________  Instructor:  ________________
  Date:  _________________  Instructor:  ________________

Quarterly builds documented: (attach unit log)

=========================================================
RECORD MAINTAINED BY:  _________________________________
Last Updated:          _________________________________
=========================================================
```

---

## APPENDIX C — NO-GO REMEDIATION FORM

```
=========================================================
MSS TRAINING NO-GO REMEDIATION RECORD
=========================================================
Trainee Name:       _____________________________________
Course:             _____________________________________
Original Eval Date: _____________________________________
Evaluator:          _____________________________________

FAILED TASKS AND REASONS
Task 1: _________________________ Reason: _______________
Task 2: _________________________ Reason: _______________
Task 3: _________________________ Reason: _______________
Task 4: _________________________ Reason: _______________
(attach additional sheet if needed)

ROOT CAUSE ASSESSMENT (check all that apply)
[ ] Insufficient pre-course reading
[ ] Missing prerequisite knowledge/skill
[ ] Access or equipment issue during evaluation
[ ] Misunderstood task requirements
[ ] Insufficient lab practice time (note which labs)
[ ] Other: _______________________________________________

REMEDIATION PLAN
Start Date:   ___________________________________________
End Date:     ___________________________________________
Total Hours:  ___________________________________________
Method:       [ ] Supervised lab  [ ] Self-study + lab
Remediation Instructor: ________________________________

Tasks to re-practice (specific to failures above):
1. _____________________________________________________
2. _____________________________________________________
3. _____________________________________________________

Re-evaluation Date:   __________________________________
Re-evaluation Evaluator: _______________________________

TRAINEE SIGNATURE:  ___________________________________
INSTRUCTOR SIGNATURE: _________________________________
UNIT TRAINING NCO SIGNATURE: _________________________
DATE:  _________________________________________________

=========================================================
FOR C2DAO USE (second No-Go only)
Commander's request received: ____________
C2DAO approval:  [ ] Approved  [ ] Denied
Action directed: ________________________________________
C2DAO POC:       _______________________________________
=========================================================
```

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*CAD MSS-CAD-001 | Version 1.0 | March 2026*
