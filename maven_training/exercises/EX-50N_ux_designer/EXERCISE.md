# EX-50N — Advanced UI/UX Designer
## Practical Exercise — TM-50N Proficiency

| Field | Value |
|-------|-------|
| **Version** | 1.0 — March 2026 |
| **Prerequisite** | TM-40N REQUIRED (Go evaluation on file); TM-50N — Advanced UI/UX Designer Technical Manual |
| **Duration** | 3–4 hours |
| **Environment** | MSS with Workshop access, design tool (Figma or equivalent) — see EX-40N ENVIRONMENT_SETUP.md (same environment) |

## COMPANION RESOURCES

| Resource | Reference |
|----------|-----------|
| Technical Manual | TM-50N — Advanced UI/UX Designer |
| Syllabus | SYLLABUS_TM50N |
| Pre-Exercise Exam | EXAM_TM50N_PRE |
| Post-Exercise Exam | EXAM_TM50N_POST |

## SCENARIO

The MSS application portfolio has grown to 10+ Workshop applications built by different teams over the past year. Consistency is degrading — each application uses slightly different status colors, navigation patterns, and data table layouts. The OPDATA team needs a design system foundation, a DDIL-aware redesign of a key application, and a governance proposal to prevent further drift.

## TASK LIST

### Task 1 — Design System Component (45 min)

- [ ] Select a common UI element used inconsistently across MSS applications (e.g., status indicator, data table, filter bar)
- [ ] Design a standardized component with full documentation: variants, accessibility notes, do/don't examples, data binding, responsive behavior
- [ ] Define associated design tokens (color, typography, spacing) with governance classification (locked vs. configurable)

| Standard | Criteria |
|----------|----------|
| **Go** | Component documented per TM-50N §2-2 standard; tokens have governance rules; accessibility notes complete |
| **No-Go** | Component lacks documentation, tokens, or accessibility specification |

### Task 2 — DDIL-Aware Redesign (45 min)

- [ ] Select an existing MSS application design (from TM-40N exercise or provided example)
- [ ] Redesign for DDIL resilience: add data freshness indicators, offline-first interaction patterns, graceful degradation
- [ ] Design for all four DDIL tiers (full connectivity, degraded, intermittent, disconnected)
- [ ] Annotate the design with tier-specific behavior for each data element and interaction

| Standard | Criteria |
|----------|----------|
| **Go** | All four DDIL tiers addressed; freshness indicators on data elements; offline interaction patterns specified; degradation is graceful (not blank screens) |
| **No-Go** | Fewer than 4 tiers addressed; no freshness indicators; disconnected state shows blank/error screen |

### Task 3 — Cross-Domain UI Specification (30 min)

- [ ] Select an MSS application that users access at multiple classification levels (e.g., a readiness dashboard available at both SECRET and TOP SECRET)
- [ ] Design the classification transition experience: banner placement, session boundary UI, and deliberate user action required to cross domains
- [ ] Specify multi-classification display rules: how data from different classification levels is visually separated, how classification markings persist during scroll/modal/overlay, and how print output retains markings on every page
- [ ] Annotate the design with ISSM review checkpoints — identify which design decisions require ISSM approval before implementation

| Standard | Criteria |
|----------|----------|
| **Go** | Classification banners visible at all times (never hidden by scroll, modal, or overlay); domain transition requires deliberate user action; data from different classification levels visually separated with ISSM-approved design; ISSM review checkpoints identified |
| **No-Go** | Classification banners can be obscured; domain transition is automatic or ambiguous; mixed-classification data displayed without explicit separation; no ISSM review checkpoints |

### Task 4 — Coalition-Ready Interface (30 min)

- [ ] Redesign a key screen from Task 2 or Task 3 for coalition partner use in a multinational USAREUR-AF context
- [ ] Replace idioms, unexpanded abbreviations, and culturally ambiguous elements with plain-language equivalents suitable for non-native English readers
- [ ] Apply international date/time conventions: DTG standard for military use, ISO 8601 as fallback — no MM/DD/YYYY format
- [ ] Add REL TO releasability markings alongside classification banners; design filter controls that enforce releasability restrictions
- [ ] Verify metric-primary unit display for coalition contexts and document any dual-display requirements

| Standard | Criteria |
|----------|----------|
| **Go** | No unexpanded abbreviations or idioms in user-facing labels; date/time uses DTG or ISO 8601 (no MM/DD/YYYY); REL TO markings displayed alongside classification; releasability filter controls enforce restrictions; units of measure are metric-primary |
| **No-Go** | Abbreviations without expansion; MM/DD/YYYY date format present; no releasability markings; filter controls do not enforce releasability; units default to imperial without metric |

### Task 5 — Governance Proposal (30 min)

- [ ] Propose a design review governance process: review types, triggers, reviewers, criteria
- [ ] Define 3+ design quality metrics with targets
- [ ] Propose a research repository structure for sharing insights across MSS design teams

| Standard | Criteria |
|----------|----------|
| **Go** | Governance process is actionable (not aspirational); metrics have measurable targets; research repository structure is defined |
| **No-Go** | Governance process is vague; no measurable metrics; no research repository |
