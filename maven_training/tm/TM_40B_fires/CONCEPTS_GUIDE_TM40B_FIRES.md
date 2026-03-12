# CONCEPTS GUIDE — TM-40B COMPANION
## FIRES WARFIGHTING FUNCTION
## MAVEN SMART SYSTEM (MSS)

**HEADQUARTERS, UNITED STATES ARMY EUROPE AND AFRICA**
Wiesbaden, Germany

2026

**Version 1.0 | March 2026**

**PURPOSE:** This guide is the conceptual companion to TM-40B. It is not a how-to manual. It explains the WHY behind fires operations in MSS — the doctrinal logic that makes certain data requirements non-negotiable, the mental models that separate effective fires practitioners from those who treat MSS as an expensive slide deck, and the failure patterns that fires units must actively avoid.

**PRIMARY AUDIENCE:** FSCOORD, DIVARTY CDR, AMD TF CDR, fires brigade commanders, division and corps fires cell chiefs, senior FA and ADA warrants. This guide is also appropriate for BCT S3s and XOs who receive and brief fires products.

**PREREQUISITE:** Read before beginning TM-40B. The procedural tasks in TM-40B make more sense — and are more likely to be executed correctly under pressure — when this conceptual foundation is in place.

**HOW TO USE THIS GUIDE:** Read it linearly. Each section builds on the previous. Sections 1 and 2 establish the foundational data obligation for fires. Sections 3 and 4 apply that foundation to the two most safety-sensitive fires data domains: FSCM coordination and AMD engagement authority. Section 5 addresses the organizational challenge of fires-intel integration. Section 6 addresses assessment as a fires learning loop. Section 7 identifies the failure modes that occur when the principles in Sections 1–6 are not applied — and provides the diagnostic tools to identify and correct them. Senior leaders may read Section 7 first if they want to start with failure mode recognition. Return to Sections 1–6 for the conceptual grounding that makes the corrections durable.

**DOCTRINAL BASIS:** ADP 3-19, FM 3-09, FM 3-60, ATP 3-01.8, ATP 3-52.2, ATP 3-09.42, ATP 3-09.50. Where this guide interprets doctrinal principles in the context of MSS, the interpretation is operationally derived. Doctrinal authority resides in the cited source documents. Changes to referenced doctrine after the publication date of this guide take precedence over any conflicting guidance in this text.

**COMPANION PUBLICATION:** TM-40B, Fires Warfighting Function, Intermediate Operator's Manual.

**DISTRIBUTION RESTRICTION:** UNCLASSIFIED // FOR OFFICIAL USE ONLY.

---

## TABLE OF CONTENTS

- Section 1 — The Fires WFF and Data: How ADP 3-19 Translates to MSS Data Requirements
- Section 2 — Targeting as a Data Process: D3A as Information Flow
- Section 3 — Fire Support Coordination as a Data Problem: Why FSCM, ROE, and ACA Data Must Be Authoritative
- Section 4 — AMD Operations Mental Model: The Layered Defense as a Data Picture
- Section 5 — Fires-Intel Integration: The Intelligence-Fires Nexus and Shared Data in MSS
- Section 6 — The Role of Assessment in Fires: BDA and Re-Attack as a Feedback Loop
- Section 7 — Fires Failure Modes in MSS: Eight Ways Fires Units Misuse the Platform

---

## SECTION 1 — THE FIRES WFF AND DATA: HOW ADP 3-19 TRANSLATES TO MSS DATA REQUIREMENTS

### The Fires Principles Are Data Requirements in Disguise

ADP 3-19 establishes five fires principles: massed effects, range, accuracy, responsiveness, and sustainability. Every fires commander and fires officer can recite them. Fewer have thought through what each principle demands from a data management perspective. When you read ADP 3-19's fires principles with MSS in mind, they become a prescription for the data standards your fires cell must maintain.

**Massed effects** means coordinating fires from multiple systems to achieve effects at a specific place and time greater than what any single system can achieve alone. Massing effects is impossible without current target data. You cannot mass effects against a target whose location is stale, whose confidence level is "templated," or whose attack guidance is ambiguous. The HPTL in MSS is the mechanism by which the FSCOORD directs the fires team's attention toward the targets where massing effects will have the greatest operational impact. A well-maintained HPTL is not administrative overhead — it is the fires team's shared picture of where mass matters.

**Range** means positioning fires systems to place effects on targets when required. In MSS, range is visualized through asset position overlays and range ring displays. Fires can only be massed at maximum range when the fires cell knows where each system is positioned and what ammunition type it carries. Asset status data in MSS is what makes range a planning variable rather than an unknown. Units whose asset status data is outdated in MSS are planning fires with blindfolded range analysis.

**Accuracy** in fires requires correct target location data, current MET data, and valid ballistic computation. MSS contributes to fires accuracy by maintaining target location data with confidence levels, managing MET message currency, and ensuring that the target coordinates passed to firing units are the most recently confirmed position — not an outdated templated location. Target location error is the primary driver of fires inaccuracy. MSS does not eliminate TLE, but it makes TLE visible by requiring location source and confidence level fields on every target record.

**Responsiveness** means delivering fires at the time and place the supported commander needs them. Responsiveness has two data dependencies: knowing what fires assets are available and knowing the approval status of the request. The FSEM in MSS tracks both — which assets are assigned to which missions, and at what status. A fires cell that updates the FSEM in real time can tell the FSCOORD within seconds whether a new fires request can be accommodated. A fires cell that updates the FSEM occasionally leaves the FSCOORD operating on guesses about available capacity.

**Sustainability** means maintaining fires capacity over time through ammunition management and logistics synchronization. Class V data in MSS is the data expression of sustainability. The fires cell that tracks ammunition consumption rigorously in MSS can forecast when units will reach critical thresholds and request resupply before capability degrades. The fires cell that ignores Class V tracking until batteries report low will find its ammunition data perpetually reactive — confirming shortfalls after they occur rather than preventing them.

Each fires principle, properly understood, creates a specific data quality obligation. Officers who approach MSS as a data entry burden have inverted the relationship. The data is the fires capability. Keep the data current, and the fires principles are achievable. Let the data degrade, and the principles become aspirational slogans.

### Fires Data as Safety Data

In most military applications, poor data quality is an operational inconvenience. In fires, poor data quality is a safety hazard. This is the dimension of fires data management that no FSCOORD should allow to become routine or complacent.

The most consequential fires safety data in MSS is FSCM data. An FSCM is not merely an administrative boundary — it is the legal and safety framework within which lethal fires are authorized. When an NFA is entered with the wrong boundary in MSS, and a subordinate FSO clears fires based on that display, the result can be fires on a protected site, a civilian area, or a medical facility. When an RFL expires and is not updated in MSS, a unit clearing fires based on an expired restrictive measure may inadvertently fire across a boundary into adjacent friendly forces.

The consequences of stale FSCM data are not hypothetical. Fratricide events in historical operations have traced to FSCM confusion — cases where coordination measures were updated in one system but not propagated to others, leaving FSOs working from different operational pictures. MSS reduces this risk by centralizing FSCM publication in a single platform visible to all fires users simultaneously. But that reduction in risk only materializes when FSCM data is entered correctly, updated promptly, and verified before clearance of fires near coordination boundaries.

Target coordinate data carries a similar safety obligation. A target that has moved since it was last reported carries a stale coordinate. If fires are delivered to the last reported position rather than the current position, effects may be placed in the wrong location — potentially on friendly forces, civilians, or infrastructure. The confidence level field in the MSS target record exists precisely to flag this risk. "Templated" means expected, not confirmed. Fires against a templated target in a complex operational environment require additional verification that ADP 3-19's precision fires principles demand.

ROE data in MSS is the third critical safety domain. The rules of engagement governing who can be targeted, what collateral damage thresholds apply, and under what circumstances fires are authorized are the legal constraints on lethal action. When ROE data in MSS is incorrect — when the AGM reflects outdated guidance, when collateral damage estimates are missing, when engagement authority is recorded inaccurately — the fires team is operating on flawed legal authority. This is not an MSS configuration problem; it is a command responsibility problem. The FSCOORD who allows ROE data in MSS to lag behind the actual, current ROE authorization is creating risk at the intersection of operational law and lethal decision-making.

### The Data Stewardship Obligation for Fires Officers

The fires data stewardship obligation begins with the FSCOORD and cascades to every fires officer and NCO in the formation. Data stewardship in the fires context means three things: maintaining data currency, ensuring data accuracy, and exercising command authority over data changes.

Data currency means that MSS fires data reflects the current operational situation. FSCMs are updated when they change. Targets are updated when collection reports new information. Asset status is updated on the reporting cycle. Ammunition data is updated daily and on event. Currency does not happen automatically — it requires fires personnel to enter information into MSS as operational events occur, rather than accumulating updates and entering them during quiet periods.

Data accuracy means that what is entered in MSS is correct. Coordinate errors, wrong FSCM types, incorrect confidence levels, and missing BDA data all degrade the fires operational picture. The FSCOORD cannot see what is wrong with data they have not entered. Training fires teams on MSS data entry standards — not just which buttons to push, but why each field matters — is the investment that produces accurate fires data.

Command authority over data changes means that not everyone has the authority to change every piece of fires data. HPTL changes require FSCOORD approval. FSCM changes require the establishing headquarters' authorization. Engagement authority changes require the AMD TF commander. These authority constraints exist in MSS through access controls, but they also exist as a command climate issue. Fires teams under pressure will cut corners on data accuracy if the command climate tolerates it. The FSCOORD who enforces data standards under pressure — who demands that FSCM changes go through proper authorization even when it takes time — is the FSCOORD who prevents the fratricide event that the shortcut would have enabled.

---

## SECTION 2 — TARGETING AS A DATA PROCESS: D3A AS INFORMATION FLOW

### Precision as a Data Property

There is a conceptual shift embedded in how MSS changes fires operations that fires commanders should make explicit to their teams: precision in fires is now partly a data property, not just a ballistic property.

Before integrated fires data platforms, fires precision was almost entirely a function of the ballistic solution — correct propellant charge, accurate fuze setting, wind corrections applied. The target location was assumed to be where the FO reported it, and the fires chain focused on the ballistic pathway from weapon to target.

MSS introduces a data precision dimension. A ballistically perfect fire mission delivered to an incorrect or outdated target location is not a precise engagement — it is a precise application of fires at the wrong place. Target location data quality, FSCM boundary accuracy, and sensor feed currency are now as much drivers of fires precision as ballistic computation. Fires commanders who understand this shift will enforce data standards with the same rigor they enforce gunnery standards.

---

### The D3A Circuit

FM 3-60 describes the D3A methodology as four steps: Decide, Detect, Deliver, Assess. This sequential description is useful for instruction. It is misleading if taken as a description of how targeting actually operates in combat.

Targeting is not a linear four-step process. It is a continuous information circuit. The Assess phase does not conclude the targeting cycle — it feeds the Decide phase for the next cycle. Detection data does not arrive in a clean stream after the Decide phase is complete — it arrives continuously, often disrupting and updating target data established at the last targeting working group. Delivery does not wait for a complete Assess phase — re-attack decisions must sometimes be made before BDA from the previous strike is available.

MSS, properly used, supports this circuit by making the data connections between phases visible and fast. When a 13F FSO submits BDA data in the MSS BDA module, that data is immediately visible to the targeting officer and the FSCOORD. When a Q-36 radar reports a new POO track, it appears in the fires operational picture linked to the counterfire target category on the HPTL. When a collection asset reports a positive find on a suspected target, the intelligence officer can update the target record confidence level from "Suspected" to "Confirmed" in real time, immediately making that target available for fires planning.

The unit that uses MSS to run a continuous targeting circuit — where detection data immediately updates target records, where BDA immediately feeds re-attack recommendations, where collection gaps immediately generate new PIR submissions — operates at a targeting tempo its adversary cannot match. The unit that uses MSS as a periodic update system, entering data at the end of shifts rather than in real time, runs the targeting circuit at a fraction of its potential speed.

### MSS and Each Phase of D3A

**Decide phase: the target library as a living document.** The targeting working group produces an HPTL and AGM. In most legacy operations, these products existed as slides — produced at the TWG, briefed to the commander, and then slowly becoming stale as the operation continued and the enemy adapted. MSS changes this by making the HPTL a live data object in the fires workspace, visible to every fires user in the formation simultaneously.

The Decide phase in MSS requires that the FSCOORD and targeting officer treat the HPTL as a continuously managed data product rather than a periodic publication. When the commander's guidance changes — when a new OPFOR system emerges as a priority or when operational phase changes shift which targets matter — the HPTL in MSS must reflect that change before subordinate fires elements begin planning. A subordinate FSO planning fires support for the next phase based on an outdated HPTL is misaligned with the commander's intent, and neither the FSO nor the FSCOORD will know it unless the HPTL in MSS reflects the current guidance.

**Detect phase: sensor integration and the confidence problem.** Target detection in MSS is only as good as the data that enters the platform. MSS does not conduct collection. It displays and organizes what collectors report. This means the fires staff is dependent on collection and intelligence personnel entering accurate, timely detection data into MSS — or on automated data feeds from radar systems functioning correctly.

The confidence level assigned to each target in MSS is the detect phase's most important output. A "Confirmed" target has been positively identified by two or more independent sources. A "Suspected" target has been reported by one source and awaits corroboration. A "Templated" target is placed at an expected location based on OPFOR TTPs, not by actual detection. These categories are not academic distinctions — they drive fires planning and ROE compliance. Fires against a Confirmed target carry a different risk calculus than fires against a Templated one. The FSCOORD who allows the fires team to treat all three categories identically is accepting legal and operational risk that the doctrinal confidence level system exists specifically to prevent.

**Deliver phase: fires mission tracking and the deconfliction problem.** The Deliver phase in MSS is about visibility and deconfliction, not execution. AFATDS executes. MSS makes execution visible to the fires staff.

The critical fires staff function during the Deliver phase is deconfliction — ensuring that two fire missions do not occupy the same airspace simultaneously, that fires near FSCM boundaries are coordinated before clearance, and that the fires cell knows which assets are committed to current missions before assigning new ones. MSS enables this deconfliction by displaying active missions on the fires picture, maintaining the FSCM overlay, and showing asset engagement status in real time.

The latency problem in the Deliver phase is real: the time between a mission being fired at AFATDS and the corresponding MSS record being updated may be non-trivial if the AFATDS-MSS interface is degraded or if FDC personnel are not immediately updating MSS. Fires cells must account for this latency in their deconfliction procedures — not assuming MSS is perfectly current during high-tempo fires execution.

**Assess phase: BDA as a decision product, not a historical record.** BDA in MSS is operationally useful only if it is entered correctly, entered timely, and used to drive the next targeting decision. When BDA is entered as a bureaucratic completion step — filling in the record after the fact with minimal analysis — it becomes a historical log rather than a decision product.

The assess phase in MSS should drive three decisions: Does this target require re-attack? Does this BDA result change the commander's priorities on the HPTL? Does this BDA indicate a collection shortfall that requires a new ISR tasking? When the fires team uses BDA actively to ask these three questions after each strike, the targeting circuit accelerates. When the fires team enters BDA and moves on, the circuit runs in only one direction.

### What MSS Cannot Do

Understanding what MSS cannot do is as important as understanding what it can. This distinction prevents dangerous over-reliance on the platform.

MSS cannot compute a ballistic fire command. The targeting solution — elevation, deflection, charge, fuze — comes from AFATDS. MSS records the fire mission; it does not compute it. If a fires cell loses AFATDS and relies on MSS for fire direction, it will have visibility without execution capability.

MSS cannot make a fires decision. It provides data to inform decisions. The decision to clear a fire mission, to approve a counterfire nomination, to authorize engagement of an air track — all of these are human decisions made by qualified officers and NCOs. MSS makes those decisions more informed; it does not make them.

MSS cannot guarantee data accuracy. MSS displays what has been entered. Incorrect data entered accurately is still incorrect data displayed accurately. The fires cell that enters wrong coordinates, wrong BDA, or wrong engagement authority into MSS will see those errors faithfully reproduced on every display that queries that data. Garbage in, garbage out applies with particular consequence in a fires data context.

### The Sensor-to-Shooter Data Chain

The sensor-to-shooter chain is the data path from detection of a target to delivery of fires on that target. Every link in that chain has latency — time between the event and the data representing the event appearing in MSS. Latency matters in fires because targets move and opportunities close. A counterfire target detected by Q-36 radar may have repositioned within 10 minutes of firing. A time-sensitive target identified by an ISR asset may have a 15-minute window before it disperses.

MSS reduces sensor-to-shooter latency when data feeds are active and fires personnel are disciplined about immediate data entry. It cannot eliminate latency. The fires cell that understands where latency exists in its sensor-to-shooter chain — where data is delayed by interface issues, reporting chains, or staffing — can compensate with faster human coordination alongside the MSS record.

The dangerous assumption is that the MSS picture is current when it may not be. Target data in MSS carries a "last detection DTG" field precisely to make data age visible. Fires planners must check that field before planning strikes, not assume that a target on the HPTL was confirmed recently. A target detected six hours ago in a high-tempo environment may have moved, been engaged by another unit, or ceased activity. Six-hour-old data is not a current target.

---

## SECTION 3 — FIRE SUPPORT COORDINATION AS A DATA PROBLEM

### Why FSCM Data Must Be Authoritative and Current

Fire support coordination measures exist to prevent two things: friendly fire on friendly forces, and fires on protected sites. They accomplish this by establishing geographic boundaries and conditions within which fires are permitted or restricted. Every FSCM is either a permission structure or a restriction structure. When FSCM data in MSS is wrong, the fires cell is operating with false permissions or false restrictions — either of which can produce catastrophic outcomes.

The word "authoritative" has a specific meaning in the context of FSCM data. An authoritative FSCM record is one that has been entered into MSS by an authorized user, reflects the FSCM as approved by the establishing headquarters, is accompanied by the correct effective period and geographic boundary, and has been verified for accuracy before publication to subordinate fires workspaces. These are not bureaucratic requirements — they are the conditions that make the FSCM display trustworthy as a clearance of fires tool.

Many fires staff errors in FSCM management come from shortcuts in the authorization chain. The FSCOORD's RDO updates an FSCM in MSS without confirming the change with the establishing headquarters. A subordinate FSO moves an NFA boundary in MSS to reflect what they believe the correct boundary should be, without authority. A fires cell publishes an FSCM from a draft order before final approval. Each of these shortcuts creates a version of the FSCM in MSS that may not match the authoritative version — and the fires team using MSS to clear fires will clear based on the version that appears on their display, not the authoritative version they have not seen.

Current FSCM data requires an active update process tied to the fires planning cycle. Every order and FRAGO that modifies a coordination measure must produce an immediate MSS update. The standard that FSCM overlays in MSS are updated within one hour of order publication is not arbitrary — it reflects the time window within which fires planning and execution may be conducted against the previous FSCM picture. An hour of operations with a stale FSCM picture is an hour of operations with an unmanaged fratricide risk.

### The Concept of FSCM Drift

FSCM drift is the gradual divergence between the FSCM overlay in MSS and the actual, current coordination measures in effect across the battlespace. It is one of the most insidious fires data problems because it is cumulative and often invisible until it produces a near-miss or incident.

FSCM drift begins when a coordination measure changes but MSS is not updated immediately. The establishing headquarters issues a FRAGO, the fires cell acknowledges it, but the duty officer updates the PowerPoint annex and defers MSS entry until "there's time." Time does not come during the battle rhythm, and by the next morning's targeting working group, the FSCM overlay in MSS is 18 hours out of date. Fires were cleared during the night based on the display. No incident occurred — by chance.

The second driver of FSCM drift is the expiration problem. FSCMs entered in MSS with expiration DTGs expire quietly. If the fires cell does not actively monitor FSCM expiration and either renew or archive expired measures, expired FSCMs accumulate on the overlay, degrading its fidelity. Fires personnel who know a particular NFA is "supposed to still be active" may ignore the expired indicator and continue treating it as authoritative. This behavior defeats the purpose of the expiration field entirely.

The third driver is the echelon problem. At BCT, the FSCM overlay in MSS receives measures from division as well as BCT's own organic measures. If the division fires cell is not publishing FSCM updates promptly, the BCT fires cell is working with a partially stale overlay even if they have maintained their own measures perfectly. Shared responsibility for a shared data product requires shared discipline across echelons.

Fires leaders combat FSCM drift through three practices: real-time update discipline (enter FSCM changes immediately, not at the next opportunity), expiration monitoring (the fires cell designates a duty officer responsible for reviewing FSCM expiration status daily), and cross-echelon verification (FSOs periodically confirm the FSCM overlay against the establishing headquarters' record, not just against MSS).

### Shared Workspace Discipline

The MSS fires workspace is shared across all fires personnel — FSCOORD, targeting officer, FSOs, FDC, AMD operations center. This sharing is the source of MSS's greatest operational value: every fires user sees the same picture simultaneously. It is also the source of its greatest vulnerability: any user with write access can degrade the shared picture by entering incorrect data.

Shared workspace discipline begins with access control. The MSS system administrator, in coordination with the FSCOORD, configures write access for fires modules consistent with duty position authorities. The FSCOORD does not give every fires user write access to every module. Write access to the HPTL is limited to the FSCOORD and targeting officer. Write access to FSCM overlays is limited to fires cell staff with establishing headquarters coordination responsibility. Write access to BDA records belongs to FSOs and the targeting officer. These controls are not bureaucratic obstacles — they are the first line of defense against accidental or unauthorized data corruption in a shared fires workspace.

Beyond access controls, shared workspace discipline requires that fires users understand the consequences of their data entries on everyone who shares the workspace. When a 13F FSO enters a BDA record, that record becomes visible to the targeting officer and FSCOORD immediately. If the BDA is inaccurate, the targeting officer may generate a faulty re-attack recommendation based on it. When a fires cell NCO archives an active FSCM, that measure disappears from every FSO's display simultaneously. The immediate impact of individual data actions on the shared fires picture should be part of every fires team's training on MSS.

### The Relationship Between the Fire Support Plan and the MSS FSCM Overlay

The fire support plan is the foundational document. The MSS FSCM overlay is the operational data expression of the fire support plan's coordination measures. These two must be synchronized, but they are not the same thing.

The fire support plan exists in the OPORD annex. It is a text and graphics product that describes the fires scheme, priority targets, and coordination measures. It is published through the orders process and has a specific format, authority chain, and legal standing. When the FSCOORD publishes a fires annex, it is the authoritative planning document.

The MSS FSCM overlay translates the coordination measures from that annex into a live geospatial display. It adds operational value the printed document cannot — real-time updates, expiration monitoring, simultaneous visibility across all fires users, and integration with the fire mission log and targeting module. But the MSS overlay is derivative of the fire support plan, not primary to it. When the two conflict — when the MSS overlay shows an NFA boundary that does not match the fires annex — the fires annex is authoritative, and the MSS overlay requires correction.

Fires staffs that use MSS as the primary fire support planning tool and treat the written fires annex as a summary of MSS data have reversed this relationship in a way that creates risk. Orders have legal standing; MSS data does not. When an operational law review of fires clearances occurs, the authoritative record is the fires annex and the clearance documentation — not the MSS display at the time of clearance. Fires cells must maintain both.

---

## SECTION 4 — AMD OPERATIONS MENTAL MODEL: THE LAYERED DEFENSE AS A DATA PICTURE

### The Layered Defense in Data Terms

AMD doctrine organizes air and missile defense in layers: HIMAD (Patriot) providing long-range and high-altitude protection, SHORAD providing medium and short-range protection, and MANPADS/guns providing point defense. Each layer has different sensors, different engagement envelopes, and different engagement authorities. Coordinating these layers to provide continuous, gap-free defense of critical assets is the AMD task force commander's core challenge.

MSS supports that challenge by presenting the layered defense as a data picture rather than a graphic. In MSS, each AMD system is a data object with location, coverage parameters, readiness status, missile inventory, and engagement authority. The AMD TF commander who views the MSS AMD display sees — for the first time with a single display — whether the Patriot sector of fire overlaps cleanly with the M-SHORAD coverage area, whether the combined coverage envelope covers all DAL assets, and where the defense design has gaps that require repositioning or reinforcement.

The critical insight is that the layered defense is not static once established. Systems move. Systems go non-mission capable. Threats change their approach vectors. The defended assets list changes as the operational situation evolves. The AMD defense design must adapt continuously, and MSS enables that adaptation by making the current state of the layered defense visible in real time. An AMD TF commander who reviews the MSS AMD display at the morning update and then does not review it again until the evening update is accepting six to twelve hours of unmonitored defense design drift. AMD operations demand continuous monitoring, and MSS enables it.

The data picture of the layered defense also makes visible what the defense design cannot cover. This is uncomfortable but necessary information. No AMD force has enough resources to defend all critical assets against all threat axes simultaneously. The AMD TF commander's job is to make explicit decisions about prioritization — which assets are defended, which are not, and what residual risk the commander accepts for undefended or under-defended assets. MSS makes those gaps visible in the coverage display, forcing explicit command decisions about risk rather than allowing coverage gaps to remain invisible assumptions.

### Engagement Authority as a Command Function

Nothing in AMD operations is more important to get right than engagement authority. Engagement authority determines which personnel can authorize weapon release against which track categories in which circumstances. In AMD, the consequences of getting this wrong flow in both directions: an unauthorized engagement may produce fratricide of a friendly aircraft; a failure to engage when authority was available may result in a missile striking a defended asset.

MSS records engagement authority status across all AMD systems. That record is operationally valuable — the AMD TF commander can see at a glance whether all systems are at Weapons Tight, whether any area is at Weapons Hold, and whether engagement authority has been delegated to subordinate elements. But the record in MSS is not the engagement authority itself. It is a data representation of command decisions that have been made and communicated through the command authority chain.

This distinction matters for two reasons. First, if the engagement authority displayed in MSS does not match the commander's actual current directive — because the record was not updated after a verbal directive, because a FRAGO changed engagement authority before MSS was updated, or because an entry error was made — the displayed authority is misleading. AMD operators who reference MSS to confirm engagement authority without cross-checking against the commander's directive are relying on potentially stale data in a lethal decision context.

Second, engagement authority in MSS is a record of decisions, not an automated approval system. There is no scenario in which a displayed "Weapons Tight" status in MSS authorizes an engagement that the commander has not directed. The MSS display confirms what has been directed; it does not substitute for the commander directing it. AMD units must train this distinction to every operator: MSS tells you the current status; it does not give you authority.

### CAL/DAL Management as a Continuous Process

The common approach to CAL/DAL management treats it as a planning product: produced during mission analysis, approved by the commander, and then referenced throughout the operation. This approach is correct for the initial production of the CAL/DAL. It is insufficient for CAL/DAL management over the duration of an operation.

Critical assets move. HQDA facilities relocate as the operational situation changes. Forward logistics elements displace. Command posts jump. Theater hospitals relocate. Each of these movements changes the CAL/DAL because the position data underlying the defense design is no longer accurate. If the CAL/DAL in MSS has not been updated to reflect asset movement, the defense design display shows AMD systems defending positions that the defended assets have vacated — and the actual positions of those assets may be undefended.

The second dynamic is AMD system status. A Patriot battery that goes NMC cannot defend its sector. When the battery goes NMC, the effective defended area contracts until the battery is restored to FMC. If the DAL in MSS is not updated to reflect the battery's NMC status, the display shows continuous coverage that no longer exists. The AMD TF commander needs to know this immediately — not at the next update cycle.

Effective CAL/DAL management in MSS requires two standing practices. First, every movement of a CAL-listed asset triggers an immediate CAL/DAL update. Unit SOP must include notification to the AMD operations center when a defended asset displaces. Second, every AMD system status change triggers a coverage reassessment. The 14A's daily review of AMD system status includes an assessment of whether current system positioning and readiness can still defend all DAL assets — and if not, an immediate report to the AMD TF commander.

### HIMAD/SHORAD Integration: Different Data Domains, Shared Picture

Patriot (HIMAD) and SHORAD/M-SHORAD systems operate in different data environments with different organic command and control systems. Patriot systems operate under IBCS (or legacy AMDWS). SHORAD and M-SHORAD systems operate under FAAD C2. These systems do not natively speak the same data language, and their pictures are not automatically integrated.

MSS provides the integration layer where both HIMAD and SHORAD data appear on a single AMD operational picture. This is the operational value of MSS in the AMD domain: the AMD TF commander does not need to switch between IBCS and FAAD C2 displays to see both layers of the defense — they see both in MSS simultaneously.

The integration comes with a limitation that AMD leaders must understand. MSS receives data from IBCS and FAAD C2. It does not control them. The AMD TF commander uses MSS to visualize the integrated defense picture and to maintain the CAL/DAL and engagement authority records. Command and control of AMD engagements flows through IBCS and FAAD C2, not through MSS. This means that a degradation in the IBCS or FAAD C2 data feeds to MSS will degrade the MSS AMD picture even when both AMD systems are fully operational. AMD operations continue through IBCS and FAAD C2; MSS simply has reduced visibility until the feed is restored.

---

## SECTION 5 — FIRES-INTEL INTEGRATION: THE INTELLIGENCE-FIRES NEXUS IN MSS

### The Shared Data Problem

Fires and intelligence share a fundamental data problem: both depend on knowing where the enemy is, what they are doing, and what capabilities they can bring to bear. In legacy operations, fires and intelligence operated largely in parallel, sharing products through formal reporting channels but often working from different operational pictures. ISR data went to the S2; targeting data stayed in the fires cell. The two communities synchronized at the TWG but operated separately in between.

MSS changes this by providing a shared data environment where fires and intelligence data coexist. The target record in MSS that carries a "Suspected" confidence level is reflecting intelligence collection status. The BDA record in MSS that the targeting officer enters after a strike is an intelligence product. The HPTL that the FSCOORD maintains in MSS is derived from intelligence assessments of OPFOR capability priorities.

The shared environment creates an integration opportunity. When intelligence and fires personnel both maintain their data in MSS and both review each other's entries, the fires picture updates faster, the intelligence picture is more operationally relevant, and the targeting cycle runs at higher tempo. The S2 who updates a target record's confidence level from "Suspected" to "Confirmed" in MSS provides immediate operational value to the fires cell without a formal reporting transaction. The fires cell that updates BDA records promptly provides the S2 real-time data for battle damage assessment that the intelligence analytical products can incorporate.

The shared environment also creates an integration risk. When fires and intelligence personnel have different update disciplines — when fires data is entered in real time but intelligence data lags, or vice versa — the shared picture is internally inconsistent. The fires cell sees target data that intelligence has not updated with new collection. The intelligence cell sees BDA data that the fires cell entered without adequate collection foundation. Both sides of this inconsistency produce operational problems.

### Collection Requirements and the PIR-to-HPT Chain

The intelligence-fires nexus in MSS is most visible in the relationship between priority intelligence requirements (PIR) and high-payoff targets. PIR are the questions whose answers the commander needs most urgently to make decisions. HPTs are the targets whose engagement will most decisively affect the operation. In a well-functioning targeting process, every HPT category on the HPTL is linked to a PIR question, and every PIR question drives a collection requirement against a specific ISR asset.

In MSS, this chain is visible. The targeting module links HPT categories to collection requirements. The collection management module links collection requirements to ISR assets. When an ISR asset reports a positive find on an HPT category, that find updates the target record, the HPTL confidence level, and the collection status simultaneously. The fires cell targeting officer can see immediately that an HPT has been confirmed, and the targeting cycle can proceed to the Deliver phase.

The chain breaks when collection requirements are not entered in MSS, when ISR assets are tasked to collect against HPTs but the collection plan is not documented in MSS, or when collection results are reported through channels outside MSS and not entered into the target record. Each break in the chain is a point where fires-intel integration degrades from a functioning circuit into two separate processes that synchronize only when personnel communicate explicitly — which under operational stress and tempo, may not happen often enough.

### BDA as an Intelligence Product

BDA occupies an interesting position in the fires-intelligence relationship. Fires personnel produce and enter BDA in MSS. But BDA is fundamentally an intelligence product — it answers the question "what effects did fires produce on OPFOR capability?" That question is an intelligence question, requiring collection and analysis by personnel with the training and access to assess enemy system status.

The tension between fires ownership of BDA and intelligence ownership of BDA assessment is a recurring challenge in targeting operations. Fires teams are responsible for recording BDA from their fires; they own the data entry. Intelligence teams are responsible for assessing the accuracy and depth of BDA; they own the analytical product. In MSS, both can coexist: the fires team enters BDA collection data (what observers reported, what imagery shows), and the intelligence team annotates with analytical confidence and system disruption assessment.

Effective BDA in MSS requires both communities to treat the BDA record as a shared product. Fires teams that enter BDA without seeking intelligence input on functional and system disruption levels are producing incomplete BDA. Intelligence teams that assess BDA without updating the MSS record are producing assessment products that do not feed the targeting cycle. The targeting working group is the synchronization event that brings both communities together around the BDA data — but the data must be entered and maintained by both communities between TWGs for the synchronization to be meaningful.

### The Targeting Working Group as a Data Synchronization Event

The targeting working group is typically described as a decision-making forum: the fires cell, intelligence, operations, and effects community reviews the targeting picture and makes recommendations to the FSCOORD and commander on priorities and attack guidance. That description is accurate, but it undersells the TWG's data function.

The TWG is also the moment when everyone in the targeting process aligns on the same data picture. Before the TWG, fires, intelligence, and operations may have been working from slightly different versions of the HPTL, the target list, and the BDA record — each maintaining their own products with different update cycles. The TWG forces reconciliation of these products into a single authoritative picture, and that reconciliation updates MSS.

When the TWG uses MSS as its primary display — when the HPTL, BDA log, and target status are projected from MSS rather than from a separate PowerPoint — the TWG output naturally flows into MSS. Target priority changes made at the TWG are entered in real time. New collection requirements generated by the TWG are entered immediately. BDA analytical updates from the S2 are entered on the spot. The TWG becomes a live data review that produces updated MSS records rather than a separate slide product that requires a subsequent data entry step.

Units that run the TWG from PowerPoint slides and then have a separate step to update MSS afterward introduce delay and error. The slides and MSS diverge during the update process. Priorities approved at the TWG may take hours to appear in MSS. Subordinate FSOs planning fires support for the next phase may be planning against a HPTL that has not yet been updated in MSS from the TWG output.

---

## SECTION 6 — THE ROLE OF ASSESSMENT IN FIRES

### BDA and Re-Attack as a Fires Learning Loop

Fires without assessment is shooting in the dark. Assessment closes the targeting cycle by answering whether fires achieved the intended effects and whether the target requires re-engagement. Without that answer, the fires process cannot learn, adapt, or confirm that it is achieving the commander's objectives.

BDA in MSS is the mechanism for capturing that answer. When BDA is entered accurately and analyzed rigorously, it enables the fires cell to determine whether re-attack is necessary, whether the AGM guidance produced the right effects, and whether the fires plan is achieving operational objectives. These are not administrative questions — they are the feedback loop that makes fires a precision capability rather than a blunt instrument.

The learning loop requires that BDA records in MSS are treated as more than completion entries. Each BDA record should prompt three questions: Was the effect achieved? If not, why not (wrong munition, incorrect target, missed location, OPFOR countermeasures)? What does this tell us about the AGM guidance for this target category? When fires teams ask these questions systematically, the AGM evolves through the operation to reflect what actually works against the threat the formation is encountering — not what worked in a different theater against a different OPFOR.

The firing data linked to BDA records in MSS supports this learning loop. When the fire mission log is connected to the BDA record, the fires cell can assess fires effectiveness against the munition type, weapon system, and effects desired for each target category. Over multiple engagements, patterns emerge: certain munitions consistently fail to achieve desired effects against certain target types; certain weapons systems produce more consistent results against certain target categories. This is fires learning in data form, and it requires the fire mission log and BDA records in MSS to be complete and linked.

### How MSS Enables Fires Assessment

MSS enables fires assessment at three levels: individual mission BDA, HPTL engagement tracking, and theater-level fires effectiveness analysis.

At the individual mission level, BDA records in MSS carry the full assessment data required by FM 3-60: physical destruction, functional damage, and system disruption. When these fields are completed with collection data and analytical confidence levels, they provide the targeting officer with the information needed to make a re-attack recommendation within minutes of BDA collection — not at the next day's TWG.

At the HPTL level, MSS tracks the engagement status of all target categories: how many confirmed targets have been engaged, what BDA results have been recorded, how many targets remain unengaged, and how many re-attack nominations are outstanding. This HPTL engagement status view is the fires assessment product the FSCOORD needs to brief the commander: "Of 12 HPTL categories, we have engaged 8 with confirmed BDA meeting standard. Four categories remain unengaged due to collection shortfalls. Two engaged categories have re-attack nominations pending TWG."

At the theater level, fires effectiveness analysis in MSS aggregates BDA data across multiple targeting cycles and formations to assess the cumulative effects of fires on OPFOR capabilities. This analysis is the operational-level fires assessment product — it connects tactical BDA to the operational question of whether fires are degrading OPFOR combat power at the rate required to achieve conditions for the decisive operation. The MOE/MOP framework in MSS provides the structure for this analysis; the BDA data is the input.

### The Command Climate Dimension of BDA

There is a dimension of BDA that no technical platform can address: the human incentive to report BDA optimistically. This is not a new problem. Fires assessment has struggled with BDA inflation as long as fires have been employed. The incentive to report fires as effective is real — it reflects positively on the delivering unit, supports the fires plan, and avoids the uncomfortable conversation about re-attack. MSS does not eliminate this incentive. It makes BDA records visible and permanent, which creates accountability — but accountability only operates if commanders demand it.

The FSCOORD who creates a command climate where honest BDA is expected and rewarded, and where inflated BDA is identified and corrected, will have fires assessment data in MSS that actually supports sound re-attack decisions. The FSCOORD who allows optimistic BDA to persist because it is administratively convenient will have an HPTL engagement status that looks positive while the operational effects are insufficient.

BDA quality in MSS is ultimately a command climate issue, not a technical one. The technical controls — required fields, confidence level entries, collection source documentation — provide structure. The command climate determines whether that structure produces honest data or compliant but inaccurate records.

### MOE vs. MOP for Fires

### The Assessment Clock

Fires assessment is perishable in a way that fires planning and execution are not. A BDA record entered 48 hours after fires execution reflects a 48-hour-old picture of the target's status. In a dynamic operational environment, that target may have reconstituted, repositioned, been engaged by another unit, or changed its operational significance entirely in those 48 hours.

The fires cell that treats BDA entry as a completion step — something done when time permits after the operational action — is producing a historical record rather than an operational product. BDA that drives re-attack decisions must be current. BDA that is entered the next day to satisfy an administrative requirement does not drive re-attack decisions; it confirms what has already been assumed.

Assessment tempo is a command priority. When the FSCOORD establishes and enforces the BDA entry standard — entry within two hours of fires execution or within one hour of BDA collection, whichever occurs first — the assessment product in MSS is operationally relevant. When the FSCOORD allows BDA entry to accumulate and be entered in batches at the end of the day, the assessment product is a log. Both can look identical in MSS. Only one is operationally useful.

---

### MOE vs. MOP for Fires

Fires assessment uses both measures of performance (MOP) and measures of effectiveness (MOE), and the distinction matters for how fires leaders interpret MSS assessment data.

MOPs measure whether fires did what fires were supposed to do. Response time (time from CFF to first round), mission completion rate (missions executed vs. missions assigned), and BDA timeliness (time from execution to BDA entry) are all MOPs. They tell the fires cell whether the fires process is running at the right tempo and with the right discipline. A poor MOP — slow response time, high mission cancellation rate, chronically late BDA — indicates a fires process problem that requires correction at the fires cell or FDC level.

MOEs measure whether fires achieved the effects the commander needed to achieve the operational objective. Physical destruction achieved, functional capability degraded, system-level OPFOR capability affected — these are MOEs. They tell the commander whether fires are contributing to operational success. A strong MOP (fires were delivered quickly and efficiently) combined with a weak MOE (fires are not degrading OPFOR capability) indicates a targeting problem, not a fires process problem — the fires team is doing its job well but targeting the wrong things or with the wrong effects approach.

Fires leaders who conflate MOPs with MOEs will brief good performance while missing operational failure. A fires cell with excellent response times, high mission completion rates, and timely BDA entry (strong MOPs) but an HPTL of targets that are being repeatedly re-attacked without cumulative degradation of OPFOR capability (weak MOEs) is an efficient fires cell producing insufficient operational effects. The commander needs to know this distinction. MSS provides the data for both analyses; the fires leader must ensure both are being asked.

The commander's fires briefing should present both dimensions explicitly. "We executed 47 missions this reporting period with an average response time of 8 minutes and 98% mission completion rate" is an MOP briefing. It tells the commander how the fires process performed. "We engaged 7 of 12 HPTL target categories. Confirmed BDA shows four categories at PMCII or NMC functional status. Three categories require re-attack. OPFOR indirect fire volume in the BCT AO has decreased by 40% over the past 48 hours" is an MOE briefing. It tells the commander whether fires are contributing to operational success. Both briefings require different MSS data views, but both are available from MSS when data is maintained to standard. Present both. A commander who receives only one is making operational decisions without half the fires assessment picture.

---

## SECTION 7 — FIRES FAILURE MODES IN MSS

### The Fires Commander's MSS Posture

Before working through the eight failure modes, a framing observation for fires commanders: the difference between fires units that use MSS effectively and those that do not is rarely technical. The platform is the same. The difference is posture — whether the fires commander treats MSS as the operational fires data environment or as an administrative reporting tool.

Commanders who treat MSS as operational will: attend targeting working groups that use MSS as the primary display rather than PowerPoint exports; ask fires cell members to pull specific data from MSS in real time rather than accepting pre-prepared slides; spot-check FSCM currency in MSS before clearing fires near coordination boundaries; review BDA records linked to mission records rather than accepting verbal BDA summaries. These behaviors signal to the fires team that MSS accuracy has operational consequences.

Commanders who treat MSS as administrative will: accept PowerPoint slides summarizing MSS data without checking the source; allow the fires cell to update MSS "when there's time"; treat MSS training as a check-the-box requirement; and accept BDA report formats disconnected from MSS records. These behaviors signal to the fires team that MSS is for reporting to higher, not for operational decision-making.

The eight failure modes documented below are downstream effects of a fires team that has received the second signal rather than the first.

---

### Introduction

Fires units fail in MSS in predictable ways. The following eight failure modes have been identified across USAREUR-AF exercises, after action reviews, and operational observations. Each failure mode has a root cause, an indicator visible to a senior leader reviewing MSS data, and a correction. Senior leaders who understand these failure modes can identify them early — before they produce operational consequences.

Understanding failure modes before they occur is the fires commander's analytical advantage. The eight failure modes documented here are not exotic. All are preventable. Most are visible to a senior leader who knows what to look for in MSS data.

The pattern across these failure modes is consistent: they are not primarily technical failures. They are human and organizational failures that manifest in the data. Stale target data does not create itself — someone stopped updating it. FSCM drift does not occur spontaneously — someone deferred an update. BDA inflation does not emerge from the platform — someone entered optimistic data. Targeting without intelligence integration does not happen by accident — two organizational cultures failed to establish a shared data workflow.

This means the corrections are also human and organizational, not primarily technical. Better MSS training helps. Correct access configuration helps. But the primary variable is command climate — whether the fires commander creates conditions where data accuracy and currency are valued, enforced, and modeled. The senior leader who reads each failure mode's "senior leader indicator" should ask: have I seen this in my fires cell? If the answer is yes, is the correction already in place?

---

### Failure Mode 1: Stale Target Data

**Description.** Target records in the HPTL and target library are not updated as collection assets report new information. Target locations reflect initial detection data rather than most recent confirmed position. Confidence levels remain at "Suspected" or "Templated" for targets that collection assets have continued to observe.

**Root cause.** Intelligence and fires personnel do not maintain the habit of updating target records in real time. The target library is treated as a planning product rather than a live data object. The S2 produces intelligence products in separate formats (slides, overlays, reports) without synchronizing them to MSS target records. The fires cell does not have a defined process for incorporating intelligence updates into the target record.

**Senior leader indicator.** Target records show "last detection DTG" values more than 24 hours old for active-collection targets. Multiple targets show "Templated" confidence level despite active ISR tasking against that target category. BDA records exist for targets that still show "Active" status in the target library.

**Correction.** Establish a target record update standard: every intelligence reporting cycle produces target record updates in MSS, not just intelligence summary products. Assign the targeting officer and S2 joint ownership of the target library. Make the "last detection DTG" field a TWG review item at every targeting meeting.

---

### Failure Mode 2: FSCM Drift

**Description.** The FSCM overlay in MSS does not reflect the current coordination measures in effect. Expired FSCMs remain on the overlay. New FSCMs from orders and FRAGOs have not been entered. FSCM boundaries in MSS do not match the boundaries in the fires annex or the establishing headquarters' record.

**Root cause.** FSCM updates are deferred to convenient moments rather than made immediately on order publication. The fires cell does not have an active FSCM expiration monitoring process. Echelon-level FSCM ownership is unclear — BCT fires cell is waiting for division to update the overlay; division fires cell believes BCT has made updates it has not.

**Senior leader indicator.** FSCM publication DTGs more than 12 hours old in an active environment. Expired FSCMs visible on the overlay with no archive or renewal action. FSOs reporting that the MSS FSCM overlay "doesn't match what we were briefed" in the fires annex.

**Correction.** Make FSCM overlay currency a daily fires cell inspection item. Assign a specific individual (fires cell operations NCO or duty officer) as FSCM currency monitor. Establish a rule: FSCM changes are entered in MSS before the battle update briefing that follows the order that changed them.

---

### Failure Mode 3: Sensor-to-Shooter Disconnect

**Description.** MSS target records do not receive detection data from active sensors in time to drive counterfire or time-sensitive targeting. Radar data feed to MSS is delayed or inactive. Intelligence reports of confirmed target locations are not reflected in target records. The fires cell is making targeting decisions based on MSS data that is significantly behind the sensor picture.

**Root cause.** The AFATDS-MSS interface or the radar-MSS data feed is degraded and has not been restored. Manual entry procedures have not been activated. Intelligence reports arrive in MSS later than in the S2's own intelligence tools because the S2 updates separate intelligence systems first and MSS second.

**Senior leader indicator.** Fire missions being executed against targets whose MSS location data has not been updated since the previous day. Counterfire nominations being generated hours after POO detections because the radar data feed was not checked. BDA records linked to targets whose location data had not been updated between the initial detection and the fires execution.

**Correction.** Establish sensor interface status as a fires cell monitoring responsibility. When any sensor-MSS interface degrades, activate manual entry immediately rather than waiting for the interface to restore. Make intelligence-MSS synchronization a TWG standard: every TWG begins with a review of the gap between intelligence product reporting and MSS target record currency.

---

### Failure Mode 4: AMD ROE Confusion

**Description.** The engagement authority status recorded in MSS does not match the commander's actual current directive. Different AMD elements are operating under different understandings of engagement authority. The MSS AMD module shows "Weapons Tight" but the commander has verbally directed a more restrictive posture in a specific area without a corresponding MSS update.

**Root cause.** Verbal engagement authority directives are not immediately entered into MSS. FRAGO-driven changes to engagement authority reach the AMD operations center through voice channels before the MSS record is updated. Personnel reference the MSS display for engagement authority without cross-checking against the most recent directive.

**Senior leader indicator.** AMD personnel who cannot immediately confirm whether the MSS engagement authority record reflects the most recent commander's directive. Engagement authority records without a corresponding order or directive reference. AMD units reporting engagement authority from verbal direction that does not match MSS records.

**Correction.** Establish a firm rule: every engagement authority change is entered in MSS within 15 minutes, referencing the order, FRAGO, or directive that established it. The 14A confirms the MSS record with the AMD TF commander at every battle update briefing. AMD personnel are trained that MSS is the record, not the source of authority — they must always cross-check the MSS record against the most recent directive.

---

### Failure Mode 5: BDA Inflation

**Description.** BDA records in MSS reflect more favorable effects than collection data actually supports. Physical destruction percentages are higher than imagery or observer reports justify. Functional damage assessments report systems as NMC when collection data supports only PMCI. System disruption assessments are reported as C3 or C4 (significant capability degradation) when the basis for that assessment is speculative.

**Root cause.** Fires teams enter BDA based on assumptions rather than collection data. The command climate implicitly rewards positive BDA. The fires cell does not cross-check BDA entries against the collection source documents. Intelligence assessment of BDA is not sought or incorporated into BDA records.

**Senior leader indicator.** Repeat re-attack cycles on targets that MSS records as "assessed — effects achieved." High percentage of BDA records where the collection source field is "Observer" without supporting documentation. Intelligence community assessments of OPFOR capability that conflict with the fires cell BDA picture.

**Correction.** Require collection source documentation for all BDA entries above PMCII level. Establish joint fires-intelligence review of BDA records at the TWG. The FSCOORD reviews a random sample of BDA records each week against the supporting collection data. Create a command climate where honest BDA — including NMC upgraded to PMCI when revisit collection reveals the target has reconstituted — is expected and valued.

---

### Failure Mode 6: AFATDS/MSS Data Duplication and Inconsistency

**Description.** Fire mission records in MSS are inconsistent with AFATDS fire mission records. Rounds expended in MSS do not match rounds expended in AFATDS. Targets engaged in MSS are not the same as targets engaged in AFATDS. Class V consumption data in MSS and Class V records in the FDC are misaligned.

**Root cause.** The AFATDS-MSS interface is partially degraded, producing incomplete automatic data transfer. Manual update procedures are applied inconsistently — some missions are manually entered, some are entered only in AFATDS, some are double-entered producing duplicates. FDC personnel update AFATDS (their primary system) without corresponding MSS updates.

**Senior leader indicator.** Fire mission count discrepancies between the FSCOORD's MSS briefing and the FDC's daily mission count. Class V data in MSS that does not match the battery commander's actual on-hand report. BDA records in MSS with no corresponding fire mission record, or fire mission records with no associated BDA.

**Correction.** Establish AFATDS-MSS reconciliation as a daily FDC responsibility. The 13J or 13P reconciles the AFATDS fire mission log against the MSS fire mission log each morning and at every duty officer change. Discrepancies are corrected before the daily ammunition status update is submitted. The FSCOORD periodically reviews the reconciliation report, not just the fires summary.

---

### Failure Mode 7: Targeting Without Intelligence Integration

**Description.** The fires cell develops and prosecutes targeting against the HPTL without active synchronization with the intelligence cycle. Target records receive the initial intelligence-derived location at the time of HPTL development and are not updated by subsequent collection. BDA analytical assessment from the S2 does not appear in MSS BDA records. The TWG functions primarily as a fires cell product review rather than a fires-intelligence integration event.

**Root cause.** The fires cell and S2 section operate on different update cycles and do not share data in MSS in real time. The S2 maintains an intelligence picture in separate tools (DCGS-A, CIDNE, unit intelligence management systems) that is more current than the fires cell's MSS picture. The S2 provides intelligence support to fires through briefings at the TWG rather than through continuous MSS data maintenance.

**Senior leader indicator.** Target records that have never been updated by the S2 section — all data was entered by fires personnel at HPTL creation. BDA records with no functional or system disruption assessment, because the S2 section is not reviewing and annotating fires BDA in MSS. HPTL categories with stale "last detection DTG" values despite active collection against those target categories in the intelligence community's picture.

**Correction.** Make MSS target record co-ownership a fires-intelligence operating agreement. The S2 section designates a targeting warrant or NCO whose MSS responsibilities include updating target records and BDA assessments. The TWG includes an MSS data review segment where fires and intelligence personnel reconcile the MSS picture against the intelligence community's current assessment.

---

### Failure Mode 8: Fires-Maneuver FSCM Deconfliction Failure

**Description.** FSCM boundaries in MSS do not reflect the current position of maneuver forces, creating conditions where fires could be cleared short of friendly force positions or where fires restrictions protect areas that maneuver forces have vacated. The FSCL or RFL has not been updated to reflect maneuver progress. FSOs at the BCT are clearing fires based on FSCM boundaries that do not account for adjacent unit positions.

**Root cause.** Maneuver and fires staff do not maintain a synchronized common operating picture. The fires cell updates FSCMs based on orders but does not continuously track the relationship between maneuver force positions and FSCM boundaries. Maneuver S3 section and fires cell do not have a shared process for triggering FSCM updates when force positions change significantly.

**Senior leader indicator.** FSCL or RFL boundaries in MSS that have not been updated since the previous operational phase change, while maneuver forces have moved significantly. FSOs noting that the CFL has not been updated to reflect the unit's advance. Adjacent unit fires cells that are working with different FSCM boundaries than the supported maneuver element's fires cell.

**Correction.** Establish maneuver position-to-FSCM review as a standard item at every fires cell update: what has maneuver done, and does it require an FSCM update? The S3 and FSCOORD share responsibility for triggering FSCM updates when maneuver exceeds established position triggers. The FSO at the battalion level confirms with the fires cell that FSCM boundaries in MSS reflect current unit positions before clearing any fire mission near those boundaries.

---

### Summary Table: Fires Failure Modes in MSS

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

*UNCLASSIFIED // FOR OFFICIAL USE ONLY*

*CONCEPTS GUIDE — TM-40B COMPANION, Version 1.0, March 2026*

*HEADQUARTERS, UNITED STATES ARMY EUROPE AND AFRICA, Wiesbaden, Germany*

---

## COMMAND GUIDANCE FOR FIRES LEADERS

### For the FSCOORD and Fires Brigade Commander

This guide has two practical implications for fires commanders that go beyond the conceptual content.

First, MSS is only as good as the command climate that drives its use. A fires cell that updates MSS accurately under normal conditions but cuts corners under operational pressure will degrade the fires picture precisely when accurate data matters most. The FSCOORD who enforces MSS data standards during garrison and exercise training — who insists on correct FSCM entries, proper BDA documentation, and accurate Class V data — is building the habit discipline that will hold under operational stress. The FSCOORD who treats MSS as an administrative afterthought during training will find MSS unreliable in combat.

Second, the eight failure modes in Section 7 are not theoretical. They have appeared in USAREUR-AF exercises and in after action reviews of operational engagements. Each failure mode has a specific command action that prevents it. The FSCOORD who reviews Section 7 and identifies which failure modes their fires cell is most susceptible to — based on personnel, training posture, and system configuration — can focus corrective actions before the failure occurs.

For fires brigade and DIVARTY commanders: your most consequential MSS decisions are personnel decisions. The targeting officer who maintains the HPTL with discipline, the fires cell NCO who enforces data currency standards, and the 14A who keeps AMD data honest are the human infrastructure of the fires data picture. Invest in their MSS proficiency the same way you invest in their gunnery certification and fire direction proficiency. The consequences of deficiency are equally operational.

### For the AMD TF Commander

Section 4 of this guide addresses the AMD mental model directly. Two points warrant emphasis for AMD commanders.

The engagement authority section is not academic. AMD engagement decisions occur under the most time-compressed conditions in military operations. The commander who has clearly established, correctly recorded, and regularly confirmed engagement authority in MSS has given their AMD operators the best possible foundation for those decisions. Ambiguity in AMD engagement authority, whether it exists in the commander's mind, in the written ROE, or in the MSS record, is a risk that resolves badly in either direction.

CAL/DAL management as a continuous process — not a planning product — is the AMD TF commander's most underappreciated MSS responsibility. Review the CAL/DAL in MSS at every battle update briefing. Not once per operation. Every battle update. The defense of critical assets is only as good as the accuracy of the data that describes where those assets are and which AMD systems are covering them.

---

*UNCLASSIFIED // FOR OFFICIAL USE ONLY*

*CONCEPTS GUIDE — TM-40B COMPANION, Version 1.0, March 2026*

*HEADQUARTERS, UNITED STATES ARMY EUROPE AND AFRICA, Wiesbaden, Germany*

*Read this guide before beginning TM-40B. The procedural knowledge in TM-40B is more durable when it rests on the conceptual foundation this guide provides.*

*Questions and feedback on this guide should be directed to the USAREUR-AF C2DAO fires functional area representative. Doctrinal discrepancies between this guide and current Army doctrine will be resolved in favor of doctrine; report discrepancies for correction in the next revision.*
