# POLICY LETTER — MSS TRAINING PROGRAM
## Program Director's Policy Letter No. 1 | 12 March 2026

---

DEPARTMENT OF THE ARMY
USAREUR-AF G6 / C2DAO
UNIT 29331
APO AE 09014

AETT-C2DAO                                                    12 March 2026

MEMORANDUM FOR All USAREUR-AF Personnel, Unit Commanders, G6/S6 Sections, Data Team Personnel

SUBJECT: USAREUR-AF Maven Smart System (MSS) Training Program — Program Director's Policy Letter No. 1

---

**1. PURPOSE.** This letter establishes policy for the Maven Smart System (MSS) Training Program within USAREUR-AF. It applies to all personnel assigned to USAREUR-AF units who require MSS access or who perform data management, analytics, or software engineering duties on the MSS platform.

**2. BACKGROUND.** The USAREUR-AF C2DAO has established and maintains the MSS Training Program to ensure all personnel operating on MSS (built on the Palantir Foundry platform) meet a defined, evaluated standard before performing duties that involve creating, modifying, or consuming operational data products. This program replaces informal, ad hoc on-the-job training that produced inconsistent skill levels, data quality issues, and governance violations across the force.

**3. TRAINING REQUIREMENT.**

   **a.** TM-10 (Maven User) is mandatory for all USAREUR-AF personnel who require access to the production MSS environment. There are no waivers. Rank, seniority, or prior data experience does not substitute for a TM-10 evaluation with a Go result on file.

   **b.** Personnel who build, maintain, or support MSS data products must complete the appropriate higher-level training before performing those duties:

| TM Level | Requirement | Prerequisite |
|----------|-------------|-------------|
| TM-20 (Builder) | Required before building any project, pipeline, Ontology, or Workshop application | TM-10 |
| TM-30 (Advanced Builder) | Required before serving as a unit data lead or deploying multi-source production data products | TM-20 |
| TM-40 WFF tracks (A–F) | Required before performing warfighting function operator duties on MSS | TM-30 |
| TM-40 specialist tracks (G–L) | Required before performing specialist functions (ORSA, AI, ML, PM, KM, SWE) | TM-30 |

   **c.** Commanders will ensure newly assigned personnel complete TM-10 within **30 days** of assignment to a USAREUR-AF unit. Personnel assigned to data-adjacent roles will complete the appropriate higher training level within **90 days** of assignment.

**4. GOVERNANCE STANDARDS.** The following governance standards are in force for all MSS data products. Violations will result in data steward rejection of the affected product:

   **a.** All datasets, pipelines, Object Types, and Workshop applications will follow the C2DAO naming and governance standards published in `maven_training/standards/NAMING_AND_GOVERNANCE_STANDARDS.md`.

   **b.** All changes to production MSS data products will be made on a branch and promoted through the C2DAO data steward review process. No direct modifications to production data products are authorized.

   **c.** AIP Logic workflows that write to production Ontology Objects must include a human review gate. No AIP-generated data will be written directly to production Object properties without a tested human checkpoint.

   **d.** Classification markings will be applied to all datasets and data products at the time of creation. Exports will be authorized to destinations commensurate with the classification of the data.

**5. TRAINING QUALITY STANDARDS.**

   **a.** The Go/No-Go evaluation at the end of each course is the authoritative measure of completion. Attendance without a Go result does not constitute training completion.

   **b.** Personnel who receive a No-Go result will complete remediation training before re-evaluation. All remediation and re-evaluation events will be documented in the individual training record.

   **c.** Sustainment training is required:

| Personnel Category | Sustainment Requirement |
|-------------------|------------------------|
| All personnel | Annual TM-10 refresher |
| TM-20 and above | Quarterly build exercises |

**6. INSTRUCTOR STANDARDS.** Instructors will meet the qualifications and maintain the certifications specified in the Program of Instruction (POI-MSS-001). C2DAO will maintain an instructor roster and conduct annual instructor observations for all MSS instructors.

**7. ACCESS PROVISIONING.** Units will ensure personnel have the appropriate MSS access level provisioned before they attend training. Arriving at training without provisioned access is a unit administrative failure. Access lead times are published in the Course Administrative Data and the Program of Instruction.

**8. REPORTING.** Units will maintain the Unit Training Status Matrix (see MTP Appendix A) and report MSS training status to C2DAO quarterly. Required report elements:

- Total personnel requiring TM-10
- Number with Go result on file
- Any personnel in No-Go remediation status

**9. EFFECTIVE DATE.** This policy is effective immediately and supersedes any previous informal MSS training guidance.

**10. QUESTIONS.** Direct questions regarding this policy or the MSS Training Program to the C2DAO Training POC via the unit MSS Administrator.

FOR THE COMMANDER:

________________________________
[C2DAO TRAINING OIC]
[Rank, Name]
Chief, C2DAO Training and Standards Division

---

**DISTRIBUTION:**
- USAREUR-AF G6 (1)
- All G/S6 sections (as applicable)
- USAREUR-AF Data Team Personnel (all)
- Unit Training NCOs/Officers (via unit MSS Administrators)

---

**ENCLOSURES:**
1. MSS Training Program POI (POI-MSS-001)
2. Course Administrative Data (CAD-MSS-001)
3. Mission Training Plan (MTP-MSS-001)
4. Annual Training Schedule (current year)

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*Policy Letter No. 1 | 12 March 2026*
