# CDA Interactive Training Applications

## Purpose

This directory contains interactive HTML training tools developed by the USAREUR-AF Operational Data Team (ODT) under the Chief Data Architecture (CDA) program. These apps are standalone, browser-based tools that reinforce concepts taught in the Maven Smart System (MSS) training curriculum. They require no server — open directly in a browser or embed in Foundry Workshop.

## Applications

### 1. EA vs DA Reference (`ea-vs-da-reference/`)

**File:** `index.html`

**Description:** Interactive reference establishing the relationship between Enterprise Architecture (EA) and Data Architecture (DA). Covers definitions, scope, typical outputs, side-by-side comparison table, and the EA/DA hierarchy model. Enforces the principle that DA is a first-class child of EA — not a downstream ETL concern.

**Supports:** TM-30 (Advanced Builder), TM-40K (Knowledge Manager), TM-40L (Software Engineer)

---

### 2. Enterprise Data Compass (`enterprise-data-compass/`)

**File:** `index.html`

**Description:** The authoritative interactive reference for USAREUR-AF data architecture standards. Covers the five governing principles, the 5-Layer Data Stack (with L3 Semantic identified as the critical layer), ontology design standards (nine authorized object type varieties), governance model (ARB, peer review, DDOF lifecycle), the VAULTIS-A quality framework, cross-domain architecture rules, and NATO interoperability requirements (NAFv4, DODAF DIV-1/2/3, STANAGs). Signed by CTO and Chief Data Architect.

**Supports:** TM-40J (Program Manager), TM-40K (Knowledge Manager)

---

### 3. Lessons Learned (`lessons-learned/`)

**File:** `index.html`

**Description:** After Action Review (AAR) format lessons learned tool. Documents ODT Lessons Learned #001 — AVT25 Assessment Tools: how five tools in the same enclave multiplied work exponentially by failing to share doctrinal primitives. Provides a template for capturing, categorizing, and disseminating lessons learned across the program.

**Supports:** All TM tracks (AAR/lessons learned methodology applies across all roles)

---

### 4. Plan for Success (`plan-for-success/`)

**Files:** `index.html`, `data/meta.json`, `data/plan.json`, `data/radar.json`

**Description:** A two-view interactive tool combining a Technology Radar and a phased Program Plan. The radar view maps approved/trial/assessed/hold standards and tools across the 5-Layer Data Stack and four quadrants (Standards & Governance, Platform & Tools, Ontology & Modeling, Interoperability & Security). The plan view presents a five-phase program roadmap (Establish Authority → Build Foundation → Scale Through Training → Govern and Measure → Expand and Sustain) with deliverables, approval chains, and exit criteria. Data is loaded from the `data/` subdirectory JSON files — update `plan.json` and `radar.json` to reflect current program state.

**Supports:** TM-40J (Program Manager), TM-30 (Advanced Builder)

---

## Shared Assets (`shared/`)

| File | Description |
|------|-------------|
| `nato-theme.css` | NATO dark theme design tokens. Used by: ea-vs-da-reference, enterprise-data-compass, lessons-learned, plan-for-success. Import before app-specific styles. |
| `hermes-theme.css` | HERMES program identity theme. Purple/cyan glassmorphism palette. Used by HERMES hub and landing pages. |

## TM Track Cross-Reference

| Application | TM-10 | TM-20 | TM-30 | TM-40A-F (WFF) | TM-40G | TM-40H | TM-40I | TM-40J | TM-40K | TM-40L |
|-------------|-------|-------|-------|----------------|--------|--------|--------|--------|--------|--------|
| EA vs DA Reference | | | X | | | | | | X | X |
| Enterprise Data Compass | | | | | | | | X | X | |
| Lessons Learned | X | X | X | X | X | X | X | X | X | X |
| Plan for Success | | | X | | | | | X | | |

## Usage Notes

1. These apps are self-contained. All CSS and JavaScript is inline or loaded from CDN (IBM Plex fonts from Google Fonts). No build step required.
2. The `plan-for-success` app loads data from relative paths (`./data/meta.json`, etc.). Keep the `data/` directory co-located with `index.html`.
3. All apps display UNCLASSIFIED // FOUO classification banners. Do not modify classification markings without authorization.
4. Portal navigation links in some apps reference `../../index.html` (the CDA Portal index). These links will be broken in this `source_material` context — that is expected. The apps function fully without portal navigation.

## Provenance

Source: `/odt_workspace/src/architecture/cda/apps/`
Copied: 2026-03-13
Authority: Operational Data Team, USAREUR-AF
