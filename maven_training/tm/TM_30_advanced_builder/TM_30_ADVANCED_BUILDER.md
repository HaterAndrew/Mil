# TM-30 — MAVEN SMART SYSTEM (MSS)
## ADVANCED BUILDER TECHNICAL MANUAL

**HEADQUARTERS, UNITED STATES ARMY EUROPE AND AFRICA**
Wiesbaden, Germany

2026

**PREREQUISITE PUBLICATIONS:** TM-10, Maven User; TM-20, Builder; ADRP 1, Data Literacy (required)

**DISTRIBUTION RESTRICTION:** Approved for public release; distribution is unlimited.

---

## SAFETY SUMMARY

Advanced builders operate at the operational-technical boundary of MSS. At TM-30 level, you design solutions that affect shared infrastructure, coalition-facing data products, and enterprise ontology models that underpin applications used across the entire formation.

Before performing any task at TM-30 level:

- Understand the full downstream impact of ontology changes, schema modifications, and pipeline alterations before initiating them
- Coordinate with data stewards and the USAREUR-AF C2DAO before modifying any shared production resource
- Never prototype or test in the production environment — use Foundry branching for all development work
- AIP Logic workflows that operate on operational data require authorization review before deployment
- Data products accessible to Mission Partner Environment (MPE) or coalition-facing systems require C2DAO coordination and NAFv4 compliance review — this is a hard gate, not a suggestion
- If you are unsure whether your design requires a -40 developer to implement, it probably does — escalate before building

> **WARNING: Advanced builders are responsible for the integrity of shared data infrastructure. Errors at this level do not affect one application — they affect the data environment of the entire formation, including coalition partners. Apply engineering discipline to every design decision.**

---

## TABLE OF CONTENTS

- Chapter 1 — Introduction: The Advanced Builder Role
- Chapter 2 — Advanced Workshop Application Design
- Chapter 3 — Advanced Pipeline Builder
- Chapter 4 — Ontology Design Methodology
- Chapter 5 — Advanced Action Design via UI
- Chapter 6 — AIP Logic Configuration
- Chapter 7 — Advanced Contour and Quiver
- Chapter 8 — Data Governance and Stewardship
- Chapter 9 — Environment Management and Production Discipline
- Chapter 10 — NATO and Coalition Data Considerations
- Appendix A — -30 to -40 Handoff Guide (Technical Requirements Template)
- Appendix B — Application Design Checklist
- Appendix C — UDRA Alignment Checklist
- Glossary

---

## CHAPTER 1 — INTRODUCTION: THE ADVANCED BUILDER ROLE

### 1-1. Purpose and Scope

This manual provides design-level instruction for advanced builders operating on the Maven Smart System (MSS). MSS is the USAREUR-AF enterprise AI/data platform built on Palantir Foundry. TM-30 qualified personnel are the operational-technical bridge between mission requirements and technical implementation.

**TM-30 covers:**
- Designing complex, multi-page Workshop applications with conditional logic and parameter passing
- Designing advanced Pipeline Builder workflows using the visual UI (multi-source joins, transformations, scheduling)
- Designing Ontology models — Object Types, Link Types, and Actions — for operational use cases
- Configuring advanced Actions via the UI (multi-step workflows, approval chains, conditional logic)
- Configuring AIP Logic workflows and writing prompts that connect AI to operational ontology data
- Advanced Contour analysis and Quiver dashboard design
- Reading and acting on data lineage graphs
- Data quality governance and stewardship responsibilities
- Environment management, branching strategy, and production discipline
- NATO and coalition data considerations

**TM-30 does NOT cover:**
- Python, PySpark, or any scripting or coding — see TM-40 (Developer)
- SQL query writing — see TM-40
- TypeScript, Functions on Objects, or OSDK development — see TM-40
- Code Workspaces or any IDE-based development — see TM-40
- Agent Studio application development — see TM-40
- @incremental transform logic — see TM-40

> **NOTE:** The TM-30 graduate designs solutions. A TM-40 developer implements technical components. Understanding where this boundary falls is the most important skill in this manual. Chapter 4 addresses this explicitly.

Complete TM-10 and TM-20 before beginning this manual. TM-30 assumes full fluency in all TM-20 material. If you cannot independently build a basic Workshop application, configure an Object Type, and create an Action, stop and complete TM-20 first.

---

### 1-2. The Advanced Builder's Role in USAREUR-AF

United States Army Europe and Africa (USAREUR-AF) is the Army Service Component Command (ASCC) to United States European Command (USEUCOM), responsible for theater land operations across the European AOR and integration with NATO Allied command structures and Joint All-Domain Command and Control (JADC2). Major subordinate commands — V Corps, 21st Theater Sustainment Command (TSC), 7th Army Training Command (ATC), USAREUR-AF G2, and multinational force elements — all generate and consume data through MSS.

The advanced builder is the operational-technical bridge in this formation. You translate what the G2 analyst needs to see, what the S6 NCO needs to track, and what the G9 coordinator needs to report — into a design specification that can be built. You operate at the intersection of domain expertise and platform capability.

**The -30 role in the USAREUR-AF data chain:**

```
MISSION REQUIREMENT
        |
        v
   -30 BUILDER                <- You are here
   (Design + Configure)
        |
        v
   -40 DEVELOPER              <- Technical implementation when required
   (Code + Deploy)
        |
        v
   DATA PRODUCT
   (Ontology + Application)
        |
        v
   -10 USER
   (Consume + Act)
```

A sharp G2 all-source analyst qualified at TM-30 can design a complete ISR tracking application — specifying the Object Types, Link Types, Action flows, Workshop layout, filter logic, and data lineage — and hand a complete technical requirements package to a -40 developer for any components requiring code. That analyst need never touch Python or TypeScript. Their value is knowing what to build and how to specify it precisely.

---

### 1-3. What -30 Graduates Can Design

| Capability | -30 Can Design | -40 Required For |
|---|---|---|
| Workshop applications | Multi-page, conditional layouts, parameter passing, linked widgets | Custom JavaScript, complex external integrations |
| Pipeline Builder workflows | Multi-source joins, transformations, scheduling, error monitoring | PySpark, @incremental, custom connectors, complex deduplication logic |
| Ontology models | Object Types, Link Types, properties, Actions, Action Forms | Functions on Objects (TypeScript), OSDK, derived property logic |
| Actions | Multi-step, conditional logic, approval chains, form design | Webhook integration, external system write-back, complex validation logic |
| AIP Logic | Workflow configuration, prompt writing, ontology data connections | Agent Studio development, custom function integration, TypeScript logic |
| Contour / Quiver | Formula editor, aggregations, pivot tables, cross-dataset analysis | Custom chart plugins, programmatic report generation |
| Data governance | Lineage review, quality check review, stewardship coordination | Custom @check logic, automated quality gate coding |
| Environment management | Branch management (UI), review coordination, publish decisions | CI/CD pipeline code, automated testing |

The -30 builder is not blocked by not knowing code. The -30 builder is blocked only by insufficient understanding of the platform and the operational domain. Both are correctable.

---

### 1-4. The USAREUR-AF 5-Layer Data Stack

All TM-30 work occurs within the USAREUR-AF 5-Layer Data Stack. Understanding which layer your design affects determines who you coordinate with and what governance steps apply.

```
+---------------------------------------------------------------+
|  LAYER 5: ACTIVATION                                          |
|  (Decisions, Actions, AIP outputs, external system feeds)     |
+---------------------------------------------------------------+
|  LAYER 4: ANALYTICS                                           |
|  (Workshop apps, Contour, Quiver, AIP Logic dashboards)       |
+---------------------------------------------------------------+
|  LAYER 3: SEMANTIC (ONTOLOGY)                                 |
|  (Object Types, Link Types, Actions, AIP-connected objects)   |
+---------------------------------------------------------------+
|  LAYER 2: INTEGRATION                                         |
|  (Pipeline Builder, transforms, staging and curated datasets) |
+---------------------------------------------------------------+
|  LAYER 1: INFRASTRUCTURE                                      |
|  (Connectors, sources, access control, cross-domain arch)     |
+---------------------------------------------------------------+
```

**TM-30 Chapter to 5-Layer Stack Mapping:**

| Chapter | Topic | Primary Layer |
|---|---|---|
| Chapter 2 | Advanced Workshop Design | Layer 4 |
| Chapter 3 | Advanced Pipeline Builder | Layer 2 |
| Chapter 4 | Ontology Design Methodology | Layer 3 |
| Chapter 5 | Advanced Action Design | Layer 3 / Layer 5 |
| Chapter 6 | AIP Logic Configuration | Layer 4 / Layer 5 |
| Chapter 7 | Advanced Contour and Quiver | Layer 4 |
| Chapter 8 | Data Governance and Stewardship | Layer 1 / Layer 2 |
| Chapter 9 | Environment Management | Layer 2 / Layer 3 |
| Chapter 10 | NATO/Coalition Data | Layer 1 (cross-layer) |

---

### 1-5. UDRA Alignment and Governance Responsibilities

All data products designed at TM-30 level must align with the Unified Data Reference Architecture (UDRA) v1.1 (February 2025) and Army CIO Data Stewardship Policy (April 2, 2024).

**Core UDRA requirements for -30 builders:**

1. **Domain ownership.** Every data product must be traceable to a defined data domain with an identified domain owner. You cannot design a data product in isolation — identify the domain before you begin design.
2. **Federated governance.** Data governance is distributed. The C2DAO sets architecture standards; domain stewards govern content. Know which steward owns the data you are designing against.
3. **Data product thinking.** Treat every output — dataset, Ontology object, Workshop application — as a product with a defined consumer, a stated SLA, and documented quality standards.
4. **Layer verification.** Before publishing, verify your product is operating at the correct layer and not bypassing governance gates (e.g., a Workshop app reading directly from raw data — not authorized).

> **NOTE:** The VAUTI framework (Visible, Accessible, Understandable, Trustable, Interoperable) from DoD Data Strategy (2020) applies to all MSS data products. Advanced builders are responsible for ensuring their designs meet all five criteria before publication.

See Appendix C for the UDRA Alignment Checklist. Complete this checklist for every data product before publishing to production.

---

### 1-6. Governing References

| Document | Relevance |
|---|---|
| Army CIO Data Stewardship Policy (April 2, 2024) | Data stewardship hierarchy, governance chain, data product standards |
| UDRA v1.1 (February 2025) | Unified Data Reference Architecture — domain ownership, federated governance |
| DoD Data Strategy (2020) | VAUTI framework — Visible, Accessible, Understandable, Trustable, Interoperable |
| USAREUR-AF C2DAO Guidance | Theater-level architecture standards for MSS data products |
| NATO Architecture Framework v4 (NAFv4) | Coalition data architecture standards for MPE-accessible products |
| AJP-3.2 | Allied land operations doctrine and data exchange requirements |

> **NOTE:** Advanced builders should consult `learn-data.armydev.com` for authoritative design patterns and reference implementations:
> - **Object Type Cookbook v2 + Addendum A** — canonical ontology modeling reference for operational Object Types
> - **DDOF Playbook** — Doctrine-Driven Ontology Framework design patterns
> - **Doctrine-Driven Development** — aligning ontology models to Army operational doctrine
> - **ADP to JP to NATO Crosswalk** — mapping Army, Joint, and NATO data constructs
> - **Engagement Ontology (YAML v2.0)** — reference implementation for operational event modeling

---

### 1-7. Prerequisites and Access Requirements

Before performing any TM-30 level work on MSS, confirm the following:

**Knowledge prerequisites:**
- [ ] TM-10 (Maven User) completed
- [ ] TM-20 (Builder) completed — fluency confirmed by team lead
- [ ] ADRP 1, Data Literacy completed (required at TM-30 level)

**Access requirements:**
- [ ] Advanced Builder role requested and approved through chain of command
- [ ] Editor/Owner role on relevant project folders confirmed
- [ ] Ontology Editor role confirmed
- [ ] AIP Logic access confirmed (if applicable to your role)
- [ ] Data steward for your primary data domain identified

**Orientation requirements:**
- [ ] Reviewed the data lineage graph for your team's primary pipeline
- [ ] Located and reviewed the Ontology model for your primary data domain
- [ ] Identified the C2DAO architecture authority and your domain data steward
- [ ] Reviewed at least one existing complex Workshop application end-to-end (not as a user — as a builder examining the design)

Do not begin TM-30 level design work until all items above are confirmed. The elevated access you hold at this level can affect production systems. Orientation is not optional.

---

## CHAPTER 2 — ADVANCED WORKSHOP APPLICATION DESIGN

### 2-1. The Multi-Page Application Model

TM-20 Workshop applications are typically single-page, purpose-specific tools. TM-30 applications are multi-page, cross-functional platforms that serve multiple user roles within a single application experience. A well-designed multi-page application reduces application sprawl, maintains consistent data context across views, and reduces the burden on end users who would otherwise navigate between multiple tools.

**When to build multi-page vs. multiple single-page applications:**

| Scenario | Recommendation |
|---|---|
| Same user roles, different analytical views of the same data | Multi-page application |
| Same data domain, different user roles with different access requirements | Multi-page with role-based visibility |
| Completely different data domains used by different formations | Separate applications |
| One application is a summary; others are detailed drill-downs | Multi-page with navigation links |
| Theater-level readiness dashboard (G3/G4/G6 shared view) | Multi-page — one app per staff section is application sprawl |

**Operational example:** A Grafenwöhr exercise support platform might have four pages: (1) Unit Readiness Status, (2) Logistics Tracking, (3) ISR Event Log, and (4) SITREP Submission Form. All four use overlapping data (unit identifiers, grid references, DTGs) and serve overlapping users. A single multi-page application is the correct design.

---

**TASK 2-1. DESIGN A MULTI-PAGE WORKSHOP APPLICATION**

**CONDITIONS:** Given an existing Workshop project and a set of user requirements covering multiple analytical views or user roles, when designing a new application structure.

**STANDARDS:** The builder will produce a multi-page application with logical page organization, consistent navigation, and a documented page map before building any individual page.

**PROCEDURE:**
1. Open Workshop and navigate to the target project folder in Compass.
2. Create a new Workshop application. Name it per USAREUR-AF naming conventions: `[Formation] [Function] [Application Type]` (e.g., `USAREUR-AF G3 Readiness Platform`).
3. Before adding any widget, create the page structure. In the left panel, select **Pages** and add pages for each major view. Name pages plainly: `Readiness Overview`, `Unit Detail`, `Logistics Tracker`, `SITREP Submission`.
4. Create a Page Map document (outside MSS — a whiteboard sketch, notes document, or Appendix B checklist). Document: page name, primary user role, primary Object Types displayed, and Actions available on each page.
5. Configure the navigation bar on each page to include links to all other pages. Do not hide pages from navigation unless role-based access requires it.
6. Identify shared parameters (filters, selections) that must persist across page navigation. Document these before building widgets. See Task 2-3 for parameter design.
7. Build pages in order: start with the page that contains the most data-intensive view (typically the overview or map page). Resolve data binding issues on the hardest page first before replicating patterns to simpler pages.

> **NOTE:** Page count is not a quality metric. Three well-designed pages that answer the user's questions are better than eight pages of redundant views. Review your page map with the end user before building.

---

### 2-2. Conditional Layouts

Conditional layouts allow a single application to present different content based on user role, selected object state, or dynamic filter values. This eliminates the need for separate applications for different user types and reduces maintenance burden.

**Common conditional layout patterns in USAREUR-AF applications:**

| Pattern | Use Case |
|---|---|
| Role-based visibility | G2 users see ISR fields; G4 users see logistics fields; same application |
| Object state-driven content | Show AMBER status detail panel only when a unit's readiness is below threshold |
| Empty state handling | Display a placeholder panel when no object is selected in a list |
| Filter result handling | Show a "no results" message when a filter combination returns zero objects |

---

**TASK 2-2. CONFIGURE CONDITIONAL VISIBILITY ON A WORKSHOP WIDGET**

**CONDITIONS:** Given a Workshop application with multiple user roles defined, when a widget or panel should display only under specific conditions.

**STANDARDS:** The builder will configure the conditional visibility expression so that the widget renders correctly for the intended condition and is hidden otherwise, with no widget errors in either state.

**PROCEDURE:**
1. Select the widget or container panel to which you want to apply conditional visibility.
2. In the right-hand properties panel, locate the **Visibility** section.
3. Select **Conditional** (not Always Visible or Always Hidden).
4. Open the expression editor. The expression must evaluate to true (show) or false (hide).
5. For role-based visibility: reference the built-in `currentUser.groups` variable. Example: show a panel only to users in the `G2-ISR-Analysts` group.
6. For object-state-driven visibility: reference the selected object's property. Example: show an escalation panel only when `UnitStatus.readinessLevel` equals `AMBER` or `RED`.
7. For empty state handling: use the `isNull()` or `isEmpty()` functions against the relevant variable.
8. After configuring the expression, use the Workshop preview mode to test both the visible and hidden states.

> **CAUTION: Conditional visibility hides widgets — it does not restrict data access. A user who can access the application can still access the underlying data even if a widget displaying that data is hidden from their view. For true access restriction, use Foundry object-level security configured by your platform admin. Do not use conditional visibility as a security control.**

---

### 2-3. Variable and Parameter Design

Variables and parameters are the connective tissue of complex Workshop applications. They allow user selections on one widget to drive content on other widgets, across multiple pages, and within Action forms. Poor variable design is the most common cause of complex application performance problems.

**Variable types and when to use each:**

| Variable Type | Best For | Avoid For |
|---|---|---|
| Object Set Variable | Driving lists, tables, maps from a filtered object set | Storing single values — use a property variable instead |
| String/Number Variable | Capturing filter values, storing user input for display | Large data payloads |
| URL Parameters | Sharing application state via link; deep-linking to a specific object | Sensitive data — URL parameters are visible |
| Temporary Variable | Local state within a single page | Cross-page state — temporary variables do not persist across navigation |

---

**TASK 2-3. CONFIGURE A CROSS-PAGE PARAMETER TO PASS OBJECT SELECTION BETWEEN PAGES**

**CONDITIONS:** Given a multi-page Workshop application where a user selects an object on Page 1 (e.g., a unit from a readiness table) and needs to see that object's detail view on Page 2.

**STANDARDS:** The selected object on Page 1 persists as the context object on Page 2 without requiring the user to re-select. Page 2 displays detail content for the object selected on Page 1.

**PROCEDURE:**
1. On Page 1, identify the widget that contains the primary object selection (e.g., a Table or List widget displaying `UnitStatus` objects).
2. In the Page 1 variable panel, create a new **Object Variable** of the appropriate Object Type (e.g., `UnitStatus`).
3. Bind the Table widget's "selected row" output to this Object Variable.
4. On the Page 1 navigation button or link that routes to Page 2, open the **Pass Variables** configuration.
5. Map the Page 1 Object Variable to a corresponding Object Variable on Page 2. Create the Page 2 variable if it does not yet exist.
6. On Page 2, build widgets that reference the passed Object Variable as their data source.
7. Configure the empty state for Page 2 widgets to display a meaningful message when no object has been passed (i.e., the user navigated to Page 2 directly without selecting an object on Page 1).
8. Test the full flow: select an object on Page 1, navigate to Page 2, verify the correct object's data appears, navigate back, select a different object, verify Page 2 updates.

> **NOTE:** URL parameters are an alternative to page-level variable passing. URL parameters allow deep-linking — a user can share a URL that opens the application directly to a specific object. Use URL parameters when you need shareable links (e.g., a SITREP that links directly to the unit detail view for a specific reporting unit). Configure URL parameters in the Application Settings panel.

---

### 2-4. Complex Filter Chains

Complex filter chains allow Workshop applications to support multi-dimensional operational analysis — for example, filtering a Baltic flank readiness view by AOR, readiness tier, reporting period, and unit type simultaneously. Poorly designed filter chains degrade application performance and confuse users.

**Design principles for complex filter chains:**

1. **Order filters from most selective to least.** Apply the filter that reduces the object set the most first. For USAREUR-AF use cases, AOR or formation filters are almost always the most selective and should be applied first.
2. **Use dependent filters.** A dependent filter's options update based on the selection in a prior filter (e.g., after selecting V Corps as the formation, the unit list filter shows only V Corps units). Configure dependency in the filter widget's data source expression.
3. **Provide a "clear all filters" control.** Users will inevitably filter themselves into a zero-result state. A single button that resets all filter variables to their default values prevents confusion.
4. **Document the filter chain in your design.** Before building, draw the filter dependency graph. Filters with circular dependencies will cause infinite loops.

---

**TASK 2-4. BUILD A DEPENDENT FILTER CHAIN FOR AN OPERATIONAL READINESS VIEW**

**CONDITIONS:** Given a Workshop application displaying `UnitStatus` objects for USAREUR-AF formations, when a user needs to filter by theater, then corps, then division, then brigade in sequence.

**STANDARDS:** Each filter in the chain updates its available options based on the prior selection. Selecting V Corps in the Corps filter shows only V Corps divisions in the Division filter. The object view updates after all filters are applied.

**PROCEDURE:**
1. Create String Variables for each filter level: `selectedTheater`, `selectedCorps`, `selectedDivision`, `selectedBrigade`.
2. Add a Dropdown widget for Theater. Set its data source to the distinct values of `UnitStatus.theaterLevel`. Bind its output to `selectedTheater`.
3. Add a Dropdown widget for Corps. Set its data source to the distinct values of `UnitStatus.corpsLevel` filtered where `theaterLevel` equals `selectedTheater`. Bind its output to `selectedCorps`.
4. Repeat this pattern for Division and Brigade, each filtered by the preceding selection.
5. Configure the primary Object Set (the data source for the readiness table or map) to apply all four filters: `UnitStatus` where all four level variables match. Use null-safe comparisons so that if a filter variable is empty (not yet selected), that filter does not constrain the result.
6. Add a **Clear Filters** Button widget. Configure its click action to reset all four String Variables to null/empty.
7. Test all filter combinations, including the empty state (no filters selected) and the fully-filtered state (all four filters selected).

> **CAUTION: Dependent filter chains that reference large object sets without indexed properties can significantly degrade application load time. If a filter chain over more than 50,000 objects is responding slowly, escalate to a -40 developer to review the underlying object set and index configuration before deploying to production.**

---

### 2-5. Linked Widgets and Synchronized Views

Linked widgets allow user interaction with one widget (e.g., selecting a row in a table) to drive updates in other widgets simultaneously (e.g., a map zooms to that unit's location, a detail panel shows that unit's properties, a chart filters to that unit's historical data). This pattern is the foundation of operational dashboards.

---

**TASK 2-5. CONFIGURE LINKED WIDGETS FOR A SITREP DASHBOARD**

**CONDITIONS:** Given a SITREP aggregation application with a unit roster table, a theater map, a readiness trend chart, and a detail panel, when a user selects a unit in the table.

**STANDARDS:** Selecting a unit in the table simultaneously (a) highlights that unit's marker on the map, (b) updates the trend chart to show that unit's data only, and (c) populates the detail panel with that unit's current SITREP properties.

**PROCEDURE:**
1. Create an Object Variable `selectedUnit` of type `UnitStatus`.
2. On the Table widget: bind the "selected row" output to `selectedUnit`.
3. On the Map widget: configure the "highlight layer" or "selected object" binding to reference `selectedUnit`. The map will highlight the marker for the selected object.
4. On the Trend Chart widget: set the data filter to `UnitStatus where objectId = selectedUnit.objectId`. The chart will update to show only the selected unit's historical data.
5. On the Detail Panel container: set each property display widget's data source to the corresponding property of `selectedUnit`. The panel will update all fields simultaneously when `selectedUnit` changes.
6. Set the empty state for the map highlight, chart, and detail panel to display appropriate placeholder content when `selectedUnit` is null.
7. Test by selecting multiple rows in the table sequentially and verifying all linked widgets update correctly.

> **NOTE:** Do not attempt to link more than five to seven widgets to a single Object Variable without testing performance. Each widget re-renders on selection change. Applications with 15 or more linked widgets may exhibit noticeable lag on large object sets. Test with realistic data volumes, not sample data.

---

### 2-6. Application Performance Considerations

Performance is a design responsibility. A slow application that serves the right data is functionally unusable in an operational environment. Understand the common causes of Workshop application performance problems before designing at TM-30 level.

**Performance design principles:**

| Principle | Action |
|---|---|
| Filter early | Apply the most restrictive filters at the object set level, not at the widget level |
| Paginate large tables | Do not display more than 200-500 rows without pagination — configure page size in Table widget settings |
| Avoid deeply nested containers | More than three levels of nested containers increases render time |
| Minimize real-time refresh intervals | Default auto-refresh is sufficient for most operational views; do not set sub-minute refresh without a specific requirement |
| Use object-level security, not widget-level visibility, for access control | Widget visibility checks run client-side; object security runs server-side and is more efficient |
| Limit concurrent linked widgets | See Task 2-5 note above |

**When to escalate to a -40 developer:**
- Application takes more than 5 seconds to load on the first page render with production-volume data
- A filter operation on a large object set (100,000 or more objects) consistently hangs or times out
- A required feature cannot be achieved with available Workshop widgets and formula functions

---

## CHAPTER 3 — ADVANCED PIPELINE BUILDER

### 3-1. Pipeline Builder Capabilities at TM-30 Level

Pipeline Builder is MSS's visual ETL tool. TM-20 covered single-source ingestion pipelines with basic transformations. TM-30 covers multi-source joins, complex transformations using the visual transform library, error handling, scheduling optimization, and pipeline monitoring.

> **NOTE:** Pipeline Builder is a no-code visual tool. TM-30 builders configure pipelines entirely through the UI. If a pipeline requirement cannot be achieved in Pipeline Builder's visual interface — for example, complex deduplication logic, @incremental watermark patterns, or custom Python transformations — that requirement belongs to a -40 developer. Design what you can; specify the rest. See Chapter 4 and Appendix A for the handoff process.

**When Pipeline Builder is sufficient (TM-30 can own):**
- Multi-source joins with standard join types (inner, left, full outer)
- Column renaming, type casting, filtering, and calculated columns using built-in formula functions
- Schema harmonization across sources with compatible field names and types
- Aggregations: group-by, sum, count, average, min, max
- Scheduled execution with standard recurrence patterns
- Basic deduplication using row-number ranking on a key column

**When a -40 developer is required:**
- @incremental (watermark-based) pipelines
- Custom deduplication logic requiring complex business rules
- PySpark transformations
- External API calls or custom connectors
- Complex date/time business logic beyond built-in functions
- Pipelines processing more than approximately 10 million rows that require execution optimization

---

### 3-2. Multi-Source Join Design

Joining multiple data sources in Pipeline Builder requires careful design. The most common errors in multi-source pipelines are (a) join key mismatches due to data quality issues, (b) fan-out (unintended row multiplication from one-to-many joins), and (c) performance degradation from large cross-joins.

**Join design principles:**

1. **Identify join keys before opening Pipeline Builder.** Know the exact field names and data types of every join key across all sources. Data type mismatches (e.g., joining a string unit ID to an integer unit ID) will silently drop rows.
2. **Profile both sides before joining.** Use the Column Statistics view in the dataset preview to check null rates and distinct value counts on join key columns before building the join node.
3. **Understand cardinality.** A one-to-many join will multiply rows. An ISR event table joined to a unit roster where one unit has 50 events will produce 50 rows per unit. Design downstream aggregations accordingly.
4. **Validate row counts after every join.** After adding a join node, preview the output and check: input row count vs. expected output based on relationship type. If it does not match, the join condition is wrong.

---

**TASK 3-1. BUILD A MULTI-SOURCE JOIN PIPELINE IN PIPELINE BUILDER**

**CONDITIONS:** Given two curated datasets — a unit status dataset and a location dataset — that share a common unit identifier, when building a pipeline to produce a unified unit profile dataset.

**STANDARDS:** The output dataset contains one row per unit, with columns from both source datasets correctly joined. Row count equals the number of unique unit identifiers in the status dataset. No duplicate rows. No unexpected nulls on expected join-key fields.

**PROCEDURE:**
1. Open Compass and navigate to your project's pipeline folder.
2. Create a new Pipeline. Name it per USAREUR-AF naming conventions.
3. Add the first Source node. Configure it to reference the unit status curated dataset.
4. Add the second Source node. Configure it to reference the unit location curated dataset.
5. Add a **Join** node. Connect both Source nodes to the Join node.
6. Configure the Join type. For a standard unit roster join: use **Left Join** (keep all units from the status dataset; add location data where available; null location fields where the unit has no location record).
7. Set the join condition: `status.unitId = location.unitId`. Confirm both fields are the same data type in the column headers.
8. Preview the Join output. Check: row count matches the unit status source row count. If row count is higher, there are duplicate keys in the location dataset — resolve before proceeding.
9. Add a **Select Columns** node downstream of the Join. Remove duplicate key columns (the join produces two copies of `unitId`). Retain only required columns.
10. Add the Output node. Configure the output path per naming conventions (using the `/curated` tier path).
11. Run the pipeline manually. Review the build log for warnings (e.g., type coercion warnings indicate silent data conversion).
12. Preview the final output. Spot-check five to ten rows against source records to verify field alignment.

> **CAUTION: Do not join raw datasets. Always join curated or staging datasets where data quality has been validated. Joining raw datasets propagates upstream data quality problems into joined outputs, and these problems are difficult to trace after the fact.**

---

### 3-3. Calculated Columns and Transformations

Pipeline Builder's **Derived Column** node allows creation of calculated columns using the built-in formula language. This is the primary TM-30 mechanism for data enrichment — adding readiness scores, normalizing status codes, computing time deltas, and flagging records that meet operational thresholds.

**Common operational calculated columns:**

| Use Case | Formula Pattern |
|---|---|
| Days since last SITREP | `dateDiff(today(), lastSitrepDate, "day")` |
| Readiness tier flag | `if(readinessScore >= 90, "GREEN", if(readinessScore >= 75, "AMBER", "RED"))` |
| Unit display name normalization | `concat(echelon, " ", unitDesignation, " (", bia, ")")` |
| Null-safe status label | `coalesce(reportedStatus, "UNKNOWN")` |
| DTG to readable format | `dateFormat(dtgTimestamp, "DDHHMMZ MMM YYYY")` |

---

**TASK 3-2. ADD A READINESS TIER CALCULATED COLUMN**

**CONDITIONS:** Given a pipeline with a unit status dataset containing a numeric `readinessScore` field (0-100), when the downstream Ontology and Workshop application require a categorical readiness tier field (GREEN, AMBER, RED).

**STANDARDS:** The output dataset contains a `readinessTier` column populated with the correct categorical value for every row. No nulls in `readinessTier` (use UNKNOWN as default for null input scores).

**PROCEDURE:**
1. Downstream of the source or join node (but before the output node), add a **Derived Column** node.
2. Name the new column `readinessTier`.
3. Open the formula editor.
4. Enter the conditional expression: `if(isNull(readinessScore), "UNKNOWN", if(readinessScore >= 90, "GREEN", if(readinessScore >= 75, "AMBER", "RED")))`.
5. Preview the Derived Column output. Verify that the formula correctly categorizes sample rows across the GREEN, AMBER, RED, and null-input cases.
6. Check the distinct values of `readinessTier` in the Column Statistics view. Verify no unexpected values appear.

> **NOTE:** The formula language in Pipeline Builder's Derived Column node uses the same syntax as Contour's calculated column editor (see Chapter 7). Mastery of this formula language is a high-leverage TM-30 skill — it applies across Pipeline Builder, Contour, and Workshop formula-driven widgets.

---

### 3-4. Error Handling and Pipeline Monitoring

TM-30 builders own the operational health of the pipelines they design. A pipeline that silently produces incorrect output is more dangerous than one that fails loudly.

**Pipeline error categories and response:**

| Error Category | Symptom | TM-30 Action |
|---|---|---|
| Schema change in source | Pipeline fails with "column not found" | Investigate source dataset, update Select Columns node, notify data steward |
| Join key null spike | Row count drops unexpectedly | Check null rate on join key in source; notify upstream data steward |
| Type coercion warning | Numeric column shows string values | Add explicit type cast node upstream; check source data quality |
| Execution timeout | Pipeline marked failed after long run | Reduce payload (add filter node); escalate to -40 developer for optimization |
| Missing output rows | Output row count lower than expected | Check join type, filter conditions, and source freshness |

---

**TASK 3-3. CONFIGURE PIPELINE FAILURE ALERTING**

**CONDITIONS:** Given a production pipeline running on a scheduled cadence, when the pipeline fails or produces output below an expected row count threshold.

**STANDARDS:** The designated team lead receives an MSS notification within 15 minutes of a pipeline failure. The notification includes the pipeline name, failure timestamp, and last successful run time.

**PROCEDURE:**
1. Open the target pipeline in Pipeline Builder.
2. Navigate to the **Schedule and Alerts** configuration panel.
3. Under **Alerts**, select **Add Alert**.
4. Configure trigger condition: **On Failure** — alerts when the pipeline build fails for any reason.
5. Optionally add a second alert: **On Row Count Below Threshold** — configure the expected minimum row count for the output dataset (e.g., if the unit status dataset should never contain fewer than 50 rows, set threshold at 50).
6. Set notification recipients: add the team lead's MSS username and any other required recipients.
7. Set the notification channel: MSS in-platform notification (default) or email (if configured by your platform admin).
8. Save alert configuration and confirm it appears in the pipeline's alert summary.
9. Document the alert configuration in the pipeline description field.

---

### 3-5. Scheduling Optimization

Pipeline scheduling must be designed to balance data freshness requirements against platform resource constraints. Not every pipeline needs to run every hour.

**Scheduling design guidance for USAREUR-AF pipelines:**

| Data Type | Recommended Cadence | Rationale |
|---|---|---|
| SITREP aggregations | Every 2-4 hours during operational hours | SITREPs are submitted on 6-12 hour cycles; more frequent refresh provides no value |
| ISR event feeds | Every 30-60 minutes (if source updates at this rate) | ISR data has time-sensitivity; match pipeline cadence to source update rate |
| Readiness/personnel data | Daily (off-peak hours) | PERSTAT/readiness data changes on daily cycles; hourly runs waste resources |
| Logistics visibility | Every 4-6 hours | Logistics transactions process in batches; match cadence to batch cycle |
| Exercise support pipelines | On-demand or every 15-30 minutes during exercise window only | High-tempo during exercise; disable or extend to daily after exercise concludes |

> **CAUTION: Setting pipeline schedules more frequently than the source data update rate provides no benefit and consumes platform resources shared across the entire formation. Coordinate with the source system owner to understand the actual data update cadence before configuring pipeline schedule.**

---

**TASK 3-4. CONFIGURE A PIPELINE SCHEDULE**

**CONDITIONS:** Given a production pipeline that must run during operational hours at the required cadence, when configuring the pipeline's execution schedule.

**STANDARDS:** The pipeline runs at the configured cadence within the operational window. The schedule is documented in the pipeline description.

**PROCEDURE:**
1. Open the target pipeline in Pipeline Builder.
2. Navigate to **Schedule and Alerts** (same panel as Task 3-3).
3. Enable the **Schedule** toggle.
4. Select the recurrence pattern: hourly, daily, weekly, or custom cron expression.
5. For operationally-sensitive pipelines (e.g., SITREP aggregation before a commander's daily update brief), use a custom cron expression to ensure the pipeline completes at least 30 minutes before the brief time.
6. Set the time zone to `Europe/Berlin` (CET/CEST) for USAREUR-AF headquarters pipelines. Confirm with your team lead for pipelines supporting units in other time zones.
7. If the pipeline only needs to run during exercises or operational events: configure a **Start Date** and **End Date** for the schedule. This prevents the pipeline from consuming resources outside the operational window.
8. Click **Save Schedule**. Verify the next scheduled run time displays correctly.
9. Document the schedule and rationale in the pipeline description field (e.g., "Runs every 2 hours 0600-2200 CET. Aligned to USAREUR-AF daily SITREP cycle. Disable outside exercise windows.").

---

## CHAPTER 4 — ONTOLOGY DESIGN METHODOLOGY

### 4-1. The -30 Builder's Role in Ontology Design

The Ontology is the semantic layer of MSS. It translates data tables into operational concepts — a row in a dataset becomes a `UnitStatus`, a `LogisticsShipment`, or an `ISREvent`. The Ontology is shared infrastructure. Changes to it affect every application and pipeline that references the modified objects.

At TM-30 level, you **design** Ontology models. You define the Object Types, Link Types, properties, and Actions that are required to meet an operational need. Some of this design work you can implement yourself through the Ontology Manager UI. Some of it — Functions on Objects, derived properties requiring TypeScript, OSDK integration — requires a -40 developer to implement. Your job is to produce a design specification precise enough that a developer can implement it without needing to re-derive the requirements.

This chapter covers:
- How to think about Object Type design
- How to design Link Types that reflect operational relationships
- How to design Actions that support operational workflows
- How to write technical requirements for a -40 developer
- Reference resources and design patterns from `learn-data.armydev.com`

> **NOTE:** The Object Type Cookbook v2 at `learn-data.armydev.com` is the authoritative reference for Object Type design in the USAREUR-AF environment. Addendum A covers operational Object Types specific to Army warfighting functions. Review both before designing any new Object Type.

---

### 4-2. Object Type Design Methodology

Object Types must reflect operational concepts, not database schema. The question "what is a record in this table?" is a data question. The question "what is the operational entity this data represents, and how do commanders and staff reason about it?" is an Ontology design question.

**Object Type design decision framework:**

| Question | Guidance |
|---|---|
| What real-world operational concept does this represent? | Name the Object Type after the concept, not the table (e.g., `UnitStatus`, not `unit_status_curated`) |
| Who uses this object and what decisions do they make with it? | Properties must support the user's decision — include the properties that matter; exclude irrelevant database fields |
| How does this object relate to other objects in the Ontology? | Identify Link Types before finalizing properties — some relationships will drive additional property requirements |
| Will this object need to be searched, filtered, or aggregated at scale? | Identify search-eligible and indexed properties during design |
| Will this object's properties ever be computed (not directly stored)? | Flag these for -40 developer implementation as derived properties or Functions on Objects |
| Does this object type already exist in the Ontology? | Check the Ontology Manager and Object Type Cookbook before creating a new type — avoid duplication |

**Design anti-patterns to avoid:**

| Anti-Pattern | Why It Fails |
|---|---|
| Creating an Object Type for every dataset table | Object Types represent concepts, not tables. One concept may draw from multiple tables. |
| Naming Object Types after systems or source feeds | `AFATDSEvent` is a system name; `FireMissionRequest` is an operational concept |
| Including every column from the source table as a property | More properties equals more maintenance; include only operationally relevant properties |
| Creating separate Object Types for status variations | `ActiveUnitStatus` and `InactiveUnitStatus` should be one type with a `status` property |
| Designing without checking existing Ontology | May duplicate existing Object Types and create parallel, conflicting models |

---

### 4-3. Link Type Design

Link Types represent relationships between Object Types. A `UnitStatus` is linked to `PersonnelRecord` objects (the soldiers assigned to it). An `ISREvent` is linked to `GridReference` objects (where it occurred) and `UnitStatus` objects (the reporting unit). Link Types are how the Ontology models operational context.

**Link Type design principles:**

1. **Name Link Types as verb phrases** from the perspective of the source object. `UnitStatus` assigns to `GarrisonLocation`. Read naturally: "A UnitStatus is assigned to a GarrisonLocation."
2. **Define cardinality explicitly.** One-to-one, one-to-many, or many-to-many. Cardinality affects how Workshop applications can traverse links and how Contour can aggregate across them.
3. **Only create Link Types that serve a business need.** If no application or analysis will traverse the link, the link adds maintenance burden without value.
4. **Document the foreign key.** Every Link Type must have an identified foreign key relationship between the backing datasets. Document this in the Link Type description field.
5. **Consult the Engagement Ontology (YAML v2.0) at `learn-data.armydev.com`** before designing links for operational event models. The Engagement Ontology provides the canonical link model for combat events, ISR events, and unit interactions.

---

### 4-4. Designing Actions

Actions are the mechanism through which users write data back to the Ontology. TM-20 covers basic single-step Actions. TM-30 designs Actions that support complex operational workflows — multi-step submission flows, conditional logic, approval chains, and integration with other Actions.

Action design is separate from Action configuration. Designing an Action means:
1. Defining the operational workflow the Action supports
2. Specifying the inputs (form fields) required
3. Specifying the validation rules that must pass before submission
4. Specifying what data changes (which Object Type properties, which objects)
5. Determining whether the Action requires approval before execution
6. Identifying any downstream notifications or follow-on actions

Design this on paper or in a requirements document before opening the Ontology Manager. Configuration follows design.

---

### 4-5. Writing Technical Requirements for a -40 Developer

When your design requires a -40 developer to implement technical components (Functions on Objects, derived properties, OSDK integration, @incremental pipeline logic, complex Action validation), you must provide a complete and precise technical requirements document.

> **NOTE:** A vague handoff to a developer wastes time and produces incorrect implementations. The requirements document in Appendix A is the standard template for all -30 to -40 handoffs on USAREUR-AF MSS projects. Use it every time.

**What a good -30 to -40 requirements document covers:**

| Section | Content Required |
|---|---|
| Operational context | What mission problem this solves; who the users are; what decision they make |
| Data inputs | Source datasets (by path), relevant columns, known data quality issues |
| Object Types and Link Types | Which existing types are involved; which new types are needed (with full property specs) |
| Required technical components | Specific functions, pipelines, or integrations needed — with inputs, outputs, and logic description |
| Non-functional requirements | Performance expectations, refresh rate, data volume |
| Acceptance criteria | How will you verify the implementation is correct? Specific, measurable. |
| Timeline and priority | When this is needed; priority relative to other work |
| Point of contact | Who owns the requirement; who to ask for clarification |

See Appendix A for the full template.

---

**TASK 4-1. DESIGN AN OBJECT TYPE FOR AN OPERATIONAL USE CASE**

**CONDITIONS:** Given a G2 requirement to track ISR collection events on the Baltic flank — including event type, grid reference, collection asset, reporting unit, DTG, and analyst assessment — when designing the corresponding Ontology model.

**STANDARDS:** The builder will produce a complete Object Type design document (outside MSS, prior to any implementation) specifying: Object Type name, all properties with data type and source field mapping, linked Object Types, required Link Types with cardinality, and a list of any components requiring -40 developer implementation.

**PROCEDURE:**
1. Review the source data available: identify the dataset(s) that will back the Object Type. Note the dataset paths, column names, and data types.
2. Name the Object Type. Use PascalCase, singular noun, operational concept name: `ISRCollectionEvent`.
3. List all properties. For each property, document:
   - Property name (camelCase)
   - Data type (string, integer, timestamp, boolean, geo-point)
   - Source dataset column name
   - Whether this property is search-eligible (can users search for it?)
   - Whether this property is required to be non-null
4. Identify related Object Types: `UnitStatus` (reporting unit), `GridReference` (location of event), `CollectionAsset` (sensor or platform). Check the Ontology Manager to confirm these Object Types already exist before designing new ones.
5. Define Link Types. For each: name (verb phrase from `ISRCollectionEvent`'s perspective), target Object Type, cardinality, foreign key.
6. Identify derived properties or computed values (e.g., "time since collection event" is time-relative — requires a Function on Objects). Flag each as requiring -40 developer implementation.
7. Document the design in the -30 to -40 handoff template (Appendix A) and review with your team lead before beginning implementation in Ontology Manager.

> **NOTE:** Consult the DDOF Playbook at `learn-data.armydev.com` for the Doctrine-Driven Ontology Framework design patterns before designing Object Types for ISR, fires, or maneuver tracking use cases. The Doctrine-Driven Development framework provides Army doctrine-aligned patterns for these domains that have been validated against ADP 3-0, FM 3-55, and NATO doctrine equivalents.

> **NOTE:** The ADP to JP to NATO Crosswalk at `learn-data.armydev.com` provides mappings between Army doctrine terms, Joint doctrine equivalents, and NATO/STANAG terminology. Use this reference when designing Object Types for products that will be shared with joint or coalition partners — use the NATO-compatible term as the canonical Object Type name where applicable.

---

## CHAPTER 5 — ADVANCED ACTION DESIGN VIA UI

### 5-1. Actions at TM-30 Level

TM-20 Actions are single-step: a user fills out a form, submits it, and one object is updated. TM-30 Actions support operational workflows: multi-step submission processes, conditional routing based on submitted values, approval chains requiring sign-off before data changes are applied, and form logic that dynamically adjusts what fields are shown based on prior inputs.

All TM-30 Action design is performed through the Action Editor UI in Ontology Manager. No code is required. If a workflow requirement cannot be achieved through the Action Editor UI — for example, calling an external system API on submission, or executing complex server-side validation logic — that requirement belongs to a -40 developer. Design the workflow; specify the technical gap; hand it off.

---

### 5-2. Multi-Step Action Workflows

Multi-step Actions guide users through a structured process with distinct phases. A SITREP submission workflow might have three steps: (1) Unit identification and reporting period, (2) Status data entry by warfighting function, (3) Commander's narrative and certification. Each step uses previously submitted data from prior steps.

---

**TASK 5-1. CONFIGURE A MULTI-STEP ACTION WORKFLOW**

**CONDITIONS:** Given an operational requirement for a structured unit status report submission with three phases (identification, data entry, certification), when configuring the Action in Ontology Manager.

**STANDARDS:** The Action presents users with three distinct form sections in sequence. Users cannot advance to Step 2 without completing required fields in Step 1. Step 3 shows a summary of all entered data before final submission. On submission, the designated `UnitStatus` object is updated with all submitted values.

**PROCEDURE:**
1. Open Ontology Manager and navigate to the target Object Type (`UnitStatus`).
2. Select **Actions** then **New Action**.
3. Name the Action operationally: `Submit Unit Status Report`.
4. In the Action Editor, select **Multi-Step Form** layout.
5. Configure Step 1 — Identification:
   - Add fields: `reportingUnit` (Object selector, linked to `UnitStatus`), `reportingPeriod` (date range picker), `reportingOfficer` (current user, auto-populated).
   - Mark all three fields as **Required**.
6. Configure Step 2 — Status Data:
   - Add fields for each warfighting function status (personnel, readiness, logistics, maintenance, communications) as appropriate dropdown or numeric fields.
   - Use conditional field visibility: show the `maintenanceDetailNotes` text field only if `maintenanceStatus` is set to AMBER or RED.
7. Configure Step 3 — Certification:
   - Set this step as read-only summary mode — display all values from Steps 1 and 2.
   - Add a single **Certify and Submit** checkbox: "I certify this report is accurate and complete."
   - Mark the checkbox as **Required** before submission is enabled.
8. Configure the **Effect** (what the Action does on submission): update the `UnitStatus` object properties with the submitted values. Map each form field to the corresponding Object Type property.
9. Configure the **Confirmation Message**: display the unit name and reporting period in the confirmation.
10. Test the Action using the Ontology Manager preview. Submit a test record and verify the target object updates correctly.

> **CAUTION: Multi-step Actions that modify production objects must be tested against a non-production Ontology branch before deployment. Test with a designated test object, not a live operational record. Confirm with your team lead before publishing any Action that modifies shared operational data.**

---

### 5-3. Conditional Logic in Actions

Conditional logic in Actions controls which fields are displayed, which fields are required, and which validation rules apply based on the values submitted in the same or prior steps. This allows a single Action to support multiple scenarios without creating separate Actions for each case.

**Common conditional patterns in USAREUR-AF Actions:**

| Scenario | Conditional Logic |
|---|---|
| Show maintenance notes only for AMBER/RED maintenance status | Show `maintenanceNotes` field if `maintenanceStatus` is AMBER or RED |
| Require commander signature for RED readiness submissions | Mark `commanderSignature` field required if `overallReadiness` equals RED |
| Show coalition sharing confirmation only for non-SECRET reports | Show `mpeShareConfirmation` checkbox if `reportClassification` is not SECRET |
| Route logistics shortfall to G4 Action queue | On submission: if `criticalShortfall` is true, trigger G4 notification Action |

---

**TASK 5-2. CONFIGURE CONDITIONAL FIELD VISIBILITY IN AN ACTION FORM**

**CONDITIONS:** Given an Action form for SITREP submission, when a conditional field should display only when specific conditions are met in a prior field selection.

**STANDARDS:** The conditional field is hidden by default. It becomes visible and required immediately when the triggering condition is met. It returns to hidden (and its value cleared) if the triggering condition is removed before submission.

**PROCEDURE:**
1. In the target Action's form editor, locate the trigger field (the field whose value controls visibility of the conditional field).
2. Add the conditional field below the trigger field.
3. In the conditional field's settings, locate the **Visibility** control.
4. Set visibility to **Conditional on field value**: select the trigger field and specify the triggering value(s) (e.g., show when `maintenanceStatus` is AMBER or RED).
5. In the conditional field's **Required** setting, enable **Conditionally Required**: required when visible (trigger condition met); not required when hidden.
6. Enable **Clear on hide**: ensures the conditional field's value is cleared if the user changes the trigger field back to a non-triggering value before submitting.
7. Preview the form. Test by setting the trigger field to a non-triggering value (confirm conditional field is hidden), then to the triggering value (confirm it appears and is required), then back to non-triggering (confirm it hides and clears).

---

### 5-4. Approval Chain Configuration

Approval chains require one or more designated reviewers to approve an Action submission before the Effect is applied to the Ontology. This is required for operational workflows where data changes require command authority — for example, changing a unit's readiness rating, publishing a theater logistics assessment, or updating an ISR collection priority.

---

**TASK 5-3. CONFIGURE AN APPROVAL CHAIN FOR A HIGH-IMPACT ACTION**

**CONDITIONS:** Given an Action that modifies a unit's official readiness status, when this modification requires review and approval by the unit's S3 or G3 before taking effect.

**STANDARDS:** On submission, the Action enters a pending state and routes a notification to the designated approver(s). The Ontology object is not updated until the approver explicitly approves the submission. Rejection returns the submission to the submitter with rejection comments.

**PROCEDURE:**
1. In the target Action's editor, navigate to the **Approval** settings section.
2. Enable **Requires Approval**.
3. Configure the **Approver** assignment:
   - Static approver: designate a specific MSS user or group (e.g., the `G3-ReadinessApprovers` group) as required approvers.
   - Dynamic approver: if the approver should vary based on the submitted data (e.g., the approver is the supervisor of the reporting unit), configure a dynamic approver lookup using the relevant Ontology link. This requires the `supervisor` or `commandingOfficer` link to be properly configured on the Object Type.
4. Set the **Approval Deadline**: configure an auto-escalation if the approval is not completed within a specified time (e.g., 24 hours escalates to the next level).
5. Configure the **Rejection Flow**: enable a rejection reason comment field. Route the rejection back to the original submitter as an MSS notification with the reviewer's comment.
6. Configure the **Notification**: ensure approvers receive an MSS notification with the pending Action details and a direct link to the approval queue.
7. Test the approval flow using two test accounts: submit with the submitter account; approve or reject with the approver account. Verify the Ontology object updates only on approval, not on initial submission.

> **NOTE:** Approval chains are only as effective as the process governance around them. An approval chain with no defined SLA for review is a bottleneck, not a control. Define and communicate the expected review window to designated approvers before deploying any approval-gated Action to production.

---

## CHAPTER 6 — AIP LOGIC CONFIGURATION

### 6-1. AIP Logic at TM-30 Level

AIP Logic is MSS's framework for integrating large language models and AI reasoning into operational workflows. At TM-30 level, the advanced builder configures AIP Logic workflows — defining inputs, writing prompts, connecting AI outputs to ontology data, and designing human review gates — entirely through the AIP Logic configuration UI.

TM-30 builders do not write code in AIP Logic configuration. You design the workflow logic, write prompts, and connect the AI to ontology data sources. If a workflow requires custom TypeScript logic, external API calls, or Functions on Objects integration, that work is for a -40 developer.

> **WARNING: AIP Logic workflows that operate on operational data — particularly ISR products, personnel data, or readiness assessments — require authorization review by your chain of command and coordination with the USAREUR-AF C2DAO before deployment. AI-assisted outputs that inform operational decisions must include human review gates. Do not deploy AIP Logic workflows that produce outputs used directly in operational reports without a documented human-in-the-loop checkpoint.**

---

### 6-2. AIP Logic Workflow Design

Before configuring anything in the AIP Logic UI, design the workflow on paper. A poorly designed AIP Logic workflow that produces plausible-sounding but incorrect outputs is worse than no AI integration — it introduces confident errors into operational products.

**AIP Logic workflow design checklist:**

- [ ] What operational question is the AI answering? State it in one sentence.
- [ ] What data inputs does the AI need to answer that question? (Ontology objects, dataset fields, user-provided context)
- [ ] What is the expected output format? (Structured JSON, natural language summary, classification label, ranked list)
- [ ] How will the output be validated before use? Who reviews it? Is there a documented review gate?
- [ ] What happens when the AI produces an incorrect or low-confidence output? Is there a fallback?
- [ ] Is there a requirement to retain a record of AI inputs and outputs for auditability?
- [ ] Has this use case been reviewed for authorization compliance?

---

### 6-3. Prompt Engineering Basics

Prompt quality determines output quality. Advanced builders writing prompts for operational AIP Logic workflows must apply basic prompt engineering discipline.

**Prompt design principles:**

1. **Be explicit about role and context.** Tell the model who it is and what context it is operating in. Example: "You are an operational data analyst supporting USAREUR-AF readiness reporting. You are reviewing SITREP submissions from subordinate units in the V Corps AOR."
2. **Specify output format precisely.** If you need structured output, specify the exact format in the prompt: "Return your assessment as a JSON object with the fields: `readinessTier` (GREEN, AMBER, or RED), `primaryConcern` (one sentence), and `recommendedAction` (one sentence)."
3. **Provide constraints.** Tell the model what it must not do: "Do not speculate about future operations. Do not reference specific classified information. Do not produce assessments for units not included in the provided data."
4. **Include examples where applicable (few-shot prompting).** For classification tasks, provide one to three examples of correct input-output pairs in the prompt. This significantly improves consistency.
5. **Test with edge cases.** Deliberately test your prompt with incomplete data, conflicting values, and boundary conditions. Prompt behavior at the edges is often worse than at the center.

---

**TASK 6-1. CONFIGURE AN AIP LOGIC WORKFLOW FOR SITREP SUMMARIZATION**

**CONDITIONS:** Given AIP Logic access and a `UnitSITREP` Object Type containing structured readiness data from multiple subordinate units, when configuring a workflow that generates a commander's summary of theater readiness from current SITREP data.

**STANDARDS:** The workflow accepts a filtered set of `UnitSITREP` objects as input, generates a structured readiness summary in the configured output format, and routes the output to a human reviewer queue before the summary is published to any application. The workflow completes in under 30 seconds for inputs of up to 50 SITREP records.

**PROCEDURE:**
1. Open AIP Logic from the left navigation panel.
2. Create a new Logic workflow. Name it: `USAREUR-AF Daily Readiness Summarization`.
3. Configure the **Input** node:
   - Select **Object Set** as input type.
   - Link the input to the `UnitSITREP` Object Type.
   - Configure input filters: allow the calling application (Workshop) to pass a filtered object set (e.g., filtered by reporting period and AOR).
4. Configure the **Prompt** node:
   - Write the system prompt per the principles in section 6-3. Begin with explicit role and context framing.
   - Reference input object properties in the prompt using the available property insertion syntax. Insert `reportingUnit`, `reportingPeriod`, `personnelReadiness`, `equipmentReadiness`, and `commanderNote` fields from each SITREP object.
   - Specify output format: require a JSON structure with `overallTheaterAssessment`, `criticalShortfalls` (list), `units_at_risk` (list of unit names), and `recommendedActions` (list).
5. Configure the **Output** node:
   - Set output type to **Structured JSON** matching the format specified in the prompt.
   - Map the output fields to a `ReadinessSummary` Object Type (configure this object type first if it does not exist).
6. Configure the **Human Review Gate**:
   - Enable **Requires Human Review** before the output is committed to the Ontology.
   - Route the review task to the designated reviewer group (e.g., `G3-ReadinessReviewers`).
   - Set the review deadline (e.g., 2 hours).
7. Test the workflow using a sample SITREP object set. Verify output format, review gate routing, and response time.

> **CAUTION: AIP Logic outputs must not be automatically published to coalition-accessible data products without both human review and C2DAO coordination. Any AIP-generated product that could reach MPE systems or coalition partners requires a separate authorization review.**

---

### 6-4. Connecting AIP Logic to Ontology Data

AIP Logic workflows that connect to real Ontology data produce more contextually accurate outputs than workflows operating on raw text inputs. Connecting AI to structured Ontology data allows the model to reason about operational entities — units, locations, events — with the same semantic context that your Workshop applications use.

**Key connection patterns:**

| Pattern | Use Case |
|---|---|
| Object Set input | Pass a filtered set of Ontology objects as the AI's primary data source (see Task 6-1) |
| Link traversal in prompt context | Provide not just the primary object's properties but also linked objects' properties (e.g., provide the unit's current location and garrison alongside its status report) |
| Object property output | Write the AI's output back to a specific Ontology object property (e.g., write the generated summary to `ReadinessSummary.aiGeneratedNarrative`) |
| Object creation output | Have the AI create new Ontology objects (e.g., generate a `RiskFlag` object for each identified shortfall) — configure via Action-type output in AIP Logic |

> **NOTE:** Link traversal in AIP Logic prompts requires that the relevant Link Types are properly configured on the Object Type. Verify link configuration in Ontology Manager before designing a workflow that depends on linked object properties. If the required links do not exist, design them (per Chapter 4) before proceeding.

---

## CHAPTER 7 — ADVANCED CONTOUR AND QUIVER

### 7-1. Contour at TM-30 Level

Contour is MSS's data analysis workspace. TM-20 covered basic filtering, sorting, and simple aggregations. TM-30 covers the formula editor for calculated columns, complex multi-table aggregations, pivot table analysis, and cross-dataset joins within Contour. These capabilities support the G2, G9, and logistics analysis workflows that require operational analytics beyond what Workshop dashboards provide.

---

### 7-2. The Contour Formula Editor

The formula editor allows creation of calculated columns using Contour's built-in function library. This is the TM-30 mechanism for operational analytics — computing derived metrics, normalizing data, and creating display-ready fields without modifying the underlying dataset.

**Contour formula function categories:**

| Category | Key Functions | Operational Use |
|---|---|---|
| Conditional | `if()`, `case()`, `coalesce()` | Readiness tier classification, null handling |
| Date/time | `dateDiff()`, `dateAdd()`, `dateFormat()`, `daysOld()` | Days since SITREP, reporting lag analysis |
| String | `concat()`, `trim()`, `left()`, `right()`, `replace()` | Unit display name formatting, DTG normalization |
| Math | `round()`, `abs()`, `min()`, `max()`, `percentage()` | Readiness score calculations, fill rate percentages |
| Aggregation | `sum()`, `count()`, `countDistinct()`, `avg()` | Unit counts by status, aggregate readiness |
| Lookup | `lookup()` | Cross-dataset reference lookups |

---

**TASK 7-1. CREATE A CALCULATED COLUMN IN CONTOUR**

**CONDITIONS:** Given a Contour analysis with a unit status dataset containing a `lastSitrepDate` timestamp field, when the analysis requires a "days since last SITREP" column for staleness analysis.

**STANDARDS:** The calculated column `daysSinceLastSitrep` correctly computes the number of whole days between `lastSitrepDate` and today's date. The column displays correctly for all rows including null `lastSitrepDate` values (display N/A for nulls).

**PROCEDURE:**
1. Open the target Contour analysis. Verify the dataset containing `lastSitrepDate` is loaded.
2. In the column header row, select **+ Add Column** then **Calculated Column**.
3. Name the column: `daysSinceLastSitrep`.
4. Open the formula editor.
5. Enter: `if(isNull(lastSitrepDate), "N/A", string(dateDiff(today(), lastSitrepDate, "day")))`.
6. Click **Preview** to validate the formula against sample rows.
7. Verify: rows with valid `lastSitrepDate` show a positive integer. Rows with null `lastSitrepDate` show N/A.
8. Apply the column. Sort by `daysSinceLastSitrep` descending to identify units with the most stale reporting.

> **NOTE:** The formula language in Contour's calculated column editor uses the same syntax as Pipeline Builder's Derived Column node (see Chapter 3). Formulas developed and validated in Contour can be transferred to Pipeline Builder when the calculation needs to be made persistent in the dataset. This two-step workflow — prototype in Contour, promote to Pipeline Builder — is the recommended approach for new calculated columns.

---

### 7-3. Pivot Table Analysis

Pivot tables in Contour aggregate data across two or more categorical dimensions simultaneously. For USAREUR-AF operational analysis, pivot tables answer questions like: "What is the distribution of readiness tiers across formations and warfighting functions?" or "How many ISR events were recorded by collection type and by Baltic flank sector this week?"

---

**TASK 7-2. BUILD A PIVOT TABLE FOR THEATER READINESS ANALYSIS**

**CONDITIONS:** Given a Contour analysis with a unit status dataset containing `formation`, `warfightingFunction`, and `readinessTier` fields, when performing cross-dimensional readiness analysis.

**STANDARDS:** The pivot table displays formations as rows, warfighting functions as columns, and count of records in cells. The analyst can identify at a glance which formation-function combinations have the highest concentration of AMBER/RED status.

**PROCEDURE:**
1. In the Contour analysis, select **Transform** then **Pivot**.
2. Set **Row dimension**: `formation`.
3. Set **Column dimension**: `warfightingFunction`.
4. Set **Value**: Count of UnitStatus records.
5. Apply a conditional color format (heat map) to the cells: green background for cells where no RED tiers are present; amber background for cells with any AMBER; red background for cells with any RED.
6. Add a filter on `reportingPeriod` to restrict the analysis to the current reporting window.
7. Export the pivot table to a Contour View (saved analysis) named per USAREUR-AF naming conventions for reuse.

---

### 7-4. Cross-Dataset Analysis

Contour supports joining datasets within an analysis — analogous to Pipeline Builder joins, but performed analytically without modifying underlying datasets. This supports ad hoc analysis that bridges data domains without requiring a new integration pipeline.

> **CAUTION: Cross-dataset joins in Contour are analytical — they produce results in the analysis workspace, not persistent new datasets. If an analysis join produces valuable curated data that should be shared with other users or applications, promote it to a Pipeline Builder pipeline (coordinating with your team lead) rather than using Contour as a data production tool. Contour is for analysis; Pipeline Builder is for data production.**

---

**TASK 7-3. PERFORM A CROSS-DATASET ANALYSIS IN CONTOUR**

**CONDITIONS:** Given a readiness dataset and a separate logistics dataset sharing a `unitId` key, when performing an analysis to identify correlations between logistics shortfalls and readiness degradation.

**STANDARDS:** The analysis workspace contains a joined view of both datasets on `unitId`. The analyst can create calculated columns and pivot tables that reference fields from both source datasets simultaneously. The analysis is saved as a Contour View for team access.

**PROCEDURE:**
1. Open Contour and load the readiness dataset as the primary source.
2. Select **Join Dataset** from the transform toolbar.
3. Select the logistics dataset as the secondary source.
4. Configure join type: **Left Join** on `unitId = unitId`. Verify column name disambiguation for any duplicate column names (e.g., rename `logistics.reportingDate` to `logisticsReportingDate`).
5. Preview the joined output. Check row count equals primary dataset row count (assuming one-to-one relationship).
6. Create a calculated column: `logisticsShortfallFlag = if(criticalShortfallCount > 0, "YES", "NO")`.
7. Create a scatter plot: X axis = `readinessScore`, Y axis = `criticalShortfallCount`, color = `readinessTier`. Assess visual correlation.
8. Save the analysis as a Contour View. Name it per conventions. Set access to the appropriate team group.

---

### 7-5. Advanced Quiver Dashboards

Quiver is MSS's linked analysis and visualization environment. Quiver dashboards allow multiple chart views to be linked — selecting a data point in one chart updates all other charts in the dashboard simultaneously. Quiver is appropriate for analytical deep-dives; Workshop is appropriate for operational dashboards used in daily operations. Both are TM-30 tools.

**Quiver vs. Workshop selection guide:**

| Criterion | Quiver | Workshop |
|---|---|---|
| Primary audience | Analysts (G2, G9, S2 shops) | Operators, commanders, staff at all levels |
| Interaction pattern | Click to explore, drill down | Monitor status, submit updates, take action |
| Data modification | Read-only | Actions and write-back supported |
| Layout flexibility | Analysis-optimized, chart-dense | Flexible, operationally designed |
| Embedding | Embeddable in Workshop as an iframe | Native Workshop |

---

**TASK 7-4. BUILD A LINKED QUIVER DASHBOARD FOR ISR EVENT ANALYSIS**

**CONDITIONS:** Given ISR event data from the Baltic flank in a Contour analysis, when an ISR analyst needs a linked dashboard showing event distribution by type, time, and grid sector simultaneously.

**STANDARDS:** The Quiver dashboard contains at least three linked chart views: (1) event count by type (bar chart), (2) event timeline (time series), (3) event density by grid sector (map or heat map). Selecting a bar in chart 1 filters both chart 2 and chart 3 to that event type. All charts update simultaneously on selection.

**PROCEDURE:**
1. Open the source Contour analysis containing the ISR event data.
2. Select **Create Quiver Dashboard** from the analysis toolbar.
3. In the Quiver dashboard editor, add the first panel: **Bar Chart** — event count by `eventType`.
4. Add the second panel: **Time Series** — event count over time, grouped by `eventType`.
5. Add the third panel: **Map** (or **Heat Map** if precise grid coordinates are available) — event density by grid sector.
6. Enable **Link Selections**: in the dashboard settings, configure all three panels to share a common selection state on the `eventType` field.
7. Test linked behavior: click a bar in chart 1. Verify charts 2 and 3 update to show only events of the selected type.
8. Configure the dashboard title, description, and access group.
9. To embed this Quiver dashboard in a Workshop application: copy the embed URL from the dashboard share settings. In Workshop, add an **Iframe** widget and paste the embed URL. Size the iframe appropriately within the Workshop layout.

> **NOTE:** Quiver dashboards embedded in Workshop via iframe do not inherit Workshop's variable context. A user's selection in a Workshop object table will not automatically filter the embedded Quiver dashboard. If synchronized filtering between Workshop and embedded Quiver is required, coordinate with a -40 developer — this integration requires URL parameter passing that goes beyond standard Quiver embed configuration.

---

## CHAPTER 8 — DATA GOVERNANCE AND STEWARDSHIP

### 8-1. The -30 Builder's Governance Responsibilities

Advanced builders are not just consumers of the data governance framework — at TM-30 level, you are active participants in it. You are responsible for the quality, lineage, and domain alignment of the data products you design and publish.

**Governance responsibilities at TM-30 level:**

| Responsibility | What It Means in Practice |
|---|---|
| Lineage documentation | Every pipeline you design must have documented lineage. After build, verify the lineage graph is complete and correct. |
| Data quality review | Review quality check results for datasets your pipelines produce. Investigate and resolve flagged issues. |
| Steward coordination | Coordinate with the domain data steward before modifying shared Object Types, publishing new data products, or changing access controls. |
| UDRA alignment | Complete the UDRA Alignment Checklist (Appendix C) for every new data product. |
| Domain assignment | Every dataset and Object Type you create must have a domain assignment. Confirm the correct domain with your steward before creating resources. |
| Data product SLA | Define and document the refresh rate, acceptable downtime, and quality floor for every data product you own. |

---

### 8-2. Reading and Interpreting Data Lineage Graphs

Data lineage in MSS tracks the path of data from its source through every transformation, join, and enrichment step to its final output. The lineage graph is your primary tool for: (a) understanding how a downstream error propagated from an upstream source, (b) assessing the impact of a planned change to a shared dataset, and (c) documenting provenance for governance audits.

---

**TASK 8-1. TRACE A DATA QUALITY ISSUE USING THE LINEAGE GRAPH**

**CONDITIONS:** Given a downstream Workshop application displaying incorrect readiness values, when the root cause is unknown and must be traced through the data pipeline.

**STANDARDS:** The builder identifies the specific transform or pipeline node where the incorrect values originate, documents the finding, and notifies the relevant data steward and/or pipeline owner for remediation.

**PROCEDURE:**
1. Open Compass. Navigate to the output dataset backing the affected Workshop application (identify the dataset from the Workshop widget's data source binding).
2. Open the dataset preview. Identify a specific row with the incorrect value and note the record's unique identifier.
3. Select **View Lineage** from the dataset options menu. The lineage graph opens showing all upstream dependencies.
4. Starting from the output dataset, trace upstream one hop at a time. At each node (transform, join, source dataset), preview that dataset and look up the same record by its unique identifier.
5. When you find the first hop where the value is incorrect, you have identified the transform or source data where the problem originates.
6. If the problem is in a transform node: note the transform name and the specific logic step. Escalate to the pipeline owner or -40 developer with: the affected dataset RID, the record identifier, the incorrect value, the expected value, and the lineage path.
7. If the problem is in the source data: note the source dataset and the record. Notify the source system data steward.
8. Document your findings in the team's issue tracking log.

> **NOTE:** The lineage graph also supports impact analysis — the reverse direction. Before modifying a shared dataset, use lineage to view all downstream consumers. Any dataset, Object Type, or Workshop application that depends on the dataset you are about to modify will be shown. Review all downstream consumers before making changes to shared production resources.

---

### 8-3. Data Quality Review and Stewardship

MSS runs automated data quality checks on configured datasets. At TM-30 level, you review these check results, investigate failures, and coordinate remediation with upstream data owners and -40 developers.

**Quality check severity levels:**

| Severity | Meaning | Required Action |
|---|---|---|
| ERROR | Check failed; data does not meet quality standard | Pipeline should not proceed to downstream consumers until resolved; escalate immediately |
| WARNING | Check flagged a potential issue; data may still be usable | Investigate within 24 hours; document disposition; notify data steward |
| INFO | Informational check; no action required but worth noting | Review during routine pipeline monitoring |

---

**TASK 8-2. REVIEW DATA QUALITY CHECK RESULTS AND ESCALATE APPROPRIATELY**

**CONDITIONS:** Given a production dataset with configured quality checks, when the quality check report for the most recent pipeline run is available for review.

**STANDARDS:** The builder reviews all check results, documents any failures or warnings, assesses impact on downstream consumers, and escalates ERROR-level failures within the required time window.

**PROCEDURE:**
1. Open the target dataset in Compass.
2. Select the **Quality Checks** tab (or navigate to the pipeline's build log and select the checks view).
3. Review all check results from the most recent run. Note: check name, severity, expected value, actual value, affected row count.
4. For each ERROR-level failure:
   a. Assess downstream impact using the lineage graph (which applications and Object Types consume this dataset?).
   b. Determine if downstream consumers should be paused or flagged as potentially unreliable.
   c. Escalate to the pipeline owner (or -40 developer if the check involves custom logic) within 2 hours.
   d. Notify the domain data steward.
   e. If downstream applications are actively displaying data to operational users, notify the application owner so they can alert users to the data quality issue.
5. For each WARNING-level failure:
   a. Investigate the root cause.
   b. Document in the team issue log: check name, actual value, expected value, suspected cause.
   c. Notify the data steward within 24 hours.
6. Document all actions taken in the team's issue tracking log with timestamps.

---

### 8-4. UDRA Domain Alignment

All data products created on MSS must align with UDRA v1.1. Domain alignment means assigning every dataset, Object Type, and application to a specific data domain with a designated domain owner responsible for its governance.

**USAREUR-AF primary data domains (representative):**

| Domain | Covers | Primary Steward |
|---|---|---|
| Personnel and Readiness | PERSTAT, readiness ratings, strength data | G1 / C2DAO |
| Intelligence | ISR events, collection assets, threat assessments | G2 |
| Operations | SITREPs, task organization, operational reports | G3 |
| Logistics | Supply, maintenance, transportation, distribution | G4 |
| Plans | OPORD-related data, course of action products | G5 |
| Comms / C2 Systems | Network status, C2 systems data | G6 / S6 |
| Civil Affairs | CMO assessments, host nation data, HCA projects | G9 |
| Coalition/MPE | Partner nation data products, MPE-shared resources | C2DAO / G6 |

> **NOTE:** Confirm your data domain assignment with the USAREUR-AF C2DAO data governance team before creating any new data product. Domain assignments affect access control, stewardship responsibility, and downstream sharing eligibility. An incorrectly assigned domain can result in a data product being blocked from the users who need it or shared with users who should not have it.

---

### 8-5. Coordinating with the Data Steward and C2DAO

The data steward is the operational authority for a data domain. The C2DAO is the USAREUR-AF architecture authority. Know when to coordinate with each.

**When to contact the data steward:**
- Before creating a new Object Type in their domain
- Before modifying properties on a shared Object Type
- When a quality check ERROR is detected on a dataset in their domain
- Before publishing a new data product to production
- When access controls for a domain dataset need to change

**When to contact the C2DAO:**
- Before publishing any data product accessible to MPE or coalition-facing systems
- Before designing a new data domain or sub-domain
- When a design decision has enterprise-wide architecture implications
- Before integrating a new external data source into MSS
- Before deploying an AIP Logic workflow on operationally significant data

---

## CHAPTER 9 — ENVIRONMENT MANAGEMENT AND PRODUCTION DISCIPLINE

### 9-1. The MSS Development Lifecycle

MSS supports a branched development lifecycle that separates development work from production resources. At TM-30 level, understanding and following the branching strategy is not optional — it is how you protect shared infrastructure from your own development work.

**Standard USAREUR-AF MSS development lifecycle stages:**

```
DEVELOPMENT BRANCH
(Personal or feature branch — safe to break)
        |
        v
TEAM REVIEW
(Pull request or branch review — peer check)
        |
        v
STAGING / TEST
(Integrated test environment — validated against production data volume)
        |
        v
PRODUCTION
(Main branch — live operational data, commander visibility)
```

Nothing enters production without passing through team review. Nothing skips staging for "quick fixes." There are no quick fixes in production data infrastructure.

---

### 9-2. Ontology Branch Management

The Ontology is a shared resource. Multiple builders may be working on different features simultaneously. Ontology branches allow each builder to work on their feature without interfering with others and without affecting production.

---

**TASK 9-1. CREATE AND MANAGE AN ONTOLOGY DEVELOPMENT BRANCH**

**CONDITIONS:** Given a new Ontology design task (e.g., adding a new Object Type or modifying Link Type cardinality), when beginning development on the shared Ontology.

**STANDARDS:** All development occurs on a named development branch. No changes are made to the main Ontology branch. The development branch is reviewed and approved before merge.

**PROCEDURE:**
1. Open Ontology Manager.
2. In the branch selector (top of the Ontology Manager interface), select **Create New Branch**.
3. Name the branch: `dev-[feature]` or `dev-[your-name]-[feature]` (e.g., `dev-isr-event-object`, `dev-smith-readiness-action`).
4. Confirm you are working on the named branch (the branch name should be displayed in the Ontology Manager header at all times during your session).
5. Make all Object Type, Link Type, and Action changes on this branch.
6. When development is complete, request a branch review from your team lead. Provide: the branch name, a summary of all changes made, and the test results from your functional testing.
7. After review approval, merge the branch to main. Do not self-approve — a second set of eyes is required for all Ontology changes.
8. After merge, confirm the changes are visible in the main branch and verify no unexpected impacts on existing Workshop applications (check application health indicators in Workshop after the merge).

> **CAUTION: Deleting an Object Type or Link Type property from a production Ontology branch immediately breaks every Workshop application widget, Contour analysis, and Pipeline Builder node that references that property. Before removing any property, search for all references using the Ontology Manager's "find usages" function. Coordinate with all application owners before proceeding.**

---

### 9-3. Dataset and Pipeline Branching

Pipeline Builder supports branching for dataset development. Like Ontology branching, dataset branches allow you to develop and test pipeline changes against a copy of production data without affecting the production dataset.

---

**TASK 9-2. MANAGE A PIPELINE DEVELOPMENT BRANCH**

**CONDITIONS:** Given a modification to a production pipeline (e.g., adding a new calculated column or modifying join logic), when the change cannot be tested in production.

**STANDARDS:** The modification is developed and tested on a named branch. The branch output is validated against a production-representative data sample before merge. The modification reaches production only after team lead approval.

**PROCEDURE:**
1. In Pipeline Builder, open the target pipeline.
2. Select **Create Branch** from the pipeline options menu.
3. Name the branch per conventions. Confirm the branch name is displayed in the pipeline editor header.
4. Make all modifications on the branch.
5. Run the branch pipeline against the full dataset (or a representative sample if full-volume testing is impractical).
6. Validate output: check row counts, spot-check calculated column values, verify no quality check failures.
7. Document test results: the expected output vs. actual output for at least three representative records.
8. Submit the branch for team lead review. Include: branch name, change summary, test results, and downstream impact assessment (from lineage review).
9. After approval, merge to main and monitor the first scheduled run in production.

---

### 9-4. Production Gate Criteria

**A data product is ready for production when:**

- [ ] All development and testing completed on a named development branch
- [ ] Branch review completed and approved by team lead
- [ ] Quality checks pass (no ERROR-level failures on staging run)
- [ ] Data lineage graph is complete and accurate
- [ ] UDRA Alignment Checklist (Appendix C) completed
- [ ] Application Design Checklist (Appendix B) completed (for Workshop applications)
- [ ] Data steward has been notified and has approved publication
- [ ] All downstream consumers have been identified via lineage review
- [ ] Access controls configured correctly and verified
- [ ] Pipeline alerts configured (for pipelines)
- [ ] If MPE/coalition-accessible: C2DAO coordination complete and documented

**A data product is NOT ready for production if:**

- Testing was performed on the production branch
- Quality checks have unresolved ERROR-level failures
- The data steward has not been notified
- Downstream impact has not been assessed
- Access controls have not been verified

---

### 9-5. Coordinating with -40 Developers in the Development Lifecycle

When your design includes components that require a -40 developer, the development lifecycle has an additional coordination layer.

**-30 to -40 coordination protocol:**

1. **Before development begins.** Provide the -40 developer with the complete requirements document (Appendix A template). Do not begin any implementation work — in Pipeline Builder, Ontology Manager, or Workshop — until the -40 developer has reviewed and confirmed the requirements are complete and implementable.
2. **During development.** Coordinate on branch strategy. If the -40 developer's code changes and your Ontology/Pipeline changes are interdependent, agree on the order of implementation and the integration test plan before either party begins.
3. **Before production.** Participate in the integration review. As the -30 designer, you are the acceptance authority — verify that the implemented system meets the operational requirements you specified.
4. **After production.** You own the operational monitoring. The -40 developer owns the technical components. Alert the -40 developer when a quality check or performance anomaly suggests a problem in the technical implementation.

---

## CHAPTER 10 — NATO AND COALITION DATA CONSIDERATIONS

### 10-1. The Coalition Data Environment

USAREUR-AF operates in an inherently coalition environment. V Corps functions as a NATO corps headquarters. Exercise DEFENDER and associated operations involve forces from across the Alliance. The Suwałki Gap defense concept and Baltic flank posture require near-seamless data sharing with Estonian, Latvian, Lithuanian, and Polish forces, as well as other NATO Allies.

MSS is a U.S. national system. Coalition partners access shared data products through the Mission Partner Environment (MPE). Data products designed on MSS that will be shared with coalition partners cross a domain boundary when they enter the MPE. This boundary has governance, technical, and security implications that TM-30 builders must understand — not to implement solutions to, but to recognize when escalation is required.

> **CAUTION: Data products shared with NATO partners or accessible in the Mission Partner Environment must comply with NAFv4 architecture standards and applicable STANAG requirements. Coordinate with G6/S6 and the USAREUR-AF C2DAO before publishing any cross-domain data product. Failure to comply may result in the product being blocked from coalition-facing distribution or revoked post-publication.**

---

### 10-2. MPE Data Handling

The Mission Partner Environment is a separate network environment from the U.S. national network hosting MSS. Data products that need to be available to coalition partners must be explicitly authorized, formatted for cross-domain transfer, and reviewed by the C2DAO and G6 before transfer to the MPE.

**What TM-30 builders must know about MPE:**

| Topic | What -30 Needs to Know |
|---|---|
| MPE eligibility | Not all data products are eligible for MPE sharing. Eligibility is determined by classification, releasability markings, and C2DAO review — not by the builder. |
| Data markings | MPE-eligible data products must carry correct releasability markings (e.g., REL TO USA, [PARTNER NATIONS]). Markings are configured in dataset settings and must be set correctly before any MPE transfer. |
| NAFv4 format requirements | Data products shared via MPE must conform to NAFv4 architecture standards. This includes standardized vocabulary, NATO-compatible terminology, and documented data element definitions. |
| STANAG compliance | Specific STANAGs govern data exchange for specific domains (e.g., STANAG 5516 for tactical data links). Identify applicable STANAGs before designing any product intended for coalition exchange. |
| C2DAO coordination | The C2DAO is the approval authority for MSS data products entering the MPE. No data crosses the boundary without C2DAO sign-off. |
| G6/S6 coordination | G6/S6 manages the technical cross-domain solution (CDS). They must be involved in any discussion of MPE data transfer — they own the pipes. |

---

### 10-3. NAFv4 Awareness for Builders

NATO Architecture Framework version 4 (NAFv4) is the enterprise architecture standard for NATO and Allied systems. TM-30 builders are not expected to implement NAFv4 compliance — that is a C2DAO and G6 responsibility. But you must be aware of NAFv4 requirements during the design phase, because retroactively making a non-compliant data product NAFv4-compliant after it has been published to coalition partners is expensive and sometimes impossible.

**NAFv4 design considerations for -30 builders:**

1. **Use NATO-compatible terminology in Object Type names and properties where applicable.** The ADP to JP to NATO Crosswalk at `learn-data.armydev.com` provides the mapping between Army, Joint, and NATO data terms. If your data product might reach coalition partners, use the NATO-compatible term in your design.
2. **Document data element definitions.** NAFv4 requires that all shared data elements be defined in a shared data dictionary. For any Object Type property that will be in a coalition-shared product, write a clear definition in the property description field — not just the field name.
3. **Flag potential MPE-eligible products early.** If you suspect during design that a data product might eventually need to be shared with coalition partners — even if it is not the immediate requirement — flag this in your design document. It is far easier to design for MPE eligibility from the start than to retrofit it later.
4. **Do not design around the boundary.** Some builders attempt to design workarounds that avoid the MPE governance process. This is a security violation. The boundary exists for a reason. Escalate; do not circumvent.

> **NOTE:** For operational data products supporting Suwałki Gap defense planning, Baltic flank posture assessments, or exercises involving the Enhanced Forward Presence (eFP) battlegroups in Estonia, Latvia, Lithuania, or Poland — initiate C2DAO and G6 coordination at the design stage, before any implementation. These products have a high likelihood of requiring coalition data sharing and benefit from early governance engagement.

---

### 10-4. When to Escalate

Knowing when to escalate — and to whom — is a primary TM-30 competency for coalition data issues.

**Escalation matrix for coalition data questions:**

| Situation | Escalate To |
|---|---|
| Data product may be shared with coalition partners | C2DAO (architecture review) + G6/S6 (CDS/MPE technical) |
| Unsure of releasability marking for a dataset | Data steward for the domain + G2 (for classification questions) |
| NAFv4 or STANAG compliance question | C2DAO architecture authority |
| Coalition partner requests access to an MSS data product | G6/S6 + C2DAO — do not grant access directly; route through governance |
| A coalition partner's data needs to be ingested into MSS | G6/S6 (source connectivity) + C2DAO (domain assignment) + data steward (quality/governance) |
| AIP Logic output may be shared with MPE | C2DAO + G6/S6 + chain of command (AIP authorization review) |
| Existing data product is already on MPE and needs to be modified | C2DAO — modification of a cross-domain product requires re-review |

> **WARNING: Do not independently initiate data sharing with coalition partners or MPE systems. Even if the data appears unclassified and the intent is benign, unauthorized cross-domain data transfer is a security incident. Route all coalition data sharing requests through G6/S6 and the C2DAO without exception.**

---

### 10-5. NATO Exercises and Multi-National Data Environments

During major exercises — DEFENDER, IRON WOLF, SABER STRIKE, STEADFAST DEFENDER — the MSS data environment expands significantly. Additional users from Allied and partner nation formations access shared data products. Exercise data volumes increase. New data feeds are often stood up with compressed timelines.

**Advanced builder responsibilities during exercise support:**

1. **Pre-exercise data product review.** Review all data products your team owns for exercise-period relevance. Update pipelines, schedules, and alert thresholds for exercise tempo before the exercise start date.
2. **Coalition user access coordination.** If coalition partners will access your applications during the exercise, coordinate access provisioning through G6/S6 and C2DAO at least two weeks before the exercise. Access provisioning at the start of an exercise is a common failure point.
3. **Exercise-specific pipelines.** If the exercise requires new pipelines or Object Types, build them well in advance. Post-exercise cleanup — archiving or decommissioning exercise-specific data products — must be planned before the exercise, not after.
4. **Data segregation.** Exercise data and live operational data must not be commingled in shared Object Types without explicit design intent and data steward approval. If an exercise-specific Object Type is required, create it with an `EX-` prefix in the name to indicate exercise data.
5. **After-action data preservation.** Exercise data products that have analytical or doctrinal value should be archived, not deleted. Coordinate with G2/G3/C2DAO on exercise data retention requirements before the exercise ends.

---

## APPENDIX A — -30 TO -40 HANDOFF GUIDE: TECHNICAL REQUIREMENTS TEMPLATE

This appendix provides the standard template for -30 advanced builders to communicate design requirements to -40 developers when technical implementation components are required. Complete every section. Incomplete requirements documents waste developer time and produce incorrect implementations.

---

**TECHNICAL REQUIREMENTS DOCUMENT**

**Date:** ___________

**Requesting Builder (Name / Unit / Role):** ___________

**Developer Assigned:** ___________

**Priority:** URGENT / HIGH / ROUTINE

**Required Completion Date:** ___________

---

**SECTION 1: OPERATIONAL CONTEXT**

What mission problem does this solve?

___________

Who are the users? What decisions do they make with this product?

___________

What does success look like? Describe the operational state when this requirement is met.

___________

---

**SECTION 2: DATA INPUTS**

| Dataset | Path in Compass (RID if known) | Relevant Columns | Known Data Quality Issues |
|---|---|---|---|
| | | | |
| | | | |

Is this dataset already in MSS, or does it need to be ingested? If ingestion is required, describe the source.

___________

---

**SECTION 3: ONTOLOGY MODEL**

List all existing Object Types involved. Confirm they exist in Ontology Manager before completing this section.

| Object Type | Existing or New? | Properties Involved |
|---|---|---|
| | | |

If new Object Types are needed, provide the full specification:

| Property Name | Data Type | Source Field | Required? | Searchable? | Notes |
|---|---|---|---|---|---|
| | | | | | |

List all Link Types needed (existing or new):

| Link Type (Verb Phrase) | From Object Type | To Object Type | Cardinality | Foreign Key |
|---|---|---|---|---|
| | | | | |

---

**SECTION 4: TECHNICAL COMPONENTS REQUIRED**

Describe each component requiring -40 implementation. Be specific.

| Component | Type (FOO / Transform / OSDK / Other) | Inputs | Expected Output | Logic Description |
|---|---|---|---|---|
| | | | | |

If the component requires specific business logic (e.g., a deduplication rule or a calculation formula), describe the logic precisely. Do not write code — write the logic in plain language with examples.

___________

---

**SECTION 5: NON-FUNCTIONAL REQUIREMENTS**

| Requirement | Value |
|---|---|
| Expected data volume (rows) | |
| Required refresh rate | |
| Maximum acceptable latency | |
| Concurrent user estimate | |
| Availability requirement (e.g., 0600-2200 CET) | |

---

**SECTION 6: ACCEPTANCE CRITERIA**

How will you verify the implementation is correct? List specific, measurable checks.

1. ___________
2. ___________
3. ___________

What are the edge cases that must be tested?

1. ___________
2. ___________

---

**SECTION 7: TIMELINE, DEPENDENCIES, AND CONTACTS**

Is this requirement dependent on any other work in progress?

___________

Who must be consulted before implementation begins? (Data steward, C2DAO, G6, etc.)

___________

Requesting builder contact (phone / SIPR):

___________

Approving team lead (signature):

___________

---

## APPENDIX B — APPLICATION DESIGN CHECKLIST

Complete this checklist for every Workshop application before publishing to production. No application is published without a completed checklist on file.

**Application Information:**
- Application Name: ___________
- Builder Name / Unit: ___________
- Target User Group: ___________
- Primary Object Type(s): ___________
- Completion Date: ___________

---

**DESIGN**
- [ ] Page map completed and reviewed with end user before build began
- [ ] User roles defined and documented
- [ ] Required data (Object Types, Link Types) confirmed to exist in Ontology
- [ ] No raw datasets used as application data sources (curated only)
- [ ] Variable and parameter design documented before building

**BUILD QUALITY**
- [ ] All filter chains tested — including zero-result and all-results states
- [ ] All conditional visibility logic tested for both visible and hidden states
- [ ] Empty states configured for all widgets that display object data
- [ ] Multi-page navigation tested for all page combinations
- [ ] Cross-page parameter passing tested end-to-end
- [ ] Conditional visibility used only for UX, not for access control

**PERFORMANCE**
- [ ] Application tested with production-representative data volume (not sample data)
- [ ] Page load time under 5 seconds for primary page with production data
- [ ] Table widgets configured with pagination for sets over 200 rows
- [ ] No more than 7 linked widgets bound to a single Object Variable
- [ ] Auto-refresh intervals justified and documented (if configured below 30 minutes)

**GOVERNANCE**
- [ ] All widgets sourcing data from Ontology objects (not raw datasets)
- [ ] Application name follows USAREUR-AF naming conventions
- [ ] All widgets have descriptive titles or labels
- [ ] Access group configured — application is not world-readable unless required
- [ ] UDRA domain alignment confirmed with data steward
- [ ] Appendix C (UDRA Alignment Checklist) completed
- [ ] If MPE/coalition-accessible: C2DAO coordination complete and documented

**REVIEW**
- [ ] Team lead reviewed the application before publication
- [ ] End user(s) tested the application in staging before publication
- [ ] Any Actions in the application tested with test objects (not production records)
- [ ] Approval chains (if any) tested end-to-end with test accounts

---

## APPENDIX C — UDRA ALIGNMENT CHECKLIST

Complete this checklist for every new data product (dataset, Object Type, Workshop application, Pipeline) before publishing to production. UDRA v1.1 compliance is required for all MSS data products in the USAREUR-AF environment.

**Data Product Information:**
- Product Name: ___________
- Product Type (Dataset / Object Type / Application / Pipeline): ___________
- Builder Name / Unit: ___________
- Completion Date: ___________

---

**DOMAIN OWNERSHIP**
- [ ] Data domain assigned (see Chapter 8, section 8-4 for domain list)
- [ ] Domain assignment confirmed with USAREUR-AF C2DAO or designated domain steward
- [ ] Domain data steward identified by name and contact
- [ ] Product registered in the USAREUR-AF data product catalog (if applicable)

**DATA PRODUCT THINKING**
- [ ] Consumer(s) identified: who will use this product and what decisions do they make?
- [ ] Product owner designated (the -30 builder or delegated owner responsible for ongoing quality)
- [ ] Product description written — clear, jargon-free, accessible to a new user
- [ ] SLA defined: refresh rate, acceptable downtime, minimum quality floor

**LAYER VERIFICATION**
- [ ] Layer assignment confirmed: which of the 5 layers does this product operate at?
- [ ] No Workshop application reads from raw or staging datasets (curated only)
- [ ] No Object Type backed by an unvalidated source dataset
- [ ] Pipeline output passes all configured quality checks before downstream consumption

**FEDERATED GOVERNANCE**
- [ ] Data steward notified and approved publication
- [ ] Modifications to shared Object Types coordinated with all dependent application owners
- [ ] Access controls set per least-privilege principle — users have access to data they need, not broader access
- [ ] Data retention and archival policy identified (how long will this product be maintained?)

**DATA QUALITY (VAUTI)**
- [ ] Visible: product is discoverable in Compass with an accurate description
- [ ] Accessible: correct users have access; incorrect users do not
- [ ] Understandable: all fields/properties have descriptions; units and formats are documented
- [ ] Trustable: quality checks are configured; pipeline alerts are configured; lineage is complete
- [ ] Interoperable: if coalition-shared — NAFv4 compliance review completed (C2DAO); STANAG applicability assessed

**NATO/COALITION (if applicable)**
- [ ] MPE eligibility assessed (not assumed)
- [ ] Releasability markings correct and applied
- [ ] C2DAO coordination complete for any MPE-accessible product
- [ ] G6/S6 coordination complete for any cross-domain data transfer
- [ ] NATO-compatible terminology used in Object Type names and property names where applicable
- [ ] ADP to JP to NATO Crosswalk consulted for terminology alignment

---

## GLOSSARY

**Action.** An Ontology-configured workflow that allows MSS users to write data back to an Object Type. Actions have defined inputs (form fields), validation rules, effects (what changes), and optionally an approval chain. Configured in Ontology Manager.

**AIP Logic.** MSS's framework for integrating AI capabilities into operational workflows. AIP Logic allows advanced builders to configure AI-assisted workflows — including prompt design and ontology data connections — through a visual UI without writing code.

**Approval Chain.** A governance mechanism within an Action that requires designated reviewer(s) to approve a submission before the Action's effect is applied to the Ontology. Used for high-impact data changes that require command authority.

**C2DAO (Command and Control Data Architecture Office).** USAREUR-AF's designated architecture authority for MSS and the enterprise data environment. The C2DAO sets data architecture standards, approves domain assignments, and serves as the cross-domain authorization authority for MPE-eligible data products.

**Calculated Column.** A column derived from a formula expression applied to existing data fields. In Contour, calculated columns are analytical and do not modify the source dataset. In Pipeline Builder's Derived Column node, calculated columns become persistent in the output dataset.

**Conditional Layout.** A Workshop application design pattern in which the visibility or content of a widget or container panel is controlled by an expression rather than being static. Enables role-based views and state-driven UI without building separate applications.

**Contour.** MSS's data analysis workspace. Supports filtering, calculated columns, aggregations, pivot tables, cross-dataset joins, and chart visualizations. Analytical outputs in Contour are not persistent datasets unless explicitly promoted to Pipeline Builder.

**Cross-Domain Solution (CDS).** The technical infrastructure that enables controlled data transfer between separate network domains (e.g., from the U.S. national network to the MPE). Owned and operated by G6/S6. All data crossing the CDS boundary requires C2DAO approval.

**Data Domain.** A defined grouping of related data assets under the governance of a designated domain owner. In UDRA v1.1, all MSS data products must be assigned to a domain. Domain examples: Personnel and Readiness, Intelligence, Operations, Logistics.

**Data Lineage.** The documented path of data from its source through every transformation, join, and enrichment step to its final output. Viewed in MSS as the lineage graph. Used for root cause analysis of data quality issues and for impact assessment before modifying shared resources.

**Data Product.** In UDRA v1.1 terms, any MSS resource — dataset, Object Type, Workshop application, pipeline — that has a defined consumer, a documented purpose, a designated owner, and a stated quality SLA. All TM-30 outputs should be designed and managed as data products.

**Data Steward.** The operational authority for a data domain. Responsible for the quality, accuracy, and governance of all data products within their domain. The data steward is the first point of contact for all domain-related governance questions.

**DDOF (Doctrine-Driven Ontology Framework).** A design framework, documented at `learn-data.armydev.com`, for modeling Army operational concepts in the MSS Ontology using Army doctrinal definitions as the authoritative source for Object Type names and semantics.

**Dependent Filter.** A Workshop filter widget whose available options are constrained by the selection in a prior filter. Dependent filters prevent users from selecting filter combinations that yield no results and reduce the options presented at each step.

**eFP (Enhanced Forward Presence).** NATO's deterrence posture in the Baltic states and Poland, consisting of multinational battlegroups in Estonia, Latvia, Lithuania, and Poland. USAREUR-AF data products supporting eFP are among the highest-probability candidates for coalition data sharing.

**Federated Governance.** The UDRA model in which data governance authority is distributed among domain stewards, with the C2DAO setting architecture standards but domain stewards owning content governance for their respective domains.

**Link Type.** An Ontology configuration that defines a relationship between two Object Types. Named as a verb phrase from the perspective of the source object. Has defined cardinality (one-to-one, one-to-many, many-to-many).

**Mission Partner Environment (MPE).** The network environment through which authorized coalition partners access shared U.S. data products. Separate from the U.S. national network. All data transfer to the MPE crosses a domain boundary requiring CDS and C2DAO authorization.

**Multi-Step Action.** An Action configured with a sequential form that guides users through distinct phases of a workflow (e.g., identification, data entry, certification). Users cannot advance to the next step without completing required fields in the current step.

**NAFv4 (NATO Architecture Framework version 4).** The enterprise architecture standard governing all systems and data products operating in the NATO/EUCOM coalition environment. Data products shared with coalition partners via the MPE must comply with NAFv4 standards.

**Object Set Variable.** A Workshop variable type that holds a filtered collection of Ontology objects. Used to drive lists, tables, maps, and charts from a dynamically filtered view of an Object Type.

**Object Type.** The fundamental Ontology construct in MSS. Represents an operational concept (e.g., `UnitStatus`, `ISRCollectionEvent`) and is backed by a curated dataset. Has properties, Links, and Actions.

**Object Type Cookbook v2.** The authoritative reference for Object Type design patterns in the USAREUR-AF MSS environment, available at `learn-data.armydev.com`. Addendum A covers operational Object Types for Army warfighting functions.

**Ontology.** The semantic layer of MSS (Layer 3 of the 5-Layer Data Stack). Translates dataset rows into operational concepts with named properties, relationships (Link Types), and configurable workflows (Actions).

**Pipeline Builder.** MSS's visual (no-code) ETL tool. Allows builders to configure data ingestion, multi-source joins, column transformations, calculated columns, and scheduled execution through a drag-and-drop interface.

**Pivot Table.** An aggregation view in Contour that cross-tabulates data across two or more categorical dimensions. Displays aggregate values (count, sum, average) at each dimension intersection.

**Production Discipline.** The practice of developing all changes on named development branches, requiring review before merge, and never testing in the production environment. A foundational TM-30 professional standard.

**Prompt Engineering.** The practice of writing effective input instructions for an AI model to produce useful and accurate outputs. For TM-30 builders configuring AIP Logic, prompt engineering involves specifying role, context, output format, constraints, and examples.

**Quiver.** MSS's linked analysis and visualization environment. Supports multiple chart views linked by a common selection state, allowing interactive exploration across multiple analytical dimensions simultaneously. Embeddable in Workshop applications.

**STANAG (Standardization Agreement).** NATO standards governing specific technical domains, including data exchange formats and protocols for coalition interoperability. Applicable STANAGs vary by data domain (e.g., STANAG 5516 for tactical data links).

**UDRA v1.1 (Unified Data Reference Architecture, version 1.1, February 2025).** The Army's unified architecture standard for data products, requiring domain ownership, federated governance, data product thinking, layer verification, and VAUTI compliance.

**URL Parameter.** A Workshop application parameter passed through the application URL. Enables deep-linking — sharing a URL that opens the application with a pre-applied filter or selected object. URL parameters are visible in the URL and should not contain sensitive data.

**VAUTI.** The DoD data quality framework from the DoD Data Strategy (2020): Visible, Accessible, Understandable, Trustable, Interoperable. All MSS data products must meet all five criteria.

**Workshop.** MSS's drag-and-drop application builder. The primary tool for creating operational dashboards, data entry forms, and action-enabled applications for end users. Applications are built on Ontology Object Types and support Actions for write-back.

---

*TM-30 — MAVEN SMART SYSTEM (MSS) ADVANCED BUILDER TECHNICAL MANUAL*

*HEADQUARTERS, UNITED STATES ARMY EUROPE AND AFRICA, Wiesbaden, Germany*

*2026*

*By order of the Commanding General, United States Army Europe and Africa.*

*Distribution: Approved for public release; distribution is unlimited.*
