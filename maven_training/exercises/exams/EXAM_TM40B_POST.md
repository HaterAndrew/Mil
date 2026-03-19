# POST-TEST — TM-40B: FIRES
## Maven Smart System (MSS) — USAREUR-AF

| Field | Detail |
|---|---|
| **Course** | TM-40B: Fires WFF Track |
| **Form** | Post-Test |
| **Level** | TM-40B (WFF Track) |
| **Audience** | FSE staff, fire support officers, targeting teams, artillery/mortar officers; prerequisite: completion of TM-40B training |
| **Time Allowed** | 30 minutes |
| **Passing Score** | 80% (32/40 points) |

---

## INSTRUCTIONS

This assessment confirms proficiency upon completion of TM-40B training. A score of 80% (32/40) is required for course completion certification. Results are recorded on the student training record.

---

## SECTION 1 — MULTIPLE CHOICE

*Circle the letter of the best answer. (2 points each)*

**1. You configured an MSS alert to notify the FSO when an HVT enters TAI ANVIL. The alert does not fire when you input a test event placing an HVT inside TAI ANVIL's coordinates. The most likely cause is:**

A. MSS does not support geographic-based alerts for fires data
B. The test event must be submitted through the official fires reporting channel before MSS can register it
C. Fires alerts require 48 hours to activate after initial configuration
D. The TAI ANVIL geographic boundary is incorrectly defined in the alert configuration, or the alert is pulling from a different target data feed than the one containing the test event

**2. During a targeting working group, you display a fires product in MSS Workshop. The targeting officer asks how old the target data is. The product has no data-as-of timestamps on any element. You should:**

A. Halt the brief, add explicit data-as-of timestamps to all data elements before continuing, and note the omission for after-action review
B. Estimate the data age based on the last time you updated the product manually and brief that estimate
C. Proceed with the brief since the targeting officer can check the source datasets independently
D. Note the omission verbally and continue — adding timestamps is only required for products distributed outside the unit

**3. Your BDA layer in MSS shows an initial damage assessment (IDA) for Target AC-07 — but no follow-on BDA (FUBA) or confirmed BDA (CUBA). The targeting board asks for target status. You should:**

A. Brief Target AC-07 as destroyed since the IDA confirms the strike occurred
B. Brief the IDA as reported; state that FUBA and CUBA are pending; characterize the current target status as initial assessment only — do not characterize the target as destroyed or neutralized without confirmed BDA
C. Remove Target AC-07 from the fires product until CUBA is received to avoid confusion
D. Request that the targeting board defer any decisions on Target AC-07 until MSS automatically upgrades the assessment to confirmed

**4. FSCMs on the MSS COP are 24 hours old and have not been updated since the last planning cycle. The targeting board is about to approve a fire mission. You should:**

A. Proceed with the targeting board — FSCMs are stable unless changed by written order, and 24 hours is within normal refresh tolerance
B. Delete the stale FSCMs from the COP and proceed without them until updated versions are received
C. Pause the targeting board; verify FSCM status with the S3 and higher fires cell before approving any fires; brief the board that displayed FSCMs may not reflect the current coordination picture
D. Route the fire mission to higher headquarters for approval since your FSCMs are outdated

**5. A correctly structured fires alert in MSS for ammunition readiness includes:**

A. "Monitor ammunition status" — flagged as a standing fires requirement
B. "Alert if any ammunition status changes" — configured for all firing units in the AOR
C. "Trigger: Brigade fires ammunition readiness below 70% for any firing unit; data source: Fires Readiness feed; notify: FSO, S4 via MSS alert"
D. "Daily ammunition check to be briefed at morning fires update — no MSS alert required"

**6. You need to share the targeting product from MSS Workshop with the aviation liaison officer (AVLO) for deconfliction review before the targeting board. The correct approach is:**

A. Export the targeting product to a PDF and post it to the unit's shared drive for the AVLO to retrieve
B. Grant the AVLO read-only access to the specific targeting Workshop product; confirm correct classification marking; verify the AVLO can view the product but cannot modify target data
C. Brief the AVLO verbally on target locations rather than sharing the MSS product to minimize distribution
D. Add the AVLO as an editor so they can annotate the product directly with deconfliction notes

**7. After a fires mission, the MSS COP still displays the engaged target as active. The most accurate characterization is:**

A. A data reporting gap — MSS is displaying the last reported target status; the fires reporting chain has not yet submitted post-strike reporting, or the BDA pipeline has not updated the display
B. The target was not successfully engaged — MSS would automatically update target status upon successful engagement
C. A system error requiring immediate notification to the MSS administrator
D. Normal behavior — COP target displays are always one reporting cycle behind actual fires execution

**8. In a degraded connectivity scenario where MSS is unavailable, fire support personnel should:**

A. Suspend all fires planning until MSS connectivity is restored
B. Use personal devices to access MSS through civilian network connectivity to maintain fires data display
C. Transfer all targeting authority to higher headquarters until connectivity is restored
D. Continue fires planning using manual targeting and fire support coordination procedures; maintain a manual record of FSCM locations and target status; identify which MSS-supported products are now stale and brief accordingly when connectivity is restored

**9. Table 2-3 in TM-40B maps the D3A targeting cycle to data platform functions. Which of the following correctly pairs a D3A phase with its key data products?**

A. Decide — ICSM, NAI/TAI tracking, target confidence records
B. Detect — HPTL, TSS, AGM
C. Deliver — Fire missions, FSEM updates, BDA requests
D. Assess — HPTL, TSS, target nomination records

**10. The CARVER scoring methodology (Table 2-6, FM 3-60 Appendix G) evaluates targets across six criteria, each scored 1–5. Which of the following correctly defines a CARVER factor and its scoring scale?**

A. Criticality — how quickly the OPFOR can replace the target; 1 = immediate replacement, 5 = irreplaceable within campaign timeline
B. Vulnerability — how important the target is to OPFOR capability; 1 = minimal impact, 5 = catastrophic loss
C. Recuperability — how susceptible the target is to available munitions; 1 = hardened/deeply buried, 5 = soft/exposed
D. Accessibility — whether the target can be reached by available fires means; 1 = deeply protected, 5 = fully accessible to multiple systems

---

## SECTION 2 — SHORT ANSWER

*Answer in 3–5 sentences. (5 points each)*

**11. Your fires officer has configured three MSS alerts for the targeting working group. During a test run, Alert 2 (HVT in TAI HAMMER) fires when no HVT data is present in that area. Walk through the troubleshooting steps you would take to identify and resolve the false-positive before the next targeting board.**

*(Write your answer below)*

_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

**12. The S3 asks why the fires product in MSS Workshop still shows Target AC-12 as unengaged when the FSE submitted a fires report confirming the mission completed 90 minutes ago. Explain the difference between fires reporting submission and MSS data display, and describe how you would resolve the discrepancy before the targeting board convenes.**

*(Write your answer below)*

_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

---

## SECTION 3 — SCENARIO (10 points)

**Read the following scenario and answer the question below.**

It is 0615. The targeting working group convenes at 0700. You open MSS to finalize the fires product and discover:

- BDA for Target AC-09 is missing — the strike was executed at 1800 yesterday and no BDA has been entered
- BDA for Targets AC-10, AC-11, and AC-12 is current (entered 0530)
- Fires Alert 1 (HVT in TAI ANVIL) has not fired based on current data
- A target acquisition report submitted at 0545 places an HVT-type vehicle inside TAI ANVIL — but Alert 1 has not fired

You have 45 minutes before the TWG.

**13. Describe your complete course of action for the next 45 minutes. Include: (a) what you investigate first and why, (b) what you will brief as confirmed vs. what you will caveat, (c) how you characterize the Target AC-09 BDA gap to the targeting board, and (d) what follow-on action you assign to resolve the Alert 1 failure.**

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
1. D — geographic boundary misconfiguration or wrong data feed is the most common fires alert failure
2. A — halt and add timestamps before continuing; omission must be corrected, not estimated
3. B — brief IDA as reported; characterize as initial assessment only; do not brief as destroyed without CUBA
4. C — pause the board; verify FSCMs before approving any fires; brief the FSCM currency gap
5. C — complete fires alert: trigger condition + data source + notification path
6. B — read-only access; classification marking; verify viewer-only permissions
7. A — data reporting gap; BDA pipeline has not updated the COP
8. D — manual fires procedures + manual FSCM tracking + brief stale products when connectivity restored

**Section 2 — Expected elements:**
11. Should include: verify the TAI HAMMER geographic boundary definition (check polygon coordinates against the targeting officer's map product), confirm the data source selected for Alert 2 is the correct HVT track feed, test with a known-negative event location outside TAI HAMMER to isolate whether the boundary or the feed configuration is the fault, check whether multiple overlapping TAI boundaries could be causing a cross-trigger.
12. Should explain: pipeline latency between fires report submission and dataset update in MSS; the fires report enters the reporting system but the MSS dataset may not have refreshed; need to trace the data pipeline to find where the update is queued; caveat the targeting product with "as of [last pipeline update]" timestamp; escalate to S6 if the pipeline is stalled.

**Section 3 — Expected elements:**
(a) Investigate Alert 1 failure first — an actual target acquisition report placing an HVT in TAI ANVIL that did not trigger Alert 1 is a higher-priority problem than missing BDA for AC-09, because it affects an active targeting decision the board may need to make today.
(b) Brief Targets AC-10, AC-11, and AC-12 BDA as current; present Target AC-09 with no BDA — characterize it as post-strike status unknown pending BDA submission; for the 0545 acquisition report, brief it as reported intelligence pending MSS correlation — do not brief absence of Alert 1 as confirmation the HVT is not present.
(c) Tell the targeting board: Target AC-09 was engaged at 1800 yesterday; no BDA has been entered; current target status is post-strike unknown; recommend the board treat AC-09 as requiring re-acquisition or re-engagement until BDA is confirmed; note the reporting gap and flag for immediate action by the fires reporting chain.
(d) Assign S2/FSE to contact the S6 to investigate why the 0545 target acquisition report did not update the HVT layer and trigger Alert 1; require a status report before the end of the TWG; if the alert configuration is confirmed as the failure point, re-configure and test before the next targeting cycle.

---

*Total points: 40 (MC: 10 × 2 = 20, SA: 2 × 5 = 10, Scenario: 10). Passing score: 32 (80%).*

*USAREUR-AF Operational Data Team*
*EX_TM40B-POST | Version 1.0 | March 2026*
