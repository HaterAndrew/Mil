# CONCEPTS GUIDE — TM-30 COMPANION — ADVANCED BUILDER · MAVEN SMART SYSTEM (MSS)

> **BLUF:** TM-30 is the shift from building to designing. A Builder (TM-20) configures tools. An Advanced Builder (TM-30) designs systems — pipelines that others feed, Ontology models that others extend, Workshop applications that commanders rely on for operational decisions. This guide develops the mental models required before those systems are built.
> **Purpose:** Establishes conceptual foundations for multi-source pipeline architecture, Ontology design, Workshop application composition, AIP Logic configuration, and data governance. Read before beginning TM-30 task instruction.
> *HQ USAREUR-AF · v1.0 · 2026 · DISTRIB: USG only*

---

## SECTION 1 — WHAT TM-30 ADDS

**BLUF:** TM-20 teaches you to use tools. TM-30 teaches you to design with them. The distinction is not a matter of technical skill — it is a matter of accountability. At TM-30, your designs become the infrastructure others depend on.

### 1-1. The Shift from Builder to Advanced Builder

At TM-20, the primary question is: *How do I use this tool to get this output?*

At TM-30, the primary question is: *What should this system look like, and what will break if I get it wrong?*

| Dimension | TM-20 Builder | TM-30 Advanced Builder |
|---|---|---|
| **Unit of output** | A single pipeline, widget, or Object Type | A system of interconnected pipelines, Objects, and applications |
| **User of your output** | Self or a specific analyst | Any operator (TM-10) or builder (TM-20) in the formation |
| **Scope of errors** | Affects one dataset or application | Affects downstream consumers across multiple staff sections |
| **Governance role** | Follows naming conventions | Enforces them, reviews peer work, coordinates promotion cycles |
| **Pipeline design** | Single-source, basic transforms | Multi-source joins, grain management, incremental refresh, fan-out awareness |
| **Ontology design** | Configure existing Object Types | Design Object Type hierarchies, Link Types, and Action schemas from scratch |
| **Workshop design** | Single-page apps, basic widgets | Multi-page applications, variable chains, conditional logic, command-audience layout |
| **AIP Logic** | Aware of existing AI workflows | Configures parameters, monitors outputs, escalates authoring to TM-40H |
| **Environment management** | Aware of branching | Executes and governs branch-review-promote cycles |

### 1-2. Why the Distinction Matters Operationally

An error at TM-20 is contained. An error at TM-30 is systemic. When a TM-30 Advanced Builder designs an Object Type that other builders extend, names a property incorrectly, or configures a pipeline join at the wrong grain — the consequences propagate downstream. Applications break. Dashboard widgets go blank. SITREP counts double. Commanders see incorrect readiness data.

V Corps incident (2025): A TM-30 builder renamed a property on the `SoldierReadiness` Object Type in production without auditing downstream consumers. Three Workshop applications owned by G1, G4, and Brigade S3 went blank within 30 minutes. Restoration took four hours. The downstream impact assessment required before the change would have taken five minutes.

**TM-30 discipline is not process for its own sake. It is operational risk management.**

### 1-3. What TM-30 Does Not Cover

TM-30 is a UI boundary. Every TM-30 task is accomplished through Foundry's graphical tools. Where that boundary is, and what lies beyond it, is as important as what is within it.

| Requirement | TM-30 Scope? | Escalation |
|---|---|---|
| Multi-page Workshop app, conditional logic, variable chains | YES | Build per TM-30, Chapter 2 |
| Multi-source joins, grain management, incremental pipelines | YES | Build per TM-30, Chapter 3 |
| Object Type hierarchies, Link Types, Action schemas | YES | Design per TM-30, Chapter 4 |
| AIP Logic parameter configuration and monitoring | YES | Configure per TM-30, Chapter 6 |
| Python / PySpark transform authoring | NO | TM-40L |
| TypeScript Functions on Objects (FOO) | NO | TM-40H or TM-40L |
| OSDK integration or custom application code | NO | TM-40L |
| Authoring new AIP Logic workflows from scratch | NO | TM-40H |
| Configuring new source connector types | NO | TM-40L |
| Writing code-based data quality checks | NO | TM-40L |

Rule: if a requirement involves writing, editing, or debugging code in any language — it is TM-40.

---

## SECTION 2 — PIPELINE ARCHITECTURE

**BLUF:** A pipeline at TM-30 level is not a data filter — it is an architectural decision. How you design grain, join logic, and refresh behavior determines whether downstream consumers get reliable data or a compounding series of surprises.

### 2-1. Transform Graph Thinking

At TM-20, pipelines are linear: one source → one or two transforms → one output. At TM-30, pipelines are directed acyclic graphs (DAGs): multiple sources, multiple intermediate datasets, multiple output shapes, all connected in dependency chains.

**Think before you build by answering four structural questions:**

| Question | Purpose | Example |
|---|---|---|
| **What are all the sources?** | Identify every upstream feed before touching the UI | GCSS-A maintenance records, PBUSE property book, personnel feed from eMILPO |
| **What shape does each source have?** | Document grain (one row per what?) and key fields before joining | GCSS-A: one row per maintenance event. PBUSE: one row per line item. Grain mismatch on join = row multiplication. |
| **What shape does the output need?** | The Ontology Object Type defines the required output grain — design the pipeline to produce it, not to produce something close | If the `VehicleReadiness` Object Type expects one row per vehicle per day, every transform in the pipeline must preserve or produce that grain |
| **What happens when a source is delayed or absent?** | Pipeline failure mode design is part of pipeline design, not an afterthought | If the GCSS-A feed is 24 hours late, does the pipeline fail, use stale data, or produce a gap? Document the behavior before production. |

### 2-2. Dependency Chains and Cascade Risk

When Pipeline B depends on the output of Pipeline A, a failure in A cascades to B. In a well-designed system, cascade failure is bounded and detectable. In a poorly designed system, it is silent — Pipeline B produces output from stale data and no one knows.

**Dependency chain design rules:**

| Rule | Rationale |
|---|---|
| No more than three pipeline hops in a single dependency chain where possible | Each hop multiplies latency and failure surface area |
| Every intermediate dataset has a documented owner | If a dataset breaks, someone is accountable to fix it |
| Monitoring configured on each node of the chain | Stale data must be detected at the node that goes stale, not three hops downstream |
| Failure in an upstream pipeline surfaces in the downstream application | A Workshop table showing "last updated 72 hours ago" is better than a table silently showing stale data as current |

### 2-3. Incremental vs. Full Refresh

**Full refresh:** The pipeline drops and rebuilds the output dataset on every run. Always correct if it completes. Expensive on large datasets. Appropriate for: small datasets, reference tables, datasets where correctness is more important than compute cost.

**Incremental refresh:** The pipeline processes only new or changed records since the last successful run. Much cheaper at scale. Produces incorrect output if the change detection logic is wrong.

> **CAUTION:** Incremental refresh requires a reliable watermark — a field indicating when each record was last modified. If source systems do not produce a reliable watermark (e.g., modification timestamps that are not updated on all record changes), incremental logic will miss updates. Validate the watermark before configuring incremental refresh. If in doubt, use full refresh.

| Dataset Characteristic | Recommended Refresh Mode |
|---|---|
| < 500K rows, reference data, slow-changing | Full refresh |
| > 1M rows, append-only (events, logs) | Incremental |
| High volume + frequent updates (not append-only) | Incremental with robust change detection, or windowed full refresh |
| Mission-critical, zero tolerance for missed updates | Full refresh or incremental with verification transform |

For USAREUR-AF operational data: GCSS-A maintenance records typically use incremental; PBUSE property book typically uses full refresh; SITREP feeds typically use append-only incremental.

### 2-4. Grain Management at Scale — The Primary TM-30 Pipeline Failure Mode

**Grain** is the level of detail a dataset represents: one row per vehicle, one row per Soldier per day, one row per maintenance event. Joining two datasets with different grains produces **row multiplication** — a silent correctness error.

**Example:** `VehicleStatus` table: 1 row per vehicle (500 rows for a brigade fleet). `MaintenanceEvent` table: 1 row per maintenance event (3,000 rows for that same fleet, average 6 events per vehicle). Joining on vehicle ID without aggregating first produces 3,000 output rows — but the downstream Object Type expects 500. The Ontology now has 6x the expected vehicle count. Every readiness percentage computed from that data is wrong.

**Pre-join checklist:**

- [ ] Document grain of Source A (one row per \_\_\_?)
- [ ] Document grain of Source B (one row per \_\_\_?)
- [ ] Are the grains the same? If not, which source will you aggregate before joining, and by what key?
- [ ] After the join, verify output row count against expected grain
- [ ] Add a row-count validation transform that alerts if output deviates from expected range

### 2-5. Fan-Out Risk with Large Datasets

**Fan-out** occurs when one dataset feeds many downstream pipelines, applications, and Object Types. A change to the fan-out source propagates to all consumers simultaneously.

| Fan-Out Risk | Mitigation |
|---|---|
| Schema change in the source dataset breaks all downstream pipelines | Audit all downstream consumers before any schema change; use Ontology Manager's dependency view |
| A data quality issue in the source dataset appears in all downstream products simultaneously | Implement data quality checks at the source, not downstream |
| Refresh schedule change cascades to downstream run windows | Coordinate refresh schedules across the dependency graph — do not change one pipeline's schedule in isolation |

> **WARNING:** On the USAREUR-AF MSS, foundational datasets (unit hierarchy, vehicle master, personnel roll-up) are consumed by dozens of downstream pipelines and applications. A schema change to one of these datasets without a full downstream impact assessment is a formation-level incident risk. Route all changes to these datasets through C2DAO review regardless of how minor the change appears.

---

## SECTION 3 — ONTOLOGY DESIGN PRINCIPLES

**BLUF:** An Ontology is a model of operational reality. Design it to reflect how the Army talks about its entities and relationships — not to match the shape of a source dataset. When your Object Types are wrong, every product built on them inherits the error.

### 3-1. Object Type Design: Starting from Doctrine

Object Types are nouns — real-world entities that commanders and staff think, talk, and decide about. Start design from doctrine and operational language, not from source data structure.

**Three questions before creating any Object Type:**

| Question | What It Prevents |
|---|---|
| Does this entity exist in Army doctrine (FM, ADP, ATP, CATS)? | Prevents inventing entities that have no operational meaning |
| What does a commander or staff officer need to do with this entity? | Grounds the design in operational use, not data convenience |
| Does an Object Type for this entity already exist in the MSS Ontology? | Prevents duplication — always check before creating |

**Object Type hierarchy principles:**

- Parent types represent broad categories. Child types inherit properties and add specificity.
- A `Vehicle` parent type is appropriate. `VehicleM1126Stryker` as a distinct Object Type is almost certainly wrong — use a property (`vehicle_type`) to distinguish.
- Hierarchies should reflect the Army's own organizational and materiel hierarchies, not your data's filing system.
- Flat is usually better than deep. Three levels of hierarchy is the practical maximum for most operational entities.

### 3-2. Primary Key Stability — The Most Important Design Decision

Every Object Type requires a primary key — a stable, unique identifier that persists across the life of the entity. This decision has more downstream consequence than any other design choice.

> **WARNING:** If you get the primary key wrong, you cannot fix it without rebuilding the Object Type and every pipeline, Link, and Action that references it. Choose carefully before publishing.

| Primary Key Characteristic | Why It Matters |
|---|---|
| **Stable** — does not change when the entity changes status, location, or assignment | An Object keyed on unit location will generate new Objects every time a unit moves |
| **Unique** — no two Objects of the same Type share the same key | Non-unique keys produce Object merge/collision in the Ontology |
| **Available from all source systems** — the key value appears in every upstream data feed | If the key is only in one of three sources, join logic to the other two fails |
| **Army-standard where possible** — use existing IDs (UIC, NSN, DODAAC, EDIPI) | Inventing proprietary IDs when Army standard IDs exist creates reconciliation problems |

For USAREUR-AF MSS: vehicle primary key = NSN + bumper number + UIC. Unit primary key = UIC. Soldier primary key = EDIPI. Equipment record primary key = Document Number from GCSS-A.

### 3-3. Cardinality — Modeling Relationships Correctly

Link Types connect Object Types. Every Link Type has a cardinality that specifies how many of one Object can be linked to how many of another.

| Cardinality | Meaning | Example |
|---|---|---|
| One-to-one | Each Object A links to exactly one Object B | One deployment order → one unit (if orders are unit-specific) |
| One-to-many | One Object A links to many Object Bs | One unit → many vehicles |
| Many-to-many | Many Object As link to many Object Bs | Many Soldiers assigned to many duty positions over time |

**Design errors in cardinality are silent in the Ontology and loud in applications.** A many-to-one relationship modeled as one-to-one will produce missing Links when a second relationship is created. A one-to-one relationship modeled as many-to-many will cause Workshop applications to display unexpectedly large result sets.

> **NOTE:** Many-to-many Links are the most complex to query and the most prone to returning unexpected result sets. If a relationship appears to be many-to-many, check whether there is a bridging entity (e.g., an Assignment event that connects a Soldier to a Unit for a defined time period). Model the bridge as an Object Type — it usually produces cleaner queries and cleaner Workshop UX.

### 3-4. Structural vs. Behavioral Links

**Structural Links** represent how entities are organized in reality — hierarchy, assignment, location. They change infrequently and represent the "static" structure of the operational environment.

**Behavioral Links** represent events, transactions, or interactions — maintenance events on a vehicle, logistics requests between units, inspection outcomes. They change frequently and represent what happened.

| Link Type | Structural or Behavioral | Design Implication |
|---|---|---|
| Unit → Parent Unit | Structural | Changes infrequently; query patterns expect stable values |
| Vehicle → Assigned Unit | Structural | Changes on reassignment; requires effective-date tracking if history matters |
| Vehicle → Maintenance Event | Behavioral | Appended frequently; design for high-volume append, not update |
| Soldier → Duty Position | Behavioral-structural hybrid | Changes on assignment; track with effective dates |

Mixing structural and behavioral Links in the same Link Type is a design error. A `VehicleRelationship` Link Type that contains both "assigned to unit" relationships and "had maintenance event" relationships will produce queries that return mixed result types — structurally unclear and operationally confusing.

### 3-5. Ontology Anti-Patterns

| Anti-Pattern | Symptom | Correction |
|---|---|---|
| **Free-text status fields** | Status values like "NMC", "FMC", "DEADLINE" appear inconsistently; filters break on typos | Use an enumerated property with controlled vocabulary; enforce at Action level |
| **Source dataset as Object Type** | Object Type structure matches a source table schema, not an operational entity | Redesign from operational language; use pipelines to reshape source data into the Object model |
| **Primary key from a mutable field** | Objects "disappear" or duplicate when unit names, locations, or status values change | Use immutable IDs (UIC, NSN, EDIPI); never use names or status values as primary keys |
| **Overloaded Object Type** | One Object Type carries 50+ properties; used for three different operational purposes | Split into focused Object Types; create Links between them |
| **Undifferentiated date fields** | Object has `date1`, `date2`, `date3` — no one knows what they mean | Name dates semantically: `maintenance_completion_date`, `inspection_scheduled_date`, `report_as_of_date` |
| **Missing Links** | Analysts copy-paste IDs between applications because the Ontology does not connect related entities | Model the relationships as Links; let the Ontology be the join, not the analyst |
| **Action without validation** | Actions allow status updates with no input validation; nonsense values written to production Objects | Add validation rules to every Action that modifies a property value |
| **Versioning in property names** | Properties named `readiness_v1`, `readiness_v2`, `readiness_final` | Use a single canonical property; manage versions through branching and governance, not naming |

---

## SECTION 4 — WORKSHOP APPLICATION ARCHITECTURE

**BLUF:** A Workshop application for a command audience is not a dashboard — it is an operational interface. Design it as you would design a briefing product: what does the commander need to see, in what order, with what level of detail? Then build the application to deliver exactly that.

### 4-1. Application Composition Patterns

| Pattern | Use Case | Structure |
|---|---|---|
| **Summary → Detail** | Commanders need formation-wide overview, then can drill to specific units or equipment | Page 1: formation-level rollup. Page 2 (conditional): unit detail triggered by page-1 selection. |
| **Multi-domain parallel** | Staff sections need simultaneous views of related data (readiness + logistics + personnel) | Tab-based navigation or side-panel layout; shared filter variable drives all domains simultaneously |
| **Event timeline** | Operations or logistics staff tracking events over time | Timeline widget on page 1; event detail on page 2 triggered by event selection |
| **Workflow state machine** | Users need to move records through defined states (submitted → reviewed → approved) | Status filter on page 1; Action buttons conditional on current record state; audit log on page 2 |

### 4-2. Layout for Command Audiences

Commanders are TM-10 Operators. They use applications you build to make decisions — not to explore data. Design with these principles:

- **Critical data above the fold.** The most important number — readiness percentage, critical shortfall count, days to exercise — must be visible without scrolling.
- **Traffic light before table.** Status indicators (RED/AMBER/GREEN) before detailed tables. Commanders scan for anomalies; analysts drill into detail.
- **One action per screen state.** If the commander's action is to approve a request, that button is the most prominent element on the screen when a request is selected. Do not hide actions in menus.
- **Labels in operational language.** Widget labels use the terms commanders use: "Equipment Operational Rate," not `vehicle_fmc_pct`. "Days Since Last Inspection," not `inspection_delta_d`.
- **Print-ready layouts for briefings.** If the application output will be screenshotted or printed for a battle rhythm brief, ensure the layout prints cleanly without requiring screen cropping.

### 4-3. Embedding vs. Standalone Applications

**Standalone applications** are accessed via direct URL or the MSS application portal. Appropriate for: dedicated staff section tools, workflow applications, applications with complex multi-page navigation.

**Embedded applications** are surfaced within another system (SharePoint, Teams, or an external portal via iFrame). Appropriate for: executive dashboards accessed from existing collaboration platforms, single-metric status widgets.

| Consideration | Standalone | Embedded |
|---|---|---|
| Navigation complexity | Full multi-page navigation supported | Single-page or minimal navigation; deep navigation is unusable in small iFrame |
| Authentication | MSS authentication is the access gate | Embedding environment may have independent auth; confirm with C2DAO before publishing |
| Performance | Full Workshop runtime | Embedded iFrames may have bandwidth constraints; optimize widget count |
| Maintenance | Self-contained | Changes to the embedded application must be tested in the embedding context, not just standalone |

> **NOTE:** Embedding Workshop applications in SharePoint or Teams environments requires coordination with C2DAO and the installation network team. Do not configure iFrame embedding without explicit approval — authentication behavior in embedded contexts may bypass MSS access controls.

### 4-4. Performance at Scale

Workshop applications slow down when they try to do too much at once. Performance degradation is not a cosmetic problem — it affects operator trust and usage.

**Common performance problems and mitigations:**

| Problem | Root Cause | Mitigation |
|---|---|---|
| Table widget loads slowly on page open | Table is querying a large Object Type without a default filter | Configure a default filter that limits initial load to a meaningful subset; require user to select before expanding |
| Application hangs when multiple filter dropdowns are changed in sequence | Each dropdown change triggers a re-query independently | Use an "Apply Filters" button pattern rather than immediate-on-change queries |
| Chart renders before filter is selected, then re-renders | Chart is configured to show all data before user narrows scope | Add conditional visibility — show charts only after required filters are populated |
| Object set widget freezes with large result set | Object set has no result limit | Set a practical upper bound; add a counter showing "displaying top N of M results" |

---

## SECTION 5 — AIP LOGIC — CONFIGURATION AND SCOPE

**BLUF:** TM-30 Advanced Builders configure and monitor AIP Logic workflows. They do not author them. Understanding what AIP Logic is and when to escalate to TM-40H is as important as knowing how to configure parameters.

### 5-1. What AIP Logic Is

AIP Logic is Foundry's no-code/low-code framework for building AI-augmented workflows on Ontology data. A workflow defines: what data to retrieve from the Ontology → how to assemble it into a prompt context → how to call the LLM → what to do with the output.

**From a TM-30 perspective, AIP Logic is a configured pipeline with an LLM in the middle.** The pipeline structure, the Ontology connections, and the output handling are all visible in the AIP Logic UI. The LLM prompt itself is a configuration artifact — not code — but authoring a new prompt from scratch for an operational use case is TM-40H work.

### 5-2. TM-30 AIP Logic Scope vs. TM-40H Escalation

| Task | TM-30 Scope | TM-40H Required |
|---|---|---|
| Adjust parameters on an existing AIP Logic workflow (temperature, max tokens, data filters) | YES | — |
| Monitor workflow run history, view outputs, report anomalies | YES | — |
| Configure which Object properties feed the prompt context (within an existing workflow's data bindings) | YES | — |
| Update NLQ (natural language query) synonym tables and ontology-to-NLQ mappings | YES | — |
| Author a new AIP Logic workflow for a new operational use case | NO | TM-40H |
| Modify prompt text or prompt logic for an existing workflow | NO — escalate | TM-40H unless change is trivial and approved |
| Integrate AIP Logic output into a new Action that writes back to the Ontology | NO | TM-40H + C2DAO governance |
| Debug a workflow producing unexpected outputs (hallucination, format errors) | Diagnose and report | TM-40H for remediation |

### 5-3. Parameter Configuration — What TM-30 Controls

When a TM-40H AI engineer hands off a configured AIP Logic workflow, TM-30 is responsible for:

| Parameter | What It Controls | TM-30 Guidance |
|---|---|---|
| **Temperature** | Randomness/creativity of LLM output. 0 = deterministic. 1 = maximum variability. | For operational workflows (SITREP synthesis, readiness summaries): keep at 0 or 0.1. Never increase without C2DAO approval. |
| **Max output tokens** | Maximum length of LLM response | Set to the minimum that covers the expected output; do not set to maximum by default |
| **Data filter bindings** | Which Object properties are retrieved and passed to the prompt context | Modify only when you understand the full prompt context — removing a property the prompt relies on will break the workflow |
| **NLQ synonym tables** | What terms users can type to trigger correct Ontology queries | Add synonyms for unit abbreviations, equipment nomenclature, common operational terms |
| **Run schedule** | When the workflow executes automatically | Coordinate with downstream consumers before changing; a daily briefing product should run well before the briefing, not after |

### 5-4. When to Escalate to TM-40H

Escalate immediately when:

- The workflow is producing outputs that do not match the ground truth in the Ontology (hallucination, data drift, stale context)
- The operational requirement has changed in a way that requires a new prompt or new data bindings
- The human review step is being bypassed or is not functioning as designed
- The workflow is writing back to the Ontology through an Action and producing incorrect writes
- Users are reporting that the workflow answers questions outside its intended scope

> **CAUTION:** Do not attempt to fix AIP Logic workflow errors by adjusting parameters you do not fully understand. A temperature change or data filter modification can alter workflow behavior in ways that are not visible until the workflow runs on real data. Report anomalies to TM-40H; do not troubleshoot by trial and error on a production workflow.

### 5-5. NLQ Setup and Monitoring

Natural Language Query (NLQ) allows users to query the Ontology in plain language. TM-30 configures the synonym tables and ontology-to-NLQ mappings that determine what queries the system understands.

**NLQ synonym table design principles:**

- Map every common abbreviation to its full term: `GCSS-A → Global Combat Support System - Army`, `UIC → Unit Identification Code`, `FMC → Fully Mission Capable`
- Add WFF staff section terms: `readiness → equipment operational rate`, `deadlines → NMC equipment count`
- Add USAREUR-AF–specific unit names: map informal unit nicknames to canonical UIC-based Object lookups
- Review NLQ query logs monthly — failed or unrecognized queries indicate missing synonym coverage

---

## SECTION 6 — DATA GOVERNANCE AND C2DAO

**BLUF:** Governance at TM-30 is not a checklist item — it is the operational discipline that prevents your work from breaking the formation's data picture. C2DAO (Command and Control Data Authoritative Organization) is the authority. Branch workflow is the mechanism. Naming standards are the enforcement.

### 6-1. What the Governance Layer Means Operationally

USAREUR-AF MSS data products inform commanders. When the readiness dashboard shows 76% operational rate, a commander may make a force generation decision on that number. When the SITREP data feed shows 14 deadlines, a logistics officer may task a recovery element.

**If the underlying data product is wrong — because a builder changed a property name in production, configured a join at the wrong grain, or deployed an untested Action — the command decision is made on a false operational picture.**

C2DAO governance exists because the MSS is not a development environment — it is a command data system. The governance layer is the mechanism that keeps development discipline between a builder's intent and the commander's data.

### 6-2. Naming Standards as Operational Discipline

Naming conventions are not stylistic preferences. They are the mechanism that makes datasets, Object Types, and applications findable, auditable, and maintainable by any qualified builder in the formation — not just the person who built them.

| Category | USAREUR-AF Naming Convention | Example |
|---|---|---|
| Datasets | `[domain]_[descriptor]_[grain]_[version]` | `log_vehicle_readiness_daily_v2` |
| Object Types | `[Domain][EntityName]` (PascalCase) | `LogVehicleReadiness`, `OpsUnitHierarchy` |
| Properties | `[entity]_[descriptor]_[unit_if_applicable]` (snake_case) | `vehicle_fmc_pct`, `maintenance_completion_date` |
| Pipeline/transform | `[domain]_[function]_[source]_to_[target]` | `log_join_gcssa_to_vehicle_readiness` |
| Workshop application | `[domain]_[audience]_[function]_app` | `log_bde_readiness_dashboard_app` |
| Variables (Workshop) | `[domain]_[descriptor]_[type]` | `ops_selected_unit_string`, `log_date_filter_date` |

> **NOTE:** Consult `maven_training/standards/NAMING_AND_GOVERNANCE_STANDARDS.md` for the full USAREUR-AF naming reference before publishing any named artifact. Non-compliant names are grounds for rejection during C2DAO review.

### 6-3. Access Control Principles

Access control on MSS follows least-privilege: users see what their role requires for their operational function. Advanced builders configure access control; they do not default to open access.

| Principle | Application |
|---|---|
| **Default to restricted** | New datasets and applications start as private; access is added intentionally, not inherited |
| **Role-based, not individual** | Grant access to the S4 role, not to CPT Smith. When CPT Smith rotates, the next S4 has access without a ticket. |
| **Access mirrors classification** | A dataset containing operationally sensitive data is not accessible to all MSS users by default |
| **No shared credentials** | Each user accesses MSS under their own identity; shared service accounts are a C2DAO exception, not a norm |
| **Audit trail required** | Sensitive datasets require audit logging of who accessed what and when; configure this before publishing |

### 6-4. Branch Workflow and Production Discipline

**The branch workflow is the mechanism that prevents development from corrupting production.** At TM-30, you execute this workflow — you do not just understand it exists.

Required sequence for any change to a production artifact:

1. **Create a branch** — never develop or test changes on the main/production branch
2. **Build and test on the branch** — verify the change works as intended with realistic data
3. **Audit downstream impact** — use Ontology Manager's dependency view before any schema change
4. **Notify downstream owners** — if your change affects another team's application, contact them before promoting
5. **Submit for C2DAO review** — all production promotions for changes to shared artifacts require review
6. **Promote after approval** — merge to production only after C2DAO approval is documented
7. **Verify post-promotion** — check downstream applications and pipelines within 30 minutes of promotion

> **WARNING:** "I'll fix it on the main branch and promote later" is not a workflow. It is the description of how production incidents happen. Branch before you change anything.

---

## SECTION 7 — TM-30 VS. TM-40 DECISION BOUNDARY

**BLUF:** TM-30 owns the UI layer. TM-40 owns the code layer. When a requirement crosses the UI boundary, escalation is the correct action — not improvisation. Know the boundary before you encounter it in the field.

### 7-1. Full Decision Table

| Requirement | TM-30 Owns | TM-40 Track | Notes |
|---|---|---|---|
| Workshop multi-page application design and build | YES | — | Full TM-30 scope per Chapter 2 |
| Variable chains, conditional visibility, cascading filters | YES | — | Full TM-30 scope per Chapter 2 |
| Multi-source pipeline join with grain management | YES | — | Full TM-30 scope per Chapter 3 |
| Ontology Object Type and Link Type design | YES | — | Full TM-30 scope per Chapter 4 |
| Action schema design (no-code Actions) | YES | — | Full TM-30 scope per Chapter 5 |
| AIP Logic parameter configuration and monitoring | YES | — | Full TM-30 scope per Chapter 6 |
| Python / PySpark pipeline authoring | NO | TM-40L (SWE) | Refer when data volume or logic complexity exceeds Pipeline Builder |
| Incremental transform logic requiring @incremental decorator | NO | TM-40L (SWE) | TM-30 configures schedule; SWE authors the transform logic |
| TypeScript Functions on Objects (FOO) | NO | TM-40H (AI Eng) or TM-40L (SWE) | FOO requires TypeScript authoring |
| New AIP Logic workflow authoring | NO | TM-40H (AI Eng) | TM-30 configures existing workflows |
| Agent Studio workflow authoring | NO | TM-40H (AI Eng) | Above TM-30 scope |
| Statistical modeling, regression, Monte Carlo | NO | TM-40G (ORSA) | ORSA methodology required |
| ML model development and integration | NO | TM-40M (MLE) | Model development is code-layer |
| OSDK application development | NO | TM-40L (SWE) | Custom application code |
| Data product governance program management | TM-30 enforces standards | TM-40J (PM) for enterprise-level program coordination | PM track for cross-organizational governance programs |
| Data product documentation and taxonomy | TM-30 applies standards | TM-40K (KM) for organizational knowledge architecture | KM track for enterprise knowledge design |
| Source connector configuration (new connector types) | NO | TM-40L (SWE) | Existing connector configuration is TM-30 scope; new types are not |
| Custom data quality checks in code | NO | TM-40L (SWE) | UI-based quality checks are TM-30; code-based checks are TM-40L |

### 7-2. The Escalation Standard

Escalating is not failure. Escalating when a requirement exceeds your lane is the correct action. Attempting to build something that requires TM-40 capability at the TM-30 level produces:

- A fragile solution that breaks when the underlying data changes
- A solution that cannot be maintained by any TM-40 engineer (because it circumvents proper tool use)
- A C2DAO compliance violation if the workaround produces unauthorized data writes

**Document the requirement, identify the correct TM-40 track, and route it.** If you are uncertain which TM-40 track owns a requirement, refer to the escalation decision table in Section 9.

---

## SECTION 8 — ANTI-PATTERNS

**BLUF:** The following failures appear routinely in TM-30-level work across the formation. Recognize them before building. Most are easier to prevent than to fix after production deployment.

| # | Anti-Pattern | Symptom | Root Cause | Correction |
|---|---|---|---|---|
| 1 | **Production direct editing** | Builders make schema changes directly on the main branch; downstream applications break | Discipline gap; time pressure | Branch before every change, without exception; branch creation takes 90 seconds |
| 2 | **No downstream impact audit** | A property rename breaks three applications; discovery happens during a commander's brief | Assuming no one else uses your Object Type | Run the dependency audit in Ontology Manager before any schema change |
| 3 | **Wrong grain join** | Row count in output is 6x expected; downstream charts double-count units or vehicles | Not documenting grain of each source before joining | Pre-join checklist (Section 2-4) before every multi-source join |
| 4 | **Free-text status as filter** | Dashboard filters on `status = "FMC"` miss records where status was entered as "fmc" or "Fully Mission Capable" | Using string properties for controlled-vocabulary data | Enumerated properties with a controlled vocabulary; enforce at Action level |
| 5 | **Mutable primary key** | Objects duplicate or disappear when unit names or locations change | Using name or location fields as primary key | Use immutable IDs: UIC, NSN, EDIPI, Document Number |
| 6 | **Open access by default** | Sensitive readiness data is visible to all MSS users | Access control never configured | Default to private; add role-based access intentionally |
| 7 | **AIP Logic prompt modification without escalation** | Workflow output changes unexpectedly after "minor" parameter edits | TM-30 modifying prompt text that is TM-40H scope | TM-30 adjusts parameters only; any prompt text change routes to TM-40H |
| 8 | **Dashboard label uses internal field names** | Commander's brief shows column headers like `vehicle_fmc_pct` and `maint_completion_date` | Widget labels not customized from property name defaults | Replace all property-name labels with operational language before publishing |
| 9 | **Full record load on table open** | Dashboard is slow; users complain; operators abandon application | Table widget configured with no default filter | Require a filter selection before table loads, or set a practical default filter |
| 10 | **Variable with no default value** | Cascading filter chain breaks on first page load; user sees no data and assumes the system is broken | Workshop variables created without a default value | Always set a meaningful default value; test the page-load experience before publishing |
| 11 | **Action without validation rule** | Invalid values (negative readiness percentages, future maintenance dates, blank unit names) written to production Objects | Action configured without input validation | Add validation rules to every Action; test with boundary and invalid inputs |
| 12 | **Undocumented pipeline** | Three months after build, no one can explain what the pipeline does or why intermediate datasets exist | No inline documentation during build | Document dataset purpose, grain, owner, and downstream consumers in the dataset description field at creation time |
| 13 | **Incremental refresh on untrustworthy watermark** | Pipeline misses updates; stale data appears current | Configured incremental refresh without validating that source system watermarks are reliable | Validate watermark coverage before configuring incremental; default to full refresh if uncertain |

---

## SECTION 9 — ESCALATION DECISION TABLE

**BLUF:** When a requirement exceeds TM-30 scope, route it to the correct TM-40 specialist. Do not route everything to TM-40L because "it needs code." Each specialist has a lane.

| Signal | Route to | Why |
|---|---|---|
| Requirement needs Python or PySpark transform authoring, OSDK integration, or custom connector configuration | **TM-40L — Software Engineer** | Code-layer pipeline and application development is SWE lane |
| Requirement needs a new AIP Logic workflow authored from scratch, prompt engineering, Agent Studio, or TypeScript Functions on Objects | **TM-40H — AI Engineer** | LLM workflow design and AI reasoning layer is AI Eng lane |
| Requirement involves statistical analysis: regression, forecasting, simulation, Monte Carlo, decision support modeling | **TM-40G — ORSA** | Quantitative analysis methodology is ORSA lane; tools alone do not make analysis valid |
| Requirement needs a machine learning model built, trained, validated, or integrated into the Ontology | **TM-40M — ML Engineer** | Model development and inference pipelines are MLE lane |
| Requirement involves cross-organizational coordination, data product governance program, stakeholder management across multiple units or functional areas | **TM-40J — Program Manager** | Enterprise governance coordination is PM lane |
| Requirement involves building or restructuring a knowledge taxonomy, documentation architecture, or data product catalog for the organization | **TM-40K — Knowledge Manager** | Organizational knowledge architecture is KM lane |
| Requirement appears to need multiple specialist tracks (e.g., ML model + Workshop application + governance program) | **TM-40J (PM) as coordinator first**, then PM routes to other specialists | Complex requirements need a PM to coordinate scope and delivery across lanes |

> **NOTE:** When escalating, document the requirement clearly before routing — do not hand off a vague verbal description. Write down: what the user needs, what data is involved, what you have already assessed as TM-30 capable vs. not, and what the deadline is. A clear handoff accelerates TM-40 response.

---

## SECTION 10 — PRE-BUILD CHECKLIST

**BLUF:** Complete this checklist before beginning any TM-30 design or build task. If any item cannot be confirmed, resolve it before building. Building on an unconfirmed foundation produces rework.

| # | Item | Confirmed? |
|---|---|---|
| 1 | Operational requirement documented in writing — what decision this product supports, who the user is, what they need to see or do | |
| 2 | Scope boundary assessed — confirmed whether the requirement is fully within TM-30 scope or requires TM-40 escalation for any component | |
| 3 | Existing Ontology audited — checked whether Object Types, Link Types, or pipelines already exist that partially or fully address this requirement | |
| 4 | Source data identified — all upstream sources named, grain documented, data quality assessed | |
| 5 | Output grain defined — the required grain of each pipeline output and each Object Type documented before any pipeline is built | |
| 6 | Branch created — a development branch exists; no work will be performed on the main/production branch | |
| 7 | Naming convention confirmed — dataset, Object Type, property, pipeline, and application names are compliant with C2DAO standards before any artifact is created | |
| 8 | Access control plan defined — who will have access, at what permission level, and what is restricted | |
| 9 | Downstream impact assessed — if modifying an existing shared artifact, all downstream consumers identified and notified | |
| 10 | Human review step defined (if AIP Logic) — if the build includes AIP Logic configuration, the human review workflow is documented before configuration begins | |
| 11 | Test plan defined — how correctness will be verified: expected row counts, expected output values, user acceptance criteria | |
| 12 | C2DAO promotion path confirmed — know who will review and approve the production promotion before building begins | |

---

## SECTION 11 — GATING QUESTIONS FOR READINESS ASSESSMENT

Proceed to TM-30 task instruction when you can answer all six questions without consulting this guide.

**1. What is the difference between a TM-20 Builder and a TM-30 Advanced Builder in terms of accountability and downstream impact?**

A TM-20 builder's errors are typically self-contained. A TM-30 Advanced Builder's errors propagate to every downstream consumer of shared Ontology artifacts, pipelines, and applications. TM-30 accountability is formation-level.

**2. A pipeline joins vehicle maintenance records (one row per maintenance event) with a vehicle master table (one row per vehicle). What must be done before the join executes, and why?**

The maintenance records must be aggregated to the vehicle grain (e.g., count of events, date of most recent event per vehicle) before the join. Joining at different grains without aggregating first produces one output row per maintenance event — multiplying the vehicle count by the average events-per-vehicle and inflating all downstream metrics.

**3. You are about to rename a property on the `VehicleReadiness` Object Type that has been in production for six months. What must you do before making any change?**

Run a downstream dependency audit using Ontology Manager. Identify every Workshop widget, Contour analysis, Quiver dashboard, pipeline transform, and AIP Logic data binding that references the property by name. Notify owners of all affected artifacts. Make the change on a development branch. Coordinate with downstream owners to update their references before promotion. Promote only after all downstream consumers are tested and confirmed functional.

**4. What does TM-30 own in AIP Logic, and what requires escalation to TM-40H?**

TM-30 owns parameter configuration (temperature, max tokens, data filter bindings, NLQ synonyms, run schedule) and monitoring. Authoring new workflows, modifying prompt text, authoring TypeScript Functions on Objects, and integrating AIP Logic output with Actions that write to the Ontology are TM-40H scope.

**5. A commander's Workshop application is loading slowly because a table widget returns 200,000 vehicle records on page open. What is the correct fix?**

Configure a meaningful default filter that limits the initial query to a relevant subset (e.g., vehicles assigned to the commander's formation, or vehicles with a status requiring action). Alternatively, implement the "Apply Filters" button pattern so the table does not query until the user has set at least one filter. Do not increase server resources or accept slow load as a design characteristic.

**6. An analyst asks you to build a statistical regression model predicting equipment failure probability based on maintenance history. Is this TM-30 scope? If not, where does it route?**

Not TM-30 scope. Statistical modeling requiring regression analysis routes to TM-40G (ORSA). If the requirement also involves building an ML pipeline to serve the model at inference time, that component routes to TM-40M (ML Engineer). TM-30's contribution is the Workshop application that displays ORSA or MLE outputs — not the analysis or model itself.

---

## USAREUR-AF VIGNETTES

### Vignette A — 21st TSC Vehicle Readiness Dashboard

The 21st Theater Sustainment Command G4 needs a brigade-level vehicle readiness dashboard aggregating GCSS-A maintenance data across six subordinate brigades. The dashboard must show formation-level operational rate, drill to brigade level, and further to individual vehicles with deadline status.

**TM-30 design decisions:**

- **Pipeline grain:** `VehicleReadiness` Object Type at one row per vehicle per day. GCSS-A maintenance events (many per vehicle) aggregated in the pipeline before Ontology ingestion.
- **Pipeline type:** Incremental refresh — GCSS-A feeds update daily; full refresh on a 50,000-vehicle dataset is compute-expensive.
- **Watermark risk:** GCSS-A modification timestamps are not always updated on status-only changes. Mitigation: supplement watermark with a daily windowed full refresh of the prior 72 hours to catch missed updates.
- **Workshop pattern:** Summary → Detail. Page 1: formation-level rollup with RAG traffic lights. Page 2 (conditional on brigade selection): brigade fleet table sorted by deadline status. Page 3 (conditional on vehicle selection): individual vehicle maintenance history timeline.
- **Access control:** G4 section can view and export. Subordinate S4s can view their own brigade, not others. Dashboard visible to commanding general read-only.
- **Escalation trigger:** If the requirement adds a predictive maintenance model, route the model to TM-40M; TM-30 builds the Workshop display layer only.

### Vignette B — V Corps SITREP Data Quality Workflow

V Corps G3 identifies that incoming SITREPs contain inconsistent status codes — "RED", "red", "R", and "DEADLINE" are all used interchangeably, breaking dashboard filters. The requirement is to standardize status at ingestion and surface data quality issues to the submitting units.

**TM-30 design decisions:**

- **Ontology fix:** Change `sitrep_status` from a free-text property to an enumerated property with controlled vocabulary: `{FMC, PMC, NMC, DEADLINE}`. This is a TM-30 Ontology design task.
- **Pipeline fix:** Add a normalization transform that maps incoming string values to the controlled vocabulary before Ontology ingestion. This is a TM-30 Pipeline Builder task if achievable with no-code transforms. If the normalization logic requires a Python lookup table, escalate the transform to TM-40L; TM-30 owns the Ontology property design regardless.
- **Action:** Configure a SITREP submission Action that validates status against the controlled vocabulary before write; invalid submissions return an error message to the submitting user.
- **Data quality surface:** Add a Workshop widget (visible to G3 data steward only) showing submission error log: unit, submission timestamp, invalid value submitted, required value.
- **Branch discipline:** All Ontology schema changes go through a development branch with full downstream impact audit before promotion. Estimated downstream consumers: 14 Workshop widgets, 3 Contour analyses, 2 pipeline transforms.

---

## TRANSITION TO TM-30

This guide establishes the mental models applied throughout TM-30. TM-30 task instruction assumes this conceptual foundation. It will not re-explain why branch workflow is mandatory, why grain management determines pipeline correctness, or why primary key stability is the most consequential Ontology design decision.

Proceed to TM-30, Chapter 1, when you can answer the six gating questions in Section 11 without referencing this guide.

When TM-30 qualification is complete, select a TM-40 specialist track based on assigned duties and billet. All specialist tracks (TM-40G through TM-40O) require TM-30 as a hard prerequisite.

---

## NATO AND COALITION STRATEGIC GUIDANCE

> The following are strategic guidance documents — not doctrine — that inform MSS training design and operational context.

| Document | Authority | Relevance |
|---|---|---|
| NATO Data Strategy for the Alliance (Feb 2025) | NATO | Alliance-wide data governance mandate — governs coalition data sharing requirements applicable to TM-30 ontology design |
| NATO Data Quality Framework for the Alliance (Aug 2025) | NATO | Quality governance and metrics — applicable to multi-national data products built at TM-30 level |

---

## CURRICULUM NOTES

**Prerequisites:** TM-10 (Maven User) and TM-20 (Builder) are REQUIRED before beginning TM-30 or this guide. The Data Literacy Technical Reference is also required reading.

**Next steps after TM-30:**
- WFF tracks (TM-40A–F): for Intelligence, Fires, Movement and Maneuver, Sustainment, Protection, and Mission Command operators. Prereq is TM-30 (required).
- Specialist tracks (TM-40G–O): ORSA, AI Engineer, ML Engineer, Program Manager, Knowledge Manager, Software Engineer, UX Designer, Platform Engineer. Prereq is TM-30 (required).

**Peer specialist cross-references:**
- **TM-40H (AI Engineer):** TM-30 configures AIP Logic workflows that TM-40H authors. The boundary is clear: TM-30 adjusts parameters; TM-40H changes prompts, workflow logic, and Ontology write-back integrations.
- **TM-40L (Software Engineer):** TM-30 builds no-code pipelines; TM-40L authors Python/PySpark transforms when Pipeline Builder cannot handle the logic. Know the boundary before routing work.
- **TM-40G (ORSA):** TM-30 builds the Workshop display layer for ORSA analysis outputs. The ORSA designs the methodology and owns the analytical validity; TM-30 makes it accessible to operators.
- **TM-40K (Knowledge Manager):** TM-30 applies naming and documentation standards that TM-40K establishes. When the naming standard is unclear or the data catalog structure needs redesign, TM-40K is the authority.

*CONCEPTS GUIDE — TM-30 COMPANION, ADVANCED BUILDER, MAVEN SMART SYSTEM (MSS)*
*Headquarters, United States Army Europe and Africa, Wiesbaden, Germany, 2026*
*Distribution restriction: Distribution authorized to U.S. Government agencies and their contractors only. Other requests must be referred to Headquarters, C2DAO, Wiesbaden, Germany.*
