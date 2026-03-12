# EX-40E — Knowledge Manager
## Practical Exercise — TM-40E Proficiency

**Version 1.0 | March 2026**
**Prerequisite:** TM-40E, Knowledge Manager Technical Manual (and TM-10 through TM-30)
**Duration:** 2–3 hours
**Environment:** MSS with Workshop, form builder, and lessons learned dataset access (see ENVIRONMENT_SETUP.md)

---

## SCENARIO

Your unit just completed a 30-day field exercise. The G7 Knowledge Manager has tasked you to: build a lessons learned submission form in Workshop, ingest a backlog of 20 synthetic after-action reports, tag and categorize them using a controlled vocabulary, and produce a searchable lessons learned dashboard for the command group.

**Training dataset:** 20 synthetic AAR documents (free text + structured fields).

---

## TASK LIST

### Task 1 — Build a Lessons Learned Submission Form (45 min)
- [ ] Create a Workshop form with fields: date, unit, exercise name, category (dropdown — use the 6-category taxonomy from TM-40E), observation (text), recommendation (text), OPR (responsible office), priority (H/M/L)
- [ ] Add input validation: required fields, category constrained to taxonomy
- [ ] Test form submission with a sample entry; verify it writes to the lessons learned dataset
- **Go:** Form renders; all fields present; submission writes correctly; validation fires on required fields
- **No-Go:** Missing fields, broken submission, or validation absent

### Task 2 — Ingest and Tag the AAR Backlog (30 min)
- [ ] Ingest the 20 synthetic AAR documents into the lessons learned dataset
- [ ] Apply category tags using the controlled vocabulary (Pipeline Builder or manual review — your choice)
- [ ] Flag any documents that are ambiguous or span multiple categories
- **Go:** All 20 records ingested; each has a category tag; ambiguous records flagged
- **No-Go:** Missing records or uncategorized entries without flags

### Task 3 — Build the Lessons Learned Dashboard (30 min)
- [ ] Create a Workshop dashboard: summary count by category, timeline of submissions, searchable table of all records
- [ ] Add a filter by category and priority
- [ ] Ensure the dashboard is accessible to the command group (read-only permission)
- **Go:** All three components present; filters work; command group has read access
- **No-Go:** Missing component or permissions incorrect

### Task 4 — Institutional Memory Linkage (20 min)
- [ ] Identify 2 lessons from the ingested AAR backlog that contradict each other (conflicting recommendations on the same topic)
- [ ] Write a 1-paragraph reconciliation note: what the conflict is, which recommendation is preferred and why
- **Go:** Conflict correctly identified; reconciliation note is substantive
- **No-Go:** No conflict identified (check dataset — conflicts are present) or note is superficial

---

## EVALUATOR NOTES

> **TODO:** Complete after dry run. Task 4 requires planting conflicting recommendations in the synthetic AAR dataset — confirm this is done before exercise. Note: Task 1 timing varies widely by prior Workshop experience.

Scoring: 4 tasks. Go on 3 of 4 = overall Go. No-Go on Task 1 = automatic No-Go (core KM build competency).

---

## ENVIRONMENT SETUP

> **TODO:** Prepare 20 synthetic AAR documents — include at least 2 with conflicting recommendations on the same topic. Pre-create the lessons learned dataset schema. Document in `ENVIRONMENT_SETUP.md`.
