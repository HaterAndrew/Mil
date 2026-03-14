# EX-40K — Knowledge Manager
## Practical Exercise — TM-40K Proficiency

| Field | Value |
|-------|-------|
| **Version** | 1.0 — March 2026 |
| **Prerequisite** | TM-30 REQUIRED; TM-40K — Knowledge Manager Technical Manual (and TM-10 through TM-20) |
| **Duration** | 2–3 hours |
| **Environment** | MSS with Workshop, form builder, and lessons learned dataset access — see ENVIRONMENT_SETUP.md |

## COMPANION RESOURCES

| Resource | Reference |
|----------|-----------|
| Technical Manual | TM-40K — Knowledge Manager |
| Syllabus | SYLLABUS_TM40K |
| Pre-Exercise Exam | EXAM_TM40K_PRE |
| Post-Exercise Exam | EXAM_TM40K_POST |
| Continuation Track | TM-50K — Advanced Knowledge Manager |

## WFF AWARENESS

The lessons learned repository and submission form built in this exercise are consumed by all WFF track personnel (TM-40A–F) — intelligence, fires, movement & maneuver, sustainment, protection, and mission command operators all contribute to and draw from institutional knowledge repositories. Evaluators should assess whether the dashboard and taxonomy are usable by non-KM-specialist audiences.

## SCENARIO

Your unit just completed a 30-day field exercise. The G7 Knowledge Manager has tasked you to: build a lessons learned submission form in Workshop, ingest a backlog of 20 synthetic after-action reports, tag and categorize them using a controlled vocabulary, and produce a searchable lessons learned dashboard for the command group.

**Training dataset:** 20 synthetic AAR documents (free text + structured fields).

## TASK LIST

### Task 1 — Build a Lessons Learned Submission Form (45 min)

Create a Workshop form with the following fields:

| Field | Type | Constraint |
|-------|------|------------|
| Date | Date | Required |
| Unit | Text | Required |
| Exercise Name | Text | Required |
| Category | Dropdown | Required; constrained to the 6-category taxonomy from TM-40K |
| Observation | Text (long) | Required |
| Recommendation | Text (long) | Required |
| OPR | Text | Required |
| Priority | Dropdown | H/M/L |

- [ ] Add input validation: required fields enforced, category constrained to taxonomy
- [ ] Test form submission with a sample entry; verify it writes to the lessons learned dataset

| Standard | Criteria |
|----------|----------|
| **Go** | Form renders; all fields present; submission writes correctly; validation fires on required fields |
| **No-Go** | Missing fields, broken submission, or validation absent |

### Task 2 — Ingest and Tag the AAR Backlog (30 min)

- [ ] Ingest the 20 synthetic AAR documents into the lessons learned dataset
- [ ] Apply category tags using the controlled vocabulary (Pipeline Builder or manual review — your choice)
- [ ] Flag any documents that are ambiguous or span multiple categories

| Standard | Criteria |
|----------|----------|
| **Go** | All 20 records ingested; each has a category tag; ambiguous records flagged |
| **No-Go** | Missing records or uncategorized entries without flags |

### Task 3 — Build the Lessons Learned Dashboard (30 min)

Create a Workshop dashboard with:
- Summary count by category
- Timeline of submissions
- Searchable table of all records
- Filter by category and priority
- Read-only permission for the command group

| Standard | Criteria |
|----------|----------|
| **Go** | All three components present; filters work; command group has read access |
| **No-Go** | Missing component or permissions incorrect |

### Task 4 — Institutional Memory Linkage (20 min)

- [ ] Identify 2 lessons from the ingested AAR backlog that contradict each other (conflicting recommendations on the same topic)
- [ ] Write a 1-paragraph reconciliation note: what the conflict is, which recommendation is preferred and why

| Standard | Criteria |
|----------|----------|
| **Go** | Conflict correctly identified; reconciliation note is substantive and commits to a preferred recommendation |
| **No-Go** | No conflict identified (check dataset — conflicts are present) or note is superficial |

## EVALUATOR NOTES

**Scoring:** 4 tasks. Go on 3 of 4 = overall Go. No-Go on Task 1 = automatic No-Go (form building and data capture are the core KM platform competency).

### Pre-Exercise Checklist

- [ ] Confirm the 20 synthetic AAR documents are pre-loaded and accessible to training accounts
- [ ] Confirm the lessons learned dataset schema is pre-created (participant populates, does not create schema)
- [ ] Verify at least 2 AAR documents contain conflicting recommendations (see ENVIRONMENT_SETUP.md)
- [ ] Confirm Workshop form builder is accessible to training accounts

### Common Failure Modes

| Task | Common Failure | Evaluator Guidance |
|------|---------------|--------------------|
| Task 1 | Form validation fires on focus, not on submit | Ask participant to fill out the form with a missing required field and click Submit — if form submits, No-Go |
| Task 1 | Category dropdown not constrained to taxonomy | Open values accepted instead of the 6-category list — No-Go; taxonomy enforcement is a core KM governance requirement |
| Task 2 | Some AAR documents uncategorized | Anything uncategorized without a flag is No-Go; flagging ambiguous records is acceptable and encouraged |
| Task 3 | Dashboard visible but command group cannot access it | Ask participant to demonstrate access from a second account; permissions misconfiguration is No-Go |
| Task 4 | Conflict not identified | Confirm the conflicting pair exists in the ingested data (see ENVIRONMENT_SETUP.md answer key) — if participant cannot find it after 10 min, prompt: "Review records on [topic]" |
| Task 4 | Reconciliation note describes the conflict but makes no recommendation | "Both views have merit" is not acceptable — participant must commit to a preferred recommendation with reasoning |

### Timing Notes

- Task 1 is the most variable in timing (30–60 min) — prior Workshop experience is the primary factor
- Task 4 (reconciliation note) typically takes 10–15 min for participants who locate the conflict quickly
- If participant completes early, ask them to explain the 6-category taxonomy and why they chose it for a specific ambiguous document (verbal check)

## NEXT STEPS

Participants who receive an overall Go on EX-40K are eligible to enroll in **TM-50K — Advanced Knowledge Manager**. TM-50K extends into enterprise knowledge architecture, cross-command taxonomy alignment, and AI-assisted knowledge capture at scale. No TM-50A–F tracks exist.

## ENVIRONMENT SETUP

See [ENVIRONMENT_SETUP.md](ENVIRONMENT_SETUP.md) for full setup instructions.
