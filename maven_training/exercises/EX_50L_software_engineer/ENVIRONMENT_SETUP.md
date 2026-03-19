# ENVIRONMENT SETUP — EX_50L Advanced Software Engineer (TM-50L)

**Companion resources:** TM_50L_SOFTWARE_ENGINEER_ADVANCED.md | SYLLABUS_TM50L | EXAM_TM50L_POST

## Environment Type

MSS Code Workspace (TypeScript + Python), OSDK TypeScript SDK (advanced — branch manipulation, Function authoring), CI/CD pipeline (training environment build/configure access), Ontology editor (limited). This is the most technically complex EX_50 exercise environment. All three access types must be confirmed independently before exercise day.

## Required Access

| Account | Role |
|---------|------|
| Participant | Code Workspace (TypeScript), OSDK advanced (Function authoring, Object Type read), CI/CD pipeline (create/configure), Ontology read, training project read/write |
| Evaluator | Training project read (to receive Task 5 submission and review Task 4 checklist), CI/CD pipeline read (to verify Task 3 pipeline configuration) |

**Lead time:**
- Code Workspace (TypeScript): 5–7 duty days
- OSDK advanced Function authoring: 7 duty days (separate request from standard OSDK)
- CI/CD pipeline access: **7–10 duty days** (separate request — often the longest lead time item)

Do not assume CI/CD access is bundled with Code Workspace. Request it independently and confirm with a test pipeline creation before exercise day.

## Pre-Load Instructions

### 1. Application Source Code

Load `EX_50L_SWE_Training_Data/equipment_readiness_app/` into participant's Code Workspace:

```
equipment_readiness_app/
├── src/
│   ├── AppConfig.ts           (planted Issue 3 — over-permissioned scope)
│   ├── EquipmentStatusPanel.tsx   (planted Issue 1 — N+1 query loop)
│   ├── ReadinessCalculator.ts     (planted Issue 2 — unmemoized computed property)
│   ├── MaintenanceView.tsx    (no issues — correct reference implementation)
│   ├── types.ts               (shared types — no issues)
│   └── index.tsx              (app entry point — no issues)
├── tests/
│   └── ReadinessCalculator.test.ts
├── tsconfig.json
├── package.json
└── .eslintrc.js
```

**Verification:** Run `tsc --noEmit` before exercise day — must complete with no errors (issues are architectural, not syntactic). Run `npm test` — tests should pass in the pre-exercise state.

### 2. Planted Code Issues

**Issue 1 — N+1 query pattern** (`EquipmentStatusPanel.tsx` lines 45–78):

```typescript
// PLANTED ISSUE — loop-per-unit query pattern (replace with bulk Object Set query)
const statuses = [];
for (const unitId of unitIds) {
  const status = await client.objects.EquipmentStatus
    .where({ unitId: unitId })
    .fetchOne();
  statuses.push(status);
}
```

Expected fix (bulk query):
```typescript
const statuses = await client.objects.EquipmentStatus
  .where({ unitId: { $in: unitIds } })
  .fetchAll();
```

**Issue 2 — Unmemoized computed property** (`ReadinessCalculator.ts` lines 12–34):

```typescript
// PLANTED ISSUE — recomputed on every render; wrap in useMemo with [equipmentData] dependency
export const averageReadiness = (equipmentData: EquipmentStatus[]) => {
  return equipmentData.reduce((sum, e) => sum + e.readinessPct, 0) / equipmentData.length;
};
```

**Issue 3 — Over-permissioned OSDK scope** (`AppConfig.ts` line 8):

```typescript
// PLANTED ISSUE — requests all Object Types; should scope to EquipmentStatus and MaintenanceRequest only
const osdkConfig = {
  scopes: ['*'],   // replace with ['EquipmentStatus', 'MaintenanceRequest']
};
```

### 3. Test Fixtures

Load `EX_50L_SWE_Training_Data/test_fixtures/`:

| File | Description |
|------|-------------|
| `mockEquipmentStatus.ts` | Mock OSDK EquipmentStatus objects (10 units, various readiness states) |
| `mockMaintenanceRequest.ts` | Mock OSDK MaintenanceRequest objects (linked to equipment) |
| `osdkClientMock.ts` | Mock OSDK client for unit testing without live Ontology connection |

Verify `npm test` passes using these fixtures before exercise day.

### 4. CI/CD Environment

Confirm the training CI/CD environment supports:
- GitHub Actions, GitLab CI, or equivalent (specify which is available in the training environment)
- Node.js build runner
- `npm run build`, `npm run lint`, `npm test` commands
- Manual approval gate (environment protection rules or equivalent)

If using GitHub Actions, provide a starter `.github/workflows/` directory with a blank workflow file (scaffold only — participant must configure stages).

If using GitLab CI, provide a blank `.gitlab-ci.yml` (scaffold only).

### 5. Blank Security Review Checklist

Place `usareur_swe_security_review_checklist_blank.md` in participant's project folder:

Sections:
1. Input Validation (boundary list, validation status per boundary)
2. Authentication/Authorization (credential handling, OSDK token patterns)
3. OSDK Permission Scope (requested vs. required scopes)
4. Finding Table (ID, location, severity, status, recommended action)
5. Disposition (sign-off / conditional / defer) with rationale
6. Reviewer name, date, application name and version

## Environment URL

```
[Insert training MSS tenant URL here]
```

## Scoring Sheet Reference

Evaluators record task Go/No-Go on standard EX_50L Evaluation Form (available from training NCO). For Task 2, record the before/after query count documentation. For Task 3, screenshot or log the CI/CD pipeline configuration. For Task 4, attach or photograph the completed security review checklist. Overall Go/No-Go, participant name, evaluator name, and date required for training record submission.

## Notes

- CI/CD pipeline access is the most common provisioning failure for this exercise — request it 10 duty days out even if the syllabus says 7
- If CI/CD access cannot be provisioned before exercise day, Task 3 may be completed as a documented pipeline design (YAML configuration file + SOP), but note the deviation on the evaluation form and flag to C2DAO
- The planted issues are calibrated to require substantive architectural reasoning to identify — they are not trivial bugs; a participant who identifies Issue 3 (over-permissioned scope) as a performance issue rather than a security issue should be coached on the security implication even if the identification is partially correct
- TypeScript version must match `tsconfig.json` target in the provided source — do not upgrade the TypeScript version in the training environment without testing against the source first
