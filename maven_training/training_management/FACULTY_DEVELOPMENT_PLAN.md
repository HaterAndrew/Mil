# FACULTY DEVELOPMENT PLAN
## Maven Smart System (MSS) Training Program
### USAREUR-AF Operational Data Team — C2DAO

---

| | |
|---|---|
| **Document** | Faculty Development Plan (FDP) |
| **Proponent** | USAREUR-AF C2DAO Training Division |
| **Effective Date** | March 2026 |
| **Review Cycle** | Annual |

---

## SECTION 1 — PURPOSE AND SCOPE

### 1-1. Purpose

This plan establishes how MSS instructors are certified, maintained, and developed. It ensures that the training program's quality is consistent across all instructors and all iterations of each course. An MSS data product built by a trainee is only as good as the instruction they received. Instructor quality directly affects operational data quality across USAREUR-AF.

### 1-2. Scope

This plan applies to:
- All C2DAO staff who serve as primary instructors for any MSS course
- Adjunct instructors who deliver specific blocks of instruction
- Evaluators who conduct Go/No-Go evaluations (must be separately certified as evaluators)
- Subject matter experts who provide technical review and course currency updates

---

## SECTION 2 — INSTRUCTOR QUALIFICATION STANDARDS

### 2-1. Baseline Requirements by Course Level

All instructors must meet the following minimum qualifications before being assigned to teach any course:

| Course | Minimum Instructor Qualification | Domain Requirement |
|---|---|---|
| TM-10 | TM-20 Go on file; 90 days active MSS use | Foundry platform fundamentals |
| TM-20 | TM-30 Go on file; 6+ months Foundry build experience; has built at least 2 production data products | Pipelines, Ontology, Workshop |
| TM-30 | TM-40 (any track) Go on file or C2DAO SME designation; can conduct Ontology design critiques | Advanced pipeline, Ontology design, AIP Logic configuration |
| TM-40A (INT) | Intelligence professional (35-series preferred); TM-20 Go on file; MSS COP and CCIR experience | INT WFF functions, COP management, CCIR configuration |
| TM-40B (FIRES) | Fire support officer or NCO (FA preferred); TM-20 Go on file; MSS fires display experience | Fires WFF functions, targeting data, fire support coordination |
| TM-40C (M2) | Maneuver officer or NCO (infantry/armor preferred); TM-20 Go on file | M2 WFF functions, unit position tracking, route analysis |
| TM-40D (SUST) | Logistics officer or NCO (88/92-series preferred); TM-20 Go on file | Sustainment WFF functions, LOGSTAT, readiness data |
| TM-40E (PROT) | Force protection officer or CBRN officer; TM-20 Go on file | Protection WFF functions, force protection CCIRs, PERSTAT |
| TM-40F (MC) | Operations officer or XO (O-4 or above preferred); TM-20 Go on file | Mission command WFF, BUA products, synchronization matrices |
| TM-40G | FA49 officer, ORSA-designated civilian, or equivalent quantitative background; TM-40G Go on file or C2DAO ORSA SME designation | Statistical modeling, time series, Monte Carlo, LP |
| TM-40H | AIP Logic authoring experience (minimum 3 production workflows deployed); C2DAO AI SME designation; TM-40H Go on file | AIP Logic, Agent Studio, RAG, AI safety |
| TM-40I | ML model deployed to production (minimum 1); TM-40I Go on file; C2DAO MLE SME designation | Feature engineering, model training, MLOps, governance |
| TM-40J | Program management background (PM-certified preferred); TM-30 Go on file; GFEBS/IMS proficiency | IMS, GFEBS, dashboard standards |
| TM-40K | Knowledge management background (CKM or equivalent preferred); TM-30 Go on file | KM systems, AIP summarization, PCS continuity |
| TM-40L | Software engineering background; OSDK/Platform SDK production experience; TM-40L Go on file | OSDK, Platform SDK, TypeScript FOO, Slate, security |

### 2-2. Evaluator Certification

Evaluators (instructors who conduct Go/No-Go evaluations) must hold a higher certification level than the course they evaluate:

| Evaluator for Course | Minimum Evaluator Certification |
|---|---|
| TM-10 | TM-20 certified instructor |
| TM-20 | TM-30 certified instructor |
| TM-30 | TM-40 (any track) certified instructor |
| TM-40A (INT) | INT professional (35-series preferred); MSS COP/CCIR proficiency |
| TM-40B (FIRES) | Fire support professional (FA preferred); MSS fires display proficiency |
| TM-40C (M2) | Maneuver officer or NCO; MSS position tracking proficiency |
| TM-40D (SUST) | Logistics professional (88/92-series preferred); MSS LOGSTAT proficiency |
| TM-40E (PROT) | Force protection or CBRN officer; MSS CCIR/PERSTAT proficiency |
| TM-40F (MC) | Operations officer; MSS BUA/synchronization product proficiency |
| TM-40G | FA49 or equivalent; C2DAO ORSA SME designation |
| TM-40H | C2DAO AI SME; has deployed at least 3 production AIP workflows |
| TM-40I | MLE with production deployment experience; C2DAO MLE SME designation |
| TM-40J | PM background; has delivered production PM dashboards on MSS |
| TM-40K | KM background; C2DAO-designated KM evaluator |
| TM-40L | Senior SWE; OSDK/Slate production experience; security review background |

---

## SECTION 3 — INSTRUCTOR CERTIFICATION PROCESS

### 3-1. Initial Certification Path

New instructors complete the following sequence before being permitted to teach independently:

**Phase 1: Audit (2 full course iterations as student-observer)**
- Attend the target course as an observer — not a student, not an assistant. Observe instruction, lab dynamics, and evaluation procedures.
- Complete the Observer Checklist after each iteration (Appendix A).
- Debrief with the lead instructor after each day.

**Phase 2: Assistant Instructor (1 full course iteration)**
- Deliver at least 40% of the blocks of instruction, supervised by the lead instructor.
- The lead instructor is present in the room throughout.
- Receive written feedback from the lead instructor after each day.
- Complete a self-assessment after the course iteration.

**Phase 3: Lead Instructor (Observed)**
- Deliver the complete course independently.
- C2DAO Training OIC or designated senior instructor observes at least 2 blocks per day.
- Evaluator certification requires separate observation of at least 1 complete evaluation.
- Receive a formal Instructor Observation Report (Appendix B) after the course.

**Phase 4: Certification**
- Upon completion of Phase 3 with a satisfactory observation report:
  - C2DAO Training OIC issues instructor certification in writing.
  - Certification is entered in the Instructor Roster (Appendix C).
  - Certified instructor may now teach independently and conduct evaluations (if evaluator-certified).

### 3-2. Cross-Certification (Adding Courses)

An instructor certified for one course level may be cross-certified for an adjacent level by completing:
- Phase 1 (Audit): 1 course iteration (reduced from 2)
- Phase 2 (Assistant): 1 course iteration
- Phase 3 (Lead, Observed): 1 course iteration

An instructor certified for TM-30 who wishes to teach TM-40J or TM-40K may use the cross-certification path if they have the domain background requirement. Instructors teaching WFF tracks (TM-40A–F) require functional domain expertise (INT, FIRES, M2, SUST, PROT, or MC) in addition to TM-30 certification — the cross-certification path applies to all TM-40 instructors.

---

## SECTION 4 — INSTRUCTOR SUSTAINMENT REQUIREMENTS

### 4-1. Annual Requirements

All certified instructors must complete the following annually to maintain certification:

| Requirement | Frequency | Description |
|---|---|---|
| Platform Currency | Continuous | Instructors must actively use the MSS platform — at minimum, complete one build exercise per quarter. Instructors who have not used the platform in 90+ days must complete a re-familiarization lab before teaching. |
| Annual Observation | Annual | C2DAO Training OIC or designated evaluator observes at least 2 blocks of instruction per course the instructor teaches annually. |
| Annual Observation Report | Annual | Written feedback on observed blocks; documented in instructor file. |
| New Feature Familiarization | Per platform release | Within 30 days of a major Foundry platform update, instructors must complete the new feature familiarization training before delivering blocks covering updated features. |
| Instructor Professional Development | Semi-annual | C2DAO-led instructor development session (April, October). Topics: training methodology, course currency review, emerging Foundry features, evaluation standardization. |

### 4-2. Lapse of Certification

An instructor who has not taught in more than **12 months** must complete:
- Re-familiarization lab (minimum 4 hours) with the C2DAO Training OIC
- One observed block of instruction before teaching independently

An instructor who has not used the MSS platform in more than **90 days** must:
- Complete the relevant build exercise before next teaching assignment
- Notify the C2DAO Training OIC so re-familiarization can be scheduled

---

## SECTION 5 — PROFESSIONAL DEVELOPMENT PROGRAM

### 5-1. Semi-Annual Instructor PD Sessions

C2DAO conducts instructor professional development sessions semi-annually (April and October).

**Session Structure (4 hours):**

| Block | Topic | Duration |
|---|---|---|
| 1 | Course Currency Review: what changed in the platform since last session; what needs to be updated in lessons | 1 hour |
| 2 | Training Methodology: one focused topic per session (adult learning principles, lab facilitation, check-on-learning techniques, evaluation standardization) | 1 hour |
| 3 | Evaluation Standardization: review of T&EO scoring from recent evaluations; calibration of GO/NO-GO decisions across instructors | 1 hour |
| 4 | Case Studies: review of common trainee errors and instructor interventions from recent iterations; identify curriculum gaps | 1 hour |

Attendance is mandatory for all certified instructors. Instructors who miss a session must complete a make-up review with the Training OIC within 30 days.

### 5-2. Lesson Improvement Process

Instructors are expected to continuously improve lesson content. The improvement cycle:

1. **During delivery:** Note any lesson weakness (confusing explanation, missing example, lab step that consistently fails). Record in the Lesson Improvement Log (Appendix D).
2. **After each course iteration:** Review lesson improvement notes; draft revisions.
3. **Before next iteration:** Submit proposed lesson revisions to C2DAO Training OIC for review.
4. **Approved revisions:** Incorporated into lesson plans; version history updated.

Lesson plans must be reviewed and updated at minimum annually, or within 30 days of any Foundry platform update affecting covered content.

### 5-3. Guest Instructors and SME Blocks

For specialist content requiring domain expertise not held by C2DAO staff (e.g., FA49 ORSA evaluators for TM-40G commander brief evaluation, security specialists for TM-40L security block), C2DAO may designate Guest Instructors who:
- Hold the relevant domain qualification
- Are briefed by C2DAO Training OIC on course standards and evaluation criteria before their block
- Receive an orientation to the T&EOs for any blocks they evaluate
- Submit a block assessment after delivery

Guest Instructors are not independently certified MSS instructors — they deliver specific blocks under C2DAO supervision.

---

## SECTION 6 — INSTRUCTOR PERFORMANCE STANDARDS

### 6-1. Instructor Observation Criteria

Instructors are evaluated on the following during observations:

| Criterion | Description |
|---|---|
| Technical Accuracy | Instruction is technically correct. Errors are corrected immediately; errors not noticed by the instructor are flagged in the observation report. |
| Instructional Clarity | Explanations are clear and appropriately paced. Concepts are reinforced with examples relevant to USAREUR-AF operational context. |
| Student Engagement | Students are actively engaged during labs. Instructor identifies and assists students who are lost. Dead time (students waiting, not working) is minimized. |
| Check on Learning | Instructor uses effective check-on-learning questions throughout each block. Questions require more than yes/no. |
| Lab Management | Labs proceed on schedule. Instructor manages common errors efficiently without solving every student's problem for them. |
| Evaluation Fidelity | Evaluations follow T&EO procedures. Evaluator does not assist during evaluation periods. GO/NO-GO decisions are documented. |
| Course Materials Currency | Lesson plan is current; slides reference correct platform version. |

### 6-2. Unsatisfactory Performance

An instructor who receives an unsatisfactory observation report on 2+ criteria will:
1. Receive a written improvement plan within 5 duty days
2. Be placed in Phase 2 (supervised delivery) for the next course iteration
3. Be re-observed after that iteration

An instructor who receives unsatisfactory performance on the same criteria after the improvement period will have their certification reviewed by the C2DAO Training OIC. Certification may be suspended pending additional training.

---

## SECTION 7 — INSTRUCTOR ROSTER AND RECORDS

### 7-1. Instructor Roster

C2DAO maintains a current instructor roster documenting:
- Name, rank/grade
- Courses certified to teach (with certification date)
- Evaluator certification (yes/no; courses)
- Most recent observation date and result
- Platform currency status
- Guest instructor designations

The roster is reviewed monthly by the C2DAO Training OIC and updated within 5 duty days of any certification event.

### 7-2. Instructor File Contents

Each instructor's file contains:
- Certification documentation (Phase 3 observation report; certification letter)
- Annual observation reports (last 3 years)
- Platform currency attestations
- PD session attendance records
- Lesson Improvement Log submissions
- Any performance improvement documentation

---

## APPENDIX A — INSTRUCTOR OBSERVER CHECKLIST

```
=========================================================
MSS INSTRUCTOR OBSERVATION — OBSERVER CHECKLIST
(Phase 1: Audit Observation)
=========================================================
Observer Name:       _______________________________________
Instructor Observed: _______________________________________
Course:              _______________________________________
Date:                _______________________________________
Blocks Observed:     _______________________________________
=========================================================

OBSERVATION NOTES (complete during/after each block):

Block ___ : ____________________________________________
  - What worked well in the instruction?
    __________________________________________________
  - What was confusing or unclear?
    __________________________________________________
  - What errors did students make? How did the instructor address them?
    __________________________________________________
  - What would you do differently?
    __________________________________________________

Block ___ : ____________________________________________
  (repeat for each block observed)

OVERALL DEBRIEF NOTES (complete with lead instructor after course):
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________

Observer Signature: ___________________________________
Lead Instructor Signature: ____________________________
=========================================================
```

---

## APPENDIX B — INSTRUCTOR OBSERVATION REPORT

```
=========================================================
MSS INSTRUCTOR OBSERVATION REPORT
(Phase 3 / Annual Observation)
=========================================================
Instructor:          _______________________________________
Course:              _______________________________________
Dates Observed:      _______________________________________
Observer:            _______________________________________
=========================================================

OBSERVATION CRITERIA RATINGS: S = Satisfactory | U = Unsatisfactory

Criterion                    | Rating | Notes
-----------------------------|--------|---------------------------
Technical Accuracy           |        |
Instructional Clarity        |        |
Student Engagement           |        |
Check on Learning            |        |
Lab Management               |        |
Evaluation Fidelity          |        | (if evaluation observed)
Course Materials Currency    |        |

OVERALL RATING:   [ ] Satisfactory   [ ] Unsatisfactory

STRENGTHS:
_____________________________________________________________

AREAS FOR IMPROVEMENT:
_____________________________________________________________

REQUIRED ACTIONS (if any):
_____________________________________________________________

CERTIFICATION RECOMMENDATION:
[ ] Certify / Maintain certification
[ ] Conditional — complete improvement plan
[ ] Suspend certification pending additional training

Observer Signature: ___________________________________
Observer Rank/Title: __________________________________
Date: ________________________________________________

Instructor Acknowledgment: ___________________________
Date: ________________________________________________
=========================================================
```

---

## APPENDIX C — INSTRUCTOR ROSTER (TEMPLATE)

```
=========================================================
C2DAO MSS INSTRUCTOR ROSTER
As of: _______________
=========================================================
Name | Courses Certified | Eval Cert | Last Observed | Platform Currency
-----|-------------------|-----------|---------------|------------------
     | TM-10, TM-20      | Yes (TM-10/20) | MM/YYYY | Current
     | TM-30, TM-40J     | Yes (TM-30)    | MM/YYYY | Current
     | TM-40H            | Yes (TM-40H)   | MM/YYYY | Current

GUEST INSTRUCTORS:
Name | Block(s) | Course | Qualification | Last Briefed
-----|----------|--------|---------------|-------------
     | ORSA Brief Eval | TM-40G | FA49 | MM/YYYY

Roster Maintained By: ____________________________
Last Updated: ____________________________________
=========================================================
```

---

## APPENDIX D — LESSON IMPROVEMENT LOG

```
=========================================================
LESSON IMPROVEMENT LOG
=========================================================
Instructor:    _______________________________________
Course:        _______________________________________
Iteration:     _______________________________________

LESSON IMPROVEMENT NOTES

Block # | Issue Observed | Proposed Change | Priority
--------|----------------|-----------------|--------
        |                |                 | H/M/L
        |                |                 | H/M/L
        |                |                 | H/M/L

SUBMITTED TO C2DAO TRAINING OIC: _____________________
REVIEW DECISION: [ ] Approved [ ] Revised [ ] Declined
INCORPORATED IN LESSON PLAN VERSION: ________________
=========================================================
```

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*Faculty Development Plan | Version 1.0 | March 2026*
