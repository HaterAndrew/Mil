# CONCEPTS GUIDE — TM-20 COMPANION — BUILDER · MAVEN SMART SYSTEM (MSS)

> **BLUF:** A Builder is a trained MSS user who creates pipelines, Ontology configurations, and applications using no-code tools. Builders are not operators, and they are not Advanced Builders or developers. Understanding where you sit in this hierarchy determines what you are authorized — and equipped — to build.
> **Purpose:** Develops the mental models required to design, build, and govern no-code applications and data pipelines on MSS effectively. Read before beginning TM-20 task instruction.
> *HQ USAREUR-AF · v1.0 · 2026 · DISTRIB: USG only*

---

## SECTION 1 — WHAT IS A BUILDER?

**BLUF:** A Builder is a trained MSS user who creates pipelines, Ontology configurations, and applications using no-code tools. Builders are not operators, and they are not Advanced Builders or developers. Understanding where you sit in this hierarchy determines what you are authorized — and equipped — to build.

### 1-1. The Three-Level Spectrum

MSS users operate across a defined capability spectrum. Each level has a distinct lane.

| Level | Who They Are | What They Build | What They Touch |
|---|---|---|---|
| **Operator (TM-10)** | All MSS users with read access | Nothing; they consume | Dashboards, reports, queries — read only |
| **Builder (TM-20)** | Staff with builder access and TM-20 certification | No-code pipelines, Object Types, simple Actions, Workshop apps | Pipeline Builder, Ontology UI, Workshop |
| **Advanced Builder (TM-30)** | Technically experienced staff | Multi-source pipelines, complex Ontology patterns, AIP Logic, multi-page apps | All TM-20 tools plus @incremental, SQL/Python, TypeScript Functions |
| **Specialist (TM-40G–L)** | Domain experts with TM-30 base | ML models, OSDK apps, AI workflows, statistical pipelines | All prior tools plus Code Workspaces, AIP Logic, Agent Studio, OSDK |

A TM-20 Builder builds pipelines and applications using drag-and-drop, form-based tools — no code. When a requirement demands code, custom functions, or complex conditional logic, a Builder stops and escalates. That is not a failure. That is correct execution.

### 1-2. The Builder's Relationship to the Governance Chain

Builders do not operate in isolation. Every build activity sits inside a governance chain that constrains what can be built, on what data, with what access.

```
ARMY CIO
  |  Army Data Plan; CIO Data Stewardship Policy (Apr 2024)
  v
USAREUR-AF C2DAO
  |  Theater-level data governance authority
  |  Approves new data sources, Ontology changes, access policies
  v
UNIT DATA STEWARD
  |  First point of contact for all data questions
  |  Approves access lists, ingestion requests, write-back authorizations
  v
FUNCTIONAL DATA MANAGER
  |  Day-to-day domain oversight
  v
BUILDER (YOU)
     Build within approved scope, on approved data, against approved requirements
```

A Builder who acts outside this chain — ingesting unauthorized data, creating Object Types without Data Steward coordination, granting access beyond the approved list — creates compliance findings that affect the whole team. When in doubt, stop and ask your Data Steward.

### 1-3. When to Build vs. When to Escalate

**Rule of thumb:** If you cannot complete the requirement using only Pipeline Builder nodes, Ontology Manager form fields, and Workshop widget properties — escalate. Do not approximate a TM-30 solution with TM-20 tools.

| Situation | Builder Action |
|---|---|
| Requirement fits within Pipeline Builder, Ontology UI, and Workshop drag-and-drop | Build it |
| Requirement needs a single-source filter/rename/join/aggregate | Build it |
| Requirement needs a simple, single-step form Action | Build it |
| Requirement needs multi-step conditional routing, approval chains, or multi-record writes | Escalate to TM-30 |
| Requirement needs @incremental logic or watermark-based pipeline refresh | Escalate to TM-30 |
| Requirement needs Python, PySpark, SQL, or TypeScript | Escalate to TM-40L (Software Engineer) |
| Requirement needs AIP Logic, Agent Studio, or AI-augmented workflows | Escalate to TM-40H (AI Engineer) |
| Requirement needs ML model integration | Escalate to TM-40I (ML Engineer) |
| Requirement needs complex many-to-many Ontology modeling | Escalate to TM-30 |

### 1-4. The Three Pre-Build Questions

Answer these three questions in order before opening any build tool. Do not skip ahead.

**Q1: Who is my user and what decision are they making?**

The application or pipeline you build exists to help a specific person make a specific decision or take a specific action. Name that person and that decision before touching the platform. Vague requirements produce useless builds.

| Clear Requirement | Unclear Requirement |
|---|---|
| "The S4 NCO at Rose Barracks needs to see which vehicles are deadlined by class, updated daily, to prioritize morning maintenance scheduling." | "The S4 needs a readiness dashboard." |
| "The battalion XO needs personnel fill by company before the Monday 0800 briefing so they can report up to brigade." | "G2 wants to see unit data." |

If you have an unclear requirement, get a clearer one before you build. Resolving ambiguity before building takes 30 minutes. Rebuilding after delivering something wrong takes days.

**Q2: What data do I need and where does it come from?**

Map the pipeline before building it:

```
DECISION REQUIREMENT       DATA ELEMENTS NEEDED         SOURCE SYSTEM
"Which vehicles are  →  Equipment ID, status, class, →  GCSS-A (via existing
 deadlined by fleet?"    location, deadline reason        ingestion pipeline)
```

Verify the data exists and is already in MSS before designing anything that depends on it. If the data is not in MSS, you have an ingestion problem — not a Workshop problem. Ingestion decisions require Data Steward coordination.

**Q3: Where does my work fit in the three-phase workflow?**

| Phase | What Happens | Pre-Check |
|---|---|---|
| Phase 1 — Pipeline Builder | Data ingested, cleaned, output to curated dataset | Is source data already in MSS and approved for ingestion? |
| Phase 2 — Ontology | Object Type created, backed by curated dataset | Does an existing Object Type already cover this? |
| Phase 3 — Workshop | User-facing application assembled | Is the Ontology solid before I start the app? |

Build bottom-up. Phase 1 must be complete before Phase 2. Phase 2 must be complete before Phase 3. An application built on an unstable pipeline is a liability, not a product.

---

## SECTION 2 — ETL FUNDAMENTALS

**BLUF:** ETL — Extract, Transform, Load — is the three-step process that takes raw data from a source system and produces clean, reliable output your application can use. Pipeline Builder is MSS's no-code ETL tool. Understand ETL conceptually before you touch a node.

### 2-1. What ETL Means in Plain Language

**Extract:** Pull data from a source system. In MSS, this means connecting a Pipeline Builder source node to a GCSS-A feed, a SharePoint file, or an existing MSS dataset.

**Transform:** Clean, reshape, or filter the data. Select only the columns you need. Rename system codes ("veh_status_cd") to plain English ("Vehicle Status"). Filter to your unit's UICs. Join two tables to combine vehicle records with maintenance logs.

**Load:** Write the processed result to a destination dataset in MSS. That output dataset becomes the foundation for your Ontology Object Type.

**USAREUR-AF example:**

| Step | What Happens | MSS Tool |
|---|---|---|
| Extract | Pull vehicle records from the GCSS-A connector — all UICs, all statuses, all classes | Source node in Pipeline Builder |
| Transform | Filter to your brigade's UICs only; rename "veh_status_cd" to "Vehicle Status"; drop columns not needed for readiness reporting | Filter node, Select Columns node |
| Load | Write result to `/VCORPS-READINESS/curated/gcss_a_vehicles_curated` | Output Dataset node |

The curated dataset feeds the `VehicleStatus` Object Type in the Ontology, which feeds a Workshop readiness application the S4 uses every morning.

### 2-2. Extract: Source Systems and Ingestion Boundaries

Sources available to TM-20 Builders are limited to pre-authorized connectors and existing MSS datasets. You do not create new connectors or modify connector configurations. You use what has been approved.

> **WARNING:** Before connecting any new data source, coordinate with your unit Data Steward and the USAREUR-AF C2DAO. Unauthorized ingestion of operational data — even from Army systems — may violate Army CIO policy and create compliance findings. The approval requirement applies even if you personally have access to the source system.

**Authorized source types for TM-20 Builders:**

| Source Type | Example | Who Authorizes |
|---|---|---|
| Existing MSS dataset | Another team's curated SITREP feed | Data Steward confirmation that sharing is approved |
| Pre-built connector | GCSS-A vehicle feed, SharePoint file | C2DAO approval for initial connector; Data Steward for each new use |
| Manual file upload (exceptional) | One-time CSV of exercise data | Data Steward written approval, marked FOUO or below |

Document all ingestion sources in your pipeline description field. If you cannot name the authorizing official and the date of approval, the ingestion is not authorized.

### 2-3. Transform: What Is Appropriate at TM-20 Level

TM-20 transforms are limited to the no-code nodes available in Pipeline Builder. These cover the majority of operational data requirements.

| Transform Operation | Pipeline Builder Node | TM-20? |
|---|---|---|
| Filter rows by column value, date range, or null | Filter | Yes |
| Select, rename, reorder, or drop columns | Select Columns | Yes |
| Join two datasets on a shared key | Join | Yes |
| Aggregate (count, sum, average, group by) | Aggregate | Yes |
| Append (union) two datasets with matching schemas | Append | Yes |
| Remove exact duplicate rows | Deduplicate | Yes |
| Parse dates from string format | Select Columns (type cast) | Yes |
| Multi-step conditional business logic | — | **No — escalate to TM-30** |
| Deduplication across sources with fuzzy matching | — | **No — escalate to TM-30** |
| Watermark-based incremental processing | — | **No — escalate to TM-30** |
| Custom Python/SQL transformations | — | **No — escalate to TM-40L** |

> **CAUTION:** Do not attempt to approximate complex logic using chains of simple nodes. A Builder who builds a 20-node pipeline to work around missing TM-30 capability produces something fragile, undocumented, and impossible for a replacement to maintain. Escalate when the requirement exceeds TM-20 tools.

### 2-4. Load: Writing to a Dataset vs. Writing to the Ontology

When your pipeline runs, it writes its output to a Foundry dataset. That dataset then backs an Ontology Object Type. These are two separate concepts with separate purposes.

| Layer | What It Is | Written By |
|---|---|---|
| **Dataset** | A managed table in Foundry. Raw storage. No semantics — just columns and rows. | Pipeline Builder output node |
| **Ontology Object Type** | A semantic representation of a real-world entity, backed by a dataset. Has properties, links, and actions. | Ontology Manager configuration; not a write target for pipeline output |

**Write to a dataset** when: your pipeline produces clean output that needs to be available for Ontology configuration or for other pipelines to consume.

**Write to the Ontology (via Actions)** when: a user needs to submit a form in Workshop that updates a property on an existing Object (e.g., submitting a maintenance status update). Actions write back to the dataset that backs the Object Type.

A common Builder misconception: "I need my pipeline to update the Ontology." Pipelines do not update Ontology configurations — they update the datasets those configurations read from. The Ontology reads from the dataset automatically on refresh.

### 2-5. Data Grain: What It Is, Why It Matters, and How Fan-Out Destroys It

**Data grain** is the level of detail represented by one row in a dataset. Every pipeline and every Object Type has a grain. Know the grain of your data before you build anything.

| Dataset | Grain (what one row represents) |
|---|---|
| GCSS-A vehicle status feed | One vehicle, one reporting date |
| SITREP feed | One SITREP submission, one unit, one report period |
| Personnel readiness | One soldier, one snapshot date |
| Maintenance log | One maintenance event, one vehicle, one date |

**Why grain matters:** Your Object Type's primary key must map to the grain. If your pipeline produces one row per vehicle per day and you set the primary key to `vehicle_id`, you get one Object per vehicle — which object represents today's record vs. yesterday's? The system will arbitrarily pick one. Primary key must uniquely identify one row at the grain you intend.

**Fan-out: how a join multiplies rows and destroys grain**

Fan-out occurs when a join creates more rows than the left dataset because the right dataset has multiple matching rows for each key. The result is incorrect aggregations and double-counted metrics.

**Example — equipment readiness joined to maintenance log:**

| Source | Rows | Grain |
|---|---|---|
| vehicles | 20 rows | One row per vehicle |
| maintenance_events | 60 rows | One row per maintenance event (3 events per vehicle on average) |

After an inner join on `vehicle_id`:

| Join Type | Result Rows | What Happened |
|---|---|---|
| Inner join on `vehicle_id` | 60 rows | Each vehicle now appears 3 times — once per maintenance event |
| Intended result | 20 rows | One row per vehicle with latest maintenance status |

A Workshop table built on this dataset would show 60 vehicles instead of 20. A count metric would show "60 vehicles" when the fleet is 20. The fix is to aggregate maintenance events to one-per-vehicle (latest event) before joining. Know your grain and protect it through every transform.

> **NOTE:** Unexpected row multiplication after a join is the most common TM-20 data quality problem. Always check row counts before and after each join. If the count grows beyond what you expect, stop and investigate before proceeding.

### 2-6. Idempotency: Why Pipelines Should Produce the Same Output If Re-Run

An **idempotent** pipeline produces identical output every time it runs on the same input data, regardless of how many times it runs. A non-idempotent pipeline appends duplicate rows, changes row counts on each run, or behaves differently based on internal state.

TM-20 Builders using Pipeline Builder's output node (full refresh mode, which is the default) get idempotency automatically — the output dataset is overwritten on each build. Do not change the output mode to append unless your Data Steward has explicitly authorized it and your pipeline includes deduplication logic.

**Why idempotency matters for USAREUR-AF operations:** If a pipeline runs twice due to a platform retry, the output dataset should look the same as if it ran once. A readiness report showing double the actual equipment count because the pipeline appended twice is an operational data integrity failure.

---

## SECTION 3 — FOUNDRY DATA ARCHITECTURE (BUILDER VIEW)

**BLUF:** MSS is built on Palantir Foundry. As a Builder, you work across four layers of the Foundry architecture. Understand each layer's purpose and its relationship to the others before building.

### 3-1. The Four Layers You Work In

```
┌─────────────────────────────────────────────────────────────────┐
│  SOURCE SYSTEM                                                  │
│  GCSS-A | SharePoint | DTMS | external feeds                   │
└────────────────────────────┬────────────────────────────────────┘
                             │ Extract (connector/source node)
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 1: DATASETS                                              │
│  Raw, staging, curated tiers                                   │
│  Managed tables: schema, rows, history                         │
│  Folders in Compass: /raw/ → /staging/ → /curated/            │
└────────────────────────────┬────────────────────────────────────┘
                             │ Transform + Load (Pipeline Builder)
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 2: PIPELINE BUILDER                                      │
│  Visual ETL: Filter → Select → Join → Aggregate → Output       │
│  Scheduled runs; Build Log monitoring                          │
│  Produces curated datasets consumed by Layer 3                 │
└────────────────────────────┬────────────────────────────────────┘
                             │ Back Object Types
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 3: ONTOLOGY                                              │
│  Object Types: UnitStatus, VehicleReadiness, MaintenanceRecord │
│  Link Types: assignedTo, reportedBy, locatedAt                 │
│  Actions: Submit SITREP Update, Mark Maintenance Complete      │
│  Semantic layer: turns tables into meaningful connected objects │
└────────────────────────────┬────────────────────────────────────┘
                             │ Read from Ontology
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 4: APPLICATIONS (TM-20 scope)                           │
│  Workshop: drag-and-drop user applications                     │
│  Contour: saved exploratory analysis                           │
│  Quiver: self-service analytics and dashboards                 │
│  AIP Logic / Agent Studio: AI workflows (TM-40H scope only)   │
└─────────────────────────────────────────────────────────────────┘
```

### 3-2. Datasets: Raw Storage, Schema, and Immutability

A Foundry dataset is a managed table. It has a schema (column names and data types), rows of data, and a build history (you can view past versions). The dataset path is permanent — renaming or moving a dataset breaks all downstream references.

**Three-tier dataset pattern:**

| Tier | Folder | Contents | Who Reads It |
|---|---|---|---|
| **Raw** | `/raw/` | Data exactly as it arrived from source — no transforms | Staging pipeline |
| **Staging** | `/staging/` | Cleaned, validated, intermediate state | Curated pipeline |
| **Curated** | `/curated/` | Publication-ready, Ontology-backed | Ontology Object Types, Workshop |

Never build a Workshop application or Ontology Object Type directly on a raw dataset. Raw data has not been validated, renamed, or filtered. Expose only curated data to application users.

### 3-3. Pipeline Builder: The Transform Layer and the DAG

Pipeline Builder implements a **DAG** — Directed Acyclic Graph. Each node you add is a step in the graph. Data flows from left (source) to right (output). Cycles (loops) are not possible — data can only flow forward.

The DAG concept matters when troubleshooting. When a pipeline fails, the failing node is highlighted in the graph. Because data flows forward, a failure at any node means all downstream nodes did not execute. Identify the root-cause node — not just the last error message — before attempting a fix.

### 3-4. Ontology: The Semantic Layer

The Ontology answers the question: "What does this data mean?" A dataset row with columns `veh_id`, `status_cd`, `uic` is meaningless without context. A `VehicleReadiness` Object with properties "Vehicle ID," "Status," and "Unit" is understandable to an operator who has never seen the underlying dataset.

The Ontology is shared. Every Object Type, Link Type, and Action you configure is available to every Workshop application (and every user) with access to your environment. This is why branching and peer review before promotion are non-negotiable.

### 3-5. Workshop: The Presentation Layer

Workshop reads exclusively from the Ontology. It does not read directly from datasets. If your Ontology Object Type is broken, your Workshop application shows no data — regardless of how well the pipeline built.

This dependency chain is the reason for the build-order rule: Pipeline first. Ontology second. Workshop third.

---

## SECTION 4 — ONTOLOGY CONCEPTS FOR BUILDERS

**BLUF:** The Ontology is the most consequential thing a TM-20 Builder configures. A pipeline mistake affects one output dataset. An Ontology mistake affects every application reading that Object Type. Understand the core concepts before configuring anything.

### 4-1. Object Type: What It Represents and the Primary Key

An **Object Type** is a named entity in MSS that represents a real-world thing: a unit, a soldier, a vehicle, a maintenance record, a SITREP submission. It is backed by a curated dataset. Each row in that dataset becomes one Object instance.

The **Primary Key** is the property that uniquely identifies each object. It must be unique across every row in the backing dataset at the intended grain.

| Object Type | Backing Dataset Grain | Correct Primary Key |
|---|---|---|
| `UnitStatus` | One row per unit per report date | `unit_id` + `report_date` (composite) or a generated unique ID |
| `VehicleReadiness` | One row per vehicle (latest status only) | `vehicle_id` |
| `SoldierReadiness` | One row per soldier | `dodid` |
| `MaintenanceRecord` | One row per maintenance event | `event_id` |

> **WARNING:** If your primary key column is not unique in the backing dataset, objects will overwrite each other. Preview your Object Type immediately after creation. If the object count is lower than your row count, you have a primary key collision — fix the dataset before continuing.

### 4-2. Property: Type Immutability and Why It Matters

A **Property** is a configured attribute on an Object Type, backed by a column in the dataset. Each property has a data type: String, Number, Boolean, Date, or Timestamp.

**Type immutability** means that once a property's type is set, changing it later requires deleting and recreating the property — and updating every Workshop application that references it. Choose types carefully the first time.

| Data | Correct Type | Common Mistake | Consequence |
|---|---|---|---|
| Readiness percentage (85.5) | Number | String | Cannot sort numerically; cannot use in chart Y-axis |
| Report date (2026-03-14) | Date | String | Cannot filter by date range; cannot sort chronologically |
| FMC/NMC status flag | Boolean | String | Filtering is verbose; conditional visibility logic breaks |
| DODID (0001234567) | String | Number | Leading zeros dropped; joins fail on mismatch |

**Rule:** If a value will ever be used in math, sort by value, or date-range filtering — use the correct numeric or date type. If a value is a code or identifier that will only be matched exactly — use String, even if it looks like a number.

### 4-3. Link Type: Relationships, Cardinality, and the Right Use Case

A **Link Type** defines a relationship between two Object Types. Links allow Workshop applications to navigate from one Object to related Objects — from a `UnitStatus` to all `SoldierReadiness` records for that unit, for example.

**Cardinality** describes the nature of the relationship:

| Cardinality | What It Means | Example |
|---|---|---|
| **Many-to-One** | Many source objects → one target object | Many soldiers assigned to one unit |
| **One-to-One** | One source → one target | One vehicle → one current maintenance record |
| **Many-to-Many** | Many source → many target | Soldiers with multiple qualifications; qualifications held by multiple soldiers — requires junction dataset (TM-30 scope) |

**USAREUR-AF example:** A `SoldierReadiness` Object Type linked to `UnitStatus` via `assignedTo` (many-to-one). The foreign key in `SoldierReadiness` is `unit_id`. The primary key on `UnitStatus` is `unit_id`. When the link is configured, clicking a `UnitStatus` object in Workshop shows all soldiers assigned to that unit.

**Common Link Type mistakes:**

| Mistake | Why It Happens | Why It's Harmful |
|---|---|---|
| Using an ad-hoc property ("Unit ID text field") instead of a Link Type | Faster to configure | Workshop cannot navigate to linked objects; relationship is not semantically represented; breaks search and filtering |
| Setting cardinality to many-to-one when the relationship is many-to-many | Did not check for multiple matching rows | Broken links; incomplete data display; silent data loss |
| Naming a link type with a noun instead of a verb phrase | Doesn't know the convention | Confusing Ontology; fails naming governance review |

### 4-4. Actions: What They Are and How They Differ from Pipeline Writes

An **Action** is a user-triggered operation that writes a value back to an Object's backing dataset. Actions allow operators to submit SITREP updates, mark maintenance complete, or record a status change — directly from a Workshop form, without touching the dataset directly.

**Actions vs. pipeline writes:**

| Write Method | Who Triggers It | When | Example |
|---|---|---|---|
| **Pipeline output** | Automated schedule or manual build | When the pipeline runs | Nightly refresh of vehicle status from GCSS-A |
| **Action** | An operator submitting a form in Workshop | On demand, any time | S4 NCO marks a vehicle as returned from maintenance |

TM-20 Actions are single-step and form-based: one form, one submit, one field updated. Multi-step Actions with conditional routing or approval chains are TM-30 scope.

> **CAUTION:** Actions that write to datasets affect all downstream applications immediately. Test every Action on a development branch with test data — never on live operational records — before promoting to production.

### 4-5. Common Ontology Mistakes

| Mistake | Correct Approach |
|---|---|
| Using a free-text property to store a foreign key instead of creating a Link Type | Create the Link Type with proper foreign key mapping |
| Naming properties with system codes ("veh_status_cd") instead of plain English ("Vehicle Status") | Always use plain English, title case, in property display names |
| Creating a new Object Type when an existing one already covers the use case | Check existing Object Types in Ontology Manager before creating; consult your Data Steward |
| Skipping the primary key configuration | Every Object Type must have a primary key; object previews will be unreliable without one |
| Configuring the Ontology before the curated dataset has a stable schema | Stabilize the pipeline and curated dataset schema before configuring the Ontology |

---

## SECTION 5 — WORKSHOP APPLICATION DESIGN

**BLUF:** Workshop is the application layer operators see every day. A poorly designed Workshop app creates friction, errors, and distrust. Design for the operator's decision — not for your technical comfort.

### 5-1. Widget Selection: Use the Right Tool for the Decision

| Widget | Best For | Do Not Use When |
|---|---|---|
| **Table** | Displaying a list of records that users need to scan, sort, or select from | The user only needs to see an aggregate number — use a Metric Tile |
| **Bar Chart** | Comparing a value across discrete categories (readiness by battalion) | The categories are too many to read on screen (>15); use a Table instead |
| **Line Chart** | Showing a trend over time (equipment readiness rate over 30 days) | There is only one data point — meaningless as a trend |
| **Pie/Donut Chart** | Showing proportions of a whole (FMC vs. NMC composition) | There are more than 5–6 categories; slices become unreadable |
| **Metric Tile** | Displaying a single KPI (total deadlined vehicles: 14) | The metric is not immediately interpretable without context |
| **Filter — Dropdown** | Letting users restrict data by a known category (unit, status, class) | The distinct values are > 50; use a Search filter instead |
| **Filter — Date Range** | Restricting data to a time window | Your data has no date property to filter on |
| **Form / Action Widget** | Allowing operators to submit status updates | The Action requires multi-step logic or conditional fields — escalate to TM-30 |
| **Map** | Displaying geographically distributed data (unit locations, logistics nodes) | Your data has no latitude/longitude or geocodable address |
| **Object Explorer** | Showing detailed properties of one selected object | Users need to compare multiple objects — use a Table |

### 5-2. Filter Logic: How Filters Work and Why Default Values Matter

A filter widget in Workshop sets a **variable** — a value that other widgets read to restrict their data. When a filter is unset (no selection), the behavior depends on your configuration.

**Connected filter:** The filter variable is wired to the Object Type source of a downstream widget. When the filter is set, the widget shows only matching objects. When the filter is cleared, the widget shows all objects.

**Unconnected filter:** The filter widget is present but not wired to any widget source. It displays but has no effect. This is always a configuration error — remove unconnected filters.

**Default values — why they matter:**

| Default Value Set? | What the Operator Sees on Page Load | Risk |
|---|---|---|
| Yes — e.g., filter defaults to current user's unit | Relevant data immediately visible | None; good design |
| No — filter blank on load | All records across all units displayed | Slow page load; operator confused; may see data outside their area |
| Yes — default set to an invalid value | Zero records displayed; page looks broken | Operator loses trust in the application |

> **CAUTION:** For operational data applications, always set a meaningful default filter value. An application that loads 50,000 records with no filter is a performance and security risk. Filter to a relevant default scope — the user's unit, the current report period, active records only.

### 5-3. Role-Based Access: Editor vs. Viewer, and Why Actions Must Be Tested as Viewer

Workshop applications have two access roles:

| Role | Can Do | Cannot Do |
|---|---|---|
| **Viewer** | Use the published application: view data, apply filters, submit Actions they are authorized for | Edit application layout, modify widget configuration, access edit mode |
| **Editor** | All Viewer rights plus modify application layout and widgets | Not the role for operational users |

**Critical rule:** Test your Actions as a Viewer before publishing. Builders who test only in edit mode often find that Actions behave differently — or are invisible — when a Viewer accesses the published application. A "Submit SITREP Update" Action tested only by the Builder in edit mode and never tested by a Viewer is not tested.

**Pre-publish access test procedure:**

1. Publish the application to a development URL.
2. Open the application in an incognito browser window (or ask a team member without Editor access to open it).
3. Confirm all expected widgets display.
4. Confirm all expected Actions are visible and submittable.
5. Submit a test Action using test data. Confirm the backing dataset reflects the write.
6. Confirm data the Viewer should not see is not visible.

### 5-4. Performance Considerations

| Issue | Cause | Fix |
|---|---|---|
| Page loads slowly | Object Type has no default filter; all records load on open | Set a meaningful default filter that limits initial record count to <1,000 |
| Table is slow to scroll | Displaying too many columns; no pagination | Remove unnecessary columns; enable pagination |
| Chart takes > 10 seconds to render | Source Object Type has 50,000+ objects with no pre-aggregation | Aggregate in Pipeline Builder before the Ontology; chart only aggregated data |
| Application times out | Joining two large datasets in Workshop widget config | Perform joins in Pipeline Builder, not Workshop; Workshop is for display, not computation |
| Action form submits slowly | Action writes to a large dataset without indexing | Escalate to TM-30 for optimization |

### 5-5. Publishing and Sharing

Before publishing any Workshop application:

- [ ] All widgets display correct data in preview mode.
- [ ] All filters have default values set.
- [ ] All Actions tested as Viewer.
- [ ] Access list reviewed against Data Steward approved list.
- [ ] Application description completed: purpose, intended users, owning unit, data steward POC.
- [ ] Development branch peer-reviewed and approved for merge.
- [ ] Application promoted from development branch to main branch before publishing.

> **WARNING:** Do not publish a Workshop application directly from a development branch. Publishing from a development branch makes development-state data and configurations visible to all authorized users. Promote to main branch first.

---

## SECTION 6 — BRANCHING AND CHANGE MANAGEMENT

**BLUF:** Branching protects the production environment from development mistakes. Every change to a shared pipeline, Object Type, or Workshop application happens on a branch — not on main. No exceptions.

### 6-1. Why Branching Exists

The Ontology and pipelines on MSS are shared resources. A change made directly to the main branch immediately affects every user and every downstream application. A pipeline edit that breaks a filter on the main branch breaks the S4's morning readiness view for all of V Corps.

A development branch is an isolated copy of the resource where you can build and break things without affecting production. Changes only reach production after they are reviewed and merged.

### 6-2. Dev Branch Lifecycle

```
CREATE branch (dev-[feature] or dev-[lastname])
    |
    | Build, configure, test in isolation
    ▼
BUILD — verify no build errors
    |
    ▼
TEST — preview data; test Actions as Viewer; confirm row counts
    |
    ▼
PEER REVIEW — second Builder or Data Steward reviews your changes
    |
    ▼
PROMOTE (merge) to main branch
    |
    ▼
VERIFY — confirm production resource reflects intended changes
```

**Branch naming convention:**

| Purpose | Branch Name Format | Example |
|---|---|---|
| New feature or pipeline | `dev-[feature-name]` | `dev-sitrep-ingestion` |
| Personal development work | `dev-[lastname]` | `dev-rodriguez` |
| Bug fix | `fix-[issue-description]` | `fix-vehicle-filter` |

### 6-3. What "Promoting" Means

Promoting a branch merges your branch's changes into the main branch, making them visible to all users. In Foundry, this is typically called a **branch promotion** or **merge**. The platform shows a diff of what changed — which nodes were added, which properties were modified.

Before promoting:
- Pipeline builds on your branch with zero errors.
- Output data previewed and verified against known-good values.
- Actions tested as Viewer.
- Peer reviewer has confirmed the changes.

After promoting:
- Open the main branch and confirm the change is present.
- For pipelines: trigger a manual build on the main branch and confirm success.
- For Ontology changes: preview the Object Type and confirm expected objects and properties are visible.
- For Workshop apps: open the published application as a Viewer and confirm expected behavior.

### 6-4. Rollback Procedure

If a promoted change causes a production issue:

1. Identify the change that caused the problem using the Foundry build log and branch history.
2. Contact your Data Steward immediately — do not attempt to fix a production data issue silently.
3. If the issue is a pipeline error: revert the pipeline to the previous version using Foundry's version history (click the pipeline → History → select last known-good version → Restore).
4. If the issue is an Ontology change: create a new branch, revert the Object Type or Link Type configuration to its previous state, get peer review, and promote the revert.
5. Document the failure, the cause, and the remediation in the pipeline or resource description field.
6. Report the incident to your Data Steward within 24 hours regardless of severity.

> **NOTE:** Foundry maintains resource version history. You can always view and restore a previous version. Do not delete or overwrite broken resources in an attempt to hide mistakes — the history is visible and deletions may be irreversible.

---

## SECTION 7 — NAMING CONVENTIONS AND GOVERNANCE

**BLUF:** Naming conventions exist because MSS is shared infrastructure. A resource named "dashboard1" or "test_pipeline_final_v2" is a resource no one can maintain, find, or trust. Follow conventions exactly — non-compliant resources will be renamed or removed.

### 7-1. Why Naming Conventions Exist

MSS is operated by dozens of teams across USAREUR-AF, V Corps, 21st TSC, and 7th ATC. A resource named ambiguously:

- Cannot be found by a new team member who inherits the project.
- Cannot be audited by the C2DAO during governance reviews.
- Cannot be safely deprecated without verifying downstream consumers first.
- Creates confusion when similar datasets exist for different units or time periods.

A resource named following convention can be found, understood, and maintained by anyone with appropriate access — including your replacement, six months after you've moved to a new assignment.

### 7-2. Dataset Naming: Domain, Entity, and Grain

**Format:** `[DOMAIN]_[ENTITY]_[TIER]`

Where TIER is `raw`, `staging`, or `curated`.

| Dataset | Name | Reads As |
|---|---|---|
| Raw GCSS-A vehicle data | `gcss_a_vehicles_raw` | "GCSS-A, vehicles, raw tier" |
| Cleaned vehicle status | `gcss_a_vehicles_staging` | "GCSS-A, vehicles, staging tier" |
| Publication-ready vehicle status | `gcss_a_vehicles_curated` | "GCSS-A, vehicles, curated tier" |
| Raw SITREP feed from SharePoint | `sitrep_feed_raw` | "SITREP feed, raw tier" |
| Curated personnel readiness | `dtms_personnel_readiness_curated` | "DTMS, personnel readiness, curated" |

For datasets with a specific time grain, append the grain after the tier: `gcss_a_vehicles_curated_daily` vs. `gcss_a_vehicles_curated_snapshot`.

### 7-3. Object Type, Pipeline, and Workshop Naming

| Resource | Convention | Example |
|---|---|---|
| **Object Type** | PascalCase, singular noun phrase | `VehicleReadiness`, `UnitStatus`, `MaintenanceRecord`, `SoldierReadiness` |
| **Link Type** | camelCase verb phrase | `assignedTo`, `reportedBy`, `locatedAt`, `ownedBy` |
| **Pipeline** | Lowercase, hyphen-separated verb phrase | `gcss-a-vehicle-ingestion-pipeline`, `sitrep-ingestion-pipeline` |
| **Workshop App** | Plain English, audience + purpose | `Unit Readiness Tracker`, `EUCOM SITREP Dashboard`, `V Corps Maintenance View` |
| **Project folder** | All caps, `[AOR]-[FUNCTION]` | `VCORPS-READINESS`, `USAREUR-AF-SITREP`, `21TSC-LOGISTICS` |
| **Dev branch** | Lowercase, `dev-[feature]` or `dev-[lastname]` | `dev-vehicle-status`, `dev-rodriguez` |

> **CAUTION:** Never use PII, classified nicknames, operational codenames, or system credentials in any resource name, description, or label. All resource names and descriptions appear in audit logs and are visible to all users with project access.

### 7-4. Governance Chain for Builder Decisions

| Decision | Who Authorizes |
|---|---|
| Create a new top-level project | Data Steward + C2DAO written approval |
| Ingest a new data source | Data Steward + C2DAO approval |
| Create a new Object Type | Consult Data Steward; verify no existing type covers the use case |
| Add a new Link Type | Data Steward review for shared Object Types |
| Enable write-back Action | Data Steward written authorization |
| Add a new team member at Editor role | Team lead + Data Steward approved access list |
| Publish a Workshop application | Peer review complete; Data Steward notification |
| Promote a branch to main | Peer review + Data Steward or team lead sign-off |

**First contact for all governance questions: your unit Data Steward.** They are the accountable data official and the first link between your build activity and C2DAO policy. Do not go directly to C2DAO without first consulting your Data Steward.

---

## SECTION 8 — COMMON BUILDER ANTI-PATTERNS

**BLUF:** Most build failures are not technical failures — they are design or governance failures. The following anti-patterns represent the most common ways TM-20 Builders produce outputs that are fragile, non-compliant, or operationally harmful.

| Anti-Pattern | Why It Happens | Why It's Harmful | Correct Approach |
|---|---|---|---|
| **Building without a clear requirement** | User asked for "a dashboard," Builder started immediately | Produces something that looks complete but does not help anyone make a decision; rebuilding wastes time | Answer the three pre-build questions before touching the platform; if requirement is vague, ask for a clearer one |
| **Building Phase 3 (Workshop) before Phase 1 and 2 are stable** | Workshop is more visible and feels like progress | Application shows no data or breaks when the pipeline changes; wasted design work | Pipeline first. Ontology second. Workshop third. No exceptions. |
| **Ignoring fan-out after a join** | Did not check row counts before and after | Metrics are double-counted; operators see wrong totals; decisions are made on bad data | Always check row counts before and after joins; aggregate before joining when right-side has multiple rows per key |
| **Editing main branch directly** | Branching feels like extra steps | A single mistake breaks all production applications and downstream consumers immediately | Always create a dev branch; every change to shared resources goes through branch → peer review → promote |
| **Using a property instead of a Link Type for relationships** | Faster to configure; Link Types feel complex | Workshop cannot navigate between related objects; relationship is not semantically represented; search and filtering break | Create Link Types with proper foreign key mapping for all object-to-object relationships |
| **Assigning Editor access to all team members** | Easier than evaluating each person's role | Any Editor can delete shared datasets and modify pipeline configurations; principle of least privilege violated | Operators get Viewer; only trained Builders get Editor; team leads get Owner; Data Steward approves all assignments |
| **Scheduling pipelines to run more frequently than source data updates** | Trying to make data appear "as real-time as possible" | Excessive builds waste platform resources, may rate-limit connectors, and produce identical outputs with extra overhead | Match refresh cadence to source update frequency; daily is appropriate for most USAREUR-AF feeds |
| **Deploying to production without peer review** | Time pressure; "it works on my branch" | A second set of eyes catches naming violations, grain problems, and broken filters that the Builder missed | Peer review is required before promotion; document the reviewer and date in the resource description |
| **Documenting after the fact (or not at all)** | Documentation feels like overhead | A replacement Builder inheriting an undocumented pipeline has no way to understand the data flow, source system, or known limitations | Fill pipeline description before branch merge; description format is specified in TM-20, Task 3-6 |
| **Attempting TM-30 patterns with TM-20 tools** | The requirement genuinely needs TM-30 capability; Builder tries to approximate | Produces fragile, unmaintainable pipelines and Ontology configurations; creates technical debt that TM-30 builders spend time unraveling | Recognize TM-30 patterns (see Section 9); escalate correctly rather than approximating |

---

## SECTION 9 — ESCALATION GUIDE: TM-20 VS. TM-30 VS. TM-40

**BLUF:** Knowing when to stop and escalate is a core Builder competency. The table below defines the scope boundary between TM-20, TM-30, and TM-40. When in doubt, escalate.

| Task | TM-20 Builder? | Escalate To... |
|---|---|---|
| Single-source filter, rename, and column select | Yes | — |
| Simple inner or left join on a shared key | Yes | — |
| Aggregate (count, sum, average, group by) | Yes | — |
| Append (union) two datasets with matching schemas | Yes | — |
| Deduplicate exact rows | Yes | — |
| Create an Object Type with primary key and properties | Yes | — |
| Create a many-to-one Link Type | Yes | — |
| Create a single-step, form-based Action | Yes | — |
| Build a single-page Workshop application with filters, tables, and charts | Yes | — |
| Schedule a pipeline refresh | Yes | — |
| Manage project access using the UI access list | Yes | — |
| Multi-source join with deduplication across sources | No | TM-30 |
| Watermark-based incremental pipeline (@incremental) | No | TM-30 |
| Many-to-many Link Type with junction dataset logic | No | TM-30 |
| Multi-step Action with conditional routing or approval chain | No | TM-30 |
| Multi-page Workshop application with conditional navigation | No | TM-30 |
| AIP Logic workflow configuration | No | TM-30 (config) / TM-40H (design) |
| Custom business logic requiring conditional transforms | No | TM-30 |
| Hierarchical Ontology modeling (three or more linked types) | No | TM-30 |
| Any pipeline requiring Python, PySpark, or SQL code | No | TM-40L (Software Engineer) |
| TypeScript Functions or OSDK application development | No | TM-40L (Software Engineer) |
| Machine learning model integration | No | TM-40I (ML Engineer) |
| AI workflow design (LLM chains, Agent Studio) | No | TM-40H (AI Engineer) |
| Statistical analysis and modeling (ORSA work) | No | TM-40G (ORSA) |
| Data program governance and policy | No | TM-40J (Program Manager) |
| Knowledge management architecture | No | TM-40K (Knowledge Manager) |
| New data source connector configuration | No | Data Steward + C2DAO |
| Top-level project creation | No | Data Steward + C2DAO |
| Ontology changes affecting coalition-facing data products | No | C2DAO review required |
| Any action you are uncertain is authorized | No | Data Steward first; C2DAO if Data Steward advises |

---

## SUMMARY: THE BUILDER'S PRE-BUILD CHECKLIST

Before starting any TM-20 build task, confirm:

| Item | Confirmed |
|---|---|
| Three pre-build questions answered: user identified, decision named, data confirmed in MSS (Section 1-4) | |
| Data source authorized for ingestion; Data Steward coordination documented (Section 2-2) | |
| Dataset tier structure follows naming convention (Section 7-2) | |
| Working on a development branch — not main (Section 6-2) | |
| Existing Object Types checked before creating a new one (Section 4-5) | |
| Primary key is unique at the intended grain (Section 4-1) | |
| Row counts checked before and after each join (Section 2-5) | |
| All Actions tested as Viewer before publishing (Section 5-3) | |
| Default filter values set on all Workshop filter widgets (Section 5-2) | |
| Pipeline documented per Task 3-6 format before branch merge (Section 8) | |
| Peer review completed; reviewer identity and date documented | |
| Promoted to main before publishing any Workshop application (Section 5-5) | |

---

## TRANSITION TO TM-20

This guide establishes the mental models applied throughout TM-20. TM-20 task instruction assumes this conceptual foundation — it will not re-explain why branching is required, why grain must be protected through joins, or why the three-phase build order is mandatory.

Proceed to TM-20, Chapter 1, when you can answer the following without referencing this guide:

1. What are the three pre-build questions, and why must they be answered before opening any build tool?
2. What is data grain, and what happens to grain during a join when the right-side dataset has multiple rows per key?
3. What is the correct build order for TM-20 work, and why?
4. What is the difference between a dataset and an Ontology Object Type?
5. What is the difference between an Ontology Action and a pipeline write?
6. When should a TM-20 Builder stop and escalate to TM-30?

If any answer requires looking it up, re-read the relevant section before proceeding.

---

---

## CURRICULUM NOTES

**Prerequisite:** TM-10 (Maven User) is REQUIRED before beginning TM-20 or this guide. TM-20 assumes full operator competency. Review TM-10, Tasks 2-1 through 2-4, 3-1 through 3-3, 5-1, and Chapter 7 before proceeding.

**Advancement tracks:** TM-20 graduates have two advancement paths:

- **TM-30 (Advanced Builder):** Required for all personnel before proceeding to any TM-40 track. TM-30 is the gateway to both WFF tracks (TM-40A–F) and specialist tracks (TM-40G–L).
- **WFF Tracks (TM-40A–F):** For operational staff whose primary role is warfighting function data use, not technical development. Prerequisite: TM-30 (required).

| WFF Track | Title | For Personnel |
|---|---|---|
| TM-40A | Intelligence WFF | G2 / S2 staff |
| TM-40B | Fires WFF | Fire support personnel |
| TM-40C | Movement & Maneuver WFF | G3 / S3 staff |
| TM-40D | Sustainment WFF | G4 / S4 / logistics staff |
| TM-40E | Protection WFF | Protection officers and NCOs |
| TM-40F | Mission Command WFF | G6 / S6 and command staff |

**Peer references:**
- **TM-10 (Operator Manual):** Build with the operator experience in mind. Review TM-10, Chapters 4 and 5 to understand what operators see and expect before you design any application.
- **Data Literacy Technical Reference:** For conceptual grounding in data management, governance frameworks (DoD VAUTI), and the full five-layer Foundry architecture diagram. Recommended reading before TM-20 instruction begins.

*CONCEPTS GUIDE — TM-20 COMPANION, BUILDER, MAVEN SMART SYSTEM (MSS)*
*Headquarters, United States Army Europe and Africa, Wiesbaden, Germany, 2026*
*Distribution restriction: Distribution authorized to U.S. Government agencies and their contractors only. Other requests must be referred to Headquarters, C2DAO, Wiesbaden, Germany.*
