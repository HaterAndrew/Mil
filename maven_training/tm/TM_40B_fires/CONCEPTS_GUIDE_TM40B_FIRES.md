# CONCEPTS GUIDE — TM-40B COMPANION — Fires Warfighting Function — Maven Smart System (MSS)

> **Purpose:** This guide is the conceptual companion to TM-40B. It explains the WHY behind fires operations in MSS — the doctrinal logic that makes certain data requirements non-negotiable, the mental models that separate effective fires practitioners from those who treat MSS as an expensive slide deck, and the failure patterns fires units must actively avoid.
> *HQ USAREUR-AF · v1.0 · 2026 · DISTRIB: USG only*

---

## SECTION 1 — THE FIRES WFF AND DATA

### The Fires Principles Are Data Requirements in Disguise

ADP 3-19 establishes five fires principles: massed effects, range, accuracy, responsiveness, and sustainability. Every fires commander and fires officer can recite them. Fewer have thought through what each principle demands from a data management perspective. When you read ADP 3-19's fires principles with MSS in mind, they become a prescription for the data standards your fires cell must maintain.

| ADP 3-19 Principle | MSS Data Obligation |
|-------------------|---------------------|
| **Massed effects** | Current target data in the HPTL. A well-maintained HPTL is the fires team's shared picture of where mass matters. Stale or ambiguous target data makes massing effects impossible. |
| **Range** | Current asset position overlays and range ring displays. Units whose asset status data is outdated in MSS are planning fires with blindfolded range analysis. |
| **Accuracy** | Target location data with confidence levels; current MET data; valid ballistic computation inputs. MSS requires location source and confidence level fields on every target record, making target location error visible. |
| **Responsiveness** | Current FSEM tracking asset assignment and request approval status. A fires cell that updates the FSEM in real time can tell the FSCOORD within seconds whether a new fires request can be accommodated. |
| **Sustainability** | Current Class V data enabling proactive resupply forecasting. The fires cell that tracks ammunition consumption rigorously in MSS can prevent shortfalls rather than confirm them after the fact. |

Each fires principle, properly understood, creates a specific data quality obligation. Officers who approach MSS as a data entry burden have inverted the relationship. The data is the fires capability.

### Fires Data as Safety Data

In most military applications, poor data quality is an operational inconvenience. In fires, poor data quality is a safety hazard.

The most consequential fires safety data in MSS is FSCM data. An FSCM is not merely an administrative boundary — it is the legal and safety framework within which lethal fires are authorized. When an NFA is entered with the wrong boundary in MSS, and a subordinate FSO clears fires based on that display, the result can be fires on a protected site, a civilian area, or a medical facility. When an RFL expires and is not updated in MSS, a unit clearing fires based on an expired restrictive measure may inadvertently fire across a boundary into adjacent friendly forces.

The consequences of stale FSCM data are not hypothetical. Fratricide events in historical operations have traced to FSCM confusion — cases where coordination measures were updated in one system but not propagated to others. MSS reduces this risk by centralizing FSCM publication in a single platform visible to all fires users simultaneously. But that reduction in risk only materializes when FSCM data is entered correctly, updated promptly, and verified before clearance of fires near coordination boundaries.

Target coordinate data carries a similar safety obligation. A target that has moved since it was last reported carries a stale coordinate. The confidence level field in the MSS target record exists precisely to flag this risk. "Templated" means expected, not confirmed. Fires against a templated target in a complex operational environment require additional verification.

ROE data in MSS is the third critical safety domain. The rules of engagement governing who can be targeted, what collateral damage thresholds apply, and under what circumstances fires are authorized are the legal constraints on lethal action. The FSCOORD who allows ROE data in MSS to lag behind the actual, current ROE authorization is creating risk at the intersection of operational law and lethal decision-making.

### The Data Stewardship Obligation for Fires Officers

The fires data stewardship obligation begins with the FSCOORD and cascades to every fires officer and NCO in the formation. Data stewardship in the fires context means three things:

| Obligation | Definition |
|------------|------------|
| **Data currency** | MSS fires data reflects the current operational situation. FSCMs updated when they change. Targets updated when collection reports new information. Asset status updated on the reporting cycle. Ammunition data updated daily and on event. |
| **Data accuracy** | What is entered in MSS is correct. Coordinate errors, wrong FSCM types, incorrect confidence levels, and missing BDA data all degrade the fires operational picture. |
| **Command authority over data changes** | HPTL changes require FSCOORD approval. FSCM changes require the establishing headquarters' authorization. Engagement authority changes require the AMD TF commander. These constraints exist in MSS through access controls and through command climate. |

---

## SECTION 2 — TARGETING AS A DATA PROCESS

### Precision as a Data Property

There is a conceptual shift embedded in how MSS changes fires operations that fires commanders should make explicit to their teams: precision in fires is now partly a data property, not just a ballistic property.

Before integrated fires data platforms, fires precision was almost entirely a function of the ballistic solution. MSS introduces a data precision dimension. A ballistically perfect fire mission delivered to an incorrect or outdated target location is not a precise engagement — it is a precise application of fires at the wrong place. Target location data quality, FSCM boundary accuracy, and sensor feed currency are now as much drivers of fires precision as ballistic computation.

### The D3A Circuit

FM 3-60 describes the D3A methodology as four steps: Decide, Detect, Deliver, Assess. This sequential description is useful for instruction. It is misleading if taken as a description of how targeting actually operates in combat.

Targeting is not a linear four-step process. It is a continuous information circuit. The Assess phase does not conclude the targeting cycle — it feeds the Decide phase for the next cycle. Detection data does not arrive in a clean stream after the Decide phase is complete — it arrives continuously, often disrupting and updating target data established at the last targeting working group. Delivery does not wait for a complete Assess phase.

MSS, properly used, supports this circuit by making the data connections between phases visible and fast. The unit that uses MSS to run a continuous targeting circuit operates at a targeting tempo its adversary cannot match. The unit that uses MSS as a periodic update system runs the targeting circuit at a fraction of its potential speed.

### MSS and Each Phase of D3A

**Decide phase — the target library as a living document.** The FSCOORD and targeting officer must treat the HPTL as a continuously managed data product rather than a periodic publication. When the commander's guidance changes, the HPTL in MSS must reflect that change before subordinate fires elements begin planning. A subordinate FSO planning fires support based on an outdated HPTL is misaligned with the commander's intent, and neither the FSO nor the FSCOORD will know it unless the HPTL in MSS reflects the current guidance.

**Detect phase — sensor integration and the confidence problem.** Target detection in MSS is only as good as the data that enters the platform. The confidence level assigned to each target in MSS is the detect phase's most important output:

| Confidence Level | Meaning | Planning/ROE Implication |
|-----------------|---------|--------------------------|
| Confirmed | Positively identified by two or more independent sources | Highest confidence; standard fires planning applies |
| Suspected | Reported by one source; awaits corroboration | Different risk calculus; additional verification required |
| Templated | Placed at expected location based on OPFOR TTPs, not actual detection | Fires against templated targets carry heightened legal and operational risk |

**Deliver phase — fires mission tracking and the deconfliction problem.** The Deliver phase in MSS is about visibility and deconfliction, not execution. AFATDS executes. MSS makes execution visible to the fires staff. The critical fires staff function during the Deliver phase is deconfliction — ensuring fire missions do not occupy the same airspace simultaneously, that fires near FSCM boundaries are coordinated before clearance, and that the fires cell knows which assets are committed before assigning new ones.

The latency problem in the Deliver phase is real: the time between a mission being fired at AFATDS and the corresponding MSS record being updated may be non-trivial if the AFATDS-MSS interface is degraded. Fires cells must account for this latency in deconfliction procedures.

**Assess phase — BDA as a decision product, not a historical record.** BDA in MSS is operationally useful only if it is entered correctly, entered timely, and used to drive the next targeting decision. Each BDA record should prompt three questions: Does this target require re-attack? Does this BDA result change the commander's priorities on the HPTL? Does this BDA indicate a collection shortfall requiring a new ISR tasking?

### What MSS Cannot Do

| Limitation | Detail |
|------------|--------|
| Compute a ballistic fire command | The targeting solution — elevation, deflection, charge, fuze — comes from AFATDS. MSS records the fire mission; it does not compute it. |
| Make a fires decision | MSS provides data to inform decisions. The decision to clear a fire mission, approve a counterfire nomination, or authorize engagement of an air track is a human decision. |
| Guarantee data accuracy | MSS displays what has been entered. Incorrect data entered accurately is still incorrect data displayed accurately. |

### The Sensor-to-Shooter Data Chain

The sensor-to-shooter chain is the data path from detection of a target to delivery of fires on that target. Every link in that chain has latency. A counterfire target detected by Q-36 radar may have repositioned within 10 minutes of firing. A time-sensitive target may have a 15-minute window before it disperses.

MSS reduces sensor-to-shooter latency when data feeds are active and fires personnel are disciplined about immediate data entry. It cannot eliminate latency. Target data in MSS carries a "last detection DTG" field precisely to make data age visible. Fires planners must check that field before planning strikes. A target detected six hours ago in a high-tempo environment may have moved, been engaged by another unit, or ceased activity.

---

## SECTION 3 — FIRE SUPPORT COORDINATION AS A DATA PROBLEM

### Why FSCM Data Must Be Authoritative and Current

Fire support coordination measures exist to prevent two things: friendly fire on friendly forces, and fires on protected sites. Every FSCM is either a permission structure or a restriction structure. When FSCM data in MSS is wrong, the fires cell is operating with false permissions or false restrictions — either of which can produce catastrophic outcomes.

An authoritative FSCM record meets all four conditions:
1. Entered into MSS by an authorized user
2. Reflects the FSCM as approved by the establishing headquarters
3. Accompanied by the correct effective period and geographic boundary
4. Verified for accuracy before publication to subordinate fires workspaces

Many fires staff errors in FSCM management come from shortcuts in the authorization chain. The FSCOORD's RDO updates an FSCM in MSS without confirming the change with the establishing headquarters. A subordinate FSO moves an NFA boundary in MSS to reflect what they believe the correct boundary should be, without authority. Each shortcut creates a version of the FSCM in MSS that may not match the authoritative version.

The standard that FSCM overlays in MSS are updated within one hour of order publication reflects the time window within which fires planning and execution may be conducted against the previous FSCM picture. An hour of operations with a stale FSCM picture is an hour of operations with an unmanaged fratricide risk.

### The Concept of FSCM Drift

FSCM drift is the gradual divergence between the FSCM overlay in MSS and the actual, current coordination measures in effect across the battlespace. It is one of the most insidious fires data problems because it is cumulative and often invisible until it produces a near-miss or incident.

FSCM drift has three drivers:

| Driver | Description |
|--------|-------------|
| **Deferred entry** | A FRAGO changes a coordination measure; the fires cell acknowledges it but defers MSS entry until "there's time." Time does not come during the battle rhythm. |
| **Expiration accumulation** | FSCMs entered with expiration DTGs expire quietly. If the fires cell does not actively monitor FSCM expiration and renew or archive expired measures, expired FSCMs accumulate on the overlay. |
| **Echelon problem** | At BCT, the FSCM overlay receives measures from division as well as BCT's own organic measures. If the division fires cell is not publishing updates promptly, the BCT fires cell is working with a partially stale overlay even if they have maintained their own measures perfectly. |

Fires leaders combat FSCM drift through three practices: real-time update discipline, expiration monitoring, and cross-echelon verification.

### Shared Workspace Discipline

The MSS fires workspace is shared across all fires personnel — FSCOORD, targeting officer, FSOs, FDC, AMD operations center. This sharing is the source of MSS's greatest operational value and its greatest vulnerability: any user with write access can degrade the shared picture by entering incorrect data.

Shared workspace discipline begins with access control. Write access to the HPTL is limited to the FSCOORD and targeting officer. Write access to FSCM overlays is limited to fires cell staff with establishing headquarters coordination responsibility. Write access to BDA records belongs to FSOs and the targeting officer. These controls are not bureaucratic obstacles — they are the first line of defense against accidental or unauthorized data corruption in a shared fires workspace.

### The Relationship Between the Fire Support Plan and the MSS FSCM Overlay

The fire support plan is the foundational document. The MSS FSCM overlay is the operational data expression of the fire support plan's coordination measures. These two must be synchronized, but they are not the same thing.

The fire support plan exists in the OPORD annex with a specific format, authority chain, and legal standing. The MSS FSCM overlay translates coordination measures from that annex into a live geospatial display. But the MSS overlay is derivative of the fire support plan, not primary to it. When the two conflict, the fires annex is authoritative and the MSS overlay requires correction.

Fires staffs that use MSS as the primary fire support planning tool and treat the written fires annex as a summary of MSS data have reversed this relationship in a way that creates risk. Orders have legal standing; MSS data does not.

---

## SECTION 4 — AMD OPERATIONS MENTAL MODEL

### The Layered Defense in Data Terms

AMD doctrine organizes air and missile defense in layers: HIMAD (Patriot) providing long-range and high-altitude protection, SHORAD providing medium and short-range protection, and MANPADS/guns providing point defense. Coordinating these layers to provide continuous, gap-free defense of critical assets is the AMD task force commander's core challenge.

In MSS, each AMD system is a data object with location, coverage parameters, readiness status, missile inventory, and engagement authority. The AMD TF commander who views the MSS AMD display sees — for the first time with a single display — whether Patriot sector of fire overlaps cleanly with M-SHORAD coverage, whether the combined coverage envelope covers all DAL assets, and where the defense design has gaps.

The critical insight is that the layered defense is not static once established. Systems move. Systems go non-mission capable. Threats change approach vectors. The defended assets list changes as the operational situation evolves. An AMD TF commander who reviews the MSS AMD display at the morning update and then does not review it again until the evening update is accepting six to twelve hours of unmonitored defense design drift.

The data picture of the layered defense also makes visible what the defense design cannot cover. No AMD force has enough resources to defend all critical assets against all threat axes simultaneously. MSS makes coverage gaps visible in the coverage display, forcing explicit command decisions about risk rather than allowing coverage gaps to remain invisible assumptions.

### Engagement Authority as a Command Function

Nothing in AMD operations is more important to get right than engagement authority. Engagement authority determines which personnel can authorize weapon release against which track categories in which circumstances. The consequences of getting this wrong flow in both directions: an unauthorized engagement may produce fratricide of a friendly aircraft; a failure to engage when authority was available may result in a missile striking a defended asset.

MSS records engagement authority status across all AMD systems. But the record in MSS is not the engagement authority itself — it is a data representation of command decisions that have been made and communicated through the command authority chain.

This distinction matters for two reasons:
1. If the engagement authority displayed in MSS does not match the commander's actual current directive — because the record was not updated after a verbal directive, or a FRAGO changed engagement authority before MSS was updated — the displayed authority is misleading. AMD operators who reference MSS to confirm engagement authority without cross-checking against the commander's directive are relying on potentially stale data in a lethal decision context.
2. Engagement authority in MSS is a record of decisions, not an automated approval system. There is no scenario in which a displayed "Weapons Tight" status in MSS authorizes an engagement that the commander has not directed.

### CAL/DAL Management as a Continuous Process

The common approach to CAL/DAL management treats it as a planning product: produced during mission analysis, approved by the commander, and then referenced throughout the operation. This is correct for initial production. It is insufficient for CAL/DAL management over the duration of an operation.

Two dynamics require continuous management:

| Dynamic | Required Action |
|---------|----------------|
| Critical asset movement | Every movement of a CAL-listed asset triggers an immediate CAL/DAL update. Unit SOP must include notification to the AMD operations center when a defended asset displaces. |
| AMD system status changes | Every AMD system status change triggers a coverage reassessment. A Patriot battery that goes NMC cannot defend its sector — if the DAL in MSS is not updated, the display shows continuous coverage that no longer exists. |

### HIMAD/SHORAD Integration: Different Data Domains, Shared Picture

Patriot (HIMAD) systems operate under IBCS (or legacy AMDWS). SHORAD and M-SHORAD systems operate under FAAD C2. These systems do not natively speak the same data language, and their pictures are not automatically integrated.

MSS provides the integration layer where both HIMAD and SHORAD data appear on a single AMD operational picture. The AMD TF commander does not need to switch between IBCS and FAAD C2 displays — they see both in MSS simultaneously.

The integration comes with a critical limitation: MSS receives data from IBCS and FAAD C2 but does not control them. A degradation in the IBCS or FAAD C2 data feeds to MSS will degrade the MSS AMD picture even when both AMD systems are fully operational. AMD operations continue through IBCS and FAAD C2; MSS simply has reduced visibility until the feed is restored.

---

## SECTION 5 — FIRES-INTEL INTEGRATION

### The Shared Data Problem

Fires and intelligence share a fundamental data problem: both depend on knowing where the enemy is, what they are doing, and what capabilities they can bring to bear. In legacy operations, fires and intelligence operated largely in parallel, sharing products through formal reporting channels but often working from different operational pictures.

MSS changes this by providing a shared data environment where fires and intelligence data coexist. The target record in MSS that carries a "Suspected" confidence level is reflecting intelligence collection status. The BDA record in MSS that the targeting officer enters after a strike is an intelligence product. The HPTL that the FSCOORD maintains is derived from intelligence assessments of OPFOR capability priorities.

The shared environment creates both an integration opportunity and an integration risk. When fires and intelligence personnel have different update disciplines, the shared picture is internally inconsistent. The fires cell sees target data that intelligence has not updated with new collection. The intelligence cell sees BDA data that the fires cell entered without adequate collection foundation.

### Collection Requirements and the PIR-to-HPT Chain

The intelligence-fires nexus in MSS is most visible in the relationship between priority intelligence requirements (PIR) and high-payoff targets. In MSS, the targeting module links HPT categories to collection requirements. The collection management module links collection requirements to ISR assets. When an ISR asset reports a positive find on an HPT category, that find updates the target record, the HPTL confidence level, and the collection status simultaneously.

The chain breaks when:
- Collection requirements are not entered in MSS
- ISR assets are tasked to collect against HPTs but the collection plan is not documented in MSS
- Collection results are reported through channels outside MSS and not entered into the target record

Each break is a point where fires-intel integration degrades from a functioning circuit into two separate processes that synchronize only when personnel communicate explicitly.

### BDA as an Intelligence Product

BDA occupies an interesting position in the fires-intelligence relationship. Fires personnel produce and enter BDA in MSS. But BDA is fundamentally an intelligence product — it answers the question "what effects did fires produce on OPFOR capability?"

The tension between fires ownership of BDA and intelligence ownership of BDA assessment is a recurring challenge in targeting operations. In MSS, both can coexist: the fires team enters BDA collection data (what observers reported, what imagery shows), and the intelligence team annotates with analytical confidence and system disruption assessment.

Fires teams that enter BDA without seeking intelligence input on functional and system disruption levels are producing incomplete BDA. Intelligence teams that assess BDA without updating the MSS record are producing assessment products that do not feed the targeting cycle.

### The Targeting Working Group as a Data Synchronization Event

The TWG is described as a decision-making forum. It is also the moment when everyone in the targeting process aligns on the same data picture. Before the TWG, fires, intelligence, and operations may have been working from slightly different versions of the HPTL, the target list, and the BDA record.

When the TWG uses MSS as its primary display — when the HPTL, BDA log, and target status are projected from MSS rather than from a separate PowerPoint — the TWG output naturally flows into MSS. Target priority changes are entered in real time. New collection requirements are entered immediately. BDA analytical updates from the S2 are entered on the spot.

Units that run the TWG from PowerPoint slides and then have a separate step to update MSS afterward introduce delay and error. Subordinate FSOs planning fires support for the next phase may be planning against a HPTL that has not yet been updated in MSS from the TWG output.

---

## SECTION 6 — THE ROLE OF ASSESSMENT IN FIRES

### BDA and Re-Attack as a Fires Learning Loop

Fires without assessment is shooting in the dark. Assessment closes the targeting cycle by answering whether fires achieved the intended effects and whether the target requires re-engagement. BDA in MSS is the mechanism for capturing that answer.

The learning loop requires that BDA records in MSS are treated as more than completion entries. Each BDA record should prompt three questions:
1. Was the effect achieved?
2. If not, why not (wrong munition, incorrect target, missed location, OPFOR countermeasures)?
3. What does this tell us about the AGM guidance for this target category?

When fires teams ask these questions systematically, the AGM evolves through the operation to reflect what actually works against the threat the formation is encountering.

### How MSS Enables Fires Assessment

MSS enables fires assessment at three levels:

| Level | Description |
|-------|-------------|
| Individual mission BDA | BDA records carry full assessment data required by FM 3-60: physical destruction, functional damage, and system disruption. When completed with collection data and analytical confidence levels, they enable a re-attack recommendation within minutes of BDA collection. |
| HPTL engagement tracking | MSS tracks engagement status of all target categories: confirmed targets engaged, BDA results recorded, targets remaining unengaged, re-attack nominations outstanding. This is the fires assessment product the FSCOORD needs to brief the commander. |
| Theater-level fires effectiveness | MSS aggregates BDA data across multiple targeting cycles and formations to assess the cumulative effects of fires on OPFOR capabilities — connecting tactical BDA to the operational question of whether fires are degrading OPFOR combat power at the required rate. |

### The Command Climate Dimension of BDA

There is a dimension of BDA that no technical platform can address: the human incentive to report BDA optimistically. MSS makes BDA records visible and permanent, which creates accountability — but accountability only operates if commanders demand it.

The FSCOORD who creates a command climate where honest BDA is expected and rewarded will have fires assessment data in MSS that actually supports sound re-attack decisions. The FSCOORD who allows optimistic BDA to persist because it is administratively convenient will have an HPTL engagement status that looks positive while the operational effects are insufficient.

BDA quality in MSS is ultimately a command climate issue, not a technical one. The technical controls — required fields, confidence level entries, collection source documentation — provide structure. The command climate determines whether that structure produces honest data or compliant but inaccurate records.

### MOE vs. MOP for Fires

Fires assessment uses both measures of performance (MOP) and measures of effectiveness (MOE), and the distinction matters for how fires leaders interpret MSS assessment data.

| Measure | What It Measures | Implication |
|---------|-----------------|-------------|
| **MOP** | Whether fires did what fires were supposed to do. Response time, mission completion rate, BDA timeliness. | Tells the fires cell whether the fires process is running at the right tempo and discipline. A poor MOP indicates a fires process problem. |
| **MOE** | Whether fires achieved the effects the commander needed. Physical destruction achieved, functional capability degraded, system-level OPFOR capability affected. | Tells the commander whether fires are contributing to operational success. A strong MOP combined with a weak MOE indicates a targeting problem, not a fires process problem. |

Fires leaders who conflate MOPs with MOEs will brief good performance while missing operational failure. The commander's fires briefing should present both dimensions explicitly. Both analyses require different MSS data views, but both are available from MSS when data is maintained to standard.

### The Assessment Clock

Fires assessment is perishable in a way that fires planning and execution are not. A BDA record entered 48 hours after fires execution reflects a 48-hour-old picture of the target's status. In a dynamic operational environment, that target may have reconstituted, repositioned, been engaged by another unit, or changed its operational significance entirely.

The fires cell that treats BDA entry as a completion step — something done when time permits — is producing a historical record rather than an operational product. Assessment tempo is a command priority.

When the FSCOORD establishes and enforces the BDA entry standard — entry within two hours of fires execution or within one hour of BDA collection, whichever occurs first — the assessment product in MSS is operationally relevant. When the FSCOORD allows BDA entry to accumulate and be entered in batches at the end of the day, the assessment product is a log.

---

## SECTION 7 — FIRES FAILURE MODES IN MSS

### The Fires Commander's MSS Posture

The difference between fires units that use MSS effectively and those that do not is rarely technical. The difference is posture — whether the fires commander treats MSS as the operational fires data environment or as an administrative reporting tool.

| Posture | Behaviors |
|---------|-----------|
| **Operational** | Attends TWGs that use MSS as the primary display; asks fires cell members to pull specific data from MSS in real time; spot-checks FSCM currency before clearing fires near coordination boundaries; reviews BDA records linked to mission records |
| **Administrative** | Accepts PowerPoint slides summarizing MSS data without checking the source; allows fires cell to update MSS "when there's time"; treats MSS training as a check-the-box requirement; accepts BDA report formats disconnected from MSS records |

The operational posture signals to the fires team that MSS accuracy has operational consequences. The administrative posture signals that MSS is for reporting to higher, not for decision-making. The eight failure modes documented below are downstream effects of a fires team that has received the second signal rather than the first.

### Eight Failure Modes — Introduction

Fires units fail in MSS in predictable ways. The following eight failure modes have been identified across USAREUR-AF exercises, after action reviews, and operational observations.

The pattern across these failure modes is consistent: they are not primarily technical failures. They are human and organizational failures that manifest in the data. Stale target data does not create itself — someone stopped updating it. FSCM drift does not occur spontaneously — someone deferred an update. BDA inflation does not emerge from the platform — someone entered optimistic data. The corrections are therefore human and organizational, not primarily technical. The primary variable is command climate.

---

### Failure Mode 1 — Stale Target Data

**Description.** Target records in the HPTL and target library are not updated as collection assets report new information. Target locations reflect initial detection data. Confidence levels remain at "Suspected" or "Templated" for targets that collection assets have continued to observe.

**Root cause.** Intelligence and fires personnel do not maintain the habit of updating target records in real time. The target library is treated as a planning product rather than a live data object. The S2 produces intelligence products in separate formats without synchronizing them to MSS target records.

**Senior leader indicator.** Target records show "last detection DTG" values more than 24 hours old for active-collection targets. Multiple targets show "Templated" confidence level despite active ISR tasking. BDA records exist for targets that still show "Active" status in the target library.

**Correction.** Establish a target record update standard: every intelligence reporting cycle produces target record updates in MSS, not just intelligence summary products. Assign joint fires-intel ownership of the target library. Make the "last detection DTG" field a TWG review item at every targeting meeting.

---

### Failure Mode 2 — FSCM Drift

**Description.** The FSCM overlay in MSS does not reflect the current coordination measures in effect. Expired FSCMs remain on the overlay. New FSCMs from orders and FRAGOs have not been entered.

**Root cause.** FSCM updates are deferred rather than made immediately on order publication. The fires cell does not have an active FSCM expiration monitoring process. Echelon-level FSCM ownership is unclear.

**Senior leader indicator.** FSCM publication DTGs more than 12 hours old in an active environment. Expired FSCMs visible on the overlay with no archive or renewal action. FSOs reporting that the MSS FSCM overlay "doesn't match what we were briefed" in the fires annex.

**Correction.** Make FSCM overlay currency a daily fires cell inspection item. Assign a specific individual as FSCM currency monitor. Establish a rule: FSCM changes are entered in MSS before the battle update briefing that follows the order that changed them.

---

### Failure Mode 3 — Sensor-to-Shooter Disconnect

**Description.** MSS target records do not receive detection data from active sensors in time to drive counterfire or time-sensitive targeting. The fires cell is making targeting decisions based on MSS data that is significantly behind the sensor picture.

**Root cause.** The AFATDS-MSS interface or the radar-MSS data feed is degraded and has not been restored. Manual entry procedures have not been activated. Intelligence reports arrive in MSS later than in the S2's own intelligence tools because the S2 updates separate intelligence systems first and MSS second.

**Senior leader indicator.** Fire missions being executed against targets whose MSS location data has not been updated since the previous day. Counterfire nominations generated hours after POO detections because the radar data feed was not checked.

**Correction.** Establish sensor interface status as a fires cell monitoring responsibility. When any sensor-MSS interface degrades, activate manual entry immediately rather than waiting for the interface to restore. Make intelligence-MSS synchronization a TWG standard: every TWG begins with a review of the gap between intelligence product reporting and MSS target record currency.

---

### Failure Mode 4 — AMD ROE Confusion

**Description.** The engagement authority status recorded in MSS does not match the commander's actual current directive. Different AMD elements are operating under different understandings of engagement authority.

**Root cause.** Verbal engagement authority directives are not immediately entered into MSS. FRAGO-driven changes to engagement authority reach the AMD operations center through voice channels before the MSS record is updated.

**Senior leader indicator.** AMD personnel who cannot immediately confirm whether the MSS engagement authority record reflects the most recent commander's directive. Engagement authority records without a corresponding order or directive reference. AMD units reporting engagement authority from verbal direction that does not match MSS records.

**Correction.** Establish a firm rule: every engagement authority change is entered in MSS within 15 minutes, referencing the order, FRAGO, or directive that established it. The 14A confirms the MSS record with the AMD TF commander at every battle update briefing.

---

### Failure Mode 5 — BDA Inflation

**Description.** BDA records in MSS reflect more favorable effects than collection data actually supports. Physical destruction percentages are higher than imagery or observer reports justify. System disruption assessments are reported as C3 or C4 when the basis for that assessment is speculative.

**Root cause.** Fires teams enter BDA based on assumptions rather than collection data. The command climate implicitly rewards positive BDA. The fires cell does not cross-check BDA entries against the collection source documents. Intelligence assessment of BDA is not sought or incorporated.

**Senior leader indicator.** Repeat re-attack cycles on targets that MSS records as "assessed — effects achieved." High percentage of BDA records where the collection source field is "Observer" without supporting documentation. Intelligence community assessments of OPFOR capability that conflict with the fires cell BDA picture.

**Correction.** Require collection source documentation for all BDA entries above PMCII level. Establish joint fires-intelligence review of BDA records at the TWG. Create a command climate where honest BDA — including NMC upgraded to PMCI when revisit collection reveals the target has reconstituted — is expected and valued.

---

### Failure Mode 6 — AFATDS/MSS Data Duplication and Inconsistency

**Description.** Fire mission records in MSS are inconsistent with AFATDS fire mission records. Rounds expended in MSS do not match rounds expended in AFATDS. Class V consumption data in MSS and Class V records in the FDC are misaligned.

**Root cause.** The AFATDS-MSS interface is partially degraded, producing incomplete automatic data transfer. Manual update procedures are applied inconsistently. FDC personnel update AFATDS (their primary system) without corresponding MSS updates.

**Senior leader indicator.** Fire mission count discrepancies between the FSCOORD's MSS briefing and the FDC's daily mission count. Class V data in MSS that does not match the battery commander's actual on-hand report. BDA records in MSS with no corresponding fire mission record, or fire mission records with no associated BDA.

**Correction.** Establish AFATDS-MSS reconciliation as a daily FDC responsibility. The 13J or 13P reconciles the AFATDS fire mission log against the MSS fire mission log each morning and at every duty officer change. The FSCOORD periodically reviews the reconciliation report, not just the fires summary.

---

### Failure Mode 7 — Targeting Without Intelligence Integration

**Description.** The fires cell develops and prosecutes targeting against the HPTL without active synchronization with the intelligence cycle. Target records receive the initial intelligence-derived location at HPTL development and are not updated by subsequent collection. BDA analytical assessment from the S2 does not appear in MSS BDA records.

**Root cause.** The fires cell and S2 section operate on different update cycles and do not share data in MSS in real time. The S2 maintains an intelligence picture in separate tools (DCGS-A, CIDNE, unit intelligence management systems) that is more current than the fires cell's MSS picture.

**Senior leader indicator.** Target records that have never been updated by the S2 section — all data was entered by fires personnel at HPTL creation. BDA records with no functional or system disruption assessment. HPTL categories with stale "last detection DTG" values despite active collection against those target categories.

**Correction.** Make MSS target record co-ownership a fires-intelligence operating agreement. The S2 section designates a targeting warrant or NCO whose MSS responsibilities include updating target records and BDA assessments. The TWG includes an MSS data review segment where fires and intelligence personnel reconcile the MSS picture against the intelligence community's current assessment.

---

### Failure Mode 8 — Fires-Maneuver FSCM Deconfliction Failure

**Description.** FSCM boundaries in MSS do not reflect the current position of maneuver forces, creating conditions where fires could be cleared short of friendly force positions or where fires restrictions protect areas that maneuver forces have vacated.

**Root cause.** Maneuver and fires staff do not maintain a synchronized common operating picture. The fires cell updates FSCMs based on orders but does not continuously track the relationship between maneuver force positions and FSCM boundaries.

**Senior leader indicator.** FSCL or RFL boundaries in MSS that have not been updated since the previous operational phase change, while maneuver forces have moved significantly. FSOs noting that the CFL has not been updated to reflect the unit's advance.

**Correction.** Establish maneuver position-to-FSCM review as a standard item at every fires cell update: what has maneuver done, and does it require an FSCM update? The S3 and FSCOORD share responsibility for triggering FSCM updates when maneuver exceeds established position triggers.

---

### Summary Table — Eight Fires Failure Modes

| Failure Mode | Root Cause | Senior Leader Indicator | Primary Correction |
|-------------|-----------|------------------------|-------------------|
| 1. Stale target data | Target library treated as planning product, not live data | Last detection DTG values stale; confidence levels unchanged despite active collection | Joint fires-intel ownership of target records; update at every intelligence cycle |
| 2. FSCM drift | Deferred FSCM updates; no expiration monitoring | Old publication DTGs; expired FSCMs on display; FSO reports mismatch | FSCM currency monitor; immediate update on order publication |
| 3. Sensor-to-shooter disconnect | Degraded data feeds without manual backup | Targets planned against location data hours behind sensor picture | Interface monitoring; immediate manual entry when feeds degrade |
| 4. AMD ROE confusion | Verbal directives not entered in MSS; personnel reference display without cross-checking | Engagement authority records without order reference; unit reports not matching MSS | 15-minute entry standard; commander confirmation at every battle update briefing |
| 5. BDA inflation | Command climate; no cross-check against collection source | Re-attacks on "assessed" targets; intelligence picture conflicts with fires BDA | Collection source documentation required; joint fires-intel BDA review at TWG |
| 6. AFATDS/MSS inconsistency | Partial interface degradation without manual backup; inconsistent manual procedures | Mission count discrepancies; Class V mismatch | Daily reconciliation by 13J/13P; FSCOORD periodic review |
| 7. Targeting without intel integration | Separate update cycles; intel in non-MSS tools | Target records never updated by S2; no functional BDA assessments | Intel designates MSS co-owner; shared operating agreement |
| 8. Fires-maneuver FSCM deconfliction | Fires and maneuver not sharing position updates; no trigger for FSCM review | FSCL/RFL not updated through operational phase changes | Position-to-FSCM review at every fires update; shared S3-FSCOORD trigger |

---

## COMMAND GUIDANCE FOR FIRES LEADERS

### For the FSCOORD and Fires Brigade Commander

This guide has two practical implications beyond the conceptual content.

First, MSS is only as good as the command climate that drives its use. A fires cell that updates MSS accurately under normal conditions but cuts corners under operational pressure will degrade the fires picture precisely when accurate data matters most. The FSCOORD who enforces MSS data standards during garrison and exercise training — who insists on correct FSCM entries, proper BDA documentation, and accurate Class V data — is building the habit discipline that will hold under operational stress.

Second, the eight failure modes in Section 7 are not theoretical. They have appeared in USAREUR-AF exercises and in after action reviews of operational engagements. Each failure mode has a specific command action that prevents it. The FSCOORD who reviews Section 7 and identifies which failure modes their fires cell is most susceptible to — based on personnel, training posture, and system configuration — can focus corrective actions before the failure occurs.

For fires brigade and DIVARTY commanders: your most consequential MSS decisions are personnel decisions. The targeting officer who maintains the HPTL with discipline, the fires cell NCO who enforces data currency standards, and the 14A who keeps AMD data honest are the human infrastructure of the fires data picture. Invest in their MSS proficiency the same way you invest in their gunnery certification and fire direction proficiency.

### For the AMD TF Commander

Two points warrant emphasis.

The engagement authority section is not academic. AMD engagement decisions occur under the most time-compressed conditions in military operations. Ambiguity in AMD engagement authority — whether it exists in the commander's mind, in the written ROE, or in the MSS record — is a risk that resolves badly in either direction.

CAL/DAL management as a continuous process — not a planning product — is the AMD TF commander's most underappreciated MSS responsibility. Review the CAL/DAL in MSS at every battle update briefing. Not once per operation. Every battle update. The defense of critical assets is only as good as the accuracy of the data that describes where those assets are and which AMD systems are covering them.

---

## RELATED TRACKS AND PUBLICATIONS

### WFF Peer Tracks

All six WFF tracks are at the same tier. All six WFF tracks require TM-10, TM-20, and TM-30 as prerequisites. Fires practitioners are encouraged to develop working awareness of TM-40A (Intelligence) and TM-40E (Protection) — the two WFF tracks with the most intensive fires data coordination requirements.

| Track | Title | Prereq | Relationship to Fires WFF |
|-------|-------|--------|--------------------------|
| TM-40A | Intelligence WFF | TM-10 + TM-20 + TM-30 | Targeting data, BDA, ISR collection — the fires-intel integration that makes targeting lethal and discriminate |
| TM-40B | Fires WFF | TM-10 + TM-20 + TM-30 | This track |
| TM-40C | Movement and Maneuver WFF | TM-10 + TM-20 + TM-30 | FSCM coordination, airspace deconfliction, maneuver-fires synchronization |
| TM-40D | Sustainment WFF | TM-10 + TM-20 + TM-30 | CSR, ammunition readiness |
| TM-40E | Protection WFF | TM-10 + TM-20 + TM-30 | AMD coordination — fires and protection share AMD data domain |
| TM-40F | Mission Command WFF | TM-10 + TM-20 + TM-30 | Fires products integrate into the commander's CCIR dashboard |

### Specialist Tracks (Prerequisite: TM-30)

For personnel pursuing technical depth, specialist tracks (TM-40G–L, prereq TM-30) are available. Not required for fires WFF employment.

| Track | Title |
|-------|-------|
| TM-40G | ORSA (→ TM-50G) |
| TM-40H | AI Engineer (→ TM-50H) |
| TM-40I | ML Engineer (→ TM-50I) |
| TM-40J | Program Manager (→ TM-50J) |
| TM-40K | Knowledge Manager (→ TM-50K) |
| TM-40L | Software Engineer (→ TM-50L) |

---

*UNCLASSIFIED // FOR OFFICIAL USE ONLY*

*CONCEPTS GUIDE — TM-40B COMPANION, Version 1.0, March 2026*

*HEADQUARTERS, UNITED STATES ARMY EUROPE AND AFRICA, Wiesbaden, Germany*

*Read this guide before beginning TM-40B. The procedural knowledge in TM-40B is more durable when it rests on the conceptual foundation this guide provides.*

*Questions and feedback on this guide should be directed to the USAREUR-AF C2DAO fires functional area representative. Doctrinal discrepancies between this guide and current Army doctrine will be resolved in favor of doctrine; report discrepancies for correction in the next revision.*
