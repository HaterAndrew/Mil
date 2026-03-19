# TM-50N — MAVEN SMART SYSTEM (MSS)

> **BLUF:** TM-50N qualifies advanced UI/UX designers to build and govern design systems at scale, design for DDIL and cross-domain environments, lead coalition UI integration, and establish design operations that sustain quality across the MSS application portfolio. This manual extends TM-40N from individual application design to enterprise design leadership.
> **Prereqs:** TM-40N, UI/UX Designer (required, Go evaluation on file); demonstrated portfolio of 2+ MSS application designs from TM-40N practical exercise or operational assignment
> *HQ USAREUR-AF · v1.0 · 2026 · DISTRIB: USG only · AUTH: C2DAO/UDRA v1.1*

> **WARNING: Design system decisions at TM-50N level propagate across every MSS application. A poorly designed component, an inconsistent pattern, or a broken accessibility standard scales from one application to the entire portfolio. Validate design system changes across representative applications before publishing.**
> **CAUTION: Cross-domain and coalition UI design involves classification boundary decisions. Designs that cross classification levels must be reviewed by the ISSM before implementation. Do not assume a design pattern valid at one classification level is valid at another.**

---

## CHAPTER 1 — INTRODUCTION: THE ADVANCED UI/UX DESIGNER ROLE IN MSS

### 1-1. Purpose and Scope

**BLUF:** TM-50N extends TM-40N from designing individual applications to designing the design system itself — the patterns, components, governance, and operations that ensure consistency, accessibility, and quality across the MSS application portfolio.

This manual provides task-based instruction for advanced UI/UX designers operating on the Maven Smart System (MSS). TM-50N personnel define the design standards that all MSS application designers follow, lead design for complex multi-domain and coalition environments, and establish the operational processes that sustain design quality at scale.

**TM-50N covers:**
- Design systems at scale: building and maintaining reusable component libraries, pattern documentation, and design tokens across the MSS portfolio
- DDIL-aware design: designing applications that function under denied, disrupted, intermittent, and limited bandwidth conditions
- Cross-domain and coalition UI: designing interfaces that operate across classification levels and serve multinational users in the USAREUR-AF AOR
- Design operations (DesignOps): design review governance, quality metrics, design tooling, onboarding new designers
- Accessibility at enterprise scale: automated accessibility testing, remediation prioritization, compliance reporting
- Research operations (ResearchOps): systematizing user research across the portfolio, maintaining a research repository, preventing research duplication

**TM-50N does NOT cover:**
- Individual application design fundamentals — see TM-40N
- Custom widget implementation — see TM-40L, TM-50L
- Platform infrastructure — see TM-40O, TM-50O
- Foundry platform administration — vendor-managed

### 1-2. Curriculum Position

**Prerequisite:** TM-40N (UI/UX Designer) is REQUIRED with Go evaluation on file. Demonstrated experience designing at least 2 MSS applications (from TM-40N practical exercise or operational assignment).

**Peer advanced tracks:** Coordinate with TM-50J (Advanced PM) on portfolio-level product strategy. Coordinate with TM-50L (Advanced SWE) on design system implementation architecture and shared component libraries. Coordinate with TM-50O (Advanced Platform Engineer) on performance budgets and deployment constraints that affect design patterns.

---

## CHAPTER 2 — DESIGN SYSTEMS AT SCALE

### 2-1. MSS Design System Architecture

**BLUF:** A design system is not a style guide — it is a product that serves other products. It has users (designers and developers), releases, versioning, and governance.

**Design system layers:**

| Layer | Contents | Audience |
|-------|----------|----------|
| Design tokens | Colors, typography, spacing, shadows — the atomic values | Designers + Developers |
| Components | Buttons, tables, forms, status indicators, classification banners | Designers + Developers |
| Patterns | Page layouts, navigation, data entry workflows, drill-down patterns | Designers |
| Templates | Pre-built page templates for common MSS application types | Designers + Builders (TM-30) |
| Guidelines | Usage rules, accessibility requirements, when-to-use/when-not-to-use | Designers |

### 2-2. Component Library Management

**BLUF:** Every component in the library must be documented, accessible, tested, and versioned. Undocumented components are tech debt in the design layer.

**Component documentation standard:**

Each component entry must include:
1. **Name and description:** What it is and when to use it
2. **Variants:** All supported configurations (sizes, states, themes)
3. **Accessibility notes:** Keyboard behavior, ARIA roles, screen reader behavior
4. **Do/Don't examples:** Correct and incorrect usage with explanation
5. **Data binding:** Which Ontology property types it supports
6. **Responsive behavior:** How it adapts across target screen sizes
7. **Classification awareness:** How it handles classification-marked data

### 2-3. Design Token Architecture

**BLUF:** Design tokens are the single source of truth for visual values. Change a token, change every component that uses it — consistently, everywhere.

**Token categories for MSS:**

| Category | Examples | Governance |
|----------|----------|------------|
| Color — classification | Banner colors per IC/DoD standard | Locked — cannot be overridden by application designers |
| Color — status | Ready/Degraded/Not Ready/Unknown | Locked — MSS-wide standard |
| Color — neutral | Backgrounds, borders, text | Configurable within palette constraints |
| Color — accent | Interactive elements, highlights | Configurable within contrast ratio requirements |
| Typography | Font family, size scale, weight scale, line height | Locked — MSS-wide standard |
| Spacing | Padding, margin scale (4px base unit) | Locked — MSS-wide standard |
| Elevation | Shadows, z-index layers | Locked |

### 2-4. Design System Versioning

**BLUF:** A design system is a dependency for every MSS application. Unversioned changes to tokens or components break downstream applications the same way unversioned API changes break consumers. Version the design system like a product release.

**Versioning scheme:**

Follow semantic versioning (MAJOR.MINOR.PATCH) applied to the design system as a whole:

| Change Type | Version Bump | Example |
|-------------|-------------|---------|
| Breaking — component API change, removed variant, token rename | MAJOR | Button removes `compact` variant; applications using it must update |
| Additive — new component, new variant, new token | MINOR | New `StatusChip` component added; no existing application affected |
| Fix — bug fix, accessibility fix, visual correction | PATCH | Tooltip z-index corrected; no API change |

**Breaking vs. non-breaking changes:**

| Breaking (requires consumer action) | Non-Breaking (safe to adopt immediately) |
|--------------------------------------|------------------------------------------|
| Remove or rename a component | Add a new component |
| Remove or rename a component prop/variant | Add a new prop/variant with a default value |
| Change a token name or remove a token | Add a new token |
| Change default behavior of an existing pattern | Add a new pattern |
| Alter component DOM structure that affects automated tests | Fix an accessibility defect |

**Deprecation strategy:**

1. **Announce:** Mark component/token as deprecated in the design system documentation. Add a `@deprecated` tag with the replacement path and target removal version.
2. **Warn:** Tooling flags deprecated component usage during design reviews and CI builds. Set a deprecation window — minimum 2 release cycles or 90 days, whichever is longer.
3. **Migrate:** Provide a migration guide for each deprecation: what to replace, how to replace it, edge cases. For token renames, provide a find-and-replace mapping file.
4. **Remove:** Remove the deprecated element in the announced MAJOR version. Removal without completing the deprecation window requires Lead Designer approval and documented justification.

**Migration paths:**

- **Token changes:** Publish a token migration map (old name → new name) as a consumable file. Application teams apply it via automated find-and-replace or design tooling plugin.
- **Component changes:** Provide a side-by-side comparison (old vs. new component), document prop mapping, and supply code snippets showing the before/after. Where feasible, ship a compatibility wrapper that translates old props to new ones during the transition window.
- **Pattern changes:** Update the pattern documentation with the new pattern, mark the old pattern as deprecated, and schedule application-by-application migration during normal maintenance cycles — not as emergency work.

**Governance tie-in:** All MAJOR version releases require design review per Section 5-1. The review must confirm that the migration guide is complete, the deprecation window was honored, and at least one representative application has been migrated successfully before fleet-wide rollout.

---

## CHAPTER 3 — DDIL-AWARE DESIGN

### 3-1. Designing for Degraded Connectivity

**BLUF:** In the USAREUR-AF AOR, "always connected" is a fiction. Design every application to function — not just survive — when the network is slow, intermittent, or absent.

**DDIL design tiers:**

| Tier | Network Condition | Design Response |
|------|-------------------|-----------------|
| Full connectivity | Normal bandwidth, low latency | Full application functionality; real-time data |
| Degraded | Reduced bandwidth, higher latency | Reduce data payload; defer non-critical updates; show loading indicators with time estimates |
| Intermittent | Connection drops and reconnects | Queue actions locally; sync on reconnect; show connection status; indicate data freshness |
| Disconnected | No connectivity | Read-only cached data; indicate staleness prominently; queue writes for later sync |

### 3-2. Data Freshness Indicators

**BLUF:** Stale data without a staleness indicator is worse than no data — it creates false confidence.

Every data element displayed under DDIL conditions must indicate:
- **Last updated timestamp:** When was this data last confirmed current?
- **Staleness threshold:** Visual indicator when data exceeds its freshness window (e.g., readiness data >4 hours old gets amber border)
- **Source status:** Is the upstream data source currently reachable? Show connection indicator.

### 3-3. Offline-First Interaction Patterns

**BLUF:** If the user performs an action offline, the system must acknowledge the action, queue it, and sync it — or clearly explain why it cannot.

| Pattern | Behavior | User Feedback |
|---------|----------|---------------|
| Optimistic action | Accept action immediately; sync to server when connected | "Action saved locally. Will sync when connected." |
| Queued action | Accept action; hold in queue until connectivity confirmed | "Action queued. [3 actions pending sync]" |
| Blocked action | Action requires server confirmation; cannot be performed offline | "This action requires network connectivity. Currently offline." |

---

## CHAPTER 4 — CROSS-DOMAIN AND COALITION UI

### 4-1. Multi-Classification Display

**BLUF:** When users work across classification levels, the UI must make the current classification level unmistakable at all times. Ambiguity is a security violation.

**Cross-domain design requirements:**
- Classification banners visible at ALL times — never hidden by scroll, modal, or overlay
- Color-coded banners per IC/DoD standard with redundant text labels
- Data from different classification levels NEVER displayed on the same screen without explicit domain separation and ISSM-approved design
- Session transition between classification levels requires deliberate user action (not automatic)
- Print output includes classification markings on every page

### 4-2. Coalition and Multinational UI

**BLUF:** USAREUR-AF operates with NATO and partner nation forces. Interfaces shared with coalition partners must account for language, cultural conventions, and releasability markings.

**Coalition UI considerations:**

| Consideration | Design Response |
|--------------|-----------------|
| Language | English as primary; critical labels and status indicators designed for non-native English readers (simple vocabulary, no idioms, no abbreviations without expansion) |
| Date/time format | DTG standard for military use; ISO 8601 as fallback; never MM/DD/YYYY (ambiguous internationally) |
| Units of measure | Metric primary for coalition contexts; dual display where required |
| Releasability markings | REL TO markings displayed alongside classification; filter controls enforce releasability |
| Cultural conventions | Left-to-right layout assumption documented; color associations verified across partner nation conventions |

---

## CHAPTER 5 — DESIGN OPERATIONS (DESIGNOPS)

### 5-1. Design Review Governance

**BLUF:** Without governance, a design system erodes. New applications introduce inconsistencies, accessibility regressions, and pattern drift. DesignOps prevents this.

**Design review process (enterprise scale):**

| Review Type | Trigger | Reviewers | Output |
|-------------|---------|-----------|--------|
| New application design | Before development begins | Lead Designer + PM + SWE | Approved design spec or revision requests |
| Component addition | New component proposed for design system | Design system team (2+ designers) | Accept to library, reject, or merge with existing |
| Pattern deviation | Application needs to deviate from standard pattern | Lead Designer + requesting Designer | Approved exception (documented) or redesign using standard pattern |
| Accessibility audit | Quarterly, or before major release | Designer + automated tools | Compliance report with remediation priorities |
| Portfolio consistency check | Semi-annual | Lead Designer reviews 5 representative applications | Consistency scorecard; remediation backlog |

### 5-2. Design Quality Metrics

**BLUF:** What gets measured gets improved. Define metrics that drive design quality, not just design output.

**Recommended metrics:**

| Metric | What It Measures | Target |
|--------|-----------------|--------|
| Accessibility compliance rate | % of applications meeting WCAG 2.1 AA | 100% |
| Design system adoption | % of components using design system tokens/components | >90% |
| Usability test cadence | % of applications tested with representative users in past 6 months | 100% |
| Design-to-deploy fidelity | % of implemented features matching design specification | >95% |
| Time to first design | Days from requirement to first design review | <5 business days |
| Pattern reuse rate | % of new designs using existing patterns vs. creating new ones | >70% |

### 5-3. Research Repository

**BLUF:** User research is expensive to conduct. A research repository prevents teams from re-asking questions that have already been answered.

**Research repository structure:**
- **Study records:** Who was studied, when, where, methodology, key findings
- **Insight library:** Validated insights tagged by user role, WFF track, application domain
- **Persona library:** Maintained set of user personas updated with each research cycle
- **Recommendation tracker:** Design recommendations with implementation status

---

## CHAPTER 6 — ACCESSIBILITY AT ENTERPRISE SCALE

### 6-1. Automated Accessibility Testing

**BLUF:** Manual accessibility testing does not scale across a portfolio. Automate what can be automated; reserve manual testing for what cannot.

**Automation vs. manual testing:**

| Can Automate | Must Test Manually |
|-------------|-------------------|
| Color contrast ratios | Logical reading order for screen readers |
| Missing alt text | Meaningfulness of alt text content |
| Missing form labels | Clarity of error messages |
| Keyboard focus indicators present | Keyboard navigation flow is logical |
| ARIA roles present | ARIA roles are correct for the interaction |
| Touch target size | Touch target placement makes sense in context |

### 6-2. Accessibility Remediation Prioritization

**BLUF:** Not all accessibility issues are equal. Prioritize by operational impact.

| Priority | Criteria | Response |
|----------|----------|----------|
| P0 — Blocker | User cannot complete the primary task at all | Fix before next deployment |
| P1 — Critical | User can complete the task but with significant difficulty | Fix within current sprint |
| P2 — Major | User experience is degraded but task is completable | Schedule in next sprint |
| P3 — Minor | Cosmetic or minor friction; does not affect task completion | Backlog; address during next design system update |

---

## APPENDIX A — REFERENCES

| Reference | Relevance |
|-----------|-----------|
| TM-40N — UI/UX Designer | Prerequisite; individual application design |
| TM-50J — Advanced Program Manager | Portfolio-level product strategy coordination |
| TM-50L — Advanced Software Engineer | Design system implementation, shared component architecture |
| TM-50O — Advanced Platform Engineer | Performance budgets, deployment constraints |
| WCAG 2.1 (W3C) | Accessibility technical standard |
| IC/DoD Classification Marking Guide | Classification banner requirements |
| NATO STANAG 4774/4778 | Coalition information exchange metadata |

---

## APPENDIX B — PEER TM-50 CROSS-REFERENCES AND WFF INTEGRATION

**Peer TM-50 Publications.** Advanced UI/UX Designers should coordinate with practitioners in these companion advanced-track publications rather than operating in isolation.

| Publication | Track | Coordination Point |
|---|---|---|
| TM-50G | Advanced ORSA | Data visualization design for analytical products; dashboard UX for ORSA outputs |
| TM-50H | Advanced AI Engineer | UI/UX for AI-driven applications; model output presentation; automation bias mitigation through interface design |
| TM-50M | Advanced ML Engineer | Visualization of ML model performance; feature importance displays; experiment tracking dashboards |
| TM-50J | Advanced Program Manager | Portfolio-level product strategy; design system roadmap prioritization; resource allocation for UX research |
| TM-50K | Advanced Knowledge Manager | Knowledge portal UX; search interface design; taxonomy visualization; glossary integration |
| TM-50L | Advanced Software Engineer | Design system implementation architecture; shared component libraries; design token-to-code pipeline |
| TM-50O | Advanced Platform Engineer | Platform portal design; performance budgets; deployment constraints affecting design patterns; CDN hosting for design assets |

**WFF Operational Consumer Note.** Design systems, DDIL patterns, and accessibility standards built by TM-50N designers are consumed by the six Warfighting Function (WFF) tracks: Intelligence (TM-40A), Fires (TM-40B), Movement and Maneuver (TM-40C), Sustainment (TM-40D), Protection (TM-40E), and Mission Command (TM-40F). These practitioners are the operational users of every dashboard, COP layer, and decision support product in the MSS portfolio. A G2 intelligence dashboard has different layout priorities than a G4 sustainment status board; both must be accessible, DDIL-resilient, classification-explicit, and unambiguous about data freshness. Design system decisions at the TM-50N level propagate to every application these WFF operators depend on — design with their operational conditions, not garrison connectivity, as the baseline.
