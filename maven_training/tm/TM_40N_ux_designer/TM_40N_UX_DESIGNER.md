# TM-40N — MAVEN SMART SYSTEM (MSS)

> **BLUF:** TM-40N qualifies UI/UX designers to conduct user research, design information architectures, build interactive prototypes, and deliver production-ready Workshop and Slate application designs on the MSS platform. This is a design manual — it produces validated, implementable design artifacts, not just wireframes.
> **Prereqs:** TM-10, Maven User; TM-20, Builder; TM-30, Advanced Builder (required); familiarity with user research methods and visual design principles
> *HQ USAREUR-AF · v1.0 · 2026 · DISTRIB: USG only · AUTH: C2DAO/UDRA v1.1*

> **WARNING: Design decisions at TM-40N level directly shape how commanders and staff consume operational data. A poorly designed dashboard can obscure critical information, delay decisions, or create false confidence in incomplete data. Apply Soldier Centered Design discipline. Validate with users. Test in representative environments.**
> **CAUTION: User research in operational and classified environments requires OPSEC awareness. Interview notes, usability recordings, and design artifacts may contain operationally sensitive information. Handle and store IAW unit classification guidance.**

---

## CHAPTER 1 — INTRODUCTION: THE UI/UX DESIGNER ROLE IN MSS

### 1-1. Purpose and Scope

**BLUF:** TM-40N qualifies UI/UX designers to conduct user research, design information architectures, build interactive prototypes, and deliver production-ready application designs on the MSS platform. The designer is the main conduit between the user and the product team.

This manual provides task-based instruction for UI/UX designers operating on the Maven Smart System (MSS). MSS is the USAREUR-AF enterprise AI/data platform built on Palantir Foundry. TM-40N personnel translate operational requirements into usable, accessible interfaces that WFF-qualified users (TM-40A–F) and all MSS consumers interact with daily.

**TM-40N covers:**
- Soldier Centered Design (SCD): the Army adaptation of human-centered design methodology for operational environments
- User research: interview techniques, contextual inquiry, usability testing in classified/OCONUS settings
- Information architecture: organizing data-dense displays for rapid decision-making under stress
- Visual design for military applications: color systems for tactical displays, classification marking in UI, contrast and readability in field conditions
- Workshop application design: layout patterns, widget selection, dashboard hierarchy, responsive design within Foundry constraints
- Prototyping: low-fidelity sketches through high-fidelity interactive mockups; design-to-backlog handoff
- Accessibility: Section 508 compliance, WCAG 2.1 AA standards, assistive technology considerations
- Design governance: pattern libraries, design review processes, consistency across MSS applications

**TM-40N does NOT cover:**
- TypeScript/OSDK application development — see TM-40L (Software Engineer)
- Custom React widget coding — see TM-40L; TM-40N defines the design, TM-40L implements
- Pipeline design or data modeling — see TM-30
- AI/ML model interface design — see TM-40H (AI Engineer) for AIP Logic; TM-40N may design the surface
- Program/project management — see TM-40J (Program Manager)

> **NOTE:** TM-40N is peer to TM-40J (Program Manager) and TM-40L (Software Engineer). Together, these three tracks form the ASF-aligned "balanced team" triad: PM + Designer + Engineer. All specialist tracks require TM-30 as prerequisite. Coordinate across tracks — operational systems require all three disciplines working in concert.

### 1-2. Curriculum Position, Advanced Track, and WFF Context

**Prerequisite:** TM-30 (Advanced Builder) is REQUIRED. Familiarity with visual design tools (Figma, Sketch, or equivalent) and user research methods is recommended independently of the TM series.

**Advanced track:** Upon completing TM-40N, qualified UI/UX Designers should pursue **TM-50N (Advanced UI/UX Designer)** for advanced topics including design systems at scale, DDIL-aware design patterns, cross-domain and coalition UI challenges, and design operations governance.

**Peer specialist tracks:** The UI/UX Designer defines how users interact with every MSS application surface. Coordinate with TM-40J (Program Manager) on backlog prioritization — the PM owns the backlog, the Designer validates what goes into it based on user research. Coordinate with TM-40L (Software Engineer) on implementation feasibility — the SWE implements what the Designer specifies; the Designer-SWE interface is a high-frequency coordination point. Coordinate with TM-40H (AI Engineer) when AI-powered features require user-facing surfaces — AIP Logic outputs need designed interaction patterns.

**WFF awareness:** UI/UX Designers on MSS build the interaction layer that WFF-qualified users (TM-40A through TM-40F — Intelligence, Fires, Movement and Maneuver, Sustainment, Protection, and Mission Command) depend on for operational decision-making. A dashboard that buries critical readiness data, a form that introduces data entry errors, or a workflow that adds unnecessary steps to a time-sensitive process has direct operational impact. Design quality is a WFF readiness factor.

---

### 1-3. The UI/UX Designer's Role in USAREUR-AF

USAREUR-AF is the Army Service Component Command (ASCC) to USEUCOM. MSS supports theater land operations across the European AOR including V Corps, 21st TSC, 7th ATC, G2 all-source, and multinational elements. UI/UX Designers at TM-40N level are the human-systems integrators of the USAREUR-AF data ecosystem.

**The TM-40N role in the data chain:**

```
MISSION REQUIREMENT
        |
   USER RESEARCH (TM-40N)
        |
   DESIGN ARTIFACTS (TM-40N)
        |
   PM BACKLOG (TM-40J) ←→ DESIGN VALIDATION (TM-40N)
        |
   IMPLEMENTATION (TM-40L / TM-30)
        |
   USABILITY TESTING (TM-40N)
        |
OPERATIONAL USE (TM-40A–F, TM-10)
```

The Designer does not build in isolation. SCD requires continuous contact with the user population — observing how soldiers actually use the system in their operational context, not how the team assumes they use it. In USAREUR-AF, this means understanding that users may be operating across multiple classification levels, in austere field environments, on varying screen sizes, under time pressure, and potentially under degraded network conditions (DDIL).

---

## CHAPTER 2 — SOLDIER CENTERED DESIGN (SCD) METHODOLOGY

### 2-1. SCD Overview

**BLUF:** Soldier Centered Design is the Army's adaptation of human-centered design. It adds operational context, classification awareness, and military decision-making frameworks to commercial UX methodology.

SCD follows a four-phase iterative cycle:

```
    DISCOVER              DEFINE
  (User Research)    (Problem Framing)
        \                /
         \              /
          \            /
           \          /
    DELIVER           DEVELOP
  (Test & Iterate)  (Prototype)
```

**Phase 1 — Discover:** Understand the user, their environment, their tasks, and their pain points through direct observation and interviews. In military context, this includes understanding the operational tempo, classification constraints, and decision-making hierarchy.

**Phase 2 — Define:** Synthesize research findings into problem statements, user personas, and journey maps. Frame the design problem in operational terms — what decision does this tool support, and what information does the decision-maker need, in what format, at what speed?

**Phase 3 — Develop:** Generate design solutions through sketching, wireframing, and prototyping. Evaluate against operational requirements, not just usability heuristics. A design that is "usable" but does not support the operational decision is a failed design.

**Phase 4 — Deliver:** Test prototypes with representative users in representative environments. Iterate based on feedback. Hand off validated designs to the engineering team (TM-40L) with specifications sufficient for implementation.

### 2-2. User Research in Operational Environments

**BLUF:** User research in a military context has constraints that commercial UX does not — classification, OPSEC, rank dynamics, and limited access windows. Plan for these or your research will fail.

**Research methods applicable to MSS:**

| Method | When to Use | Classification Considerations |
|--------|-------------|------------------------------|
| Contextual inquiry | Observe users in their actual work environment | Must be conducted at the classification level of the work; notes inherit classification of observed content |
| Semi-structured interview | Understand goals, frustrations, workflows | Interview guide can be unclassified; responses may not be — plan accordingly |
| Usability testing | Validate prototypes against real tasks | Test data must match classification level; synthetic data preferred for unclassified testing |
| Card sorting | Understand mental models for information architecture | Generally unclassified unless categories reference operational data |
| Survey / questionnaire | Broad feedback from distributed user base | Can be administered across USAREUR-AF geography; must clear unit approval |

**Rank dynamics:** A PFC will not freely critique a system in front of a COL, even if the COL built it. Conduct research sessions with peers or small rank-band groups. Anonymous surveys supplement but do not replace direct observation.

**Access windows:** Operational units have limited time for UX research. Negotiate research sessions during low-tempo periods. Prepare thoroughly — you may get one 30-minute window with a key user group. Do not waste it on questions you could answer by reading doctrine.

### 2-3. Design Artifacts and Handoff

**BLUF:** Every design artifact must be specific enough for a TM-40L SWE to implement without guessing intent.

**Required artifacts for design-to-development handoff:**

1. **User persona(s)** — role, rank range, operational context, key tasks, pain points
2. **Information architecture** — what data appears where, hierarchy, navigation
3. **Wireframes** — layout, widget placement, interaction flow (low-fi acceptable for review; high-fi required for handoff)
4. **Interaction specification** — what happens when the user clicks, filters, submits; error states; loading states; empty states
5. **Visual design specification** — colors, typography, spacing, classification markings, responsive behavior
6. **Accessibility checklist** — 508/WCAG compliance verification for the specific design

---

## CHAPTER 3 — INFORMATION ARCHITECTURE FOR MSS

### 3-1. Data-Dense Display Design

**BLUF:** Military users consume more data per screen than commercial users. The goal is not minimalism — it is structured density. Every pixel should earn its place.

MSS dashboards typically display operational data that supports time-sensitive decisions. Commercial UX principles like "reduce cognitive load through whitespace" must be adapted: a commander reviewing a readiness dashboard needs to see all critical indicators simultaneously, not click through tabs to find them.

**Principles for MSS information architecture:**

1. **Decision-first hierarchy:** Structure the display around the decision the user needs to make, not the data model. What question is the user answering? Put the answer at the top.
2. **Progressive disclosure for detail, not for primary data:** Summary views are acceptable; hiding critical operational data behind clicks is not.
3. **Spatial consistency:** Once a user learns where "readiness" appears on the screen, it must always appear there. Cross-application consistency matters more than individual application aesthetics.
4. **Status encoding:** Use redundant encoding (color + icon + text) for status indicators. Color alone fails for colorblind users and under poor lighting conditions. Classification markings must use approved color codes.

### 3-2. Workshop Layout Patterns

**BLUF:** Workshop is the primary application surface on MSS. Designers must understand its layout system, widget catalog, and constraints before designing.

Workshop applications use a grid-based layout system with configurable widgets. The Designer's role is to specify:

- Grid layout and widget placement
- Widget type selection (table, chart, map, filter, action button, text, metric card)
- Data binding: which Ontology properties map to which widget elements
- Filter logic: what filtering controls are available and how they chain
- Action integration: where action buttons appear and what workflows they trigger

**Common Workshop patterns for MSS:**

| Pattern | Use Case | Layout |
|---------|----------|--------|
| Command dashboard | Commander's overview of operational readiness | Top: KPI metric cards; Middle: map + status table; Bottom: trend charts |
| Data entry form | Structured data input by operators | Left: navigation/context; Center: form fields; Right: reference data |
| Drill-down explorer | Analyst deep-dive into specific entities | Top: filters; Center: object list with detail pane; Bottom: related objects |
| Comparison view | Side-by-side analysis of units, time periods | Split layout with synchronized filters |

---

## CHAPTER 4 — VISUAL DESIGN FOR MILITARY APPLICATIONS

### 4-1. Color Systems and Classification Marking

**BLUF:** Color in military applications serves functional purposes beyond aesthetics. Classification banners, status indicators, and threat levels all have mandated or conventionally expected color mappings.

**Classification banner requirements:**
- Every MSS application must display the classification level of the data being viewed
- Banner position: top and bottom of every screen
- Banner colors follow IC/DoD standards (green = UNCLASSIFIED, blue = CONFIDENTIAL, red = SECRET, yellow = TOP SECRET, etc.)
- Classification banners are not optional design elements — they are security requirements

**Status color conventions for MSS:**

| Status | Primary Color | Secondary Indicator |
|--------|--------------|---------------------|
| Operational / Ready | Green | ● filled circle + "READY" text |
| Degraded / Partial | Amber/Yellow | ◐ half circle + "DEGRADED" text |
| Non-operational / Not Ready | Red | ○ empty circle + "NOT READY" text |
| Unknown / No Data | Gray | ? icon + "NO DATA" text |

> **NOTE:** Always pair color with a secondary indicator (icon, text, pattern). Per WCAG 2.1, color must not be the sole means of conveying information (Success Criterion 1.4.1).

### 4-2. Typography and Readability

**BLUF:** MSS applications are used in offices, TOCs, and field environments. Design for the worst viewing conditions, not the best.

- Minimum body text size: 14px (field environments); 12px acceptable for dense data tables in office environments only
- Minimum contrast ratio: 4.5:1 for normal text, 3:1 for large text (WCAG AA)
- Font selection: sans-serif for screen; monospace for data values, codes, DTGs
- Line length: 60–80 characters for reading text; data tables may be wider
- DTG (Date-Time Group) formatting: always monospace, always consistent format across all applications

### 4-3. Designing for Field Conditions

**BLUF:** If the design only works on a 27-inch monitor in a climate-controlled office, it fails in the AOR.

Field environment design constraints:
- **Screen size:** Laptops (13–15 inch) are the most common field platform; some users access via tablets
- **Lighting:** TOCs may have reduced lighting; outdoor use involves glare. High contrast is mandatory, not optional
- **Gloves:** Touchscreen users in winter may wear gloves. Touch targets must be minimum 44x44px (WCAG) — 48x48px preferred for gloved operation
- **Network:** DDIL conditions mean applications may load slowly or partially. Design loading states and offline indicators explicitly

---

## CHAPTER 5 — PROTOTYPING AND USABILITY TESTING

### 5-1. Prototyping Workflow

**BLUF:** Start with paper. End with a clickable prototype that a SWE can build from. Skip nothing in between.

**Prototyping progression:**

| Stage | Fidelity | Tool | Purpose | Review Gate |
|-------|----------|------|---------|-------------|
| 1. Sketches | Low | Paper, whiteboard | Explore layout options; rapid iteration | Team review (PM + SWE) |
| 2. Wireframes | Medium | Figma, Balsamiq, or equivalent | Structure, content hierarchy, interaction flow | Stakeholder review |
| 3. Interactive mockup | High | Figma prototyping, or HTML/CSS static | Visual design, interaction behavior, realistic data | Usability test with representative users |
| 4. Workshop prototype | Production | Foundry Workshop | Actual platform with real/synthetic data | Go/No-Go evaluation |

**Design-to-backlog handoff:** At Stage 3, the Designer produces a handoff package (see §2-3) for the PM (TM-40J) to write user stories and the SWE (TM-40L) to implement. The Designer reviews implementation against the specification during sprint review.

### 5-2. Usability Testing on MSS

**BLUF:** Test with soldiers, not with the design team. If you only tested with people who built it, you did not test.

**Usability test protocol for MSS applications:**

1. **Recruit:** 5–8 representative users from the target WFF track. Include range of ranks and experience levels.
2. **Prepare:** Write task scenarios based on real operational tasks, not abstract exercises. Use synthetic data at the appropriate classification level.
3. **Conduct:** Think-aloud protocol. Observer takes notes on task completion, errors, confusion points, time on task. Do not lead or coach.
4. **Analyze:** Identify patterns across participants. Prioritize issues by severity (blocks task completion > causes errors > causes confusion > minor friction).
5. **Report:** Findings document with severity ratings, screenshots, and recommended design changes. Route to PM for backlog prioritization.

---

## CHAPTER 6 — ACCESSIBILITY AND COMPLIANCE

### 6-1. Section 508 and WCAG 2.1 Requirements

**BLUF:** Federal systems must meet Section 508 accessibility standards. WCAG 2.1 AA is the technical benchmark. This is not optional.

**Key WCAG 2.1 AA requirements for MSS applications:**

| Principle | Requirement | MSS Application |
|-----------|-------------|-----------------|
| Perceivable | Text alternatives for non-text content | All icons, charts, and images need alt text or aria labels |
| Perceivable | Color is not the sole means of conveying information | Status indicators must include icon + text (see §4-1) |
| Perceivable | Minimum contrast ratio 4.5:1 | Verify all text against background colors |
| Operable | Keyboard navigable | All interactive elements reachable via keyboard |
| Operable | Touch target minimum 44x44px | Critical for tablet and field use |
| Understandable | Consistent navigation | Same navigation pattern across all MSS applications |
| Understandable | Error identification and suggestion | Form validation messages must be specific and actionable |
| Robust | Compatible with assistive technologies | Semantic HTML, ARIA roles where needed |

### 6-2. Accessibility Testing Checklist

Before any MSS application design is approved for implementation:

- [ ] Contrast ratios verified (use automated tool + manual spot check)
- [ ] All interactive elements keyboard-accessible
- [ ] All non-text content has text alternatives
- [ ] Color is not sole information carrier
- [ ] Touch targets meet minimum size
- [ ] Classification banners render correctly at all viewport sizes
- [ ] Screen reader can parse page structure and content order
- [ ] Error messages are specific, actionable, and associated with the correct form field
- [ ] Loading and empty states are announced to assistive technology

---

## CHAPTER 7 — DESIGN GOVERNANCE AND PATTERN LIBRARIES

### 7-1. MSS Design System

**BLUF:** Consistency across MSS applications is a design requirement, not a nice-to-have. Users should not have to relearn navigation, status indicators, or interaction patterns when moving between applications.

**MSS design system components:**

| Component | Standard | Owner |
|-----------|----------|-------|
| Classification banners | IC/DoD mandated colors and placement | Security; Designer verifies implementation |
| Status indicators | Color + icon + text (§4-1) | TM-40N defines; TM-40L implements |
| Navigation pattern | Left sidebar for app-level; top bar for global/MSS-level | TM-40N defines |
| Data tables | Sortable, filterable, paginated; consistent column header styling | TM-40N defines; Workshop provides base |
| Form patterns | Label position, validation timing, error message format | TM-40N defines |
| Typography scale | Heading hierarchy, body text, data values, DTGs | TM-40N defines |
| Color palette | Operational colors (§4-1), neutral palette, accent palette | TM-40N defines |

### 7-2. Design Review Process

**BLUF:** No design ships without review. The review catches consistency violations, accessibility gaps, and operational misalignment before code is written.

**Design review gates:**

| Gate | Reviewer | Criteria |
|------|----------|----------|
| Concept review | PM (TM-40J) + SWE (TM-40L) | Problem framing, feasibility, scope |
| Design review | Peer Designer + PM | Pattern library compliance, accessibility checklist, information hierarchy |
| Usability review | Representative users (5+) | Task completion, error rate, satisfaction |
| Implementation review | Designer reviews SWE build | Fidelity to specification, accessibility in production |

---

## CHAPTER 8 — CROSS-TRACK COORDINATION

### 8-1. The Balanced Team Model

**BLUF:** PM + Designer + Engineer is the minimum viable product team. The Designer is the voice of the user on the team — the "Empathizer in Chief" who ensures every product decision is grounded in validated user needs.

The Army Software Factory (ASF) balanced team model places Designer, PM, and Engineer as co-equal roles on a product team. The ASF concept of the Designer as Empathizer in Chief means the Designer owns the team's understanding of the user: who they are, what they need, where the current experience fails them, and what "better" looks like in their operational context. This is not a courtesy title — it is a functional responsibility. If no one on the team can articulate the user's top three pain points from direct observation, the Empathizer in Chief has not done the job. In the MSS training framework:

| Role | TM Track | Primary Responsibility |
|------|----------|----------------------|
| Program Manager | TM-40J | Backlog, priorities, stakeholder management |
| UI/UX Designer | TM-40N | User research, design specification, usability validation |
| Software Engineer | TM-40L | Implementation, code quality, deployment |

**Coordination cadence:**

- **Daily:** Designer and SWE sync on in-progress implementation questions
- **Sprint planning:** Designer presents validated designs; PM writes stories; SWE estimates
- **Sprint review:** Designer evaluates implementation fidelity; PM evaluates against acceptance criteria
- **Research share-out:** Designer presents user research findings to full team (minimum monthly)

### 8-2. Designer-Engineer Handoff

**BLUF:** The handoff specification is a contract. Ambiguity in the spec becomes bugs in the product.

The Designer-SWE interface requires explicit specification of:

1. **Layout:** Grid positions, responsive breakpoints, minimum/maximum widths
2. **Data binding:** Which Ontology property maps to which visual element
3. **Interaction:** Click, hover, filter, sort, submit — what triggers what
4. **States:** Default, loading, empty, error, success — every state designed, not just the happy path
5. **Edge cases:** What happens with 0 results? 10,000 results? A 200-character unit name? Null values?

### 8-3. Designer-Platform Engineer Coordination

**BLUF:** The Platform Engineer (TM-40O) controls the environment where designs run. Coordinate on performance budgets, CDN configuration, and deployment constraints.

When designing applications that will be deployed across USAREUR-AF networks:

- Confirm maximum page load budget with Platform Engineering (target: <3s on degraded network)
- Confirm image/asset optimization requirements (compression, lazy loading)
- Confirm browser/platform compatibility requirements (which browsers, which versions)
- Confirm offline/DDIL fallback behavior with Platform Engineering

---

## APPENDIX A — GLOSSARY

| Term | Definition |
|------|-----------|
| SCD | Soldier Centered Design — Army adaptation of human-centered design methodology |
| DDIL | Denied, Disrupted, Intermittent, and Limited bandwidth — network conditions common in tactical environments |
| WFF | Warfighting Function — Army doctrinal framework organizing combat power (Intelligence, Fires, M&M, Sustainment, Protection, Mission Command) |
| DTG | Date-Time Group — standardized military date/time format |
| WCAG | Web Content Accessibility Guidelines — W3C standard for web accessibility |
| 508 | Section 508 of the Rehabilitation Act — federal accessibility requirements |
| TOC | Tactical Operations Center |
| AOR | Area of Responsibility |
| Workshop | Foundry's no-code application builder — primary MSS application surface |
| Slate | Foundry's legacy code-based application builder (HTML/CSS/JS) — maintenance only for existing apps |

## APPENDIX B — REFERENCES

| Reference | Relevance |
|-----------|-----------|
| TM-40J — Program Manager | Balanced team coordination, backlog management |
| TM-40L — Software Engineer | Implementation partner, design handoff consumer |
| TM-40O — Platform Engineer | Deployment environment, performance constraints |
| TM-30 — Advanced Builder | Workshop configuration skills (prerequisite) |
| WCAG 2.1 (W3C) | Accessibility technical standard |
| DoD Software Modernization Strategy (Feb 2022) | Strategic context for software factory approach |
| ASF Soldier Centered Design methodology | Foundation for SCD practice in TM-40N |
