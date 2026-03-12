# COURSE ADMINISTRATIVE DATA
## Maven Smart System (MSS) Training Program
### USAREUR-AF Operational Data Team — C2DAO

| | |
|---|---|
| **Document** | Course Administrative Data (CAD) |
| **Program** | Maven Smart System (MSS) Training |
| **Proponent** | USAREUR-AF C2DAO |
| **Effective Date** | March 2026 |
| **Applies To** | All trainees enrolled in TM-10 through TM-40L |
| **Classification** | UNCLASSIFIED |

---

## SECTION 1 — PROGRAM OVERVIEW AND ADMINISTRATION

### 1-1. What This Document Covers

This CAD governs all administrative requirements for MSS training. Read it before Day 1. It answers what to bring, what happens if you miss a day, what happens if you fail, how to request a seat, and what the rules are.

### 1-2. Training Proponent

**USAREUR-AF C2DAO** is the proponent for all MSS training. Course content, access provisioning, schedule, and evaluation disputes go to C2DAO. Your unit MSS Administrator handles account provisioning for standard access (TM-10/20). C2DAO handles elevated access (TM-30 AIP, TM-40 Code Workspace, TM-40L OSDK).

**C2DAO Training POC:** Contact via your unit MSS Administrator or G6/G9 data team.

### 1-3. Training Environment

All training is in the **MSS Training Environment** — a Foundry instance separate from production MSS. Training datasets are synthetic. Do not attempt to access the production MSS environment during training.

### 1-4. Class Schedule

| Course | Typical Cadence | Max Class Size | Min Class Size |
|---|---|---|---|
| TM-10 | Monthly or as-needed | 20 students | 4 students |
| TM-20 | Quarterly | 12 students | 4 students |
| TM-30 | Quarterly | 8 students | 3 students |
| TM-40G/H/I/L | Semi-annual or on demand | 6 students | 2 students |
| TM-40J/K | Quarterly | 8 students | 3 students |

Classes below the minimum size threshold are typically consolidated with a subsequent iteration. Contact C2DAO Training POC for current schedule.

---

## SECTION 2 — ENROLLMENT AND PREREQUISITES

### 2-1. How to Request a Seat

1. Complete the **Enrollment Request Form** (Appendix A)
2. Submit to your unit Training NCO/Officer, who forwards to your unit MSS Administrator
3. The MSS Administrator submits to C2DAO Training POC
4. C2DAO confirms enrollment and notifies the student and unit training coordinator

Seats are allocated by unit quota. Units with unfilled quotas may be reassigned at 10 days prior to course start.

### 2-2. Prerequisite Verification

Prerequisites are verified by C2DAO before a seat is confirmed. Do not assume enrollment is complete until you receive confirmation.

| Course | Prerequisites (all must be verified as Go) |
|---|---|
| TM-10 | None. All personnel eligible. |
| TM-20 | TM-10 Go on file |
| TM-30 | TM-10 and TM-20 Go on file |
| TM-40G | TM-10, TM-20, TM-30 Go on file; quantitative background (statistics, linear algebra); Python or R proficiency |
| TM-40H | TM-10, TM-20, TM-30 Go on file; Python proficiency; Data Literacy Technical Reference read |
| TM-40I | TM-10, TM-20, TM-30 Go on file; Python proficiency (pandas, scikit-learn, PyTorch or equivalent) |
| TM-40J | TM-10, TM-20, TM-30 Go on file (all required) |
| TM-40K | TM-10, TM-20, TM-30 Go on file (all required) |
| TM-40L | TM-10, TM-20, TM-30 Go on file; TypeScript or Python proficiency; REST API familiarity |

TM-30 is a hard prerequisite for all TM-40G–L specialist tracks, including TM-40J and TM-40K.

### 2-3. Technical Prerequisite Verification (Specialist Tracks)

For TM-40G, TM-40H, TM-40I, and TM-40L, trainees must verify the required access level is active **before Day 1**:

- [ ] Code Workspace running provided test script (TM-40G, TM-40I)
- [ ] AIP Logic authoring access active (TM-40H)
- [ ] GPU-enabled Code Workspace running provided test script (TM-40I)
- [ ] OSDK developer access and developer token working (TM-40L)

If access is not confirmed before Day 1, the seat may be forfeited. Do not arrive expecting to resolve access issues on Day 1 morning.

---

## SECTION 3 — REPORTING INSTRUCTIONS AND DAY 1 PREPARATION

### 3-1. Reporting

Report on Day 1 NLT 15 minutes before the scheduled start time. Training starts at 0800 unless otherwise published. Report to the designated MSS Training Room.

**Day 1 readiness checklist:**
- [ ] CAC and PIV PIN — know your PIV PIN before you arrive. Tested on Day 1 of TM-10.
- [ ] Network connectivity to MSS Training Environment confirmed on the MSS-connected workstation
- [ ] Account active in the MSS Training Environment (test login before Day 1)
- [ ] Required pre-course reading completed (see course syllabus)
- [ ] For TM-40L: configured laptop (Node.js LTS, TypeScript, IDE) brought to training

### 3-2. Day-Before Checklist

- [ ] Log in to the MSS Training Environment and confirm your access level matches the requirement
- [ ] Review the course syllabus to confirm pre-course reading is complete
- [ ] Check that any elevated access (Builder, Editor, Code Workspace, OSDK) is active
- [ ] For TM-40I/40L: run the provided test script on your workspace/environment; if it fails, contact C2DAO **today**, not tomorrow

If access issues cannot be resolved before Day 1, notify your unit MSS Administrator and the C2DAO Training POC immediately.

### 3-3. What to Bring

- Government-issued workstation with CAC reader and network connectivity to MSS
- Printed or digital copy of the relevant TM (provided by C2DAO before course)
- Printed course syllabus
- Note-taking materials
- For TM-40L: personal laptop configured per the pre-course checklist (external IDE permitted and recommended)

---

## SECTION 4 — ACADEMIC POLICIES

### 4-1. Attendance

Attendance at all scheduled blocks is required. A trainee who misses more than **10% of scheduled instructional hours** may be administratively withdrawn and rescheduled.

| Course | Max Missed Hours (10% threshold) |
|---|---|
| TM-10 (8 hrs) | 0 hours — no absences permitted for a 1-day course |
| TM-20 (40 hrs) | 4 hours |
| TM-30 (40 hrs) | 4 hours |
| TM-40G/H/I/L (40 hrs) | 4 hours |
| TM-40J/K (24 hrs) | 2.4 hours (effectively 0 — contact C2DAO if you must miss any time) |

An absence does not excuse a trainee from evaluation. Missed instruction that covers evaluated tasks places the full burden of self-remediation on the trainee.

**No absence from TM-40H Block 1 (AI Safety Seminar) is permitted under any circumstances.** This block cannot be made up independently. A trainee who misses it must attend TM-40H at a future iteration.

### 4-2. Tardiness

More than 15 minutes late to any block counts as an absence for that block. Three or more instances of tardiness is grounds for administrative withdrawal.

### 4-3. Make-Up Policy

If a trainee misses instruction due to a documented duty requirement (exercise, assigned mission, medical):
1. Notify the instructor and unit Training NCO on the same duty day
2. Instructor identifies whether the missed block covers evaluated tasks
3. Trainee completes self-study of the missed material using the relevant TM and lesson plan outline
4. Instructor determines whether a make-up lab is feasible within the course timeline

Make-up labs are not automatically provided — they are at instructor discretion and subject to training environment availability.

### 4-4. Academic Integrity

MSS evaluations are individual assessments. During all evaluated practical exercises:
- **No assistance from other trainees**
- **No access to the internet**, other training resources, or completed examples from prior trainees
- Reference to the relevant TM and course syllabus is **permitted** (open-book)
- Reference to instructor-provided reference cards is **permitted**
- The evaluator may ask the trainee to explain design decisions — this is a standard evaluation procedure

Violation of academic integrity standards results in automatic No-Go and is reported to the trainee's commander.

### 4-5. Conduct

Trainees are expected to:
- Actively engage with labs and discussions
- Ask questions when lost — passive watching is the most common cause of failed evaluations
- Support other trainees' learning (but not during evaluations)
- Comply with all MSS Training Environment access controls — do not access data, projects, or tools outside the scope of the current lab

---

## SECTION 5 — EVALUATION AND GO/NO-GO STANDARDS

### 5-1. How Evaluations Work

Each course ends with a practical exercise. The evaluation:
- Is conducted in the MSS Training Environment
- Uses scenario materials provided by the instructor at the start of the evaluation period
- Is Go/No-Go — no partial credit; each task either meets standard or it does not
- Is open TM — trainees may reference the relevant TM and course syllabus
- Requires tasks to be completed **independently** — the evaluator observes but does not assist

The evaluator may ask questions during the evaluation to verify understanding. These questions are part of the evaluation.

### 5-2. Go Standard

A trainee receives **Go** when:
1. All evaluated tasks are completed to standard without instructor assistance
2. No hard No-Go items are violated (see Section 5-3)
3. The minimum task threshold is met (see course syllabus — typically all tasks, or a stated minimum)

### 5-3. No-Go Standard

A trainee receives **No-Go** when:
1. A hard No-Go item is violated (automatic No-Go; remaining tasks still evaluated for feedback)
2. The minimum task threshold is not met within the allotted evaluation time
3. The trainee requests instructor assistance during the evaluation (automatically fails that task)

**Hard No-Go items result in automatic No-Go regardless of all other performance.** See POI Chapter 5 for the full hard No-Go item list.

### 5-4. Evaluation Time

The evaluator does not extend the evaluation period. If time runs out before all tasks are completed, uncompleted tasks are marked No-Go.

### 5-5. Evaluation Documentation

The evaluator documents the evaluation outcome on the Individual Training Record (Appendix B). Results are provided to the trainee and recorded in the Unit Training Status Matrix within 2 duty days.

---

## SECTION 6 — NO-GO AND REMEDIATION POLICY

### 6-1. Receiving a No-Go

A No-Go is not a permanent record of failure — it is a signal that more training time is required before the trainee is certified. An MSS product built by a trainee who cannot independently meet the standard creates data quality and governance risk for the unit.

### 6-2. Immediate Actions on No-Go

Within 1 duty day of a No-Go result:
1. Evaluator provides written debrief identifying each failed task and reason for No-Go
2. Instructor and trainee complete counseling documenting: failed tasks, recommended remediation plan, re-evaluation date
3. Unit Training NCO is notified
4. For TM-40G/H/I/L: trainee's commander is notified

### 6-3. Remediation Training Requirements

| Course | Minimum Remediation Hours | Method |
|---|---|---|
| TM-10 | 2 hours | Self-study with TM + supervised lab with instructor |
| TM-20, TM-40J, TM-40K | 4 hours | Supervised lab on failed tasks; build from scratch on a different dataset |
| TM-30, TM-40G, TM-40H, TM-40I, TM-40L | 8 hours | Full-day supervised lab; rebuilding failed components |

Remediation focuses on failed tasks. The re-evaluation covers all course tasks — not just previously failed ones.

### 6-4. Re-Evaluation

Re-evaluation uses a different practical exercise scenario (different dataset and scenario context) but the same task structure. The trainee demonstrates the same competencies, not the prior scenario from memory.

Re-evaluation is scheduled within **10 duty days** of the No-Go result. Extensions require C2DAO approval.

### 6-5. Second No-Go

A trainee who receives No-Go on both initial and first re-evaluation requires:
1. Written request from the trainee's commander to C2DAO Training POC
2. C2DAO review and approval before scheduling
3. Additional remediation as directed by C2DAO (typically requires re-attending a future course iteration)

A second No-Go typically indicates a prerequisite gap, not a performance issue. C2DAO will assess whether the prerequisite progression was appropriate.

### 6-6. No-Go Record

No-Go results, remediation completion, and re-evaluation results are all documented on the Individual Training Record. A trainee who received No-Go once and passed re-evaluation is certified to the same standard as one who passed on the first attempt.

---

## SECTION 7 — SYSTEM ACCESS AND EQUIPMENT REQUIREMENTS

### 7-1. Standard Access Levels

| Access Level | Description | Who Provisions | Lead Time |
|---|---|---|---|
| Viewer (TM-10) | View data, dashboards, Workshop apps, Contour, Quiver, AIP; cannot build or modify | Unit MSS Administrator | 5 duty days |
| Builder (TM-20, 40A–F WFF, 40J, 40K) | Create projects, ingest data, build pipelines, Object Types, Actions, Workshop apps | Unit MSS Administrator | 5 duty days |
| Editor (TM-30) | Edit and promote production data products; includes Builder capabilities | Unit MSS Administrator | 7 duty days |
| AIP Logic Configuration (TM-30, 40K) | Configure AIP Logic workflows; cannot author | C2DAO or designated admin | 7 duty days |
| AIP Logic Authoring (TM-40H) | Author and modify AIP Logic workflows | C2DAO only | 7–10 duty days |
| Agent Studio (TM-40H) | Configure and test Agent Studio agents | C2DAO only | 7–10 duty days |
| Code Workspace (TM-40G) | CPU-allocated Code Workspace for Python/R analysis | C2DAO only | 7–10 duty days |
| GPU Code Workspace (TM-40I) | GPU-enabled Code Workspace for model training | C2DAO only | 10+ duty days |
| OSDK Developer (TM-40L) | OSDK developer token; access to specific Object Types for development | C2DAO only | 10+ duty days |

### 7-2. Access Troubleshooting

| Symptom | Diagnosis | Action |
|---|---|---|
| Permission denied / 403 error | Wrong access level | Contact unit MSS Administrator. Not a C2DAO issue for standard access. |
| Cannot create project / no Create button | Viewer access, not Builder | Request Builder access from unit MSS Administrator. Allow 5 duty days. |
| AIP Logic / Code Workspace not appearing | Elevated access not provisioned | Contact C2DAO Training POC. |
| Login fails entirely (not 403) | CAC issue or PIV PIN problem | Contact G6/S6 or unit IT support — not an MSS issue. |
| Test account cannot see Workshop application | Application visibility settings incorrect | See TM-20 Chapter 6. Fix before the evaluation. |

### 7-3. Lost or Compromised Credentials

If you believe your MSS account credentials have been compromised, or if you observe another user accessing accounts or data without authorization, immediately notify your unit MSS Administrator and C2DAO. Do not investigate independently.

---

## SECTION 8 — DATA HANDLING AND CLASSIFICATION

### 8-1. Training Environment Data

Training data is synthetic. However, trainees must apply the same classification habits in the Training Environment as they would in production. If you are uncertain whether a dataset is synthetic or operational, treat it as operational until confirmed.

### 8-2. Classification Markings

All MSS data products must carry classification markings. In the Training Environment, all provided datasets are UNCLASSIFIED. Trainees must:
- Confirm the marking of any dataset before using it in a lab or exercise
- Apply the correct marking to any product they build
- Not export or save data from the Training Environment outside of approved local development directories

### 8-3. Export Controls

Exporting data to external storage, emailing datasets, or saving to personal cloud storage is prohibited — even in the Training Environment. Use the MSS export procedure to a designated training output location.

### 8-4. Sensitive Architecture Details

Do not include system architecture specifics (Foundry endpoint URLs, dataset paths, API keys, token values) in commit messages, screenshots, or communications outside the training environment.

---

## SECTION 9 — STUDENT RIGHTS AND RESPONSIBILITIES

### 9-1. Trainee Rights

- Receive a pre-course syllabus and required reading list at least 5 duty days before training
- Receive a written debrief of any No-Go evaluation within 1 duty day
- Request a review of an evaluation outcome within 3 duty days of receiving results — submit a written request to C2DAO Training POC
- Expect a training environment that functions correctly; access or equipment issues documented by the instructor are not counted against the trainee

### 9-2. Trainee Responsibilities

- Complete pre-course reading before Day 1
- Arrive with required access confirmed and working
- Actively participate in labs and discussions
- Complete evening reading assignments
- Flag access or environment issues to the instructor on the same day they occur
- Maintain data discipline: correct classification, no export of training data outside approved locations, no sharing of other trainees' work during evaluations

### 9-3. Complaints and Concerns

1. First: attempt to resolve with the instructor directly
2. If unresolved: submit a written complaint to C2DAO Training POC within 5 duty days
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
TM-30 Go Date:           _________ (required for TM-40G/H/I/L)

TECHNICAL PREREQUISITES (TM-40 specialist tracks only)
[ ] Code Workspace provisioned and test script passing (TM-40G/I)
[ ] AIP Logic authoring access confirmed (TM-40H)
[ ] GPU Code Workspace provisioned and test script passing (TM-40I)
[ ] OSDK developer token active (TM-40L)

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

TM-40 WFF TRACK (circle):         40A  40B  40C  40D  40E  40F
TM-40 SPECIALIST TRACK (circle):  40G  40H  40I  40J  40K  40L
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
