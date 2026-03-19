# CONCEPTS GUIDE — TM-40C COMPANION — MOVEMENT AND MANEUVER WARFIGHTING FUNCTION · MAVEN SMART SYSTEM (MSS)

> **BLUF:** ADP 3-0's principles of combined arms operations, initiative, and tempo are not data concepts — but they all depend on data quality, currency, and shared access to execute. Understanding this relationship is the foundation for effective MSS use in M&M operations.
> **Prereqs:** TM-10 (Maven User), TM-20 (Builder), and TM-30 (Advanced Builder). Read this Concepts Guide after completing TM-30 and before beginning TM-40C task instruction.
> **Purpose:** This guide develops the operational mental models required to effectively integrate MSS into Movement and Maneuver warfighting function operations. It is a prerequisite companion to TM-40C and must be read before beginning TM-40C task instruction. This guide is conceptual — it develops understanding, not procedures. No step-by-step tasks appear here. The audience is S3/G3 officers, brigade and battalion commanders, and staff officers responsible for combined arms synchronization.
> *HQ USAREUR-AF · v1.0 · 2026 · DISTRIB: USG only*

---

## SECTION 1 — THE M&M WFF AND DATA: ADP 3-0 PRINCIPLES AS DATA REQUIREMENTS

**BLUF:** ADP 3-0's principles of combined arms operations, initiative, and tempo are not data concepts — but they all depend on data quality, currency, and shared access to execute. Understanding this relationship is the foundation for effective MSS use in M&M operations.

### 1-1. Movement and Maneuver as a Warfighting Function

The Movement and Maneuver warfighting function encompasses the tasks that move and employ forces to achieve a position of advantage (ADP 3-0, para 3-3). It includes maneuver, mobility, countermobility, air maneuver, and the integration of those tasks across arms. The function is fundamentally about mass — concentrating combat power at a time and place of advantage — and the exploitation of that mass through action faster than the enemy can respond.

Data is not mass. Data is not maneuver. But the ability to concentrate forces, time their actions, synchronize fires and obstacles and aviation, and exploit success faster than the enemy — all of these require timely, shared, accurate information about where friendly forces are, where the enemy is, what the terrain permits, and what the status of supporting functions enables.

MSS does not execute the M&M WFF. It provides the data infrastructure that supports the people and organizations responsible for executing it.

### 1-2. Tempo and Information Speed

ADP 3-0 establishes tempo — the rate of military action — as a critical factor in operational success (ADP 3-0, para 2-28). A force that acts faster than the enemy can react inside its decision cycle degrades the enemy's ability to respond coherently. Tempo in execution is enabled by tempo in decision-making. Tempo in decision-making depends on the speed with which accurate, actionable information reaches commanders.

MSS directly affects information tempo. A phase line crossing that reaches the S3 via voice report and is manually plotted on a paper map may take 20–30 minutes to reach the battalion commander in an integrated form alongside the fires status, the engineer mobility picture, and the adjacent unit situation. The same crossing, if the S3 section maintains MSS current practice, is integrated into the combined arms workspace within minutes and is simultaneously visible to the battalion, brigade, and any higher headquarters with workspace access.

This is not a trivial difference. At operational tempo, 20 minutes of information latency can represent a maneuver opportunity that opens and closes. The question for the S3 section is not "should we use MSS" — it is "how well can we maintain information currency under operational conditions?"

### 1-3. ADP 3-0 Operational Principles and Their Data Relationships

ADP 3-0 describes operational concepts — including convergence, calibrated force, and the operations process — that shape how the Army employs forces (ADP 3-0, Ch. 2). Each has a data relationship.

**Convergence.** ADP 3-0 describes convergence as the alignment of lethal and nonlethal capabilities across domains to create effects that overwhelm the enemy (ADP 3-0, para 2-5). Convergence requires that fires, cyber effects, electronic warfare, space effects, and ground maneuver are synchronized in time and space. Synchronization at that scale is not achievable without integrated data — the fires officer, the ground S3, the cyber planner, and the information operations officer must all be working from a shared operational picture. MSS is the ground maneuver layer of that shared picture.

**Calibrated Force Employment.** Employing forces in the right amount, at the right time, for the right task requires current knowledge of force status — readiness, location, task organization, and available combat power (ADP 3-0, para 2-12). A commander who does not know which battalion is at C-1 and which is at C-3 cannot make a calibrated force employment decision. MSS provides the combat power data layer that makes calibrated employment possible.

**Initiative.** Seizing and maintaining the initiative requires that the friendly force acts before the enemy can set conditions to negate friendly advantages (ADP 3-0, para 2-16). Initiative in execution means subordinate leaders act on opportunity when it presents itself. It also means the S3 section sustains the situational picture that allows the commander to recognize opportunity. A combined arms workspace that is 90 minutes stale does not support operational initiative.

> **NOTE: The operational principles in ADP 3-0 are human-executed concepts. They depend on leader judgment, training, and will. MSS supports the information conditions for those concepts — it does not execute them. A well-trained S3 section with poor data is better than a poorly trained section with current data. Both data quality and analytical capability matter.**

---

## SECTION 2 — COMBINED ARMS AS AN INFORMATION PROBLEM

**BLUF:** The fundamental challenge of combined arms operations is synchronization — getting multiple arms to produce complementary effects at the same time and place. Synchronization fails most often not because of tactical incompetence, but because the information required to synchronize was absent, delayed, or misunderstood. MSS addresses the information dimension of combined arms.

### 2-1. The Nature of Combined Arms Synchronization

Combined arms is the synchronized and simultaneous application of arms to achieve an effect greater than if each arm had been employed separately (ADP 3-0, para 1-5). The combined arms concept is more than 100 years old. What has changed is the complexity of the synchronization problem — more arms, more domains, greater physical dispersion, faster operational tempo, and a more contested information environment.

Synchronizing infantry, armor, engineers, fires, aviation, and electronic warfare across a BCT AO requires that each element knows:
- Where the other elements are (fratricide prevention, coordination)
- What each element is doing (task and purpose understanding)
- What conditions must be created before each element acts (sequencing)
- What signals or reports will trigger actions or transitions (battle tracking)

Each of these requirements is, at its core, an information requirement. The combined arms fight is simultaneously a fires fight, a mobility fight, and an information fight — and the information fight is what enables the others.

### 2-2. Where Combined Arms Synchronization Breaks Down

Combat history and USAREUR-AF exercise experience identify the same recurring breakdowns in combined arms synchronization. Most are information failures, not tactical failures.

**Fratricide** occurs most often when friendly force positions are unknown or incorrectly communicated. The most dangerous moment in a combined arms operation is any transition — passage of lines, boundary changes, axis shifts — when the shared picture of friendly force disposition has not been updated. MSS reduces this risk by maintaining the shared BFT display and the operational graphic layer together. It does not eliminate the risk — it reduces the latency of position information that enables fratricide prevention.

**Fires coordination failures** occur when the fires graphic layer is not synchronized with the maneuver graphic layer. A fires officer working from a fire support plan that does not reflect the latest FRAGO boundary changes will clear fires based on an incorrect friendly force boundary. When the fires graphics in MSS match the current OPORD/FRAGO graphics, this class of error is reduced.

**Mobility failures** occur when the maneuver force arrives at an obstacle that was not reported — or at a breach site that was reported open but is actually closed. Route and obstacle data in MSS is only as current as the reports entering it. The operational question is not "does MSS have obstacle data" but "how old is the obstacle data, and what has changed since the last engineer report?"

**Aviation deconfliction failures** occur when the airspace picture is not integrated with the ground maneuver picture. An air corridor activated while indirect fire is adjusting in the same airspace block is a lethal risk. MSS reduces this risk by displaying fires graphics and aviation graphics in the same workspace — but only if both are maintained with current data.

> **NOTE: Combined arms synchronization failures are almost always multi-causal. Information failures are one cause. MSS addresses the information cause. It does not address training deficits, leadership failures, inadequate rehearsals, or operational friction beyond its scope. An organization that uses MSS to substitute for combined arms rehearsals has misunderstood what the platform can do.**

### 2-3. The Shared Picture Requirement

The combined arms requirement for a shared operational picture is not new — operations orders, overlays, and map boards have existed for this purpose since organized military operations. What MSS changes is the persistence, integration, and simultaneous accessibility of that picture.

A paper map board in the S3 section accurately represents the current situation at the moment it is updated — and then begins to become inaccurate as conditions change and the map board is not updated. An MSS workspace that is actively maintained represents the current situation continuously, updated as reports arrive, visible simultaneously to every echelon with workspace access.

This difference has command implications. When the brigade commander and all three battalion S3s are looking at the same MSS combined arms workspace, shared understanding is structural — it is built into the platform. When the brigade commander is looking at a map board built from this morning's reports and the battalion S3s are working from their own acetate updates, shared understanding requires a briefing to achieve and begins degrading the moment the briefing ends.

---

## SECTION 3 — THE OPERATIONS PROCESS AND MSS

**BLUF:** ADP 5-0 describes the operations process as plan, prepare, execute, and assess — an iterative cycle, not a linear sequence (ADP 5-0, para 1-1). MSS integrates with each phase of the operations process not as a planning tool, but as the data layer that supports continuous situational awareness across all four phases simultaneously.

### 3-1. Plan — Data Support During Planning

During planning, the M&M practitioner uses MSS to integrate the data that informs planning decisions. This includes terrain analysis, enemy situation overlays, route and obstacle data, and readiness data for the forces being planned with.

The planning phase is the most data-intensive phase of the operations process — and the phase where MSS is most underused by M&M practitioners. S3 sections frequently default to building PowerPoint products for planning briefs rather than using MSS to present integrated data. A COA brief built on MSS — showing the proposed axis of advance against the current obstacle overlay, the route classification data, the enemy situation, and the available combat power by unit — is more analytically credible and more current than a slide built from last week's data call.

The discipline to use MSS during planning, not just execution, is an important professional maturity indicator for S3 sections.

### 3-2. Prepare — Maintaining Data While the Formation Prepares

During preparation, the priority of work for the S3 section is confirming the MSS combined arms workspace is complete, accurate, and accessible before execution begins. Every data gap identified during preparation is a potential synchronization failure during execution.

Preparation is the right time to test workspace access — confirm subordinate S3 sections can see the right layers, brigade can see the right products, and aviation and fires sections have the appropriate access to the workspace. Discovering access problems during execution is operationally costly. Discovering them during RSOI or pre-operations checks is routine.

### 3-3. Execute — The Data Cycle During Operations

During execution, the operations process accelerates. ADP 5-0 describes execution as applying combat power to accomplish the mission through action — and the role of the staff during execution is to maintain the commander's situational awareness and support decision-making (ADP 5-0, para 1-27).

In MSS terms, execution converts the operations process into a continuous data maintenance task: reports arrive, are evaluated, and are entered into MSS; MSS provides the current picture; the commander assesses the picture and makes decisions; FRAGOs are generated; and the cycle restarts. The S3 section that can sustain this cycle at operational tempo — maintaining MSS currency within established standards while simultaneously managing voice reporting, coordinating with fires and aviation, and supporting the battle captain — has achieved the operational utility of MSS for maneuver.

The staff that slows to update MSS during high-intensity execution moments — when the most data is arriving and decisions are most urgent — has not integrated MSS into operational culture. It has added MSS as an administrative burden. This failure mode is addressed in Section 7.

### 3-4. Assess — The Continuous Assessment Data Layer

Assessment in the operations process is the deliberate comparison of progress toward desired conditions against the current situation (ADP 5-0, para 1-58). For M&M practitioners, assessment centers on:

- Are maneuver forces achieving their objectives on timeline?
- Is the friendly force's combat power enabling continued operations?
- Are mobility corridors open for logistical resupply and reinforcement?
- Are reconnaissance and security forces producing information that answers PIRs?

Each of these assessment questions has a data answer that MSS can provide — if the data is current. The M&M practitioner who builds assessment products from MSS data is drawing on the integrated picture of objective status, combat power, route status, and reconnaissance progress simultaneously. This is the assessment advantage of MSS over legacy tools.

> **NOTE: Assessment in ADP 5-0 is a command-and-staff function, not a platform function. MSS provides data for assessment — it does not conduct assessment. The staff officer who presents a readiness dashboard to the commander without analysis has not assessed anything. The dashboard is an input. The assessment is the interpretation of what the data means for the mission.**

---

## SECTION 4 — TERRAIN AND MOBILITY AS DATA

**BLUF:** Terrain analysis and mobility assessment are among the oldest military staff functions — but they have historically produced static products that become inaccurate as conditions change. MSS converts terrain and mobility into dynamic data — updated as reconnaissance reports arrive, as obstacle conditions change, and as engineer assessments are completed.

### 4-1. OAKOC as a Data Framework

The OAKOC terrain analysis framework (Observation, Avenues of approach, Key terrain, Obstacles, Cover and concealment — ADP 3-90, para 2-5) was designed for map analysis. In MSS, each OAKOC factor becomes a data layer with associated reporting standards and update triggers.

**Observation and fields of fire** depend on knowing where observation posts are, what they can see, and what dead ground exists between friendly positions and the likely enemy approach. This is OP/LP data, combined with terrain data. In MSS, the observation layer integrates OP positions, observation sectors, and dead ground analysis — but only when the S2 and S3 sections actively maintain it. An OP that has been overrun or displaced but not updated in MSS continues to show as "occupied" — creating a false sense of security in the observation network.

**Avenues of approach** are route analysis — the S3 section's primary route data maintenance task. The avenue of approach picture in MSS is only as accurate as the route classification data, obstacle reports, and bridge classifications loaded into the system. An avenue of approach that appears clear on MSS but has an unreported vehicle obstacle at a choke point is a doctrinal avenue of approach that is tactically closed.

**Key terrain** in MSS is identified as named graphic objects. The operational problem is ensuring that the organization agrees on what constitutes key terrain before operations begin — and that terrain features gain or lose key terrain designation as the operational situation changes. Key terrain that was essential in Phase I may be irrelevant in Phase III; failing to update the designation creates false prioritization in the combined arms picture.

**Obstacles** are the most time-sensitive element of the OAKOC picture. Obstacle conditions change: minefields are breached, road craters are filled, wire is cut, new FASCAM strikes occur. The S3 section's obligation is to ensure the obstacle layer in MSS reflects the most current reported obstacle picture — not the picture at operation start.

**Cover and concealment** data in MSS is largely static — it reflects terrain features and urban structures that provide concealment. The dynamic element is unit reporting of effective cover and concealment in actual operating conditions, which supplements the static map data.

### 4-2. Engineer Data as the Mobility Decision Layer

The engineer staff section (12A officer, 12B section) is the primary source of mobility data in MSS. The S3 section integrates this data but does not own it. This distinction matters.

When route status changes — a bridge is damaged, a ford site is found, a new minefield is reported — the engineer section updates MSS. The S3 section receives the update, integrates it into the maneuver picture, and adjusts plans accordingly. When the S3 section attempts to maintain the mobility picture without engineer input, the result is route data that reflects maneuver assumptions rather than engineering reality — which is operationally dangerous.

The institutional discipline to maintain the engineer-S3 data relationship — with the engineer section owning and updating mobility data, and the S3 integrating it — is a professional staff behavior that must be enforced by the XO and S3.

### 4-3. The Route Status Decision Chain

Route status decisions — open, restricted, closed — have direct operational consequences. A route declared open in MSS will be used by units that trust the display. If the display is wrong, the consequences range from vehicle damage to route compromise to personnel casualties.

The decision chain for route status in MSS should be:

1. Reconnaissance or patrol reports route status change to S3 via voice/digital.
2. Engineer section evaluates military significance (bridge MLC change, obstacle impact on vehicle types, etc.).
3. S3 section updates MSS route status with engineer concurrence.
4. S3 notifies affected units of the route status change.

A route status change that enters MSS without engineer concurrence — made by an S3 NCO acting on a single voice report — may be correct or may reflect incomplete reporting. The engineer concurrence step reduces the risk of acting on a single source. This procedural discipline must be trained, not assumed.

---

## SECTION 5 — RECONNAISSANCE AND THE INFORMATION REQUIREMENT

**BLUF:** FM 3-98 describes reconnaissance as the task of obtaining, by visual observation or other detection methods, information about the activities and resources of an enemy (FM 3-98, para 1-1). Reconnaissance products are the primary input to the maneuver commander's intelligence requirement (IR) and priority intelligence requirement (PIR). MSS integrates reconnaissance products into the combined arms picture and provides the mechanism for continuous PIR tracking.

### 5-1. PIRs and IRs as MSS Data Management Drivers

The commander's PIRs drive the reconnaissance and security effort. PIRs define what information the commander needs to make a specific decision (FM 6-0, para 9-4). In MSS, PIRs should be loaded as named requirements, associated with the reconnaissance objectives tasked to answer them, and tracked against the reporting timeline.

The failure mode — common in USAREUR-AF exercises — is that PIRs are briefed at the beginning of planning and then drift. The reconnaissance effort produces information; that information goes to the S2; but the S3 section never confirms whether the PIR was answered. The maneuver commander makes a decision based on incomplete PIR satisfaction and does not know it.

MSS addresses this by keeping PIRs visible alongside reconnaissance status. When reconnaissance objective 1 (tasked to answer PIR 1) shows status "complete — reporting," the S3 section and S2 can confirm whether the report actually answered the PIR or whether the information was incomplete. If incomplete, a follow-on reconnaissance task must be generated immediately — not at the next battle rhythm event.

### 5-2. Named Areas of Interest and Targeted Areas of Interest

Named areas of interest (NAIs) are geographic locations where activity or lack of activity will answer a PIR (FM 3-98, para 1-11). Targeted areas of interest (TAIs) are locations where enemy forces are expected and where fires or maneuver can be employed to affect them.

NAIs are reconnaissance data. TAIs are targeting data. In MSS, both are displayed as graphic overlays — but they serve different functions and must not be conflated.

An NAI that shows enemy activity confirmed by reconnaissance transitions to a targeting input — the S3 and S2 must coordinate the handoff of that information to the fires officer for targeting development. MSS does not do this automatically. The staff discipline to recognize when an NAI has produced intelligence that requires a targeting action — and to execute the coordination — is a human function.

### 5-3. Reconnaissance Pull vs. Intelligence Push

FM 3-98 describes two reconnaissance concepts: reconnaissance pull and intelligence push (FM 3-98, para 1-9). Reconnaissance pull means the commander directly controls reconnaissance assets to answer specific questions. Intelligence push means the intelligence system provides products based on assessed enemy courses of action.

MSS integrates both: the S2 section maintains enemy situation overlays (intelligence push), and the S3 section tracks reconnaissance objective status (reconnaissance pull). The practical challenge is ensuring both layers are visible in the same workspace and are updated with equivalent discipline. An S3 section that maintains current reconnaissance status but displays a stale enemy overlay from two days ago has a combined arms workspace that creates false confidence — the friendly reconnaissance picture appears comprehensive while the underlying intelligence basis is outdated.

---

## SECTION 6 — BLUE FORCE TRACKING AND THE COMMON OPERATIONAL PICTURE

**BLUF:** Blue Force Tracking (BFT) provides the maneuver commander a persistent, updated picture of friendly force positions. It is the most operationally powerful data layer in the M&M workspace — and the most dangerous if misread. The tension between location accuracy and operational security is the fundamental BFT management challenge.

### 6-1. What BFT Represents — and What It Does Not

BFT in MSS displays the last reported position of each tracked unit as of the most recent update. It does not display current position. It does not predict future position. The distinction matters operationally.

A unit displayed at grid 354 278 in MSS BFT was at that location when it last updated — which may be 30 seconds ago or 8 minutes ago, depending on the system update interval and communications status. During active combat, especially in urban terrain or areas with degraded comms, that difference can represent significant position change. Using BFT without accounting for update intervals in a fires deconfliction or passage of lines scenario introduces risk.

The operational standard is: always note the "last updated" timestamp for any unit before using its BFT position for a time-sensitive coordination task. When the timestamp is outside the unit's normal update interval, assume the unit has moved and confirm by voice.

### 6-2. The Common Operational Picture and Its Limits

The COP is the single display of relevant information shared by more than one command (FM 6-0, para 11-14). MSS enables a persistent COP across echelons — the division commander and the battalion S3 can look at the same workspace simultaneously. This is a genuine capability improvement over the era of disconnected map boards.

But the COP is not the same as situational awareness. The COP is the shared data display. Situational awareness is the commander's or staff officer's understanding of the current situation built from the COP data and from all other information sources — voice reports, liaison officers, observation, and judgment.

A staff section that achieves COP access — everyone can see the workspace — without achieving situational awareness has accomplished the technical task and failed the operational one. The COP is a means, not an end. The end is a commander who understands what is happening well enough to make sound decisions.

### 6-3. OPSEC and the Force Tracking Tension

BFT and the shared COP create a structural OPSEC tension: the same visibility that enables friendly force coordination also represents a significant intelligence target if the platform is compromised or its data is exfiltrated.

The operational rule for M&M practitioners is: the COP is shared as widely as operational necessity requires — and no further. Units and personnel who do not need to see the combined arms workspace should not have access to it. Operational graphics, BFT data, and route status information are operationally sensitive. The fact that MSS stores this data in an enterprise platform does not reduce its sensitivity — it concentrates it.

Coordinate with the S6 and IMO for appropriate access controls on M&M workspaces. Review workspace access lists at the start of each operation and after any significant change in the personnel with workspace access.

> **NOTE: OPSEC for MSS data is not an S6 function — it is an S3 function with S6 technical support. The S3 section owns what data is displayed, who can see it, and what products are exported from MSS. The S6 provides the technical access controls. The S3 directs them.**

---

## SECTION 7 — M&M FAILURE MODES IN MSS

**BLUF:** USAREUR-AF exercises and operational experience identify eight recurring failure modes for M&M practitioners using MSS. Most failures are not technical — they are disciplinary. The platform works; the staff practice does not.

### Failure Mode 1: Stale Graphics Left Uncorrected After FRAGO

**What it looks like:** The operational workspace displays phase lines and objectives from the previous OPORD. A FRAGO modified two boundary lines and added a new phase line three hours ago. The MSS workspace still shows the original graphics.

**Why it happens:** The S3 section is managing voice reporting, coordinating with fires, and supporting the battle captain. Updating MSS graphics after every FRAGO requires a dedicated operator focus that the section cannot sustain without deliberate task assignment.

**Consequence:** Subordinate S3 sections and the brigade commander are looking at the wrong operational picture. Fires deconfliction, passage of lines coordination, and boundary management are conducted against incorrect graphic references. Fratricide risk increases.

**Standard:** Assign one operator in the S3 section as the primary MSS maintainer during execution. FRAGO graphics are updated within 30 minutes of FRAGO receipt — every time, without exception.

---

### Failure Mode 2: Incorrect Symbology on Tactical Graphics

**What it looks like:** An engineer minefield is loaded as a blue (friendly) obstacle when it is an enemy minefield, or vice versa. A no-fire area uses the wrong symbol type. Friendly unit icons appear as enemy icons due to symbology selection errors.

**Why it happens:** MSS symbology selection during graphic loading requires the operator to select the correct symbol from the MIL-STD-2525D library. Operators who are not trained in military symbology make symbol selection errors, particularly under time pressure.

**Consequence:** Fires coordination failures from incorrect FSCM symbology. Route planning errors from swapped obstacle symbology. Fratricide risk from incorrect unit symbology.

**Standard:** Every graphic loaded into the combined arms workspace is reviewed by a second operator before publishing. All personnel who load graphics into MSS must complete symbology training as a prerequisite.

---

### Failure Mode 3: Routing Around Reports — Using Stale Data Selectively

**What it looks like:** A unit is planning a route that MSS shows as "open." An engineer OBSREP from two hours ago identified a new obstacle on that route. The OBSREP data has not been entered into MSS. The planner uses MSS to confirm the route is open without checking engineer reporting channels.

**Why it happens:** MSS is the path of least resistance. If the workspace shows a route as open, planners trust it — particularly under time pressure. Checking the engineer section for additional reports requires coordination effort.

**Consequence:** A unit routes onto a route with an unreported obstacle. The consequences range from mission delay to vehicle damage to enemy contact at a choke point.

**Standard:** Before using route status data from MSS for execution, confirm with the engineer section whether any reports have been received that have not yet been entered. The MSS display is a snapshot of entered data — it is not a real-time sensor of ground conditions.

---

### Failure Mode 4: Using BFT Without Checking Update Timestamps

**What it looks like:** During a FRAGO coordination, the S3 uses a unit's MSS BFT position to determine whether the unit is clear of a boundary change. The BFT position is 12 minutes old. The unit has moved 2 kilometers since its last update. The boundary change is made based on an incorrect position.

**Why it happens:** BFT positions display prominently and appear authoritative. The timestamp is smaller and requires deliberate attention to read.

**Consequence:** Fires coordination error from a boundary based on a stale position. Passage of lines coordination failure from an inaccurate friendly unit position reference.

**Standard:** Every use of BFT for a time-sensitive coordination task requires a verbal or visual check of the last-updated timestamp. If the timestamp is outside the unit's normal update interval, confirm position by voice before proceeding.

---

### Failure Mode 5: Platform Dependency — Inability to Track Without MSS

**What it looks like:** MSS goes offline during a training exercise. The S3 section cannot produce a current ground picture within 30 minutes. The paper maps do not have current graphics. The battle captain cannot brief the commander from manual tracking records.

**Why it happens:** As MSS adoption increases, manual battle tracking skills atrophy. S3 sections that rely on MSS for every tracking function do not maintain the backup procedures and physical materials required for degraded operations.

**Consequence:** An S3 section unable to sustain situational awareness during MSS outage is operationally non-functional for the duration of the outage. In a contested environment where network outages are expected, this is an unacceptable capability gap.

**Standard:** Conduct quarterly degraded operations training with no MSS access. Evaluate S3 section ability to maintain a current ground picture on paper within 30 minutes of simulated MSS outage.

---

### Failure Mode 6: Confusing "Reported" With "Current"

**What it looks like:** The S3 briefs the commander: "Sir, 2-5 Cav is on screen line at Phase Line COBRA, and 2nd Brigade has no obstacles reported on MSR TAMPA." Both statements are accurate as of the last MSS update — which was three hours ago, at the start of the battle rhythm cycle.

**Why it happens:** MSS data is persistent and visually authoritative. It is easy to present what the platform displays as if it represents current conditions rather than the last reported conditions.

**Consequence:** Commander makes decisions based on a situation that may be significantly different from what is displayed. The confidence of the MSS display masks the potential for significant information lag.

**Standard:** Every MSS-sourced brief must include a data currency statement: "As of [DTG], per MSS — [data element]." Briefing MSS data without a currency reference is a prohibited staff practice.

---

### Failure Mode 7: Treating the Workspace as a Product, Not a Process

**What it looks like:** The S3 section "builds" the MSS workspace before an exercise — loads all graphics, BFT feeds, obstacle overlays — and then treats it as complete. As operations progress, the workspace is not updated. By Day 3, the workspace represents Day 1 conditions.

**Why it happens:** Building the workspace takes effort. The S3 section underestimates the effort required to maintain it under operational conditions. The workspace is perceived as a product rather than a continuous process.

**Consequence:** The workspace diverges from ground reality as operations progress. By the time the divergence is recognized, significant rework is required — and the window in which the data was accurate has closed.

**Standard:** MSS workspace maintenance is a continuous task, not a one-time setup action. Every battle rhythm cycle must include a dedicated MSS review and update period. The XO ensures the S3 section has a dedicated operator assigned to workspace maintenance throughout execution.

---

### Failure Mode 8: Aviation and Fires Graphic Layers Not Maintained

**What it looks like:** The fires officer updated the no-fire area graphic to reflect a new NGO facility added to the protected site list. The change was made in the fires officer's workspace but not synchronized to the combined arms workspace visible to the S3 section. The S3 plans a route for an assault force that passes through the new NFA.

**Why it happens:** Cross-section graphic synchronization requires deliberate coordination. The fires officer updates the fires layer; the S3 section does not see the update unless they actively pull it or unless the workspace is configured for automatic synchronization.

**Consequence:** Maneuver plan violates a fire support coordination measure the maneuver element did not know existed. The consequence ranges from a fires restriction that delays the mission to a LOAC violation if fires are cleared against a protected site.

**Standard:** Every FSCM change must be immediately communicated to the S3 section via primary means — not only updated in the fires workspace. The S3 section confirms the change is reflected in the combined arms workspace. Cross-section graphic updates require acknowledgment — a push to the workspace is not confirmation that the S3 section has seen and integrated the change.

---

## SECTION 6 (CONTINUED) — THE ECHELON DIMENSION OF THE COP

### 6-4. What Each Echelon Needs from the COP

The COP serves different functions at different echelons. Understanding this distinction prevents one of the most common MSS configuration errors — building a single workspace that attempts to serve every echelon simultaneously and ends up serving none well.

**Company/Troop Level.** The company commander needs to see the battalion operational graphics (phase lines, objectives, boundaries), the BFT display of friendly positions in the AO, and the route status for routes the company will use. The company commander does not need — and should not have — write access to the battalion combined arms workspace. A read-only view with the relevant layers is the appropriate configuration.

**Battalion Level.** The battalion S3 section needs the full combined arms workspace with write access: operational graphics, BFT, fires layer (FSCM), engineer/route/obstacle layer, and aviation layer. The battalion S3 is the primary maintainer of the battalion workspace and the primary consumer of the integrated combined arms picture.

**BCT Level.** The BCT S3/G3 section needs visibility into all three battalion workspaces simultaneously — not to manage battalion-level data, but to see the battalion pictures in aggregate. BCT-level MSS products are derivatives of battalion-level data: the BCT combat power assessment draws on all three battalion readiness pictures; the BCT operational picture integrates all three battalion AOs into the brigade boundary display.

**Division/Corps Level.** At division and corps, the operational picture is too broad for tactical-graphic maintenance. Division/corps S3 sections use MSS to track phase status across multiple BCTs, monitor main-effort combat power, and assess operational conditions. They do not maintain tactical graphics — they consume the products maintained by BCT S3 sections.

> **NOTE: A workspace that meets the needs of every echelon simultaneously is usually too cluttered to be useful at any echelon. Build echelon-appropriate workspaces with appropriate access controls. The battalion workspace is not the brigade workspace — it is an input to the brigade workspace.**

---

## SECTION 7 (CONTINUED) — ADDITIONAL CONSIDERATIONS FOR LEADERS

### The M&M Data Culture Problem

The eight failure modes described in Section 7 have a common root: M&M practitioners do not yet have a data culture that treats MSS maintenance as an operational task equivalent in importance to voice reporting, battle captain functions, and fires coordination.

This is not a criticism of individuals — it reflects the recency of MSS adoption. Units have operated for generations with paper maps, acetate overlays, and periodic voice reporting. The introduction of MSS does not eliminate those practices overnight. What it does is add a new maintenance requirement without always adding the time and personnel to sustain it.

The leader's challenge is to reframe MSS maintenance from "an additional administrative burden" to "a core staff function that enables everything else." A BUA where the commander can read the current combined arms picture from a well-maintained MSS workspace is a better BUA than one where the staff brings a manually compiled slide with data pulled from four systems this morning. But achieving that BUA requires the staff work — the continuous update discipline — that makes the workspace trustworthy.

**Three Leader Actions That Create M&M Data Culture:**

**First — hold the workspace to a standard.** If the S3 brief references MSS data, the commander should occasionally ask: when was this last updated? What is the source? If the S3 section cannot answer quickly and accurately, the standard is not being met.

**Second — train degraded operations with equal rigor.** A unit that trains exclusively with MSS creates platform dependency that is operationally dangerous in a contested environment. Quarterly degraded-mode exercises where the S3 section must sustain situational awareness without MSS access are not optional — they are a training requirement.

**Third — make data maintenance a battle rhythm task, not a residual task.** The S3 section's battle rhythm should include dedicated MSS update periods — not "update MSS when you get a chance" but "update MSS as a specified task at specified intervals." The XO ensures the time is protected. The S3 NCOIC ensures the standard is met.

---

### The Integration Requirement: S3 and S2 Coordination for M&M MSS

The movement and maneuver picture in MSS is incomplete without the intelligence picture. A combined arms workspace that shows friendly force positions, operational graphics, and route status — but not the current enemy situation — gives the commander an incomplete operational picture.

The S3 and S2 sections must maintain coordinated workspaces. The mechanics vary by unit configuration, but the principle is constant: the S3 combined arms workspace must have read-access to the S2 intelligence overlays. The S2 must have read-access to the S3 operational graphics. Neither section can maintain a useful operational picture in isolation from the other.

The most important coordination point is reconnaissance reporting. When the 19D cavalry section reports a reconnaissance finding — enemy vehicle at grid, obstacle confirmed at bridge site, route clear to Phase Line COBRA — that report serves both the S2 (intelligence value) and the S3 (maneuver planning value). It must be entered into MSS in a way that is visible to both sections. The unit SOP must define who enters reconnaissance reports, under what timeline standard, and in which workspace layer.

### The Concept of "Data Ownership" in M&M Operations

One of the persistent coordination problems in MSS M&M employment is data ownership ambiguity. Who is responsible for updating the obstacle layer when a patrol reports a new minefield? Who updates route status after a route clearance report? Who corrects a reconnaissance objective status when the cavalry troop reports completion?

The doctrinal answer is clear: the section that owns the warfighting function task owns the data. Engineers own obstacle data. The S2 owns enemy situation data. The FSO owns fires graphics. The S3 section owns operational graphics and coordinates everything into the combined arms workspace.

The practical challenge is that data ownership requires data discipline. The engineer section must update the obstacle layer the same way the S3 section updates operational graphics — not as a residual task when time permits, but as a specified staff function with a time standard. The FSO must update FSCM graphics with the same urgency as voice notification of fires changes. The S2 must update the enemy overlay with the same rigor used to brief the commander.

When any section treats MSS data maintenance as a secondary task — something done after the "real" work is complete — the combined arms workspace degrades. The section that enters data late is not harming only its own work. It is degrading the operational picture that the S3, the commander, the battle captain, and every other section depends on for decision-making.

The XO is the right officer to enforce cross-section MSS data standards. The XO has authority across all staff sections and is accountable for staff integration. An XO who holds every section to the MSS data standards — not just the S3 section — creates the conditions for a trustworthy combined arms workspace.

### The Relationship Between MSS Proficiency and Tactical Proficiency

There is a tension that experienced S3 officers recognize: investing time in MSS training and data maintenance competes with time available for tactical planning, coordination, rehearsals, and leader development. The unit that spends six hours per week in MSS familiarization training at the expense of squad and platoon battle drills has made a poor resource allocation decision.

The resolution to this tension is not to reduce MSS investment — it is to integrate MSS training into tactical training rather than treating them as competing activities. A battle staff exercise that runs with full MSS employment provides both tactical staff training and MSS proficiency simultaneously. A route reconnaissance that requires the engineer section to submit a correctly formatted OBSREP into MSS develops both reconnaissance skills and data entry discipline. A BCT CPX that includes a degraded operations period — where MSS goes down for four hours in the middle of execution — tests tactical problem-solving and backup procedures simultaneously.

The best MSS training is operational training conducted with MSS as the primary information management tool. The goal is not "MSS training" and "tactical training" as separate events — it is operationally realistic training where MSS is employed as it would be in actual operations.

### The Doctrinal Justification: Why This Matters at USAREUR-AF

USAREUR-AF operates in a mature theater — large formation operations, multinational coordination, extensive pre-positioned infrastructure — but against a peer-level threat that contests the information environment deliberately. In a peer-contested environment, the information advantage that MSS provides is not guaranteed. It must be earned through operational and informational security, network resilience, and the staff discipline to maintain accurate data under degraded conditions.

The M&M practitioner who understands why MSS works — and why it fails — is better equipped to sustain the operational advantage it provides than one who has only learned the mechanics of loading graphics and reading dashboards. Doctrine, platform capability, and staff discipline are all required. None is sufficient alone.

### 6-5. The Adversary's View of Your COP

A final dimension of BFT and COP management that is easy to overlook in training environments but critical in real operations: the adversary is actively working to understand your operational picture. The COP that MSS provides is a target — not just a tool.

A sophisticated adversary with access to signals intelligence, cyber exploitation capabilities, or insider access can potentially see what is displayed in your MSS workspace. This is not a reason to stop using MSS — it is a reason to use it with appropriate OPSEC discipline.

The OPSEC calculus for MSS is: the operational advantage of a shared, current, integrated COP outweighs the risk of adversary access to it, provided OPSEC measures are implemented. Those measures include: appropriate access controls, classification handling, limiting COP exports and screenshots, and avoiding routine patterns of data access that could reveal operational timing.

The S3 section does not manage this alone. The S6 provides technical security. The OPSEC officer provides policy guidance. The unit's intelligence officer monitors for adversary collection against the unit's information systems. What the S3 section contributes is the operational discipline to follow OPSEC guidelines for MSS use — because the operational advantage of the platform is only preserved if the adversary cannot exploit it.

> **NOTE: OPSEC for MSS is not a separate plan or annex. It is a continuous behavior integrated into every MSS operation. Checking access controls before sharing a workspace takes 30 seconds. The operational cost of a compromised COP is not recoverable.**

ADP 3-0 provides the doctrinal framework. MSS provides the platform capability. TM-40C provides the procedural guidance. This Concepts Guide provides the "why" behind both. The unit's investment in training all three dimensions determines whether MSS becomes a genuine operational advantage or an expensive administrative layer.

### A Note on the Peer Threat Context

USAREUR-AF's operating environment is defined by potential peer-level adversaries who contest every dimension of operations — including the information environment. A peer adversary has the capability to degrade networks, disrupt GPS-dependent systems, and contest the electromagnetic spectrum that MSS communications traverse.

This context shapes how M&M practitioners must think about MSS. In permissive network environments (exercises, garrison operations), MSS provides continuous, reliable operational advantage. In a peer-contested environment, that advantage is intermittent — available when networks are intact, degraded when they are not. The doctrine, training, and staff discipline required for effective MSS employment must therefore account for the contested environment as the baseline condition, not the exception.

The M&M practitioner who is fully proficient on MSS but has no backup capability has trained for the permissive environment. The M&M practitioner who maintains full backup capability and integrates MSS as the primary tool when networks are available has prepared for the actual USAREUR-AF operational environment.

This is the synthesis of everything in this Concepts Guide: MSS is a powerful enabler, but the unit's capability cannot depend on MSS. The platform should accelerate and enhance staff functions that the unit can perform without it. The unit that achieves this standard is operationally resilient — capable in the full-capability environment, capable in the degraded environment, and never caught operationally blind because a network was contested.

---

### The Senior Leader's Role in MSS M&M Culture

Brigade and battalion commanders set the culture for MSS employment. When the commander references MSS data during the BUA and asks "when was this updated?" — the section develops data currency discipline. When the commander accepts stale briefings without questioning the timestamp, the section learns that currency is optional.

Three commander behaviors directly shape MSS M&M culture:

**First — brief from the workspace, not from slides built from the workspace.** When the S3 briefs the ground situation from a printed screenshot taken two hours ago, the commander is not seeing a current picture. When the S3 briefs from the live workspace, the commander sees what the platform knows right now. The difference in information quality is significant; the commander's preference drives which approach the section uses.

**Second — enforce the data currency standard publicly.** When a stale data point is identified during a brief, the right response is: "When was this last updated? Why hasn't it been updated? Let's fix it before we continue." This response, repeated consistently, produces a section that updates data before it becomes stale — because the cost of a stale brief is visible and immediate.

**Third — conduct degraded operations training without advance notice.** An announced degraded operations exercise allows the section to prepare. An unannounced one tests the actual capability. Commanders who occasionally direct "MSS is down — work from manual tracking" during exercises find out quickly whether their section has a real backup capability or an aspirational one.

---

## CLOSING NOTE FOR LEADERS

The eight failure modes in Section 7 are not technology problems. They are organizational discipline problems — staff practices that must be established, rehearsed, and enforced by leaders. MSS is a powerful enabler for M&M operations, but it requires the same institutional discipline as any other critical staff function.

The standard for MSS employment in M&M operations is simple to state and demanding to sustain: the combined arms workspace must reflect the current situation — not the planned situation, not this morning's situation, not what the previous shift built. It must reflect the current situation, updated within established standards, accessible to every echelon that needs it.

Units that achieve this standard have converted MSS from an administrative tool into an operational advantage. Units that do not have added a maintenance burden to an already demanding staff workload without achieving the situational awareness gain the platform is designed to provide.

The S3 section sets the standard. The XO enforces it. The commander demands it.

**A final note on organizational learning.** The most effective M&M MSS units in USAREUR-AF exercises are not the ones with the most technically sophisticated workspaces. They are the ones where the S3 section has internalized a simple discipline: when information arrives, it goes into the workspace. When conditions change, the workspace changes. When MSS goes down, the section keeps tracking by hand. This discipline — simple in statement, demanding in execution — is the foundation of effective M&M MSS employment.

Build the discipline first. The platform capabilities follow naturally when the discipline is present. Without the discipline, even the most capable platform configuration produces a workspace that is stale by noon, unreliable by the next day, and operationally dangerous by the second week of sustained operations.

Every S3 section in USAREUR-AF is capable of the discipline. The question is whether leadership demands it consistently enough to make it a habit. That is the leader's task. The platform is ready. The doctrine is clear. The standard is set.

---

## DOCTRINAL REFERENCES SUMMARY

| Publication | Relevance to M&M MSS |
|---|---|
| ADP 3-0, Operations | Combined arms concept, tempo, initiative, operational principles |
| ADP 3-90, Offense and Defense | OAKOC, M&M tasks, offensive and defensive fundamentals |
| ADP 5-0, The Operations Process | Plan/prepare/execute/assess cycle; assessment framework |
| ADP 6-0, Mission Command | Shared understanding; commander's intent; disciplined initiative |
| FM 3-0, Operations | Combined arms integration, M&M WFF tasks |
| FM 3-90, Offense and Defense (May 2023) | Offensive and defensive control measures, passages of lines, reconnaissance, security, tactical enabling tasks |
| FM 3-98, Reconnaissance and Security Operations | PIR/IR framework, reconnaissance fundamentals |
| FM 5-0, Planning and Orders Production | MDMP, orders, assessment products |
| FM 6-0, Commander and Staff Organization | Staff roles, battle rhythm, CCIRs |
| ATP 3-04.94, Brigade Aviation Element | Aviation-maneuver coordination, air corridor procedures |
| ATP 3-90.8, Combined Arms Breaching Operations | SOSRA sequence, breach task organization |
| ADP 3-07, Stability | Stability operations, lines of effort, civil considerations |
| FM 3-96, Brigade Combat Team | BCT organization, combined arms integration at brigade |

Practitioners are encouraged to read the doctrinal publications relevant to their primary duty position alongside TM-40C. Doctrine provides the why; TM-40C provides the how. Both are required for competent M&M MSS employment.

---

## RELATED TRACKS AND PUBLICATIONS

### WFF Peer Tracks

All six WFF tracks are at the same tier. All six WFF tracks require TM-10, TM-20, and TM-30 as prerequisites. M&M practitioners are encouraged to develop working awareness of TM-40A (Intelligence) and TM-40F (Mission Command) — the two WFF tracks with the most intensive M&M data integration.

| Track | Title | Prereq | Relationship to M&M WFF |
|-------|-------|--------|------------------------|
| TM-40A | Intelligence WFF | TM-10 + TM-20 + TM-30 | NAI/TAI overlays, PIR/IR supporting reconnaissance planning |
| TM-40B | Fires WFF | TM-10 + TM-20 + TM-30 | FSCM management, airspace deconfliction, maneuver-fires synchronization |
| TM-40C | Movement and Maneuver WFF | TM-10 + TM-20 + TM-30 | This track |
| TM-40D | Sustainment WFF | TM-10 + TM-20 + TM-30 | Route capacity, maneuver unit readiness, supply constraints on COA |
| TM-40E | Protection WFF | TM-10 + TM-20 + TM-30 | Physical security integration, NBC threat overlays |
| TM-40F | Mission Command WFF | TM-10 + TM-20 + TM-30 | Combined arms COP, CCIR thresholds for maneuver decision points |

### Specialist Tracks (Prerequisite: TM-30)

For personnel pursuing technical depth, specialist tracks (TM-40G–O, prereq TM-30) are available. Not required for M&M WFF employment.

| Track | Title |
|-------|-------|
| TM-40G | ORSA (→ TM-50G) |
| TM-40H | AI Engineer (→ TM-50H) |
| TM-40M | ML Engineer (→ TM-50M) |
| TM-40J | Program Manager (→ TM-50J) |
| TM-40K | Knowledge Manager (→ TM-50K) |
| TM-40L | Software Engineer (→ TM-50L) |

---

*CONCEPTS GUIDE — TM-40C COMPANION: MOVEMENT AND MANEUVER WARFIGHTING FUNCTION*
*Version 1.0 — March 2026*
> **NOTE — New Doctrine Content in TM-40C:** TM-40C now includes PMESII-PT/METT-TC(I) data frameworks with the 2025 "I" (Informational) addition (section 2-1a), force ratio calculations with combat power CAUTION (section 8-4a), scheme of maneuver as geospatial data (section 5-2a), and reconnaissance as data collection (section 4-4a, FM 3-98). These sections ground M&M data management in their authoritative doctrinal sources.

*HEADQUARTERS, UNITED STATES ARMY EUROPE AND AFRICA — Wiesbaden, Germany*
*DISTRIBUTION RESTRICTION: Distribution authorized to U.S. Government agencies and their contractors only. Other requests must be referred to Headquarters, C2DAO, Wiesbaden, Germany.*
