# POST-TEST — TM-40F: MISSION COMMAND
## Maven Smart System (MSS) — USAREUR-AF

| Field | Detail |
|---|---|
| **Course** | TM-40F: Mission Command WFF Track |
| **Form** | Post-Test |
| **Level** | TM-40F (WFF Track) |
| **Audience** | G3/S3 staff, battle captains, XOs, CDRs; prerequisite: completion of TM-40F training |
| **Time Allowed** | 30 minutes |
| **Passing Score** | 80% (32/40 points) |

---

## INSTRUCTIONS

This assessment confirms proficiency upon completion of TM-40F training. A score of 80% (32/40) is required for course completion certification. Results are recorded on the student training record.

---

## SECTION 1 — MULTIPLE CHOICE

*Circle the letter of the best answer. (2 points each)*

**1. You are configuring a CCIR in MSS for a battalion readiness threshold. After configuring the alert, it does not fire when you input a test value that should exceed the threshold. The most likely cause is:**

A. The CCIR feature is not supported in the current MSS version
B. The test value must be submitted through the official LOGSTAT process to trigger the alert
C. The CCIR needs 24 hours to activate after configuration
D. The threshold was entered correctly but the data source feed selected for the CCIR is the wrong dataset

**2. When building a Battle Update Assessment (BUA) product in MSS Workshop, which of the following formatting requirements is mandatory?**

A. Include a data-as-of timestamp on every data element displayed
B. Use only charts — no text or tables
C. Route the product through the S6 for classification review before displaying to the commander
D. Limit the product to a single page regardless of content

**3. A CCIR alert fires indicating 1st Battalion personnel strength is below the configured threshold. Before briefing the commander, you should:**

A. Immediately halt all current operations and alert the theater headquarters
B. Dismiss the alert as likely a data entry error and note it in the daily log
C. Validate the reported status against primary reporting channels (1st Battalion S1) before briefing
D. Reconfigure the CCIR threshold to a lower value to reduce false positives

**4. During a battle rhythm dashboard review, you find that the readiness widget is showing data from 3 days ago. The correct course of action is:**

A. Manually type the current readiness values into the widget text field
B. Identify the data pipeline feeding the widget, escalate to the S6 if the pipeline has failed, and caveat the displayed value until the feed is restored
C. Delete the widget and replace it with a static text field showing the last known values
D. Brief the commander that readiness is unknown until the next LOGSTAT cycle

**5. Which of the following describes a correctly structured CCIR for MSS configuration?**

A. "Equipment readiness for 2nd Battalion below 65%, data source: BCT Readiness feed, notify: Battle Captain, S3 via MSS alert"
B. "Monitor readiness" — flagged as a standing requirement
C. "Review all battalion reports daily at 0700 and compare to last week"
D. "Alert S2 if any intelligence event occurs anywhere in the AOR"

**6. You need to share the BUA Workshop product with the commander's aide for pre-brief distribution. The correct permission setting is:**

A. Editor — so the aide can make updates as needed
B. Commenter — so the aide can annotate the product
C. Viewer — read-only access prevents unintended modification of a commander product
D. No sharing is needed — the commander should access MSS directly

**7. The MSS COP shows 3rd Battalion positions have not updated in 8 hours. This is most accurately characterized as:**

A. 3rd Battalion has moved outside MSS coverage and is now off the grid
B. Normal behavior — COP updates are expected once every 8–12 hours
C. A network failure requiring immediate theater notification
D. A data reporting gap — MSS is showing the last reported position, which may no longer reflect actual location

**8. In degraded operations when MSS connectivity is unavailable, Mission Command staff should:**

A. Suspend all decision-making until connectivity is restored
B. Execute manual information management procedures, maintain awareness of what MSS data is now stale, and restore connectivity per the S6 continuity plan
C. Continue to use MSS with reduced functionality by accessing it through personal devices on civilian networks
D. Transfer all CCIR monitoring responsibilities to higher echelon until connectivity is restored

**9. FM 6-0 defines information management (IM) as comprising six tasks. Table 1-3 in TM-40F maps each IM task to its MSS data platform implementation. Which of the following correctly lists all six FM 6-0 IM tasks?**

A. Plan, Collect, Analyze, Brief, Archive, Secure
B. Collect, Process, Store, Display, Disseminate, Protect
C. Ingest, Transform, Model, Visualize, Share, Encrypt
D. Receive, Validate, Catalog, Present, Distribute, Classify

**10. Table 1-4 in TM-40F crosswalks FM 6-0 information relevance criteria to VAULTIS-A data quality dimensions. Which FM 6-0 criterion maps to the VAULTIS-A "Timeliness" dimension?**

A. Accurate — free from error; faithful to the source
B. Useable — in a format appropriate to the consumer
C. Timely — available in time to support the decision
D. Complete — contains all elements necessary for the decision

---

## SECTION 2 — SHORT ANSWER

*Answer in 3–5 sentences. (5 points each)*

**11. Your commander's guidance card specifies three CCIRs. You have configured all three in MSS. During a test run, CCIR 2 (geographic event trigger) fires when no events are present in the sensitivity area. Walk through the troubleshooting steps you would take to identify and resolve the false-positive trigger before the next BUA.**

*(Write your answer below)*

_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

**12. A subordinate unit S3 asks you why the BUA read-ahead still shows 2nd Battalion at 72% readiness when they just submitted an updated LOGSTAT showing 81%. Explain the difference between reported status and displayed status in MSS, and describe how you would resolve the discrepancy.**

*(Write your answer below)*

_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

---

## SECTION 3 — SCENARIO (10 points)

**Read the following scenario and answer the question below.**

It is 0630. The morning BUA begins at 0700. You open MSS to build the final read-ahead and discover:
- 1st Battalion readiness data is 14 hours old (last updated 1600 yesterday)
- 2nd and 3rd Battalion readiness data is current (updated at 0600)
- CCIR 1 (readiness threshold) has not fired for any battalion based on the current data
- A new operational event at grid 488792 was submitted at 0530 — within the CCIR 2 sensitivity area — but CCIR 2 has not fired

You have 30 minutes before the BUA.

**13. Describe your complete course of action for the next 30 minutes. Include: (a) what you will investigate first and why, (b) what you will brief vs. what you will caveat, (c) how you will characterize the 1st Battalion data gap to the commander, and (d) what follow-on action you will assign to resolve the CCIR 2 failure.**

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
1. D — wrong data source is the most common CCIR configuration failure
2. A — data-as-of timestamps on every element are mandatory
3. C — validate before briefing; never brief an unvalidated CCIR trigger
4. B — identify pipeline issue, escalate to S6, caveat displayed value
5. A — complete CCIR: threshold + data source + notification path
6. C — Viewer only for commander products
7. D — data reporting gap, not a network failure
8. B — manual procedures + awareness of stale data + restore per S6 plan

**Section 2 — Expected elements:**
11. Should include: verify the geographic boundary configuration, check whether the event filter is using correct coordinate fields, check whether the sensitivity area polygon was entered correctly, test with a known-negative event location.
12. Should explain: pipeline latency between LOGSTAT submission and dataset update; need to trace the data pipeline to find where the 81% update is held up; caveat the BUA with "as of [last update time]" until resolved.

**Section 3 — Expected elements:**
(a) Investigate CCIR 2 failure first — an actual event in the sensitivity area that did not trigger is more operationally significant than stale readiness data.
(b) Brief 2nd and 3rd Bn readiness as current; caveat 1st Bn readiness with data-as-of timestamp and note it may not reflect current status.
(c) Tell the commander: 1st Bn data is 14 hours old; current status is unconfirmed; you have contacted 1st Bn S4 for a spot report; you recommend the commander note the uncertainty for 1st Bn-dependent decisions.
(d) Assign S6 to investigate CCIR 2 geographic trigger failure; have them report status before the next BUA.

---

*Total points: 40 (MC: 10 × 2 = 20, SA: 2 × 5 = 10, Scenario: 10). Passing score: 32 (80%).*

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*EX_TM40F-POST | Version 1.0 | March 2026*
