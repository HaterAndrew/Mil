# ENROLLMENT STANDARD OPERATING PROCEDURE
## Maven Smart System (MSS) Training Program
### USAREUR-AF Operational Data Team — C2DAO

---

| | |
|---|---|
| **Document** | Enrollment SOP |
| **Proponent** | USAREUR-AF C2DAO Training Division |
| **Effective Date** | March 2026 |
| **Applies To** | Unit Training NCOs/Officers, MSS Administrators, Trainees, C2DAO Training Staff |

---

## OVERVIEW

The enrollment process has five phases:

```
1. IDENTIFY → 2. REQUEST → 3. PROVISION → 4. CONFIRM → 5. COMPLETE
(Unit)          (Unit TNG)    (MSS Admin)    (C2DAO)       (C2DAO)
```

Total lead time for most courses: **10–35 duty days before Day 1**, depending on access requirements.

---

## PHASE 1 — IDENTIFY TRAINING NEED

**Who:** Unit Commander, Unit Training NCO/Officer, or individual

**When:** As early as possible — use the minimum advance planning timelines in the Annual Training Schedule.

### Step 1: Determine Required Training Level

| Personnel Category | Required Training Level |
|---|---|
| All newly assigned USAREUR-AF personnel | TM-10 (complete within 30 days of assignment) |
| Personnel assigned to build/maintain data products | TM-20 (complete within 90 days of data assignment) |
| Unit data leads, data-adjacent specialists (17/25-series, S6/G6, G2/G9) | TM-30 (complete within 90 days of data-lead assignment) |
| ORSA analysts working on MSS | TM-40A |
| AI engineers building AIP workflows | TM-40B |
| ML engineers building/deploying models | TM-40C |
| Program managers and resource managers | TM-40D |
| Knowledge managers and KMOs | TM-40E |
| Software engineers building Foundry integrations | TM-40F |

### Step 2: Verify Prerequisites

Before submitting an enrollment request, verify that the trainee meets all prerequisites:

| Course | Prerequisites to Verify |
|---|---|
| TM-10 | None |
| TM-20 | TM-10 Go on file (check Individual Training Record) |
| TM-30 | TM-10 and TM-20 Go on file |
| TM-40A | TM-10, TM-20, TM-30 Go on file; graduate-level quantitative background; Python or R proficiency |
| TM-40B | TM-10, TM-20, TM-30 Go on file; Python proficiency; Data Literacy Technical Reference read |
| TM-40C | TM-10, TM-20, TM-30 Go on file; Python ML proficiency (pandas, scikit-learn, PyTorch) |
| TM-40D | TM-10, TM-20 Go on file |
| TM-40E | TM-10, TM-20 Go on file |
| TM-40F | TM-10, TM-20, TM-30 Go on file; TypeScript or Python proficiency; REST API familiarity |

**Do not submit an enrollment request for a trainee who does not meet prerequisites.** C2DAO will not confirm enrollment without verified prerequisites, and the trainee will be unable to complete the course.

### Step 3: Check Training Schedule

Identify the target course iteration from the Annual Training Schedule. Confirm dates do not conflict with known unit training events, deployment windows, or leave periods.

---

## PHASE 2 — SUBMIT ENROLLMENT REQUEST

**Who:** Unit Training NCO/Officer (submitter); MSS Administrator (coordinator)

**When:** At or before the enrollment deadline (T-10 to T-21 days depending on course — see Annual Training Schedule)

### Step 4: Complete the Enrollment Request Form

The Enrollment Request Form is in CAD Appendix A. Complete all fields:
- Trainee personal data (name, rank, unit, MOS, DSN, email)
- Requested course and preferred dates
- Prerequisites with verification dates (attach copies of Go evaluation records or training record extracts)
- Technical prerequisites (for TM-40 courses — confirm access provisioning status)
- Unit Training NCO/Officer signature

### Step 5: Submit to MSS Administrator

The Unit Training NCO/Officer submits the completed form to the unit MSS Administrator. The MSS Administrator reviews the form for completeness before forwarding to C2DAO.

**MSS Administrator review checklist:**
- [ ] All fields on the Enrollment Request Form completed
- [ ] Prerequisites verified and documentation attached
- [ ] For TM-30+: confirm if elevated access provisioning is already in place or needs to be initiated
- [ ] For TM-40 specialist tracks: confirm if technical prerequisites (Code Workspace, OSDK, etc.) are active or being requested concurrently

### Step 6: Forward to C2DAO Training POC

MSS Administrator forwards the complete package to the C2DAO Training POC via NIPR email or official messaging. Subject line format: `MSS ENROLLMENT REQUEST — [UNIT] — [COURSE] — [REQUESTED DATE]`

---

## PHASE 3 — ACCESS PROVISIONING

**Who:** MSS Administrator (standard access); C2DAO (elevated access)

**When:** Immediately upon initiating enrollment — do not wait for C2DAO seat confirmation before starting provisioning

### Step 7: Initiate Access Provisioning

The MSS Administrator initiates the access provisioning request based on the course requirements:

| Course | Access Level Required | Who Provisions | Minimum Lead Time |
|---|---|---|---|
| TM-10 | Viewer | Unit MSS Administrator | 5 duty days |
| TM-20, TM-40D, TM-40E | Builder | Unit MSS Administrator | 5 duty days |
| TM-30 | Editor + AIP Logic configuration | Unit MSS Admin (Editor); C2DAO (AIP Logic config) | 7 duty days |
| TM-40A | Code Workspace (CPU) | C2DAO only | 7–10 duty days |
| TM-40B | AIP Logic authoring + Agent Studio | C2DAO only | 7–10 duty days |
| TM-40C | GPU Code Workspace | C2DAO only | 10+ duty days |
| TM-40F | OSDK developer access + developer token | C2DAO only | 10+ duty days |

**IMPORTANT:** Access provisioning lead times are minimums. C2DAO provisioning depends on current queue depth and approval chain. For TM-40C (GPU workspace) and TM-40F (OSDK), start provisioning at least 5 weeks before Day 1.

### Step 8: Confirm Access Before Day 1

**This is a trainee responsibility, confirmed by the MSS Administrator.**

At T-3 duty days (3 duty days before Day 1):
- [ ] Trainee logs in to MSS Training Environment successfully
- [ ] Trainee confirms access level is correct (e.g., Builder access shows "Create" buttons)
- [ ] For TM-40A/C: trainee runs the provided test script; confirms it executes without error
- [ ] For TM-40B: trainee confirms AIP Logic authoring tab appears in the platform
- [ ] For TM-40F: trainee runs OSDK authentication test with their developer token

If access is NOT confirmed at T-3 days:
1. Trainee notifies MSS Administrator immediately
2. MSS Administrator contacts C2DAO Training POC with urgency flag
3. C2DAO attempts to resolve; if unresolvable before Day 1, the seat may be deferred to the next iteration

**Do not arrive at training expecting to resolve access issues on Day 1 morning.** C2DAO does not have a Day 1 IT support window. Unresolved access issues on Day 1 typically cannot be fixed same-day.

---

## PHASE 4 — C2DAO CONFIRMATION

**Who:** C2DAO Training POC

**When:** Within 5 duty days of receiving the enrollment request

### Step 9: C2DAO Reviews Enrollment Request

C2DAO reviews the enrollment package:
- Prerequisites verified against training records
- Seat availability in requested iteration confirmed
- Access provisioning status noted

### Step 10: C2DAO Issues Enrollment Confirmation

C2DAO issues an enrollment confirmation to the MSS Administrator and trainee via NIPR email. The confirmation includes:
- Trainee name and course
- Confirmed course dates and location
- Reporting instructions (time, room)
- Pre-course reading list
- Day-before checklist
- Any open access provisioning items that require trainee action

### Step 11: No-Seat / Waitlist Response

If no seat is available in the requested iteration:
- C2DAO notifies the MSS Administrator with the next available iteration date
- C2DAO adds the trainee to the waitlist for the requested iteration (in case of seat openings)
- Unit has 5 days to confirm acceptance of the next available date

---

## PHASE 5 — PRE-COURSE PREPARATION AND COURSE COMPLETION

**Who:** Trainee; Unit Training NCO/Officer

### Step 12: Trainee Completes Pre-Course Requirements

Upon receiving enrollment confirmation, the trainee:
- [ ] Reads the Day-before checklist in the CAD (Section 3-2)
- [ ] Completes pre-course reading assignments listed in the course syllabus (at minimum 5 duty days before Day 1)
- [ ] Confirms access is active at T-3 days
- [ ] Brings all required materials on Day 1

The unit Training NCO/Officer confirms pre-course requirements are complete at T-2 days.

### Step 13: Course Completion Documentation

Upon Go evaluation result:
1. Evaluator completes Individual Training Record (CAD Appendix B)
2. Evaluator signs and issues Completion Certificate to trainee
3. For TM-30 and above: C2DAO sends Commander Notification Letter within 3 duty days
4. C2DAO updates the Unit Training Status Matrix within 2 duty days
5. Trainee retains certificate; copy filed by unit Training NCO/Officer

Upon No-Go evaluation result:
1. Evaluator completes Individual Training Record (No-Go section)
2. Evaluator completes No-Go Remediation Form (CAD Appendix C)
3. Counseling conducted within 1 duty day (unit)
4. For TM-40 series: C2DAO sends Commander Notification Letter within 3 duty days
5. Remediation plan established; re-evaluation scheduled within 10 duty days

---

## ENROLLMENT TIMELINE SUMMARY

| Task | When | Who |
|---|---|---|
| Identify training need; check prerequisites | ASAP; at minimum T+lead time | Unit Commander/Training NCO |
| Initiate access provisioning | Immediately upon identifying enrollment | MSS Administrator |
| Complete Enrollment Request Form | T-21 to T-10 days (course-dependent) | Unit Training NCO |
| Submit request to C2DAO | T-21 to T-10 days | MSS Administrator |
| C2DAO confirms enrollment | Within 5 duty days of receipt | C2DAO Training POC |
| Trainee completes pre-course reading | T-5 days | Trainee |
| Confirm access active | T-3 days | Trainee + MSS Administrator |
| Complete Day-before checklist | Day before Day 1 | Trainee |
| Report for training | Day 1 NLT 15 min before start | Trainee |
| Evaluator documents result | Day of evaluation | Evaluator |
| C2DAO updates training records | Within 2 duty days of evaluation | C2DAO Training POC |
| Commander notification (TM-30+) | Within 3 duty days of evaluation | C2DAO Training POC |

---

## SPECIAL ENROLLMENT SITUATIONS

### Urgent Enrollment (Deployments / Short-Notice Requirements)

For urgent enrollment needs (e.g., imminent deployment, key personnel vacancy):
1. Unit Commander submits an urgent enrollment request directly to C2DAO Training POC via NIPR with justification
2. C2DAO will evaluate seat availability and access provisioning feasibility
3. If access cannot be provisioned in time, C2DAO will advise on the earliest feasible date

Note: urgent enrollment cannot override access provisioning lead times. A TM-40C enrollment with 2 weeks' notice cannot provision a GPU workspace in 2 weeks if the current lead time is 10+ days.

### Re-Enrollment After No-Go

A trainee re-enrolling after a No-Go result does not need to submit a new full enrollment request. The MSS Administrator notifies C2DAO Training POC of the re-evaluation date. Access remains active from the initial enrollment.

### Cancelled Enrollment

If a trainee cannot attend after enrollment is confirmed:
1. Notify C2DAO Training POC at least T-5 days to allow seat reallocation
2. Access provisioning for TM-30+ elevated access will be suspended until re-enrollment
3. Unit is responsible for the forfeited quota

### Command-Directed Training

In cases where C2DAO or higher headquarters directs unit-wide MSS training (e.g., new deployment requirement, system upgrade training), the enrollment process is initiated by C2DAO. C2DAO will coordinate with unit MSS Administrators on access provisioning and scheduling.

---

## FREQUENTLY ASKED QUESTIONS

**Q: My Soldier completed TM-10 at a previous assignment. Do they need to repeat it?**
A: No — TM-10 completion is a permanent certification. Verify the Go result is on file (request a transcript from C2DAO Training POC if the Individual Training Record is not available). Annual sustainment refresher is still required.

**Q: My Soldier has extensive Foundry experience from a contractor background. Can they waive TM-10?**
A: No. TM-10 is required for all USAREUR-AF personnel regardless of prior experience. The evaluation ensures they know USAREUR-AF classification procedures and data governance requirements — not just how to use the platform.

**Q: The trainee's access isn't working on Day 1. What happens?**
A: If the issue is a unit-side provisioning failure (access was never requested), the trainee will likely need to reschedule. If the issue is a C2DAO or platform-side issue (access was requested and confirmed but is not functioning), C2DAO will attempt to resolve — the training day is preserved if possible. Document the issue and notify C2DAO Training POC immediately.

**Q: Can a unit request a dedicated course iteration for their personnel only?**
A: Yes, if the minimum class size is met (see CAD Section 1-4). Submit a request to C2DAO Training POC with the proposed dates, course, and number of students. C2DAO will schedule if instructor and environment are available.

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*Enrollment SOP | Version 1.0 | March 2026*
