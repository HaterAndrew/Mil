<!-- MAVEN TRAINING CORPUS — DOCTRINE REFERENCE
     Source: odt_workspace/docs/architecture/cg-guidance.md
     Supports: TM-10, TM-20, DATA_LITERACY_senior_leaders
     Type: Senior Leader Doctrine / Orientation
-->

# CG Guidance — Commanding General Public Guidance Aggregator

This module collects public statements, interviews, speeches, and written guidance from general officers relevant to the Cross-Domain Architecture. The purpose is to trace architecture decisions back to senior leader intent and ensure alignment between what leadership has publicly directed and what the architecture actually delivers.

**This is not doctrine.** Doctrine lives in ADP/FM publications. This is the spoken and written guidance that tells you how leadership thinks about the problems doctrine addresses — the why behind the what.

---

## How to Use This Module

1. **Before starting a new architecture initiative**, check the extracted directives to see if CG guidance constrains or steers the approach
2. **When writing ADRs**, reference specific guidance entries as rationale where applicable
3. **When briefing leadership**, use their own language — the quotes and themes here are how they frame the problems
4. **When evaluating vendor solutions**, apply the industry standards captured here as pass/fail criteria

---

## Source Index

| ID | Speaker | Source | Date | Format | Key Topics |
|----|---------|--------|------|--------|------------|
| CG-001 | GEN Christopher Donahue | AUSA Coffee Series | 2025 | Video/Transcript | Eastern Flank Deterrence Line, ground deterrence, new forms of mass, industry requirements, Russia adaptation, NextG C2, drone warfare as data problem |
| CG-002 | GEN Christopher Donahue | From the Green Notebook Podcast | 2026 | Video/Transcript | Leading change (why/vision/plan/process), lethality study, understand-adapt-integrate, offensive operations challenge, AI observability, convergence of headquarters |

---

## Adding New Sources

When adding a new source:

1. Obtain the transcript or text
2. Save the raw file to `sources/` with naming convention: `{speaker}_{source}_{year}_raw.txt`
3. Add a row to the Source Index above
4. Extract relevant directives and add them to `directives.md` under the appropriate theme
5. If the guidance contradicts an existing directive, flag it — don't silently overwrite

Acceptable source types:
- Public speeches and panel appearances (AUSA, MILCOM, War on the Rocks, etc.)
- Podcast interviews (From the Green Notebook, Irregular Warfare, etc.)
- Published articles (Military Review, Parameters, Joint Force Quarterly)
- Official public guidance memoranda
- Congressional testimony (public record)

**Do not include classified, FOUO, or CUI material.**
