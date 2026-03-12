# POST-TEST — TM-40D: PROGRAM MANAGER
## Maven Smart System (MSS) — USAREUR-AF

| | |
|---|---|
| **Course** | TM-40D: Program Manager |
| **Form** | Post-Test |
| **Level** | TM-40D (Specialist) |
| **Audience** | Program managers / G8-S8 / resource managers; prerequisite: TM-10 + TM-20 |
| **Time Allowed** | 45 minutes |
| **Passing Score** | 70% (42/60) |

---

## INSTRUCTIONS

This assessment evaluates mastery of course learning objectives. A passing score of 70% is required to receive credit. Complete independently without reference to training materials.

---

## SECTION 1 — MULTIPLE CHOICE

*Circle the letter of the best answer. (2 points each)*

**1. Per TM-40D, a PM dashboard that does NOT display a data-as-of timestamp:**

A. Should be rebuilt with the timestamp added before the next scheduled brief
B. Automatically fails the PM Dashboard Standards Checklist — this is an automatic disqualifier
C. Is acceptable if the data is refreshed on a known fixed schedule that users understand
D. Requires a waiver from the data steward before it can be used for briefings

**2. Your IMS spreadsheet has a `planned_completion_date` column with values stored as text (e.g., "14 FEB 2025"). To compute milestone variance in Pipeline Builder, the FIRST step is:**

A. Create a calculated column that parses the text string manually
B. Apply a CAST step to convert the text column to a Date data type before performing the DATEDIFF calculation
C. Export the IMS to Excel, convert the dates, and re-import
D. Use the DATEDIFF function directly — Pipeline Builder automatically handles text-to-date conversion

**3. Your GFEBS obligation pipeline is designed to build a historical obligation tracking dataset. The correct write mode is:**

A. Overwrite — replace the dataset on each run with the most current snapshot
B. Append — add each new snapshot to the existing dataset to preserve history
C. Merge — combine the new snapshot with the existing data based on a matching key
D. Branch — write to a separate branch and merge quarterly

**4. After two GFEBS Append pipeline runs, you verify the dataset has only ONE snapshot record instead of TWO. The most likely cause is:**

A. The Append mode is not supported for GFEBS data sources
B. The pipeline is configured in Overwrite mode, not Append — each run replaces the previous record
C. The pipeline failed on the second run and the second snapshot was not written
D. GFEBS data exports are deduplicated automatically on ingest

**5. A PM Dashboard Standards Checklist item requires that the dashboard display a reference line in the Quiver obligation chart showing the quarterly target obligation rate. For Q2 (midpoint of the fiscal year), this reference line should be placed at:**

A. 25% — Q1 target
B. 50% — midpoint target for two completed quarters
C. 75% — aggressive spend target
D. 100% — full-year target for comparison

**6. In a Contour portfolio health matrix showing 12 programs, the matrix should be sorted by `overall_status` in which order to surface the highest-priority programs first?**

A. Descending — GREEN programs listed first
B. Ascending — RED programs listed first (RED sorts lower alphabetically than GREEN)
C. By program name alphabetically — commanders know the programs by name
D. By milestone variance in descending order

**7. You are building a Pipeline Builder pipeline that ingests an IMS spreadsheet and computes RAG status for each milestone. A milestone is RED if it is more than 14 days late, AMBER if 1–14 days late, and GREEN if on time or early. The correct Pipeline Builder step to implement this logic is:**

A. Filter rows step with three separate pipelines, one for each status
B. A calculated column step using a conditional expression (CASE/IF-THEN-ELSE) on the variance field
C. A join step that maps the variance range to a status lookup table
D. A Group By step that aggregates milestones by their variance buckets

**8. The scheduled pipeline refresh for a PM dashboard is configured to run daily at 0500. The email alert recipient should be:**

A. The data steward, who will notify the PM if there is a failure
B. The PM or a designated data point of contact who can investigate and resolve failures before the daily battle rhythm
C. All dashboard viewers, so they know when data is current
D. The MSS program office, who manages all scheduled pipeline failures

**9. Per the PM Dashboard Standards Checklist, which of the following is required to appear on the IPR product exported from MSS?**

A. A digital signature from the PM and data steward
B. The data-as-of timestamp, program name, classification marking, and all required status indicators (schedule, cost, performance)
C. A comparison chart showing current status vs. prior quarter
D. A footnote listing all data sources feeding the dashboard

**10. Your portfolio health matrix in Contour shows a program with GREEN schedule status but RED cost status. The `overall_status` computed column should reflect:**

A. GREEN — schedule is the primary indicator for IPR purposes
B. An average of the two scores
C. RED — the worst individual indicator determines the composite health
D. AMBER — mixed status defaults to the middle value

**11. A resource manager asks why two consecutive GFEBS obligation snapshots show identical obligation totals, even though obligations were made in the intervening period. The FIRST check is:**

A. Whether the GFEBS export file contains the new obligations
B. Whether the pipeline is running in Append mode or Overwrite mode
C. Whether the obligation pipeline has a filter excluding recently created obligations
D. Whether the GFEBS system had a data entry delay for the new obligations

**12. The `data_as_of` field in a PM dashboard dataset should be populated with:**

A. The current date when the user opens the dashboard
B. The timestamp of the pipeline run that produced the data — not the current date
C. The date the original source data was exported from GFEBS
D. The date the data steward last approved the dataset for use

**13. A Quiver visualization for budget execution should display obligation amounts by quarter with a reference line showing the expected quarterly obligation rate. This reference line is best described as:**

A. A filter control that allows the user to select different target rates
B. A static reference annotation showing the expected obligation rate at each quarter, enabling visual comparison to actual
C. A calculated column in the underlying dataset
D. A Workshop variable passed to the Quiver configuration

**14. Per TM-40D, which of the following is NOT a required element of the program data architecture you design in Foundry?**

A. Program Object Type
B. Milestone Object Type
C. Resource/Obligation Object Type
D. Personnel Assignment Object Type

**15. A PM presents a commander's brief based on a dashboard. After the brief, the commander's aide notes that the dashboard data was last refreshed 11 days ago. Per TM-40D PM Dashboard Standards, what should the PM have done?**

A. Refreshed the pipeline manually immediately before the brief
B. Prominently displayed the data-as-of timestamp during the brief and explicitly stated the data currency to the commander before presenting status conclusions
C. Cancelled the brief and rescheduled it when current data was available
D. Added a verbal disclaimer at the end of the brief noting potential data staleness

---

## SECTION 2 — SHORT ANSWER

*Answer in 2–5 sentences. (6 points each)*

**SA-1. Describe the complete Pipeline Builder pipeline you would build to ingest a weekly IMS spreadsheet and compute RAG milestone status. List the specific pipeline steps in order, including the CAST step for date fields, the DATEDIFF calculation, and the conditional RAG column logic.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-2. Your GFEBS obligation pipeline has been running in Append mode for six months. The data steward asks how you would verify that the historical tracking is working correctly. Describe your verification steps.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-3. Design the Workshop PM dashboard for an IPR brief. List the required widgets (table, metrics, charts, timestamp) and describe what data each displays. Explain how conditional formatting is applied to the milestone status table.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-4. The G8 resource manager asks you to build a portfolio health matrix in Contour showing all 14 active programs sorted to surface the highest-priority programs first. Describe the data structure required, the `overall_status` computation logic, and the Contour sort configuration.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-5. You are presenting an IPR product exported from MSS to a GO. Walk through the PM Dashboard Standards Checklist: list at least six items that must be verified before the product is presented, and identify which single item is an automatic failure if absent.**

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
1. B — Missing data-as-of timestamp = automatic checklist failure per TM-40D standards.
2. B — CAST step to Date type is required before DATEDIFF calculation.
3. B — GFEBS historical tracking requires Append mode, not Overwrite.
4. B — Overwrite mode on a pipeline that should be Append is the most common cause of single-snapshot datasets.
5. B — Q2 reference line = 50% (midpoint of fiscal year, two quarters complete).
6. B — Ascending sort surfaces RED programs first (RED < AMBER < GREEN alphabetically).
7. B — Calculated column with CASE/IF-THEN-ELSE conditional expression on the variance field.
8. B — PM or designated data POC receives the failure alert for timely resolution.
9. B — Data-as-of timestamp, program name, classification marking, and required status indicators.
10. C — Worst individual indicator (RED cost) determines composite health = RED.
11. A — First check: does the GFEBS export file contain the new obligations (source before pipeline).
12. B — Data-as-of = pipeline run timestamp, not current date or steward approval date.
13. B — Reference line = static annotation for visual comparison to actual obligation amounts.
14. D — Personnel Assignment Object Type is not a required element of the TM-40D PM data architecture.
15. B — PM must display data-as-of timestamp and explicitly state data currency before presenting conclusions.

**Short Answer Guidance:**

SA-1. Full credit: (1) Ingest IMS CSV; (2) rename columns for C2DAO compliance; (3) CAST `planned_date` and `actual_date` from text to Date type; (4) calculated column: `variance_days = DATEDIFF(actual_date, planned_date)` (or forecast date if actual is null); (5) calculated column: `rag_status = CASE WHEN variance_days > 14 THEN 'RED' WHEN variance_days >= 1 THEN 'AMBER' ELSE 'GREEN' END`; (6) filter step to remove header rows or invalid records; (7) Ontology write step. Must include CAST step and conditional CASE logic for full credit.

SA-2. Full credit: query the output dataset and count distinct snapshot_date values — should equal number of pipeline runs; verify earliest snapshot date matches first pipeline run date; verify latest snapshot reflects most recent GFEBS export; sum obligations by snapshot_date and confirm each period shows incremental growth consistent with known obligation activity; if only one snapshot exists, check pipeline write mode — likely configured as Overwrite.

SA-3. Full credit: required widgets — (1) data-as-of timestamp widget (displayed prominently, not in footer); (2) milestone status table with planned_date, actual_date, variance_days, rag_status columns; (3) obligation rate metric widget (% of budget obligated); (4) bar chart of milestones by status (RED/AMBER/GREEN count); (5) Quiver or line chart of obligation trend over time; conditional formatting: rag_status = RED → row background red, AMBER → amber/yellow, GREEN → green. All five widgets plus conditional formatting required for full credit.

SA-4. Full credit: data structure — programs table with columns for schedule_status, cost_status, performance_status, and overall_status; computed column: `overall_status = CASE WHEN MIN(schedule_status, cost_status, performance_status) = 'RED' THEN 'RED' WHEN MIN(...) = 'AMBER' THEN 'AMBER' ELSE 'GREEN' END` (or equivalent worst-of logic); Contour sort: configure the matrix to sort by `overall_status` ascending — this places RED programs first; secondary sort by cost_status or variance_days to rank within each status tier.

SA-5. Full credit: six required checklist items — (1) data-as-of timestamp visible on product [AUTOMATIC FAILURE if absent]; (2) program name and classification marking present; (3) all required status indicators present (schedule, cost, performance RAG); (4) milestone table shows planned date, actual/forecast date, and variance in days; (5) obligation chart includes Q2 reference line at 50%; (6) portfolio sort surfaces RED programs first; (7) pipeline last-run confirmed within acceptable currency window; (8) all data sources feeding the dashboard refreshed. Automatic failure item: data-as-of timestamp absent. Partial credit (3 pts) for five or more items without identifying the automatic failure.

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*TM-40D Post-Test | Version 1.0 | March 2026*
