# Training App Module Review — Consolidated Feedback

**Date:** 2026-03-27
**Modules reviewed:** TM-10 (Maven User), TM-20 (Builder), TM-30 (Advanced Builder)
**Method:** Three independent simulated students reviewed each module end-to-end

---

## Executive Summary

| Module | Chapters | Units | Empty/Stub Units | Tasks Empty | Knowledge Checks |
|--------|----------|-------|-------------------|-------------|-----------------|
| TM-10  | 7        | 50    | ~16 (tables/stubs) | 0          | 0               |
| TM-20  | 9        | 64    | ~11 concept units  | 0 (but 2 have embedded sub-tasks) | 0 |
| TM-30  | 11       | 63    | 29 (46%)           | 26/26 (all) | 0               |

**TM-10** is the most complete — task procedures are fully written. Primary issue: ~16 units end with a table reference or dangling colon and no content follows (stubs).

**TM-20** has solid task procedures in Chapters 3 and 5, but 11 concept/overview units are empty, branching (Ch 7) is taught after it's needed (Ch 3), and two tasks have other tasks crammed inside their steps arrays.

**TM-30** has good conceptual framing but zero procedural content — all 26 task units are empty. The module cannot be used for self-paced learning in its current state.

**No module has any knowledge checks or exercises.**

---

## Critical Issues (All Modules)

### 1. Stub/Empty Units

Units that end with a table reference, dangling colon, or have no content at all. These leave learners staring at incomplete thoughts.

**TM-10 stubs (content ends mid-thought or with empty table reference):**
- tm10-1-2a — Cognitive Hierarchy: "defines a four-level hierarchy:" → nothing
- tm10-1-2b — GMAD Framework: "Table 1-1a" → no table
- tm10-1-2c — Operations Process: ends with colon, no content
- tm10-1-4 — Governance Chain: "top to bottom:" → nothing
- tm10-1-7 — How to Get Help: "Table 1-2" → no table **(high priority — operational phone book)**
- tm10-1-9 — How Data Reaches You: "The chain, simplified:" → nothing
- tm10-1-10 — Learning Path: "Advancement path:" → nothing
- tm10-3-1 — Resource Types: "Table 3-1" → no table
- tm10-5-1 — Data Basics: "flows through processing layers:" → nothing
- tm10-5-5 (concept) — VAULTIS-A: eight dimensions never listed
- tm10-6-1 — Markings: "Table 6-1" → no table **(high priority — security)**
- tm10-6-2 — Authorization Boundaries: "Table 6-2" → no table
- tm10-6-5 — Incident Reporting: "Table 6-3" → no table **(high priority — security)**
- tm10-7-1 — Troubleshooting: "Table 7-1" → no table
- tm10-7-6 — Support Contacts: "Table 7-2" → no table **(high priority)**

**TM-20 empty concept/overview units:**
- tm20-1-6 — Governance and Escalation Chain: one sentence, no chain
- tm20-3-2 — Pipeline Builder Interface Overview: empty
- tm20-4-2 — Ontology Manager Interface Overview: empty
- tm20-5-2 — Widget Library: empty
- tm20-5-3 — Workshop Interface Overview: empty
- tm20-6-1, 6-2, 6-3 — Contour/Quiver concept units: all empty
- tm20-7-2 — Foundry Branching Concepts: empty
- tm20-8-3 — C2DAO Approval Triggers: empty
- tm20-9-2, 9-3, 9-4 — Error tables: all empty

**TM-30 empty units (29 of 63):**
- tm30-1-2 — What SL 3 Advances Beyond SL 2: **completely empty — highest priority in module**
- All 26 task units: empty
- tm30-2-5, 2-6 — Kairos/Target Workbench concept units: empty
- Plus 8 truncated concept units that end mid-sentence

### 2. Zero Knowledge Checks Across All Three Modules

177 total units, zero comprehension checks, zero exercises, zero scenario-based questions. For self-paced interactive training — especially where completion grants elevated platform privileges (SL 2, SL 3) — this is a significant gap.

**Recommended minimum:** One knowledge check per chapter in TM-10 and TM-20, one per chapter in TM-30 once tasks are populated.

### 3. Chapter Sequencing Issue in TM-20

Chapter 7 (Branching) must come before Chapter 3 (Pipelines). Every build task in Chapters 3–6 has a precondition of "working on a development branch," but branching isn't taught until Chapter 7. A student following chapters sequentially will be blocked at TM-20 Chapter 3, Step 4.

### 4. BLUF Field Consistently Empty

The `bluf` field is empty across most units in all three modules, even where BLUF content exists in the `content` field. If `bluf` drives a distinct rendered element in the training app, these need to be populated. If it's deprecated, the field should be removed from the schema.

### 5. Callouts Not in Callout Arrays

WARNING, CAUTION, and NOTE statements are frequently embedded in step body text rather than placed in the `callouts` array. This means they won't receive visual treatment (colored boxes, icons) in the rendered output. Affected units include most tasks in TM-10 Chapters 2–6 and several TM-20 tasks.

---

## Module-Specific Feedback

### TM-10: Maven User (SL 1)

**What works well:**
- Task format (Conditions, Standards, Equipment, Steps) is applied consistently and correctly
- Escalation language is strong throughout — clear on who owns what problem
- Named examples are grounded in USAREUR-AF (SGT Okonkwo/1-9 FA, WO2 Patterson/21st TSC, CPL Davis/3ID)
- Chapter 6 aggregation risk treatment and Chapter 7 escalation decision guide are genuinely good
- "The AI does not have rank. You do." (tm10-4-8) — most memorable line in all three modules

**Issues to address:**

| ID | Issue | Priority |
|----|-------|----------|
| T10-1 | ~16 stub units (see list above) — tables/lists never rendered | High |
| T10-2 | Task 4-1 has forward dependency on Task 4-2 — reorder | Medium |
| T10-3 | Duplicate ref "5-5" on both a task and concept unit | Medium |
| T10-4 | Chapter 1 doctrine block (1-2a through 1-2d) front-loads 4 conceptual sub-units before any practical content — risk of losing entry-level learners | Medium |
| T10-5 | `objective` field duplicates `intro` verbatim in chapter headers | Low |
| T10-6 | Task 3-1 has three separate numbered sequences (Method 1/2/Bookmarking) merged into one flat step list — will render as "1,2,3,4,1,2,3,4" | Medium |
| T10-7 | Numbering gap: no 4-7 between Task 4-6 and concept 4-8 | Low |
| T10-8 | AIP acronym used before definition in tm10-4-8 | Low |
| T10-9 | PII guidance in tm10-task-4-8b too permissive for SL 1 — tighten to "do not enter PII into chat; consult data steward if task requires it" | Medium |
| T10-10 | Tasks 5-4 and 5-5 have redundant timestamp-checking steps — consolidate | Low |

---

### TM-20: Builder (SL 2)

**What works well:**
- Three-phase workflow model (Pipeline → Ontology → Workshop) is the right organizing principle
- "The most common builder failure is building the wrong thing correctly" (tm20-1-2) — strong opener
- SSG Kim vignette in Chapter 3 is the best engagement element — replicate in Chapters 4–6
- Chapter 3 task procedures are well-developed and close to publication-ready
- Chapter 8 accountability and data quality checklist content is solid

**Issues to address:**

| ID | Issue | Priority |
|----|-------|----------|
| T20-1 | **Chapter 7 (Branching) must precede Chapter 3** — every build task assumes an active dev branch | Critical |
| T20-2 | 11 empty concept/overview units (interface overviews, error tables, etc.) | High |
| T20-3 | tm20-task-2-5 has Tasks 2-1, 2-2, 2-3 embedded inside its steps array — extract into separate units | High |
| T20-4 | tm20-task-3-3 — all procedural steps are in the `duration` field, not `steps` array | High |
| T20-5 | tm20-task-7-3 has Task 7-4 (conflict resolution) embedded inside steps — extract | Medium |
| T20-6 | tm20-2-1, 2-2, 2-3 concept units are placeholder-level (one sentence each, no actual content) | Medium |
| T20-7 | Undefined terms at first use: RID, curated dataset, cardinality, filter variable, junction dataset | Medium |
| T20-8 | tm20-5-1 content ends mid-sentence: "The build order:" → nothing | Medium |
| T20-9 | tm20-8-2 references "Chapter 2-3 for naming conventions" but 2-3 is nearly empty — broken cross-ref | Medium |
| T20-10 | Task 4-1 cites Palantir community forum as authority for design rules — should attribute to C2DAO | Medium |
| T20-11 | No knowledge checks anywhere in 9 chapters | Medium |
| T20-12 | Chapter 6 has no guidance on classification implications of sharing Contour/Quiver links | Medium |
| T20-13 | tm20-9-5 references SQL COUNT(*) — no-code builders may not know SQL; reframe in Pipeline Builder terms | Low |

---

### TM-30: Advanced Builder (SL 3)

**What works well:**
- Chapter structure is logical and SL 3 scope boundary is consistently maintained
- tm30-6-0 (AIP landscape overview) is the best concept unit across all three modules
- tm30-1-5 design principles are memorable: "Start with the command requirement, not the tool capability"
- tm30-3-2 naming conventions and documentation standards are immediately usable
- Chapter 11 governance checklist is a strong, printable artifact
- Operational consequences framing is effective throughout

**Issues to address:**

| ID | Issue | Priority |
|----|-------|----------|
| T30-1 | **All 26 task units are empty** — module has zero procedural instruction | Critical |
| T30-2 | tm30-1-2 (What SL 3 Advances Beyond SL 2) is empty — foundational orientation missing | Critical |
| T30-3 | 8 concept units truncated mid-sentence (1-4, 1-6, 1-7, 8-1, 8-2, 9-1, 10-1, 11-3) | High |
| T30-4 | Chapters 7 and 9: Q1 2026 feature updates appear before base concept content — inverted priority | Medium |
| T30-5 | BLUF duplication in tm30-1-10e and tm30-1-5 — same text in `bluf` field AND `[BLUF]` callout | Medium |
| T30-6 | Units tm30-1-10a through 1-10e are numbered out of sequence (appear between 1-4a and 1-5) | Medium |
| T30-7 | No concept unit for Interfaces before task tm30-task-4-4 | Medium |
| T30-8 | Chapter 5 has no Quiver concept content despite "Contour and Quiver" in chapter title | Medium |
| T30-9 | Steepest SL 2→SL 3 jump in Chapters 4 and 5 — needs bridging content | Medium |
| T30-10 | tm30-9-1a Autopilot section appears truncated mid-word | Low |
| T30-11 | Minor naming convention inconsistency: version suffix `_v1` vs `_1` between 3-2 and 11-1 | Low |

---

## Recommended Fix Priority

### Immediate (before any learner touches this)
1. **TM-30:** Write all 26 task procedures (start with Chapters 2, 3, 4)
2. **TM-30:** Write tm30-1-2 (What SL 3 Advances Beyond SL 2)
3. **TM-20:** Move Chapter 7 before Chapter 3 (or add mandatory forward reference)
4. **TM-20:** Extract embedded tasks from tm20-task-2-5 and tm20-task-7-3
5. **TM-20:** Fix tm20-task-3-3 (steps in wrong JSON field)

### High (before wide release)
6. **TM-10:** Fill all stub units — especially tables for help contacts (1-7), markings (6-1), incident reporting (6-5), troubleshooting (7-1)
7. **TM-20:** Populate 11 empty concept/overview units
8. **TM-30:** Complete 8 truncated concept units
9. **All:** Promote embedded WARNING/CAUTION/NOTE text to callout objects

### Medium (quality improvements)
10. **All:** Add knowledge checks — minimum one per chapter
11. **TM-10:** Fix Task 4-1/4-2 sequencing, resolve duplicate ref "5-5"
12. **TM-20:** Define terms at first use (RID, curated dataset, etc.)
13. **TM-30:** Reorder Q1 2026 updates after base concept content in Chapters 7, 9
14. **All:** Populate or remove empty `bluf` fields; deduplicate `objective`/`intro`

---

## Bright Spots Worth Preserving

These elements should be used as models when filling gaps:

- **SGT Okonkwo AIP verification example** (tm10-task-4-8a) — teaches nuanced outcome (2 of 14 records wrong, not all)
- **SSG Kim vignette** (TM-20 Ch 3) — grounded scenario that connects procedure to purpose; replicate in TM-20 Chapters 4–6
- **"The AI does not have rank. You do."** (tm10-4-8) — memorable, sets correct frame
- **AIP landscape overview** (tm30-6-0) — model for how to orient a learner to a tool ecosystem
- **Task 5-4 escalation language template** (tm10-task-5-4) — gives exact words to use when reporting; replicate pattern
- **Chapter 11 governance checklist** (tm30-11-4) — printable, immediately usable artifact
