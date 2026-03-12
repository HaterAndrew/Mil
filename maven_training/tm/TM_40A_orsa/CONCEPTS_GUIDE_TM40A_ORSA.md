# CONCEPTS GUIDE — TM-40A COMPANION
## OPERATIONS RESEARCH / SYSTEMS ANALYSIS (ORSA)
## MAVEN SMART SYSTEM (MSS)

**HEADQUARTERS, UNITED STATES ARMY EUROPE AND AFRICA**
Wiesbaden, Germany
2026

**PURPOSE:** This guide develops the analytical mental models required to operate effectively as an ORSA on MSS. It is a prerequisite companion to TM-40A and is intended to be read before beginning TM-40A task instruction.

**DISTRIBUTION RESTRICTION:** Approved for public release; distribution is unlimited.

---

## TABLE OF CONTENTS

1. The ORSA's Job on MSS
2. How to Decompose a Commander's Question
3. Choosing the Right Method
4. Statistical Thinking in an Operational Context
5. Working with Operational Data Quality
6. The Analytical Product Mental Model
7. MSS/Foundry-Specific ORSA Mental Models
8. Common ORSA Failure Modes on MSS

---

## SECTION 1 — THE ORSA'S JOB ON MSS

**BLUF:** The ORSA's primary output is a commander's decision product. Every other capability — modeling, visualization, data access — exists in service of that product.

### 1-1. What the ORSA Does That Others Don't

MSS/Foundry supports several distinct analyst roles. Understanding where ORSA work begins and ends is not an organizational formality — it shapes how you frame every problem, what tools you reach for, and how you present results.

The **data engineer** owns the pipeline. Their product is a reliable, validated dataset arriving at the right place at the right time. When 21st TSC logistics records are ingesting cleanly and the readiness roll-up is updating on schedule, the data engineer has succeeded. They are not responsible for what happens analytically after that point.

The **ML engineer** owns the model. Their product is a trained, validated, deployed algorithm that generalizes from historical data to new inputs. When a classification model correctly predicts whether a unit will pass a maintenance inspection, the ML engineer has succeeded. They are not primarily responsible for whether the commander acts on that prediction.

The **ORSA** owns the decision product. Your product is a recommendation or a structured quantitative analysis that enables a specific decision by a specific commander at a specific time. When the V Corps G3 can walk into a battle rhythm meeting and say "our analysis shows the 2nd Cavalry Regiment's M1A2 readiness will fall below C-2 within 19 days if current parts consumption rates continue, and here are the three courses of action with estimated timelines and resource costs" — that is an ORSA product. The model that produced the forecast may have been built by an ML engineer. The data pipeline may have been built by a data engineer. But the decision-ready product, contextualized for the commander's specific question and authority, is yours.

This distinction matters on MSS because the platform does not enforce it. Foundry gives an ORSA access to datasets, notebooks, transforms, ontology objects, and dashboards. You can do data engineering in a Code Workspace. You can build a model in one. The fact that you can do everything does not mean you should. ORSA time is most valuable closest to the commander. Guard it accordingly.

### 1-2. What "Decision Product" Means in Practice

A decision product answers a specific question, makes the uncertainty explicit, and names the action it enables. It is not a visualization. It is not a model output dump. It is not a dashboard with no narrative.

A decision product has:
- A BLUF that states the analytical finding in one sentence
- A quantified answer with explicit bounds or confidence characterization
- A "so what" that connects the finding to a specific command action or decision point
- A section documenting data sources, assumptions, and limitations

A V Corps logistics readiness brief that shows C-rating trends for the last 90 days is a visualization. The same brief that shows trends, attributes the trajectory to three specific failure modes, forecasts C-rating outcomes under two logistic support scenarios, and recommends a decision point by a named date — that is a decision product.

### 1-3. How MSS Fits the ORSA Workflow

MSS/Foundry is the ORSA's analytical environment, not merely a data repository. The platform connects three capabilities that ORSA work requires:

**Access to integrated operational data.** Unit readiness, logistics status, personnel accountability, exercise outcomes, and sustainment data that previously required separate data calls and manual aggregation are available through the Ontology layer. An ORSA analyzing DEFENDER exercise throughput at Grafenwoehr can join unit readiness records to equipment arrival timelines to maintenance work orders in a single Code Workspace — without submitting six separate RFIs to six different staff sections.

**A reproducible analytical environment.** Foundry Code Workspaces persist. Analysis you ran last week is still there. The datasets it used are versioned. If the G2 asks why your threat assessment changed between the February and March MDMP cycles, you can trace the answer to a specific dataset update, not "my spreadsheet changed." This reproducibility is not a technical nicety — it is an operational accountability requirement.

**A product delivery channel.** Contour dashboards and Quiver reports allow ORSA products to reach commanders through MSS rather than through email attachments. This means your analysis is live against current data when the commander reads it. A readiness forecast built Tuesday is outdated by Friday's maintenance cycle. A Contour dashboard built on the same underlying Ontology objects is current every time the commander opens it.

---

## SECTION 2 — HOW TO DECOMPOSE A COMMANDER'S QUESTION

**BLUF:** Most ORSA failures begin at problem framing, not at modeling. A rigorous decomposition framework applied before opening a Code Workspace prevents most of them.

### 2-1. The Decomposition Framework

Commanders ask operational questions. They do not ask statistical questions. "Are we ready for DEFENDER?" is not a statistical question. It is an operational judgment that, when properly decomposed, resolves into a set of analytical questions that can be answered with data.

The decomposition framework has four steps, in order:

```
DECISION → REQUIRED INFORMATION → AVAILABLE DATA → APPROPRIATE METHOD
```

This sequence is non-negotiable. Skipping from DECISION directly to METHOD — "the commander asked about readiness, so I'll build a regression model on C-ratings" — is the most common ORSA failure mode on MSS and in every other analytical environment. The framework forces you to check data availability before committing to a method, and to validate that the information you can produce actually supports the decision the commander faces.

**Step 1 — DECISION:** State the specific decision the commander must make and when. Not "assess readiness" — that is a task. The decision is: "V Corps commander must decide by 15 April whether to request additional Class IX pre-positioning support for DEFENDER or accept risk to readiness targets." A decision has a decision-maker, a choice space, and a deadline. If you cannot state the decision in these terms, return to the commander or staff for clarification before proceeding.

**Step 2 — REQUIRED INFORMATION:** List the specific information that would allow the commander to make that decision with acceptable confidence. For the example above: projected readiness rates for mission-essential equipment at D-Day, Class IX demand forecast vs. current pre-positioned stock levels, historical readiness recovery rate after high-tempo exercises. This step does not ask what data exists — it asks what information the decision requires. Generate this list independently of what you know is in MSS.

**Step 3 — AVAILABLE DATA:** Now check what data is actually available in MSS and whether it can support the required information. This step often reveals gaps: demand forecasts require historical consumption rates that may not exist, or readiness records exist but only at echelons that don't map cleanly to the mission-essential equipment list. Document gaps explicitly. Gaps do not mean the analysis cannot proceed — they mean the uncertainty is higher and must be characterized.

**Step 4 — APPROPRIATE METHOD:** Only after completing steps 1-3 do you select the analytical method. The method is dictated by the gap between required information and available data, and by the decision timeline. A method that produces a precise answer in three weeks when the commander decides in three days is not an appropriate method, regardless of its technical sophistication.

### 2-2. Applying the Framework to Common ORSA Taskers

The following table applies the decomposition framework to three representative USAREUR-AF taskers.

| Commander Question | Decision | Required Information | Common Data Gap | Method Implication |
|---|---|---|---|---|
| "Are we ready for DEFENDER?" | Accept risk or request support by 15 April | Equipment readiness by type, parts on hand, PMCS completion rates | Consumption rates by exercise phase not in MSS | Descriptive + trend analysis; flag gap; present scenarios |
| "Where are the logistics bottlenecks?" | Allocate limited transport assets to maximize throughput | Time-in-status by node, delay causes, network load | Cause-of-delay often missing or free-text | Descriptive + root cause; manual review of records for cause data |
| "What happens if we surge two brigades simultaneously?" | Approve or modify the surge plan | Projected supply consumption, maintenance surge, personnel tempo | No historical simultaneous surge data at this scale | Simulation; explicitly state model is extrapolation beyond historical range |

### 2-3. When Clarification Is Required Before Analysis Begins

Do not begin analysis on an ambiguous tasker. Return for clarification when:

- The decision-maker and decision point are not identified. "Leadership wants to understand readiness" is not an analytical tasker.
- The required output format is unclear. A Contour dashboard, a written decision brief, and a Python notebook produce different analytical products — they are not interchangeable.
- The timeline is incompatible with rigorous analysis and the commander has not been advised of the tradeoff. If the G3 needs an answer in two hours, they should receive a well-characterized estimate based on available data, not a poorly validated model presented as though it were a fully developed analysis.

> **VIGNETTE:** During a pre-DEFENDER planning cycle, a 21st TSC ORSA received a tasker to "analyze Class IX readiness." After applying the decomposition framework, the ORSA identified that the tasker implied five separate decisions with different timelines, different decision-makers, and different data requirements. Returning to the G4 with a one-page decomposition memo — before touching MSS — reduced the analytical scope by 40 percent and eliminated two weeks of work on a product no commander had actually requested.

---

## SECTION 3 — CHOOSING THE RIGHT METHOD

**BLUF:** Method selection follows from the question type. Use the simplest method that serves the commander's decision. Complexity that is not required is a liability.

### 3-1. The Four Question Types

Every analytical question falls into one of four categories. The category determines the appropriate method class. Most ORSA products address one primary category and may touch a second.

| Question Type | Form | ORSA Answer | Example |
|---|---|---|---|
| **Descriptive** | What happened? | Summary statistics, aggregations, visualizations | What was the average C-rating for V Corps brigades during the last 90 days? |
| **Diagnostic** | Why did it happen? | Root cause analysis, segmentation, correlation analysis | Why did the 173rd Airborne Brigade's readiness rate decline during January? |
| **Predictive** | What will happen? | Regression, time series, simulation, ML forecasting | What will Class IX demand be during the DEFENDER exercise surge period? |
| **Prescriptive** | What should we do? | Optimization, decision analysis, COA comparison | How should 21st TSC allocate limited transport assets across four LOCs to maximize readiness rates? |

### 3-2. Method Selection Heuristics

The following heuristics govern method selection in an operational ORSA context.

**Use the simplest method that serves the decision.** A count table that shows five units are below C-2 and three have been below C-2 for more than 30 days serves a readiness review meeting better than a logistic regression model that produces the same actionable list. The regression model is appropriate when the commander needs a probability estimate or a forecast, not when they need a current status.

**Match method sophistication to data quality.** Sophisticated methods extract signal from data. They also amplify noise and launder uncertainty into false precision. A Monte Carlo simulation built on three data points of historical exercise consumption is not a simulation — it is a dressed-up assumption. If data quality limits the method, say so and use a simpler method with explicit uncertainty characterization.

**Predictive questions require baseline descriptive analysis first.** Before building a readiness forecast, you must understand the current readiness distribution, the historical trend, and the seasonal or operational patterns. A predictive model built without first understanding the descriptive picture will produce results that are technically valid but operationally uninterpretable.

**Prescriptive analysis requires explicit COA definition.** Optimization models optimize against defined constraints and objectives. If the commander has not defined the constraints (available transport, acceptable risk to other missions) and the objective (maximize total readiness? minimize time below C-2 threshold?), optimization produces a mathematically correct answer to the wrong question.

### 3-3. When Not to Model

Some operational questions are not analytic problems — they are judgment calls that benefit from structured data but not from models. Recognizing this distinction is an advanced ORSA competency.

If a commander asks whether to accept a particular course of action, the ORSA role is to characterize the quantifiable risk and uncertainty components, not to produce a model that outputs "accept" or "reject." COA selection involves values, authorities, and political considerations that no model captures. Presenting a quantitative recommendation as though it subsumes those factors misrepresents the analytical product and can undermine commander trust in ORSA support.

> **VIGNETTE:** During a V Corps logistics planning conference, an ORSA built an optimization model that recommended pre-positioning 60 percent of Class IX assets to Poland ahead of a DEFENDER exercise. The model was technically sound. However, the G4 later identified that the model's constraint set omitted host-nation storage limitations and classified force protection requirements — factors the ORSA had not been briefed on. The recommendation required complete rework. The correct course of action was to brief the model's output as a planning bound, document its constraint assumptions explicitly, and coordinate with the G4 before presenting to the commander.

---

## SECTION 4 — STATISTICAL THINKING IN AN OPERATIONAL CONTEXT

**BLUF:** Statistical concepts apply differently in small-n, high-stakes operational settings. ORSA analysts must translate statistical ideas into operationally meaningful language without losing precision or creating false confidence.

### 4-1. The Small-n Problem

Classical statistical inference assumes large samples. Many ORSA problems do not provide them. USAREUR-AF has a finite number of brigades. A given exercise happens once. A specific class of vehicle failure may have occurred three times in the historical record. In these settings, p-values and confidence intervals derived from asymptotic theory are not reliable guides, and presenting them as though they were is a form of analytical dishonesty.

When n is small, the ORSA's job is to:
- Characterize what the data shows directly, without overfitting inference to a small sample
- Identify analogous historical cases (from other theaters, other exercises, doctrinal planning factors) that can inform planning assumptions
- Quantify uncertainty through ranges and scenarios rather than point estimates with confidence intervals that the sample cannot support
- State directly in the product: "This estimate is based on [n] historical observations and should be treated as a planning assumption, not a statistical finding."

### 4-2. Uncertainty Quantification for Operational Audiences

Commanders are comfortable with ranges and risk. They use them every day in planning. They are not comfortable with p-values, regression coefficients, or AUC curves — and they should not have to be. The ORSA's job is to translate statistical outputs into operationally meaningful uncertainty characterizations.

The following table maps statistical concepts to commander-appropriate language.

| Statistical Concept | Commander Translation | Operational Example |
|---|---|---|
| 95% confidence interval | "We expect the actual value to fall in this range in 19 out of 20 similar situations." | "We expect exercise Class IX demand to fall between 4,200 and 5,800 short tons. Plan to the high end if pre-positioning is available." |
| p-value < 0.05 | Avoid presenting p-values directly. Translate to effect size. | "Units with fewer than 80% PMCS completion are three times more likely to fall below C-2 during the exercise surge period." |
| Model prediction interval | "This is the range of outcomes our model considers plausible for an individual case." | "For a unit at this readiness state entering an exercise, our model projects C-rating recovery in 14 to 28 days." |
| R-squared | Avoid. Describe explanatory power in plain language if relevant. | "Maintenance staffing levels explain about two-thirds of the variation in readiness recovery time across units in our dataset." |
| Sensitivity analysis | "Here is how the answer changes if our key assumption is wrong." | "If Class IX consumption rates are 20% higher than historical average — consistent with the DEFENDER 24 exercise — the demand estimate increases to 6,400 short tons." |

### 4-3. Precision vs. Accuracy in Operational Data

Precision and accuracy are distinct. A precise measurement is tightly clustered. An accurate measurement is close to the true value. Operational data can be highly precise and completely inaccurate — and when it is, ORSA products built on it will be systematically wrong in ways that are difficult to detect until the numbers fail to match operational reality.

A common example in USAREUR-AF data: unit readiness reports may update on a precise daily schedule (high precision) but reflect commanders' inputs rather than objective sensor data (unknown accuracy). An ORSA building a readiness forecast from this data is building on a foundation that is precise but only as accurate as the reporting culture of the units in question.

The ORSA's product must characterize both. "Our forecast is precise to within 5% based on the analytical method, but accuracy is limited by the self-reported nature of the input data" is a complete characterization. "Our forecast is precise to within 5%" is not.

> **VIGNETTE:** A 21st TSC ORSA building a parts-demand forecast for a Corps exercise noticed that Class IX consumption records showed zero demand on weekends for three consecutive months — implausibly low given tempo. Investigation revealed that the MSS feed from a legacy logistics system did not process weekend transactions until Monday morning, systematically understating weekend demand in the historical record. The forecast built on that data would have underestimated peak demand. The ORSA corrected the data, documented the anomaly, and included a data quality note in the product's assumptions section.

---

## SECTION 5 — WORKING WITH OPERATIONAL DATA QUALITY

**BLUF:** Operational data is collected for operational purposes, not analytical ones. ORSA analysts inherit that data and must characterize its quality before drawing conclusions from it.

### 5-1. Why Operational Data Quality Differs from Research Data

Research datasets are collected to support analysis. Operational datasets are collected to support operations — specifically, the reporting requirements, system integrations, and command information needs of the moment. The incentives, timelines, and quality controls are different.

An ORSA working with MSS data is working with:
- Reports submitted by unit S4s under time pressure, with varying levels of training on the reporting system
- System-to-system feeds that may apply different field definitions, time zones, or update frequencies
- Historical records that span multiple system migrations, each of which may have changed field meanings
- Data collected for a different purpose than the current analytical question (e.g., personnel accountability records used to infer operational tempo)

None of these conditions make operational data unusable. They make thorough data quality assessment non-optional.

### 5-2. ORSA-Specific Data Quality Concerns

**Missing records.** Absence of data is not the same as absence of activity. If MSS shows no maintenance work orders for a unit during a two-week period, the ORSA must determine whether no maintenance occurred, whether maintenance occurred but was not entered, or whether the MSS data feed was interrupted. These three explanations produce different analytical treatments.

**Duplicates from source system merges.** MSS aggregates feeds from multiple authoritative data sources. When those sources are merged or migrated, duplicate records often appear — the same event represented twice under slightly different identifiers. Readiness counts built on undeduped records will overstate the population. The ORSA should validate record counts against known ground truth (brigade size, equipment density) before proceeding.

**Time-zone mismatches.** USAREUR-AF operates across multiple time zones with units, headquarters, and sustainment nodes distributed from Germany to the Black Sea. Timestamp fields in MSS may be in UTC, local time, or Zulu time depending on the source system. An ORSA building a time-series analysis that joins records from two systems with different timestamp conventions will create phantom time-of-day patterns that reflect data engineering artifacts, not operational reality.

**Classification-driven data gaps.** Some operational data is reported in classified systems and not replicated to MSS/Foundry. An ORSA working on a readiness analysis may have access to equipment status but not to the mission requirements that explain why a unit is intentionally holding equipment in maintenance rather than fielding it. Gaps driven by classification must be characterized in the product's limitations section, not papered over.

**Free-text fields.** Cause-of-failure, delay reason, and similar diagnostic fields are often free text in operational data systems. They require normalization before analysis. Common entries include: blank, "N/A", "see remarks", and non-standard abbreviations that change by unit. Do not build causal analysis on raw free-text fields without a normalization step, and document your normalization approach.

### 5-3. Documenting Data Quality in Every Product

Every analytical product delivered to a commander or staff section must include a data quality characterization. This is not a disclaimer to minimize ORSA accountability — it is the information the commander needs to apply appropriate confidence to the finding.

A minimum data quality characterization includes:
- Source systems and data pull date
- Known gaps, exclusions, or anomalies in the data
- Steps taken to address quality issues (deduplication, normalization, interpolation)
- Impact of remaining quality issues on the analytical finding

A finding that says "readiness rates are trending down" with no data quality characterization is an incomplete product. A finding that says "readiness rates are trending down based on GCSS-Army records ingested into MSS through [date]; weekend reporting gaps were corrected using a weekday-carry-forward method; two units were excluded due to system migration anomalies; these exclusions are expected to slightly overstate theater-level readiness trends" is an analytical product.

---

## SECTION 6 — THE ANALYTICAL PRODUCT MENTAL MODEL

**BLUF:** Every analytical product has three audiences simultaneously. Design for all three from the start, or you will redesign the product after it is finished.

### 6-1. Three Audiences, One Product

**The commander (action).** The commander reads your product to make a decision. They need a clear finding, explicit uncertainty, and a named recommended action or decision point. The commander's section of the product is the executive summary and the BLUF. It should be readable in under two minutes. If a commander must read 20 pages to determine whether the answer is "yes" or "no," the product has failed its primary audience.

**The staff (context).** Staff sections — G3, G4, G6, IG — use the analytical product to understand the reasoning behind a commander's decision, coordinate follow-on actions, and build context for the next analytical cycle. They need the methodology, the data sources, the assumptions, and the supporting analysis. The staff section of the product is the body — methods, data, results tables, charts with labeled axes and source notes. This section should be complete enough that a competent analyst could reproduce the analysis from the description.

**The record (accountability).** Analytical products become part of the command record. A decision made in 2026 based on a readiness forecast may be revisited in 2028. The record audience needs the raw data references, the version of the model, the specific dataset pull date, and the document version. An analytical product without version control and a clear data lineage cannot serve the accountability function.

### 6-2. Product Architecture

The following architecture satisfies all three audiences in a standard ORSA product.

| Section | Audience | Content |
|---|---|---|
| **Cover / Header** | All | Title, date, classification, distribution restriction, analyst |
| **BLUF / Executive Summary** | Commander | One-paragraph finding with uncertainty bounds and recommended action |
| **Background and Tasker** | Staff, Record | Decision supported, source of tasker, scope, and constraints |
| **Data and Methods** | Staff, Record | Datasets used, pull dates, quality assessment, analytical methods, assumptions |
| **Findings** | Commander, Staff | Results tables, charts, visualizations with source notes |
| **Sensitivity Analysis** | Commander, Staff | How findings change if key assumptions are wrong |
| **Limitations** | All | Data gaps, scope exclusions, model constraints |
| **Recommendations** | Commander | Named action, decision point, risk characterization |
| **Annexes** | Record | Raw data summaries, detailed model output, supporting calculations |

### 6-3. Briefing Products vs. Decision Products

A briefing product informs. A decision product enables action. Both are legitimate, and both are necessary in different command environments. Confusing them produces products that partially serve both purposes and fully serve neither.

A briefing product (situation update, readiness dashboard, exercise after-action summary) presents current state and trend. It does not require a finding or a recommendation. It requires accuracy, currency, and clarity.

A decision product (COA analysis, resource allocation recommendation, risk assessment) requires a finding, uncertainty bounds, a recommended action, and a stated decision point. It does not simply present data — it synthesizes data into a recommendation.

The V Corps G3's weekly readiness update is a briefing product. The G3's recommendation to the CG on whether to request supplemental Class IX pre-positioning is a decision product. Both may be built from the same MSS data. They are not the same product, and they should not be built the same way.

> **VIGNETTE:** An ORSA supporting a 21st TSC logistics review built a 35-slide briefing deck showing detailed readiness trends, demand forecasts, and consumption analysis. When the CG asked "what do you recommend?" the ORSA had no answer — the product had been designed to inform, not to decide. The CG left the brief without a decision. A one-page decision product BLUF-ing the same analysis would have taken 30 seconds to read and enabled the decision the CG needed to make.

---

## SECTION 7 — MSS/FOUNDRY-SPECIFIC ORSA MENTAL MODELS

**BLUF:** Foundry's architecture changes how ORSA work is structured. Understanding the Ontology model, the Contour/Workspace split, and reproducibility requirements prevents avoidable friction.

### 7-1. The Ontology as an Analytical Frame

Foundry's Ontology layer represents operational data as Objects, Properties, and Links — not as raw database tables. This is not merely a presentation layer. It is an analytical frame that affects how ORSA problems are structured.

An ORSA working directly with raw rows asks: "What is in this dataset, and what can I compute from it?" An ORSA working with the Ontology asks: "What Objects exist, what Properties describe them, and what Links connect them?" These are different starting questions and they lead to different analyses.

The Ontology frame is advantageous for ORSA work because it encodes domain knowledge. A Unit Object in the USAREUR-AF Ontology has Properties (UIC, echelon, assigned equipment density, current C-rating) and Links (to superior headquarters, to subordinate units, to associated logistics support elements) that an ORSA would otherwise have to reconstruct from joins across multiple raw datasets. Building from the Ontology means you inherit the data model that domain experts built and validated — you are not rebuilding it in every Code Workspace.

The Ontology frame also constrains what you can do directly without going back to raw data. Complex temporal joins, window functions across partitioned datasets, and multi-step data quality corrections are often easier in a Code Workspace against raw datasets than through Ontology queries. Knowing when to work through the Ontology (structured, standardized, reproducible) and when to go to raw datasets (flexible, complex, requires more documentation) is a judgment ORSA analysts develop through practice.

### 7-2. Contour vs. Code Workspaces — When to Use Each

Contour and Code Workspaces are not alternatives to each other. They serve different stages of the analytical product lifecycle.

**Code Workspaces** are for developing and executing analysis. Python or R notebooks in a Code Workspace are where the ORSA writes the statistical model, validates data quality, runs sensitivity analysis, and generates the numbers that support the product. Code Workspaces are the analytical engine. They are appropriate for work-in-progress, iterative exploration, and one-time analytical products that will not require live refresh.

**Contour** is for delivering recurring products to command audiences. Contour dashboards sit on top of live Ontology data and update without analyst intervention. They are appropriate for readiness monitors, exercise tracking dashboards, and any product that a commander or staff section will consult repeatedly against current data. Contour does not support complex statistical analysis — it supports structured display of computed results.

The error to avoid: building a complex analytical product in Contour because the commander wants "a dashboard." Contour is a delivery channel, not an analytical environment. Complex analysis belongs in a Code Workspace notebook or a Foundry Transform. Contour displays the outputs of that analysis, not the analysis itself.

| Use Case | Contour | Code Workspace |
|---|---|---|
| Weekly readiness status brief | Yes | No |
| Exercise consumption forecast | No | Yes |
| Unit-level C-rating trend monitor | Yes | Development phase only |
| Monte Carlo risk simulation | No | Yes |
| Real-time logistics node status | Yes | No |
| COA comparison analysis | No | Yes |

### 7-3. Reproducibility as an Operational Requirement

In a research context, reproducibility is a methodological virtue. In an operational ORSA context, reproducibility is an accountability requirement. If your analysis produced a different number yesterday than today, you must be able to explain why — and "the model changed" is not an explanation.

Reproducibility in MSS/Foundry requires:

**Dataset versioning.** Foundry tracks dataset versions. When you run an analysis, record the dataset version or the data pull timestamp in your product. If the analysis is run again against updated data, document what changed and why the numbers changed.

**Notebook version control.** Code Workspaces in Foundry support save states. Maintain version discipline: do not overwrite a notebook that produced an already-delivered product without saving the prior version. The CG may return to a three-month-old readiness forecast and ask why the methodology changed.

**Assumption documentation.** Every parameter, threshold, and assumption in your model is a potential source of variation across runs. Document all of them in the notebook, not just in the product narrative. The documentation in the product may be summarized; the documentation in the notebook should be complete.

**Differential explanation.** When a recurring product (monthly readiness brief, quarterly demand forecast) shows a significant change from the prior period, the product should explicitly address whether the change reflects operational reality or changes in data, methodology, or reporting. "Readiness declined 8 points" is incomplete. "Readiness declined 8 points; 5 points are attributable to the inclusion of two newly-assigned units not in the prior report; 3 points reflect actual equipment status degradation" is a reproducibility-compliant explanation.

> **VIGNETTE:** A V Corps ORSA running a monthly sustainment demand forecast noticed that the February forecast was 12 percent higher than the January forecast with no significant change in operational tempo. Investigation revealed that a Foundry Transform had been updated by the data engineering team to correct a historical undercounting of Class IX transactions — the correct decision, but one that changed the historical baseline the model trained on. The ORSA documented the change, rebaselined the model, and included a note in the February product explaining the revision. The G4 appreciated the transparency; the alternative — presenting the unexplained jump as an operational trend — would have driven unnecessary logistics decisions.

---

## SECTION 8 — COMMON ORSA FAILURE MODES ON MSS

**BLUF:** ORSA errors on MSS cluster into five failure modes. Recognizing them before they occur is more efficient than correcting them after a product is delivered.

### 8-1. Over-Engineering

**Description:** Applying a complex method when a simpler one would serve the commander's decision.

**How it manifests on MSS:** Building a gradient boosted classifier to predict which units will fall below C-2 when a threshold rule based on current C-rating and PMCS completion rate produces the same actionable list. Spending two weeks developing a stochastic simulation when the commander needs a planning estimate in two days.

**Why it happens:** Analytical training incentivizes sophistication. Platform capability enables it. The sunk-cost of time already spent on a complex model creates reluctance to simplify. ORSA analysts with strong technical backgrounds may default to complex methods as a demonstration of competence.

**The correction:** Before building any model, write down in one sentence what decision the output will enable. Then ask: "What is the simplest output that would enable that decision?" Build to that standard first. Add complexity only if the simple version cannot adequately characterize the decision space.

### 8-2. Underspecifying Uncertainty

**Description:** Delivering a result — a number, a trend, a forecast — without explicit uncertainty bounds or characterization.

**How it manifests on MSS:** A Contour dashboard that shows "Projected Exercise Demand: 5,200 ST" with no range, no confidence characterization, and no sensitivity note. A regression output copied from a Python notebook into a briefing slide with no explanation of prediction intervals or model limitations.

**Why it happens:** Uncertainty characterization requires additional work. Commanders sometimes respond impatiently to ranges ("just give me the number"). Analysts may fear that presenting uncertainty will undermine confidence in their work.

**The correction:** Refer to the TM-40A Safety Summary: a number without uncertainty is not an analytical product, it is a guess with formatting. A range is more useful to a commander than false precision. Train yourself to never finalize a product without asking: "Does this have a range? Does it have a data quality note? Does it document assumptions?"

### 8-3. Correlation and Causation Confusion

**Description:** Presenting a correlation finding as though it implies causation, or recommending action based on a correlation that reflects a confounding factor.

**How it manifests on MSS:** Finding that units with higher maintenance staffing have better readiness rates and recommending increased maintenance staffing, when both are actually driven by echelon — senior headquarters units have more staff and better support infrastructure at every level. Finding that exercise participation correlates with readiness decline and recommending reduced exercise frequency, when exercises are scheduled precisely because readiness is already declining.

**Why it happens:** Observational data is all an ORSA typically has. Controlled experiments are rarely available. Correlation analysis is fast; causal analysis is slow and requires domain expertise.

**The correction:** State the correlation clearly. State the causal question explicitly and separately. List alternative explanations. Recommend causal investigation (mechanism analysis, comparison of similar units with different interventions) before action. Do not make resource allocation recommendations based on unadjusted correlation findings in operational data.

### 8-4. Anchoring to Platform Tools

**Description:** Framing the analytical problem around what MSS/Foundry can do rather than what the commander's decision requires.

**How it manifests on MSS:** Building a readiness analysis using only the Ontology Objects that are easy to query, ignoring relevant data in harder-to-access datasets. Recommending a Contour dashboard when the commander's question requires a one-time decision analysis. Defaulting to time-series visualization because Contour makes it easy, rather than because the analytical question calls for it.

**Why it happens:** Familiarity and convenience shape analytical choices on every platform. Analysts learn what the tools do and reach for familiar tools before verifying they are appropriate.

**The correction:** Apply the decomposition framework (Section 2) before opening any Foundry application. The analytical requirement drives tool selection. Tool availability does not constrain the analytical requirement — it may constrain the execution, which must be documented.

### 8-5. Missing the "So What"

**Description:** Delivering a technically correct analytical product that does not connect findings to a specific action or decision.

**How it manifests on MSS:** A readiness trend analysis showing declining C-ratings across three brigades with no explanation of what the commander should do about it, by when, and with what expected effect. A demand forecast that shows the projected Class IX shortfall without naming the logistics action that would address it.

**Why it happens:** ORSA training emphasizes analytical rigor. Product communication is a separate skill that receives less emphasis. Analysts who are confident in their methods may be uncertain about making recommendations that involve judgment beyond their technical domain.

**The correction:** Every analytical product must answer three questions: What is the finding? How certain are we? What should the commander do? If the third question is genuinely outside ORSA authority (e.g., a political decision), the product should name the decision-maker who must answer it and provide the analytical inputs they need. "The data supports the following action" or "the following decision point is triggered by these conditions" — these are the sentences a product needs before it leaves the ORSA.

---

## SUMMARY — MENTAL MODEL CHECKLIST

Before delivering any analytical product, the ORSA should confirm each item.

| Item | Check |
|---|---|
| The commander's decision is stated: decision-maker, choice space, deadline | |
| The decomposition framework (Decision → Information → Data → Method) was applied before analysis began | |
| The method is the simplest one that serves the decision | |
| All findings include uncertainty characterization (range, confidence, sensitivity) | |
| Data quality was assessed and documented in the product | |
| The product addresses all three audiences: commander, staff, record | |
| Correlation findings are not presented as causal recommendations | |
| The "so what" — a named action or decision point — is stated | |
| Dataset version and pull date are documented | |
| Foundry notebook or workspace version is saved and labeled | |

---

*This guide is a prerequisite companion to TM-40A. Proceed to TM-40A for task-based instruction in statistical modeling, time series analysis, simulation, optimization, and decision product delivery on MSS/Foundry.*

---

**HEADQUARTERS, UNITED STATES ARMY EUROPE AND AFRICA**
Wiesbaden, Germany
2026

DISTRIBUTION RESTRICTION: Approved for public release; distribution is unlimited.
