# CURRICULUM MAINTENANCE SOP
## Maven Smart System (MSS) Training Curriculum

**Version 1.0 | March 2026**
**Owner:** USAREUR-AF C2 Data and Analytics Office (C2DAO)
**Review cycle:** Quarterly, or upon trigger event (see Section 3)

---

## 1. PURPOSE

This SOP establishes the process for keeping the MSS training curriculum current. Without an active maintenance process, training materials go stale as the platform evolves, creating a gap between what students learn and what they encounter in production.

---

## 2. CURRICULUM OWNER AND ROLES

| Role | Responsibility |
|------|---------------|
| **Curriculum Owner** (C2DAO) | Final approval authority for all changes; owns the version log |
| **Subject Matter Expert (SME)** per track | Reviews TM content accuracy for their track; proposes changes |
| **Instructors** | Submit AAR discrepancy reports; flag outdated content during delivery |
| **Unit Data Stewards** | Submit change requests when operational procedures diverge from curriculum |

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
- Brief instructors on any change affecting TM-10 through TM-30 (broad audience impact)
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
| 2026-03-12 | All TMs | Addition | Version tags added to all TM-10 through TM-50F documents | 1.0 | C2DAO |
| 2026-03-12 | TM-50 series | Addition | Prerequisite warning blocks added to all TM-50 documents | 1.0 | C2DAO |
| 2026-03-12 | QUICK_START.md | Addition | New 30-minute operator onboarding guide created | 1.0 | C2DAO |
| 2026-03-12 | exercises/ | Addition | Exercise stubs created for TM-10 through TM-40F tracks | 1.0 | C2DAO |
| 2026-03-12 | AAR_TEMPLATE.md | Addition | Instructor AAR/feedback template created | 1.0 | C2DAO |
| 2026-03-12 | This SOP | Creation | Initial publication | 1.0 | C2DAO |
