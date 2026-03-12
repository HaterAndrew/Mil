# POST-TEST — TM-40C: MOVEMENT & MANEUVER
## Maven Smart System (MSS) — USAREUR-AF

| Field | Detail |
|---|---|
| **Course** | TM-40C: Movement & Maneuver WFF Track |
| **Form** | Post-Test |
| **Level** | TM-40C (WFF Track) |
| **Audience** | G3/S3 maneuver staff, operations officers, S3 NCOs, maneuver planners; prerequisite: completion of TM-40C training |
| **Time Allowed** | 30 minutes |
| **Passing Score** | 80% (24/30 points) |

---

## INSTRUCTIONS

This assessment confirms proficiency upon completion of TM-40C training. A score of 80% (24/30) is required for course completion certification. Results are recorded on the student training record.

---

## SECTION 1 — MULTIPLE CHOICE

*Circle the letter of the best answer. (2 points each)*

**1. You configure a CCIR in MSS to alert when any maneuver battalion crosses Phase Line AMBER. After configuring the alert, it does not fire during a test run even though test data shows 2nd Battalion at the correct grid reference. The most likely cause is:**

A. Geographic CCIR alerts require 30-minute activation lead time after configuration
B. The CCIR is configured against the wrong data source — it may be pointed at a static position layer rather than the live unit position feed
C. Phase line-based CCIRs are not supported in the current MSS version
D. The test data must be submitted through an official movement report to trigger the alert

**2. A maneuver planner builds a COA sketch overlay in MSS showing axis of advance, phase lines, and unit boundaries. Before distributing this product for the COA brief, the most important check is:**

A. Verify the overlay colors match the brigade's standard slide template
B. Confirm data-as-of timestamps are displayed, OPSEC markings are applied, and distribution is limited to personnel with operational need to know
C. Export the overlay to PowerPoint before the brief to prevent MSS connectivity issues
D. Route the product through the S6 for network classification review

**3. During a movement-to-contact, the COP shows that 3rd Battalion's last reported position is six hours old. The battalion is currently in a communications-restricted area. The operations officer should:**

A. Remove 3rd Battalion from the COP to prevent the commander from seeing stale data
B. Continue briefing 3rd Battalion's last reported position as current — six hours is acceptable
C. Display the last reported position with a data-as-of caveat and brief the commander on the communications gap; do not present last reported as current
D. File a data quality report with the MSS administrator before the next brief

**4. Which of the following most accurately describes MSS's role during the COA Analysis (war gaming) step of MDMP?**

A. MSS generates probability scores for each COA based on terrain and unit data
B. MSS provides a shared visualization environment where staff can display COA overlays, terrain data, and unit positions to support the war game discussion — judgment and analysis remain with the staff
C. War gaming requires printed maps only — MSS products are not suitable for MDMP
D. MSS replaces the red cell function by automating enemy COA generation

**5. An obstacle overlay in MSS has been loaded from an engineer report submitted three days ago. The maneuver planner should:**

A. Use the overlay without verification — three days is within normal obstacle data standards
B. Display the overlay with a data-as-of timestamp, note to the staff that obstacle conditions may have changed, and coordinate with the engineer section for current status
C. Delete the overlay and wait for a new engineer report before displaying any obstacles
D. Convert the overlay to a static image so the data-as-of problem is no longer displayed

**6. Task organization data in MSS shows that Alpha Company is OPCON to 2nd Battalion. The S3 learns through a verbal order that Alpha Company has been returned to 1st Battalion, but the MSS display has not been updated. The correct action is:**

A. Brief the old task organization — verbal orders are not authoritative until MSS is updated
B. Immediately update the MSS task org display to reflect the verbal order and note that the FRAGO has not yet been published
C. Brief the current situation accurately to the commander, note the discrepancy between what MSS shows and current status, and update MSS when the written FRAGO is received
D. Contact the task org data administrator and wait for an automated update

**7. A route corridor displayed on the MSS COP shows green status (passable) based on a report submitted 18 hours ago. A staff officer wants to brief the route as passable for tonight's movement. The operations officer should:**

A. Brief the route as passable — green status in MSS is authoritative
B. Validate the 18-hour-old data against current route reconnaissance or TCP reports before briefing passability; 18 hours is significant for route status
C. Display the route with yellow status to be conservative
D. Remove the route from the COP and conduct the brief without route status

**8. When applying OPSEC procedures to a maneuver visualization product in MSS, which combination of elements requires the most careful handling?**

A. Phase lines and objective names only — unit positions are not sensitive
B. Unit positions, axis of advance, phase line sequence, and timing data together — this combination reveals current locations, intended direction, and timeline of friendly action
C. Equipment readiness data only — maneuver graphics are unclassified
D. Traffic control point locations only — all other maneuver data is publicly releasable

---

## SECTION 2 — SHORT ANSWER

*Answer in 3–5 sentences. (5 points each)*

**9. During a rehearsal of concept (ROC) drill, the S3 asks you to display four units simultaneously on the maneuver COP: three maneuver battalions and an attached cavalry squadron. The cavalry squadron feed is showing data that is 90 minutes old — all other feeds are current. Walk through how you would handle this discrepancy in the COP display and what you would say to the S3 before the ROC begins.**

*(Write your answer below)*

_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

**10. An operations officer briefs the commander that 1st Battalion has crossed Phase Line AMBER based on MSS COP data. The battalion S3 immediately calls and says they are still short of Phase Line AMBER — the COP is wrong. Explain what likely caused this discrepancy and what the operations officer should have done differently before briefing.**

*(Write your answer below)*

_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

---

## SECTION 3 — SCENARIO (10 points)

**Read the following scenario and answer the question below.**

It is H-3 hours before an attack order brief. You are the S3 NCO responsible for the maneuver COP. The current state:
- 1st Battalion position feed: current (updated 15 minutes ago)
- 2nd Battalion position feed: stale — last updated 2 hours 45 minutes ago
- 3rd Battalion position feed: current (updated 20 minutes ago)
- Phase line overlay: loaded and current
- Axis of advance overlay: not yet loaded
- Task org display: showing the previous operation's task organization — needs to be updated for this attack

The attack order brief is in three hours. The commander expects a fully configured maneuver COP.

**11. Describe your complete course of action for the next three hours. Include: (a) how you prioritize and sequence the tasks, (b) how you handle the 2nd Battalion data gap before the brief, (c) what you brief to the S3 about COP status before the commander enters, and (d) one OPSEC action you take before the brief begins.**

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
1. B — wrong data source is the most common geographic CCIR failure; the alert must point to the live feed
2. B — OPSEC marking and distribution control are the critical checks before distribution of any maneuver product
3. C — last reported position displayed with caveat is correct; never brief stale data as current
4. B — MSS supports visualization and data access; analysis and judgment remain with the staff
5. B — display with timestamp and coordinate with engineers; obstacle data currency is operationally significant
6. C — brief current status accurately; note the MSS discrepancy; do not brief incorrect MSS data as current
7. B — 18 hours is significant for route status; validate before briefing passability
8. B — the combination of positions, direction, phase line sequence, and timing is the most sensitive aggregate

**Section 2 — Expected elements:**
9. Should include: display the cavalry feed with a visible data-as-of timestamp; tell the S3 the cavalry position is 90 minutes old and may not reflect current location; recommend the S3 contact the cav squadron's TOC for a spot report before the ROC; note the discrepancy on the COP so the commander is not surprised.
10. Should explain: the COP shows last reported position, not confirmed current position; the operations officer should have stated data-as-of time when briefing the phase line crossing; should have confirmed through primary reporting channel (radio check with 1st Bn S3) before briefing the commander a maneuver milestone.

**Section 3 — Expected elements:**
(a) Prioritize: load the axis of advance overlay and update task org first (missing graphics, not just stale); then address the 2nd Battalion feed — contact 2nd Bn TOC for current position; COP completeness matters more than order.
(b) Attempt to reach 2nd Bn for a spot report; if unavailable, display last known position with data-as-of timestamp and prepare a caveat for the S3 brief.
(c) Before commander arrives, brief the S3 on: which elements are current, the 2nd Bn data gap and what steps were taken, COP is complete for all other elements — S3 decides whether to proceed.
(d) Apply correct classification marking to the COP view and verify distribution controls before the brief — confirm no unauthorized users have access to the maneuver product.

---

*Total points: 30. Passing score: 24 (80%).*

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*EX-TM40C-POST | Version 1.0 | March 2026*
