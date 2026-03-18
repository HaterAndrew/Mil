# CONCEPTS GUIDE — TM-40G COMPANION — OPERATIONS RESEARCH / SYSTEMS ANALYSIS (ORSA) · MAVEN SMART SYSTEM (MSS)

> **BLUF:** The ORSA's primary output is a commander's decision product. Every other capability — modeling, visualization, data access — exists in service of that product.
> **Purpose:** Develops the analytical mental models required to operate effectively as an ORSA on MSS. Read before beginning TM-40G task instruction.
> *HQ USAREUR-AF · v1.0 · 2026 · DISTRIB: USG only*

---

## SECTION 1 — THE ORSA'S JOB ON MSS

**BLUF:** The ORSA's primary output is a commander's decision product. Every other capability — modeling, visualization, data access — exists in service of that product.

### 1-1. Role Distinctions

MSS supports several analyst roles. The boundaries are not organizational formalities — they shape how you frame every problem, what tools you reach for, and how you present results.

| Role | Primary Output | Success Condition |
|---|---|---|
| Data Engineer | Reliable, validated dataset arriving at the right place on schedule | Clean ingestion, on-time delivery |
| ML Engineer | Trained, validated, deployed algorithm that generalizes to new inputs | Model predicts correctly at scale |
| **ORSA** | **Decision-ready recommendation or structured quantitative analysis enabling a specific commander's decision** | **Commander can decide with confidence** |

The platform does not enforce these boundaries. Foundry gives an ORSA access to datasets, notebooks, transforms, ontology objects, and dashboards. The fact that you can do everything does not mean you should. ORSA time is most valuable closest to the commander. Guard it accordingly.

> **NOTE — Assessment Framework (TM-40G Section 1-7, Table 1-2):** TM-40G now includes a formal MOE/MOP/indicator assessment framework with worked examples. Review Table 1-2 for the standard indicator taxonomy before building any assessment product.

### 1-2. What "Decision Product" Means

A decision product answers a specific question, makes uncertainty explicit, and names the action it enables. It is not a visualization, a model output dump, or a dashboard with no narrative.

**Required elements of a decision product:**
- A BLUF stating the analytical finding in one sentence
- A quantified answer with explicit bounds or confidence characterization
- A "so what" connecting the finding to a specific command action or decision point
- A section documenting data sources, assumptions, and limitations

A V Corps logistics brief showing C-rating trends for the last 90 days is a visualization. The same brief that attributes a trajectory to specific failure modes, forecasts outcomes under two support scenarios, and recommends a decision point by a named date — that is a decision product.

### 1-3. How MSS Fits the ORSA Workflow

MSS connects three capabilities ORSA work requires:

**Integrated operational data.** Unit readiness, logistics status, personnel accountability, exercise outcomes, and sustainment data previously requiring separate data calls are available through the Ontology. An ORSA analyzing DEFENDER exercise throughput at Grafenwoehr can join unit readiness records, equipment arrival timelines, and maintenance work orders in a single Code Workspace — without six separate RFIs.

**Reproducible analytical environment.** Code Workspaces persist. Datasets are versioned. If the G2 asks why your threat assessment changed between MDMP cycles, you can trace the answer to a specific dataset update. This reproducibility is an operational accountability requirement.

**Product delivery channel.** Contour dashboards and Quiver reports allow ORSA products to reach commanders through MSS against current data. A readiness forecast built Tuesday is outdated by Friday's maintenance cycle. A Contour dashboard built on the same Ontology objects is current every time the commander opens it.

---

## SECTION 2 — HOW TO DECOMPOSE A COMMANDER'S QUESTION

**BLUF:** Most ORSA failures begin at problem framing, not at modeling. Apply the decomposition framework before opening a Code Workspace.

### 2-1. The Decomposition Framework

Commanders ask operational questions, not statistical questions. "Are we ready for DEFENDER?" is not a statistical question — it is an operational judgment that, properly decomposed, resolves into answerable analytical questions.

The framework has four steps, in sequence:

```
DECISION → REQUIRED INFORMATION → AVAILABLE DATA → APPROPRIATE METHOD
```

Skipping from DECISION directly to METHOD — "the commander asked about readiness, so I'll build a regression model on C-ratings" — is the most common ORSA failure mode on MSS. The framework forces you to check data availability before committing to a method, and to validate that the information you can produce actually supports the decision the commander faces.

| Step | Action | Output |
|---|---|---|
| **1 — DECISION** | State the specific decision, decision-maker, choice space, and deadline | "V Corps commander must decide by 15 April whether to request additional Class IX pre-positioning for DEFENDER or accept risk." |
| **2 — REQUIRED INFORMATION** | List what the commander needs to decide — independently of what data exists | Projected readiness at D-Day; Class IX demand vs. stock; historical readiness recovery rate |
| **3 — AVAILABLE DATA** | Map required information to MSS data; document gaps explicitly | Gaps do not stop analysis — they raise uncertainty and must be characterized |
| **4 — APPROPRIATE METHOD** | Select the method after steps 1–3; match to decision timeline | A method producing a precise answer in three weeks when the commander decides in three days is not appropriate |

### 2-2. Framework Applied to Common USAREUR-AF Taskers

| Commander Question | Decision | Required Information | Common Data Gap | Method Implication |
|---|---|---|---|---|
| "Are we ready for DEFENDER?" | Accept risk or request support by 15 April | Equipment readiness by type, parts on hand, PMCS completion | Consumption rates by exercise phase not in MSS | Descriptive + trend analysis; flag gap; present scenarios |
| "Where are the logistics bottlenecks?" | Allocate limited transport assets | Time-in-status by node, delay causes, network load | Cause-of-delay often missing or free-text | Descriptive + root cause; manual review of records for cause data |
| "What happens if we surge two brigades simultaneously?" | Approve or modify the surge plan | Projected supply consumption, maintenance surge, personnel tempo | No historical simultaneous surge data at this scale | Simulation; explicitly state model extrapolates beyond historical range |

### 2-3. When to Return for Clarification

Do not begin analysis on an ambiguous tasker. Return for clarification when:

- The decision-maker and decision point are not identified. "Leadership wants to understand readiness" is not an analytical tasker.
- The required output format is unclear. A Contour dashboard, a written decision brief, and a Python notebook are not interchangeable products.
- The timeline is incompatible with rigorous analysis and the commander has not been advised of the tradeoff. If the G3 needs an answer in two hours, they receive a well-characterized estimate based on available data — not a poorly validated model presented as fully developed.

> **VIGNETTE:** A 21st TSC ORSA received a tasker to "analyze Class IX readiness." After applying the decomposition framework, the ORSA identified five separate decisions with different timelines, decision-makers, and data requirements. A one-page decomposition memo — before touching MSS — reduced analytical scope by 40 percent and eliminated two weeks of work on a product no commander had actually requested.

---

## SECTION 3 — CHOOSING THE RIGHT METHOD

**BLUF:** Method selection follows from the question type. Use the simplest method that serves the commander's decision. Complexity that is not required is a liability.

### 3-1. The Four Question Types

| Question Type | Form | ORSA Answer | Example |
|---|---|---|---|
| **Descriptive** | What happened? | Summary statistics, aggregations, visualizations | Average C-rating for V Corps brigades over 90 days |
| **Diagnostic** | Why did it happen? | Root cause analysis, segmentation, correlation | Why did 173rd Airborne Brigade readiness decline in January? |
| **Predictive** | What will happen? | Regression, time series, simulation, ML forecasting | Class IX demand during DEFENDER surge period |
| **Prescriptive** | What should we do? | Optimization, decision analysis, COA comparison | How to allocate limited transport assets across four LOCs to maximize readiness |

### 3-2. Method Selection Heuristics

**Use the simplest method that serves the decision.** A count table showing five units below C-2 — three for more than 30 days — serves a readiness review better than a logistic regression producing the same actionable list. Regression is appropriate when the commander needs a probability estimate or forecast, not a current status.

**Match method sophistication to data quality.** Sophisticated methods extract signal. They also amplify noise and launder uncertainty into false precision. A Monte Carlo simulation built on three data points of historical consumption is not a simulation — it is a dressed-up assumption.

**Predictive questions require baseline descriptive analysis first.** Understand the current readiness distribution, historical trend, and seasonal patterns before building a forecast. A predictive model built without first understanding the descriptive picture produces results that are technically valid but operationally uninterpretable.

**Prescriptive analysis requires explicit COA definition.** Optimization models optimize against defined constraints and objectives. If the commander has not defined the constraints and objectives, optimization produces a mathematically correct answer to the wrong question.

> **NOTE — COA Evaluation and CARVER Scoring (TM-40G Sections 3-4 and 5-4):** TM-40G now provides a structured COA evaluation criteria schema (Section 3-4) and a CARVER target-value scoring methodology with Table 5-4 (Section 5-4). Use these frameworks when conducting prescriptive COA comparison analyses.

### 3-3. When Not to Model

Some operational questions are judgment calls that benefit from structured data but not from models. If a commander asks whether to accept a COA, the ORSA characterizes quantifiable risk and uncertainty components — not a model outputting "accept" or "reject." COA selection involves values, authorities, and political considerations no model captures.

> **VIGNETTE:** During a V Corps logistics planning conference, an ORSA built an optimization model recommending pre-positioning 60 percent of Class IX assets to Poland ahead of a DEFENDER exercise. The model was technically sound but omitted host-nation storage limitations and classified force protection requirements. The correct course of action: brief the model's output as a planning bound, document constraint assumptions explicitly, and coordinate with the G4 before presenting to the commander.

---

## SECTION 4 — STATISTICAL THINKING IN AN OPERATIONAL CONTEXT

**BLUF:** Statistical concepts apply differently in small-n, high-stakes operational settings. Translate statistical ideas into operationally meaningful language without losing precision or creating false confidence.

### 4-1. The Small-n Problem

Classical statistical inference assumes large samples. Many ORSA problems do not provide them — USAREUR-AF has a finite number of brigades, a given exercise happens once, and a specific vehicle failure class may have only three historical records. In these settings, p-values and confidence intervals derived from asymptotic theory are not reliable guides.

When n is small:
- Characterize what the data shows directly, without overfitting inference to a small sample
- Identify analogous historical cases from other theaters, exercises, or doctrinal planning factors
- Quantify uncertainty through ranges and scenarios rather than point estimates with unsupportable confidence intervals
- State directly in the product: "This estimate is based on [n] historical observations and should be treated as a planning assumption, not a statistical finding."

### 4-2. Uncertainty Quantification for Operational Audiences

Commanders are comfortable with ranges and risk. They are not comfortable with p-values, regression coefficients, or AUC curves — and they should not have to be.

| Statistical Concept | Commander Translation | Operational Example |
|---|---|---|
| 95% confidence interval | "We expect the actual value in this range in 19 out of 20 similar situations." | "Exercise Class IX demand: 4,200 to 5,800 short tons. Plan to the high end if pre-positioning is available." |
| p-value < 0.05 | Avoid presenting directly. Translate to effect size. | "Units below 80% PMCS completion are three times more likely to fall below C-2 during exercise surge." |
| Model prediction interval | "Range of outcomes the model considers plausible for an individual case." | "C-rating recovery for a unit at this readiness state: 14 to 28 days." |
| R-squared | Avoid. Describe explanatory power in plain language if relevant. | "Maintenance staffing explains about two-thirds of the variation in readiness recovery time." |
| Sensitivity analysis | "Here is how the answer changes if our key assumption is wrong." | "If consumption is 20% above historical average — consistent with DEFENDER 24 — demand increases to 6,400 short tons." |

### 4-3. Precision vs. Accuracy

Precision and accuracy are distinct. Operational data can be highly precise and completely inaccurate. Unit readiness reports may update on a precise daily schedule (high precision) but reflect commanders' inputs rather than objective sensor data (unknown accuracy).

An ORSA product must characterize both: "Our forecast is precise to within 5% based on the method, but accuracy is limited by the self-reported nature of the input data." Reporting precision alone is an incomplete characterization.

> **VIGNETTE:** A 21st TSC ORSA building a parts-demand forecast noticed that Class IX consumption records showed zero demand on weekends for three consecutive months — implausibly low given tempo. A legacy logistics system fed did not process weekend transactions until Monday morning, systematically understating weekend demand. The ORSA corrected the data, documented the anomaly, and included a data quality note in the product's assumptions section.

---

## SECTION 5 — WORKING WITH OPERATIONAL DATA QUALITY

**BLUF:** Operational data is collected for operational purposes, not analytical ones. Thorough data quality assessment is non-optional before drawing conclusions.

### 5-1. Why Operational Data Quality Differs

An ORSA working with MSS data is working with:
- Reports submitted by unit S4s under time pressure, with varying training on the reporting system
- System-to-system feeds applying different field definitions, time zones, or update frequencies
- Historical records spanning multiple system migrations, each potentially changing field meanings
- Data collected for a different purpose than the current analytical question

None of these conditions make operational data unusable. They make data quality assessment mandatory.

### 5-2. ORSA-Specific Data Quality Concerns

| Concern | Description | Analytical Treatment |
|---|---|---|
| **Missing records** | Absence of data ≠ absence of activity. No maintenance work orders may mean no maintenance occurred, maintenance not entered, or MSS feed interrupted. | Determine which explanation applies before treating as a zero |
| **Duplicates from source merges** | MSS aggregates multiple feeds; merges produce duplicate records — same event under different identifiers | Validate record counts against known ground truth; dedup before counting |
| **Time-zone mismatches** | Timestamps may be UTC, local, or Zulu depending on source system | Verify time zones before any time-series join across systems |
| **Classification-driven gaps** | Some data is in classified systems and not replicated to MSS | Characterize classification-driven gaps in the product's limitations section |
| **Free-text cause fields** | Cause-of-failure, delay reason fields are often free text requiring normalization | Do not build causal analysis on raw free-text without normalization; document normalization approach |

### 5-3. Documenting Data Quality in Every Product

Every product delivered to a commander or staff section must include a data quality characterization. It is not a disclaimer — it is the information the commander needs to apply appropriate confidence to the finding.

**Minimum data quality characterization:**
- Source systems and data pull date
- Known gaps, exclusions, or anomalies
- Steps taken to address quality issues (deduplication, normalization, interpolation)
- Impact of remaining quality issues on the analytical finding

"Readiness rates are trending down based on GCSS-Army records ingested into MSS through [date]; weekend reporting gaps corrected using weekday-carry-forward method; two units excluded due to system migration anomalies; these exclusions are expected to slightly overstate theater-level readiness trends" is an analytical product. "Readiness rates are trending down" is not.

---

## SECTION 6 — THE ANALYTICAL PRODUCT MENTAL MODEL

**BLUF:** Every analytical product has three audiences simultaneously. Design for all three from the start.

### 6-1. Three Audiences, One Product

| Audience | Need | Product Section | Read Time |
|---|---|---|---|
| **Commander (action)** | Clear finding, explicit uncertainty, named recommended action or decision point | Executive summary and BLUF | Under 2 minutes |
| **Staff (context)** | Methodology, data sources, assumptions, supporting analysis — complete enough to reproduce | Body — methods, data, results tables, charts | 10–20 minutes |
| **Record (accountability)** | Raw data references, model version, dataset pull date, document version | Annexes and version control metadata | Archival |

### 6-2. Product Architecture

| Section | Audience | Content |
|---|---|---|
| Cover / Header | All | Title, date, classification, distribution restriction, analyst |
| BLUF / Executive Summary | Commander | One-paragraph finding with uncertainty bounds and recommended action |
| Background and Tasker | Staff, Record | Decision supported, source of tasker, scope, constraints |
| Data and Methods | Staff, Record | Datasets, pull dates, quality assessment, methods, assumptions |
| Findings | Commander, Staff | Results tables, charts, visualizations with source notes |
| Sensitivity Analysis | Commander, Staff | How findings change if key assumptions are wrong |
| Limitations | All | Data gaps, scope exclusions, model constraints |
| Recommendations | Commander | Named action, decision point, risk characterization |
| Annexes | Record | Raw data summaries, detailed model output, supporting calculations |

### 6-3. Briefing Products vs. Decision Products

| Type | Purpose | Required Elements |
|---|---|---|
| **Briefing product** | Informs — presents current state and trend | Accuracy, currency, clarity |
| **Decision product** | Enables action — synthesizes data into a recommendation | Finding, uncertainty bounds, recommended action, stated decision point |

The V Corps G3's weekly readiness update is a briefing product. The G3's recommendation to the CG on whether to request supplemental Class IX pre-positioning is a decision product. Both may be built from the same MSS data. They are not the same product.

> **VIGNETTE:** An ORSA supporting a 21st TSC logistics review built a 35-slide briefing deck showing detailed trends, demand forecasts, and consumption analysis. When the CG asked "what do you recommend?" the ORSA had no answer — the product was designed to inform, not to decide. A one-page decision product BLUFing the same analysis would have taken 30 seconds to read and enabled the decision the CG needed to make.

---

## SECTION 7 — MSS/FOUNDRY-SPECIFIC ORSA MENTAL MODELS

**BLUF:** Foundry's architecture changes how ORSA work is structured. Understanding the Ontology model, the Contour/Workspace split, and reproducibility requirements prevents avoidable friction.

> **NOTE — Force Ratio and Combat Power Index (TM-40G Section 7-0a):** TM-40G Section 7-0a introduces a force ratio and combat power index methodology for quantitative force comparison. Reference this section when building comparative strength analyses or COA risk assessments.

### 7-1. The Ontology as an Analytical Frame

The Ontology represents operational data as Objects, Properties, and Links — not raw database tables. This is an analytical frame that affects how problems are structured.

An ORSA working directly with raw rows asks: "What is in this dataset, and what can I compute from it?" An ORSA working with the Ontology asks: "What Objects exist, what Properties describe them, and what Links connect them?" These lead to different analyses.

The Ontology is advantageous because it encodes domain knowledge. A Unit Object has Properties (UIC, echelon, equipment density, current C-rating) and Links (to superior headquarters, subordinates, logistics support elements) that an ORSA would otherwise reconstruct from raw joins. Building from the Ontology means inheriting the validated data model domain experts built.

Complex temporal joins, window functions across partitioned datasets, and multi-step data quality corrections are often easier in a Code Workspace against raw datasets than through Ontology queries. Knowing when to work through the Ontology (structured, standardized, reproducible) vs. raw datasets (flexible, complex, requires more documentation) is a judgment developed through practice.

### 7-2. Contour vs. Code Workspaces

| Dimension | Code Workspaces | Contour |
|---|---|---|
| Purpose | Develop and execute analysis | Deliver recurring products to command audiences |
| Appropriate for | Work-in-progress, iterative exploration, one-time products | Readiness monitors, exercise tracking, products consulted repeatedly against current data |
| Supports complex statistics | Yes | No — displays computed results |
| Live data refresh | No | Yes — sits on live Ontology |

**Use cases by tool:**

| Use Case | Contour | Code Workspace |
|---|---|---|
| Weekly readiness status brief | Yes | No |
| Exercise consumption forecast | No | Yes |
| Unit-level C-rating trend monitor | Yes | Development only |
| Monte Carlo risk simulation | No | Yes |
| Real-time logistics node status | Yes | No |
| COA comparison analysis | No | Yes |

**Error to avoid:** Building a complex analytical product in Contour because the commander wants "a dashboard." Contour is a delivery channel, not an analytical environment. Complex analysis belongs in a Code Workspace notebook or Transform. Contour displays the outputs of that analysis.

### 7-3. Reproducibility as an Operational Requirement

In research, reproducibility is a methodological virtue. In operational ORSA, it is an accountability requirement. If your analysis produced a different number today than yesterday, you must explain why — and "the model changed" is not an explanation.

**Reproducibility requirements on MSS/Foundry:**

- **Dataset versioning.** Record the dataset version or data pull timestamp in your product. When re-run against updated data, document what changed and why.
- **Notebook version control.** Do not overwrite a notebook that produced a delivered product without saving the prior version.
- **Assumption documentation.** Document every parameter, threshold, and assumption in the notebook — not just in the product narrative.
- **Differential explanation.** When a recurring product shows a significant change, explicitly address whether the change reflects operational reality or changes in data, methodology, or reporting. "Readiness declined 8 points; 5 points are attributable to inclusion of two newly-assigned units not in the prior report; 3 points reflect actual equipment status degradation" is a reproducibility-compliant explanation.

> **VIGNETTE:** A V Corps ORSA running a monthly sustainment demand forecast found the February forecast 12 percent higher than January with no significant change in operational tempo. A Foundry Transform had been updated by the data engineering team to correct historical undercounting of Class IX transactions — correct, but it changed the historical baseline the model trained on. The ORSA documented the change, rebaselined the model, and included a note in the February product. The G4 appreciated the transparency; presenting the unexplained jump as an operational trend would have driven unnecessary logistics decisions.

---

## SECTION 8 — COMMON ORSA FAILURE MODES ON MSS

**BLUF:** ORSA errors on MSS cluster into five failure modes. Recognize them before they occur.

### 8-1. Failure Mode Summary

| Failure Mode | Description | Manifestation | Correction |
|---|---|---|---|
| **Over-Engineering** | Applying complex method when simpler one serves the decision | Gradient boosted classifier to predict units below C-2 when a threshold rule produces the same actionable list | Write in one sentence what decision the output enables; build to the simplest standard that achieves it |
| **Underspecifying Uncertainty** | Delivering results without explicit uncertainty bounds | Contour dashboard showing "Projected Demand: 5,200 ST" with no range, no confidence, no sensitivity note | Never finalize a product without a range, a data quality note, and documented assumptions |
| **Correlation/Causation Confusion** | Presenting correlation as causal, or recommending action on a confounded correlation | Units with higher maintenance staffing have better readiness → recommend more staffing (both driven by echelon) | State correlation clearly; state causal question separately; list alternative explanations; recommend causal investigation before action |
| **Anchoring to Platform Tools** | Framing the analytical problem around what MSS can do rather than what the decision requires | Defaulting to time-series visualization because Contour makes it easy | Apply decomposition framework (Section 2) before opening any Foundry application |
| **Missing the "So What"** | Technically correct product that does not connect findings to a specific action or decision | Readiness trend showing declining C-ratings across three brigades with no recommendation for what the commander should do, by when, with what expected effect | Every product answers: What is the finding? How certain are we? What should the commander do? |

---

## SUMMARY — MENTAL MODEL CHECKLIST

Before delivering any analytical product, confirm each item.

| Item | Check |
|---|---|
| Commander's decision stated: decision-maker, choice space, deadline | |
| Decomposition framework (Decision → Information → Data → Method) applied before analysis began | |
| Method is the simplest one that serves the decision | |
| All findings include uncertainty characterization (range, confidence, sensitivity) | |
| Data quality assessed and documented in the product | |
| Product addresses all three audiences: commander, staff, record | |
| Correlation findings not presented as causal recommendations | |
| "So what" — a named action or decision point — is stated | |
| Dataset version and pull date documented | |
| Foundry notebook or workspace version saved and labeled | |

---

---

## CURRICULUM NOTES

**Prerequisite:** TM-30 (Advanced Builder) is REQUIRED before beginning TM-40G or this guide. Graduate-level quantitative background (statistics, R or Python) is separately required.

**Advanced track:** TM-40G graduates should pursue **TM-50G (Advanced ORSA)** as the next step in the specialist progression. TM-50G addresses Bayesian methods, complex simulation, multi-objective optimization, and campaign analysis support at theater level.

**Peer specialist cross-references:**
- **TM-40M (ML Engineer):** Coordinate when a recurring prediction requirement exceeds one-time ORSA analysis — the MLE operationalizes the analytical approach as a production pipeline.
- **TM-40H (AI Engineer):** Coordinate when ORSA decision products need to be wrapped in AI-assisted synthesis or automated SITREP generation workflows.
- **TM-40L (Software Engineer):** Coordinate when ORSA products require production-grade pipeline implementation, OSDK delivery surfaces, or custom visualization logic.

**WFF awareness:** ORSA products serve all six Warfighting Functions. TM-40A (Intelligence), TM-40B (Fires), TM-40C (Movement and Maneuver), TM-40D (Sustainment), TM-40E (Protection), and TM-40F (Mission Command) personnel are the primary consumers of ORSA decision products. Apply the decomposition framework in Section 2 to every WFF tasker — the WFF function determines the decision, the information requirement, and the appropriate method.

**ORSA-specific governing references:**

| Publication | Title | Relevance |
|---|---|---|
| DA PAM 600-3 | Officer Professional Development | Defines FA 49 (ORSA) career progression and qualifications |
| AR 5-11 | Management of Army M&S | M&S governance policy |
| DA PAM 5-11 | VV&A of Army Models and Simulations | Model credibility and accreditation standards |
| ATP 5-0.3 | Multi-Service TTP for Operation Assessment | Assessment methodology, MOE/MOP analytical frameworks |

> **NOTE — New Doctrine Content in TM-40G:** TM-40G now includes a formal assessment framework (MOE/MOP/indicators, Table 1-2) with the FM 5-0 COA evaluation criteria schema, a CARVER target value analysis scoring model (Table 5-4, FM 3-60 Appendix G), and force ratio/relative combat power calculations (section 7-0a, FM 5-0 Table 5-4). These sections provide the doctrinal grounding for the quantitative methods taught in this concepts guide.

*This guide is a prerequisite companion to TM-40G. Proceed to TM-40G for task-based instruction in statistical modeling, time series analysis, simulation, optimization, and decision product delivery on MSS/Foundry.*

---

**HEADQUARTERS, UNITED STATES ARMY EUROPE AND AFRICA**
Wiesbaden, Germany | 2026

DISTRIBUTION RESTRICTION: Distribution authorized to U.S. Government agencies and their contractors only. Other requests must be referred to Headquarters, C2DAO, Wiesbaden, Germany.
