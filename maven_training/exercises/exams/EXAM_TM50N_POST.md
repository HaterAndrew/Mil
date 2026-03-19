# POST-TEST — TM-50N: ADVANCED UI/UX DESIGNER
## Maven Smart System (MSS) — USAREUR-AF

| Field | Detail |
|---|---|
| **Course** | TM-50N: Advanced UI/UX Designer |
| **Form** | Post-Test |
| **Level** | TM-50N (Advanced Specialist) |
| **Audience** | Experienced UI/UX designers completing TM-50N training |
| **Time Allowed** | 45 minutes |
| **Passing Score** | 70% (32/45) |

---

## INSTRUCTIONS

This assessment evaluates knowledge and skills gained during TM-50N training. Answer all questions. A score of 70% or higher is required for course credit.

---

## SECTION 1 — MULTIPLE CHOICE

*Circle the letter of the best answer. (2 points each)*

**1. In the MSS design token architecture, "classification colors" are classified as:**

A. Configurable — application teams can choose their own classification banner colors
B. Optional — only required for applications handling classified data
C. Inherited — automatically derived from the application's accent color
D. Locked — mandated by IC/DoD standards and cannot be overridden by application designers

**2. The four DDIL design tiers are:**

A. Full connectivity, Degraded, Intermittent, Disconnected
B. Online, Offline, Error, Maintenance
C. Local, Regional, National, Global
D. Classified, Unclassified, Coalition, Public

**3. When an MSS application is in "disconnected" (Tier 4 DDIL) mode, the correct design response is:**

A. Show a full-screen error message and block all interaction
B. Display cached data with prominent staleness indicators, queue user actions for later sync, and clearly communicate offline status
C. Redirect the user to a different application
D. Show only the classification banner and nothing else

**4. A component in the MSS design system library must include documentation covering:**

A. Only a screenshot showing what it looks like
B. Only the Figma source file
C. Name, variants, accessibility notes, do/don't examples, data binding support, and responsive behavior
D. A video tutorial showing how to use it

**5. The purpose of accessibility remediation prioritization (P0–P3) is:**

A. To delay fixing accessibility issues as long as possible
B. To focus remediation effort on issues with the highest operational impact first — P0 (user cannot complete task) before P3 (minor friction)
C. To assign accessibility issues to different teams based on severity
D. To determine which WCAG criteria to comply with and which to ignore

---

## SECTION 2 — SHORT ANSWER

*Answer in 2–3 sentences. (5 points each)*

**6. Explain the difference between "automated" and "manual" accessibility testing. Give one example of something that can only be tested manually.**

**7. Describe the "optimistic action" pattern for offline/DDIL interaction. When should it be used, and when should "blocked action" be used instead?**

**8. How would you handle a coalition UI where date formats differ across partner nations (US uses MM/DD/YYYY, most NATO partners use DD/MM/YYYY)?**

---

## SECTION 3 — SCENARIO

*Answer in 5–8 sentences. (10 points each)*

**9. An application designer proposes a new component that does not exist in the MSS design system library. They want to build it as a one-off for their application. Using the TM-50N design governance framework, describe the process: what review happens, who decides, and what are the possible outcomes?**

**10. You are designing a DDIL-aware version of a readiness dashboard. The data source updates every 15 minutes when connected, but the user may be disconnected for up to 4 hours. Describe your design approach: what freshness indicators would you use, how would you handle stale data, and what interaction patterns would you use for user actions during disconnection?**

---

## SCORING SUMMARY

| Section | Questions | Points Each | Total Points |
|---|---|---|---|
| Multiple Choice | 5 | 2 | 10 |
| Short Answer | 3 | 5 | 15 |
| Scenario | 2 | 10 | 20 |
| **Total** | — | — | **45** |

Passing: 32/45 (70%) — Post-test only. Pre-test is diagnostic.

---

## ANSWER KEY — INSTRUCTOR USE ONLY

*Do not distribute to students.*

**Multiple Choice:**
1. D — Classification colors are locked tokens — mandated by IC/DoD standards and cannot be overridden by application designers.
2. A — The four DDIL tiers are: Full connectivity, Degraded, Intermittent, and Disconnected.
3. B — In disconnected (Tier 4) mode: display cached data with staleness indicators, queue actions for later sync, and clearly communicate offline status.
4. C — Component documentation must include: name, variants, accessibility notes, do/don't examples, data binding support, and responsive behavior.
5. B — Remediation prioritization focuses effort on highest operational impact first — P0 (user cannot complete task) before P3 (minor friction).

**Short Answer Guidance:**

SA-6. Full credit: automated testing uses tools (axe, Lighthouse, WAVE) to check programmatically detectable issues — missing alt text, insufficient contrast, missing ARIA labels, broken tab order. Manual testing requires human judgment — example: verifying that alt text is actually meaningful (not just "image.png"), that the reading order makes logical sense, that keyboard navigation follows a coherent flow, or that screen reader announcements are understandable in context. Something only testable manually: whether alternative text accurately describes the image content and conveys the same information a sighted user would get. Partial credit (3 pts) for correct distinction without a manual-only example.

SA-7. Full credit: the optimistic action pattern assumes the action will succeed — the UI immediately reflects the change and queues it for sync when connectivity returns (e.g., updating a status field). Use optimistic when: the action is low-risk and reversible. Use blocked action when: the action is high-risk, irreversible, or requires server-side validation before proceeding (e.g., approving a fire mission, changing a classification level). Must distinguish the two patterns and provide a valid use case for each. Partial credit (3 pts) for correct definition without use cases.

SA-8. Full credit: use an unambiguous date format that eliminates misinterpretation — options: (1) display dates as "DD MMM YYYY" (e.g., "15 Mar 2026") — the month name removes ambiguity; (2) allow each user to set their locale preference and render dates accordingly; (3) store dates in ISO 8601 internally (YYYY-MM-DD) and localize on display. The key principle: never display a date that could be misread — "03/04/2026" is ambiguous; "04 Mar 2026" is not. Must propose a specific solution and explain why it eliminates ambiguity. Partial credit (3 pts) for identifying the problem without a concrete solution.

**Scenario Guidance:**

S-9. Full credit (10 pts): the process follows TM-50N design governance: (1) the designer submits a component proposal to the design system team — documenting the use case, why no existing component meets the need, and the proposed specification; (2) the design system team reviews: does this need apply to one application or many? Could an existing component be extended?; (3) possible outcomes: (a) the proposal is adopted into the design system as a new shared component (if the need is broadly applicable); (b) the designer is directed to use or extend an existing component (if a suitable one exists); (c) an exception is granted for a one-off — but it must still follow design system tokens, accessibility standards, and documentation requirements, and it is flagged for future system inclusion if other teams need it. Must describe the review process, the decision criteria, and at least two possible outcomes. Partial credit (5 pts) for describing the process without decision criteria.

S-10. Full credit (10 pts): freshness indicators: (1) a timestamp showing "Last updated: HH:MM DD MMM" in a fixed location; (2) a color-coded freshness badge (green = <15 min, amber = 15 min–1 hr, red = >1 hr, black = >4 hr / unknown); (3) a connectivity status indicator (connected/degraded/disconnected). Stale data handling: data remains visible but visually de-emphasized (reduced opacity or desaturated), with a prominent "STALE DATA" banner; critical values that may have changed significantly show a warning icon. Interaction patterns during disconnection: use the optimistic action pattern for low-risk actions (status updates, notes); use the blocked action pattern for high-risk actions (approvals, resource commitments) with a clear "Action queued — will submit when connected" message. Must address all three areas (freshness, stale data, interaction). Partial credit (5 pts) for two of three areas.

---

*USAREUR-AF Operational Data Team*
*TM-50N Post-Test | Version 1.0 | March 2026*
