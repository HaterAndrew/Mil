# POST-TEST — TM-40N: UI/UX DESIGNER
## Maven Smart System (MSS) — USAREUR-AF

| Field | Detail |
|---|---|
| **Course** | TM-40N: UI/UX Designer |
| **Form** | Post-Test |
| **Level** | TM-40N (Specialist) |
| **Audience** | UI/UX designers completing TM-40N training |
| **Time Allowed** | 45 minutes |
| **Passing Score** | 70% (39/56) |

---

## INSTRUCTIONS

This assessment evaluates knowledge and skills gained during TM-40N training. Answer all questions. A score of 70% or higher is required for course credit.

---

## SECTION 1 — MULTIPLE CHOICE

*Circle the letter of the best answer. (2 points each)*

**1. Soldier Centered Design (SCD) differs from commercial UX primarily because:**

A. It uses different software tools
B. It accounts for operational context — classification constraints, DDIL environments, rank dynamics, and higher-stakes decision-making
C. It skips user research to save time in operational settings
D. It only applies to mobile applications

**2. In the "glance, scan, commit" framework, the "glance" level (2 seconds) should allow the user to:**

A. Read all data values on the screen
B. Complete a data entry form
C. Navigate to a different application
D. Identify the overall status (e.g., green/amber/red) without reading specific values

**3. Classification banners in MSS applications must:**

A. Be displayed at the top and bottom of every screen, using IC/DoD mandated colors, and remain visible at all times
B. Be displayed only on the login screen
C. Be hidden during presentations to avoid distraction
D. Use the application's accent color for aesthetic consistency

**4. When designing status indicators for MSS, the correct approach is:**

A. Use color alone (red/amber/green) for maximum speed of recognition
B. Use icons alone to save screen space
C. Use redundant encoding: color + icon + text, because color alone fails for colorblind users and in poor lighting
D. Let each application team choose their own status encoding

**5. A design handoff to a TM-40L Software Engineer should include:**

A. Only the final mockup image
B. The mockup plus all states (default, loading, empty, error, success), interaction specification, data bindings, accessibility checklist, and edge case documentation
C. A verbal description of what the application should do
D. The Figma file only — the SWE will figure out the details

**6. When conducting user research with military personnel, a key consideration is:**

A. Rank dynamics — a junior soldier may not freely critique a system in front of senior leaders; use peer groups or anonymous methods
B. Research should only be conducted with officers
C. All research must be conducted in a SCIF
D. User research is not necessary in military settings because requirements come from higher headquarters

**7. Workshop applications on MSS use:**

A. Custom HTML/CSS with no constraints
B. A drag-and-drop interface that supports any visual design
C. React components that designers code directly
D. A grid-based layout with a fixed catalog of widget types — designers must know the widget vocabulary before designing

**8. The minimum touch target size recommended for field/gloved operation is:**

A. 20x20px
B. 32x32px
C. 44x44px (WCAG minimum), with 48x48px preferred for gloved operation
D. 100x100px

---

## SECTION 2 — SHORT ANSWER

*Answer in 2–3 sentences. (5 points each)*

**9. Describe the four phases of the SCD cycle and what happens in each phase.**

**10. You are designing a readiness dashboard. The primary user is a battalion S3 who needs to make a go/no-go decision within 30 seconds of looking at the screen. Apply the "decision-first hierarchy" principle: what should be at the top of the screen, and why?**

**11. Explain why accessibility is an operational requirement in MSS, not just a compliance checkbox. Give two specific examples of how field conditions create accessibility needs.**

**12. What are the risks of the Designer producing a handoff package that only shows the "happy path" (default state with good data)? What states are missing, and what problems does this cause during implementation?**

---

## SECTION 3 — SCENARIO

*Answer in 5–8 sentences. (10 points each)*

**13. You have designed a Workshop dashboard for the G4 Sustainment section. During usability testing, 3 out of 5 users failed to notice a critical low-stock alert because it was displayed as a small red number in the bottom-right corner. Describe: (a) why this is a severity-rated usability finding, (b) what design principle it violates, (c) what you would change, and (d) how you would verify the fix.**

**14. A TM-40L Software Engineer pushes back on your design, saying "Workshop can't do that — the widget you specified doesn't exist." Describe how you would handle this situation using the balanced team model. What are your options? Who else should be involved in the decision?**

---

## SCORING SUMMARY

| Section | Questions | Points Each | Total Points |
|---|---|---|---|
| Multiple Choice | 8 | 2 | 16 |
| Short Answer | 4 | 5 | 20 |
| Scenario | 2 | 10 | 20 |
| **Total** | — | — | **56** |

Passing: 39/56 (70%) — Post-test only. Pre-test is diagnostic.

---

## ANSWER KEY — INSTRUCTOR USE ONLY

*Do not distribute to students.*

**Multiple Choice:**
1. B — SCD accounts for operational context: classification constraints, DDIL environments, rank dynamics, and higher-stakes decision-making.
2. D — At the "glance" level (2 seconds), the user should identify overall status (green/amber/red) without reading specific values.
3. A — Classification banners must be displayed at the top and bottom of every screen, using IC/DoD mandated colors, and remain visible at all times.
4. C — Redundant encoding (color + icon + text) is required because color alone fails for colorblind users and in poor lighting.
5. B — A complete handoff includes mockups for all states, interaction specification, data bindings, accessibility checklist, and edge case documentation.
6. A — Rank dynamics require peer groups or anonymous methods; a junior soldier may not freely critique a system in front of senior leaders.
7. D — Workshop uses a grid-based layout with a fixed catalog of widget types; designers must know the widget vocabulary before designing.
8. C — WCAG minimum is 44x44px, with 48x48px preferred for gloved/field operation.

**Short Answer Guidance:**

SA-9. Full credit: SCD has four phases — (1) Discover (user research: interviews, contextual inquiry, understand the operational problem); (2) Define (synthesize research into personas, user stories, design requirements); (3) Design (wireframes, prototypes, iterate with users); (4) Deliver (handoff to engineering, usability validation, post-deployment monitoring). Each phase must be named with a description of what happens. Partial credit (3 pts) for naming phases without descriptions.

SA-10. Full credit: the top of the screen should show the go/no-go decision indicator (green/amber/red) at the "glance" level — the S3's primary task is a binary decision, so the answer to that decision must be immediately visible. Supporting data (which units are not ready, why) goes below in the "scan" level. Detail data (individual equipment status) goes in drill-down views at the "commit" level. Must cite the "decision-first hierarchy" principle and connect it to the S3's decision. Partial credit (3 pts) for correct layout without citing the decision-first principle.

SA-11. Full credit: accessibility is operational because field conditions create accessibility needs for ALL users, not just those with permanent disabilities — (1) bright sunlight washes out low-contrast screens (affects all users outdoors); (2) gloved hands cannot hit small touch targets (affects all dismounted soldiers); additional examples: NVG use restricts color perception, vehicle vibration impairs fine motor control, noise prevents audio-only cues. Must frame accessibility as an operational requirement with two specific field examples. Partial credit (3 pts) for compliance framing without operational reasoning.

SA-12. Full credit: a happy-path-only handoff is missing: loading states (what does the user see while data is fetching?), empty states (what if there's no data yet?), error states (what if the API fails?), success confirmations, boundary conditions (max text length, truncation, missing fields), and offline/DDIL states. Risks: the developer invents these states ad hoc — inconsistent UX, missed accessibility, user confusion, and rework when QA catches the gaps. Must name at least three missing states and explain the downstream impact. Partial credit (3 pts) for naming missing states without explaining consequences.

**Scenario Guidance:**

S-13. Full credit (10 pts): (a) severity: this is a high-severity finding — users failed to notice a critical alert, meaning the dashboard fails its primary purpose of surfacing urgent information; (b) violated principle: violates visual hierarchy / "glance-level" visibility — critical alerts must be at the top of the visual hierarchy, not buried in a corner; also violates redundant encoding — a small red number alone is insufficient (needs icon, animation, or prominent placement); (c) fix: move the alert to a prominent position (top of screen or modal overlay), increase size, add an icon and text label, use animation or pulse to draw attention; (d) verify: re-run usability test with 5 new users on the same task — success criterion: 5/5 users notice the alert within 5 seconds. Must address all four parts (a–d). Partial credit (5 pts) for addressing only two parts. Deduct 3 pts if the student does not include a verification method.

S-14. Full credit (10 pts): in the balanced team model, the designer, engineer, and product manager are co-equals; when a technical constraint prevents the ideal design, the correct response is: (1) understand the constraint — ask the SWE to explain what Workshop can and cannot do; (2) explore alternatives together — can the design be achieved with a different widget combination? Is there a Workshop-supported pattern that achieves the same user goal?; (3) if no Workshop solution exists, involve the Product Manager to decide: accept a design compromise, request a new widget from the platform team (TM-40O), or de-scope the feature; (4) document the decision and rationale. Must demonstrate collaborative problem-solving, not either "override the SWE" or "just accept the limitation." Partial credit (5 pts) for collaborative approach without involving PM. Deduct 3 pts if student's answer implies designer authority over engineer.

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*TM-40N Post-Test | Version 1.0 | March 2026*
