# TM-40C — MAVEN SMART SYSTEM (MSS)

> **Forward:** The Movement and Maneuver (M&M) warfighting function encompasses all tasks associated with moving and employing forces to achieve a position of advantage over the enemy (ADP 3-0, para 3-3). MSS supports M&M by integrating force tracking, route data, obstacle overlays, reconnaissance products, and operational graphics into a single enterprise platform accessible across the formation.
> **Prereqs:** TM-10, Maven User; TM-20, Builder; TM-30, Advanced Builder; CONCEPTS_GUIDE_TM40C_MOVEMENT_MANEUVER (required before beginning this manual). No coding, pipeline development, or transform experience is required or assumed.
> *HQ USAREUR-AF · v1.0 · 2026 · DISTRIB: USG only · AUTH: C2DAO/UDRA v1.1*

> **WARNING: Using stale MSS obstacle or route data without verification during a breach or route clearance operation can result in personnel casualties and mission failure. Always confirm obstacle and route data currency against S2 and engineer reporting channels before committing forces.**
> **CAUTION: MSS Blue Force Tracking displays the last reported position of a unit — not its current position. BFT update intervals, comms outages, and GPS errors can produce positional errors on the display. Do not use MSS BFT as the sole reference for fire support deconfliction, no-fire area management, or fratricide prevention.**
> **NOTE: MSS does not replace the military decision-making process, reconnaissance, or the commander's estimate. It integrates and visualizes the information that feeds those processes. ADP 3-0 combined arms integration requires human analysis and synthesis. MSS provides the data layer to support it.**

---

## CHAPTER 1 — OVERVIEW: MOVEMENT AND MANEUVER FUNCTION IN MSS

**BLUF:** The Movement and Maneuver (M&M) warfighting function encompasses all tasks associated with moving and employing forces to achieve a position of advantage over the enemy (ADP 3-0, para 3-3). MSS supports M&M by integrating force tracking, route data, obstacle overlays, reconnaissance products, and operational graphics into a single enterprise platform accessible across the formation.

### 1-1. Movement & Maneuver Specialist Manual

The Movement and Maneuver warfighting function includes the tasks of maneuver, mobility, countermobility, air maneuver, and interoperability with joint and multinational partners (ADP 3-0, para 3-3). On MSS, M&M data is not isolated — it is integrated with fires, intelligence, protection, sustainment, and mission command data layers. This integration is the operational value of MSS for M&M practitioners.

Historically, M&M practitioners managed operational graphics in one system (CPCE), force tracking in another (FBCB2/JBC-P), route data in spreadsheets, and obstacle data in separate engineer overlays. Reconciling these sources during a dynamic operation consumed significant S3 section time. MSS consolidates these data streams — not by replacing each source system, but by integrating their outputs into a unified operational picture.

> **NOTE: MSS integrates data from authoritative source systems. It does not replace them. CPCE remains the authoritative OPORD management system. JBC-P remains the authoritative Blue Force Tracking feed. MSS visualizes and analyzes data from these systems in a unified environment.**

### 1-2. Combined Arms Operations and MSS

ADP 3-0 defines combined arms as the synchronized and simultaneous application of arms to achieve an effect greater than if each arm had been employed separately (ADP 3-0, para 1-5). MSS enables combined arms by making cross-functional data visible simultaneously across all arms.

The S3 who can see the unit's infantry force tracking, engineer obstacle clearance status, fires synchronization line, and aviation deconfliction data on a single MSS workspace makes better combined arms decisions than one who assembles those products from separate systems during the battle captain battle update. The advantage is not the platform — it is the integration of data that previously lived in silos.

**Table 1-1. Combined Arms Data Integration in MSS**

| Arm | Primary Data Type in MSS | Integration Value |
|---|---|---|
| Infantry / Armor | Force tracking, phase line reporting, objective status | Ground maneuver synchronization |
| Engineers | Obstacle overlays, route classification, breach status | Mobility / countermobility picture |
| Fires | Fire support coordination measures (FSCMs), target overlays | Maneuver-fires deconfliction |
| Aviation | Air corridor status, LZ/PZ tracking, CASEVAC status | Airspace deconfliction |
| Intelligence | NAI/TAI overlays, PIR status, enemy situation | Decision support for maneuver timing |
| Sustainment | CL III/V status, maintenance readiness, route capacity | Combat power projection |

### 1-3. M&M Data Types in MSS

M&M practitioners work with six primary data types on MSS.

**Unit location data.** Unit locations reported through JBC-P, manual position reports, or integrated tracking systems. Represents the friendly force ground picture — both current and historical.

**Route data.** MSR/ASR designations, route reconnaissance reports, bridge classification data, and route status (open/closed/restricted). Maintained by the S3 section in coordination with engineers.

**Obstacle overlays.** Engineer-maintained obstacle data including minefield overlays, vehicle obstacle classifications, FASCAM reports, and deliberate obstacle data. Source of record for mobility/countermobility products.

**Operational graphics.** Phase lines, objectives, boundaries, axes of advance, fire support coordination measures, and all tactical control measures. The shared reference for combined arms integration.

**Reconnaissance products.** Named areas of interest (NAIs), targeted areas of interest (TAIs), reconnaissance objectives, screen lines, and observation post locations. Source of record for the reconnaissance and security effort.

**Combat power data.** Equipment readiness status, personnel accountability, and ammunition status by unit — the basis for maneuver unit combat power assessment.

### 1-4. MSS Versus Legacy Tools

**Table 1-2. MSS vs. Legacy M&M Tools**

| Function | Legacy Tool | MSS Capability | Key Difference |
|---|---|---|---|
| OPORD Management | CPCE | MSS OPORD Viewer / Foundry Workshop | MSS integrates OPORD with live execution data |
| Force Tracking | FBCB2 / JBC-P | MSS BFT Integration Dashboard | MSS adds analytics and historical track replay |
| Route Management | Spreadsheet / unit SOP | MSS Route Analysis Dashboard | MSS integrates route data with obstacle and engineer reporting |
| Fire Support Coordination | JADOCS / AFATDS | MSS FSCM Layer | MSS displays FSCM alongside maneuver graphics |
| Aviation Coordination | AMDCOORD / TAIS | MSS Airspace Dashboard | MSS integrates airspace with ground maneuver picture |
| Obstacle Data | Engineer overlay / paper | MSS Obstacle Layer | MSS links obstacle data to route status and breach planning |

> **CAUTION: MSS does not replace CPCE for OPORD publication, JADOCS/AFATDS for fire mission processing, or JBC-P for authoritative BFT. Use MSS to integrate and analyze data from these systems — not to replace their primary functions.**

### 1-5. Workspace Organization for Combined Arms Units

M&M units organize MSS workspaces by operational function, not by section. A combined arms workspace that displays force tracking, obstacle overlays, and fire support coordination measures simultaneously is more useful to the S3 section than three separate workspaces organized by data type.

**Standard M&M Workspace Configuration:**

- **Layer 1 (Base):** Operational graphics — phase lines, boundaries, objectives, axes
- **Layer 2 (Blue Force):** Friendly unit tracking — current positions, tracks, last-reported
- **Layer 3 (Red Force):** Enemy situation — known/templated, NAI/TAI overlays
- **Layer 4 (Engineer):** Obstacle overlays, route status, bridge classifications
- **Layer 5 (Fires):** FSCM, no-fire areas, target overlays
- **Layer 6 (Aviation):** Air corridors, LZ/PZ, restricted areas

> **NOTE: Activate only the layers required for the current task. Displaying all six layers simultaneously produces visual clutter that degrades situational awareness rather than improving it. Use layer toggles to manage display density.**

### 1-6. The S3/G3 as Primary M&M Data Manager

The S3/G3 section is the primary data manager for M&M data in MSS (FM 3-0, para 4-2). This includes operational graphics, force tracking oversight, route status management, and combined arms synchronization data. The S3 section does not own all M&M data — engineer data is owned by the engineer staff section, fires data by the FSO/FECC, aviation data by the A2C2 — but the S3 coordinates and integrates all M&M data streams into the combined arms picture.

**Table 1-3. M&M Data Ownership by Section**

| Data Type | Primary Owner | Secondary (Coordination) | MSS Workspace Role |
|---|---|---|---|
| Operational graphics | S3 / G3 | XO review | Publish, maintain currency |
| Force tracking | S3 | S6 (network), S2 (integration) | Monitor, validate against reports |
| Route status | S3 | 12A/12B (engineer section) | Update on receipt of route recon |
| Obstacle data | 12A/12B (engineer) | S3 (integration) | Publish to shared workspace |
| FSCM graphics | FSO / FECC | S3 (deconfliction) | Maintain in fires layer |
| Aviation corridors | A2C2 / 15A | S3 (deconfliction) | Maintain in aviation layer |
| PIR/NAI/TAI | S2 | S3 (targeting) | Maintain in Intel layer |

---

## CHAPTER 2 — OPERATIONAL PLANNING AND ORDERS IN MSS

**BLUF:** MSS supports every step of the Military Decision-Making Process (MDMP) by integrating data that informs each step — from mission analysis through orders production. This chapter describes how S3 sections and operations officers use MSS during MDMP and orders management.

### 2-1. MDMP Support in MSS

The MDMP is a deliberate, collaborative, and iterative planning process (FM 5-0, para 1-1). MSS does not replace MDMP or any of its seven steps. It improves the quality of information available at each step by making data accessible, integrated, and current.

**Step 1 — Receipt of Mission.** Load the higher headquarters OPORD overlay immediately upon receipt. Establish the operational graphics layer with phase lines, boundaries, and objectives from higher. This creates the shared geographic reference that all subsequent planning builds on.

**Step 2 — Mission Analysis.** Use the MSS Intelligence layer to display current enemy situation, NAI/TAI overlays, and IPB products. Use the terrain analysis data to review route classifications, obstacle data, and mobility corridors. Cross-reference S2-maintained enemy overlays with engineer route and obstacle data.

**Step 3 — COA Development.** Use MSS to sketch and compare COA graphics. Create draft operational overlays for each COA. Use route data to assess mobility corridors for each COA axis of advance.

**Step 4 — COA Analysis (Wargame).** Display competing COA overlays simultaneously for comparison. Use historical route data and obstacle reports to assess COA feasibility. Display the fires synchronization matrix and FSCM constraints against each COA.

**Step 5 — COA Comparison.** Display COA decision matrix data in Workshop. Use readiness and combat power data to validate which COAs are supportable given current unit status.

**Step 6 — COA Approval.** Brief the commander using MSS workspace displays. The commander's workspace should show the selected COA, current force posture, and the key decision points.

**Step 7 — Orders Production.** Finalize operational graphics in MSS. Publish phase lines, objectives, boundaries, and fire support coordination measures to the formation's shared workspace. Confirm subordinate units can see the published graphics before OPORD briefing.

> **NOTE: MSS supports MDMP as a data integration layer — it does not conduct wargaming, recommend COAs, or produce the OPORD. Staff analysis and commander judgment remain the center of each MDMP step.**

### 2-1a. Operational Variables and Mission Variables as MSS Data Frameworks

ADP 3-0 (Operations, March 2025) establishes two complementary variable sets that define what data the M&M analyst must collect and organize in MSS. Operational variables describe the broad operational environment. Mission variables describe the specific factors a commander analyzes for a given operation. Together, they form the data collection and planning framework for every MDMP iteration.

**Operational Variables — PMESII-PT (ADP 3-0, para 1-8).** The eight operational variables define the operational environment (OE) at the strategic and operational level. M&M analysts use PMESII-PT to structure OE analysis data in MSS before planning begins.

**Table 2-1a. PMESII-PT Operational Variables as MSS Data Categories**

| Variable | Full Name | M&M Data Relevance | MSS Data Source |
|---|---|---|---|
| P | Political | Host nation political boundaries, governance structures, status of forces agreements affecting freedom of movement | S9/POLAD input, Intel layer |
| M | Military | Threat force composition, disposition, and doctrine; friendly force laydown | S2 Intel layer, BFT layer |
| E | Economic | Infrastructure capacity (roads, bridges, rail), industrial areas affecting route planning | Route layer, engineer data |
| S | Social | Population centers, displaced persons routes, civilian movement patterns | S9/S5 data, protection layer |
| I | Information | Communications infrastructure, EMCON considerations, information operations effects | S6 data, IO cell input |
| I | Infrastructure | Transportation networks, utilities, key facilities that constrain or enable maneuver | Route layer, engineer recon |
| P | Physical Environment | Terrain, weather, hydrology, vegetation — directly affects mobility corridors | Terrain analysis layer, weather feed |
| T | Time | Operational timelines, seasonal effects on terrain, light data | Planning timeline data |

**Mission Variables — METT-TC(I) (ADP 3-0, March 2025; FM 5-0, para 2-4).** The seven mission variables are the planning data framework the commander and staff analyze for each specific operation. The "I" (Informational Considerations) was added in the March 2025 revision of ADP 3-0 to account for the information dimension of operations.

**Table 2-1b. METT-TC(I) Mission Variables as MSS Planning Data**

| Variable | Full Name | MSS Data Product | Primary Staff Section |
|---|---|---|---|
| M | Mission | OPORD/FRAGO text and graphics | S3 |
| E | Enemy | Enemy situation overlay, SITTEMP, OB data | S2 (Intel layer) |
| T | Terrain and Weather | Terrain analysis (OAKOC), weather overlays, light data | S2/engineer |
| T | Troops and Support Available | Task organization, combat power dashboards, enabler availability | S3/S1/S4 |
| T | Time Available | Planning timeline, movement timeline, phase triggers | S3 |
| C | Civil Considerations | ASCOPE analysis, civilian movement data, key infrastructure | S9/S5 |
| (I) | Informational Considerations | Information environment effects, OPSEC indicators, adversary information capabilities | IO cell / S3 |

> **NOTE: METT-TC(I) with the added "I" for Informational Considerations reflects ADP 3-0 (March 2025). Units still using METT-TC without the "I" should update their planning frameworks. In MSS, Informational Considerations data is maintained as a separate data category in the planning workspace to ensure it is not overlooked during mission analysis.**

The M&M analyst's responsibility is to ensure MSS contains structured, current data for each variable before MDMP Step 2 (Mission Analysis) begins. A mission analysis conducted against an MSS workspace that lacks data for one or more PMESII-PT or METT-TC(I) variables has a blind spot the staff may not recognize.

### 2-2. OPORD Visualization in MSS

Once the OPORD is published, the S3 section maintains the OPORD graphics in MSS as the authoritative visual reference. This includes:

**Control Measures.** Phase lines, limit of advance (LOA), line of departure (LD), assault positions, attack positions, objectives, axes of advance, and directions of attack. Each must be loaded with correct military symbology, labeled with the doctrinal designator, and assigned to the correct layer.

**Fire Support Coordination Measures.** Coordinated fire line (CFL), fire support coordination line (FSCL), no-fire areas (NFA), restrictive fire areas (RFA), restrictive fire lines (RFL), and final protective fires (FPF). These must be maintained in the fires layer and updated immediately when changed.

**Task Organization Graphics.** Unit boundaries, areas of operations (AO), and tactical assembly areas (TAA). These define the geographic framework for combined arms integration and must match the OPORD graphics exactly.

> **WARNING: OPORD graphics in MSS must match the published OPORD exactly. Any discrepancy between the MSS display and the published OPORD creates risk of fratricide, boundary violations, and fires coordination errors. Verify graphics against the published OPORD after every update.**

### 2-3. COA Development and Comparison Data

During COA development, the S3 uses MSS to overlay planning data on the operational graphics.

**Route Analysis for COA Development.** Display MSR/ASR data, route classification, and obstacle reports against the proposed COA axes of advance. A COA that routes the main effort along a route with a known bridge gap or active obstacle belt requires either a mobility task or an alternate route.

**Combat Power Assessment by COA.** Load the current readiness and strength data for each maneuver unit. Compare task organization requirements against actual combat power available. A COA that requires a degraded battalion to serve as the main effort is at risk.

**Time-Distance Analysis.** Use historical movement data and route capacity data to assess whether each COA is achievable within the timeline. MSS route data includes estimated movement times based on route classification and unit type where this data has been loaded.

### 2-4. Task Organization Display and Tracking

Task organization in MSS is a dynamic product — it changes with every FRAGO. The S3 section is responsible for maintaining the current task organization in MSS at all times.

**Standard Task Organization Display:**
- Echelon, unit designation, and parent relationship
- Current OPCON/TACON relationships when applicable
- Attachment status and effective date/time
- Key weapons and enabler attachments (engineer platoon, fire support team, etc.)

> **CAUTION: Task organization displays in MSS become inaccurate when FRAGOs are not processed promptly. A stale task organization display will show a unit in the wrong parent relationship — which distorts the combined arms synchronization picture and can cause coordination gaps.**

### 2-5. FRAGO Management and Version Control

FRAGOs are the tactical commander's primary tool for adjusting operations in execution. MSS supports FRAGO management by maintaining version-controlled graphics and data updates.

**FRAGO Processing Procedure:**

1. Receive FRAGO from higher via primary means (voice/digital).
2. Identify all graphic changes in the FRAGO (new phase lines, boundary changes, updated objectives, revised FSCM).
3. Update MSS graphics to reflect FRAGO changes. Note the FRAGO number and effective DTG.
4. Notify all subordinate S3 sections that the MSS workspace has been updated.
5. Confirm subordinate S3s have acknowledged the update and the change is reflected at their echelon.

> **NOTE: Every MSS graphic change associated with a FRAGO must be annotated with the FRAGO number and effective DTG in the object metadata. This creates a version trail that allows reconstruction of the operational picture at any point in execution.**

### 2-6. Fire Support Plan Integration with Maneuver Graphics

The fires officer (FSO) maintains fire support graphics in the fires layer of MSS. The S3 section integrates fires graphics with maneuver graphics to produce the combined arms synchronization display.

**Integration Checklist:**
- FSCMs are displayed in the fires layer, visible to both the S3 and FSO
- Phase line triggers for FSCM changes are annotated in the graphics
- No-fire areas are cross-referenced against maneuver routes and assembly areas
- Artillery position areas (APA) are displayed and deconflicted against maneuver routes
- Target overlays are integrated with NAI/TAI and ground maneuver objectives

---

## CHAPTER 3 — ROUTE PLANNING AND MOBILITY OPERATIONS

**BLUF:** Route planning and mobility operations in MSS integrate engineer data, reconnaissance reports, and obstacle overlays into a unified route picture. The S3 and engineer staff sections maintain this data collaboratively. Route decisions must always be validated against current field reporting — MSS displays what has been reported, not what is currently on the ground.

### 3-1. Route Analysis in MSS: MSR/ASR Management

Main supply routes (MSRs) and alternate supply routes (ASRs) are the logistical and maneuver arteries of the AOR. MSS maintains a route management layer that integrates route classification, current status, and reporting history.

**Route Data Elements in MSS:**

| Data Field | Description | Owner | Update Trigger |
|---|---|---|---|
| Route Designation | MSR/ASR name/number (e.g., MSR TAMPA) | S3 | OPORD / FRAGO |
| Route Classification | Vehicle classification, surface type, bridge MLC | 12A/12B | Route recon report |
| Current Status | Open / Restricted / Closed | S3 (with engineer input) | Status report or incident |
| Threat Overlay | IED/mine threat, enemy interdiction overlay | S2 | Intelligence update |
| Clearance Date/Time | Last route clearance DTG | Engineer section | Route clearance report |
| Chokepoints | Bridge locations, tunnels, ford sites, grades | 12A/12B | Route recon report |

### 3-2. Engineer Mobility Data: Obstacle Reports and Bridge Classification

The engineer section (12A officer, 12B NCO) is the primary owner of mobility data in MSS. This includes:

**Obstacle Reports (OBSREP).** Reported obstacles are loaded into the obstacle layer with location, type (wire, ditch, minefield, reinforced), emplacing agency (friendly/enemy/unknown), and status (breached/unbreached/bypassed).

**Bridge Classifications.** Military load classification (MLC) for each bridge on MSR/ASR routes. MLC data is loaded by the engineer section and updated after bridge reconnaissance or following any bridge damage report.

**Minefield Data.** FASCAM (Family of Scatterable Mines) and deliberate minefield overlays are maintained as polygon graphics in the obstacle layer. Each minefield must include: location, size, date emplaced, emplacing unit, self-destruct time (FASCAM), and breach lane status.

> **WARNING: Minefield overlays on MSS represent reported positions only. Actual minefield boundaries may vary from reported positions due to delivery error, wind drift (FASCAM), or emplacement error. Always maintain a safety buffer when routing forces near reported minefield overlays.**

### 3-3. 12B/12A Engineer Workflow: Mobility/Countermobility/Survivability

Combat engineers support M&M through three tasks (FM 3-0, para 3-12):

**Mobility.** Reducing or breaching obstacles to allow friendly forces to move. MSS tracks mobility task status (obstacle cleared, breach lane open/closed, ford improved) and provides the combined arms force the current mobility picture.

**Countermobility.** Emplacing obstacles to restrict, disrupt, or delay enemy movement. MSS maintains the friendly obstacle overlay as the authoritative record of deliberate obstacles emplaced by friendly engineers. This record is critical for fratricide prevention when friendly forces retrograde through their own obstacle belt.

**Survivability.** Field fortifications, fighting positions, and force protection works. MSS can track survivability work by unit and location when engineer sections maintain this data.

**Engineer MSS Daily Tasks:**
1. Review obstacle layer for currency — update any obstacles reported changed since last review.
2. Review route status layer — update bridge classification and route status from overnight reconnaissance or patrol reports.
3. Confirm MSS obstacle layer matches the engineer section's hard copy obstacle record.
4. Post any new OBSREP data received from subordinate engineers or patrols.
5. Coordinate with S3 to ensure obstacle data is visible in the combined arms workspace.

### 3-4. Route Clearance Operations Tracking

Route clearance operations are tracked in MSS to provide the S3 a real-time picture of route status across the AOR.

---

**TASK: Route Clearance Tracking in MSS**

**CONDITIONS:** A route clearance team has completed a clearance operation on MSR TAMPA. The S3 section has received a route clearance report via voice and digital means.

**STANDARDS:** The S3 section updates the MSS route status layer within 30 minutes of clearance report receipt. The update includes: clearance DTG, reporting unit, route segment cleared, any obstacles found (disposition), and current route status. The update is visible to all subordinate S3 sections.

**PROCEDURE:**

1. Receive the route clearance report. Confirm: reporting unit, route designation, segment start/end grid, clearance DTG, obstacles found/disposition, and current route status.
2. Navigate to the MSS Route Management Dashboard.
3. Select the route segment that was cleared.
4. Update the route status field: Open / Restricted (with restriction details) / Closed.
5. Enter the clearance DTG and reporting unit in the metadata field.
6. If any new obstacles were found: create obstacle report objects in the obstacle layer.
7. Publish the update to the shared combined arms workspace.
8. Notify subordinate S3 sections via primary means that the route status has been updated.

---

### 3-5. Breach Planning Data Requirements

Breach operations are among the most data-intensive operations in the combined arms repertoire. ATP 3-90.8 establishes the breach sequence and combined arms requirements. MSS supports breach planning by integrating the obstacle data, route data, fires data, and force tracking required to plan and execute a deliberate breach.

**Data Requirements for Breach Planning in MSS:**

| Data Requirement | Source | MSS Layer | Criticality |
|---|---|---|---|
| Obstacle location and type | OBSREP / engineer recon | Obstacle layer | Required — cannot plan breach without |
| Obstacle dimensions | Engineer recon | Obstacle layer attributes | Required for lane sizing |
| Breach site approach routes | Route recon | Route layer | Required for task org movement |
| Enemy obstacle covering fires | S2 / SIGINT | Intel layer | Required for suppression planning |
| Fire support coordination | FSO / FECC | Fires layer | Required for suppression, obscuration |
| Engineer force tracking | 12A section | Blue Force layer | Required for synchronization |
| Assault force position | S3 | Blue Force layer | Required for breach coordination |

### 3-6. ATP 3-90.8 Breach Sequence as MSS Workflow

ATP 3-90.8 describes the breach sequence as: suppress, obscure, secure, reduce, assault (SOSRA). MSS supports each phase.

**Suppress.** Fire support plan is displayed in the fires layer. S3 confirms FSCM graphics enable suppression of obstacle covering forces. Fire support triggers are annotated on the operational graphics.

**Obscure.** Smoke plan overlays (if maintained) are displayed in the fires layer. Engineer smoke employment positions are tracked in the Blue Force layer.

**Secure.** Security task organization is displayed in the combined arms workspace. Security element positions and sectors are shown as tactical graphics.

**Reduce.** Engineer force tracking shows breach team positioning. Obstacle layer shows the breach objective. Lane status (open/in-progress/complete) is updated by the engineer section in real time.

**Assault.** Assault force positions are tracked through BFT. Phase lines and limit of advance are displayed. Report triggers for phase line crossings are active in the MSS dashboard.

> **NOTE: MSS supports breach planning and synchronization. It does not replace the breach rehearsal or the breaching task force battle drill. All SOSRA execution is managed by leaders on the ground — MSS provides the shared data layer for command and control above the breach site.**

---

## CHAPTER 4 — RECONNAISSANCE AND SECURITY OPERATIONS

**BLUF:** Reconnaissance and security operations are the maneuver commander's primary tool for reducing uncertainty (FM 3-98, para 1-1). MSS integrates reconnaissance products, named areas of interest, and security mission graphics into the operational picture. The 19D cavalry scout section is the primary M&M data contributor for reconnaissance and security data in MSS.

### 4-1. 19D Cavalry Scout Workflows in MSS

Cavalry scouts (19D) are the primary reconnaissance and security force for BCT and division operations (FM 3-98). The reconnaissance troop S3 and troop commanders use MSS to:

- Display reconnaissance objectives and reconnaissance routes
- Track execution against the reconnaissance plan
- Report reconnaissance findings into the shared operational picture
- Maintain screen/guard/cover mission graphics and phase lines
- Coordinate handoff of reconnaissance information to higher and adjacent

**Daily Scout Section MSS Tasks:**
1. Confirm all reconnaissance objectives are displayed with current status (not started / in progress / complete / reporting).
2. Verify screen line or guard boundary graphics match the current OPORD.
3. Update OP/LP locations from the most recent reporting.
4. Post any new SPOTREP data to the Intel layer (in coordination with S2).
5. Confirm the enemy situation overlay reflects current reconnaissance findings.

### 4-2. Reconnaissance Objective Management

Reconnaissance objectives define what the reconnaissance force must discover (FM 3-98, para 2-4). In MSS, each reconnaissance objective is a named graphic object with:

- Objective designation and geographic location/area
- Priority information requirement (PIR) or IR it supports
- Reconnaissance task assigned (zone, route, area, reconnaissance in force)
- Unit assigned
- Timeline (SP time, RP time, reporting deadline)
- Current status

**Table 4-1. Reconnaissance Objective Status States in MSS**

| Status | Definition | Action Required |
|---|---|---|
| Not Started | Reconnaissance has not begun | Confirm unit SP time |
| In Progress | Reconnaissance element is on objective | Monitor for reporting |
| Complete — Reporting | Reconnaissance complete, SPOTREP submitted | S2 integrates report into picture |
| Complete — No Contact | Objective cleared, nothing significant found | Document for PIR tracking |
| Delayed | Unit has not reached objective by planned time | Notify S3, assess cause |
| Cancelled | Objective removed from plan by FRAGO | Archive object, document reason |

### 4-3. Screen, Guard, and Cover Mission Tracking

Screen, guard, and cover are the three security missions (FM 3-98, para 4-2). Each has distinct graphic requirements in MSS.

**Screen.** Display the screen line as a linear graphic with direction of observation, screen positions (OP/LP), and cavalry troop boundary. Track each screen team/OP as a force tracking object.

**Guard.** Display the guard zone boundary, main body it is protecting, and cavalry squadron axis of advance. Track guard element positions within the guard zone.

**Cover.** Display the cover route/axis, the force being covered, and the AO boundary. Track covering force positions. Coordinate with S2 for enemy contact reporting along the cover axis.

---

**TASK: Load and Manage a Reconnaissance Plan in MSS**

**CONDITIONS:** The S3 section has received a reconnaissance order from higher. The order includes three reconnaissance objectives, a route reconnaissance of MSR MADISON, and a screen mission along Phase Line COBRA. The cavalry troop is preparing to execute.

**STANDARDS:** The S3 section loads all reconnaissance objectives, the route reconnaissance task, and the screen mission graphics into MSS within two hours of OPORD receipt. All graphics are correctly symbologized, labeled, and assigned to the Intelligence or Operations layer as appropriate. Subordinate S3 sections and the S2 can access the reconnaissance plan in the shared workspace.

**PROCEDURE:**

1. Load the three reconnaissance objectives as named graphic objects in the Operations layer. Assign each a priority (1, 2, 3) and the supporting PIR.
2. Create the route reconnaissance graphic for MSR MADISON: start point, route, end point, reporting checkpoints.
3. Load the screen mission: screen line graphic, OP/LP positions (use initial positions from OPORD — update as troop positions), cavalry boundary.
4. Set initial status for all objectives to "Not Started."
5. Publish to the combined arms workspace.
6. Brief S2 that reconnaissance plan is loaded and they should coordinate to update objective status and post SPOTREP data as the mission executes.

---

### 4-4. FM 3-98 Reconnaissance Fundamentals as MSS Data Practice

FM 3-98 establishes five fundamentals of reconnaissance: retain freedom of maneuver, report all information rapidly and accurately, maintain contact (enemy, terrain, key areas), ensure continuous reconnaissance, and develop the situation rapidly (FM 3-98, para 1-8).

**Report all information rapidly and accurately** has direct MSS implications. Reconnaissance information reported through voice alone does not reach the combined arms picture until someone loads it manually. Cavalry scout sections that post SPOTREP data directly into MSS — with S2 coordination — accelerate information integration across the formation. The standard is: every significant reconnaissance report reaches MSS within 30 minutes of receipt at the S3 section.

**Maintain contact** produces a continuous data requirement. OP/LP locations must be updated in MSS every time positions change. Screen line status must reflect real-time execution, not the planned position.

> **NOTE: The reconnaissance principle "report all information rapidly and accurately" (FM 3-98) translates directly to an MSS data currency standard. Reconnaissance data that reaches the S3 but is not posted to MSS has not reached the combined arms picture. MSS is only as current as the data entered into it.**

### 4-4a. Reconnaissance as a Data Collection Operation (FM 3-98)

FM 3-98 (Reconnaissance and Security Operations) defines reconnaissance fundamentally as a data collection operation — the purpose is to obtain information about the enemy, terrain, and civil conditions that reduces uncertainty for the commander. Every reconnaissance mission produces structured data products that must be captured in MSS. The M&M analyst treats reconnaissance outputs as data, not just reports.

**Reconnaissance Types and Their Structured Data Products.** Each reconnaissance type (FM 3-98, Chapter 2) generates a distinct set of data products. The M&M analyst must ensure MSS is configured to receive and store these products before the reconnaissance element departs.

**Table 4-4a. Reconnaissance Types and MSS Data Products**

| Recon Type | Purpose (FM 3-98) | Structured Data Products for MSS |
|---|---|---|
| Route Reconnaissance | Obtain detailed information on a specific route and adjacent terrain | Route classification (surface, width, MLC), bridge data (MLC, width, bypass), obstacle locations and types, chokepoint identification, ford site assessment, overhead clearance |
| Zone Reconnaissance | Obtain detailed information on all routes, obstacles, terrain, and enemy forces within a zone | NAI reports, obstacle overlay updates, terrain trafficability data, enemy contact reports (SPOTREP), civilian activity, key terrain identification |
| Area Reconnaissance | Obtain detailed information on a specific area (town, hill, bridge, intersection) | Facility/structure assessment, enemy disposition within area, obstacle data, civilian status, key infrastructure condition |
| Reconnaissance in Force | Determine enemy strength, disposition, and reaction through deliberate contact | Enemy contact data (size, activity, location, unit, time, equipment), enemy defensive positions, engagement area boundaries, weapons systems identified |

**NAI Data Structure in MSS.** Named Areas of Interest generated or refined during reconnaissance are structured data objects in the intelligence layer. Each NAI in MSS carries:

- NAI designator and geographic location (point or polygon)
- Associated PIR or IR it supports
- Indicator list (what activity at this NAI confirms or denies)
- Collection asset assigned
- Observation window (start/end DTG)
- Current status: No activity / Activity observed / PIR answered
- Reporting history (linked SPOTREPs)

**Obstacle Reports as Reconnaissance Data Products.** Route and zone reconnaissance generate obstacle report data that feeds directly into the engineer obstacle layer (Chapter 3). Each obstacle identified during reconnaissance produces a structured OBSREP object: location, type, dimensions, emplacing agency (friendly/enemy/unknown), bypass assessment, and recommended reduction method. The reconnaissance element collects this data; the engineer section validates and maintains it in MSS.

**Route Classification Data from Reconnaissance.** Route reconnaissance produces the most structured data of any reconnaissance type. FM 3-34.400 defines the route classification data fields. In MSS, each route segment assessed during reconnaissance is updated with: surface type, route width, maximum vehicle classification, bridge MLC at each crossing, gradient data, chokepoint locations, and overhead clearance restrictions. This data directly feeds the route analysis products used in COA development (section 2-3) and time-distance calculations (section 5-2a).

> **NOTE: Reconnaissance is the M&M commander's primary means of collecting data about the operational environment before committing the main body. A reconnaissance plan that does not specify what data products each element will collect — and how those products will enter MSS — wastes the reconnaissance effort. The S3 must coordinate with the S2 and cavalry troop to define MSS data product requirements before issuing the reconnaissance order.**

### 4-5. OP/LP Management in MSS

Observation posts (OPs) and listening posts (LPs) are the physical sensors of the reconnaissance and security effort. MSS tracks OP/LP data to give the S3 a picture of the sensor grid.

**OP/LP Data Elements in MSS:**

| Data Field | Description |
|---|---|
| Position | Grid coordinate (8-digit minimum) |
| Unit | Assigned observation element |
| Observation sector | Direction of observation, sector limits |
| Communications status | Primary/alternate comms status, last check-in DTG |
| Status | Occupied / Unoccupied / Compromised |
| Reporting triggers | Named event (enemy contact, vehicle movement) |

> **CAUTION: OP/LP positions are operationally sensitive. Confirm that the MSS workspace containing OP/LP data is access-controlled and not visible to personnel outside the originating unit and higher headquarters. Coordinate with the IMO and S2 for appropriate access controls.**

### 4-6. Counter-Reconnaissance Data Management

Counter-reconnaissance is the effort to deny the enemy information about friendly forces (FM 3-98, para 1-12). MSS supports counter-reconnaissance by tracking patrol routes, timing, and friendly signature management data.

**Counter-Recon Data in MSS:**

- Patrol routes and times (coordination with S2 and protection cell)
- Radar silence periods and emissions control (EMCON) schedules
- Known or suspected enemy reconnaissance assets (from S2 overlay)
- Friendly signature minimization measures (vehicle positions, covered/concealed areas)

---

## CHAPTER 5 — GROUND COMBAT OPERATIONS

**BLUF:** Ground combat operations in MSS require the S3 section to maintain current operational graphics, track phase line reporting, manage combined arms task organization data, and provide the commander a real-time ground picture. This chapter covers offensive and defensive operations for infantry, armor, and combined arms team employment.

### 5-1. 11A/11B/19A Maneuver Unit Operations in MSS

Infantry officers (11A), infantrymen (11B), and armor officers/crews (19A/19K) operate at the tactical edge — platoon through battalion. MSS use at company level and below is limited but critical.

**Company/Troop Level MSS Use:**
- Company commanders view the battalion combined arms workspace (read-only in most configurations)
- View current operational graphics — phase lines, objectives, boundaries
- Confirm task organization and adjacent unit boundaries
- View BFT display showing friendly company/platoon positions
- Report phase line crossings and checkpoint reports via MSS reporting function (where configured)

**Battalion S3 MSS Use:**
- Maintain all operational graphics for the battalion AO
- Track company/team phase line crossing reports
- Update task organization as companies attach/detach
- Synchronize with fires, engineer, and aviation enablers via cross-functional workspace

### 5-2. Objective Graphic Control Measures in MSS

Objectives are the geographic areas a unit must seize, secure, or neutralize (FM 3-90, para 1-22). In MSS, objectives are graphic objects with associated metadata.

**Objective Data Requirements in MSS:**

| Field | Description | Required |
|---|---|---|
| Objective designation | Alpha designator (OBJ COBRA, OBJ 4) | Yes |
| Location | Grid or polygon boundary | Yes |
| Assigned unit | Who is tasked to seize/secure | Yes |
| Phase | Which phase this objective belongs to | Yes |
| Current status | Not Started / In Progress / Seized / Secured / Complete | Yes |
| Seizure DTG | Actual time objective was secured | On completion |

**Control Measures Displayed with Objectives:**
- Line of departure (LD) / line of contact (LC)
- Assault position / attack position
- Phase lines controlling movement to objective
- Limit of advance (LOA)
- Consolidation and reorganization area

### 5-2a. Scheme of Maneuver as Structured Geospatial Data

The scheme of maneuver is the commander's visualization of how forces will move and fight to accomplish the mission. In MSS, the scheme of maneuver is not a narrative paragraph — it is a set of structured geospatial data objects that must be created, attributed, and maintained in the platform throughout the operation.

**Graphic Control Measures as Structured Data.** Every control measure in the scheme of maneuver — phase lines, objectives, boundaries, checkpoints, contact points, passage points, axes of advance, directions of attack, assembly areas, and limit of advance — is a discrete geospatial object in MSS. Each object carries metadata: designator, type, owning unit, effective DTG, associated OPORD/FRAGO number, and current status. These are not map annotations. They are structured data that other systems and dashboards can query, filter, and display contextually.

**Table 5-2a. Scheme of Maneuver Graphic Control Measures in MSS**

| Control Measure | MSS Object Type | Required Attributes | Update Trigger |
|---|---|---|---|
| Phase Line (PL) | Linear | Designator, DTG effective, associated unit, crossing status | OPORD/FRAGO; unit crossing report |
| Objective (OBJ) | Polygon/Point | Designator, assigned unit, phase, status (not started/in progress/seized/secured) | OPORD/FRAGO; unit report |
| Boundary | Linear | Designator, left/right unit, effective DTG | OPORD/FRAGO |
| Checkpoint (CP) | Point | Designator, associated route, reporting requirement | OPORD/FRAGO; unit report |
| Axis of Advance | Linear | Designator, assigned unit, direction, width | OPORD/FRAGO |
| Assembly Area (AA) | Polygon | Designator, assigned unit, occupy/depart DTG | OPORD/FRAGO |
| Limit of Advance (LOA) | Linear | Designator, effective DTG, associated phase | OPORD/FRAGO |

**Route Status, Movement Rates, and Time-Distance Analysis.** Route status data (section 3-1), movement rate data, and time-distance calculations are M&M-specific data products that underpin the scheme of maneuver. MSS maintains these as structured datasets, not static overlays.

- **Route status** is maintained per MSR/ASR segment with classification, current condition, and last-verified DTG.
- **Movement rates** are stored by unit type and route classification. A mechanized infantry battalion moves at a different rate on an improved road than on an unimproved trail. MSS uses these rates when loaded to support time-distance calculations for COA analysis.
- **Time-distance analysis** is computed from route length, route classification, unit type movement rate, and known delays (obstacles, chokepoints, passage points). The output is an estimated time of arrival for each unit at each phase line or objective — a planning product the S3 uses to synchronize the scheme of maneuver with fires, aviation, and engineer support.

> **NOTE: Graphic control measures in MSS are live data objects, not static drawings. When a FRAGO changes a phase line or adds a boundary, the S3 must update the MSS object — not draw a new annotation on top of the old one. Stale control measures left in the workspace alongside current ones create ambiguity that degrades combined arms coordination.**

### 5-3. Combined Arms Team Task Organization and Tracking

Combined arms teams — infantry platoons with tank attachments, or armor platoons with infantry attachments — require accurate task organization data in MSS to prevent command relationship confusion and fires coordination errors.

**Combined Arms Team Tracking Requirements:**
- Parent battalion and current OPCON/TACON relationship
- Organic and attached elements (by type and number)
- Current position in the combined arms workspace
- Commander/officer-in-charge identification
- Support relationship to fires, engineers, aviation

> **NOTE: When a platoon is task-organized to a different company or team, update the task organization display in MSS immediately when the attachment becomes effective. A platoon displayed under the wrong parent creates a control measure conflict risk and can cause fires deconfliction errors.**

### 5-4. Phase Line Management and Reporting Triggers

Phase lines (PLs) control the timing of maneuver, synchronize combined arms actions, and provide reporting triggers for the commander (FM 3-90, para 2-10). MSS uses phase lines as both graphic control measures and automated reporting triggers.

**Phase Line Functions in MSS:**
- Visual reference on the operational graphics layer
- Trigger point for CCIR evaluation (does crossing PL DRAGON trigger a decision point?)
- Reporting reference (units report when they cross)
- Synchronization event (when does fires shift? When does aviation lift?)

**Phase Line Reporting in MSS:**
- Unit reports PL crossing via voice/digital
- S3 updates PL crossing status in MSS within 15 minutes of report
- PL status (Friendly crossed / Enemy reported at) triggers downstream actions
- Multiple simultaneous PL crossings by different units are tracked and timestamped

### 5-5. Checkpoint and Passage of Lines Coordination Data

Passages of lines (POL) are among the most complex combined arms coordination tasks in maneuver operations (FM 3-90, para 4-5). MSS supports POL coordination by maintaining:

**Forward / Rearward Passage Data:**
- Passage point location and designation
- Passing unit (identity, size, route)
- Stationary unit (identity, contact forward boundary)
- Passage window (not earlier than / not later than DTG)
- Guide location and contact information
- Current status: Planned / Coordinated / In Progress / Complete

> **WARNING: Incomplete passage of lines data in MSS during execution can result in fires coordination failures, fratricide risk, and command relationship confusion. Confirm all POL data is loaded and visible to both the passing and stationary unit S3 sections before passage begins.**

### 5-6. Consolidation and Reorganization Tracking

After seizing an objective, consolidation and reorganization (C2) is the phase where the unit establishes the defense, accounts for personnel and equipment, and reconstitutes combat power (FM 3-90, para 4-13). MSS supports C2 tracking by:

- Updating objective status from "Seized" to "Consolidating" to "Consolidated/Reorganized"
- Displaying unit positions on the objective during consolidation
- Tracking personnel accountability and equipment status input during reorganization
- Providing the data layer for the consolidated position defense graphics

---

## CHAPTER 6 — AVIATION INTEGRATION

**BLUF:** Aviation integration in MSS requires airspace deconfliction data, air corridor management, and synchronization of air maneuver with ground maneuver graphics. The aviation officer (15A) and A2C2 section maintain aviation data in MSS. The UAS operator (15W) requires special integration for airspace deconfliction.

### 6-1. 15A Aviation Officer MSS Workflow

The aviation officer (15A) serves as the S3 air or brigade aviation officer (BAO) in BCT or division operations (FM 3-96, para 4-18). The 15A uses MSS to:

- Maintain air corridor graphics in the aviation layer
- Track aviation mission status (air assault, CASEVAC, resupply, reconnaissance)
- Deconflict aviation routes with ground maneuver graphics and FSCMs
- Coordinate airspace with the ADAM/BAE cell (ADA/aviation)
- Manage LZ/PZ locations and status

### 6-2. Air Corridor Management and Deconfliction Data

Air corridors are the airspace lanes that aviation uses to access and egress the objective area (ATP 3-04.94). In MSS, air corridors are displayed as linear or polygon graphics in the aviation layer, deconflicted against ground maneuver graphics and FSCMs.

**Air Corridor Data in MSS:**

| Field | Description |
|---|---|
| Corridor designation | Name/number (e.g., AIR CORRIDOR BLUE) |
| Entry/Exit points | Grid coordinates |
| Altitude block | Minimum and maximum altitude (AGL/MSL) |
| Airspeed restriction | Maximum airspeed for corridor |
| Time window | Activation/deactivation DTG |
| Status | Active / Inactive / Closed |

**Deconfliction Checks Before Activating an Air Corridor:**
1. Confirm corridor does not penetrate any active no-fly zones or restricted airspace.
2. Confirm corridor altitude block does not conflict with indirect fire trajectories in the same time window.
3. Confirm corridor is deconflicted with any active UAS airspace reservations.
4. Confirm corridor route does not cross active maneuver boundaries at altitudes that create ground-to-air risk.
5. Coordinate with FECC/FSO for artillery restrictions during corridor activation window.

### 6-3. UAS Operations: 15W Integration and Airspace Deconfliction

UAS operators (15W) require airspace reservations — altitude blocks over an area for a specified time — that must be deconflicted against crewed aviation corridors and indirect fire trajectories.

**UAS Airspace Data in MSS:**

- Operating area (polygon with altitude block and time window)
- UAS type and associated signature (relevant for OPFOR context)
- Home station/launch-recovery site
- Mission (reconnaissance, ISR, targeting, assessment)
- Handoff coordination (if UAS products are fed to MSS directly)

> **CAUTION: UAS altitude reservations and crewed aviation corridors must be deconflicted in time, space, and altitude block. Overlapping reservations create mid-air collision risk. The A2C2 section owns airspace deconfliction — MSS provides the visualization layer, not the deconfliction authority.**

### 6-4. Air Assault and Air Movement Data Management

Air assault operations require the most complex aviation-ground maneuver integration. MSS supports air assault planning and execution by maintaining:

**Air Assault Data Requirements:**

| Data Element | MSS Layer | Owner |
|---|---|---|
| LZ / PZ locations and status | Aviation layer | 15A / S3 |
| Air assault routes (ingress/egress) | Aviation layer | 15A |
| Objective graphics | Operations layer | S3 |
| Assault force task organization | Operations layer | S3 |
| Fire support plan (FSCM) | Fires layer | FSO |
| PZ time windows | Aviation layer | 15A |
| LZ control team positions | Blue Force layer | S3 |
| EW / air defense threat overlay | Intel layer | S2 |

> **NOTE: Air assault LZ/PZ graphics and time windows are among the most operationally sensitive graphics in MSS. Coordinate with the S2 and OPSEC officer before publishing LZ/PZ data to any shared workspace that extends beyond the originating unit.**

### 6-5. CASEVAC/MEDEVAC Landing Zone Tracking

CASEVAC and MEDEVAC LZ management requires real-time updates as operational conditions change. MSS tracks designated LZ locations, status, and mission history.

**LZ Status Fields:**
- Location (grid)
- Status: Designated / Cleared / Active / Closed / Contaminated
- Surface type and dimensions (if engineer-assessed)
- Marking system (smoke color/panel)
- Security status (secured/unsecured)
- Last use DTG

### 6-6. Aviation-Maneuver Coordination in MSS

Effective aviation-maneuver coordination requires that both the ground S3 and the aviation element can see the same operational picture (ATP 3-04.94). MSS enables this by giving aviation and ground S3 sections access to the same workspace with appropriate layer permissions.

**Aviation-Maneuver Coordination Checklist (pre-mission):**
- [ ] Air corridor graphics loaded and visible to both ground and aviation S3
- [ ] FSCM layer confirms no active fires restrictions in corridor during activation window
- [ ] LZ/PZ graphics visible in aviation layer with current status
- [ ] UAS deconfliction confirmed with A2C2 section
- [ ] BFT layer shows ground maneuver unit positions along flight route
- [ ] Abort criteria and alternate LZ loaded in aviation workspace

---

## CHAPTER 7 — URBAN OPERATIONS AND SPECIAL ENVIRONMENTS

**BLUF:** Urban terrain, mountain/cold weather environments, and river crossings present unique data management challenges for MSS users. Data from special environments requires additional context, precision, and verification standards compared to open terrain operations.

### 7-1. Urban Terrain Data Management in MSS (MOUT)

Military Operations on Urban Terrain (MOUT) require building- and block-level data precision that exceeds standard open terrain requirements. MSS supports MOUT operations by integrating urban terrain data from multiple sources.

**Urban Data Sources in MSS:**
- Commercial mapping layers (building outlines, road networks)
- Engineer urban reconnaissance reports
- Intelligence urban terrain analysis products
- Unit reporting during MOUT operations (clearance status, damage assessment)

**Urban Layer Configuration:**
- Building/facility layer (individual structures as graphic objects)
- Street/route layer (vehicle/dismounted route separation)
- Key terrain and facilities layer (bridges, utilities, government buildings, hospitals)
- Clearance status overlay (cleared/uncleared/enemy occupied)

### 7-2. Building and Facility Tracking and Clearance Status

During MOUT operations, tracking clearance status by building is a safety and tactical imperative. MSS supports building-by-building tracking when the unit has loaded the appropriate urban data layer.

**Building Status Fields in MSS:**

| Status | Symbol Color (MSS) | Definition |
|---|---|---|
| Unknown | Gray | Not yet reconnoitered |
| Cleared — Friendly | Blue | Cleared and occupied by friendly forces |
| Cleared — Unoccupied | White | Cleared, no one inside |
| Enemy Occupied | Red | Confirmed enemy in building |
| Contested | Yellow | Combat ongoing or recent |
| Hazardous | Orange | Structural damage, CBRN risk, or booby trap suspected |

---

**TASK: Building Clearance Tracking in MSS During MOUT**

**CONDITIONS:** An infantry company is conducting urban clearance operations. Platoons are reporting clearance status of buildings as they clear them. The S3 section has received three clearance reports in the past hour.

**STANDARDS:** The S3 updates building status in MSS within 20 minutes of receipt of each clearance report. Building status reflects the current conditions as reported. The company commander and battalion S3 can see current clearance status on the shared MOUT workspace.

**PROCEDURE:**

1. Receive clearance report from platoon. Confirm: building identifier, status, time of clearance, clearing unit.
2. Navigate to the MOUT workspace and select the building graphic by identifier.
3. Update the building status field to reflect reported status.
4. Enter clearing unit and clearance DTG in the metadata.
5. If an enemy-occupied building was identified, coordinate with S2 to update the enemy situation overlay.
6. Publish update to the combined arms MOUT workspace.

---

### 7-3. Mountain and Cold Weather Environment Data Considerations

Mountain and cold weather operations present unique data management challenges that MSS users must account for.

**Mountain Environment Data:**
- Route classification changes significantly in mountain terrain (gradient, switchbacks, avalanche risk). MSS route data must include terrain classification updates from engineer reconnaissance.
- LZ/PZ assessments for mountain helicopter operations must account for altitude density, surface conditions, and obstacles. MSS LZ data fields must be populated with mountain-specific conditions.
- Ground force positions on steep terrain may appear distorted on flat-projection MSS maps. Confirm grid positions with leader ground confirmation, not solely MSS display.

**Cold Weather Environment Data:**
- Ice road and frozen waterway classification (load bearing capacity, thickness measurements) must be maintained in the route layer for cold weather operations.
- Temperature data affects route load classification for ice crossings — update route status when temperatures change significantly.
- Equipment status data during extreme cold must account for cold-weather degradation rates (batteries, hydraulics, comms equipment).

### 7-4. River Crossing Operations Data Management

River crossing operations require engineer and maneuver data integration across the crossing site, near-side assembly area, far-side exploitation area, and the entire crossing complex (FM 3-90, para 5-1).

**River Crossing Data Elements in MSS:**

| Element | Data Required | Owner |
|---|---|---|
| Crossing site | Location, type (wet gap/dry gap), MLC, current water level | 12A/12B |
| Assault crossing site | Grid, current status, crossing means type | S3 / 12A |
| Near-side assembly area | Boundary, unit positions, staging graphics | S3 |
| Far-side bridgehead | Boundary, objective, security task org | S3 |
| Bridge/raft sites | MLC, capacity, current status, engineer team tracking | 12A |
| Air defense coverage | ADA coverage footprint over crossing site | S6 / ADA section |

> **WARNING: River crossing operations are among the most vulnerable to enemy air and indirect fire. The crossing site and bridging equipment are high-value targets. Confirm MSS graphics for crossing operations are access-controlled to the minimum required audience before publication.**

### 7-5. Special Terrain Analysis in MSS

Terrain analysis in MSS is performed using OAKOC: Observation and fields of fire, Avenues of approach, Key terrain, Obstacles, and Cover and concealment (ADP 3-90, para 2-5). Each OAKOC factor has MSS implications.

**OAKOC in MSS:**
- **Observation / fields of fire:** OP/LP coverage overlays, dead ground areas, engagement ranges
- **Avenues of approach:** Route analysis data, axis width/classification, chokepoints
- **Key terrain:** Designated key terrain features as named graphic objects, control measure priority
- **Obstacles:** Obstacle layer with all reported obstacles, FASCAM, wire, anti-tank ditches
- **Cover and concealment:** Vegetation density data, urban block analysis, dead ground to air

---

## CHAPTER 8 — FORCE TRACKING AND BLUE FORCE SITUATIONAL AWARENESS

**BLUF:** Blue Force Tracking (BFT) in MSS provides the S3 section a real-time-updated picture of friendly force positions. BFT data in MSS reflects last reported positions through integrated tracking systems. The S3 section is responsible for validating BFT accuracy against voice and digital reporting.

### 8-1. Blue Force Tracking Data Integration with MSS

MSS integrates BFT data from JBC-P and other approved tracking systems. This integration provides the S3 section a unified force picture without requiring manual position updates for each vehicle or unit.

**BFT Integration Data Elements:**
- Unit identifier
- Last reported position (grid)
- Last update DTG
- Platform type (vehicle, aircraft, dismount)
- Communications status

> **CAUTION: BFT update intervals range from 30 seconds to several minutes depending on system, position-reporting interval settings, and communications availability. A position displayed as current on MSS BFT may reflect a position update from several minutes ago. Always note the "last updated" timestamp before using BFT for precision targeting, fires deconfliction, or passage of lines coordination.**

### 8-2. Unit Location Reporting Standards in MSS

Not all units have BFT-integrated tracking. Units without automated tracking report positions manually to the S3 section, which updates MSS.

**Manual Position Reporting Standard:**
- Report frequency: IAW unit SOP (minimum every 2 hours, or at each phase line crossing)
- Report format: Unit designation, grid (8-digit minimum), DTG, status (SALUTE/LACE as applicable)
- S3 update standard: Manual reports entered into MSS within 15 minutes of receipt

**Table 8-1. Position Reporting Standards by Echelon**

| Echelon | Update Frequency | Method | S3 Update Deadline |
|---|---|---|---|
| Company/Troop | 2 hours / PL crossing | JBC-P or voice | 15 min from report |
| Battalion | 4 hours / phase event | JBC-P or voice | 30 min from report |
| Brigade | 6 hours / major event | JBC-P or voice | 30 min from report |
| Division / Corps | 8 hours / major phase | Digital / MSS push | On receipt |

### 8-3. Equipment Tracking and Status

Beyond unit positions, MSS tracks equipment status to give the S3 a combat power picture. This data comes from the maintenance section and GCSS-Army integration where configured.

**Equipment Status Data in MSS:**
- Authorized vs. assigned equipment (by type)
- Deadline status (number and type of equipment deadlined)
- Estimated return to operational status (EOS) for deadlined systems
- Equipment location (if tracked separately from unit BFT)

### 8-4. Personnel Readiness and Combat Power Reporting

Personnel strength data from IPPS-A integration gives the S3 a personnel readiness picture alongside equipment status. Combined, these are the inputs to the commander's combat power assessment.

**Combat Power Data Elements:**
- Personnel: Assigned / present for duty / available for operations (accounting for training, profile, etc.)
- Equipment: Operational rate for primary weapon systems (tanks, Bradley, HMMWV, etc.)
- Combat power rating (C-1 through C-4) calculated or manually assessed

**Table 8-2. Combat Power Ratings (FM 6-99 Reference)**

| Rating | Definition | MSS Display Standard |
|---|---|---|
| C-1 | 90% or above — fully combat ready | Green |
| C-2 | 80–89% — substantially ready | Green-Yellow |
| C-3 | 70–79% — marginally ready | Yellow |
| C-4 | Below 70% — not ready | Red |

### 8-4a. Force Ratio Calculations and Relative Combat Power Assessment

> **NOTE: Relative combat power assessment requires quantitative force ratio data — friendly versus threat — across sectors, axes, and objectives. This is a core analytical product for M&M planners (FM 5-0, Table 5-4). The force ratio does not determine the outcome of an engagement, but it provides the quantitative baseline the commander uses when allocating forces to the main effort, supporting efforts, and reserve. Ratios without context are misleading; ratios informed by terrain, training, morale, and situational factors are the basis of sound maneuver planning.**

Force ratio calculations in MSS compare friendly combat power against assessed threat combat power at each decision point, axis, or objective. The S3 section builds force ratio data from two MSS sources: the friendly combat power dashboard (section 8-4) and the S2 threat order of battle data in the intelligence layer.

**Force Ratio Data Elements in MSS:**

| Data Element | Source | MSS Layer | Update Trigger |
|---|---|---|---|
| Friendly maneuver strength (by unit type/sector) | S3 combat power dashboard | Operations layer | Personnel/equipment status change |
| Threat assessed strength (by unit type/sector) | S2 order of battle | Intel layer | Intelligence update or reassessment |
| Sector or axis assignment | S3 OPORD / task organization | Operations layer | OPORD or FRAGO |
| Computed force ratio (friendly:threat) | Staff calculation from MSS data | Planning workspace | Before each COA analysis or decision point |

**Standard Force Ratios (FM 5-0 Planning Reference):**

| Operation Type | Minimum Planning Ratio (Friendly:Threat) |
|---|---|
| Deliberate attack | 3:1 at the point of penetration |
| Hasty attack | 3:1 desired; 2.5:1 minimum acceptable |
| Defense (prepared) | 1:3 (defender advantage) |
| Delay | 1:6 (with prepared positions and obstacles) |
| Counterattack | 3:1 at the point of counterattack |

> **CAUTION: Force ratios are planning factors, not prescriptive requirements. A 3:1 ratio does not guarantee success, and a 1:1 ratio does not guarantee failure. The force ratio must be analyzed alongside terrain, training level, morale, surprise, and combined arms integration. Display force ratios in MSS alongside these qualitative factors so the commander can make an informed assessment — not a formulaic one.**

### 8-5. Lost Communications Procedures for Location Reporting

When a unit loses communications and cannot report its position, the S3 section must account for the gap in MSS.

**Lost Comms Procedure:**
1. Identify the unit with lost comms and its last reported position/DTG in MSS.
2. Mark the unit's position in MSS as "Last Known — Comms Lost" with the DTG.
3. Do not delete the unit position; do not update it with estimated positions.
4. Activate alternate comms channels IAW the unit PACE plan.
5. Notify adjacent units and higher S3 that the unit is not reporting.
6. When comms are restored, confirm current unit position and update MSS immediately.

> **WARNING: Never update a unit's MSS position based on estimated movement or dead reckoning without voice confirmation. False position data in MSS is more dangerous than acknowledged data gaps — it can create fratricide conditions by misrepresenting friendly force locations.**

---

## CHAPTER 9 — ECHELON-SPECIFIC M&M OPERATIONS

**BLUF:** MSS use for M&M operations scales by echelon. Company-level use is primarily consumption of read-only graphics. Battalion S3 sections are the primary maintainers. BCT S3/G3 sections synchronize combined arms at the operational level. Division and Corps use MSS for operational art and phase management.

### 9-1. Company/Troop Level

**Primary Users:** Company commanders, platoon leaders, first sergeants, platoon sergeants.

**MSS Role:** Consumers of the battalion combined arms workspace. Limited write access in most configurations.

**Company-Level Use:**
- View current operational graphics (phase lines, objectives, boundaries)
- Confirm task organization and adjacent unit boundaries
- View BFT to confirm own position and adjacent unit positions
- Submit phase line crossing reports via MSS (where configured)
- Access the route status dashboard to confirm MSR/ASR status before movement

**Company Commander Minimum Literacy Requirements:**
- Can navigate to the battalion combined arms workspace
- Can read and interpret all operational graphic types displayed
- Understands BFT update intervals and limitations
- Can submit a position report or phase line crossing report
- Can identify data staleness (data-as-of timestamp)

### 9-2. Battalion Level

**Primary Users:** S3, XO, battle captain, S3 NCOIC, assistant S3.

**MSS Role:** Primary maintainer of all battalion-level M&M data. Integrates enabler data from engineers, fires, and aviation into the combined arms workspace. Reports to brigade S3.

**Battalion S3 Daily Battle Rhythm (MSS Tasks):**
1. 0600 — Review all operational graphic currency. Confirm graphics match current OPORD.
2. 0700 — Update task organization display with any overnight changes.
3. 0800 — BUA preparation — build maneuver status products from MSS data.
4. Continuous — Process position reports and update MSS within standard.
5. On receipt — FRAGO processing: update graphics and notify subordinate S3s.

**Key Battalion S3 MSS Products:**
- Combined arms workspace (all M&M data integrated)
- Phase line crossing status tracker
- Route status dashboard
- Combat power dashboard (personnel + equipment combined)
- Obstacle overlay (maintained by 12A section, displayed in combined arms workspace)

### 9-3. Brigade Combat Team (BCT)

**Primary Users:** G3/S3, deputy S3, battle captain, BCT XO, functional area officers (FA 50 series).

**MSS Role:** Integrates all battalion-level combined arms data into the BCT operational picture. Synchronizes deep, close, and rear operations (FM 3-96, para 2-1). Manages the BCT operations process data cycle.

**BCT-Level M&M MSS Functions:**
- Maintain BCT-level operational graphics (BCT boundaries, phase lines, objectives)
- Integrate all battalion combined arms workspaces into the BCT picture
- Synchronize fires (BCT FECC), engineer (BEB), and aviation (BAO) data
- Manage the deep / close / rear synchronization picture
- Support the BCT commander's decision support matrix (DSM) with MSS data products
- Maintain the battle rhythm data products for BCT battle update assessment

**Deep / Close / Rear in MSS:**
- Deep: NAI/TAI overlays, interdiction targets, reconnaissance objectives beyond FLOT
- Close: Current maneuver graphics, phase lines, objective status, BFT
- Rear: CSS graphics, route status, MSR/ASR management, sustainment base locations

### 9-4. Division and Corps

**Primary Users:** G3 staff, division and corps planners (FA 50/51/53), operations officers.

**MSS Role:** Operational art and phase management. Division and Corps use MSS to track phased operations across multiple subordinate BCTs or divisions. The focus at this echelon is the integrated operational picture, not tactical-level graphic maintenance.

**Division/Corps M&M MSS Functions:**
- Display subordinate BCT/division combined arms workspaces in the higher-level view
- Track operational phase status (Phase I / II / III) across the AOR
- Monitor main effort / supporting effort combat power in the combined arms picture
- Maintain the theater reserve and commitment decision data
- Support operational assessment products (MOE/MOP) for phased operations

---

## CHAPTER 10 — DEGRADED OPERATIONS

**BLUF:** MSS is a networked platform — network degradation or outage directly impacts M&M data availability. Units must maintain backup procedures for all M&M functions and train to a defined PACE plan for each critical data product.

### 10-1. Maneuver Operations When MSS is Degraded

MSS degradation does not stop operations. The formation must be trained and equipped to maintain maneuver situational awareness through backup means.

**What is Lost When MSS is Degraded:**
- Integrated real-time BFT display
- Shared operational graphics visibility
- Route status dashboard
- Combined arms synchronization workspace
- Automated phase line crossing alerts

**What is NOT Lost:**
- JBC-P (separate system, not dependent on MSS)
- Voice reporting (primary maneuver reporting channel)
- Physical maps and acetate overlays (always maintained)
- Unit SOPs and battle drills
- Commander's intent and mission orders

> **NOTE: MSS is a Mission Command enabler, not a requirement for operations. USAREUR-AF BCTs fought for decades without MSS. A unit that cannot operate without MSS is not tactically proficient — it is platform-dependent. Train degraded operations with the same rigor as full MSS employment.**

### 10-2. Manual Battle Tracking Backup

Every S3 section must maintain a manual battle tracking capability that does not depend on MSS.

**Manual Battle Tracking Kit (Minimum Requirements):**
- 1:50,000 or 1:25,000 paper maps with acetate overlays of current operational graphics
- Current task organization on acetate or whiteboard
- BFT position data printed or manually plotted within last update cycle
- Phase line crossing log (paper format)
- Route status log (paper format with MSR/ASR and current status)

**Transition from MSS to Manual Battle Tracking:**
1. S3 confirms MSS is degraded (not just a display issue — confirm at S6).
2. Print or photograph the last current MSS combined arms workspace.
3. Transfer current positions and graphics to paper map/acetate.
4. Activate voice-primary reporting to all subordinate S3 sections.
5. Notify higher S3 that unit is on degraded operations.

### 10-3. PACE Plan for M&M Data

Every S3 section must have a PACE plan for each critical M&M data type.

**Table 10-1. M&M Data PACE Plan Template**

| Data Type | Primary | Alternate | Contingency | Emergency |
|---|---|---|---|---|
| Force tracking | MSS BFT integration | JBC-P standalone | Voice periodic reports | Manual map plot from last known position |
| Operational graphics | MSS workspace | Printed MSS product | Acetate overlay | Published OPORD graphics (paper) |
| Route status | MSS route dashboard | Route status radio report | Unit SOP route status log | Last known status (note DTG) |
| Obstacle data | MSS obstacle layer | Engineer section overlay | Hard copy OBSREP | Last known engineer report |
| Phase line reports | MSS automated trigger | JBC-P message | Voice report | Scheduled radio check |

### 10-4. Minimum Essential Products Without MSS

When MSS is unavailable, the S3 section must be able to produce the following minimum products by manual means:

- Current ground situation map (paper/acetate)
- Current task organization
- Combat power status (personnel and equipment, by unit)
- Route status (open/closed/restricted, by MSR/ASR)
- Priority intelligence requirements (current PIRs from S2 brief)
- Current phase line status

These products must be producible within 30 minutes of MSS degradation. If the S3 section requires more than 30 minutes, backup procedures require additional training.

### 10-5. Reconstitution After Outage

When MSS is restored after an outage, the S3 section must reconstitute the MSS data picture before reverting to MSS as the primary tool.

**Reconstitution Procedure:**
1. Confirm MSS platform is restored and all layers are accessible.
2. Compare the manual battle tracking map to the MSS workspace. Identify all discrepancies.
3. Update MSS to reflect the current situation: positions, route status, phase line crossings that occurred during the outage.
4. Enter the outage window (start/end DTG) in the workspace metadata.
5. Notify all subordinate S3 sections that MSS is restored and the workspace has been updated to current status.
6. Brief the commander that MSS data from the outage period has been reconstructed from manual records.

> **NOTE: Do not simply revert to MSS after an outage without reconstituting the data. An MSS workspace that displays the pre-outage picture as if it is current is more dangerous than an acknowledged manual tracking situation — it creates false situational awareness.**

---

## CHAPTER 11 — REPORTING AND PRODUCTS FOR MANEUVER OPERATIONS

**BLUF:** The M&M practitioner in MSS is both a data consumer and a data producer. Reports generated from MSS — or entered into MSS — feed the combined arms picture at every echelon. This chapter covers the reporting standards and product types that M&M practitioners generate and receive in MSS.

### 11-1. Report Types for M&M Practitioners

M&M practitioners generate and consume several report types in MSS. Understanding which reports are entered into MSS, which are consumed from MSS products, and which originate outside MSS is essential to maintaining accurate data.

**Table 11-1. M&M Report Types and MSS Relationship**

| Report Type | Abbreviation | Direction | MSS Role |
|---|---|---|---|
| Situation Report | SITREP | Up to higher | Generated from MSS data; posted to workspace |
| Spot Report | SPOTREP | Up and lateral | Entered into MSS intelligence layer (coord with S2) |
| Contact Report | CONTREP | Up immediately | Entered into MSS after voice — updates BFT and enemy overlay |
| Route Reconnaissance Report | RTE RECON | To S3 / engineer | Entered into route and obstacle layers |
| Obstacle Report | OBSREP | To engineer / S3 | Entered into obstacle layer by engineer section |
| NBC Report | NBCR | Up to higher | Entered into protection layer (see TM-40E) |
| Engineer Report | ENGREP | To S3 / S4 | Route status, bridge classification, obstacle status update |
| Air Mission Report | AMR | To aviation / S3 | LZ/PZ status, corridor status, air mission completion |
| Personnel Status Report | PERSTAT | Up to higher | Sourced from IPPS-A integration; displayed in MSS |
| Equipment Status Report | EQUIP STAT | Up to higher | Sourced from GCSS-Army integration; displayed in MSS |

### 11-2. SITREP Generation in MSS

The SITREP is the primary periodic report the S3 section provides to higher headquarters. In MSS, the SITREP is built from the combined arms workspace — not manually assembled from separate source systems.

**MSS Data Sources for the SITREP:**

- **Friendly situation (BLUFOR):** BFT layer — current unit positions and last reported status
- **Enemy situation:** S2 intelligence layer — current enemy overlay, NAI/TAI status
- **Combat power:** Readiness dashboard — personnel and equipment status by unit
- **Route status:** Route layer — current MSR/ASR status
- **Obstacle status:** Obstacle layer — significant obstacle changes since last SITREP
- **Aviation:** Aviation layer — current corridor status, LZ/PZ status
- **Phase line / objective status:** Operations layer — phase line crossings, objective status

**SITREP Currency Standard:** SITREP data pulled from MSS must be current within four hours of submission. If the workspace has not been updated within four hours, the S3 must manually verify critical data elements before submitting the SITREP.

> **NOTE: Submitting a SITREP from MSS does not validate the data — it only extracts it. The S3 section is responsible for confirming that the MSS data used for the SITREP is accurate and current. A SITREP built from stale data is worse than no SITREP, because it establishes a false baseline for higher headquarters.**

### 11-3. SPOTREP Submission and MSS Integration

The SPOTREP is a rapid report of significant observations — enemy forces, unusual activity, civilian movement, or other significant events. SPOTREPs originate at the observation point (OP, patrol, aircraft) and travel up the reporting chain.

In MSS, the SPOTREP enters the system when the S3 section or S2 section enters the reported information into the intelligence layer. The reporting chain is:

1. Observer reports by voice or JBC-P message.
2. S2 section receives the SPOTREP.
3. S2 enters the contact/observation into the enemy situation layer.
4. S3 section confirms the SPOTREP has been reflected in the combined arms workspace.
5. S3 evaluates whether the SPOTREP triggers a CCIR or decision point.

> **CAUTION: SPOTREPs represent single-source, unconfirmed observations. Enter them into MSS as "reported" or "unconfirmed" — do not enter them as confirmed intelligence. The intelligence layer must distinguish between confirmed and reported enemy data. Entering an unconfirmed SPOTREP as confirmed intelligence distorts the enemy picture and may produce incorrect maneuver or fires decisions.**

### 11-4. Contact Report (CONTREP) Procedures

A contact report is a rapid, immediate report of any contact with enemy forces. It is a time-critical report — voice is primary, MSS is secondary.

**CONTREP MSS Procedure:**

1. Contact is reported by voice on primary net immediately (SALUTE format — Size, Activity, Location, Unit, Time, Equipment).
2. Battle captain acknowledges and relays to higher by voice.
3. S3 section enters the contact into the MSS enemy situation layer within 15 minutes of voice report.
4. Contact entry includes: grid, unit type, activity, time, reporting unit, and source reliability (confirmed/reported).
5. S3 evaluates whether contact triggers a CCIR notification.
6. If contact is in a NAI, update the NAI status and notify the S2.

**Contact Report Data Entry Standard:**
- Location: 8-digit grid minimum; 10-digit for point contacts
- Time: Actual observation time, not report time
- Status: Reported (single source) / Confirmed (multiple sources or physical confirmation)
- Source: Reporting element identity

### 11-5. Daily Commander's Update Assessment (CUA) Product in MSS

Many USAREUR-AF units conduct a daily Commander's Update Assessment (CUA) — the daily operational brief to the commander that replaces or supplements the BUA at some echelons. MSS supports the CUA by providing pre-built, current data products that the S3 section exports for the brief.

**Standard CUA Products from MSS:**

| Product | MSS Source | Update Standard |
|---|---|---|
| Ground Situation Map | Combined arms workspace screenshot | Current within 2 hr of brief |
| Combat Power Chart | Readiness dashboard | Current within 4 hr of brief |
| Route Status Summary | Route layer table | Current within 4 hr of brief |
| Enemy Situation | Intelligence layer | S2 confirms current within 2 hr of brief |
| Phase Line / Objective Status | Operations layer | Current within 2 hr of brief |
| Key Event Timeline | Workspace event log | Last 24 hours of significant events |

> **NOTE: The CUA product built from MSS is only as good as the data in the workspace. The S3 section must conduct a workspace review 60 minutes before the CUA to confirm all data is current. Discrepancies identified during the review must be resolved before the brief or disclosed to the commander during the brief.**

### 11-6. Assessment Products for M&M Operations

Assessment is the determination of the significance of information to operations (ADP 5-0, para 1-58). For M&M practitioners, assessment products focus on progress toward the operational end state.

**M&M Assessment Products in MSS:**

**Phase Completion Assessment.** Displays the status of each operational phase — planned conditions, current conditions, and whether the unit is on timeline. Built from phase line crossing data, objective status, and combat power data.

**Combat Power Trend.** Tracks unit readiness over time — not just current status, but the trend (improving, stable, degrading). This requires historical data to have been maintained in MSS through the operation period. A unit that resets MSS data with each operation loses the trend data that makes the assessment meaningful.

**Mobility Assessment.** Summarizes the current mobility picture: which routes are open, restricted, or closed; which obstacles are breached; which bridge crossings are available. Used to assess freedom of maneuver for the next phase.

**Reconnaissance Achievement Assessment.** Tracks which PIRs have been answered by reconnaissance, which remain outstanding, and which reconnaissance objectives produced positive or negative reports. This is the primary input to the decision support matrix review.

---

## CHAPTER 12 — FIRE SUPPORT AND MANEUVER SYNCHRONIZATION IN MSS

**BLUF:** Fire support and maneuver synchronization is a life-safety function. The S3 section and FSO must maintain the fires and maneuver graphic layers in MSS with identical accuracy and currency standards. A mismatch between the fires graphic layer and the maneuver graphic layer creates fratricide conditions.

### 12-0. Pre-Mission Fires Coordination Checklist for M&M Practitioners

Before any offensive operation begins, the S3 section must complete the following fires coordination checks in MSS. This checklist supplements — it does not replace — the fires rehearsal and FSO coordination.

**Pre-Mission Fires Coordination Checklist:**

- [ ] All current FSCMs loaded in the fires layer and verified against the published fire support annex
- [ ] CFL positioned to cover the attacking force at H-hour (not the position at OPORD publication)
- [ ] All NFAs visible in the fires layer, with reason and authority documented
- [ ] FPF locations loaded for all defensive positions (if attack is preceded by a defense)
- [ ] Fires phase lines (triggers for FSCL movement) annotated on operational graphics
- [ ] Target overlays integrated with NAI/TAI from the intelligence layer
- [ ] No-fire areas cross-referenced against planned maneuver routes and assembly areas
- [ ] FSO has confirmed fires layer graphic accuracy before the mission begins

> **NOTE: This checklist is a minimum standard. Complex operations — air assault, breach, river crossing — require additional fires coordination steps beyond this checklist. Refer to the fires annex and FSO coordination for operation-specific requirements.**

### 12-1. The Fires-Maneuver Data Relationship

Fire support is not a separate warfighting function from maneuver — it is a component of combined arms, synchronized to produce the effects the maneuver commander needs (FM 3-09, para 1-2). In MSS, fires and maneuver data live in separate layers but must be visible simultaneously to both the S3 section and the fires officer.

The fundamental rule: any FSCM that affects maneuver — restricts routes, limits indirect fire in an objective area, designates a no-fire area — must be visible in the maneuver workspace. Any maneuver graphic that affects fires deconfliction — boundaries, phase lines that control fires transitions, LOAs that define the forward limit of indirect fire — must be visible to the FSO.

This requires either a single combined arms workspace with both layers, or two linked workspaces with cross-access. The mechanics are a configuration decision; the requirement is non-negotiable.

### 12-2. Fires Coordination Measures by Phase

FSCM requirements change as operations progress through phases. The S3 section must ensure that FSCM changes associated with phase transitions are updated in MSS before the transition occurs — not after.

**Common FSCM Transitions by Phase:**

| Transition Event | FSCM Change | MSS Update Standard |
|---|---|---|
| Crossing LD | CFL shifts forward to cover attacking force | Update before LD crossing |
| Reaching Phase Line | FSCL adjusts / CFL advances | Update on PL crossing report |
| Seizure of Objective | NFA established over objective area (for consolidation) | Update on objective seizure report |
| Passage of Lines | Fires responsibility transfers; boundary changes | Update when POL is initiated |
| Retrograde | CFL/FSCL pull back | Update before retrograde begins |

> **WARNING: An FSCM that has not been updated in MSS before a phase transition creates fires coordination risk at the moment of greatest tactical activity. The S3 and FSO must coordinate every FSCM change before execution, not discover the discrepancy during the battle captain's battle update.**

### 12-3. No-Fire Area and Restricted Fire Area Management

No-fire areas (NFA) and restricted fire areas (RFA) are among the most operationally sensitive graphics in the combined arms workspace. An NFA prohibits all fires; an RFA imposes conditions on fires delivery (no area fires, no fires without FSO coordination, etc.).

**NFA/RFA Data Requirements in MSS:**

| Field | Description |
|---|---|
| Area boundary | Polygon graphic, clearly bounded |
| Type | NFA / RFA / Restricted Fire Line |
| Effective period | Not earlier than / not later than (or permanent) |
| Authority | Who designated the NFA/RFA (higher, LOAC, CIV considerations) |
| Reason | Military, civilian, LOAC, interagency |
| Exceptions | Any permitted fires (e.g., "immediate self-defense only") |

> **NOTE: LOAC-based NFAs (hospitals, religious sites, civilian critical infrastructure) are permanent for the duration of the conflict unless the site loses protected status. They are never overridden by a single FRAGO or ad hoc decision. Coordinate any question about LOAC-based NFA status with the SJA before making changes in MSS.**

### 12-4. Final Protective Fires and Perimeter Defense Integration

Final protective fires (FPF) are an immediate, continuous volume of preplanned fires designed to impede enemy movement across defensive lines (FM 3-09, para 4-23). For defensive operations, the FPF is the most critical fires graphic in the combined arms workspace.

**FPF Data in MSS:**
- FPF location (line or point)
- Assigned weapon system (FA battery, mortar platoon)
- Priority of fires assignment
- Defensive position it protects
- Trigger (who calls, under what condition)

The S3 section must confirm the FPF graphic is in MSS before any defensive operation. The FPF is a preparatory requirement — it must be registered and confirmed before the unit occupies the defensive position. An FPF that exists on paper but is not in MSS is invisible to the combined arms picture and risks fratricide if the unit retrograde pulls through the FPF impact area.

---

## CHAPTER 13 — DEFENSIVE OPERATIONS IN MSS

**BLUF:** Defensive operations in MSS require the S3 section to manage the obstacle and fires picture as the primary data effort, alongside force tracking for the defending force. The defensive plan is more static than the offensive plan — but the data environment becomes more dynamic as the enemy approaches and engages.

### 13-0. Defensive Operations MSS Workspace Configuration

The defensive workspace differs from the offensive workspace in the balance of data layers. In the defense, the obstacle layer and the fires layer carry more operational weight than in the offense — because the defense is built around obstacle-fires integration to shape the enemy's approach into prepared engagement areas.

**Defensive Workspace Layer Priority:**

| Priority | Layer | Reason |
|---|---|---|
| 1 | Obstacle layer | Friendly obstacles define the defensive framework |
| 2 | Fires layer | FPF, target overlays, FSCM are the primary lethal mechanism |
| 3 | Blue Force layer | Defending unit positions and track |
| 4 | Operations layer | Battle positions, EA boundaries, withdrawal routes |
| 5 | Intelligence layer | Enemy templated approach, NAI/TAI for early warning |
| 6 | Aviation layer | ADA coverage, CASEVAC LZ |

> **NOTE: The priority order above is a general guideline for a deliberate defense. Hasty defense or delay operations may require a different priority balance. The S3 section adjusts workspace layer emphasis based on the specific operation and the commander's priority intelligence and fires requirements.**

### 13-1. Defensive Graphic Control Measures

The defensive plan uses a different set of graphic control measures than the offensive plan (FM 3-90, para 3-1). The S3 section must load the appropriate defensive graphics before the unit occupies defensive positions.

**Defensive Graphic Requirements in MSS:**

| Graphic | Purpose | MSS Layer |
|---|---|---|
| Main Battle Area (MBA) boundary | Defines the primary defensive space | Operations layer |
| Security area boundary | Area forward of the MBA for security forces | Operations layer |
| Battle positions | Named positions for defending units | Operations layer |
| Engagement areas (EA) | Named areas where fires will be concentrated | Operations layer / Fires layer |
| Obstacles (friendly) | Wire, AT ditches, minefields, reinforced obstacles | Obstacle layer |
| Target reference points (TRP) | Named aiming points for direct fire systems | Operations / Fires layer |
| FPF locations | Final protective fires for each defensive position | Fires layer |
| Withdrawal routes | Routes for retrograde if required | Route layer |

### 13-2. Engagement Area Development Data

Engagement areas (EAs) are where the defending commander plans to destroy the enemy (FM 3-90, para 3-25). EA development involves terrain analysis, obstacle integration, and fires synchronization — all of which are supported by MSS data layers.

**EA Development Data in MSS:**

- **Terrain overlay:** Dead ground, observation posts, flanking observation positions
- **Obstacle overlay:** Existing and planned obstacles that canalize enemy into the EA
- **Direct fire control measures:** TRPs, weapon positions, sectors of fire
- **Indirect fire overlay:** Target numbers, FPF, FSCM that enable EA fires
- **Enemy templated approach:** S2-maintained template of expected enemy avenue of approach into EA

### 13-3. Retrograde and Delay Operations

Retrograde operations — delay, withdrawal, and retirement — present unique data management challenges because the operational picture changes rapidly and the risk of fratricide during rearward movement is high (FM 3-90, para 3-1).

**Critical Data Tasks During Retrograde:**

- Update phase lines as the defending force falls back through successive PLs
- Track all friendly unit positions continuously during movement — retrograde creates significant BFT management demand because units are moving simultaneously
- Confirm withdrawal routes are current in the route layer and accessible to all subordinate S3 sections
- Update obstacle status as friendly forces retrograde through their own obstacle belt (confirm which lanes are open, which are being closed behind the force)
- Notify fires and aviation that the retrograde is in progress — FSCM may need to adjust as the force displaces

> **WARNING: Retrograde through a friendly obstacle belt is one of the highest-fratricide-risk maneuvers in ground operations. MSS must display the current obstacle lane status — open or closed — in real time during retrograde. An obstacle layer that shows a lane as open when it has been closed behind a withdrawing unit can direct a follow-on unit into a closed lane under fire.**

---

## CHAPTER 14 — MULTINATIONAL AND JOINT FORCE OPERATIONS

**BLUF:** USAREUR-AF BCTs routinely operate alongside NATO allies and joint service partners. MSS data sharing with multinational partners requires deliberate coordination — different nations use different systems, different symbology standards, and different data classification frameworks.

### 14-0. The Multinational Information Environment in USAREUR-AF

USAREUR-AF's operational environment is inherently multinational. NATO Article 5 operations, exercise DEFENDER series, and bilateral training events all involve coalition partners sharing the same AO. MSS is a US Army system — but the information it manages directly affects multinational operations.

The S3 section operating in a multinational environment must be able to answer two questions before every operation: what MSS data must be shared with allied partners to enable combined operations, and what data must be protected from sharing for OPSEC or classification reasons?

The answer to the first question is generally: operational graphics, route status, and key coordination graphics (FSCMs, LZ/PZ, boundaries) need to be shared to the extent that allied partners require them to conduct assigned tasks. The answer to the second question is: BFT data (precise friendly positions), source-sensitive intelligence overlays, and any data marked at a classification level not releasable to the partner nation must not be shared.

The coordination between what is shared and what is protected is a command decision — not a platform decision. MSS provides the access controls to implement the decision; the S3 section and the commander must make it.

### 14-1. Multinational Force Data Integration

NATO allies operating in the USAREUR-AF AOR may have access to MSS through approved partner accounts, or may use their own national C2 systems with liaison interfaces. The S3 section must understand which allies can see what in MSS and coordinate liaison accordingly.

**Multinational MSS Considerations:**

- **NATO symbology.** MIL-STD-2525D is interoperable with APP-6 (NATO military symbology standard). Most symbols are identical or very similar. Verify with multinational partners that symbols displayed in MSS are correctly interpreted. Some non-standard symbols may require translation.
- **Data classification.** MSS workspaces carrying REL-NATO data must be appropriately marked and access-controlled. Coordinate with the unit classification manager and S6 before sharing workspaces with allied partners.
- **Route naming.** MSR/ASR names used in MSS may not match the names in allied force orders. Establish a cross-reference table for route designators in multinational environments.
- **Grid reference systems.** MGRS is the US standard. Allied forces may use national grid systems. Confirm all graphics are in MGRS before sharing with multinational partners.

### 14-2. Joint Force Integration

Joint force operations — with US Air Force, Navy, or Marine Corps elements — present similar data integration challenges. MSS is an Army system; joint partners use different platforms. The S3 section coordinates with the J3/G3 joint coordination element for data sharing procedures.

**Joint Force MSS Coordination Points:**

- **USAF CAS coordination.** Close air support (CAS) graphics (fire support coordination areas, talk-on data, JTAC position) must be deconflicted with ground maneuver graphics. Establish a shared fires workspace with the ASOC/TACP that covers CAS area graphics.
- **Navy fires integration.** Naval gunfire support (NGFS) coordination requires the same fires graphic deconfliction standard as Army FA. NSFS mission areas and FSCM applicable to NGFS must be in the fires layer.
- **Marine Corps interoperability.** USMC units may use GCCS-M or other systems. Liaison officer procedures for MSS data sharing must be established before joint operations begin.

### 14-2. Allied Force Position Tracking

Allied partner force positions may or may not be in the MSS BFT feed. When allied forces have approved BFT integration through NATO interfaces, their positions appear in the Blue Force layer automatically. When they do not, the S3 section must manually track allied force positions using the same manual reporting standards as untracked US units.

**Allied Force Manual Tracking Procedure:**

1. Establish a reporting standard with the allied unit LNO: report format, frequency, and means.
2. Create named graphic objects for allied unit positions in the Blue Force layer — labeled with the allied unit designation in a format that prevents confusion with US units.
3. Update allied positions on receipt of each report, annotating the "last updated" DTG.
4. Brief allied positions to the commander with the same data currency standard as US unit positions.
5. Coordinate with the S2 to ensure allied positions are deconflicted with any enemy situation data.

> **CAUTION: Allied force positions are operationally sensitive. Ensure allied unit location data is access-controlled to personnel with a legitimate operational need. Coordinate with the multinational coordination cell and the S6 for appropriate access controls.**

### 14-3. Liaison Officer MSS Procedures

Liaison officers (LNOs) are the primary human interface for data exchange with partners who do not have MSS access. The LNO must understand the MSS combined arms workspace well enough to translate between the MSS picture and the partner's C2 system.

**LNO MSS Minimum Requirements:**
- Can read and interpret all M&M graphic types in the combined arms workspace
- Can export a specific workspace layer or screenshot for sharing with the partner unit
- Can receive partner force data and identify the appropriate MSS layer for entry
- Can identify data discrepancies between the MSS picture and the partner's force picture and report them to the S3

---

## CHAPTER 15 — TRAINING AND CERTIFICATION STANDARDS

**BLUF:** MSS certification for M&M practitioners requires completion of TM-10, TM-20, and TM-30 prerequisites and demonstrated proficiency on the tasks in this manual. This chapter describes the training path, assessment criteria, and recertification requirements for M&M practitioners.

### 15-1. Training Prerequisites and Path

**Prerequisites for TM-40C:**
1. TM-10, Maven User (Basic) — Completed and documented
2. TM-20, Builder — Completed and documented
3. TM-30, Advanced Builder — Completed and documented
4. CONCEPTS_GUIDE_TM40C_MOVEMENT_MANEUVER — Read prior to beginning TM-40C
5. Unit MOS qualification (11A, 19A, 12A, 15A, or equivalent) — Active

**TM-40C Training Sequence:**
1. Read the CONCEPTS_GUIDE (prerequisite)
2. Chapter 1 — Classroom/online instruction (overview and workspace orientation)
3. Chapters 2–5 — Practical exercises (planning, routing, reconnaissance, ground combat)
4. Chapters 6–8 — Practical exercises (aviation, urban, force tracking)
5. Chapters 9–10 — Scenario-based assessment (echelon-specific and degraded)
6. Chapters 11–13 — Reporting and fires integration (practical and assessed)
7. Certification assessment — Written and practical

### 15-2. Certification Assessment Criteria

A practitioner is certified at the TM-40C level when they demonstrate proficiency on the following tasks:

**Table 15-1. TM-40C Certification Task List**

| Task | Type | Minimum Standard |
|---|---|---|
| Load and publish OPORD graphics | Practical | All control measures loaded, correct symbology, published within time standard |
| Process a FRAGO graphic update | Practical | Graphics updated, versioned, subordinate notified within 30 min |
| Load and manage a reconnaissance plan | Practical | All objectives, routes, screen mission loaded; access confirmed |
| Update route status from clearance report | Practical | Status updated within 30 min; correct data fields populated |
| Build a combined arms workspace | Practical | All six layers configured; access controls set; echelon-appropriate |
| Generate SITREP data products | Practical | Data current within standard; all required elements present |
| Conduct degraded operations tracking | Practical | Current ground picture on paper within 30 min of simulated outage |
| Identify and correct stale graphics | Written/Practical | Identify three or more data errors in a prepared scenario workspace |
| Describe eight failure modes | Written | All eight failure modes described with correct mitigation standard |

### 15-3. Recertification Requirements

TM-40C certification is valid for 24 months. Recertification requires:

- Completion of any platform updates to TM-40C since initial certification
- Practical assessment on a minimum of three tasks from Table 15-1
- Demonstrated proficiency on degraded operations procedures

> **NOTE: Recertification requirements apply to the platform skills described in TM-40C. MOS qualification and unit training requirements (JRTC, DEFENDER exercise participation, etc.) are separate from MSS certification and governed by applicable Army training management publications.**

### 15-3a. Leader Assessment Standards — XO and S3

Leaders responsible for the S3 section's MSS employment must be able to assess, not just observe, MSS proficiency. The following indicators help the XO and S3 assess section proficiency during exercises and operations.

**Indicators of High Proficiency:**
- Section can state the data-as-of timestamp for any layer without prompting
- FRAGO graphic updates are complete before the S3 briefs the commander on the FRAGO
- The section proactively identifies stale data and reports it as an issue requiring correction
- Degraded operations transition is smooth and the current ground picture is available within 15 minutes
- Cross-section coordination (S2, engineer, FSO) produces same-day workspace updates without S3 prompting

**Indicators of Developing Proficiency:**
- Section updates MSS when time permits, not on a defined schedule
- FRAGO graphic updates lag the voice notification by more than 30 minutes
- The section defers stale data correction to the next battle rhythm cycle
- Degraded operations produces confusion and 45+ minute gap in the ground picture
- Cross-section coordination requires multiple S3 requests before workspace updates occur

**Indicators of Insufficient Proficiency:**
- Section is unable to identify data currency for a specific layer
- FRAGO graphic changes are found to be missing at the next BUA
- The section treats MSS as a PowerPoint support tool rather than an operational tracking system
- Degraded operations produce a gap of more than 60 minutes in the ground picture
- The workspace has not been updated in the last 4+ hours with no acknowledged outage explanation

### 15-4. Unit-Level Training Integration

TM-40C proficiency is not sustained by initial certification alone. S3 sections must integrate MSS M&M tasks into regular unit training events to sustain skills and train newly assigned personnel.

**Recommended Unit Training Integration:**

| Event | MSS M&M Training Integration | Frequency |
|---|---|---|
| Battle Staff Exercise (BSX) | Run full MSS combined arms workspace from mission receipt through execution; assess workspace currency standards | Quarterly |
| Command Post Exercise (CPX) | Full MSS employment by all staff sections; assess cross-section data standards | Semi-annually |
| Mission Rehearsal Exercise (MRE) | Live DEFENDER-standard MSS employment; degraded ops exercise included | Annually (DEFENDER preparation) |
| Battle Captain Shift Training | Route update, FRAGO graphic processing, SITREP data pull | Monthly |
| New Personnel Orientation | TM-10, TM-20, TM-30, and TM-40C read-through; supervised workspace access | Within 30 days of assignment |

### 15-4a. Sustainment of Proficiency During High-Operational-Tempo Periods

High operational tempo (OPTEMPO) periods — pre-deployment workups, DEFENDER preparation, JRTC rotations — create competing demands that squeeze MSS sustainment training. Units entering high OPTEMPO periods tend to reduce training maintenance activities to focus on collective tasks. MSS proficiency degrades rapidly without practice.

The S3 section should identify and protect three minimum MSS activities during high-OPTEMPO periods that sustain proficiency without consuming large blocks of training time:

**Minimum Sustainment Activities (High OPTEMPO):**

1. **Weekly workspace review (30 minutes).** One operator walks through the combined arms workspace and identifies any stale or incorrect data. The review does not need to correct all issues — it identifies them and creates a prioritized update list.

2. **Monthly timed exercise (60 minutes).** One complete FRAGO processing cycle, timed. Receive a FRAGO (from the supervisor), update all affected graphics, version-annotate, and notify subordinate S3 (simulated). Assessed against the 30-minute standard.

3. **Quarterly degraded drill (2 hours).** Full degraded operations exercise: MSS unavailable for 90 minutes. Section must maintain situational awareness, produce current ground picture, and restore to MSS within 30 minutes of "network restored" signal.

These three activities, conducted consistently, sustain the core proficiency required for operations. They do not fully develop new personnel or prepare the section for new platform features — but they prevent the skill degradation that occurs when MSS is used only as a presentation tool and not as an operational system.

### 15-5. Common Assessment Failures and Remediation

USAREUR-AF assessments of TM-40C proficiency identify common failure patterns that appear across units. S3 sections should self-assess against these patterns before formal assessments.

**Common Assessment Failures:**

**Symbology errors on obstacle graphics.** Assessed personnel select the incorrect obstacle type symbol or apply the wrong friendly/enemy color scheme. Remediation: dedicated symbology training with MIL-STD-2525D reference before practical assessment.

**Failure to version FRAGO graphics.** Assessed personnel update FRAGO graphics but do not annotate FRAGO number and effective DTG. Remediation: standardize FRAGO processing checklist and make version annotation a mandatory step before publishing.

**Missing data fields in route and obstacle reports.** Assessed personnel create route and obstacle objects with incomplete data fields — missing bridge MLC, missing obstacle dimensions, missing clearance DTG. Remediation: print the required fields checklists (Appendix C and D) and verify against them before submitting objects.

**Unable to produce manual battle tracking products within time standard.** Assessed personnel take more than 30 minutes to produce a current ground picture from manual records during simulated MSS outage. Remediation: conduct monthly timed degraded operations drills until the standard is consistently met.

---

## APPENDIX K — REFERENCES

The following publications are referenced in TM-40C. Practitioners should have access to the current version of each reference. Access through the Army Publishing Directorate (APD) at armypubs.army.mil.

### K-1. Doctrinal References by M&M Domain

TM-40C aligns to multiple doctrinal publications. Table K-1 provides a quick reference to the primary doctrinal sources for each M&M domain covered in this manual.

**Table K-1. Doctrinal References by M&M Domain**

| Publication | Key Content | MSS Chapter Reference |
|---|---|---|
| ADP 3-0, Operations (2019) | Foundation M&M doctrine; combined arms definition (para 1-5); M&M WFF tasks (para 3-3); operational framework | 1, 5, 9, Glossary |
| ADP 3-07, Stability (2019) | Stability operations framework; ASCOPE civil considerations; lines of effort construct | Appendix F |
| ADP 3-90, Offense and Defense (2019) | OAKOC terrain analysis factors (para 2-5); offensive/defensive task taxonomy | 7, 13, Glossary |
| ADP 5-0, The Operations Process (2019) | Operations process; assessment definition and methodology (para 1-58) | 11 |
| ADP 6-0, Mission Command (2019) | Mission command philosophy; C2 of Army forces | 1, 9 |
| FM 3-0, Operations (Mar 2025) | Current operations doctrine; S3/G3 roles and responsibilities (para 4-2); engineer mobility/countermobility tasks (para 3-12) | 1, 3, 9, Glossary |
| FM 3-09, Fire Support and Field Artillery Operations (Aug 2024) | Fire support doctrine; FSCM definition (para 1-1); FPF standards (para 4-23); fires-maneuver synchronization | 12, Glossary |
| FM 3-90, Offense and Defense (May 2023) | Offense/defense TTP; objective graphics (para 1-22); phase lines (para 2-10); passage of lines (para 4-5); consolidation and reorganization (para 4-13); river crossing operations (para 5-1); defensive graphic control measures (para 3-1); engagement area development (para 3-25) | 5, 7, 13, Glossary |
| FM 3-96, Brigade Combat Team (2015) | BCT operations; aviation officer roles (para 4-18); BCT combined arms integration (para 2-1) | 6, 9 |
| FM 3-98, Reconnaissance and Security Operations (2015) | Recon fundamentals (para 1-8); recon objectives (para 2-4); security missions — screen, guard, cover (para 4-2); counter-reconnaissance (para 1-12); NAI/TAI definitions (para 1-11) | 4, Glossary |
| FM 5-0, Planning and Orders Production (Nov 2024) | MDMP seven-step process (para 1-1); planning and orders production | 2 |
| FM 6-0, Commander's Activities (May 2022) | Commander's activities; battle rhythm; running estimates | 2, 9 |
| FM 3-81, Maneuver Enhancement Brigade (Nov 2021) | MEB doctrine; support area operations; area security | 9 |
| ATP 3-04.94, Brigade Aviation Element (2015) | Air corridor management; aviation-ground maneuver coordination; A2C2 procedures | 6 |
| ATP 3-90.4, Combined Arms Mobility (CUI) | Breaching and mobility operations; engineer mobility TTP | 3 |
| ATP 3-90.8, Combined Arms Breaching Operations (2020) | SOSRA breach sequence; breach planning data requirements; combined arms breach coordination | 3 |

**Standards and Policy:**

| Publication | Key Content | MSS Chapter Reference |
|---|---|---|
| MIL-STD-2525D, Joint Military Symbology (2014) | Tactical graphic standards; friendly/enemy/neutral color scheme; obstacle and FSCM symbology | All, Appendix B |
| Army CIO Memorandum, Data and Analytics Policy (Apr 2024) | Army data governance and analytics policy | All |
| ADatP-36, Friendly Force Information (FFI) | NATO standard for real-time friendly force tracking data exchange — position reports, unit status | 8, 14 |

**Strategic Guidance:**

> The following are strategic guidance documents — not doctrine — that inform MSS training design and operational context.

| Document | Authority | Relevance |
|---|---|---|
| Unified Data Reference Architecture (UDRA) v1.1 (Feb 2025) | Army | Enterprise data architecture reference for MSS integration |
| NATO Digital Transformation Implementation Strategy (Oct 2024) | NATO | MDO interoperability context — frames maneuver data sharing in coalition operations |
| DDOF Playbook v2.2 (December 2025) | T2COM C2DAO | VAULTIS-A quality framework (8 dimensions); 6-phase data product lifecycle; 85% quality gate; MVP mandate 30 days |

### K-2. Prerequisite Manuals

- TM-10, Maven User (Basic Operator's Manual)
- TM-20, Builder (Light Builder's Manual)
- TM-30, Advanced Builder
- CONCEPTS_GUIDE_TM40C_MOVEMENT_MANEUVER (companion to this manual)

---

## APPENDIX L — QUICK REFERENCE: KEY STANDARDS SUMMARY

The following table consolidates the key data currency and update standards from across TM-40C. Print and post at the S3 section workstation.

**Table L-1. TM-40C Key Standards at a Glance**

| Task | Standard | Chapter |
|---|---|---|
| FRAGO graphic update | Within 30 min of receipt | Ch. 2 |
| Phase line crossing update | Within 15 min of crossing report | Ch. 5 |
| Route clearance status update | Within 30 min of clearance report | Ch. 3 |
| Obstacle report entry | Within 30 min of OBSREP receipt | Ch. 3 |
| SPOTREP / CONTREP entry | Within 15 min of voice report | Ch. 11 |
| Manual position update | Within 15 min of report (no BFT) | Ch. 8 |
| SITREP data currency | All data within 4 hr of submission | Ch. 11 |
| BUA product preparation | Workspace current within 2 hr of brief | Ch. 9 |
| Building clearance update (MOUT) | Within 20 min of clearance report | Ch. 7 |
| MSS reconstitution after outage | All manual data entered within 60 min of restoration | Ch. 10 |
| Degraded ops manual picture | Current ground picture producible within 30 min | Ch. 10 |
| Allied force position update | On receipt of periodic report (per established standard) | Ch. 14 |

---

## APPENDIX A — M&M-SPECIFIC NAMING CONVENTIONS IN MSS

### A-1. Operational Graphics Naming

All operational graphic objects in MSS must follow the unit naming convention.

**Format:** [UNIT]-[TYPE]-[DESIGNATOR]-[VERSION]

Examples:
- `2-5CAV-PL-DRAGON-v1` — 2nd Squadron 5th Cavalry Regiment, Phase Line Dragon, version 1
- `1BDE-OBJ-COBRA-v2` — 1st Brigade, Objective Cobra, version 2 (updated)
- `1-502IN-BOUND-ALPHA-v1` — 1st Battalion 502d Infantry, Boundary Alpha, version 1

### A-2. Route Naming

**Format:** [TYPE]-[DESIGNATION]-[SEGMENT] where applicable

Examples:
- `MSR-TAMPA` — Main Supply Route Tampa
- `ASR-MADISON-SEG2` — Alternate Supply Route Madison, Segment 2
- `RTE-FORD-SITE-3` — Route to Ford Site 3 (engineer-classified)

### A-3. Obstacle Naming

**Format:** [UNIT]-[OBSREP]-[SEQUENCE NUMBER]-[DATE]

Examples:
- `12B-OBSREP-003-2026MAR12` — 12B company, obstacle report number 3, 12 March 2026

### A-4. Version Control Standard

All graphics that are modified by FRAGO must be versioned: add `-FRAGO[number]` to the object name and retain the previous version archived in the workspace with a "superseded" tag.

---

## APPENDIX B — TACTICAL GRAPHIC STANDARDS (MILITARY SYMBOLS IN MSS)

### B-1. Military Symbol Standard

All tactical graphics in MSS will conform to MIL-STD-2525D (Joint Military Symbology). The S3 section is responsible for ensuring all graphics use correct symbology before publishing to any shared workspace.

**Common M&M Symbology in MSS:**

| Symbol | Type | Color | Usage |
|---|---|---|---|
| Phase Line | Line | Black | Movement control, reporting triggers |
| Boundary | Line | Black (dashed) | Unit area definition |
| Objective | Rectangle/Circle | Black | Seizure/security objective |
| Axis of Advance | Arrow | Black | Direction/route of attack |
| Limit of Advance | Line | Black | Maximum forward position |
| Screen Line | Line | Blue | Cavalry screen position |
| Obstacle | X-pattern | Red | Enemy/unknown obstacles; Blue = friendly |
| Minefield | X-hatch pattern | Red/Blue | Enemy/friendly minefields |
| No-Fire Area | Circle with X | Black | Fire restriction boundary |

### B-2. Friendly vs. Enemy Symbology

**Friendly force graphics:** Blue fill / Blue outline (BLUFOR standard)
**Enemy graphics:** Red fill / Red outline (OPFOR standard)
**Neutral/Unknown:** Yellow or Green (IAW MIL-STD-2525D)

> **WARNING: Incorrect symbology — particularly swapping friendly and enemy colors on obstacle or FSCM graphics — creates direct fratricide and fires coordination risk. Verify all graphic colors against MIL-STD-2525D before publishing to the combined arms workspace.**

---

## APPENDIX C — ROUTE RECONNAISSANCE REPORT DATA FIELDS

The following data fields must be populated for every route reconnaissance report entered into MSS.

**Standard Route Reconnaissance Report Fields:**

| Field | Required | Description |
|---|---|---|
| Route designation | Yes | MSR/ASR name, number |
| Reconnaissance unit | Yes | Unit that conducted the reconnaissance |
| Reconnaissance DTG (complete) | Yes | Date/time reconnaissance was completed |
| Route segment covered | Yes | Start grid to end grid |
| Surface type | Yes | Improved / Unimproved / Trail / Cross-country |
| Road width | Yes | Width in meters |
| Vehicle classification | Yes | Wheeled / Tracked / Both |
| Maximum vehicle weight | Yes | In tons (MLC) |
| Bridges (each) | Yes if any | Location, MLC, current status |
| Obstacles (each) | Yes if any | Location, type, dimensions, status |
| Choke points | Yes if any | Location, width restriction, clearance |
| Threat data | Yes | IED indicators, mine signs, observation |
| Route status recommendation | Yes | Open / Restricted / Closed + reason |
| Special instructions | As needed | Convoy timing, lights, EMCON |

---

## APPENDIX D — ENGINEER OBSTACLE AND MOBILITY DATA STANDARDS

### D-1. Obstacle Report (OBSREP) Required Fields

| Field | Required | Description |
|---|---|---|
| Location | Yes | Center grid (8-digit minimum) |
| Obstacle type | Yes | Wire / Ditch / Minefield / Reinforced / FASCAM / IED belt |
| Dimensions | Yes | Length, width, depth (where applicable) |
| Emplacing agency | Yes | Friendly / Enemy / Unknown |
| Date/time emplaced | Yes if known | Estimated if not confirmed |
| Status | Yes | Breached / Unbreached / Bypassed |
| Bypass options | Yes if available | Left / Right / No bypass — distance |
| Covering fires | Yes if observed | Direction, weapon type |
| Self-destruct time | FASCAM only | DTG and time remaining |
| Reporting unit | Yes | Unit that submitted the OBSREP |

### D-2. Bridge Classification Data Fields

| Field | Required |
|---|---|
| Bridge location | Yes |
| Bridge name/designation | Yes |
| Military load classification (MLC) | Yes |
| Classification type | Yes — Wheeled/Tracked/Both |
| Condition | Yes — Intact / Damaged / Destroyed |
| Classification date | Yes |
| Classification authority | Yes — unit that classified |
| Special restrictions | As applicable |

---

## APPENDIX E — COMBINED ARMS SYNCHRONIZATION CHECKLIST

The S3 section uses this checklist before any major operation to confirm the MSS combined arms workspace is complete, accurate, and accessible.

### Pre-Execution Checklist

**Operational Graphics:**
- [ ] All phase lines loaded with correct designations
- [ ] All boundaries current (match published OPORD/FRAGO)
- [ ] All objectives loaded with assigned units and current status
- [ ] LD/LC, assault positions, attack positions loaded
- [ ] LOA loaded if specified

**Force Tracking:**
- [ ] All subordinate unit positions current (within reporting standard)
- [ ] Task organization display current
- [ ] BFT integration confirmed operational (coordinate with S6)

**Engineer / Route Data:**
- [ ] All known obstacles loaded in obstacle layer
- [ ] Route status current for all MSR/ASR in the AO
- [ ] Bridge classifications loaded for all crossing sites on planned routes
- [ ] Breach site data loaded (if applicable)

**Fires Integration:**
- [ ] All FSCMs loaded and current
- [ ] FSCMs deconflicted with maneuver routes and assembly areas
- [ ] Fire support triggers annotated on phase line graphics
- [ ] No-fire areas confirmed with FSO

**Aviation Integration:**
- [ ] Air corridors loaded with activation windows
- [ ] LZ/PZ graphics loaded with current status
- [ ] UAS airspace reservations loaded and deconflicted

**Reconnaissance / Intelligence:**
- [ ] NAI/TAI overlays current
- [ ] Reconnaissance objectives loaded with current status
- [ ] OP/LP positions current

**Access and Sharing:**
- [ ] Subordinate S3 sections confirmed access to combined arms workspace
- [ ] Higher S3 confirmed access
- [ ] Classification and access controls confirmed with IMO

---

## APPENDIX F — STABILITY OPERATIONS DATA MANAGEMENT (ADP 3-07)

### F-1. MSS in Stability Operations

Stability operations present a fundamentally different data environment from offensive and defensive operations (ADP 3-07, para 1-1). The enemy is less clearly defined; the population, host-nation government, and partner security forces become primary data sets; and the measures of effectiveness shift from terrain control to population stability, governance capacity, and security sector development.

M&M practitioners operating in a stability environment must adapt their MSS workspace from a warfighting orientation to a stability orientation. The same platform is used; the data types, layers, and products change.

**Key Data Type Differences in Stability Operations:**

| Offensive/Defensive | Stability Equivalent |
|---|---|
| Unit positions (BLUFOR/OPFOR) | Unit positions + partner force positions + civilian locations |
| Phase lines and objectives | Lines of effort (LOE), end state conditions |
| Obstacle overlays | Infrastructure status, route condition, key node functionality |
| Combat power ratings | Partner force capacity, civil authority presence, economic indicators |
| PIR / NAI / TAI | Civil considerations OAKOC-C (Community, Organizations, Attitudes, Key leaders, Capabilities) |

### F-2. Civil Considerations as M&M Data

ADP 3-07 identifies civil considerations under the OAKOC-C framework (Community, Organizations, Attitudes, Key leaders, Capabilities, and Environment — ASCOPE in some references) as the primary information framework for stability operations (ADP 3-07, para 1-22). MSS can represent civil considerations as named graphic objects and data layers when the unit has loaded the appropriate data.

**Civil Considerations Data in MSS:**

- **Key population centers:** Named polygon graphics with population data, stability assessment, and unit responsible for area
- **Critical infrastructure:** Named point graphics for power stations, water treatment facilities, bridges, hospitals, government buildings — with current status (functional/degraded/destroyed)
- **Partner security force positions:** Tracking of host-nation military, police, and security forces in the operational area
- **NGO / interagency locations:** Organization identity and contact information for civil-military coordination

### F-3. LOE Tracking in MSS

Lines of effort (LOE) in stability operations link tasks to achieving the desired end state (ADP 3-07, para 2-10). Unlike phase lines — which are geographic — LOEs are conceptual, measuring progress toward a condition rather than a position.

MSS supports LOE tracking by associating tasks, activities, and assessment indicators with named LOE objects. The S3 section, in coordination with the civil affairs section and the assessment officer, maintains the LOE status display in MSS.

**LOE Status States:**
- On Track: Progress indicators consistent with the campaign timeline
- At Risk: Progress lagging; requires assessment and potential course correction
- Behind: Significant shortfall; requires FRAGO or operational adjustment
- Complete: End state condition achieved for this LOE

---

## APPENDIX G — GLOSSARY OF M&M TERMS IN MSS CONTEXT

The following terms are used in this manual. Definitions reflect Army doctrinal usage adapted to MSS employment context.

**Axis of Advance.** A route or series of routes that a force uses to advance from one area to another (FM 3-90, para 1-24). In MSS, displayed as a directional arrow graphic in the operations layer.

**Blue Force Tracking (BFT).** A system that provides situational awareness of friendly force positions through GPS-derived location data transmitted to a networked display. In MSS, integrated from JBC-P and similar systems.

**Combined Arms.** The synchronized and simultaneous application of the elements of combat power to achieve an effect greater than if each element were employed separately (ADP 3-0, para 1-5). MSS supports combined arms by integrating cross-functional data into a single workspace.

**Countermobility.** The collection of obstacles and associated actions that degrade the enemy force's ability to move (FM 3-0, para 3-12). In MSS, represented by the obstacle layer maintained by the engineer section.

**Fire Support Coordination Measure (FSCM).** A measure employed by land forces to facilitate the rapid engagement of targets and simultaneously provide safeguards for friendly forces (FM 3-09, para 1-1). In MSS, maintained in the fires layer by the FSO.

**Line of Departure (LD).** A phase line used to coordinate the departure of attack elements (FM 3-90, para 1-25). In MSS, a linear graphic in the operations layer that serves as a reporting trigger.

**Military Load Classification (MLC).** A numerical designation that represents the load carrying capacity of a bridge or the equivalent weight of a vehicle crossing the bridge (FM 3-34.400). In MSS, a required data attribute for all bridge objects in the route layer.

**Mobility.** The combination of engineer tasks that support the force's ability to maneuver in the operating environment (FM 3-0, para 3-12). In MSS, represented by route status data, bridge classifications, and breach lane status.

**Named Area of Interest (NAI).** A point or area where activity or lack of activity is expected to confirm or deny a course of action or answer a priority intelligence requirement (FM 3-98, para 1-11). In MSS, maintained in the intelligence layer by the S2 section.

**Objective.** A location on the ground used to orient operations, phase operations, facilitate changes of direction, and provide for unity of effort (FM 3-90, para 1-22). In MSS, a polygon or point graphic in the operations layer.

**Phase Line (PL).** A line used for control and coordination of military operations — usually a recognizable terrain feature (FM 3-90, para 1-25). In MSS, a linear graphic that also functions as a reporting trigger when configured.

**Reconnaissance Objective.** An area, named feature, or activity designated for reconnaissance collection by a specific unit within a defined timeline (FM 3-98, para 2-4). In MSS, a named graphic with associated PIR, assigned unit, timeline, and status.

**Route.** A line of communications connecting one area with another (FM 3-34.400). In MSS, a linear or point-series graphic with associated route classification attributes.

**Screen.** A security task that primarily provides early warning to the protected force (FM 3-98, para 4-2). In MSS, represented by a screen line graphic, OP/LP positions, and cavalry unit tracking.

**Targeted Area of Interest (TAI).** The geographical area or point along a mobility corridor where enemy forces are expected to be engaged to achieve a desired effect, in support of the commander's scheme of maneuver and concept of fires (FM 3-98, para 1-11). In MSS, maintained in the intelligence/fires layer.

---

## APPENDIX H — MOS QUICK REFERENCE BY DUTY POSITION

**Table H-1. M&M MOS Quick Reference**

| MOS | Title | Primary MSS Function | TM-40C Chapters |
|---|---|---|---|
| 11A | Infantry Officer | Company/bn S3 M&M data — plan, track, report | 2, 3, 5, 9 |
| 11B | Infantryman | Consumer of bn workspace; phase line reports | 5, 9 |
| 11C | Indirect Fire Infantryman | Fire support graphic integration at company | 2, 5 |
| 11Z | Infantry Senior Sergeant | NCOIC quality control of M&M data | 2, 5, 8 |
| 19A | Armor Officer | Combined arms team S3 — M&M planning and tracking | 2, 3, 5, 9 |
| 19D | Cavalry Scout | Reconnaissance plan management, screen/guard tracking | 4, 8 |
| 19K | M1 Armor Crewmember | Consumer of bn workspace; phase line reports | 5, 8 |
| 19Z | Armor Senior Sergeant | NCOIC quality control of M&M data | 5, 8, 9 |
| 12A | Engineer Officer | Engineer data section — obstacle, route, bridge data | 3, 4, 7 |
| 12B | Combat Engineer | Obstacle and route data entry, breach tracking | 3, 7 |
| 12C | Bridge Crewmember | Bridge classification data, river crossing status | 3, 7 |
| 12G | Quarrying Specialist | Terrain and materials data (route surface / fill material) | 3 |
| 15A | Aviation Officer | Aviation layer — corridors, LZ/PZ, deconfliction | 6 |
| 15W | UAS Operator | UAS airspace data, mission tracking, ISR product push | 6 |
| 120A | Construction Engineering Technician | Infrastructure data, route classification | 3, 7 |
| 125D | UAS Repairer | UAS status and maintenance data (where tracked) | 6 |

---

## APPENDIX I — BATTLE RHYTHM INTEGRATION FOR M&M MSS TASKS

The S3 section maintains MSS as part of the unit battle rhythm. The following template identifies the minimum MSS tasks required at each battle rhythm event.

**Table I-1. M&M MSS Battle Rhythm Integration**

| Event | Frequency | MSS Task | Owner | Time Standard |
|---|---|---|---|---|
| Battle Update Assessment (BUA) | Daily (minimum) | Build maneuver status product; confirm all graphics current | S3 / Battle Captain | 60 min before BUA |
| FRAGO processing | On receipt | Update all affected graphics; notify subordinate S3 | Primary MSS operator | 30 min after receipt |
| Position report cycle | Per SOP | Update BFT / manual positions for all subordinate units | S3 NCO | 15 min from report |
| Route status update | Per SOP / on report | Update route status layer with current clearance/obstacle data | S3 / Engineer section | 30 min from report |
| Obstacle report (OBSREP) | On receipt | Load new obstacles in obstacle layer | Engineer section | 30 min from receipt |
| Reconnaissance debrief | Per SOP | Update reconnaissance objective status; post SPOTREP data | S3 / S2 (coordinated) | 30 min from debrief |
| Combat power brief | Per SOP | Pull readiness / strength data for maneuver status product | S3 NCOIC | 60 min before brief |
| Phase line crossing report | On event | Update phase line status in MSS; notify higher S3 | Battle Captain | 15 min from report |
| Aviation coordination | Pre-mission | Confirm air corridors, LZ/PZ, and UAS deconfliction in workspace | 15A / S3 (coordinated) | 2 hr before mission |
| Workspace access review | Start of each operation | Confirm access for all users; update as personnel change | S6 (technical) / S3 (direction) | Before execution begins |

---

## APPENDIX J — INDIVIDUAL TASK STANDARDS SUMMARY

The following tasks appear in this manual with full Conditions/Standards/Procedure blocks. This appendix provides a quick-reference summary of the standard for each task.

**Table J-1. TM-40C Task Standards Summary**

| Task | Standard | Reference |
|---|---|---|
| Route Clearance Tracking in MSS | Update route status within 30 min of clearance report; include DTG, unit, segment, and obstacle disposition | Chapter 3, para 3-4 |
| Load and Manage a Reconnaissance Plan in MSS | All objectives, route recon task, and screen mission loaded within 2 hr of OPORD receipt; correct symbology; subordinate access confirmed | Chapter 4, para 4-3 |
| Building Clearance Tracking in MSS During MOUT | Update building status within 20 min of clearance report; clearing unit and DTG entered; visible on shared MOUT workspace | Chapter 7, para 7-2 |
| Manual Battle Tracking Reconstitution | Produce current ground picture on paper within 30 min of MSS outage; complete with positions, graphics, route status | Chapter 10, para 10-2 |
| FRAGO Graphic Update | All graphic changes updated within 30 min of FRAGO receipt; FRAGO number and effective DTG annotated; subordinate S3 notification complete | Chapter 2, para 2-5 |
| Combat Power Dashboard Update | Personnel and equipment status current within 4 hr; C-rating displayed by unit; visible to battle captain | Chapter 8, para 8-4 |
| Passage of Lines Data Load | All POL data loaded (passing unit, route, window, guide) before passage begins; both passing and stationary unit S3 sections have workspace access | Chapter 5, para 5-5 |
| MSS Reconstitution After Outage | Manual data reconciled and MSS updated within 60 min of system restoration; outage window documented; subordinate S3 notification complete | Chapter 10, para 10-5 |

---

---

## GLOSSARY

**AO.** Area of Operations.

**ASR.** Alternate Supply Route.

**BFT.** Blue Force Tracking.

**BUA.** Battle Update Assessment.

**CFL.** Coordinated Fire Line.

**COA.** Course of Action.

**CONTREP.** Contact Report.

**COP.** Common Operational Picture.

**CP.** Command Post.

**CUA.** Commander's Update Assessment.

**DTG.** Date-Time Group.

**EA.** Engagement Area.

**EOS.** Estimated Return to Operational Status.

**FPF.** Final Protective Fire.

**FRAGO.** Fragmentary Order.

**FSCM.** Fire Support Coordination Measure.

**FSCL.** Fire Support Coordination Line.

**IMO.** Information Management Officer.

**LD.** Line of Departure.

**LOA.** Limit of Advance.

**LOE.** Line of Effort.

**LZ.** Landing Zone.

**MDMP.** Military Decision-Making Process.

**MLC.** Military Load Classification.

**MSR.** Main Supply Route.

**NAI.** Named Area of Interest.

**NFA.** No-Fire Area.

**OBSREP.** Obstacle Report.

**OAKOC.** Observation and Fields of Fire, Avenues of Approach, Key Terrain, Obstacles, Cover and Concealment.

**OPORD.** Operations Order.

**PACE.** Primary, Alternate, Contingency, Emergency.

**PIR.** Priority Intelligence Requirement.

**PL.** Phase Line.

**POL.** Passage of Lines.

**PZ.** Pickup Zone.

**RFA.** Restricted Fire Area.

**SITREP.** Situation Report.

**SPOTREP.** Spot Report.

**TAI.** Targeted Area of Interest.

**TCS.** Task-Condition-Standard.

**TRP.** Target Reference Point.

---

## RELATED MANUALS AND TRAINING TRACKS

### WFF Peer Tracks

TM-40C is one of six Warfighting Function tracks at the same tier. All six WFF tracks require TM-10, TM-20, and TM-30 as prerequisites. M&M practitioners should develop working familiarity with TM-40A (Intelligence) and TM-40F (Mission Command) — the peer tracks with the most intensive M&M coordination requirements.

**Table. WFF Peer Track Quick Reference**

| Track | Title | Prereq | Primary M&M Coordination Point |
|-------|-------|--------|--------------------------------|
| TM-40A | Intelligence WFF | TM-10 + TM-20 + TM-30 | NAI/TAI overlays, PIR/IR supporting reconnaissance |
| TM-40B | Fires WFF | TM-10 + TM-20 + TM-30 | FSCM coordination, airspace deconfliction |
| TM-40C | Movement and Maneuver WFF | TM-10 + TM-20 + TM-30 | This manual |
| TM-40D | Sustainment WFF | TM-10 + TM-20 + TM-30 | Maneuver unit readiness, route capacity, supply constraints |
| TM-40E | Protection WFF | TM-10 + TM-20 + TM-30 | Physical security, NBC threat overlays (see NBC report cross-ref) |
| TM-40F | Mission Command WFF | TM-10 + TM-20 + TM-30 | Combined arms COP, CCIR thresholds for maneuver triggers |

### Specialist Tracks (Prerequisite: TM-30)

For technical specialists pursuing advanced capability development, specialist tracks are available after completing TM-30. Not required for M&M WFF employment.

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

## APPENDIX M — PROFESSIONAL READING LIST

> Curated articles from Army professional journals and military publications. These supplement doctrinal references with contemporary operational perspectives.

| Source | Title | Date | Relevance |
|---|---|---|---|
| Infantry Magazine | "Moneyball for Gunnery" (1/4 ID BCT data analytics) | 2024 | Data analytics for maneuver readiness |
| Field Artillery Bulletin | "The Combat Aviation Brigade and Digital Call for Fire" | 2024 | Digital fires-maneuver integration |

---

*TM-40C — MOVEMENT AND MANEUVER WARFIGHTING FUNCTION — Version 1.0 — March 2026*
*HEADQUARTERS, UNITED STATES ARMY EUROPE AND AFRICA — Wiesbaden, Germany*
*DISTRIBUTION RESTRICTION: Distribution authorized to U.S. Government agencies and their contractors only. Other requests must be referred to Headquarters, C2DAO, Wiesbaden, Germany.*

**DoD and Army Strategic References:**

- **JADC2 Strategy Summary (March 2022)** — Cross-domain data integration strategy for Joint All-Domain Command and Control
- **DoD Directive 3000.09, Autonomy in Weapon Systems (January 2023 update)** — Policy on autonomous and semi-autonomous functions in weapon systems; context for autonomous maneuver systems
- **DDOF Playbook v2.2 (December 2025)** — T2COM C2DAO; VAULTIS-A quality framework (8 dimensions); 6-phase data product lifecycle; 85% quality gate; MVP mandate 30 days
