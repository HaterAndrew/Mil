# TM-40D — MAVEN SMART SYSTEM (MSS)
## SUSTAINMENT WARFIGHTING FUNCTION
## INTERMEDIATE OPERATOR'S MANUAL

**HEADQUARTERS, UNITED STATES ARMY EUROPE AND AFRICA**
Wiesbaden, Germany

2026

**Version 1.0 | March 2026**

**PREREQUISITE PUBLICATIONS:** TM-10, Maven User; TM-20, Builder; CONCEPTS_GUIDE_TM40D_SUSTAINMENT (required before beginning this manual). No coding, pipeline development, or transform experience is required or assumed.

**DISTRIBUTION RESTRICTION:** Approved for public release; distribution is unlimited.

**AUTHORITY:** This publication is issued under authority of the USAREUR-AF C2 Data and Analytics Office (C2DAO). It implements Army CIO Memorandum, Data and Analytics Policy (April 2024), aligns to the Unified Data Reference Architecture (UDRA) v1.1 (February 2025), and supports implementation of ADP 4-0, FM 4-0, ATP 4-0.1, FM 4-01, ATP 4-42, ATP 4-41, ATP 4-15, and FM 4-30. Reference learn-data.armydev.com for current platform documentation.

---

## SAFETY SUMMARY

Sustainment practitioners using MSS operate at the intersection of logistics data, equipment readiness reporting, and personnel accountability. Errors in supply status, readiness reporting, or personnel accountability data can degrade the supported commander's ability to generate combat power — and produce failed missions at the moment of need.

Before using MSS sustainment products to support any decision:

- Verify data freshness before reporting. Every MSS product displays a data-as-of timestamp. Stale LOGSTAT or readiness data presented as current status is operationally dangerous. A maintenance report reflecting yesterday's deadline count does not reflect today's readiness.
- Do not allow MSS to substitute for physical verification. MSS reports what has been reported into the system. It does not independently verify what is on-hand or operational. A supply status that shows 100% fill may reflect a requisition status, not a delivery confirmation. Verify through the supply chain.
- GCSS-Army and MSS data must be reconciled. MSS pulls data from GCSS-Army feeds. Discrepancies between GCSS-Army records and MSS displays indicate a feed latency or entry error — not that one system is right and the other is wrong. Reconcile at the source.
- Ammunition data is safety-critical. Errors in ammunition basic load reporting, DODIC management, or lot number tracking in MSS have potential for catastrophic consequences. Validate ammunition status against physical inventories, not solely against MSS displays.
- PERSTAT accuracy has tactical consequences. Inaccurate personnel accountability data fed into MSS CCIR thresholds can mask casualty reporting failures or strength shortfalls. Verify PERSTAT inputs against unit first-sergeant accountability before reporting to higher.
- OPSEC applies to sustainment data. Supply status, ammunition basic loads, petroleum inventory, and personnel strength data are operationally sensitive. Dashboard screenshots, exported LOGSTAT products, and MSS data extracts are subject to the same handling requirements as the underlying data. Coordinate with the unit IMO before distributing outside the originating classification domain.

> **WARNING: Presenting MSS sustainment data to a commander without verifying data currency and source reconciliation can lead to supply, maintenance, or readiness decisions based on false situational awareness. Always confirm data-as-of timestamp and GCSS-Army source feed status before any LOGSTAT brief or commander sustainment update.**

> **CAUTION: MSS readiness and supply thresholds are dependent on reported data entered into source systems (GCSS-Army, SAMS-E, PBUSE). An alert indicating a supply shortage or readiness decline is a prompt to investigate through the supply chain and with unit property accountability officers — not a confirmed status. Validate all MSS threshold triggers against primary source records.**

> **NOTE: MSS does not replace GCSS-Army, SAMS-E, STAMIS, PBUSE, or LIW as authoritative supply and maintenance management systems. MSS integrates and visualizes data from those systems. Transactions that affect accountability, property records, or official supply status must be entered in the authoritative system — not only in MSS.**

---

## TABLE OF CONTENTS

- Chapter 1 — Overview: The Sustainment WFF and MSS
- Chapter 2 — Supply Chain Management in MSS
- Chapter 3 — Maintenance Management
- Chapter 4 — Transportation and Distribution Operations
- Chapter 5 — Ammunition Management
- Chapter 6 — Petroleum and Water Operations
- Chapter 7 — Human Resources and Personnel Accountability
- Chapter 8 — Field Services and Health Service Support
- Chapter 9 — Echelon-Specific Sustainment Operations
- Chapter 10 — Degraded Operations
- Appendix A — Sustainment-Specific Naming Conventions in MSS
- Appendix B — LOGSTAT Report Fields and Standards
- Appendix C — Supply Class Quick Reference (Class I–IX)
- Appendix D — Maintenance Priority Matrix
- Appendix E — Distribution Synchronization Checklist
- Glossary

---

## CHAPTER 1 — OVERVIEW: THE SUSTAINMENT WFF AND MSS

**BLUF:** TM-40D teaches sustainment practitioners — supply sergeants, maintenance NCOs, transportation coordinators, ammunition specialists, and HR professionals — how to use MSS in daily sustainment work. No coding or pipeline development. This is operational use of a data-enabled enterprise platform in direct support of the Sustainment warfighting function.

### 1-1. The Sustainment Warfighting Function

The Sustainment warfighting function is the related tasks and systems that provide support and services to ensure freedom of action, extend operational reach, and prolong endurance (ADP 4-0, para 1-1). Sustainment enables commanders to sustain their forces anywhere, in any environment, for as long as necessary (ADP 4-0, para 1-3).

The six elements of the Sustainment warfighting function are:

1. **Supply** — providing materiel to forces, including Class I–IX and Class X
2. **Maintenance** — providing support to extend the operational life of systems and equipment
3. **Transportation** — moving personnel, equipment, and materiel throughout the operational area
4. **Field services** — performing essential support to Soldiers: food service, laundry, bath, mortuary affairs
5. **Health service support** — medical care, evacuation, and medical logistics
6. **Human resources support** — accounting for and supporting personnel

MSS integrates data from all six elements into a single visible picture. Before MSS, the Sustainment warfighting function was characterized by data silos: maintenance data lived in SAMS-E, supply data in GCSS-Army, personnel data in IPPS-A, and each section maintained its own trackers to bridge the gaps. The S4 building a LOGSTAT for higher pulled from four systems and hoped the numbers reconciled. On MSS, authoritative source feeds populate a unified Ontology layer, enabling integrated sustainment products for any echelon.

> **NOTE: MSS does not replace authoritative sustainment management systems. GCSS-Army remains the system of record for supply transactions. SAMS-E remains the system of record for maintenance work orders. MSS integrates and displays the data from those systems — it does not duplicate their transactional functions.**

### 1-2. MSS and Sustainment Data Types

**Table 1-1. Sustainment Data Types in MSS**

| Data Category | Source System | MSS Function |
|---|---|---|
| Supply status (Class I–IX) | GCSS-Army, unit property book | Dashboard display, threshold alerts, LOGSTAT generation |
| Equipment readiness (PMCS/deadline) | SAMS-E, GCSS-Army | Readiness trend display, NMC tracking, maintenance priority dashboard |
| Transportation assets | GCSS-Army, unit reports | Convoy status, vehicle availability, movement request tracking |
| Personnel accountability | IPPS-A, unit PERSTAT | Strength dashboard, CCIR threshold monitoring |
| Ammunition (ASR/CSR, basic load) | SAAS-MOD, unit ammunition officer | Ammunition status, DODIC tracking, basic load comparison |
| Petroleum (POL status) | Unit reports, LOGSTAT | Fuel point status, throughput tracking, distribution routing |
| Water (Class I-W) | Unit reports | Purification status, distribution tracking |
| Medical supply (Class VIII) | Medical logistics, MEDCENS | Coordination product — not authoritative MSS domain |
| FLIPL / report of survey | Unit property book officer | Accountability exception tracking |
| Personnel actions | IPPS-A | Awards, actions pipeline — HR specialist domain |

### 1-3. MSS vs. Legacy Sustainment Tools

**Table 1-2. MSS vs. Legacy Tools — Functional Comparison**

| Function | Legacy Tool | MSS Role |
|---|---|---|
| Supply transactions | GCSS-Army | Integrates and visualizes GCSS-Army data |
| Maintenance work orders | SAMS-E | Displays work order status, readiness trend |
| Property accountability | PBUSE | Integrates property book data for accountability dashboards |
| Parts/supply requisition | GCSS-Army, LIW | Displays requisition status, EDD tracking |
| Personnel accountability | IPPS-A, unit PERSTAT | Strength dashboard, PERSTAT products |
| Ammunition management | SAAS-MOD | Displays ammunition status, basic load comparison |
| Transportation management | GCSS-Army, manual | Convoy status, movement request tracking |
| LOGSTAT (roll-up) | Manual/email | Automated LOGSTAT aggregation across formation |
| Fuel tracking | Manual/LOGSTAT | POL point status, distribution throughput |

**CAUTION: Do not use MSS as a substitute for entering transactions in authoritative systems. A supply status entered only in MSS, and not recorded in GCSS-Army, is not an official transaction. Authoritative records drive financial accountability, property book accuracy, and audit readiness.**

### 1-4. Sustainment Workspace Organization

MSS organizes sustainment data in unit-level workspaces. Each workspace mirrors the unit's sustainment organizational structure.

**Standard Sustainment Workspace Components:**

- **LOGSTAT Dashboard** — integrated supply, maintenance, transportation, and personnel status for LOGSTAT reporting to higher
- **Supply Status** — Class I–IX on-hand vs. requirement, requisition pipeline
- **Maintenance Status** — equipment readiness, deadline tracking, NMC summary by unit
- **Transportation** — vehicle availability, convoy status, movement request pipeline
- **Ammunition** — basic load status, ASR/CSR comparison, retrograde tracking
- **Personnel** — PERSTAT, strength by unit, FFIR threshold monitoring
- **Sustainment BUA** — consolidated sustainment update product for battle rhythm events

### 1-5. Doctrinal References

TM-40D is written in alignment with the following doctrinal publications. These publications are not required reading before using this manual — but sustainment practitioners who are responsible for S4 functions or sustainment command positions should be familiar with them.

**Table 1-2. Primary Doctrinal References**

| Publication | Title | Relevance to TM-40D |
|---|---|---|
| ADP 4-0 | Sustainment | Sustainment WFF definition, principles, and echelon roles |
| FM 4-0 | Sustainment Operations | Detailed sustainment procedures; LOGSTAT format |
| ATP 4-0.1 | Army Theater Sustainment Operations | Theater-level sustainment; TSC/ESC operations |
| FM 4-01 | Army Transportation Operations | 88-series MOS procedures; movement management |
| ATP 4-42 | Field Ordering Officer / Purchasing Agent | Field ordering procedures; contracting in the AOR |
| ATP 4-41 | Army Field Feeding and Class I Operations | 92G procedures; ration management |
| ATP 4-15 | Army Watercraft Operations | 88K/88L procedures; port and waterway operations |
| FM 4-30 | Ordnance Operations | Maintenance; EOD; ammunition |
| AR 700-138 | Army Logistics Readiness and Sustainability | Equipment readiness reporting; C-rating criteria |
| AR 710-2 | Supply Policy Below the National Level | Supply accountability; sensitive items |
| AR 750-1 | Army Materiel Maintenance Policy | Maintenance management; controlled exchange |
| AR 638-8 | Army Casualty Program | Casualty reporting and notification |
| DA Pam 55-353 | Defense Transportation Regulation, Part II | Vehicle load limits; HAZMAT transport |

### 1-6. BSB / FSB / ESB / TSB Workspace Configuration

Workspace configuration varies by sustainment echelon.

**Table 1-3. Workspace Configuration by Sustainment Echelon**

| Echelon | Unit | Primary MSS Products |
|---|---|---|
| Battalion S4 section | Brigade S4 (non-BSB) | LOGSTAT contribution to BSB, maintenance and supply status for own battalion |
| BSB | Brigade Support Battalion | Distribution company tracking, LOGSTAT rollup for brigade, Class I–III–V status |
| FSB | Forward Support Battalion (DIV) | Class I–III status, maintenance status for supported brigade |
| ESB | Engineer Support Battalion | Equipment-heavy maintenance tracking, mobility/barrier materiel |
| TSC/ESC | Theater Sustainment Command / Expeditionary Sustainment Command | Theater-level distribution, HNS tracking, ASL status, strategic LOC monitoring |
| CSSB | Combat Sustainment Support Battalion | Area sustainment, fuel points, water points, Class I–III distribution |

### 1-6. Scope: What TM-40D Covers and Does Not Cover

**TM-40D covers:**

- Supply chain management and LOGSTAT procedures for 92A, 92Y, 90A, and S4 sections
- Maintenance management workflows for 91-series and 915A/914A warrant officers
- Transportation and distribution coordination for 88-series MOSs and 88N coordinators
- Ammunition management procedures for 89A and 89B specialists
- Petroleum and water operations for 92F and 92W specialists
- HR and personnel accountability for 42A specialists
- Field services data management for 92G food service
- Echelon-specific procedures from company through TSC
- Degraded operations and fallback procedures

**TM-40D does NOT cover:**

- Building MSS pipelines, transforms, or dashboards — see TM-20 and TM-30
- Ontology modification or dataset schema changes — see TM-30
- Machine learning models — see TM-40C (TM-50I)
- GCSS-Army transaction entry procedures — see GCSS-Army user documentation
- SAMS-E work order entry — see SAMS-E user manuals
- IPPS-A personnel transactions — see IPPS-A user documentation

### 1-6. Relationship to Other TMs in the MSS Curriculum

**Table 1-3. TM Curriculum Relationships**

| TM | Title | Relationship to TM-40D |
|---|---|---|
| TM-10 | Maven User | Foundation prerequisite. Platform navigation, basic data access. Required before this manual. |
| TM-20 | Builder | Not required. Builds sustainment dashboards and Workshop products that TM-40D users consume. |
| TM-30 | Advanced Builder | Not required. Designs data pipelines that feed sustainment products. Coordinate through S6 or C2DAO. |
| TM-40A | Intelligence | Companion. Intel products feed threat data; sustainment data (LOC status, supply point security) feeds intel picture. |
| TM-40B | Fires | Companion. Ammunition management (Ch. 5) requires coordination with fires WFF for CSR and expenditure data. |
| TM-40C | Movement and Maneuver | Companion. Maneuver unit readiness and supply status feed the sustainment picture; sustainment constraints feed the maneuver plan. |
| TM-40D | Sustainment | This manual. |
| TM-40E | Protection | Complementary. Force protection data affects sustainment convoy routes and supply point security. |
| TM-40F | Mission Command | Complementary. S4 sustainment products contribute to the COP (S3 product); LOGSTAT feeds commander FFIR monitoring. |
| TM-50 Series | Advanced Specialist Tracks | Post-graduate level for technical specialists. Not applicable to operational sustainment practitioners. |

> **NOTE: TM-20 (Builder) is NOT required for this manual. TM-40D assumes no ability to build pipelines or transforms. If you encounter a sustainment data product that does not exist and needs to be built, coordinate with your unit's designated MSS Builder (TM-20 qualified) or the C2DAO.**

### 1-7. Audience and MOS Coverage

**Table 1-4. Primary Audience by Function and MOS**

| Function | Officer / Warrant | Enlisted | Position Examples |
|---|---|---|---|
| Logistics (multifunctional) | 90A | — | S4, BSB CDR, Sustainment BDE staff |
| Supply | — | 92A, 92Y | Supply Sergeant, Automated Log Spec, Unit Supply Spec |
| Maintenance | 915A, 914A | 91A–91Z | Maintenance Officer, Maintenance Warrant, Shop OIC/NCOIC |
| Transportation | 88A | 88H, 88M, 88N | Transportation OIC, Cargo Spec, Motor Transport Operator, TC Coordinator |
| Watercraft | 88A | 88K, 88L | Watercraft Officer, Watercraft Operator/Engineer |
| Ammunition | 89D (EOD/Ammo) | 89A, 89B | ASP OIC, Ammunition Stock Control NCO, Ammunition Specialist |
| Petroleum | — | 92F | POL NCO, Fuel Point Supervisor |
| Water | — | 92W | Water Treatment Specialist |
| Food Service | — | 92G | Food Service Sergeant, DFAC NCOIC |
| HR / Personnel | 42B | 42A, 42H | S1, HR NCOIC, Strength Manager |
| Parachute Rigger | — | 92R | Rigger Section Chief |

### 1-8. How to Use This Manual

TM-40D is organized by sustainment function. Read Chapter 1 in full before beginning any other chapter. Subsequent chapters are organized by supply class and functional area — read the chapters that apply to your MOS and duty position. Not every practitioner needs every chapter.

**Reading guide by MOS/position:**

| If you are... | Read these chapters |
|---|---|
| S4 (90A) | All chapters; focus on Ch. 1, 2, 3, 4, 9 |
| Supply Sergeant (92A/92Y) | Ch. 1, 2, 8; Appendix C |
| Maintenance NCO/Warrant (91Z, 914A, 915A) | Ch. 1, 3; Appendix D |
| Transportation (88A, 88N) | Ch. 1, 4; Appendix E |
| Motor Transport Operator (88M) | Ch. 1, para 4-6 |
| Watercraft (88K, 88L) | Ch. 1, para 4-7 |
| Ammunition (89A, 89B) | Ch. 1, 5; Appendix C (Class V rows) |
| Petroleum (92F) | Ch. 1, 6 |
| Water (92W) | Ch. 1, para 6-5, 6-7 |
| HR Specialist (42A) | Ch. 1, 7 |
| Food Service (92G) | Ch. 1, 8 |
| Parachute Rigger (92R) | Ch. 1, para 5-7 |
| All sustainers | Ch. 10 (degraded operations) |

### 1-9. Prerequisites

Before beginning this manual, verify the following:

**Platform prerequisites:**
- [ ] TM-10 complete — can log into MSS, navigate Workshop, access assigned datasets, and use standard dashboard views
- [ ] CONCEPTS_GUIDE_TM40D complete — Sustainment doctrine/MSS integration mental models established
- [ ] MSS account provisioned with appropriate role and permissions — coordinate with unit S6
- [ ] GCSS-Army account active and current with appropriate role for your unit and function

**Operational prerequisites:**
- [ ] Familiar with unit sustainment SOP — LOGSTAT reporting requirements, times, and formats
- [ ] Familiar with unit supply and maintenance management procedures
- [ ] Familiar with SAMS-E and GCSS-Army at the level required for your position
- [ ] Completed unit-level OPSEC training for MSS data handling

---

## CHAPTER 2 — SUPPLY CHAIN MANAGEMENT IN MSS

**BLUF:** The 92A automated logistician and the S4 section are the primary users of supply chain data in MSS. This chapter covers Class I–IX tracking, push vs. pull logistics visualization, distribution dashboards, critical supply thresholds, and supply point data management. All procedures in this chapter support LOGSTAT reporting IAW FM 4-0.

### 2-1. Supply Classes and MSS Tracking

The Army uses nine supply classes (Class I–IX, plus Class X — agricultural and economic development material). Each class requires different tracking approaches in MSS.

**Table 2-1. Supply Class Reference and MSS Tracking Priority**

| Class | Type | MSS Priority | Primary Metric |
|---|---|---|---|
| I | Rations, water | High — daily tracking | Days of Supply (DOS), ration cycle status |
| II | Clothing, tools, hand tools | Medium | On-hand vs. authorized, due-in status |
| III | POL (packaged) | High — daily tracking | On-hand gallons, consumption rate, DOS |
| IIIB | Bulk fuel | High — daily tracking | Capacity %, throughput, distribution status |
| IV | Barrier/construction material | Medium | On-hand vs. plan, task-specific tracking |
| V | Ammunition | High — daily tracking | Basic load %, ASR/CSR status |
| VI | Personal demand items | Low | Unit-level accountability |
| VII | Major end items | High — readiness-linked | Authorized vs. on-hand, deadline status |
| VIII | Medical | Coordination product | Managed by HSS; S4 monitors availability |
| IX | Repair parts | High — maintenance-linked | PLL fill rate, requisition pipeline, EDD |

### 2-2. 92A Automated Logistician Workflow in MSS

**Task: Supply Requisition and Receipt Tracking**

**Conditions:** 92A specialist with MSS access, GCSS-Army authoritative system access, assigned to BSB or unit supply section.

**Standards:** All requisitions reflected in MSS supply dashboard within 24 hours of submission in GCSS-Army. Critical shortages (Class I below 3 DOS, Class V below 90% basic load, Class IX PLL below 80% fill) reflected in MSS threshold alerts within 8 hours of update.

**Procedure:**

1. Log into MSS and navigate to the Supply workspace for your unit.
2. Open the Supply Status dashboard. Verify data-as-of timestamp is within 24 hours. If data is stale, notify MSS Administrator (unit S6 or C2DAO point of contact).
3. Review Class I status: compare on-hand DOS to current authorized strength. If below unit SOP threshold (typically 3 DOS), confirm MSS alert is active. Verify actual on-hand against physical inventory.
4. Review Class IX PLL status: compare on-hand parts to PLL document. Identify critical shortages by equipment type. Cross-reference with SAMS-E open work orders to identify parts needed for deadline equipment.
5. Review requisition pipeline: confirm all open requisitions from GCSS-Army are reflected in MSS. Note estimated delivery dates (EDD) for critical parts.
6. Review due-in status for Class VII (major end items): any end item with due-in status affects readiness picture and LOGSTAT.
7. Update MSS notes/annotation fields with operational status not captured in GCSS-Army feeds (e.g., actual delivery on-hand but not yet receipted).
8. Export or record supply status for LOGSTAT preparation (see Appendix B).

> **NOTE: GCSS-Army is the system of record. Discrepancies between MSS display and GCSS-Army records must be resolved in GCSS-Army. Do not manually override MSS supply displays to show a different number than GCSS-Army reflects. Identify the discrepancy and correct the source record.**

### 2-3. Push vs. Pull Logistics Visualization

ADP 4-0 describes two fundamental distribution methods: push (anticipatory, forward-loaded logistics) and pull (responsive, requisition-driven logistics) (ADP 4-0, para 2-12). MSS visualizes both.

**Push Logistics on MSS:**
- Theater-level push distribution displays scheduled delivery windows, convoy manifests, and throughput tracking
- Supply officer can see incoming push quantities against projected demand — enabling pre-positioning and storage coordination
- ASL (Authorized Stockage List) fill rate tracks whether push quantities meet requirement

**Pull Logistics on MSS:**
- Requisition pipeline dashboard shows all open pull requests, status, and EDD
- Pull effectiveness metric: time from requisition submission to receipt (requisition-to-delivery cycle time)
- Units below fill rate thresholds appear as alerts for S4 and BSB staff

> **BLUF:** Push logistics requires anticipation data — projected consumption, operational planning factors. Pull logistics requires pipeline visibility — requisition status, EDD, backorder identification. MSS supports both. The 92A uses both views daily to manage supply status.**

### 2-4. Distribution Management Dashboard

**Task: Monitor Distribution Status**

**Conditions:** 92A or S4 officer with MSS access. Distribution operations are active within the AOR. Convoy operations underway or planned.

**Standards:** All active convoys reflected in MSS distribution dashboard with current status, checkpoint data, and estimated arrival. Delays of more than 30 minutes from planned schedule trigger automated threshold alert.

**Procedure:**

1. Navigate to Transportation/Distribution workspace.
2. Open Distribution Dashboard. Review all active convoys: departure location, destination, current status, checkpoint reporting, ETA.
3. Identify any convoys past scheduled checkpoint with no report. Coordinate with convoy commander through primary communications means — do not use MSS as a substitute for convoy communications.
4. Review upcoming planned convoys: verify load data (cargo class, weight/cube, hazmat status) is entered in MSS movement request fields.
5. Coordinate distribution priority conflicts: when two units require resupply and only one convoy is available, use MSS priority fields to record S4 distribution priority decision.
6. Update delivery confirmation: upon convoy arrival, confirm receipt entry in GCSS-Army. MSS dashboard will update from GCSS-Army feed.

### 2-5. Critical Supply Threshold Alerts

MSS generates automated alerts when monitored supply levels cross configured thresholds. Thresholds are set by the unit S4 or MSS Administrator.

**Standard Sustainment Thresholds (Army Planning Factors):**

| Supply Class | Warning Threshold | Critical Threshold |
|---|---|---|
| Class I | 3 DOS | 1 DOS |
| Class III (packaged) | 3 DOS | 1 DOS |
| Class IIIB (bulk fuel) | 30% capacity | 15% capacity |
| Class V (ammunition basic load) | 90% | 70% |
| Class IX (PLL fill rate) | 80% | 60% |
| Water (Class I-W) | 3 DOS | 1 DOS |

> **CAUTION: Thresholds in MSS are only as accurate as the values configured by the unit S4. Before relying on automated alerts, verify that threshold values match commander's published sustainment planning factors for the current operation. Thresholds set for garrison operations may not be appropriate for deployed operations.**

### 2-6. Supply Point Operations Data Management

92A and 92Y specialists assigned to supply points use MSS to track throughput, product on-hand, and distribution queue.

**Supply Point Data Entry Standards:**
- Update supply point status in MSS at a minimum twice daily (morning and evening) or as directed by SOP
- Record all receipts and issues by class, quantity, and unit
- Maintain distribution queue: which units are scheduled for resupply, quantities allocated, and time windows
- Flag any Class I, III, or V shortages that will affect next-day distribution

**Table 2-2. Supply Point MSS Data Fields (Minimum Required)**

| Field | Requirement | Update Frequency |
|---|---|---|
| Location (grid) | 8-digit grid, verified against current position | Each move |
| Capacity by class | Authorized vs. on-hand by supply class | Daily |
| Distribution completed | Units served, quantities issued | Daily |
| Shortages | Items below threshold, back-ordered | Real-time when identified |
| Incoming deliveries | Convoy number, ETA, quantity | As scheduled |

### 2-7. 92Y Unit Supply Specialist Workflow

**MOS:** 92Y (Unit Supply Specialist)
**Positions:** Unit Supply Sergeant, Property Book NCO, Organizational Supply Room

The 92Y unit supply specialist manages the unit's supply room: receiving, storing, and issuing supplies and equipment to the company or battalion. In MSS, the 92Y's primary role is unit-level supply accountability and status reporting.

**Task: Unit Supply Status Update**

**Conditions:** 92Y assigned to unit supply room. All receipts and issues from previous duty day have been processed in GCSS-Army. Commanders' supply requirements have been reviewed.

**Standards:** Unit supply room on-hand quantities reflected accurately in MSS within 24 hours of GCSS-Army entry. All pending requisitions (not yet received) reflected in MSS with open status. Shortages below unit SOP thresholds flagged in MSS.

**Procedure:**

1. Pull daily on-hand report from GCSS-Army for unit supply room.
2. Log into MSS. Navigate to Supply > Unit Supply Status.
3. Verify on-hand quantities in MSS match GCSS-Army on-hand report. Reconcile discrepancies (see paragraph 2-5 note on GCSS-Army as system of record).
4. Review open requisitions: confirm all outstanding requests are reflected with correct status (submitted, approved, due-in).
5. Review shortage list: any Class II, VII, or IX items below minimum authorized. Verify shortage annex is current if applicable.
6. Update sensitive item accountability confirmation: weapons, NVGs, COMSEC — confirm inventory was completed and reflected in MSS sensitive item tracker.
7. Prepare supply room status input for LOGSTAT contribution.

**Sensitive Item Accountability in MSS:**

> **WARNING: Sensitive items (weapons, NVGs, COMSEC equipment, and other high-value controlled items) require accountability procedures IAW AR 710-2 and unit SOP. MSS sensitive item tracking is a management tool — it does not replace the physical inventory requirement. Do not mark a sensitive item inventory "complete" in MSS unless a physical count was actually conducted. Administrative closure of sensitive item inventories in MSS without physical verification is a serious accountability failure.**

### 2-8. 90A Multifunctional Logistician Officer — S4 Section Integration

**MOS:** 90A (Multifunctional Logistician Officer)
**Positions:** S4, BSB CDR, FSB CDR, COSCOM/TSC G4 staff

The 90A multifunctional logistician officer is the integrating function for all sustainment operations within a formation. In MSS, the 90A's primary role is integrating the six supply functions into a coherent sustainment picture — and translating that picture into operational recommendations to the supported commander.

**S4 Section Daily Workflow:**
1. Open MSS LOGSTAT dashboard at start of duty day. Review overnight changes.
2. Review threshold alerts: identify any class of supply or readiness metric that crossed a threshold during the night.
3. Prepare S4 daily update for battalion/brigade commander: current status, trajectory, and recommended actions.
4. Direct subordinate supply, maintenance, and transportation NCOs to update any stale data before the morning battle rhythm event.
5. Attend battle rhythm event. Present sustainment picture using MSS LOGSTAT dashboard.
6. Direct resupply requests for any below-threshold items.
7. Coordinate distribution for next 24 hours in DSM (see paragraph 4-8).
8. Review end-of-day status before submitting evening LOGSTAT.

---

## CHAPTER 3 — MAINTENANCE MANAGEMENT

**BLUF:** Maintenance management in MSS integrates equipment readiness data from SAMS-E and GCSS-Army into a visible picture for maintenance NCOs, warrant officers, and S4 sections. This chapter covers the 91Z/91A maintenance workflow, deadline tracking, work order management, shop stock and PLL management, and GCSS-Army data reconciliation.

### 3-1. Equipment Readiness and the Maintenance Reporting Chain

IAW AR 700-138, unit commanders report equipment readiness status using the Equipment Status Report (ESR). The readiness classification system uses C-ratings (C-1 through C-4 for equipment) based on the percentage of operational equipment within the unit.

MSS integrates SAMS-E work order data and GCSS-Army records to produce a continuously-updated readiness picture — replacing the manual aggregation process that formerly required Excel-based compilation at each echelon.

**Equipment Status Categories in MSS:**

| Status | Definition | MSS Color Code |
|---|---|---|
| FMC (Fully Mission Capable) | Equipment meets all readiness standards | Green |
| PMC (Partially Mission Capable) | Equipment has faults but can perform primary mission | Amber |
| NMC/NMCS (Not Mission Capable, Supply) | Equipment deadlined; awaiting parts | Red |
| NMC/NMCM (Not Mission Capable, Maintenance) | Equipment deadlined; awaiting maintenance labor | Red |
| In maintenance float | Equipment dispatched to higher maintenance | Gray |
| Awaiting evacuation | Equipment awaiting recovery | Gray |

### 3-2. 91Z / 91A Maintenance Sergeant Workflow

**Task: Daily Equipment Readiness Status Update**

**Conditions:** 91Z or 91A assigned as maintenance NCO. SAMS-E is operational and current. MSS account provisioned with maintenance workspace access. Deadline list from morning motor pool inspection is complete.

**Standards:** MSS equipment readiness dashboard reflects current SAMS-E work order status within 4 hours of morning motor pool. All new deadlines entered in SAMS-E and reflected in MSS before 1000 daily. NMC equipment status includes NMC reason code and estimated repair date.

**Procedure:**

1. Complete morning motor pool inspection. Record all new deadline equipment on DA Form 5988-E.
2. Log into SAMS-E. Enter new work orders for all newly deadlined equipment. Assign NMC reason code (NMC-Supply or NMC-Maintenance) and priority.
3. Submit all Class IX requisitions for parts-waiting equipment in GCSS-Army. Record requisition document number in SAMS-E work order.
4. Log into MSS. Navigate to Maintenance workspace.
5. Review MSS readiness dashboard. Verify new deadline equipment appears with correct status and NMC reason code. If discrepancy exists between SAMS-E and MSS, contact MSS Administrator — do not manually override.
6. Review critical deadline list: equipment supporting immediate operations or scheduled for next PMCS cycle that is currently NMC.
7. Update maintenance priority in MSS priority field: use unit SOP priority codes or see Appendix D for standard maintenance priority matrix.
8. Prepare maintenance status input for LOGSTAT. Use MSS export function to generate unit maintenance status snapshot.

### 3-3. PMCS Status Tracking

Preventive Maintenance Checks and Services (PMCS) schedules are managed in SAMS-E. MSS displays PMCS compliance status by unit and equipment type.

**PMCS Compliance Dashboard:**
- Shows percentage of vehicles with current PMCS (before/during/after, quarterly, semiannual, annual)
- Identifies equipment with overdue PMCS (flags for maintenance scheduling)
- Trends PMCS completion rate over time — provides visibility into unit maintenance discipline

> **NOTE: High PMCS compliance rates reduce equipment deadline rates. Commanders who monitor PMCS compliance trends on MSS can identify units trending toward readiness degradation before equipment deadlines accumulate. This is a predictive application — not a reactive one.**

### 3-4. Work Order Management and Maintenance Priority

**Table 3-1. Maintenance Priority Codes**

| Priority | Code | Definition | MSS Treatment |
|---|---|---|---|
| Emergency | P1 | Combat operations being degraded NOW | Immediate notification to maintenance officer; appears on daily commander's brief |
| Urgent | P2 | Combat readiness will be degraded within 24 hours | Daily review by maintenance officer; EDD tracked |
| Routine | P3 | Does not affect current combat mission | Managed within normal work order queue |
| Deferred | P4 | Administrative maintenance, garrison scheduling | Tracked but not reflected in operational readiness metrics |

**Work Order Data Entry Standards for MSS Integration:**
- NMC reason code (NMCS or NMCM) required on every deadline entry
- Parts requisition document number required for all NMCS work orders
- EDD (Estimated Delivery Date) required for all parts-waiting items
- Estimated repair time required for all NMCM work orders

### 3-5. FLIPL Tracking and Accountability

The Financial Liability Investigation of Property Loss (FLIPL) process generates accountability exceptions when equipment is lost, damaged, or destroyed. MSS tracks open FLIPLs for unit property accountability.

**FLIPL Dashboard in MSS:**
- Displays all open FLIPLs by line number, initiating date, appointing official, and status
- Tracks suspense dates for FLIPL completion
- Links FLIPL items to property book records

> **CAUTION: FLIPL data in MSS is a management tool. The official FLIPL record is maintained in the property book system (PBUSE or GCSS-Army). Decisions on financial liability must be based on the official record — not on MSS tracking fields. MSS ensures suspense dates do not slip, not that the FLIPL is properly adjudicated.**

### 3-6. Shop Stock and PLL Management

**Task: PLL Status Review and Requisition Tracking**

**Conditions:** 91A parts NCO or 92A automated logistician with PLL management responsibility. GCSS-Army operational, PLL document current.

**Standards:** PLL fill rate displayed in MSS. All parts below minimum authorized stockage level generate threshold alerts in MSS. All critical PLL shortages for deadline equipment reflected in MSS within 4 hours.

**Procedure:**

1. Pull current PLL document from GCSS-Army. Verify on-hand quantities against GCSS-Army records.
2. In MSS, open the Maintenance > PLL Status dashboard.
3. Review PLL fill rate by equipment type. Note any items below 80% fill rate.
4. Cross-reference PLL shortages against open SAMS-E work orders. Identify whether any PLL shortages are directly contributing to current deadline equipment.
5. Identify PLL items with no open requisitions that are below minimum. Submit requisitions in GCSS-Army.
6. Update PLL dashboard notes with any controlled substitution or controlled exchange actions.

### 3-7. Maintenance Float and Controlled Exchange Tracking

Maintenance float — serviceable equipment held at higher echelon to replace deadlined equipment — is tracked in MSS at sustainment brigade level and above.

**Float Tracking in MSS:**
- Available float assets by system type and echelon
- Request pipeline: unit requests for float fill, approval status, dispatch status
- Return pipeline: deadlined equipment dispatched to depot or DRMO

**Controlled Exchange (CE) Tracking:**
- CE actions (cannibalization) must be documented and authorized IAW AR 750-1
- MSS tracks authorized CE actions: source equipment, donor parts, recipient equipment, authorizing official
- Open CE documentation tracked for parts return compliance

### 3-8. GCSS-Army Integration and Data Reconciliation

MSS feeds from GCSS-Army data pipelines. Reconciliation is a recurring maintenance task.

**Reconciliation Triggers:**
- Weekly scheduled reconciliation (standard)
- Any time MSS displays conflict with GCSS-Army records
- Prior to LOGSTAT submission
- Prior to any command maintenance inspection

**Reconciliation Procedure:**
1. Pull GCSS-Army equipment readiness report for unit.
2. Compare line-by-line against MSS maintenance dashboard.
3. Document all discrepancies (MSS shows FMC, GCSS-Army shows NMC; or vice versa).
4. Resolve at source: enter correction in GCSS-Army. MSS will update on next feed cycle.
5. If discrepancy persists after GCSS-Army correction, notify MSS Administrator for pipeline troubleshooting.

> **NOTE: The most common cause of GCSS-Army / MSS discrepancy is data entry lag — GCSS-Army records updated after MSS snapshot. Verify the GCSS-Army timestamp before concluding a reconciliation error exists.**

### 3-9. Warrant Officer Logistician (914A / 915A) Workflow

**Warrant Officer MOS:** 914A (Allied Trades Maintenance Technician), 915A (Automotive Maintenance Technician)
**Positions:** Maintenance Warrant Officer, Technical Inspector, Battalion/Brigade Maintenance Officer

The 914A and 915A warrant officers provide technical expertise in maintenance management that bridges the tactical maintenance NCO and the operational maintenance officer. In the MSS context, their primary roles are:

**Technical Inspection and Quality Assurance:**
- Review MSS work order entries for technical accuracy and completeness
- Identify work orders with unrealistic repair time estimates or incorrect NMC reason codes
- Flag SAMS-E entries requiring technical review before closure

**Readiness Analysis:**
- Conduct trend analysis on NMC reasons by equipment type — is there a pattern of recurring failures on the same platform?
- Review PLL usage patterns to identify items that should be added to the PLL based on historical demand
- Assess parts pipeline health: are EDDs realistic? Are parts being ordered at the correct priority?

**Controlled Exchange and Float Management:**
- Authorize controlled exchange (CE) actions — document in MSS with DA Form 2404 reference
- Coordinate maintenance float requests through MSS: verify eligibility, initiate request, track dispatch status
- Track CE return compliance: ensure donor parts are retrograded within authorized timeframe

**GCSS-Army Technical Assistance:**
- Provide technical guidance on correct NSN usage, part substitution, and requisitioning procedures
- Identify requisition errors that are causing NMCS delays: wrong NSN, wrong unit of issue, insufficient justification

---

## CHAPTER 4 — TRANSPORTATION AND DISTRIBUTION OPERATIONS

**BLUF:** Transportation and distribution in MSS gives the 88A transportation officer, 88N coordinator, and 88M motor transport operator visibility of vehicle status, convoy operations, cargo manifests, and movement requests across the formation. This chapter covers the core transportation workflows for MSS users at all echelons.

### 4-1. Transportation Officer / Coordinator Workflow

**MOS:** 88A (Transportation Officer), 88N (Transportation Management Coordinator)
**Positions:** Transportation OIC, Movement Control Officer, Distribution Company Commander, BSB S4 Transportation Officer

**MSS Transportation Data Domain:**
- Vehicle availability and readiness status
- Movement requests (submitted, approved, assigned, executed, complete)
- Convoy status and checkpoint reporting
- Distribution run scheduling and execution
- Load data: cargo class, weight, cube, hazmat

### 4-2. Vehicle Status and Readiness Tracking

**Task: Daily Vehicle Status Update**

**Conditions:** 88N or S4 transportation NCO. Unit is in operational status. GCSS-Army vehicle records are current. Morning vehicle inspection complete.

**Standards:** MSS vehicle status reflects current operationally ready (OR) percentage for all organic and attached vehicles. All deadlined vehicles reflected with NMC code within 4 hours of PMCS. Organic vehicles available for tasking clearly identified.

**Procedure:**

1. Obtain morning vehicle inspection results from motor sergeant.
2. Verify all vehicle status updates have been entered in GCSS-Army (or SAMS-E for maintenance).
3. Log into MSS. Open Transportation > Vehicle Status dashboard.
4. Verify vehicle OR rate reflects current status. Note any discrepancy between morning inspection and MSS display — reconcile against GCSS-Army records.
5. Identify vehicles available for movement tasking. Flag vehicles with upcoming scheduled PMCS that will affect availability.
6. Update movement planning horizon: vehicles scheduled for PMCS within 72 hours should not be assigned to multi-day convoys without coordination with maintenance.
7. Export vehicle availability report for daily transportation coordination meeting.

### 4-3. Convoy Planning and Route Management

**Task: Convoy Data Entry and Monitoring**

**Conditions:** 88N transportation coordinator. Movement order or transportation request has been approved. Convoy departure within 48 hours.

**Standards:** All required convoy data entered in MSS prior to dispatch. Convoy manifest complete. Checkpoint schedule loaded. Hazmat declarations complete if applicable.

**Procedure:**

1. Open MSS Transportation > Movement Request workspace.
2. Select approved movement request. Verify all cargo data is complete: class of supply, weight, cube, special handling requirements (hazmat, controlled items).
3. Enter convoy data:
   - Convoy commander name and contact
   - Serial number and vehicle count
   - Departure location and time
   - Route (primary and alternate) — link to MSS route overlay if available
   - Checkpoints with scheduled reporting times
   - Destination and ETA
4. Upload convoy manifest (if scanned) to MSS document link, or manually enter manifest line items.
5. Activate convoy tracking in MSS. Monitor checkpoint reporting during execution.
6. Upon convoy completion, close convoy record in MSS and confirm delivery with supply point or receiving unit.

**Table 4-1. Convoy Data Entry Requirements**

| Field | Required | Notes |
|---|---|---|
| Serial number | Yes | Assign per unit SOP |
| Convoy commander | Yes | Name and rank |
| Vehicle count | Yes | Include vehicle type |
| Primary route | Yes | Reference route overlay |
| Alternate route | Yes | Required for all convoys |
| Cargo class | Yes | Class I, III, V, IX, or mixed |
| Total weight | Yes | In pounds or short tons |
| Hazmat declaration | Yes (if applicable) | HAZMAT class and quantity |
| Checkpoint schedule | Yes | At least one intermediate checkpoint per 2 hours |
| ETA destination | Yes | |

### 4-4. Load Planning Data

**CAUTION: Load planning data in MSS does not replace the legal load requirements of DA Pam 55-353 or TC 55-88. MSS displays load data for tracking and coordination. The convoy commander retains responsibility for legal loads, vehicle weight limits, and hazmat compliance.**

Load planning data in MSS includes:
- Cargo manifest by line item
- Total weight vs. vehicle rated capacity
- Cube utilization
- Hazmat quantity and class (for emergency response planning)
- Special equipment requirements (flatbed, refrigerated, tanker)

### 4-5. Movement Request Management

The movement request (MOVREQ) process is the formal mechanism for requesting transportation support. MSS manages the MOVREQ pipeline.

**MOVREQ Status Workflow in MSS:**

| Status | Meaning | Action Required |
|---|---|---|
| Submitted | Unit has submitted request | Transportation officer reviews and validates |
| Approved | Request approved, not yet assigned | Assign to convoy package |
| Assigned | Assets allocated | Convoy data entry required |
| Executing | Convoy en route | Monitor checkpoint reporting |
| Complete | Delivery confirmed | Close request, reconcile supply records |
| Cancelled | Request withdrawn | Note reason for cancellation |

### 4-6. 88M Motor Transport Operator — Convoy Reporting

**MOS:** 88M (Motor Transport Operator)
**Task: Checkpoint Reporting**

**Conditions:** 88M is convoy team leader or vehicle commander on active convoy. Communication with higher is available. MSS is accessible to TC/dispatcher at home station.

**Standards:** Checkpoint reports submitted on time IAW convoy order. All significant events (accident, vehicle breakdown, route change) reported immediately through primary comms, with MSS update at next available opportunity.

> **NOTE: MSS is NOT the primary reporting mechanism for convoy status. Primary communications means (radio, FBCB2/JCR, phone) are the primary means for real-time convoy reporting. MSS is the tracking and aggregation tool used by the transportation coordinator at home station or operations center. Do not delay reporting a significant event because MSS is unavailable.**

**Checkpoint Report Data Elements:**
- Convoy serial number
- Current location (grid or checkpoint designation)
- Vehicle count (present vs. departed)
- Status (all OK, vehicle breakdown, delay, significant event)
- ETA to next checkpoint or destination

### 4-7. Watercraft Operations — 88K / 88L Port and Waterway Data

**MOS:** 88K (Watercraft Operator), 88L (Watercraft Engineer)

MSS supports watercraft operations in USAREUR-AF with the following data products (IAW ATP 4-15):

**Port Operations Data:**
- Vessel availability and readiness status (similar to vehicle status — see paragraph 4-2)
- Berth availability and scheduling
- Port throughput: tonnage per day, cargo processed
- Cargo queue at port: awaiting loading, loaded awaiting departure

**Waterway and Route Data:**
- River/inland waterway route status (draft clearance, bridge clearance, obstacle data)
- Weather/hydrological factors affecting waterway operations
- Port and waterway capacity compared to throughput requirements

> **NOTE: Waterway data in MSS is dependent on reporting from watercraft operations elements and theater engineer assessments. Maintain currency by updating waterway status after each transit and after any significant weather event that may affect water levels or navigation.**

### 4-8. Distribution Synchronization Meeting

The Distribution Synchronization Meeting (DSM) is the battle rhythm event where the S4 section deconflicts distribution requirements, allocates scarce transportation assets, and publishes the distribution run schedule for the next 24–48 hours. MSS is the primary product used in the DSM.

**Task: Prepare Distribution Synchronization Meeting Products**

**Conditions:** 88N or BSB S4 section. DSM is scheduled within 2 hours. All subordinate unit movement requests have been received (or the suspense has passed). Vehicle availability is current in MSS.

**Standards:** DSM products reflect current data from MSS. All movement requests are reflected in the product. Transportation asset allocation is documented in MSS. Distribution run schedule for next 24 hours is complete and visible in MSS before DSM begins.

**Procedure:**

1. Open MSS Transportation workspace. Pull movement requests received since last DSM.
2. Sort by priority: emergency, urgent, routine (use LOGSTAT threshold data to determine priority — units below Class I or V critical threshold move to high priority).
3. Review vehicle availability. Total available trucks vs. total requests. Identify gaps.
4. Build distribution run schedule: match trucks to requests, assign convoy commanders, identify escort requirements.
5. Deconflict routes: ensure two convoys are not using the same route at the same time in the same direction where route capacity is constrained.
6. Publish distribution schedule in MSS. Ensure all subordinate unit S4 sections can see their assigned resupply window.
7. Brief distribution schedule at DSM. Record any priority changes directed by S4 in MSS.

**Table 4-2. Distribution Priority Decision Matrix**

| Priority | Criteria | Transportation Allocation |
|---|---|---|
| Emergency | Unit below Class I 1 DOS or Class V 70% basic load | First available truck; consider ground/air coordination |
| High | Unit below Class I 3 DOS or Class V 90% | Next scheduled run; same-day execution |
| Routine | Unit above threshold, resupply in normal cycle | Next scheduled distribution run |
| Deferred | Administrative resupply; no operational urgency | Consolidate with routine run; delay acceptable |

### 4-9. Unit Movement Control in USAREUR-AF

USAREUR-AF transportation operations occur across the European theater, including rail, waterway, and road movement across multiple host nations. MSS provides the data framework for multi-modal movement coordination.

**Rail Movement Data in MSS:**
- Rail request status: submitted, approved, manifested, executing, complete
- Rail car assignments and cargo manifests by car
- Departure and arrival station data
- HNS rail coordination points

**Air Movement Coordination (LOGAIR / SEALIFT):**
- Air movement requests: priority, cargo class, weight/cube, hazardous cargo
- Aircraft availability and scheduling coordination (limited — air movement is S3/G3 function; S4 provides cargo data)
- Port call data for unit movements

**Sea/Inland Waterway (ATP 4-15):**
- Vessel request status
- Port throughput: cargo on-hand at port vs. shipping schedule
- Vessel readiness (88K/88L data — see paragraph 4-7)

---

## CHAPTER 5 — AMMUNITION MANAGEMENT

**BLUF:** Ammunition management in MSS gives the 89A and 89B specialist visibility of ammunition basic loads, ASR/CSR status, DODIC tracking, and retrograde pipeline. All ammunition data in MSS supplements — and does not replace — SAAS-MOD transactions and DA Form 581 documentation.

### 5-1. Ammunition Specialist Workflow in MSS

**MOS:** 89A (Ammunition Stock Control and Accounting Specialist), 89B (Ammunition Specialist)

**MSS Ammunition Data Domain:**
- Basic load status by unit and DODIC
- Ammunition Supply Rate (ASR) vs. Controlled Supply Rate (CSR) comparison
- Lot number tracking for safety recall compliance
- Retrograde and turn-in tracking
- Integration with fires mission data for expenditure reporting

> **WARNING: Ammunition data in MSS must be validated against physical inventory and SAAS-MOD records before any command decision on ammunition availability, supply rate adjustment, or fires planning. Errors in basic load reporting can result in fires units requesting fire missions beyond available ammunition stocks — a potentially catastrophic operational error. Physical counts are authoritative.**

### 5-2. Ammunition Basic Load Management

**Task: Basic Load Status Review**

**Conditions:** 89A assigned to ASP or unit ammunition officer. SAAS-MOD is operational. Current authorized basic load (ABL) document is available. Physical inventory completed within 72 hours.

**Standards:** MSS basic load dashboard reflects current on-hand quantities within 5% variance of SAAS-MOD records. All units below 90% ABL on Class V reflected as threshold alerts. All critical DODIC shortages (affecting fire mission capability) reflected in MSS within 4 hours of identification.

**Procedure:**

1. Pull current SAAS-MOD on-hand report.
2. Log into MSS. Navigate to Ammunition workspace.
3. Open Basic Load dashboard. Verify data-as-of timestamp.
4. Compare MSS quantities to SAAS-MOD report by DODIC. Document discrepancies.
5. Review ABL fill rate by unit. Identify units below 90% and below 70% thresholds.
6. Identify DODICs with outstanding requisitions. Verify EDD is entered in MSS for all back-ordered ammunition items.
7. Generate basic load status report for LOGSTAT or fires coordination.

### 5-3. ASR and CSR Tracking

The Ammunition Supply Rate (ASR) is the number of rounds per weapon per day that can be sustained with expected supply rates (FM 6-0). The Controlled Supply Rate (CSR) is the actual rate allocated by the commander based on tactical requirements and availability.

**ASR/CSR Display in MSS:**
- Current ASR by weapon system (established by higher headquarters)
- Current CSR by unit (allocated by supported commander)
- CSR vs. ASR comparison: shows whether allocated CSR is within supportable ASR
- Expenditure tracking: actual expenditure vs. CSR allocation

> **NOTE: When expenditures approach CSR limits, MSS alerts the ammunition officer and S4. This does not mean resupply is unavailable — it means consumption is approaching the threshold that requires commander decision to either adjust CSR, request ASR increase, or reduce fires tempo. The ammunition officer briefs the S4; the S4 briefs the commander.**

### 5-4. DODIC Management and Lot Number Tracking

**DODIC (Department of Defense Identification Code) Management:**
- MSS tracks all active DODICs in the unit's basic load
- Displays quantity by DODIC, lot number, and storage location
- Identifies DODICs subject to safety recalls (data input required by ammunition officer when recall is received)

**Lot Number Safety:**

> **WARNING: Lot number data in MSS enables recall identification — but the ammunition officer must input recall lot numbers when safety messages are received. MSS does not automatically receive Army safety message data. If an ammunition safety message is received, immediately cross-reference affected lot numbers against MSS records and physical inventory. Do not wait for MSS to generate an alert on its own.**

### 5-5. Retrograde and Turn-In Tracking

**Task: Retrograde Ammunition Tracking**

**Conditions:** Ammunition is being turned in or retrograded to ASP or higher echelon ammunition unit. Retrograde order or authorization has been received.

**Standards:** All retrograde actions reflected in MSS within 24 hours of initiation. Turned-in quantities reflected in basic load reduction within 24 hours of SAAS-MOD transaction.

**Procedure:**

1. Initiate retrograde documentation in SAAS-MOD (DA Form 581).
2. Log into MSS. Open Ammunition > Retrograde Tracking workspace.
3. Enter retrograde record: unit, DODIC, lot number, quantity, authorization document number, destination ASP.
4. Track retrograde status from initiated to in-transit to accepted at destination.
5. Upon confirmation of receipt at destination ASP, verify SAAS-MOD transaction is complete.
6. Confirm basic load reduction is reflected in MSS after SAAS-MOD update.

### 5-6. Integration with Fires Ammunition Reporting

The fires WFF and sustainment WFF share ammunition data in MSS. The fires section (FSO, S3 fires cell) uses ammunition status data to plan fire missions within CSR constraints.

**Fires-Sustainment Integration Points:**
- Ammunition officer publishes current CSR and ABL status to fires workspace in MSS
- Fires cell records planned and executed fire missions against CSR tracker
- Expenditure data flows from fires to sustainment for resupply planning
- S4 and fires cell coordinate CSR adjustments through MSS notification workflow

### 5-7. Parachute Rigger (92R) — Special Operations and JRTC/NTC Support

**MOS:** 92R (Parachute Rigger)
**Position:** Rigger Section Chief, FORSS NCO (Forward Operating Rigger Support Section)

The 92R parachute rigger's MSS role is primarily in aerial delivery tracking and container/airdrop equipment accountability.

**MSS Applications for 92R:**
- Container delivery system (CDS) bundle status: bundles prepared, manifested, expended, recovered
- Personnel parachute inventory: T-11, MC-6, reserve chutes on-hand vs. authorized
- Container accountability: TRIWALL, A-22, A-7A on-hand and status
- Rigging schedule: units scheduled for rigging support, rigging status

**Table 5-1. Ammunition Nomenclature and DODIC Quick Reference (Common)**

| DODIC | Description | Platform | Notes |
|---|---|---|---|
| A059 | 5.56mm Ball (M855A1) | M4/M249 | Standard infantry cartridge |
| A080 | 7.62mm Ball (M80A1) | M240/M14 | Crew-served and SOF |
| A555 | 9mm Ball (M882) | M17/M18 | Pistol standard |
| A877 | .50 Cal Ball (M33) | M2HB | Heavy machine gun |
| B507 | 40mm HE (M430) | MK19 | Grenade machine gun |
| B900 | 60mm Mortar HE | M224 | Light mortar |
| C516 | 81mm Mortar HE | M252 | Medium mortar |
| C748 | 120mm Mortar HE | M120 | Heavy mortar |
| D563 | 155mm HE (M107) | M777/M109 | Field Artillery |
| G811 | TOW Missile | M220 | ATGM |
| H490 | Javelin | CLU/RCU | ATGM — controlled item |

---

## CHAPTER 6 — PETROLEUM AND WATER OPERATIONS

**BLUF:** Petroleum (Class IIIB) and water (Class I-W) are among the most operationally critical supplies the sustainment force manages. MSS gives the 92F petroleum supply specialist and the 92W water treatment specialist real-time visibility of POL point status, bulk fuel distribution, and water source and distribution tracking.

### 6-1. Petroleum Supply Workflow in MSS

**MOS:** 92F (Petroleum Supply Specialist)
**Positions:** POL Sergeant, Petroleum Section Chief, Bulk Fuel Point Supervisor

**MSS POL Data Domain:**
- Fuel point status: location, capacity, current on-hand (by product type), throughput
- Distribution tracking: fuel tanker convoys, delivery confirmations
- Demand tracking: units served, quantities issued, consumption rate
- Pipeline status: (where applicable) pump station status, throughput

### 6-2. POL Point Status Tracking

**Task: Fuel Point Status Update**

**Conditions:** 92F assigned to FARP (Forward Arming and Refueling Point) or bulk fuel point. MSS access available. Current fuel quantities verified against meter readings and tank gauges.

**Standards:** MSS fuel point status updated twice daily (0700 and 1900) minimum, or as directed by SOP. On-hand quantities reflect actual meter-verified holdings — not estimated. Product type (MOGAS, JP-8, diesel) accurately entered by tank. Capacity percentage displayed accurately.

**Procedure:**

1. Read tank gauges or meters. Record actual on-hand quantity by product type.
2. Log into MSS. Navigate to Petroleum > Fuel Point Status.
3. Select your fuel point. Update on-hand quantities by product type.
4. Update throughput for previous 24-hour period: total gallons issued.
5. Record any operational status changes: point offline, limited capacity, contamination detected (see Note below).
6. If on-hand falls below 30% capacity, verify MSS threshold alert is active.
7. Record incoming deliveries: tanker serial number, quantity, product type, ETA.

> **CAUTION: If fuel contamination is suspected (water in fuel, product cross-contamination, foreign material), immediately suspend operations and report through chain of command. Update MSS fuel point status to "offline — contamination investigation" so that distribution planners reroute deliveries. Do not issue fuel pending contamination clearance.**

### 6-3. Bulk Fuel Distribution Tracking

Bulk fuel distribution in MSS uses the same convoy tracking framework as general cargo distribution (Chapter 4) but includes fuel-specific data fields:

**Fuel Convoy Additional Data Fields:**
- Product type (JP-8, MOGAS, diesel — do not mix)
- Tanker capacity vs. loaded quantity
- Flashpoint and handling requirements
- HAZMAT placard compliance confirmation

**Distribution Planning:**
- Fuel consumption rates by unit and equipment type are available in MSS planning factors
- Distribution scheduler compares consumption rate vs. on-hand to generate resupply trigger
- Priority allocation: MSS supports fuel allocation by priority when demand exceeds supply

### 6-4. LOGSTAT Fuel Status Reporting

The LOGSTAT requires Class III and Class IIIB status reporting from every echelon. MSS generates LOGSTAT fuel entries automatically from fuel point status data.

**LOGSTAT Fuel Fields (Standard):**
- Class IIIB on-hand (gallons)
- Class IIIB consumption previous 24 hours (gallons)
- DOS at current consumption rate
- Resupply requested (yes/no, quantity, ETA)
- Fuel point status (operational, limited, offline)

### 6-5. Water Treatment and Distribution Tracking

**MOS:** 92W (Water Treatment Specialist)
**Task: Water Status Update**

**Conditions:** 92W assigned to water point or water purification unit. Water source has been tested. Distribution operations are active.

**Standards:** MSS water status updated twice daily. Water source status (operational, contaminated, offline) current. On-hand distribution (gallons) accurate. Distribution rate by unit complete for previous 24 hours.

**Procedure:**

1. Complete water quality testing for current source. Record results.
2. Calculate on-hand potable water (distribution containers on-hand, bulk storage on-hand).
3. Log into MSS. Navigate to Field Services > Water Status.
4. Update water point status: source quality (pass/fail), on-hand gallons, capacity.
5. Record previous 24-hour distribution: total gallons issued, units served.
6. Calculate DOS at current consumption rate. Update MSS field.
7. If DOS falls below 3 days, verify MSS alert is active and notify S4.

> **WARNING: Do not distribute water that has failed quality testing. MSS water status must immediately reflect "offline — quality failure" when a source fails testing. Units planning water operations from MSS products will route distribution accordingly. Update MSS before any other coordination — downstream units depend on that status to find alternative sources.**

### 6-6. Fuel Planning Factors

The S4 uses standard fuel consumption planning factors to project demand and determine resupply requirements. MSS planning factor fields allow the S4 to load unit-specific consumption rates based on vehicle density and operational tempo.

**Table 6-1. Standard Fuel Consumption Planning Factors (JP-8, representative values)**

| Platform | Gallons per Hour (Idle) | Gallons per Mile (Road) | Notes |
|---|---|---|---|
| M1A2 SEP (Abrams) | ~0.9 | ~1.85 | Varies significantly with speed/terrain |
| M2/M3 Bradley | ~0.4 | ~1.2 | |
| M109A7 (Paladin) | ~0.4 | ~1.1 | |
| HMMWV (standard) | ~0.2 | ~0.35 | |
| LMTV 2.5-ton | ~0.2 | ~0.40 | |
| FMTV 5-ton | ~0.25 | ~0.55 | |
| HEMTT (10-ton) | ~0.35 | ~0.80 | |
| CH-47 (Chinook) | — | ~1.0 gal/NM (approx) | Aviation fuel — JP-8 common |
| UH-60 (Black Hawk) | — | ~0.8 gal/NM (approx) | Aviation fuel |

> **CAUTION: Planning factors above are approximate values for planning purposes only. Actual consumption varies with speed, terrain, temperature, and equipment condition. Always use unit historical consumption data from MSS trend analysis to refine planning factors before a major operation.**

### 6-7. Water Planning Factors and Class I-W Standards

**Minimum Water Requirements per Soldier per Day (FM 4-0 planning factors):**

| Condition | Minimum Potable Water | Total Requirement (incl. hygiene/cooking) |
|---|---|---|
| Temperate (< 80°F) | 1.5 gallons | 3.5 gallons |
| Hot (80–100°F) | 2.0 gallons | 5.0 gallons |
| Extreme heat (> 100°F) | 2.5+ gallons | 6.5+ gallons |
| Cold weather (< 32°F) | 2.0 gallons | 4.0 gallons (including heating) |

**MSS Water Planning Field Usage:**
- Enter unit strength in MSS water planning workspace
- Select environmental condition (temperate/hot/extreme/cold)
- MSS calculates daily water requirement and compares to current on-hand
- DOS calculation adjusts automatically when strength or consumption rate changes

---

## CHAPTER 7 — HUMAN RESOURCES AND PERSONNEL ACCOUNTABILITY

**BLUF:** The 42A HR specialist uses MSS to manage PERSTAT data, casualty tracking, personnel accountability for FFIR thresholds, and strength reporting to higher. Accurate personnel data is mission-critical — it directly affects the commander's ability to task-organize, assess risk, and comply with reporting requirements.

### 7-1. HR Specialist Workflow in MSS

**MOS:** 42A (Human Resources Specialist), 42H (Senior HR Sergeant)
**Positions:** S1 NCO, HR NCOIC, Strength Manager, Casualty Operations NCO

**MSS HR Data Domain:**
- Personnel strength by unit (assigned, present for duty, attached, AWOL, sick, detailed)
- PERSTAT data (unit-level and roll-up)
- Casualty tracking (WIA, KIA, MIA, NBC casualty)
- Awards and personnel actions pipeline
- Theater strength management (TSC/ESC level)

### 7-2. PERSTAT Management

**Task: PERSTAT Update and Submission**

**Conditions:** 42A assigned to S1 section. Unit morning formation accountability complete. Previous PERSTAT is on file. IPPS-A is accessible.

**Standards:** PERSTAT reflects current accountability as of formation. MSS strength dashboard updated within 2 hours of formation time. Discrepancies between unit PERSTAT and IPPS-A strength report documented and flagged for resolution. PERSTAT submitted to higher per unit SOP (typically daily at 0800 and 2000).

**Procedure:**

1. Collect accountability results from all subordinate units. Verify completeness.
2. Compile unit PERSTAT by category: assigned, present for duty, sick (in quarters, hospitalized), TDY, leave, AWOL, attached in, attached out, detailed.
3. Log into MSS. Navigate to Personnel > PERSTAT workspace.
4. Update unit strength data by category for each subordinate unit.
5. Verify roll-up total matches unit PERSTAT submitted to S3/S4 for LOGSTAT.
6. Review CCIR threshold alerts: if any unit falls below personnel FFIR threshold (configured by S1 in coordination with S3), confirm alert is active.
7. Submit PERSTAT to higher per SOP — confirm MSS roll-up product is available for higher's viewing.

### 7-3. Casualty Reporting Workflow in MSS

> **WARNING: Casualty data requires immediate handling IAW AR 638-8. MSS is a tracking tool — it does not replace the official casualty report (CASREP) submitted through chain of command. Enter initial casualty data in MSS for unit tracking, but ensure the official CASREP is submitted through S1 channels simultaneously. Casualty notification to next of kin is a command function governed by AR 638-8 — not driven by MSS data entry.**

**Task: Casualty Record Entry in MSS**

**Conditions:** Casualty has occurred within the unit. Initial report received. Verification in progress. CASREP has been submitted through official channels.

**Standards:** Casualty record entered in MSS within 1 hour of official CASREP submission. Status (WIA, KIA, MIA) accurately reflects current information. Record updated as status changes. All casualty records marked with classification level appropriate to the operational environment.

**Procedure:**

1. Receive official casualty information from company or subordinate unit.
2. Verify CASREP has been submitted through official channels (do not enter MSS data first).
3. Log into MSS. Navigate to Personnel > Casualty Tracking.
4. Create new casualty record: name (or SSN last four per security requirements), unit, date-time of incident, category (WIA, KIA, MIA, other), location (grid), brief description.
5. Link to CASREP document number if available.
6. Update PERSTAT to reflect strength change immediately.
7. Monitor for status updates. Update casualty record when status changes (e.g., WIA to RTD, WIA to KIA).

### 7-4. Personnel FFIR Thresholds

The Commander's Critical Information Requirements (CCIR) include Friendly Force Information Requirements (FFIR). Personnel strength is a common FFIR category.

**Standard Personnel FFIR Thresholds (example — unit commander determines actual values):**

| FFIR Category | Warning | Critical |
|---|---|---|
| Unit strength vs. required for mission | < 80% | < 70% |
| Effective strength (present for duty) | < 75% | < 65% |
| Casualty rate in 24-hour period | > 5% unit strength | > 10% unit strength |
| Medical evacuation rate | > 3% | > 5% |

**Configuring FFIR Thresholds in MSS:**
- S1 coordinates with S3 to establish FFIR thresholds aligned to commander's published CCIRs
- Thresholds entered by MSS Administrator or unit S6 in CCIR configuration workspace
- S1 receives automated alerts when thresholds are crossed; validates against PERSTAT; notifies S3 for commander briefing

### 7-5. Awards and Personnel Actions Tracking

**Personnel Actions Pipeline in MSS:**

MSS tracks the pipeline status for pending personnel actions: awards, promotions, re-enlistments, officer evaluations, NCOERs, and adverse actions. This replaces unit-maintained Excel trackers.

**Data Entry for Awards:**
- Soldier name and unit
- Award type
- Action initiation date
- Current status (submitted, endorsed, approved, returned)
- Suspense date
- Approving authority

> **NOTE: MSS personnel actions tracking is a unit-level management tool. It does not replace IPPS-A for official personnel action processing. Awards not processed in IPPS-A are not officially recorded — regardless of their status in MSS. Ensure all actions tracked in MSS are also submitted through IPPS-A.**

### 7-6. Theater Strength Management

At TSC and ESC level, theater strength management involves tracking personnel across the entire operational area — including deployed forces, transient personnel, and contractor personnel supporting the force.

**Theater Strength Data in MSS:**
- Total deployed strength by unit, echelon, and AOR sector
- Personnel in theater but not assigned to a permanent unit (transient strength)
- Contractor personnel supporting theater operations (LOGCAP, AFCAP, other)
- Strength requirements vs. fill rate for theater priority billets
- Replacement pipeline: personnel en route from CONUS or OCONUS to fill theater requirements

**Table 7-1. PERSTAT Category Definitions**

| Category | Definition | Notes |
|---|---|---|
| Assigned | On unit rolls; regardless of location | Reflects IPPS-A assignment data |
| Present for Duty (PDY) | Assigned, present at duty location, available for tasks | Primary operational strength metric |
| Sick (In Quarters) | Assigned; on profile; not hospitalized; limited duty | Available for administrative tasks, not physical |
| Hospitalized | Admitted to medical treatment facility | Not available; may affect FFIR |
| Leave (Authorized) | On official leave; scheduled return date known | Not available; date return known |
| TDY/School | Assigned; temporarily absent on orders | Not available; return date known |
| AWOL | Absent without authorization | Report to S2/MP per AR 630-10 |
| Attached In | Not on rolls; OPCON/TACON to unit; operationally available | Count toward effective strength for mission |
| Attached Out | On rolls; OPCON/TACON to another unit | Not available to parent unit |
| Detailed | Attached but not OPCON; performing specific supporting task | Limited availability to parent unit |

### 7-7. Finance and Pay Operations Coordination

**MOS:** 42R (Financial Management Technician) / 44B (Finance Specialist)

While financial management is a separate function from the standard S1 HR mission, MSS supports the coordination between S1 personnel data and finance pay operations.

**Finance-HR Integration Points:**
- Deployment entitlements: HFTP, CZTE, FSA, HFP — tracked against deployment dates in MSS
- Combat pay eligibility: linked to AOR entry dates maintained in personnel data
- Casualty pay actions: survivors' benefits, SBP coordination — casualty records link to finance actions
- Missing pay actions: Soldiers reporting pay discrepancies require cross-reference between IPPS-A and finance records

> **NOTE: Finance pay actions are not processed through MSS. MSS provides the personnel data framework that finance specialists use to verify entitlement eligibility. The authoritative record for all pay actions is IPPS-A and the Defense Joint Military Pay System (DJMS). MSS does not override or replace those systems.**

---

## CHAPTER 8 — FIELD SERVICES AND HEALTH SERVICE SUPPORT

**BLUF:** Field services — food service, laundry, bath, mortuary affairs — and coordination for health service support (HSS) require data tracking in MSS for LOGSTAT accuracy, accountability, and sustainment planning. This chapter covers 92G food service workflow, Class VIII coordination, property accountability exceptions, and services management.

### 8-1. Food Service Workflow in MSS

**MOS:** 92G (Food Service Specialist)
**Positions:** Food Service Sergeant, DFAC NCOIC, Class I OIC

**Task: Ration Cycle and Headcount Tracking**

**Conditions:** 92G assigned to dining facility or field kitchen. Ration draws are complete. Headcount records from previous meal are on file.

**Standards:** MSS ration status reflects current on-hand meals by type (MRE, UGR-H&S, UGR-A, B-ration). Headcount for previous 24 hours entered in MSS by 2100 daily. DOS calculation current. Ration requests to supply point submitted and reflected in requisition pipeline.

**Procedure:**

1. Record headcount for each meal period (breakfast, lunch, dinner) on DA Form 3032.
2. Calculate ration consumption vs. on-hand. Determine DOS at current consumption.
3. Log into MSS. Navigate to Field Services > Ration Cycle.
4. Enter headcount data for the meal periods since last update.
5. Update on-hand rations by type (MRE, UGR variant). Verify DOS calculation in MSS matches manual calculation.
6. Enter any ration requests submitted to supply point. Track request status in supply requisition pipeline.
7. Flag any quality or safety issues with rations (damaged packaging, expiration) in MSS notes.

**Table 8-1. Ration Type Reference**

| Ration Type | Context | Tracking Priority |
|---|---|---|
| MRE (Meal, Ready-to-Eat) | Combat, dismounted, emergency | High — DOS < 3 days triggers alert |
| UGR-H&S (Unitized Group Ration — Heat and Serve) | Field, limited cooking capability | High |
| UGR-A (Unitized Group Ration — A-ration) | Base camp with field kitchen | Medium |
| FSR (First Strike Ration) | Air assault, ranger operations | High — pre-mission planning |
| Class I-W (water) | All operations | High — see Chapter 6 |

### 8-2. Class VIII Coordination

Class VIII (medical materiel) is managed primarily by the Health Service Support (HSS) system — the medical logistics officer and medical supply NCO. The S4 section coordinates Class VIII visibility for LOGSTAT reporting.

**S4 / 92A Coordination with Medical Logistics:**
- S4 section receives Class VIII status inputs from medical platoon / BAS for LOGSTAT
- MSS reflects Class VIII as a coordination product — the source data is medical logistics, not S4
- S4 monitors that Class VIII status is reported; does not manage the medical supply chain
- Critical Class VIII shortages affecting treatment capability are reported to S3 for CCIR monitoring

> **NOTE: Class VIII accountability is a joint HSS-S4 responsibility. S4 ensures Class VIII is included in the LOGSTAT. Medical logistics officer ensures medical supply records are accurate. Do not allow Class VIII to be omitted from LOGSTAT because it is perceived as solely a medical function.**

### 8-3. Property Accountability: FLIPL and Report of Survey

In addition to FLIPL tracking in Chapter 3 (equipment), MSS tracks unit-level property accountability exceptions:

**Property Book Exception Tracking:**
- Open FLIPLs (see paragraph 3-5)
- Reports of Survey: initiated, appointing official assigned, findings due, adjudicated
- Shortage annexes (items missing from property book with pending investigation)
- Controlled item accountability (sensitive items inventories)

**Sensitive Item Inventory Compliance:**
- MSS tracks sensitive item inventory completion by unit
- Required frequencies: weapons/NVGs — daily; COMSEC — weekly; controlled items — as directed
- Units with overdue inventories flagged in MSS accountability dashboard

### 8-4. Services Management Data

**Laundry and Bath Services:**
- Capacity tracking: number of personnel served per day vs. capacity
- Schedule tracking: unit appointment windows for laundry/bath assets
- Status: operational, limited, offline

**Mortuary Affairs:**
> **WARNING: Mortuary affairs data is subject to strict privacy and handling requirements IAW AR 638-34. Mortuary affairs records in MSS must be handled at the appropriate classification level. Access to mortuary affairs data workspace must be restricted to authorized personnel only. Contact the unit S1 and Judge Advocate before entering or distributing any mortuary affairs data in MSS.**

### 8-4. Services Management Data

**Laundry and Bath Services:**
- Capacity tracking: number of personnel served per day vs. capacity
- Schedule tracking: unit appointment windows for laundry/bath assets
- Status: operational, limited, offline

**Mortuary Affairs:**
> **WARNING: Mortuary affairs data is subject to strict privacy and handling requirements IAW AR 638-34. Mortuary affairs records in MSS must be handled at the appropriate classification level. Access to mortuary affairs data workspace must be restricted to authorized personnel only. Contact the unit S1 and Judge Advocate before entering or distributing any mortuary affairs data in MSS.**

**Laundry, Bath, and Clothing Repair (LBCR) Unit Data:**
- LBCR unit capacity: pounds of laundry per day, bath facilities (shower units) throughput
- Unit scheduling: appointments by time window, units served per day
- Water consumption tracking: coordinates with Class I-W management (see Chapter 6)
- Chemical usage: detergent and supply consumption rate, DOS on-hand

### 8-5. Environmental Considerations and HAZMAT Tracking

Sustainment operations involve hazardous materials — fuel, ammunition, chemicals, and contaminated water. MSS tracks HAZMAT data for planning and incident response.

**HAZMAT Categories in MSS:**
- Bulk fuel (Class IIIB): fire hazard; tracks quantity, storage tank type, secondary containment compliance
- Ammunition: blast/fragment hazard; tracks storage location, quantity, safety distance requirements
- Petroleum products (packaged): flammable/explosive; tracks quantity by product
- Batteries (lead acid, lithium): chemical hazard; tracks quantity for storage planning
- Solvents and chemicals (maintenance shop): tracks storage compliance

**Spill Reporting:**
- Any spill exceeding the reportable quantity (RQ) per 40 CFR must be reported to the installation environmental office
- MSS incident record: date/time, material spilled, quantity, location, initial response actions taken
- Coordinate with unit environmental coordinator (UEC) for proper reporting procedures

> **CAUTION: Environmental spill reporting requirements exist under federal law (CERCLA, RCRA) and SOFA agreements in USAREUR-AF. Failure to report a qualifying spill can result in personal and command liability. Update MSS with spill incident data, but ensure the official report goes through the installation environmental office simultaneously — MSS tracking does not constitute official reporting.**

---

## CHAPTER 9 — ECHELON-SPECIFIC SUSTAINMENT OPERATIONS

**BLUF:** MSS use varies by echelon. A company supply sergeant uses MSS differently than a TSC S4. This chapter provides echelon-specific guidance for company/battery through theater-level sustainment operations.

### 9-1. Company / Battery Level

**Primary Users:** Supply sergeant (92Y), motor sergeant (91Z), first sergeant (PA)
**Primary MSS Products Consumed:** Unit supply status, vehicle readiness, PERSTAT

**Company Supply Sergeant (92Y) Tasks:**
- Maintain unit basic load data in MSS: Class I, III, V, IX status
- Update PMCS status for motor pool (coordinates with motor sergeant)
- Submit daily supply status input to BSB/FSB S4 workspace through MSS
- Track Class IX requisitions through supply pipeline — notify platoon leaders of EDD for deadline parts

**Motor Sergeant (91Z) Tasks:**
- Update deadline equipment status in MSS daily (coordinates with 92A/91A on parts)
- Track work order status for deadline equipment
- Ensure GCSS-Army / SAMS-E entries are current before submitting MSS LOGSTAT data

**First Sergeant (Personnel Accountability):**
- Verify PERSTAT is updated in MSS after each formation
- Review strength data for FFIR threshold monitoring
- Coordinate with S1 for PERSTAT discrepancy resolution

### 9-1a. Company-Level Sustainment Data Entry Standards

The accuracy of the sustainment picture in MSS depends on disciplined data entry at the lowest echelon — the company. The following standards apply to all company-level sustainment data entry.

**Supply Sergeant (92Y) Standards:**
- Update supply room on-hand quantities in GCSS-Army same day as receipt or issue
- Submit LOGSTAT contribution to BSB supply workspace by time directed in SOP (typically 0700)
- Flag any shortages below threshold immediately — do not wait for the morning LOGSTAT

**Motor Sergeant (91Z) Standards:**
- Enter all new deadlines in SAMS-E within 4 hours of morning motor pool
- Close work orders in SAMS-E the same day repairs are completed
- Submit Class IX requisitions in GCSS-Army on the same day the work order is opened

**First Sergeant (Personnel) Standards:**
- Complete accountability before submitting PERSTAT — never submit before formation
- Update MSS PERSTAT within 1 hour of formation time
- Report any status change (casualty, emergency leave, AWOL) immediately to S1

**Table 9-2. Company Data Entry Standards Summary**

| Data Element | Source System | MSS Update | Responsible |
|---|---|---|---|
| Supply on-hand | GCSS-Army | Automated (same day as GCSS-Army entry) | 92Y |
| New requisitions | GCSS-Army | Automated | 92Y |
| New deadlines | SAMS-E | Automated (within 4 hours) | 91Z |
| Work order closures | SAMS-E | Automated (same day) | 91Z |
| PERSTAT | Unit formation | Manual entry | First Sergeant |
| Sensitive item inventory | Physical count | Manual confirmation | Supply Sergeant |

### 9-2. BSB — Brigade Support Battalion

**Primary Users:** BSB S4 section, distribution company commander, support company NCOIC
**Primary Products:** LOGSTAT rollup for brigade, distribution scheduling, Class I–III–V status

**BSB S4 Section Workflow:**
1. Receive LOGSTAT inputs from all supported battalions through MSS at SOP-directed time
2. Compile brigade-level LOGSTAT: aggregate supply, maintenance, transportation, and personnel status
3. Review threshold alerts: identify battalions below critical thresholds in any supply class
4. Coordinate distribution priorities: allocate limited supplies to highest-priority units per brigade S4 guidance
5. Submit brigade LOGSTAT to DIV G4 through MSS at prescribed time

**Distribution Company Coordination:**
- Distribution company tracks all active convoys in MSS (see Chapter 4)
- Delivery confirmations from all distribution runs updated in MSS before daily LOGSTAT
- Convoy scheduling for next 24–48 hours visible to BSB S4 for deconfliction

**Table 9-1. BSB Daily MSS Product Schedule**

| Time | Product | Responsible Section |
|---|---|---|
| 0600 | Unit PERSTAT from each supported BN | S1 NCOs |
| 0700 | Class I–III–V status from supply points | 92A/92F |
| 0800 | Maintenance status from all supported BNs | Maintenance OIC |
| 0900 | LOGSTAT compilation complete | BSB S4 |
| 1000 | Brigade LOGSTAT submitted to DIV G4 | BSB S4 |
| 1600 | PM supply/maintenance update | 92A/91Z |
| 2000 | PERSTAT evening update | S1 |

### 9-3. Division / COSCOM Level

**Primary Users:** DIV G4 section, DISCOM/COSCOM sustainment brigade staff
**Primary Products:** Division LOGSTAT, sustainment synchronization, distribution prioritization

**G4 Section Workflow:**
1. Receive brigade-level LOGSTATs from all three (or more) maneuver brigades via MSS
2. Aggregate division-level supply, maintenance, transportation status
3. Identify division-level shortfalls: supplies below sustainment level that require ESC/TSC action
4. Prepare division sustainment synchronization matrix: which brigades get priority resupply, which convoys are scheduled, what theater-level support is requested
5. Submit division LOGSTAT to Corps/ESC per SOP

**Sustainment Brigade Synchronization:**
- Sustainment brigade at division operates CSS Area Operations — coordinating BSB support across multiple brigades
- MSS enables synchronization by showing all brigades' status simultaneously
- Sustainment brigade S4 uses MSS to identify and resolve cross-brigade distribution conflicts

### 9-4. TSC / ESC — Theater Sustainment

**Primary Users:** TSC and ESC G4 staff, theater distribution management center (TDMC)
**Primary Products:** Theater distribution picture, ASL status, HNS tracking, strategic LOC monitoring

**Theater-Level MSS Products:**
- **Theater distribution picture**: all active distribution convoys, rail movements, waterway shipments across the theater
- **ASL (Authorized Stockage List) status**: forward stocks vs. requirement, days forward
- **Host Nation Support (HNS) tracking**: contracted logistics support, HNS agreement execution status, contractor availability
- **Strategic LOC monitoring**: key lines of communication status — bridges, road segments, rail choke points, ports
- **Theater LOGSTAT**: aggregation of all division-level LOGSTATs into theater supply status picture

**HNS Tracking in MSS:**
- HNS contracts and agreements visible by support category (fuel, transportation, billeting, engineering)
- Performance tracking: HNS delivery vs. contracted quantity and schedule
- Issue tracking: contractor performance problems, HNS availability changes

### 9-5. Corps / ASCC Level

**Primary Users:** Corps G4, ASCC G4, Theater Army G4
**Primary Products:** Theater-level readiness assessment, strategic LOC risk assessment, LOGSTAT synthesis

At corps and ASCC level, MSS is primarily a strategic-to-operational integration tool. The volume of data from subordinate formations requires aggregation into theater-level views that senior leaders can use for campaign planning and resource allocation.

**Corps G4 MSS Products:**
- **Theater distribution picture**: aggregate of all division and brigade LOGSTATs — DOS status, equipment readiness, personnel strength by echelon
- **Strategic supply risk dashboard**: Class I, III, V status across theater against 30-day consumption projections
- **Host Nation Support compliance**: HNS agreement execution vs. contract; payment status; performance tracking
- **SOFA and LOC monitoring**: theater road, rail, and waterway status affecting strategic sustainment
- **Contractor logistics (LOGCAP/AFCAP) status**: performance metrics, cost-to-task, contractor strength in theater

**Planning Support:**
- Corps G4 uses MSS to support campaign planning — specifically the logistics feasibility analysis for concept plans (CONPLANs) and OPLANs
- MSS sustainment data feeds the logistics preparation of the theater (LPT) process
- Supply risk products inform the corps commander's decisions on operational sequencing and phasing

### 9-6. Multi-National and Joint Considerations

USAREUR-AF operations are inherently multi-national and joint. MSS is a U.S. Army platform; it does not natively integrate data from allied nation logistics systems. However, MSS can be used to coordinate sustainment support to and from allied partners.

**Allied Nation Coordination:**
- HNS agreements tracked in MSS by support category, providing nation, and execution status
- Multinational logistics arrangements (role specialization) tracked: which nation provides Class III, which provides medical support
- Liaison officer (LNO) data coordination: allied LNOs can be granted MSS access for coordination products

**Joint Logistics Enterprise (JLEnt) Interface:**
- JLOC (Joint Logistics Operations Center) products visible in MSS through theater sustainment workspace at TSC/ESC level
- Army component sustainment data feeds the joint picture; MSS provides the Army data layer
- Coordinate with theater J4 for joint logistics product requirements that must be built on or fed to MSS

---

## CHAPTER 10 — DEGRADED OPERATIONS

**BLUF:** MSS will experience outages. Sustainment operations cannot stop. This chapter provides the PACE plan for sustainment data, manual LOGSTAT fallback procedures, and reconstitution procedures for restoring MSS sustainment workspace after an outage.

### 10-1. When MSS Is Degraded

MSS degradation can result from:
- Network connectivity loss (tactical network, VPN, garrison connectivity)
- Foundry platform maintenance or outage
- User account or permission issues
- Data pipeline failure (GCSS-Army feed is down, not MSS itself)

**First Actions on MSS Degradation:**
1. Verify whether the issue is local (workstation/network) or platform-wide. Contact unit S6.
2. Notify S4 and higher S4 that MSS reporting capability is degraded.
3. Activate manual LOGSTAT procedures (see paragraph 10-2).
4. Continue all sustainment operations using authoritative source systems (GCSS-Army, SAMS-E remain operational).
5. Record all data that would have been entered in MSS in the manual backup format.

### 10-2. Manual LOGSTAT Procedures

**The LOGSTAT does not stop because MSS is unavailable.**

**Manual LOGSTAT Format (Minimum Required Data):**

Use the standard LOGSTAT format IAW FM 4-0 Appendix D. At a minimum, the manual LOGSTAT must capture:

- Unit, DTG, grid location
- Class I: on-hand DOS, consumption previous 24 hours
- Class IIIB: on-hand gallons, consumption previous 24 hours, DOS
- Class V: basic load % by primary weapon system
- Class IX: PLL fill rate %, critical shortages
- Equipment: total authorized / total on-hand / FMC / NMC (NMCS/NMCM)
- Personnel: assigned / present for duty / WIA / KIA / MIA
- Significant sustainment events: convoy contacts, supply point disruptions, maintenance anomalies

**Submit manual LOGSTAT via:**
- **Primary**: Encrypted email or SIPR message to higher S4
- **Alternate**: Voice (secure) to higher S4 with written record
- **Contingency**: FM radio voice report using standard LOGSTAT format
- **Emergency**: Runner or liaison officer with hard-copy LOGSTAT

### 10-3. PACE Plan for Sustainment Data

**Table 10-1. Sustainment PACE Plan**

| Method | System | Conditions for Use |
|---|---|---|
| Primary | MSS — full LOGSTAT, automated dashboards | MSS and network fully operational |
| Alternate | GCSS-Army direct reports + S4 manual compilation | MSS unavailable; GCSS-Army operational |
| Contingency | Manual LOGSTAT forms + encrypted email/voice | Both MSS and GCSS-Army access unavailable |
| Emergency | Voice radio + runner + hard-copy DA forms | All digital systems unavailable |

### 10-4. Priority Sustainment Products Without MSS

When MSS is unavailable, sustain the following products manually in priority order:

1. **LOGSTAT** — non-negotiable; required by higher regardless of system status
2. **PERSTAT** — personnel accountability is required; compile from unit first-sergeant reports
3. **Equipment readiness** — pull from SAMS-E directly; compile manually by company
4. **Ammunition basic load status** — pull from SAAS-MOD; compile by unit
5. **Distribution tracking** — use convoy manifests and radio checkpoint reports; maintain paper convoy log

### 10-5. Reconstitution of Sustainment Workspace After Outage

After MSS is restored following an extended outage:

**Procedure:**

1. Do not immediately accept MSS data as current. Verify data-as-of timestamps for all products.
2. Identify the "gap window" — period for which MSS data was not updated.
3. Enter all data from the gap window into source systems (GCSS-Army, SAMS-E) first.
4. Allow MSS feeds to update from authoritative sources. Do not manually enter data that should come from a GCSS-Army feed — it will be overwritten.
5. Reconcile MSS LOGSTAT products against the manual LOGSTATs submitted during the outage. Document discrepancies.
6. Notify higher S4 that MSS has been reconstituted and current status is verified as of specific DTG.
7. Brief S4 on any significant data gaps that could not be recovered (e.g., convoy status during outage that was not manually recorded).

> **NOTE: After an extended MSS outage, the first LOGSTAT submitted from MSS must be annotated with the data reconstitution DTG: "MSS reconstituted as of [DTG]. Data prior to [DTG] may not be reflected in pipeline." This prevents higher from treating a reconstituted product as continuously-updated data.**

### 10-6. Network-Degraded vs. MSS-Degraded — Distinguishing the Failure Mode

Not all MSS outages are the same. The response depends on what is degraded.

**Table 10-2. MSS Degradation Types and Responses**

| Failure Mode | Symptoms | Response |
|---|---|---|
| User authentication failure | Individual user cannot log in; others can | S6 or C2DAO account issue. Submit ticket. Continue on other workstation or request colleague access. |
| Local network failure | No MSS access from specific location; others on different network can access | S6 network troubleshooting. Consider relocating to alternate network node. |
| GCSS-Army feed down | MSS accessible but supply/maintenance data is stale/frozen | Annotate in MSS that data is frozen. Use GCSS-Army direct access for current data. Note feed outage on LOGSTAT. |
| Foundry platform outage | MSS inaccessible across theater or for all users | Platform-wide outage. Notify S6. Activate full manual LOGSTAT procedures. Estimated recovery time from C2DAO. |
| Workspace misconfiguration | Products visible but displaying incorrect data | Unit MSS administrator or C2DAO investigation required. Do not brief misconfigured data. |

### 10-7. Sustainment Common Operating Picture — Reconstitution Priority

After MSS is restored, reconstitute the sustainment COP in priority order:

1. **PERSTAT** — update strength data first; commander needs personnel accountability before any other sustainment picture
2. **Equipment readiness** — enter all gap-period SAMS-E updates; reconcile FMC/NMC status
3. **Class V (Ammunition)** — basic load status is safety and mission-critical; update before fires operations resume
4. **Class IIIB (Fuel)** — POL status for ongoing or planned operations
5. **Class I (Rations)** — DOS update to reflect any consumption and resupply during gap period
6. **Class IX (Parts)** — update requisition pipeline; enter any receipts processed during outage
7. **Distribution status** — close all convoys that completed during outage; update delivery confirmations
8. **Personnel actions** — awards, casualties, and other actions can be entered after operational data is current

### 10-8. Sustainment Battle Rhythm Integration

The sustainment battle rhythm synchronizes MSS data products with decision-making events. Table 10-3 provides a standard sustainment battle rhythm framework that integrates MSS products.

**Table 10-3. Sustainment Battle Rhythm Framework (BSB Level — example)**

| Event | Frequency | MSS Product Used | Data Input Required Before |
|---|---|---|---|
| Morning supply status review | Daily | Supply Status dashboard | Unit supply update (0700) |
| Distribution Synchronization Meeting (DSM) | Daily | Distribution dashboard, MOVREQ pipeline | Vehicle status, pending MOVREQs |
| Maintenance status review | Daily | Maintenance/Readiness dashboard | SAMS-E updates, new deadlines |
| LOGSTAT compilation | 2x daily (0900/2100) | LOGSTAT dashboard | All supply, maint, PERSTAT data |
| Sustainment Update Brief | Daily | Consolidated LOGSTAT product | LOGSTAT compilation complete |
| Weekly readiness review | Weekly | Readiness trend, PMCS compliance | Current SAMS-E data, all work orders |
| Class V review (with fires) | As required / battle rhythm | Ammunition dashboard | SAAS-MOD update, CSR allocation |

---

## APPENDIX A — SUSTAINMENT-SPECIFIC NAMING CONVENTIONS IN MSS

Consistent naming enables search, reporting, and cross-unit data sharing. Follow these conventions for all sustainment data entries in MSS.

**A-1. Unit Designations**

Use the standard Army unit designation format: [Size]-[Branch]-[Function]-[Parent Unit]

Examples:
- `BSB-1-4IN` — BSB supporting 1st Battalion, 4th Infantry
- `FSC-2-68AR` — Forward Support Company, 2nd Battalion, 68th Armor
- `CSSB-18` — 18th Combat Sustainment Support Battalion

**A-2. Supply Status Entries**

Format: `[CLASS]-[UNIT]-[YYYYMMDD]`

Example: `CL1-BSB-1-4IN-20260315`

**A-3. Maintenance Work Order References**

Format: `WO-[UNIT]-[EQUIPMENT]-[YYYYMMDD]-[SEQ]`

Example: `WO-FSC-2-68AR-M1A2-20260315-001`

**A-4. Convoy Serial Numbers**

Follow unit SOP. Recommend: `[UNIT ABBR]-[YYYY]-[JULIAN DAY]-[SEQ]`

Example: `BSB-2026-074-003`

**A-5. LOGSTAT Products**

Format: `LOGSTAT-[UNIT]-[DTG]`

Example: `LOGSTAT-2BCT-300800ZMAR26`

### A-6. Personnel Action Naming

Format: `PA-[TYPE]-[UNIT]-[YYYYMMDD]`

Examples:
- `PA-AWARD-1PLT-A-2-68AR-20260315` — Award action
- `PA-PROMO-HHC-1-4IN-20260315` — Promotion action

### A-7. Fuel Point Designations

Format: `FARP-[NAME]-[YYYYMMDD]` or `POL-[NAME]-[YYYYMMDD]`

Examples:
- `FARP-WHISKEY-20260315`
- `POL-MAINPT-20260315`

---

## APPENDIX B — LOGSTAT REPORT FIELDS AND STANDARDS

### B-1. LOGSTAT Submission Standards

**Frequency:** As directed by higher SOP; standard is twice daily (0900 and 2100 local) during deployed operations.
**Format:** MSS-generated export product, or manual format IAW FM 4-0 Appendix D when MSS is unavailable.
**Distribution:** Submit to higher S4/G4 section via approved means (SIPR email, MSS push, voice with written record to follow).
**Currency standard:** LOGSTAT must reflect data no older than 8 hours. Data older than 8 hours must be annotated with actual data collection time.

**Table B-1. LOGSTAT Standard Fields IAW FM 4-0**

| Field | Required | Standard | Notes |
|---|---|---|---|
| Unit | Yes | Standard unit designation | BCT, BN, or separate company |
| DTG | Yes | 6-digit DTG + zone | Must be current to within 2 hours |
| Location | Yes | 8-digit grid | Current main CP location |
| Class I | Yes | DOS on-hand | Minimum 3 DOS required for C-1 |
| Class IIIB | Yes | Gallons + DOS | Both bulk and packaged |
| Class V | Yes | % of basic load | By primary weapon system if space permits |
| Class IX | Yes | PLL fill rate % | Separate NMCS count if available |
| Equipment | Yes | Auth/OH/FMC/NMC | Include NMC subcategory (NMCS/NMCM) if reported |
| Personnel | Yes | Assigned/PDY/Cas | WIA/KIA/MIA on separate line |
| Resupply requested | Yes | Yes/No; if Yes, specify class and quantity | |
| Significant events | As required | Any events affecting sustainment posture | |

### B-2. LOGSTAT Quality Control Checklist

Before submitting any LOGSTAT from MSS, verify:

- [ ] Data-as-of timestamp verified for all supply class entries (within 8 hours)
- [ ] Equipment readiness count matches SAMS-E current output (no variance > 1 vehicle)
- [ ] PERSTAT matches last confirmed formation accountability
- [ ] Class V basic load verified against SAAS-MOD (not solely MSS display)
- [ ] All threshold-breaching items have resupply requests submitted (document request number)
- [ ] Significant sustainment events from past 24 hours documented in remarks
- [ ] LOGSTAT annotated with MSS reconstitution DTG if applicable (see para 10-5)

---

## APPENDIX C — SUPPLY CLASS QUICK REFERENCE

**Table C-1. Army Supply Classes Reference**

| Class | Contents | Key Planning Factors |
|---|---|---|
| I | Subsistence (food, water) | 3 DOS minimum; 72-hour assault load minimum |
| II | Clothing, tools, hand tools, OCIE | Managed by unit supply; SB 700-20 governs |
| III | POL — packaged | 3 DOS minimum; includes lubricants, oil |
| IIIB | POL — bulk fuel | 3 DOS minimum; JP-8 (aviation), MOGAS, diesel |
| IV | Construction/barrier material | Mission-dependent; stockage based on engineer plan |
| V | Ammunition | 100% ABL; ASR/CSR management |
| VI | Personal demand items | Unit manages; sold through AAFES or unit fund |
| VII | Major end items | AUTH = MTOE; readiness = FMC rate |
| VIII | Medical material | HSS responsibility; S4 tracks for LOGSTAT |
| IX | Repair parts, components | PLL fill rate ≥ 80% required; EDD on all back-orders |
| X | Agricultural/nonmilitary programs | USAREUR-AF specific; stability operations |

### C-1. Supply Class Resupply Triggers

**Table C-2. Standard Resupply Trigger Points**

| Supply Class | Resupply Request Trigger | Emergency Resupply Trigger |
|---|---|---|
| I (Rations) | 3 DOS on-hand | 1 DOS on-hand |
| II (Clothing/tools) | Below 80% fill on critical items | Commander directed |
| III (Packaged POL) | 3 DOS on-hand | 1 DOS on-hand |
| IIIB (Bulk fuel) | 30% capacity | 15% capacity |
| IV (Construction) | Mission-dependent | Commander directed |
| V (Ammunition) | Basic load below 90% | Basic load below 70% |
| VII (End items) | NMC creates C-3 status | NMC for P1 mission equipment |
| VIII (Medical) | Coordinated with HSS; 7-day supply | 3-day supply |
| IX (Repair parts) | PLL below 80% fill | PLL below 60% fill; NMCS deadline on P1 equipment |

---

## APPENDIX D — MAINTENANCE PRIORITY MATRIX

**Table D-1. Maintenance Priority Matrix**

| Priority | Code | Criteria | Required Action Timeline |
|---|---|---|---|
| Emergency | P1 | Current combat operations degraded; combat mission failure imminent | Immediate; work through all available means; notify chain of command |
| Urgent | P2 | Combat readiness will degrade within 24 hours without repair; operation planned within 48 hours | Begin repair within 4 hours; daily tracking; escalate if EDD > 24 hours |
| Routine | P3 | Equipment not required for current operations; can wait 72+ hours | Schedule within normal workload; track in SAMS-E |
| Deferred | P4 | Garrison or administrative maintenance; no operational impact | Schedule around operational requirements; not tracked in operational LOGSTAT |

**Notes on Priority Assignment:**
- Priority assigned by maintenance officer or 91Z maintenance sergeant
- P1 and P2 require notification to S4 and commanding officer
- Equipment supporting P1 operations takes precedence over all other work orders
- Priority may change as the operational situation changes — review priority list daily

### D-1. Equipment C-Rating Criteria (IAW AR 700-138)

**Table D-2. Equipment C-Rating Thresholds**

| C-Rating | Equipment Readiness Level | Combat Capability |
|---|---|---|
| C-1 | ≥ 90% FMC | Unit has required resources; fully capable |
| C-2 | 80–89% FMC | Unit has most required resources; minor shortfalls |
| C-3 | 70–79% FMC | Unit has less than required resources; significant shortfalls |
| C-4 | < 70% FMC | Unit requires additional resources; not able to perform all missions |
| C-5 | N/A | Unit is forming, activating, or rebuilding (non-deployable) |

> **NOTE: Equipment C-rating is one of four resource readiness factors reported in the DRRS-A (Defense Readiness Reporting System — Army). The overall unit readiness assessment integrates personnel, equipment (on-hand), training, and leadership ratings. MSS tracks the equipment and personnel components; training data feeds from DTMS. The unit commander provides the leadership/command climate assessment. All four components feed the unit's overall C-rating briefed to higher.**

---

## APPENDIX E — DISTRIBUTION SYNCHRONIZATION CHECKLIST

Use this checklist before every distribution synchronization meeting or LOGSTAT submission.

**Distribution Data Verification:**
- [ ] All active convoys in MSS show current checkpoint status
- [ ] No convoy is overdue at checkpoint (> 30 min past scheduled time)
- [ ] Upcoming convoys for next 24 hours have complete data entered (cargo, route, manifest)
- [ ] All MOVREQ requests in "approved" status have been assigned to a convoy package
- [ ] Vehicle availability is current (morning inspection results reflected)
- [ ] Hazmat declarations complete for any Class V or Class III convoys

**Supply Status Verification:**
- [ ] Class I, III, V, IX status current (within 8 hours)
- [ ] All threshold alerts reviewed and acknowledged
- [ ] Resupply requests submitted for all below-threshold classes
- [ ] Distribution priorities confirmed with S4 for limited assets

**Personnel and Equipment Verification:**
- [ ] Convoy commander and driver manifests complete for all convoys
- [ ] Escort requirements confirmed if applicable
- [ ] Vehicle maintenance status confirms all assigned vehicles are FMC or PMC (capable of mission)

---

## GLOSSARY

**ABL (Authorized Basic Load).** The quantity of Class V ammunition a unit is authorized to carry on its organic vehicles and equipment. ABL fill rate is the percentage of the ABL actually on-hand.

**AFCAP (Air Force Contract Augmentation Program).** Contractor logistics support program analogous to LOGCAP for Air Force-managed requirements.

**AR 700-138.** Army Regulation governing equipment readiness reporting, including C-rating criteria and LOGSTAT procedures.

**ASL (Authorized Stockage List).** Pre-positioned stocks of supplies at a support activity, sized to provide immediate issue to supported units pending resupply from higher echelon.

**ASR (Ammunition Supply Rate).** The number of rounds per weapon per day of fire that can be sustained based on estimated supply rates (FM 6-0).

**BSB (Brigade Support Battalion).** The primary sustainment unit for a Brigade Combat Team; provides supply, maintenance, transportation, and medical support.

**CSSB (Combat Sustainment Support Battalion).** A modular sustainment battalion that provides area sustainment support to forces in its operational area.

**CSR (Controlled Supply Rate).** The amount of ammunition allocated by the commander for each weapon per day based on tactical requirements and available stocks.

**DOS (Days of Supply).** A quantity of supplies required to support operations for a specified number of days.

**EDD (Estimated Delivery Date).** The projected date a requisitioned item will be delivered to the requesting unit.

**ESC (Expeditionary Sustainment Command).** A theater Army logistics headquarters that provides command and control for sustainment operations in an operational area.

**FLIPL (Financial Liability Investigation of Property Loss).** The Army process for determining accountability for lost, damaged, or destroyed government property.

**GCSS-Army (Global Combat Support System — Army).** The Army's primary supply chain management system; the authoritative system of record for supply transactions.

**HNS (Host Nation Support).** Materiel, facilities, services, and support provided by a host nation to an Army force in its territory.

**LOGSTAT (Logistics Status Report).** The recurring report submitted by sustainment units to report Class I–IX status, equipment readiness, and personnel accountability.

**MTOE (Modified Table of Organization and Equipment).** The authorization document that prescribes the number, type, and quantity of personnel and equipment for a unit.

**NMC (Not Mission Capable).** Equipment status indicating a system cannot perform its primary mission. NMCS — not mission capable, supply (awaiting parts). NMCM — not mission capable, maintenance (awaiting labor).

**PERSTAT (Personnel Status Report).** The daily report of unit personnel strength by category.

**PLL (Prescribed Load List).** A list of repair parts and tools authorized and pre-positioned at unit level for immediate maintenance use.

**PMCS (Preventive Maintenance Checks and Services).** Regularly scheduled checks and services performed on equipment to prevent failure and extend operational life.

**POL (Petroleum, Oils, and Lubricants).** General term for Class III and Class IIIB supplies.

**SAAS-MOD (Standard Army Ammunition System — Modernization).** The Army's primary ammunition management system.

**SAMS-E (Standard Army Maintenance System — Enhanced).** The Army's maintenance management information system for work order management and equipment readiness.

**TSC (Theater Sustainment Command).** The senior Army logistical headquarters in a theater of operations.

**TDMC (Theater Distribution Management Center).** The TSC element that manages theater-level distribution coordination, including rail, waterway, air, and road transport across the operational theater.

**DODIC (Department of Defense Identification Code).** A four-character alphanumeric code that identifies a specific ammunition item for accounting and requisitioning purposes.

**DRMO (Defense Reutilization and Marketing Office).** The organization responsible for disposal, reuse, or sale of excess government property — including deadlined equipment condemned by maintenance.

**DSM (Distribution Synchronization Meeting).** The regularly scheduled battle rhythm event where the S4 section deconflicts distribution requirements and allocates transportation assets for the next 24–48 hours.

**FARP (Forward Arming and Refueling Point).** A temporary facility organized and operated by aviation units to provide fuel and ammunition to aviation assets in support of operations.

**FMC (Fully Mission Capable).** Equipment status indicating a system meets all requirements for its primary mission.

**FSB (Forward Support Battalion).** A type of support battalion at division level that provides direct support to maneuver brigades.

**HAZMAT (Hazardous Material).** Any material that poses a threat to health, safety, or the environment, including fuels, ammunition, batteries, solvents, and chemicals.

**IPPS-A (Integrated Personnel and Pay System — Army).** The Army's enterprise HR and pay system; authoritative system of record for personnel transactions and strength data.

**JLOC (Joint Logistics Operations Center).** The joint logistics coordination center at theater level responsible for synchronizing joint logistics across all services.

**LOGCAP (Logistics Civil Augmentation Program).** The Army contractor logistics support program that provides a wide range of logistics services to support deployed forces.

**LPT (Logistics Preparation of the Theater).** The process of establishing the theater logistics infrastructure and supply stockage before major operations begin.

**MSR (Main Supply Route).** A route designated by competent authority over which the bulk of traffic flows in support of military operations.

**NMCM (Not Mission Capable, Maintenance).** Equipment deadlined awaiting labor to complete repairs; parts are available.

**NMCS (Not Mission Capable, Supply).** Equipment deadlined awaiting parts; repair labor is available but parts have not arrived.

**NSN (National Stock Number).** A 13-digit number used to identify and requisition items in the Army supply system.

**OR Rate (Operational Readiness Rate).** Percentage of vehicles in a fleet that are fully or partially mission capable and available for operations.

**PBUSE (Property Book Unit Supply Enhanced).** The Army's property book management system; used for property accountability at unit and property book officer level.

**PMC (Partially Mission Capable).** Equipment status indicating a system has one or more faults but can still perform its primary mission.

**SAAS-MOD (Standard Army Ammunition System — Modernization).** The Army's primary ammunition management system for accounting, requisitioning, and reporting ammunition at ASP and unit level.

**SOFA (Status of Forces Agreement).** An agreement defining the legal status of military forces operating in a host nation; affects property disposition, HAZMAT reporting, and contractor operations in USAREUR-AF.

**UEC (Unit Environmental Coordinator).** The unit-level officer or NCO responsible for environmental compliance, HAZMAT management, and spill reporting.

---

*TM-40D, Version 1.0, March 2026*
*Headquarters, United States Army Europe and Africa, Wiesbaden, Germany*
*UNCLASSIFIED // FOR OFFICIAL USE ONLY*
