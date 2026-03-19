# TM-40B — MAVEN SMART SYSTEM (MSS)

> **Prereqs:** TM-10, Maven User; TM-20, Builder; TM-30, Advanced Builder; CONCEPTS_GUIDE_TM40B_FIRES (required before beginning this manual). No coding, pipeline development, or transform experience is required or assumed.
> *HQ USAREUR-AF · v1.0 · 2026 · DISTRIB: USG only · AUTH: C2DAO/UDRA v1.1*

> **WARNING: Using stale MSS target data or FSCM overlays to clear fires without cross-checking against the establishing authority can result in fratricide or violation of ROE. Always confirm FSCM publication date and data-as-of timestamp before clearing any fire mission near a coordination boundary.**
> **WARNING: MSS air picture data is a supplemental display. AMD engagement authority requires validation against primary AMD systems. Do not base weapon release decisions solely on MSS track data.**
> **CAUTION: MSS target tracking data reflects reported status only. Gaps in reporting do not indicate absence of targets. Validate target data against all available collection sources before committing to BDA assessments or re-attack recommendations.**
> **NOTE: MSS does not replace AFATDS, IBCS, AMDWS, or FAAD C2. It integrates and displays data from those systems to enable fires staff planning, targeting, and assessment. The primary fires systems remain authoritative for mission processing and engagement execution. MSS is the data integration and visualization layer above those systems.**

---

## CHAPTER 1 — OVERVIEW AND FIRES FUNCTION IN MSS

### 1-1. Purpose

1-1. This manual provides fires warfighting function (WFF) practitioners with the knowledge and tasks required to use the Maven Smart System (MSS) in support of fires planning, targeting, and assessment operations. It is written for all FA and ADA MOS personnel from individual operator through fires cell staff.

1-2. MSS is the USAREUR-AF enterprise data and analytics platform. For fires personnel, MSS is not a fires control system. It is the integrated data environment where fires data — targets, coordination measures, asset status, sensor feeds, BDA records — is organized, visualized, and shared across the force.

1-3. Every fires task in MSS begins with understanding what MSS is and is not. MSS enables the human fires process. It does not execute fires.

1-3a. This manual is organized to move from the general to the specific: Chapter 1 provides orientation and context; Chapters 2 through 4 cover the core FA fires tasks (targeting, fire support planning, fire direction); Chapter 5 covers AMD operations; Chapter 6 covers sensor operations and C-RAM; Chapters 7 through 9 cover joint fires integration, assessment and reporting, and echelon-specific applications; Chapter 10 addresses degraded operations; and Chapter 11 addresses training and proficiency. Read the relevant chapters for your duty position. All fires personnel should read Chapters 1 and 10 regardless of MOS.

1-3b. This manual does not address MSS system administration, data pipeline management, or technical platform architecture. Those topics are addressed in TM-30 (Advanced Builder) and TM-40L (Software Engineer). If a fires task in this manual cannot be executed because of a platform configuration issue, report the issue to the unit S6 and the USAREUR-AF C2DAO fires functional representative rather than attempting technical workarounds.

---

### 1-1a. How to Use This Manual

1-3c. Task boxes throughout this manual are the primary reference for procedure execution. Each task box includes Conditions, Standards, and a numbered Procedure. Before executing any task in an operational environment, review the task's Conditions to confirm all prerequisites are met. Review the Standards to understand the performance threshold before beginning — not after.

1-3d. WARNING and CAUTION callouts appear throughout the manual. Read them. They identify the points in fires operations where MSS misuse causes operational risk, fratricide potential, or ROE violations. They are placed at the moments of greatest risk in the procedure, not at the beginning of the chapter.

---

### 1-2. Role of the Fires WFF in the MSS Ecosystem

> **BLUF: MSS supports all five fires WFF tasks — deliver fires, conduct AMD, integrate fires, conduct targeting, and execute the fires plan — through data visualization, target management, coordination measure publication, and assessment reporting.**

1-4. The fires WFF comprises five tactical tasks IAW ADP 3-19, para 1-2: deliver fires, conduct AMD, integrate fires, conduct targeting, and execute the fires plan. MSS provides data infrastructure supporting all five.

1-5. For fires to be effective, data must flow continuously through the fires process — from collection through target development, from mission assignment through BDA. Breaks in that data chain degrade fires effectiveness. MSS closes data gaps that previously existed between AFATDS, the targeting cell, the FSO, and the maneuver commander.

1-6. MSS does not compete with AFATDS, IBCS, or FAAD C2. Those systems execute fires and AMD. MSS integrates what those systems report, combines it with ISR data, maneuver graphics, and logistics feeds, and presents a single fires operational picture to commanders and staff.

1-7. The fires WFF in MSS is organized around four operational functions:
- Target management: development, tracking, and prioritization of targets
- Fire support coordination: FSCM management, clearance of fires, ROE visualization
- Asset management: readiness, positioning, and employment status of fires systems
- Assessment: BDA recording, fires effectiveness analysis, and re-attack recommendations

---

### 1-3. How MSS Supports the Fires Process

1-8. The fires process — plan, prepare, execute, assess — maps directly onto MSS capabilities. MSS data must be current at every phase.

**Plan phase.** MSS supports fires planning by maintaining the target list, publishing FSCMs, tracking priority targets against collection requirements, and providing fires asset status to inform scheme of fires development.

**Prepare phase.** MSS displays the synchronization of collection assets against HPTs, tracks fire support execution matrix (FSEM) data, and maintains ammunition status to confirm units can execute the plan as written.

**Execute phase.** MSS tracks fire missions in near real-time, maintains the air picture for AMD coordination, and provides the FSCOORD visibility of active coordination measures and asset engagement status.

**Assess phase.** MSS is the primary platform for BDA recording, effects assessment, and re-attack recommendations. After each fires event, assessment data enters MSS and informs the next targeting cycle.

1-9. The value of MSS grows with data discipline. Units that update MSS consistently during all four phases maintain a fires picture that commanders can trust. Units that update MSS selectively — only during certain phases or certain events — produce a degraded common operating picture that introduces risk.

---

### 1-4. Fires Data Types in MSS

1-10. MSS hosts four categories of fires data. Each category has different currency requirements and different roles in the fires process.

**Target data.** The target list, high-payoff target list (HPTL), attack guidance matrix (AGM), and joint target list (JTL) data maintained in the MSS targeting module. Target data ages quickly in a dynamic environment. 13A/13F officers own target data currency within their areas of responsibility.

**Sensor data.** Feeds from Q-36 and Q-37 radar systems, ISR platforms, and other collection assets. Sensor data is the most time-sensitive fires data in MSS. Point of origin (POO) and point of impact (POI) data from radar must be acted on within minutes to drive counterfire. MSS displays radar feeds; 13R operators manage the sensor interface.

**Asset status data.** Position, readiness, and ammunition status of all fires systems — FA howitzers, rocket systems (MLRS/HIMARS), mortars, Patriot batteries, SHORAD systems, and M-SHORAD platoons. Asset status data enables the FSCOORD to match fires requirements to available means.

**ROE and coordination measure data.** FSCMs, rules of engagement (ROE) restrictions, airspace coordination areas (ACA), and engagement authority data. This category carries the highest safety consequence of any fires data in MSS. Outdated or incorrect FSCMs create fratricide risk. 13F FSOs and the fires cell staff jointly own FSCM data in MSS.

---

### 1-5. Doctrinal References

TM-40B is written in alignment with the following doctrinal publications. These publications are not required reading before using this manual — but fires practitioners who are responsible for targeting, fire support coordination, or AMD functions should be familiar with them.

**Table 1-1. Primary Doctrinal References**

| Publication | Title | Relevance to TM-40B |
|---|---|---|
| ADP 3-19 | Fires | Foundational fires warfighting function doctrine |
| FM 3-09 | Fire Support and Field Artillery Operations | Capstone fires FM |
| FM 3-27 | Army Global Integrated Fires (~2023) | Long-range precision fires, convergence, multi-domain fires |
| FM 3-60 | Army Targeting (Aug 2023) | D3A/F3EAD targeting methodology (replaces ATP 3-60) |
| ATP 3-09.42 | Fire Support for the BCT | FSE operations at BCT level |
| ATP 3-01.81 | Counter-UAS Techniques | C-UAS detection, tracking, defeat |
| FM 3-01 | Air and Missile Defense Operations | AMD doctrine |

**Strategic Guidance:**

> The following are strategic guidance documents — not doctrine — that inform MSS training design and operational context.

| Document | Authority | Relevance |
|---|---|---|
| NATO Digital Transformation Implementation Strategy (Oct 2024) | NATO | MDO interoperability context — frames fires data sharing in coalition operations |
| DDOF Playbook v2.2 (December 2025) | T2COM C2DAO | VAULTIS-A quality framework (8 dimensions); 6-phase data product lifecycle; 85% quality gate; MVP mandate 30 days |

---

### 1-5a. MSS vs. Legacy Fires Tools

1-11. Fires practitioners in USAREUR-AF formations have used AFATDS, Q-53 radar feeds, AMDWS, IBCS, and FAAD C2 for years. MSS does not replace those tools. It integrates data from them into a unified operational picture.

1-12. The key distinction is the function each system performs:

**Table 1-2: Legacy Tool vs. MSS Comparison**

| System | Primary Function | MSS Relationship |
|--------|-----------------|-----------------|
| AFATDS | Fire mission processing, ballistic computation, FDC operations | MSS receives and displays mission data from AFATDS; AFATDS remains authoritative for ballistic computation |
| Q-36/Q-37 Firefinder Radar | Point of origin/impact detection, counterfire cueing | MSS receives radar track data for display; radar remains authoritative detection system |
| AMDWS | AMD command and control, air picture compilation | MSS receives AMDWS track data; AMDWS remains authoritative for AMD C2 |
| IBCS | Integrated AMD fire control, sensor-shooter integration | MSS displays IBCS engagement status; IBCS executes AMD engagement |
| FAAD C2 | Forward area air defense command, SHORAD integration | MSS receives FAAD C2 data; FAAD C2 remains SHORAD authoritative system |
| MSS | Data integration, visualization, targeting, assessment, fires staff coordination | Aggregates and visualizes data from all above systems; does not execute fires or AMD |

1-13. Fires personnel must resist the temptation to use MSS as a fires execution system. MSS is a staff coordination and visualization tool. When the radio goes down and AFATDS loses connectivity, fires still happen via voice and manual procedures. When MSS is degraded, fires continue through primary systems. See Chapter 10 for degraded operations.

---

### 1-5b. Transitioning from Legacy Tool Habits to MSS

1-13a. Fires personnel with experience on AFATDS, AMDWS, or legacy fire support coordination tools will find MSS approaches coordination and data management differently. Several transition points require deliberate attention:

**Data persistence.** AFATDS and AMDWS store data in unit-specific databases that are not automatically shared across echelons. MSS stores fires data in a shared cloud-accessible workspace visible simultaneously to all authorized users. Fires personnel accustomed to managing their own data in their own system must adapt to shared workspace discipline — understanding that their entries are immediately visible to the FSCOORD, adjacent fires cells, and higher headquarters simultaneously.

**Separation of execution from visualization.** AFATDS executes fire missions. MSS visualizes them. Fires personnel must not attempt to use MSS for fire direction or expect MSS to replace AFATDS functions. The transition error of treating MSS as a replacement for primary fires systems produces confusion and operational risk.

**Real-time update expectation.** Legacy fires products (HPTL slides, printed FSCM overlays, paper ammunition reports) were updated at discrete intervals. MSS enables and requires near-real-time updates. The fires cell that updates MSS on the legacy product cycle — daily or at TWG — is using MSS below its capability and below the data currency standard.

---

### 1-6. Fires Workspace Organization and Access Controls

1-14. MSS organizes fires data within a fires workspace that mirrors the fires WFF functional organization. Each echelon from BCT through theater has a fires workspace configured to its functions.

1-15. Access within the fires workspace follows the principle of least privilege. Personnel have access to the data categories they need to perform their duties.

**Table 1-3: MOS/Duty Position Cross-Reference with MSS Access Level**

| MOS / Duty Position | MSS Fires Access Level | Primary Data Responsibility |
|--------------------|----------------------|----------------------------|
| 13A (FA Officer) / FSCOORD | Read/Write — Full fires workspace | Target management, FSCM publication, fires synchronization |
| 13A (FA Officer) / FSO | Read/Write — FSO module, FSCM overlay | FSCM currency, CFF tracking, direct support coordination |
| 13B (Cannon Crewmember) | Read — Asset status; Write — mission completion | Ammunition status updates, position reporting |
| 13F (Fire Support Specialist) | Read/Write — FSO module, CFF log | CFF submission, BDA entry, FSCM observation |
| 13J (Fire Control Specialist) | Read/Write — Fire direction module | Fire mission log, mission tracking, ammunition tracking |
| 13M (Multiple Launch Rocket Operator) | Read — Asset status; Write — mission reporting | Position updates, mission completion entries |
| 13P (MLRS Operations/Fire Direction Specialist) | Read/Write — Fire direction module | Fire mission log, MLRS-specific tracking |
| 13R (Firefinder Radar Operator) | Read/Write — Radar/sensor module | Radar zone management, POO/POI reporting, C-RAM tracking |
| 13S (Field Artillery Surveyor/Meteorological) | Read/Write — MET module | MET data upload, ballistic meteorological message management |
| 14A (ADA Officer) | Read/Write — AMD module | CAL/DAL management, AMD status, engagement authority tracking |
| 14E (Patriot MMS/AMD Systems Maintainer) | Read — AMD module; Write — system status | Patriot system status, readiness reporting |
| 14P (Air Defense Enhanced Early Warning) | Read/Write — Air picture module | Track management, early warning reporting |
| 14S (Avenger Crew Member) | Read — AMD status; Write — engagement log | Engagement logging, system position updates |
| 14T (Patriot Launching Station Operator) | Read — AMD module; Write — battery status | Battery readiness and status updates |
| 131A (FA Warrant Officer) | Read/Write — Full fires workspace | Technical fires data management, counterfire coordination |

---

**Table 1-4: Fires Data Categories in MSS**

| Data Category | Subcategories | Primary MOS Owner | Update Frequency | Safety Criticality |
|--------------|--------------|-------------------|-----------------|-------------------|
| Target Data | HPTL, AGM, JTL, target library, BDA records | 13A / 13F | Per collection/reporting cycle | HIGH — stale targets drive incorrect effects delivery |
| Sensor Data | Radar feeds, ISR product integration, POO/POI data | 13R / 13S | Continuous (automated feeds) / per mission | CRITICAL — time-sensitive counterfire data |
| Asset Status | FA unit positions, ammo loads, system readiness | 13B/13J/13M/13P | Daily minimum; on-event updates | HIGH — inaccurate asset data degrades fires synchronization |
| FSCM/ROE Data | FSCMs, ACAs, ROE restrictions, engagement authority | 13A (FSCOORD) / 13F (FSO) | On-change; minimum every 12 hours | CRITICAL — stale FSCMs create fratricide risk |
| AMD Data | CAL/DAL, air tracks, engagement logs, HIMAD/SHORAD status | 14A / 14P | Continuous (air picture) / daily (CAL/DAL) | CRITICAL — stale AMD data affects engagement authority |
| Fires Reports | AMMO SITREP, FIREP, BDA reports, fires effectiveness | All fires MOS | Per reporting cycle IAW unit SOP | MEDIUM — reporting failures degrade commander's assessment |

---

## CHAPTER 2 — TARGETING AND THE D3A PROCESS IN MSS

### 2-1. Overview

> **BLUF: The D3A targeting process — Decide, Detect, Deliver, Assess — is the operational framework for fires. MSS supports every phase of D3A by providing the data infrastructure to manage targets, track sensor feeds, synchronize delivery, and record assessment results.**

2-1. Targeting is the process of selecting and prioritizing targets and matching the appropriate response to them IAW commander's objectives and capability. The D3A methodology — Decide, Detect, Deliver, Assess — provides the framework for that process. MSS provides the data backbone for all four phases.

2-2. Targeting in MSS is a continuous process, not a daily product cycle. The target list is alive. Sensor feeds update it. BDA results alter it. The commander's guidance shapes it. MSS enables that continuous loop when used correctly.

---

### 2-2. Decide: HPTL and AGM Management in MSS

2-3. The Decide phase is where the commander's intent translates into targeting priorities. The output of the Decide phase is two key products: the high-payoff target list (HPTL) and the attack guidance matrix (AGM). MSS is the authoritative repository for both.

2-4. The HPTL identifies which target categories the commander designates as high priority. It drives collection, determines what the ISR plan must find, and establishes the priority for fires resources. In MSS, the HPTL is a live data object, not a slide. Each HPTL entry carries associated target type, priority ranking, phase applicability, and collection-to-fires link.

2-5. The AGM translates the HPTL into delivery guidance: what weapon system to use, what effects to achieve, what ROE apply, and what delivery constraints govern each target category. MSS links AGM entries to HPTL entries so fires personnel can quickly determine the approved attack method for any priority target.

2-6. Target development in MSS follows a workflow from nomination through validation to HPTL placement. Any authorized user can nominate a target. 13A officers validate and place targets on the HPTL. The FSCOORD approves HPTL changes.

2-7. Joint target list (JTL) management in MSS applies at division and above. JTL data enters MSS from the joint targeting process and must be synchronized with the HPTL to prevent duplicate targeting or conflicting attack guidance.

2-8. JTL synchronization in MSS requires the division or corps targeting officer to review the JTL against the HPTL at each targeting working group cycle. Three types of conflicts require resolution:
- **Duplicate targeting:** A target on the HPTL is also on the JTL, and both the land and joint component have allocated fires resources against it. Resolution requires fires deconfliction — designating one component as the primary attack authority.
- **Conflicting attack guidance:** The HPTL AGM specifies one set of desired effects while the JTL specifies different effects or different constraints for the same target. Resolution requires FSCOORD coordination with the joint targeting element to align guidance.
- **JTL restrictions on HPTL targets:** The JTL designates certain targets as restricted from land fires attack — allocated to air-delivered fires or to joint special operations. HPTL entries for these targets must carry the JTL restriction flag to prevent erroneous land fires assignment.

2-9. Time-sensitive target (TST) management in MSS: TSTs are targets with a time-limited engagement window — they will move, disperse, or lose their value if not engaged within a defined window. MSS supports TST management by flagging HPTL entries as TSTs and by enabling rapid counterfire nomination for radar-detected targets. The TST flag in MSS is set by the FSCOORD at the targeting working group and reviewed at each cycle. Any target identified as a TST in intelligence reports is flagged immediately and routed for FSCOORD approval of TST designation without waiting for the next TWG.

---

### 2-3. Detect: Sensor Feed Integration and Target Tracking

2-10. The Detect phase covers all collection activity that locates, identifies, and tracks HPTs. MSS aggregates detection data from multiple sources: radar feeds, ISR product reporting, human source reporting entered by intelligence personnel, and manual updates entered by 13F FSOs.

2-11. Target tracking in MSS links detection data to HPTL entries. When a Q-36 radar reports a confirmed artillery position, that report links to the artillery target category on the HPTL and populates the target track with location, type, confidence level, and time of report.

2-12. Radar data visualization in MSS provides a geographic display of POO/POI data on the fires operational overlay. The radar feed does not replace the radar's organic display; it provides the fires staff visibility of radar-detected events on the integrated fires picture.

2-13. ISR synchronization in MSS links the ISR synchronization matrix (ISRM) to the HPTL. Collection assets assigned against HPT categories appear on the ISRM display. When an asset reports a positive find, that find updates the target track automatically if the data feed is active, or through manual entry by intelligence or fires personnel.

2-14. Target confidence levels in MSS:
- **Confirmed:** Target positively identified by two or more independent sources or by direct observation
- **Suspected:** Target reported by one source; awaiting corroboration
- **Templated:** Target placed at expected location based on OPFOR TTPs; not yet detected

> **CAUTION: Never plan fires against a templated target without confirming currency of the template and compliance with ROE for templated target attack. Templated locations reflect expected positions, not confirmed ones.**

2-15. Target location error (TLE) and its impact on fires: Every target location in MSS carries an implicit TLE — the difference between the reported position and the actual target position. TLE is not a constant. It varies by collection method, sensor capability, and age of the detection. A target located by survey-grade JDAM terminal guidance has very low TLE. A target reported by a ground observer with binoculars at 8km has potentially significant TLE. MSS does not compute TLE automatically — the targeting officer enters the location confidence level that represents TLE in categorical form. Fires planned against a high-TLE target require munitions with wider effects radii or multiple delivery runs to compensate.

2-16. ISR synchronization matrix (ISRM) in MSS: The ISRM displays which collection assets are tasked against which HPT categories, their collection windows, and their reporting status. The targeting officer reviews the ISRM daily at division and above to identify collection gaps — HPT categories with no active collection coverage — and generate requests to fill those gaps. MSS links ISRM data to the HPTL target categories, making the collection-to-fires relationship visible in a single display.

---

### 2-4. Deliver: Fire Mission Tracking and FSEM Coordination

2-17. The Deliver phase is where fires resources execute against confirmed targets. MSS supports the Deliver phase through fire mission tracking, FSEM management, asset-to-target matching, and delivery deconfliction.

2-18. Fire mission tracking in MSS provides visibility of active, pending, and completed fire missions. Each fire mission record in MSS carries: mission number, requesting unit, target number and type, weapon system assigned, time of request, time of execution, and execution status.

2-19. FSEM management in MSS organizes the fire support execution matrix by phase line, objective, or time period IAW the fire support plan. The FSEM in MSS is a live document — it updates as mission assignments are made and completed.

2-20. Asset-to-target matching in MSS supports the fires cell in assigning the most appropriate system to each target. MSS displays available fires assets with their current status, range rings overlaid on the fires picture, and current ammunition loads. The FSCOORD or targeting officer uses this display to make assignment decisions; MSS does not make assignments automatically.

2-21. Delivery deconfliction in MSS occurs through the FSCM overlay and airspace coordination display. Before clearing any fire mission near an FSCM boundary, the FSO confirms FSCM currency in MSS and cross-checks with the establishing headquarters. The airspace deconfliction module prevents assignment of fire missions through active ACAs without explicit coordination.

---

### 2-5. Assess: BDA Tracking and Effectiveness Reporting

2-22. The Assess phase closes the targeting cycle. BDA — battle damage assessment — records the effects achieved against the target and drives the re-attack recommendation. MSS is the primary platform for BDA recording in USAREUR-AF formations.

2-23. BDA in MSS records three levels of assessment IAW FM 3-60:
- **Physical destruction:** Percentage of target physically destroyed or damaged
- **Functional damage:** Whether the target can still perform its function
- **System disruption:** Impact on the OPFOR capability system the target supported

2-24. Re-attack recommendations in MSS link directly to the BDA record. When BDA indicates insufficient effects, the targeting officer generates a re-attack recommendation within MSS, links it to the original target record, and routes it for FSCOORD approval.

2-25. Fires effectiveness reports (FIREP) aggregate BDA data across the targeting cycle and report fires effectiveness to the commander. MSS generates the data for FIREP; the fires cell analyzes and formats it.

---

**Table 2-1: AGM Data Fields**

| Field | Description | Required/Optional | Owner |
|-------|-------------|-------------------|-------|
| Target Type | Describes OPFOR system/activity being targeted | Required | FSCOORD/Targeting Officer |
| Priority | Numeric rank within HPTL | Required | FSCOORD |
| Phase | Operational phase(s) in which target is active | Required | FSCOORD |
| Attack Method | Approved delivery systems (type and effects) | Required | FSCOORD / JAG coordination |
| ROE Restrictions | Applicable ROE constraints | Required | SJA/FSCOORD |
| Desired Effects | Physical, functional, or systemic effects desired | Required | FSCOORD |
| Time-Sensitive Indicator | Yes/No — whether target is time-sensitive (TST) | Required | FSCOORD |
| Collateral Damage Estimate | CDE category IAW CDE methodology | Required (ROE-driven) | Targeting/SJA |
| Collection Requirement | ISR task linked to target detection | Optional | Targeting Officer |
| Re-attack Criteria | Conditions under which re-attack is authorized | Required | FSCOORD |

---

**Table 2-2: BDA Effects Categories**

| BDA Category | Definition | Assessment Standard | Reporting Format |
|-------------|-----------|-------------------|-----------------|
| Physical Destruction | Target physically destroyed or damaged | % of physical structure/system destroyed | Report as P1 (>50%) or P2 (<50%) |
| Functional Damage | Target unable to perform primary function | Capability assessment: FMC, PMCI, PMCII, NMC | Report as F1 (mission incapable) or F2 (degraded) |
| System Disruption | OPFOR capability system affected beyond single target | Assessed at system/unit level | Report as qualitative narrative + C1-C4 rating |
| No Damage | No observable or reportable effects | Fires strike confirmed; no BDA indicators observed | Report as ND with source and basis |
| Unknown | Insufficient information to assess | Missing collection coverage or reporting gap | Report as UNK with collection shortfall noted |

---

**TASK: Build and Update the HPTL in MSS**

**CONDITIONS:** 13A officer or targeting officer, with access to the MSS fires workspace, a completed targeting guidance from the FSCOORD, and current HPTL from the last targeting working group (TWG). Fires cell targeting team assembled.

**STANDARDS:** HPTL in MSS reflects approved commander's targeting guidance. All HPTL entries have required AGM fields completed. HPTL is linked to active collection requirements. HPTL is synchronized with JTL (if applicable). HPTL is published to subordinate fires workspaces within one hour of TWG approval.

**PROCEDURE:**

1. Navigate to the MSS Fires Workspace and select the Targeting module.
2. Open the current HPTL display. Review existing entries against the latest targeting guidance.
3. For each target category the FSCOORD has approved to add or modify:
   a. Select "Add Target Category" or open the existing entry.
   b. Enter target type, priority ranking, and applicable phase.
   c. Enter or confirm attack method, desired effects, and ROE restrictions.
   d. Enter collateral damage estimate category.
   e. Set the time-sensitive target (TST) indicator if applicable.
   f. Link the target category to the applicable collection requirement on the ISRM.
4. Remove or archive any target categories the FSCOORD has removed from the HPTL.
5. Review the AGM matrix to confirm all HPTL entries have corresponding AGM data.
6. Cross-reference HPTL against the JTL (if at division or above) for deconfliction.
7. Submit HPTL update for FSCOORD review and approval within MSS.
8. After FSCOORD approval, publish HPTL to subordinate fires workspaces.
9. Notify subordinate FSOs of HPTL update via MSS notification or radio/PACE.
10. Record the HPTL update in the fires cell log with DTG and approving officer.

> **NOTE: The HPTL in MSS must reflect the same HPTL approved at the last targeting working group (TWG). Any discrepancy between the TWG slide product and the MSS HPTL represents a data integrity failure. Reconcile discrepancies immediately — the TWG slide is an informational product; MSS is the operational record.**

---

**TASK: Submit and Track BDA in MSS**

**CONDITIONS:** 13F FSO or targeting officer, with access to the MSS BDA module, a confirmed fires strike executed against a listed target, and available collection data (SIGINT, IMINT, visual observation, or HUMINT report).

**STANDARDS:** BDA record entered in MSS within two hours of fires execution or within one hour of BDA collection, whichever occurs first. All required BDA fields completed. Physical, functional, and system assessment levels recorded. Re-attack recommendation linked to BDA record when applicable. BDA report routed to FSCOORD for review.

**PROCEDURE:**

1. Navigate to the MSS Fires Workspace, select the Targeting module, and open the BDA log.
2. Locate the fire mission record corresponding to the completed strike.
3. Select "Enter BDA" linked to that mission record.
4. Enter the following required fields:
   a. Target number and type (auto-populated from mission record — confirm accuracy).
   b. BDA collection source (IMINT, SIGINT, observer, HUMINT, multisource).
   c. BDA collection DTG.
   d. Physical destruction assessment (percentage and basis).
   e. Functional damage assessment (FMC/PMCI/PMCII/NMC rating with basis).
   f. System disruption assessment (narrative and C1-C4 rating).
5. Attach any supporting documentation (imagery, report text) IAW OPSEC and classification guidance.
6. Enter re-attack recommendation: Yes/No. If Yes, state basis and proposed attack method.
7. Submit BDA record for FSCOORD review.
8. FSCOORD reviews and approves BDA record. If re-attack recommended, FSCOORD routes to targeting for TWG consideration or approves immediate re-attack per ROE.
9. Update target record in the target library: change target status from "Engaged" to "Assessed" with BDA category entered.
10. If re-attack approved, link new mission record to original target record and re-attack recommendation.

---

### 2-6. D3A as Data Lifecycle

2-22. The D3A targeting methodology maps directly onto the data platform lifecycle. Each phase of D3A produces, consumes, and transforms specific data products within MSS. Understanding this mapping enables fires personnel to treat D3A not merely as a doctrinal process but as a data pipeline — where each phase depends on the data quality of the preceding phase and produces structured outputs for the next.

2-23. Table 2-3 maps each D3A phase to its corresponding MSS platform function and key data products. Fires staff should use this table to identify where data gaps in the targeting cycle originate and which platform functions to inspect when targeting products are incomplete or stale.

**Table 2-3: D3A as Data Lifecycle — Platform Function Mapping**

| D3A Phase | Data Platform Function | Key Data Products |
|---|---|---|
| Decide | Requirements analysis, target nomination, priority ranking | HPTL, TSS, AGM |
| Detect | Collection management, sensor tasking, feed integration | ICSM, NAI/TAI tracking, target confidence records |
| Deliver | Execution tracking, engagement management, asset-to-target matching | Fire missions, FSEM updates, BDA requests |
| Assess | Effects assessment, feedback loop, re-attack recommendation | BDA reports, MOE/MOP metrics, FIREP data |

> *Source: FM 3-60, Army Targeting (August 2023)*

2-24. When any column in Table 2-3 is incomplete — when the Decide phase produces an HPTL with no linked collection requirements, or when the Assess phase records BDA without MOE/MOP linkage — the targeting cycle degrades. MSS makes these gaps visible. The targeting officer's job is to act on them.

---

### 2-7. FIVE-O Target Taxonomy

2-25. FM 3-60 establishes the FIVE-O taxonomy for categorizing targets: **Facilities, Individuals, Virtual, Equipment, Organizations**. This taxonomy is not merely a doctrinal classification scheme — it maps directly to ontology object types in the MSS data platform.

2-26. Table 2-4 maps FIVE-O categories to their MSS ontology equivalents and provides examples relevant to fires targeting.

**Table 2-4: FIVE-O Target Taxonomy — MSS Ontology Mapping**

| FIVE-O Category | Definition | MSS Object Type | Example Targets |
|---|---|---|---|
| Facilities | Fixed or semi-fixed structures and installations | Infrastructure object | C2 bunkers, ammo supply points, bridges, radar sites |
| Individuals | Persons of significance to OPFOR capability | Person object | Key leaders, technical specialists, forward observers |
| Virtual | Non-physical targets in the information domain | Cyber/information object | Communication networks, data links, EW emitters |
| Equipment | Material systems and platforms | Equipment/asset object | Artillery systems, AD launchers, EW platforms, vehicles |
| Organizations | Military units and organizational structures | Organization object | BN-level units, fires batteries, logistics elements |

> *Source: FM 3-60, Army Targeting (August 2023)*

2-27. When building or maintaining the target library in MSS, every target entry must map to one FIVE-O category. This ensures consistent data structure across echelons and enables automated aggregation of targeting data from subordinate to higher fires cells. A target that does not fit a FIVE-O category is either miscategorized or not yet sufficiently developed for nomination.

> **NOTE: FIVE-O categories are mutually exclusive for target record purposes. A radar site is an Equipment target, not a Facilities target, even though it may be co-located with a fixed structure. Assign the category based on the primary targeting objective — what effect the commander seeks to achieve against that specific target.**

---

### 2-8. TTLODAC Fire Mission Data Schema

2-28. Every fire mission processed through the fires system follows the TTLODAC data schema: **Target, Task, Location, Observer, Delivery system, Attack guidance, Communications**. TTLODAC is the structured data record for fire mission processing IAW FM 3-09. MSS fire mission records mirror this schema.

2-29. Table 2-5 defines each TTLODAC element, its MSS data field, and the responsible role.

**Table 2-5: TTLODAC Fire Mission Data Schema**

| TTLODAC Element | Definition | MSS Data Field | Responsible Role |
|---|---|---|---|
| Target | What is being engaged — target number, type, and description | Target ID, target type, FIVE-O category | Targeting officer / FSO |
| Task | Fire-for-effect, suppression, illumination, smoke, or other mission type | Mission type code | FSO / FDO |
| Location | Grid coordinates, altitude, and target location error (TLE) category | Grid reference (MGRS), altitude, TLE category | Observer / targeting officer |
| Observer | Who is observing the target and will adjust fires or confirm effects | Observer call sign, position, observation method | FSO / JTAC / FO |
| Delivery system | Which weapon system is assigned to execute the mission | Asset ID, weapon type, unit | FDO / FSCOORD |
| Attack guidance | ROE constraints, desired effects, CDE category, FSCM compliance | AGM linkage, ROE flags, CDE category | FSCOORD / SJA |
| Communications | Frequencies, call signs, and digital links between observer and firing unit | PACE plan entries, net assignments | FSO / FDO |

> *Source: FM 3-09, Fire Support and Field Artillery Operations (August 2024)*

2-30. TTLODAC completeness is a fires safety issue. An incomplete TTLODAC record — missing observer data, absent ROE flags, or stale location information — creates risk of fratricide, collateral damage, or ROE violation. MSS enforces required field completion on fire mission records. Do not override required field prompts to expedite mission processing.

> **WARNING: A fire mission record in MSS with an empty or defaulted Attack Guidance field has no ROE validation. Never clear a fire mission for execution without confirming that Attack Guidance reflects current ROE and FSCM constraints. The system will accept the record — it will not reject it on ROE grounds. ROE compliance is a human responsibility, not a system function.**

---

### 2-9. CARVER Target Value Analysis

2-31. The CARVER matrix is a structured scoring methodology for target value analysis IAW FM 3-60, Appendix G. CARVER evaluates targets across six criteria: **Criticality, Accessibility, Recuperability, Vulnerability, Effect, Recognizability**. Each criterion is scored on a 1–5 scale. The aggregate score provides a quantitative basis for target prioritization.

2-32. CARVER is directly implementable as an analytical pipeline in MSS. Each criterion maps to a scored data field on the target record. Automated scoring models can pre-populate CARVER values based on target type and known characteristics; the targeting officer validates and adjusts scores based on current intelligence.

2-33. Table 2-6 defines each CARVER criterion and its MSS implementation.

**Table 2-6: CARVER Target Value Analysis — Criteria and MSS Implementation**

| CARVER Criterion | Definition | Scoring Basis (1–5) | MSS Implementation |
|---|---|---|---|
| Criticality | How important is the target to OPFOR capability? | 1 = minimal impact; 5 = catastrophic loss of capability | Linked to OPFOR OOB; scored against functional dependency |
| Accessibility | Can the target be reached by available fires means? | 1 = deeply protected; 5 = fully accessible to multiple systems | Computed from range rings, terrain mask, AD threat overlay |
| Recuperability | How quickly can the OPFOR replace or repair the target? | 1 = immediate replacement; 5 = irreplaceable within campaign timeline | Intelligence estimate; scored by targeting officer |
| Vulnerability | How susceptible is the target to available munitions? | 1 = hardened/deeply buried; 5 = soft/exposed | Munitions-target pairing analysis; scored by FDO/targeting |
| Effect | What is the broader operational effect of engaging the target? | 1 = localized effect only; 5 = cascading effect across OPFOR systems | Linked to commander's desired effects and HPTL priority |
| Recognizability | Can the target be positively identified by available sensors? | 1 = extremely difficult to identify; 5 = readily identifiable | Collection capability assessment; ISR coverage overlay |

> *Source: FM 3-60, Appendix G, Army Targeting (August 2023)*

2-34. CARVER scoring in MSS supports the targeting working group (TWG) by providing a quantitative input to HPTL prioritization. The CARVER score does not replace the commander's judgment — it informs it. A target with a high CARVER score that the commander deprioritizes remains deprioritized. The score is an analytical tool, not an authority.

2-35. To build a CARVER pipeline in MSS, the fires analyst configures a scoring model that pulls target attributes from the target library, computes preliminary CARVER scores based on standing criteria, and presents the scored target list to the targeting officer for validation before each TWG. See TM-40G (ORSA) for analytical pipeline construction techniques applicable to CARVER implementation.

> **NOTE: CARVER scores are perishable. A target scored as highly accessible (A=5) today may become inaccessible (A=1) tomorrow if OPFOR repositions AD assets or the weather degrades sensor coverage. Re-score CARVER at each targeting cycle, not once per operation.**

---

## CHAPTER 3 — FIRE SUPPORT PLANNING IN MSS

### 3-1. Overview

> **BLUF: MSS is the platform where the fire support plan lives as a data product — not just a document. FSCMs, the FSEM, and fires synchronization data must be maintained in MSS as live, current products throughout the operation.**

3-1. Fire support planning produces the products that synchronize fires with maneuver and enable the FSCOORD to execute the fires plan. In MSS, fire support planning products are data objects, not static documents. They update as the operation changes.

3-2. The primary fire support planning products maintained in MSS are:
- The fire support plan (FSPLAN) — fires scheme and priorities
- FSCM overlay — all coordination measures published geospatially
- Fire support execution matrix (FSEM) — task-organized fires tasks by phase and event
- Radar zone management — Cued Target Zone (CTZ), Attack Target Zone (ATZ), and exclusion zones
- Counterfire plan — sensor-to-shooter chain for counterfire engagements

---

### 3-2. Fire Support Plan Data Management

3-3. The fire support plan in MSS is organized as a linked set of data objects: the commander's fires concept, the FSCM overlay, the FSEM, and the fires synchronization matrix. Each component is maintained separately and linked within the MSS fires workspace.

3-4. FSPLAN management in MSS requires:
- FSPLAN version control: each published revision carries a version number and DTG
- Subordinate access: all subordinate FSOs have read access to the parent FSPLAN
- Change notification: when the FSPLAN is updated, MSS sends automated notifications to linked subordinate workspaces
- Archive: previous FSPLAN versions are archived, not deleted — they support operational review and legal requirements

3-5. The FSPLAN is not an upload of a Word document. The data within the plan — target priorities, fires tasks, coordination measures, fire support tasks (FST) — is entered as structured data in MSS so it can drive other fires modules.

---

### 3-3. FSCM Visualization

3-6. Fire support coordination measures (FSCMs) are the legal and safety boundaries within which fires are cleared. They include permissive measures that allow fires (free fire area, attack by fire position) and restrictive measures that limit or prohibit fires (no fire area, restrictive fire area, restrictive fire line, fire support coordination line, etc.).

3-7. In MSS, FSCMs appear as a geospatial overlay on the fires operational picture. Each FSCM carries:
- FSCM type and identifier
- Geographic boundary (line, area, or point)
- Establishing headquarters
- Effective period (from DTG to DTG or until further notice)
- Publication DTG (when it was entered into MSS)
- Approval authority

3-8. FSCMs in the overlay are color-coded by type and currency. Active, current FSCMs display in standard colors. FSCMs approaching expiration display in a warning color. Expired FSCMs display in a degraded color and require renewal or removal.

3-9. The following coordination measures are maintained in the MSS FSCM overlay:

**Table 3-1: FSCM Types and Definitions**

| FSCM | Type | Definition | Who Establishes | Safety Implication |
|------|------|-----------|----------------|-------------------|
| FSCL (Fire Support Coordination Line) | Permissive | A line short of which all fires are coordinated by land forces; long of which all fires are coordinated with the air component | Corps or JTF | Fires across FSCL require joint coordination |
| RFL (Restrictive Fire Line) | Restrictive | A line established between converging friendly forces; fires across the RFL require coordination | Higher HQ | Fires near RFL require cross-unit coordination |
| NFA (No Fire Area) | Restrictive | An area where no fires are permitted | Division/Corps | No fires of any kind without specific approval from NFA-establishing HQ |
| RFA (Restrictive Fire Area) | Restrictive | An area with specific restrictions; fires permitted with established HQ approval | Division/Corps | Fires require approval from RFA-establishing HQ |
| FFA (Free Fire Area) | Permissive | An area where fires may be delivered without additional coordination | Division/Corps | Fires permitted; confirm FFA still active before clearing |
| ATI (Area Target Indicator) | Coordination | Marks an area of engagement activity for identification purposes | Fires cell | Informational; does not restrict or permit fires |
| ACA (Airspace Coordination Area) | Airspace | Reserved airspace for aircraft; fire missions through ACA require specific coordination | G3/Air | Fire through ACA requires airspace coordination authority approval |
| SEAD Corridor | Airspace | Defined airspace for SEAD aircraft ingress/egress | Corps/AF liaison | Fire in SEAD corridor requires explicit SEAD coordination approval |
| FA (Final Approach) | Airspace | A low-altitude airspace for aircraft nap-of-earth operations | Aviation/G3 Air | Fire near FA requires aviation coordination |

---

### 3-4. 13F FSO Workflow in MSS

3-10. The direct support FSO (13F) is the primary fires interface between the maneuver battalion or brigade and the fires system. In MSS, the FSO workflow follows the fires cycle: receive request → confirm FSCM currency → coordinate clearance → track execution → enter BDA.

3-11. Call for fire (CFF) request submission in MSS: The 13F enters CFF data into the MSS fires module linked to the requesting unit, target record, and applicable FSCM overlay. This creates a linked record enabling the fires cell to track execution.

3-12. Clearance of fires workflow: Before clearing any fire mission, the FSO:
1. Checks the FSCM overlay in MSS for active measures near the target location
2. Confirms FSCM currency by checking the publication DTG and effective period
3. If near an FSCM boundary, contacts the establishing headquarters to confirm status
4. Clears fires per approved ROE and records the clearance in the MSS CFF log
5. Tracks mission execution and enters BDA on mission completion

3-13. BDA entry: The FSO enters BDA in MSS within the time standard established by unit SOP (typically two hours of fires execution or one hour of BDA collection).

---

### 3-5. Fire Support Execution Matrix in MSS

3-14. The FSEM is the fires synchronization product that sequences fires tasks by phase, objective, and event. In MSS, the FSEM is a structured data table linked to the FSPLAN and to individual mission records.

**Table 3-2: FSEM Column Definitions**

| FSEM Column | Definition | Data Owner | Update Trigger |
|------------|-----------|-----------|---------------|
| Phase/Event | Operational phase or named event triggering fires task | FSCOORD | Phase change, order update |
| Fire Support Task | Specific fires task to be executed | FSCOORD / FSO | Planning update |
| Target or Area | Target number, type, or geographic area | Targeting Officer | Target list update |
| System Assigned | Fires system tasked to execute | FSCOORD | Fires synchronization |
| Method/Munition | Delivery method and munition type | Targeting/FSCOORD | AGM update |
| Timing | Execute timing (on order, at time, on call) | FSCOORD | Planning update |
| Coordination Required | Airspace, FSCM, or unit coordination requirements | FSO / FSCOORD | Per mission |
| Status | Planned, Assigned, Executing, Complete, Cancelled | Fires cell | On-event updates |
| BDA | Link to BDA record upon completion | 13F FSO | Post-execution |

---

### 3-6. Radar Zone Management in MSS

3-15. Radar zones define the geographic areas within which Q-36 and Q-37 Firefinder radars collect counterfire data. Zone management is a fires staff responsibility integrated into the fires planning process.

3-16. Two primary radar zone types appear in MSS:
- **Cued Target Zone (CTZ):** Area where radar is tasked to detect and track targets for counterfire. Multiple CTZs may be active simultaneously. CTZs are oriented on enemy indirect fire avenues of approach and expected firing positions.
- **Attack Target Zone (ATZ):** A priority subset of the CTZ. The radar prioritizes detection and reporting of targets within the ATZ. ATZ placement reflects the HPTL and counterfire plan priorities.

3-17. Radar zone data in MSS shows current zone boundaries as overlays on the fires picture, radar assignment against zones, and coverage gaps where radar does not currently provide counterfire coverage. The counterfire officer uses this display to identify collection gaps and recommend radar positioning adjustments.

---

### 3-7. Counterfire Plan Management in MSS

3-18. The counterfire plan defines the fires cell's approach to detecting, nominating, and engaging enemy indirect fire systems. In MSS, the counterfire plan is maintained as a linked set of data elements: radar zone assignments, counterfire target categories on the HPTL, the counterfire approval chain, and the historical counterfire log from the C-RAM tracker.

3-19. Counterfire plan data maintained in MSS:
- Radar assignments: which radar is assigned to which CTZ/ATZ, current radar status, and zone coverage display
- Counterfire target categories: artillery, mortar, and rocket categories on the HPTL with associated AGM guidance
- Counterfire approval thresholds: criteria for immediate approval (specific POO confidence levels, weapon types, locations) vs. FSCOORD review
- Historical counterfire data: POO track history enabling pattern analysis of enemy indirect fire patterns and preferred firing positions

3-20. Counterfire pattern analysis in MSS: Over multiple operations periods, POO data accumulates in the C-RAM tracker. The counterfire officer reviews this historical data to identify enemy preferred firing positions, typical engagement ranges, and TTPs that can be countered with pre-planned counterfire zones. MSS enables this analysis by maintaining the POO historical record with geographic display — a capability that did not exist when counterfire data was maintained in paper logs.

3-21. Pre-planned counterfire in MSS: When counterfire pattern analysis identifies a frequently used enemy firing position, the counterfire officer can pre-plan a counterfire mission in the FSEM linked to that position. The pre-planned mission carries a confirmed target record, pre-approved munition and weapons system, and immediate execution authority. When the Q-36 reports that position again, the counterfire officer initiates the pre-planned mission with minimal coordination delay.

> **CAUTION: Pre-planned counterfire missions against frequently used firing positions must be reviewed against current FSCM data and ROE before each execution. An area that was a valid counterfire target last week may have a new NFA overlay or changed ROE this week. Never execute a pre-planned counterfire mission without confirming current FSCM status and ROE applicability.**

---

**TASK: Build and Maintain FSCM Overlay in MSS**

**CONDITIONS:** FSCOORD or fires cell targeting officer, with access to the MSS fires workspace and FSCM overlay module. Current operations order (OPORD) or fragmentary order (FRAGO) with fires annex received. FSCMs approved by the FSCOORD and ready for publication.

**STANDARDS:** All FSCMs from the approved fires annex are entered in MSS with correct type, geographic boundaries, effective period, and establishing headquarters. FSCM overlay is published to all subordinate fires workspaces. Expired FSCMs are archived. An FSCM update is published within one hour of any FSCM change approval. Subordinate FSOs are notified of updates via MSS notification and alternate means per PACE plan.

**PROCEDURE:**

1. Navigate to the MSS Fires Workspace and select the FSCM Overlay module.
2. Review the current overlay against the approved fires annex for the current OPORD or FRAGO.
3. For each new FSCM to be added:
   a. Select "Add FSCM" and choose the correct FSCM type from the dropdown.
   b. Enter the FSCM identifier (e.g., NFA-01, RFA-ALPHA).
   c. Draw or enter the geographic boundary (line, polygon, or point) using MSS geospatial tools or manual coordinate entry.
   d. Enter the establishing headquarters.
   e. Enter the effective period: from DTG and to DTG (or "Until Further Notice").
   f. Enter the approving authority name and rank.
   g. Enter any specific fires restriction or permission text associated with the FSCM.
4. For each FSCM requiring modification:
   a. Open the existing FSCM record.
   b. Edit the geographic boundary, effective period, or restriction text as approved.
   c. Update the version number and enter the modification DTG.
5. For each expired or cancelled FSCM:
   a. Change the status from "Active" to "Expired" or "Cancelled."
   b. Archive the FSCM record — do not delete.
6. Verify the overlay by zooming to each FSCM boundary and confirming correct placement.
7. Publish the updated overlay to all subordinate fires workspaces.
8. Send MSS notification and alternate means notification (radio, voice) to all subordinate FSOs.
9. Record the FSCM update in the fires cell log with DTG and FSCOORD confirmation.

> **WARNING: Do not publish an FSCM to MSS without FSCOORD approval. Unauthorized FSCM publication can create false fires restrictions or false permission to fire, endangering friendly forces.**

---

## CHAPTER 4 — FIRE DIRECTION AND MISSION PROCESSING

### 4-1. Overview

> **BLUF: FDC personnel use MSS to track fire missions, record ammunition consumption, and maintain Class V status. AFATDS remains the authoritative system for ballistic computation. MSS is the fires staff visibility and tracking layer — not the fire direction system.**

4-1. Fire direction is the computation and technical processing of fire missions from receipt of the call for fire through execution of fire commands. Fire direction in USAREUR-AF formations runs through AFATDS at the battery FDC level. MSS provides fire mission visibility to fires staffs above FDC level.

4-2. FDC personnel (13J, 13P) use MSS to:
- Record and track fire missions in the fire mission log
- Report ammunition consumption and current ammunition status
- Coordinate with the fires cell on priority mission assignment
- Log fire mission records for fires assessment and BDA linkage

---

### 4-2. Fire Mission Data Tracking

4-3. The MSS fire mission log is the fires staff's record of all fire missions executed within the formation. Each record carries the data fields required to support BDA linkage, fires assessment, and operational review.

4-4. Fire mission records in MSS are initiated by the fires cell when a mission is assigned and completed by the FDC when the mission executes and fires cease. This shared ownership ensures the record is both assigned (fires cell perspective) and executed (FDC perspective).

**Table 4-1: Fire Mission Log Fields**

| Field | Definition | Entry By | Required/Optional |
|-------|-----------|----------|-------------------|
| Mission Number | Assigned mission identifier (unit-unique) | FDC / Fires cell | Required |
| Requesting Unit | Unit submitting the CFF | FSO / Fires cell | Required |
| Target Number | Linked target list or target record identifier | Fires cell | Required |
| Target Type | OPFOR system, activity, or area description | Fires cell | Required |
| Target Location | Grid coordinates (8+ digit MGRS) | FDC / FSO | Required |
| Weapon System | Howitzer, MLRS/HIMARS, mortar, other | FDC | Required |
| Munition Type | Projectile type, fuze, charge (from AFATDS) | FDC | Required |
| Rounds Expended | Number of rounds fired per mission | FDC | Required |
| Time of Request | DTG mission was submitted | FSO / Fires cell | Required |
| Time of First Round | DTG first round fired | FDC | Required |
| Time of Fires Cease | DTG cease fire called | FDC | Required |
| Response Time | Calculated: Time of First Round minus Time of Request | Auto-calculated | Auto |
| Mission Status | Pending, Executing, Complete, Cancelled | FDC / Fires cell | Required |
| BDA Link | Link to BDA record when available | Targeting Officer | Optional (required when BDA collected) |
| Remarks | Non-standard data: airspace conflicts, mission deviations, safety issues | FDC | Optional |

---

### 4-3. 13P/13J Workflow in MSS

4-5. The 13P (MLRS Operations/Fire Direction Specialist) and 13J (Fire Control Specialist) use MSS to track missions within their sections and report execution data to the fires cell. The 13J or 13P workflow in MSS does not replace AFATDS — it supplements it by providing the fires staff visibility of execution status.

4-6. On receipt of a fire mission in AFATDS:
1. The 13J/13P confirms the mission in AFATDS for ballistic computation.
2. The 13J/13P updates the corresponding MSS mission record status to "Executing."
3. On completion, the 13J/13P enters rounds expended, munition type, and time of fires cease in MSS.
4. If there are mission deviations (range safety abort, target shift, mission cancellation), the 13J/13P enters remarks in the MSS record.

4-7. The FDC does not use MSS to compute fire commands. Fire commands come from AFATDS. MSS records what AFATDS computes and executes.

> **NOTE: AFATDS remains the authoritative system for all ballistic computation. MSS fire mission records reflect reported data from AFATDS, not computed fire commands. Discrepancies between AFATDS records and MSS records are resolved in favor of AFATDS unless the discrepancy is a data entry error.**

---

### 4-4. Ammunition Status and Consumption Tracking

4-8. Class V (ammunition) tracking in MSS provides the fires cell and FSCOORD visibility of ammunition loads across the formation. MSS Class V data supports fires synchronization by ensuring the FSCOORD knows whether assigned systems have the ammunition to execute assigned missions.

4-9. Daily ammunition status updates in MSS are a mandatory fires reporting requirement. Each battery or platoon reports its on-hand ammunition by type and quantity at the times established by unit SOP. The fires cell aggregates this data across the formation for FSCOORD review.

4-10. Ammunition consumption tracking occurs at the mission level through the fire mission log. Each completed mission record includes rounds expended by type. MSS calculates running consumption rates automatically from fire mission records linked to the start of the reporting period.

**Table 4-2: Class V (Ammunition) Data Fields**

| Field | Definition | Unit of Measure | Update Frequency |
|-------|-----------|----------------|-----------------|
| System | Fires system (e.g., M109A7, M270A2, M1064, Patriot PAC-3) | System identifier | On status change |
| Unit | Reporting unit (battery/platoon) | Unit ID | On status change |
| Munition Type | Specific round/missile type (e.g., M549A1 HE, M30A1 GMLRS, MSE) | By type | Daily + on consumption |
| Quantity on Hand | Rounds/missiles currently on hand | Each | Daily + post-mission |
| Basic Load Percentage | On-hand quantity as % of authorizedbasic load | Percentage | Auto-calculated |
| Rounds Expended (Period) | Total rounds expended since last status update | Each | Auto-calculated from mission log |
| Resupply Requested | Quantity of each type on current resupply request | Each | On request submission |
| Resupply Status | Pending, In Transit, Received | Status field | On change |
| Location | Current ammunition storage position | 8-digit MGRS | On movement |
| Remarks | Non-standard ammunition, special authorization, deviations | Text | As needed |

---

**TASK: Conduct Daily Ammunition Status Update in MSS**

**CONDITIONS:** 13J or 13P, with access to the MSS fire direction module. Physical ammunition count completed or confirmed from battery/platoon inventory. Unit SOP-specified update time reached.

**STANDARDS:** All ammunition lines for all assigned munition types updated in MSS within 30 minutes of the unit SOP-specified update time. On-hand quantities accurate within one round per line. Any discrepancies from the previous status annotated in remarks. Any on-hand quantity below 50% of basic load flagged to the fires cell immediately.

**PROCEDURE:**

1. Complete or confirm the physical ammunition count at the battery/platoon level.
2. Navigate to the MSS Fire Direction module and select Class V Status.
3. Open the ammunition status record for your unit.
4. For each munition type on the unit's authorized basic load:
   a. Enter the current on-hand quantity.
   b. Confirm the munition type code is correct.
   c. Verify the basic load percentage auto-calculates correctly.
5. If any munition type is below 50% of basic load, flag the line as "Low" and notify the fires cell immediately via MSS and alternate means.
6. Enter the quantity expended since last update in the "Expended Since Last Report" field.
7. If there is an active resupply request, update its status (Pending/In Transit/Received).
8. Enter remarks for any non-standard items, deviations, or issues.
9. Submit the ammunition status update. The fires cell receives automatic notification.
10. Record update submission in the FDC log with DTG and signature.

---

### 4-5. AFATDS-MSS Data Handoff Procedures

4-11. AFATDS and MSS exchange data through a defined interface maintained by the unit S6 and fires system administrators. The handoff procedures ensure fires staff visibility in MSS reflects what AFATDS has computed and executed.

> **NOTE: The AFATDS-MSS interface reliability varies across units and network environments. The fires cell must not assume the interface is active — it must verify interface status daily. When the interface drops, fires staff visibility in MSS becomes stale immediately. Fires cells that discover the interface has been inactive for 12 hours should assume their MSS fire mission log and ammunition data are unreliable and reconcile manually before the next fires allocation decision.**

4-12. Data from AFATDS that flows into MSS:
- Fire mission records (mission number, target data, weapon, rounds)
- Ammunition consumption (auto-update when interface is active)
- Position data for reporting FA units (for asset status display)

4-13. Data that does NOT flow from MSS to AFATDS:
- HPTL and AGM data (fires staff planning products, not FDC products)
- FSCM overlays (MSS FSCM is a staff visualization product; AFATDS maintains its own FSCM input)
- BDA records (BDA is a fires staff function, not FDC)

4-14. When the AFATDS-MSS interface is degraded or inactive, FDC personnel manually update MSS fire mission records. Manual updates must occur within 30 minutes of mission execution. See Chapter 10 for degraded operations procedures.

---

## CHAPTER 5 — AIR DEFENSE OPERATIONS IN MSS

### 5-1. Overview

> **BLUF: MSS supports AMD operations by providing an integrated air picture, CAL/DAL management, HIMAD/SHORAD coordination, and engagement authority status tracking. AMD engagement decisions are a command function — MSS informs those decisions, it does not make them.**

5-1. Air and missile defense (AMD) operations protect the force from air and missile attack. The AMD task force commander synchronizes Patriot (HIMAD), SHORAD, and M-SHORAD systems to provide layered defense of the defended area. MSS supports AMD operations by integrating the air picture, maintaining the defended asset list, and providing the AMD TF commander visibility of engagement status across all systems.

5-2. AMD operations in MSS are organized around four functions:
- Air picture display: track visualization, identification management, threat display
- Defense design data: CAL/DAL management, defended area overlay, coverage analysis
- Engagement authority tracking: ROE status, engagement authority delegation, status display
- Status reporting: system readiness, engagement log, daily AMD SITREP data

---

### 5-2. Air Picture Visualization in MSS

5-3. The MSS air picture displays air tracks reported by AMD sensors, AMDWS, and IBCS. Each track carries identification (friend, hostile, unknown, assumed friend, suspect, pending, assumed hostile) and data including speed, altitude, heading, and identification basis.

5-4. Track identification in MSS follows the standard track ID categories IAW ATP 3-01.8. Identification is not made in MSS — it is reported from AMD systems and displayed in MSS. The difference is operationally critical: the displayed identification reflects what AMD systems have assessed, not an independent MSS assessment.

5-5. The AMD TF commander and staff use the MSS air picture to:
- Monitor the overall air situation across the defended area
- Identify coverage gaps in the AMD defensive umbrella
- Track inbound threats and system engagement status
- Coordinate HIMAD/SHORAD engagement responsibilities

5-6. The MSS air picture is supplemental to primary AMD systems. AMDWS and IBCS are the authoritative AMD command and control systems. MSS receives their output for fires staff integration and commander visualization.

> **WARNING: AMD engagement authority is a command function. MSS displays track data and engagement status. It does not authorize weapon release. Weapon release authority follows the established ROE and the commander's delegated engagement authority — not MSS displays. Basing engagement decisions solely on MSS track data without validating against IBCS or AMDWS is a violation of AMD procedures.**

---

### 5-3. 14A AMD Officer Workflow in MSS

5-7. The 14A AMD officer maintains the AMD defense design and tracks engagement authority status in MSS. The 14A workflow covers:
- Defense design: entry and maintenance of the defended area, CAL/DAL, and AMD coverage display
- Engagement authority tracking: current ROE status, delegated engagement authority for each system
- Reporting: daily AMD status roll-up and SITREP data

5-8. Defense design in MSS begins with the defended area overlay. The 14A enters the defended area polygon, places defended asset icons at their reported positions, and assigns each asset to its applicable AMD coverage tier (HIMAD, SHORAD, or point defense).

5-9. The 14A reviews the coverage analysis tool in MSS to identify sectors where the defense design has coverage gaps. Coverage gaps drive AMD positioning recommendations and are reported to the AMD TF commander.

---

### 5-4. HIMAD/SHORAD Integration

5-10. HIMAD (Patriot) and SHORAD/M-SHORAD systems operate at different engagement envelopes and in different engagement authorities. Integration of these systems in MSS requires maintaining both systems' status and engagement authority in a way that supports joint engagement planning.

5-11. Patriot data in MSS includes battery location, sector of fire, system readiness (FMC/PMCI/PMCII/NMC), missile inventory (PAC-2, PAC-3 MSE on hand), and current engagement authority status.

5-12. SHORAD (M-SHORAD, MANPADS, SHORAD gun) data in MSS includes platoon/team position, weapon type, system readiness, and engagement authority status.

5-13. Coordination between HIMAD and SHORAD in MSS ensures that the AMD TF commander has a single display of all AMD assets and their engagement authorities, enabling the commander to direct engagement responsibilities and deconflict simultaneous engagements.

---

### 5-4a. IBCS Integration and Data Sharing

5-13a. The Integrated Air and Missile Defense Battle Command System (IBCS) is the Army's AMD network centric battle management system. IBCS integrates sensors and weapons across the AMD force and provides the AMD battle command capability for Patriot and future AMD systems. MSS receives IBCS engagement status data through the IBCS-MSS data interface.

5-13b. Data IBCS provides to MSS:
- Air track picture: all tracks tracked by the IBCS sensor network (identification, speed, altitude, heading)
- Engagement status: active engagements, weapon assignments, intercept status
- System readiness: Patriot battery fire control readiness as reported through IBCS

5-13c. Data MSS provides that IBCS does not:
- Integrated fires picture: land fires, FSCM overlays, and AMD data in a single display
- CAL/DAL management: MSS is the authoritative CAL/DAL data platform
- Fires assessment records: BDA and fires effectiveness data does not reside in IBCS

5-13d. The AMD TF commander uses both IBCS and MSS. IBCS for AMD execution and AMD-specific battle command. MSS for integrated fires visualization, CAL/DAL management, and AMD reporting. These are complementary tools, not competing ones. AMD personnel who treat IBCS and MSS as alternatives will use neither effectively. They are designed for different but complementary functions in the AMD operations workflow.

---

### 5-5. ROE Management and Engagement Authority Tracking

5-14. Rules of engagement (ROE) for AMD are among the most sensitive and consequential data elements in MSS. ROE status determines which systems can engage which track categories without further coordination. Changes to ROE authority in MSS must be initiated only by the AMD TF commander or higher, and must be confirmed against the written ROE authorization before taking effect.

5-15. Engagement authority in MSS is tracked at three levels:
- **Weapons Free:** Systems may engage any track not positively identified as friendly without specific commander approval (used only in the most threatening environments and only with explicit commander authorization)
- **Weapons Tight:** Systems may engage tracks positively identified as hostile (normal operating condition for most AMD operations)
- **Weapons Hold:** Systems may not engage except in self-defense (most restrictive; used in specific areas or conditions per commander directive)

5-16. Engagement authority changes are logged in MSS with the authorizing officer, DTG, and applicable geographic area or unit. The AMD TF commander approves all engagement authority changes; the 14A enters and maintains the record in MSS.

---

### 5-6. Critical Asset List (CAL) / Defended Asset List (DAL) Management

5-17. The Critical Asset List (CAL) identifies assets whose loss would critically affect the operational effectiveness of the force. The Defended Asset List (DAL) is the subset of CAL assets that AMD resources can actually protect given available means. CAL/DAL management is a continuous fires staff process — not a one-time planning product.

5-18. CAL/DAL data in MSS includes:
- Asset identification, type, and location
- CAL priority ranking
- DAL inclusion/exclusion status with basis
- AMD system assigned to defend each DAL asset
- Coverage confirmation (is the assigned AMD system positioned to defend the asset?)
- CAL/DAL review cycle: updated at each operational phase change and on significant force structure or positioning changes

---

**TASK: Update AMD Status and CAL/DAL in MSS**

**CONDITIONS:** 14A AMD officer or AMD operations NCO, with access to the MSS AMD module. Current AMD system status reports received from all subordinate Patriot batteries and SHORAD/M-SHORAD elements. Current CAL from the fires cell or higher headquarters.

**STANDARDS:** All AMD systems updated in MSS with current readiness status, missile inventory, position, and engagement authority within one hour of the unit SOP reporting time. CAL/DAL reflects current commander-approved list. Any system reporting PMCII or NMC status is flagged immediately to the AMD TF commander. CAL/DAL discrepancies (assets on CAL but not on DAL due to coverage gaps) are annotated in MSS and reported to the AMD TF commander.

**PROCEDURE:**

1. Collect status reports from all Patriot batteries and SHORAD/M-SHORAD elements (via MSS system status reports, radio, or direct coordination).
2. Navigate to the MSS AMD module and select System Status.
3. For each Patriot battery:
   a. Open the battery record.
   b. Update readiness status (FMC/PMCI/PMCII/NMC) with basis and DTG.
   c. Update PAC-2 and PAC-3 MSE missile on-hand quantities.
   d. Confirm or update battery position (8-digit MGRS).
   e. Confirm sector of fire and engagement authority status.
4. For each SHORAD/M-SHORAD element:
   a. Open the element record.
   b. Update readiness status and missile/gun inventory.
   c. Confirm position and engagement authority.
5. Navigate to the CAL/DAL module.
6. Review the current CAL against the approved CAL from the fires cell or higher HQ.
7. For each CAL asset:
   a. Confirm asset position and status are current.
   b. Confirm the assigned AMD system is capable of and positioned for defense.
   c. If the assigned system is degraded or repositioned, update the coverage assessment and flag any coverage gap.
8. Update the DAL to reflect what AMD resources can currently defend given current system status and positioning.
9. If any CAL asset has moved from the DAL due to coverage gaps, annotate in MSS and report immediately to AMD TF commander.
10. Submit AMD status update. Record update in the AMD operations log with DTG.

---

**Table 5-1: AMD Systems and MSS Data Interface**

| AMD System | MSS Data Received | MSS Data Entered | Primary Owner in MSS | Update Frequency |
|-----------|-------------------|-----------------|---------------------|-----------------|
| Patriot (PAC-2/PAC-3) | Engagement status (from IBCS/AMDWS) | Battery readiness, missile inventory, position | 14A / 14E | Daily + on-event |
| M-SHORAD | Engagement status (from FAAD C2) | Platoon readiness, system status, position | 14A / 14S | Daily + on-event |
| SHORAD (Avenger, Stinger) | Engagement status reports | Team readiness, weapon inventory, position | 14A / 14S | Daily + on-event |
| IBCS | Track picture (via data feed) | N/A (IBCS is source system) | IBCS system admin | Continuous |
| AMDWS | AMD common operating picture | N/A (AMDWS is source system) | S6/AMD S6 | Continuous |
| FAAD C2 | SHORAD common picture | N/A (FAAD C2 is source system) | S6/AMD S6 | Continuous |

---

## CHAPTER 6 — COUNTER-ROCKET, ARTILLERY, MORTAR (C-RAM) AND SENSOR OPERATIONS

### 6-1. Overview

> **BLUF: C-RAM operations use radar data to detect incoming fires, generate counterfire nominations, and track hostile fire events. The 13R and 13S are the primary MSS users for sensor and meteorological data. Speed is the critical variable — counterfire data is perishable.**

6-1. Counter-rocket, artillery, mortar (C-RAM) operations detect, warn, and when possible intercept or defeat incoming indirect fire. The primary detection tools are Q-36 (Firefinder) and Q-37 (Firefinder) radars, supplemented by the Q-53 (Counterfire Target Acquisition Radar System). MSS integrates radar data from these systems to display point of origin and point of impact data on the fires operational picture.

6-2. The C-RAM process in MSS has three functional components:
- Radar data display: POO/POI visualization on the fires picture
- Hostile fire event tracking: recording and reporting incoming fire events
- Counterfire nomination: generating and routing counterfire engagements from confirmed radar data

---

### 6-2. Q-36/Q-37 Radar Data Integration in MSS

6-3. Q-36 and Q-37 Firefinder radars detect incoming indirect fire and back-azimuth the trajectory to a point of origin. When the data interface with MSS is active, radar-detected POO and POI data appears automatically on the MSS fires operational picture.

6-4. MSS displays radar data as a geospatial icon at the reported POO and POI location, linked to the radar unit's report. Each radar report in MSS carries:
- Radar unit identifier
- POO grid coordinates (8-digit MGRS or better)
- POI grid coordinates (if computed)
- Detection time DTG
- Target type (mortar, artillery, or rocket assessed by trajectory)
- Confidence level (based on radar return quality)

6-5. Multiple radar reports of the same POO location within a short time window allow MSS to correlate reports into a single target track, increasing confidence and driving counterfire nomination. The fires cell targeting officer or counterfire officer reviews correlated POO tracks and initiates the counterfire nomination process.

---

### 6-3. 13R Firefinder Operator MSS Workflow

6-6. The 13R Firefinder operator manages the radar zone data in MSS and ensures POO/POI data is reported accurately. The 13R workflow includes:

6-7. Radar zone management: The 13R confirms that CTZ and ATZ boundaries in MSS match the zones loaded in the organic radar system. Zone changes approved by the fires cell are entered in both the radar system and MSS. Discrepancies between MSS zone display and loaded radar zones are reported immediately to the fires cell.

6-8. Radar status reporting: The 13R enters radar system status in MSS (operational, degraded, maintenance, out of action) at the unit SOP reporting time. Status entries include the degraded capability if the system is PMCI or PMCII, enabling the counterfire officer to assess collection coverage.

6-9. POO/POI data quality: When the radar detects a target, the 13R confirms the automatic MSS data entry is accurate (if the data interface is active) or manually enters the POO/POI data in the sensor module (if the interface is degraded). Manual entry must occur within five minutes of radar detection to preserve counterfire response time.

---

### 6-4. C-RAM Tracker in MSS

6-10. The C-RAM tracker in MSS records all incoming fire events reported by radar or by units on the ground. Each hostile fire event record enables fires staff tracking, counterfire nomination, and operational reporting.

6-11. C-RAM tracker data in MSS:
- Incoming fire event identifier (auto-generated)
- Reporting unit or radar unit
- POO grid (from radar or reported by ground unit)
- POI grid (from radar or reported by ground unit)
- Weapon type (mortar, artillery, rocket, or unknown)
- Number of rounds reported
- Detection/impact DTG
- Casualties or damage report (if known at time of entry)
- Counterfire nomination status (Nominated, Approved, Fired, Pending BDA, or No Counterfire)

---

### 6-5. Meteorological Data Management in MSS

6-12. Accurate ballistic meteorological (MET) data is required for fires accuracy. 13S MET team survey specialists collect upper air data, produce MET messages, and distribute them to firing elements. MSS maintains the current and historical MET message library.

6-13. MET data in MSS:
- Current ballistic MET message (upper air data in METGM or standard Army format)
- MET message effective period (typically two to four hours depending on atmospheric conditions)
- MET release DTG and issuing unit
- Archive of previous MET messages for the current operational period

6-14. 13S MET team data upload: On completion of an upper air observation and computation, the 13S uploads the MET message to MSS. Firing units access the current message from MSS when the radio/data link for direct transmission is degraded.

---

### 6-6. Counterfire Nomination and Approval Workflow in MSS

6-15. Counterfire is the most time-sensitive fires task in the fires process. A confirmed POO detection from Firefinder has a very short exploitation window — the target is mobile and will likely move within minutes of firing. MSS supports counterfire by streamlining the nomination-to-approval workflow.

6-16. Counterfire nomination in MSS:
1. Radar detection produces a POO track in MSS (automatic via interface or manual entry).
2. Counterfire officer reviews the POO track: confirms location, target type, and confidence.
3. Counterfire officer generates a counterfire nomination in MSS linked to the POO track.
4. Nomination includes: target grid, target type, recommended fires system, recommended munition, desired effects, and time-sensitivity flag.
5. FSCOORD reviews and approves or disapproves the nomination in MSS.
6. If approved, the mission is assigned to the nominated system in the FSEM module.
7. 13J/13P receives the mission via AFATDS (primary) or voice (backup).
8. Mission execution and BDA are linked to the counterfire record in MSS.

6-17. The counterfire nomination-to-approval workflow in MSS must not substitute for voice coordination when time is critical. The FSCOORD approves counterfire nominations in MSS and simultaneously communicates approval to the FDC via voice or digital means. MSS records the action; it does not replace the approval communication.

---

**TASK: Report Hostile Fire Event in MSS**

**CONDITIONS:** 13R Firefinder operator or fires cell NCO, with access to the MSS C-RAM tracker module. Radar detection of incoming fire has occurred and POO/POI data is available. Data interface may be active (automatic entry) or degraded (manual entry required).

**STANDARDS:** Hostile fire event entered in MSS within five minutes of radar detection or ground report. All required data fields completed. Counterfire nomination generated within 10 minutes of detection for confirmed POO data meeting counterfire criteria. Event record updated with counterfire status and BDA when available. Hostile fire event reported to higher headquarters per unit SOP reporting timeline.

**PROCEDURE:**

1. On radar detection, confirm the automatic MSS C-RAM tracker entry if the data interface is active (POO/POI icon appears on the fires picture).
   - If auto-entry is confirmed: proceed to step 3.
   - If interface is degraded: proceed to step 2.
2. (Manual entry) Navigate to the MSS Fires Workspace, select C-RAM Tracker, and select "New Event."
   a. Enter POO grid from radar display (8-digit MGRS minimum).
   b. Enter POI grid if available.
   c. Enter detection DTG.
   d. Select weapon type (mortar, artillery, rocket, or unknown).
   e. Enter number of rounds detected.
   f. Select reporting unit (your radar unit identifier).
3. Review the auto-populated or manually entered data for accuracy. Correct any errors.
4. Enter initial casualty/damage report if known (or annotate "Unknown — assessment pending").
5. If POO data is confirmed and the target meets counterfire criteria (time since detection under threshold, location within engagement area, confidence level meets standard):
   a. Select "Generate Counterfire Nomination" linked to this event record.
   b. Enter recommended fires system, munition, and desired effects.
   c. Submit nomination to FSCOORD.
6. Track counterfire nomination status in the event record.
7. When counterfire is executed, update event record with fires system, rounds, and time of execution.
8. When BDA is available, update event record with BDA data.
9. Submit hostile fire event report to higher headquarters per unit SOP.

---

**Table 6-1: Radar Zone Definitions and Management**

| Zone Type | Definition | Purpose in MSS | Who Manages | Update Trigger |
|-----------|-----------|---------------|------------|----------------|
| Cued Target Zone (CTZ) | Geographic area tasked to the radar for counterfire detection | Displays active radar collection area; drives target track location context | 13R / Counterfire Officer | On change to radar tasking |
| Attack Target Zone (ATZ) | Priority subset of the CTZ; highest priority for detection and reporting | Marks highest-priority counterfire collection areas; linked to HPTL | Counterfire Officer / 13A | On change to counterfire priorities |
| Exclusion Zone | Area within CTZ where radar returns are suppressed or excluded | Prevents false reports from friendly indirect fire or known non-hostile activities | Counterfire Officer | On change to friendly fires plan |
| Displacement Reporting Zone | Zone that triggers radar displacement reporting requirement | Identifies areas where radar presence is reported to the fires cell | Fires Cell / 13R | Per SOP and positioning guidance |

---

## CHAPTER 7 — JOINT FIRES INTEGRATION

### 7-1. Overview

> **BLUF: Joint fires require more coordination data, not less. JTAC/JFO workflows, ATO data, airspace deconfliction, and SEAD coordination all enter MSS to enable the fires cell to synchronize joint effects with organic fires.**

7-1. Joint fires integration brings air-delivered fires and land-based fires into a synchronized scheme of effects under the FSCOORD's coordination. MSS supports joint fires integration by maintaining joint coordination data — the ATO, JTAC/JFO reports, airspace deconfliction measures, and SEAD/DEAD coordination — alongside organic fires data in a single fires workspace.

7-2. Joint fires in USAREUR-AF formations operate under ATP 3-09.42 (Fire Support for Brigade Combat Teams), FM 3-09.32 (JFIRE), and applicable USAFE-AFAFRICA coordinating instructions. MSS does not replace the joint fires coordination communication structure — it records and visualizes coordination data to support the fires staff.

---

### 7-2. JTAC/JFO Workflows and MSS

7-3. Joint terminal attack controllers (JTACs) and joint fires observers (JFOs) coordinate and execute air-delivered fires. Their MSS workflow supports:
- Submitting close air support (CAS) requests and linking them to the target list
- Recording 9-line and 15-line brief data for tracking purposes
- Tracking CAS mission execution status
- Entering BDA for air-delivered strikes

7-4. The JTAC's primary communications and coordination occur via voice (radio) and through digital CAS request formats. MSS provides the fires staff visibility of active CAS requests and their execution status, enabling the FSCOORD to synchronize CAS with organic fires and manage airspace deconfliction.

7-5. JFO report tracking in MSS: When a JFO submits a target report or BDA report, it enters the MSS fires workspace and links to the target record. This linkage ensures that JFO observations contribute to the BDA record and counterfire picture regardless of whether they result in an immediate fires request.

7-5a. 9-line CAS request data in MSS: The fires cell maintains a log of 9-line CAS requests linked to the fire mission log. Each CAS log entry carries:
- Request sequence number and JTAC callsign
- 9-line data (line 1 through line 9 as transmitted)
- Aircraft type and callsign assigned
- Time on station window
- Target number from the fires target list (if pre-planned) or ad hoc target reference
- Execution status: pending, active, complete, cancelled, abort
- BDA entry on completion

7-5b. JTAC-MSS interface at BCT: The JTAC assigned to a supported maneuver battalion typically has access to the BCT fires workspace. JTAC access is configured for read access to the HPTL and FSCM overlay, and write access to the CAS request log and BDA module. This access enables the JTAC to confirm FSCM currency before clearance and to enter BDA directly after strike execution without routing through the fires cell.

> **CAUTION: JTACs and JFOs entering BDA in MSS must apply the same collection source documentation standards as fires personnel. Untraceable BDA entries from JTACs — marked as "JTAC visual" without location, date, or specific observation detail — do not meet the BDA standard and will not support re-attack decisions or operational law reviews.**

---

### 7-3. Air Tasking Order Data Management

7-6. The Air Tasking Order (ATO) is the joint fires authority document governing air-delivered fires within the joint AOR. ATO data relevant to the fires staff includes:
- Allocated CAS sorties (time, aircraft type, ordnance, duration of availability)
- Restricted operations areas (ROA) that limit land fires to protect airspace
- SEAD/DEAD planned sorties affecting fires deconfliction
- No-drop lines and airspace management measures relevant to land fires

7-7. ATO data enters MSS from the fires cell liaison with the USAFE-AFAFRICA air operations center (AOC) or the aviation liaison officer (ALO)/TACP assigned to the formation. ATO data is imported into MSS by the fires cell staff officer responsible for joint fires coordination.

7-8. ATO currency is a fires planning imperative. The ATO is published daily with changes posted as fragmentary changes (FRAGOs to the ATO). Fires staffs must maintain current ATO data in MSS to prevent fires deconfliction failures.

---

### 7-4. SEAD/DEAD Planning Data in MSS

7-9. Suppression of enemy air defenses (SEAD) and destruction of enemy air defenses (DEAD) are joint fires tasks that require extensive deconfliction between air and land fires. MSS maintains SEAD/DEAD planning data including:
- SEAD mission timing windows (when aircraft are operating in the planned area)
- SEAD corridors (airspace reserved for SEAD aircraft ingress/egress)
- DEAD target list (linked to the joint target list)
- Land fires restrictions during SEAD operations (which areas require fires cessation or restriction)

7-10. When SEAD corridors are active, MSS displays the corridor on the fires operational picture as an airspace coordination measure (see Chapter 3, Table 3-1). Fires near the SEAD corridor require coordination with the TACP/ALO before execution.

---

### 7-5. Airspace Deconfliction Data Management

7-11. Airspace deconfliction prevents collision between fires trajectories and aircraft. In MSS, airspace deconfliction data includes:
- ACAs (airspace coordination areas) from the airspace control order (ACO)
- Aircraft routing and minimum risk routes (MRR) affecting fires planning
- Artillery target intelligence (ATI) areas marking active fires zones
- Altitude reservation (ALTRV) data affecting fires deconfliction

7-12. The fires cell airspace NCO or warrant officer maintains airspace deconfliction data in MSS IAW the current ACO. Changes to ACO data affecting fires trigger immediate FSCM/ACA overlay updates in MSS.

---

**TASK: Build Joint Fires Coordination Data in MSS**

**CONDITIONS:** Fires cell staff officer or warrant officer responsible for joint fires, with access to the MSS fires workspace and joint fires module. Current ATO, ACO, and SEAD coordination data received from the TACP/ALO or higher fires cell. Joint fires working group (JFWG) products are available.

**STANDARDS:** All ATO sorties allocated to the formation are entered in MSS with time, aircraft type, ordnance, and area of operations. Current ACO-derived airspace measures are entered as FSCM/ACA entries in the FSCM overlay. SEAD corridors and mission timing windows are entered with correct effective periods. Joint fires coordination data is published to all subordinate fires workspaces within two hours of ATO receipt. TACP/ALO verifies accuracy of entered data before publication.

**PROCEDURE:**

1. Receive the current ATO and ACO from the TACP/ALO, higher fires cell, or joint fires coordination channel.
2. Navigate to the MSS Joint Fires module.
3. Enter ATO CAS allocation data:
   a. For each allocated CAS sortie, enter aircraft type, time on station, ordnance load, callsign, and area of operations.
   b. Link each sortie to the applicable target category on the HPTL or FSEM if pre-planned.
4. Navigate to the FSCM overlay module.
5. Enter ACO-derived airspace measures:
   a. ACAs: enter boundaries, effective period, and supported unit.
   b. SEAD corridors: enter geographic corridor boundaries and activation timing window.
   c. ROAs: enter boundaries and effective period.
6. Cross-check entered measures against the current FSCM overlay for conflicts with land fires coordination measures. Report any conflicts to the FSCOORD.
7. Coordinate with TACP/ALO to confirm accuracy of entered ATO and airspace data before publishing.
8. Publish updated joint fires overlay to all subordinate fires workspaces.
9. Notify subordinate FSOs and JTACs of ATO and airspace updates via MSS notification and alternate means.
10. Record publication DTG and confirming officer in the fires cell log.

---

**Table 7-1: Joint Fires Coordination Measure Types**

| Measure Type | Definition | Source Document | Fires Restriction |
|-------------|-----------|----------------|------------------|
| ACA (Airspace Coordination Area) | Reserved airspace for aircraft operations | Airspace Control Order (ACO) | Fire through ACA requires coordination with airspace control authority |
| SEAD Corridor | Airspace reserved for SEAD aircraft ingress/egress | SEAD coordination order / ATO | No fires in SEAD corridor during active window without SEAD coordination |
| ROA (Restricted Operations Area) | Area restricting air or land operations | ACO / OPORD | Fires in ROA require higher coordination per ROA establishment order |
| MRR (Minimum Risk Route) | Low-altitude aircraft routing | ACO | Fire near MRR requires altitude and timing deconfliction |
| Kill Box | A geographic area established for offensive operations; land and air fires may be delivered simultaneously | Joint fires authority | Land fires in kill box require confirmation that kill box is "open" (no aircraft active) |

---

## CHAPTER 8 — FIRES ASSESSMENT AND REPORTING

### 8-1. Overview

> **BLUF: Fires assessment closes the targeting loop. Without accurate and timely BDA, the fires cell cannot assess effects, update the HPTL, or make sound re-attack recommendations. MSS is the assessment data platform — the fires cell must use it rigorously, not selectively.**

8-1. Fires assessment encompasses BDA, fires effectiveness analysis, and fires reporting. IAW FM 3-60, BDA is the timely and accurate estimate of damage resulting from fires. BDA drives re-attack decisions and feeds the targeting cycle. MSS provides the platform for recording, analyzing, and reporting fires assessment data.

---

### 8-2. BDA Reporting Workflow in MSS

8-2. The BDA workflow in MSS follows a standard sequence from fires execution through assessment entry, re-attack recommendation, and FIREP generation. This workflow is the responsibility of the targeting officer and fires cell, with critical input from 13F FSOs and intelligence personnel.

8-3. BDA entry timeline: BDA is entered in MSS within two hours of fires execution or within one hour of BDA collection, whichever occurs first. When BDA is unavailable within two hours, a "BDA Pending" record is entered with the expected collection method and timeline.

8-4. Physical destruction BDA: Reports the percentage of target physically destroyed or damaged, the basis for the assessment (IMINT, visual, SIGINT, HUMINT, or multisource), and the confidence level.

8-5. Functional damage BDA: Assesses whether the target can still perform its function. Uses the standard rating: FMC (fully mission capable), PMCI (partially mission capable — maintenance), PMCII (partially mission capable — parts), NMC (non-mission capable). Applied to OPFOR systems using equivalent logic.

8-6. System disruption BDA: The highest-level assessment — what effect did the strike have on the OPFOR capability system the target supported? System disruption BDA is a targeting officer/S2 product requiring intelligence input. MSS links system disruption BDA to the higher-level effects assessment.

---

### 8-2a. Commander's Critical Fires Information in MSS

8-5a. The commander's critical fires information (CCFI) is the subset of fires data the commander needs to make operational decisions. MSS supports CCFI by providing a configurable fires dashboard that displays the metrics the FSCOORD and commander have identified as most operationally significant.

8-5b. Typical CCFI elements maintained in the MSS fires dashboard:
- HPTL engagement status: percentage of HPTL categories engaged with acceptable BDA, current period
- Outstanding re-attack nominations: number of nominations awaiting FSCOORD action
- Long-range fires inventory: ATACMS/PrSM missiles on hand vs. basic load (where applicable)
- AMD system readiness: percentage of Patriot and SHORAD assets FMC
- Class V status: batteries below 50% basic load, currently on resupply request
- Response time trend: 72-hour rolling average time from CFF to first round

8-5c. The FSCOORD configures the CCFI dashboard at the beginning of each operational phase to reflect the commander's current priorities. A commander preparing for a deliberate attack prioritizes HPTL engagement status and re-attack nominations. A commander in a defensive posture may prioritize AMD readiness and counterfire effectiveness. MSS dashboard configuration is a fires planning task, not an IT task.

---

### 8-3. Fires Effectiveness Assessment: MOE/MOP Framework

8-7. Fires effectiveness assessment uses measures of effectiveness (MOE) and measures of performance (MOP) to evaluate both tactical execution quality and operational effects.

**Table 8-1: Fires MOE/MOP Matrix**

| Assessment Type | Metric | Definition | Data Source in MSS | Threshold for Re-attack |
|----------------|--------|-----------|-------------------|------------------------|
| MOP — Response Time | Time of First Round minus Time of Request | Speed of fires delivery from CFF to first round | Fire mission log (auto-calculated) | >10 minutes drives fires process review |
| MOP — Mission Accuracy | Rounds on target vs. rounds expended | Fires accuracy indicator | Fire mission log + BDA | Below threshold triggers technical review |
| MOP — BDA Timeliness | Time from fires execution to BDA entry | Assessment timeliness indicator | BDA record timestamp | >4 hours drives collection shortfall review |
| MOE — Physical Destruction | % of target physically destroyed | Tactical effects indicator | BDA record (physical destruction field) | Below desired effects threshold drives re-attack |
| MOE — Functional Damage | FMC/PMCI/PMCII/NMC of targeted system | Target capability degradation | BDA record (functional assessment field) | NMC or PMCII may satisfy; FMC drives re-attack |
| MOE — Mission Impact | Assessment of impact on OPFOR mission capability | Operational-level fires effectiveness | System disruption BDA + intelligence assessment | Commander determination; no formula |
| MOE — HPTL Progress | Percentage of HPTL targets engaged with acceptable BDA | Targeting cycle efficiency | HPTL status display in MSS | Commander-established target engagement rate |

---

### 8-3a. Mission-Level After Action Reporting

8-7a. Mission-level AAR data in MSS supports fires learning beyond the individual BDA record. The mission AAR captures fires process performance data separate from effects data: response time, number of rounds expended, any mission deviations, coordination issues encountered, and FSCM or airspace coordination complications.

8-7b. Mission AAR entries in MSS are the fires cell's operational record. They support commander's inquiries, operational law reviews, and after-action reviews following major operations. Units that maintain complete mission AAR data in MSS emerge from operations with an authoritative fires record. Units that do not maintain this data emerge with gaps that are reconstructed from memory — a less reliable foundation for both operational learning and legal compliance.

8-7c. The fires cell targeting officer reviews a sample of mission AAR data at the weekly fires cell update, looking for patterns in fires process performance: are certain missions consistently slow in the approval chain? Are missions near specific FSCM boundaries generating disproportionate coordination workload? Are certain weapons systems generating BDA outcomes significantly above or below the AGM desired effects standard? These patterns inform fires cell process improvement.

---

### 8-4. Fires Status Reporting in MSS

8-8. Fires status reporting provides commanders and higher headquarters with current fires capability, consumption, and effectiveness data. MSS is the data source for all fires status reports; the fires cell generates the reports from MSS data.

8-9. Fires reporting is a command requirement, not an administrative preference. Higher headquarters use fires reports to make decisions about fires resource allocation, re-attack authorization, and operational sequencing. Incomplete or inaccurate fires reports from MSS produce decisions at higher echelon that are based on wrong or partial information. The FSCOORD who allows fires reports to be submitted with incomplete MSS data because "we'll fix it later" is providing the corps FSCOORD with degraded information at the moment decisions must be made.

8-10. Required fires reports and their MSS data sources:

**Table 8-2: Required Fires Reports, Frequency, and Responsible Position**

| Report | Definition | Frequency | Responsible Position | MSS Data Source |
|--------|-----------|-----------|---------------------|----------------|
| AMMO SITREP | Class V on-hand quantities by type and system | IAW unit SOP (typically daily at 0600Z) | FDC Chief (13J/13P) | Class V tracking module |
| FIREP (Fires Report) | Fires executed, targets engaged, BDA summary | IAW higher headquarters requirement | Targeting Officer / S3 | Fire mission log + BDA records |
| RADSTAT | Radar operational status and zone status | Daily and on status change | Counterfire Officer / 13R | Radar/sensor module |
| AMD SITREP | AMD system readiness, engagement log, CAL/DAL status | IAW AMD TF SOP (typically daily) | AMD TF S3 / 14A | AMD module |
| COUNTERFIRE REPORT | POO/POI data summary, counterfire missions executed | Per reporting cycle (typically 12-24 hours) | Counterfire Officer | C-RAM tracker + fire mission log |
| TARGETING SITREP | HPTL engagement status, BDA summary, re-attack nominations | Per targeting working group cycle | Targeting Officer | Targeting module (HPTL + BDA) |
| FIRES EFFECTIVENESS REPORT | MOE/MOP summary for fires in the reporting period | Per operation order or commander guidance | FSCOORD / Targeting Officer | MOE/MOP dashboard in MSS |

---

**TASK: Prepare Fires SITREP from MSS**

**CONDITIONS:** Targeting officer or fires cell S3 NCO, with access to the MSS fires workspace. All subordinate fires units have submitted current Class V, mission log, BDA, and AMD status updates to MSS for the reporting period. Reporting time established by unit SOP has been reached.

**STANDARDS:** Fires SITREP reflects current MSS data as of report time. All required data fields present (Class V, fire missions executed, HPTL status, BDA summary, AMD status, and counterfire summary). SITREP submitted to higher headquarters NLT the unit SOP reporting time. Discrepancies between MSS data and reported status are annotated and reconciled.

**PROCEDURE:**

1. Navigate to the MSS Fires Workspace and open the Fires Reporting module.
2. Select "Fires SITREP" template.
3. Confirm the reporting period start and end DTGs.
4. Populate Class V summary:
   a. Review the Class V tracking module for all assigned FA and AMD systems.
   b. Confirm all batteries and platoons have submitted Class V updates for the period.
   c. Export Class V summary data to the SITREP template (or manually enter).
5. Populate fire missions executed:
   a. Open the fire mission log filtered by the reporting period.
   b. Count and record: total missions executed, total rounds expended by type, missions cancelled, and average response time.
6. Populate HPTL engagement status:
   a. Open the HPTL display.
   b. Record: total HPTL targets, targets engaged this period, targets with confirmed BDA, targets pending BDA, and outstanding re-attack nominations.
7. Populate BDA summary:
   a. Open the BDA log filtered by reporting period.
   b. Record: physical destruction (average %), functional damage summary (FMC/PMCI/PMCII/NMC counts), and system disruption summary.
8. Populate AMD status:
   a. From the AMD module, extract system readiness summary (FMC/PMCI/PMCII/NMC for each system type) and engagement log.
9. Populate counterfire summary from the C-RAM tracker for the reporting period.
10. Review the completed SITREP for internal consistency. Reconcile any discrepancies.
11. Submit SITREP to higher headquarters via MSS (if higher HQ is on MSS) or export and transmit via alternate means per PACE plan.
12. Archive the submitted SITREP in the fires cell records module.

---

## CHAPTER 9 — ECHELON-SPECIFIC FIRES OPERATIONS

### 9-1. Overview

9-1. Fires operations in MSS are configured differently at each echelon, reflecting the different fires responsibilities and products at BCT, division, corps, and theater. This chapter addresses the specific MSS workflows for fires personnel at each echelon.

> **BLUF: MSS fires workspaces are echelon-specific. The FSCOORD at BCT manages a different data set than the DIVARTY CDR at division. Both use the same platform; they use it for different purposes with different authorities.**

---

### 9-2. BCT Fires Operations in MSS

9-2. At BCT level, fires operations in MSS focus on:
- Battalion FSO coordination: direct support fire missions, CFF tracking, FSCM currency
- FSCOORD fires synchronization: fires task organization, FSEM management, target engagement tracking
- Targeting: HPTL management at BCT level, AGM publication to subordinate FSOs
- BDA: FSO-submitted BDA from direct support operations

9-3. The BCT fires cell workload in MSS is highest during the prepare and execute phases. During planning, the FSCOORD publishes FSCMs and the FSEM. During execution, FSOs submit CFFs and BDA at high tempo.

9-4. BCT-specific MSS considerations:
- The BCT fires workspace receives FSCM data from division — BCT does not establish FSCMs above its own organic measures
- BCT HPTL is derived from division targeting guidance; BCT targeting identifies time-sensitive targets for immediate engagement
- Battalion FSOs have read access to the BCT fires workspace and write access to their own FSO module

9-5. BCT fires cell key MSS tasks and owners:
- FSCOORD: HPTL and FSEM management, FSCM overlay publication, fires synchronization across supported battalions
- Targeting officer (13A): target record maintenance, AGM linkage, BDA review, TWG products in MSS
- Fire support NCO: fire mission log accuracy, BDA completeness checks, Class V roll-up from subordinate batteries
- Battalion FSOs: CFF submissions, local FSCM observation and reporting, BDA entry within standard

9-6. BCT HPTL management in MSS differs from division-level targeting in scope and tempo. BCT targeting focuses on enemy systems directly affecting the BCT scheme of maneuver: indirect fire systems threatening the supported battalions, air defense assets that may interfere with aviation, combat engineering obstacles, and command and control nodes. BCT HPTL entries are fewer than division-level entries but require faster update cycles because BCT-level targets are in immediate contact range.

9-7. Direct support FSO MSS workflow at BCT: Each supported battalion's FSO maintains a CFF log in MSS linked to the BCT fires workspace. The BCT fires cell monitors all active CFF requests in real time. When the FSCOORD approves a mission, the assignment appears in both the BCT fires cell and the FSO's module simultaneously. This real-time visibility eliminates the need for voice status calls on mission assignment during high-tempo operations.

9-8. BCT counterfire operations in MSS: The BCT counterfire officer (typically the Q-36 section chief or a designated 131A warrant) manages radar zone data and counterfire nominations at BCT level. BCT counterfire targets go directly to the BCT fires cell for FSCOORD approval, bypassing division targeting for immediate counterfire. MSS counterfire nominations at BCT level must be processed within the time window before the target displaces — BCT counterfire is the most time-critical targeting function in the fires cell.

---

### 9-3. Division Fires Brigade Operations in MSS

9-9. At division level, the fires brigade adds organic capabilities (cannon and rocket artillery battalions, target acquisition battery) that expand both fires capacity and MSS data volume.

9-10. Division fires MSS functions:
- Targeting working group (TWG) products: HPTL, AGM, and JTL management at division level
- Collection management: linking ISR assets to HPTL requirements in the collection management module
- Fires brigade employment: multiple battalion status, positioning, and ammunition tracking
- EW integration: EW target data integration with the fires target list (where applicable and authorized)
- DIVARTY FSCOORD fires synchronization: allocating fires resources among supported BCTs and division artillery

9-11. The targeting officer at division fires brigade is the primary MSS fires user for targeting module management. The division targeting officer ensures HPTL and BDA data in MSS is current and published to supported BCTs.

9-12. Division targeting working group MSS protocol: The TWG is the primary collective fires data event at division level. The division targeting officer configures MSS for each TWG session:
- HPTL display projected for collective review and update
- Target status sorted by engagement status (unengaged, engaged-BDA pending, assessed)
- Collection status display linked to ISRM and outstanding collection requirements
- BDA log filtered by the previous TWG cycle for re-attack recommendation review

9-13. DIVARTY Class V management in MSS aggregates ammunition data from multiple FA battalions. The DIVARTY fires cell maintains the consolidated Class V picture across all assigned and attached FA units. This aggregated picture supports fires allocation decisions: which battalion has the ammunition load to support a sustained fires task, and which requires resupply before being assigned additional missions.

9-14. Target acquisition battery MSS integration: The target acquisition battery (TAB) at division operates Q-36 and Q-37 radars across the division AO. The TAB is the primary counterfire sensor organization for the division. TAB section chiefs maintain radar zone data in MSS for their assigned sectors. The TAB headquarters maintains the consolidated radar coverage picture for the division fires brigade FSCOORD.

9-15. Division fires brigade EW-fires integration: Where Electronic Warfare (EW) targets are approved for inclusion in fires targeting, EW target data enters MSS through a coordinated process involving the division G7 (information operations) officer and the division fires cell targeting officer. EW targets on the fires target list are marked with an EW indicator and require specific AGM guidance reflecting the EW-fires coordination constraints. This integration enables the division FSCOORD to synchronize fires effects against EW targets when EW suppression alone is insufficient to achieve desired effects.

---

### 9-4. Corps Artillery Operations in MSS

9-16. Corps fires operations involve larger formation coverage, extended-range fires systems (ATACMS, PrSM), and the corps targeting working group (TWG) that synchronizes targeting across multiple divisions.

9-17. Corps fires MSS functions:
- TWG data management: corps-level HPTL, joint target list synchronization, high-value target tracking
- Corps fires cell data: multiple fires brigade status, long-range fires asset tracking, fires allocation management
- Theater coordination: interface with theater fires support element for joint fires nomination
- Counterfire planning at corps level: sensor coverage assessment across the corps AO, counterfire task organization

9-18. Corps-level HPTL management in MSS operates on a larger target set than division. Corps targeting focuses on OPFOR echelons above regiment (EAR), key logistics nodes, integrated air defense systems (IADS), and command nodes at army group or above. These targets are typically longer-dwell targets — they do not change position as frequently as tactical counterfire targets — but their engagement requires more extensive legal review, collateral damage estimation, and command authority.

9-19. Corps long-range fires asset tracking in MSS: ATACMS and PrSM missiles are limited-quantity assets managed at corps level. The corps fires cell tracking officer maintains inventory, employment history, and mission assignments for long-range fires assets in MSS. The FSCOORD uses this display to manage allocation of limited-quantity assets against corps-level HPTL targets.

9-20. Corps fires allocation in MSS: The corps FSCOORD allocates fires assets among supported divisions based on operational priorities and available means. MSS provides the corps fires cell visibility of each division fires brigade's asset status, ammunition level, and current mission load. This allocation function in MSS prevents the corps FSCOORD from over-tasking degraded units or under-utilizing fresh units.

---

### 9-5. Theater Fires Support Element

9-21. At theater, the fires support element (FSE) coordinates joint fires across the USAREUR-AF theater. MSS at theater level integrates:
- Joint target list (JTL) management with the JFLCC and JFACC
- Theater fires asset allocation: ATACMS, PrSM, and joint air-delivered fires across the theater
- Theater FSCM management: FSCLs and theater-level coordination measures
- Joint fires assessment: theater-level BDA and fires effectiveness reporting to the JFLCC

9-22. Theater-level fires data volume in MSS is the largest in the formation. The theater FSE manages JTL entries from multiple corps and joint component commands, theater-level FSCM coordinates, and fires effectiveness analysis across the entire theater AOR. The theater fires data officer is a dedicated MSS user responsible for data quality at this level.

9-23. The theater FSCL in MSS is the most consequential single coordination measure in the fires data picture. The FSCL determines whether fires are coordinated with land forces (short of the FSCL) or with the joint component (long of the FSCL). FSCL changes in MSS at theater level cascade to every fires workspace at every echelon simultaneously. Theater fires staff must treat FSCL changes as the highest-priority FSCM update action in MSS — completing publication within the shortest possible time after theater command approval.

---

**Table 9-1: Fires Workspace Configuration by Echelon**

| Echelon | Primary Fires Module Users | HPTL Authority | FSCM Authority | BDA Authority | Counterfire Focus |
|---------|--------------------------|----------------|----------------|---------------|------------------|
| Battalion FSO | 13F — CFF module, BDA log | Receive only | Observe and report | 13F submits | N/A (mortars only) |
| BCT Fires Cell | FSCOORD, targeting officer, 13A | BCT HPTL (limited) | BCT-area FSCMs | BCT fires BDA | Q-36 section CTZ |
| Division Fires Brigade | DIVARTY FSCOORD, targeting officer, TWG cell | Division HPTL | Division FSCMs | Division fires BDA | Division Q-36/Q-37 task org |
| Corps Fires Cell | Corps FSE chief, targeting officer, counterfire officer | Corps HPTL + JTL input | Corps FSCMs, FSCL | Corps BDA roll-up | Corps counterfire plan |
| Theater FSE | Theater fires coordinator, joint fires liaison | JTL management | Theater FSCMs, FSCL establishment | Theater fires effectiveness | Theater counterfire architecture |

---

## CHAPTER 10 — DEGRADED OPERATIONS

### 10-1. Overview

> **BLUF: Fires must continue when MSS is degraded. AFATDS is primary for fire direction. Voice is backup. The fires cell must maintain manual fires products for all contingencies. MSS degradation is a data problem — not a fires capability problem.**

10-1. Degraded operations occur when MSS is partially or fully unavailable due to network disruption, system maintenance, cyberattack, or electronic warfare effects. Fires do not stop because MSS is unavailable. The fires process continues through primary fires systems (AFATDS, IBCS, AMDWS) and voice procedures.

10-2. MSS degradation affects fires primarily in three areas:
- Targeting visibility: the fires cell loses real-time HPTL status and target tracking
- FSCM currency: FSOs cannot confirm current FSCM status through MSS
- Reporting: automated SITREP data compilation and BDA tracking are unavailable

10-3. These degradations are serious but manageable. The fires cell maintains manual fires products that support operations without MSS. The most dangerous assumption a fires unit can make is that MSS will always be available. Train and exercise fires tasks manually.

---

### 10-2. Manual Fire Direction Backup

10-4. Fire direction backups follow the established AFATDS-to-voice hierarchy:
1. **AFATDS (digital):** Primary fire direction system. AFATDS operates independently of MSS. Fire missions continue through AFATDS when MSS is unavailable.
2. **Voice (radio):** When AFATDS is also degraded, fire missions are executed via voice CFF and voice fire commands. All FA and ADA personnel are required to be proficient in voice procedures.
3. **Manual computation:** When AFATDS is unavailable, manual fire direction procedures (using firing tables or manual computation devices) provide ballistic computation capability. This is the tertiary backup.

10-5. MSS degradation does not affect AFATDS operation. These are separate systems. Loss of MSS visibility is a fires staff coordination problem; it is not a fire direction system failure.

---

### 10-3. PACE Plan for Fires Data Management

10-6. Each fires cell maintains a PACE plan for fires data management that addresses primary, alternate, contingency, and emergency communications and data management methods.

**Table 10-1: Fires PACE Plan**

| Data Function | Primary | Alternate | Contingency | Emergency |
|--------------|---------|-----------|-------------|-----------|
| Fire Mission Processing | AFATDS (digital) | AFATDS (radio) | Voice radio (CFF/fire commands) | Voice + manual computation |
| FSCM Publication | MSS FSCM overlay (digital) | Digital map overlay (ATAK) | Printed/drawn map overlay | Voice FSCM notification |
| Target List Management | MSS targeting module | Shared drive (fires cell) | Printed HPTL/AGM | Voice HPTL/AGM dissemination |
| Ammunition Status | MSS Class V module | Digital message (email/chat) | Voice AMMO SITREP | Manual tally sheet |
| BDA Reporting | MSS BDA module | Digital message format | Voice BDA report | Notebook + periodic voice report |
| Counterfire Nomination | MSS counterfire workflow | Voice counterfire request | Immediate voice approval from FSCOORD | Same as contingency |
| AMD Status | MSS AMD module | AMDWS/IBCS | Voice status update | Manual status board |
| MET Data | MSS MET module | Direct transmission to firing units | Voice transmission (abbreviated MET) | Computed MET from last known data |

---

### 10-4. Minimum Essential Fires Products Without MSS

10-7. When MSS is unavailable, fires cells maintain the following minimum essential products in manual or alternate-digital formats:
- Printed or digitally saved HPTL and AGM (updated at last available MSS sync)
- Printed or drawn FSCM overlay (map sheet or ATAK overlay)
- Printed fire mission log (manual entry from radio/voice missions)
- Manual ammunition status tally by battery/platoon
- Manual BDA log

10-8. These products are maintained continuously — not just when MSS fails. Units that rely exclusively on MSS and have no manual backup products will be unable to operate effectively during degraded periods.

10-8a. The fires cell conducts a quarterly manual products review to confirm that all backup products are current and available. This review verifies:
- Printed HPTL and AGM are no more than 24 hours behind the last MSS update
- FSCM overlay alternate (ATAK or printed) reflects the current FSCM picture
- Manual fire mission log sheets are stocked and the format is understood by all fires personnel
- Backup Class V tally format is posted in the fires cell operations area
- All fires personnel know where manual backup materials are stored and how to activate them

10-8b. Fires cells that discover during a degradation event that backup materials are missing, out of date, or not understood by current personnel have a training failure — not an equipment failure. Conduct the quarterly review. Train the backup.

---

### 10-5. Reconstitution After Outage

10-9. When MSS service is restored after an outage, the fires cell conducts a data reconstitution sequence to restore MSS to current operational status:

1. Determine the MSS last-known-good time (the last time MSS data was accurate before the outage).
2. Enter all fire missions executed during the outage from the manual fire mission log.
3. Enter any BDA collected during the outage from the manual BDA log.
4. Update Class V status from current battery reports.
5. Reconcile the FSCM overlay against any FSCM changes that occurred during the outage (via fires cell records and voice coordination).
6. Update the C-RAM tracker with any hostile fire events recorded during the outage.
7. Update AMD status from AMD unit reports.
8. Brief the FSCOORD on the data reconstitution status and any gaps in the reconstituted record.
9. Resume normal MSS update cycles.

10-10. Data reconstitution is a fires staff responsibility. Do not delay reconstitution because the outage period was brief. Even a two-hour outage in an active targeting cycle can produce significant data gaps.

---

### 10-6. Partial Degradation — Module-Level Failures

10-11. MSS may experience partial degradation where specific modules fail while others remain operational. Fires cells must know how to operate with module-specific outages without assuming all fires data management is unavailable.

10-12. Common partial degradation scenarios and fires cell response:

**Targeting module unavailable.** The HPTL and BDA functions are inaccessible. Response: maintain the current printed HPTL and AGM as the operational reference. Record fire missions and BDA in the manual log. When targeting module restores, reconcile manual records to MSS.

**FSCM overlay module unavailable.** The FSCM display is inaccessible. Response: the FSCM overlay from the last MSS print or export is the reference. For fires near coordination boundaries, confirm directly with the establishing headquarters via radio before clearance. Do not delay fires based on FSCM overlay unavailability — execute with manual confirmation.

**Class V module unavailable.** Ammunition tracking is inaccessible. Response: collect battery ammunition status via voice or digital message. Record in manual format. Fires cell continues fires allocation planning using verbally reported ammunition status. When module restores, enter updates from the manual record.

**C-RAM tracker unavailable.** Hostile fire event tracking is inaccessible. Response: record hostile fire events in the manual log with the same data fields as the C-RAM tracker (POO, POI, weapon type, rounds, DTG). Counterfire nominations proceed via voice without MSS workflow. When module restores, enter manual records.

10-13. Module-level failures must be reported to the S6 and USAREUR-AF C2DAO fires functional representative immediately. The fires cell tracks the outage start DTG and logs the workaround method used. This data supports platform issue resolution and informs PACE plan updates.

---

**TASK: Execute Fires Operations During MSS Degradation**

**CONDITIONS:** FSCOORD or fires cell chief, with the fires cell assembled and MSS partially or fully unavailable. Fires operations are ongoing. Manual backup materials (printed HPTL/AGM, printed/drawn FSCM overlay, manual fire mission log, manual Class V tally) are on hand.

**STANDARDS:** Fires operations continue without pause during MSS degradation. Fire missions are processed through AFATDS and voice. FSCM currency is confirmed via voice with establishing headquarters before clearing fires near coordination boundaries. Manual logs capture all fires events during the outage. MSS is reconstituted within two hours of restoration. No fires decisions are delayed beyond doctrinal time standards due to MSS unavailability.

**PROCEDURE:**

1. On MSS degradation, notify the FSCOORD and fires cell immediately.
2. Announce the degradation status to all fires users: "MSS is degraded — execute backup procedures."
3. Confirm AFATDS is operational and fire direction continues through primary system.
4. Issue the most recent printed HPTL/AGM to the targeting officer as the operational reference.
5. Confirm all FSOs are notified of MSS degradation and have current printed FSCM overlays or alternate digital overlays (ATAK).
6. Direct FSOs: for fires near FSCM boundaries, confirm FSCM currency via voice with the establishing headquarters before clearance. Do not rely on last-known MSS FSCM display.
7. Activate manual fire mission log. Assign a fires cell NCO to capture all missions with required data fields during the outage.
8. Activate manual Class V tally. Collect battery status via voice at next SOP reporting time.
9. For counterfire events: receive POO data from 13R via voice. FSCOORD approves counterfire nominations via voice. 13J/13P receives missions via AFATDS.
10. Contact S6 to report MSS degradation and initiate troubleshooting.
11. Brief the FSCOORD on fires status and manual backup posture at the next fires cell update.
12. On MSS restoration, execute data reconstitution sequence (see paragraph 10-9).

> **NOTE: Fires cells that train manual backup procedures regularly will execute this task with minimal disruption. Fires cells that have not trained manual procedures will experience operational degradation even when fires execution through AFATDS continues. Train the backup.**

---

## CHAPTER 11 — FIRES STAFF TRAINING AND MSS PROFICIENCY

### 11-1. Overview

> **BLUF: Fires MSS proficiency is not a one-time certification event. It is a continuous training requirement maintained through unit training programs, exercises, and battle rhythm events. The FSCOORD owns fires MSS training within the formation.**

11-1. MSS is a perishable skill. A 13F FSO who completes initial MSS training and then does not use the BDA module for four months will not perform that task competently under operational pressure. The fires cell that trains MSS procedures only during pre-deployment certification will find its proficiency degraded when it is needed most.

11-2. This chapter addresses the fires MSS training program: individual proficiency requirements by MOS, collective training integration, battle rhythm events that sustain proficiency, and the FSCOORD's responsibilities for training oversight.

---

### 11-2. Individual Proficiency Requirements by MOS

11-3. Every fires MOS has a defined set of MSS tasks for which individual proficiency is required. Proficiency is defined as the ability to execute the task to standard without reference to the procedural task boxes in this manual, within the stated time standard, under simulated operational conditions.

11-4. Proficiency requirements by duty position:

**13A/13F (FA Officer / FSO):**
- Build and Update the HPTL in MSS (Chapter 2 task)
- Submit and Track BDA in MSS (Chapter 2 task)
- Build and Maintain FSCM Overlay in MSS (Chapter 3 task)
- Build Joint Fires Coordination Data in MSS (Chapter 7 task)
- Prepare Fires SITREP from MSS (Chapter 8 task)
- Navigate the fires workspace and all fires modules

**13J/13P (Fire Control / MLRS Operations):**
- Conduct Daily Ammunition Status Update in MSS (Chapter 4 task)
- Update fire mission log records (Chapter 4 procedures)
- Execute AFATDS-MSS data handoff procedures (Chapter 4 procedures)

**13R (Firefinder Radar Operator):**
- Report Hostile Fire Event in MSS (Chapter 6 task)
- Manage radar zone display (CTZ/ATZ) in MSS (Chapter 6 procedures)
- Update radar system status in MSS

**13S (MET Surveyor):**
- Upload MET message to MSS (Chapter 6 procedures)
- Confirm MET message distribution via MSS

**14A (ADA Officer):**
- Update AMD Status and CAL/DAL in MSS (Chapter 5 task)
- Maintain engagement authority records in MSS (Chapter 5 procedures)
- Review AMD coverage display and identify gaps

**14E/14P/14S/14T (ADA Enlisted):**
- Update assigned system status in MSS (Chapter 5 procedures)
- Enter engagement log data in MSS

11-5. The FSCOORD certifies individual proficiency for all 13-series MOS personnel assigned to the fires cell. The AMD TF commander certifies 14-series MOS personnel. Certification occurs at the initial qualification event and annually thereafter, or following any MSS platform upgrade.

---

### 11-3. Collective Training Integration

11-6. Fires MSS training is most effective when integrated into collective training events — not conducted as separate standalone MSS training. The fires team should practice MSS tasks while executing the fires tasks those MSS modules support.

11-7. **Targeting Working Group (TWG) integration.** The most effective venue for fires MSS collective training is the targeting working group, conducted with MSS as the primary display and data management tool. Units that run the TWG from a PowerPoint template and update MSS afterward are missing the primary opportunity to build fires team MSS proficiency through repetition. TWGs conducted with MSS as the live data source build proficiency naturally: the targeting officer updates the HPTL in real time as the FSCOORD approves changes; the S2 updates target confidence levels during the meeting; BDA review produces updated MSS records as the TWG proceeds.

11-8. **Fire support coordination exercise (FASCOX) integration.** FASOCXs provide the opportunity to exercise fires coordination across echelons with MSS as the coordination medium. The FSCOORD should establish the FSCM overlay in MSS before the FASCOX, require subordinate FSOs to submit CFFs through the MSS fires module, and require BDA submission at the end of each exercise scenario. This replicates the execution-phase MSS workflow under controlled conditions before operational deployment.

11-9. **Command post exercise (CPX) integration.** CPXs at BCT and above provide the opportunity to exercise fires cell MSS workflows across the planning, preparation, and execution phases simultaneously. The fires cell OPFOR (notional enemy actions) drives target tracking updates, counterfire events, and HPTL changes that require real-time MSS updates during the CPX. MSS is not a display tool during the CPX — it is the primary fires data management medium.

11-10. **Fire support rehearsal integration.** The fire support rehearsal immediately before a live-fire exercise or gunnery event should include an MSS component: the HPTL is confirmed in MSS, the FSCM overlay is verified, and the FSEM is reviewed. This rehearsal builds the habit of checking MSS products as an integral part of fires preparation.

---

### 11-4. Proficiency Sustainment Through Battle Rhythm

11-11. Individual and collective MSS proficiency is sustained through deliberate inclusion of MSS-dependent tasks in the fires cell battle rhythm. Battle rhythm events that sustain fires MSS proficiency include:

**Daily fires cell update.** The fires cell's daily update to the FSCOORD should include a data quality review: HPTL currency, FSCM currency, Class V status, BDA log completeness. This five-minute review keeps the fires team aware of data gaps and creates the expectation that MSS data is maintained continuously.

**Weekly data reconciliation.** Once per week, the targeting officer conducts a systematic reconciliation of MSS target records against all intelligence products received since the last reconciliation. Target confidence levels are updated, stale detections are flagged, and collection gaps are identified. This is a training event as well as a data quality event.

**Monthly MSS task review.** Once per month, each fires cell member executes one proficiency task from their MOS requirement list, timed and graded by the targeting officer or FSCOORD. Results are recorded and any proficiency gaps trigger individual coaching or remedial training.

**Exercise scenario injection.** During garrison periods, the FSCOORD or targeting officer injects scenario-driven updates into MSS (new target detections, FSCM changes, AMD status changes, hostile fire events) and requires fires cell members to respond using correct MSS procedures. These injections require five to 10 minutes and can be conducted during normal battle rhythm without disrupting other operations.

---

### 11-5. New Personnel Onboarding

11-12. When a new fires team member arrives — whether a newly assigned 13F FSO, a replacement 13J, or a new 14A — their MSS onboarding follows a defined sequence before they are given write access to fires modules.

11-13. MSS onboarding sequence for fires personnel:

1. Complete TM-10 (Maven User) self-paced training — navigate the MSS interface, understand workspace structure, complete basic user tasks.
2. Complete TM-20 (Builder) self-paced training — understand MSS data objects, object sets, and basic workspace navigation.
3. Complete TM-30 (Advanced Builder) self-paced training — advanced platform capabilities and data governance required for WFF track enrollment.
4. Read CONCEPTS_GUIDE_TM40B_FIRES — understand the conceptual foundation before executing procedures.
5. Read this manual (TM-40B) — focus on chapters relevant to their duty position.
6. Observe a proficient fires team member execute each task in their MOS requirement list.
7. Execute each task under supervision, with the supervising officer or NCO correcting errors in real time.
8. Execute each task independently and demonstrate proficiency to standard.
9. FSCOORD or supervisor certifies proficiency and grants appropriate write access.

11-14. The total onboarding time for a proficient fires officer or NCO is typically three to five days of deliberate training. Units that rush this onboarding sequence will have uncertified fires personnel making data entries in a shared fires workspace that supports operational decisions. This is not an administrative risk — it is an operational data integrity risk.

---

### 11-6. MSS Upgrade and Platform Change Procedures

11-15. MSS undergoes periodic platform updates that may change the interface, module structure, or workflow for fires tasks. When a platform update affects fires modules, the fires cell conducts a post-update proficiency check before resuming operational use of updated modules.

11-16. Post-update actions for fires cells:

1. The FSCOORD designates a fires cell member as the point of contact (POC) for the update.
2. The POC reviews the USAREUR-AF C2DAO release notes for fires module changes.
3. The POC executes each fires task affected by the update in the MSS training environment to identify changes to procedures.
4. The POC briefs the fires team on changed procedures before operational use resumes.
5. Fires team members execute affected tasks in the training environment before the updated procedures are used in the operational workspace.
6. Updated procedures are annotated in unit SOPs.

> **NOTE: When MSS undergoes a major version update, the USAREUR-AF C2DAO publishes updated TM content and supplemental training materials. Check the MSS learning center for updated fires module training before relying on procedures from this manual for tasks significantly altered by the update.**

---

### 11-7. FSCOORD Training Oversight Responsibilities

11-17. The FSCOORD is responsible for the fires MSS training program within the BCT or fires brigade. This responsibility includes:

- Maintaining proficiency records for all fires personnel in assigned modules
- Conducting or designating oversight for the monthly proficiency check
- Ensuring MSS training is integrated into all collective training events
- Reporting MSS training status as part of the formation's overall fires training readiness
- Escalating MSS platform issues that affect training to the S6 and USAREUR-AF C2DAO fires functional representative

11-18. The FSCOORD should brief MSS proficiency status at the fires cell quarterly training briefing alongside other fires training metrics (gunnery certification, CFF qualification, AFATDS proficiency). MSS is not a separate administrative tracking system — it is a fires readiness metric with the same operational consequence as gunnery qualifications.

11-19. The AMD TF commander holds the same oversight responsibility for 14-series personnel that the FSCOORD holds for 13-series personnel. In formations where fires and AMD MSS training are managed separately, coordination between the FSCOORD and AMD TF commander ensures consistent data standards across the integrated fires workspace.

---

**TASK: Conduct Fires MSS Proficiency Check**

**CONDITIONS:** FSCOORD or designated supervising officer/NCO, with access to the MSS training environment. Fires cell member being evaluated, with their assigned duty position proficiency task list. Scenario data prepared to drive the proficiency task (target data, FSCM changes, ammunition status data, or BDA collection data as appropriate for the task).

**STANDARDS:** Fires cell member executes the designated proficiency task in the MSS training environment without procedural prompting. Task is completed within the time standard specified in the applicable task box in this manual. All required fields are completed accurately. The fires cell member correctly applies all applicable WARNING and CAUTION requirements (FSCM authorization, BDA collection source documentation, engagement authority confirmation). FSCOORD or supervisor certifies pass/fail and records result.

**PROCEDURE:**

1. Brief the evaluatee on the proficiency check scenario: duty position, situation, available data, and task to be executed.
2. Provide any necessary scenario inputs (target data, FSCM boundary data, Class V numbers, BDA collection report) without procedural guidance.
3. Direct the evaluatee to execute the task to standard.
4. Observe execution without intervening unless the evaluatee is about to make an entry that would corrupt shared training environment data.
5. Record deviations from standard procedure, missed fields, and any time standard exceedances.
6. On task completion, review the evaluatee's MSS entries against the standard:
   a. Are all required fields completed?
   b. Is the data accurately entered?
   c. Were authorization and WARNING requirements observed?
   d. Was the time standard met?
7. Brief the evaluatee on the proficiency check results.
8. If PASS: record certification in the proficiency tracking record with date and evaluator.
9. If NO-GO: identify specific deficiencies, prescribe remedial training, and schedule a follow-on proficiency check within 14 days.

---

## APPENDIX A — FIRES-SPECIFIC MSS NAMING CONVENTIONS

**A-1. Purpose.** Consistent naming conventions enable fires data to be searched, sorted, and shared across echelons without ambiguity. All fires personnel entering data in MSS use these conventions.

**A-2. Target Naming.** Targets are named using the format: [ECHELON]-[TARGET TYPE]-[SEQUENCE NUMBER]-[PHASE]. Example: BCT-ARTY-001-PH1 (BCT echelon, artillery target, first in sequence, Phase 1).

**A-3. FSCM Naming.** FSCMs are named using the format: [FSCM TYPE]-[IDENTIFIER]-[ESTABLISHING ECHELON]. Example: NFA-01-DIV (No Fire Area, first in sequence, established by Division). RFA-ALPHA-BCT.

**A-4. Fire Mission Log.** Mission numbers follow the unit SOP convention. MSS accepts any format but must include unit identifier and sequence number at minimum. Example: 1-9FA-0342 (1-9 FA battalion, mission 342).

**A-5. BDA Records.** BDA records are named to match the fire mission record: [MISSION NUMBER]-BDA. Example: 1-9FA-0342-BDA.

**A-6. C-RAM Events.** Hostile fire events are auto-generated by the C-RAM tracker with the format: CRAMP-[DATE]-[SEQUENCE]. Manual entries use the same format. Example: CRAMP-20260315-001.

**A-7. AMD Status Records.** AMD system records are named: [SYSTEM]-[UNIT]-[SEQUENCE]. Example: PAT-1-4ADA-BTRY-A (Patriot, 1-4 ADA, Battery A). M-SHORAD-1-4ADA-PLT-1.

**A-8. MET Messages.** MET messages are named: MET-[ISSUING UNIT]-[DTG]. Example: MET-13S-13PLT-1403150600Z.

**A-9. General Naming Discipline.** All MSS fires data entries must avoid use of classified information in names, titles, or descriptive fields that appear in unclassified workspaces. Target names, FSCM identifiers, and mission records should use reference codes rather than operationally sensitive terms in MSS field names visible in unclassified systems. Consult the unit classification guide and OPSEC officer before creating named data objects in MSS that reference specific operations, persons, or locations. When in doubt, use codes rather than plain language in public-facing MSS data fields.

---

## APPENDIX B — FIRE SUPPORT COORDINATION MEASURE REFERENCE

**B-1.** All FSCMs in MSS are drawn and labeled IAW FM 1-02 (Operational Terms and Military Symbols) and ADP 3-19.

| FSCM | Type | Symbol Color | Definition | Notes |
|------|------|-------------|-----------|-------|
| FSCL | Permissive | Black/Blue | Fire Support Coordination Line — divides land and joint fire responsibility | Must be coordinated with joint fires authority |
| RFL | Restrictive | Red | Restrictive Fire Line — between converging forces | Cross-RFL fires require coordination with adjacent unit |
| NFA | Restrictive | Red | No Fire Area | No fires without establishing HQ approval; specific approval required |
| RFA | Restrictive | Red/Yellow | Restrictive Fire Area | Fires with restrictions; comply with specific restrictions in order |
| FFA | Permissive | Green | Free Fire Area | Confirm still active before clearing fires |
| ATI | Reference | Blue | Artillery Target Intelligence | Informational; no fires restriction |
| ACA | Airspace | Purple | Airspace Coordination Area | Fire through ACA requires airspace authority |
| FCA | Coordination | Blue | Final Coordination Area | Coordination between adjacent fire support elements |
| BCL | Coordination | Blue | Boundary Coordination Line | Lateral boundary requiring coordination for fires |
| CFL | Permissive | Blue | Coordinated Fire Line | Fires forward of CFL require coordination with forward element |

---

## APPENDIX C — TARGET TRACKING STANDARD FIELDS

**C-1.** Target records in MSS require the following fields for all HPTL-listed targets.

| Field | Required/Optional | Data Type | Source |
|-------|------------------|-----------|--------|
| Target Number | Required | Alphanumeric (unit naming convention) | Targeting Officer |
| Target Type | Required | Controlled vocabulary (dropdown) | Targeting Officer |
| Target Category | Required | Controlled vocabulary (HPTL category) | Targeting Officer |
| Location | Required | MGRS 8-digit minimum | 13F FSO / ISR report / radar |
| Location Confidence | Required | Confirmed / Suspected / Templated | Targeting Officer |
| Last Detection DTG | Required | Date-time group | Auto from sensor or manual entry |
| Reporting Source | Required | Sensor type / unit reporting | Targeting Officer / 13F |
| HPTL Priority | Required (for HPTL targets) | Numeric rank | FSCOORD |
| AGM Link | Required (for HPTL targets) | Link to AGM entry | Targeting Officer |
| Collection Requirement | Required (for unconfirmed targets) | ISR task identifier | Targeting Officer / S2 |
| Target Status | Required | Active / Engaged / Assessed / Archived | Targeting Officer / 13F |
| BDA Link | Optional (required when BDA exists) | Link to BDA record | Targeting Officer / 13F |
| Engagement History | Optional | Log of prior engagements | Auto from fire mission links |
| Re-attack Recommended | Optional | Yes / No + basis | Targeting Officer |
| ROE Category | Required | ROE category per AGM | FSCOORD |
| Collateral Damage Estimate | Required | CDE tier (I-V) | SJA / Targeting Officer |

---

## APPENDIX D — FIRES-INTEL INTEGRATION CHECKLIST

**D-1. Purpose.** This checklist supports the fires cell and targeting officer in ensuring fires-intel integration is complete before and during targeting operations. Complete before each targeting working group (TWG).

| # | Checklist Item | Responsible Position | Verified (Y/N) |
|---|---------------|---------------------|----------------|
| 1 | Current collection plan (ISRM) linked to all HPTL target categories | Targeting Officer / S2 | |
| 2 | All HPTL targets have at least one confirmed or active collection requirement | Targeting Officer | |
| 3 | PIR questions are linked to HPT categories requiring detection | S2 / Targeting Officer | |
| 4 | Current intelligence products (OPFOR template, SIGINTSUMMARY) reviewed for target updates | S2 / Targeting Officer | |
| 5 | Radar data (Q-36/Q-37 POO data) reviewed for potential counterfire target nominations | Counterfire Officer / 13R | |
| 6 | All confirmed target detections linked to target records in MSS | Targeting Officer | |
| 7 | BDA records for all engaged targets updated and reviewed | Targeting Officer / 13F | |
| 8 | Re-attack nominations reviewed against current collection plan for updated targeting data | Targeting Officer / S2 | |
| 9 | Intelligence gaps affecting targeting identified and submitted as collection requirements | S2 / Targeting Officer | |
| 10 | JTL synchronized with HPTL — no duplicates, no conflicts | Targeting Officer (div and above) | |
| 11 | EW intelligence integrated with fires targeting (where applicable and authorized) | EW Officer / Targeting Officer | |
| 12 | BDA trending reviewed for indicators of OPFOR reconstitution or target category change | S2 / Targeting Officer | |
| 13 | All ISR collection results from previous cycle reviewed for missed or late target reports | S2 | |
| 14 | Sensitive site list reviewed against targeting plan — no targeting conflicts | SJA / Targeting Officer | |
| 15 | LOAC review complete for all targets on approved strike list | SJA / FSCOORD | |

---

## APPENDIX E — AMD OPERATIONS QUICK REFERENCE IN MSS

**E-1.** This quick reference supports 14A AMD officers and AMD operations NCOs in maintaining AMD data in MSS.

**E-2. Daily AMD MSS Tasks:**
1. Update all AMD system readiness status (FMC/PMCI/PMCII/NMC) with DTG.
2. Update missile/gun inventory for all systems.
3. Confirm CAL/DAL currency — update any asset that has moved or changed status.
4. Review AMD coverage display for gaps — report gaps to AMD TF commander.
5. Confirm engagement authority status for all systems is current and correct.
6. Review air picture display — confirm AMDWS/IBCS data feed is active.
7. Submit daily AMD SITREP from MSS AMD module.

**E-3. On-Event AMD MSS Tasks:**
- On engagement: enter engagement record within 15 minutes (system, track type, engagement outcome).
- On system outage/return to service: update system status immediately.
- On ROE change: update engagement authority record with approving officer and DTG.
- On CAL/DAL change: update CAL/DAL with change basis and FSCOORD/AMD TF CDR approval.
- On air threat: ensure AMDWS/IBCS feed is active; confirm MSS air picture reflects current tracks.

**E-4. Warning: Engagement Authority in MSS.** The engagement authority displayed in MSS reflects the commander-approved ROE status entered by the 14A. It is a record of command decisions, not an automated authorization system. When the displayed engagement authority does not match the commander's direction, correct the MSS record immediately and report the discrepancy.

**E-5. AMD SITREP Reporting from MSS.** The daily AMD SITREP is generated from the AMD module by the AMD operations NCO or 14A. The SITREP includes: all AMD system readiness status, missile inventory by type, engagement log for the reporting period, CAL/DAL status, and coverage gap summary. The AMD TF commander reviews the SITREP before submission to higher headquarters. Any coverage gap or system degradation below PMCI for a primary DAL-defending system is flagged to the AMD TF commander immediately — not deferred to the SITREP cycle.

**E-6. Cross-training requirement.** Each AMD operations center should have at least two personnel proficient in AMD MSS tasks — the primary 14A or operations NCO, and a designated backup. AMD operations do not pause for duty shifts or personnel absences. Backup proficiency for AMD MSS tasks is a readiness requirement, not an optional training goal.

**E-7. AMD MSS and operational security.** CAL/DAL data, AMD system positions, engagement authority status, and air track data are operationally sensitive. AMD personnel must treat MSS screenshots, exports, and data pulls from the AMD module with the same OPSEC discipline as any AMD operations product. Do not export AMD position data or CAL/DAL to uncontrolled networks, personal devices, or shared drives without explicit authorization from the AMD TF commander and in compliance with the unit classification guide.

---

## GLOSSARY

**ACA (Airspace Coordination Area).** A three-dimensional block of airspace in a target area, established by the appropriate airspace authority, to facilitate the simultaneous attack of targets by air and surface fires.

**AFATDS (Advanced Field Artillery Tactical Data System).** The Army's digital fire direction system for cannon, rocket, and mortar units. AFATDS processes fire missions, computes ballistic solutions, and communicates fire commands to firing elements. AFATDS is authoritative for fire direction; MSS is the fires staff integration and visualization layer.

**AGM (Attack Guidance Matrix).** A decision-making tool that tells fires elements how to attack high-payoff targets. The AGM provides approved delivery systems, desired effects, ROE considerations, and re-attack criteria for each target category on the HPTL.

**AMD (Air and Missile Defense).** Defensive measures designed to destroy attacking enemy aircraft or missiles in the atmosphere, or to nullify or reduce the effectiveness of such attack.

**ATZ (Attack Target Zone).** A priority subset of the counterfire radar's cued target zone. Targets within the ATZ receive the highest priority for detection and reporting.

**BDA (Battle Damage Assessment).** The timely and accurate estimate of damage resulting from the application of lethal or non-lethal means. BDA comprises physical destruction, functional damage, and system disruption assessments.

**CAL (Critical Asset List).** A prioritized list of assets or areas designated by a commander for protection from enemy action or exploitation.

**CFF (Call for Fire).** A request for fire containing data necessary for the delivery of fire on a target.

**CTZ (Cued Target Zone).** A geographic area assigned to a counterfire radar for target detection and reporting.

**D3A (Decide-Detect-Deliver-Assess).** The targeting methodology used by Army fires to synchronize fires with maneuver and enable the commander to affect enemy systems and functions.

**DAL (Defended Asset List).** The sublist of assets from the critical asset list that the joint force commander has chosen to defend with active air and missile defense assets.

**DEAD (Destruction of Enemy Air Defenses).** Activity that permanently degrades surface-based air defense by destroying or disabling target systems.

**FSCM (Fire Support Coordination Measure).** A measure employed by land or amphibious commanders to facilitate the rapid engagement of targets and simultaneously provide safeguards for friendly forces.

**FSCOORD (Fire Support Coordinator).** The officer responsible for coordinating fires with maneuver and integrating fires into the scheme of maneuver. Typically the artillery commander at BCT and division level.

**FSEM (Fire Support Execution Matrix).** A product that integrates all fire support tasks into the scheme of maneuver, synchronized by phase and event.

**HPTL (High-Payoff Target List).** A prioritized list of high-payoff targets selected by the targeting working group, approved by the commander, that the commander wants to engage.

**HIMAD (High-to-Medium Altitude Air Defense).** AMD operations conducted by Patriot and other systems in the medium and high altitude bands.

**IBCS (Integrated Air and Missile Defense Battle Command System).** The Army's digital AMD battle management system that integrates AMD sensors, weapons, and command elements.

**JTL (Joint Target List).** A consolidated list of selected targets of interest to the joint force, maintained by the joint targeting process.

**MET (Meteorological).** Data concerning atmospheric conditions (temperature, wind, pressure, humidity) used to compute ballistic corrections for indirect fires. MET messages are produced by 13S MET survey teams.

**MOE (Measure of Effectiveness).** A criterion used to assess changes in system behavior, capability, or operational environment attributes relevant to measuring the attainment of an end state, achievement of an objective, or creation of an effect.

**MOP (Measure of Performance).** A criterion used to assess friendly actions that is tied to measuring task accomplishment.

**NFA (No Fire Area).** A designated area into which no fires or the effects of fires are delivered.

**POI (Point of Impact).** The geographic location where an indirect fire projectile or rocket impacts. Reported by Firefinder radar and ground observers.

**POO (Point of Origin).** The geographic location from which indirect fire is delivered. Computed by Firefinder radar from back-azimuth of the detected trajectory.

**RFA (Restrictive Fire Area).** An area in which specific restrictions are imposed and into which fires that exceed those restrictions will not be delivered without coordination with the establishing headquarters.

**ROE (Rules of Engagement).** Directives issued by competent military authority that delineate the circumstances and limitations under which forces will initiate and/or continue combat engagement with other forces encountered.

**SEAD (Suppression of Enemy Air Defenses).** Activity that neutralizes, destroys, or temporarily degrades surface-based enemy air defenses by destructive and/or disruptive means.

**SHORAD (Short-Range Air Defense).** AMD operations conducted by Avenger, M-SHORAD, and MANPADS systems in the low altitude band.

**TST (Time-Sensitive Target).** A target requiring immediate response because it presents a highly lucrative, fleeting opportunity and/or it poses (or will soon pose) a danger to friendly forces.

**TLE (Target Location Error).** The difference between the reported or estimated location of a target and the actual location of the target. TLE is driven by sensor accuracy, range to target, and age of detection. MSS target confidence levels (Confirmed, Suspected, Templated) are categorical representations of TLE risk. High TLE requires either higher-accuracy confirmation before fires, or munitions with sufficient effects radius to compensate.

**TWG (Targeting Working Group).** A staff working group that meets regularly to review the HPTL, assess BDA, develop re-attack recommendations, and synchronize the targeting cycle.

**PACE (Primary, Alternate, Contingency, Emergency).** A communications and data management planning framework used to ensure operations continue when primary methods are unavailable. Fires cells maintain PACE plans for all critical fires data management functions. MSS is typically the primary method; alternate digital tools (ATAK, shared drives), voice, and manual methods fill the remaining tiers.

**FSPLAN (Fire Support Plan).** The fires annex to the operations order that describes the scheme of fires, fire support tasks, FSCM locations, target priorities, and fires synchronization guidance. In MSS, the FSPLAN exists as a linked set of data objects (HPTL, AGM, FSCM overlay, FSEM) rather than a single document. Maintaining consistency between the written FSPLAN and the MSS data objects is a fires cell data stewardship obligation.

**CAS (Close Air Support).** Air action by fixed- or rotary-wing aircraft against hostile targets that are in close proximity to friendly forces. CAS requires detailed integration with the fire and movement of ground forces. In MSS, CAS requests are tracked in the joint fires module linked to the target list. FSCM overlay currency is critical for all CAS missions near coordination boundaries.

**ISRM (Intelligence, Surveillance, and Reconnaissance Synchronization Matrix).** A planning product that links collection assets to collection requirements against specific target categories. In MSS, the ISRM links collection assets to HPTL target categories, enabling the fires cell and targeting officer to track which HPTs have active collection coverage and identify collection gaps that require tasking action.

---

## APPENDIX F — PROFESSIONAL READING LIST

> Curated articles from Army professional journals and military publications. These supplement doctrinal references with contemporary operational perspectives.

| Source | Title | Date | Relevance |
|---|---|---|---|
| Field Artillery Bulletin | "The New Digital Kill Chain" | 2025 | Digital fire support modernization |
| Field Artillery Bulletin | "AI's New Frontier in War Planning" | 2025 | AI in fire support planning |
| Field Artillery Bulletin | "Project Convergence: Revolutionizing Targeting in LSCO" | 2025 | Joint fires convergence |
| Field Artillery Bulletin | "Enhancing Tactical Level Targeting With AI" | 2024 | AI-assisted targeting |
| Field Artillery Bulletin | "The Future of Strategic Fires Target Acquisition" | 2024 | Strategic fires modernization |

---

## APPENDIX — RELATED MANUALS AND TRAINING TRACKS

### WFF Peer Tracks

TM-40B is one of six Warfighting Function tracks at the same tier. All six WFF tracks require TM-10, TM-20, and TM-30 as prerequisites. Fires practitioners should develop working familiarity with TM-40A (Intelligence) and TM-40C (Movement and Maneuver) — the peer tracks with the most intensive fires coordination requirements.

**Table. WFF Peer Track Quick Reference**

| Track | Title | Prereq | Primary Fires Coordination Point |
|-------|-------|--------|----------------------------------|
| TM-40A | Intelligence WFF | TM-10 + TM-20 + TM-30 | Targeting workspace, ISR task/collect, BDA data |
| TM-40B | Fires WFF | TM-10 + TM-20 + TM-30 | This manual |
| TM-40C | Movement and Maneuver WFF | TM-10 + TM-20 + TM-30 | FSCM coordination, airspace deconfliction |
| TM-40D | Sustainment WFF | TM-10 + TM-20 + TM-30 | CSR, ammunition status, LOGSTAT |
| TM-40E | Protection WFF | TM-10 + TM-20 + TM-30 | AMD coordination — fires and protection share AMD data domain |
| TM-40F | Mission Command WFF | TM-10 + TM-20 + TM-30 | CCIR monitoring, fires products to commander's COP |

### Specialist Tracks (Prerequisite: TM-30)

For technical specialists pursuing advanced data engineering or analytical capability, specialist tracks are available after completing TM-30. Not required for fires WFF employment.

**Table. Specialist and Advanced Track Quick Reference**

| Track | Title | Advanced Track |
|-------|-------|----------------|
| TM-40G | ORSA | TM-50G |
| TM-40H | AI Engineer | TM-50H |
| TM-40M | ML Engineer | TM-50M |
| TM-40J | Program Manager | TM-50J |
| TM-40K | Knowledge Manager | TM-50K |
| TM-40L | Software Engineer | TM-50L |

---

*UNCLASSIFIED // FOR OFFICIAL USE ONLY*

*TM-40B, Version 1.0, March 2026*

*HEADQUARTERS, UNITED STATES ARMY EUROPE AND AFRICA, Wiesbaden, Germany*

*This publication supersedes all previous guidance on fires operations in MSS within USAREUR-AF. Questions regarding this publication should be directed to the USAREUR-AF C2DAO fires functional area representative.*

---

**CHANGE LOG**

| Version | Date | Description of Change | Authority |
|---------|------|----------------------|-----------|
| 1.0 | March 2026 | Initial publication | USAREUR-AF C2DAO |

*Future changes to this manual will be published as versioned updates through the USAREUR-AF C2DAO learning management system. Units are responsible for maintaining the current version and distributing changes to all fires personnel.*

**DoD and Army Strategic References:**

- **JADC2 Strategy Summary (March 2022)** — Cross-domain data integration strategy for Joint All-Domain Command and Control
- **DoD Directive 3000.09, Autonomy in Weapon Systems (January 2023 update)** — Policy on autonomous and semi-autonomous functions in weapon systems; context for fire control and targeting systems
- **DDOF Playbook v2.2 (December 2025)** — T2COM C2DAO; VAULTIS-A quality framework (8 dimensions); 6-phase data product lifecycle; 85% quality gate; MVP mandate 30 days
