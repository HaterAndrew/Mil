# CURRICULUM MAINTENANCE SOP
## Maven Smart System (MSS) Training Curriculum

**Version 1.0 | March 2026**
**Owner:** USAREUR-AF C2 Data and Analytics Office (C2DAO)
**Review cycle:** Quarterly, or upon trigger event (see Section 3)

---

## 1. PURPOSE

This SOP establishes the process for keeping the MSS training curriculum current. Without an active maintenance process, training materials go stale as the platform evolves, creating a gap between what students learn and what they encounter in production.

---

## Authoritative References

| Publication | Title | Relevance |
|---|---|---|
| AR 350-1 | Army Training and Leader Development | Master regulation for Army training policy; governs curriculum review and update requirements |
| TR 350-70 | Army Learning Policy and Systems | TRADOC master regulation governing course maintenance, version control, and learning product lifecycle |
| TP 350-70-14 | Training Development in Institutional Domain | TRADOC pamphlet governing curriculum development, revision procedures, and quality assurance |

> **NOTE:** TR 350-70 and TP 350-70-14 are published by TRADOC at adminpubs.tradoc.army.mil, not DA APD.

---

## 2. CURRICULUM OWNER AND ROLES

| Role | Responsibility |
|------|---------------|
| **Curriculum Owner** (C2DAO) | Final approval authority for all changes; owns the version log |
| **Platform Monitor** (C2DAO designated) | Watches Palantir release notes; triages platform changes against TM content; initiates review for any feature change affecting a trained task. One person designated; backup required. |
| **Subject Matter Expert (SME)** per track | Reviews TM content accuracy for their track; proposes changes |
| **Instructors** | Submit AAR discrepancy reports; flag outdated content during delivery |
| **Unit Data Stewards** | Submit change requests when operational procedures diverge from curriculum |

---

## 2A. PLATFORM MONITORING PROCEDURE

The Platform Monitor is responsible for proactively watching Palantir MSS platform changes and triaging their impact on training content. This is a standing, recurring responsibility — not a reactive one.

**Monitoring cadence:**

| Source | Frequency | Action |
|---|---|---|
| Palantir release notes (MSS instance) | Weekly check | Log any UI, workflow, or feature change; cross-reference against TM task list |
| Palantir developer blog / changelog | Monthly | Flag any foundational changes (Pipeline Builder, Workshop, Ontology Manager, AIP Logic) |
| C2DAO technical feed | As published | Immediate review for any MSS-specific configuration or policy change |

**Triage process:**
1. Platform Monitor logs the change with: date noticed, feature affected, and preliminary TM impact assessment
2. Cross-reference against the TM task list to identify every task that touches the changed feature
3. Classify impact: **None** (UI cosmetic only), **Minor** (procedure wording update needed), **Major** (task steps change or new capability affects scope)
4. For Minor/Major: open a change request, assign to the relevant SME, and set review timeline per Section 3 trigger table
5. For None: log in the monitoring record and close

**Handoff on personnel change:** When the Platform Monitor role changes personnel, the incoming monitor must conduct a walk-through of the current monitoring log with the outgoing monitor before the handoff is complete. Gaps in monitoring coverage (e.g., during PCS) must be reported to the Curriculum Owner.

---

## 3. TRIGGER EVENTS — UPDATE REQUIRED

Any of the following triggers a mandatory curriculum review:

| Trigger | Scope | Timeline |
|---------|-------|----------|
| Palantir MSS platform release (major version) | All TMs potentially affected | Review within 30 days of release |
| Palantir MSS platform release (minor/patch) | Spot-check affected TMs | Review within 60 days |
| Army CIO data policy update | Doctrine publications + all TMs | Review within 45 days |
| USAREUR-AF G6/C2DAO policy change | All TMs | Review within 30 days |
| AAR discrepancy report — Severity H | Specific document cited | Review within 7 days |
| AAR discrepancy report — Severity M | Specific document cited | Batch into next quarterly review |
| AAR discrepancy report — Severity L | Specific document cited | Batch into next quarterly review |
| Instructor identifies content error during delivery | Specific document | Flag immediately; batch fix within 30 days |

---

## 4. CHANGE PROCESS

### Step 1 — Identify the Change
- Source: AAR report, SME review, trigger event, or user feedback
- Document in the Change Log (Section 7) before making edits

### Step 2 — Classify the Change

| Change Type | Description | Approval Required |
|-------------|-------------|------------------|
| **Correction** | Fixing factual error, broken link, outdated procedure | SME review + Curriculum Owner notification |
| **Update** | Revising content to reflect platform/policy change | SME review + Curriculum Owner approval |
| **Addition** | New task, section, or publication | SME review + Curriculum Owner approval |
| **Deletion** | Removing content no longer applicable | Curriculum Owner approval |
| **Restructure** | Changing document organization or prerequisite chain | Curriculum Owner approval + SME review for affected tracks |

### Step 3 — Make the Change
- Edit the source Markdown file
- Increment the version tag in the document header:
  - Correction → increment patch (1.0 → 1.0.1)
  - Update or Addition → increment minor (1.0 → 1.1)
  - Restructure → increment major (1.0 → 2.0)
- Update `## CHANGE LOG` section at the end of the document (if present) or add one

### Step 4 — Regenerate PDFs
- Run `scripts/build_pdfs.py` from repo root
- Verify changed documents rendered correctly
- Commit source + PDF together in the same commit

### Step 5 — Log the Change
- Update Section 7 (Change Log) of this SOP
- If the change affects a SYLLABUS or exercise package, update those documents too

### Step 6 — Notify
- Brief instructors on any change affecting SL 1 through SL 3 (broad audience impact)
- Email C2DAO distribution for any major version change

---

## 5. QUARTERLY REVIEW CHECKLIST

Conduct quarterly (Jan, Apr, Jul, Oct). Assign to Curriculum Owner or designated SME.

- [ ] Review Palantir release notes since last review — flag any MSS feature changes affecting TM content
- [ ] Review Army CIO / USAREUR-AF policy updates — flag doctrine document impacts
- [ ] Review all open M/L-severity AAR discrepancy reports — batch fix or close
- [ ] Spot-check 3 random TM sections for accuracy against current platform
- [ ] Verify all external links (portal URLs, policy citations) are still valid
- [ ] Confirm exercise ENVIRONMENT_SETUP.md files are current for each active exercise
- [ ] Update this SOP if the process itself has changed
- [ ] Log completion in Section 7

---

## 5A. SEMI-ANNUAL CURRICULUM DEEP REVIEW

The quarterly checklist (Section 5) is a maintenance check. The semi-annual deep review is a curriculum audit — a structured assessment of whether the training program still teaches what it claims to teach, at the standard it claims to require.

**Conducted:** April and October (following the April and October quarterly check).
**Owner:** Curriculum Owner, with SME representation from each active track.
**Duration:** 2–3 working days minimum. This is not a desk review.

### Semi-Annual Review Scope

| Review Area | Standard | Responsible |
|---|---|---|
| **Teach-test alignment** | For every evaluated task in every syllabus: is it explicitly taught in the daily schedule? If not, add instruction or remove the evaluation. | SME per track |
| **LO-to-evaluation mapping** | Every Learning Objective must map to at least one evaluated task. Orphaned LOs are either added to the evaluation or reclassified as knowledge-only. | SME per track |
| **Platform accuracy** | 10% random sample of TM task steps verified against the current MSS platform by a practitioner (not the author). Steps that no longer match the UI are flagged. | Platform Monitor + SME |
| **Prerequisite chain integrity** | Verify that SL 4/5 content does not re-teach SL 3 material, and SL 3 content does not re-teach SL 2 material. Content that duplicates a lower level is flagged for removal or restructuring. | Curriculum Owner |
| **AAR trend analysis** | All AAR discrepancy reports from the preceding 6 months reviewed in aggregate. Identify patterns (same task failing repeatedly, same concept misunderstood) and address with curriculum changes, not just individual remediation. | Curriculum Owner + Instructors |
| **Go/No-Go standard quality** | All practical exercise Go standards reviewed against Bloom's taxonomy level appropriate to the course level. Vague standards ("demonstrates understanding," "performs adequately") are rewritten with specific measurable criteria. | SME per track |
| **Duration sufficiency** | Block time vs. content volume check: is the allocated time sufficient for the taught content, including student practice time? Flag any block where instruction time leaves no room for practice. | Instructors |

### Semi-Annual Review Output

The semi-annual review produces:
1. A brief findings summary (1–2 pages) documenting what was checked and what changes were directed
2. A list of specific change requests with assigned SMEs and due dates
3. A change log entry in Section 7 of this SOP documenting the review was conducted

**No curriculum changes are required** if the review finds no issues — but the review must be documented regardless. An undocumented review did not happen for governance purposes.

---

## 6. VERSION NUMBERING CONVENTION

All curriculum documents use semantic versioning: `MAJOR.MINOR.PATCH`

| Increment | When |
|-----------|------|
| PATCH (x.x.**1**) | Typo fix, broken link, minor wording correction |
| MINOR (x.**1**.0) | Content updated/added due to platform or policy change |
| MAJOR (**2**.0.0) | Document restructured, prerequisite chain changed, or content substantially rewritten |

Format in document header: `**Version 1.2 | Month Year**`

---

## 7. CHANGE LOG

| Date | Document | Change Type | Summary | Version After | Author |
|------|----------|-------------|---------|---------------|--------|
| 2026-03-12 | All TMs | Addition | Version tags added to all SL 1 through SL 5M documents | 1.0 | C2DAO |
| 2026-03-12 | SL 5 series | Addition | Prerequisite warning blocks added to all SL 5 documents | 1.0 | C2DAO |
| 2026-03-12 | QUICK_START.md | Addition | New 30-minute operator onboarding guide created | 1.0 | C2DAO |
| 2026-03-12 | exercises/ | Addition | Exercise stubs created for SL 1 through SL 4L tracks (WFF SL 4A–F and specialist SL 4G–O) | 1.0 | C2DAO |
| 2026-03-12 | AAR_TEMPLATE.md | Addition | Instructor AAR/feedback template created | 1.0 | C2DAO |
| 2026-03-12 | This SOP | Creation | Initial publication | 1.0 | C2DAO |
