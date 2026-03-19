# TM-40F — MAVEN SMART SYSTEM (MSS)

> **BLUF:** TM-40F teaches Mission Command practitioners — S3s, XOs, battle captains, and G3 staff — how to use MSS in daily operational work. No coding or pipeline development. Pure operational use of a data-enabled enterprise platform in support of the Mission Command warfighting function.
> **Prereqs:** TM-10, Maven User; TM-20, Builder; TM-30, Advanced Builder; CONCEPTS_GUIDE_TM40F_MISSION_COMMAND (required before beginning this manual). Builder skills are not exercised in this track — Mission Command practitioners operate pre-built MSS products (see paragraph 1-4, NOTE). No coding, pipeline development, or transform experience is required or assumed.
> *HQ USAREUR-AF · v1.0 · 2026 · DISTRIB: USG only · AUTH: C2DAO/UDRA v1.1*

> **WARNING: Presenting MSS data to a commander without verifying data currency and source validation can lead to decisions based on false situational awareness. Always confirm data-as-of timestamp and source pipeline status before the BUA or any commander brief.**
> **CAUTION: MSS CCIR alerts are threshold-based and dependent on reported data. An alert is a prompt to investigate — not a confirmed event. Validate CCIR triggers against primary reporting channels before taking action or briefing up.**
> **NOTE: MSS does not replace the battle rhythm, the MDMP, or commander/staff judgment. It accelerates and integrates the information that feeds those processes. The operations process (ADP 5-0) remains the framework. MSS is the data layer within it.**

---

## CHAPTER 1 — INTRODUCTION: DOCTRINAL BASIS AND PURPOSE

**BLUF:** TM-40F teaches Mission Command practitioners — S3s, XOs, battle captains, and G3 staff — how to use MSS in daily operational work. No coding or pipeline development. Pure operational use of a data-enabled enterprise platform in support of the Mission Command warfighting function.

### 1-1. Mission Command Doctrine and MSS

Mission Command is the Army's approach to command and control that empowers subordinate commanders to exercise disciplined initiative within the commander's intent, enabling agile and adaptive action (ADP 6-0, para 1-1). The seven principles of Mission Command are: build cohesive teams through mutual trust; create shared understanding; provide a clear commander's intent; exercise disciplined initiative; use mission orders; accept prudent risk; and foster collaborative, inclusive leadership (ADP 6-0, para 1-28).

MSS does not change any of these principles. It changes the quality, speed, and integration of the information that supports them. A staff that formerly spent significant hours assembling slide products from disparate report streams can, with MSS properly employed, arrive at the BUA with pre-built, current, integrated data products — and spend that recovered time on analysis, planning, and coordination.

The USAREUR-AF C2DAO built MSS on Palantir Foundry specifically to integrate operational data streams — readiness, personnel, logistics, intelligence feeds, and training data — into a single enterprise platform accessible across the formation. This does not centralize decision authority. It enables shared understanding (ADP 6-0, para 2-8), which is the prerequisite for disciplined initiative at every echelon.

> **NOTE: MSS is a Mission Command enabler. Shared understanding — the foundation of Mission Command — depends on information quality, speed, and accessibility. MSS addresses all three. The principles remain constant; the information environment has changed.**

> **NOTE:** The **EUCOM Thunderforge AI Planning Ecosystem** (DIU/Scale AI contract, 2024–25) employs AI agents to augment MDMP and wargaming at theater level, compressing planning timelines. Mission Command practitioners trained on MSS are the operational users of Thunderforge-class AI planning tools — the staff integration and MDMP data procedures in TM-40F are directly applicable to AI-augmented planning environments where human judgment remains authoritative over AI-generated options.

### 1-2. Scope: What TM-40F Covers and Does Not Cover

**TM-40F covers:**

- Staff role integration with MSS for each section (S1 through S6, cross-functional cells, functional area officers)
- MDMP data support procedures for all seven steps (FM 5-0)
- Battle rhythm design, mapping, and data product management (FM 6-0, ATP 6-0.5)
- CP configuration and MSS display management across echelon types (ATP 6-0.5)
- CCIR loading, monitoring, and decision support product management (FM 6-0)
- COP architecture and data layer integration (FM 6-02)
- Assessment product generation (MOE/MOP) on MSS (ADP 5-0, FM 5-0)
- SITREP, SPOTREP, and readiness report generation from MSS data
- Degraded operations procedures and fallback products
- Echelon-specific guidance from BCT through Corps

**TM-40F does NOT cover:**

- Pipeline construction, data transforms, or code development — see TM-30 and TM-40 series technical manuals
- Ontology design or dataset schema modification — see TM-30
- Machine learning model management — see TM-40M
- AI Logic (AIP) application development — see TM-40H
- Financial management data systems — see unit S6/IMO
- Building Workshop applications — see TM-20

### 1-3. Audience and MOS Coverage

This manual is written for Mission Command practitioners who consume and direct the use of MSS data products in operational settings. Table 1-1 identifies the primary audience by section and MOS.

**Table 1-1. Primary Audience by Section and MOS**

| Section | Officer MOS / Branch | Enlisted MOS | Position Examples |
|---|---|---|---|
| S3 / G3 | 11A, 19A, 13A (and branch equivalents) | 11Z, 19Z, 13Z | S3, XO, Battle Captain, Current Ops OIC |
| S2 / G2 | 35A, 35D | 35F, 35N, 35G | S2, All-Source Section Chief, IPB NCO |
| S1 / G1 | 42A (HR Officer) | 42A, 42H, 42R | S1, HR NCOIC, Strength Manager |
| S4 / G4 | 90A (AG/QM) | 92A, 92Y, 92F | S4, Supply OIC, Maintenance OIC |
| S6 / G6 | 25A (Signal) | 25U, 25Z | S6, Network OIC, MSS Administrator |
| Fires (FECC) | 13A (FA) | 13F, 13B | FSO, FSCOORD, Targeting Officer |
| CBRN | 74A, 74D | 74D | CBRN Officer, CBRN NCO |
| SJA | 27A, 27D | — | Staff Judge Advocate, Legal NCO |
| FA Officers | 50A, 51A, 53A, 54A | — | Force Manager, Engineer, Info Systems, IO |
| ADAM/BAE | 15A, 15B | 15Q, 15R | Aviation Officer, A2C2 Officer |

### 1-4. Prerequisites

Before beginning this manual, verify the following:

**Platform prerequisites:**
- [ ] TM-10 complete — can log into MSS, navigate Workshop, access assigned datasets, and use standard dashboard views
- [ ] CONCEPTS_GUIDE_TM40F complete — Mission Command doctrine / MSS integration mental models established
- [ ] MSS account provisioned with appropriate role and permissions — coordinate with unit S6

**Operational prerequisites:**
- [ ] Familiar with unit battle rhythm events and reporting requirements
- [ ] Familiar with commander's published CCIR list and decision support requirements
- [ ] Familiar with basic CP organization and staff section responsibilities at your echelon
- [ ] Completed unit-level OPSEC training for MSS data handling

> **NOTE: TM-20 and TM-30 are required as prerequisites (Go evaluations on file) but builder skills are not exercised in this manual. TM-40F assumes no ability to build pipelines or transforms. If you encounter a data product that does not exist and needs to be built, coordinate with your unit's designated MSS Builder (TM-30 qualified) or the C2DAO.**

### 1-5. Relationship to Other TMs in the MSS Curriculum

**Table 1-2. TM Curriculum Relationships**

| TM | Title | Relationship to TM-40F |
|---|---|---|
| TM-10 | Maven User | Foundation prerequisite. Platform navigation, basic data access. |
| TM-20 | Builder | Required as prerequisite (Go evaluation on file). Builder skills are not exercised in this track — TM-40F practitioners consume pre-built products. The TM-20 cert is part of the progression chain to TM-30. |
| TM-30 | Advanced Builder | Required prerequisite (Go evaluation on file). Advanced builder skills are not exercised in this track. TM-30 completion certifies platform literacy at the level required before WFF track enrollment. |
| TM-40A | Intelligence WFF | WFF peer track (prereq TM-10 + TM-20 + TM-30). PIR-derived CCIR components feed the Mission Command CCIR dashboard. |
| TM-40B | Fires WFF | WFF peer track (prereq TM-10 + TM-20 + TM-30). Fires products integrate into the commander's COP and CCIR monitoring. |
| TM-40C | Movement and Maneuver WFF | WFF peer track (prereq TM-10 + TM-20 + TM-30). Force tracking, route status, and phase line reporting feed the COP. |
| TM-40D | Sustainment WFF | WFF peer track (prereq TM-10 + TM-20 + TM-30). LOGSTAT feeds commander FFIR thresholds and sustainment picture on the COP. |
| TM-40E | Protection WFF | WFF peer track (prereq TM-10 + TM-20 + TM-30). Protection data integrates into the COP; CCIR thresholds consume protection status. |
| TM-40F | Mission Command WFF | This manual. |
| TM-40G | ORSA | Specialist track (prereq TM-30). Companion. ORSA analysts build quantitative products that TM-40F users receive and brief. |
| TM-40H | AI Engineer | Specialist track (prereq TM-30). Awareness-level: produces AI-enabled alerts in CCIR monitoring. |
| TM-40M | ML Engineer | Specialist track (prereq TM-30). Awareness-level: produces predictive products on MSS. |
| TM-40J | Program Manager | Specialist track (prereq TM-30). PM data feeds readiness and portfolio products consumed by S3. |
| TM-40K | Knowledge Manager | Specialist track (prereq TM-30). KM maintains information products and lessons learned accessible in MSS. |
| TM-40L | Software Engineer | Specialist track (prereq TM-30). Builds platform integrations and data pipelines behind TM-40F products. |
| TM-50G–M | Advanced Specialist Tracks | Post-graduate level for technical specialists (prereq TM-40G–M). Not applicable to operational staff. |

### 1-6. FM 6-0 Information Management Framework and MSS

FM 6-0 (May 2022) defines information management (IM) as the science of using procedures and information systems to collect, process, store, display, disseminate, and protect knowledge products, data, and information (FM 6-0, para 4-1). MSS implements all six IM tasks as platform capabilities. Table 1-3 maps each FM 6-0 IM task to its MSS implementation.

**Table 1-3. FM 6-0 Information Management Tasks — MSS Implementation**

| IM Task (FM 6-0) | FM 6-0 Definition | Data Platform Implementation |
|---|---|---|
| Collect | Acquire data and information from organic and external sources | Data ingestion pipelines, sensor feeds, manual entry, GCSS-Army/DTMS/DPAS connectors |
| Process | Convert data into a form suitable for analysis and decision-making | ETL transforms, data wrangling, enrichment, deduplication, schema normalization |
| Store | Maintain data in accessible repositories with appropriate retention | Data repositories, datasets, object storage, version-controlled pipelines |
| Display | Present data in formats that support understanding and decision-making | Dashboards, COP overlays, reports, Workshop visualizations, briefing products |
| Disseminate | Distribute data products to authorized users at the right time | API endpoints, data sharing permissions, automated notifications, CCIR alerts |
| Protect | Safeguard data from unauthorized access, modification, or destruction | Access controls (RBAC), encryption, classification enforcement, OPSEC markings |

> **NOTE: Every staff section in the TM-40F framework (Chapter 2) executes all six IM tasks within its data domain. The S6 coordinates the technical enablement; the S3 directs the operational requirements; each section owns the accuracy and currency of its data products.**

**Information Relevance Criteria.** FM 6-0, para 4-6 establishes six criteria for determining whether information meets commander requirements. These criteria map directly to the VAULTIS-A data quality dimensions used in the DDOF Playbook v2.2 (see Appendix D, Strategic Guidance). Table 1-4 provides the crosswalk.

**Table 1-4. FM 6-0 Information Relevance Criteria — VAULTIS-A Crosswalk**

| FM 6-0 Criterion | FM 6-0 Definition | VAULTIS-A Dimension |
|---|---|---|
| Accurate | Free from error; faithful to the source | Accuracy |
| Timely | Available in time to support the decision | Timeliness |
| Useable | In a format appropriate to the consumer | Usability |
| Complete | Contains all elements necessary for the decision | Completeness |
| Precise | Specific enough for the intended purpose | (Contributes to Accuracy and Completeness) |
| Secure | Protected from unauthorized access or compromise | Security |

> **NOTE: When a data product fails a VAULTIS-A quality gate (85% threshold per DDOF Playbook), staff should diagnose the failure against these six FM 6-0 criteria. This ensures corrective action is framed in doctrinal language the commander understands — not just technical metrics.**

---

## CHAPTER 2 — STAFF ORGANIZATION AND MSS ROLE INTEGRATION

**BLUF:** Every staff section has a data domain on MSS. Role integration means each section owns its data, contributes it to the shared COP, and consumes data from adjacent sections — not through ad hoc coordination, but through structured MSS products. This chapter defines those roles for every section from S1 to cross-functional cells and functional area officers (FM 6-0, Chapter 3).

### 2-1. S3 / G3 Section — Operations

**MOS:** 11A, 19A, 13A (branch equivalents); 11Z, 19Z (senior NCOs)
**Positions:** S3, XO, Battle Captain, Current Ops OIC, Future Operations Officer

**Role Description.** The S3 is the primary consumer of all MSS data products in the Mission Command context. The S3 directs data requirements — which products need to exist, at what level of detail, with what data freshness — and ensures those products are available for commander decision-making. The S3 also owns the operations data layer: task organization, mission tracking, battle rhythm event management, and synchronization of data products across the formation (FM 6-0, para 3-11).

**MSS Data Domain:**
- Task organization (TASKORG) data — unit attachments, detachments, operational control (OPCON), tactical control (TACON)
- Mission status and progress tracking
- Decision point status and decision brief products
- Synchronization matrix data
- Operations order (OPORD) data management — branches, sequels, CCIR triggers

**Specific Tasks on MSS:**
1. Load and maintain the current TASKORG in the unit's MSS organizational workspace.
2. Monitor COP data currency — verify data freshness before every BUA (see paragraph 7-5).
3. Direct MSS product development — specify required products to unit MSS Builders or C2DAO.
4. Manage CCIR alerts — review automated triggers, validate against primary reporting channels, brief commander.
5. Maintain decision point status — update DPs as triggered or no longer valid.
6. Build or direct the build of the Battle Update Assessment (BUA) data product package (see paragraph 4-3).
7. Coordinate synchronization matrix data with S2 (intel), S4 (logistics), and fire support for integrated products.

**CCIR Responsibilities (FM 6-0, para 2-17):**
- Maintains the master CCIR list in MSS, aligned to the commander's published CCIRs.
- Ensures FFIR thresholds (personnel, readiness, logistics) are accurately loaded.
- Receives CCIR alert notifications, validates, and briefs the commander.
- Coordinates with S2 to ensure PIR triggers are connected to MSS intelligence data feeds.

**Coordination with Other Sections:**
- S2: Receives INTSUM products, PIR status, and threat overlay data.
- S4: Receives LOGSTAT, maintenance status, and Class I–IX data for readiness picture.
- S1: Receives PERSTAT and casualty data for strength and personnel FFIR monitoring.
- S6: Coordinates on network configuration, MSS display setup, and CP connectivity.

---

### 2-2. S2 / G2 Section — Intelligence

**MOS:** 35A (MI Officer), 35D (All-Source Intel Officer); 35F (Intel Analyst), 35N (SIGINT Analyst), 35G (Geospatial)
**Positions:** S2, All-Source Section Chief, IPB NCO, SIGINT Team Chief

**Role Description.** The S2 section is the primary contributor of threat, IPB, and intelligence data to the MSS Common Operating Picture. S2 maintains the intelligence data layer that informs commander decisions on threat disposition, terrain analysis, and enemy COA probability. The S2 also supports CCIR monitoring by providing PIR-relevant data through MSS intelligence integration (FM 6-0, para 3-9).

**MSS Data Domain:**
- Threat disposition overlays (enemy known/templated positions)
- IPB data layers: terrain analysis, trafficability data, weather-effects integration
- PIR tracking and status
- INTSUM source data
- Target nominations and high-value target (HVT) tracking

**Specific Tasks on MSS:**
1. Maintain the threat overlay on MSS with current enemy disposition data. Update frequency: per SOPs, minimum before every BUA.
2. Load and monitor PIRs as linked CCIRs in the MSS CCIR management workspace (see Chapter 6).
3. Build and maintain the IPB data layer: terrain, trafficability, weather effects as applicable.
4. Produce the INTSUM as an MSS-based product, drawing on current threat and intelligence feeds available on the platform.
5. Contribute target nominations to the MSS fires integration workspace (see paragraph 2-7 for FECC coordination).
6. Provide intelligence data in support of COA analysis and wargame products (see paragraph 3-2, Step 4).

**CCIR Responsibilities:**
- Owns PIR entries in the unit MSS CCIR workspace. Formats PIR triggers as observable, reportable, and threshold-based.
- Monitors MSS intelligence data feeds for PIR-relevant information.
- Triggers PIR reporting to S3 through MSS notification when PIR collection threshold is met or intel is denied.

**S2/S3 Integration Procedures:**
- S2 provides the current threat overlay to S3 before every BUA. The S3 battle captain validates currency.
- PIR status brief is a standing BUA agenda item. S2 prepares the MSS PIR product for this brief.
- S2 and S3 coordinate COA analysis data sets: S2 provides threat and IPB data; S3 provides BLUFOR TASKORG and mission data.
- Intelligence collection plan is managed in MSS with S3 coordination for collection asset tasking.

> **NOTE: S2 data on MSS reflects what has been reported and processed. The S2 must distinguish between "reported" and "assessed" enemy status in all MSS products. Label products accordingly to prevent consumers from treating templated positions as confirmed.**

---

### 2-3. S1 / G1 Section — Personnel

**MOS:** 42A (HR Specialist), 42H (Senior HR Sergeant), 42R (Financial Management Technician)
**Positions:** S1, HR NCOIC, Strength Manager, Casualty Operations Officer

**Role Description.** The S1 section manages the personnel data domain on MSS: strength accounting, PERSTAT, casualty data, and personnel readiness inputs. S1 data feeds directly into the Mission Command picture — specifically the personnel FFIR thresholds and the unit readiness assessment (FM 6-0, para 3-7). Accurate S1 data is a prerequisite for accurate strength-to-task analysis in planning.

**MSS Data Domain:**
- PERSTAT (Personnel Status Report): assigned, present, absent, deployable
- Casualty data: WIA, KIA, MIA, non-battle injuries (NBI)
- Strength by unit (TASKORG-aligned)
- Personnel FFIR thresholds (% fill, specialist availability)
- Replacement requisition status

**Specific Tasks on MSS:**
1. Maintain the PERSTAT workspace in MSS. Update on the battle rhythm schedule (minimum: daily, or per standing CCIR threshold events).
2. Cross-reference PERSTAT data against S3 TASKORG to identify strength-to-task gaps by position or specialty.
3. Validate casualty data input to MSS against primary casualty reporting channels (DCIPS, unit casualty reports). MSS displays reported data; primary reporting is authoritative.
4. Monitor personnel FFIR thresholds in the CCIR workspace. Alert S3 when fill percentage or specialist availability crosses the commander-published threshold.
5. Prepare the personnel component of the BUA data product package (S1 PERSTAT slide built from MSS data).
6. Coordinate replacement data with S4 on logistics of personnel movement (reception, staging, onward movement data in MSS).

**CCIR Responsibilities:**
- Owns FFIR entries for personnel fill percentage, casualty thresholds, and critical specialist shortfalls.
- Reports to S3 when personnel FFIR thresholds are triggered. Uses MSS alert notification.
- Coordinates with S2 on POW/detainee data (separate from casualty tracking, but requires S2/S1 coordination per theater policy).

**Cross-Reference to S3 for Task Organization Manpower Data:**
When the S3 builds or modifies the TASKORG in MSS, S1 must validate that strength data aligns with the modified TASKORG. A TASKORG change that creates a new task force without updating S1's strength allocation will produce incorrect PERSTAT data in the MSS COP. S1 and S3 must establish a standing coordination SOP for TASKORG change notification.

> **CAUTION: Personnel data in MSS reflects submitted reports, not ground truth. Casualty figures, strength counts, and fill percentages are only as accurate as the reporting discipline of subordinate units. S1 must establish and enforce reporting standards, and label MSS products with data-as-of timestamps and source validation status.**

---

### 2-4. S4 / G4 Section — Logistics

**MOS:** 90A (AG/QM Officer); 92A (Automated Logistical Specialist), 92Y (Unit Supply Specialist), 92F (POL)
**Positions:** S4, Supply OIC/NCOIC, Maintenance Officer, Property Book Officer

**Role Description.** The S4 section contributes logistics data to the MSS Mission Command picture, specifically the LOGSTAT and readiness data components. S4 data enables the commander to assess sustainability against the operational timeline and identify Class I–IX shortfalls before they become operational constraints (FM 6-0, para 3-14). The S4/S3 data interface is particularly important: S3 cannot accurately assess mission-capable task organization without S4 readiness and sustainability data.

**MSS Data Domain:**
- LOGSTAT (Logistics Status Report): Class I–IX status and days of supply (DOS)
- Maintenance status: deadline equipment, maintenance float, estimated return to full capability (ERFC)
- GCSS-Army integration data: maintenance work orders, parts requisitions, supply status
- Fuel status: Class III bulk and packaged
- Ammunition: Class V status by type and unit
- Transportation: organic and TPFDD lift availability

**Specific Tasks on MSS:**
1. Maintain the LOGSTAT workspace in MSS. Update on the battle rhythm schedule.
2. Build the logistics component of the BUA product package: Class I–IX status by unit, days of supply trends, and maintenance readiness percentage.
3. Cross-reference maintenance deadline data with S3 TASKORG to produce the readiness-to-mission analysis (percent of assigned equipment available for the current or planned mission).
4. Monitor Class III and Class V CCIR thresholds. Alert S3 when fuel or ammunition status crosses the commander-published consumption planning threshold.
5. Maintain GCSS-Army data linkage. Coordinate with S6 on GCSS-Army feed configuration if data is not flowing to MSS correctly.
6. Support logistics synchronization meeting (LOGSYNCH) with MSS-built logistics data products (see paragraph 4-5).

**S4/S3 Coordination on Readiness-to-Mission Linkage:**
The most operationally significant S4/S3 interface on MSS is the readiness-to-mission product. This product answers: "Of the forces in the current TASKORG, what percentage of assigned equipment is available for the planned mission?" This requires S4 deadline data and S3 TASKORG data integrated in a single MSS view. Procedure:

1. S4 provides current deadline list to S3 battle captain, or via MSS shared workspace.
2. S3 cross-references deadline data against TASKORG using the MSS unit status overlay (see paragraph 7-2).
3. Integrated product: mission-capable rate by maneuver unit, presented at BUA and readiness review.

> **CAUTION: GCSS-Army data flowing into MSS is subject to reporting lag and input quality at unit level. If MSS shows significantly different readiness numbers than the S4's internal tracking, investigate the data pipeline before briefing the commander. Coordinate with S6 and C2DAO to identify and resolve feed discrepancies.**

---

### 2-5. S6 / G6 Section — Signal / Communications

**MOS:** 25A (Signal Officer); 25U (Signal Support Systems Specialist), 25Z (Senior Signal Sergeant)
**Positions:** S6, Network OIC, MSS Administrator, Comms NCOIC

**Role Description.** The S6 section is the technical enabler of MSS at unit level. S6 manages network infrastructure, MSS account provisioning, CP connectivity, and PACE planning for MSS. S6 is the first responder when MSS connectivity or access issues occur and the primary coordinator with C2DAO on platform technical matters (FM 6-02, para 2-4). S6 does not own operational data domains, but enables every other section's use of the platform.

**MSS Network Infrastructure — CP Connectivity Requirements:**
MSS operates as a network-enabled enterprise application (FM 6-02, para 3-12). Minimum connectivity requirements by CP type are established in Table 5-1 (see Chapter 5). Key infrastructure requirements:

- NIPR connectivity to MSS tenant (minimum bandwidth: per C2DAO published standards, typically 10 Mbps sustained per active dashboard user)
- SIPR connectivity for classified MSS tenant operations (if applicable per unit authorization)
- Multi-factor authentication (MFA) infrastructure for MSS login
- Local network switch and Wi-Fi configuration for TOC/CP workstations and map board displays

**Account Management and Provisioning:**
S6 owns the MSS access management process at unit level:
1. New user requests: collect user information (name, DOD ID, unit, required role), submit to C2DAO MSS Administrator via the unit access request form.
2. Role assignment: provisioned roles must match the user's operational need (least-privilege principle). Do not assign builder or admin roles to operational staff who only require consumer access.
3. Offboarding: remove or suspend access for personnel who PCS, separate, or no longer require MSS access. Conduct quarterly access audits.
4. Password and MFA issues: provide first-line helpdesk. Escalate unresolved issues to C2DAO.

**CP PACE Planning for MSS (ATP 6-0.5, para 4-12):**
S6 builds PACE (Primary, Alternate, Contingency, Emergency) for MSS as part of the unit communications plan:

- **Primary:** NIPR network via primary tactical communications network to MSS tenant
- **Alternate:** Satellite connectivity (SATCOM) to MSS tenant
- **Contingency:** Standalone MSS data cache / offline data package (coordinate with C2DAO for capability)
- **Emergency:** Manual products / printed backup products per degraded operations SOP (see Chapter 10)

**TAC CP vs. Main CP Network Architecture:**
The TAC CP operates with reduced network infrastructure. MSS display at the TAC CP is a deliberate design decision — not all Main CP MSS products replicate to the TAC CP automatically (see Chapter 5). S6 configures the TAC CP MSS terminal with the Minimal Essential Data Set (MEDS) defined by the S3 (see paragraph 5-3).

**Technical POC — Coordination with C2DAO:**
S6 is the primary interface between the unit and C2DAO for:
- Platform outages and data feed failures
- Access management escalations
- New data integration requests
- Pipeline performance issues
- Security incidents involving MSS data

> **NOTE: S6 is the MSS Administrator at unit level. However, S6 does not own operational data products. When data content errors are identified (wrong TASKORG, missing units, incorrect readiness data), the owning section corrects the data — not S6. S6 resolves the technical access or connectivity issue; the data owner resolves content issues.**

---

### 2-6. S5 / G5 Section — Civil Affairs

**MOS:** 38A (CA Officer); 38B (Civil Affairs Specialist)
**Positions:** S5, CA Team Leader, CA NCO

**Role Description.** The S5 section contributes civil affairs and civil-military operations (CMO) data to the MSS picture. In USAREUR-AF operations, S5 data typically includes host-nation coordination status, civil considerations overlays, and CMO event tracking.

**MSS Data Domain:**
- Civil considerations overlay: population centers, key infrastructure, CMO event locations
- Host-nation coordination tracking: agreements, liaison events, civil liaison officer (CLO) status
- Humanitarian assistance and disaster response (HADR) tracking where applicable
- Civil affairs team (CAT) locations and activity status

**Specific Tasks on MSS:**
1. Maintain civil considerations overlay in the MSS COP layer. Coordinate with S2 for integration with threat analysis.
2. Track CMO events and host-nation coordination milestones in the MSS operational tracking workspace.
3. Provide civil environment data to S3 and S2 for integration into MDMP assessments of civilian impact on operations.

---

### 2-6a. S9 / Civil Affairs Section — Civil Affairs Operations (CA/CMO Integration)

**MOS:** 38A (Civil Affairs Officer), 38B (Civil Affairs Specialist); 41A (Foreign Affairs Officer) at division/corps
**Positions:** S9 (at division and above), S5 (at BCT), CA Team Leader, CMO Coordinator

**Role Description.** The S9 section (Civil Affairs (CA) at division and above; functions performed by S5 at BCT) manages civil affairs operations data and civil-military operations (CMO) integration on MSS. In USAREUR-AF's multinational operating environment, civil considerations — host-nation relationships, key leader engagement (KLE) tracking, and civil effects monitoring — are operationally significant and require dedicated data management (FM 6-0, para 3-16).

**MSS Data Domain:**
- Civil considerations overlay: population centers, key terrain (infrastructure, utilities, LOCs with civilian use)
- Host-nation coordination tracking: agreements, pending requests, liaison officer positions
- Key leader engagement (KLE) tracker: scheduled and completed engagements, outcomes
- Civil affairs team (CAT) locations and activity status
- CMO effects monitoring: civil indicators linked to MOEs (example: civilian movement patterns, infrastructure status)
- Humanitarian assistance and disaster response (HADR) event tracking where applicable

**Specific Tasks on MSS:**
1. Maintain civil considerations overlay in the MSS COP layer. Overlay includes: population centers, critical infrastructure (bridges, power, water), CMO event locations, and civil restriction areas.
2. Track KLE events in the MSS CMO workspace: date, location, participating leaders, outcomes, follow-up requirements.
3. Update host-nation coordination status: pending agreements, active coordination, and liaison officer contacts.
4. Provide civil environment data to S3 and S2 for integration into MDMP assessments of civilian impact on operations. Specifically:
   - Step 2 (Mission Analysis): civilian considerations factored into COG analysis and task organization planning.
   - Step 4 (Wargame): civilian impact at each phase wargamed with S9 data on the synchronization matrix.
   - Step 5 (COA Comparison): COA comparison includes civil effects criterion using S9 data.
5. Monitor civil MOEs linked to the operation's end state. Example: if the operation's end state includes conditions for host-nation stability, S9 provides the civil indicators data for that MOE.
6. Brief civil affairs status at the BUA as required by S3 — typically weekly in garrison, more frequently in operations that have significant civil effects.

**CCIR Responsibilities:**
The S9 does not typically own CCIRs in the traditional PIR/FFIR sense, but contributes civil indicators to MOE monitoring. If the commander identifies a civil situation (example: displacement of civilian population, collapse of municipal services) as a decision-relevant event, S9 loads that indicator into the MSS assessment workspace as an MOE threshold.

**Coordination with S2 and S3:**
- S2: Civil considerations overlay integrates with S2 terrain and threat analysis. Displaced civilian population can indicate enemy movement or pressure. S9 coordinates with S2 on this integration.
- S3: Civil effects are part of the synchronization matrix. S9 coordinates with S3 to ensure CMO events are on the battle rhythm schedule and synchronized with operational timelines.
- SJA: S9 coordinates with SJA on ROE civil protection compliance and law of war civil considerations in targeting.

---

### 2-7. Fires and Effects Coordination Cell (FECC)

**MOS:** 13A (Field Artillery Officer), 13F (Fire Support Specialist), 13B (Cannon Crewmember), 13D (Field Artillery Automated Tactical Data Systems Specialist)
**Positions:** Fires Support Officer (FSO), FSCOORD, Targeting Officer, Fire Support NCO

**Role Description.** The FECC integrates fires and effects data into the Mission Command picture. On MSS, the FECC maintains the fires integration layer, supports the targeting process, and builds fires-related decision support products that support the S3 in synchronizing lethal and non-lethal effects (FM 6-0, para 3-19).

**MSS Data Domain:**
- No-fire areas (NFA) and restricted fire areas (RFA) overlays
- Target nominations and target list management (high-payoff targets (HPT), high-value targets (HVT))
- Fires asset status: FA units, available fires, shells and propellant status
- Targeting cycle status: D3A (Decide, Detect, Deliver, Assess) tracking
- Effects tracking: battle damage assessment (BDA) data

**Fires Integration into Decision Support Products:**
1. Maintain NFA/RFA overlays in MSS COP, updated per OPORD and FRAGO. Coordinate with S2 for threat integration.
2. Build the target list and HPT tracker in MSS for use at the targeting meeting (see paragraph 4-4).
3. Cross-reference fires asset status with S3 synchronization matrix: which fires are available at each decision point?
4. Build BDA data products from post-mission reporting for FSCOORD and S3 assessment.

**Coordination with S3 and S2:**
- S3 directs the targeting process (commander's targeting guidance); FECC executes and tracks.
- S2 provides intelligence support to targeting: confirming HPT locations, verifying BDA.
- FECC briefs fires and effects status at the BUA as a standing agenda item.

---

### 2-8. ADAM/BAE — Air Defense/Airspace Management and Brigade Aviation Element

**MOS:** 14A (Air Defense Artillery Officer), 14P (Air Defense Artillery Operations Assistant), 15A (Aviation Officer)
**Positions:** A2C2 Officer, ADAM NCO, Aviation LNO

**Role Description.** The ADAM/BAE cell manages airspace and aviation coordination in the MSS COP. In USAREUR-AF operations, airspace management is increasingly complex with unmanned aircraft systems (UAS), fires, and aviation operating in the same airspace. MSS provides an integrated airspace picture when properly configured.

**MSS Data Domain:**
- Airspace coordination area (ACA) overlays
- UAS operating area management
- Air defense status: ADA unit locations, engagement zones
- Aviation asset status and flight track data (where integrated)
- Coordinating altitude data

**Specific Tasks on MSS:**
1. Maintain ACA and airspace restriction overlays in the MSS COP layer.
2. Track UAS operating areas and deconfliction status.
3. Monitor air defense status and maintain ADA overlay currency.
4. Provide airspace data to S3 for OPORD airspace annex support.

---

### 2-9. CBRN Officer

**MOS:** 74A (CBRN Officer), 74D (CBRN Specialist)
**Positions:** CBRN Officer, CBRN NCO, CBRN Recon Team Leader

**Role Description.** The CBRN officer maintains CBRN monitoring and incident tracking in MSS. MSS provides the CBRN officer with a platform for tracking contamination areas, decontamination site locations, and CBRN incident reports integrated with the operational picture.

**MSS Data Domain:**
- CBRN incident tracking: confirmed and suspected events, contamination areas
- Decontamination site locations and status
- NBC-1 and NBC-4 report integration
- CBRN sensor overlay (where integrated)
- MOPP status tracking by unit

**Specific Tasks on MSS:**
1. Maintain CBRN incident overlay. Update with confirmed and suspected contamination events.
2. Track decontamination site status and capacity.
3. Input NBC-1/NBC-4 reports to MSS and share with S3 for COP integration.
4. Maintain MOPP status by unit in the MSS COP (coordinate with S1 for personnel-linked MOPP data).

> **WARNING: CBRN contamination data on MSS does not automatically deconflict routes or movement orders. A confirmed contamination event logged in MSS requires immediate coordination with S3 to assess impact on current operations. Do not assume the S3 has seen a new CBRN overlay update — actively brief it.**

---

### 2-10. Staff Judge Advocate (SJA)

**MOS:** 27A (Judge Advocate), 27D (Paralegal Specialist)
**Positions:** Staff Judge Advocate, Legal NCO, Law of War Advisor

**Role Description.** The SJA provides legal support to operations, including law of war compliance data, ROE integration, and detainee operations legal support. On MSS, the SJA accesses targeting data, ROE documentation, and detainee tracking data relevant to legal review functions.

**MSS Data Domain:**
- ROE documentation and version tracking in MSS document management
- Targeting legal review tracking (no-strike list, protected sites overlay)
- Detainee tracking data (coordinate with S2/S1 for data ownership)
- Legal incident reporting for law of war compliance

**Specific Tasks on MSS:**
1. Maintain the no-strike list and protected sites overlay in MSS COP (coordinate with FECC).
2. Document legal review of targeting nominations in the MSS targeting workspace.
3. Track ROE change requests and effective ROE version in MSS document management.

---

### 2-11. Functional Area Officers

**50A — Force Management Officer:**
The Force Management Officer tracks unit structure, manpower authorizations, and force design data. On MSS, 50A accesses organizational data to support structure analysis and MTO&E alignment assessments. Data domain: unit authorization data, structure change documentation, MTOE tracking.

**51A — Engineer Officer:**
The Engineer Officer contributes mobility/counter-mobility and survivability data to the MSS picture. Data domain: obstacle overlays, survivability works tracking, route status (mobility), bridge classification data. Engineer data integrates with the S2 terrain overlay and S3 maneuver planning.

**53A — Information Systems Management Officer (Army Acquisition, Logistics, and Technology):**
The 53A coordinates on information system integration at enterprise level. In the MSS context, the 53A interface is typically at G6 level, addressing enterprise system-of-systems integration, data architecture, and technical standards coordination with C2DAO.

**54A — Information Operations Officer:**
The IO Officer maintains IO integration data in the MSS COP. Data domain: IO event tracking, MISO product coordination, EW deconfliction, OPSEC vulnerability tracking. IO data informs the S3's integration of informational effects with physical operations.

---

### 2-12. Executive Officer (XO) — MSS Governance and Staff Synchronization

**MOS:** All branches (XO is a position, not an MOS)
**Positions:** Battalion XO, Brigade XO, Division or Corps Deputy CofS

**Role Description.** The XO is the principal staff officer responsible for coordinating staff actions and ensuring that all sections function as an integrated team (FM 6-0, para 3-5). In the MSS context, the XO plays a governance role: ensuring that MSS data standards are enforced, that staff sections are maintaining their data domains, and that the commander receives the integrated products the platform is designed to deliver.

**XO MSS Responsibilities:**

1. **Enforce data update standards.** The XO holds sections accountable for maintaining their MSS data on schedule. If the S4 LOGSTAT is stale before the BUA, the XO addresses it — not as a platform problem, but as a staff discipline issue.
2. **Direct battle rhythm synchronization.** The XO reviews the battle rhythm template (Appendix B) and ensures that every recurring event has a designated MSS product and a responsible section. Gaps in the battle rhythm data coverage are a command risk.
3. **Approve MSS product development requests.** Product development requests (Appendix A, para A-4) that require Builder-level development (TM-20) or C2DAO support are routed through the XO for priority setting before submission. The XO balances competing requests and ensures C2DAO bandwidth is used efficiently.
4. **Conduct monthly MSS data quality review.** The XO leads a monthly (or per operational tempo) review of MSS data quality:
   - Are CCIR thresholds current and aligned to the commander's published CCIRs?
   - Are access lists current? Has the S6 conducted the quarterly access audit?
   - Are any data feeds consistently degraded or unreliable?
   - Are there reporting requirements that have been formally eliminated per paragraph 4-8?
5. **Support commander's MSS orientation.** When a new commander arrives, the XO ensures the commander receives an MSS orientation brief from S3 and S6 — covering COP capabilities, CCIR dashboard, and how to read decision support products. The commander does not need to operate MSS, but must be able to interpret what it shows.

> **NOTE: The XO cannot manage MSS governance from the S3 operations cell. The XO needs a workstation with at minimum read access to the CCIR dashboard, the assessment workspace, and staff section update timestamps. The S6 provisions this access as part of initial CP configuration.**

---

## CHAPTER 3 — THE OPERATIONS PROCESS ON MSS

**BLUF:** MSS integrates data into every phase of the operations process — Planning, Preparing, Executing, and Assessing (ADP 5-0, para 1-8). This chapter defines what data MSS provides at each phase and what actions the S3 and staff must take to leverage it. The operations process remains the framework; MSS is the data layer within it.

### 3-1. Operations Process Overview and MSS Integration Points

ADP 5-0 defines the operations process as the major command activities performed during operations: planning, preparing, executing, and assessing (ADP 5-0, para 1-7). Commanders and staffs use the operations process iteratively and continuously to plan operations, prepare for execution, execute, and assess results (ADP 5-0, para 1-8).

MSS integrates at each phase:

- **Planning:** MDMP data support — forces available, intelligence, sustainment estimates, COA analysis products.
- **Preparing:** Pre-execution checks, rehearsal data packages, subordinate synchronization products.
- **Executing:** Battle tracking, current operations management, battle rhythm data products.
- **Assessing:** MOE/MOP monitoring, reporting products, trend analysis for continuous assessment.

The operations process is continuous and overlapping — not sequential. MSS support is also continuous. The battle captain monitoring CCIRs during execution is assessing the operation; the S3 building a branch plan during execution is planning. MSS must support all phases simultaneously.

### 3-2. Planning Support — Full MDMP

FM 5-0 defines MDMP as a seven-step process that integrates the activities of the commander, staff, and subordinate headquarters in planning operations (FM 5-0, para 2-4). Each step has specific MSS data integration tasks.

#### Step 1: Receipt of Mission — Initial Data Pull

**BLUF:** Receipt of mission triggers an immediate MSS data pull to establish the planning baseline.

**Conditions:** Higher HQ has issued a warning order (WARNORD) or mission tasking has been received. MDMP begins.

**Standards:** Within 60 minutes of receipt of mission, the S3 section completes an initial data pull from MSS covering forces available, current readiness status, and the intelligence picture.

**Procedure:**
1. Log into MSS. Navigate to the unit's planning workspace.
2. Pull current PERSTAT from the S1 workspace — record assigned and present-for-duty strength by unit.
3. Pull current LOGSTAT from the S4 workspace — record Class III, V status; days of supply.
4. Pull current maintenance readiness from the S4 workspace — record mission-capable rate by maneuver unit.
5. Pull current threat overlay from S2 workspace — confirm last updated timestamp.
6. Document the data-as-of timestamp for each data element. This becomes the planning baseline.
7. Cross-reference forces available against higher HQ TASKORG in the mission tasking.

> **NOTE: Receipt of mission data pull is a snapshot. Data will change during MDMP. Maintain a clear record of the baseline and update it as the MDMP progresses. Do not allow planning products built on the Step 1 baseline to go stale without updating them.**

#### Step 2: Mission Analysis — Forces Available, Sustainment, Risk

**BLUF:** Mission analysis uses MSS data to quantify the problem — what do we have, against what threat, to accomplish what task, with what logistics?

**Conditions:** Step 1 complete. Commander has issued initial guidance. Mission analysis is underway.

**Standards:** Mission analysis products include MSS-sourced forces available table, current readiness by unit, current logistics status, and S2-provided intelligence summary — all with data-as-of timestamps (FM 5-0, para 2-16).

**Procedure:**
1. Build forces available table from MSS TASKORG and PERSTAT data. Include: unit, assigned strength, present-for-duty, mission-capable equipment percentage.
2. Build sustainment assessment from MSS LOGSTAT data. Answer: can current logistics support sustain the mission for the planned duration? At current consumption rates, when does Class III/V reach critical threshold?
3. Build initial risk assessment using readiness and sustainment data — identify units below threshold that create risk to the operation.
4. Brief S2 intelligence summary: current threat overlay, IPB assessment (terrain, weather effects), enemy COA probability assessment.
5. Compile mission analysis brief product. Each data element includes source (MSS workspace) and data-as-of timestamp.
6. Brief the commander on mission analysis findings. Record the commander's initial guidance and planning guidance for Step 3.

> **NOTE: Mission analysis risk assessment is qualitative assessment supported by quantitative data — not automated. MSS provides the data; the S3 and staff synthesize the assessment. Never present a raw MSS data export as a risk assessment. Synthesize the data into an analytical product.**

#### Step 3: COA Development — Data-Driven Constraints

**BLUF:** COA development uses MSS data to identify constraints, limitations, and risk factors that shape viable courses of action.

**Conditions:** Mission analysis complete. Commander's planning guidance issued. Staff is developing COAs.

**Standards:** Each COA includes data-supported identification of: forces required vs. available, sustainment constraints, timeline feasibility against readiness data (FM 5-0, para 2-29).

**Procedure:**
1. Review forces available data from Step 2 against each COA's force requirements. Flag units below mission-capable threshold.
2. Review logistics data from Step 2 against each COA's sustainment requirements. Identify Class III/V constraints.
3. Review S2 threat overlay for each COA's proposed scheme of maneuver — terrain and threat friction points.
4. Document MSS-sourced data that constrains each COA. These become the "constraints" inputs to the COA briefing.
5. Update forces available data if significant changes occurred since Step 2. Note changes in the planning record.

#### Step 4: COA Analysis/Wargame — Synchronization Data Support

**BLUF:** The wargame uses MSS data to populate the synchronization matrix, assess COA friction points, and identify decision points.

**Conditions:** COAs developed and approved for wargaming. Wargame is being conducted.

**Standards:** Synchronization matrix is MSS-sourced (forces, logistics, fires, intelligence) and captures actions, decision points, and branch triggers by phase (FM 5-0, para 2-35).

**Procedure:**
1. Open the MSS synchronization workspace (or build it if not yet established).
2. Populate the synchronization matrix with TASKORG data (who does what, where, when) from MSS.
3. Integrate fires data (FECC): fires assets available by phase, NFA/RFA overlays at each phase.
4. Integrate logistics data (S4): sustainment events, Class III/V replenishment timelines, maintenance recovery points.
5. Integrate intelligence data (S2): threat positions and COA at each decision point.
6. Identify decision points: specific events, at specific times/locations, requiring commander decision. Load these into the MSS decision point tracker (see paragraph 6-5).
7. Identify branches and sequels: which triggers activate which plans? Load into MSS operational tracking workspace.

#### Step 5: COA Comparison — Quantified Decision Products

**BLUF:** COA comparison uses MSS data to quantify relative advantage and risk across COAs against commander-weighted decision criteria.

**Conditions:** Wargame complete. Staff is comparing COAs against the commander's evaluation criteria.

**Standards:** COA comparison product includes quantified assessment of each COA against criteria — not solely qualitative text. Data elements are sourced from MSS with timestamps (FM 5-0, para 2-42).

**Procedure:**
1. Establish evaluation criteria and criteria weights from the commander's planning guidance.
2. Build a comparison matrix. For each criterion, assign each COA a score based on MSS data.
3. Criteria with MSS data support:
   - **Sustainment:** Days of supply at end-state vs. LOC data. Source: S4 LOGSTAT.
   - **Readiness:** Mission-capable rate at key decision points. Source: S4/S3 maintenance status.
   - **Personnel risk:** Maneuver unit strength at key decision points. Source: S1 PERSTAT, casualty estimates.
   - **Intelligence support:** S2 PIR collection feasibility by COA. Source: S2 collection plan analysis.
4. Present quantified comparison product to the commander with source data visible.
5. Document the comparison rationale in the MSS planning workspace for future reference (branches, sequel triggers).

#### Step 6: COA Approval — Decision Brief Preparation

**BLUF:** The decision brief is the integration product — MSS data assembled into a briefing package that gives the commander what is needed to approve a COA.

**Conditions:** COA comparison complete. Staff prepares decision brief for commander approval.

**Standards:** Decision brief product includes: current readiness status, current intelligence picture, COA comparison product, recommended COA with rationale, and initial risk assessment — all with current data timestamps (FM 5-0, para 2-46).

**Procedure:**
1. Pull updated readiness and logistics data from MSS immediately before the decision brief — do not use Step 2 baseline data if it is more than 12 hours old.
2. Pull current threat overlay from S2. Confirm no significant intelligence updates since the wargame.
3. Assemble decision brief product: current status + COA comparison + recommendation.
4. Brief the commander. Capture the commander's decision and planning guidance in the MSS planning workspace.
5. Publish the approved COA in the MSS planning workspace to enable Step 7 products.

#### Step 7: Orders Production — Data Handoff to Subordinates

**BLUF:** Orders production translates the approved COA into executable orders with MSS data products distributed to subordinate units.

**Conditions:** COA approved. Staff is producing the OPORD.

**Standards:** OPORD is supported by MSS data products that subordinate S3s can access on the platform — TASKORG, fires overlays, logistics paragraph support data, intelligence annexes (FM 5-0, para 2-49).

**Procedure:**
1. Publish the TASKORG in MSS organizational workspace. All subordinate units can see their task organization.
2. Distribute fires overlays: NFA/RFAs and fire support plan data published in MSS COP layer.
3. Distribute logistics support plan data: CSS MSR routes, supply point locations, sustainment schedule in MSS logistics workspace.
4. Confirm subordinate unit S6s have access to the relevant MSS workspaces for their planning use.
5. Archive the MDMP planning record in MSS for branch/sequel reference and lessons learned.

> **NOTE: The OPORD is the authoritative order — not the MSS data package. MSS supports orders production; it does not replace the order. Subordinate units execute the OPORD. MSS provides the data layer that supports execution.**

---

### 3-3. Preparing — Pre-Execution Checks and Rehearsal Data

**BLUF:** The preparation phase uses MSS to validate that forces are ready to execute — readiness validated against the OPORD's requirements.

During the preparation phase, the S3 and staff use MSS to:

1. **Monitor readiness against planning assumptions.** If mission-capable rates drop below the wargame assumptions before execution, the S3 must assess whether a plan change is required.
2. **Support rehearsals.** The synchronization matrix and fires overlays from MSS provide the data layer for rehearsal facilitation. Battle captains should have MSS displays available during rehearsals.
3. **Validate CCIR thresholds.** Confirm that CCIR thresholds loaded in MSS match the commander's published CCIRs for the operation. Update thresholds if planning has refined them.
4. **Confirm subordinate unit data input.** Before execution, subordinate units should have provided initial PERSTAT, LOGSTAT, and reporting data to MSS. Validate that data is current.
5. **Confirm CP configuration.** Verify MSS displays are configured for execution — not planning (see Chapter 5).

### 3-4. Executing — Battle Tracking and Current Operations Management

**BLUF:** During execution, MSS is the current operations platform. Battle captains use it to track the battle, monitor CCIRs, and support the commander's decision-making in the fluid environment of combat operations.

During execution, the S3 section uses MSS for:

1. **Battle tracking:** Unit locations, task completion status, contact reports, and phase line crossings tracked in MSS COP.
2. **CCIR monitoring:** Automated alerts from MSS CCIR workspace. Battle captains monitor the CCIR dashboard continuously during execution.
3. **Decision point monitoring:** As the battle develops, decision points approach. Battle captains monitor MSS decision point tracker against the timeline and ground situation.
4. **Current operations integration:** S1 PERSTAT updates, S4 LOGSTAT updates, S2 intelligence updates, and CBRN reports all flow into MSS. The battle captain integrates these into the current operations picture.
5. **FRAGO development:** When situation changes require FRAGO, the S3 pulls current status from MSS for the update package.

> **CAUTION: During execution, data update frequency is high and data quality can degrade. Battle captains must distinguish between confirmed event data and unverified contacts or reports in the MSS COP. Label unverified data as such. Brief the commander on data confidence levels, not just raw data.**

### 3-5. Assessing — MOE/MOP Framework on MSS

**BLUF:** Continuous assessment (ADP 5-0, para 1-9) requires systematic monitoring of mission progress. MSS provides the MOE and MOP data layer that makes assessment quantitative, not just intuitive.

FM 5-0 defines two types of measures (FM 5-0, para 4-10):

- **Measures of Performance (MOPs):** Tasks performed correctly. "Did we do what we planned to do?" (e.g., Did the battalion clear Objective IRON on time? Did Class III resupply occur at PL VIKING?)
- **Measures of Effectiveness (MOEs):** Effects achieved. "Is our action creating the desired effect?" (e.g., Has route security improved in Sector 3? Has enemy activity decreased by D+5?)

**Building the MOE/MOP Framework in MSS:**

1. Identify MOPs and MOEs from the OPORD, CONOPS, and commander's assessment plan during MDMP.
2. Load MOPs and MOEs as trackable items in the MSS assessment workspace, linked to the relevant data sources.
3. Set thresholds: what value indicates the MOP is achieved? What MOE value indicates the effect is achieved?
4. Assign data owners: which staff section provides the data for each MOP/MOE?
5. Establish update frequency: MOPs update on the battle rhythm reporting schedule; MOEs may update less frequently.
6. Review at each BUA: brief the commander on current MOE/MOP status and trend (not just current snapshot).

**Table 3-1. Example MOE/MOP Framework**

| Indicator | Type | Data Source | Threshold | Owner |
|---|---|---|---|---|
| % of phase line crossings on schedule | MOP | S3 tracking | >80% on time = satisfactory | S3 |
| Mission-capable rate at execution D-Day | MOP | S4/S3 | >85% MC for assigned maneuver units | S4 |
| Sustainment sorties completed vs. planned | MOP | S4 | >90% completion rate | S4 |
| Enemy contact rate (engagements/day) | MOE | S2/S3 | Decreasing trend D+3 to D+7 = favorable | S2 |
| Route security incidents per 24hr | MOE | S2 | <3 incidents/day by D+5 = favorable | S2 |
| Personnel fill rate (combat-capable) | MOE | S1 | >80% fill through D+14 = sustainable | S1 |

---

## CHAPTER 4 — BATTLE RHYTHM MANAGEMENT

**BLUF:** The battle rhythm is a deliberate cycle of activities within a headquarters that synchronizes the decision-making cycle (FM 6-0, para 4-8). MSS transforms the battle rhythm by replacing ad hoc slide assembly with pre-built data products, reducing preparation time and increasing decision quality. This chapter defines how to design and manage an MSS-enabled battle rhythm.

### 4-1. Battle Rhythm Design Principles

FM 6-0 establishes battle rhythm as commander-directed. The battle rhythm must support the operations process, not compete with it (FM 6-0, para 4-8). Core principles for an MSS-enabled battle rhythm:

1. **Every recurring event has a designated MSS product.** If a meeting requires data, that data comes from a pre-built MSS product — not from slides assembled by an individual staff officer in the two hours before the meeting.
2. **Data products are maintained continuously, not built before meetings.** MSS products for the BUA are valid because sections maintain their data continuously, not because someone updated them the morning of the BUA.
3. **Battle rhythm events drive data update frequency.** The schedule of MSS data updates (PERSTAT, LOGSTAT, threat overlay) is derived from the battle rhythm — which meeting needs the data, and how current must it be?
4. **Eliminate reporting redundancy.** If subordinate units report data that flows directly into MSS, the command should not also require those units to submit separate slides or spreadsheets with the same data (see paragraph 4-8).

### 4-2. Mapping Battle Rhythm Events to MSS Data Products

**Table 4-1. Battle Rhythm Event to MSS Data Product Mapping**

| Battle Rhythm Event | Frequency | MSS Data Products Required | Data Owners | Data Freshness Requirement |
|---|---|---|---|---|
| Battle Update Assessment (BUA) | Daily (or per unit SOP) | COP snapshot, PERSTAT, LOGSTAT, intelligence summary, CCIR status, decision point status | S1, S2, S3, S4 | All data <4 hours old |
| Targeting Meeting | Per targeting cycle (typically daily) | Target list, HPT status, BDA, fires assets available, NFA/RFAs | FECC, S2, S3 | All data <2 hours old |
| Logistics Synchronization | Daily/48-hr cycle | Class I–IX status, maintenance status, transportation plan, supply priorities | S4, S3 | All data <8 hours old |
| Readiness Review | Weekly / monthly | C-rating trend (30-day), equipment deadline trend, training readiness status | S3, S4, S1 | All data <24 hours old |
| Intelligence Synchronization | Per unit SOP | PIR status, collection plan update, INTSUM, threat overlay | S2, S3 | All data <4 hours old |
| Commander's Update Brief (CUB) | Weekly | Decision product package: readiness trend, mission progress MOE/MOP, logistics forecast | S3, S2, S4, S1 | All data <24 hours old |
| Rehearsal Support | Per operation | Synchronization matrix, fires overlays, logistics plan, route overlays | S3, FECC, S4, S2 | All data <4 hours old |
| After-Action Review (AAR) | Post-mission | AAR data package: MOE/MOP results, incident timeline, unit performance data | S3, S2, S4, S1 | Complete and validated |

### 4-3. Battle Update Assessment — Data Preparation Standard

**BLUF:** The BUA is the primary recurring event at which the commander assesses current status against the operation. MSS products for the BUA must meet a defined standard — not just be available, but be current, validated, and in the prescribed format.

**Conditions:** S3 section prepares BUA data package. BUA is scheduled. All staff sections are required to have their MSS data current.

**Standards:** BUA data package contains, at minimum: current PERSTAT (S1), current LOGSTAT (S4), current threat overlay (S2), current CCIR status (S3), and current COP screenshot — all with data-as-of timestamps less than four hours old unless mission constraints prevent it.

**BUA Data Preparation Checklist (abbreviated — full checklist in Appendix A):**

1. **T-60 min before BUA:** Battle captain checks all MSS data timestamps. Notifies sections with stale data.
2. **T-45 min before BUA:** Sections update their MSS data (PERSTAT, LOGSTAT, threat overlay).
3. **T-30 min before BUA:** Battle captain validates all data refreshed and timestamps current.
4. **T-15 min before BUA:** S3 reviews CCIR status. No new CCIR triggers since last BUA? Confirm with CCIR dashboard.
5. **T-5 min before BUA:** Pull final COP screenshot for opening slide. Confirm last updated timestamp visible.
6. **During BUA:** Lead with COP current picture. Sequence: S2 threat, S3 operations, S1 personnel, S4 logistics, fires, CCIR status, decision points.

### 4-4. Targeting Meetings — Intel/Fires/Operations Data Integration

**BLUF:** The targeting meeting synchronizes lethal and non-lethal effects with the operational timeline. MSS provides the integrated data product that replaces disparate slide builds from S2, FECC, and S3.

The targeting meeting data package includes:

1. **Target list (FECC):** Current HPT/HVT list from MSS fires workspace. Include: target name/ID, grid, method of engagement, status (nominated, approved, engaged, BDA pending, BDA complete).
2. **Fires assets available (FECC):** Current fires status — available systems, ammunition status, priority of fires.
3. **Intelligence support (S2):** Current confirmation of target locations. PIR collection supporting targeting. BDA assessment for previously engaged targets.
4. **Restrictions (FECC/SJA):** Current NFA/RFA overlays. No-strike list. ROE constraint summary (not the full ROE document).
5. **Operations synchronization (S3):** Which targets are within the current OPORD targeting authority? Which require FRAGO or higher approval?

Targeting meeting chair is the FSCOORD or S3 per unit SOP. MSS displays should be available in the targeting meeting room, displaying the current target list and fires overlays simultaneously.

### 4-5. Logistics Synchronization — S4/S3 Data Coordination

**BLUF:** The logistics synchronization meeting connects sustainment status to the operational timeline. MSS enables real-time visibility of Class I–IX status and maintenance data that replaces phone reports and disconnected spreadsheets.

LOGSYNCH data package (S4 prepares, S3 reviews for operational impact):

1. **Class I (Water/Rations):** Current days of supply (DOS) by supported unit. Consumption rate vs. planned rate.
2. **Class III (Fuel):** Current gallons on hand. DOS at current consumption rate. Next resupply date.
3. **Class V (Ammunition):** Current basic load percentage. Expenditure rate vs. planned. Next resupply date.
4. **Class IX (Repair Parts):** Critical shortage list. Deadline parts on order — estimated delivery.
5. **Maintenance Status:** Deadlines by unit. Estimated return-to-full-capability (ERFC) for top-10 deadline items.
6. **GCSS-Army alignment:** Confirm MSS logistics data aligns with GCSS-Army records. Flag discrepancies.

**S4/S3 Coordination Point:** S3 reviews logistics data against the operational timeline — specifically: do current logistics shortfalls create operational risk within the planned window? If yes, identify and brief the risk to the commander at the BUA.

### 4-6. Readiness Reviews — 30-Day Trend Products

**BLUF:** The readiness review uses MSS trend data to give the commander a forward-looking readiness picture — not just today's status, but where readiness is heading.

A 30-day readiness trend product includes:

1. **C-rating trend (S3):** Unit C-ratings over the past 30 days, displayed as time-series trend. Are C-ratings improving, declining, or stable?
2. **Deadline equipment trend (S4):** Number of deadline vehicles/systems by type over 30 days. Which end items are consistently going down?
3. **Personnel fill trend (S1):** Fill percentage over 30 days. Is strength increasing (replacements arriving), declining (no replacements, casualties), or flat?
4. **Training readiness (S3 with TM officer):** Critical task training completion rates. Which units are below-threshold on collective training tasks?

These products are available in MSS if data has been consistently reported. The 30-day trend requires 30 days of consistent reporting. If units have not been reporting consistently, the trend product will be incomplete — address reporting discipline as a precondition for the readiness review product.

### 4-7. Commander's Update Brief — Decision Product Standards

**BLUF:** The CUB (or equivalent weekly commander brief) is the primary venue for decision products — not just status. MSS enables the shift from status-briefing to decision-briefing.

CUB product standards (FM 6-0, para 4-12):

1. **Current operations assessment:** MOE/MOP status (see paragraph 3-5). Are we on track? What does the data show?
2. **Readiness projection:** 30-day trend. Where is the formation headed? What decisions are needed to reverse negative trends?
3. **Logistics forecast:** Days-of-supply projection. When does the formation cross critical thresholds? What is the resupply plan?
4. **Intelligence update:** PIR status, threat changes since last CUB. Assessment of threat COA probability.
5. **Decision points:** Which decision points are approaching? What decision is required, and what is the recommended course of action?
6. **Upcoming requirements:** Next 30 days — major operations, reporting requirements, exercises, inspections.

**Decision Product Format Standard:** Each recommendation to the commander includes: current data, trend, threshold, and recommended decision. Format: "Data shows [X]. Trend is [direction]. At current rate, we reach critical threshold [date]. Recommended action: [action]. Commander's decision: [blank for commander to complete]."

### 4-8. Eliminating Redundant Subordinate Reporting

**BLUF:** If subordinate units report data that flows directly into MSS, the command headquarters should not simultaneously require those units to submit separate reports with the same data. Redundant reporting burns subordinate staff time and introduces data consistency errors.

Procedure for reporting redundancy elimination:

1. **Audit current reporting requirements.** List every report subordinate units submit to the command: PERSTAT, LOGSTAT, SALUTE/SPOT, contact reports, readiness reports, etc.
2. **Identify MSS data coverage.** For each report, determine: does this data flow into MSS? Is it visible on the platform at the required frequency and fidelity?
3. **Eliminate redundant requirements.** Where MSS data fully covers a reporting requirement, eliminate the separate report and brief the commander accordingly.
4. **Modify partial-coverage requirements.** Where MSS partially covers a requirement, modify the report to capture only the data elements not on MSS.
5. **Publish and enforce.** Issue a FRAGO or SOP update formalizing the new reporting requirements. Track compliance.

> **NOTE: Reporting redundancy elimination is a command decision, not a staff action. The S3 recommends the changes; the commander approves them. Brief the commander on which reports are being eliminated and what MSS products replace them.**

---

## CHAPTER 5 — COMMAND POST OPERATIONS AND MSS CONFIGURATION

**BLUF:** CP type (Main, TAC, Alt, Jump) determines what MSS capability is available, what displays are configured, and what data the battle captain can access. This chapter defines configuration standards for each CP type and displacement procedures (ATP 6-0.5).

### 5-1. CP Echelon Data Requirements — Main, TAC, Alt, Assault CPs

ATP 6-0.5 defines four CP types based on capability, size, and mission (ATP 6-0.5, para 2-4):

- **Main CP:** Full staff, full capability, primary command and control node.
- **TAC CP:** Mobile, reduced-staff CP for forward operations. Commander forward.
- **Alt CP:** Alternate Main CP. Assumes Main CP functions if Main CP is degraded.
- **Jump CP:** Minimal, fast-moving. Commander and essential staff only.

**Table 5-1. MSS Capability Requirements by CP Type**

| CP Type | MSS Capability | Minimum Network | Display Configuration | Data Freshness Requirement |
|---|---|---|---|---|
| Main CP | Full — all workspaces, all displays, all staff section access | 10 Mbps sustained | Full COP, all staff section dashboards, CCIR monitoring | Real-time, <4 hours for BUA products |
| TAC CP | Minimal Essential Data Set (MEDS) — COP, CCIR alerts, current operations | 2 Mbps sustained | COP display, CCIR dashboard, current ops | <2 hours |
| Alt CP | Full — mirror of Main CP configuration | 10 Mbps sustained | Full COP, all staff section dashboards, CCIR monitoring | Real-time, <4 hours for BUA products |
| Jump CP | COP read-only, CCIR alerts only | 1 Mbps (minimum) | COP display only | <4 hours |

### 5-2. Main CP MSS Display Configuration

The Main CP is the primary MSS operating environment. Display configuration is S3-directed; S6 implements. Standard Main CP MSS display configuration:

**Battle Captain Workstation:**
- Left monitor: COP display (full view — all data layers active per current operational display SOP)
- Center monitor: CCIR monitoring dashboard (persistent, always visible during operations)
- Right monitor: Current task — SITREP preparation, MDMP product, decision brief assembly

**Operations NCO Workstation:**
- Primary monitor: Current operations tracking — task status, phase line crossings, contact tracking
- Secondary monitor: S4 LOGSTAT dashboard (logistics sustainability monitoring)

**S2 Workstation:**
- Primary monitor: Threat overlay and intelligence dashboard
- Secondary monitor: PIR status and collection plan

**Map Board Display (large format):**
- COP full display — unit locations, threat overlay, fires graphics, all current operational overlays
- Refresh: automated (confirm S6 has set auto-refresh interval per unit SOP)

**Table 5-2. Main CP Display Configuration Summary**

| Display Location | Primary Application | Secondary Application | Refresh Interval |
|---|---|---|---|
| Battle Captain — Left | COP (all layers) | — | Auto, 5 min |
| Battle Captain — Center | CCIR Dashboard | Decision Point Tracker | Auto, 1 min |
| Battle Captain — Right | Current Task | — | Manual |
| Ops NCO | Current Ops Tracker | LOGSTAT Dashboard | Auto, 10 min |
| S2 Position | Threat Overlay | PIR Status | Auto, 5 min |
| Map Board | COP (display mode) | — | Auto, 5 min |

### 5-3. TAC CP — Minimal Essential Data Set

**BLUF:** The TAC CP operates with reduced displays and reduced connectivity. The Minimal Essential Data Set (MEDS) defines what MSS capability is essential for the commander at the TAC CP.

**MEDS Definition — Established by S3, approved by Commander:**

1. **COP Display:** Current unit positions, threat overlay, fires graphics (read-only). Essential: commander must see the current picture.
2. **CCIR Dashboard:** Current CCIR status, any triggered alerts. Essential: commander must know when CCIRs are triggered.
3. **Current Ops Tracker:** Task status, contact log, phase line status. Essential: commander must track mission execution.
4. **Communications:** MSS connectivity to Main CP for data pull/push. Essential: TAC CP must be able to update data and receive Main CP updates.

**What is NOT in the TAC CP MEDS:**
- S1 PERSTAT workspace (managed at Main CP; summary data available via COP)
- S4 detailed LOGSTAT workspace (LOGSYNCH at Main CP; critical shortfall alerts available via CCIR)
- Planning workspace (MDMP at Main CP)
- Targeting workspace (managed at Main CP/FECC; fires summary available via COP)

> **NOTE: The MEDS is commander-directed. If the commander determines that a specific data element is essential at the TAC CP, it is added to the MEDS. The default MEDS defined above is a starting point — not a rigid constraint. Coordinate MEDS changes with S6 to ensure network bandwidth supports the additional display requirement.**

### 5-4. Alt CP — Continuity Configuration

**BLUF:** The Alt CP must be able to assume Main CP functions immediately upon Main CP degradation. MSS configuration at the Alt CP mirrors the Main CP.

Alt CP configuration requirements:

1. **Mirror Main CP display configuration.** All workspaces accessible at the Alt CP. All staff section access provisioned for Alt CP personnel.
2. **Validate quarterly.** S6 conducts quarterly validation drill: disconnect Main CP from MSS, verify Alt CP can access all required workspaces within 15 minutes.
3. **Data state synchronization.** Because MSS is a cloud-hosted enterprise platform, the Alt CP accesses the same data state as the Main CP. There is no separate data synchronization required — connectivity is the critical factor.
4. **Document Alt CP connectivity configuration.** S6 maintains a written PACE plan for Alt CP MSS connectivity, tested and current.

### 5-5. CP Displacement — Network Continuity and Data Handoff Procedures

**BLUF:** CP displacement creates a period of network connectivity gap for MSS. The S6 manages the displacement sequence to minimize the COP gap. The S3 manages the operational data state before and after displacement.

**Procedure — Pre-Displacement:**
1. **T-6 hours before displacement:** S3 conducts a full data save — capture current COP screenshot, print key data products (CCIR status, current ops tracker, TASKORG). This is the manual backup if MSS connectivity is lost during displacement.
2. **T-4 hours before displacement:** S6 confirms receiving site connectivity. MSS is accessible at the new CP location before the old CP comes down.
3. **T-2 hours before displacement:** Sections complete data updates. PERSTAT, LOGSTAT, threat overlay all refreshed. Data currency confirmed.
4. **T-1 hour before displacement:** S3 publishes current COP picture to subordinate units via MSS (push notification or workspace update).

**Procedure — Displacement:**
1. TAC CP (if separate) assumes current operations monitoring during displacement.
2. Main CP brings down non-essential MSS workstations in sequence. Battle captain workstation and CCIR monitoring remain active until final takedown.
3. MSS connectivity confirmed at new site before final takedown at old site.

**Procedure — Post-Displacement:**
1. Restore all MSS displays in new CP configuration.
2. Validate data currency — have any data feeds missed updates during displacement? S6 checks pipeline status.
3. Pull current data from all sections. Confirm COP accuracy before resuming battle rhythm.
4. Notify Main CP MSS users via MSS notification: "Displacement complete. CP operational. COP current as of [timestamp]."

### 5-6. Operations Center Display Management

The operations center (TOC) is the physical environment where MSS displays live. S3 directs display content; S6 maintains the physical infrastructure.

**Display content management:**
- The battle captain owns TOC display content and layout.
- Any change to a TOC display (data layer added/removed, new product displayed) requires battle captain authorization.
- Operations NCO maintains the display during watch transitions — handoff includes current COP picture, CCIR status, and any active incidents or pending reports.
- Classified displays: if MSS operates at a classified level, physical security applies to display placement. Coordinate with unit security manager.

> **CAUTION: TOC MSS displays are visible to all personnel in the TOC, including visitors. Before conducting briefings or admitting visitors, verify that displayed data is appropriate for the visitor's clearance level and need-to-know. Do not allow MSS displays to remain active on classified tenants when uncleared personnel are in the TOC.**

### 5-7. Watch Officer / Shift Transition Procedures

**BLUF:** Shift transitions are a high-risk period for MSS data continuity and situational awareness. An incomplete or rushed transition can leave the incoming battle captain without accurate COP data, unresolved CCIR alerts, or incomplete knowledge of current operations status. A standard MSS-enabled transition procedure reduces this risk.

**Conditions:** Battle captain shift transition is occurring. Operations are ongoing or standby posture is in effect.

**Standards:** Incoming battle captain is fully briefed on current COP status, CCIR status, open incidents, pending reports, and any outstanding MSS data issues within 15 minutes of assuming the watch. Both outgoing and incoming battle captains sign the shift transition log.

**Procedure — Outgoing Battle Captain:**
1. **T-30 min before transition:** Begin the shift transition brief preparation.
   - Pull current COP screenshot. Note data freshness for each layer.
   - Review CCIR dashboard: any unresolved alerts? Any near-threshold indicators?
   - Review current operations tracker: any open incidents? Any pending SPOTREPs?
   - Review pending reporting obligations: what reports are due in the next 4 hours?
   - Review MSS pipeline status: any data feeds degraded?
2. **T-15 min before transition:** Brief incoming battle captain on:
   - Current COP picture: unit dispositions, contact reports since last BUA, changes to threat overlay.
   - CCIR status: any near-threshold indicators, any triggered CCIRs awaiting resolution.
   - Open incidents: current contacts, ongoing missions, in-progress reports.
   - Upcoming reporting: what is due, to whom, by when.
   - MSS status: any data feeds degraded, any platform issues S6 is working.
   - Commander's priorities: any specific monitoring tasks the S3 directed for this watch period.
3. **Transition:** Both battle captains confirm the brief is complete. Incoming signs onto the watch log in MSS (or physical log per unit SOP). Outgoing is relieved.

**Procedure — Incoming Battle Captain:**
1. Confirm CCIR dashboard is displayed and active.
2. Verify COP data freshness for all active layers — check each layer's timestamp.
3. Verify no unacknowledged CCIR alerts in the dashboard.
4. Confirm the next reporting deadline and begin preparation per the battle rhythm schedule.
5. If any data layer is stale, immediately notify the owning section to update.

**MSS Watch Log:**
Maintain a watch log in the MSS current operations workspace (or physical log if MSS is degraded). Watch log entries include:
- Time of transition (DTG)
- Outgoing battle captain name and rank
- Incoming battle captain name and rank
- Summary of significant events during the watch
- Outstanding actions at time of transition
- MSS status at time of transition (all feeds operational / identified degradations)

> **NOTE: The watch transition is a command function, not just an administrative handoff. The S3 or XO should periodically observe watch transitions to validate that the standard is being met. A degraded transition standard is a readiness risk.**

---

## CHAPTER 6 — CCIR AND DECISION SUPPORT MANAGEMENT

**BLUF:** CCIRs are the commander's most important information requirements — specifically, information that affects decisions. MSS automates CCIR monitoring and alert generation, but does not replace commander judgment on what constitutes a decision-relevant threshold. The S3 owns the CCIR process; every staff section has CCIR responsibilities (FM 6-0, para 2-17).

### 6-1. CCIR Framework — PIR, FFIR, EEFI

FM 6-0 defines three components of CCIRs (FM 6-0, para 2-17):

- **Priority Intelligence Requirements (PIRs):** Information about the enemy or environment that the commander needs to make decisions. PIR = "What do I need to know about the enemy?"
- **Friendly Force Information Requirements (FFIRs):** Information about friendly forces that the commander needs. FFIR = "What do I need to know about my own forces?"
- **Essential Elements of Friendly Information (EEFIs):** Critical friendly information that must be protected from enemy collection. EEFI = "What must the enemy NOT learn about us?"

MSS supports PIR and FFIR monitoring. EEFIs are addressed through OPSEC measures, not MSS alerts.

**PIR characteristics (for loading in MSS):**
- Tied to a specific decision (not just general intelligence interest)
- Observable and reportable (MSS data can support confirmation or denial)
- Time-limited (associated with a specific phase or decision point)

**FFIR characteristics (for loading in MSS):**
- Specific threshold (not vague — "personnel readiness falls below 80% fill" not "personnel readiness decreases")
- Associated with a decision (what decision does this threshold trigger?)
- Measurable from MSS data (the data element must exist on the platform)

### 6-2. Loading and Managing CCIRs in MSS

**Conditions:** Commander has published CCIRs. S3 is responsible for loading CCIRs into the MSS CCIR management workspace.

**Standards:** All commander-published CCIRs loaded in MSS within 12 hours of publication. Each CCIR entry includes: description, threshold (quantified), data source (MSS workspace), associated decision, and alert notification routing.

**Procedure — Loading a CCIR in MSS:**
1. Navigate to the CCIR Management workspace in MSS.
2. Select "New CCIR" and choose type: PIR or FFIR.
3. Enter CCIR description. Use the commander's published language — do not paraphrase.
4. Enter threshold value (numeric). Example: "Personnel fill drops below 75% at BN level."
5. Link to data source: select the MSS dataset or workspace that provides the threshold data (e.g., S1 PERSTAT workspace).
6. Set alert routing: who receives the MSS notification when threshold is crossed? (Battle captain, S3, XO — per unit SOP.)
7. Set alert sensitivity: immediate (real-time monitoring) or periodic (checked at defined intervals).
8. Associate with decision: what decision does this CCIR support? Record the commander's decision criteria.
9. Save. Confirm the CCIR appears in the CCIR monitoring dashboard.

**Procedure — Modifying a CCIR in MSS:**
1. Open the CCIR entry in the CCIR Management workspace.
2. Edit the threshold, data source, or routing as required.
3. Document the reason for the change in the CCIR record notes field.
4. Notify affected sections of the CCIR modification via MSS notification.
5. Archive the old threshold value in the CCIR history record.

**Procedure — Archiving a CCIR in MSS:**
1. When a CCIR expires (phase complete, decision made, operation concluded) — archive, do not delete.
2. Open the CCIR entry and change status to "Archived."
3. Add an archive note: why is this CCIR no longer active?
4. CCIRs remain searchable in archive for lessons learned and planning reference.

### 6-3. FFIR Monitoring — Readiness, Personnel, Logistics CCIRs

**BLUF:** FFIRs monitor the commander's own forces. Three primary FFIR categories are supported by MSS data: readiness (S4), personnel (S1), and logistics (S4).

**Readiness FFIRs (S4 data source — maintenance status workspace):**
- Equipment mission-capable rate by unit drops below threshold (commander sets threshold by unit type)
- Specific critical system (example: aviation or bridging assets) deadline exceeds defined number
- Maintenance float exceeds X% of organic equipment

**Personnel FFIRs (S1 data source — PERSTAT workspace):**
- Personnel fill rate by unit drops below threshold
- Casualty rate exceeds threshold (total or by category: KIA, WIA)
- Critical specialist (MOS-specific) availability drops below minimum

**Logistics FFIRs (S4 data source — LOGSTAT workspace):**
- Days of supply for Class III drops below threshold
- Days of supply for Class V drops below threshold
- Transportation lift availability drops below requirement for sustainment plan

**FFIR Monitoring Procedure during Operations:**
1. Battle captain checks CCIR dashboard at defined intervals (minimum: each watch transition, typically hourly).
2. If MSS CCIR alert fires: battle captain validates the alert against the primary data source (call to section, not just MSS display).
3. If alert validated: battle captain briefs the commander immediately — do not wait for the BUA.
4. Commander's decision is recorded in MSS CCIR record: what action was taken?
5. If alert is a false positive (MSS data incorrect): battle captain corrects the data issue and documents the discrepancy.

### 6-4. PIR Support — Intelligence Data Integration

**BLUF:** PIRs require intelligence data that may come from multiple sources. MSS integrates those sources into a single PIR monitoring framework. S2 owns PIR entries; S3 coordinates on decision linkage.

**PIR monitoring procedure:**
1. S2 loads PIR in MSS CCIR workspace (see paragraph 6-2 procedure).
2. S2 links the PIR to the intelligence data feed or workspace that provides collection data.
3. S2 monitors PIR status continuously. MSS displays current collection results against PIR criteria.
4. When PIR threshold is met (confirmed or denied): S2 triggers PIR report to S3. MSS notification fires to alert routing list.
5. S3 receives PIR report. Assesses whether the associated decision is now required.
6. Commander is briefed. Decision is recorded.

**PIR denial:** If collection confirms that the PIR cannot be answered (enemy activity obscured, collection asset denied), this is also reportable. S2 logs the PIR denial in MSS with the denial reason and re-tasks collection.

### 6-5. Decision Point Identification and Tracking

**BLUF:** Decision points are specific events, at specific times or locations, that require a commander decision. MSS tracks decision points and provides the status data that informs the decision (FM 5-0, para 2-35).

**Loading a Decision Point in MSS:**
1. Navigate to the Decision Point tracker in the MSS operations workspace.
2. Create a new decision point entry: name, description, geographic trigger (if applicable), time trigger (if applicable), associated CCIR(s), and available COAs.
3. Assign a decision point owner (staff section responsible for monitoring trigger conditions).
4. Set decision due time: when must the commander decide? What is the latest time (LTIOV) for the decision?
5. Link associated CCIRs: which CCIRs, when triggered, advance this decision point?
6. Save. Decision point appears in the decision point monitoring dashboard.

**Decision Point Monitoring during Operations:**
1. Battle captain monitors the decision point tracker continuously.
2. As trigger conditions approach (geographic phase line, time, CCIR trigger), battle captain alerts S3.
3. S3 prepares decision brief product (see paragraph 6-6).
4. Commander makes decision. Decision is recorded in MSS decision point record.

### 6-6. Decision Brief Products — Format and Standards

A decision brief product answers three questions: What is the situation? What are the options? What does the staff recommend?

**Decision Brief Product Format (MSS-supported):**

1. **Situation (MSS-sourced data):** Current COP screenshot with relevant data layers active. CCIR status. Current readiness and logistics summary. Decision point trigger status.
2. **Options:** COA 1, COA 2 (from MDMP wargame record if applicable). For each option: key advantages, key risks, data-supported assessment.
3. **Recommendation:** Staff recommendation with supporting data rationale. Data elements cited by source and timestamp.
4. **Decision Required:** One clear decision statement. Space for commander to record the decision.

**Time standard:** Decision brief products should be preparable within 30 minutes of a decision point trigger, using pre-positioned MSS data products. If it takes longer than 30 minutes to prepare a decision brief, the staff is not maintaining MSS products proactively enough.

---

## CHAPTER 7 — COMMON OPERATING PICTURE AND SITUATIONAL AWARENESS

**BLUF:** The Common Operating Picture (COP) is the shared display of relevant information within a command — the operational picture that enables shared understanding (ADP 6-0, para 2-8). MSS provides the data layer behind the COP, integrating data streams from every staff section into a coherent operational display (FM 6-02, para 3-8).

### 7-1. COP Architecture — Traditional C2 Systems and MSS Data Layer

The USAREUR-AF COP combines traditional C2 system data (CPOF, FBCB2/Blue Force Tracker, ABCS) with MSS data layers. These are complementary, not competing:

- **Traditional C2 systems:** Near-real-time position data (vehicle GPS/BFT tracks), digital radio reports, mission command network data.
- **MSS data layer:** Readiness data, personnel data, logistics data, analytical products, CCIR monitoring, historical trend data, decision support products.

The COP integrated with MSS is richer than either system alone. A battle captain who can see unit tracks (CPOF) alongside mission-capable rates (MSS) has a materially better operational picture than one who sees only position data.

**COP data layer architecture in MSS:**
- **Layer 1 (Base):** Terrain — map imagery, elevation data, terrain features.
- **Layer 2:** BLUFOR disposition — friendly units, TASKORG overlay, phase lines.
- **Layer 3:** OPFOR/Threat — enemy known and templated positions (S2-owned).
- **Layer 4:** Unit Status — readiness and personnel data overlay (S3/S4/S1-owned).
- **Layer 5:** Logistics — supply routes, supply point locations, Class III/V status overlay (S4-owned).
- **Layer 6:** Fires Graphics — NFA/RFAs, fire support plans, target overlays (FECC-owned).
- **Layer 7:** Special overlays — CBRN, airspace, civil affairs (section-owned).

The battle captain controls which layers are visible at any given time. Not all layers are displayed simultaneously — layer management is part of the battle captain's COP management function.

### 7-2. Unit Status Overlay — Readiness and Personnel Data

**BLUF:** The unit status overlay integrates S4 readiness data and S1 personnel data into a geographic display — showing not just where units are, but what their status is.

**Unit Status Overlay Construction:**
1. Navigate to the Unit Status Layer in MSS COP workspace.
2. The overlay defaults to displaying unit icons at TASKORG-mapped locations.
3. Toggle "Status Layer" to display unit status indicators:
   - **Green:** Unit above mission-capable threshold (commander-defined).
   - **Amber:** Unit at marginal status — approaching threshold.
   - **Red:** Unit below threshold — requires commander decision.
4. Click any unit icon to expand the unit status summary: personnel fill %, equipment MC rate, current mission status.

**Data Sources for Unit Status Overlay:**
- Personnel data: S1 PERSTAT workspace (must be current)
- Equipment readiness: S4 maintenance status workspace (must be current)
- Current mission: S3 current operations tracker

**Data currency requirement:** Unit status overlay is only as reliable as the underlying data. If S1 has not updated PERSTAT, the status overlay will reflect outdated data. Data freshness indicators are visible on the overlay — a grayed-out unit icon indicates data is older than the configured staleness threshold.

### 7-3. Logistics Status Layer — Supply and Maintenance Data

**BLUF:** The logistics status layer shows the sustainability picture — where supply points are, what status they carry, and which units are approaching critical thresholds.

**Logistics Status Layer Contents:**
1. **Supply point locations:** Class I/III/V supply points marked on the COP with current stock levels.
2. **MSR status:** Main supply routes — green (open), amber (restricted), red (closed/interdicted).
3. **Unit DOS indicators:** Days of supply by unit, color-coded against commander thresholds.
4. **MEDEVAC route status:** Medical evacuation routes and MEDEVAC asset locations (coordinate with supporting medical unit).

**Building the Logistics Status Layer (S4 responsibility):**
1. Enter supply point locations in the MSS logistics workspace.
2. Update DOS values for each supported unit on the battle rhythm schedule.
3. Flag MSR status changes immediately (not on the scheduled update cycle).
4. Coordinate with S2 on MSR interdiction threat data — if S2 identifies MSR threat, S4 updates MSR status immediately.

### 7-4. Intelligence Integration Layer — Threat and IPB Data

**BLUF:** The intelligence integration layer places S2 threat and IPB data directly into the operational picture, enabling the S3 and commander to assess the threat in context of the operational terrain and BLUFOR disposition.

**Intelligence Layer Contents (S2-owned):**
1. **Enemy positions:** Known enemy unit locations (confirmed) marked with enemy icons.
2. **Templated positions:** Enemy most probable and most dangerous COA positions (distinguished from confirmed by icon shading per unit SOP).
3. **Terrain overlay:** Mobility corridors, trafficability by soil type, key terrain identified in the IPB.
4. **Weather effects:** Terrain effects modified by current and forecast weather (particularly mobility effects).
5. **Collection plan overlay:** Collection asset positions and coverage areas.

**S2 display discipline:** S2 must maintain strict labeling discipline in the intelligence layer:
- Confirmed enemy = solid enemy icon
- Templated/assessed enemy = dashed enemy icon
- Old/unvalidated = grayed icon with last-confirmed timestamp

This discipline prevents the commander from treating templated positions as confirmed, which can produce false confidence in the threat picture.

### 7-5. Maintaining COP Currency — Data Freshness Standards

**BLUF:** A stale COP is worse than no COP — because it provides false confidence. Data freshness is a command standard, not a preference.

**Table 7-1. COP Data Freshness Standards**

| Data Layer | Required Freshness (Operations) | Required Freshness (Garrison/Training) | Owner |
|---|---|---|---|
| BLUFOR positions (MSS layer) | <4 hours | <24 hours | S3 |
| Threat overlay | <4 hours | <24 hours | S2 |
| Unit Status (readiness/personnel) | <8 hours | <24 hours | S3/S4/S1 |
| Logistics Status (DOS, MSR) | <8 hours | <24 hours | S4 |
| CCIR Status | Continuous (real-time alert) | <4 hours | S3 |
| Decision Point Status | Continuous | <24 hours | S3 |
| Fires Graphics (NFA/RFA) | <4 hours (or per FRAGO) | <24 hours | FECC |

**Enforcing freshness standards:**
1. Battle captain checks data timestamps at every watch transition.
2. Stale data is flagged immediately — battle captain notifies the owning section to update.
3. If a section cannot update (personnel unavailable, connectivity issue), battle captain reports to S3.
4. S3 makes a command decision: accept the risk of stale data, or take corrective action (request update, shift reporting responsibility temporarily).

### 7-6. Shared COP Access — Subordinate Integration

**BLUF:** ADP 6-0 requires shared understanding (ADP 6-0, para 2-8). MSS enables shared COP access across echelons — subordinate units can see the higher HQ COP (read-only) and contribute their own data upward. This is a force multiplier for shared understanding.

**Subordinate COP integration procedure:**
1. S6 ensures subordinate unit MSS accounts have read access to the appropriate parent COP workspace.
2. S3 establishes subordinate unit data contribution responsibilities: which data do subordinates push to the higher HQ COP? (PERSTAT, LOGSTAT, contact reports — per unit SOP.)
3. Subordinate S3/battle captains access the higher HQ COP for orientation, decision point awareness, and logistics planning.
4. Higher HQ MSS administrator (coordinated by S6) manages the access permissions hierarchy.

> **NOTE: Shared COP access across echelons requires disciplined data contribution from subordinates. If subordinate units do not update their data, their portion of the higher HQ COP will be stale. Subordinate data reporting discipline is a command climate issue — not a technology issue.**

---

## CHAPTER 8 — ASSESSMENT AND REPORTING

**BLUF:** Assessment is the process of determining the progress of the force toward accomplishing the mission (ADP 5-0, para 1-9). MSS enables systematic, data-driven assessment by providing a platform to track MOEs and MOPs, generate reports from data, and identify trends that would be invisible in single-snapshot reporting.

### 8-1. Continuous Assessment — MOE and MOP Products on MSS

Continuous assessment requires persistent tracking infrastructure — not periodic snapshots (ADP 5-0, para 1-9). MSS provides that infrastructure through the assessment workspace.

**Building the Assessment Workspace:**
1. Open the MSS assessment workspace (or create one if not yet established for the current operation).
2. Load all MOPs from the OPORD assessment plan and Step 4 wargame record.
3. Load all MOEs from the OPORD assessment plan.
4. For each MOP and MOE: link to the data source, set the threshold, assign the data owner, and set update frequency.
5. Configure the assessment dashboard to display current MOP/MOE status, trend direction, and comparison to threshold.

**Table 8-1. Assessment Product Format**

| Indicator | Current Value | Threshold | Status | Trend (7-day) | Owner | Data As-Of |
|---|---|---|---|---|---|---|
| [MOP or MOE name] | [current] | [threshold] | [G/A/R] | [↑/↓/→] | [section] | [timestamp] |

**Assessment review cycle:** MOPs and MOEs are reviewed at every BUA (daily status check) and every CUB (weekly trend analysis). The daily check answers: are we still on track? The weekly analysis answers: is the trend line pointing in the right direction?

**Assessment Brief Format — Presenting to the Commander:**

Assessment products presented to the commander must answer three questions, in order (ADP 5-0, para 1-9):

1. **Where are we?** Current MOE/MOP values against thresholds. Green/Amber/Red status.
2. **Where are we going?** Trend direction. Is the situation improving, stable, or deteriorating?
3. **What should we do?** The staff recommendation — adjust, reinforce, accept, or exploit — supported by the assessment data.

The third question is the critical gap in most assessment briefs. Staffs present the data (questions 1 and 2) but leave the commander without a staff recommendation (question 3). MSS provides the data for questions 1 and 2. The S3 and staff are responsible for synthesizing that data into a recommendation for question 3.

**Limitations of MSS-Based Assessment:**

MSS assessment products are quantitative — they measure what can be counted. Not all operationally relevant information is quantitative. MSS will show that route security incidents are decreasing; it will not show that the local population's willingness to cooperate with the force is increasing. The S3 must integrate MSS quantitative assessment with S2 qualitative assessments, S9 civil indicators, and commander observations to produce a complete operational assessment.

> **NOTE: Assessment is a judgment, not a calculation. MSS provides the data inputs. The operations process — specifically the collaborative assessment discussion at the BUA and CUB — transforms data inputs into operational judgment. Design battle rhythm products to support that discussion, not to replace it (ADP 5-0, para 1-9).**

### 8-2. SITREP Generation from MSS Data

**BLUF:** The SITREP is the primary recurring operational report. MSS data substantially reduces the time required to compile a SITREP by providing pre-integrated status data from all sections.

**Conditions:** SITREP is due per reporting schedule. Battle captain is responsible for SITREP compilation.

**Standards:** SITREP is accurate, current, and submitted within the timeline specified by higher HQ. Data is sourced from MSS with timestamps. Format conforms to higher HQ SITREP format.

**Procedure — SITREP Generation from MSS:**
1. Open the MSS reporting workspace and navigate to the SITREP template.
2. Pull current COP screenshot for the operations paragraph. Confirm timestamp.
3. Pull current PERSTAT from S1 workspace for the personnel paragraph. Note data-as-of timestamp.
4. Pull current LOGSTAT from S4 workspace for the logistics paragraph. Note data-as-of timestamp.
5. Pull current CCIR status from the CCIR dashboard for the CCIR paragraph. Note any triggered CCIRs since last SITREP.
6. Pull current assessment status (MOPs/MOEs) for the assessment paragraph.
7. S3 or battle captain reviews the compiled data for accuracy. Adds narrative synthesis (MSS provides data; the S3 provides the assessment and synthesis narrative).
8. Routes for commander or XO review per unit SOP.
9. Submits via approved reporting channel. Archives submitted SITREP in MSS reporting workspace.

> **NOTE: MSS provides the data for the SITREP. The narrative synthesis — "what does this mean for the operation?" — is the S3's responsibility. Do not submit raw data extracts as SITREPs. Synthesize the data into an operational assessment.**

### 8-3. SPOTREP Integration

**BLUF:** SPOTREPs are immediate-action reports for significant events. MSS integrates SPOTREP data into the COP and SITREP record.

**SPOTREP procedure on MSS:**
1. When a significant event occurs, the reporting unit submits a SPOTREP via approved channel (radio, digital, MSS direct-entry — per unit SOP).
2. Battle captain receives the SPOTREP. Enters the event into the MSS contact tracking workspace.
3. Event appears in the COP with the SPOTREP data (location, type, unit, time, narrative).
4. Battle captain assesses: does this event trigger a CCIR? If yes, process per CCIR procedure (paragraph 6-3).
5. Battle captain assesses: does this event affect a decision point? If yes, alert S3 immediately.
6. SPOTREP is archived in the MSS contact tracking workspace for SITREP and AAR use.

### 8-4. Readiness Reporting — C-Rating Trend Products

**BLUF:** Readiness reporting in MSS goes beyond the current C-rating snapshot. The trend — where readiness is going — is operationally more valuable than the current point.

**C-Rating Trend Product:**
1. Open the readiness trend workspace in MSS.
2. Select time period: 30 days is the standard for the readiness review brief; 90 days for the CUB strategic trend analysis.
3. Display C-rating by unit over the selected time period. MSS plots the trend line automatically if data has been consistently reported.
4. Add reference lines: C-1 threshold, C-2 threshold, C-3 threshold.
5. Annotate significant events on the trend line: major maintenance cycles, personnel changes, equipment resets, field exercises.
6. S3 synthesizes the trend: is readiness improving, stable, or declining? What is driving the trend?

> **CAUTION: C-rating trends are only as valid as the C-rating reporting discipline. If units have been reporting artificially high or inconsistently, the trend line is not analytically valid. S3 must cross-reference C-rating trends against maintenance data (deadlines, ERFC) and personnel data (fill rates) to validate trend credibility before briefing the commander.**

### 8-5. After-Action Review Data Collection and Analysis

**BLUF:** The AAR is the primary Army learning event. MSS supports AAR data collection by maintaining a chronological record of operations — COP snapshots, CCIR events, contact reports, decision point events, and MOE/MOP trends — that provides the factual basis for AAR discussion.

**AAR Data Package (S3 prepares using MSS):**
1. **Timeline reconstruction:** Pull contact tracking data and decision point events from MSS for the operation period. Build an event timeline.
2. **MOE/MOP results:** Pull final assessment data — were MOPs achieved? Did MOEs reach threshold?
3. **CCIR history:** Pull CCIR event log from the CCIR workspace — when were CCIRs triggered, what was the response?
4. **COP snapshots:** Pull COP snapshots at key time stamps from the operation (for map-based discussion in the AAR).
5. **Readiness and logistics data:** Pull readiness and logistics trend data for the operation period.

The AAR facilitator uses the MSS data package as the factual baseline. The AAR discussion then focuses on "what should have been different" — not on reconstructing what actually happened. MSS eliminates the factual reconstruction phase of the AAR and focuses the discussion on learning.

---

## CHAPTER 9 — ECHELON-SPECIFIC GUIDANCE

**BLUF:** MSS integration varies by echelon. BCT-level operations are characterized by current operations intensity; division and corps-level operations emphasize longer planning horizons, larger data aggregation, and more complex synchronization products. This chapter addresses MSS employment at each echelon.

### 9-1. BCT — S3 and Battle Captain Focus

**Brigade Combat Team (BCT) MSS Employment:**

At BCT level, the S3 section is the primary MSS consumer. The battle captain is the most frequent MSS user, monitoring the COP and CCIRs continuously during operations. MSS at BCT is primarily an execution tool — current operations management, CCIR monitoring, and battle rhythm support.

**BCT-Specific MSS Configuration:**
- Battle rhythm is typically 24-hour cycle: daily BUA, targeting meeting, LOGSYNCH.
- CCIRs are primarily readiness and logistics FFIRs — the BCT commander's most immediate concerns.
- MDMP at BCT is typically 24–48 hours. MSS planning workspace is compressed but still used.
- Subordinate battalion S3s have read access to BCT COP; battalion PERSTAT/LOGSTAT flows up to BCT MSS automatically.

**BCT Battle Captain Primary Tasks:**
1. Monitor COP and CCIR dashboard continuously during operations.
2. Prepare BUA data package (T-60 min procedure, paragraph 4-3).
3. Track decision points and alert S3 when triggers approach.
4. Compile SITREP from MSS data (paragraph 8-2).
5. Manage watch transition — hand off current COP picture, CCIR status, and open incidents.

**BCT MSS Product Priority List:**
- Priority 1: COP (always current, always visible)
- Priority 2: CCIR Dashboard (always active, always monitored)
- Priority 3: BUA Product Package (prepared before every BUA)
- Priority 4: Readiness Trend (weekly, for readiness review and CUB)
- Priority 5: SITREP (per reporting schedule)

### 9-2. Division — G3 Section Integration

**Division MSS Employment:**

At division level, the G3 section manages a larger formation across a wider AOR. MSS integration emphasizes aggregation — pulling data from subordinate BCTs into a division-level COP, and building the assessment products that inform division-level decision-making.

**Division-Specific MSS Configuration:**
- Division G3 has visibility of subordinate BCT MSS workspaces (read access for planning and assessment).
- Division-level CCIR thresholds are different from BCT thresholds — typically aggregated (e.g., "if any two subordinate BCTs reach C-3 readiness simultaneously").
- Future Operations (G35) and Current Operations (G33) sections each have distinct MSS workspaces and product responsibilities.
- Division MDMP planning horizon is typically 72 hours or longer; planning workspace is more complex.

**G3 vs. G35 MSS Responsibilities:**
- **G33 (Current Operations):** Owns the division current COP, CCIR monitoring, BUA products, and SITREP.
- **G35 (Future Operations):** Owns MDMP planning workspace, COA development data, decision support products for future operations.
- **G39 (Civil Affairs/IO integration):** Owns civil considerations overlay and IO event tracking.

**Division-Level Decision Support Products:**
- Cross-BCT readiness comparison (which BCT is best positioned for next mission?)
- Division logistics aggregation (total Class I–IX across all BCTs — where are the formation shortfalls?)
- Division assessment (MOE/MOP aggregated from BCT operations — is the division operation achieving effects?)

### 9-3. Corps — G3/G35 Future Operations Integration

**Corps MSS Employment:**

At corps level, MSS employment emphasizes planning support for complex, multi-division operations, and the integration of joint and combined arms data into the corps COP. The G3/G35 Future Operations section is the primary MSS user at corps level.

**Corps-Specific MSS Configuration:**
- Corps G3 accesses subordinate division MSS workspaces for aggregated readiness, logistics, and assessment data.
- Corps-level CCIRs are typically multi-echelon and longer-horizon.
- Planning workspace at corps supports 72-hour to 7-day planning horizons.
- ORSA staff (TM-40G) integrated with G35 to support COA analysis and quantitative decision products.
- AI/ML-enabled products (TM-40H, TM-40M) integrated into corps-level predictive assessments.

**Corps COP Architecture:**
- Division-level COPs are visible within the corps COP (federated display).
- Corps G2 maintains the combined threat picture across all division AOs.
- Corps fires data integrates theater-level fires (MLRS, aviation fires, joint fires) into the corps COP.
- Joint interface: if joint fires or joint logistics are integrated, coordinate with J3/J4 equivalent through the C2DAO for MSS data feed integration.

### 9-3a. Special Operations Forces (SOF) Integration Considerations

When a conventional force headquarters (BCT, Division, Corps) is operating with or in support of SOF, MSS integration requires additional coordination. SOF units may operate separate MSS tenants or may be integrated into the conventional force COP with restricted access.

**Key coordination points for SOF/CF MSS integration:**
1. **Access deconfliction:** SOF liaison officer (LNO) accesses the conventional force COP with a consumer-level account. SOF-specific operational data is not automatically visible in the conventional force COP — coordinate with J3/G3 on what SOF data should be integrated and what must remain siloed.
2. **COP integration level:** At minimum, SOF unit locations should appear in the conventional force COP to prevent fratricide and support airspace deconfliction. SOF LNO coordinates what is displayed.
3. **CCIR integration:** If the commander's CCIRs include events that SOF activity would trigger (example: enemy HVT neutralized by SOF), coordinate with SOF LNO on how that information flows into the MSS CCIR system.
4. **Fires deconfliction:** SOF operating areas must be integrated into the fires restrictions overlay in MSS. FECC coordinates with SOF fires representative.

### 9-4. Integration with Higher HQ MSS Instances

When USAREUR-AF operates as a subordinate to a joint or combined command, MSS integration with higher HQ instances may be required. Coordination points:

1. **Access provisioning:** S6 coordinates with higher HQ S6/G6 to provision MSS accounts for liaison officers and required cross-HQ data access.
2. **Data feed integration:** C2DAO coordinates with higher HQ data team to establish approved data feeds from higher MSS instance.
3. **COP sharing:** Read access to higher HQ COP is established via C2DAO coordination — not independently by unit S6.
4. **CCIR alignment:** Review unit CCIRs for consistency with higher HQ CCIRs. Redundant or conflicting CCIRs should be deconflicted with the higher HQ S3.
5. **Reporting integration:** Confirm that MSS-generated reports (SITREP, readiness reports) meet higher HQ format and data requirements.

---

## CHAPTER 10 — DEGRADED OPERATIONS

**BLUF:** MSS is a network-dependent platform. When the network degrades, MSS availability degrades. The operations process does not stop. Staffs must be able to execute the Mission Command function at reduced capability, using manual fallback products and non-digital methods, until MSS connectivity is restored (FM 6-02, para 5-8).

### 10-1. MSS Degradation Levels

Four degradation levels define the MSS operating condition:

**Level 1 — Partial Degradation:**
- Definition: MSS is accessible but one or more data feeds are unavailable or significantly delayed (>4 hours stale for operational data).
- Impact: Specific data layers (example: S2 threat overlay, S4 LOGSTAT) are stale. Other functions normal.
- Staff action: Identify which feeds are degraded. Use alternate reporting channels for the affected data. Continue MSS use for non-degraded functions.

**Level 2 — Significant Degradation:**
- Definition: MSS is accessible but multiple data feeds are unavailable. Data across most staff sections is >8 hours stale.
- Impact: COP picture is significantly outdated. CCIR monitoring is unreliable. BUA products cannot be built to standard.
- Staff action: Shift to manual data collection. Request verbal and written reports from all sections. Build manual BUA product (see paragraph 10-2). Notify S6 and C2DAO. Continue MSS monitoring for recovery.

**Level 3 — Full Outage:**
- Definition: MSS is inaccessible. Network connectivity to the MSS tenant is down.
- Impact: No MSS functions available. All data management reverts to manual.
- Staff action: Immediately implement degraded operations plan. Shift all reporting to non-digital channels. Build manual COP using acetate overlay on paper maps. Notify S6, C2DAO, and higher HQ.

**Level 4 — Sustained Outage:**
- Definition: MSS has been inaccessible for >12 hours (or as defined by unit SOP).
- Impact: Extended manual operations. Significant data accumulation gap — when MSS returns, historical data must be re-entered or reconstructed.
- Staff action: Maintain manual operations through the outage. Document all significant events, report data, and status changes. When MSS returns, conduct data reconstruction (see paragraph 10-3).

### 10-2. Manual Fallback Products by Staff Section

**S3 (Current Operations):**
- Manual COP: paper map with acetate overlay. Battle captain maintains using grease pencil. Unit positions from radio reports and BFT.
- Manual CCIR monitoring: battle captain maintains a written CCIR log. Sections report by voice/radio when thresholds are crossed.
- Manual BUA product: whiteboard or paper-based status briefing. S3 compiles from verbal section reports.

**S1 (Personnel):**
- Manual PERSTAT: unit submits PERSTAT by radio or runner. S1 maintains a paper PERSTAT tally board.
- Manual casualty tracking: DA Form 1156 (Casualty Feeder Report) and unit casualty log.

**S2 (Intelligence):**
- Manual threat overlay: acetate on map, maintained by S2 from radio reports and BFT contacts.
- Manual INTSUM: typed or handwritten, distributed physically or via radio brief to the staff.

**S4 (Logistics):**
- Manual LOGSTAT: unit submits by radio/runner. S4 maintains a paper LOGSTAT tally.
- Manual Class III/V tracking: vehicle fuel status from radio reports; ammunition by DA Form 581 (Request for Issue/Turn-In of Ammunition).

**FECC (Fires):**
- Manual target list: printed last-known-good target list from MSS (paper backup) maintained in a three-ring binder.
- Manual fires tracking: whiteboard target list. AFATDS continues to function independently of MSS.

**Table 10-1. Manual Fallback Products**

| Staff Section | Manual Product | Medium | Update Frequency | Data Source |
|---|---|---|---|---|
| S3 | Manual COP | Paper map, acetate | Continuous | Radio, BFT, runner |
| S3 | CCIR Log | Written log | Continuous | Section voice reports |
| S1 | PERSTAT Tally Board | Whiteboard | 2x daily | Radio/runner |
| S2 | Threat Overlay | Acetate overlay | 4-hour cycle | Radio, sensor reports |
| S4 | LOGSTAT Tally Board | Whiteboard | 2x daily | Radio/runner |
| FECC | Printed Target List | Paper binder | Per engagement | AFATDS, radio |

### 10-3. Network Restoration and Data Validation Procedures

When MSS connectivity is restored after Level 3 or Level 4 degradation:

**Phase 1 — Connectivity Restoration (S6):**
1. S6 confirms MSS connectivity is fully restored. Validate access from all CP workstations.
2. S6 checks pipeline status: are all data feeds flowing? Are there any pipeline errors?
3. S6 notifies S3 and all sections: "MSS restored. Begin data update sequence."

**Phase 2 — Data Update (all sections simultaneously):**
1. Each section logs into MSS and enters the current status (PERSTAT, LOGSTAT, threat overlay, etc.).
2. Each section backtracks: enters significant status changes that occurred during the outage (casualties, equipment deadlines, intelligence reports) with the time of occurrence — not the time of entry.
3. MSS CCIR thresholds are validated: did any thresholds cross during the outage? Were they captured in the manual log? If yes, enter them in MSS with the actual time of occurrence.

**Phase 3 — COP Validation (S3):**
1. S3 reviews the reconstructed COP against the manual product maintained during the outage.
2. Discrepancies between the manual record and MSS reconstruction are investigated and resolved.
3. S3 certifies the COP as valid before resuming MSS-based battle rhythm products.
4. Timeline: COP validation complete within 60 minutes of MSS restoration.

**Phase 4 — Lessons Learned (post-operation):**
1. S6 and C2DAO document the outage: cause, duration, affected functions.
2. S3 documents operational impact: what decisions were delayed or degraded due to MSS unavailability?
3. Unit incorporates lessons into degraded operations SOP update.

### 10-4. OPSEC and Security During Degraded Operations

**BLUF:** Degraded operations increase OPSEC risk. Manual products are easier to lose, capture, or inadvertently expose. Additional OPSEC measures apply during MSS degradation.

1. **Hardcopy data handling:** Printed MSS products and manual fallback products are classified at the level of the data they contain. Handle accordingly. Do not leave printed COP products unattended in uncontrolled areas.
2. **Communications:** During MSS outage, voice radio is used for data reporting. Encrypt sensitive data per communications OPSEC plan. Do not transmit clear-text sensitive data on non-encrypted channels.
3. **Data reconstruction:** When entering backtracked data into MSS after restoration, apply the same data handling standards as normal operations. Ensure re-entered data does not create data integrity issues (duplicate entries, conflicting timestamps).
4. **Reporting:** If MSS outage is due to a cyberattack, notify S6 and unit information systems security manager (ISSM) immediately. Follow unit cyber incident response SOP. Do not attempt to restore connectivity without S6 and ISSM coordination.

> **WARNING: A cyber-induced MSS outage is a reportable cybersecurity incident. Do not treat it as a routine connectivity failure. Notify S6, ISSM, and higher HQ G6/C2DAO immediately. Follow the unit cybersecurity incident response plan.**

---

## APPENDIX A — MISSION COMMAND PRODUCT STANDARDS CHECKLIST

### A-1. Pre-Brief Checklist (BUA / CUB / Decision Brief)

**Complete T-60 minutes before any commander brief using MSS data:**

- [ ] COP data freshness verified — all layers within required currency (Table 7-1)
- [ ] S1 PERSTAT updated — timestamp confirmed <4 hours (operations) / <24 hours (garrison)
- [ ] S2 threat overlay updated — timestamp confirmed <4 hours
- [ ] S4 LOGSTAT updated — timestamp confirmed <8 hours
- [ ] CCIR dashboard reviewed — no unresolved triggered alerts
- [ ] Decision point tracker reviewed — any DPs approaching or triggered since last brief?
- [ ] Assessment dashboard reviewed — any MOP/MOE status changes since last brief?
- [ ] All data products include data-as-of timestamp (visible on the product)
- [ ] All data products include source attribution (which MSS workspace / data feed)
- [ ] Commander's brief format conforms to unit SOP / higher HQ guidance

### A-2. CCIR Monitoring Checklist (Watch Transition)

**Complete at every watch transition (or at minimum, hourly during active operations):**

- [ ] CCIR dashboard open and visible on battle captain workstation
- [ ] Review all active CCIRs: any alerts since last check?
- [ ] For each alert: validate against primary data source before briefing commander
- [ ] False positive? Correct MSS data and document in CCIR record
- [ ] Valid trigger? Brief S3 immediately. Record trigger event in CCIR record.
- [ ] Decision point tracker: any DPs triggered or approaching?
- [ ] MSS data feeds: check pipeline status — any feeds showing errors or significant latency?
- [ ] Watch transition brief: outgoing battle captain briefs incoming on current CCIR status and any open incidents

### A-3. SITREP Preparation Checklist

**Complete before each SITREP submission:**

- [ ] Open MSS reporting workspace — SITREP template active
- [ ] Pull current COP screenshot — timestamp visible
- [ ] Pull S1 PERSTAT — timestamp verified
- [ ] Pull S4 LOGSTAT — timestamp verified
- [ ] Pull current CCIR status — any triggered CCIRs since last SITREP?
- [ ] Pull MOE/MOP assessment status
- [ ] S3 / battle captain reviews all data for accuracy
- [ ] Narrative synthesis written (not raw data — assessed status)
- [ ] SITREP reviewed by XO or S3 per unit SOP
- [ ] Submitted via approved channel
- [ ] Archived in MSS reporting workspace with submission timestamp

### A-4. MSS Product Development Request Format

Use this format when requesting a new MSS data product from a unit Builder (TM-20 qualified) or C2DAO:

---

**MSS PRODUCT DEVELOPMENT REQUEST**

**Date/Time:** [DTG]
**Requesting Section:** [S3, S2, S4, etc.]
**POC:** [Name, position, contact info]

**Product Name:** [Short descriptive title]

**Operational Need:** [Why is this product needed? What decision does it support? What problem does it solve?]

**Data Required:** [What data sources / datasets must be used? Existing MSS data or new feed required?]

**Display Format:** [Dashboard, COP overlay, table, chart, combination — describe or sketch]

**Update Frequency:** [How often must the product refresh? Real-time, hourly, daily, per reporting cycle?]

**Target Audience:** [Who will use this product? Battle captain only, all staff sections, commander?]

**Required By (NLT):** [Date/time when the product is needed for operations]

**Priority:** [Routine / Priority / Emergency — and justification for Emergency classification]

**Approved By:** [S3 signature / date for Routine; XO for Priority; Commander for Emergency]

---

---

## APPENDIX B — BATTLE RHYTHM INTEGRATION TEMPLATE

### B-1. Battle Rhythm Event Table Template

| Event | Frequency | Time | Location | Chair | MSS Product Required | Data Owner | Freshness NLT |
|---|---|---|---|---|---|---|---|
| BUA | Daily | 1800L | TOC | S3/XO | BUA Package | S1, S2, S3, S4 | T-60 min |
| Targeting | Daily | 1400L | TOC | FSCOORD | Target List Package | FECC, S2, S3 | T-30 min |
| LOGSYNCH | Daily | 1000L | TOC | S4 | LOGSTAT Package | S4, S3 | T-30 min |
| Readiness Review | Weekly | TBD | TOC | S3 | Readiness Trend | S3, S4, S1 | T-120 min |
| Intel Sync | Daily | 0700L | S2 Cell | S2 | PIR Status, INTSUM | S2 | T-30 min |
| CUB | Weekly | TBD | CP | Commander | Decision Package | All | T-240 min |

*(Adjust frequency, time, and location for unit-specific battle rhythm)*

### B-2. Reporting Requirement Elimination Analysis Worksheet

| Current Report | Frequency | From Who | Data Elements | MSS Coverage? | Recommended Action | Commander Decision |
|---|---|---|---|---|---|---|
| [Report name] | [Freq] | [Unit] | [List] | Full / Partial / None | Eliminate / Modify / Retain | Approved / Not Approved |

Instructions:
1. List every recurring report currently required from subordinate units.
2. For each report, identify which data elements are available in MSS at the required freshness.
3. Where MSS coverage is Full: recommend elimination of the report.
4. Where MSS coverage is Partial: recommend modification to capture only non-MSS elements.
5. Where MSS coverage is None: retain the report.
6. Brief the commander. Record the decision.

### B-3. Battle Rhythm Synchronization Matrix

| Staff Section | BUA Contribution | Targeting Contribution | LOGSYNCH Contribution | CUB Contribution | MSS Workspace | Update SOP |
|---|---|---|---|---|---|---|
| S1 | PERSTAT | — | Personnel in the logistics picture | Personnel trend | S1 Workspace | Daily, by 1700L |
| S2 | INTSUM, Threat Overlay | Target confirmation, BDA | — | Intel assessment | S2 Workspace | Daily, by 1700L |
| S3 | COP, Decision Points | Fires sync | Op timeline vs. sustainment | MOE/MOP results | S3 Workspace | Continuous |
| S4 | LOGSTAT | Fires assets status | Full LOGSTAT | Logistics forecast | S4 Workspace | Daily, by 1700L |
| FECC | Fires summary | Full target package | Ammunition status | Fires assessment | Fires Workspace | Per targeting cycle |
| S6 | Network status | — | — | System availability | S6 Workspace | As required |

---

## APPENDIX C — MSS DASHBOARD REFERENCE FOR MISSION COMMAND

**Table C-1. MSS Dashboards for Mission Command Practitioners**

| Dashboard Name | Purpose | Primary User | Access Level Required | Update Source | Freshness Standard |
|---|---|---|---|---|---|
| COP — Main Display | Integrated operational picture | Battle Captain, S3 | Consumer (read) | S3, S2, S4, S1 | <4 hours (ops) |
| CCIR Monitoring Dashboard | Automated CCIR alert monitoring | Battle Captain, S3 | Consumer (read) | S3 (CCIR configuration), All sections (data) | Real-time |
| PERSTAT Dashboard | Personnel status by unit | Battle Captain, S1 | Consumer (read) | S1 | <4 hours (ops) |
| LOGSTAT Dashboard | Logistics status by unit and class | Battle Captain, S4 | Consumer (read) | S4 | <8 hours (ops) |
| Threat Overlay | Enemy and IPB data layer on COP | Battle Captain, S2, S3 | Consumer (read) | S2 | <4 hours (ops) |
| Assessment Dashboard (MOE/MOP) | Mission progress tracking | S3, XO, Commander | Consumer (read) | S3 (configuration), all sections (data) | Per assessment SOP |
| Targeting Workspace | Target list, fires assets, BDA | FECC, S2, S3 | Consumer (read) | FECC, S2 | <2 hours (targeting cycle) |
| Decision Point Tracker | Decision point status and triggers | Battle Captain, S3, XO | Consumer (read) | S3 | Continuous |
| Readiness Trend | 30/90-day readiness trends | S3, XO, Commander | Consumer (read) | S3, S4 | <24 hours (weekly review) |
| Reporting Workspace (SITREP) | SITREP and reporting product compilation | Battle Captain, S3 | Consumer (read/write) | S3 | Per reporting schedule |

> **NOTE: "Consumer (read)" access means the dashboard is a pre-built product visible to operational staff. Modifying dashboard configuration (adding data sources, changing thresholds, changing layouts) requires Builder access (TM-20 qualified) or coordination with C2DAO.**

---

## APPENDIX D — DOCTRINAL REFERENCES QUICK CARD

**Table D-1. Doctrinal References for TM-40F**

| Publication | Title | Key Sections | Key Relevance to TM-40F |
|---|---|---|---|
| ADP 6-0 | Mission Command | Ch.1, para 1-1 (definition), para 1-28 (7 principles); Ch.2, para 2-8 (shared understanding), para 2-17 (CCIR) | 7 principles; shared understanding; commander's intent; disciplined initiative |
| FM 6-0 (May 2022) | Commander and Staff Organization and Operations | Ch.3 (staff organization S1–S9); Ch.4, para 4-1 (IM definition), para 4-6 (information relevance criteria), para 4-8 (battle rhythm); Ch.5 (CCIRs — PIR, FFIR, EEFI); Ch.12 (decision support) | Staff responsibilities; 6 IM tasks (collect, process, store, display, disseminate, protect); CCIRs; battle rhythm; decision support; information relevance criteria |
| FM 5-0 (Nov 2024) | Planning and Orders Production | Ch.2–8 (MDMP steps 1–7); Ch.10 (assessment — MOE/MOP framework); Appendix B (running estimates) | Operations process; MDMP 7 steps; assessment MOE/MOP framework; running estimates |
| ADP 5-0 | The Operations Process | Ch.1 (fundamentals); Ch.2 (plan); Ch.3 (prepare); Ch.4 (execute); Ch.5 (assess — continuous assessment cycle) | Operations process fundamentals: plan, prepare, execute, assess; continuous assessment |
| FM 3-0 | Operations | Ch.1 (operational environment); Ch.3 (elements of decisive action — offense, defense, stability); Ch.7 (information); Ch.9 (integrating processes — IPB, targeting, risk management) | Operational framework; decisive action context for MSS data products; integrating processes that drive COP and CCIR requirements |
| ATP 6-0.5 | Command Post Organization and Operations | Ch.2 (CP types — Main/TAC/Alt/Jump); Ch.3 (battle rhythm events and design); Ch.5 (CP displacement and PACE planning) | Main/TAC/Alt/Jump CP configuration; battle rhythm event design; CP displacement procedures; MEDS concept |
| FM 6-02 | Signal Support to Operations | Ch.3, para 3-12 (network-enabled applications); Ch.4 (signal support to the CP); Ch.6 (network operations) | Network architecture; MSS as network-enabled C2 application; CP connectivity requirements |
| ATP 5-0.3 | Commander and Staff Estimates | Ch.2 (estimate methodology); Ch.3 (running estimate format); Appendixes B–H (staff-specific estimate formats — S1 through S6) | Running estimates inform MSS dashboard design; staff estimate formats map to MSS data domains by section; estimate update triggers align to CCIR thresholds |
| ATP 5-19 | Risk Management | Ch.2 (5-step process); Ch.3 (hazard assessment); Ch.4 (risk acceptance authority levels) | Risk management in planning; operational risk assessment methodology; risk data on MSS |
| ADP 2-0 | Intelligence | Ch.1 (intelligence fundamentals); Ch.2 (IPB); Ch.3 (intelligence support to the operations process — PIR management) | IPB; PIR management; intelligence support to operations process; threat overlay data |
| FM 3-09 | Fire Support and Field Artillery Operations | Ch.2 (fire support planning); Ch.4 (targeting — D3A/decide-detect-deliver-assess); Ch.6 (fire support coordination) | Fires integration with the operations process; targeting process; BDA data flow to COP |
| ATP 4-90 | Brigade Support Battalion | Ch.2 (logistics operations); Ch.3 (LOGSTAT reporting); Ch.5 (maintenance operations) | Logistics operations; LOGSTAT format and data flow; supply and maintenance status reporting |
| ATP 5-0.1 | Army Design Methodology | Ch.2 (ADM steps); Ch.3 (framing the operational environment) | ADM critical thinking before MDMP; environmental framing informs MSS data requirements |
| TC 6-0.2 | Training the C2 WFF for BN/BDE/BCT | Part I (C2 training tables); Part II (battle drills and collective tasks) | C2 training tables; collective task standards for MSS-enabled battle rhythm execution |

**Strategic Guidance:**

> The following are strategic guidance documents — not doctrine — that inform MSS training design and operational context.

| Document | Authority | Relevance |
|---|---|---|
| NATO Warfighting Capstone Concept (2021) | NATO NWCC | 6 Critical Enablers including Data — frames MSS as enabler of alliance warfighting |
| NATO Digital Transformation Implementation Strategy (Oct 2024) | NATO | Digital transformation roadmap — MDO interoperability context for mission command systems |
| DDOF Playbook v2.2 (December 2025) | T2COM C2DAO | VAULTIS-A quality framework (8 dimensions); 6-phase data product lifecycle; 85% quality gate; MVP mandate 30 days |

---

## APPENDIX E — MOS QUICK REFERENCE BY SECTION

**Table E-1. MOS Quick Reference — Mission Command MSS Users**

| Section | Officer Branch / MOS | Warrant Officer MOS | Enlisted MOS | Primary MSS Role |
|---|---|---|---|---|
| S3 / G3 | 11A, 19A, 13A (and branch-equivalent INF, AR, FA) | — | 11Z, 19Z, 13Z, 25Z | Primary consumer; CCIR monitoring; battle rhythm; MDMP support |
| S2 / G2 | 35A (MI), 35D (All-Source) | 350F (All-Source Technician) | 35F, 35N, 35G, 35L | Intelligence data layer; PIR management; threat overlay; INTSUM |
| S1 / G1 | 42A (Human Resources) | 420A (HR Technician) | 42A, 42H, 42R | PERSTAT; casualty tracking; personnel FFIR monitoring |
| S4 / G4 | 90A (AG/QM) | 920A (Property Accounting), 920B (Supply Systems) | 92A, 92Y, 92F | LOGSTAT; maintenance status; logistics FFIR monitoring; GCSS-Army coordination |
| S6 / G6 | 25A (Signal) | 255A (Information Services Technician) | 25U, 25Z | Network; account management; PACE planning; C2DAO liaison |
| FECC | 13A (FA), FSO branches | — | 13F, 13B, 13D | Fires overlays; target list; BDA; targeting workspace |
| ADAM/BAE | 14A (ADA), 15A (Aviation) | 150A (Aviation Technician) | 14P, 15Q, 15R | Airspace overlays; ADA status; aviation integration |
| CBRN | 74A (CBRN) | — | 74D | CBRN incident tracking; contamination overlays; MOPP status |
| SJA | 27A (JA), 27D (Paralegal) | — | 27D | Targeting legal review; no-strike list; ROE documentation |
| Civil Affairs | 38A (CA) | — | 38B | Civil considerations overlay; CMO event tracking |
| FA Officers | 50A, 51A, 53A, 54A | — | — | Domain-specific (force management, engineer, info systems, IO) |

---

## APPENDIX F — PROFESSIONAL READING LIST

> Curated articles from Army professional journals and military publications. These supplement doctrinal references with contemporary operational perspectives.

| Source | Title | Date | Relevance |
|---|---|---|---|
| War on the Rocks | "The U.S. Army, AI, and Mission Command" | Mar 2025 | AI impact on mission command philosophy |
| Military Review | "The True Test of Mission Command" | Sep-Oct 2024 | Mission command in practice |
| Military Review | "Modernizing Military Decision-Making: Integrating AI into Army Planning" | Aug 2025 | AI-augmented MDMP |
| Small Wars Journal | "Elevating Information as a Core WfF for MDO" | Apr 2025 | Information as warfighting function |

---

## GLOSSARY

**After-Action Review (AAR):** A professional discussion of an event, focused on performance standards, that enables soldiers to discover for themselves what happened, why it happened, and how to sustain strengths and improve on weaknesses (FM 7-0).

**Battle Captain:** The S3 section officer or senior NCO responsible for maintaining current operations in the TOC, monitoring CCIRs, and supporting the S3. The primary MSS operator during current operations.

**Battle Rhythm:** A deliberate daily cycle of activity within a headquarters that coordinates the decision-making cycle (FM 6-0).

**Battle Update Assessment (BUA):** A daily commander meeting at which staff sections brief current status — readiness, personnel, logistics, intelligence, CCIR status — using MSS data products.

**BLUF (Bottom Line Up Front):** An Army writing convention requiring the key point or recommendation to appear at the beginning of the product, not at the end.

**C-Rating:** Army readiness rating system: C-1 (fully ready), C-2 (mostly ready), C-3 (marginally ready), C-4 (not ready). Based on personnel, equipment, training, and supply readiness inputs.

**C2DAO (Command and Control Data and Analytics Office):** The USAREUR-AF organization responsible for MSS platform management, data governance, and technical standards.

**CCIR (Commander's Critical Information Requirement):** Identified by the commander as critical to facilitating timely decision making. Includes PIRs and FFIRs (FM 6-0).

**Common Operating Picture (COP):** A single identical display of relevant information shared by more than one command, enabling shared understanding (FM 3-0).

**CP PACE Plan:** Primary, Alternate, Contingency, Emergency plan for command post communications, including MSS connectivity.

**Decision Point:** A point in space and time at which the commander or staff anticipates making a decision concerning a specific course of action (FM 5-0).

**EEFI (Essential Elements of Friendly Information):** Critical friendly information that, if known by the enemy, would compromise or jeopardize the mission (FM 6-0).

**FFIR (Friendly Force Information Requirement):** Information the commander needs about friendly forces to make decisions (FM 6-0).

**GCSS-Army:** Global Combat Support System-Army. The Army's integrated enterprise resource planning (ERP) system for logistics and maintenance data.

**INTSUM:** Intelligence Summary. A recurring intelligence product briefing current enemy and environmental assessments.

**IPB (Intelligence Preparation of the Battlefield):** A systematic, continuous process of analyzing the threat and environment in a specific geographic area (ATP 2-01.3).

**LOGSTAT:** Logistics Status Report. Recurring report capturing Class I–IX status, days of supply, and maintenance data.

**MDMP (Military Decision Making Process):** A seven-step, iterative planning process that integrates the activities of the commander, staff, and subordinate commanders (FM 5-0).

**MEDS (Minimal Essential Data Set):** The commander-directed minimum MSS data products required at the TAC CP to sustain Mission Command during forward operations.

**MOE (Measure of Effectiveness):** A criterion used to assess changes in system behavior, capability, or operational environment that is tied to measuring the attainment of an end state, achievement of an objective, or creation of an effect (JP 3-0).

**MOP (Measure of Performance):** A criterion used to assess friendly actions that is tied to measuring task accomplishment (JP 3-0).

**MSS (Maven Smart System):** The USAREUR-AF enterprise AI/data platform built on Palantir Foundry. Integrates operational data from multiple sources into a unified data environment supporting Mission Command, analytics, and AI-enabled decision support.

**OPFOR:** Opposing Forces. Enemy forces in the operational context.

**PERSTAT:** Personnel Status Report. Recurring report capturing unit strength, present-for-duty, and casualty data.

**PIR (Priority Intelligence Requirement):** An intelligence requirement, stated as a priority for intelligence support, that the commander and staff need to understand the adversary or the operational environment (FM 6-0).

**SITREP:** Situation Report. Periodic report to higher HQ on current operational status, personnel, logistics, and intelligence.

**SPOTREP:** Spot Report. Immediate-action report for significant, time-sensitive operational events.

**TASKORG (Task Organization):** The temporary grouping of forces designed to accomplish a particular mission (ADP 5-0).

**TOC (Tactical Operations Center):** The operations section of a headquarters. The physical location where battle captains, S2/S3 staffs, and supporting elements conduct current operations management.

**UDRA (Unified Data Reference Architecture):** USAREUR-AF data governance framework establishing data standards, platform authorization, and access management requirements for all enterprise data systems.

---

*TM-40F — Maven Smart System (MSS): Mission Command Warfighting Function — Intermediate Operator's Manual*
*Headquarters, United States Army Europe and Africa, Wiesbaden, Germany*
*Version 1.0 | March 2026*
*Distribution: Distribution authorized to U.S. Government agencies and their contractors only. Other requests must be referred to Headquarters, USAREUR-AF, C2DAO, Wiesbaden, Germany.*
*Authority: USAREUR-AF C2DAO*

**DoD and Army Strategic References:**

- **JADC2 Strategy Summary (March 2022)** — Cross-domain data integration strategy for Joint All-Domain Command and Control
- **DoD Directive 3000.09, Autonomy in Weapon Systems (January 2023 update)** — Policy on autonomous and semi-autonomous functions in weapon systems; context for mission command decision support
- **JCOIE (Joint Concept for Operating in the Information Environment)** — Joint framework for information operations and decision advantage in the information environment
- **DDOF Playbook v2.2 (December 2025)** — T2COM C2DAO; VAULTIS-A quality framework (8 dimensions); 6-phase data product lifecycle; 85% quality gate; MVP mandate 30 days
