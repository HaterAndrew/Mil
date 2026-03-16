# LESSON PLAN OUTLINES — TM-40 WFF TRACKS
## USAREUR-AF Operational Data Team — C2DAO
**Covers:** TM-40A (Intelligence) | TM-40B (Fires) | TM-40C (Movement & Maneuver) | TM-40D (Sustainment) | TM-40E (Protection) | TM-40F (Mission Command)
**Version:** 1.0 — March 2026

> Abbreviated LP outlines for TM-40 WFF functional courses. All six tracks follow the same 3-day structure with WFF-specific content.
> Instructors must have functional staff background in the WFF they are teaching. These outlines supplement that expertise — they do not replace it.
> Expand using `LP_TEMPLATE.md`. For complete LP examples see `TM10/TM10_LESSON_PLANS.md`.
> **Prerequisite for all WFF tracks:** TM-10, TM-20, TM-30 (Go evaluations on file). No coding or pipeline experience required of trainees.

---

# PART A — TM-40A: INTELLIGENCE WFF

**Duration:** 3 days (24 hours) | **T:I ratio:** 6:1 | **Instructor req:** G2/S2 background with MSS COP and AIP Logic experience; TM-40-level certification or C2DAO INT SME
**Doctrinal references:** FM 2-0, ATP 2-01, FM 3-60

---

### Block 1 — Doctrinal Context: MSS in Intelligence Operations
**Hours:** 1.0 | **Method:** Brief | **Day:** 1 | **Time:** 0800–0900

**Purpose:** Before trainees touch the COP, they need the doctrinal framing: MSS is not DCGS — it is a data integration and visualization layer. This block prevents the first-day confusion between what MSS shows and what the intelligence process produces.

**TLO:** The trainee will describe how MSS supports FM 2-0 intelligence operations and state the critical distinction between reported intelligence (MSS displays) and assessed intelligence (analyst judgment).

**Key Delivery Notes:**
- MSS role: integrates reporting feeds, displays COP overlays, enables PIR alert configuration. It does not produce assessed intelligence.
- Doctrinal links: MSS COP supports IPB products (FM 2-0 Ch 2), collection management (ATP 2-01), and targeting (FM 3-60).
- Open with a question: "Who has seen a threat overlay on MSS that turned out to be stale?" This surfaces the data currency problem early.
- Hard rule for the course: every intelligence product built this week must have a data-as-of timestamp and a source attribution label.

**Assessment:** Verbal check-on-learning. Evaluator will revisit reported vs. assessed distinction during Practical Exercise brief on Day 3.

---

### Block 2 — Intelligence COP Configuration
**Hours:** 2.0 | **Method:** Demo/Lab | **Day:** 1 | **Time:** 0900–1100

**Purpose:** The intelligence COP is the primary product G2/S2 staff deliver via MSS. Trainees must be able to configure all required layers from scratch before building anything on top of them.

**TLO:** The trainee will configure an intelligence COP with threat activity layers, NAI/TAI overlays, FSCM overlays with intelligence annotations, and IPB products — with correct display standards and data source linkages.

**Key Delivery Notes:**
- Start with layer architecture. Layer order matters: FSCM sits above terrain, threat sits above FSCM. Wrong layer order obscures data.
- Data source linkages: each layer should be tied to a named source pipeline, not manually drawn. Manual overlays have no currency indicator.
- NAI/TAI overlays: shape, label, and activation status must be present. An unlabeled NAI polygon is operationally useless.
- Display standards: echelon-appropriate symbology per FM 1-02.1. Review the standard before live demo.
- Instructor demos the full build, then trainees replicate independently on their training accounts.

**Student Activity:** Replicate the full intelligence COP configuration. Instructor spot-checks: (1) correct data source linkage on the threat layer, (2) NAI labels present, (3) data-as-of timestamp visible.

**Common Errors:**

| Error | Action |
|-------|--------|
| Manually drawing overlays instead of linking to data source | Flag immediately — this overlay will not auto-update |
| NAI/TAI unlabeled | Correct before moving to Block 3 |
| Threat layer below FSCM overlay | Adjust layer order now — visual error will compound |

**Assessment:** Foundation for Practical Exercise Task 1.

---

### Block 3 — Data Currency Verification
**Hours:** 0.75 | **Method:** Lab | **Day:** 1 | **Time:** 1115–1200

**Purpose:** A stale intelligence COP briefed as current is a command failure. This block builds the habit of reading and communicating timestamps before every product presentation.

**TLO:** The trainee will locate and interpret data-as-of timestamps for each COP layer, trace a threat feed to its source pipeline, and describe the correct escalation path when a feed goes dark.

**Key Delivery Notes:**
- Timestamp location varies by layer type — show where to find it for each layer configured in Block 2.
- Feed verification: open the source dataset and check the most recent transaction timestamp. If it is older than the update cadence (usually 1–4 hours), the feed may be stale.
- Escalation path: data steward → pipeline owner → C2DAO. Trainees should know all three contacts before going live.
- Practice: provide a training COP with one intentionally stale layer. Trainees must identify it.

**Assessment:** Evaluated indirectly in Practical Exercise Task 1 — evaluator will ask trainees to state the data-as-of time for each briefed layer.

---

### Block 4 — PIR Alert Configuration
**Hours:** 2.0 | **Method:** Lab | **Day:** 1 | **Time:** 1300–1500

**Purpose:** PIR alerts are the mechanism that drives timely intelligence reporting. A PIR not translated into an MSS alert is a PIR that will be missed during execution.

**TLO:** Given a commander's PIR card, the trainee will configure 3 PIR alerts with correct trigger conditions (geographic, threshold, or data-source), route notifications to the correct staff element, and verify each alert triggers on test data.

**Key Delivery Notes:**
- A complete PIR alert has three required elements: (1) trigger condition (geographic boundary OR data threshold), (2) data source (which dataset drives the trigger), (3) notification routing (who gets the alert). Missing any element = incomplete alert.
- Common trigger types: geographic (entity appears in polygon), threshold (count of entities exceeds value), data-change (field value changes from X to Y).
- Have trainees write out the trigger logic on paper before configuring in the tool. "Report enemy activity in the AOR" is not a trigger — it is a PIR. The trigger is specific.
- Test each alert against a provided test dataset before moving to Block 5.

**Student Activity:** Translate 3 PIRs from the provided commander PIR card into MSS alerts. Configure all three elements for each. Test-fire against the training dataset.

**Common Errors:**

| Error | Action |
|-------|--------|
| Alert configured with correct geography but wrong data source | Alert will not fire — confirm source pipeline before testing |
| Notification routed to "All Users" | Not operationally correct; route to specific staff element |
| PIR not tested against test data | Cannot confirm it works; test is mandatory before Day 3 PE |

**Assessment:** Evaluated in Practical Exercise Task 2.

---

### Block 5 — PIR Scenario Exercise
**Hours:** 1.75 | **Method:** Exercise | **Day:** 1 | **Time:** 1515–1700

**Purpose:** Extends Blocks 3 and 4 into a scenario drill. Trainees apply COP configuration and PIR alerts under simulated time pressure.

**TLO:** Given a scenario, the trainee will configure 3 PIR alerts and verify correct trigger behavior — without instructor assistance.

**Key Delivery Notes:**
- New scenario, different PIR card than Block 4. Trainees should not need instructor assistance; this is a practice run for the Day 3 evaluation.
- Instructor circulates and observes without intervening on technique (intervene only for system errors).
- Note which trainees struggle with trigger condition translation — follow up before Day 3.

**Assessment:** Formative. Evaluator notes readiness for Day 3 PE.

---

### Block 6 — Collection Management Visualization
**Hours:** 2.0 | **Method:** Demo/Lab | **Day:** 2 | **Time:** 0830–1030

**Purpose:** Collection management is the G2's primary contribution to the targeting cycle. An MSS collection status display must show gap status, not just task status.

**TLO:** The trainee will build a collection status dashboard showing NAI/TAI coverage status, collection asset task status, and identified collection gaps against published PIRs.

**Key Delivery Notes:**
- NAI status: active collection, reporting gap, or no task assigned. These are three different conditions — distinguish them explicitly in the display.
- Collection gaps: identify NAIs where no asset is tasked or where the tasked asset has not reported within cadence. Display these as GAP, not as unknown.
- Asset task status: link the dashboard to the collection management dataset — show asset ID, tasked NAI, last report timestamp.
- The briefing product must not imply collection where there is none. A blank NAI polygon implies unknown status, not absence of enemy.

**Student Activity:** Build the collection status dashboard from the provided training dataset. Instructor evaluates: gap NAIs identified, correctly labeled as GAP (not blank), asset task status visible.

**Assessment:** Evaluated in Practical Exercise Task 3.

---

### Block 7 — All-Source Fusion Product
**Hours:** 1.25 | **Method:** Lab | **Day:** 2 | **Time:** 1045–1200

**Purpose:** An all-source product that doesn't show its seams is dangerous. Trainees must display corroboration and contradiction across intelligence layers explicitly.

**TLO:** The trainee will build an intelligence summary product integrating at least two intelligence data layers, with explicit source attribution and a data currency caveat on each element.

**Key Delivery Notes:**
- Show two overlapping data layers simultaneously and compare: where do they corroborate? Where do they contradict? Display the contradiction — don't hide it.
- Attribution label format: "Source: [FEED NAME], as of [DTG]." This is not optional.
- INTSUM format: assessment (analyst judgment) separated from reporting (what MSS shows). Never combine them in the same text block without clear labeling.

**Assessment:** Evaluated in Practical Exercise Task 4.

---

### Block 8 — Targeting Data Product
**Hours:** 2.0 | **Method:** Demo/Lab | **Day:** 2 | **Time:** 1300–1500

**Purpose:** The targeting data product is the G2's direct contribution to targeting board preparation. Errors in confirmed/unconfirmed target distinction or BDA accuracy directly affect fires employment.

**TLO:** The trainee will build a targeting product distinguishing confirmed from unconfirmed targets — with attribution to reporting source, data-as-of timestamps, and current BDA status on each target element.

**Key Delivery Notes:**
- Confirmed vs. unconfirmed: confirmed requires two independent sources OR a voice confirmation. One reporting source = unconfirmed. Configure this as a display flag on the targeting layer.
- BDA status must be current: show the BDA data-as-of timestamp. If BDA is >6 hours old, label it as STALE on the product.
- "Confirmed" targets with no attribution source will fail the practical exercise. Every confirmed target must have a source reference.
- Instructor builds a target product with a deliberate error (confirmed target with single source). Have trainees identify it.

**Student Activity:** Build a targeting product from the provided dataset. Display confirmed/unconfirmed flag, source attribution, data-as-of timestamp, and BDA status for each target.

**Assessment:** Evaluated in Practical Exercise Task 4. Hard No-Go: target marked confirmed with single source attribution.

---

### Block 9 — Targeting Product Drill
**Hours:** 1.75 | **Method:** Exercise | **Day:** 2 | **Time:** 1515–1700

**Purpose:** Practice run for the Day 3 targeting product evaluation. New dataset, no instructor assistance.

**TLO:** The trainee will build a complete targeting product from a new dataset — confirmed/unconfirmed distinction, source attribution, BDA status, OPSEC marking — without instructor assistance.

**Key Delivery Notes:**
- Evaluator reviews for: timestamp on every target, confirmed/unconfirmed flag, attribution source, BDA data-as-of.
- Trainees who finish early: have them review a partner's product using the Practical Exercise checklist.

**Assessment:** Formative. Instructor notes targeting product quality for Day 3 awareness.

---

### Block 10 — OPSEC for Intelligence Products
**Hours:** 1.0 | **Method:** Brief | **Day:** 3 | **Time:** 0800–0900

**Purpose:** Intelligence products have the highest sensitivity of any MSS output. Export controls and need-to-know verification are non-optional at this level.

**TLO:** The trainee will describe the OPSEC procedures for intelligence products: classification marking requirements, distribution controls, export handling, and need-to-know verification before sharing.

**Key Delivery Notes:**
- Classification label placement: every exported product (PDF, PNG, CSV) must have a classification header and footer. MSS does not automatically add these to exports — the S2 is responsible.
- Export handling: intelligence COP exports containing threat activity should be treated as the classification level of the most sensitive layer displayed.
- Need-to-know: before sharing any MSS product, confirm the recipient is in the distribution. "I sent it to the battalion group chat" is not authorized distribution.
- OPSEC violation scenario: walk through what happens if a targeting product with unconfirmed enemy positions is shared outside the targeting working group. Make the consequence concrete.

**Assessment:** OPSEC compliance is evaluated in all Practical Exercise tasks. Any product without correct marking is an automatic No-Go.

---

### Block 11 — Collection Gap Response
**Hours:** 1.25 | **Method:** Demo/Lab | **Day:** 3 | **Time:** 0900–1015

**Purpose:** The most dangerous moment in intelligence operations is when a collection feed goes dark. Trainees must know how to characterize the gap correctly and what they will/will not brief to the targeting board.

**TLO:** The trainee will identify a collection gap on the COP, update the collection status dashboard to reflect the gap, and brief the evaluator on what can and cannot be stated about the NAI affected by the gap.

**Key Delivery Notes:**
- The fatal error: briefing a NAI as "clear" when the collection feed is down. Correct characterization: "NAI [NAME] status unknown — collection gap, feed [SOURCE] last reported [DTG]."
- Update the collection status dashboard: change the affected NAI status from "Active Collection" to "GAP" and timestamp the update.
- Products dependent on the gapped NAI must be caveated: "Assessment valid as of [DTG] — collection gap on NAI TIGER as of [DTG]. Assess with caution."
- Role-play: instructor plays commander who wants a definitive answer. Trainee must give an honest characterization without overstating or understating risk.

**Assessment:** Evaluated in Practical Exercise Task 5. Briefing a gapped NAI as "clear" is an automatic No-Go.

---

### Block 12 — Practical Exercise Scenario Brief and Prep
**Hours:** 1.5 | **Method:** Brief/Prep | **Day:** 3 | **Time:** 1030–1200 (includes lunch prep)

**Key Delivery Notes:**
- Issue scenario brief at 1030. Trainees have the block and lunch period to review the Practical Exercise checklist and confirm their training environment is ready.
- Review the Go/No-Go criteria explicitly: Pass 5 of 6 tasks. Auto No-Go conditions: PIR alert with wrong data source; briefing a gapped NAI as "clear"; any product missing classification marking.
- Evaluator does not answer technique questions after the scenario brief is issued.

---

### Block 13 — Practical Exercise (Evaluated)
**Hours:** 4.0 | **Method:** Evaluation | **Day:** 3 | **Time:** 1300–1700

**Scenario:** S2 section at a BCT headquarters during force projection. Commander requires a fully configured intelligence COP, PIR alerts active, collection status dashboard, and targeting product before a targeting working group in four hours. At T+90 min, evaluator injects: primary collection feed for NAI TIGER stops reporting.

**Tasks:**

| Task | Standard |
|------|----------|
| 1 | Configure intelligence COP: threat layers, NAI/TAI, IPB products; verify data currency on all feeds |
| 2 | Build 3 PIR alerts from the provided commander PIR card; verify each triggers on test data |
| 3 | Construct collection status dashboard: NAI coverage, asset task status, identified gaps |
| 4 | Build targeting product: confirmed/unconfirmed distinction, source attribution, data-as-of timestamps, BDA status |
| 5 | Respond to collection gap inject: update dashboard, caveat affected products, brief evaluator correctly |
| 6 | Apply OPSEC procedures to all products before simulated distribution |

**Go standard:** Pass 5 of 6. Auto No-Go: PIR alert with wrong data source (Task 2); briefing NAI TIGER as "clear" when feed is down (Task 5); any product missing classification marking.

---

## TM-40A COURSE COMPLETION — NEXT STEPS

TM-40A graduates are eligible to re-enroll in any other WFF track independently (no additional prerequisites beyond TM-30). Personnel with analytical roles may also consider specialist tracks TM-40G (ORSA) or TM-40H (AI Engineer) if they meet the domain prerequisites.

---

---

# PART B — TM-40B: FIRES WFF

**Duration:** 3 days (24 hours) | **T:I ratio:** 6:1 | **Instructor req:** Fires/targeting background (FSO, FA officer, or targeting cell experience); TM-40-level certification or C2DAO Fires SME
**Doctrinal references:** FM 3-09, ATP 3-09.42, FM 3-60

---

### Block 1 — Doctrinal Context: MSS in Fires and Targeting
**Hours:** 1.0 | **Method:** Brief | **Day:** 1 | **Time:** 0800–0900

**Purpose:** Establishes MSS's role in the D3A cycle before any tool work. A fires officer who treats MSS as a mapping tool will not configure it correctly. MSS is a targeting data integration and effects assessment platform.

**TLO:** The trainee will describe how MSS supports FM 3-09 fires operations and FM 3-60 targeting, and state the critical distinction between reported effects (what fires elements transmit) and assessed effects (targeting officer judgment).

**Key Delivery Notes:**
- MSS role in fires: integrates FSCM data, tracks active target lists, displays BDA from fires elements. It does not replace the fires cell's judgment.
- D3A linkage: MSS supports Detect (reporting feeds), Deliver (target list management), and Assess (BDA dashboards). It does not support the Decide step — that is a human decision.
- Hard rule for the course: every targeting product must distinguish reported effects from assessed effects. Never combine them in the same text field.

**Assessment:** Verbal check. Reported vs. assessed distinction revisited in Day 3 PE.

---

### Block 2 — Fires COP Configuration: FSCMs and Target Layers
**Hours:** 2.0 | **Method:** Demo/Lab | **Day:** 1 | **Time:** 0900–1100

**Purpose:** The fires COP must display FSCMs and the active target list simultaneously and accurately. An incorrect FSCM on the COP is a fires safety issue.

**TLO:** The trainee will configure a fires COP with FSCM overlays (correct symbology and authority reference), active target list layers, and BDA status overlays — with data currency indicators on each layer.

**Key Delivery Notes:**
- FSCM display standards: each FSCM must show the authority who established it (e.g., "CFL — BDE FSO"), the effective time (DTG established / expires), and the correct graphical symbol per FM 1-02.1.
- Target list layer: link to the targeting dataset, not a manual overlay. Each target entry must show target ID, grid, status (nominated/confirmed/engaged/BDA complete), and the data-as-of timestamp.
- BDA overlay: separate from the target list. Shows confirmed effects by target, not just engagement status.
- Danger: FSCM manually drawn (not linked to authoritative source) will not update when the FSCM is modified by higher. Always link to source.

**Student Activity:** Configure fires COP with 3 FSCMs and a provided target list. Instructor checks: FSCM authority label present, target list linked to dataset (not manual), data currency indicator visible.

**Assessment:** Foundation for Practical Exercise Task 1.

---

### Block 3 — Data Currency Verification: Targeting and BDA Feeds
**Hours:** 0.75 | **Method:** Lab | **Day:** 1 | **Time:** 1115–1200

**Purpose:** A targeting product built on stale BDA data could lead to re-engagement of a neutralized target. Data currency verification is a fires safety procedure, not a software housekeeping task.

**TLO:** The trainee will verify data currency for the target list feed and BDA reporting feed, identify a stale data condition in the training environment, and state the correct escalation procedure.

**Key Delivery Notes:**
- Check: when did the target list dataset last update? Check the transaction timestamp on the source dataset, not the COP layer.
- BDA feed: BDA reports come from fires elements after mission. If BDA is >6 hours old during active operations, the BDA layer must be labeled STALE on any product.
- Escalation: fires cell → reporting unit → C2DAO data steward. If BDA reporting has stopped, it may indicate a reporting failure or a communications outage — not absence of effects.

**Assessment:** Timestamp literacy evaluated in all Practical Exercise tasks.

---

### Block 4 — CCIR Configuration for Fires
**Hours:** 2.0 | **Method:** Lab | **Day:** 1 | **Time:** 1300–1500

**Purpose:** Fires-relevant CCIRs must fire at the right time to enable timely targeting decisions. A CCIR configured with the wrong trigger threshold or wrong data source fails the commander at the moment it matters most.

**TLO:** The trainee will configure 3 fires-relevant CCIR alerts — target-engaged status, effects-confirmed status, and FSCM violation trigger — with correct data source linkages and notification routing.

**Key Delivery Notes:**
- Target-engaged trigger: fires on target status change from "Nominated" to "Engaged" in the targeting dataset. Data source must be the targeting feed, not a manual status field.
- Effects-confirmed trigger: fires when BDA status on a target changes to "BDA Complete" or equivalent. Requires BDA feed as source.
- FSCM violation trigger: complex configuration. Requires a geospatial rule comparing target grids against FSCM geometries. Demonstrate how to configure the trigger, but note it requires data steward support to fully implement in production.
- All notifications: route to FSO (primary) and targeting officer (secondary), not to "All Users."

**Assessment:** Evaluated in Practical Exercise Task 2.

---

### Block 5 — CCIR Drill
**Hours:** 1.75 | **Method:** Exercise | **Day:** 1 | **Time:** 1515–1700

**Purpose:** Practice run. Trainees configure fires CCIRs independently against a new scenario and dataset.

**TLO:** Given a fires CCIR card, the trainee will configure 3 CCIRs and verify correct trigger behavior — without instructor assistance.

**Key Delivery Notes:**
- Instructor circulates, observes, notes readiness for Day 3 PE. Does not provide technique assistance.
- Common observation: trainees who configure the trigger threshold correctly but link the wrong data source. Catch this pattern here.

---

### Block 6 — Targeting Data Product: Confirmed vs. Suspected
**Hours:** 2.0 | **Method:** Demo/Lab | **Day:** 2 | **Time:** 0830–1030

**Purpose:** The targeting data product is the fires cell's primary contribution to the targeting working group. The confirmed/suspected target distinction is not a formatting choice — it is an operational and legal requirement.

**TLO:** The trainee will build a targeting product distinguishing confirmed from suspected targets, with attribution to reporting source, data-as-of timestamps, and current BDA status on each target element.

**Key Delivery Notes:**
- Confirmed target standard: two independent intelligence sources OR voice confirmation from a maneuver element that has eyes on. Reiterate from Block 1 doctrinal brief.
- Display convention: confirmed targets = solid engagement symbol; suspected = dashed/outlined symbol. Per FM 1-02.1.
- Attribution: each target entry must name the source(s) that confirmed it. "INT reporting" is not sufficient — name the specific feed or report number.
- BDA: if BDA is not yet received, show "BDA Pending" with the data-as-of timestamp of the last engagement update.

**Assessment:** Evaluated in Practical Exercise Task 3. Hard No-Go: target marked confirmed with single-source attribution.

---

### Block 7 — BDA Dashboard
**Hours:** 1.25 | **Method:** Lab | **Day:** 2 | **Time:** 1045–1200

**Purpose:** BDA is the effects assessment foundation for the next targeting cycle. A BDA dashboard that combines reporting from multiple fires elements without source labeling is analytically useless.

**TLO:** The trainee will build a BDA effects assessment dashboard integrating BDA data from multiple fires elements — with source attribution per fires element and explicit data currency indicators.

**Key Delivery Notes:**
- Each fires element's BDA is a separate data source. Do not aggregate without labeling the contributing sources.
- Currency indicator: show the last-reported timestamp per fires element. If one element has not reported in 8+ hours, label its BDA column as STALE.
- Dashboard summary row: overall effects picture (targets BDA complete / pending / no BDA) — this is the "fires summary" for the targeting working group.

**Assessment:** Evaluated in Practical Exercise Task 3.

---

### Block 8 — Effects Assessment and Reporting
**Hours:** 2.0 | **Method:** Demo/Lab | **Day:** 2 | **Time:** 1300–1500

**Purpose:** Effects assessment is where fires data becomes targeting intelligence. This block builds the product that a targeting officer briefs to the commander — integrating BDA, target status, and effects analysis into a cohesive product.

**TLO:** The trainee will build a fires effects assessment product integrating BDA dashboard data, target engagement status, and an effects summary — distinguishing reported effects from assessed effects with explicit labeling.

**Key Delivery Notes:**
- Reported effects section: what the BDA reports show. Direct from the dataset. No interpretation.
- Assessed effects section: targeting officer's judgment based on reported BDA. Labeled as "ASSESSED" and attributed to the officer who made the assessment and the date.
- Never combine reported and assessed in the same sentence without explicit labeling. "Target neutralized (REPORTED: BDA complete; ASSESSED: objective achieved)" is the correct format.

**Assessment:** Evaluated in Practical Exercise Task 4.

---

### Block 9 — Fires Product Drill
**Hours:** 1.75 | **Method:** Exercise | **Day:** 2 | **Time:** 1515–1700

**TLO:** The trainee will build a complete targeting and BDA product from a new dataset — without instructor assistance — applying all standards from Day 2.

---

### Block 10 — OPSEC for Fires Products
**Hours:** 1.0 | **Method:** Brief | **Day:** 3 | **Time:** 0800–0900

**Purpose:** Targeting data has the highest sensitivity in fires operations. An exported target list distributed outside the targeting working group is a significant OPSEC violation.

**TLO:** The trainee will describe OPSEC procedures for fires products: classification marking for targeting data, distribution controls, and handling instructions for target lists and BDA products.

**Key Delivery Notes:**
- Target list exports: target list with grid coordinates and engagement status is classified at the data classification level of the source. Label every export. Do not share via unclassified channels.
- BDA products: assessed effects carry the source classification. If reporting sources are classified, the BDA product inherits that classification.
- Distribution: targeting products to targeting working group only. Confirmed target lists to fires cell and S3/G3 only. Never to unsecured distribution lists.

---

### Block 11 — Targeting Data Staleness Response
**Hours:** 1.25 | **Method:** Demo/Lab | **Day:** 3 | **Time:** 0900–1015

**Purpose:** A targeting working group with stale BDA or a target list that has not updated is worse than no MSS product — it presents false confidence. Trainees must know how to identify staleness and respond before briefing.

**TLO:** The trainee will identify a targeting data staleness condition, update all affected product labels, and brief the evaluator on what can be stated with confidence and what requires caveat.

**Key Delivery Notes:**
- Staleness definition for targeting data: BDA feed >4 hours old during active operations; target list >2 hours old during a time-sensitive targeting event.
- Response: update all products with "STALE — LAST UPDATED [DTG]" label. Brief the targeting working group on the staleness before presenting the product. Do not brief a stale product as current.
- Escalation: if the target list feed is down, go to voice confirmation with the targeting cell. Document the verbal update with a DTG.

---

### Block 12 — Practical Exercise Scenario Brief and Prep
**Hours:** 1.5 | **Method:** Brief/Prep | **Day:** 3 | **Time:** 1030–1200

**Key Delivery Notes:**
- Issue scenario brief. Review Go/No-Go criteria: Pass 4 of 5 tasks. Auto No-Go: target marked confirmed with single source; stale BDA briefed as current; any product missing classification marking.

---

### Block 13 — Practical Exercise (Evaluated)
**Hours:** 4.0 | **Method:** Evaluation | **Day:** 3 | **Time:** 1300–1700

**Scenario:** Fires cell supporting a targeting working group. Two hours until the TWG. Provided: a fires dataset with target list, BDA reports from three fires elements, and an FSCM overlay. At T+90 min, evaluator injects: BDA feed from one fires element stops reporting.

**Tasks:**

| Task | Standard |
|------|----------|
| 1 | Configure fires COP: FSCMs with authority reference, target list layer, BDA overlay; verify data currency |
| 2 | Configure 3 fires CCIRs from the provided CCIR card; verify trigger behavior |
| 3 | Build targeting product: confirmed/suspected distinction, source attribution, BDA status, timestamps |
| 4 | Build BDA dashboard: multi-element BDA with source attribution and currency indicators |
| 5 | Respond to BDA feed failure inject: update products, caveat affected elements, brief evaluator |

**Go standard:** Pass 4 of 5. Auto No-Go: confirmed target with single source; stale BDA briefed as current; product missing classification marking.

---

---

# PART C — TM-40C: MOVEMENT AND MANEUVER WFF

**Duration:** 3 days (24 hours) | **T:I ratio:** 6:1 | **Instructor req:** G3/S3 background (operations officer or senior S3 NCO); TM-40-level certification or C2DAO M&M SME
**Doctrinal references:** ADP 3-0, FM 3-0, ATP 3-90.90

---

### Block 1 — Doctrinal Context: MSS in Maneuver Operations
**Hours:** 1.0 | **Method:** Brief | **Day:** 1 | **Time:** 0800–0900

**TLO:** The trainee will describe how MSS supports ADP 3-0 maneuver operations and state the distinction between reported unit positions (from MSS feeds) and confirmed positions (voice/digital verification by the S3).

**Key Delivery Notes:**
- MSS in maneuver: integrates blue force tracking feeds, displays maneuver graphics, supports MDMP products. It does not replace voice confirmation.
- Reported vs. confirmed position: a blue icon on MSS means a reporting system said a unit was at that location at that time — it does not mean the S3 has confirmed the unit is there now.
- Hard rule: never brief a unit as "at grid" from MSS alone without a voice/digital confirmation timestamp.

---

### Block 2 — Maneuver COP Configuration
**Hours:** 2.0 | **Method:** Demo/Lab | **Day:** 1 | **Time:** 0900–1100

**TLO:** The trainee will configure a maneuver COP with unit position layers, phase line and obstacle overlays, and route data sources — with data freshness indicators and correct display standards.

**Key Delivery Notes:**
- Unit position layers: link to BFT/ATAK feed, not manual placement. Show the reporting timestamp next to each icon.
- Phase lines and obstacle overlays: draw from the OPORD graphics overlay, not manual reproduction. Label with the designator from the OPORD.
- Route data: link to route database showing route condition status (open/closed/degraded) and last-verified timestamp.
- Common error: drawing phase lines by hand on the COP. This creates an unattributed overlay with no update mechanism. Correct method: import from the OPORD-generated overlay or link to the route/graphics dataset.

**Assessment:** Foundation for Practical Exercise Task 1.

---

### Block 3 — Position Data Currency and Reporting Gaps
**Hours:** 0.75 | **Method:** Lab | **Day:** 1 | **Time:** 1115–1200

**TLO:** The trainee will read position reporting timestamps for each unit displayed on the COP, identify a unit with a position reporting gap, and state the correct characterization for a briefing.

**Key Delivery Notes:**
- Position update cadence: varies by reporting system (BFT = up to 5 min, ATAK = near-real-time, manual position reports = at reporting intervals). Know the cadence for your units' reporting systems.
- Gap identification: if a unit's last position report is older than 2× the normal reporting interval, it is a reporting gap — not a confirmed position.
- Briefing characterization: "2-3 BN last reported position [GRID] at [DTG] — current position unconfirmed."

---

### Block 4 — Movement-Relevant CCIR Configuration
**Hours:** 2.0 | **Method:** Lab | **Day:** 1 | **Time:** 1300–1500

**TLO:** The trainee will configure phase line crossing alerts, objective status update triggers, and unit position reporting gap alerts — with correct data sources and notification routing.

**Key Delivery Notes:**
- Phase line crossing alert: geospatial trigger fires when a unit position icon crosses the phase line polygon. Requires the phase line as a geofence object in the alert configuration.
- Objective status trigger: fires when the objective dataset status field changes to "Secure" or "Clear." Data source must be the objective status feed, not manual.
- Reporting gap alert: fires when a unit's last position timestamp exceeds the reporting interval threshold. Configure the threshold per the supported unit's reporting standard.

**Assessment:** Evaluated in Practical Exercise Task 2.

---

### Block 5 — CCIR Configuration Drill
**Hours:** 1.75 | **Method:** Exercise | **Day:** 1 | **Time:** 1515–1700

**TLO:** Given a maneuver CCIR card, the trainee will configure phase line crossing and objective status alerts and verify trigger behavior — without instructor assistance.

---

### Block 6 — COA Overlay Build and MDMP Support
**Hours:** 2.0 | **Method:** Demo/Lab | **Day:** 2 | **Time:** 0830–1030

**TLO:** The trainee will build a COA sketch overlay in MSS linked to task organization data, formatted for a commander presentation during MDMP.

**Key Delivery Notes:**
- COA overlay: import graphics from the staff planning template. Do not redraw on the COP — import the overlay from the planning staff's digital product.
- Link the overlay to the task organization dataset: each maneuver element on the COA should reference the unit from the task org.
- MDMP format: COA overlay displays simultaneously with the current situation (threat and unit positions). The S3 must be able to show "current situation" and "proposed COA" on the same canvas.
- Trainees bring their unit's task organization from the pre-course checklist.

**Assessment:** Evaluated in Practical Exercise Task 3.

---

### Block 7 — Task Organization Visualization
**Hours:** 1.25 | **Method:** Lab | **Day:** 2 | **Time:** 1045–1200

**TLO:** The trainee will build a task organization visualization in MSS displaying all subordinate maneuver elements with readiness and position status indicators.

**Key Delivery Notes:**
- Task org display: hierarchical structure linked to the unit registry dataset. Status indicators (readiness, current task, location) update from live feeds.
- Change management: when task organization changes (TACON, OPCON, attachment), update the display within 30 minutes of the change taking effect.

---

### Block 8 — MDMP and Synchronization Products
**Hours:** 2.0 | **Method:** Demo/Lab | **Day:** 2 | **Time:** 1300–1500

**TLO:** The trainee will build a synchronization matrix visualization and a decision support product for an MDMP gate review — displaying COA comparison data from the provided dataset.

**Key Delivery Notes:**
- Synchronization matrix: time-phased display of each WFF's actions at each phase line or time hack. Link to the OPORD tasks dataset.
- Decision support product: wargame results summary — for each COA, display expected phase line achievement times, risk assessment, and critical task dependencies.
- Format: commanders want to see COA A vs. COA B side by side. Build the product for two COAs simultaneously.

**Assessment:** Evaluated in Practical Exercise Task 3.

---

### Block 9 — Maneuver Product Drill
**Hours:** 1.75 | **Method:** Exercise | **Day:** 2 | **Time:** 1515–1700

**TLO:** The trainee will build a COA overlay and task organization product from a provided OPORD fragment — without instructor assistance.

---

### Block 10 — OPSEC for Maneuver Products
**Hours:** 1.0 | **Method:** Brief | **Day:** 3 | **Time:** 0800–0900

**TLO:** The trainee will describe OPSEC procedures for maneuver data products: classification requirements for unit position data, axes of advance overlays, and route information.

**Key Delivery Notes:**
- Unit position data: current positions of friendly units are classified. Every export must be labeled. Never share via unclassified channel.
- Route overlays: MSR/ASR route overlays with condition data and traffic control point locations may be classified depending on classification level of source data.
- Axes of advance: classified when linked to an actual OPORD. Training overlays may be UNCLASSIFIED — confirm classification before sharing.

---

### Block 11 — Position Reporting Gap Response
**Hours:** 1.25 | **Method:** Demo/Lab | **Day:** 3 | **Time:** 0900–1015

**TLO:** The trainee will identify a unit position reporting gap on the COP, update the position layer with a "REPORTING GAP" indicator, and brief the evaluator on what can and cannot be stated about the affected unit's current location.

**Key Delivery Notes:**
- Correct characterization: "2-3 BN position as of [DTG] — reporting gap as of [DTG]. Last confirmed position via voice [DTG]."
- Products showing the affected unit must be caveated. Do not brief a gap as a position.
- Escalation: S3 initiates voice/digital contact to confirm position. Update the COP display when confirmed.

---

### Block 12 — Practical Exercise Scenario Brief and Prep
**Hours:** 1.5 | **Method:** Brief/Prep | **Day:** 3 | **Time:** 1030–1200

**Key Delivery Notes:**
- Issue scenario brief. Go/No-Go: Pass 4 of 5 tasks. Auto No-Go: unit position reporting gap briefed as confirmed position; any product missing classification marking.

---

### Block 13 — Practical Exercise (Evaluated)
**Hours:** 4.0 | **Method:** Evaluation | **Day:** 3 | **Time:** 1300–1700

**Scenario:** S3 section during an offensive operation. Provided: BFT feed, phase line graphic, task organization, and a COA overlay from a recent OPORD. At T+90 min, evaluator injects: one subordinate battalion's BFT stops reporting.

**Tasks:**

| Task | Standard |
|------|----------|
| 1 | Configure maneuver COP: unit positions, phase lines, obstacle overlays, routes; verify data currency |
| 2 | Configure 3 maneuver CCIRs; verify trigger behavior |
| 3 | Build COA overlay and task organization visualization; format for commander presentation |
| 4 | Build MDMP decision support product for a 2-COA wargame |
| 5 | Respond to reporting gap inject: update COP, caveat product, brief evaluator correctly |

**Go standard:** Pass 4 of 5. Auto No-Go: reporting gap briefed as confirmed position; product missing classification marking.

---

---

# PART D — TM-40D: SUSTAINMENT WFF

**Duration:** 3 days (24 hours) | **T:I ratio:** 6:1 | **Instructor req:** G4/S4 background (logistics officer or senior S4 NCO); TM-40-level certification or C2DAO sustainment SME
**Doctrinal references:** ADP 4-0, FM 4-0, ATP 4-0.1

---

### Block 1 — Doctrinal Context: MSS in Sustainment
**Hours:** 1.0 | **Method:** Brief | **Day:** 1 | **Time:** 0800–0900

**TLO:** The trainee will describe how MSS supports ADP 4-0 sustainment operations and state the distinction between reported readiness (LOGSTAT submission) and estimated readiness (S4 calculation when reporting is delayed).

**Key Delivery Notes:**
- MSS role in sustainment: integrates LOGSTAT data, displays logistics overlays, enables readiness alerts. It does not replace the S4's situational understanding.
- Reported vs. estimated readiness: if the last LOGSTAT is 24 hours old during operations, MSS shows reported readiness from 24 hours ago. The S4 must estimate current readiness — and label it as estimated.
- Hard rule: never brief LOGSTAT data as "current" without checking the submission timestamp.

---

### Block 2 — Logistics COP Configuration
**Hours:** 2.0 | **Method:** Demo/Lab | **Day:** 1 | **Time:** 0900–1100

**TLO:** The trainee will configure a logistics COP with readiness status overlays, supply class distribution displays, and transportation network layers — with data-as-of timestamps on each layer.

**Key Delivery Notes:**
- Readiness overlays: color-code by C-rating (C1=GREEN, C2=AMBER, C3/C4=RED). Link to LOGSTAT dataset, not manual entry.
- Supply class layer: display Class III/V/IX status by supported element. Link to supply management dataset.
- Transportation network: route condition status (open/closed) and convoy position if available. Link to logistics movement dataset.
- Common error: manually entering readiness data into the overlay. Manual data will not update when LOGSTAT refreshes. Always link to source.

**Assessment:** Foundation for Practical Exercise Task 1.

---

### Block 3 — LOGSTAT Pipeline Currency Verification
**Hours:** 0.75 | **Method:** Lab | **Day:** 1 | **Time:** 1115–1200

**TLO:** The trainee will verify LOGSTAT pipeline currency, identify a delayed submission in the training dataset, and state the correct characterization for a sustainment synchronization brief.

**Key Delivery Notes:**
- LOGSTAT submission cadence: typically 2×/day during operations. A unit that has not submitted in >12 hours during operations is a gap.
- Gap identification: check the LOGSTAT dataset for units with submission timestamps older than the submission cadence. These are gaps, not current reporting.
- Briefing characterization: "3-BDE readiness as of [DTG LAST SUBMISSION] — current readiness estimated at [ESTIMATED LEVEL] based on [LOGIC]."

---

### Block 4 — CCIR Configuration for Sustainment
**Hours:** 2.0 | **Method:** Lab | **Day:** 1 | **Time:** 1300–1500

**TLO:** The trainee will configure readiness-below-threshold CCIR alerts, supply shortage notifications, and LOGSTAT submission gap alerts — with correct thresholds and notification routing.

**Key Delivery Notes:**
- Readiness threshold alert: fires when a unit's reported C-rating drops below C2 (configurable threshold). Data source: LOGSTAT readiness field.
- Supply shortage alert: fires when Class III/V stock drops below a defined days-of-supply threshold. Confirm the threshold with the S4 before configuring.
- Submission gap alert: fires when a unit has not submitted LOGSTAT within the submission window. Configuration: timestamp comparison against the expected cadence.
- Notifications: all sustainment CCIRs route to S4 (primary) and XO (secondary).

**Assessment:** Evaluated in Practical Exercise Task 2.

---

### Block 5 — CCIR Drill
**Hours:** 1.75 | **Method:** Exercise | **Day:** 1 | **Time:** 1515–1700

**TLO:** Given a sustainment CCIR card, the trainee will configure 3 sustainment CCIRs and verify trigger behavior — without instructor assistance.

---

### Block 6 — Supply Chain Status Product
**Hours:** 2.0 | **Method:** Demo/Lab | **Day:** 2 | **Time:** 0830–1030

**TLO:** The trainee will build a supply chain status product for a sustainment synchronization brief — showing supply class status by supported element with data-as-of timestamps and shortfall flags.

**Key Delivery Notes:**
- Supply class status rows: one row per supported unit, one column per supply class. Status = ADEQUATE / SHORTAGE / CRITICAL. Define thresholds before building.
- Shortfall flag: any Class III below X days of supply or Class IX critical parts shortage should be flagged RED with the specific shortage labeled (not just a red cell).
- Data-as-of: each supply class status cell must show the timestamp of the last LOGSTAT submission that drove the status. Different units submit at different times — timestamps will vary.

**Assessment:** Evaluated in Practical Exercise Task 3.

---

### Block 7 — Distribution Data and Transportation Overlays
**Hours:** 1.25 | **Method:** Lab | **Day:** 2 | **Time:** 1045–1200

**TLO:** The trainee will display transportation route overlays, active convoy position data, and distribution node status — linked to the logistics movement dataset.

**Key Delivery Notes:**
- Route condition: status per each MSR/ASR (open/closed/degraded). Link to route condition dataset. If route data is manual, caveat as "not from authoritative source."
- Convoy tracking: if LOGPAX/ATAK data is available, display active convoy positions. If not, display planned movement windows with estimated arrival times.
- Distribution nodes: show BSA/FSB position and status. Link to logistics node registry.

---

### Block 8 — Readiness Dashboard for Sustainment Sync
**Hours:** 2.0 | **Method:** Demo/Lab | **Day:** 2 | **Time:** 1300–1500

**TLO:** The trainee will build an integrated readiness dashboard combining LOGSTAT data with supply class status and distribution status — formatted for a sustainment synchronization brief and BUA.

**Key Delivery Notes:**
- Dashboard layout: readiness summary at top (overall unit readiness by C-rating), supply class status table in center, distribution status at bottom.
- BUA format: commanders want one page with: overall readiness status, biggest shortfall, recovery action, and timeline. Build this as a single-screen product.
- Data-as-of banner: show the oldest timestamp among all displayed data sources at the top of the dashboard. This is the "freshness floor" — all data on this dashboard is at least as current as this timestamp.

**Assessment:** Evaluated in Practical Exercise Task 3.

---

### Block 9 — Sustainment Product Drill
**Hours:** 1.75 | **Method:** Exercise | **Day:** 2 | **Time:** 1515–1700

**TLO:** The trainee will build a readiness summary and supply chain status product from a provided LOGSTAT dataset — without instructor assistance.

---

### Block 10 — OPSEC for Sustainment Products
**Hours:** 1.0 | **Method:** Brief | **Day:** 3 | **Time:** 0800–0900

**TLO:** The trainee will describe OPSEC procedures for sustainment products: classification for readiness data, handling instructions for supply status, and distribution controls.

**Key Delivery Notes:**
- Readiness data: C-rating information for formations is classified. Do not share via unclassified channel.
- Class V status: ammunition supply information is classified. Label accordingly.
- Distribution: sustainment sync products to S4 and XO only. Readiness data to CDR/XO/S4 only. Do not include in all-hands products.

---

### Block 11 — LOGSTAT Data Staleness Response
**Hours:** 1.25 | **Method:** Demo/Lab | **Day:** 3 | **Time:** 0900–1015

**TLO:** The trainee will identify a LOGSTAT submission gap, estimate current readiness using the S4's estimation methodology, and brief the evaluator on the difference between reported and estimated readiness.

**Key Delivery Notes:**
- When a LOGSTAT is >12 hours old: do not brief the old submission as current. State: "Readiness as reported at [DTG]. Current readiness estimated [LEVEL] — LOGSTAT gap since [DTG]."
- Estimation methodology: prior submission rate + known consumption rate + activities since last submission. Document the estimation logic.
- Escalation: contact the non-submitting unit directly. If no contact possible, brief the gap to the CDR before the sustainment sync.

---

### Block 12 — Practical Exercise Scenario Brief and Prep
**Hours:** 1.5 | **Method:** Brief/Prep | **Day:** 3 | **Time:** 1030–1200

---

### Block 13 — Practical Exercise (Evaluated)
**Hours:** 4.0 | **Method:** Evaluation | **Day:** 3 | **Time:** 1300–1700

**Scenario:** S4 section preparing for a sustainment synchronization brief. Provided: LOGSTAT dataset from subordinate units, supply class status data, and a transportation overlay. At T+90 min, evaluator injects: one subordinate unit's LOGSTAT submission is now 18 hours old.

**Tasks:**

| Task | Standard |
|------|----------|
| 1 | Configure logistics COP: readiness overlays, supply class layers, transportation data; verify currency |
| 2 | Configure 3 sustainment CCIRs; verify trigger behavior |
| 3 | Build supply chain status product and readiness dashboard for sustainment sync |
| 4 | Respond to LOGSTAT gap inject: estimate readiness, update dashboard, brief evaluator |
| 5 | Apply OPSEC procedures to all sustainment products |

**Go standard:** Pass 4 of 5. Auto No-Go: stale LOGSTAT briefed as current; product missing classification marking.

---

---

# PART E — TM-40E: PROTECTION WFF

**Duration:** 3 days (24 hours) | **T:I ratio:** 6:1 | **Instructor req:** Force protection officer or CBRN background; TM-40-level certification or C2DAO Protection SME
**Doctrinal references:** ADP 3-37, ATP 3-37.2

---

### Block 1 — Doctrinal Context: MSS in Force Protection
**Hours:** 1.0 | **Method:** Brief | **Day:** 1 | **Time:** 0800–0900

**TLO:** The trainee will describe how MSS supports ADP 3-37 protection operations and state the difference between reported threat incidents (from MSS feeds) and assessed threat patterns (FP officer judgment).

**Key Delivery Notes:**
- MSS role in protection: aggregates threat incident reporting, displays installation and route vulnerability overlays, enables CCIR alerts for FP events. It does not replace threat assessment.
- Reported vs. assessed threat: MSS can show 14 threat incidents in a grid square over 30 days. The FP officer assesses whether this constitutes a pattern. Never brief aggregated data as an assessment without that judgment step.
- Hard rule: all protection products must identify whether coverage of an area is adequate or inadequate based on reporting density — not just presence/absence of incidents.

---

### Block 2 — Threat Data Layer Configuration
**Hours:** 2.0 | **Method:** Demo/Lab | **Day:** 1 | **Time:** 0900–1100

**TLO:** The trainee will configure threat incident layers, IED reporting feeds, and threat trend overlays on the MSS protection COP — with source attribution and data freshness verification.

**Key Delivery Notes:**
- Threat incident layer: link to threat reporting dataset. Each incident icon must show: incident type, date/time of occurrence (not date/time of reporting), reporting source, and current status (confirmed/unconfirmed).
- IED reporting: date of occurrence vs. date of reporting can differ significantly. Display the occurrence date on the map — not the reporting date.
- Threat trend overlay: heat map or density overlay showing incident concentration over a configurable time window. Link to the same source dataset.
- Source attribution: every threat incident must name the reporting source (patrol report, human intelligence, law enforcement). Aggregated layers that don't preserve source attribution are not useful for assessment.

**Assessment:** Foundation for Practical Exercise Task 1.

---

### Block 3 — Vulnerability Assessment Visualization
**Hours:** 0.75 | **Method:** Lab | **Day:** 1 | **Time:** 1115–1200

**TLO:** The trainee will configure installation perimeter overlays and route vulnerability displays — cross-referencing threat layers with friendly position data to show exposure areas.

**Key Delivery Notes:**
- Perimeter overlay: installation boundary linked to facility registry. Show entry/exit control points as labeled icons.
- Route vulnerability: cross-reference route overlay with threat incident density. Highlight route segments that pass through high-incident-density areas.
- Exposure analysis: areas where friendly force movement patterns (from BFT/LOGSTAT) intersect with high threat density. This is an analytical product — label it as "ASSESSED EXPOSURE" not as confirmed threat.

---

### Block 4 — Force Protection CCIR Configuration
**Hours:** 2.0 | **Method:** Lab | **Day:** 1 | **Time:** 1300–1500

**TLO:** The trainee will configure threat-in-area triggers, casualty threshold CCIR alerts, and CBRN event triggers — with correct geographic boundaries and notification routing.

**Key Delivery Notes:**
- Threat-in-area trigger: geospatial alert fires when a threat incident is reported within a defined geographic boundary (installation perimeter, patrol route corridor).
- Casualty threshold: fires when PERSTAT casualty count in a reporting period exceeds threshold. Data source: PERSTAT feed.
- CBRN event alert: fires when CBRN sensor data in the source feed reports a detection event. Requires CBRN sensor feed access — confirm with C2DAO before configuring.
- All FP CCIRs: primary notification to FP officer, secondary to CDR/XO.

**Assessment:** Evaluated in Practical Exercise Task 2.

---

### Block 5 — CCIR Drill
**Hours:** 1.75 | **Method:** Exercise | **Day:** 1 | **Time:** 1515–1700

**TLO:** Given a force protection CCIR card, the trainee will configure 3 FP CCIRs and verify trigger behavior — without instructor assistance.

---

### Block 6 — CBRN Data Visualization
**Hours:** 2.0 | **Method:** Demo/Lab | **Day:** 2 | **Time:** 0830–1030

**TLO:** The trainee will display CBRN sensor data layers, contamination overlays, and downwind hazard estimate visualizations — with data currency requirements for CBRN products.

**Key Delivery Notes:**
- CBRN sensor layer: display sensor location icons linked to the CBRN sensor feed. Status indicator: active/no-read/offline. Offline sensors must be labeled — an offline sensor has no coverage; that coverage gap must be visible.
- Contamination overlay: show the contamination area polygon from the CBRN reporting dataset. Include the detection DTG on the polygon label.
- Downwind hazard estimate: link to the CBRN downwind hazard estimate dataset if available. Show the hazard area and the estimate validity window. After the validity window expires, label the estimate as EXPIRED.
- CBRN data currency: CBRN products require the freshest available data. If sensor data is >1 hour old, the CBRN display must show a STALE warning.

**Assessment:** Evaluated in Practical Exercise Task 3.

---

### Block 7 — PERSTAT and Accountability Dashboard
**Hours:** 1.25 | **Method:** Lab | **Day:** 2 | **Time:** 1045–1200

**TLO:** The trainee will build a PERSTAT display integrating strength data from subordinate elements with accountability status indicators and data-as-of timestamps per reporting unit.

**Key Delivery Notes:**
- PERSTAT display: one row per subordinate element, columns for personnel strength (assigned/attached/present), casualty status, and last-submission timestamp.
- Accountability status: FULLY ACCOUNTED / PARTIALLY ACCOUNTED / NOT REPORTED. Each status tied to whether the unit has submitted a PERSTAT within the reporting window.
- Data-as-of: timestamp per row (not a single banner timestamp — units submit at different times and their currency differs).

**Assessment:** Evaluated in Practical Exercise Task 3.

---

### Block 8 — Integrated Protection Picture
**Hours:** 2.0 | **Method:** Demo/Lab | **Day:** 2 | **Time:** 1300–1500

**TLO:** The trainee will build an integrated protection picture combining threat overlays, CBRN data, vulnerability assessment, and PERSTAT — formatted for a protection working group at O-4/O-5 audience level.

**Key Delivery Notes:**
- Layout: threat situation at top, CBRN status in center, PERSTAT at bottom. The commander needs to see all three simultaneously.
- Integrated product format: one product, three data domains. No switching between applications during the protection working group brief.
- Caveat requirements: any data element older than its update cadence must be labeled STALE with the as-of timestamp. The commander must be able to assess the currency of every displayed element in under 30 seconds.

**Assessment:** Evaluated in Practical Exercise Task 4.

---

### Block 9 — Protection Product Drill
**Hours:** 1.75 | **Method:** Exercise | **Day:** 2 | **Time:** 1515–1700

**TLO:** The trainee will build a CBRN overlay and PERSTAT display from a provided dataset — without instructor assistance.

---

### Block 10 — OPSEC for Force Protection Products
**Hours:** 1.0 | **Method:** Brief | **Day:** 3 | **Time:** 0800–0900

**TLO:** The trainee will describe OPSEC procedures for force protection products: classification for threat incident data, handling for CBRN products, and distribution controls.

**Key Delivery Notes:**
- Threat incident data: specific location and timing data for threat incidents is classified. Never share via unclassified channel.
- CBRN products: contamination overlays with sensor location data are classified based on source. CBRN downwind hazard estimates may be FOUO minimum.
- PERSTAT: accountability data with casualty counts is classified. Do not include in unclassified products.
- Vulnerability assessment products: installation perimeter overlays with entry/exit points are classified. Distribute to FP cell only.

---

### Block 11 — Reporting Gap and CBRN Sensor Offline Response
**Hours:** 1.25 | **Method:** Demo/Lab | **Day:** 3 | **Time:** 0900–1015

**TLO:** The trainee will identify a CBRN sensor offline condition, update the protection COP to label the coverage gap, and brief the evaluator on what can and cannot be stated about the area previously covered by that sensor.

**Key Delivery Notes:**
- Sensor offline: mark the sensor icon as OFFLINE on the COP. Update the coverage overlay to show the gap area (the area that sensor covered is now without coverage).
- Briefing characterization: "Sensor [ID] offline as of [DTG]. [AREA] has no current CBRN detection coverage. Last clear reading from this sensor [DTG]."
- Do not brief the previously covered area as clear. Correct: "No detection as of [LAST READING DTG] — no current coverage."
- Actions: escalate to CBRN cell. Deploy backup CBRN monitoring if available. Brief the CDR on the coverage gap before the protection working group.

---

### Block 12 — Practical Exercise Scenario Brief and Prep
**Hours:** 1.5 | **Method:** Brief/Prep | **Day:** 3 | **Time:** 1030–1200

---

### Block 13 — Practical Exercise (Evaluated)
**Hours:** 4.0 | **Method:** Evaluation | **Day:** 3 | **Time:** 1300–1700

**Scenario:** FP officer preparing for a protection working group. Provided: threat incident dataset, CBRN sensor data, and PERSTAT from subordinate units. At T+90 min, evaluator injects: CBRN sensor covering the main supply route goes offline.

**Tasks:**

| Task | Standard |
|------|----------|
| 1 | Configure threat data layers and vulnerability overlays; verify data currency and source attribution |
| 2 | Configure 3 FP CCIRs; verify trigger behavior |
| 3 | Build CBRN overlay and PERSTAT dashboard with timestamps |
| 4 | Build integrated protection picture for O-5 audience |
| 5 | Respond to CBRN sensor offline inject: update COP, caveat coverage gap, brief evaluator |

**Go standard:** Pass 4 of 5. Auto No-Go: offline sensor area briefed as clear; product missing classification marking.

---

---

# PART F — TM-40F: MISSION COMMAND WFF

**Duration:** 3 days (24 hours) | **T:I ratio:** 6:1 | **Instructor req:** G3/S3, battle captain, or XO background; TM-40-level certification or C2DAO Mission Command SME
**Doctrinal references:** ADP 6-0, FM 6-0

---

### Block 1 — Doctrinal Context: MSS in Mission Command
**Hours:** 1.0 | **Method:** Brief | **Day:** 1 | **Time:** 0800–0900

**TLO:** The trainee will describe how MSS supports ADP 6-0 mission command and state the distinction between reported status (what MSS displays) and assessed status (what the commander judges).

**Key Delivery Notes:**
- MSS role in mission command: integrates operational data, displays COP, enables CCIR alerts, and supports battle rhythm products. It does not make decisions.
- The mission command principle of "disciplined initiative" applies to MSS: the COP informs — it does not direct.
- Hard rule: the assessed status (commander's judgment) must never be confused with reported status (what feeds show). Every MSS product must be clear about which it is presenting.

---

### Block 2 — COP Configuration for Mission Command
**Hours:** 2.0 | **Method:** Demo/Lab | **Day:** 1 | **Time:** 0900–1100

**TLO:** The trainee will configure a mission command COP with appropriate layers for echelon (BCT or above), data freshness indicators, and correct source attribution per layer.

**Key Delivery Notes:**
- Echelon-appropriate layers: BCT-level COP shows subordinate battalion and higher echelon data. Do not display company-level detail at BCT level — it clutters the picture.
- Layer configuration: each layer must name its source pipeline, display the last-updated timestamp, and indicate the update cadence.
- Data freshness indicator: if any layer is older than its expected cadence, it must display a STALE indicator. The CDR needs to know at a glance which information is current.
- Common error: too many layers on the COP. Mission command COP should show: unit positions, FSCM/graphical control measures, status overlays (readiness, supply), and CCIR status. All on one clean display.

**Assessment:** Foundation for Practical Exercise Task 1.

---

### Block 3 — Data Currency Verification
**Hours:** 0.75 | **Method:** Lab | **Day:** 1 | **Time:** 1115–1200

**TLO:** The trainee will verify data currency for each COP layer, identify a stale feed in the training environment, and describe the escalation path.

**Key Delivery Notes:**
- Currency check procedure: for each layer, open the source dataset and read the last transaction timestamp. Compare to the expected update cadence. Document the result before any briefing.
- Staleness threshold: if a layer is older than 2× its expected cadence, it is stale for briefing purposes.
- Escalation: data steward → pipeline owner → C2DAO. If a layer cannot be verified as current, it must be labeled STALE on any product derived from it.

---

### Block 4 — CCIR Configuration for Mission Command
**Hours:** 2.0 | **Method:** Lab | **Day:** 1 | **Time:** 1300–1500

**TLO:** The trainee will configure mission command CCIRs with correct thresholds, data sources, and notification routing — covering at least one readiness trigger, one operational event trigger, and one time-based reminder.

**Key Delivery Notes:**
- Readiness trigger: C-rating below threshold on a subordinate element. Data source: LOGSTAT feed.
- Operational event trigger: objective status change, phase line crossing, or significant event in the operational dataset. Must link to the specific dataset that tracks that event.
- Time-based reminder: CCIR review cadence reminder (e.g., "No CCIR update in 4 hours"). Configured as a scheduled alert, not a data trigger.
- All CCIRs: route to CDR (primary), XO (secondary), battle captain (tertiary).

**Assessment:** Evaluated in Practical Exercise Task 2.

---

### Block 5 — CCIR Configuration Drill
**Hours:** 1.75 | **Method:** Exercise | **Day:** 1 | **Time:** 1515–1700

**TLO:** Given a commander's CCIR guidance, the trainee will configure mission command CCIRs and verify trigger behavior — without instructor assistance.

---

### Block 6 — Battle Rhythm Dashboard
**Hours:** 2.0 | **Method:** Demo/Lab | **Day:** 2 | **Time:** 0830–1030

**TLO:** The trainee will build a battle rhythm dashboard tracking the weekly meeting cycle — linking each meeting to its associated data products and displaying product readiness status.

**Key Delivery Notes:**
- Battle rhythm display: weekly calendar format showing each meeting (BUA, SYNC, ADVON, planning gate reviews). For each meeting, display: scheduled time, associated products, and product readiness status (Ready / In Work / Not Started).
- Product linkage: each meeting links to the data products required for it. Clicking on BUA shows the BUA read-ahead workspace; clicking on SYNC shows the synchronization product.
- Update cadence: the battle rhythm dashboard updates on a daily basis. The battle captain is responsible for confirming product readiness status each morning.

**Assessment:** Evaluated in Practical Exercise Task 3.

---

### Block 7 — BUA and Assessment Products
**Hours:** 1.25 | **Method:** Lab | **Day:** 2 | **Time:** 1045–1200

**TLO:** The trainee will build a BUA read-ahead product integrating readiness, operational, and intelligence data — formatted for O-5/CG audience, with data-as-of timestamps on every element.

**Key Delivery Notes:**
- BUA product: one-screen product with four panels: (1) readiness status (by element, C-rating), (2) operational situation (COP summary, key events since last BUA), (3) intelligence summary (threat activity, PIR status), (4) next 24 hours (planned activities, CCIRs to watch).
- Timestamp: each panel has a data-as-of timestamp. The CDR needs to know which information is from this morning and which is from yesterday evening.
- Format: the BUA is a decision support product. Every data element should drive a decision or inform a commander's assessment. Remove any element that does not serve that purpose.

**Assessment:** Evaluated in Practical Exercise Task 3.

---

### Block 8 — Battle Tracking and SITREP Products
**Hours:** 2.0 | **Method:** Demo/Lab | **Day:** 2 | **Time:** 1300–1500

**TLO:** The trainee will build a battle tracking product and SITREP format in MSS — distinguishing reported events from assessed operational significance, with explicit timestamps.

**Key Delivery Notes:**
- Battle tracking: chronological event log linked to the operational event dataset. Each event shows: DTG, reporting unit, event type, location, and current status (ongoing/completed/unconfirmed).
- SITREP format: situation summary at top (current operational status as assessed by the S3), events below (reported, linked to the battle tracking dataset), CCIR status at bottom.
- Reported vs. assessed: the SITREP situation summary is the S3's assessed operational picture. Events are reported. Never put a situation summary in the events log or vice versa.

**Assessment:** Evaluated in Practical Exercise Task 4.

---

### Block 9 — Commander Product Drill
**Hours:** 1.75 | **Method:** Exercise | **Day:** 2 | **Time:** 1515–1700

**TLO:** The trainee will build a BUA read-ahead from a provided operational dataset — without instructor assistance.

---

### Block 10 — OPSEC for Mission Command Products
**Hours:** 1.0 | **Method:** Brief | **Day:** 3 | **Time:** 0800–0900

**TLO:** The trainee will describe OPSEC procedures for mission command products: classification handling for CCIR status, BUA products, and SITREPs; export controls; and CP displacement data continuity procedures.

**Key Delivery Notes:**
- CCIR status: the fact that a CCIR has been triggered is classified. Do not share trigger logs in unclassified products.
- BUA products: BUA read-aheads with readiness data and operational assessment are classified. Control distribution to BUA attendees only.
- CP displacement continuity: MSS data handoff procedure when displacing. Before moving, snapshot the COP and confirm the receiving CP has access restored before the displacing CP goes offline.

---

### Block 11 — Data Staleness and Feed Failure Response
**Hours:** 1.25 | **Method:** Demo/Lab | **Day:** 3 | **Time:** 0900–1015

**TLO:** The trainee will identify a data feed failure affecting the mission command COP, update affected products with STALE labels, and brief the evaluator on what can be briefed confidently and what requires caveat.

**Key Delivery Notes:**
- Feed failure response: identify which COP layers are affected, label them STALE, and update the data-as-of indicator.
- Products derived from the stale feed must also be labeled: "Readiness data as of [DTG LAST GOOD] — feed offline since [DTG]."
- Briefing guidance: brief the CDR on the staleness before presenting any product derived from the failed feed. "Sir/Ma'am, readiness data is stale as of [DTG] — I'll brief what we have with that caveat."

---

### Block 12 — Practical Exercise Scenario Brief and Prep
**Hours:** 1.5 | **Method:** Brief/Prep | **Day:** 3 | **Time:** 1030–1200

**Key Delivery Notes:**
- Issue scenario brief. Go/No-Go: Pass 4 of 5 tasks. Auto No-Go: stale data briefed as current; CCIR product without classification marking; BUA product not formatted for CDR audience.

---

### Block 13 — Practical Exercise (Evaluated)
**Hours:** 4.0 | **Method:** Evaluation | **Day:** 3 | **Time:** 1300–1700

**Scenario:** Battle captain/S3 preparing for a BUA with the CG in two hours. Provided: multi-layer operational data, CCIR card, and a battle rhythm from a recent exercise. At T+90 min, evaluator injects: readiness data feed from one subordinate brigade stops updating.

**Tasks:**

| Task | Standard |
|------|----------|
| 1 | Configure mission command COP with echelon-appropriate layers; verify data currency |
| 2 | Configure 3 mission command CCIRs; verify trigger behavior |
| 3 | Build battle rhythm dashboard and BUA read-ahead product |
| 4 | Build battle tracking product and SITREP; distinguish reported from assessed |
| 5 | Respond to readiness feed failure inject: update COP and products, caveat, brief evaluator |

**Go standard:** Pass 4 of 5. Auto No-Go: stale data briefed as current to CDR; product missing classification marking.

---

---

## WFF INSTRUCTOR NOTES — APPLICABLE TO ALL TRACKS

**Before Day 1:**
- Confirm training environment access for all trainees — standard user access is sufficient but must be verified.
- Review the track-specific CONCEPTS_GUIDE and confirm trainees completed required pre-reading.
- Prepare a track-specific training dataset (or use provided training data). All scenarios and drills reference this dataset.
- Know the Go/No-Go criteria cold — the evaluator does not refer to a checklist during Day 3. They know the standards.

**Day 3 Evaluation Standards:**
- Evaluator is observer-only until the collection/reporting gap inject at T+90 min.
- After the inject, the evaluator plays the role described in the scenario (commander waiting for a brief, targeting board member, etc.).
- Hard No-Go conditions are not subject to partial credit. A trainee who briefs a stale/gap feed as current does not pass, regardless of other task performance.
- Go/No-Go decision is communicated at end of Day 3, before trainees leave.

**T:I Ratio:** 6:1 maximum. Do not exceed. WFF courses require individual instructor assessment during Blocks 2, 4, 6, 8, and 13.

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*TM-40 WFF Track Lesson Plan Outlines | Version 1.0 | March 2026*
