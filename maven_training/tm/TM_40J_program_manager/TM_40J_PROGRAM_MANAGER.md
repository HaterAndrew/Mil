# TM-40J — MAVEN SMART SYSTEM (MSS)
## PROGRAM MANAGER (TECHNICAL) TECHNICAL MANUAL

**HEADQUARTERS, UNITED STATES ARMY EUROPE AND AFRICA**
Wiesbaden, Germany

2026

**Version 1.0 | March 2026**

**PREREQUISITE PUBLICATIONS:** TM-10, Maven User; TM-20, Builder; TM-30, Advanced Builder (required); Data Literacy Technical Reference (required).
**APPLIES TO:** Technical Project Managers, Product Owners, Team Leads managing data/AI/software capability builds on MSS. Civilian tech PMs, officer/NCO project leads, ORSA/MLE/SWE/KM team leads.
**DISTRIBUTION RESTRICTION:** Approved for public release; distribution is unlimited.

---

## SAFETY SUMMARY

Technical PMs managing MSS projects make decisions that affect production data environments, live
dashboards, and AI-driven tools that operational users depend on. An incorrect release, a broken
model, or a misconfigured access control is not an IT inconvenience — it degrades the operational
picture for USAREUR-AF formations in the AOR.

Before performing any task at TM-40J level:

- Do not promote a data product to production without completing the Definition of Done checklist
  (Appendix B). Partial releases create false confidence in downstream consumers.
- Do not grant Foundry project access outside the least-privilege model. Data products built on MSS
  may contain operationally sensitive ontology objects. Coordinate access decisions with the
  USAREUR-AF C2DAO.
- Do not scope-creep a data/AI project into production ML without involving TM-40C (ML Engineer)
  and TM-40B (AI Engineer) resources. Deploying an untested model as a "quick prototype" is a
  data quality risk that can corrupt downstream operational products.
- Never schedule an automated pipeline to overwrite production data without a rollback path. Define
  the rollback procedure before the deployment window opens.
- When deploying a new capability to operational users, communicate the change 48 hours in advance
  to unit data points of contact. Silent deployments that change workflows cause user resistance
  and loss of trust in the platform.

> **WARNING:** MSS data products built under TM-40J oversight directly support commander decision
> making at the theater level. A PM who approves a defective release, ships a dashboard with
> incorrect business logic, or fails to validate model outputs before production is accountable
> for the downstream operational impact. Apply a mission brief standard to every release decision:
> confirm, coordinate, communicate before execution.

---

## TABLE OF CONTENTS

- Chapter 1 — Introduction: The Technical PM Role
- Chapter 2 — Agile Project Management for Data and AI Projects
- Chapter 3 — Managing ML and AI Project Lifecycles
- Chapter 4 — Stakeholder Management and Requirements Translation
- Chapter 5 — Building Project Tracking Systems on MSS
- Chapter 6 — Risk and Dependency Management
- Chapter 7 — Delivery Planning and Production Readiness
- Chapter 8 — Change Management and User Adoption
- Appendix A — Project Kickoff Checklist
- Appendix B — Definition of Done — Data Product Standards
- Glossary

---

# CHAPTER 1 — INTRODUCTION: THE TECHNICAL PM ROLE

## 1-1. Purpose and Scope

**BLUF:** TM-40J qualifies Technical Project Managers, Product Owners, and Team Leads to plan,
execute, and govern data, AI, and software capability builds on the Maven Smart System (MSS).
This track bridges technical execution (TM-40A through TM-40F developers) and operational
requirements (commanders, staff, end users).

This manual provides task-level instruction for managing the full lifecycle of a data or AI
project on MSS — from initial stakeholder requirements through sprint planning, execution, release,
and sustainment. TM-40J graduates serve as the connective tissue between technical build teams
and the operational units they support.

**TM-40J covers:**

- Agile project management methods adapted for data and AI projects in a military operational
  context
- Backlog management: writing user stories and acceptance criteria for data products and dashboards
- Managing ML and AI project lifecycles from research through production and sustainment
- Translating operational requirements from commanders and staff into actionable technical tasks
- Building live project tracking systems on MSS using Workshop, Ontology, and Pipeline Builder
- Risk and dependency management specific to data availability, model performance, and technical debt
- Delivery planning: scope, timeline, and quality tradeoffs for data product releases
- Coordinating across technical tracks: when to pull in TM-40A (AI Engineer), TM-40B (Software
  Engineer), TM-40C (ML Engineer), TM-40E (Knowledge Manager), and TM-40F (SWE)
- Change management: deploying new MSS capabilities to operational users who resist change
- Platform governance from a PM perspective: Foundry project permissions, resource allocation,
  and access stewardship

**TM-40J does NOT cover:**

- Raw coding of Foundry transforms, Functions on Objects, or API integrations — see TM-40F
- Machine learning model development and validation — see TM-40C (ML Engineer)
- AI agent and workflow automation build — see TM-40B (AI Engineer)
- Advanced statistical analysis and modeling — see TM-40A (ORSA)
- Knowledge management architecture and data dictionary design — see TM-40E (KM)

> **NOTE:** TM-40J is a management and coordination track. The PM does not need to write code.
> The PM must understand enough about each technical discipline to write accurate user stories,
> identify blockers, assess risk, and make scope tradeoff decisions. Technical depth comes from
> the TM-40 specialists the PM leads.

---

## 1-2. The Technical PM in the MSS Ecosystem

USAREUR-AF data and AI capability builds operate at speed. Theater requirements generate demands
for new dashboards, new data pipelines, new AI-assisted tools, and new integrations faster than
any single developer can absorb. Technical PMs manage the backlog, prioritize the work, protect
the team from scope sprawl, and ensure that what ships is operationally sound.

The MSS ecosystem involves multiple technical disciplines that must be coordinated:

| Track  | Role                          | What They Build                                              |
|--------|-------------------------------|--------------------------------------------------------------|
| TM-40A | ORSA                          | Quantitative models, statistical analysis, analytical products |
| TM-40B | AI Engineer                   | AI agents, AIP Logic, automated workflows, LLM integrations  |
| TM-40C | ML Engineer                   | ML models, training pipelines, model evaluation and deployment |
| TM-40J | Program Manager (Technical)   | Project tracking, stakeholder mgmt, delivery coordination    |
| TM-40E | Knowledge Manager             | Data dictionaries, ontology governance, data stewardship     |
| TM-40F | Software Engineer             | Custom Foundry code, Functions, API integrations, services   |

The PM does not manage people's performance in the HR sense. The PM manages scope, timeline,
risk, and stakeholder communication. The PM shields the technical team from requirements churn
and ensures the team delivers the right thing to the right standard at the right time.

---

## 1-3. Prerequisites and Entry Standards

### Conditions

Personnel seeking TM-40J qualification have completed TM-30 (Advanced Builder) and can operate
MSS at the advanced no-code level. They are assigned or designated as a project lead, product
owner, or team lead for a data or AI capability build.

### Standards

Upon completion of TM-40J, the Technical PM can:

1. Stand up an Agile project structure (backlog, sprint cadence, ceremonies) for a data/AI project
2. Write user stories and acceptance criteria that TM-40A through TM-40F developers can execute
   without ambiguity
3. Manage an ML/AI project from research brief through production release using the MSS lifecycle
   model
4. Translate a commander or staff requirement into a structured requirements document and prioritized
   backlog
5. Build a live project tracking dashboard on MSS Workshop visible to all project stakeholders
6. Identify and track top five project risks and dependency blockers at any point in the project
7. Conduct a production readiness review against the Definition of Done (Appendix B)
8. Execute a change management plan for a new MSS capability deployment to operational users

### Equipment

- MSS account with Builder access (TM-30 level)
- Foundry Workshop, Pipeline Builder, and Ontology UI access
- Access to the USAREUR-AF C2DAO project space for coordination
- Connectivity to project communication channels (Teams, SharePoint, or MSS-hosted)

---

## 1-4. TM-40J in the Curriculum Architecture

TM-40J sits at the top of the no-code track and the entry point of the management track.

```
TM-10 (User) → TM-20 (Builder) → TM-30 (Advanced Builder) → TM-40J (Technical PM)
                                                           ↘ TM-40A (ORSA)
                                                           ↘ TM-40B (AI Engineer)
                                                           ↘ TM-40C (ML Engineer)
                                                           ↘ TM-40E (KM)
                                                           ↘ TM-40F (SWE)
```

The PM must have completed TM-30 to understand what each specialist track builds and why decisions
have technical consequences. A PM who has never built on MSS cannot accurately estimate effort,
identify blockers, or write meaningful acceptance criteria for MSS-based deliverables.

---

# CHAPTER 2 — AGILE PROJECT MANAGEMENT FOR DATA AND AI PROJECTS

## 2-1. Why Agile for Data Projects

**BLUF:** Traditional waterfall project management fails for data and AI projects because
requirements evolve as the data is understood. Agile methods — particularly Scrum and Kanban —
accommodate the iterative, discovery-driven nature of data work.

Data and AI projects have characteristics that make fixed-scope, fixed-timeline planning
unreliable:

- **Data availability is unknown until the data is examined.** A pipeline that looks straightforward
  may hit schema changes, missing records, or access barriers that were not visible during scoping.
- **Model performance is uncertain.** An ML model may require three iterations to reach acceptable
  accuracy. The PM cannot know the final timeline until the data is cleaned, features are
  engineered, and baselines are established.
- **Operational requirements change.** Commanders get new missions. Staff priorities shift. A
  dashboard built for one reporting cycle may need to change format before the next cycle.
- **Technical dependencies are interdependent.** A data pipeline feeds a model that feeds a
  dashboard. A block at any layer propagates up. Fixed waterfall schedules cannot absorb these
  cascading delays without scope cuts or deadline slips.

Agile methods address these realities by delivering value in short increments (sprints), surfacing
blockers early (daily standups), and recalibrating scope and priorities based on what the team
learns each sprint.

> **NOTE:** Agile does not mean undisciplined. It means structured iteration with explicit
> decisions about scope and priority at each cycle boundary. The PM is responsible for that
> discipline. Undisciplined "agile" is just disorganized waterfall.

---

## 2-2. Scrum Framework for MSS Projects

### Conditions

The PM is standing up a new data or AI project on MSS with a team of two to eight personnel
across TM-40 tracks.

### Standards

The PM establishes a Scrum structure that includes: defined roles (PM as Scrum Master/Product
Owner), a groomed product backlog, a sprint cadence (one or two weeks), and the four core
ceremonies (sprint planning, daily standup, sprint review, retrospective).

### Procedure — Standing Up a Scrum Project

1. **Define the product.** Write a one-paragraph product vision statement: what the product does,
   who uses it, and what operational outcome it enables. Post this in the project space. All
   backlog prioritization decisions reference this statement.

2. **Identify team members and tracks.** List each team member and their TM-40 track. Clarify
   who contributes to what layer of the product (data pipeline, model, dashboard, API).

3. **Set sprint length.** Recommend: two-week sprints for projects with six or more team members
   or complex ML components. One-week sprints for small teams or dashboard-only projects requiring
   rapid stakeholder feedback.

4. **Establish sprint cadence calendar.** Block recurring times for:
   - Sprint Planning: first day of sprint, 60-90 minutes
   - Daily Standup: every working day, 15 minutes (async acceptable if team is distributed)
   - Sprint Review: last day of sprint, 30-45 minutes with stakeholder attendance
   - Retrospective: last day of sprint, 30 minutes (team only)

5. **Build the initial product backlog.** See task 2-3 for user story format. Initial backlog
   should contain enough stories to fill two to three sprints before the first sprint starts.

6. **Define the sprint goal format.** Each sprint has one sentence stating what the team will
   demonstrate at the sprint review. Example: "At the end of this sprint, stakeholders can view
   live equipment readiness by unit on the Workshop dashboard."

7. **Create the project tracking workspace on MSS.** See Chapter 5 for build instructions.
   The Scrum board must be live on MSS before sprint 1 begins — not in a spreadsheet.

> **CAUTION:** Do not run sprints without a defined sprint goal. Teams without a sprint goal
> default to ticket-grinding with no coherent output for the stakeholder review. The sprint goal
> is the PM's tool for maintaining delivery focus.

---

## 2-3. Backlog Management and User Stories

### 2-3a. User Story Format

User stories for data products follow the standard Agile format adapted for operational context:

```
AS A [type of user — commander, analyst, logistics officer, data engineer]
I WANT [a specific capability or information need]
SO THAT [the operational or analytical outcome it enables]
```

**Examples — good user stories for MSS data products:**

| Story                                                                                                                | Track Owner | Size  |
|----------------------------------------------------------------------------------------------------------------------|-------------|-------|
| As a G4 officer, I want a live equipment readiness dashboard filtered by subordinate unit so that I can identify maintenance bottlenecks before the morning update. | TM-40F / TM-30 | M     |
| As a data scientist, I want a cleaned and deduplicated personnel roster dataset refreshed daily so that my models have current input data. | TM-40F      | S     |
| As a G2 analyst, I want the anomaly detection model to flag records scoring above 0.85 probability with an explanation of contributing features so that I can triage alerts without reviewing all raw data. | TM-40C      | L     |
| As a battalion S6, I want a Workshop form that submits equipment status updates directly to the MSS ontology so that I no longer re-key data from paper forms. | TM-40F / TM-30 | M     |

**Bad user story patterns to reject:**

- "Build the data pipeline." (No user, no outcome — this is a task, not a story)
- "Improve model performance." (No specific acceptance criteria — unmeasurable)
- "Fix the dashboard." (No description of what is broken or what done looks like)

### 2-3b. Acceptance Criteria

Every user story requires explicit acceptance criteria (AC). AC are the conditions the PM uses
to determine whether a story is complete. Write AC as testable statements.

**Format:**

```
GIVEN [the system state or precondition]
WHEN [the user takes a specific action]
THEN [the expected result that confirms the story is done]
```

**Example — acceptance criteria for the G4 readiness dashboard story:**

```
GIVEN I am logged into MSS Workshop with G4 role
WHEN I open the Equipment Readiness Dashboard
THEN I see a filterable table of readiness rates by subordinate unit, updated within the last
24 hours, with drill-down to individual equipment records
AND records with readiness below 70% are flagged in red
AND I can export the current view to PDF without requesting developer assistance
```

> **NOTE:** The PM writes acceptance criteria in collaboration with the stakeholder — not in
> isolation. AC written without stakeholder input often miss the actual operational requirement.
> Always walk the stakeholder through the AC before the story enters the sprint.

### 2-3c. Story Sizing and Velocity

Size stories using T-shirt sizing (S/M/L/XL) or story points (Fibonacci: 1/2/3/5/8/13).
For MSS projects, T-shirt sizing is recommended for teams new to Agile:

| Size | Description                                                                 | Typical Duration     |
|------|-----------------------------------------------------------------------------|----------------------|
| S    | Single-layer change: one dataset, one Workshop widget, one configuration    | <1 day               |
| M    | Two-layer change: pipeline + dashboard, or model update + evaluation        | 1-3 days             |
| L    | Multi-layer: new ontology type + pipeline + dashboard + access control      | 3-7 days             |
| XL   | New capability end-to-end: new data source, model, product, governance      | >1 sprint — decompose |

> **CAUTION:** Stories sized XL should be decomposed before entering the sprint. An undecomposed
> XL story in a sprint almost always carries over unfinished. Decompose into L or M stories with
> their own acceptance criteria.

**Velocity:** Track how many story points or T-shirt sizes the team completes each sprint.
After three sprints, use average velocity to forecast delivery dates. Do not commit to external
stakeholder deadlines based on sprint 1 velocity alone — it takes three to four sprints for a
team to establish a reliable throughput baseline.

---

## 2-4. Kanban for Operational Support Work

Kanban is appropriate for MSS teams performing ongoing support and enhancement work rather than
building a defined new product. Use Kanban when:

- The team is in sustainment mode for a production product
- Work arrives continuously from multiple stakeholders at unpredictable rates
- There is no defined end state or launch date

### Kanban Board Structure for MSS Support Teams

| Column         | Definition                                                                         |
|----------------|------------------------------------------------------------------------------------|
| Backlog        | All requested work, unscheduled                                                    |
| Ready          | Groomed, sized, assigned, has acceptance criteria — ready to start                |
| In Progress    | Actively being worked — WIP limit: 2 per developer                                |
| In Review      | Built, pending PM or peer review before promoting to production                    |
| Done           | Accepted by stakeholder and promoted to production (or closed as won't do)        |

**WIP Limits.** Work-in-progress (WIP) limits are the single most important Kanban discipline.
A developer with five items In Progress finishes nothing. WIP limit of two per developer forces
completion before starting new work. Enforce WIP limits. Resist requests to bypass them.

---

## 2-5. Sprint Ceremonies — Execution Standards

### 2-5a. Sprint Planning

**Duration:** 60 minutes for a one-week sprint; 90 minutes for a two-week sprint.

**Procedure:**

1. PM presents the sprint goal (one sentence).
2. PM walks the top backlog items in priority order. Team asks clarifying questions.
3. Each team member pulls stories they are committing to deliver by sprint end.
4. Team confirms: does the sum of committed stories match the sprint goal?
5. PM records the committed sprint scope in the MSS tracking board (Chapter 5).
6. Close: team and PM confirm the sprint start date, standup time, and review date.

> **NOTE:** Sprint planning is not a negotiation session. The PM holds final authority on
> priority order. Developers hold final authority on technical feasibility within the sprint.
> If a developer says a story cannot be completed in the sprint as scoped, the PM either
> rescopes the story or moves it to the next sprint. Do not override developer effort estimates.

### 2-5b. Daily Standup

**Duration:** 15 minutes. Timebox strictly.

**Format:** Each team member answers three questions:
1. What did I complete since last standup?
2. What will I complete before next standup?
3. What is blocking me?

The PM records blockers in the risk/dependency tracker (Chapter 6). The standup is not a status
meeting for the PM — it is a synchronization mechanism for the team. Take problem-solving
offline. Do not let standup run over 15 minutes regardless of how many blockers surface.

### 2-5c. Sprint Review

**Duration:** 30-45 minutes. Stakeholders attend.

**Procedure:**

1. PM presents the sprint goal and whether it was achieved.
2. Each developer demonstrates what they built — live in MSS, not PowerPoint slides.
3. Stakeholders provide direct feedback.
4. PM notes any stories not completed and explains whether they carry forward or are rescoped.
5. PM presents the updated product roadmap showing projected delivery for remaining features.

> **WARNING:** Do not demo a feature that is not deployed to the review environment. Demoing
> locally and saying "it will work the same way in production" is a PM failure mode. The
> sprint review demo must use the actual deployed product.

### 2-5d. Retrospective

**Duration:** 30 minutes. Team only — no stakeholders.

**Format:** Three questions, time-boxed discussion, one to two action items maximum:

1. What went well this sprint? (Keep doing)
2. What did not go well? (Stop doing or change)
3. What will we try differently next sprint? (One to two specific, ownable changes)

The PM owns tracking retrospective action items. If a retro action item is not tracked and
followed up, retrospectives become a venting session with no effect on team performance.

---

# CHAPTER 3 — MANAGING ML AND AI PROJECT LIFECYCLES

## 3-1. The ML/AI Project Lifecycle

**BLUF:** ML and AI projects do not follow the same lifecycle as dashboard or pipeline builds.
They have a research-to-production funnel that the PM must manage explicitly. Most ML projects
fail not because the model is bad — they fail because the PM did not manage the funnel correctly.

The MSS ML/AI lifecycle has six phases:

```
[1] PROBLEM DEFINITION → [2] DATA AUDIT → [3] PROTOTYPE → [4] EVALUATION → [5] PRODUCTION → [6] SUSTAINMENT
```

Each phase has a PM gate — a decision point where the PM reviews outputs and decides whether to
proceed, iterate, or stop.

---

## 3-2. Phase 1 — Problem Definition

### Conditions

The PM has received a stakeholder requirement for an AI or ML capability and must determine
whether it is technically feasible and operationally scoped correctly before committing
development resources.

### Standards

The PM produces a one-page Problem Definition document containing: the operational question
the model must answer, the input data sources, the output format, the success metric, and the
recommended TM-40 tracks to assign.

### Procedure

1. **State the operational question precisely.** "Use AI to help G2" is not a problem definition.
   "Predict which equipment records are most likely to require unscheduled maintenance in the
   next 30 days, ranked by probability, so the G4 can pre-position maintenance teams" is a
   problem definition.

2. **Identify the input data.** What datasets does the model need? Where do they live on MSS?
   What is the refresh rate? Who owns them? Pull in TM-40E (KM) to validate data availability
   and quality before committing to a model approach.

3. **Define the output format.** A ranked list? A probability score per record? A binary
   flag? A natural language explanation? The output format drives the model architecture and
   the Workshop display design. Define it before building.

4. **Define the success metric.** How will the PM know the model is good enough to release?
   Examples: precision/recall thresholds, false positive rate limits, agreement rate with
   subject matter expert review, stakeholder acceptance rate in evaluation. Write this down
   before modeling begins — do not let TM-40C define done post hoc.

5. **Assign tracks.** Typical ML project assignment:
   - TM-40C: model development, training pipeline, evaluation
   - TM-40F: data pipeline, feature engineering code
   - TM-40A: baseline statistical analysis, performance benchmarking
   - TM-40B: AIP integration if model output feeds an AI agent or workflow
   - TM-40E: data dictionary, ontology objects for model inputs/outputs
   - TM-40J (PM): project tracking, stakeholder communication, gate reviews

> **NOTE:** Engage TM-40E at problem definition, not after the model is built. Data quality
> issues surface early if the KM is involved in assessing input sources. Discovering a critical
> data quality problem after two sprints of model development is a PM failure.

---

## 3-3. Phase 2 — Data Audit

### Conditions

The team has identified input data sources for the ML project and must assess whether the
data is sufficient to train, validate, and run the model in production.

### Standards

TM-40C and TM-40E deliver a Data Audit Report. The PM reviews the report and makes a
go/no-go decision before authorizing prototype development.

### Procedure

1. **Pull TM-40C and TM-40E to audit each data source.** For each source, document:

   | Attribute            | Question to Answer                                                    |
   |----------------------|-----------------------------------------------------------------------|
   | Completeness         | What percentage of records have the key fields populated?             |
   | Timeliness           | How current is the data? What is the refresh lag?                     |
   | Historical depth     | How far back does history go? Is it sufficient for training?          |
   | Label availability   | For supervised models: are ground truth labels available?             |
   | Class balance        | For classification: are rare events represented in sufficient volume? |
   | Access               | Does the team have read access to the source dataset on MSS?          |
   | Schema stability     | Has the schema changed in the last 12 months? Will it change again?   |

2. **PM gate — Data Audit Review.** Review the completed Data Audit Report. Gate criteria:
   - If critical fields are less than 80% complete: stop. Require data remediation before
     proceeding. Assign TM-40F to build a data quality pipeline.
   - If historical depth is insufficient for training: stop. Present the constraint to the
     stakeholder. Offer alternative: rule-based heuristics instead of ML, or a simpler
     statistical model that requires less history.
   - If labels are unavailable for a supervised approach: reassess model type. Unsupervised
     or semi-supervised methods may apply; engage TM-40C for recommendation.
   - If access is blocked: escalate to C2DAO immediately. Do not let access blockers sit.

3. **Document the data audit decision.** Record in the project tracker: data sources approved,
   known quality limitations, and any data remediation tasks added to the backlog.

> **WARNING:** Skipping the data audit and proceeding directly to prototype is the most common
> cause of ML project failure. A model trained on incomplete or misunderstood data will not
> generalize. The PM who authorizes prototype work without a data audit owns the subsequent
> failure.

---

## 3-4. Phase 3 — Prototype

### Conditions

The data audit is complete. Data sources are accessible, sufficiently complete, and historically
deep enough to support model training. The prototype sprint begins.

### Standards

At the end of the prototype phase, TM-40C delivers a working model that can run on the
approved input data and produce output in the defined format, with preliminary performance
metrics against the defined success criteria.

### Procedure — PM Actions During Prototype Phase

1. **Scope the prototype sprint(s) tightly.** The prototype is not the production model. It is
   a proof of feasibility. Resist stakeholder requests to add features, expand the data scope,
   or integrate the prototype with production Workshop before evaluation is complete.

2. **Protect TM-40C from distraction.** Model development requires sustained focus. Do not pull
   TM-40C into stakeholder demonstrations, unrelated tasks, or data pipeline work during
   prototype sprints unless it is directly required for the model.

3. **Check in daily on blockers — not on model progress.** Ask: "Are you blocked on anything?"
   not "How accurate is the model today?" Premature accuracy questions push developers toward
   overfitting and rushed evaluation.

4. **Track prototype milestones:**
   - Milestone 1: First model version runs end-to-end on training data
   - Milestone 2: Initial performance metrics generated against holdout dataset
   - Milestone 3: Model output presented to PM in defined output format

5. **Do not show prototype outputs to operational stakeholders.** A prototype is not a product.
   Showing prototype model outputs to a commander before evaluation is complete risks anchoring
   the stakeholder on incomplete results.

---

## 3-5. Phase 4 — Evaluation

### Conditions

The prototype model produces output. The PM must now determine whether the model meets the
defined success metric and is ready to enter a production readiness review.

### Standards

The PM conducts an Evaluation Review with TM-40C, TM-40A (for independent statistical
assessment), and at least one operational subject matter expert (SME). The review produces a
documented pass/fail/iterate decision.

### Procedure

1. **Assemble the evaluation package.** TM-40C delivers:
   - Performance metrics (precision, recall, F1, AUC, or task-appropriate metrics)
   - Confusion matrix or error analysis
   - Feature importance or model explanation summary
   - Examples of correct predictions and failure cases

2. **Assign TM-40A to conduct independent validation.** TM-40A (ORSA) independently reviews
   the methodology and performance claims. The ORSA does not re-train the model — they
   validate the evaluation process and flag any statistical concerns.

3. **Conduct SME review.** Present the model outputs to an operational SME (the stakeholder's
   representative who understands the domain). Ask: Do these outputs make operational sense?
   Are the false positives operationally tolerable? Are the false negatives operationally
   tolerable?

4. **PM Evaluation Gate decision:**

   | Outcome           | Condition                                                           | PM Action                                      |
   |-------------------|---------------------------------------------------------------------|------------------------------------------------|
   | Pass              | Metrics meet threshold; SME accepts output quality                  | Proceed to Phase 5 (Production)                |
   | Iterate           | Metrics near threshold; specific failure mode identified and fixable| Return to prototype with scoped improvement task|
   | Stop — Redesign   | Fundamental data or approach problem; metrics far from threshold    | Restart at Phase 1 or 2 with revised approach  |
   | Stop — Descope    | Model not feasible given data; simpler heuristic approach better    | Descope ML; proceed with rule-based product     |

> **CAUTION:** Do not iterate indefinitely. Set a maximum of two iteration cycles before making
> a Stop decision. Unlimited iteration on a failing model is a resource drain and delays delivery
> of an alternative solution that might actually work.

---

## 3-6. Phase 5 — Production

### Conditions

The model passes evaluation. The PM must now manage the production deployment process.

### Standards

The PM completes the Definition of Done checklist (Appendix B), coordinates a production
release plan with TM-40F and TM-40C, and communicates the release to operational users
before deployment.

### Procedure

1. **Complete the Definition of Done checklist.** Do not abbreviate or skip items.
   If any DoD item is not satisfied, the release does not proceed.

2. **Build the production monitoring plan.** Define:
   - How will model performance be monitored in production? (Input data distribution shifts,
     output confidence score distribution, user override rate)
   - Who is the model owner responsible for monitoring? (Typically TM-40C)
   - What threshold triggers a model review? (Define numerically — not "if it seems off")
   - What is the rollback procedure if the model degrades?

3. **Coordinate the deployment window.** Schedule the production deployment during a low-
   operational-tempo window. Notify downstream users 48 hours in advance per the Safety Summary.

4. **Execute the deployment with TM-40F and TM-40C present.** Run the deployment against the
   production environment. Validate model outputs after deployment before declaring success.

5. **Brief the operational stakeholder.** Walk the stakeholder through the production product:
   how to read the outputs, what confidence thresholds mean, how to report anomalies, and who
   to contact if the model produces results that seem wrong.

---

## 3-7. Phase 6 — Sustainment

**BLUF:** A model in production is not done — it is a system that requires active management.
Model performance degrades as input data drifts, operational contexts change, and upstream
data sources change schema or refresh rates.

### PM Sustainment Responsibilities

1. **Schedule quarterly model reviews.** TM-40C reviews performance metrics quarterly.
   PM reviews the report and decides: sustain, retrain, or retire.

2. **Track upstream data source changes.** If a TM-40F pipeline engineer or a TM-40E KM
   flags that an input data source has changed schema or refresh rate, escalate immediately.
   A changed input can silently degrade model performance without triggering any obvious error.

3. **Maintain model version tracking on MSS.** Model deployment in Foundry follows this pattern: batch inference transforms write predictions to a Foundry dataset, which then serves as the source for computed properties on Object Types, or models are integrated into AIP Logic workflows. The TM-40C model owner must keep the model card and associated dataset documentation current — reflecting version, training date, performance metrics, and owner — after every retrain.

4. **Manage model retirement.** When a model is retired (superseded, no longer operationally
   relevant, or failing sustainment review), the PM coordinates: stakeholder notification,
   shutdown of the Workshop display, archival of the model artifacts, and documentation of
   the retirement decision.

---

# CHAPTER 4 — STAKEHOLDER MANAGEMENT AND REQUIREMENTS TRANSLATION

## 4-1. The Translation Problem

**BLUF:** The PM's most critical skill is translating between two languages: the operational
language of commanders and staff and the technical language of developers and data scientists.
Failure to translate accurately in both directions is the leading cause of delivering the wrong
product.

The translation problem manifests in two directions:

**Direction 1 — Operational to Technical:** A commander says "I need better situational
awareness on logistics." The PM must translate this into: a specific dataset, a refresh
cadence, a display format, a user story, and acceptance criteria that TM-40F can build.

**Direction 2 — Technical to Operational:** A TM-40C says "the model has an AUC of 0.87
but the recall on the minority class is 0.61 at the 0.5 threshold." The PM must translate
this into: "The model correctly identifies roughly six out of every ten high-risk events,
which means it misses four. For this use case, missing four out of ten is operationally
acceptable because the cost of a false alarm is low."

Neither translation is automatic. Both require the PM to understand enough of both domains
to bridge them accurately.

---

## 4-2. Requirements Elicitation

### Conditions

The PM has been assigned to scope a new data or AI capability. The operational stakeholder
has expressed a requirement in vague or general terms.

### Standards

The PM produces a Requirements Document containing: the stakeholder's operational need,
the current workaround or pain point, the proposed MSS solution, the input data required,
the output format, the users and roles, the success metric, and the out-of-scope boundaries.

### Procedure

1. **Conduct a discovery interview with the operational stakeholder.** Ask:
   - Walk me through your current workflow for [the task]. What are you doing today?
   - Where does that process break down or slow down?
   - What would done look like? What would you be able to do that you cannot do today?
   - Who else uses this information? Who are the downstream consumers?
   - How often does this need to update? Real-time, daily, weekly?
   - What would make you not use this product? What would make it wrong?

2. **Resist accepting the stakeholder's proposed solution as the requirement.** Stakeholders
   often bring a solution ("I need a dashboard") when the PM needs to understand the problem
   ("I cannot track equipment readiness across all subordinate units without calling each S4").
   The PM's job is to validate whether the proposed solution actually solves the problem.

3. **Draft the Requirements Document.** Use the template:

   ```
   REQUIREMENT: [One sentence — what operational outcome the product enables]
   STAKEHOLDER: [Name, role, unit]
   CURRENT STATE: [How the stakeholder handles this today — the workaround or manual process]
   PROPOSED SOLUTION: [What will be built on MSS]
   INPUT DATA: [Datasets required — names, sources, owners, refresh rates]
   OUTPUT FORMAT: [Dashboard / alert / export / API / model score — be specific]
   USERS AND ROLES: [Who will use the product — by role, not by name]
   SUCCESS METRIC: [How the PM and stakeholder will know it is working]
   OUT OF SCOPE: [What this product will NOT do — prevents scope creep]
   PRIORITY: [Must have / Should have / Nice to have]
   ```

4. **Review the Requirements Document with the stakeholder before starting work.** Read back
   the requirement, success metric, and out-of-scope section explicitly. Confirm agreement
   before the document is baselined and backlog items are created.

> **NOTE:** A signed-off Requirements Document does not prevent requirements from changing.
> It creates a baseline for managing change. When a stakeholder requests a scope change, the
> PM compares the request to the baselined requirements, estimates impact, and presents
> options — not just "yes" and not just "no."

---

## 4-3. Managing Stakeholder Expectations

### 4-3a. Setting Delivery Expectations

Do not commit to a delivery date before three sprints of velocity data exist. Use this
language with stakeholders:

| Stage               | What to Say                                                                                         |
|---------------------|-----------------------------------------------------------------------------------------------------|
| Project kickoff     | "We will have an initial estimate after two sprints. First sprint is scoping and data validation." |
| After sprint 1      | "Still building velocity baseline. Initial sense is [X sprints] but that may change."              |
| After sprint 3      | "Based on velocity, we project delivery of [feature set] by [date range] +/- one sprint."         |
| Confirmed forecast  | "We are committed to [feature set] by [date]. Scope changes after this point require a tradeoff."  |

### 4-3b. Stakeholder Communication Cadence

| Stakeholder Type       | Recommended Touchpoint                                       | Format                                          |
|------------------------|--------------------------------------------------------------|-------------------------------------------------|
| Direct operational user| Sprint review attendance (every sprint)                      | Live demo on MSS                                |
| Commanding officer     | Monthly project status update                                | MSS dashboard (Chapter 5) — not a slide deck   |
| Technical leadership   | Sprint review + async update in project channel              | MSS board + brief written summary              |
| C2DAO / platform team  | As needed for governance events (access, ontology, deploys)  | Coordination via C2DAO workflow                 |

> **NOTE:** Commander-level project status should be served from a live MSS Workshop dashboard,
> not a PowerPoint deck. A static briefing slide is stale the moment it is printed. A live
> dashboard shows real data. Chapter 5 covers building the commander-facing project status
> dashboard.

---

## 4-4. Managing the Technical Team

### 4-4a. PM Authority vs. Technical Authority

The PM holds authority over: scope, priority, stakeholder communication, release timing, and
project tracking. The PM does not hold authority over: how a developer implements a feature,
which algorithm a TM-40C uses, or how TM-40F structures code.

Attempting to micro-manage technical implementation decisions creates friction, reduces team
ownership, and produces worse outcomes. Delegate technical decisions to the appropriate TM-40
track and hold them accountable to the acceptance criteria — not to the implementation method.

### 4-4b. Protecting the Team from Scope Sprawl

Scope sprawl is the most common project killer in operational data environments. Stakeholders
who see a working dashboard immediately want to add filters, additional datasets, new metrics,
and new features — before the current sprint is complete.

PM procedure for incoming scope requests during a sprint:

1. Record the request in the backlog immediately.
2. Acknowledge the stakeholder: "Logged. We will assess priority in sprint planning."
3. Do not add the request to the current sprint unless it is a blocking defect.
4. At sprint planning, assess priority against current backlog. Let the stakeholder make
   the tradeoff: "If we add this to the sprint, we move [existing item] to the next sprint.
   Which do you prefer?"

### 4-4c. Cross-Track Coordination

When a story requires multiple TM-40 tracks, the PM must sequence the work and manage the
hand-off points:

| Dependency Pattern                              | PM Action                                                                          |
|-------------------------------------------------|------------------------------------------------------------------------------------|
| TM-40F pipeline must complete before TM-40C can train | Make pipeline story a sprint 1 item; model story a sprint 2 item with explicit dependency noted |
| TM-40E ontology object must exist before TM-40F can write to it | TM-40E story goes in sprint backlog; TM-40F story blocked until merged |
| TM-40B agent workflow depends on TM-40C model output format | PM defines the output schema interface in sprint planning; both tracks work to that contract |
| TM-30 Workshop dashboard depends on TM-40F pipeline | Pipeline completes and is validated before Workshop build begins                    |

---

# CHAPTER 5 — BUILDING PROJECT TRACKING SYSTEMS ON MSS

## 5-1. Why Track on MSS, Not Spreadsheets

**BLUF:** Project tracking on MSS provides live visibility to all stakeholders without the
version-control and distribution problems of spreadsheets. A Workshop-based project tracker
is the single source of truth, accessible to every team member with the correct Foundry role,
updated in real time.

A Jira-style spreadsheet or SharePoint tracker has the following failure modes in USAREUR-AF
operations:

- Multiple versions in circulation with no authoritative copy
- Commander-level visibility requires manual compilation into a briefing slide
- Status updates depend on someone remembering to update a cell
- No automated alert when a milestone slips or a blocker exceeds SLA

An MSS-based tracker eliminates all of these. This chapter covers the procedure for building it.

---

## 5-2. Designing the Project Tracker Ontology

### Conditions

The PM is setting up a new project on MSS and needs a tracking infrastructure. This task is
performed in coordination with TM-40E (Knowledge Manager) if a new ontology design is needed,
or by the PM using an existing project tracker template if one is available in the USAREUR-AF
project tracker library.

### Standards

The project tracker Ontology contains the following Object Types at minimum: Project, Sprint,
Story (or Task), Team Member, Risk, and Dependency. Links connect Stories to Sprint, Sprint to
Project, and Team Member to Stories (as assignee).

### Procedure — Ontology Design for Project Tracker

1. **Check the USAREUR-AF project tracker library first.** The C2DAO maintains reusable
   Ontology templates. Do not rebuild from scratch if a validated template exists.

2. **Define the Object Types.** For each type, define the properties:

   **Project Object Type**

   | Property          | Type     | Notes                                       |
   |-------------------|----------|---------------------------------------------|
   | project_name      | String   | Short name, used as display label           |
   | product_vision    | String   | One-paragraph product vision statement      |
   | pm_owner          | String   | PM name and TM-40J track                   |
   | start_date        | Date     |                                             |
   | target_end_date   | Date     | Expected delivery — not a commitment        |
   | current_status    | Enum     | On Track / At Risk / Blocked / Complete     |
   | stakeholder_org   | String   | Unit or directorate of primary stakeholder  |

   **Sprint Object Type**

   | Property          | Type     | Notes                                       |
   |-------------------|----------|---------------------------------------------|
   | sprint_name       | String   | e.g., "Sprint 4 — 10-21 Mar 2026"          |
   | sprint_goal       | String   | One sentence                                |
   | start_date        | Date     |                                             |
   | end_date          | Date     |                                             |
   | velocity_planned  | Integer  | Story points or T-shirt size count planned  |
   | velocity_actual   | Integer  | Completed at sprint end                     |
   | status            | Enum     | Planning / Active / Review / Complete       |

   **Story Object Type**

   | Property          | Type     | Notes                                       |
   |-------------------|----------|---------------------------------------------|
   | story_id          | String   | Unique ID (auto-generated or manual)        |
   | story_title       | String   | Short title for board display               |
   | story_text        | String   | Full "As a / I want / So that" text         |
   | acceptance_criteria | String | Full AC text                               |
   | size              | Enum     | S / M / L / XL                             |
   | status            | Enum     | Backlog / Ready / In Progress / In Review / Done |
   | assignee          | String   | TM-40 track + name                         |
   | track             | Enum     | 40A / 40B / 40C / 40E / 40F / 30           |
   | blocked           | Boolean  | True if blocker exists                      |
   | blocker_description | String | Description of blocker (if blocked = true) |
   | sprint_link       | Link     | → Sprint                                    |

   **Risk Object Type** — see Chapter 6.

   **Dependency Object Type** — see Chapter 6.

3. **Create the Object Types in the Foundry Ontology UI.** Use the UI to create types and
   properties. Coordinate with TM-40E if the project tracker will share any Object Types
   with the enterprise ontology (e.g., linking Team Members to an existing Personnel object).

4. **Configure write access for all team members.** Each team member must have write access
   to update their own Story records. The PM configures role-based access in the Foundry
   project settings.

> **NOTE:** If TM-40E has already designed a standard project tracker ontology for USAREUR-AF,
> use it. Ontology proliferation — every PM designing their own object types — creates
> governance debt that TM-40E must clean up. Check before designing.

---

## 5-3. Building the Sprint Board in Workshop

### Conditions

The Ontology is defined and populated with at least one Sprint and its associated Stories.
The PM is building the Scrum board view in Foundry Workshop.

### Standards

The Workshop application displays: the current sprint goal, a Kanban-style board with Story
cards grouped by status column, a blockers panel, and a velocity chart. The board updates in
real time as team members change Story status.

### Procedure

1. **Create a new Workshop application** in the MSS project space. Name it:
   `[Project Name] — Sprint Board`.

2. **Add a Sprint Selector widget** at the top of the page. This allows users to switch between
   viewing the current sprint and historical sprints for reference.

3. **Add a Kanban Board widget** linked to the Story Object Type, filtered to the selected
   sprint. Configure columns: Backlog | Ready | In Progress | In Review | Done. Each card
   shows: story_title, assignee, size, and a red indicator if blocked = true.

4. **Add a Sprint Goal banner** at the top: a text widget that displays the sprint_goal
   property of the selected Sprint object.

5. **Add a Blockers Panel** below the Kanban board. Filter Stories where blocked = true.
   Display: story_title, assignee, blocker_description. This panel is visible to all
   stakeholders and creates accountability for blocker resolution.

6. **Add a Velocity Chart** on a second Workshop tab. Display a bar chart of velocity_planned
   vs. velocity_actual for all completed sprints in the project. This is the PM's forecasting
   tool.

7. **Configure Workshop publication permissions.** The sprint board should be visible to:
   the full project team (read/write for own stories), the PM (read/write all), and the
   stakeholder (read-only). Do not publish to a wider audience than required — story-level
   tracking data may contain information about resourcing and capability gaps.

> **CAUTION:** Do not use the same Workshop application for internal team tracking and
> commander-facing status reporting. These are different audiences with different information
> needs. Build separate applications — see 5-4 for commander-facing status.

---

## 5-4. Commander-Facing Project Status Dashboard

### Conditions

The PM must provide project status visibility to a commanding officer, directorate chief, or
senior leader who does not need sprint-level detail but requires accurate project health
information.

### Standards

The commander-facing dashboard displays: project name, current status (On Track / At Risk /
Blocked), sprint velocity trend, top risks (by severity), and projected delivery milestones.
The dashboard is designed for a 90-second read in a senior leader's workspace.

### Design Principles for Senior Leader Dashboards

| Principle             | Application                                                                          |
|-----------------------|--------------------------------------------------------------------------------------|
| BLUF first            | Status indicator (green/amber/red) visible at top of page, no scrolling required    |
| Numbers over narrative| Show metrics — velocity, risk count, days to milestone — not prose explanations      |
| Drill-down, don't flatten | Summary view on top; detail available on click/expand — not all on one page     |
| Current as of label   | Always display "Data as of [timestamp]" — never let staleness go unlabeled           |
| No jargon             | Story points, sprint velocity, AUC — not visible on commander dashboard. Translate.  |

### Procedure

1. **Create a new Workshop application** named: `[Project Name] — Status`.

2. **Add a Status Header block** at the top:
   - Project name (large text)
   - Current status indicator: a colored badge (green/amber/red) driven by the `current_status`
     property on the Project object
   - "As of [last_updated]" timestamp

3. **Add a Milestone Table** showing the next three to five major milestones:
   - Milestone name
   - Target date
   - Status (On Track / At Risk / Complete)
   - Color-coded by status

4. **Add a Progress Summary panel:**
   - Stories completed / total stories (shown as a fraction and progress bar)
   - Current sprint number and goal (one sentence)
   - Projected completion date range (derived from velocity trend)

5. **Add a Top Risks panel** showing the top three risks by severity score (Chapter 6).
   Display: risk description, severity, and current mitigation status. If no critical risks
   exist, show "No critical risks currently identified."

6. **Set publication permissions** to read-only for all stakeholder roles. The PM updates
   the Project object status field — the dashboard reflects the change automatically.

> **NOTE:** The commander dashboard does not replace verbal briefs. It supplements them.
> When a senior leader asks for a project update, the PM points to the live dashboard
> rather than producing a new slide. This builds trust in MSS as the authoritative source.

---

## 5-5. Automated Status Alerts

### Conditions

The PM wants to receive automated notification when a blocker exceeds a defined SLA, a
milestone passes its target date without being marked complete, or project status changes.

### Standards

The PM configures at least two automated alerts using MSS Pipeline Builder or AIP Logic:
a blocker-aging alert (fires when a story has been blocked for more than 48 hours) and a
milestone-slip alert (fires when today's date exceeds a milestone target date and status is
not Complete).

### Procedure

1. **Coordinate with TM-40B** to configure the alert logic using AIP Logic or a lightweight
   Pipeline Builder scheduled transform.

2. **Define the alert recipients** in the notification configuration. Do not configure alerts
   to send to commanders or senior leaders directly — route to the PM, who then decides
   whether to escalate.

3. **Test the alerts** in a non-production sprint before relying on them in a live project.
   Verify that the trigger condition fires correctly and that the notification reaches the
   intended recipient.

---

# CHAPTER 6 — RISK AND DEPENDENCY MANAGEMENT

## 6-1. Risk Management for Data Projects

**BLUF:** Data and AI projects have a specific risk profile that differs from general software
projects. The PM must manage technical risks, data risks, and operational risks simultaneously.

The three risk domains for MSS data/AI projects:

| Domain     | Examples                                                                                           |
|------------|----------------------------------------------------------------------------------------------------|
| Data       | Source dataset unavailable, schema changed, quality below threshold, access blocked               |
| Technical  | Model accuracy insufficient, pipeline latency too high, platform capacity constraints             |
| Operational| Stakeholder changes requirements, end users resist adoption, organizational priority shifts       |

---

## 6-2. Risk Register

### Conditions

The PM is managing an active project and must maintain a risk register that is visible to the
project team and relevant stakeholders.

### Standards

The risk register is an MSS Ontology Object Type populated with all identified risks. Each risk
has: description, domain, likelihood, impact, severity score, owner, mitigation strategy, and
current status. The register is reviewed at every sprint planning session.

### Risk Object Type Properties

| Property          | Type     | Notes                                                       |
|-------------------|----------|-------------------------------------------------------------|
| risk_id           | String   | Auto or manual unique ID                                    |
| description       | String   | Plain-language description of what could go wrong          |
| domain            | Enum     | Data / Technical / Operational                              |
| likelihood        | Enum     | Low (1) / Medium (2) / High (3)                            |
| impact            | Enum     | Low (1) / Medium (2) / High (3)                            |
| severity_score    | Integer  | Computed: likelihood × impact (1-9)                        |
| owner             | String   | Team member responsible for monitoring and mitigation       |
| mitigation        | String   | Specific action being taken to reduce likelihood or impact  |
| contingency       | String   | What will be done if the risk materializes                  |
| status            | Enum     | Open / Mitigated / Accepted / Closed                        |
| last_reviewed     | Date     | Date of last PM review                                      |

### Risk Severity Matrix

|                  | Low Impact (1) | Medium Impact (2) | High Impact (3) |
|------------------|---------------|-------------------|-----------------|
| **High Likely (3)**  | 3             | 6                 | **9 — Critical**    |
| **Med Likely (2)**   | 2             | 4                 | **6 — High**        |
| **Low Likely (1)**   | 1             | 2                 | **3 — Moderate**    |

Severity 7-9 (Critical): Escalate to project sponsor/stakeholder leadership immediately.
Severity 4-6 (High): Active mitigation required; review weekly.
Severity 1-3 (Moderate): Monitor; review at sprint planning.

### Procedure — Sprint Risk Review

1. At each sprint planning session, open the risk register in Workshop.
2. Review all Open risks with severity ≥ 4.
3. For each: has likelihood or impact changed? Has mitigation progressed?
4. Update the risk record. Change status to Mitigated if the risk has been addressed.
5. Add any new risks identified during the previous sprint.
6. Present any new Critical risks to the project sponsor before the sprint begins.

---

## 6-3. Dependency Management

**BLUF:** Data projects have more cross-team dependencies than most software projects.
A pipeline must exist before a model can train. An Ontology type must be published before
a Workshop view can display it. Managing these dependencies is a primary PM function.

### Dependency Object Type Properties

| Property          | Type     | Notes                                                         |
|-------------------|----------|---------------------------------------------------------------|
| dependency_id     | String   | Unique ID                                                     |
| description       | String   | What does Story A need from Story B (or external source)?     |
| blocking_story    | Link     | → Story that is blocked                                       |
| provider          | String   | Team member or external team providing the dependency        |
| expected_date     | Date     | When will the dependency be resolved?                        |
| actual_date       | Date     | When was it actually resolved?                               |
| status            | Enum     | Open / At Risk / Resolved                                    |

### Common Dependency Patterns

| Pattern                                               | PM Action                                                          |
|-------------------------------------------------------|--------------------------------------------------------------------|
| Data pipeline (TM-40F) blocks model training (TM-40C) | Sequence sprints; pipeline in sprint N, model in sprint N+1       |
| External data source access blocked by C2DAO          | Escalate at sprint planning; do not let access requests age        |
| TM-40E ontology design blocks TM-40F coding           | Start ontology design in sprint 1 even if build is sprint 2 work  |
| TM-40B agent depends on TM-40C model endpoint         | Define API contract in sprint planning; both tracks work to spec   |
| MSS platform upgrade changes Workshop component API   | Track platform release calendar; coordinate with TM-40F on timing |

> **WARNING:** Do not assume external dependencies will resolve on schedule. Treat all
> external dependencies (C2DAO access requests, data source onboarding, platform upgrades)
> as risks with a separate risk record. If an external dependency is on the critical path,
> escalate immediately — do not wait for the blocked sprint to surface it.

---

## 6-4. Technical Debt Management

Technical debt accumulates in data projects when shortcuts are taken to meet delivery dates:
hardcoded values instead of config files, missing documentation, untested pipeline logic,
a model deployed without a monitoring plan, or Workshop widgets that bypass the Ontology.

The PM is responsible for managing the technical debt backlog — not just the feature backlog.

### Procedure

1. **Create a "Tech Debt" label or tag in the Story tracker.** Any story addressing technical
   debt is tagged so it can be tracked separately from feature work.

2. **Reserve 15-20% of each sprint's capacity for tech debt.** Do not let technical debt
   stories compete with feature stories without a dedicated capacity allocation. Stakeholders
   will always want features; tech debt will never win if unprotected.

3. **Conduct a tech debt review at each quarterly retrospective.** TM-40F and TM-40C identify
   the highest-impact debt items. PM prioritizes the top three into the next quarter's capacity.

4. **Never allow tech debt to accumulate in production monitoring.** An ML model in production
   without a monitoring dashboard is not a debt item — it is an active risk. Treat it as
   severity-6 risk (Chapter 6-2).

---

# CHAPTER 7 — DELIVERY PLANNING AND PRODUCTION READINESS

## 7-1. Scope, Timeline, and Quality Tradeoffs

**BLUF:** The PM cannot simultaneously guarantee scope, timeline, and quality. At any decision
point, one of these three is the constraint that others must flex around. Define the constraint
explicitly before making delivery tradeoff decisions.

| Constraint Mode      | Fixed        | Can Flex                              | When to Use                                                |
|----------------------|--------------|---------------------------------------|------------------------------------------------------------|
| Fixed Deadline       | Timeline     | Scope (cut features) or Quality risk  | Hard operational deadline (exercise, OPORD, command review)|
| Fixed Scope          | Scope        | Timeline (slip the date)              | Safety-critical product where partial is unacceptable     |
| Fixed Quality        | Quality      | Timeline and scope                    | Production ML model or regulated data product              |

The PM must communicate the constraint mode to both the technical team and the stakeholder.
Failing to name the constraint results in the team trying to hold all three — which produces
a late, descoped, low-quality product.

---

## 7-2. Release Planning

### 7-2a. Milestone Types

| Milestone Type    | Definition                                                             |
|-------------------|------------------------------------------------------------------------|
| Internal Milestone| Checkpoint within the team (data audit complete, model trained)        |
| Alpha Release     | First build available for stakeholder feedback — incomplete, unstable  |
| Beta Release      | Feature-complete build for operational user testing — not production   |
| Production Release| DoD-complete, validated, deployed to production audience               |
| Patch Release     | Bug fix or minor update to a production product                        |
| Major Release     | Significant new capability added to an existing production product     |

### 7-2b. Release Planning Procedure

1. **Define release milestones at project kickoff.** Include them in the commander-facing
   dashboard from day one. Milestone dates are projections — flag them as projections until
   three-sprint velocity baseline establishes a credible forecast.

2. **Run a release readiness review before every production release.** The release readiness
   review is a PM-led meeting with TM-40F, TM-40C (if ML involved), and TM-40E. The agenda:
   - Is the Definition of Done checklist complete?
   - Are all known defects triaged — none outstanding at Critical severity?
   - Is the monitoring plan in place?
   - Is the rollback procedure documented and tested?
   - Have operational users been notified of the release?

3. **Do not release on Fridays or the day before a low-staffing period.** If a production
   deployment fails or produces bad data, the team must be available to respond.

---

## 7-3. Definition of Done — Data Product

The Definition of Done (DoD) is the PM's quality gate for every data product release.
See Appendix B for the complete checklist. The DoD has five sections:

| Section           | What It Covers                                                                  |
|-------------------|---------------------------------------------------------------------------------|
| Data Quality      | Input data validated, lineage documented, refresh pipeline tested               |
| Product Function  | All acceptance criteria met and tested, no critical defects open                |
| Access Control    | Role-based access configured; least-privilege verified; C2DAO review completed  |
| Documentation     | User guide exists, data dictionary updated, model card complete (if ML)         |
| Operability       | Monitoring plan active, rollback procedure documented, stakeholder briefed      |

No section may be skipped. If any DoD item cannot be satisfied, the release is blocked until
it is resolved or formally accepted as a known risk with documented rationale.

---

## 7-4. What "Production Ready" Means for a Data Product

Production ready is not a feeling. It is a checklist result.

For a dashboard or data pipeline product:

- All source data is connected to the live Ontology (not a static snapshot)
- The pipeline runs on schedule without manual intervention
- Access control is configured to production roles (not the developer's personal account)
- The product has been demonstrated to at least one operational user who confirmed it meets
  the requirement
- A data steward (TM-40E) has reviewed and accepted the ontology design
- The PM has completed Appendix B and no items are outstanding at Critical severity

For an ML/AI model product (in addition to the above):

- Model performance meets the defined success metric from Phase 1 (3-2)
- The model has been evaluated on data it was not trained on (holdout or production sample)
- A model card documenting training data, performance metrics, known failure modes, and
  appropriate use cases exists and is stored in the project space
- A monitoring plan is active and the model owner (TM-40C) has accepted monitoring
  responsibility
- The stakeholder has been briefed on how to interpret model outputs, including what the
  model does not do and what to do when the output seems wrong

---

## 7-5. Post-Release Review

Within two weeks of a production release, the PM conducts a Post-Release Review. This is
not a retrospective on the project — it is a review of whether the product is performing
as intended in production.

**Post-Release Review Agenda:**

1. Are users accessing the product? (Check Workshop usage analytics)
2. Are users taking the actions the product was designed to enable?
3. Have any data quality issues surfaced in production that were not caught in testing?
4. Have users reported any defects or usability problems?
5. Is the monitoring pipeline running on schedule?
6. For ML products: is the model performance distribution in production consistent with
   evaluation performance?

**PM Action:** If answers to questions 1-2 indicate the product is not being used, escalate
to Chapter 8 (Change Management). Low adoption in the first two weeks after release is the
leading indicator of a change management problem, not a product quality problem.

---

# CHAPTER 8 — CHANGE MANAGEMENT AND USER ADOPTION

## 8-1. Why Operational Users Resist New Data Products

**BLUF:** Building a technically excellent data product does not guarantee adoption. Operational
users in USAREUR-AF have established workflows, high operational tempo, and limited patience for
tools that require learning investment before delivering value. The PM must manage adoption
actively — it does not happen automatically.

Resistance to new MSS capabilities is not irrational. It comes from:

| Resistance Source                  | What Users Are Actually Saying                                         |
|------------------------------------|------------------------------------------------------------------------|
| "I don't have time to learn this"  | The tool's learning curve is longer than the value delivered per use  |
| "I don't trust the data"           | The data has been wrong before, or they cannot verify it              |
| "My current process already works" | The new tool does not improve their workflow enough to justify change  |
| "Nobody told me about this"        | The deployment was silent; users discovered it without context        |
| "It's too complicated"             | The interface was designed for builders, not operators               |

Each of these is a PM problem — not a user problem. The PM must address the root cause, not
dismiss the resistance.

---

## 8-2. Change Management Planning

### Conditions

The PM has a production-ready data product that will change the workflow of an operational
unit or staff element. The PM must plan and execute the transition from the old workflow to
the new product.

### Standards

The PM completes a Change Management Plan before the production release date. The plan
covers: stakeholder mapping, communication plan, training plan, adoption metrics, and
rollback communication plan.

### Procedure — Change Management Plan

1. **Map the affected stakeholders.** For each group that will change their workflow:

   | Stakeholder Group   | Current Workflow         | New Workflow              | Impact Level |
   |---------------------|--------------------------|---------------------------|--------------|
   | G4 officers         | Weekly Excel tracker     | Live MSS dashboard        | High         |
   | Unit S4s            | Phone calls + email      | Workshop form submission  | High         |
   | G4 staff            | Manual compilation       | Automated pipeline output | Medium       |

2. **Identify change sponsors.** For high-impact stakeholder groups, identify a senior person
   within the group who understands the new product and will champion it internally. A change
   sponsor is not a trainer — they are a peer voice who signals that the new way is endorsed
   at the unit level.

3. **Build the communication plan.** Minimum communication events:

   | Timing                  | Event                                  | Audience                     |
   |-------------------------|----------------------------------------|------------------------------|
   | T-30 days               | Announcement: "New product coming"     | All affected stakeholders    |
   | T-14 days               | Demo / preview session                 | Key users and change sponsors|
   | T-7 days                | Training session                       | End users                    |
   | T-2 days                | Final reminder + link to user guide    | All affected stakeholders    |
   | T+0 (release day)       | Go-live announcement + support contact | All affected stakeholders    |
   | T+14 days               | Adoption check-in / feedback session   | Users + change sponsors      |

4. **Build the training plan.** For MSS Workshop products, training should be:
   - 30 minutes maximum for a dashboard user
   - Hands-on in MSS — not slides about MSS
   - Recorded for users who cannot attend the live session
   - Followed by a user guide (see 8-3 for user guide standards)

5. **Define adoption metrics.** How will the PM know adoption is occurring?
   - Workshop application open rate (first 30 days)
   - Form submission volume (if the product includes user input)
   - Reduction in manual workaround behavior (e.g., no more weekly Excel distribution)
   - Stakeholder self-reported satisfaction at T+30 days

6. **Define the rollback communication plan.** If the product must be pulled back or a critical
   defect surfaces post-release, the PM communicates to all affected stakeholders within four
   hours. The rollback communication includes: what happened, what users should do in the
   interim, and when the fix will be deployed.

---

## 8-3. User Guide Standards

Every production MSS product requires a user guide. The user guide is not a technical
architecture document — it is written for the operational user, not the developer.

**User Guide Minimum Contents:**

| Section               | Content                                                                         |
|-----------------------|---------------------------------------------------------------------------------|
| Purpose               | One paragraph: what this product does and who it is for                        |
| Access                | How to access the product on MSS (URL/link + role required)                    |
| Navigating the product| Screenshots with labeled callouts of each panel and its function               |
| How to [Task 1]       | Step-by-step instructions for the primary user task                            |
| How to [Task 2]       | Repeat for each additional user task                                           |
| Interpreting outputs  | For ML/AI products: what the scores, flags, or recommendations mean            |
| Known limitations     | What the product does NOT do; data quality caveats; refresh lag                |
| How to report a problem| Contact, channel, and what information to include when reporting a defect      |

**Format standards:**
- Maximum 10 pages for any single user guide
- Screenshots from the actual production environment — not mockups
- Plain language — define any technical term used
- Reviewed by one actual end user before publication

---

## 8-4. Managing Resistance During Rollout

### When Low Adoption Surfaces at the T+14 Check-In

If the T+14 adoption check-in shows low uptake, diagnose before escalating:

1. **Is it an access problem?** Check if affected users have the correct Foundry role. Access
   provisioning gaps are the most common early-adoption blocker.

2. **Is it an awareness problem?** Check whether the communication reached all intended
   recipients. USAREUR-AF distribution lists are imperfect. Personal outreach via change
   sponsors often reaches users that mass distribution does not.

3. **Is it a usability problem?** Observe a user attempting to use the product without
   assistance. Does the interface make the primary task obvious? If users cannot complete
   the primary task without asking for help, the interface needs revision — not more training.

4. **Is it a trust problem?** Ask users directly: "Is there anything about the data that
   seems wrong or that you don't trust?" Data trust problems require evidence. Pull the data
   lineage, walk the user through the source-to-display chain, and demonstrate that the
   numbers are correct. A single trust failure that goes unaddressed destroys adoption.

5. **Is it a change sponsor problem?** If the unit-level change sponsor is not using or
   endorsing the product, junior users will not adopt it. Re-engage the sponsor. If the
   sponsor has concerns, address them before expecting the team to follow.

---

## 8-5. Platform Governance — PM Perspective

The PM is responsible for the governance of the MSS project space associated with their
product. This includes:

**Access Management:**
- Review project membership quarterly. Remove accounts of personnel who have PCS'd, completed
  TDY, or no longer require access.
- Coordinate all access additions and removals with TM-40E (KM/Data Steward) and the C2DAO.
- Do not grant admin or builder access to users who only need consumer access. Apply
  least-privilege.

**Resource Allocation:**
- Monitor dataset storage usage in the project. Unmanaged pipeline output accumulation can
  hit storage quotas and degrade platform performance for other users in the AOR.
- Coordinate with TM-40F to implement dataset retention policies on pipeline outputs that
  generate large volumes.
- Report resource constraint concerns to the C2DAO before they become capacity incidents.

**Ontology Governance:**
- Do not modify shared enterprise Ontology types (managed by TM-40E) without C2DAO review.
- When a project-local Object Type matures to the point where it should be promoted to the
  enterprise ontology, coordinate the promotion with TM-40E — do not attempt it directly.

**Audit Trails:**
- MSS maintains activity logs for Object edits, pipeline runs, and Workshop access.
- Preserve audit logs for all production data products per USAREUR-AF data retention policy.
- If a data quality incident occurs, the audit trail is the PM's first diagnostic resource.

---

# APPENDIX A — PROJECT KICKOFF CHECKLIST

## A-1. Purpose

This checklist is completed by the Technical PM before sprint 1 begins. No sprint work
starts until all items are complete or formally accepted as known gaps with a plan to close.

---

## A-2. Checklist

**Section 1 — Scope and Requirements**

- [ ] Product vision statement written and posted in the project space
- [ ] Requirements Document drafted, reviewed with stakeholder, and baselined
- [ ] Out-of-scope boundaries explicitly documented and agreed by stakeholder
- [ ] Success metrics defined and measurable (not "it works" — specific thresholds)
- [ ] Priority tiers established (Must Have / Should Have / Nice to Have)
- [ ] Initial product backlog contains at least 2 sprints of groomed, sized, AC-complete stories

**Section 2 — Team Structure**

- [ ] All team members identified by name and TM-40 track
- [ ] PM role confirmed (Scrum Master / Product Owner)
- [ ] TM-40E (Knowledge Manager) identified for ontology and data dictionary coordination
- [ ] TM-40F (or appropriate developer track) assigned to pipeline work
- [ ] Cross-track dependencies mapped and initial dependency records created

**Section 3 — MSS Project Setup**

- [ ] Foundry project space created in the correct USAREUR-AF environment
- [ ] All team members have appropriate Foundry role access (not admin unless required)
- [ ] Project tracker Ontology types created (Project, Sprint, Story, Risk, Dependency)
- [ ] Sprint Board Workshop application built and accessible to all team members
- [ ] Commander-facing Status dashboard built (even if placeholder) and stakeholder has access
- [ ] At least one Sprint object created with sprint goal, start date, and end date

**Section 4 — Data and Platform**

- [ ] Input data sources identified for each pipeline or model component
- [ ] Data access confirmed — team can read all required source datasets on MSS
- [ ] Data Audit initiated (or scheduled for sprint 1) if ML components are involved
- [ ] No blocking dependencies on external data sources that are not yet on MSS
- [ ] Platform resource constraints assessed — no current storage or compute flags

**Section 5 — Governance**

- [ ] C2DAO coordination initiated if project involves shared enterprise Ontology types
- [ ] Access control plan documented (who gets which role on production product)
- [ ] Data classification of all input sources confirmed with TM-40E
- [ ] Change management stakeholder map drafted
- [ ] Communication plan for production release drafted (even if T-0 is months away)

**Section 6 — Sprint Cadence**

- [ ] Sprint length confirmed (1 week or 2 week)
- [ ] Sprint 1 start date and end date confirmed
- [ ] Sprint ceremony calendar blocked for all team members (planning, standup, review, retro)
- [ ] Sprint 1 scope committed and visible on MSS sprint board

---

# APPENDIX B — DEFINITION OF DONE — DATA PRODUCT STANDARDS

## B-1. Purpose

The Definition of Done (DoD) is the PM's quality gate for every production release. No data
product is released to production without all DoD items satisfied or explicitly waived with
documented rationale. The PM signs off on the DoD — not the developer, not the stakeholder.

**How to use this checklist:**
- Run through the checklist at the production readiness review (7-2b)
- Each item is PASS, FAIL, or WAIVED (with written rationale)
- A FAIL on any Critical item blocks the release
- A WAIVED item requires PM signature and a documented plan to close within 30 days

---

## B-2. DoD Checklist — All Data Products

**Section 1 — Data Quality**

| # | Item | Priority | Status |
|---|------|----------|--------|
| 1.1 | Input data sources are connected to live Foundry datasets — no manual file uploads in the production pipeline | Critical | |
| 1.2 | Data lineage is documented from source to display (which dataset flows to which transform to which ontology object to which Workshop widget) | Critical | |
| 1.3 | All input datasets have a documented refresh schedule and the pipeline runs on that schedule without manual intervention | Critical | |
| 1.4 | Missing value handling is documented and tested — the pipeline does not silently produce incorrect outputs when upstream data is null or delayed | High | |
| 1.5 | Schema changes in input datasets have been accounted for — the pipeline handles variations seen in the past 12 months | High | |
| 1.6 | A data quality check (TM-40C: @check, or equivalent validation step) runs on critical input fields before outputs are published | High | |

**Section 2 — Product Function**

| # | Item | Priority | Status |
|---|------|----------|--------|
| 2.1 | All user stories in the production scope have acceptance criteria that have been tested and passed | Critical | |
| 2.2 | Zero open defects at Critical severity | Critical | |
| 2.3 | Zero open defects at High severity (or all waived with stakeholder sign-off) | High | |
| 2.4 | The product has been tested in the production environment (not only in a dev branch) | Critical | |
| 2.5 | At least one operational user (not a developer) has tested the product and confirmed it meets the stated requirement | Critical | |
| 2.6 | The product degrades gracefully when data is unavailable — it shows a "data unavailable as of [timestamp]" state, not a blank or error screen | High | |

**Section 3 — Access Control**

| # | Item | Priority | Status |
|---|------|----------|--------|
| 3.1 | Production roles are configured — access is not running under a developer's personal account | Critical | |
| 3.2 | Least-privilege applied — users have the minimum access level required for their role | Critical | |
| 3.3 | Access control reviewed and signed off by TM-40E (Data Steward) | High | |
| 3.4 | C2DAO coordination complete for any ontology types shared with the enterprise | High | |
| 3.5 | No test accounts, sandbox credentials, or temporary access grants present in the production configuration | Critical | |

**Section 4 — Documentation**

| # | Item | Priority | Status |
|---|------|----------|--------|
| 4.1 | User guide complete and reviewed by at least one end user | High | |
| 4.2 | Data dictionary entry updated in the project's TM-40E-managed data dictionary for all new datasets or ontology types | High | |
| 4.3 | Pipeline documentation updated — transform logic, schedule, and dependencies documented | High | |
| 4.4 | Known limitations section in the user guide accurately describes what the product does NOT do | High | |

**Section 5 — Operability**

| # | Item | Priority | Status |
|---|------|----------|--------|
| 5.1 | Monitoring is active — PM knows how to detect if the product stops working | Critical | |
| 5.2 | Rollback procedure is documented and has been tested (or tested in a prior comparable deployment) | Critical | |
| 5.3 | Operational users notified of the release at least 48 hours in advance | High | |
| 5.4 | Support contact identified and communicated to users — someone to call if the product fails | High | |
| 5.5 | Change management plan for post-release adoption is in place (Chapter 8) | Medium | |

---

## B-3. Additional DoD Items — ML/AI Products

Complete Section B-2 first. Then complete these additional items for any product that includes
a trained ML model, AI agent, or LLM integration.

| # | Item | Priority | Status |
|---|------|----------|--------|
| ML-1 | Model card exists and is stored in the project space: documents training data, algorithm, evaluation metrics, known failure modes, and appropriate use cases | Critical | |
| ML-2 | Model was evaluated on held-out data (not the training set). Evaluation metrics meet the defined success threshold from the Problem Definition (3-2) | Critical | |
| ML-3 | TM-40A (ORSA) has conducted independent validation of the evaluation methodology | High | |
| ML-4 | Operational SME has reviewed sample model outputs and accepted output quality | Critical | |
| ML-5 | Model output display includes confidence scores or uncertainty indicators — not bare binary outputs without context | High | |
| ML-6 | The product UI communicates what the model does NOT predict and where it should not be used | High | |
| ML-7 | Model monitoring is configured: TM-40C has accepted model owner responsibility and defined the threshold that triggers a model review | Critical | |
| ML-8 | Model version and training date are documented in the model card and associated Foundry dataset records. Model deployment in Foundry follows this pattern: batch inference transforms write predictions to a Foundry dataset, which then serves as the source for computed properties on Object Types, or models are integrated into AIP Logic workflows. | High | |
| ML-9 | Retraining schedule or trigger is documented (time-based or performance-based) | High | |

---

# GLOSSARY

**Acceptance Criteria (AC)** — Testable conditions that define when a user story is
complete. Written in GIVEN/WHEN/THEN format. The PM uses AC to verify that a story meets
the stakeholder's requirement before marking it Done.

**Agile** — An iterative approach to project management that delivers value in short
cycles (sprints), adapts to change, and emphasizes working products over comprehensive
plans. Contrast with waterfall (fixed scope, fixed timeline, single delivery).

**AIP Logic** — The Maven Smart System capability for configuring AI-driven workflow
automation and agent behaviors without writing code. Managed by TM-40B (AI Engineer).

**Backlog** — The prioritized list of all work items (user stories, tasks, defects) for
a project. Maintained by the PM. Groomed continuously as new requirements arrive or
priorities change.

**Blocker** — An impediment that prevents a team member from progressing on a story.
Identified at daily standup. Tracked as a Boolean flag on the Story object and visible
on the sprint board. The PM is responsible for resolving blockers, not just recording them.

**C2DAO** — Command and Control Data Architecture Office. The USAREUR-AF governance
authority for MSS platform configuration, enterprise Ontology design, and access decisions
that cross project boundaries.

**Change Management** — The process of planning and executing the transition of
operational users from an existing workflow to a new data product. Includes communication,
training, sponsor engagement, and adoption monitoring.

**Change Sponsor** — A peer-level advocate within an affected stakeholder group who
champions adoption of a new data capability. Not a trainer — a credible voice within
the organization that signals the change is endorsed.

**Daily Standup** — A 15-minute daily synchronization ceremony for the sprint team.
Three questions: What did I complete? What will I complete? What is blocking me?
Not a status meeting — a coordination mechanism.

**Data Audit** — A structured assessment of an input data source prior to ML model
development. Covers completeness, timeliness, historical depth, label availability, and
schema stability. PM gate before prototype authorization.

**Definition of Done (DoD)** — The PM-owned quality gate checklist for production
releases. All items must pass (or be formally waived) before a data product is deployed
to production. See Appendix B.

**Dependency** — A constraint where one story or deliverable cannot be completed until
another task or external input is available. Tracked as a Dependency Object in the project
tracker. Managed actively by the PM to prevent sprint-level blocks.

**Feature** — A discrete, user-facing capability of a data product. Composed of one or
more user stories. Features are prioritized in the backlog; stories are scheduled into sprints.

**Foundry** — The underlying Palantir platform on which the Maven Smart System (MSS) is
built. TM-40J personnel interact with Foundry primarily through Workshop, Ontology UI,
Pipeline Builder, and Contour.

**Kanban** — An Agile method that manages continuous flow of work using a visual board
with WIP limits, rather than fixed-length sprints. Used for sustainment and support work
where demand is continuous and variable.

**Model Card** — A documentation artifact for a deployed ML model. Contains: training
data description, algorithm, evaluation metrics, known failure modes, intended use cases,
and out-of-scope uses. Required for all production ML deployments under the DoD checklist.

**Model Drift** — Degradation of an ML model's production performance over time as
input data distribution shifts away from the training distribution. Detected through
production monitoring. Triggers a retraining review.

**MSS (Maven Smart System)** — The USAREUR-AF operational data and AI platform built
on Palantir Foundry. The platform within which all TM-40J project tracking, dashboards,
and data products are built and operated.

**Ontology** — The structured, semantic data model in Foundry that defines Object Types,
their properties, and the links between them. The foundation of all MSS Workshop
applications and Analytics. Governed by TM-40E (KM/Data Steward) at the enterprise level.

**OPDATA** — Operational data. Data generated by or supporting theater operations.
The primary source of requirements for MSS capability builds in USAREUR-AF.

**Product Backlog** — See Backlog.

**Product Owner** — In Scrum, the role responsible for backlog prioritization and
stakeholder representation. At USAREUR-AF, TM-40J TMs typically fulfill this role
alongside Scrum Master responsibilities.

**Production Ready** — A state in which a data product meets all Definition of Done
criteria and is deployable to operational users. Not a judgment — a checklist result.

**Retrospective** — A sprint ceremony conducted at the end of each sprint, for the
team only. Reviews what went well, what did not, and what to improve next sprint.
PM owns tracking and following up on retrospective action items.

**Risk Register** — The PM-maintained log of identified project risks, including
likelihood, impact, severity score, owner, mitigation, and status. Maintained as an
MSS Ontology Object and reviewed at every sprint planning session.

**Scrum** — An Agile framework using fixed-length sprints (typically 1-2 weeks) with
four ceremonies: Sprint Planning, Daily Standup, Sprint Review, and Retrospective.
Suited for data/AI projects with defined product outcomes and moderate team sizes.

**Scrum Master** — In Scrum, the role responsible for facilitating ceremonies, removing
blockers, and protecting the team from external disruption. At USAREUR-AF, TM-40J TMs
typically fulfill this role.

**Sprint** — A fixed-length development cycle (1 or 2 weeks) in Scrum. Each sprint has
a goal, a committed scope, and a deliverable product increment. Managed via the MSS
sprint board.

**Sprint Goal** — A one-sentence statement of what the team will demonstrate at the sprint
review. Set at sprint planning. The PM's primary alignment tool during the sprint.

**Sprint Review** — A sprint ceremony at the end of each sprint where the team demonstrates
completed work to stakeholders via live demo in MSS. Not a PowerPoint slide deck.

**Stakeholder** — Any person or organization with an interest in the outcome of a data
product. Includes operational users, commanding officers, and data governance stakeholders
(C2DAO, TM-40E).

**Story Points** — A unit of effort estimation for user stories. Often uses Fibonacci
sequence (1/2/3/5/8/13). Used to measure sprint velocity and forecast delivery timelines.
TM-40J tracks use T-shirt sizing (S/M/L/XL) as a simpler equivalent.

**Technical Debt** — Work deferred to meet a delivery deadline that must eventually be
completed to maintain product quality and operability. Examples: hardcoded values, missing
tests, undocumented transforms. PM manages tech debt as a reserved backlog capacity item.

**TM-40 Track** — Specialized capability track for data/AI professionals on MSS.
Tracks: TM-40A (ORSA), TM-40B (AI Engineer), TM-40C (ML Engineer), TM-40J (Technical PM),
TM-40E (KM), TM-40F (SWE). TM-40J coordinates across all tracks.

**UDRA** — Unified Data Reference Architecture, version 1.1 (February 2025). The Army's
authoritative data architecture guidance. Informs MSS data product design standards and
data governance practices.

**User Story** — A brief description of a feature from the perspective of the user who
will benefit from it. Format: "As a [user], I want [capability], so that [outcome]."
The primary unit of backlog work in Scrum.

**Velocity** — The average number of story points (or T-shirt size equivalents) a team
completes per sprint. Calculated after three or more sprints. The PM uses velocity to
forecast delivery timelines and plan release milestones.

**WIP Limit** — Work-in-progress limit. A Kanban discipline that caps the number of
stories a team member can have In Progress simultaneously. Enforces completion before
starting new work. Recommended: 2 per developer.

**Workshop** — The Foundry application builder tool. TM-40J PMs build sprint boards,
stakeholder-facing dashboards, and commander status products in Workshop. The primary
PM-facing tool for project tracking on MSS.

---

*TM-40J — Technical Manual: Program Manager (Technical), Maven Smart System*
*Headquarters, United States Army Europe and Africa, Wiesbaden, Germany*
*Army CIO Memo (April 2024) — Unified Data Reference Architecture v1.1 (February 2025)*
*UNCLASSIFIED — Distribution: Approved for public release; distribution is unlimited.*
