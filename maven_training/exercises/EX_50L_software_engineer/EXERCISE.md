# EX_50L — Advanced Software Engineering
## Practical Exercise — TM-50L Proficiency

| Field | Value |
|-------|-------|
| **Version** | 1.0 — March 2026 |
| **Prerequisite** | TM-40L complete (Go on file); TM-50L course completion; OSDK TypeScript SDK (advanced), CI/CD pipeline access, and Code Workspace confirmed |
| **Duration** | 6–8 hours (typically executed Day 5 of TM-50L) |
| **Environment** | MSS Code Workspace (TypeScript + Python), OSDK advanced access, CI/CD pipeline (training environment), Ontology editor; see ENVIRONMENT_SETUP.md |
| **Companion TM** | TM_50L_SOFTWARE_ENGINEER_ADVANCED.md |
| **Syllabus** | SYLLABUS_TM50L |
| **Exams** | EXAM_TM50L_POST |

## SCENARIO

You are the senior SWE lead for the USAREUR-AF MSS platform. You have inherited a Workshop application (`equipment_readiness_app/`) built by a previous team. The application works — but it has a known performance issue, no CI/CD pipeline, no security review on record, and the Object Type design is not OSDK-optimized.

Your task is to conduct an architecture review, implement targeted OSDK improvements, establish a CI/CD pipeline, and produce a security review for platform leadership sign-off.

**Training environment:** All code, schemas, and pipeline configurations are synthetic. No operational data or classified content is used.

## TASK LIST

### Task 1 — Architecture Review (75 min)

Review `equipment_readiness_app/` (TypeScript OSDK application, ~800 lines across 6 files):

- [ ] Document the current Object Type design: list the Object Types used, their primary keys, property types, and link traversal patterns
- [ ] Identify at least 3 architecture issues (see ENVIRONMENT_SETUP.md for planted issues — evaluator knows the expected findings)
- [ ] For each issue, document: (a) the issue, (b) the architectural impact (performance / maintainability / security), and (c) a recommended fix
- [ ] Produce a 1-page architecture assessment with an executive summary (1–2 sentences) suitable for a platform lead who is not the code author

| Standard | Criteria |
|----------|----------|
| **Go** | Current Object Type design documented (all types, keys, properties, links); at least 3 issues identified with impact and recommended fix; 1-page assessment with non-author-level executive summary present |
| **No-Go** | Object Type design not documented; fewer than 3 issues identified; architecture assessment absent or written for code author audience only |

### Task 2 — OSDK Optimization Implementation (90 min)

Implement 2 of the 3 identified architecture fixes (the third may be documented as a deferred recommendation if it requires Ontology changes beyond the participant's access level):

- [ ] Implement bulk query batching for the equipment status fetch (replacing the current loop-per-unit pattern): document the before/after query count and estimated latency improvement
- [ ] Implement memoization for at least one computed property that is called more than once per render cycle: document which property and why memoization is appropriate
- [ ] Verify no TypeScript compilation errors (`tsc --noEmit`); verify no new type safety warnings introduced by the changes

| Standard | Criteria |
|----------|----------|
| **Go** | Both optimizations implemented; before/after documentation present for bulk query; memoization applied to appropriate property with documented rationale; clean TypeScript compilation |
| **No-Go** | Only 1 optimization implemented; no before/after documentation; TypeScript compilation errors after changes |

### Task 3 — CI/CD Pipeline Implementation (75 min)

Configure a CI/CD pipeline for the application in the training CI/CD environment:

- [ ] Configure a build stage: TypeScript compile (`tsc`) and lint (`eslint`) run on every PR — build must pass before merge is permitted
- [ ] Configure a unit test stage: `npm test` runs and must pass with ≥80% coverage (mock OSDK objects provided in `test_fixtures/`)
- [ ] Configure a promotion gate: deployment to the staging environment requires manual approval from the engineering lead role
- [ ] Document the pipeline configuration in a 1-page pipeline SOP: what runs at each stage, what passes and fails, and what the rollback procedure is

| Standard | Criteria |
|----------|----------|
| **Go** | All three stages configured and verified to run (build, test, approval gate); pipeline SOP present with rollback procedure |
| **No-Go** | Fewer than 3 stages configured; pipeline SOP absent; rollback procedure not documented |

### Task 4 — Security Review (60 min)

Conduct a security review of `equipment_readiness_app/` using the USAREUR-AF SWE Security Review Checklist:

- [ ] Input validation: identify all input boundaries in the application; verify each has validation (mark absent validations as findings)
- [ ] Authentication/authorization: verify OSDK credential handling follows the approved pattern (no tokens in client-side code, no hardcoded credentials); document any deviations as findings
- [ ] OSDK permission scope: verify the application requests only the Ontology object types and properties it uses — document any over-permissioned scopes as findings
- [ ] Finding summary: produce a finding table (finding ID, location, severity — critical/high/medium/low, status — open/accepted/remediated, recommended action)
- [ ] Determine application disposition: sign-off (no criticals, no unmitigated highs), conditional sign-off (mitigated findings only), or defer (critical or unmitigated high present)

| Standard | Criteria |
|----------|----------|
| **Go** | All three review domains completed; finding table present with ID/location/severity/status/action for each finding; disposition decision present with rationale |
| **No-Go** | Any domain skipped; finding table absent; disposition not determined or not justified |

### Task 5 — Platform Documentation (30 min)

Produce a platform handoff package:

- [ ] System diagram: 1-page diagram showing Object Types, OSDK query patterns, Workshop application components, and CI/CD flow
- [ ] OSDK interface contracts: document the 3 primary query patterns used by the application (query name, Object Types queried, filters applied, return shape)
- [ ] API versioning note: identify any actions or queries that would break downstream consumers if the Object Type schema changes; document a deprecation notice format

| Standard | Criteria |
|----------|----------|
| **Go** | System diagram includes all four required elements; 3 query patterns documented with query name, Object Types, filters, and return shape; at least 1 breaking-change scenario identified with deprecation notice format |
| **No-Go** | System diagram missing any of the four elements; fewer than 3 query patterns documented; no breaking-change scenario identified |

## EVALUATOR NOTES

**Scoring:** 5 tasks. Go on 4 of 5 = overall Go. No-Go on Task 1 or Task 4 = automatic No-Go (architecture review and security review are the core competencies at TM-50L level).

### Pre-Exercise Checklist

- [ ] Confirm OSDK TypeScript SDK (advanced) provisioned — 7 duty days prior; verify participant can import OSDK types and build without errors before exercise day
- [ ] Confirm CI/CD pipeline access (build/configure pipelines) — separate from OSDK access; verify by having participant create a blank pipeline before exercise day
- [ ] Load `equipment_readiness_app/` source code into training project with planted architecture issues
- [ ] Load `test_fixtures/` (mock OSDK objects for unit test stage — Task 3)
- [ ] Place blank USAREUR-AF SWE Security Review Checklist in participant's project folder
- [ ] Verify TypeScript compilation errors are not present in the pre-exercise state (issues are architectural, not syntactic)

### Pre-Planted Architecture Issues (Task 1)

| Issue | Location | Type |
|-------|----------|------|
| Issue 1 | `EquipmentStatusPanel.tsx` lines 45–78 | Loop-per-unit OSDK query (N+1 pattern) — fetches equipment status one unit at a time instead of batching into a single Object Set query |
| Issue 2 | `ReadinessCalculator.ts` lines 12–34 | Computed `averageReadiness` property recalculated on every render with no memoization, despite only depending on data that changes on explicit refresh |
| Issue 3 | `AppConfig.ts` line 8 | OSDK scope configured to request ALL Ontology Object Types — over-permissioned; application only uses Equipment and MaintenanceRequest types |

Issue 1 and Issue 2 are the OSDK optimization targets for Task 2. Issue 3 is a security finding for Task 4 (over-permissioned scope).

### Common Failure Modes

| Task | Common Failure | Evaluator Guidance |
|------|---------------|--------------------|
| Task 1 | Architecture issues identified at surface level without impact documentation | Ask: "What happens at 500 units instead of 10?" — if participant cannot articulate the performance consequence, the impact characterization is insufficient |
| Task 2 | Memoization applied to a property with rapidly changing dependencies | Ask: "What does this property depend on? Does it change frequently?" — incorrect memoization target = coaching note, not automatic No-Go, but must be corrected |
| Task 2 | TypeScript errors after optimization | Must be resolved before Go — common cause: bulk query return type not narrowed correctly |
| Task 3 | Pipeline configured but not verified to run | Ask participant to trigger the pipeline and show the execution log |
| Task 4 | Over-permissioned OSDK scope (Issue 3) not caught | Probe: "Can you show me the full scope list in AppConfig.ts?" — if participant reviewed input validation and auth but skipped scope review, that domain is incomplete |
| Task 5 | System diagram shows architecture as-designed, not as-built | Diagram must reflect the post-Task-2 implementation, not the pre-exercise state |
