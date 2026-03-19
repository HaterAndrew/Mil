# ENROLLMENT STANDARD OPERATING PROCEDURE
## Maven Smart System (MSS) Training Program
### USAREUR-AF Operational Data Team — C2DAO

| | |
|---|---|
| **Document** | Enrollment SOP |
| **Proponent** | USAREUR-AF C2DAO Training Division |
| **Effective Date** | March 2026 |
| **Applies To** | Unit Training NCOs/Officers, MSS Administrators, Trainees, C2DAO Training Staff |

---

## OVERVIEW

```
1. IDENTIFY → 2. REQUEST → 3. PROVISION → 4. CONFIRM → 5. COMPLETE
(Unit)          (Unit TNG)    (MSS Admin)    (C2DAO)       (C2DAO)
```

Total lead time: **10–35 duty days before Day 1**, depending on access requirements.

---

## Authoritative References

| Publication | Title | Relevance |
|---|---|---|
| AR 350-1 | Army Training and Leader Development | Master regulation for Army training policy; governs enrollment procedures and training records |
| AR 350-10 | Management of Army Individual Training Requirements and Resources | Governs individual training seat management, resource allocation, and enrollment processes |

---

## PHASE 1 — IDENTIFY TRAINING NEED

**Who:** Unit Commander, Unit Training NCO/Officer, or individual

### Step 1: Determine Required Training Level

| Personnel Category | Required Training Level |
|---|---|
| All newly assigned USAREUR-AF personnel | TM-10 (complete within 30 days of assignment) |
| Personnel assigned to build/maintain data products | TM-20 (complete within 90 days of data assignment) |
| Unit data leads, data-adjacent specialists (17/25-series, S6/G6, G2) | TM-30 (complete within 90 days of data-lead assignment) |
| INT/FIRES/M2/SUST/PROT/MC functional staff | TM-40A through TM-40F (prereq: TM-30; 3 days each) |
| ORSA analysts working on MSS | TM-40G |
| AI engineers building AIP workflows | TM-40H |
| ML engineers building/deploying models | TM-40M |
| Program managers and resource managers | TM-40J |
| Knowledge managers and KMOs | TM-40K |
| Software engineers building Foundry integrations | TM-40L |

### Step 2: Verify Prerequisites

**Do not submit an enrollment request for a trainee who does not meet prerequisites.** C2DAO will not confirm enrollment without verified prerequisites.

| Course | Prerequisites to Verify |
|---|---|
| TM-10 | None |
| TM-20 | TM-10 Go on file |
| TM-30 | TM-10 and TM-20 Go on file |
| TM-40A through TM-40F (WFF tracks) | TM-10, TM-20, and TM-30 Go on file; WFF functional staff designation |
| TM-40G | TM-10, TM-20, TM-30 Go on file; graduate-level quantitative background; Python or R proficiency |
| TM-40H | TM-10, TM-20, TM-30 Go on file; Python proficiency; Data Literacy Technical Reference read |
| TM-40M | TM-10, TM-20, TM-30 Go on file; Python ML proficiency (pandas, scikit-learn, PyTorch) |
| TM-40J | TM-10, TM-20, TM-30 Go on file (all required) |
| TM-40K | TM-10, TM-20, TM-30 Go on file (all required) |
| TM-40L | TM-10, TM-20, TM-30 Go on file; TypeScript or Python proficiency; REST API familiarity |

### Step 3: Check Training Schedule

Identify the target course iteration from the Annual Training Schedule. Confirm dates do not conflict with known unit training events, deployment windows, or leave periods.

---

## PHASE 2 — SUBMIT ENROLLMENT REQUEST

**Who:** Unit Training NCO/Officer (submitter); MSS Administrator (coordinator)

**When:** At or before the enrollment deadline (T-10 to T-21 days depending on course)

### Step 4: Complete the Enrollment Request Form

The Enrollment Request Form is in CAD Appendix A. Complete all fields:
- Trainee personal data (name, rank, unit, MOS, DSN, email)
- Requested course and preferred dates
- Prerequisites with verification dates (attach Go evaluation records or training record extracts)
- Technical prerequisites (for TM-40 courses — confirm access provisioning status)
- Unit Training NCO/Officer signature

### Step 5: Submit to MSS Administrator

The Unit Training NCO/Officer submits to the unit MSS Administrator. The MSS Administrator reviews for completeness before forwarding to C2DAO.

**MSS Administrator review checklist:**
- [ ] All fields on the Enrollment Request Form completed
- [ ] Prerequisites verified and documentation attached
- [ ] For TM-30+: elevated access provisioning in place or being initiated
- [ ] For TM-40 specialist tracks (TM-40G through TM-40M): technical prerequisites (Code Workspace, OSDK, etc.) active or being requested concurrently

### Step 6: Forward to C2DAO Training POC

Via NIPR email or official messaging. Subject line format: `MSS ENROLLMENT REQUEST — [UNIT] — [COURSE] — [REQUESTED DATE]`

---

## PHASE 3 — ACCESS PROVISIONING

**Who:** MSS Administrator (standard access); C2DAO (elevated access)

**When:** Immediately upon initiating enrollment — do not wait for C2DAO seat confirmation before starting provisioning.

### Step 7: Initiate Access Provisioning

| Course | Access Level Required | Who Provisions | Minimum Lead Time |
|---|---|---|---|
| TM-10 | Viewer | Unit MSS Administrator | 5 duty days |
| TM-20, TM-40A–F (WFF), TM-40J, TM-40K | Builder | Unit MSS Administrator | 5 duty days |
| TM-30 | Editor + AIP Logic configuration | Unit MSS Admin (Editor); C2DAO (AIP Logic config) | 7 duty days |
| TM-40G | Code Workspace (CPU) | C2DAO only | 7–10 duty days |
| TM-40H | AIP Logic authoring + Agent Studio | C2DAO only | 7–10 duty days |
| TM-40M | GPU Code Workspace | C2DAO only | 10+ duty days |
| TM-40L | OSDK developer access + developer token | C2DAO only | 10+ duty days |

**IMPORTANT:** Lead times are minimums. For TM-40M (GPU workspace) and TM-40L (OSDK), start provisioning at least 5 weeks before Day 1.

### Step 8: Confirm Access Before Day 1

**This is a trainee responsibility, confirmed by the MSS Administrator.**

At T-3 duty days:
- [ ] Trainee logs in to MSS Training Environment successfully
- [ ] Trainee confirms access level is correct (Builder access shows "Create" buttons)
- [ ] For TM-40G/I: trainee runs the provided test script; confirms it executes without error
- [ ] For TM-40H: trainee confirms AIP Logic authoring tab appears
- [ ] For TM-40L: trainee runs OSDK authentication test with their developer token

If access is NOT confirmed at T-3:
1. Trainee notifies MSS Administrator immediately
2. MSS Administrator contacts C2DAO Training POC with urgency flag
3. If unresolvable before Day 1, the seat may be deferred to the next iteration

**Do not arrive at training expecting to resolve access issues on Day 1 morning.** C2DAO has no Day 1 IT support window. Unresolved access issues typically cannot be fixed same-day.

---

## PHASE 4 — C2DAO CONFIRMATION

**Who:** C2DAO Training POC | **When:** Within 5 duty days of receiving the enrollment request

### Step 9: C2DAO Reviews Enrollment Request

C2DAO reviews: prerequisites against training records, seat availability, access provisioning status.

### Step 10: C2DAO Issues Enrollment Confirmation

C2DAO issues confirmation via NIPR email to the MSS Administrator and trainee. The confirmation includes:
- Trainee name and course
- Confirmed course dates and location
- Reporting instructions (time, room)
- Pre-course reading list
- Day-before checklist
- Open access provisioning items requiring trainee action

### Step 11: No-Seat / Waitlist Response

If no seat is available:
- C2DAO notifies the MSS Administrator with the next available iteration date
- C2DAO adds the trainee to the waitlist for the requested iteration
- Unit has 5 days to confirm acceptance of the next available date

---

## PHASE 5 — PRE-COURSE PREPARATION AND COURSE COMPLETION

**Who:** Trainee; Unit Training NCO/Officer

### Step 12: Trainee Completes Pre-Course Requirements

Upon receiving enrollment confirmation:
- [ ] Read Day-before checklist in the CAD (Section 3-2)
- [ ] Complete pre-course reading assignments listed in the course syllabus (at minimum T-5 days before Day 1)
- [ ] Confirm access is active at T-3 days
- [ ] Bring all required materials on Day 1

The unit Training NCO/Officer confirms pre-course requirements are complete at T-2 days.

### Step 13: Course Completion Documentation

Upon Go evaluation result:
1. Evaluator completes Individual Training Record (CAD Appendix B)
2. Evaluator signs and issues Completion Certificate to trainee
3. For TM-30 and above: C2DAO sends Commander Notification Letter within 3 duty days
4. C2DAO updates Unit Training Status Matrix within 2 duty days
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

1. Unit Commander submits urgent enrollment request directly to C2DAO Training POC via NIPR with justification
2. C2DAO evaluates seat availability and access provisioning feasibility
3. If access cannot be provisioned in time, C2DAO advises on the earliest feasible date

**NOTE:** Urgent enrollment cannot override access provisioning lead times.

### Re-Enrollment After No-Go

A trainee re-enrolling after a No-Go does not need a new full enrollment request. The MSS Administrator notifies C2DAO Training POC of the re-evaluation date. Access remains active from the initial enrollment.

### Cancelled Enrollment

If a trainee cannot attend after confirmation:
1. Notify C2DAO Training POC at least T-5 days to allow seat reallocation
2. Elevated access (TM-30+) will be suspended until re-enrollment
3. Unit is responsible for the forfeited quota

### Command-Directed Training

When C2DAO or higher headquarters directs unit-wide MSS training, the enrollment process is initiated by C2DAO. C2DAO coordinates with unit MSS Administrators on access provisioning and scheduling.

---

## FREQUENTLY ASKED QUESTIONS

**Q: My Soldier completed TM-10 at a previous assignment. Do they need to repeat it?**
A: No — TM-10 completion is permanent. Verify the Go result is on file (request a transcript from C2DAO if the Individual Training Record is not available). Annual sustainment refresher is still required.

**Q: My Soldier has extensive Foundry experience from a contractor background. Can they waive TM-10?**
A: No. TM-10 is required for all USAREUR-AF personnel regardless of prior experience. The evaluation confirms USAREUR-AF classification procedures and data governance requirements — not just platform proficiency.

**Q: The trainee's access isn't working on Day 1. What happens?**
A: If the issue is a unit-side provisioning failure (access never requested), the trainee will likely need to reschedule. If the issue is C2DAO or platform-side (access was requested and confirmed but not functioning), C2DAO will attempt to resolve. Document the issue and notify C2DAO immediately.

**Q: Can a unit request a dedicated course iteration for their personnel only?**
A: Yes, if the minimum class size is met (see CAD Section 1-4). Submit a request to C2DAO Training POC with proposed dates, course, and number of students.

---

## BUILDER SPRINT (BSP) ENROLLMENT

The Builder Sprint is a separate quarterly event outside the TM-10 through TM-50 training chain. It has its own enrollment workflow. See BUILDER_SPRINT_SOP.md (BSP-SOP-001) for full procedures. Summary below.

### BSP Enrollment Summary

```
1. IDENTIFY   → 2. BRIEF      → 3. SUBMIT    → 4. VALIDATE  → 5. PROVISION → 6. CONFIRM
(Unit)           (Candidate)     (Unit TNG)     (C2DAO)        (MSS Admin)    (C2DAO)
```

**Key differences from TM course enrollment:**

| TM Course Enrollment | BSP Enrollment |
|---|---|
| Prereq: varies by course | Prereq: TM-20 Go on file — no exceptions |
| No project required | **Project Brief (CAD Appendix D) required** |
| Seat confirmed on prereq verification | Seat confirmed only after Project Brief approval |
| Access provisioned from standard access list | Sprint workspace provisioned per project list |

**BSP-specific steps:**

1. Candidate prepares Project Brief (CAD Appendix D) with supervisor signature
2. Unit Training NCO/Officer submits: standard Enrollment Request + Project Brief + TM-20 Go record
3. C2DAO reviews Project Brief within 5 duty days — approves, returns for revision, or denies
4. Enrollment confirmed in writing upon Project Brief approval
5. Sprint workspace provisioned T-10 days; access confirmed by candidate T-5 days

**BSP does not grant TM credit.** Completion appears in training records as a separate event type, not as a TM course completion.

**BSP waivers:**
- TM-20 prereq waiver: Not granted
- Project Brief waiver: Not granted
- Late brief (after T-14 days): C2DAO discretion; never later than T-5 days

---

## TRAINING RECORDS REQUIREMENTS

C2DAO maintains the authoritative training records system for MSS training. Unit Training NCOs/Officers maintain a local copy. This section defines the minimum data standard for any training record entry.

### Minimum Required Fields — Per Trainee Record

| Field | Format | Notes |
|---|---|---|
| Trainee last name, first name | String | As it appears on orders |
| Rank | Standard Army abbreviation (SSG, CPT, etc.) | |
| Unit of assignment | UIC + short name | Current unit at time of training |
| MOS/AOC | Standard format (e.g., 17C, 25D, FA49) | |
| NIPR email | DoD email address | Official contact for records |
| Course completed | TM-10, TM-20, TM-30, TM-40X, TM-50X, or BSP | Exact identifier |
| Result | Go / No-Go | |
| Evaluation date | YYYY-MM-DD | Date of practical exercise completion |
| Evaluator name and rank | String | Must match signature on completion certificate |
| Completion certificate number | Per certificate format | Unique identifier for audit |
| Prerequisites on file | Y/N per prereq | Verified at enrollment; confirm at record entry |
| Notes | Free text | No-Go remediation status, waivers, special circumstances |

### Record Retention

- **Individual Training Record (CAD Appendix B):** Completed by evaluator at time of evaluation. Original retained by C2DAO. Copy filed by unit Training NCO/Officer. Trainee retains completion certificate.
- **Unit Training Status Matrix:** Maintained by C2DAO. Updated within 2 duty days of any evaluation result. Contains current Go status per trainee per course for all enrolled units.
- **Retention period:** 3 years minimum, or through PCS cycle plus 1 year — whichever is longer. Records must be transferable to gaining unit upon PCS.

### What Is NOT an Acceptable Training Record

- Email confirmation of course attendance without an evaluator signature
- Verbal attestation by supervisor that training was completed
- Certificate from a non-C2DAO training event or commercial Palantir training (does not count toward MSS program completion)
- Completion of a prior-version course (e.g., pre-v2.0 ORSA course, now designated TM-40G) without a re-evaluation on the current curriculum

### Querying Training Records

Unit Training NCOs/Officers may request a unit training status extract from C2DAO Training POC at any time. Standard format: unit name or UIC + requested course level. Response within 3 duty days. For deployments or time-sensitive situations, request via official messaging with URGENT flag for same-day response.

---

## TRAIN-THE-TRAINER (T3) ENROLLMENT

### T3-I — Instructor Certification

T3-I enrollment follows a **selection** model, not the standard enrollment request process.

| Step | Action | Responsible |
|---|---|---|
| 1 | C2DAO Training OIC identifies instructor pipeline need | Training OIC |
| 2 | Training OIC selects candidates based on: TM-30 Go on file, platform proficiency, demonstrated aptitude for instruction, operational availability | Training OIC |
| 3 | Training OIC issues selection notification to candidate and candidate's unit | Training OIC |
| 4 | Candidate's unit acknowledges and confirms availability for the T3-I iteration | Unit CDR/S3 |
| 5 | C2DAO verifies TM-30 Go and provisions instructor-level account access | C2DAO Admin |

Self-nomination is permitted — candidates may submit a request to the Training OIC. Selection is not guaranteed.

**Lead time:** T-21 days minimum (account provisioning for instructor-level access may require elevated coordination).

### T3-F — MSC Force Multiplier

T3-F enrollment follows a **commander nomination** model.

| Step | Action | Responsible |
|---|---|---|
| 1 | Unit commander identifies need for local TM-10 delivery capability | Unit CDR |
| 2 | Commander nominates candidate via memorandum (see UDT SOP Appendix A) | Unit CDR |
| 3 | Nomination submitted to C2DAO Training Division | Unit Training NCO |
| 4 | C2DAO verifies TM-20 Go on file and active MSS account | C2DAO Admin |
| 5 | Candidate enrolled in next available T3-F iteration (typically aligned with MTT rotation to the candidate's MSC) | C2DAO Training |

**Lead time:** T-14 days minimum. When aligned with an MTT rotation, coordinate via the MTT advance party procedures.

---

## Palantir Certification Alignment

MSS training tracks prepare students for Palantir's external certification exams. The following alignment is advisory — Palantir certifications are independent of MSS completion and require separate registration.

| MSS Completion | Palantir Certification | Readiness Level | Registration |
|---------------|----------------------|-----------------|-------------|
| TM-20 | Foundry & AIP Builder Foundations Badge | Ready to attempt | [Earn badge](https://community.palantir.com/t/earn-your-foundry-aip-builder-foundations-badge/1043) |
| TM-30 + TM-40L | Foundry Data Engineer Certification | Well-prepared | [Prep guide](https://community.palantir.com/t/data-engineer-certification-preperation/2789) |
| TM-30 + TM-40L | Foundry Application Developer Certification | Well-prepared | [Exam info](https://community.palantir.com/t/what-to-expect-in-foundry-application-developer-certification-exam/548) |

> **NOTE:** Palantir certification exams may cover features or configurations not present in the USAREUR-AF MSS environment. Students should supplement with Palantir Learn (learn.palantir.com) and the [Ontologize YouTube channel](https://www.youtube.com/@Ontologize) for exam preparation. Coordinate with C2DAO for certification voucher availability.

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*Enrollment SOP | Version 2.0 | March 2026*
