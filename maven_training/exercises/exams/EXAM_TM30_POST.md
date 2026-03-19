# POST-TEST — TM-30: ADVANCED BUILDER
## Maven Smart System (MSS) — USAREUR-AF

| Field | Detail |
|---|---|
| **Course** | TM-30: Advanced Builder |
| **Form** | Post-Test |
| **Level** | TM-30 (Advanced) |
| **Audience** | Data-adjacent specialists — 17/25-series, S6/G6/G2; prerequisite: TM-10 + TM-20 |
| **Time Allowed** | 45 minutes |
| **Passing Score** | 70% (50/72) |

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

**6. A Soldier who has completed TM-30 and wants to pursue specialized data work in operations research wants to know which track to take next. The correct answer is:**

A. TM-40A — Intelligence WFF Track (for G2/S2 staff applying MSS to intelligence operations)
B. TM-40G — ORSA Specialist Track (for FA49 and quantitative analysts; operations research focus)
C. TM-50G — Advanced ORSA Track (prereq: TM-40G — not yet accessible to a TM-30 graduate)
D. TM-40F — Mission Command WFF Track (for MC-function staff applying MSS to command products)

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

**16. Per DDOF Playbook v2.2, a data product that reaches Phase 3 (Data Wrangling) must pass a quality gate scored against the VAULTIS-A framework. The number of dimensions in VAULTIS-A and the minimum weighted average required to pass are:**

A. 5 dimensions (Visible, Accessible, Understandable, Trusted, Interoperable); 80% weighted average
B. 7 dimensions (Visible, Accessible, Understandable, Linked, Trusted, Interoperable, Secure); 85% weighted average
C. 8 dimensions (Visible, Accessible, Understandable, Linked, Trusted, Interoperable, Secure, Auditable); 85% weighted average
D. 8 dimensions (Visible, Accessible, Understandable, Linked, Trusted, Interoperable, Secure, Auditable); 90% weighted average

**17. Per DDOF Playbook v2.2, a data product in production that has not been accessed by any consumer in 90 days triggers which action?**

A. Automatic retirement and deletion from the platform
B. Functional Data Manager (FDM) review; 180 days with no access initiates retirement
C. Re-certification against all six DDOF phases before continued use
D. Downgrade to "draft" status with read-only access until the owner re-validates

**18. An advanced builder is designing an MSS application for a unit operating in an environment with intermittent network connectivity. Per TM-30 DDIL planning requirements, the correct mitigation for an intermittent (periodic connectivity) environment is:**

A. Pre-staged data packages with local compute and no synchronization
B. Store-and-forward queues with delta sync when connectivity is available
C. Text-only data products with reduced refresh rates
D. Full-bandwidth replication during each connectivity window

**19. Per DDOF Playbook v2.2, the six lifecycle phases in correct order are:**

A. Problem Framing → Data Wrangling → Data Provisioning → Development → Test & Evaluation → Operations
B. Data Provisioning → Problem Framing → Data Wrangling → Development → Test & Evaluation → Operations
C. Problem Framing → Data Provisioning → Data Wrangling → Development → Test & Evaluation → Operations
D. Problem Framing → Data Provisioning → Development → Data Wrangling → Test & Evaluation → Operations

**20. During DDOF Phase 1, a requirement must pass SMART criteria before advancing to Phase 2. If the mission owner states, "I need a readiness dashboard sometime this quarter," this requirement fails SMART because:**

A. It is not Specific — "readiness dashboard" does not define what readiness data is needed
B. It is not Measurable — there is no accuracy standard against an authoritative source
C. It fails both Specific and Time-bound — the data scope is undefined and "sometime this quarter" is not a date-certain IOC
D. It is not Achievable — readiness dashboards cannot be built in one quarter

**21. Per Genesis Mission directives and DDOF Playbook v2.2, "fail-closed enforcement" means that when the authorization service is unavailable or a user's role cannot be verified, the data product must:**

A. Grant read-only access until the authorization service recovers
B. Deny access, log the denial, and require explicit re-authorization once the service recovers
C. Fall back to the user's last known role and grant access at that level
D. Queue the access request and grant it automatically when the authorization service returns

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

**SA-5. A colleague who has just completed TM-30 asks you to explain what training options are available to them next. Describe the two downstream track categories — WFF tracks and specialist tracks — available after TM-30, including: the correct track ID range for each category, the prerequisite requirement for each category, and one example track from each category with its track title.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

---

## SCORING SUMMARY

| Section | Questions | Points Each | Total Points |
|---|---|---|---|
| Multiple Choice | 21 | 2 | 42 |
| Short Answer | 5 | 6 | 30 |
| **Total** | — | — | **72** |

Passing: 50/72 (70%) — Post-test only. Pre-test is diagnostic.

---

## ANSWER KEY — INSTRUCTOR USE ONLY

*Do not distribute to students.*

**Multiple Choice:**
1. B — URL deep link with vehicle ID variable passed to Page 2 is the correct TM-30 multi-page approach.
2. B — Fan-out from a 1:M join on soldier_id duplicates roster rows, tripling aggregated sums.
3. B — Union requires identical column names and compatible types; no join key is needed.
4. C — Append adds records without deleting prior data, enabling historical accumulation.
5. B — Schedule and alerting configuration is where email alerts are set in Pipeline Builder.
6. B — TM-40G is the ORSA Specialist Track for FA49 and quantitative analysts. Options A and D are WFF tracks targeting warfighting function staff roles, not operations research. Option C (TM-50G) is the Advanced ORSA track, which requires TM-40G as its prerequisite — a Soldier who has completed only TM-30 is not yet eligible. All TM-40 tracks (WFF and Specialist) require TM-30 as a hard prerequisite.
7. B — Data steward reviews, validates, and approves or returns with feedback.
8. B — "Configure" = select templates, set parameters, connect sources; not writing chain logic.
9. B — Calculated column using fleet average reference value is the correct Contour approach.
10. B — Cross-object filter propagation: selection in one panel updates linked panels to show related records.
11. B — Workshop table cache lag; table has not refreshed to show updated pipeline data.
12. B — Promotion description must include what changed, why, and data quality check confirmation.
13. B — Pre-aggregating the many-side before joining is the standard fan-out handling technique.
14. B — Pivot table with unit as rows, ammo_type as columns, quantity as aggregated value.
15. B — Conditional show/hide: show "no data" text widget when row count = 0.
16. C — VAULTIS-A has 8 dimensions (V-A-U-L-T-I-S-A: Visible, Accessible, Understandable, Linked, Trusted, Interoperable, Secure, Auditable) and requires 85% weighted average. VAULTIS-A supersedes VAUTI (5 dimensions, AR 25-1) per DDOF Playbook v2.2 (Dec 2025). Option A describes the older VAUTI framework. Option B has 7 dimensions (omits Auditable). Option D has the correct dimensions but wrong threshold (90% vs. 85%). Source: TM-30, Section 1-10 / DDOF Playbook v2.2.
17. B — Products with no access in 90 days require FDM review; 180 days no access initiates retirement. Quality gates are enforced, not advisory — products failing below 70% quality trigger remediate-or-retire. Option A is wrong because 90 days triggers review, not automatic retirement. Option C overstates the re-certification requirement. Option D invents a "draft" downgrade status not in doctrine. Source: TM-30, Section 1-10 / DDOF Playbook v2.2.
18. B — Intermittent connectivity requires store-and-forward queues with delta sync. Option A describes mitigations for a denied (no network) environment. Option C describes limited (low bandwidth) mitigations. Option D is not a defined DDIL mitigation. Source: TM-30, Section 1-10e (DDIL Environments) / ADP 6-0 / UDRA v1.1.
19. C — The correct DDOF phase order is: Phase 1 Problem Framing → Phase 2 Data Provisioning → Phase 3 Data Wrangling → Phase 4 Development → Phase 5 Test & Evaluation → Phase 6 Operations. Option A swaps Phases 2 and 3. Option B places Data Provisioning before Problem Framing. Option D places Development before Data Wrangling. Source: TM-30, Section 1-10 / DDOF Playbook v2.2.
20. C — The requirement fails both Specific (no definition of what readiness data is needed or which units) and Time-bound ("sometime this quarter" is not a date-certain IOC). Options A and B each identify only one failure — SMART requires all five criteria, and this requirement fails at least two. Option D is incorrect because readiness dashboards are achievable within a quarter given platform and data availability. A requirement that fails any SMART criterion must be returned to the Decision Maker for refinement before Phase 2. Source: TM-30, Section 1-10b / DDOF Playbook v2.2.
21. B — Fail-closed enforcement means deny access when authorization cannot be confirmed, log all denials, and require explicit re-authorization. Option A (read-only fallback) is a fail-open variant — not permitted. Option C (last known role fallback) is also fail-open — roles may have changed. Option D (auto-grant on recovery) bypasses explicit authorization. Per Genesis Mission directives, products that default to granting access on authorization failure will not pass Phase 5 T&E. Source: TM-30, Section 1-10c / DDOF Playbook v2.2.

**Short Answer Guidance:**

SA-1. Full credit: Page 1 = map view of all communication nodes with node type filter; selecting a node sets a variable (node_id); Page 2 = filtered maintenance records list using node_id variable passed from Page 1; URL deep link on Page 1 node cards encodes node_id so the G6 team can share direct links to specific node maintenance pages. Must reference variable passing, multi-page structure, and deep linking for full credit.

SA-2. Full credit: diagnose by checking row counts before and after each join step in the pipeline; compare actual totals to a known-correct baseline (e.g., sum from the original source); most likely root cause is a one-to-many join on a field where the maintenance table has multiple records per unit, causing each unit row to be duplicated for every maintenance record — fix by pre-aggregating the maintenance table by unit before joining to the unit roster. Partial credit (3 pts) for identifying fan-out without diagnostic steps.

SA-3. Full credit: Object Types — NetworkNode (node_id, type, location, status), NetworkLink (link_id, bandwidth, protocol), MaintenanceWorkOrder (wo_id, date, technician, status, node_id_fk); Link Types — Node-to-Node via NetworkLink (M:M), Node-to-WorkOrder (1:M); design decision example: treating NetworkLink as an Object Type rather than just a property allows tracking link-specific attributes and maintenance separately from node maintenance. Partial credit (3 pts) for two Object Types with a Link Type but no design rationale.

SA-4. Full credit: Builder completes work on branch → writes promotion description (what/why/QC passed) → submits for data steward review → data steward reviews naming, schema, pipeline logic, data quality → approves or returns with feedback → builder addresses feedback → re-submits → data steward approves → branch merged to production. Most common rejection point: promotion description review — most frequent reason: naming convention violations (non-C2DAO names) or missing data quality check confirmation. Partial credit (3 pts) for correct sequence without identifying rejection point.

SA-5. Full credit: WFF tracks — TM-40A through TM-40F (Intelligence, Fires, Movement & Maneuver, Sustainment, Protection, Mission Command); prerequisite is TM-30 (required — same prereq chain as Specialist tracks: TM-10 + TM-20 + TM-30); example: TM-40A (Intelligence WFF) or any of A–F. Specialist tracks — TM-40G through TM-40M (ORSA, AI Engineer, ML Engineer, Program Manager, Knowledge Manager, Software Engineer); prerequisite is TM-30 (REQUIRED hard prereq); example: TM-40G (ORSA) or any of G–M. NOTE: TM-50 is G–M only; advanced specialist tracks are TM-50G–M (prereq: corresponding TM-40 specialist track). Partial credit (3 pts) for correctly describing one category with correct IDs, prereq, and example.

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*TM-30 Post-Test | Version 1.1 | March 2026*
