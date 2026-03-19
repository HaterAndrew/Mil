# PRE-TEST — TM-40D: SUSTAINMENT
## Maven Smart System (MSS) — USAREUR-AF

| Field | Detail |
|---|---|
| **Course** | TM-40D: Sustainment WFF Track |
| **Form** | Pre-Test |
| **Level** | TM-40D (WFF Track) |
| **Audience** | G4/S4 staff, FSB/BSB logistics officers, supply chain managers, property book officers; prerequisite: TM-10 + TM-20 + TM-30 complete |
| **Time Allowed** | 20 minutes |
| **Passing Score** | N/A — diagnostic only |

---

## INSTRUCTIONS

This diagnostic assessment establishes your baseline knowledge before training. Your score does not affect course eligibility. Answer honestly — results help the instructor tailor instruction to identified gaps.

---

## SECTION 1 — MULTIPLE CHOICE

*Circle the letter of the best answer. (2 points each)*

**1. When displaying Class III (B) (bulk fuel) supply on hand in MSS, the most important data quality check the S4 should perform before a sustainment sync is:**

A. Confirm that the symbology matches the Army logistics color standards
B. Verify the data-as-of timestamp — logistics data can change significantly between reporting cycles and stale data may reflect a critical shortfall or false surplus
C. Ensure the data is formatted as a bar chart rather than a table
D. Confirm that all Class IX (repair parts) data is displayed on the same layer

**2. A LOGSTAT is the primary sustainment reporting mechanism at echelon. In MSS, LOGSTAT data pipelines are most accurately described as:**

A. Real-time feeds that update the moment a unit submits a report
B. Data that reflects what was reported at the last LOGSTAT submission cycle — latency between unit submission and MSS display must be understood and communicated
C. Automated systems that replace the need for units to submit manual LOGSTATs
D. Classified pipelines that cannot be viewed by below-brigade echelon staff

**3. An S4 builds a readiness dashboard in MSS showing equipment readiness by battalion. The commander asks why one battalion shows 94% readiness when the battalion S4 reported 71% this morning. The most likely explanation is:**

A. MSS automatically adjusts readiness data to account for pending maintenance actions
B. The dashboard is pulling from a dataset that has not yet been updated with the morning LOGSTAT submission — there is pipeline latency between unit reporting and MSS display
C. The battalion S4 entered incorrect data into the reporting system
D. 94% is the correct figure — battalion-level reporting is unreliable

**4. Supply chain analytics in MSS are best used to:**

A. Automatically reorder supplies when on-hand quantities fall below threshold
B. Support G4 analysis of consumption trends, forecast sustainment requirements, and identify developing shortfalls — decision authority remains with the S4/G4
C. Replace the Property Book Unit Supply Enhanced (PBUSE) system for property accountability
D. Generate automated supply requests to the corps support command

**5. Which of the following MSS CCIR configurations would best support a BSB S4 monitoring Class V (ammunition) consumption during a sustained operation?**

A. An alert that fires when any subordinate unit submits a LOGSTAT
B. An alert that fires when Class V on-hand falls below the commander's specified consumption threshold, sourced from the Class V supply reporting feed
C. A daily dashboard refresh that shows ammunition status without a configured alert
D. A manual threshold check performed by the S4 each morning

**6. Property accountability data in MSS provides visibility of:**

A. Real-time physical location of all equipment items tracked by serial number
B. Reported on-hand quantities and status from property book submissions — not real-time GPS tracking of individual items
C. Automated reconciliation between hand receipt holders and the property book officer
D. Classified equipment disposition that is not accessible below brigade level

**7. Transportation and distribution data in MSS is most valuable for which sustainment task?**

A. Generating automated convoy manifests and movement orders
B. Providing visibility of distribution pipeline status — what is in transit, expected delivery windows, and routing chokepoints — to support sustainment synchronization
C. Replacing the movement control officer's tracking responsibilities
D. Calculating fuel consumption rates for wheeled vehicles

**8. Which of the following represents a correct OPSEC consideration for sustainment data products in MSS?**

A. Logistics data is unclassified and can be shared outside the unit without restriction
B. Supply on-hand quantities, consumption rates, and resupply timelines — when aggregated — can reveal unit readiness posture and operational timelines; distribution must be controlled accordingly
C. OPSEC applies only to personnel data, not logistics data
D. Transportation route data is exempt from distribution controls because it is based on open-source road networks

---

## SECTION 2 — SHORT ANSWER

*Answer in 2–4 sentences. (5 points each)*

**9. You are an FSB S4 preparing for a sustainment sync. The MSS readiness dashboard shows all subordinate units above 85% equipment readiness, but two unit S4s have told you verbally that their readiness has dropped below 70% this week. What do you do before the sync, and what do you brief?**

*(Write your answer below)*

_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

**10. Describe the difference between a supply on-hand report in MSS and a real-time inventory count. Why does this distinction matter for the S4 when making resupply decisions?**

*(Write your answer below)*

_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

---

## SECTION 3 — SCENARIO (10 points)

**Read the following scenario and answer the question.**

Your BCT is 72 hours into a sustained exercise. The G4 has directed you to build a logistics visibility dashboard in MSS showing Class I (rations), Class III (B) (fuel), Class V (ammunition), and equipment readiness for three organic battalions. The G4 also wants a CCIR configured to alert when any Class III (B) supply falls below a 2-day consumption rate threshold.

**11. Describe how you would approach building this dashboard and configuring the CCIR. For each Class of Supply display and the readiness panel, identify what data source you would use and what you would verify before presenting the dashboard to the G4. Then describe the CCIR configuration.**

*(Write your answer below)*

_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

---

*Total points: 30. Diagnostic only — score does not affect course admission.*

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*EX_TM40D-PRE | Version 1.0 | March 2026*

---

## ANSWER KEY — INSTRUCTOR USE ONLY

*Do not distribute to students. Use to identify baseline gaps and tailor Day 1 instruction accordingly.*

**Multiple Choice:**

1. B — Verify the data-as-of timestamp; logistics data changes significantly between reporting cycles and stale data may reflect a critical shortfall or false surplus. Symbology and chart format are secondary.
2. B — LOGSTAT pipeline data reflects what was reported at the last submission cycle; latency between unit submission and MSS display must be understood and communicated to commanders and the G4.
3. B — The dashboard is pulling from a dataset not yet updated with the morning LOGSTAT submission; pipeline latency between unit reporting and MSS display is the most likely explanation.
4. B — Supply chain analytics support G4 analysis of consumption trends, forecast requirements, and shortfall identification; decision authority remains with the S4/G4 — MSS does not auto-reorder.
5. B — An alert that fires when Class V on-hand falls below the commander's threshold sourced from the Class V supply reporting feed is the correct CCIR configuration; other options are manual or unfocused.
6. B — Property accountability data reflects reported on-hand quantities from property book submissions — not real-time GPS tracking of individual items.
7. B — Transportation and distribution data provides visibility of pipeline status, in-transit items, delivery windows, and routing chokepoints to support sustainment synchronization.
8. B — Aggregated supply quantities, consumption rates, and resupply timelines reveal unit readiness posture and operational timelines; distribution must be controlled accordingly.

**Short Answer Guidance:**

SA-9. Full credit (5 pts): The MSS dashboard reflects LOGSTAT submissions from a previous cycle and does not capture the verbal updates from this week; before the sync, contact both units to obtain current LOGSTAT submissions or verbal updates with a DTG; brief the dashboard as showing status as of [last submission DTG] and note explicitly that two units have verbally reported drops below 70% — do not present the dashboard figure as current readiness. Partial credit (3 pts): identifies the data currency mismatch but does not describe the steps to obtain updated data or the correct brief characterization.

SA-10. Full credit (5 pts): MSS supply on-hand reflects what was reported in the last LOGSTAT submission; a real-time inventory count requires a physical count of on-hand assets; the gap matters because LOGSTAT submissions may be hours or days old, consumption may have occurred since submission, and in-transit items are not counted in on-hand; an S4 making a resupply decision solely from MSS data without accounting for consumption since last submission or items in transit may under- or over-order. Partial credit (3 pts): identifies the distinction without explaining the decision risk.

**Scenario Guidance:**

Q-11. Full credit (10 pts): Must address all four supply class displays and the CCIR.

*Class I:* link to ration supply dataset; verify submission timestamps per battalion; confirm figures reflect the current reporting cycle.

*Class III(B):* link to fuel supply reporting dataset; same timestamp verification per battalion; identify any unit with no current submission.

*Class V:* link to ammunition supply dataset; verify submission timestamps; flag any unit with Class V at or below 1 day of supply for immediate attention.

*Readiness panel:* link to LOGSTAT equipment status dataset; verify all three battalions have submitted within the current cycle; note any unit with a gap.

*CCIR:* configure alert on Class III(B) dataset; threshold = on-hand quantity / daily consumption rate < 2 days; route to G4 (supply decision authority) and S4/XO (command awareness); verify the daily consumption rate figure is current before setting the threshold.

Partial credit (6 pts): three of five elements (four supply panels + CCIR) addressed correctly with data source and verification step. Minimum acceptable: two supply panels with CCIR correctly configured.

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*EX_TM40D-PRE | Answer Key | Version 1.0 | March 2026*
