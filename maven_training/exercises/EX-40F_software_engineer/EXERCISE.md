# EX-40F — Software Engineer
## Practical Exercise — TM-40F Proficiency

**Version 1.0 | March 2026**
**Prerequisite:** TM-40F, Software Engineer Technical Manual (and TM-10 through TM-30)
**Duration:** 3–4 hours
**Environment:** MSS with Python Transforms, TypeScript/OSDK access, Code Workbook (see ENVIRONMENT_SETUP.md)

---

## SCENARIO

The OPDATA team needs a Python Transform pipeline that ingests a synthetic personnel readiness feed, normalizes and validates the data, exposes key entities via the Ontology (OSDK), and surfaces a TypeScript-based action that lets authorized users update a record status from an external application.

**Training dataset:** Synthetic personnel readiness feed, CSV format, ~1,000 records.

---

## TASK LIST

### Task 1 — Ingest and Validate (30 min)
- [ ] Write a Python Transform that ingests the CSV feed
- [ ] Validate: required fields present, date fields parseable, numeric fields in valid range
- [ ] Log validation failures to a separate error dataset (do not silently drop bad records)
- [ ] Make the transform idempotent (re-run produces same output, no duplicates)
- **Go:** Transform runs; error dataset captures failures; idempotency verified by running twice
- **No-Go:** Errors silently dropped, transform not idempotent, or validation logic absent

### Task 2 — Normalize and Enrich (30 min)
- [ ] Normalize unit names to uppercase; trim whitespace from all string fields
- [ ] Add a `record_hash` column (SHA-256 of key fields) for change detection
- [ ] Add `ingested_at` timestamp
- [ ] Output to a clean dataset following naming standards
- **Go:** Normalization applied; hash and timestamp present; naming standard followed
- **No-Go:** Normalization missing or hash column absent

### Task 3 — Ontology Object Type and Properties (45 min)
- [ ] Create (or use a pre-created) `PersonnelRecord` Object Type in the Ontology
- [ ] Map properties: personnel_id (primary key), unit, readiness_status, record_hash, ingested_at
- [ ] Write an OSDK-backed Python snippet that retrieves all records for a given unit
- [ ] Verify the OSDK query returns correct results for a test unit
- **Go:** Object Type has correct property mapping; OSDK query returns correct records
- **No-Go:** Property mapping is wrong or query returns empty/incorrect results

### Task 4 — TypeScript Action (45 min)
- [ ] Write a TypeScript Action (Foundry Actions / OSDK) that accepts a `personnel_id` and a new `readiness_status` value and updates the record
- [ ] Add an authorization check: only users in the "data-steward" group can execute the action
- [ ] Test the action as an authorized user; verify the update persists
- [ ] Test as an unauthorized user; verify the action is blocked
- **Go:** Action updates correctly for authorized user; blocked for unauthorized user
- **No-Go:** Authorization check absent or action fails for authorized user

### Task 5 — Code Review Checklist (20 min)
- [ ] Self-review your Python Transform against the TM-40F code quality checklist: no hardcoded values, parameterized configs, no sensitive data in logs, inline comments on non-obvious logic
- [ ] Produce a written checklist with pass/fail for each criterion
- **Go:** Checklist is complete; any failures are acknowledged and explained
- **No-Go:** Checklist absent or critical failures (hardcoded credentials, sensitive data in logs) not flagged

---

## EVALUATOR NOTES

> **TODO:** Complete after dry run. Task 4 requires a "data-steward" group to be pre-configured in the training environment. Confirm OSDK TypeScript SDK is available. Task timing can run long — consider splitting over two sessions.

Scoring: 5 tasks. Go on 4 of 5 = overall Go. No-Go on Task 1 or Task 4 = automatic No-Go.

---

## ENVIRONMENT SETUP

> **TODO:** Load synthetic personnel readiness CSV. Create `PersonnelRecord` Object Type with correct properties. Configure "data-steward" group with test accounts (one in group, one not). Document in `ENVIRONMENT_SETUP.md`.
