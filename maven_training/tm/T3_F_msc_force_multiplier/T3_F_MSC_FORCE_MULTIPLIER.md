# T3-F — MSC FORCE MULTIPLIER · MAVEN SMART SYSTEM (MSS)

> **BLUF:** T3-F trains MSC-level personnel to sustain MSS training locally. Graduates earn the Unit Data Trainer (UDT) designation and are authorized to deliver TM-10 independently, facilitate TM-20 refresher labs, proctor TM-10 exams, and report training status to C2DAO. T3-F does not replace C2DAO instructor certification — it creates a sustainment capability at the unit level.
> **Prereqs:** TM-20, Builder (Go on file); unit commander nomination; CONCEPTS_GUIDE_T3F_MSC_FORCE_MULTIPLIER (read before this manual).
> *HQ USAREUR-AF · v1.0 · 2026 · DISTRIB: USG only · AUTH: C2DAO/UDRA v1.1*

> **WARNING:** Unit Data Trainers are the MSS training program's forward presence at the MSC level. The quality of TM-10 training delivered by a UDT directly affects how 80%+ of USAREUR-AF personnel experience the MSS platform for the first time.

---

## CHAPTER 1 — INTRODUCTION: THE UNIT DATA TRAINER

### 1-1. Purpose and Scope

**BLUF:** T3-F exists because C2DAO cannot be everywhere. USAREUR-AF is distributed across Europe. The MTT rotates through MSCs quarterly, but personnel turnover, new arrivals, and ongoing readiness requirements create continuous demand for TM-10 (Maven User) training between visits. UDTs fill that gap.

This manual is the reference for the T3-F course. It covers everything a UDT candidate needs to understand the training materials, deliver TM-10, evaluate trainees, troubleshoot common issues, and report status to C2DAO.

**T3-F covers:**

- How to use the TM-10 training materials (lesson plans, slides, exercises, exams, T&EOs)
- How to deliver each TM-10 block of instruction using provided lesson plans
- How to administer and score TM-10 pre-tests and post-tests
- How to conduct TM-10 Go/No-Go evaluations using T&EO scoring sheets
- How to facilitate TM-20 refresher lab sessions (Blocks 1-10 only)
- How to troubleshoot the 5 most common MSS access and environment issues
- How to report training completion status to C2DAO
- How to identify when a training need exceeds UDT authority and escalate

**T3-F does NOT cover:**

- Delivering TM-20 initial certification — requires C2DAO-certified instructor
- Delivering TM-30 or any TM-40/TM-50 course — beyond UDT scope
- Modifying curriculum, lesson plans, or evaluation criteria — curriculum authority resides with C2DAO
- Instructor certification for C2DAO-level courses — see T3-I (Instructor Certification)
- Advanced instructional methodology — T3-F includes abbreviated adult learning principles, not the full T3-I treatment

---

### 1-2. The Unit Data Trainer in the Training Ecosystem

```
C2DAO Training Division
  ├── MTT (quarterly rotation to MSCs)
  │     ├── Delivers TM-20, TM-30, TM-40 as scheduled
  │     ├── Delivers T3-F to nominated UDT candidates
  │     └── Observes existing UDTs, provides feedback
  │
  └── Certified Instructors (T3-I graduates)
        └── Deliver all TM courses per assignment

MSC / Unit Level
  └── Unit Data Trainer (T3-F graduate)
        ├── Delivers TM-10 to new arrivals between MTT visits
        ├── Facilitates TM-20 refresher labs (Blocks 1-10)
        ├── Proctors TM-10 exams for self-study/remote personnel
        └── Reports training status to C2DAO
```

The UDT is the MSS training program's forward presence. Without UDTs, new arrivals at geographically separated units wait until the next MTT rotation to receive TM-10 — potentially months without basic MSS qualification.

---

### 1-3. Prerequisites and Entry Standards

| Prerequisite | Requirement |
|---|---|
| TM-20 Go | On file with C2DAO. TM-20 ensures the candidate has Builder-level platform skills. |
| Commander Nomination | Unit commander signs nomination memorandum identifying the candidate and certifying the duty position requirement (see UDT SOP Appendix A for template). |
| Duty Position | Assigned to a billet or duty with training responsibilities: data NCO, S6 staff, unit data steward, or equivalent. |
| Platform Access | Active MSS account with Builder-level access. |
| Pre-Course Reading | CONCEPTS_GUIDE_T3F_MSC_FORCE_MULTIPLIER (complete before Day 1). |

---

### 1-4. Authorities and Limitations

See Instructor Tier Definitions §3-4 and Unit Data Trainer SOP §3 for the complete authority and limitation tables. Summary:

| Can Do | Cannot Do |
|---|---|
| Deliver TM-10 (all 9 blocks) | Deliver TM-20 initial certification |
| Administer TM-10 Go/No-Go evaluations | Deliver TM-30 or above |
| Proctor TM-10 pre/post exams (standalone) | Modify curriculum or evaluation criteria |
| Facilitate TM-20 refresher labs (Blocks 1-10) | Grant enrollment exceptions |
| Report training status to C2DAO | Certify other instructors or UDTs |
| Troubleshoot 5 common environment issues | Provision MSS accounts |

---

## CHAPTER 2 — THE TM-10 TRAINING MATERIALS

### 2-1. Document Set

The TM-10 course is fully documented. The UDT does not design instruction — the UDT delivers published materials.

| Document | Location | Purpose |
|---|---|---|
| TM-10 Course Content | `tm/TM_10_maven_user/TM_10_MAVEN_USER.md` | Primary reference; student reading material |
| TM-10 Lesson Plans | `training_management/lesson_plans/TM10/TM10_LESSON_PLANS.md` | Block-by-block delivery guide with instructor notes, student activities, check-on-learning questions |
| TM-10 Syllabus | `syllabi/SYLLABUS_TM10.md` | Schedule, learning objectives, assessment criteria |
| TM-10 Exercise | `exercises/EX_10_operator_basics/EXERCISE.md` | Practical exercise task list with Go/No-Go criteria |
| TM-10 Pre-Test | `exercises/exams/EXAM_TM10_PRE.md` | Diagnostic exam (Day 1 morning) |
| TM-10 Post-Test | `exercises/exams/EXAM_TM10_POST.md` | Knowledge check (end of course) |
| TM-10 T&EOs | `training_management/TEO_MSS.md` (Part I) | Go/No-Go performance measures and standards |

### 2-2. How to Use the Lesson Plans

Each TM-10 lesson plan block contains:

| Section | What It Tells You |
|---|---|
| **Purpose** | Why this block exists — read this aloud or paraphrase at the start of the block |
| **TLO / ELOs** | What the trainee must be able to do after the block — these are your success criteria |
| **Instructor Notes** | What to demonstrate, what to emphasize, what to skip if time is short |
| **Student Activity** | What the trainee does hands-on during the block |
| **Check-on-Learning** | Questions to verify comprehension before moving to the next block — use these, do not skip them |
| **Common Errors** | Errors trainees frequently make during this block and how to address them |

**Delivery rule:** Follow the lesson plan. The lesson plan was written by experienced instructors and reviewed by C2DAO. If you believe a lesson plan has an error or gap, deliver it as written and submit a note to C2DAO after the course iteration.

### 2-3. Printing and Materials Preparation

Before each TM-10 iteration:
- Print the student handout (TM-10 task reference — abbreviated version, not the full TM)
- Print pre-test and post-test packets (student versions — **do not print the answer key for distribution**)
- Print T&EO scoring sheets (1 per student)
- Secure the answer key in your instructor binder — do not leave it accessible to students

---

## CHAPTER 3 — DELIVERING TM-10

### 3-1. Before Day 1

Execute the pre-course checklist (UDT SOP §4-4):
- Verify all enrolled students have active MSS accounts with Viewer access
- Test-login from classroom workstations
- Notify C2DAO of planned iteration (date, student count, location)
- Review lesson plans for currency

### 3-2. Course Flow

TM-10 is a 1-day course with 9 blocks:

| Block | Topic | Method | Duration |
|---|---|---|---|
| — | Course overview, admin, pre-test | BRF | 30 min |
| 1 | What is MSS and why it matters | LEC | 30 min |
| 2 | Navigating the MSS environment | LAB | 60 min |
| 3 | Finding and viewing data | LAB | 60 min |
| — | Lunch | — | 60 min |
| 4 | Understanding dashboards and reports | LAB | 45 min |
| 5 | Basic data interpretation | LAB | 45 min |
| 6 | Classification and export rules | LEC/LAB | 30 min |
| 7 | Requesting help and reporting issues | DIS | 15 min |
| 8 | Practical exercise | EVAL | 60 min |
| 9 | Post-test, AAR, closeout | BRF | 30 min |

### 3-3. Key Delivery Points

**Block 1 — Operational context:** Do not read slides. Tell the class why MSS matters to their unit. Use local examples if possible (e.g., "Your unit's readiness dashboard runs on MSS — here's what it looks like").

**Block 2 — Navigation:** This is where students get lost. Circulate continuously. Verify every student has logged in successfully within the first 5 minutes. If anyone cannot log in, troubleshoot immediately — do not proceed with the class while a student is locked out.

**Block 6 — Classification:** This is the most consequential block. An incorrect classification marking on an export is a security violation. Ensure every student can correctly identify the classification of data before allowing them to attempt the export exercise. This is a hard No-Go item on the T&EO.

**Block 8 — Practical exercise:** Switch to evaluator mode. Announce clearly: "From this point I cannot provide assistance. You may use your task reference and notes." Do not help. Do not hint. Score each performance measure on the T&EO scoring sheet.

---

## CHAPTER 4 — EVALUATION AND GO/NO-GO

### 4-1. T&EO Scoring

Each TM-10 T&EO contains performance measures. Score each measure Go or No-Go based on observed performance:

| Score | Meaning |
|---|---|
| **Go** | The trainee performed the task to standard without assistance |
| **No-Go** | The trainee did not perform the task to standard, required assistance, or did not attempt the task |

### 4-2. Critical Items

Some performance measures are marked **Critical** in the T&EO. Failure on any critical item is automatic No-Go for the entire task, regardless of performance on other measures.

**TM-10 critical items include:**
- Correct classification marking on export (TM10-06)
- Does not navigate to production environment during any exercise

### 4-3. Overall Go/No-Go Decision

The overall Go/No-Go for TM-10 is determined by:
- Go on all critical items (mandatory)
- Go on the required number of total performance measures (per T&EO — typically 4 of 5 non-critical items)

### 4-4. No-Go Procedures

If a student receives No-Go:
1. Inform the student same-day, privately if possible
2. Identify exactly which performance measures were not met
3. Document the No-Go on the T&EO scoring sheet
4. Coordinate with the unit training NCO for remediation scheduling
5. Report the No-Go to C2DAO within 24 hours (per UDT SOP §5-2)
6. Conduct remediation and re-evaluation within 10 duty days

### 4-5. Standalone Exam Proctoring

UDTs may proctor TM-10 pre-tests and post-tests as a standalone activity for personnel who completed TM-10 via self-study or remote instruction and need a formal evaluation.

**Procedures:**
- Verify the student has completed all TM-10 required reading
- Administer the post-test under standard conditions (30 minutes, closed book except task reference)
- Score using the answer key
- If the student meets the passing score, coordinate with C2DAO for Go/No-Go practical exercise scheduling (UDT administers if all T&EO materials are available; otherwise, defer to next MTT visit or C2DAO virtual evaluation)

---

## CHAPTER 5 — TROUBLESHOOTING

### 5-1. The 5 Common Issues

T3-F teaches UDTs to resolve these 5 environment issues without C2DAO support:

| # | Issue | Diagnosis | Resolution | Time Limit |
|---|---|---|---|---|
| 1 | **CAC auth failure** | Student sees authentication error after inserting CAC | Clear browser cache; re-insert CAC; try alternate browser; verify CAC certificate is not expired | 5 min |
| 2 | **Expired account** | Student sees "account inactive" or similar | Contact MSS Admin for reactivation; in the interim, pair the student with another student for observation (do not skip the student) | 10 min (initial); escalate if not resolved |
| 3 | **Wrong environment** | Student is viewing production data instead of training data | Redirect to training environment URL; verify and update bookmarks; announce correct URL to entire class | 2 min |
| 4 | **Missing project access** | Student can log in but cannot see the training project | Check project membership in MSS Admin panel (if UDT has access); otherwise, contact MSS Admin | 10 min |
| 5 | **Stale training data** | Training datasets show old dates or missing records | Re-run synthetic data loader if UDT has access; otherwise, teach around the stale data and report to C2DAO after course | 5 min (workaround); report after |

### 5-2. When to Escalate

Escalate to C2DAO when:
- The issue is not one of the 5 common issues listed above
- The resolution does not work within the time limit
- The issue affects 3+ students simultaneously (likely a systemic problem)
- The issue involves production data visibility from training accounts (potential security concern — escalate immediately)

---

## CHAPTER 6 — REPORTING

### 6-1. Unit Training Status Report

After each TM-10 iteration, submit the Unit Training Status Report to C2DAO (see UDT SOP §5-1 for format). Key fields:
- UDT name and unit
- Iteration dates
- Students enrolled / completed / Go / No-Go
- Pre-test and post-test mean scores
- Issues encountered

**Timeline:** Within 5 duty days of iteration completion.

### 6-2. TM-20 Refresher Facilitation

When facilitating TM-20 refresher labs (Blocks 1-10), report:
- Date, unit, number of participants
- Refresher topics covered
- Any recurring skill gaps observed

This reporting is informal (email to C2DAO Training Division) and helps C2DAO calibrate the need for additional TM-20 iterations.

---

## CHAPTER 7 — SUSTAINMENT

### 7-1. Staying Current

The MSS platform updates regularly. UDTs stay current by:
- Reviewing the training repository for lesson plan updates before each iteration
- Attending semi-annual C2DAO PD sessions (virtual OK)
- Maintaining active MSS platform use (Builder-level activities, not just Viewer)

### 7-2. Annual Re-Certification

C2DAO observes each UDT annually (virtual OK). The observation covers:
- At least 2 blocks of TM-10 instruction
- 1 Go/No-Go evaluation administration
- Review of training status reports for the preceding year

### 7-3. When You PCS or Change Duty

If you PCS, ETS, or change to a duty position without training responsibilities:
- Notify C2DAO and your unit training NCO
- Recommend a replacement candidate to your commander
- Transfer local knowledge (classroom setup, workstation configuration, unit-specific scheduling) to your replacement
- Your UDT designation will lapse; your replacement must complete T3-F independently

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*T3-F MSC Force Multiplier | Version 1.0 | March 2026*
