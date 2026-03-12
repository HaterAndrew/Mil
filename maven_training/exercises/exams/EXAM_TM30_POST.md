# POST-TEST — TM-30: ADVANCED BUILDER
## Maven Smart System (MSS) — USAREUR-AF

| Field | Detail |
|---|---|
| **Course** | TM-30: Advanced Builder |
| **Form** | Post-Test |
| **Level** | TM-30 (Advanced) |
| **Audience** | Data-adjacent specialists — 17/25-series, S6/G6/G2/G9; prerequisite: TM-10 + TM-20 |
| **Time Allowed** | 45 minutes |
| **Passing Score** | 70% (42/60) |

---

## INSTRUCTIONS

This assessment evaluates mastery of course learning objectives. A passing score of 70% is required to receive credit. Complete independently without reference to training materials.

---

## SECTION 1 — MULTIPLE CHOICE

*Circle the letter of the best answer. (2 points each)*

**1. You are building a multi-page Workshop application where Page 2 should display maintenance details for the vehicle selected on Page 1. The correct TM-30 implementation approach is:**

A. Export the Page 1 selection to a pipeline variable and rebuild the dataset on navigation
B. Configure a URL deep link on Page 1 that passes the selected vehicle ID as a variable to Page 2
C. Rebuild the Page 2 filters using the same dropdown as Page 1 — no variable passing is needed
D. Use a conditional show/hide block on Page 1 to display the maintenance details in an expandable panel

**2. Your Pipeline Builder pipeline joins a unit roster (4,000 rows) to a training event table (12,000 rows) on `soldier_id`, where each Soldier can appear in multiple events. A SUM of duty hours after the join returns a value 3x higher than expected. The MOST likely cause is:**

A. The pipeline is running a full outer join instead of a left join
B. A one-to-many join fan-out is duplicating the unit roster rows, tripling aggregate sums
C. The `duty_hours` column contains nulls that are being interpreted as zeros
D. The GROUP BY step is grouping by the wrong column

**3. In a Pipeline Builder pipeline, a "union" step that combines two quarterly report datasets requires:**

A. Both datasets to share a primary key column for the union
B. Both datasets to have identical column names and compatible data types
C. The pipeline to run a deduplication step after the union
D. Both datasets to originate from the same source system

**4. A Pipeline Builder pipeline that uses an "Append" transaction mode will:**

A. Overwrite the target dataset on each run
B. Validate each record against the schema before writing
C. Add new records to the existing dataset without deleting prior records, enabling history tracking
D. Write only records that are different from the previous pipeline run

**5. You are configuring a scheduled pipeline to refresh a logistics dataset at 0400 daily and notify the G4 NCOIC by email on failure. The email alert is configured in:**

A. The Workshop application settings
B. The pipeline's schedule and alerting configuration
C. The Ontology Manager notification settings
D. The data steward's project settings

**6. The TM-30 Ontology Design Rubric evaluates a schema against how many items, and what is the minimum score to pass?**

A. 5 items; 80% to pass
B. 6 items; 75% to pass
C. 8 items; 70% to pass
D. 6 items; 70% to pass

**7. In the C2DAO promotion workflow, the data steward's role during promotion review includes:**

A. Automatically approving all changes submitted by Editor-role users
B. Reviewing the change description, validating naming conventions, checking data quality, and approving or returning the branch with feedback
C. Deploying the branch to production without further review once a Builder submits it
D. Only reviewing changes that affect Object Types — pipeline changes are auto-approved

**8. A G2 analyst asks you to configure (not author) an AIP Logic workflow to summarize incoming OSINT reports. Per TM-30 procedures, "configure" means:**

A. Writing the prompt engineering and chain logic for the AIP workflow
B. Selecting pre-built workflow templates, setting input/output parameters, and connecting to authorized data sources — not writing new chain logic
C. Deploying the workflow to production after testing
D. Reviewing and red-teaming the workflow against adversarial inputs

**9. You are building a Contour analysis of fuel consumption trends. You need to calculate a column showing each vehicle's consumption as a percentage of the fleet average. The correct Contour feature for this is:**

A. A filter control applied to the fleet average row
B. A calculated column using a window function or the fleet average as a reference value
C. A pivot table with fleet average as the row header
D. A parameter control set to the fleet average value

**10. In a Quiver multi-object dashboard, "cross-object filter propagation" means:**

A. Exporting filter selections from one Quiver view to a Pipeline Builder pipeline
B. When a user selects an object in one Quiver panel, linked objects in other panels update to show only related records
C. Applying the same date range filter to all Quiver dashboards in a project
D. Limiting which Object Types are visible based on the user's role

**11. Your Workshop application displays a readiness table with conditional formatting — RED background for readiness below 70%. After a pipeline run, three vehicles that were previously RED now correctly show 80%, but their row backgrounds remain red. The MOST likely cause is:**

A. The conditional formatting rule is hardcoded to always show RED for those vehicle IDs
B. The Workshop table is cached and has not refreshed to reflect the updated dataset
C. The Pipeline Builder pipeline is writing to the wrong Ontology property
D. The conditional formatting rule references the wrong field in the dataset

**12. Per TM-30 procedures, which of the following is a REQUIRED element in a promotion description when submitting a branch for data steward review?**

A. The names of all users who reviewed the branch before submission
B. A description of what changed, why it changed, and confirmation that data quality checks passed
C. A signed memorandum from the project owner approving the change
D. A comparison of pipeline run times before and after the change

**13. A multi-source join "fan-out handling" technique in Pipeline Builder involves:**

A. Running all source joins in parallel to reduce pipeline run time
B. Pre-aggregating the many-side table before joining to the one-side table to prevent row multiplication
C. Filtering each source table to the same date range before joining
D. Using a union step instead of a join when multiple sources are present

**14. You need to build a Contour pivot table showing ammunition consumption by unit (rows) and ammunition type (columns), with totals. The correct Contour configuration step is:**

A. Build a bar chart and manually transpose the axes
B. Configure a pivot table with `unit` as the row dimension, `ammo_type` as the column dimension, and `quantity` as the aggregated value
C. Export the dataset and create the pivot table in Excel
D. Build a calculated column that pre-aggregates by unit and type before the pivot step

**15. A Workshop application page should display a "No data available" message when a filter variable returns no matching records, instead of showing an empty table. The correct TM-30 implementation is:**

A. Set the table's empty-state message in the table widget configuration
B. Use a conditional show/hide block: show a text widget with "No data available" when the table row count equals zero, hide it otherwise
C. Configure the filter to prevent selection of values that return no records
D. Add a pipeline validation step that blocks empty results from being written to the dataset

---

## SECTION 2 — SHORT ANSWER

*Answer in 2–5 sentences. (6 points each)*

**SA-1. Your G6 section is asked to build a Workshop application for a division-level communications network tracking system. The application needs: a map view of all communication nodes, a filtered list by node type, and a drill-down page showing linked maintenance records for a selected node. Describe how you would use multi-page design, variable passing, and URL deep linking to implement this.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-2. A pipeline builder colleague shows you a pipeline where a GROUP BY aggregation of total maintenance hours by unit is returning values 5–6x higher than the actual totals. Walk through your diagnostic process and describe the most likely root cause and fix.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-3. You have been asked to design an Ontology schema for an S6 network topology tracker. The schema must track: network nodes, the links between them, and the maintenance work orders for each node. Describe the Object Types, key properties, and Link Types you would define, and explain one design decision you made and why.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-4. Describe the complete C2DAO promotion workflow from the moment a builder finishes development through production deployment. Identify the step where promotion is most commonly rejected and explain the most frequent reason.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-5. A Quiver dashboard showing unit readiness objects has a linked view of equipment assigned to each unit. When a user selects a unit in the left panel, the equipment list on the right does not filter to that unit. Describe how you would troubleshoot and resolve this cross-object filter propagation issue.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

---

## SCORING SUMMARY

| Section | Questions | Points Each | Total Points |
|---|---|---|---|
| Multiple Choice | 15 | 2 | 30 |
| Short Answer | 5 | 6 | 30 |
| **Total** | — | — | **60** |

Passing: 42/60 (70%) — Post-test only. Pre-test is diagnostic.

---

## ANSWER KEY — INSTRUCTOR USE ONLY

*Do not distribute to students.*

**Multiple Choice:**
1. B — URL deep link with vehicle ID variable passed to Page 2 is the correct TM-30 multi-page approach.
2. B — Fan-out from a 1:M join on soldier_id duplicates roster rows, tripling aggregated sums.
3. B — Union requires identical column names and compatible types; no join key is needed.
4. C — Append adds records without deleting prior data, enabling historical accumulation.
5. B — Schedule and alerting configuration is where email alerts are set in Pipeline Builder.
6. B — TM-30 Ontology Design Rubric: 6 items, 75% to pass (per TM-30 Chapter 5).
7. B — Data steward reviews, validates, and approves or returns with feedback.
8. B — "Configure" = select templates, set parameters, connect sources; not writing chain logic.
9. B — Calculated column using fleet average reference value is the correct Contour approach.
10. B — Cross-object filter propagation: selection in one panel updates linked panels to show related records.
11. B — Workshop table cache lag; table has not refreshed to show updated pipeline data.
12. B — Promotion description must include what changed, why, and data quality check confirmation.
13. B — Pre-aggregating the many-side before joining is the standard fan-out handling technique.
14. B — Pivot table with unit as rows, ammo_type as columns, quantity as aggregated value.
15. B — Conditional show/hide: show "no data" text widget when row count = 0.

**Short Answer Guidance:**

SA-1. Full credit: Page 1 = map view of all communication nodes with node type filter; selecting a node sets a variable (node_id); Page 2 = filtered maintenance records list using node_id variable passed from Page 1; URL deep link on Page 1 node cards encodes node_id so the G6 team can share direct links to specific node maintenance pages. Must reference variable passing, multi-page structure, and deep linking for full credit.

SA-2. Full credit: diagnose by checking row counts before and after each join step in the pipeline; compare actual totals to a known-correct baseline (e.g., sum from the original source); most likely root cause is a one-to-many join on a field where the maintenance table has multiple records per unit, causing each unit row to be duplicated for every maintenance record — fix by pre-aggregating the maintenance table by unit before joining to the unit roster. Partial credit (3 pts) for identifying fan-out without diagnostic steps.

SA-3. Full credit: Object Types — NetworkNode (node_id, type, location, status), NetworkLink (link_id, bandwidth, protocol), MaintenanceWorkOrder (wo_id, date, technician, status, node_id_fk); Link Types — Node-to-Node via NetworkLink (M:M), Node-to-WorkOrder (1:M); design decision example: treating NetworkLink as an Object Type rather than just a property allows tracking link-specific attributes and maintenance separately from node maintenance. Partial credit (3 pts) for two Object Types with a Link Type but no design rationale.

SA-4. Full credit: Builder completes work on branch → writes promotion description (what/why/QC passed) → submits for data steward review → data steward reviews naming, schema, pipeline logic, data quality → approves or returns with feedback → builder addresses feedback → re-submits → data steward approves → branch merged to production. Most common rejection point: promotion description review — most frequent reason: naming convention violations (non-C2DAO names) or missing data quality check confirmation. Partial credit (3 pts) for correct sequence without identifying rejection point.

SA-5. Full credit: verify the Unit Object Type and Equipment Object Type have a defined Link Type connecting them; in Quiver dashboard configuration, check that the equipment panel's filter input is wired to the unit selection variable from the unit panel; verify the Link Type cardinality is correct and the pipeline has populated the links; if links are defined but panel is not wired, add the unit selection as a filter on the equipment panel's display configuration. Partial credit (3 pts) for identifying Link Type check without panel wiring diagnosis.

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*TM-30 Post-Test | Version 1.0 | March 2026*
