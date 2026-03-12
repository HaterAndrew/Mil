# EX-40F — Mission Command
## Practical Exercise — TM-40F Proficiency

**Version 1.0 | March 2026**
**Prerequisite:** TM-40F, Mission Command WFF Technical Manual (and TM-10, TM-20); CONCEPTS_GUIDE_TM40F_MISSION_COMMAND
**Duration:** 3–4 hours
**Environment:** MSS training instance with standard user access; no coding or pipeline permissions required (see ENVIRONMENT_SETUP.md)

---

## SCENARIO

You are the battle captain at a BCT headquarters during a force projection exercise. The commander requires a fully configured MSS common operating picture, CCIR alerts active, battle rhythm dashboard, and a Battle Update Assessment (BUA) read-ahead product — all before a theater-level VTC in four hours.

At T+90 min, the evaluator will inject a data staleness event: the readiness data feed for 1st Battalion stops updating.

**Training environment:** Pre-loaded synthetic operational data (readiness, SIGACT-analog events, personnel status). No real operational data.

---

## TASK LIST

### Task 1 — Configure the Common Operating Picture (45 min)
- [ ] Add and configure the following COP layers: unit positions (3 subordinate battalions), equipment readiness status overlay, and operational event markers
- [ ] Verify the data-as-of timestamp for each layer is within the training data's current period
- [ ] Identify any layer with a stale or missing data source and note it for the evaluator
- **Go:** All three layers configured and displaying; at least one timestamp noted and verified; stale feeds identified (if any)
- **No-Go:** Layers missing or timestamps not verified; no awareness of data currency

### Task 2 — Configure CCIR Alerts (30 min)
- [ ] Using the provided Commander's CCIR Guidance Card, configure the following three CCIRs in MSS:
  - CCIR 1: Any battalion readiness below 70% (threshold-based)
  - CCIR 2: Any operational event at grid reference within the defined sensitivity area (geographic-based)
  - CCIR 3: Personnel strength below 85% for any subordinate battalion (threshold-based)
- [ ] Set notification routing for each CCIR to: Battle Captain and S3 positions
- [ ] Verify CCIRs fire correctly using the provided test dataset values
- **Go:** All three CCIRs configured with correct thresholds; routing set; at least 2 of 3 fire correctly on test data
- **No-Go:** Threshold values do not match Commander's guidance card; routing absent; fewer than 2 CCIRs fire on test data

### Task 3 — Build the Battle Rhythm Dashboard (30 min)
- [ ] Using the provided weekly event list, build a battle rhythm dashboard in Workshop showing: today's scheduled events with status (complete/pending/upcoming), this week's events, and key decision gates in the next 14 days
- [ ] Link the readiness summary widget to the live readiness dataset (not a static text widget)
- [ ] Confirm the dashboard updates when the underlying data changes
- **Go:** All three components present; readiness widget is live-linked; dashboard updates on data change
- **No-Go:** Static data used instead of live dataset; missing components; dashboard does not update

### Task 4 — Produce BUA Read-Ahead Product (45 min)
- [ ] Build a BUA read-ahead package containing: overall readiness summary (current vs. threshold), CCIR status (active/triggered/clear), operational outlook (key events next 24 hours), and data-as-of timestamps on every data element
- [ ] Format the product for an O-5/CG audience — no jargon, no raw data, no unexplained abbreviations
- [ ] Ensure the product is correctly marked per OPSEC classification guidance for training data
- **Go:** All four sections present; timestamps on all data elements; formatting appropriate for commander audience; OPSEC marking present
- **No-Go:** Missing timestamps on any data element; raw data exposed without summary; OPSEC marking absent

### Task 5 — Data Staleness Inject Response (30 min)

*Evaluator injects this at the T+90 min mark. Do not brief participants on this in advance.*

The 1st Battalion readiness data feed has stopped updating — data is now 6 hours old.

- [ ] Identify which COP elements and BUA sections are affected by the stale feed
- [ ] Update the BUA product to reflect the data gap with an explicit caveat on affected elements
- [ ] Brief the evaluator (in role as S3) on: what is affected, what is still current, what you will/will not brief to the commander, and what action you are taking to resolve the feed
- **Go:** Affected elements correctly identified; BUA updated with caveat; verbal brief covers all four elements
- **No-Go:** Stale data presented as current; no caveat added; brief to S3 misses the impact or the resolution action

### Task 6 — OPSEC and Distribution (15 min)
- [ ] Apply correct classification marking to the final BUA product
- [ ] Configure the BUA Workshop view to share with the commander's personal device account (read-only) and restrict edit access
- [ ] Confirm the evaluator (in the role of the commander) can view but not edit the product
- **Go:** Marking correct; read-only share confirmed
- **No-Go:** Marking absent or incorrect; evaluator account has edit access

---

## EVALUATOR NOTES

**Scoring:** 6 tasks. Go on 5 of 6 = overall Go. No-Go on Task 2 (CCIR configuration) or Task 5 (data staleness response) = automatic No-Go regardless of total score.

**Pre-exercise checklist:**
- Confirm training accounts have standard MSS access (no build/pipeline permissions needed)
- Pre-load the synthetic operational dataset and confirm all three COP layers have data
- Prepare the Commander's CCIR Guidance Card (see ENVIRONMENT_SETUP.md) — hand to participant at exercise start
- Know the exact threshold values on the card so you can verify Task 2 CCIR configurations
- Prepare the test dataset values for CCIR verification (Task 2)
- At T+90 min, pause the readiness feed for 1st Battalion (instructions in ENVIRONMENT_SETUP.md)

**Common failure modes:**

| Task | Common Failure | Evaluator Guidance |
|------|---------------|--------------------|
| Task 1 | Timestamps not checked | Ask: "How do you know the data is current?" — if participant cannot point to timestamp, No-Go for that element |
| Task 2 | Threshold matches card but feed not selected | CCIR with wrong data source will not fire — ask participant to show the CCIR definition |
| Task 2 | Notification routed to personal account not position | Position-based routing is required; personal account routing = coaching note but not No-Go if both are set |
| Task 3 | Battle rhythm dashboard uses static text | Ask participant to change one underlying value — if dashboard does not update, No-Go |
| Task 4 | BUA lacks data-as-of timestamps | Most common failure; ask participant to show one timestamp before grading — if none present, No-Go |
| Task 5 | Participant tries to fix the pipeline | This is the wrong response at this level; they should characterize and escalate; if they spend > 5 min trying to fix the feed, prompt: "What do you need to brief right now?" |
| Task 6 | Evaluator has edit access | Sharing step was done wrong; mark Task 6 No-Go |

**Data staleness inject procedure:**
See ENVIRONMENT_SETUP.md for the exact steps to pause the 1st Battalion readiness feed at T+90 min.

---

## ENVIRONMENT SETUP

See [ENVIRONMENT_SETUP.md](ENVIRONMENT_SETUP.md) for full setup instructions.
