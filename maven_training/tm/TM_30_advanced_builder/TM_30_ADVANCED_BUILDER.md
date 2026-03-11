```
TM-30 — MAVEN SMART SYSTEM (MSS)
ADVANCED NO-CODE BUILDER TECHNICAL MANUAL

HEADQUARTERS, UNITED STATES ARMY EUROPE AND AFRICA
Wiesbaden, Germany

2026

PREREQUISITE PUBLICATIONS: TM-10, Maven User; TM-20, Builder; ADRP 1, Data Literacy
APPLIES TO: Data-adjacent specialists (17/25-series, S6/G6/G2/G9, operational data analysts)
           Foundry Workshop, Pipeline Builder, Contour, Quiver, AIP Logic (UI only)
DISTRIBUTION RESTRICTION: Approved for public release; distribution is unlimited.
```

---

## SAFETY SUMMARY

Advanced builders operate at the level where decisions directly affect production data environments
shared across the USAREUR-AF formation. Errors at this level do not affect one application — they
affect readiness reporting, operational picture, and coalition data sharing for the entire AOR.

Before operating at TM-30 level:

- Coordinate with the designated Data Steward before modifying any shared production resource
- Never develop or test in the production environment — use a dedicated branch
- Understand the downstream impact of ontology and schema changes before publishing
- All production promotions require peer review and Data Steward sign-off per C2DAO governance
- AIP Logic configurations require authorization review before activation in production

**WARNING:** Deleting or restructuring an Object Type that is referenced by active Workshop
applications, Actions, or Quiver analyses will break those downstream products without warning.
Always audit downstream dependencies before modifying shared ontology resources.

**CAUTION:** Pipeline Builder joins on large, unfiltered datasets can generate outputs that exceed
storage quotas or degrade platform performance for other users. Profile source datasets before
building multi-source joins in production.

---

## TABLE OF CONTENTS

- Chapter 1 — Introduction and Scope
- Chapter 2 — Advanced Workshop Applications
- Chapter 3 — Advanced Pipeline Builder
- Chapter 4 — Ontology Design Through the UI
- Chapter 5 — Advanced Analytics: Contour and Quiver
- Chapter 6 — AIP Logic Configuration
- Chapter 7 — Data Governance and Lineage
- Chapter 8 — Environment Management
- Chapter 9 — Standards, Conventions, and Best Practices
- Appendix A — Advanced Builder Checklist
- Appendix B — Design Patterns Reference
- Glossary

---

# CHAPTER 1 — INTRODUCTION AND SCOPE

**BLUF:** TM-30 qualifies data-adjacent specialists to build advanced no-code solutions on the
Maven Smart System — complex Workshop applications, multi-source pipelines, well-designed ontology
models, and advanced analytics — while operating within USAREUR-AF C2DAO governance requirements.

## 1-1. Scope and Purpose

1-1. This manual qualifies advanced builders who operate entirely through the MSS platform user
interface. No code is required at the TM-30 level. All tasks in this manual are accomplished
through Foundry's graphical tools: Workshop, Pipeline Builder, Ontology Manager, Contour, Quiver,
and AIP Logic.

1-2. TM-30 is the advanced tier for data-adjacent specialists — personnel who work deeply with
data but whose primary role is operational, analytical, or systems-oriented rather than software
development. This includes 17-series and 25-series signal soldiers, S6/G6 staff, G2 analysts,
G9 civil affairs, and operational data analysts embedded in brigade and division staffs.

1-3. TM-40 covers code-level development (Python transforms, TypeScript Functions on Objects,
OSDK). If your task requires writing code, reference TM-40. TM-30 stops at the UI boundary.

> **NOTE:** All items above require a TM-40 developer. For TM-20 (no-code builder) capabilities, refer to TM-20, Chapter 1. TM-30 operates at the boundary between TM-20 no-code building and TM-40 code-based development. When in doubt whether a task is TM-20 or TM-30, refer to TM-20, Chapter 1-1 (Purpose and Scope) to assess scope before escalating.

1-4. Prerequisites. Before beginning TM-30 tasks, personnel must be qualified on:
- TM-10 (Maven User): platform navigation, object search, consuming data products
- TM-20 (Builder): basic Workshop, basic Pipeline Builder, basic Object Type configuration,
  basic Contour and Quiver
- ADRP 1, Data Literacy: data governance principles, Army data policy, command data authority

Before beginning TM-30 design work, confirm you can independently perform — without manual reference — all TM-10 operator tasks (Chapters 2-7) and all TM-20 builder tasks including Workshop application building (TM-20, Chapter 5), Ontology configuration (TM-20, Chapter 4), pipeline management (TM-20, Chapter 3), and branching/governance (TM-20, Chapter 7). If you cannot confidently perform any of these tasks without reference, complete the relevant TM before advancing.

## 1-2. What TM-30 Advances Beyond TM-20

| Capability Area | TM-20 Level | TM-30 Level |
|-----------------|-------------|-------------|
| Workshop | Single-page apps, basic widgets | Multi-page apps, conditional logic, variable passing |
| Pipeline Builder | Single-source transforms, basic filters | Multi-source joins, aggregations, calculated columns |
| Ontology | Configure existing Object Types | Design Object Types, Link Types, and Actions from scratch |
| Contour | Basic charts and filters | Pivots, calculated columns, saved analysis views |
| Quiver | Single-object analysis | Multi-object dashboards, linked views, custom object sets |
| AIP Logic | Awareness | Configure and manage existing AI workflows |
| Governance | Follow naming conventions | Enforce them, review peers, coordinate with Data Stewards |
| Environment Mgmt | Aware of branching | Execute branching, review, and promotion workflows |

> **NOTE:** Advanced builders design solutions that TM-10 operators and TM-20 builders will use. Before designing at TM-30 level, understand the operator workflows from TM-10, Chapter 1 (Introduction and Overview) and TM-10, Chapter 4 (Using Workshop Applications). Your design decisions directly affect operator productivity and data quality at the operational level.

## 1-3. USAREUR-AF Operational Context

1-5. USAREUR-AF is the Army Service Component Command (ASCC) to United States European Command
(USEUCOM). Advanced builders operating in this theater support land operations across the European
AOR and integration with NATO Allied command structures. The data products built at TM-30 level
feed readiness reporting, logistics visibility, intelligence products, and operational dashboards
used by commanders at brigade through theater level.

1-6. Errors at TM-30 level have formation-wide impact. A broken Workshop application that
misrepresents equipment readiness affects commanders' decisions. A poorly designed pipeline join
that duplicates records inflates SITREP counts. A misconfigured Action that overwrites data without
validation corrupts the operational picture. Build with the same discipline you apply to any
operational task.

1-7. Governance Authority. All MSS data products built within USAREUR-AF are governed by the
Command and Control Data Authoritative Organization (C2DAO). Advanced builders are accountable
to C2DAO for:
- Naming convention compliance (datasets, Object Types, pipelines, applications)
- Access control configuration — who can view, edit, and interact with your products
- Data quality standards and issue reporting
- Production promotion approval workflows

## 1-4. Governing Policy References

1-8. The following policy documents govern advanced builder work. Builders must be familiar with
the relevant sections.

| Document | Authority | Key Provisions for Builders |
|----------|-----------|------------------------------|
| Army CIO Memorandum (April 2024) | Army CIO/G-6 | Data governance, data product ownership, access controls |
| UDRA v1.1 (February 2025) | Army Enterprise | Unified Data Reference Architecture — domain alignment |
| USAREUR-AF C2DAO Standards | USAREUR-AF G6 | Naming conventions, promotion gates, stewardship roles |
| CDA Portal (learn-data.armydev.com) | Army CDA | Training resources, design patterns, reference implementations |

1-9. CDA Portal. The Common Data Architecture (CDA) Portal at learn-data.armydev.com is the
authoritative training and reference resource for Army data platform work. Advanced builders
should consult the following CDA resources:
- Object Type Cookbook v2 + Addendum A — authoritative Object Type design guidance
- DDOF Playbook — Doctrine-Driven Ontology Framework design patterns
- Doctrine-Driven Development framework — aligning ontology models to Army operational doctrine
- ADP to JP to NATO Crosswalk — mapping Army, Joint, and NATO data constructs

---

# CHAPTER 2 — ADVANCED WORKSHOP APPLICATIONS

**BLUF:** Advanced Workshop builders design multi-page applications with dynamic behavior —
conditional visibility, variable-driven filtering, inter-page navigation, and complex layouts —
that serve as the operational data interface for commanders and staff.

## 2-1. Overview of Advanced Workshop Capability

2-1. Workshop applications built at TM-30 level go beyond single-page dashboards. They serve as
the primary operational interface for staff sections — a G2 intelligence dashboard with linked
pages for threat assessment, unit tracking, and historical trends; an S4 readiness tracker that
lets commanders drill from fleet overview to individual equipment status; a G9 civil-military
operations board that filters by AOR, time period, and activity type simultaneously.

2-2. Advanced Workshop requires mastery of three interconnected concepts: variables, conditional
logic, and multi-page navigation. These three elements, combined, allow you to build applications
that behave like purpose-built operational software — without writing a line of code.

## 2-2. Variables and State Management

**CONDITIONS:** Access to a Workshop application in edit mode; TM-20 qualification.

**STANDARDS:** Builder configures application variables correctly, demonstrates variable passing
between widgets and pages, and verifies dynamic behavior through test interactions before
publishing.

**EQUIPMENT:** MSS platform access; Workshop edit permissions on the target application.

### 2-2a. Understanding Application Variables

2-3. Variables in Workshop are named containers that store a value the user selects or that the
application computes. Widgets read variables to filter their display; user interactions write to
variables. This read/write loop is what makes Workshop applications dynamic.

2-4. Variable types available in Workshop:

| Variable Type | Use Case | Example |
|---------------|----------|---------|
| String | Text filter, selected category | Selected unit name, status code |
| Number | Numeric threshold, count | Days since last inspection |
| Boolean | Toggle, show/hide flag | Show classified records (true/false) |
| Date/DateTime | Time window selection | Report date, inspection DTG |
| Object | Selected ontology object | Selected vehicle record |
| Object Set | Filtered set of objects | All vehicles in a brigade with status RED |

2-5. **PROCEDURE — Create an Application Variable:**
1. Open the application in Workshop edit mode.
2. Navigate to the Variables panel (left sidebar or top menu depending on Workshop version).
3. Select **Add Variable**.
4. Name the variable using the C2DAO naming convention: [domain]_[descriptor]_[type] —
   for example equip_selected_unit_string or ops_date_filter_date.
5. Set the variable type from the dropdown.
6. Set a default value appropriate to the expected initial state of the application.
7. Save the variable. It is now available to all widgets on all pages of the application.

**NOTE:** Variable names must be unique within the application and should be descriptive enough
that another builder can understand the variable's purpose without opening a widget that uses it.

### 2-2b. Connecting Widgets to Variables

2-6. Every interactive widget in Workshop — dropdowns, date pickers, search boxes, object pickers
— can be configured to write its selected value to a variable. Every display widget — tables,
charts, object sets, maps — can be configured to read a variable and apply it as a filter.

2-7. **PROCEDURE — Connect a Dropdown to a Variable (Write):**
1. Select the dropdown widget in edit mode.
2. Open widget **Configuration**.
3. Under **On Selection**, set **Write to Variable** and select the target variable.
4. Define the source of dropdown options: static list, property of an Object Type, or a dataset
   column.
5. Verify that the selected value matches the variable type (string to string, etc.).
6. Save.

2-8. **PROCEDURE — Connect a Table to a Variable (Read/Filter):**
1. Select the table widget in edit mode.
2. Open widget **Configuration**.
3. Under **Filters**, add a new filter condition.
4. Set the filter property (e.g., unit_name), set the operator (equals), and set the value
   source to **Variable**, then select the target variable.
5. Optionally configure behavior when the variable is empty: show all records, show no records,
   or show a default filtered set.
6. Save and test by interacting with the dropdown in preview mode.

**CAUTION:** Configuring a table to show all records when the filter variable is empty can return
extremely large datasets on production Object Types. Set a default value for variables used as
table filters, or configure the table to show no records until a selection is made.

### 2-2c. Variable Chaining

2-9. Variable chaining creates cascading filter behavior — the selection in one widget writes a
variable that filters the options available in a second widget. This is the pattern for
hierarchical navigation (theater to division to brigade to battalion to unit).

2-10. **PROCEDURE — Configure Cascading Dropdowns:**
1. Create two variables: ops_selected_division_string and ops_selected_brigade_string.
2. Configure the first dropdown (Division) to write to ops_selected_division_string.
3. Configure the second dropdown (Brigade) to:
   a. Source its options from the Brigade Object Type.
   b. Apply a pre-filter on the options list using ops_selected_division_string (filter to
      brigades where parent_division equals the variable).
   c. Write the user's brigade selection to ops_selected_brigade_string.
4. Configure downstream tables and charts to filter on ops_selected_brigade_string.
5. Test the complete chain: select a division, verify brigade dropdown updates, select a brigade,
   verify tables filter correctly.

**NOTE:** Always consider what should happen when a parent variable changes. If a user selects
a new division, the brigade variable retains its previous value until the user makes a new
brigade selection. If the previous brigade does not belong to the new division, downstream
widgets will show no results. Add a reset mechanism (a button that clears child variables) or
configure the brigade dropdown to auto-clear when the division variable changes.

## 2-3. Conditional Logic and Visibility

**CONDITIONS:** Existing multi-widget Workshop application; TM-20 qualification.

**STANDARDS:** Builder correctly applies conditional visibility rules so that widgets and panels
display or hide based on application state, without any visible layout breaks in the published
application.

> **NOTE:** Conditional layouts determine which panels or pages operators (TM-10) see based on their role or selected data state. Test your conditional layout logic against the operator workflows in TM-10, Chapter 4. Do not hide information from operators without a security or role-based justification. Refer to TM-10, Task 4-4 (Navigate Between Modules/Pages) and Task 4-3 (Apply Filters to a Dashboard) to validate layout behavior from the operator's perspective.

### 2-3a. Conditional Widget Visibility

2-11. Conditional visibility controls whether a widget is shown or hidden based on the value of
a variable. This allows one application to present different interfaces to different users, or to
reveal detail panels only after a user makes a selection.

2-12. **PROCEDURE — Configure Conditional Visibility:**
1. Select the widget or panel to be conditionally shown/hidden.
2. Open widget **Configuration** then **Visibility**.
3. Select **Conditional**.
4. Define the condition: Variable, Operator, Value. Example: show this panel only when
   ops_selected_unit_string is not empty.
5. Use compound conditions (AND/OR) for more complex logic. Example: show only when
   ops_selected_unit_string is not empty AND ops_view_mode_string equals detail.
6. Save and test in preview mode.

2-13. Common conditional visibility patterns for operational applications:

| Pattern | Implementation |
|---------|----------------|
| Detail panel on selection | Show detail widget when selected-object variable is not empty |
| Role-based view | Show admin controls when user-role variable equals steward |
| Empty state message | Show "Select a unit to view status" when filter variable is empty |
| Progressive disclosure | Show advanced filters when show_advanced_boolean is true |
| Alert banner | Show warning panel when data_staleness_hours variable exceeds threshold |

### 2-3b. Conditional Widget Content

2-14. Beyond visibility, certain widgets support conditional content — displaying different values,
colors, or icons based on data conditions. This is distinct from visibility rules and operates
within the widget itself.

2-15. Conditional formatting in tables: Most table widgets support row-level conditional
formatting. Configure a column to display a colored indicator (red/amber/green) based on a
status field value. This is configured within the column properties, not the variable system.

**PROCEDURE — Configure Traffic Light Status in a Table Column:**
1. Select the table widget.
2. Open **Column Configuration** for the status column.
3. Enable **Conditional Formatting**.
4. Add rules:
   - Value equals NON-MISSION CAPABLE — Red background or red icon
   - Value equals PARTIALLY MISSION CAPABLE — Amber background or amber icon
   - Value equals FULLY MISSION CAPABLE — Green background or green icon
5. Set a fallback format for unexpected values (gray or default).
6. Save and preview.

**NOTE:** Use the Army standard readiness categories (FMC, PMC, NMC) consistently. Do not
invent status labels — align to the authoritative data source definitions.

## 2-4. Multi-Page Application Architecture

**CONDITIONS:** Workshop application with more than one logical section or audience; edit
permissions.

**STANDARDS:** Builder creates a logical page structure with clear navigation, passes variables
across pages correctly, and verifies that the published application loads each page without
error.

### 2-4a. Page Design Principles

> **NOTE:** Decision framework — single-page vs. multi-page: If your application serves a single user role or a single operational workflow, design single-page (TM-20 scope — refer to TM-20, Chapter 5-3, Workshop Interface Overview). If your application serves multiple user roles simultaneously (e.g., G3 operations, G4 logistics, G6 data), or integrates multiple workflows into a unified interface, design multi-page (TM-30 scope). Multi-page application navigation is what operators experience via TM-10, Task 4-4 (Navigate Between Modules/Pages). Test your navigation design against that task.

2-16. Before building a multi-page Workshop application, design the page structure on paper or
a whiteboard. Define:
- What is the primary question each page answers?
- Who uses each page and what action do they take on it?
- What data flows from one page to the next (what variables carry across)?
- What is the navigation pattern (menu, breadcrumb, button-driven drill-down)?

2-17. Standard page patterns for USAREUR-AF operational applications:

| Page Type | Purpose | Common Widgets |
|-----------|---------|----------------|
| Overview | Command summary, fleet or force status at a glance | Metric tiles, status chart, map |
| Drill-Down | Detail for a selected unit, asset, or event | Object detail panel, linked table |
| Filter/Search | User-driven exploration of a large dataset | Search bar, multi-filter panel, results table |
| Admin | Data entry, action execution, record updates | Forms, Action buttons, validation messages |
| Governance | Data quality flags, issue reports, stewardship views | Issue queue table, action buttons |

### 2-4b. Page Navigation Configuration

2-18. **PROCEDURE — Create Multi-Page Navigation:**
1. In the application editor, open **Page Manager** (accessible from top navigation or sidebar).
2. Add pages using **Add Page** — name each page clearly using the pattern
   [Number]_[PageName] (e.g., 01_Overview, 02_UnitDetail, 03_Readiness).
3. Set the landing page (the page users see on first load).
4. Add a **Navigation** widget or a **Button** widget to each page that links to other pages.
5. For sidebar navigation: configure the navigation widget with the list of page names and
   their target pages.
6. For button-driven drill-down: configure each button's **On Click** action to navigate to
   the target page.
7. Test navigation in preview mode: verify all page links resolve, no broken navigation exists.

### 2-4c. Passing Variables Across Pages

2-19. Variables defined at the application level are available on all pages. When a user selects
a unit on the Overview page and navigates to the UnitDetail page, the selection variable retains
its value — the UnitDetail page reads the same variable to display detail for the selected unit.

2-20. **PROCEDURE — Implement Selection-Driven Navigation:**
1. On the Overview page, add an Object Set or Table widget that displays units.
2. Configure the widget's **On Row Click** or **On Object Select** to write the selected object
   to a variable (e.g., ops_selected_unit_object).
3. Add a button or auto-navigate action that transitions to the UnitDetail page on selection.
4. On the UnitDetail page, configure all widgets to filter or resolve using the
   ops_selected_unit_object variable.
5. Add a **Back** button that navigates to the Overview page.
6. Test the complete flow end-to-end.

**NOTE:** When navigating back to the Overview page, the selection variable retains the previous
value unless you explicitly clear it. This is usually desirable — users can see their previous
selection highlighted. If you need a clean state, add a button action that clears the variable
before navigating back.

## 2-5. Complex Widget Configuration

### 2-5a. Tables with Computed Columns

2-21. Workshop table widgets support computed columns — values derived from other columns in the
same row using no-code formula expressions. This removes the need to pre-compute values in the
pipeline and allows builders to surface derived metrics directly in the application.

2-22. **PROCEDURE — Add a Computed Column to a Table:**
1. Open the table widget configuration.
2. Under **Columns**, select **Add Computed Column**.
3. Name the column clearly: days_since_inspection, readiness_pct, shortfall_count.
4. Build the formula using the formula editor. Common operations available:
   - Arithmetic: property_a + property_b, or property_a / property_b * 100
   - Date math: today() - last_inspection_date (returns days as integer)
   - Conditional: if(status == "NMC", 0, 1)
   - String: concat(unit_name, " - ", equipment_type)
5. Set the column data type (number, string, date) to match the formula output.
6. Apply conditional formatting to the computed column if useful (e.g., red when days > 30).
7. Save and verify values are correct against known records.

**CAUTION:** Computed columns in Workshop tables are calculated at display time for the current
page of results. They do not create a permanent dataset. If you need the computed value
available in pipelines, Actions, or other applications, compute it in Pipeline Builder instead
and store the result in a dataset.

### 2-5b. Nested Filters and Dynamic Object Sets

2-23. An Object Set widget displays a collection of ontology objects. At TM-30 level, builders
configure Object Sets with compound filter logic — multiple conditions combined with AND/OR
logic, including variable-driven conditions.

2-24. **PROCEDURE — Configure a Multi-Condition Dynamic Object Set:**
1. Add or select an Object Set widget.
2. Open **Filter Configuration**.
3. Add the first filter condition: property, operator, value (or variable).
4. Select **Add Condition** and choose AND or OR.
5. Add the second condition. Repeat for additional conditions.
6. To use a variable as a filter value: set the value source to **Variable** and select the
   target variable.
7. Configure the **Empty Variable Behavior**: show all, show none, or show a default set.
8. Set the **Sort Order** to control display priority (e.g., sort by readiness_status
   ascending so NMC records appear first).
9. Configure visible properties to show only columns relevant to the current page.
10. Save and test.

### 2-5c. Map Widgets — Advanced Configuration

2-25. Workshop map widgets at TM-30 level support layered display, pop-up detail configuration,
and variable-driven filtering. Operational maps in USAREUR-AF applications commonly display unit
locations, equipment distribution, and event markers.

2-26. Advanced map configuration tasks:
- **Layer management:** Add multiple object sets as separate map layers, each with distinct
  marker styles (icon, color, size) based on object type or property value.
- **Pop-up configuration:** Define what properties appear when a user clicks a map marker —
  include the most operationally relevant fields (unit, status, last update DTG).
- **Variable integration:** Connect map selections to application variables so that clicking
  a map marker selects the object and drives detail panels on the same page.
- **Basemap selection:** Choose the appropriate basemap for the operational context. Avoid
  consumer map services for sensitive operational overlays.

**NOTE:** Map widgets require that Object Types have geometry or coordinate properties
configured in the Ontology. If the Object Type lacks location data, the map widget will not
display objects. Coordinate with the Data Steward to verify location property availability
before designing a map-dependent application.

---

# CHAPTER 3 — ADVANCED PIPELINE BUILDER

**BLUF:** Advanced Pipeline Builder work at TM-30 level involves joining multiple source datasets,
applying complex transformations and aggregations, and producing analysis-ready outputs — all
through the visual pipeline interface without writing code.

## 3-1. Pipeline Builder Review and TM-30 Scope

> **NOTE:** TM-20, Chapter 3 covered single-source ingestion pipelines with basic transformations. TM-30 advances to multi-source joins, complex business logic transforms, error handling that prevents silent failures, and monitoring strategy. Before designing a TM-30 pipeline, confirm the requirement genuinely exceeds TM-20 pipeline capabilities (TM-20, Chapter 3-1). If the requirement can be met with a single-source pipeline and basic transforms, build it at TM-20 level and do not escalate unnecessarily.

3-1. TM-20 covered single-source Pipeline Builder work: reading a dataset, applying column
selection, basic filters, and renaming. TM-30 advances to multi-source operations — joins,
unions, aggregations, and derived columns using Pipeline Builder's visual transform library.

3-2. Pipeline Builder represents each transformation as a visual node connected by data flow
edges. At TM-30 level, pipelines will include multiple input branches that merge, transform,
and flow into one or more outputs. Readability of the pipeline graph is itself a quality
standard — other builders must be able to read your pipeline diagram and understand what it does.

## 3-2. Multi-Source Joins

**CONDITIONS:** Two or more source datasets with a common key field; Pipeline Builder access;
verified knowledge of source dataset schemas.

**STANDARDS:** Builder completes a join correctly, verifies row counts before and after to confirm
join logic, identifies and handles NULL values from unmatched rows, and documents the join key
in the pipeline node description.

### 3-2a. Join Types and When to Use Them

3-3. Pipeline Builder supports the standard join operations. Selecting the wrong join type is
the most common advanced pipeline error.

| Join Type | Returns | Use When |
|-----------|---------|----------|
| Inner Join | Only rows that match in both datasets | You only want records that exist in both sources |
| Left Join | All rows from left dataset; NULLs where no right match | You want all records from the primary dataset, with optional enrichment from secondary |
| Right Join | All rows from right dataset; NULLs where no left match | Same as left, with datasets reversed |
| Full Outer Join | All rows from both datasets; NULLs on both sides where no match | You need a complete picture including unmatched records on either side |

3-4. **USAREUR-AF Example:** Joining a vehicle fleet dataset (left) to a maintenance record
dataset (right). Use a Left Join — you want every vehicle, whether or not it has a maintenance
record. Vehicles with no maintenance record will show NULL in maintenance fields. An Inner Join
would silently drop vehicles with no maintenance history, underreporting fleet size.

### 3-2b. Performing a Join in Pipeline Builder

3-5. **PROCEDURE — Configure a Two-Source Join:**
1. Open Pipeline Builder and create or open a pipeline.
2. Add two **Dataset** input nodes — one for each source. Label each node clearly
   (right-click then rename): src_vehicle_fleet, src_maintenance_records.
3. Add a **Join** transform node from the transform library.
4. Connect the left dataset edge to the Join node's left input port.
5. Connect the right dataset edge to the Join node's right input port.
6. Open the Join node configuration.
7. Select the join type (Inner, Left, Right, or Full Outer).
8. Define the join key: select the matching column from the left dataset and the matching
   column from the right dataset. These must be the same data type (string-to-string,
   integer-to-integer).
9. If joining on multiple keys (composite key), add additional key pairs using **Add Key Pair**.
10. Review the output schema preview — verify expected columns are present.
11. Add a **Row Count** check (using a branch to a Count node) to verify the output row count
    is within expected range before proceeding.

**CAUTION:** Joining on a column that contains NULL values in either dataset will cause those
rows to not match. If the join key may contain NULLs, add a **Filter** node upstream to remove
or handle NULL keys before the join.

**NOTE:** After a join, column names from both datasets are merged into one schema. If both
datasets have a column with the same name (other than the join key), Pipeline Builder will
prefix them. Rename these columns immediately after the join using a **Rename Columns** node
for readability.

### 3-2c. Multi-Source Union

3-6. A Union combines rows from two datasets with the same schema into a single dataset. Use
Union when you have the same type of data from multiple sources (e.g., SITREP records from
multiple subordinate units) and need to combine them into one analysis-ready dataset.

3-7. **PROCEDURE — Configure a Union:**
1. Add two or more **Dataset** input nodes with compatible schemas.
2. Add a **Union** transform node.
3. Connect all input datasets to the Union node.
4. Open Union configuration and verify column mapping — Pipeline Builder will attempt to
   auto-map columns by name. Review the mapping and correct any mismatches.
5. Enable **Deduplicate** if the same record may appear in multiple sources.
6. Preview output and verify row count equals the expected sum of input rows
   (minus duplicates if deduplication is enabled).

## 3-3. Aggregations and Summarization

**CONDITIONS:** Source dataset with repeating rows that need to be summarized; clear definition
of the grouping key and the aggregation metrics required.

**STANDARDS:** Builder configures aggregation grouping and metrics correctly, verifies output
row count is less than input (confirming rollup occurred), and names output columns
descriptively.

### 3-3a. Group By Aggregation

3-8. Aggregation in Pipeline Builder uses a **Group By** transform node. It collapses multiple
rows into a single summary row per unique combination of grouping keys.

3-9. **PROCEDURE — Configure a Group By Aggregation:**
1. Add a **Group By** transform node downstream of your data source or join.
2. Open Group By configuration.
3. Under **Group By Keys**, add the columns that define each unique group. Example:
   unit_name and equipment_type — one output row per unique combination.
4. Under **Aggregations**, add the metrics:
   - COUNT(*) — total records in the group
   - SUM(column) — total value
   - AVG(column) — mean value
   - MAX(column) / MIN(column) — range
   - COUNT_DISTINCT(column) — unique value count
5. Name each aggregated output column clearly: total_vehicles, avg_readiness_pct,
   max_days_overdue.
6. Preview output and verify the number of rows equals the expected number of unique groups.

3-10. **USAREUR-AF Example — Readiness Rollup by Unit:**
Group By keys: battalion_name, equipment_category
Aggregations: COUNT(*) to vehicle_count, SUM(is_fmc) to fmc_count,
AVG(readiness_pct) to avg_readiness_pct
Output: one row per battalion per equipment category showing fleet count and average readiness.

### 3-3b. Calculated Columns (Derived Fields)

3-11. After aggregation, add a **Calculated Column** transform node to derive additional metrics
from aggregated values. This is where you compute ratios, percentages, and composite scores
that are not directly stored in source data.

3-12. **PROCEDURE — Add a Calculated Column:**
1. Add a **Calculated Column** node downstream of the Group By node.
2. Open configuration and select **Add Column**.
3. Name the new column: readiness_rate_pct.
4. Build the formula using the no-code formula editor:
   - Arithmetic: fmc_count / vehicle_count * 100
   - Conditional: if(readiness_rate_pct >= 90, "GREEN", if(readiness_rate_pct >= 70, "AMBER", "RED"))
   - Date math: date_diff(today(), last_inspection_date, "days")
5. Set the output data type.
6. Preview and verify values against known records.

**NOTE:** Calculated columns in Pipeline Builder produce a permanent column in the output
dataset — unlike Workshop computed columns, which are display-only. Use Pipeline Builder
calculated columns when the value will be used in the Ontology, in Actions, or in other
downstream pipelines.

## 3-4. Advanced Transformation Patterns

### 3-4a. Pivot and Unpivot

3-13. Pivot transforms rotate a dataset from long format (one row per category per unit) to wide
format (one row per unit, one column per category). Use Pivot when downstream consumers need
side-by-side comparison across categories.

3-14. **PROCEDURE — Configure a Pivot Transform:**
1. Add a **Pivot** transform node.
2. Set the **Row Key**: the column that identifies each unique row in the output (unit_name).
3. Set the **Pivot Column**: the column whose unique values become new column headers
   (equipment_type).
4. Set the **Value Column**: the column whose values fill the pivoted cells (vehicle_count).
5. Set the **Aggregation**: if multiple rows exist per row key plus pivot column combination,
   how to aggregate them (SUM, AVG, MAX, etc.).
6. Preview output — verify columns match the expected pivot structure.

**CAUTION:** Pivot creates one output column for each unique value in the Pivot Column. If
the Pivot Column has high cardinality (hundreds of unique values), the output will have hundreds
of columns, which degrades performance and readability. Limit pivot operations to low-cardinality
categorical fields (fewer than 20 unique values).

### 3-4b. Handling Null Values

3-15. Production data contains NULL values. Pipelines that do not explicitly handle NULLs
produce outputs with missing data that downstream applications and the Ontology cannot reliably
use. Apply null handling immediately after source input nodes.

3-16. NULL handling patterns:

| Situation | Transform | Configuration |
|-----------|-----------|---------------|
| Drop rows with NULL in a required field | Filter | column IS NOT NULL |
| Replace NULL with a default value | Calculated Column or Coalesce | coalesce(column, "UNKNOWN") |
| Flag records with NULLs for review | Calculated Column | if(column IS NULL, true, false) into a has_missing_data boolean |
| Count NULLs for data quality reporting | Aggregation | COUNT on a flag column |

### 3-4c. Dataset Partitioning Awareness

3-17. Advanced builders do not configure partitioning in the UI — that is a TM-40 code-level
task — but they must understand how partitioning affects their pipelines and must design with
it in mind.

3-18. A partitioned dataset stores data in segments organized by a partition key (typically a
date column). Pipeline Builder reads only the partitions that satisfy your filter conditions —
this is called partition pruning. A pipeline that filters on the partition key reads far less
data than one that scans the full dataset.

3-19. Design guidance for partition-aware pipelines:
- Always apply date filters on partition keys as early as possible in the pipeline (immediately
  after the source node, before any joins).
- Ask the Data Steward or dataset owner whether a source dataset is partitioned and on what key.
- Do not build joins that scan full unpartitioned history when only recent data is needed —
  add an upstream date filter.
- If your pipeline is slow or consumes excessive resources, the most common cause is a missing
  or late-applied partition filter.

## 3-5. Pipeline Naming and Documentation Standards

> **NOTE:** When a TM-30 pipeline fails, the downstream impact is broad. Operators (TM-10, Task 5-1, View and Read a Dataset) see stale or missing data. Workshop applications fed by the pipeline display errors. Complex data products may serve dozens of operators or downstream pipelines. Refer to TM-10, Chapter 8-1 (Common Problems and Solutions) to understand the operator experience of a pipeline failure, then design your monitoring and alerting to detect failures before operators report them.

3-20. Every pipeline produced at TM-30 level must conform to C2DAO naming and documentation
standards. A pipeline that cannot be identified, understood, or maintained by another builder
is a governance deficiency.

3-21. **Pipeline naming convention:**
[domain]_[source-description]_[output-description]_[version]
Example: log_vehicle-fleet-maintenance-join_readiness-rollup_v1

3-22. **Required pipeline documentation:**
- **Pipeline Description:** What does this pipeline produce? What question does it answer?
- **Source Datasets:** List all input datasets with dataset names and owners.
- **Output Dataset:** Name, intended consumer (Workshop app, Ontology Object Type, Contour view).
- **Join Keys:** Document all join keys and join types with rationale.
- **Refresh Cadence:** How often should this pipeline run? On schedule or on-demand?
- **Data Steward:** Who is responsible for this pipeline?

3-23. Add this documentation in the Pipeline Builder description field and maintain it in the
C2DAO pipeline registry if one is maintained for your domain.

---

# CHAPTER 4 — ONTOLOGY DESIGN THROUGH THE UI

**BLUF:** Advanced builders design Object Types, Link Types, and Actions through the Ontology
Manager UI — making deliberate design decisions that affect all downstream applications,
analytics, and workflows that consume the Ontology. Good design prevents downstream pain;
poor design forces expensive rework.

## 4-1. Ontology as Operational Data Model

4-1. The Ontology is the shared data model of the platform. It defines what things exist in your
operational environment (Object Types), how they relate to each other (Link Types), and what
users can do to them (Actions). Every Workshop application, Quiver analysis, Contour chart,
and AIP Logic workflow that touches operational data does so through the Ontology.

4-2. Ontology design decisions are not easily reversed. Changing a property name, deleting a
Link Type, or restructuring an Object Type after other teams have built applications against it
causes those applications to break. Design carefully. Review with Data Stewards before publishing.

4-3. TM-30 scope: This chapter covers designing Object Types, Link Types, and Actions through
the Ontology Manager graphical interface. Writing TypeScript Functions on Objects (FOO) or
code-level ontology configuration is TM-40 scope.

> **NOTE:** TM-20 Ontology configuration (TM-20, Chapter 4) is limited to: (1) simple Object Types with straightforward properties; (2) one-to-one and one-to-many Link Types without junction complexity; (3) single-step Actions with direct form-to-field mapping. If a design requires multi-step Actions, conditional routing, derived properties with complex logic, or many-to-many Link Types beyond a simple junction, it is TM-30 scope. When assessing complexity, use TM-20, Chapter 4-2 (Ontology Manager Interface Overview) as the boundary reference.

## 4-2. Object Type Design

**CONDITIONS:** Identified operational entity to model; understanding of source data schema;
coordination with Data Steward on naming and property standards.

**STANDARDS:** Builder creates an Object Type with a correctly defined primary key, well-named
properties with correct data types, appropriate visibility settings, and documentation in the
description field. Object Type passes Data Steward review before publication to production.

### 4-2a. Object Type Design Principles

4-4. An Object Type represents a real operational entity — a vehicle, a unit, a maintenance
event, a personnel record, a facility, an equipment line item. Before creating an Object Type,
answer these questions:

1. **What is the primary key?** Every object instance must be uniquely identifiable. What field
   guarantees uniqueness? (UIC for units, NSN plus serial for equipment, DODAAC plus document
   number for transactions.)
2. **What properties describe this entity?** List the fields that will be stored on each object
   instance. Resist the urge to include everything — include what is operationally meaningful
   and what downstream consumers will actually use.
3. **What does this entity link to?** What other Object Types does it relate to? (A vehicle
   links to its unit; a maintenance event links to the vehicle it services.)
4. **Who owns this data?** Who is the Data Steward? Who authorizes changes?
5. **What is the source dataset?** What Pipeline Builder output backs this Object Type?

### 4-2b. Creating an Object Type

4-5. **PROCEDURE — Create an Object Type in Ontology Manager:**
1. Navigate to Ontology Manager in the platform.
2. Select **Create Object Type**.
3. Set the Object Type **Name**: use PascalCase, singular noun.
   C2DAO convention: [Domain][EntityName] — example: LogVehicle, OpsUnit, MedFacility.
4. Set the **API Name** (auto-generated from name — verify it follows convention).
5. Set the **Description**: one to three sentences describing the entity, its source, and its
   operational purpose.
6. Set the **Primary Key Property**: select the property that uniquely identifies each object.
   This is typically the UIC, serial number, equipment ID, or document number.
7. Add **Properties** for each attribute:
   - Name: camelCase, descriptive (unitName, equipmentStatus, lastInspectionDate)
   - Data type: String, Integer, Double, Boolean, Timestamp, Date — match the source data type
   - Mark required properties as required
   - Add a description to each property that is not self-evident
8. Set **Visibility**: who can see this Object Type? Apply the least-permissive setting that
   meets operational requirements.
9. Review configuration. Request Data Steward review before publishing.

**NOTE:** Do not create an Object Type for every dataset you have. Object Types are for entities
that need to be tracked, searched, acted upon, or related to other entities over time. Reference
data and lookup tables that are only consumed within pipelines do not need Object Types.

### 4-2c. Property Design Standards

> **NOTE:** When designing properties for an Object Type, consider how operators (TM-10) will understand and use them. Refer to TM-10, Task 5-3 (Use Quiver to Explore Ontology Objects) and Task 4-3 (Apply Filters to a Dashboard) to see how operators interact with your property names and values. Use clear operational terminology. Avoid technical abbreviations operators will not recognize in their daily workflow.

4-6. Properties are the most frequently misdesigned element of Object Types. Common errors:

| Error | Impact | Correct Practice |
|-------|--------|-----------------|
| Using String for a numeric value | Cannot sort numerically, cannot aggregate | Use Integer or Double for numeric fields |
| Using String for a date | Cannot perform date math, cannot filter by range | Use Date or Timestamp |
| Over-generic property names | Other builders cannot use the Object Type without documentation | Use descriptive names matching operational terminology |
| Including PII without authorization | Data governance violation | Coordinate with Data Steward and legal before including PII |
| Omitting description on non-obvious properties | Downstream builders don't know what the field means | Add a description to every property where the name alone is insufficient |

4-7. Status properties deserve particular attention. If a status field has a defined set of valid
values (FMC, PMC, NMC; GREEN, AMBER, RED; ACTIVE, INACTIVE), document those values in the
property description. This enables downstream builders to configure accurate Workshop filters
and Contour charts.

## 4-3. Link Type Design

**CONDITIONS:** Two existing Object Types with a defined operational relationship; coordination
with Data Steward.

**STANDARDS:** Builder creates a Link Type with the correct directionality, cardinality, and
naming. Link Type is documented and passes Data Steward review.

### 4-3a. Link Type Concepts

4-8. A Link Type defines the relationship between two Object Types. Links are what enable
Quiver's multi-object analysis, Workshop drill-down navigation, and AIP Logic contextual
reasoning across related objects.

4-9. Link Type design decisions:

| Decision | Options | Guidance |
|----------|---------|---------|
| Directionality | One-directional or bi-directional | Most operational links are bi-directional (a vehicle belongs to a unit; the unit has vehicles) |
| Cardinality | One-to-one, one-to-many, many-to-many | Reflect the actual operational reality — a vehicle has one primary unit; a unit has many vehicles |
| Link name | Should read naturally in both directions | LogVehicle to OpsUnit: forward = "assigned to", reverse = "has assigned" |

### 4-3b. Creating a Link Type

4-10. **PROCEDURE — Create a Link Type:**
1. In Ontology Manager, navigate to **Link Types** and select **Create Link Type**.
2. Set the **Name**: use descriptive language that reflects the relationship.
   Convention: [ObjectTypeA]_[RelationshipVerb]_[ObjectTypeB]
   Example: LogVehicle_assignedTo_OpsUnit
3. Set the **Source Object Type** (the "from" side of the relationship).
4. Set the **Target Object Type** (the "to" side of the relationship).
5. Set cardinality: select one-to-one, one-to-many, or many-to-many.
6. Set **Link Labels**: the label used to describe the relationship in each direction.
   Source to Target: "is assigned to"; Target to Source: "has assigned vehicle"
7. Define the **Link Key**: the shared property that connects the two object types
   (e.g., unit_uic present on both LogVehicle and OpsUnit).
8. Add a description explaining the operational meaning of this link.
9. Submit for Data Steward review before publishing.

**WARNING:** Creating a Link Type on the wrong property pair creates incorrect relationships
that appear valid in the UI but produce misleading results in Quiver, Workshop, and AIP Logic.
Verify the link key produces the expected relationships by previewing a sample of linked objects
before publishing.

## 4-4. Action Design

> **NOTE:** Distinguish TM-20 Actions from TM-30 Actions: TM-20 Actions (TM-20, Chapter 4-2) are single-step — operator fills form, field is updated. TM-30 Actions support multi-step workflows, conditional routing, and approval chains. If an Action requires: (1) sequential submission steps; (2) conditional field visibility; (3) multi-record writes; (4) command authority approval — it is TM-30 scope, covered in Chapter 5 of this manual.

**CONDITIONS:** Identified workflow where users need to create, update, or delete ontology object
data through the platform UI; Data Steward authorization to create write-back capability.

**STANDARDS:** Builder creates an Action with correct parameter definitions, appropriate
validation rules, clear user-facing labels, and appropriate authorization controls. Action is
tested end-to-end in a non-production environment before promotion.

### 4-4a. What Actions Do

> **NOTE:** TM-20 Actions (TM-20, Chapter 4-2) are single-step: operator fills a form, clicks Submit, one Object property is updated. TM-30 expands this to multi-step submission processes, conditional routing between paths, and approval chains requiring authority sign-off. If a workflow can be expressed as a single form-to-field write, do not design it at TM-30 level — hand it back to a TM-20 builder. Reserve TM-30 Action design for workflows that genuinely require the additional complexity.

4-11. Actions are the write-back mechanism of the Ontology. They allow authorized users to
create new object instances, update properties on existing objects, or delete objects — directly
from Workshop applications or Quiver views. Actions execute against the Ontology directly; they
do not require a pipeline run.

4-12. Common USAREUR-AF Action use cases:
- S4 NCO updates equipment status from NMC to PMC after partial repair
- G2 analyst flags an intelligence report as reviewed and adds a confidence rating
- Unit administrator creates a new equipment record when a vehicle arrives in theater
- Data Steward marks a data quality issue as resolved
- Operations officer logs a significant activity event with location and description

### 4-4b. Creating an Action

4-13. **PROCEDURE — Create an Action in Ontology Manager:**
1. Navigate to **Actions** in Ontology Manager and select **Create Action**.
2. Set the **Action Name**: use an imperative verb phrase that describes what the action does
   from the user's perspective. Example: Update Equipment Status, Log Maintenance Event,
   Flag Data Quality Issue.
3. Set the **Action Type**: Create Object, Modify Object, Delete Object, or Batch Modify.
4. Select the **Target Object Type**.
5. Define **Parameters** — the fields the user will fill in when executing the action:
   - Parameter name (label shown to the user)
   - Data type (String, Integer, Boolean, Date, Object reference)
   - Required or optional
   - Default value if applicable
   - Validation rules (see 4-4c)
6. Map parameters to **Object Properties**: which parameter value writes to which property
   on the object.
7. Set **Authorization**: who can execute this action? Apply least-privilege — limit to the
   role that genuinely needs write access.
8. Set the **Confirmation Message**: what does the user see before the action executes?
   Make it specific enough that the user understands what will change.
9. Set the **Success Message**: what does the user see after the action executes?
10. Test the action in a non-production environment. Verify parameter mapping is correct.
    Verify authorization allows the intended users and blocks unauthorized users.

### 4-4c. Action Validation Rules

4-14. Validation rules prevent bad data from entering the Ontology through Actions. Every Action
parameter that accepts user input should have at least one validation rule.

4-15. Validation types available in Action configuration:

| Validation Type | Use Case | Example |
|-----------------|----------|---------|
| Required field | Prevent empty submissions | Status update requires a status value |
| Allowed values list | Limit input to valid options | Status must be FMC, PMC, or NMC |
| Minimum / Maximum | Numeric range enforcement | Readiness percentage must be 0-100 |
| Date range | Prevent impossible dates | Event date cannot be in the future |
| Length limit | String field size control | Notes field maximum 500 characters |
| Pattern match | Format enforcement | UIC must match the defined UIC format |

4-16. Configure validation rules in the parameter definition within Action configuration.
Add a clear, user-facing validation error message for each rule so users understand what
correction is needed.

**NOTE:** Validation rules in Actions are the last line of defense before data enters the
Ontology. Treat them as critically as input validation at any other system boundary. A missing
validation rule is a data quality risk that will require remediation after the fact.

---

# CHAPTER 5 — ADVANCED ANALYTICS: CONTOUR AND QUIVER

**BLUF:** Advanced analytics at TM-30 level moves beyond basic charts into complex aggregations,
cross-object analysis, and saved analytical views that become persistent operational intelligence
products.

## 5-1. Advanced Contour

> **NOTE:** Contour at TM-20 level (TM-20, Chapter 6) supports basic filtering, sorting, and simple aggregations. Operators use Contour via TM-10, Task 5-2 (Use Contour for No-Code Analysis). TM-30 Contour adds the formula editor for calculated columns, complex multi-table aggregations, and pivot analysis. Before designing at TM-30 level, confirm the analysis requirement exceeds TM-20 Contour capabilities (TM-20, Chapter 6-2). If TM-20 Contour can handle the requirement, build there first.

**CONDITIONS:** Published dataset or Object Type with sufficient data for analysis; Contour access.

**STANDARDS:** Builder produces analysis with correct aggregations, meaningful calculated columns,
saved views configured for reuse, and shared appropriately with the intended audience.

### 5-1a. Complex Aggregations in Contour

5-1. Contour's aggregation capabilities extend beyond simple counts and sums. At TM-30 level,
builders use multi-level grouping, conditional aggregation, and window functions to produce
sophisticated analytical outputs.

5-2. **PROCEDURE — Multi-Level Group By in Contour:**
1. Open Contour and select your dataset or Object Type.
2. In the analysis pane, add a **Group By** operation.
3. Add the primary grouping key (e.g., division_name).
4. Add a secondary grouping key (e.g., equipment_category).
5. Add aggregation metrics: COUNT, SUM, AVG, MAX, MIN.
6. Run the analysis and verify output structure.
7. Add additional **Calculated Column** operations to derive ratios or composite metrics
   from the aggregated values.

5-3. Conditional aggregation — counting or summing only rows that meet a condition — is
achieved in Contour by combining a calculated column with an aggregation:
1. Add a **Calculated Column**: is_nmc = if(status == "NMC", 1, 0).
2. Add an **Aggregation**: SUM(is_nmc) to produce nmc_count.
3. Add another **Calculated Column**: nmc_rate = nmc_count / total_count * 100.

### 5-1b. Pivot Tables in Contour

5-4. Contour supports pivot analysis natively — rotating a grouped dataset into a cross-tabular
format for side-by-side comparison.

5-5. **PROCEDURE — Create a Pivot in Contour:**
1. Add a **Pivot** transform in the analysis pane.
2. Set the **Row Keys** (left-side group): battalion_name.
3. Set the **Pivot Column** (column headers): equipment_category.
4. Set the **Value**: the metric to display in cells (readiness_rate_pct).
5. Set the **Aggregation**: how to combine multiple values per cell (AVG, SUM, etc.).
6. Run and verify the pivot structure matches the expected layout.
7. Add a **Total** row or column if the analysis requires summary margins.

### 5-1c. Calculated Columns in Contour

5-6. Contour calculated columns are ephemeral — they exist in the analysis session and saved
views, but do not persist in the underlying dataset. This makes Contour ideal for exploratory
analysis and reporting without modifying source data.

5-7. Formula capabilities in Contour calculated columns mirror Pipeline Builder's formula
editor. Apply the same discipline: name columns descriptively, verify output values against
known records, and add a comment in the view description explaining non-obvious formulas.

### 5-1d. Saved Views and Operational Analysis Products

5-8. A Contour saved view is a persistent, shareable snapshot of a configured analysis —
including all filter settings, groupings, calculated columns, and chart configurations. Saved
views are the mechanism for creating repeatable analytical products.

5-9. **PROCEDURE — Create and Share a Saved View:**
1. Configure the analysis in Contour: filters, groupings, calculated columns, chart type.
2. Select **Save View** (or **Save As** for a new view from an existing one).
3. Name the view using the C2DAO naming convention:
   [domain]_[product-name]_[frequency-or-audience]
   Example: log_readiness-by-unit_weekly, ops_sitrep-trend_monthly.
4. Add a description: what is this analysis? Who uses it? What question does it answer?
5. Set sharing: share with specific users, groups, or make available to all authorized users.
6. Add to the relevant Workshop application if this analysis is an embedded product.

5-10. For recurring reporting products (weekly readiness summary, monthly SITREP trend),
configure Contour views to use dynamic date filters — "last 7 days," "current month" — so
the view always reflects the current period without manual reconfiguration.

### 5-1e. Chart Types and When to Use Them

| Chart Type | Best For | Avoid When |
|------------|----------|------------|
| Bar chart | Comparing values across categories | More than approximately 15 categories |
| Line chart | Trends over time | Non-time-series data |
| Scatter plot | Correlation between two numeric values | Categorical data |
| Heat map | Intensity across two categorical dimensions | Fewer than 5 categories per axis |
| Pie/donut | Part-to-whole relationships | More than 6 slices |
| Table | Precise values, multiple metrics per row | Data is better communicated visually |
| Map | Geographic distribution | Data has no meaningful geographic component |

## 5-2. Advanced Quiver

**CONDITIONS:** Published Ontology with defined Object Types and Link Types; Quiver access.

**STANDARDS:** Builder creates multi-object analyses, configures linked views, defines custom
object sets, and produces shareable analytical modules that link correctly across object types.

### 5-2a. Object Set Analysis

5-11. Quiver's fundamental unit is the object set — a filtered collection of objects from an
Object Type. At TM-30 level, builders create precise, reusable object sets using compound
filter logic and saved configurations.

5-12. **PROCEDURE — Create a Compound Filter Object Set:**
1. Open Quiver and select an Object Type.
2. In the filter panel, add the first filter condition.
3. Add additional conditions using AND/OR operators.
4. Use property-level filters: equals, not equals, greater than, less than, contains, is NULL.
5. Use object relationship filters — filter based on properties of a linked Object Type.
6. Name and save the object set for reuse.

5-13. Saved object sets in Quiver can be embedded in Workshop applications as the data source
for Object Set widgets. This creates a single definition of a critical operational set (e.g.,
"All NMC vehicles in 21st TSC") that is used consistently across multiple applications.

### 5-2b. Multi-Object Dashboards

5-14. Quiver supports dashboard layouts that display analysis across multiple Object Types
simultaneously, with views linked so that selecting an object in one view filters the display
in related views.

5-15. **PROCEDURE — Build a Multi-Object Quiver Dashboard:**
1. Open a new Quiver dashboard or layout.
2. Add an **Object Set View** for the primary Object Type (e.g., Units).
3. Add a second **Object Set View** for a related Object Type (e.g., Vehicles assigned to units).
4. Configure **Linked Views**: in the Vehicle view, set the filter source to the Unit view's
   selection — when a user selects a unit in the Unit view, the Vehicle view automatically
   filters to that unit's vehicles.
5. Add metrics and charts to each view as needed.
6. Add a **Summary Panel** at the top showing aggregate counts across both object types.
7. Save and share the dashboard.

### 5-2c. Custom Metrics in Quiver

5-16. Quiver supports custom metrics at the Object Type level — calculated values that appear
as additional columns in object tables and can be used in filters and sorting. These are distinct
from Workshop computed columns and Contour calculated columns.

5-17. Custom metrics are configured in Quiver's metric builder and may reference:
- Properties of the current Object Type (arithmetic, conditional logic)
- Properties of linked Object Types (aggregate metrics across links — e.g., count of linked
  NMC vehicles per unit)

5-18. **PROCEDURE — Create a Custom Metric in Quiver:**
1. In the Object Type's Quiver configuration, select **Add Custom Metric**.
2. Name the metric clearly: nmc_vehicle_count, avg_readiness_pct.
3. Define the formula using the metric builder:
   - For a simple calculated value: use arithmetic on existing properties.
   - For an aggregation over linked objects: select the Link Type, the target Object Type,
     and the aggregation (COUNT, SUM, AVG) on a target property.
4. Set the display format: number, percentage, date.
5. Preview the metric on sample objects.
6. Save. The metric is now available in all Quiver analyses on this Object Type.

---

# CHAPTER 6 — AIP LOGIC CONFIGURATION

**BLUF:** At TM-30 level, builders configure and manage AIP Logic workflows and their operational
parameters through the UI — activating, tuning, and monitoring AI-assisted processes without
authoring underlying model logic.

## 6-1. AIP Logic Overview

> **NOTE:** AIP Logic is TM-30 only. TM-20 builders do not configure AI workflows. TM-10 operators use AIP Logic workflows that TM-30 builders design — see TM-10, Task 6-1 (Use an AIP Logic Workflow) and Task 6-2 (Interact with an AIP Agent) for the operator's perspective. Operators must review and validate AI outputs before acting on them (emphasized in TM-10, Chapter 6). Design your AIP Logic workflows so outputs are easy for operators to validate quickly. Workflows that produce outputs requiring extensive operator review are operationally inefficient.

6-1. AIP Logic is the AI workflow layer of the platform. It enables AI-assisted analysis,
automated reasoning, and natural language interfaces to operational data. At TM-30 level,
builders do not author AIP Logic workflows — that is TM-40 scope. TM-30 builders:
- Configure the operational parameters of existing AIP Logic workflows
- Connect workflows to appropriate data sources and Object Types
- Activate and deactivate workflows in production
- Monitor workflow health and output quality
- Report configuration issues to TM-40-level developers

6-2. **CAUTION:** AIP Logic workflows that consume operational data can produce outputs that
appear authoritative. Before activating an AIP Logic workflow in production:
- Verify the workflow has been reviewed and approved by the responsible Data Steward
- Verify users will see clear labeling indicating outputs are AI-generated
- Confirm the command authority understands the scope and limitations of AI-assisted analysis
- Ensure the workflow has a human-in-the-loop review step for any decision-relevant output

## 6-2. Configuring AIP Logic Workflows

**CONDITIONS:** Existing AIP Logic workflow created by a TM-40 developer; appropriate
configuration access granted by Data Steward.

**STANDARDS:** Builder correctly configures workflow parameters, connects data sources, tests
with representative sample data, and documents the configuration for future reference.

### 6-2a. Workflow Parameter Configuration

6-3. **PROCEDURE — Configure an AIP Logic Workflow:**
1. Navigate to AIP Logic in the platform.
2. Open the target workflow. Verify you have configuration access (not just view access).
3. Review the workflow's purpose and expected behavior as documented by the TM-40 developer.
4. Under **Configuration**, review each configurable parameter:
   - Data source connections (which Object Types or datasets the workflow reads)
   - Output target (where the workflow writes its results)
   - Prompt configuration (if the workflow uses configurable natural language prompts —
     these can be adjusted for operational context without writing code)
   - Scheduling: on-demand, triggered by data change, or scheduled interval
   - Confidence threshold: the minimum confidence score before an output is surfaced to users
5. Make parameter changes according to the documented operational requirements.
6. Save the configuration.

### 6-2b. Connecting Workflows to Data Sources

6-4. AIP Logic workflows read from Ontology Object Types, datasets, or prior workflow outputs.
Advanced builders configure these connections through the workflow's data source panel.

6-5. **PROCEDURE — Update a Workflow Data Source Connection:**
1. In the workflow configuration, navigate to **Data Sources**.
2. Review existing connections — verify each connection points to the correct Object Type or
   dataset.
3. To update a connection: select the connection, choose the replacement Object Type or dataset,
   verify the field mapping (workflow input fields mapped to data source properties).
4. If the replacement data source has a different schema than the previous source, the field
   mapping will need to be reconfigured. Do not deploy a workflow with unmapped required fields.
5. Save and test with a sample data query before activating in production.

### 6-2c. Workflow Monitoring

6-6. Active AIP Logic workflows require monitoring. Advanced builders are responsible for
first-line monitoring of workflows they have configured.

6-7. Monitoring tasks:

| Task | Frequency | Action on Issue |
|------|-----------|-----------------|
| Review workflow execution logs | Weekly | Identify errors or failed executions |
| Spot-check AI output quality | Bi-weekly | Compare AI outputs to known-correct answers on sample records |
| Verify data source freshness | Weekly | Confirm source data is updating on schedule |
| Review user feedback flags | As received | Investigate flagged outputs, report to TM-40 developer |
| Check confidence score distribution | Monthly | Significant shift may indicate data drift |

6-8. If monitoring reveals a workflow producing systematically incorrect outputs, deactivate
it immediately and escalate to the TM-40 developer and Data Steward. Do not leave an incorrect
AI workflow active in production while investigating — it will continue to surface bad outputs
to users.

## 6-3. Natural Language Query Configuration

> **NOTE:** Operators (TM-10, Task 6-2, Interact with an AIP Agent) validate AI outputs against source data before acting. When engineering prompts, design with that human-review requirement in mind. Prompts should produce outputs that operators can quickly verify. Refer to TM-10, Task 6-2 for the validation workflow operators follow — then design your prompts to produce outputs compatible with that workflow.

6-9. Some AIP Logic deployments include a natural language query interface — a chat or Q&A
widget in Workshop that allows users to ask questions about operational data in plain English.
Advanced builders configure these interfaces and manage the scope of data they can access.

6-10. **PROCEDURE — Configure a Natural Language Query Scope:**
1. Navigate to the AIP Logic query interface configuration.
2. Under **Data Scope**, define which Object Types and datasets the interface can query.
   Apply least-privilege — only include data the intended users are authorized to access.
3. Under **Prompt Guidance**, configure any operational context that helps the AI produce
   relevant responses. Example: adding a glossary of command-specific terminology, unit
   abbreviations, or equipment codes.
4. Configure **Output Format**: what format should responses take? Tabular, narrative,
   a combination?
5. Enable **Source Citation**: configure the interface to cite the specific records it used
   to produce each answer, enabling user verification.
6. Test with representative operational questions. Verify the responses are accurate,
   appropriately scoped, and clearly labeled as AI-generated.

---

# CHAPTER 7 — DATA GOVERNANCE AND LINEAGE

**BLUF:** Advanced builders are frontline data governance actors — they read and understand
lineage graphs, identify and report data quality issues, work with Data Stewards on resolution,
and enforce governance standards in everything they build.

> **NOTE:** TM-20 builders follow governance standards defined in TM-20, Chapter 8 (Builder Standards and Governance). TM-30 builders have additional stewardship responsibilities because your designs affect shared infrastructure and downstream systems. At TM-30 level you are responsible for: (1) understanding operator access expectations (TM-10, Chapter 7, Security, Classification, and Markings); (2) ensuring TM-20 builders can implement your designs without overstepping their scope; (3) coordinating with data stewards before modifying any shared production resource; (4) designing for the full downstream impact across all consumers, not only the immediate use case.

## 7-1. Data Lineage

**CONDITIONS:** Access to the Lineage view for a dataset, Object Type, or pipeline;
understanding of the upstream data sources that feed the product.

**STANDARDS:** Builder correctly interprets a lineage graph, identifies all upstream
dependencies, traces a quality issue to its source, and documents findings clearly for
Data Steward review.

### 7-1a. Reading the Lineage Graph

7-1. The lineage graph is a directed graph showing data flow from source to output. Every
dataset, pipeline, and Object Type on the platform has a lineage view. Advanced builders read
lineage graphs to:
- Understand where a dataset's data comes from
- Identify the impact of a source change on downstream products
- Trace the origin of a data quality issue
- Verify that an output is derived from authoritative sources

7-2. Lineage graph elements:

| Element | Shape/Color | Meaning |
|---------|-------------|---------|
| Source dataset | Rectangle, source icon | Raw or ingested data — where data enters the platform |
| Pipeline | Arrow with transform icon | A Pipeline Builder or code transform that produced an output |
| Output dataset | Rectangle | A derived dataset produced by a pipeline |
| Object Type | Object icon | An Ontology Object Type backed by a dataset |
| External source | Cloud icon | Data from outside the platform (file upload, external feed) |
| Edge (arrow) | Directional arrow | Data flows from source to target |

7-3. **PROCEDURE — Read a Lineage Graph for an Output Dataset:**
1. Navigate to the target dataset or Object Type.
2. Open the **Lineage** tab or view.
3. Identify the immediate upstream inputs (what datasets or transforms produced this one).
4. Follow each branch upstream to the source — find the original ingestion points.
5. Note the names and owners of all upstream datasets.
6. Identify any external sources — these are data outside the platform and may have different
   quality, freshness, and reliability characteristics.
7. Document your findings: "This Object Type is produced by pipeline X, which joins dataset A
   (owned by S4) and dataset B (owned by G4 logistics). Dataset A originates from the PBUSE
   feed ingested daily at 0600Z."

### 7-1b. Impact Assessment Before Making Changes

7-4. Before modifying any shared resource — a dataset schema, an Object Type property, a
pipeline output format — perform a downstream impact assessment using the lineage graph.

7-5. **PROCEDURE — Downstream Impact Assessment:**
1. Open the lineage graph for the resource you plan to modify.
2. Switch to **Downstream** view — this shows all resources that depend on this one.
3. List all downstream datasets, Object Types, Workshop applications, Contour views, and
   Quiver analyses.
4. For each downstream resource, identify the owner and notify them of the planned change.
5. Assess whether the change is breaking (schema change, property rename, type change) or
   non-breaking (new column added, description updated).
6. For breaking changes: coordinate a maintenance window, get Data Steward approval, and
   notify all downstream owners before executing.
7. For non-breaking changes: notify downstream owners as a courtesy and document the change.

**WARNING:** Renaming a property on an Object Type is a breaking change for every Workshop
application, Contour view, Quiver analysis, and AIP Logic workflow that references that
property by name. Never rename a production property without a full downstream assessment and
coordinated cutover plan.

## 7-2. Data Quality Workflows

> **NOTE:** Operators (TM-10, Chapter 5, Working with Data) expect data to be current, accurate, and correctly marked. Use TM-10, Task 5-4 (Verify Data Currency and Source) as the benchmark for what operators require from your data products. If your pipeline or Ontology design creates data quality issues that operators cannot resolve themselves (TM-10, Chapter 5-2, What to Do When Data Looks Wrong), you are responsible for identifying and fixing the root cause.

**CONDITIONS:** Identified data quality issue in a dataset or Object Type; Data Steward contact.

**STANDARDS:** Builder correctly identifies and documents a data quality issue, reports it
through the appropriate channel, and follows up until resolution is confirmed.

### 7-2a. Identifying Data Quality Issues

7-6. Advanced builders encounter data quality issues during pipeline development, analysis, and
application testing. Common issue types:

| Issue Type | Example | Severity |
|------------|---------|----------|
| Missing data | Key field is NULL on 30% of records | High — analysis results are incomplete |
| Duplicate records | Same vehicle appears twice with different status | High — counts and aggregations are incorrect |
| Stale data | Fleet dataset last updated 5 days ago; should update daily | Medium — analysis is out of date |
| Invalid values | Status field contains "n/a" when valid values are FMC/PMC/NMC | Medium — filters and charts break |
| Schema mismatch | Column renamed in upstream source, pipeline now fails | High — output not updating |
| Referential integrity | Vehicle records reference unit UICs that don't exist in the unit dataset | Medium — joins produce NULLs |

### 7-2b. Reporting Data Quality Issues

7-7. **PROCEDURE — Report a Data Quality Issue:**
1. Document the issue with specificity:
   - What is the affected dataset or Object Type (full name)?
   - What is the issue? Be specific: "15% of records in the LogVehicle Object Type have NULL
     values in the assigned_unit_uic property as of 11 March 2026."
   - What is the operational impact? "This causes Quiver unit-to-vehicle link analysis to
     omit approximately 200 vehicles from unit rollups."
   - What is the likely source? Trace upstream using the lineage graph.
   - When was the issue first observed?
2. Identify the responsible Data Steward from the C2DAO registry.
3. Submit the issue report through the approved governance channel (data quality issue tracker,
   C2DAO issue log, or direct coordination with Data Steward per local SOP).
4. Retain a copy of the report with timestamp.
5. Do not attempt to fix a data quality issue in another team's dataset without explicit
   authorization from the Data Steward — you may be working with a copy or a view, not the
   authoritative source.

### 7-2c. Data Steward Coordination

7-8. Data Stewards are the designated authority for data quality, access control, naming
compliance, and governance within their data domain. Advanced builders work with Data Stewards
on a routine basis.

7-9. Routine Data Steward interactions for advanced builders:
- **Before creating a new Object Type or dataset:** confirm naming convention, verify the
  entity is not already modeled elsewhere
- **Before modifying a shared resource:** notify and get approval
- **When reporting a quality issue:** submit through the Data Steward's designated channel
- **Before publishing a production application:** request governance review
- **When assigning access:** confirm the access level is appropriate and approved

7-10. If you cannot identify the Data Steward for a dataset or Object Type, escalate to the
C2DAO authority for your domain. Do not proceed with modifications to unowned data without
coordination.

## 7-3. Access Control Management

> **NOTE:** Before designing coalition-facing data products at TM-30 level, understand TM-10, Chapter 7 (Security, Classification, and Markings), especially Task 7-1 (Verify Markings and Access Level). Coalition data must be correctly marked and access-controlled from ingestion through final product. Errors in releasability markings can result in data shared with unauthorized coalition partners — this is a hard governance gate, not a best practice. Coordinate with the USAREUR-AF C2DAO before any coalition-facing design decision.

**CONDITIONS:** Workshop application, dataset, or Object Type requiring access configuration;
appropriate administrative rights.

**STANDARDS:** Builder configures access using least-privilege principle, documents the access
rationale, and verifies the configuration grants access to intended users and denies access to
all others before publishing.

### 7-3a. Access Control Principles

7-11. Access control on the platform operates at multiple levels:
- **Dataset level:** who can read or write the underlying dataset
- **Object Type level:** who can view objects, who can execute Actions
- **Application level:** who can view the Workshop application, who can edit it
- **Analysis level:** who can view a Contour or Quiver saved view

7-12. The three access control questions to answer for every resource you publish:
1. **Who needs to see this?** Configure view access for those users or groups only.
2. **Who needs to edit this?** Configure edit access for those users or groups only —
   typically just you and your Data Steward at initial publication.
3. **Who should never see this?** Verify that access is not inherited from a broader group
   that includes unauthorized personnel.

### 7-3b. Configuring Access in the UI

7-13. **PROCEDURE — Set Access Controls on a Workshop Application:**
1. Open the application in edit mode.
2. Navigate to **Sharing and Permissions** (application settings).
3. Remove any default "all users" access if the application contains controlled data.
4. Add specific users or groups with the appropriate role:
   - **Viewer:** can interact with the published application, cannot edit
   - **Editor:** can modify the application in edit mode
   - **Owner:** full administrative control
5. If the application references Object Types or datasets with restricted access, verify
   that the access controls on those underlying resources match the application's access.
   Granting application view access does not grant underlying data access — both must be
   configured.
6. Document the access configuration in the application description: "Authorized for
   USAREUR-AF G4 staff (viewer), G4 data team (editor)."
7. Test access by verifying a member of each access group can interact as expected.

---

# CHAPTER 8 — ENVIRONMENT MANAGEMENT

**BLUF:** Advanced builders manage the full development lifecycle — creating branches for
development work, reviewing changes, and executing the promotion workflow to production —
entirely through the platform UI without scripting or CI/CD configuration.

## 8-1. Branching and the Development Lifecycle

> **NOTE:** TM-20 builders follow a development lifecycle defined in TM-20, Chapter 7 (Branching and Environment Management): develop on a branch, test, request merge, get approval, merge to main. TM-30 development follows the same pattern with more rigorous testing gates because your changes affect shared infrastructure. Operators (TM-10) only access the main/production branch. Every merge to main is a production release. Apply engineering discipline — test against TM-10 operator workflows (Chapter 4) before merging.

8-1. The platform uses a branching model to separate development work from production. A branch
is an isolated copy of the environment where changes can be made, tested, and reviewed without
affecting the production environment that other users depend on.

8-2. The three environments for USAREUR-AF builders:

| Environment | Purpose | Who Works Here |
|-------------|---------|----------------|
| Production (main branch) | The live environment used by all consumers | No one develops here; promotion only |
| Development branch | Where new features and changes are built | The builder working on the change |
| Review branch (pre-production) | Staging area for Data Steward and peer review before promotion | Reviewer and Data Steward |

8-3. Never develop directly on the production branch. If you are making changes in production,
you are doing it wrong.

## 8-2. Creating and Managing a Development Branch

**CONDITIONS:** Identified change to implement; Data Steward awareness of the planned change.

**STANDARDS:** Builder creates a named branch with a descriptive name, completes all development
in the branch, and does not merge to production without peer review and Data Steward sign-off.

8-4. **PROCEDURE — Create a Development Branch:**
1. Navigate to the **Branch Manager** or **Environment Manager** in the platform.
2. Select **Create Branch** from the production branch (or from main).
3. Name the branch using the convention: [builder-id]_[change-description]_[YYYYMMDD]
   Example: sgt-jones_readiness-dashboard-v2_20260311
4. Confirm the branch is created from the correct base (production).
5. Switch to the new branch in your workspace — verify you are working in the branch,
   not in production.

8-5. While working in the branch:
- Make all changes (pipeline updates, Workshop edits, ontology changes) in the branch only
- Test all changes thoroughly in the branch
- Do not promote until all tests pass and the change is ready for review

## 8-3. Peer Review Process

**CONDITIONS:** Completed development in a branch; ready for review.

**STANDARDS:** Builder submits a review request with complete documentation of changes.
Reviewer examines all changes, tests functionality, and provides written approval or documented
change requests before promotion is authorized.

8-6. **PROCEDURE — Submit a Branch for Review:**
1. In the Branch Manager, locate your development branch.
2. Select **Request Review** or **Create Review Request**.
3. Complete the review request form:
   - **Summary of changes:** what was built or modified?
   - **Test results:** what did you test? What was the outcome?
   - **Downstream impact:** what downstream products are affected?
   - **Rollback plan:** if the change breaks something in production, how will it be reversed?
   - **Data Steward notification:** confirm the Data Steward has been notified.
4. Assign the reviewer (a qualified peer or the Data Steward).
5. Submit the request.

8-7. **PROCEDURE — Review a Branch (as Reviewer):**
1. Open the review request.
2. Switch to the branch being reviewed.
3. Examine all changes:
   - Pipeline changes: verify logic, verify output schema, run a test execution and check results.
   - Workshop changes: test all interactive elements, verify variable behavior, check all pages.
   - Ontology changes: verify naming conventions, check downstream impact.
   - Access controls: verify access is configured correctly.
4. Document your review findings.
5. Approve the review (no issues found) or request changes (document specific items to address
   before promotion).

## 8-4. Production Promotion

**CONDITIONS:** Approved review; Data Steward sign-off; scheduled promotion window.

**STANDARDS:** Builder executes promotion during the authorized window, confirms production
environment is healthy after promotion, and notifies downstream application owners.

8-8. **PROCEDURE — Promote a Branch to Production:**
1. Confirm all review approvals are recorded.
2. Confirm Data Steward has provided sign-off.
3. Coordinate with downstream application owners — if the promotion will cause a brief
   downtime or change a data schema, notify consumers in advance.
4. Schedule the promotion during an approved maintenance window if the change is significant.
5. In the Branch Manager, select the reviewed branch and initiate **Promote to Production**.
6. Monitor the promotion progress in the platform logs.
7. After promotion completes:
   - Verify the production environment is healthy: open the promoted application, run a
     pipeline, check that the promoted changes are visible and correct.
   - Verify that other applications that share the changed resources are still functioning.
   - Notify downstream owners that the promotion is complete.
8. If issues are identified post-promotion, execute the rollback plan immediately. Do not
   attempt to fix issues with additional changes while production is impaired — rollback first.

**WARNING:** Promoting a change that breaks a downstream application or pipeline in production
is a significant governance event. Report the incident to the Data Steward immediately. Follow
the post-incident review process to document root cause and corrective action.

## 8-5. Production Discipline

8-9. Production discipline is the set of behaviors that maintain trust in the production
environment. Advanced builders are directly responsible for production discipline in everything
they promote.

8-10. Production discipline standards:

| Standard | Requirement |
|----------|-------------|
| No direct production edits | All changes through branches with review — no exceptions |
| Test before review | All changes tested in the development branch before requesting review |
| Review before promotion | No self-approved promotions — another qualified individual must review |
| Document all promotions | Maintain a log of what was promoted, when, by whom, and for what purpose |
| Notify downstream owners | Any promotion that affects shared resources requires advance notification |
| Rollback plan | Every significant promotion must have a documented rollback procedure |
| Incident reporting | Any production issue caused by a promotion must be reported within 24 hours |

---

# CHAPTER 9 — STANDARDS, CONVENTIONS, AND BEST PRACTICES

**BLUF:** Consistent standards across all products built by USAREUR-AF advanced builders
create a coherent, maintainable data environment. This chapter specifies the naming conventions,
design patterns, and quality standards that apply to everything built at TM-30 level.

## 9-1. Naming Conventions

9-1. All resources created on the MSS platform by USAREUR-AF builders must follow C2DAO
naming conventions. Non-compliant naming is a governance deficiency and will be flagged in
Data Steward reviews.

### 9-1a. Resource Naming Reference

9-2. **Dataset naming:**
[domain]_[source-or-description]_[output-type]_v[version]
Examples:
- log_pbuse-vehicle-fleet_cleaned_v1
- ops_sitrep-events_aggregated-daily_v2
- med_patient-encounters_anonymized_v1

9-3. **Pipeline naming:**
[domain]_[input-description]_[output-description]_v[version]
Examples:
- log_vehicle-fleet-maintenance_readiness-join_v1
- ops_sitrep-raw_dedup-aggregated_v3

9-4. **Object Type naming:**
PascalCase, singular noun, prefixed with domain abbreviation: [DomainAbbrev][EntityName]
Examples:
- LogVehicle — Logistics domain, Vehicle entity
- OpsUnit — Operations domain, Unit entity
- MedFacility — Medical domain, Facility entity
- G2IntelligenceReport — G2 domain, Intelligence Report entity

9-5. **Workshop application naming:**
[Domain] - [Audience] - [Application Purpose]
Examples:
- LOG - G4 Staff - Equipment Readiness Dashboard
- OPS - BCT CDR - Operations Summary Board
- G2 - All Staff - Intelligence Overview

9-6. **Contour and Quiver saved views:**
[domain]_[analysis-purpose]_[frequency-or-audience]
Examples:
- log_readiness-by-unit_weekly
- g2_threat-trend_cdre-brief

9-7. **Pipeline Builder node labels (within the pipeline graph):**
Label every node. Format: [action]_[subject] using snake_case.
Examples: src_vehicle_fleet, filter_active_only, join_maintenance_records,
agg_by_unit_category, out_readiness_rollup

9-8. **Variable naming (Workshop):**
[domain]_[descriptor]_[type]
Examples: ops_selected_unit_string, log_date_filter_date, g2_show_classified_boolean

### 9-1b. Domain Abbreviations

| Domain | Abbreviation | Responsible Staff |
|--------|--------------|-------------------|
| Logistics | log | G4 / S4 |
| Operations | ops | G3 / S3 |
| Medical | med | G4 / Surgeon |
| Intelligence | g2 | G2 / S2 |
| Signal/Comms | sig | G6 / S6 |
| Civil Affairs | g9 | G9 |
| Personnel | g1 | G1 / S1 |
| Finance | fin | G8 |

## 9-2. Design Best Practices

### 9-2a. Application Design

9-9. Design principles for Workshop applications:

1. **Start with the question, not the data.** What decision does this application support?
   Design the layout around the answer, then connect the data.

2. **One page, one question.** Each page should answer one operational question clearly.
   Resist the urge to put everything on one page.

3. **Design for the user's time.** Operational users are often time-constrained. The most
   important information should be visible without any clicks or scrolling.

4. **Use progressive disclosure.** Show summary first, detail on selection. Do not display
   maximum detail by default.

5. **Empty states are content.** Design what the user sees when no data matches the filters.
   "No records match the selected filters" is better than a blank page.

6. **Label everything.** Every widget should have a clear title. Every metric tile should have
   a unit of measure. Every table column should have a readable header.

7. **Consistent color use.** Use platform-standard colors for status (red/amber/green). Do not
   invent a color scheme that conflicts with other applications in the environment.

### 9-2b. Pipeline Design

9-10. Design principles for Pipeline Builder:

1. **Profile before you build.** Before joining or aggregating, examine source datasets. Know
   the row counts, key distributions, and NULL rates before designing your pipeline.

2. **Filter early.** Apply date and key filters as early in the pipeline as possible to
   minimize the data volume processed through downstream transforms.

3. **Document join decisions.** For every join node, add a description explaining why this
   join type was chosen, what the join key is, and what the expected row count ratio is.

4. **Test with known data.** Validate pipeline output against records you know the expected
   result for. If you are building a readiness rollup, manually compute the expected output
   for one battalion and compare to pipeline output.

5. **Plan for NULL.** Every production dataset contains NULLs. Add explicit NULL handling
   after every source node.

6. **Readable graphs.** Arrange pipeline nodes so the flow direction is clear (left to right
   or top to bottom). Label all nodes. Group related transforms visually.

### 9-2c. Ontology Design

9-11. Design principles for Ontology work:

1. **Model the entity, not the dataset.** An Object Type represents a real-world operational
   entity — not a row in a spreadsheet. Design properties around what the entity IS, not what
   columns happen to exist in the source data.

2. **Fewer, better properties.** Include only properties that downstream consumers will
   actually use. Unused properties add schema complexity and maintenance burden.

3. **Status fields need valid value documentation.** Any property with a defined set of valid
   values must document those values in the property description.

4. **Link Types represent real relationships.** Only create a Link Type if the relationship
   between two Object Types is operationally meaningful and will be traversed in downstream
   analysis or applications.

5. **Primary key is sacred.** The primary key must be truly unique and stable. Changing the
   primary key on a production Object Type is a major breaking change.

## 9-3. Performance Considerations

9-12. Advanced builders are responsible for the performance characteristics of what they build.
An application that loads slowly or a pipeline that takes hours degrades the operational
environment for all users.

9-13. Performance checklist before publishing to production:

| Check | How to Verify | Action if Failing |
|-------|---------------|-------------------|
| Application page load time | Preview in an incognito browser session; time the load | Reduce widget count, add filters with default values, paginate large tables |
| Object Set size | Check row count on Object Set widget | Add a default filter to limit initial load; implement pagination |
| Pipeline run time | Check pipeline execution metrics | Add early filters, verify partition pruning is active on date filters |
| Map widget object count | Preview map with production data | Limit objects displayed; add a filter requiring user selection before map populates |
| Table row count | Preview table with production data | Implement server-side pagination; add a mandatory filter before results appear |

## 9-4. USAREUR-AF C2DAO Governance Checklist Summary

9-14. Every product published to production must satisfy the following governance requirements:

**Naming Compliance:**
- [ ] Dataset, pipeline, Object Type, and application names follow C2DAO naming conventions
- [ ] All pipeline nodes are labeled descriptively
- [ ] All Workshop variables follow the naming convention

**Documentation:**
- [ ] Dataset and pipeline descriptions are complete (source, purpose, owner, refresh cadence)
- [ ] Object Type description explains the entity, source, and operational purpose
- [ ] Object Type properties have descriptions for non-obvious fields
- [ ] Actions have clear user-facing labels and confirmation messages

**Access Control:**
- [ ] Access is configured to least-privilege for the intended audience
- [ ] No unintended "all users" access on products containing sensitive or controlled data
- [ ] Access configuration is documented in the product description

**Quality:**
- [ ] NULL handling is implemented in all pipelines
- [ ] Join types are documented and correct
- [ ] Action validation rules are configured for all user-input parameters
- [ ] Downstream impact assessment completed for any change to shared resources

**Review and Promotion:**
- [ ] Development completed in a branch (not production)
- [ ] Peer review completed and documented
- [ ] Data Steward review and sign-off obtained
- [ ] Promotion window coordinated with downstream owners

---

# APPENDIX A — ADVANCED BUILDER CHECKLIST

> **NOTE:** Before initiating a TM-40 handoff, confirm the requirement genuinely exceeds TM-30 capability. Use this checklist: (1) Can this be built using TM-20 no-code tools? If yes — hand back to TM-20 builder, do not escalate to TM-40. (2) Can this be designed using TM-30 UI tools (Workshop, Ontology Manager UI, Pipeline Builder UI, AIP Logic UI)? If yes — build at TM-30 level, do not escalate. (3) Does implementation require writing code (Python, PySpark, TypeScript, SQL)? If yes — use this template and initiate TM-40 handoff. Unnecessary TM-40 escalation consumes developer capacity and delays delivery.

Use this checklist when delivering any new or significantly modified MSS data product.

## Pre-Build Checklist

- [ ] Requirement defined: what operational question does this product answer?
- [ ] Audience identified: who uses it and in what context?
- [ ] Data sources identified: what datasets or Object Types are the inputs?
- [ ] Data Steward notified: coordinated with the relevant Data Steward?
- [ ] Existing products checked: is this already built somewhere that could be reused or extended?
- [ ] Naming convention selected: what will the product be named per C2DAO standards?
- [ ] Branch created: development branch created from production?

## Build Checklist

- [ ] All work done in branch (not production)
- [ ] Source datasets profiled (row counts, key distributions, NULL rates)
- [ ] NULL handling implemented in all pipelines
- [ ] Join types documented in node descriptions
- [ ] Calculated columns verified against known records
- [ ] Workshop variables follow naming convention
- [ ] All Workshop pages tested (navigation, conditional visibility, variable behavior)
- [ ] Computed columns verified for correctness
- [ ] Access controls configured to least-privilege
- [ ] Empty states handled in Workshop (no blank pages when filters return zero results)
- [ ] Action validation rules configured for all user-input parameters
- [ ] AIP Logic configurations documented and tested with sample data

## Review and Promotion Checklist

- [ ] Self-review completed — tested with production-representative data
- [ ] Downstream impact assessment completed
- [ ] Downstream owners notified of changes
- [ ] Peer review requested and completed
- [ ] Data Steward review and sign-off obtained
- [ ] Rollback plan documented
- [ ] Promotion executed in authorized window
- [ ] Post-promotion verification completed
- [ ] Downstream application owners notified of successful promotion

---

# APPENDIX B — DESIGN PATTERNS REFERENCE

> **NOTE:** This is the TM-30 checklist for advanced multi-page, cross-functional applications. If your application is single-page and purpose-specific, use the TM-20 checklist (TM-20, Appendix C, Workshop Application Pre-Publish Checklist) instead. Before publishing any application, test it against operator workflows in TM-10, Chapter 4 (Using Workshop Applications). An application that a trained operator cannot navigate using TM-10 procedures is not ready for publication.

## Pattern 1: Commander's Dashboard

**Purpose:** Give a commander an at-a-glance operational picture with drill-down capability.

**Structure:**
- Page 1 (Overview): Metric tiles (key readiness numbers), status bar chart, map of unit locations
- Page 2 (Unit Detail): Triggered by unit selection on Page 1; shows selected unit's detail
- Page 3 (Trend): Time-series charts showing readiness trend over the past 30/60/90 days

**Key patterns:**
- Variable: ops_selected_unit_object — written by map or table selection, read by Page 2
- Default filter on Page 1 table: current reporting period only (avoid loading full history)
- Conditional visibility on Page 2: show only when ops_selected_unit_object is not empty
- Date range picker on Page 3: dynamic "last N days" filter driven by a variable

---

## Pattern 2: Status Board with Write-Back

**Purpose:** Allow authorized users to update equipment or personnel status from within the
application.

**Structure:**
- Left panel: filtered table of records (user selects a record)
- Right panel: detail view of selected record (appears on selection)
- Bottom of right panel: Action button(s) to update status

**Key patterns:**
- Variable: log_selected_record_object — written by table row click, read by detail panel
  and Action
- Conditional visibility: right panel visible only when log_selected_record_object is not empty
- Action configuration: pre-populate parameters from the selected object's properties where
  possible
- Confirmation message: shows the specific record being updated and the new value before
  execution

---

## Pattern 3: Readiness Rollup Pipeline

**Purpose:** Produce a unit-level readiness summary from an equipment dataset and maintenance
records.

**Pipeline structure:**
1. src_equipment_fleet — source dataset
2. filter_active_vehicles — filter: status is not DISPOSED AND reporting_period is current
3. src_maintenance_records — source dataset
4. filter_recent_maintenance — filter: maintenance_date within last 30 days
5. join_fleet_maintenance — Left Join on vehicle_id
6. calc_is_fmc — calculated column: if maint_status equals "FMC" then 1 else 0
7. agg_by_unit_category — Group By unit_uic and equipment_category; COUNT(*) to vehicle_count,
   SUM(is_fmc) to fmc_count
8. calc_readiness_rate — calculated column: fmc_count / vehicle_count * 100
9. calc_status_color — calculated column: if/else producing GREEN, AMBER, or RED
10. out_readiness_rollup — output dataset

---

## Pattern 4: Hierarchical Object Type Model

**Purpose:** Model an operational hierarchy (Theater — Corps — Division — Brigade — Battalion —
Unit).

**Object Types:**
- OpsTheater — Theater-level entity
- OpsCorps — Corps entity, linked to OpsTheater
- OpsDivision — Division entity, linked to OpsCorps
- OpsBrigade — Brigade entity, linked to OpsDivision
- OpsBattalion — Battalion entity, linked to OpsBrigade
- OpsUnit — Company/detachment entity, linked to OpsBattalion

**Link pattern:** Each Link Type is one-to-many (one Corps has many Divisions, etc.)
**Workshop pattern:** Cascading dropdown variables drive filter from Theater down to Unit level.
**Quiver pattern:** Traverse links upward and downward; aggregate metrics across the hierarchy.

---

## Pattern 5: Data Quality Dashboard

**Purpose:** Give Data Stewards visibility into data quality issues across their domain.

**Structure:**
- Page 1 (Summary): Counts of open issues by severity, source dataset, and age
- Page 2 (Issue Queue): Table of all open issues with filters by status, severity, and dataset
- Page 3 (Issue Detail): Detail view for a selected issue with resolution actions

**Key patterns:**
- Data quality issues stored as an Object Type (GovDataQualityIssue)
- Actions on Issue Detail page: Mark Resolved, Escalate, Add Comment
- Variable: gov_selected_issue_object — drives Page 3 detail view
- Default filter on Page 2: show only open and in-progress issues (not resolved)
- Trend chart on Page 1: shows issue count by week over rolling 90 days

---

# GLOSSARY

**Action**
A configured workflow on the Ontology that allows authorized users to create, modify, or delete
object data through the platform UI. Actions execute validation rules before writing data.

**AIP Logic**
The AI workflow layer of the MSS platform. Enables AI-assisted analysis, automated reasoning,
and natural language query interfaces. TM-30 builders configure existing AIP Logic workflows;
authoring is TM-40 scope.

**API Name**
The machine-readable identifier for an Object Type, property, or Action. Distinct from the
human-readable display name. Once published to production, the API name should not change
without a coordinated downstream impact assessment.

**Branching**
The platform mechanism for isolating development work from the production environment. Builders
create a branch from production, develop in the branch, and promote to production only after
review and approval.

**C2DAO**
Command and Control Data Authoritative Organization. The USAREUR-AF governance body responsible
for data product standards, naming conventions, access control policy, and production promotion
approvals.

**Calculated Column**
A derived data column whose value is computed from a formula applied to other columns. In
Pipeline Builder, calculated columns are permanent and stored in the output dataset. In Workshop
and Contour, they are display-only and not stored.

**Cardinality**
In data modeling, the numerical relationship between two linked Object Types. One-to-one,
one-to-many, or many-to-many. Determines how Link Types are configured in the Ontology.

**CDA Portal**
Common Data Architecture Portal. The Army's authoritative training and reference resource for
data platform work, hosted at learn-data.armydev.com.

**Conditional Visibility**
A Workshop configuration that shows or hides a widget based on the value of an application
variable. Used to create dynamic, responsive application layouts.

**Contour**
The MSS platform's visual analytics tool. Allows builders and analysts to query, aggregate,
pivot, and chart data without writing code. Produces saved analysis views that can be shared
and embedded.

**Data Product Owner**
The individual responsible for the operational accuracy, quality, and maintenance of a data
product (dataset, Object Type, or application). Designated per Army CIO Memorandum (April 2024).

**Data Steward**
The designated authority for data quality, access control, naming compliance, and governance
within a data domain. Builders coordinate with Data Stewards before creating, modifying, or
promoting shared resources.

**Downstream Impact**
The effect of a change to a shared data resource on all products that depend on it —
applications, pipelines, Object Types, analytics views. Assessment of downstream impact is
required before any production change.

**Empty State**
The visual condition of a Workshop widget when no data matches the current filter or no
selection has been made. Advanced builders design explicit empty states rather than leaving
blank panels.

**Full Outer Join**
A join operation that returns all rows from both source datasets, with NULLs where no match
exists in the other dataset.

**Governance**
The set of policies, standards, and processes that ensure data products are accurate, accessible
to authorized users, consistently named, and maintained over time. Governed by C2DAO within
USAREUR-AF.

**Group By**
A pipeline or analysis transform that collapses multiple rows into a single summary row per
unique combination of grouping keys, applying aggregation functions to the non-key columns.

**Inner Join**
A join operation that returns only rows that have a match in both source datasets. Rows without
a match in either dataset are excluded from the output.

**Left Join**
A join operation that returns all rows from the left (primary) dataset, with NULLs in right-
side columns where no match exists in the right dataset.

**Lineage Graph**
A visual representation of data flow showing the chain of sources, pipelines, and outputs that
produced a given dataset or Object Type. Used for impact assessment, quality investigation, and
governance audits.

**Link Type**
An Ontology construct that defines a named relationship between two Object Types. Enables
multi-object analysis in Quiver and relationship traversal in Workshop and AIP Logic.

**Null Handling**
Explicit pipeline logic that addresses NULL (missing) values in source data — filtering,
replacing with defaults, or flagging for review — before NULLs can propagate into outputs
and cause analysis errors.

**Object Set**
A filtered collection of objects from an Object Type, defined by one or more filter conditions.
Used as the data source for Quiver analyses and Workshop Object Set widgets.

**Object Type**
The fundamental ontology construct representing a class of real-world operational entities
(e.g., LogVehicle, OpsUnit). Each object instance represents one specific entity.

**Ontology**
The shared data model of the MSS platform. Defines what entities exist (Object Types), how
they relate (Link Types), and what users can do to them (Actions).

**Ontology Manager**
The platform UI for creating, configuring, and publishing Object Types, Link Types, and Actions.

**Partition Pruning**
The platform behavior of reading only the partitions of a dataset that satisfy the filter
conditions applied to the partition key. Requires that filters on the partition key are applied
early in the pipeline.

**Pipeline Builder**
The MSS platform's visual, no-code data transformation tool. Allows builders to read, join,
filter, aggregate, and output datasets without writing code.

**Pivot**
A transform that rotates a long-format dataset (one row per category per entity) into a wide-
format dataset (one row per entity, one column per category). Available in both Pipeline Builder
and Contour.

**Primary Key**
The property (or combination of properties) that uniquely identifies each object instance in
an Object Type. Must be unique and stable across the lifetime of the Object Type.

**Production Branch**
The live environment that operational users depend on. No development occurs in production —
all changes are promoted from reviewed development branches.

**Progressive Disclosure**
A UX design pattern in which summary information is displayed first and detail is revealed
on user selection or interaction. Reduces cognitive load and application load time.

**Property**
A named attribute of an Object Type instance. Properties store the data about each object —
its name, status, location, identifier, and other characteristics.

**Quiver**
The MSS platform's object-centric analysis tool. Allows builders and analysts to explore
Object Types, traverse Link Types, define object sets, and build multi-object dashboards.

**Saved View**
A persistently saved Contour analysis or Quiver dashboard configuration, including all filter
settings, calculated columns, and chart configurations. Enables repeatable, shareable
analytical products.

**UDRA**
Unified Data Reference Architecture. Army enterprise architecture standard (v1.1, February 2025)
that defines data domains, governance roles, and architectural patterns. All USAREUR-AF data
products must align to a UDRA domain.

**Union**
A pipeline transform that combines rows from two or more datasets with compatible schemas into
a single output dataset.

**Variable (Workshop)**
A named container in a Workshop application that stores a value set by user interaction or
application logic. Variables enable dynamic filtering, conditional visibility, and state
management across pages.

**Workshop**
The MSS platform's no-code application builder. Allows builders to create interactive,
data-driven operational interfaces using configurable widgets without writing code.

---

*TM-30 — Maven Smart System Advanced No-Code Builder Technical Manual*
*Headquarters, United States Army Europe and Africa, Wiesbaden, Germany, 2026*
*Distribution Restriction: Approved for public release; distribution is unlimited.*
