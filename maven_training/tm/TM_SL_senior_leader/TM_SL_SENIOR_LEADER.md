# TM-SL — SENIOR LEADER EXECUTIVE COURSE
## Maven Smart System (MSS) — USAREUR-AF

> **Forward:** This course gives battalion commanders, command sergeants major, and equivalent senior leaders the operational understanding of MSS required to lead formations that depend on data-driven decision-making. You will not build anything. You will learn what the platform produces, how data products affect your formation's readiness and operations, and how to guide your staff's use of data as a command function. TM-SL replaces TM-10 for O-5 / E-9+ personnel.
> **Prereqs:** None. This course assumes senior-level operational experience and familiarity with Army doctrine. No technical background required.
> *HQ USAREUR-AF · v1.0 · 2026 · DISTRIB: USG only · AUTH: C2DAO/UDRA v1.1*

---

# CHAPTER 1 — WHY THIS COURSE EXISTS

## 1-1. Senior Leader Manual

You already know how to fight. You already know how to read an operations order, assess readiness, and make decisions under uncertainty. What you may not know is how the data environment underneath those decisions has changed — and what that means for how you lead.

MSS is not an IT project. It is the command's primary instrument for converting raw operational data into the information your staff uses to brief you, the products your subordinate commanders use to plan, and the visibility you need to maintain decision advantage across the theater. The CG USAREUR-AF has stated directly: **"The race to harness live data will determine who wins the next war."**

Your formation already uses MSS. Your staff produces data products from it. Your subordinate units consume those products. The question is whether you — as the commander or senior enlisted leader — understand enough about what the platform does to guide that process, ask the right questions, and make informed resourcing decisions about your data workforce.

That is what this course addresses.

## 1-2. What This Course Is

TM-SL is a 1-day instructor-led course that produces senior leaders who can:

1. Articulate what MSS does for their formation and why it matters
2. Evaluate the data products their staff produces — not technically, but operationally
3. Guide their formation's data posture through informed resourcing, prioritization, and governance decisions
4. Ask the questions that drive data quality, timeliness, and relevance
5. Understand the training pipeline that qualifies their data workforce

**TM-SL replaces TM-10 for O-5 and E-9+ personnel.** Senior leaders do not attend TM-10. TM-SL is their entry point and terminal qualification — there is no progression to TM-20 or beyond. If a senior leader wants to build, they are welcome to enroll in TM-10 and proceed through the standard pipeline. TM-SL does not grant TM-10 credit.

## 1-3. What This Course Is NOT

- It is not a platform navigation course — you will see the platform, but you will not operate it
- It is not a data literacy primer — you are expected to understand what data is and why it matters
- It is not a policy document — policy lives in the governance chain (Chapter 5)
- It is not a substitute for TM-10 in the standard training pipeline — TM-10 remains the entry point for all non-SL personnel
- It does not qualify you to build, modify, or administer anything on the platform

## 1-4. Scope Boundaries with TM-10

TM-10 teaches personnel how to use MSS: log in, navigate, read dashboards, filter data, submit forms, export products, and handle classification. TM-SL teaches none of that. There is no overlap.

TM-SL assumes you have staff who do TM-10-level work. Your job is to understand what those staff produce, why it matters, and how to make it better through command emphasis and informed guidance.

| TM-10 Covers | TM-SL Covers Instead |
|---|---|
| How to log in and navigate the platform | Why the platform exists and what it produces for your formation |
| How to read and filter dashboards | How to evaluate whether a data product answers the operational question |
| How to submit forms and execute actions | How to direct your staff to prioritize data inputs that matter |
| How to export data and handle classification | How to set expectations for data quality, timeliness, and governance |
| How to troubleshoot access issues | How to resource the training pipeline that builds your data workforce |

## 1-5. Governing References and Policy Context

The following doctrine and policy documents establish the authority, framework, and standards under which MSS operates. TM-10 introduces these references at the operator level. At TM-SL, you need to know them at the level required to make resourcing and governance decisions.

**Governing Doctrine:**

- **ADP 3-13, Information** — Establishes information as a joint function and combat power. This is the doctrinal foundation for treating data as a command function, not an IT function. Every MSS data product exists to deliver the information advantage described in ADP 3-13.
- **ADP 6-0, Mission Command** — Establishes that commanders drive the operations process through understanding, visualizing, describing, directing, leading, and assessing. MSS directly supports three of these (understanding, directing, assessing). Chapter 3 of this course applies ADP 6-0 to data products.
- **ADP 5-0, The Operations Process** — Defines the commander's role in planning, preparation, execution, and assessment. Data products from MSS support continuous assessment during execution — the phase where most formations lose visibility. The decision cycle in Chapter 3 maps to the assess-decide-direct loop in ADP 5-0.
- **AR 25-1, Army Information Technology (Jul 2019)** — The regulatory foundation for Army data governance. Establishes the VAUTI (Visible, Accessible, Understandable, Trustable, Interoperable) data quality principles, since expanded to VAULTIS-A (adding Linked, Secure, Auditable). Chapter 5 of this course applies the full VAULTIS-A framework as your evaluation standard for data products.
- **AR 350-1, Army Training and Leader Development** — Governs training policy and leader development. The training pipeline described in Chapter 4 (TM-10 through TM-50) is structured under AR 350-1 standards.
- **FM 7-0, Training** — Unit training management procedures. Provides the context for how TM-SL and the broader MSS training pipeline integrate with your formation's training plan.

**DoD and Army Strategic References:**

> The following are strategic guidance documents — not doctrine — that inform MSS operations and governance.

- **DoD Data Strategy (October 2020)** — Foundation for the VAUTI/VAULTIS-A principles used in Chapter 5. Establishes the federal mandate that data be treated as a strategic asset.
- **Army Data Plan (2022)** — 11 strategic objectives for Army data transformation. MSS implements several of these at the theater level.
- **Army Cloud Plan (2022)** — Zero Trust architecture, secure development, data-driven decisions.
- **Army CIO Data Stewardship Policy (April 2, 2024)** — Establishes the stewardship hierarchy and data chain of responsibility shown in Chapter 5's governance chain.

NOTE: The USAREUR-AF C2DAO office implements and enforces Army data policy within this command. For governance questions, access exceptions, or policy issues, contact C2DAO through your chain of command.

---

# CHAPTER 2 — THE PLATFORM AND WHAT IT PRODUCES

## 2-1. MSS Architecture at the Senior Leader Level

MSS is built on Palantir Foundry — a secure, web-based platform authorized for Army use. You do not need to understand Foundry's internals. You need to understand the five layers your formation interacts with, because each layer is where different problems show up and different people fix them.

**Table 2-1. The Five Layers**

| Layer | What It Does | Who Works Here | What Goes Wrong Here |
|---|---|---|---|
| **Ingestion** | Brings data in from Army systems (GCSS-A, DCPDS, MEDPROS, unit feeds) | TM-30/40 engineers | Stale feeds, broken connections, missing source systems |
| **Storage & Modeling** | Organizes raw data into structured, queryable formats | TM-30/40 engineers | Poor naming, duplicate records, broken relationships between datasets |
| **Transformation** | Cleans, links, and enriches data for consumption | TM-20/30 builders | Bad business logic, incorrect calculations, filters that hide real data |
| **Application** | Dashboards, forms, reports — what your staff sees | TM-20 builders | Misleading visualizations, missing filters, stale data displayed as current |
| **AI/Analysis** | AIP queries, pattern detection, automated alerts | TM-40H/M engineers | Outputs that look authoritative but reflect training data, not ground truth |

> **Key point for leaders:** Problems at lower layers propagate upward invisibly. A dashboard that shows 95% equipment readiness may be correct according to the data it has — but if the ingestion layer lost connection to GCSS-A three days ago, that 95% is three days stale. Knowing which questions to ask about data freshness and source integrity is a command function.

## 2-2. Data Products Your Formation Produces

A data product is any output from MSS that supports a decision, a report, or an operational process. Your formation likely produces and consumes dozens of these daily without calling them "data products."

**Table 2-2. Common Data Product Types**

| Product Type | Example | Who Builds It | Who Consumes It |
|---|---|---|---|
| **Readiness dashboard** | Equipment OR rates by subordinate unit, updated daily | TM-20 builder | CDR, XO, S3, S4 |
| **Personnel tracker** | Strength accounting across the formation | TM-20 builder | CSM, S1, CDR |
| **Operational report** | SITREP data aggregated from subordinate submissions | TM-20/30 builder | CDR, higher HQ |
| **Logistics status** | Maintenance backlog, parts on order, deadline rates | TM-20 builder | S4, SPO, CDR |
| **WFF analysis** | Intel threat picture, fires target set, protection posture | TM-40A–F specialist | WFF staff, CDR |
| **Automated alert** | Threshold-based notification (e.g., readiness drops below 80%) | TM-30/40 engineer | CDR, staff principal |
| **AI-generated summary** | AIP query response synthesizing multiple data sources | TM-40H/M engineer | Staff, CDR |

Every one of these products is only as good as the data behind it, the logic that transforms it, and the question it was built to answer.

## 2-3. The Platform in Practice — What You Will See

During this course you will observe a live MSS environment. You will not operate it, but you will see:

- **Workshop applications** — the dashboards and forms your staff builds. These are the most common data product type. You will see how filters work, how data refreshes, and how a single dashboard can show different views of the same data.
- **Contour** — an analysis tool that lets users slice data by any dimension. You will see how a staff officer might use this to answer an ad hoc question from the commander.
- **Object Explorer (Quiver)** — a tool for examining individual data records and their relationships. You will see how an NCO might trace a piece of equipment from a readiness report back to its source record.
- **AIP (AI Platform)** — the AI assistant interface. You will see a query submitted and a response generated, and you will understand why AI outputs require human validation before operational use.

> **NOTE:** You are seeing these tools so you understand what your staff works with. You are not expected to use them yourself. If you want hands-on qualification, enroll in TM-10.

---

# CHAPTER 3 — HOW DATA PRODUCTS IMPACT YOUR FORMATION

## 3-1. Data as a Command Function

Per ADP 6-0 (Mission Command) and ADP 5-0 (The Operations Process), commanders drive the operations process through understanding, visualizing, describing, directing, leading, and assessing. MSS directly supports three of these:

- **Understanding** — MSS consolidates data from across the formation into a common operating picture. Without it, understanding depends on verbal reports, emails, and spreadsheets that are always incomplete and frequently contradictory.
- **Directing** — Data products enable commanders to issue informed guidance. A readiness dashboard that shows one battalion at 68% OR while the rest sit above 90% tells you where to focus maintenance effort — without waiting for the weekly BUB.
- **Assessing** — Continuous assessment requires continuous data. MSS provides it. The difference between "I think we're ready" and "the data shows we are ready, and here is where we are not" is the difference between assumption and decision advantage.

**The implication:** Data is not an IT function. It is a command function. The quality of data products in your formation is a direct reflection of command emphasis — or the lack of it.

## 3-2. How Poor Data Posture Degrades Operations

Data problems rarely announce themselves. They accumulate quietly until a decision is made on bad information. These are the patterns senior leaders need to recognize:

**Table 3-1. Data Failure Patterns**

| Pattern | What It Looks Like | What Causes It | What the CDR Can Do |
|---|---|---|---|
| **Stale data displayed as current** | Dashboard shows 95% readiness but the feed died 72 hours ago | Broken ingestion; no freshness indicator on the dashboard | Direct builders to display "last updated" timestamps on every product; ask "when was this data pulled?" |
| **Correct data, wrong question** | Beautiful dashboard that answers a question nobody is asking | Builder built what was easy, not what was needed | Define commander's priority information requirements (PIRs) for data products, just as you would for intel |
| **Orphaned products** | Dashboards that nobody uses but consume builder time to maintain | No product lifecycle management | Direct periodic review: if nobody uses it, sunset it; free the builder for priority work |
| **Shadow data** | Staff maintains a separate Excel tracker because they don't trust MSS | MSS product doesn't match what staff needs, or data quality issue eroded trust | Investigate why. Fix the MSS product or fix the data quality. Dual-tracking wastes time and creates discrepancies |
| **AI hallucination treated as fact** | AIP output cited in a brief as though it were a verified data source | No human validation step between AI output and operational use | Establish unit SOP: AI outputs are drafts, not products. Every AIP response requires human verification before briefing |
| **Single point of failure** | One TM-20 builder owns all the unit's dashboards; that person PCSes | No cross-training, no documentation, no succession plan | Treat builder capacity like any other critical MOS — plan for turnover, cross-train, document |

## 3-3. Commander's Data PIRs

Just as you define Priority Intelligence Requirements (PIRs) for your S2, you should define Priority Data Requirements for your formation's data products.

A data PIR answers: **What information do I need, from what source, at what frequency, to make what decision?**

**Table 3-2. Example Commander's Data PIRs**

| # | Data PIR | Source | Frequency | Supports |
|---|---|---|---|---|
| 1 | Equipment readiness by subordinate unit | GCSS-A via MSS | Daily refresh | Maintenance prioritization, cross-leveling |
| 2 | Personnel strength by MOS and grade | DCPDS via MSS | Daily refresh | Manning decisions, task org adjustments |
| 3 | MEDPROS compliance rate by unit | MEDPROS via MSS | Weekly refresh | Medical readiness, deployment eligibility |
| 4 | Open maintenance work orders > 30 days | GCSS-A via MSS | Daily refresh | Maintenance backlog management |
| 5 | Training qualification status by individual | Unit input via MSS | As updated | Readiness assessment, training prioritization |

If you have not told your staff what data products you need, do not be surprised when the products they build do not match your requirements.

## 3-4. Guiding the Process — What Senior Leaders Control

You do not build data products. But you control the conditions that determine whether data products are useful:

**1. Prioritization.** Your builders have limited capacity. If you do not prioritize which data products matter most, they will build what is easiest or what the loudest staff section demands. Command guidance on data priorities is no different from command guidance on training priorities.

**2. Data discipline at the point of entry.** The most common source of bad data is bad input. If your formations are not entering data accurately and on time into systems of record (GCSS-A, DCPDS, unit trackers), no amount of platform engineering will fix the output. Data discipline is a leadership function — enforce it the same way you enforce maintenance standards.

**3. Feedback loops.** Your builders need to know whether their products are useful. If a dashboard is wrong, tell them. If it is missing something, tell them. If it answers the wrong question, tell them what question to answer instead. Builders who never hear from their consumers build in a vacuum.

**4. Protection of builder time.** Building and maintaining data products requires focused, uninterrupted time. Builders who spend their days on staff duties, additional duties, and taskings will produce fewer and lower-quality data products. This is a resourcing decision only commanders can make.

**5. Governance enforcement.** Data governance — naming standards, access controls, classification markings, product lifecycle management — is boring and essential. If you do not enforce it, your data environment will degrade into an ungoverned mess of duplicate dashboards, orphaned datasets, and access control violations. Chapter 5 covers governance in detail.

---

# CHAPTER 4 — THE TRAINING PIPELINE

## 4-1. How Your People Get Qualified

The MSS training pipeline is a progressive qualification sequence. Understanding it lets you plan training calendars, make resourcing decisions, and set realistic expectations for when your formation will have the data capability you need.

**Table 4-1. Training Pipeline Overview**

| Level | Title | Duration | Who | What They Can Do After |
|---|---|---|---|---|
| **TM-SL** | Senior Leader | 1 day | O-5 / E-9+ | Lead formations that use MSS; evaluate data products; guide data posture |
| **TM-10** | Maven User | 1 day | All other personnel | Use MSS as a consumer: navigate, filter, export, submit |
| **TM-20** | Builder | 3 days | Designated builders | Build Workshop apps, basic dashboards, simple pipelines (no code) |
| **TM-30** | Advanced Builder | 5 days | Advanced builders | Complex pipelines, governance, data modeling, enterprise ontology |
| **TM-40A–F** | WFF Tracks | 3 days each | WFF staff (S2, FSE, S4, etc.) | Apply MSS to their warfighting function |
| **TM-40G–O** | Specialist Tracks | 5 days each | Data professionals | ORSA, AI, ML, PM, KM, SWE, UX, PE specializations |
| **TM-50G–O** | Advanced Specialist | 5 days each | Senior specialists | Advanced application of specialist skills |

**Prereq chain:**
```
TM-SL (senior leaders — terminal, no further progression)

TM-10 (all other personnel)
  └── TM-20
        └── TM-30
              ├── TM-40A–F (WFF tracks)
              └── TM-40G–O → TM-50G–O (specialist tracks)
```

> **NOTE:** TM-SL does not feed into the TM pipeline. A senior leader who completes TM-SL and later wants hands-on qualification enrolls in TM-10 and progresses normally.

## 4-2. Foundry Bootcamp (FBC)

The Foundry Bootcamp is a quarterly 5-day supervised build event outside the TM chain. A TM-20-qualified builder brings a command-approved operational project and builds it with SME support in the room.

FBC does not grant TM-30 credit or unlock TM-40. It exists because some builders learn best when solving a real problem under pressure. It is an excellent use of builder time when your formation has a specific project that needs to get built.

**What the commander needs to know about FBC:**
- Prereq: TM-20 Go + command-approved project
- The project must have a named consumer and a specific output
- Command sponsorship (supervisor signature) is required
- FBC seats are limited — submit enrollment requests early

## 4-3. Resourcing the Pipeline

Building a capable data workforce requires the same deliberate resourcing as any other training line:

| Decision | Consideration |
|---|---|
| **How many builders?** | Minimum viable: 2 TM-20 builders per BN, 4–6 per BDE. More is better. Plan for PCS turnover. |
| **When to train?** | TM-10 can run locally. TM-20+ requires coordination with C2DAO for instructor support and training environment access. Build into your training calendar, not your white space. |
| **Who to send?** | Identify personnel with aptitude and interest. Forcing someone into a builder role produces poor results. Look for NCOs and officers who already maintain spreadsheets, trackers, or databases — they have the instinct. |
| **How to retain capability?** | Cross-train. Document. Succession plan. If one person owns all your dashboards and that person PCSes, you lose everything they built unless someone else can maintain it. |
| **How to protect builder time?** | Builders who are also the S6 NCOIC, the UPL, and the key control officer will not produce quality data products. Prioritize and protect their time accordingly. |

## 4-4. What "Go" Means for Your Formation

When a Soldier completes a TM level, they receive a Go qualification recorded in the training management system. What that means operationally:

- **TM-10 Go** — This person can use MSS. They can find data, read dashboards, submit information, and export products. They cannot build or modify anything.
- **TM-20 Go** — This person can build. They can create Workshop dashboards, set up basic data pipelines, and configure forms. They are your unit-level data product developers.
- **TM-30 Go** — This person can design. They can build complex pipelines, work with the enterprise ontology, and handle governance-level configuration. They are your formation's data architects.
- **TM-40 Go** — This person is a functional or technical specialist. They apply MSS to a specific warfighting function or technical domain at a professional level.

When you see a data product from your staff, knowing who built it tells you what level of sophistication and governance went into it.

---

# CHAPTER 5 — GOVERNANCE AND YOUR ROLE IN IT

## 5-1. What Governance Means for Senior Leaders

Data governance is the set of rules that keeps your data environment clean, secure, and trustworthy. You do not execute governance — your data stewards and builders do. But you enforce it the same way you enforce maintenance discipline: through standards, inspections, and consequences.

Governance in MSS covers:

- **Naming standards** — Every object, dataset, and application follows a naming convention. Without this, your data environment becomes an unsearchable mess within months.
- **Access controls** — Who can see what data, and who can modify it. This is a classification and need-to-know enforcement mechanism.
- **Data quality** — Are records accurate, complete, and current? Who is responsible for correcting errors?
- **Product lifecycle** — When a dashboard is no longer needed, who retires it? Orphaned products waste builder time and confuse users.
- **Classification handling** — MSS handles data at multiple classification levels. Mishandling classification in data products is a security violation.

## 5-2. The Governance Chain

```
Army CIO / Mission Area Data Officers (MADOs)
        ↓
DoD Data Strategy (VAULTIS-A framework)
        ↓
Army CIO Data Stewardship Policy (April 2, 2024)
        ↓
USAREUR-AF Command Chief Data & Analytics Officer (C2DAO)
        ↓
Functional Data Managers (by domain: personnel, logistics, ops)
        ↓
Unit Data Stewards
        ↓
MSS Users / Builders
```

**Your role:** You own the governance posture of your formation. Your unit data steward executes governance on your behalf. If you do not have a designated data steward, designate one. If your data steward is not empowered to enforce standards, empower them.

## 5-3. Governance Red Flags

These are the indicators that your formation's data governance is breaking down:

**Table 5-3. Governance Red Flags**

| Red Flag | What It Means | Action |
|---|---|---|
| Multiple dashboards showing different numbers for the same metric | Naming/versioning breakdown; no single source of truth | Direct data steward to identify the authoritative product and sunset duplicates |
| Staff maintaining Excel trackers alongside MSS | Trust deficit in the platform or a gap in available products | Investigate root cause; fix the MSS product or build the missing one |
| Nobody knows who built a dashboard or when it was last updated | No product ownership or lifecycle management | Implement product registry; assign owners to every active product |
| Access requests taking weeks | Governance process is a bottleneck, not an enabler | Review and streamline the access request workflow |
| Builders making changes without review | No change management process | Implement peer review for production data products |
| Classification markings missing or inconsistent on data products | Security violation in progress | Stop. Fix immediately. Retrain. |

## 5-4. The VAUTI / VAULTIS-A Framework

The DoD Data Strategy (October 2020) introduced the VAUTI framework — codified in AR 25-1 — to describe the attributes of well-governed data. Subsequent Army data governance guidance expanded VAUTI to **VAULTIS-A** by adding three dimensions: **Linked** (data connected across systems and domains), **Secure** (data protected commensurate with its sensitivity), and **Auditable** (full provenance and change history maintained for accountability). As a senior leader, these eight attributes are your checklist for evaluating any data product:

| Attribute | Question to Ask |
|---|---|
| **Visible** | Can the people who need this data find it? |
| **Accessible** | Can authorized users get to it without unnecessary barriers? |
| **Understandable** | Can a consumer interpret this data without calling the builder? |
| **Linked** | Is this data connected to related data across systems and domains? |
| **Trusted** | Is the data accurate, current, and from a verified source? |
| **Interoperable** | Can this data be combined with data from other systems and shared with partners? |
| **Secure** | Is the data protected commensurate with its sensitivity and classification? |
| **Auditable** | Is the data's provenance and change history maintained for accountability and compliance? |

If a data product fails any of these eight, it has a governance problem that needs command attention.

> **NOTE:** Older references use VAUTI (5 attributes) or VAULTIS (7 attributes). VAULTIS-A (8 attributes) is the current standard. When evaluating data products, apply the full VAULTIS-A framework.

---

# CHAPTER 6 — HOW DATA PROJECTS WORK

## 6-1. Agile in 60 Seconds

Data projects do not follow the traditional Army acquisition model. They follow an agile framework — a method of building in short, iterative cycles rather than one long plan-then-execute sequence. You need to understand the basics because your data professionals work this way, and fighting it will slow them down.

**Core concepts:**

| Term | What It Means |
|---|---|
| **Sprint** | A short work cycle (typically 1–2 weeks) where the team commits to a specific set of deliverables |
| **Backlog** | The prioritized list of everything that needs to be built, ordered by importance |
| **Increment** | A working piece of the product delivered at the end of each sprint — not a briefing, not a plan, but a functional thing |
| **Standup** | A short daily check-in (10–15 min) where the team reports what they did, what they are doing, and what is blocking them |
| **Retrospective** | An after-action review at the end of each sprint — what worked, what did not, what to change |

**Why agile works for data projects:** Data requirements are rarely stable. The commander asks a question, the builder builds a product, the commander sees it and asks a better question, the builder refines. This cycle of build-show-refine is the agile loop. Trying to define every requirement up front (waterfall) produces products that answer yesterday's questions.

**What this means for you as a leader:**
- Expect to see working products early and often — not polished, but functional
- Give feedback immediately when you see a product, even if it is "this is wrong" — that feedback is the input for the next sprint
- Do not wait for a final product before engaging. If you wait, you will get what the builder guessed you wanted
- Accept that the first version will not be perfect. That is by design. The third version will be significantly better because it incorporated your feedback

## 6-2. Why a Roadmap, Not a POAM

Senior leaders are familiar with the Plan of Action and Milestones (POAM) — a document that lists tasks, responsible parties, and due dates in a linear sequence. POAMs work well for compliance actions, inspection findings, and regulatory requirements. They do not work well for data projects.

**Why POAMs fail for data work:**

| POAM Assumption | Data Project Reality |
|---|---|
| Requirements are known and stable | Requirements evolve as the commander sees early products and refines the question |
| Tasks are sequential and predictable | Data work is iterative — discovery, build, feedback, rebuild |
| Completion = done | Data products require ongoing maintenance; "done" is a myth |
| Fixed timeline drives accountability | Artificial deadlines on discovery work produce rushed, low-quality products that require rework |
| Single deliverable at the end | Value should be delivered incrementally, not all at once at the end |

**Use a roadmap instead.** A roadmap is a prioritized view of what the team plans to deliver over time, organized by outcome (not task), with flexibility built in.

**Table 6-1. POAM vs Roadmap**

| Dimension | POAM | Roadmap |
|---|---|---|
| **Organizes by** | Tasks and dates | Outcomes and priorities |
| **Timeframe** | Fixed milestones | Rolling horizons (now / next / later) |
| **Detail level** | Every step pre-defined | Near-term detailed, far-term directional |
| **Handles change by** | Rewriting the POAM | Reprioritizing the backlog |
| **Accountability** | Did you hit the date? | Did you deliver value? |
| **Update frequency** | When something slips | Every sprint (continuous) |

**What a good data roadmap looks like:**
- **Now (this sprint / next 2 weeks):** Specific deliverables the team has committed to
- **Next (next 1–2 sprints):** Planned work that is scoped and ready to build
- **Later (3+ sprints out):** Directional priorities that will be refined as the team learns more

> **Key point:** When your data professionals present a roadmap instead of a POAM, they are not avoiding accountability — they are being honest about the nature of the work. Hold them accountable for sprint commitments and outcomes, not for adherence to a plan that will be wrong by week three.

---

# CHAPTER 7 — WORKING WITH DATA PROFESSIONALS

## 7-1. Who They Are

Your formation's data professionals come from varied backgrounds. Some are 17-series Soldiers with formal training. Some are 25-series NCOs who taught themselves to build. Some are warrant officers or Civilians with deep technical expertise. Some are infantry or logistics Soldiers who happened to be good with data and got pulled into the role.

Regardless of background, data professionals share a common trait: they solve problems by building things. Their output is not a briefing or a memo — it is a functioning product. Treat them accordingly.

## 7-2. How to Get the Best Work Out of Them

| Do This | Not This | Why |
|---|---|---|
| Tell them the problem you need solved | Tell them exactly what to build | They understand the platform's capabilities better than you do; defining the solution limits them to your imagination |
| Give feedback on the product, frequently | Wait until the end to weigh in | Early feedback prevents wasted effort; silence is interpreted as approval |
| Protect their build time | Task them with additional duties | A builder who spends 20% of their time building produces 20% of the output. This is arithmetic, not opinion |
| Ask for a demo, not a brief | Ask for a PowerPoint about the project | The product is the proof. If they are building slides instead of products, something is wrong |
| Set priorities clearly | Let every staff section compete for their time equally | Without command priority, builders serve whoever is loudest. That is rarely the right allocation |
| Invest in their training pipeline | Expect them to figure it out | TM-20 → TM-30 → TM-40 is a deliberate progression. Skipping steps produces builders who can operate tools but cannot design solutions |

## 7-3. How to Talk to Them

Data professionals will often explain things in technical terms. You do not need to learn their language — they need to learn yours. But meeting halfway is efficient.

**Terms worth knowing:**

| Term | Plain English |
|---|---|
| **Object type** | A category of thing the platform tracks (e.g., "Equipment Item," "Soldier," "Work Order") |
| **Pipeline** | An automated process that moves data from a source system into MSS — like a pipe that flows data from GCSS-A into a dashboard |
| **Ontology** | The structure that defines how data is organized and related — think of it as the filing system for all data in MSS |
| **Dashboard** | A visual display of data — the product your staff reads |
| **Widget** | A single component on a dashboard (one chart, one table, one map) |
| **Data freshness** | How recently the data was updated from the source system |
| **Transformation** | A step that changes raw data into something useful (e.g., converting a date format, calculating a readiness percentage) |
| **AIP** | The AI assistant built into the platform — can query data and generate summaries |

**When they say something you do not understand, ask.** They would rather explain once than build the wrong thing because you nodded through a brief.

## 7-4. Common Friction Points

| Friction | What Is Actually Happening | Resolution |
|---|---|---|
| "They keep changing what they're building" | They are iterating based on feedback (or lack of clear requirements) | Define the problem clearly up front; expect iteration on the solution |
| "They won't give me a timeline" | They are uncomfortable committing to a date for work that involves discovery | Ask for sprint commitments instead: "What will you have by end of this sprint?" |
| "They spend too long on infrastructure and not enough on dashboards" | They are fixing technical debt that makes future work faster and more reliable | Ask them to explain the tradeoff. If the infrastructure work prevents three future failures, it is worth it |
| "They built something nobody asked for" | They saw a problem and tried to solve it, or misunderstood the requirement | Establish a prioritization process: builders work from the backlog, not from inspiration |
| "The product looks different from what I asked for" | Their interpretation of the requirement differed from yours | Review products early and often. First sprint delivery should be a check on shared understanding |

---

# CHAPTER 8 — ASKING THE RIGHT QUESTIONS

## 8-1. Why This Chapter Exists

The most impactful thing a senior leader can do for their formation's data posture is ask better questions. Not technical questions — operational questions that force rigor.

Most bad data products survive because nobody with authority asked the hard questions. This chapter gives you the questions.

## 8-2. Questions About Data Products

When your staff briefs you from a data product, ask:

| Category | Questions |
|---|---|
| **Source** | Where does this data come from? Which system of record? When was it last refreshed? |
| **Completeness** | Does this include all subordinate units? Are any units not reporting? What is the reporting compliance rate? |
| **Accuracy** | How do we know this is correct? Has anyone spot-checked the platform data against the system of record? |
| **Timeliness** | How old is this data? Is "as of" displayed on the product? Would a 24-hour delay change any of these numbers materially? |
| **Context** | What does this number mean operationally? Is 85% good or bad? Compared to what? Compared to when? |
| **Consumption** | Who else uses this product? Does the S4 see the same data the S3 sees? Are we all working from the same source? |

## 8-3. Questions About the Data Workforce

| Category | Questions |
|---|---|
| **Capacity** | How many qualified builders do we have? How many do we need? What is our bench depth if one PCSes? |
| **Utilization** | Are builders spending their time building, or are they consumed by other duties? What percentage of their time is protected for data work? |
| **Training** | Who is in the pipeline? When is the next TM-20 class? Are we sending the right people? |
| **Sustainment** | Who maintains the products we already have? Is maintenance consuming all builder capacity, leaving no room for new products? |

## 8-4. Questions About AI Outputs

AI-generated content (AIP queries, automated summaries, pattern detection) is increasingly present in data products. Senior leaders must treat AI outputs differently from verified data:

| Rule | Rationale |
|---|---|
| **AI outputs are drafts, not products** | AIP can synthesize across multiple datasets quickly, but it can also hallucinate — generate plausible-sounding information that is factually wrong |
| **Always ask: "What data did this draw from?"** | An AI summary is only as good as its source data. If the source data is stale or incomplete, the summary inherits those flaws |
| **Never cite AI output as a verified source in operational products** | AI output requires human verification. If your S2 cites an AIP response in a SITREP without verification, that is an analytical failure |
| **AI is a force multiplier, not a replacement for analysis** | Use it to generate drafts, identify patterns, and accelerate research. Do not use it to replace the human judgment that turns information into intelligence |

---

# CHAPTER 9 — AFTER THIS COURSE

## 9-1. What You Should Do Next

TM-SL is terminal — there is no TM-SL-20 or progression requirement. But the course is only useful if you apply what you learned. Here is a practical checklist:

**Within 1 week:**
- [ ] Identify your unit data steward by name. If you do not have one, designate one.
- [ ] Ask your staff: "What data products do we produce and consume? Show me the list."
- [ ] Ask your staff: "When was the last time someone verified the data in our top 3 dashboards against the system of record?"

**Within 30 days:**
- [ ] Define 3–5 Commander's Data PIRs (see Table 3-2 for format)
- [ ] Review your builder manning: how many TM-20+ qualified personnel do you have, and is that enough?
- [ ] Schedule your next round of TM-10/TM-20 training for personnel who need qualification

**Within 90 days:**
- [ ] Conduct a data product review: which products are active, which are orphaned, which are missing?
- [ ] Assess governance posture using the red flags in Table 5-3
- [ ] Establish a feedback mechanism between data product consumers (your staff) and builders

## 9-2. Continuation Paths

| If You Want To... | Path |
|---|---|
| Get hands-on with the platform | Enroll in TM-10 and proceed through the standard pipeline |
| Send builders to advanced training | Ensure TM-20 Go → enroll in TM-30 → select TM-40 track |
| Get a project built quickly | Submit a FBC project for the next quarterly bootcamp (requires TM-20 builder + command-approved project) |
| Engage with C2DAO on data strategy | Contact your Functional Data Manager or the C2DAO directly |

## 9-3. Points of Contact

| Role | Responsibility |
|---|---|
| **Unit Data Steward** | First stop for all data questions, access requests, product issues |
| **Functional Data Manager** | Domain-level governance (personnel, logistics, operations) |
| **C2DAO** | Command-level data strategy, training coordination, enterprise governance |
| **MSS Administrator** | Account provisioning, access issues, platform availability |

---

*USAREUR-AF Operational Data Team*
*TM-SL Senior Leader Executive Course | Version 1.0 | March 2026*
