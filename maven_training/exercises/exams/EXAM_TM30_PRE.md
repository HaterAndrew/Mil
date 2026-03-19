# PRE-TEST — TM-30: ADVANCED BUILDER
## Maven Smart System (MSS) — USAREUR-AF

| Field | Detail |
|---|---|
| **Course** | TM-30: Advanced Builder |
| **Form** | Pre-Test |
| **Level** | TM-30 (Advanced) |
| **Audience** | Data-adjacent specialists — 17/25-series, S6/G6/G2; prerequisite: TM-10 + TM-20 |
| **Time Allowed** | 30 minutes |
| **Passing Score** | N/A — diagnostic only |

---

## INSTRUCTIONS

This diagnostic assessment establishes your baseline knowledge before training. Your score does not affect course eligibility. Answer honestly — results help the instructor tailor instruction to gaps.

---

## SECTION 1 — MULTIPLE CHOICE

*Circle the letter of the best answer. (2 points each)*

**1. In data modeling, a "schema design" process involves:**

A. Selecting the color scheme and layout of a dashboard
B. Writing SQL queries to extract data from a production database
C. Defining the entities, attributes, relationships, and constraints that structure a data system
D. Configuring user access roles for a new data project

**2. A "many-to-many" relationship between two entities in a data model is typically implemented using:**

A. A single foreign key column on one of the two tables
B. A junction (bridge) table containing foreign keys to both entities
C. A recursive self-join on the larger of the two tables
D. A view that calculates the relationship on query

**3. In a multi-table JOIN operation, a "fan-out" problem occurs when:**

A. Two tables share the same primary key, causing a conflict
B. The query joins more than three tables, exceeding the platform's limit
C. A join condition references a column with nulls
D. A one-to-many join causes duplicate rows in aggregated results, inflating counts or sums

**4. A GROUP BY aggregation in a data pipeline is used to:**

A. Calculate summary metrics (count, sum, average) for each unique value of a grouping column
B. Sort records alphabetically by a specified column
C. Filter records to a specific subset of rows
D. Join two datasets on a common field

**5. "Conditional logic" in a UI framework (showing or hiding elements based on a variable) is closest to which programming concept?**

A. A loop
B. A function definition
C. An if-then-else statement
D. A recursive call

**6. An "APPEND" write mode in a pipeline differs from an "OVERWRITE" mode in that:**

A. Append deletes all existing records before writing new ones
B. Append adds new records to existing data, preserving historical records
C. Append validates records against the schema before writing
D. Append is used only for Object Type writes, not datasets

**7. A "parameter control" in a data visualization tool allows:**

A. The pipeline to dynamically adjust its schedule
B. The user to input a value that filters or adjusts the displayed analysis interactively
C. The system administrator to lock specific columns from editing
D. The visualization to update based on a scheduled refresh

**8. "Data governance" in the context of promotion workflows refers to:**

A. The review and approval process ensuring changes meet quality and policy standards before reaching production
B. The encryption standard applied to data in transit
C. The automated validation checks run during pipeline execution
D. The role-based permissions assigned to each user in the project

**9. A scheduled pipeline that runs at 0600 daily and sends an email alert on failure is an example of:**

A. Reactive pipeline management
B. On-demand pipeline execution
C. Manual pipeline orchestration
D. Proactive automated monitoring with alerting

**10. In a multi-page application, "URL deep linking" allows:**

A. The application to load faster by caching page state
B. Users to bookmark the application's login page
C. A specific application page and its filter state to be shared via a URL so the recipient lands directly in the correct view
D. The system to track which pages each user visits for audit purposes

**11. A "union" operation requires that:**

A. Both datasets have compatible column schemas (same names and types)
B. Both datasets share at least one common column for a join key
C. One dataset is a subset of the other
D. The datasets originate from the same source system

**12. In an Ontology schema design, an "Object Type" should represent:**

A. Any table that exists in the source data system
B. A meaningful real-world entity relevant to the operational mission
C. Each column of a dataset that will be displayed in a dashboard
D. A pipeline step that writes data to the Ontology

**13. Which of the following is a valid concern when designing an Ontology schema?**

A. Whether the proposed Object Types model the actual mission relationships or simply mirror source table structure
B. Whether the entity has enough rows to justify an Object Type
C. Whether the data was collected within the last 30 days
D. Whether each Object Type has at least five properties

**14. In the context of data pipeline scheduling, an "email alert on build failure" is most directly useful for:**

A. Informing end users that the dashboard data is stale
B. Preventing users from accessing the dashboard when data is not current
C. Documenting pipeline failures in the audit log
D. Notifying the pipeline owner immediately when automated data refresh fails so the issue can be resolved

**15. When passing variables between pages in a multi-page application, the purpose is to:**

A. Share access credentials between application pages
B. Synchronize the data refresh schedule across pages
C. Carry context (such as a selected unit or date range) from one page to another without requiring the user to re-enter it
D. Limit each page's access to a specific dataset

---

## SECTION 2 — SHORT ANSWER

*Answer in 2–5 sentences. (6 points each)*

**SA-1. Describe the fan-out problem in a multi-table join and explain how you would diagnose whether your pipeline is producing inflated aggregated values due to fan-out.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-2. An S2 section needs an Ontology schema that tracks intelligence reports, sources, and the geographic areas those sources cover. Sketch (in words) a simple schema: identify the Object Types, the key properties for each, and the Link Types connecting them.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-3. Explain the difference between "Append" and "Overwrite" pipeline write modes. Describe a scenario in which using Overwrite when you intended Append would cause an operational data problem.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-4. Describe what a "promotion workflow" is in a data platform context, and explain why bypassing the review step would be a risk in an operational environment.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-5. You are designing a Workshop application for a Civil Affairs CIMIC section that needs to view the same data but filtered differently depending on whether the user is a battalion S9 or a brigade Civil Affairs section. Describe at least two design approaches to handle this access differentiation.**

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

Passing: N/A — Pre-test is diagnostic only.

---

## ANSWER KEY — INSTRUCTOR USE ONLY

*Do not distribute to students.*

**Multiple Choice:**
1. C — Schema design defines entities, attributes, relationships, and constraints.
2. B — Many-to-many relationships use a junction/bridge table with foreign keys to both entities.
3. D — Fan-out: a one-to-many join duplicates rows, inflating aggregated totals.
4. A — GROUP BY calculates summary metrics per unique grouping value.
5. C — Conditional show/hide logic is equivalent to an if-then-else statement.
6. B — Append adds to existing data; Overwrite deletes and replaces.
7. B — Parameter control allows interactive user input that adjusts the analysis.
8. A — Governance in promotion context = review/approval before reaching production.
9. D — Proactive automated monitoring with alerting; not reactive (which waits for user discovery).
10. C — URL deep linking encodes page state in the URL for direct navigation sharing.
11. A — Union requires compatible schemas; join requires a common key.
12. B — Object Types should represent meaningful mission-relevant real-world entities.
13. A — Schema design should model actual operational relationships, not just mirror source tables.
14. D — Email alert on failure enables immediate owner notification for rapid resolution.
15. C — Variable passing carries context between pages so users don't re-enter filters.

**Short Answer Guidance:**

SA-1. Full credit: fan-out occurs when a 1:M join multiplies rows from the "1" side, causing SUM/COUNT aggregations to count the same value multiple times; diagnose by comparing aggregated totals against known correct values, or by checking the row count before and after the join. Partial credit (3 pts) for correct explanation without a diagnostic method.

SA-2. Full credit: Object Types — IntelligenceReport (properties: report_id, classification, date, summary), Source (source_id, name, type, reliability_rating), GeographicArea (area_id, name, grid_ref); Link Types — Report-to-Source (which source produced which report), Source-to-Area (which areas a source covers), Report-to-Area (which areas a report references). Partial credit (3 pts) for two of three Object Types with reasonable properties and at least one Link Type.

SA-3. Full credit: Overwrite deletes all existing records and writes the new dataset; Append adds records to existing data. Scenario: a daily SITREP pipeline runs in Overwrite mode instead of Append — seven days of historical SITREPs are deleted every morning, leaving only the most recent day's data; historical trend analysis becomes impossible. Partial credit (3 pts) for correct definition of both modes without a concrete operational scenario.

SA-4. Full credit: promotion workflow is a change-management review process where a data steward or approver reviews all pipeline/application changes on a branch before they are merged to the production environment; bypassing this step risks deploying broken pipelines, incorrect data transformations, or unauthorized data access changes directly to operational users. Partial credit (3 pts) for correct definition without risk explanation.

SA-5. Full credit: two from — (1) role-based Workshop variable — use a variable that reads the user's assigned role and applies a pre-filter to all widgets accordingly; (2) separate Workshop applications for each audience with different default filters and visibility configurations; (3) row-level filtering via the user's unit attribute read from their profile, restricting visible rows in all tables; (4) using conditional show/hide on widgets based on role variable. Partial credit (3 pts) for one valid approach with explanation.

---

*USAREUR-AF Operational Data Team*
*TM-30 Pre-Test | Version 1.0 | March 2026*
