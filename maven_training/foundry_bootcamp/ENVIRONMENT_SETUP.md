# FOUNDRY BOOTCAMP — ENVIRONMENT SETUP
## Coordinator Checklist — Pre-Bootcamp Configuration
### USAREUR-AF Operational Data Team

---

## TIMELINE

| T-minus | Action | Responsible |
|---|---|---|
| T-21 days | Enrollment window closes; finalized participant list to MSS Administrator | Coordinator |
| T-14 days | All Project Briefs approved; project list finalized | Coordinator / C2DAO |
| T-10 days | Bootcamp workspace created in MSS Training Environment | MSS Administrator |
| T-10 days | Participant access provisioned (workspace editor role) | MSS Administrator |
| T-5 days | Participants confirm access (logged in, workspace loads) | Participants |
| T-5 days | Coordinator confirms all data sources accessible to participants | Coordinator |
| T-2 days | Day 1 in-brief materials prepared; SME briefed on participant project list | Coordinator |
| Day 1 0730 | Coordinator on-site; environment check station set up | Coordinator |

---

## SPRINT WORKSPACE SETUP

### 1. Workspace Creation

The MSS Administrator creates a dedicated bootcamp workspace in the MSS Training Environment:

- **Naming convention:** `FBC_[YYYYQQ]_SPRINT` (e.g., `FBC_202602_SPRINT`)
- **Access level:** Editor for all enrolled participants; Editor for evaluator and SMEs
- **Data access:** Each participant's project-specific datasets must be accessible within the training environment. Coordinate with the unit Data Steward for any datasets not already in the training environment.

> **NOTE:** If a participant's project requires production data, coordinate with C2DAO and the unit Data Steward separately. Production access during FBC is not automatic and requires explicit approval before T-10 days.

### 2. Participant Sub-Projects

Create a sub-project folder for each participant within the bootcamp workspace:

```
FBC_[YYYYQQ]_SPRINT/
  ├── [PARTICIPANT_LASTNAME_PROJECT_SHORTNAME]/
  ├── [PARTICIPANT_LASTNAME_PROJECT_SHORTNAME]/
  └── ...
```

Participants work within their own sub-project. This isolates work and simplifies evaluator review.

### 3. Governance Template

Pre-load each participant's sub-project with:
- A README template (from FBC_GUIDE.md Appendix B)
- The naming standards reference card (quick_reference/cheatsheet.md)
- A branch pre-configured for the participant's bootcamp work (branch name: `[PARTICIPANT_LASTNAME]/bootcamp`)

---

## ACCESS VERIFICATION

Before T-5 days, confirm each participant can:

- [ ] Log into the MSS Training Environment
- [ ] **If bootcamp work spans multiple enclaves (NIPR, SIPR, MPE, etc.): participant confirms login on EACH enclave.** Accounts do not carry across enclaves.
- [ ] Access their sub-project in the bootcamp workspace
- [ ] Access all data sources listed in their Project Brief
- [ ] Create a branch within their sub-project

If any participant cannot complete these steps by T-5 days, the coordinator contacts MSS Admin for resolution. Do not wait until Day 1.

---

## SME PRE-BRIEF (T-2 days)

Provide the SME with:

1. Full participant list with names, ranks, units, and project descriptions
2. Known access issues or pre-identified complexity flags
3. Bootcamp schedule and standup format
4. Copy of the Evaluation Record template (SPRINT_PACKAGE.md Appendix A)
5. Any governance edge cases (production data access, non-standard data sources)

The SME should read each Project Brief before Day 1. The Day 1 in-brief environment check is faster when the SME knows which participants are most likely to have issues.

---

## DAY 1 ENVIRONMENT CHECK STATION

Set up a check station before 0800 on Day 1:

| Item | Details |
|---|---|
| Workstation per participant | Confirmed working; environment loaded; participant logged in |
| Network access | MSS Training Environment reachable from all workstations |
| SME contact | SME reachable by comm during build days (DSN, Teams, or presence in room) |
| Coordinator contact list | All participants have coordinator's contact info for Day 1–5 blockers |

Any participant who cannot confirm access by the end of the in-brief (0900) has a confirmed issue — the coordinator and SME resolve it as a priority. If unresolved by 1000, the coordinator contacts MSS Admin.

---

*USAREUR-AF Operational Data Team*
*Foundry Bootcamp (FBC) Environment Setup | Version 1.0 | March 2026*
