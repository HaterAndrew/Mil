# CONCEPTS GUIDE — TM-40D COMPANION — SUSTAINMENT WARFIGHTING FUNCTION · MAVEN SMART SYSTEM (MSS)

> **Forward:** ADP 4-0 defines sustainment through six functional elements and eight principles. Each element generates data. That data, historically fragmented across incompatible systems, is what MSS integrates. Understanding why MSS was built requires understanding the information problem that existed before it.
> **Prereqs:** This guide must be read before beginning TM-40D. TM-10 (Maven User), TM-20 (Builder), and TM-30 (Advanced Builder) are required before beginning TM-40D. Reading this Concepts Guide does not require builder skills, but TM-30 certification must be complete before enrolling in TM-40D.
> **Purpose:** This guide develops the operational mental models required to effectively integrate MSS into Sustainment warfighting function operations. It is a prerequisite companion to TM-40D and must be read before beginning TM-40D task instruction. This guide is conceptual — it develops understanding, not procedures. No step-by-step tasks appear here.
> *HQ USAREUR-AF · v1.0 · 2026 · DISTRIB: USG only*

---

## SECTION 1 — THE SUSTAINMENT WFF AND DATA: ADP 4-0 PRINCIPLES AND MSS REQUIREMENTS

**BLUF:** ADP 4-0 defines sustainment through six functional elements. Each element generates data. That data, historically fragmented across incompatible systems, is what MSS integrates. Understanding why MSS was built requires understanding the information problem that existed before it.

### 1-1. The Sustainment Warfighting Function Is a Data-Intensive Operation

No other warfighting function tracks as many physical objects as sustainment. Bullets, beans, fuel, parts, vehicles, people, water, blood — sustainment is fundamentally an accounting function as much as it is an operational one. Every item in the supply chain must be tracked from requisition to receipt. Every vehicle must be accounted for by status. Every Soldier must be present, sick, or on orders. Every meal must be served and counted.

This is not administrative overhead. This is how an Army sustains itself in contact. A unit that cannot account for its ammunition basic load cannot plan fires. A unit that does not know its Days of Supply for fuel cannot plan tempo. A commander who does not know strength cannot task-organize. The data is the operational picture.

ADP 4-0 describes eight principles of sustainment: integration, anticipation, responsiveness, simplicity, economy, survivability, continuity, and improvisation (ADP 4-0). All eight have direct data implications; the first four are discussed in detail below.

**Integration** means sustainment is synchronized with maneuver. Data integration is what makes this possible — specifically, the ability of the S4 and sustainment commander to see the maneuver picture and for the S3 to see the sustainment picture simultaneously. Before MSS, integration was achieved through battle rhythm events and slide products that were outdated by the time the briefing ended. MSS makes integration continuous.

**Anticipation** means logistics planners predict requirements before they are requested. Anticipation is a data analysis function. It requires trend data: what is consumption rate trending? When will Class IIIB reach the 30% capacity threshold? At current PMCS backlog rates, how many vehicles will be deadlined by the time the operation reaches Phase II? MSS does not do this analysis for the S4 — but it provides the trend data that makes the analysis possible.

**Responsiveness** means delivering the right support, to the right place, at the right time. Responsiveness is degraded when data is slow, incomplete, or siloed. A supply sergeant who does not know that a part was received at the BSB supply point three days ago — because no one updated the requisition status in GCSS-Army — cannot respond. MSS makes requisition pipeline data visible so that the accountability chain does not require manual coordination to maintain.

**Simplicity** means avoiding unnecessary complexity in logistics plans and procedures. MSS supports simplicity by consolidating the sustainment data picture into fewer products, fewer briefs, and fewer data calls. A BSB S4 section that previously managed six Excel trackers for six supply classes can, with MSS properly employed, manage one integrated dashboard. The work does not disappear — but the coordination overhead does.

### 1-2. The Information Problem MSS Solves

Before MSS, the standard sustainment data environment was characterized by three persistent problems.

**Silo fragmentation.** GCSS-Army handled supply transactions. SAMS-E handled maintenance work orders. IPPS-A handled personnel. SAAS-MOD handled ammunition. No system talked to another. The S4 sergeant who needed to compile a LOGSTAT pulled numbers from four systems, reconciled discrepancies manually, and submitted a product whose accuracy was only as good as the last person who entered data into each system. At the BCT level, this happened daily across four to six organic battalions — each with the same fragmented picture.

**Reporting latency.** Even when data was accurate in source systems, it reached decision-makers slowly. A readiness report generated in SAMS-E on Monday morning might not appear in the brigade commander's morning brief until Tuesday, after manual compilation by the BSB S4, formatting by the XO's clerk, and inclusion in the weekly readiness slide. By Tuesday, the Monday data was operationally stale.

**Accountability gaps.** The larger the formation, the wider the gaps. Unit-level data was only as current as the last data call. Companies that submitted their supply status late, maintenance NCOs who forgot to close work orders in SAMS-E, supply sergeants who receipted items in the cage before entering them in GCSS-Army — all created gaps. The LOGSTAT submitted to higher was a mosaic of data of varying currency and accuracy.

MSS does not eliminate these problems by replacing source systems. It reduces them by integrating source data into a visible, continuously-updated picture — and by making data gaps visible rather than hiding them in the compilation process.

### 1-3. The Sustainment Information Environment Before MSS

Understanding MSS's value requires understanding the problem it solved. Before MSS, USAREUR-AF sustainment staffs operated in a fragmented data environment where the full sustainment picture could only be assembled by a human being making a series of phone calls, pulling from multiple disconnected systems, and manually reconciling the results.

A BSB S4 building the brigade LOGSTAT in 2019 would:
- Log into GCSS-Army to pull supply status for each supported battalion
- Log into SAMS-E (or call each unit's maintenance NCO) to get deadline counts
- Call each unit S1 to get PERSTAT numbers
- Call the ASP to get Class V basic load status
- Call the POL sergeant to get fuel status
- Build an Excel spreadsheet to aggregate all of this
- Email the spreadsheet to brigade, where another staff officer would aggregate it with three other BSBs into a brigade product for higher

The entire process took 2–4 hours on a good day. The resulting LOGSTAT was accurate as of the moment each data point was collected — not as of the moment it was submitted. The data was already hours old by the time it was briefed.

MSS compresses this process. When source systems feed MSS correctly, the aggregation is automatic. The BSB S4 navigates to one dashboard and sees all supported units' status simultaneously, continuously updated from source data. The 2–4 hour compilation process becomes a 15-minute validation and analysis process.

The time recovered is not administrative overhead returned. It is analysis capacity restored — time the S4 and sustainment staff can spend on operational problem-solving rather than data compilation.

### 1-4. What MSS Does Not Change

MSS does not change the fundamental nature of sustainment operations. Supply trains must move. Maintenance must be performed. Soldiers must eat. Ammunition must be accounted for.

MSS does not perform sustainment. It informs it. A fuel point that runs dry because the 92F forgot to enter the tank status in MSS is not a data problem — it is a discipline problem. A LOGSTAT that shows 100% basic load when the actual count is 85% is not a platform failure — it is a data-entry failure.

The sustainment unit that understands this distinction will use MSS well. The unit that believes the platform will manage its logistics will be surprised — usually at the worst possible moment.

> **NOTE: Sustainment practitioners who master MSS gain a data-integration advantage that improves every element of their daily work. They also assume a data-stewardship responsibility: the accuracy of the sustainment picture in MSS is a direct function of the accuracy of data entry at unit level. MSS amplifies both good data discipline and poor data discipline.**

### 1-5. The Data Stewardship Obligation

Adoption of MSS creates a data stewardship obligation that did not exist in the legacy environment. When the LOGSTAT was compiled manually, data inaccuracies were caught — at least partially — in the compilation process. A supply sergeant who reported 5 DOS of fuel when the fuel point showed 1.5 DOS would likely be corrected by the BSB S4 during the phone call.

In MSS, data from source systems flows directly into the dashboard without that human correction step. The quality control is automated — and therefore dependent entirely on the quality of the original entry. A 92A who enters incorrect quantities in GCSS-Army at 0700 will see those incorrect quantities in MSS at 0700. The BSB S4 who reviews the dashboard at 0900 may not catch the error unless the GCSS-Army data is reconciled against physical inventory.

This is the data stewardship obligation: every sustainment practitioner who enters data into any source system that feeds MSS is responsible for the accuracy of that entry. The accuracy of the sustainment picture in MSS is a direct function of the data discipline of the formation's supply sergeants, maintenance NCOs, and transportation coordinators. MSS amplifies both good discipline and poor discipline.

Senior sustainment leaders — BSB commanders, G4 sections, sustainment brigade staff — must establish data quality standards and enforce them. The LOGSTAT that is wrong because of sloppy GCSS-Army entry is as dangerous as the LOGSTAT that is wrong because of equipment failure. Both give the commander a false sustainment picture.

---

## SECTION 2 — THE SUPPLY CHAIN AS A DATA PIPELINE: VELOCITY, THROUGHPUT, AND ACCOUNTABILITY

**BLUF:** A supply chain is a pipeline. Like any pipeline, it can be analyzed in terms of velocity (how fast materiel moves), throughput (how much moves), and accountability (what is at each node). MSS makes all three visible simultaneously — which is something no prior sustainment tool achieved.

### 2-1. The Supply Chain Has Multiple Nodes, Each with a Data Signature

Trace a Class IX part from requirement to receipt. A 91A in a company motor pool identifies that an M1A2 needs a fuel injector. The need generates a work order in SAMS-E (Node 1). The 92A submits a GCSS-Army requisition (Node 2). The requisition reaches the BSB supply point, where the part may or may not be on-hand in the PLL (Node 3). If not on-hand, it flows to the Division ASL (Node 4). If not there, it routes to the national-level supply system (Node 5). Eventually, a part arrives and must be receipted and issued (Node 6).

Each node generates data. Each node is a potential point of visibility — or a potential black hole. In the legacy environment, the 91A who submitted the work order had no visibility of the part's location unless someone called someone else. The 92A had no way to check whether the Division ASL had the part without a phone call to the BSB. Latency was built into the system.

On MSS, the requisition pipeline is visible from submission to EDD to receipt. The 91A's work order is linked to the requisition. The S4 can see that B Company has five open NMCS work orders with parts requested but no EDD — which means either the requisition was submitted incorrectly or the supply system has no stock. Both are actionable. Neither would have been visible without a phone call in the legacy environment.

### 2-2. Velocity: How Fast Is the Supply Chain Moving?

Velocity in the supply chain is measured by cycle time — the time elapsed from requirement identification to receipt of materiel. MSS enables cycle time analysis by capturing:

- Requisition submission date/time
- Estimated delivery date (EDD)
- Actual delivery date/time
- Days between submission and receipt (actual cycle time)

A unit with consistently long cycle times for Class IX has a problem somewhere in the supply chain. The problem might be at the unit level (incomplete requisitions, wrong NSNs, wrong priorities). It might be at the BSB (supply point that does not issue promptly). It might be at division (ASL fill rate that is chronically low). Without cycle time data, the S4 can only tell the commander "we have a parts problem." With MSS cycle time data, the S4 can tell the commander "our average cycle time for Class IX is 14 days against a standard of 7, and the bottleneck is at the BSB supply point — 11 of our last 20 requisitions were at the BSB for more than 5 days before onward movement."

That is the difference between data reporting and data analysis. MSS makes the second conversation possible.

### 2-3. Throughput: Is the Supply Chain Moving Enough?

Throughput answers the question: is the supply chain delivering enough to sustain the operation? For fuel, throughput is gallons per day. For rations, it is meals per day. For ammunition, it is rounds by DODIC per day. For repair parts, it is open work orders vs. closed work orders per day.

Throughput analysis requires comparing actual flow to required flow. MSS enables this by displaying on-hand DOS against the consumption rate. When fuel consumption rate exceeds the distribution throughput rate, DOS declines. MSS makes that decline visible before the unit hits a critical threshold — if the data is current.

The commander who sees fuel DOS declining from 5 to 3 to 1.5 over three consecutive days has time to act. The commander who only sees the LOGSTAT at the daily brief, compiled manually from data that may be 12 to 24 hours stale, may not see the decline until it is a crisis.

### 2-4. Accountability: Where Is Everything?

Accountability is the supply chain's most fundamental data requirement. The Army's property accountability system exists because equipment, ammunition, and supplies have monetary value, operational significance, and in the case of ammunition and weapons, safety implications. Property that cannot be accounted for is a command problem, a legal problem, and an operational problem.

MSS contributes to accountability by making property book data visible in context — not as a standalone accounting system, but as an operational picture. A commander who can see that three vehicles in the unit are reflected as "in maintenance float" in MSS can verify that those vehicles are actually at the maintenance activity — not missing. An ammunition officer who can see that a DODIC shows 500 rounds receipted but only 450 in the basic load can identify a documentation discrepancy that requires reconciliation.

Accountability is not automated by MSS. It is made more visible. The work of physical inventory, receipting, and GCSS-Army entry remains — MSS displays the results of that work and makes anomalies easier to identify.

### 2-5. Accountability vs. Visibility

There is a distinction that every sustainment practitioner must internalize before using MSS: the difference between accountability and visibility.

**Accountability** is the legal and regulatory requirement to account for government property, ammunition, and personnel IAW applicable regulations (AR 710-2, AR 700-138, AR 638-8). Accountability is established by physical inventory, signed documentation, and entry in authoritative systems. It carries legal weight.

**Visibility** is the operational picture displayed in MSS — what can be seen at a glance on a dashboard. Visibility is enabled by data entry in source systems and reflects what has been reported, not what has been physically verified.

These two concepts are related but not identical. A supply that is visible in MSS as "on-hand" may not be accountable — if it was never receipted in GCSS-Army. A vehicle that is accountable in GCSS-Army may not be visible in MSS as mission-capable — if the SAMS-E work order closure has not been entered.

The sustainment practitioner who confuses visibility with accountability will eventually encounter a property audit, a FLIPL investigation, or a SAAS-MOD reconciliation that exposes the gap. MSS is a visibility tool. Accountability is established in authoritative systems and through physical inventory. Both are required. Neither replaces the other.

> **NOTE: The test for accountability is always the same: can the unit produce documentation for every line item on its property book, ammunition basic load, and personnel roster? MSS does not change this test. It provides a visibility tool that makes anomalies easier to identify — which, in turn, makes accountability easier to maintain.**

### 2-6. The Risk of Supply Chain Complacency

MSS creates a subtle risk that did not exist in the legacy environment: supply chain complacency. In the legacy environment, the S4 who wanted to know the supply status had to make calls, pull reports, and manually compile data — an active, effortful process. That effort created natural checkpoints where discrepancies were caught.

When MSS is working well, the supply picture is visible with a dashboard click. The S4 checks the dashboard, sees green status across the formation, and moves on. The problem is that "green in MSS" is not the same as "green in reality." Green in MSS means the data that was entered into source systems — at whatever time it was last entered — shows above-threshold status.

A fuel point that ran dry at 1400 but has not been updated in MSS since 0700 will still show 45% capacity in MSS at 1800. A supply sergeant who receipted ammunition at 0900 but did not enter it in SAAS-MOD until 1700 shows below basic load in MSS for eight hours. These are not MSS failures — they are data entry failures that MSS makes visible when they occur and invisible when they do not.

The S4 and sustainment commander who understands this will use MSS as the first look — and treat any status that is critical or unusual as a prompt to verify against the source system and the physical record. The S4 who trusts MSS implicitly will eventually be surprised.

> **NOTE: ADP 4-0's principle of anticipation requires that sustainment planners get ahead of requirements before they become crises (ADP 4-0, para 2-3). A sustainment staff that uses MSS only to confirm current status — and not to project future status from consumption trends — is using the platform reactively, not anticipatorily. The value of MSS for anticipation is in the trend data: DOS declining over three consecutive days is a warning, not a crisis. Act on the warning.**

---

## SECTION 3 — MAINTENANCE READINESS AS A DATA PROBLEM: THE READINESS REPORTING CHAIN

**BLUF:** Equipment readiness is the product of maintenance activity, parts availability, and reporting discipline. All three are data problems. MSS surfaces all three simultaneously — which is why it is a fundamentally more useful readiness tool than the slide-based readiness briefing it replaces.

### 3-1. The Readiness Reporting Chain

The readiness reporting chain flows from vehicle operator (DA Form 5988-E) through the maintenance NCO (SAMS-E work order) through the unit maintenance officer (readiness report) through the S4 (LOGSTAT) through the G4 (DASR/equipment report) to Army Materiel Command. At each step, data is aggregated, errors accumulate, and latency increases.

The typical readiness brief tells a commander what the readiness posture was when the data was last compiled — often 12 to 24 hours before the brief. In a stable garrison environment, 24-hour latency in readiness data is acceptable. In a deployed environment where equipment deadlines directly affect mission execution, it is not.

MSS compresses the readiness reporting chain by pulling SAMS-E data continuously. A work order closed at 1400 on Monday is reflected in the MSS readiness dashboard within hours, not at the next morning's brief. A vehicle deadline entered at 0630 appears in the commander's readiness picture before the 0900 battle rhythm event. The chain still requires human action at each node — the SAMS-E entry must happen — but MSS eliminates the manual compilation steps that created latency between SAMS-E and the readiness picture.

### 3-2. Readiness Has Three Components — MSS Tracks All Three

**Physical readiness: is the equipment working?** SAMS-E records which vehicles are FMC, PMC, or NMC. MSS displays this in real time. This is the most visible component of readiness and the most commonly tracked.

**Parts readiness: can the equipment be fixed?** NMC-Supply (NMCS) means the equipment is deadlined waiting for parts. The unit cannot control how fast the supply system delivers. It can control whether the requisition was submitted correctly, whether the right priority was assigned, and whether the EDD is being tracked. MSS makes the NMCS pipeline visible — number of NMCS vehicles, DODICs on order, EDDs. A maintenance officer who sees 12 NMCS work orders with no EDD entered knows that 12 requisitions either were not submitted or were submitted without tracking information. That is a data problem that becomes a parts problem that becomes a readiness problem.

**Reporting readiness: is the readiness picture accurate?** A unit can have good maintenance discipline and poor reporting discipline simultaneously. If the motor sergeant closes a work order in SAMS-E two days after the vehicle was repaired, the readiness report shows a vehicle as deadlined when it is actually FMC. The reported readiness rate is artificially low. Commanders making task organization decisions based on that product are working from a false picture.

MSS does not solve poor reporting discipline by itself. But it makes the symptoms visible. A SAMS-E / MSS discrepancy — a vehicle showing NMC in MSS that the motor pool sergeant says is FMC — triggers a reconciliation that forces the work order to be closed. Over time, the discipline of maintaining MSS accuracy enforces better SAMS-E entry discipline.

### 3-3. The C-Rating as a Data Product

The equipment C-rating (C-1 through C-4) is a calculated value based on reported FMC percentages (AR 700-138). The C-rating a commander briefs to higher headquarters is only as accurate as the underlying SAMS-E entries.

A unit at C-2 because three vehicles are NMCS is operationally different from a unit at C-2 because three vehicles are scheduled for controlled exchange that has not yet been documented. A unit at C-2 trending upward (parts arriving, repairs being completed) is operationally different from a unit at C-2 trending downward (new deadlines accumulating faster than repairs are completed).

MSS makes this context visible. The readiness dashboard does not just show the C-rating — it shows the breakdown by NMC type, the trend over time, and the parts pipeline that will (or will not) drive recovery. The commander who understands this context makes better task organization decisions than the commander who sees only the C-rating.

### 3-4. The Maintenance Warrant Officer as Data Quality Officer

The 914A and 915A warrant officers occupy a unique position in the maintenance data chain. They are technically proficient enough to evaluate whether a SAMS-E work order is accurate, whether an NMC reason code is correctly applied, and whether an EDD is realistic. They are organizationally positioned to see patterns across multiple units or across time that a single maintenance NCO cannot see.

In the MSS context, the maintenance warrant's analytical role includes monitoring for data anomalies that indicate discipline or accuracy problems:

- A unit with unusually high FMC rates during inspection windows that returns to lower FMC after inspections — possible readiness gaming
- Work orders that are opened and closed on the same day at high frequency — possible data manipulation to meet metrics
- NMCS work orders with no EDD — possible failure to submit requisitions
- Recurring same-system deadlines — possible maintenance procedure deficiency, not just a parts problem

The warrant officer who identifies these patterns and brings them to the maintenance officer's attention is performing exactly the function the Army designed the warrant officer corps to perform. MSS makes these patterns visible. The warrant officer uses technical expertise to interpret what the patterns mean.

### 3-5. Readiness Trend Analysis as Predictive Sustainment

The most powerful application of maintenance readiness data in MSS is not looking at today's C-rating — it is looking at the readiness trend over time and projecting where the unit will be in 7, 14, and 30 days at the current rate of change.

A unit currently at C-2 with a downward trend — deadline count increasing, parts pipeline not keeping pace — will be at C-3 within a week if the trajectory continues. A unit at C-2 with an upward trend — parts arriving, work orders being closed faster than new deadlines are generated — will recover to C-1 before the operation if the trend holds.

The supported commander needs both data points: current status and projected status. MSS provides both when trend data is current. The S4 who brings the trend chart to the commander — "here is where we are, here is where we are going, here is what will change the trajectory" — is adding analytical value that no legacy slide product could provide.

This is the sustainment data analysis standard that TM-40D supports. It is not about using the platform — it is about thinking analytically about what the platform shows.

---

## SECTION 4 — DISTRIBUTION MANAGEMENT MENTAL MODEL: TRANSPORTATION AS THROUGHPUT OPTIMIZATION

**BLUF:** Distribution is a throughput problem. The question is always: given the available trucks, convoys, routes, and time, can the required supplies reach the right units at the right time? MSS makes the variables in that problem visible — which is the first step toward answering it.

### 4-1. The Distribution Problem

The S4's fundamental distribution challenge is matching supply to demand across time and space, using a finite set of transportation assets, over routes with variable availability, against a demand signal that changes with operational tempo.

In a stable garrison environment, this is a scheduling problem. In a deployed environment with enemy action, route closures, vehicle deadlines, and competing unit demands, it is a dynamic optimization problem that requires continuous adjustment.

MSS does not solve the optimization problem. It provides the data that makes solving it possible. An 88N transportation coordinator who can see, on a single screen, which convoys are executing, which routes are open, which vehicles are available for tasking, and which supply points have pending requirements can make faster, better-informed distribution decisions than one who is reconstructing this picture through a series of phone calls and radio checks.

### 4-2. The Three Data Gaps That Degrade Distribution

Three categories of data gaps consistently degrade distribution operations:

**Asset visibility gaps.** The 88N does not know how many vehicles are available because the vehicle status has not been updated since yesterday's PMCS. A convoy is planned for nine vehicles; at execution, two are deadlined. The convoy leaves undermanned or is delayed while the transportation officer reconstructs the asset picture. MSS prevents this gap when vehicle status is updated promptly after every PMCS.

**Route visibility gaps.** A convoy is planned along Route GREEN. During convoy execution, a bridge is closed. The convoy commander has an alternate route — but the home station transportation coordinator does not know about the route change until the convoy is two hours overdue at checkpoint ALPHA. MSS cannot replace real-time communications, but it provides the framework for convoy commanders to record route changes and for coordinators to track checkpoint reporting.

**Demand visibility gaps.** A supply point is planning distribution runs for the next 24 hours. Two units have submitted movement requests in MSS. A third unit submitted its request via email only and did not enter it in MSS. The transportation coordinator plans around two requests; the third unit does not receive resupply on time. MSS is only as complete as the demand signal entered into it. Units that bypass the movement request process create gaps that cannot be managed.

### 4-3. Push Logistics Requires Predictive Data; Pull Logistics Requires Pipeline Data

The push/pull distinction (ADP 4-0, para 2-12) maps directly to two different data requirements in MSS.

Push logistics is anticipatory — the sustainment force delivers supplies before they are requested, based on projected consumption. Making push work requires two data sets: consumption rates (how much did the unit use in the last 24–72 hours?) and planning factors (what is the projected demand for the next operational phase?). MSS consumption trend data feeds the first. The S4's planning factors, loaded into MSS's distribution planning workspace, feed the second.

Pull logistics is responsive — units request what they need, and the sustainment force delivers. Pull requires pipeline visibility: the movement request is the demand signal, the requisition is the pipeline record, and the delivery confirmation is the closure. MSS manages this pipeline. Units that use MSS for pull logistics gain pipeline transparency that reduces the "where is my request?" coordination burden — the answer is in MSS.

### 4-4. The Distribution Feedback Loop

Effective distribution is not a one-time scheduling problem — it is a feedback loop. The distribution plan is executed, actual delivery is recorded, consumption is tracked against delivery, and the next distribution plan is adjusted based on what actually happened versus what was planned.

MSS closes this feedback loop when used correctly:
- Planned deliveries (movement requests, convoy assignments) are recorded before execution
- Actual deliveries are confirmed in MSS when convoys return
- Supply point receipt data updates on-hand quantities
- DOS calculations update automatically
- The next distribution plan is generated against current on-hand data — not against yesterday's plan

The loop breaks when any step is skipped. The most common break point is delivery confirmation — units are resupplied but the convoy closure is not entered in MSS. The supply point receipt is processed but not reflected in MSS. The result: MSS shows critical shortages that no longer exist, or adequate status that does not reflect recent consumption.

Distribution feedback discipline — closing convoys, confirming receipts, updating on-hand quantities — is the operational discipline that keeps the distribution feedback loop working. It is not data administration. It is a combat function.

### 4-5. The S4's Role in Distribution Decision-Making

Distribution, properly understood, is a command function, not just an administrative one. Commanders who are unaware of the distribution picture cannot make informed decisions about operational tempo, resupply pauses, or maneuver risk. The S4 who manages distribution silently — solving problems without surfacing them to the commander — deprives the commander of the information needed to make risk decisions.

MSS changes this by making the distribution picture visible. The commander who can see the distribution dashboard does not need to ask the S4 "how are we doing on resupply?" — the answer is on the screen. The S4's value shifts from information provider to analyst: "the distribution picture shows we are on track, but here is the risk if Route GREEN closes, and here is my mitigation plan."

This is a cultural shift as much as a technical one. Some S4s resist making problems visible because they prefer to solve them before briefing. In the MSS environment, the commander may see the problem in the dashboard before the S4 has a mitigation. Senior sustainment leaders should establish a culture where the S4 proactively surfaces distribution risks — with or without a mitigation in hand — rather than managing information downward.

### 4-6. Multi-Modal Distribution in USAREUR-AF

USAREUR-AF is a theater with unique distribution characteristics. Unlike a continental US post or a Middle East deployment with road-dominant distribution, USAREUR-AF sustainment operates across a complex European theater with significant multi-modal options: road, rail, inland waterway, and air.

Each mode has different data characteristics in MSS.

**Rail** offers high throughput for bulk cargo and heavy equipment, but requires lead time, coordination with European rail authorities, and adherence to host nation rail schedules. MSS rail tracking includes rail request status, car assignment, departure and arrival data, and HNS coordination records. Rail is particularly important for USAREUR-AF retrograde and redeployment operations.

**Inland waterway** (Rhine, Danube, and other European river systems) offers economical heavy lift for non-time-sensitive cargo. 88K/88L watercraft data in MSS (see TM-40D, paragraph 4-7) supports the theater distribution picture. Waterway status — draft clearance, bridge clearance, seasonal ice, flood risk — must be current in MSS for distribution planners to rely on it.

**Road** remains the primary distribution mode for direct support to forward units. USAREUR-AF road distribution planning must account for HNS movement restrictions (convoy approvals required in many partner nations), bridge weight limits, and SOFA requirements.

**Air** (LOGAIR, SEALIFT, theater airlift) is available for emergency and high-priority cargo. Air movement requests are typically routed through G4 to the theater air operations center; MSS provides the cargo data that feeds air movement manifesting.

The S4 and 88N who understand multi-modal distribution — and who use MSS to track the status across all modes simultaneously — have a distribution capability that significantly exceeds road-only thinking.

---

## SECTION 5 — SUSTAINMENT-MANEUVER INTEGRATION: HOW LOGISTICS DATA FEEDS THE COP

**BLUF:** The commander's operational picture is incomplete without logistics data. A maneuver plan that ignores sustainment constraints will fail at execution. MSS enables sustainment-maneuver integration by making logistics data visible in the same platform that displays the operational picture.

### 5-1. Sustainment Data Belongs in the COP

The Common Operating Picture (COP) in MSS integrates data from multiple warfighting functions. The Mission Command WFF (TM-40F) provides the doctrinal framework for COP management. From the sustainment perspective, the key question is: what logistics data must be in the COP for the supported commander to plan effectively?

At a minimum, sustainment data in the COP must include:
- Equipment readiness by unit (C-rating and breakdown)
- Critical supply shortfalls (Class I, III, V, IX below threshold)
- Distribution status (active convoys, supply point availability)
- Personnel strength (strength percentage by unit)

These are not S4 products that get briefed at the daily sustainment update. These are data layers in the COP that the S3, XO, and commander need continuously — not just at the LOGSTAT brief.

### 5-2. The Sustainment Constraint to Maneuver Planning

FM 5-0 describes mission analysis as a step that includes identifying specified tasks, implied tasks, and constraints. Sustainment status is a common source of constraints on maneuver. A unit at C-2 readiness is constrained in which tasks it can perform. A unit with 1.5 DOS of fuel cannot plan for a 72-hour deep attack without a refueling plan.

When S4 sustainment data is visible in MSS alongside the maneuver picture, the S3 can identify sustainment constraints during planning — not after the OPORD is issued and the S4 raises a concern in the rehearsal. MSS enables the integration that ADP 4-0's integration principle requires.

### 5-3. The LOGSTAT as a COP Contribution

The LOGSTAT is not just a report submitted to higher. It is a sustainment contribution to the COP. When the LOGSTAT data is current in MSS, the supported commander can see the sustainment picture at any time — not just when the S4 briefs it.

This changes the nature of the sustainment brief in the battle rhythm. Instead of the S4 reporting data that the commander has not seen, the S4 is analyzing data the commander has already reviewed. The brief becomes an analytical product — "here is what the data means, here are my recommendations" — rather than an informational product — "here is the status." This is the higher-order use of MSS that distinguishes a data-enabled sustainment staff from one that simply uses the platform as a digital LOGSTAT form.

### 5-4. The S4 as a Producer, Not Just a Consumer, of the COP

The Mission Command COP (TM-40F) is built from contributions from every warfighting function. The S4 is a producer of COP data — not merely a consumer of it.

This distinction matters because it defines the S4's relationship to the COP differently from how most S4 sections conceive of it. Many S4 sections view the COP as an S3 product that they occasionally receive information from. In reality, the sustainment data that the S4 maintains — readiness, supply status, distribution picture — is a layer of the COP that every other staff section relies on.

The S3 uses readiness data to task-organize. The fires officer uses Class V status to plan fires. The S2 uses transportation route data for LOC analysis. The commander uses strength data to assess combat power available for courses of action. All of these downstream uses depend on the S4 maintaining current, accurate sustainment data in MSS.

The S4 who treats MSS as an internal sustainment tool — a tool for managing the S4's own work — underutilizes the platform. The S4 who understands that the sustainment workspace on MSS contributes to the formation-wide COP, and who maintains data currency accordingly, provides real operational value to every staff section that depends on sustainment data.

### 5-5. Sustainment Data as a Decision Support Tool

ADP 6-0 establishes that commanders make decisions supported by staff analysis. Sustainment data from MSS is a decision support input — specifically for:

**Task organization decisions:** Which unit gets assigned the main effort? Which has the readiness to absorb it? Which needs a period of sustainment before it can be tasked? These decisions require current readiness and personnel strength data.

**Operational pacing decisions:** How long can the current operational tempo be sustained before Class III or Class I thresholds become critical? When is the right time for an operational pause that allows resupply? These decisions require DOS trend data.

**Risk acceptance decisions:** What is the sustainment risk of executing Phase II before the Class V resupply arrives? What is the degradation to maneuver if we continue with three deadlined recovery vehicles? These decisions require the commander to see the sustainment picture alongside the operational picture.

All three decision categories require MSS sustainment data to be current, accurate, and visible to the commander. The S4's role is not just to report the sustainment status — it is to connect the sustainment status to the commander's decision points. That analytical connection is a staff function that MSS enables but does not replace.

---

## SECTION 6 — PERSONNEL ACCOUNTABILITY AS MISSION-CRITICAL DATA: WHY PERSTAT ACCURACY MATTERS

**BLUF:** The PERSTAT is not a personnel administration product. It is a combat power accountability product. A PERSTAT that is wrong by 10 Soldiers is a commander who does not know what combat power is available — and a CCIR that is not triggered when it should be.

### 6-1. PERSTAT as Combat Power Data

Personnel strength directly affects mission assignment. A company at 65% strength should not be assigned the same task as a company at 95% strength. A battalion with six KIA and twelve WIA in the last 24 hours is experiencing a casualty rate that may exceed the personnel FFIR threshold — which is a commander decision point. None of these decisions can be made accurately if the PERSTAT is wrong.

The PERSTAT in MSS is only as accurate as the accountability inputs from unit first sergeants. A first sergeant who submits a morning PERSTAT before completing formation, or who fails to report three Soldiers on emergency leave, submits bad data. That bad data flows into the MSS strength dashboard, into the LOGSTAT, and into the commander's picture. The platform cannot correct a lie — or a mistake.

### 6-2. Casualty Data Is Time-Sensitive and Legally Significant

Casualty reporting IAW AR 638-8 has time standards that are mission-driven. Delayed casualty reporting affects next-of-kin notification, theater strength accounting, unit replacement planning, and commander decisions on combat power. Casualty data entered late in MSS propagates the delay through the sustainment and personnel accountability picture.

MSS casualty tracking is a management tool — it provides visibility of open casualty records, tracks status changes, and enables PERSTAT adjustment. It is not the official record. The official CASREP submitted through S1 channels is the authoritative record. MSS and the official record must remain synchronized. When they diverge — a casualty appears in MSS but no CASREP was submitted, or vice versa — a serious accountability gap exists.

### 6-3. Strength Management Beyond the Daily Headcount

Personnel accountability in MSS is not only about who is present for duty today. It also includes:

- **Availability forecasting**: who is scheduled for leave, TDY, medical appointments, or training that will affect strength next week?
- **Strength trend analysis**: is the unit gaining or losing strength? At what rate? When will it require replacement requests?
- **Personnel action pipeline**: awards submitted to higher but not yet approved; promotions pending board; NCOERs past due — these are indicators of administrative health that affect retention and morale

A G1 or S1 that uses MSS only for daily PERSTAT is using it at its most basic level. The full value of personnel data in MSS is realized when strength trend data informs replacement planning and when personnel action visibility reduces the administrative friction that degrades NCO and officer retention.

### 6-4. The Feedback Problem: When PERSTAT Accuracy Creates Pressure

There is a tension inherent in personnel accountability that MSS makes more acute: the faster and more visible PERSTAT data becomes, the more pressure first sergeants feel to submit accurate numbers quickly. In the legacy environment, a first sergeant who was not sure about two Soldiers' status had time to check before the S1 compiled the PERSTAT. In MSS, the PERSTAT updates in near-real time and is immediately visible to higher.

This pressure can go two ways. For disciplined units, it enforces faster, more complete accountability procedures. For undisciplined units, it can create incentive to submit a number — any number — to satisfy the visible dashboard rather than to verify the actual count.

Senior leaders must address this tension directly. The standard is unambiguous: submit an accurate PERSTAT, even if it is late. A PERSTAT with an honest "unverified" annotation is more operationally useful than a PERSTAT with false data submitted to meet a time standard. The commander who knows that accountability for three Soldiers is still in progress can decide whether to wait or accept the risk of an incomplete picture. The commander who receives a false "all accounted for" has no opportunity to make that decision.

### 6-5. Personnel Accountability Across Echelons: The Aggregation Challenge

At company level, PERSTAT is a headcount. At battalion level, it is an aggregation of four to six company PERSTATs. At brigade level, it is an aggregation of three to five battalion PERSTATs. At each step, errors compound.

A single company first sergeant who submits a PERSTAT three Soldiers high will inflate the battalion strength, inflate the brigade strength, and inflate the corps strength. When the error is eventually identified — in a commander's inquiry, an IG inspection, or a theater audit — it will trace back to the original source. But in the interim, every commander above that company level has made decisions based on a false picture.

MSS does not prevent this error. It makes it easier to identify. When a unit's MSS strength suddenly increases by three Soldiers without a corresponding personnel action in IPPS-A, that anomaly is visible — to S1 analysts, to the strength manager, to anyone monitoring the strength dashboard. The platform creates visibility that the legacy environment, with its manual aggregation, could not provide.

The S1 section that monitors for anomalies — unexpected strength changes, PERSTAT submissions that are inconsistent with known personnel action patterns — uses MSS as an accountability tool, not just a reporting tool. This is the higher-order use of PERSTAT data in MSS.

---

## SECTION 7 — SUSTAINMENT FAILURE MODES IN MSS: EIGHT COMMON MISUSE PATTERNS

**BLUF:** MSS improves sustainment operations when used correctly. It creates new failure modes when used incorrectly. Eight misuse patterns appear consistently across units that adopt MSS without adequate training. Senior leaders should recognize these patterns and correct them before they become operational liabilities.

### Failure Mode 1: Stale LOGSTAT

**Pattern:** The LOGSTAT in MSS is last updated from this morning's data call, but it is now 1900 and two supply points have been resupplied, two convoys have returned, and three vehicles have been repaired. The MSS LOGSTAT still shows the morning picture. The evening LOGSTAT submitted to higher is 12 hours stale.

**Why it happens:** Units treat the LOGSTAT as a morning product. They compile data in the morning, enter it into MSS, and do not update during the day. This was adequate in the legacy environment where there was no alternative. In MSS, data can be updated continuously — and the failure to do so means the platform's primary advantage (continuous currency) is lost.

**Correction:** Establish SOP update requirements: supply point status twice daily (minimum), vehicle status after each PMCS, convoy status after each checkpoint and delivery. The LOGSTAT is a continuous product, not a morning snapshot.

### Failure Mode 2: Readiness Gaming

**Pattern:** A unit is approaching a command inspection or higher headquarters readiness review. Maintenance NCOs close work orders for vehicles that have not actually been repaired. The MSS readiness dashboard shows improved FMC rates. The commander briefs better readiness numbers than the motor pool reflects.

**Why it happens:** SAMS-E entries can be manipulated by users with data entry access. MSS displays what SAMS-E records — it does not conduct independent vehicle inspections. Units under readiness pressure sometimes adjust records to show improved status.

**Correction:** Physical inspections by impartial observers (command inspector general, higher headquarters maintenance teams) will identify discrepancies. Readiness gaming exposes units to financial liability (FLIPL for parts requisitioned but not used), legal exposure (false official statements), and operational exposure (equipment that MSS says is FMC fails at execution). Senior leaders must enforce zero tolerance for readiness gaming — the downstream operational consequences are severe.

### Failure Mode 3: Accountability Gaps from Dual Entry Neglect

**Pattern:** A supply transaction is completed. The supply sergeant receipts the item and issues it to the using unit. GCSS-Army is not updated. The item shows as "due-in" in MSS for days after delivery. The S4 continues to show a supply shortage for an item that is already on-hand.

**Why it happens:** Sustainment transactions require entry in authoritative systems (GCSS-Army, SAMS-E) to appear correctly in MSS. When units allow transactions to accumulate without entry — during high-tempo operations, during system outages, or simply from poor discipline — MSS reflects an outdated supply picture.

**Correction:** Entry in authoritative systems must be treated with the same urgency as physical transactions. A receipt that is not in GCSS-Army is not a receipt for accountability purposes — and it is invisible to every downstream user of MSS data.

### Failure Mode 4: Confusing the Platform with the Record

**Pattern:** A unit uses MSS as its primary supply tracking tool. A Class IX shortage is documented in MSS but not in GCSS-Army. The shortage appears resolved in MSS (manually annotated) but is not resolved in GCSS-Army. The annual property audit reveals the discrepancy.

**Why it happens:** MSS is visible, user-friendly, and responsive. Source systems (GCSS-Army, SAMS-E, PBUSE) are complex, require training, and are slower to use. Units develop workarounds where MSS annotations substitute for proper source system entry.

**Correction:** MSS is a visualization and integration tool. It is not the system of record for any supply transaction, maintenance work order, or property accountability action. Nothing that happens only in MSS is officially documented. Senior logisticians must enforce the primacy of authoritative systems.

### Failure Mode 5: Distribution Deconfliction Failures

**Pattern:** Two supply sergeants both coordinate with the BSB supply point directly — by phone — for resupply without entering movement requests in MSS. Both are scheduled for resupply on the same day. The distribution company has one available truck. One unit is not resupplied. The 88N transportation coordinator did not know about the second request because it was not in MSS.

**Why it happens:** Units with existing personal relationships within the sustainment network bypass formal processes. Phone calls are faster than system entry. The informal coordination works — until it does not.

**Correction:** The movement request process in MSS exists precisely to enable deconfliction. When units bypass it, the transportation coordinator cannot synchronize distribution. This is a discipline and command emphasis issue. The S4 must enforce movement request submission as a non-negotiable requirement.

### Failure Mode 6: Threshold Misconfiguration

**Pattern:** The unit is in a high-tempo operational phase. The S4 increased consumption planning factors but forgot to update MSS threshold values. Class I on-hand drops to 2.5 DOS. No MSS alert is generated because the threshold is still configured to alert at 1 DOS (the garrison standard). The S4 does not see the shortage until the next morning brief.

**Why it happens:** MSS thresholds are configured once — typically during initial setup — and rarely reviewed. As the operational situation changes, planning factors change. Thresholds that were appropriate for garrison operations may be dangerously low for deployed operations.

**Correction:** Threshold review must be a standing agenda item whenever the operational situation changes significantly: new OPORD, change in operational tempo, change in force structure or attachments. The S4 owns MSS threshold configuration. It must be treated as a tactical decision, not a system administration task.

### Failure Mode 7: PERSTAT Submission Without Verification

**Pattern:** The first sergeant submits the morning PERSTAT to the S1 without completing full formation accountability. Three Soldiers are unaccounted for. The first sergeant assumes they are with another platoon or at sick call. The PERSTAT is submitted as "all present" to meet the submission time. The three Soldiers are actually absent without authorization.

**Why it happens:** PERSTAT submission is time-constrained. First sergeants under pressure to meet reporting times may submit before accountability is complete. MSS makes the submitted status immediately visible to higher — which can create pressure to submit on time even when data is incomplete.

**Correction:** Accurate PERSTAT is more important than timely PERSTAT. AR 638-2 and AR 600-8-6 are clear on accountability requirements. A late but accurate PERSTAT is always preferable to an on-time PERSTAT with false data. Senior NCO leadership must enforce this standard consistently.

### Failure Mode 8: MSS-Only Sustainment Operations

**Pattern:** A unit becomes so dependent on MSS that when MSS is unavailable — network outage, planned maintenance, user permission issue — sustainment reporting stops. The S4 cannot generate a LOGSTAT. The supply sergeant does not know what is on-hand because the only tracker is in MSS. The convoy is delayed because the route data is only in MSS.

**Why it happens:** MSS is easy to use and integrates data effectively. Units stop maintaining parallel manual systems because they seem redundant. When MSS fails, the fallback does not exist.

**Correction:** MSS is a tool, not a system. The Army operated before MSS and will operate when MSS is unavailable. Every sustainment function must maintain a viable manual fallback: LOGSTAT formats, paper supply status forms, convoy manifests, written route data. Degraded operations proficiency must be exercised — not just briefed — during collective training events.

### Failure Mode Summary

**Table 7-1. Sustainment MSS Failure Modes — Quick Reference**

| Failure Mode | Root Cause | Senior Leader Indicator | Correction |
|---|---|---|---|
| Stale LOGSTAT | Unit treats LOGSTAT as morning snapshot only | Evening LOGSTAT matches morning data verbatim | Establish twice-daily update SOP; enforce with S4 spot-checks |
| Readiness gaming | Inspection pressure drives false SAMS-E entries | C-rating improves dramatically before inspections, drops after | Physical inspection + IG involvement; zero tolerance messaging |
| Accountability gap from dual entry neglect | Source system entry deprioritized vs. physical work | Frequent GCSS-Army / MSS discrepancies on reconciliation | Command emphasis on same-day source system entry |
| Confusing MSS with the record | MSS is easier than GCSS-Army; workarounds develop | Discrepancies found on audit that only exist in MSS | Enforce primacy of authoritative systems in SOP and counseling |
| Distribution deconfliction failure | Units bypass MOVREQ process via phone coordination | Transportation coordinator is surprised at competing requests | Enforce MOVREQ process as non-negotiable; reject informal requests |
| Threshold misconfiguration | Thresholds set at garrison standards, never reviewed | Critical situations produce no MSS alert | Add threshold review to OPORD checklist; S4 owns configuration |
| PERSTAT without verification | Time pressure from visible dashboard, not accountability first | First sergeant submits before formation is complete | Senior NCO standard: accuracy before timeliness; accept annotated late PERSTAT |
| MSS-only sustainment operations | Convenience removes manual fallback capability | Unit cannot produce LOGSTAT during MSS outage | Periodic degraded-ops exercises; manual LOGSTAT drills |

### Closing: From Awareness to Mastery

The failure modes above are not hypothetical. They have been observed in units across USAREUR-AF and in exercises at JMRC (Joint Multinational Readiness Center). They reflect the predictable adaptation patterns of organizations learning a new information system — the workarounds, the shortcuts, the metric gaming that emerge when data is visible but data discipline is not enforced.

The sustainment practitioner who reads this guide before beginning TM-40D task instruction will recognize these patterns when they appear — in their own unit, in adjacent units, and in their own habits. Recognition is the first step toward correction.

Mastery of MSS in the sustainment context is not technical mastery — it is analytical mastery. It is the 92A who sees a supply trend and knows it means a resupply request must go out today, not next week. It is the 91Z who sees the parts pipeline report and knows which three work orders need a phone call to the ASP to accelerate. It is the 88N who sees two movement requests arriving from the same unit on the same day and picks up the phone before the convoy gets issued twice.

MSS provides the picture. The sustainment practitioner provides the judgment. Both are required.

> **NOTE: The CONCEPTS_GUIDE is not a one-time read. Sustainment leaders who revisit it before major exercises, CPXs, or deployments often find that concepts that seemed abstract during initial reading are immediately applicable in context. The failure modes in Section 7, in particular, are easier to recognize — and prevent — when the conceptual framework is fresh.**

---

## RELATED TRACKS AND PUBLICATIONS

### WFF Peer Tracks

All six WFF tracks are at the same tier. All six WFF tracks require TM-10, TM-20, and TM-30 as prerequisites.

| Track | Title | Prereq | Relationship to Sustainment WFF |
|-------|-------|--------|--------------------------------|
| TM-40A | Intelligence WFF | TM-10 + TM-20 + TM-30 | LOC threat data, supply point security |
| TM-40B | Fires WFF | TM-10 + TM-20 + TM-30 | CSR, ammunition management coordination |
| TM-40C | Movement and Maneuver WFF | TM-10 + TM-20 + TM-30 | Route capacity, maneuver readiness, supply constraints |
| TM-40D | Sustainment WFF | TM-10 + TM-20 + TM-30 | This track |
| TM-40E | Protection WFF | TM-10 + TM-20 + TM-30 | CBRN resupply, convoy route protection |
| TM-40F | Mission Command WFF | TM-10 + TM-20 + TM-30 | LOGSTAT feeds commander FFIR monitoring; S4 products to COP |

### Specialist Tracks (Prerequisite: TM-30)

For personnel pursuing technical depth, specialist tracks (TM-40G–O, prereq TM-30) are available. Not required for sustainment WFF employment.

| Track | Title |
|-------|-------|
| TM-40G | ORSA (→ TM-50G) |
| TM-40H | AI Engineer (→ TM-50H) |
| TM-40M | ML Engineer (→ TM-50M) |
| TM-40J | Program Manager (→ TM-50J) |
| TM-40K | Knowledge Manager (→ TM-50K) |
| TM-40L | Software Engineer (→ TM-50L) |
| TM-40N | UI/UX Designer (→ TM-50N) |
| TM-40O | Platform Engineer (→ TM-50O) |

---

*CONCEPTS GUIDE — TM-40D Companion, Version 1.0, March 2026*
> **NOTE — New Doctrine Content in TM-40D:** TM-40D now includes the eight sustainment principles mapped to data platform analogs (Table 1-1A, ADP 4-0), ten classes of supply with source systems, data feeds, and update frequencies (Table 2-1A), and a running estimate NOTE tying battle rhythm data to commander decision support. These sections ground sustainment data management in their authoritative doctrinal sources.

*Headquarters, United States Army Europe and Africa, Wiesbaden, Germany*
