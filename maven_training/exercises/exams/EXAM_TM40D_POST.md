# POST-TEST — TM-40D: SUSTAINMENT
## Maven Smart System (MSS) — USAREUR-AF

| Field | Detail |
|---|---|
| **Course** | TM-40D: Sustainment WFF Track |
| **Form** | Post-Test |
| **Level** | TM-40D (WFF Track) |
| **Audience** | G4/S4 staff, FSB/BSB logistics officers, supply chain managers, property book officers; prerequisite: completion of TM-40D training |
| **Time Allowed** | 30 minutes |
| **Passing Score** | 80% (32/40 points) |

---

## INSTRUCTIONS

This assessment confirms proficiency upon completion of TM-40D training. A score of 80% (32/40) is required for course completion certification. Results are recorded on the student training record.

---

## SECTION 1 — MULTIPLE CHOICE

*Circle the letter of the best answer. (2 points each)*

**1. You configure a CCIR in MSS to alert when Class III (B) supply on hand falls below a 2-day consumption threshold. The alert fires during a test, but the S4 officer says the battalion just reported full tanks this morning. The most likely cause is:**

A. Class III CCIRs have a 6-hour delay built into the system by design
B. The CCIR is configured against an older dataset that predates the morning LOGSTAT submission — the live feed has not yet propagated to the dashboard layer the CCIR is monitoring
C. The alert threshold was set too high and needs to be reconfigured
D. The battalion's morning report was submitted incorrectly and should be corrected before continuing

**2. A property book officer builds a property accountability display in MSS. A unit commander asks why the display shows three vehicles on hand when two are currently deadlined at the maintenance shop. The correct explanation is:**

A. MSS tracks physical vehicle location by GPS and should show current status automatically
B. The MSS display reflects reported on-hand quantity from the property book submission — maintenance status requires a separate data source (equipment readiness feed) that must be linked separately
C. Deadlined vehicles are automatically removed from property book data when they enter the maintenance system
D. The property book officer entered the wrong quantity during the last data load

**3. During a sustainment synchronization, the readiness dashboard shows 2nd FSC at 88% equipment readiness. The FSC commander reports they are at 61% due to three vehicles deadlined for parts this week. The S4 officer's correct action is:**

A. Brief the dashboard figure — MSS data supersedes verbal reports
B. Note the discrepancy, verify through the readiness reporting channel when the last FSC LOGSTAT was submitted, caveat the dashboard figure with data-as-of time, and brief the actual reported status the commander provided
C. Pull the FSC commander out of the sync to correct the data before continuing
D. File a data quality report and delay the sync until MSS is updated

**4. An S4 wants to use MSS supply chain analytics to forecast Class I (ration) requirements for a 14-day operation. The most accurate statement about this capability is:**

A. MSS forecast tools generate binding resupply orders that the support battalion must execute
B. MSS analytics can model consumption trends against historical data to support planning estimates — the S4 must validate the model assumptions against current operational factors before using the output
C. Forecasting in MSS requires coding access and is not available to S4 staff
D. Supply forecast data in MSS is automatically submitted to theater as a logistics request

**5. The G4 directs you to build a logistics COP layer that shows distribution status — supplies currently in transit and expected delivery windows. The data staleness concern unique to distribution status (compared to supply on hand) is:**

A. Distribution data is more sensitive than supply data and requires a higher classification level
B. Distribution status changes rapidly — a convoy that departed four hours ago may have already arrived, been diverted, or been delayed; distribution data ages faster than static supply-on-hand data and requires more frequent validation
C. Distribution data can only be displayed as a table, not as a map layer
D. In-transit data is not available in MSS and must be tracked manually

**6. When configuring MSS to support a sustainment sync, which of the following best describes the correct sequence?**

A. Build the dashboard, configure CCIRs, then verify data currency
B. Verify data currency for all feeds first, configure CCIRs with correct thresholds and data sources, then build the dashboard — so that the sync products reflect the most current validated data
C. Build the dashboard and present to the G4 — CCIR configuration can wait until after the sync
D. Configure CCIRs only — dashboards are optional for sustainment syncs

**7. A supply chain manager identifies that the Class IX (repair parts) on-hand data in MSS has not updated in 36 hours. Parts requests are time-sensitive during sustained operations. The correct action is:**

A. Brief the 36-hour-old data as current until the feed is restored
B. Characterize the data gap, notify the G6/S6 to investigate the pipeline failure, contact supply units directly for current status, and caveat all Class IX displays with the data-as-of timestamp until the feed is restored
C. Remove the Class IX layer from the dashboard to avoid confusing the commander
D. Manually update the MSS display with data from phone calls and text messages

**8. Which of the following is the most operationally significant OPSEC risk associated with publishing an aggregated sustainment dashboard to a wide distribution list?**

A. Dashboard colors may not match the unit's standard briefing format
B. An aggregated view of supply on hand, consumption rates, and resupply timelines reveals the unit's operational endurance — an adversary with this data can infer planned operational tempo and duration
C. Distribution lists in MSS are public and cannot be restricted to authorized users
D. Sustainment data does not warrant OPSEC controls because it is administrative in nature

**9. ADP 4-0 establishes eight principles of sustainment. Table 1-1A in TM-40D maps each principle to a data platform application. Which principle's data platform analog is described as "consumption rate modeling, predictive demand analytics, and trend dashboards that project DOS forward based on operational tempo"?**

A. Integration — combining all elements of sustainment into unified operations
B. Anticipation — predicting future operational requirements based on current operations and historical data
C. Responsiveness — providing the right support at the right time and place
D. Simplicity — minimizing the complexity of sustainment operations

**10. Table 2-1A in TM-40D maps all ten classes of supply to their data sources, MSS feeds, and update frequencies. A logistics officer needs to track repair parts requisition status. Which class of supply covers repair parts, and what is its minimum update frequency?**

A. Class VII — major end items; update daily and immediately upon battle loss
B. Class V — ammunition; update daily and after every expenditure event
C. Class IX — repair parts (demand-supported and initial provisioning); update daily and immediately upon receipt of critical parts
D. Class II — clothing, individual equipment, and tools; update weekly

---

## SECTION 2 — SHORT ANSWER

*Answer in 3–5 sentences. (5 points each)*

**11. You are an FSB S4 preparing for a sustainment sync. Your MSS readiness dashboard shows 1st Bn FSC at 91% equipment readiness. The FSC commander calls you 20 minutes before the sync and reports they are at 58% following a vehicle accident this morning that deadlined four trucks. Walk through how you handle the next 20 minutes before the sync begins.**

*(Write your answer below)*

_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

**12. The BSB S3 asks you to explain the difference between the "supply on hand" data in MSS and actual physical inventory at the ASP. A new property book officer is listening. Explain the distinction and describe what a property book officer should do to reconcile the two.**

*(Write your answer below)*

_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

---

## SECTION 3 — SCENARIO (10 points)

**Read the following scenario and answer the question below.**

It is 0615. The sustainment sync begins at 0700. You open the MSS logistics dashboard and find the following:
- Class I (rations): data current as of 0530 — all units at 3-day supply on hand
- Class III (B) (fuel): data current for 1st and 3rd Bn FSC; 2nd Bn FSC feed has not updated since 1800 yesterday (13 hours stale)
- Class V (ammunition): current for all units; 1st Bn is below the commander's Class V CCIR threshold — CCIR has fired
- Equipment readiness: current for all units; 2nd Bn at 68% (below 70% threshold — CCIR has fired)

The G4 enters at 0655 and asks for a status update before the sync begins.

**13. Describe your complete course of action. Include: (a) what you brief to the G4 in the five minutes before the sync, (b) how you handle the 2nd Bn FSC fuel data gap, (c) how you present the two triggered CCIRs, and (d) what follow-on action you assign before the sync closes.**

*(Write your answer below)*

_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

---

## ANSWER KEY (Instructor Use Only — Do Not Distribute)

**Section 1:**
1. B — pipeline latency between LOGSTAT submission and dashboard update is the most common cause
2. B — property book reflects reported on-hand; maintenance status is a separate data source
3. B — verify data-as-of time; caveat the figure; brief actual status the commander provided
4. B — analytics support planning estimates; S4 must validate assumptions against operational factors
5. B — distribution data ages faster than supply-on-hand; frequent validation required
6. B — verify currency first, then configure CCIRs, then build dashboard
7. B — characterize gap, notify S6, get current status from source, caveat display
8. B — aggregated sustainment data reveals operational endurance — significant OPSEC risk
9. B — Table 1-1A (ADP 4-0) maps Anticipation to "consumption rate modeling, predictive demand analytics, and trend dashboards that project DOS forward based on operational tempo." Integration addresses cross-functional dashboards, Responsiveness addresses real-time threshold alerts, and Simplicity addresses standardized formats and pre-built views.
10. C — Table 2-1A (FM 4-0) identifies Class IX as repair parts (demand-supported and initial provisioning), with update frequency of daily and immediately upon receipt of critical parts. Class VII is major end items, Class V is ammunition, and Class II is clothing/equipment with weekly updates.

**Section 2 — Expected elements:**
11. Should include: immediately note the discrepancy between dashboard (91%) and reported current status (58%); verify the last LOGSTAT submission time in MSS; update the dashboard caveat with data-as-of timestamp; prepare to brief both the MSS figure and the commander-reported figure to the G4; notify the G4 before the sync begins so they are not surprised.
12. Should explain: MSS supply on hand reflects what was reported in the last property book submission — it is a point-in-time snapshot, not a real-time inventory; physical inventory at the ASP may differ due to issues receipted but not yet entered, losses not yet reported, or pipeline latency; to reconcile, the property book officer should compare the MSS figure against the ASP's most recent physical count and document discrepancies with the data-as-of date.

**Section 3 — Expected elements:**
(a) Brief the G4: Class I and Class V current and ready to brief; 2nd Bn FSC fuel data is 13 hours stale — flag as unconfirmed; two CCIRs triggered (Class V 1st Bn, readiness 2nd Bn); G4 should be aware of these before sync opens.
(b) Contact 2nd Bn FSC S4 directly for a spot report on current fuel status; display last known data with data-as-of caveat; do not brief the 1800 figure as current.
(c) Brief both CCIRs with their triggering data: Class V 1st Bn at [value] (below threshold); 2nd Bn readiness at 68% (below 70% threshold); recommend G4 decide whether to address resupply for 1st Bn and maintenance support for 2nd Bn during the sync.
(d) Assign: S6 to investigate 2nd Bn FSC fuel feed pipeline failure; 2nd Bn FSC S4 to submit updated LOGSTAT before sync closes; add CCIR resolution actions to the sync minutes.

---

*Total points: 40 (MC: 10 × 2 = 20, SA: 2 × 5 = 10, Scenario: 10). Passing score: 32 (80%).*

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*EX_TM40D-POST | Version 1.0 | March 2026*
