# SELF-STUDY ADDENDUM — TM-30: ADVANCED BUILDER
## Palantir Developers External Reference Library
### Maven Smart System (MSS) — USAREUR-AF

**Status:** Optional self-study. Not taught in TM-30 class time. Use after completing the associated TM chapter.

**Source:** All videos are available on the Palantir Developers YouTube channel (@PalantirDevelopers). These are official Palantir product deep-dives that extend the TM-30 curriculum. No account is required to view.

**Scope boundary:** TM-30 is entirely UI-based — no code required. All videos listed here use Palantir's graphical tools only (Workshop, Pipeline Builder, Contour, Quiver, AIP Logic configuration UI). Videos requiring Python, TypeScript, or CLI tools are NOT listed here — those belong to TM-40G–O.

---

## Group 1 — Workshop: Scenarios and What-If Analysis (Day 1 / Ch 2 extension)

These four videos cover the Workshop Scenarios feature — what-if / sensitivity analysis using saved parameter states. Not covered in Day 1 lab blocks due to time. Highest-value optional content for trainees building decision-support dashboards.

| Video | What It Covers | Relevant TM Chapter |
|---|---|---|
| *Workshop \| Creating What If Analyses with Scenarios* | Building a scenario set in Workshop; defining parameter variables; running what-if comparisons side by side | Ch 2 — Advanced Workshop |
| *Workshop \| Saving your What If Analyses* | Saving named scenario states; sharing saved scenarios with other users; scenario library management | Ch 2 — Advanced Workshop |
| *Workshop \| Loading and Applying Scenarios* | Loading a saved scenario; applying to a live dashboard; understanding state inheritance | Ch 2 — Advanced Workshop |
| *Workshop \| How to Preload States in Foundry Workshop Applications* | Preloading default scenario states; URL-based state injection; application load behavior | Ch 2 — Advanced Workshop |

---

## Group 2 — Pipeline Builder: Scheduling and Monitoring (Day 2 / Ch 3 extension)

These videos extend the Day 2 scheduled pipeline and monitoring content. Particularly useful for trainees who will own pipelines in production after TM-30.

| Video | What It Covers | Relevant TM Chapter |
|---|---|---|
| *Foundry \| Pipeline Builder Monitoring* | Reading the build graph monitor; identifying slow or failing transforms; retry behavior | Ch 3 — Advanced Pipeline Builder |
| *Foundry \| Scheduling Pipeline Builds* | Schedule expression syntax; configuring build failure email alerts; time zone handling | Ch 3 — Advanced Pipeline Builder |
| *Foundry \| Pipeline Build History and Audit* | Viewing build history; identifying the exact transform that failed; audit trail for governance | Ch 3 — Advanced Pipeline Builder |
| *Foundry \| Understanding Build Dependencies* | Reading the dependency graph in Pipeline Builder; understanding why upstream failures cascade | Ch 3 — Advanced Pipeline Builder |
| *Foundry \| Incremental Pipeline Builds* | Incremental vs. full rebuild trade-offs; when to use each; append-mode patterns | Ch 3 — Advanced Pipeline Builder |

---

## Group 3 — Quiver: Advanced Views and Cross-Object Analysis (Day 4 / Ch 6 extension)

Quiver linked views are the most common TM-30 practical exercise No-Go. These videos cover depth topics not fully addressed in the Day 4 lab.

| Video | What It Covers | Relevant TM Chapter |
|---|---|---|
| *Quiver \| Dependency Graph Analysis* | Using the Quiver dependency graph view; tracing upstream relationships between Object Types | Ch 6 — Quiver |
| *Quiver \| Using Parameters for Dynamic Analysis* | Configuring parameter controls in Quiver; driving filter logic from user-selected values | Ch 6 — Quiver |
| *Quiver \| Ad-Hoc Aggregations* | Building on-the-fly aggregation views; combining with linked object type data | Ch 6 — Quiver |
| *Quiver \| KPI Tracking and Threshold Alerts* | Building KPI panels in Quiver; setting threshold bands; configuring alert conditions | Ch 6 — Quiver |

---

## Group 4 — Contour: Pivot Tables and Advanced Analysis (Day 4 / Ch 5 extension)

Contour pivot tables work differently from Excel. These videos supplement the Day 4 Contour lab — read/watch the pivot table video before the lab if possible.

| Video | What It Covers | Relevant TM Chapter |
|---|---|---|
| *Contour \| Building Pivot Tables* | Contour pivot table construction; row/column configuration; value aggregation options | Ch 5 — Contour |
| *Contour \| Calculated Columns and Expressions* | Expression syntax for calculated columns; referencing other columns; conditional logic in expressions | Ch 5 — Contour |
| *Contour \| Parameter Controls* | Adding parameter widgets to a Contour workbook; driving filter and aggregation behavior from user input | Ch 5 — Contour |
| *Contour \| Saving and Sharing Analysis Views* | Saving a named analysis view; publishing to stakeholders; view permissions | Ch 5 — Contour |

---

## Group 5 — DDOF and Operational Design Patterns (Ch 1 extension)

New doctrine sections added to TM-30 Chapter 1 cover foundational operational design patterns. These self-study references support the new content.

| Section | What It Covers | Relevant TM Chapter |
|---|---|---|
| 1-10a: DDOF Roles | DDOF organizational roles (Data Officer, Data Steward, Functional Manager) and their responsibilities in the Foundry environment. Understand who owns what before building. | Ch 1 — DDOF Roles |
| 1-10b: SMART Criteria | SMART criteria (Specific, Measurable, Achievable, Relevant, Time-bound) applied to data product requirements. Every builder-level product must trace to a SMART objective. | Ch 1 — SMART Criteria |
| 1-10c: Fail-Closed Design | Fail-closed design principle for data pipelines — when a pipeline encounters an error, it stops and alerts rather than passing bad data downstream. Applied throughout Blocks 2–4 (Pipeline Builder). | Ch 1 — Fail-Closed |
| 1-10d: ADC Registration | ADC (Authoritative Data Catalog) registration process for new data products. Every production dataset must be registered in the ADC before operational use. | Ch 1 — ADC Registration |
| 1-10e: DDIL Operations | Disconnected, Degraded, Intermittent, and Limited-bandwidth (DDIL) operations considerations for MSS data products. Design for delayed sync and offline caching. | Ch 1 — DDIL Operations |

---

## Group 6 — Platform Governance and Security (Day 5 / Ch 7 extension)

These two videos supplement the Day 5 governance content with practical security administration knowledge. Relevant for trainees who will act as MSS data stewards or project owners after TM-30.

| Video | What It Covers | Relevant TM Chapter |
|---|---|---|
| *Foundry \| Managing Projects for Scale* | Project structure, folder hierarchies, access inheritance for large multi-team environments | Ch 7 — Governance and C2DAO |
| *Foundry \| Debugging User Access Issues* | Step-by-step approach to diagnosing why a user cannot see expected data; access hierarchy tracing | Ch 7 — Governance and C2DAO |

---

## Usage Guidance

**Day 1 trainees** — Watch Group 1 (Workshop Scenarios) after the Day 1 evening reading. These four videos are the highest-value addition to what the lab covers.

**Day 2 trainees** — Group 2 (Pipeline scheduling and monitoring) pairs directly with the Day 2 evening reading (TM-30, Ch 3).

**Before Day 4 practical exercise** — Watch Group 3 Quiver videos. Quiver linked view configuration is the most common single-task practical exercise failure. Do not skip these before the evaluation.

**Before Day 1 reading** — Group 5 (DDOF and Operational Design Patterns) covers new Ch 1 doctrine sections. Review Sections 1-10a through 1-10e before Day 1 to understand the governance and design context for all subsequent lab work.

**Post-TM-30 sustainment** — Groups 4 and 6 are most useful after course completion when you are operating MSS data products in a unit environment.

---

## Continuation

Trainees proceeding to TM-40 tracks may access self-study addenda for those tracks, each of which contains a substantially larger Palantir Developers reference library covering code-level topics (OSDK, Python Transforms, TypeScript Functions, etc.) appropriate to specialist-level work.

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*Self-Study Addendum | TM-30 | Palantir Developers External Reference Library | March 2026*
