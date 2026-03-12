# POST-TEST — TM-40A: INTELLIGENCE
## Maven Smart System (MSS) — USAREUR-AF

| Field | Detail |
|---|---|
| **Course** | TM-40A: Intelligence WFF Track |
| **Form** | Post-Test |
| **Level** | TM-40A (WFF Track) |
| **Audience** | G2/S2 staff, targeting officers, all-source analysts; prerequisite: completion of TM-40A training |
| **Time Allowed** | 30 minutes |
| **Passing Score** | 80% (24/30 points) |

---

## INSTRUCTIONS

This assessment confirms proficiency upon completion of TM-40A training. A score of 80% (24/30) is required for course completion certification. Results are recorded on the student training record.

---

## SECTION 1 — MULTIPLE CHOICE

*Circle the letter of the best answer. (2 points each)*

**1. You have configured a PIR alert in MSS tied to the threat activity layer for NAI TIGER. The alert does not fire when a test event is placed inside NAI TIGER's boundaries. The most likely cause is:**

A. PIR alerts are not supported in the current MSS version
B. The geographic boundary for NAI TIGER is incorrectly defined in the alert configuration, or the alert is drawing from a different data feed than the one containing the test event
C. Alerts require 24 hours to activate after initial configuration
D. The test event must be submitted through the official intelligence reporting channel to register in MSS

**2. When building a targeting product in MSS Workshop, which of the following is mandatory for every target displayed?**

A. A photograph of the target attached to the data record
B. A data-as-of timestamp and a clear distinction between confirmed and unconfirmed target status
C. Automated BDA score calculated by the MSS targeting module before the product can be shared
D. Approval from the targeting officer at the next higher echelon before display on the COP

**3. Your collection manager has configured MSS to display coverage status for six NAIs. At the morning targeting sync, you notice NAI FALCON shows 0% collection coverage and no data-as-of timestamp. You should:**

A. Brief the targeting board that NAI FALCON is clear — the absence of reporting indicates no activity
B. Report the display as a system error and proceed without NAI FALCON data
C. Identify NAI FALCON as a collection gap, brief it explicitly to the targeting board as unknown (not clear), and recommend a re-tasking action to address the gap
D. Remove NAI FALCON from the COP display until coverage is restored to avoid confusion

**4. During IPB support in MSS, a threat activity layer shows the most probable enemy course of action (MCOA) based on a 48-hour-old dataset. The commander asks for the current MCOA assessment. You should:**

A. Brief the displayed MCOA as current since it represents the last confirmed assessment
B. Caveat the briefed MCOA explicitly with the data age; assess whether conditions could have changed in 48 hours; recommend updated collection before the commander relies on the assessment for a decision
C. Delete the stale MCOA layer and re-build it with current data before the brief
D. Defer the MCOA brief entirely until new collection is complete

**5. A correctly structured PIR configured as an MSS alert includes:**

A. "Watch for enemy activity" — flagged as a standing PIR
B. "Report any change in threat force disposition anywhere in the AOR to the S2"
C. "Trigger: Threat activity event in NAI TIGER or NAI WOLF; data source: Threat Activity feed; notify: S2, targeting officer via MSS alert"
D. "All NAIs should be checked daily and briefed at the morning sync"

**6. Intelligence products built in MSS Workshop must be shared with targeting officers from a supported but non-organic unit. The correct sharing approach is:**

A. Export the product as a PDF and email it to the targeting officers' personal email accounts for speed
B. Post the raw data layers to an open project folder accessible by all users in the tenant
C. Grant the targeting officers read-only access to the specific Workshop product; ensure correct classification marking is applied; confirm they can view but not modify the product
D. Share via screenshot in the unit's messaging platform — this avoids MSS account management overhead

**7. All-source fusion using MSS is best described as:**

A. An automated process where MSS correlates HUMINT, SIGINT, and IMINT feeds and produces a fused intelligence estimate without analyst involvement
B. The analyst's use of MSS to display and compare multiple intelligence data layers simultaneously — identifying corroboration, contradiction, and gaps across sources to support a human-produced assessment
C. A feature available only to G2 staff at division level — BCT-level analysts do not have access to multi-source layers
D. Replacing all-source analysis with AI-generated threat assessments that are displayed directly on the COP

**8. Your S2 has been directed to build a daily intelligence summary (INTSUM) product in MSS Workshop. The product must be ready at 0600 each day. The data pipeline feeding the threat activity layer consistently lags by 45 minutes after each reporting cycle close. The correct course of action is:**

A. Launch the pipeline manually each morning at 0500 and wait for it to complete before building the INTSUM
B. Build the INTSUM at 0600 using whatever data is available; caveat any element sourced from the delayed pipeline with the actual data-as-of time; notify the S2 of the recurring lag so it can be addressed at the pipeline level
C. Delay the INTSUM to 0700 each day to allow the pipeline to complete — the 45-minute lag is acceptable
D. Build the INTSUM with static data from the previous cycle until the pipeline lag is resolved

---

## SECTION 2 — SHORT ANSWER

*Answer in 3–5 sentences. (5 points each)*

**9. Your commander's intelligence requirements include three PIRs. You have configured PIR alerts for all three in MSS. During a test run, PIR 2 (enemy force presence in Engagement Area BRONZE) fires when no threat data is present in that area. Walk through the troubleshooting steps you would take to identify and resolve the false-positive trigger before the next targeting working group.**

*(Write your answer below)*

_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

**10. The targeting officer asks why the targeting product displayed in MSS still shows Target AC-04 as unconfirmed when the S2 section submitted a confirmation report two hours ago. Explain the difference between intelligence reporting submission and MSS data display, and describe how you would resolve the discrepancy before the targeting board convenes.**

*(Write your answer below)*

_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

---

## SECTION 3 — SCENARIO (10 points)

**Read the following scenario and answer the question below.**

It is 0545. The targeting working group (TWG) convenes at 0630. You open MSS to finalize the intelligence products and discover:

- Threat activity data in NAI TIGER is 16 hours old (last updated 1330 yesterday)
- Threat activity data in NAIs WOLF, EAGLE, and HAWK is current (updated 0500)
- PIR 1 (enemy vehicle movement in EA BRONZE) has not fired based on current data
- A SIGINT-analog report submitted at 0430 shows vehicle activity at a grid inside EA BRONZE — PIR 1 has not fired despite this report

You have 45 minutes before the TWG.

**11. Describe your complete course of action for the next 45 minutes. Include: (a) what you investigate first and why, (b) what you will brief as confirmed vs. what you will caveat, (c) how you characterize the NAI TIGER data gap to the targeting board, and (d) what follow-on action you assign to resolve the PIR 1 failure.**

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
1. B — geographic boundary misconfiguration or wrong data feed is the most common PIR alert failure
2. B — data-as-of timestamp and confirmed/unconfirmed distinction are mandatory for all targeting products
3. C — absence of reporting means unknown, not clear; brief as collection gap and recommend re-tasking
4. B — caveat with data age, assess whether conditions could have changed, recommend updated collection
5. C — complete PIR alert: trigger condition + data source + notification path
6. C — read-only access to specific product; correct classification marking applied
7. B — all-source fusion in MSS is analyst-driven, not automated; MSS displays layers for human correlation
8. B — brief with caveat at scheduled time; notify S2 of recurring lag for pipeline-level resolution

**Section 2 — Expected elements:**
9. Should include: verify the geographic boundary definition for EA BRONZE (check polygon coordinates), confirm the data source selected for PIR 2 is the correct threat activity feed, test with a known-negative event location to isolate whether the boundary or the feed is at fault, check whether multiple overlapping data sources are both feeding the trigger.
10. Should explain: pipeline latency between report submission and dataset update in MSS; need to trace where the confirmation report is in the data pipeline (submitted to system → processed → dataset updated → COP refreshes); caveat the targeting product with "as of [last pipeline update]" until resolved; escalate to S6 if the pipeline is stalled.

**Section 3 — Expected elements:**
(a) Investigate PIR 1 failure first — an actual intelligence event in EA BRONZE that did not trigger PIR 1 is a higher-priority problem than stale NAI TIGER data because it affects immediate targeting decisions.
(b) Brief NAIs WOLF, EAGLE, and HAWK threat data as current; caveat all NAI TIGER assessments with the 16-hour data age; for the 0430 SIGINT report, brief it as received intelligence pending MSS correlation — do not treat absence of PIR 1 trigger as confirmation the event did not occur.
(c) Tell the targeting board: NAI TIGER data is 16 hours old; threat status in that NAI is unknown, not clear; recommend the board not develop targeting solutions dependent on NAI TIGER disposition until data is refreshed; note the collection gap and flag it for immediate re-tasking.
(d) Assign the S2 NCO to contact the S6 to investigate why the 0430 SIGINT report did not update the EA BRONZE threat layer and trigger PIR 1; require a status report before the end of the TWG.

---

*Total points: 30. Passing score: 24 (80%).*

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*EX-TM40A-POST | Version 1.0 | March 2026*
