# TM-40L — MAVEN SMART SYSTEM (MSS)
## SOFTWARE ENGINEER TECHNICAL MANUAL

**HEADQUARTERS, UNITED STATES ARMY EUROPE AND AFRICA**
Wiesbaden, Germany

2026

**Version 1.0 | March 2026**

**PREREQUISITE PUBLICATIONS:** TM-10, Maven User; TM-20, Builder; TM-30, Advanced Builder (required); Python proficiency (intermediate or higher); TypeScript proficiency (intermediate or higher)

**DISTRIBUTION RESTRICTION:** Distribution authorized to U.S. Government agencies and their contractors only. Reason: operational systems documentation. Other requests must be referred to USAREUR-AF G6.

---

## SAFETY SUMMARY

Software engineers on MSS operate at the deepest technical layer of the USAREUR-AF data environment. Code written at TM-40L level executes directly against the Foundry Ontology, reads and writes operational datasets, and may integrate external Army systems with production MSS pipelines. A defect in your code is not an inconvenience — it is an operational data integrity failure.

Before performing any task at TM-40L level:

- Authenticate only with authorized service accounts or personal access tokens provisioned through the C2DAO-approved credential store — never hardcode credentials in any file committed to version control
- Treat all OSDK queries and dataset reads against production as operational data access — apply the same handling discipline you would apply to a classified terminal
- Never write directly to production datasets, Ontology branches, or shared resources without authorization from the responsible data steward and C2DAO coordination
- All code that will be deployed to production must pass automated testing gates before branch promotion — no exceptions, no manual bypasses
- External application integrations that consume MSS operational data must be reviewed for CBAC compliance before go-live — access controls on the source must be preserved end-to-end in the consuming application
- TypeScript Functions on Objects (FOO) that compute derived properties across large object populations can degrade Ontology query performance for all users — profile before deploying to production

> **WARNING: Code errors at TM-40L level can corrupt shared Ontology state, break downstream pipelines, and produce incorrect data products consumed by commanders making operational decisions. Apply engineering discipline. Test thoroughly. Coordinate governance before deploying to production.**

> **CAUTION: OSDK service account tokens and Foundry Platform SDK credentials are operational secrets. Loss or exposure of these credentials constitutes a security incident. Report immediately to unit S6/G6 and C2DAO.**

---

## TABLE OF CONTENTS

- Chapter 1 — Introduction: The Software Engineer Role in MSS
- Chapter 2 — OSDK Fundamentals
- Chapter 3 — OSDK Advanced Patterns
- Chapter 4 — Foundry Platform SDK
- Chapter 5 — TypeScript Functions on Objects (FOO)
- Chapter 6 — Actions with Complex Validation
- Chapter 7 — Slate Applications (LEGACY)
- Chapter 8 — CI/CD and Code Repository Discipline
- Chapter 9 — Security and Compliance
- Appendix A — OSDK Quick Reference
- Appendix B — SWE Security Checklist
- Appendix C — Integration Patterns Reference
- Glossary

---

## CHAPTER 1 — INTRODUCTION: THE SOFTWARE ENGINEER ROLE IN MSS

### 1-1. Purpose and Scope

**BLUF:** TM-40L qualifies software engineers to build external applications, write integration code, develop TypeScript FOO logic, and deploy production-grade solutions on the MSS platform. This is a developer manual — it contains code, not just concepts.

This manual provides task-based instruction for software engineers operating on the Maven Smart System (MSS). MSS is the USAREUR-AF enterprise AI/data platform built on Palantir Foundry. TM-40L personnel design and implement the technical components that advanced builders (TM-30) specify but cannot build without code.

**TM-40L covers:**
- OSDK (Ontology SDK): authenticating, querying objects, executing actions, subscribing to changes from external applications
- Foundry Platform SDK (Python): reading and writing datasets, managing transactions, accessing file resources
- TypeScript Functions on Objects (FOO): computed properties, bulk query patterns, performance optimization
- Actions with complex validation: TypeScript validators, multi-step action flows, conditional logic
- Slate: legacy custom HTML/CSS/JavaScript application development hosted on Foundry (documented for maintenance of existing Slate apps only — do not use for new development; see Chapter 7)
- CI/CD for Foundry: repository structure, automated testing, branch promotion workflows
- Security: CBAC in external apps, credential management, marking compliance in OSDK queries, audit trails
- Integration patterns: REST APIs, webhooks, cross-system data flows connecting MSS to external Army systems

**TM-40L does NOT cover:**
- Workshop application design (no-code/low-code) — see TM-20, TM-30
- Pipeline Builder visual UI — see TM-20, TM-30
- Basic Ontology modeling (UI-based) — see TM-30
- PySpark transforms — see TM-40H (AI Engineer) for AI pipelines; TM-30 for design
- AIP Logic configuration — see TM-30
- Agent Studio development — see TM-40H

> **NOTE:** TM-40L is peer to TM-40H (AI Engineer), TM-40I (ML Engineer), and TM-40G (ORSA). All four tracks require TM-30 as prerequisite. Each track owns a distinct technical domain. Coordinate across tracks — operational systems frequently require all four disciplines.

---

### 1-2. The Software Engineer's Role in USAREUR-AF

USAREUR-AF is the Army Service Component Command (ASCC) to USEUCOM. MSS supports theater land operations across the European AOR including V Corps, 21st TSC, 7th ATC, G2 all-source, and multinational elements. Software engineers at TM-40L level are the technical implementers of the USAREUR-AF data ecosystem.

**The TM-40L role in the data chain:**

```
MISSION REQUIREMENT
        |
        v
   -30 BUILDER               <- Design + configure
   (Ontology, Workshop,
    Action design specs)
        |
        v
   -40L SOFTWARE ENGINEER    <- You are here
   (OSDK, external apps,
    FOO, CI/CD,
    integration code)
        |
        v
   OPERATIONAL PRODUCT
   (Unit tracking apps,
    SITREP automation,
    readiness dashboards,
    EUCOM integrations)
        |
        v
   -10/-20 USER
   (Consume + act on data)
```

**Typical TM-40L deliverables in the USAREUR-AF context:**

| Deliverable | Description | Example |
|---|---|---|
| External application | Web or desktop app consuming MSS Ontology via OSDK | V Corps readiness dashboard consuming unit status objects |
| SITREP automation | App that reads Ontology objects and pushes formatted reports to external systems | Automated SITREP generation to EUCOM J3 portal |
| Integration service | Microservice bridging external Army system to MSS via REST/webhook | GCSS-Army feed into MSS equipment ontology |
| Slate app | Custom HTML/JS application hosted within Foundry (LEGACY — do not use for new development) | Interactive operational map with custom layers |
| FOO library | TypeScript computed properties enriching Ontology objects | Readiness score computed from component statuses |
| CI/CD pipeline | Automated testing and promotion workflow for Foundry code resources | Branch-gated promotion for production transforms |

---

### 1-3. Prerequisites and Baseline Skills

Complete all of the following before beginning this manual:

| Prerequisite | Verification |
|---|---|
| TM-10 (Maven User) | Can navigate MSS, consume data products, submit issues |
| TM-20 (Builder) | Can build basic Workshop apps, configure Object Types, create Actions via UI |
| TM-30 (Advanced Builder) | Can design full ontology models, advanced Pipeline Builder flows, multi-step Actions |
| Python proficiency | Can write, test, and debug Python scripts; understands async patterns, exception handling, type hints |
| TypeScript proficiency | Can write typed TypeScript; understands async/await, generics, module systems |
| Git proficiency | Understands branching, merging, pull requests, rebase workflows |
| REST API familiarity | Can read and write against REST APIs; understands auth patterns (OAuth2, bearer tokens) |

> **NOTE:** This manual does not teach Python or TypeScript. If you need to develop either skill, complete coursework before proceeding. Reference `learn-data.armydev.com` for approved training resources.

---

### 1-4. Governing References

| Document | Relevance |
|---|---|
| Army CIO Data Stewardship Policy (April 2, 2024) | Data stewardship hierarchy, governance chain, API access policy |
| UDRA v1.1 (February 2025) | Unified Data Reference Architecture — domain ownership, integration standards |
| USAREUR-AF C2DAO Guidance | Theater-level architecture standards; OSDK API enrollment requirements |
| DoD Data Strategy (2020) | VAUTI framework (Visible, Accessible, Understandable, Trustable, Interoperable) |
| NATO Architecture Framework v4 (NAFv4) | Coalition data architecture — applies to any integration with MPE-accessible objects |
| AR 25-2 | Army Cybersecurity — credential handling, system authorization |

**Reference:** `learn-data.armydev.com` — authoritative reference for OSDK API versions, enrollment procedures, and approved integration patterns. Consult before beginning any new external application development.

---

### 1-5. The USAREUR-AF 5-Layer Data Stack — SWE Responsibilities

```
+---------------------------------------------------------------+
|  LAYER 5: ACTIVATION                                          |
|  External apps, SITREP automation, EUCOM integrations         |
|  --> TM-40L primary operating layer                           |
+---------------------------------------------------------------+
|  LAYER 4: ANALYTICS                                           |
|  External OSDK apps, custom dashboards, FOO-enriched objects  |
|  --> TM-40L builds custom analytical applications             |
+---------------------------------------------------------------+
|  LAYER 3: SEMANTIC (ONTOLOGY)                                 |
|  FOO computed properties, Action validators, OSDK queries     |
|  --> TM-40L writes code executing against this layer          |
+---------------------------------------------------------------+
|  LAYER 2: INTEGRATION                                         |
|  Platform SDK dataset operations, transaction management      |
|  --> TM-40L manages programmatic dataset access               |
+---------------------------------------------------------------+
|  LAYER 1: INFRASTRUCTURE                                      |
|  CBAC, marking, credential provisioning                       |
|  --> TM-40L consumes; C2DAO/G6 administers                    |
+---------------------------------------------------------------+
```

TM-40L engineers are the primary implementers of Layers 4 and 5 technical components. They write code that executes at Layer 3 (Ontology) and Layer 2 (datasets) but coordinate with C2DAO for any Layer 1 changes.

---

## CHAPTER 2 — OSDK FUNDAMENTALS

> **CODE EXAMPLES:** Runnable OSDK and Ontology access patterns referenced in this chapter are available in the local development shim at [`data_skills/13_foundry_patterns/ontology_modeling.py`](../../../data_skills/13_foundry_patterns/ontology_modeling.py). Transform and check patterns are in [`python_transforms.py`](../../../data_skills/13_foundry_patterns/python_transforms.py) and [`foundry_checks.py`](../../../data_skills/13_foundry_patterns/foundry_checks.py). Activate the venv: `source data_skills/.venv/bin/activate`.

### 2-1. What Is the OSDK

**BLUF:** The Ontology SDK (OSDK) is the primary programmatic interface for external applications to query Ontology objects and execute Actions on MSS. It is the correct integration method for any external application consuming MSS data.

The OSDK allows external Python or TypeScript applications to:
- Query Ontology Object Types (with filtering, pagination, sorting)
- Read and traverse Link Types (relationships between objects)
- Execute Actions (triggering state changes in the Ontology)
- Subscribe to real-time Ontology changes

The OSDK is not a direct database connection. It is a governed API that enforces CBAC, markings, and audit logging at every query. An external application using the OSDK cannot access data the authenticated user or service account is not authorized to see — this is the correct security behavior.

> **NOTE:** The OSDK is the only approved method for external applications to interact with the MSS Ontology. Do not attempt to access Foundry datasets directly from external applications — use the OSDK for object data and the Platform SDK (Chapter 4) for dataset operations where approved.

---

### 2-2. Authentication Architecture

**CONDITIONS:** You have been issued OSDK credentials (service account token or OAuth2 client credentials) through the C2DAO-approved process. You have a valid Foundry enrollment for your external application.

**STANDARDS:** External application authenticates to MSS OSDK endpoint using approved credential type. No credentials appear in source code or version control. Token rotation is automated or procedurally managed per AR 25-2.

**EQUIPMENT:** Approved development environment; credential store (environment variables or secrets manager); OSDK Python or TypeScript package installed.

**Authentication types supported:**

| Type | Use Case | Notes |
|---|---|---|
| Personal Access Token (PAT) | Developer testing and local development | Never use in deployed applications |
| Service Account Token | Deployed server-side applications | Provisioned by C2DAO; rotate per policy |
| OAuth2 Confidential Client | Web applications with server-side token exchange | Requires C2DAO enrollment; preferred for web apps |
| OAuth2 Public Client (PKCE) | Single-page applications; user-delegated access | User's own permissions apply; no elevation |

> **CAUTION: Personal Access Tokens authenticate as you. A PAT committed to a repository gives anyone with repository access your full Foundry permissions. Treat PATs as passwords. Never commit them.**

**PROCEDURE — Configure OSDK authentication (Python, service account):**

1. Install the OSDK package for your enrolled application:
```bash
pip install foundry-sdk-python
# Or for a specific application ontology SDK:
pip install myapp-osdk
```

2. Store the service account token in environment variables — never in source code:
```bash
# .env file (never commit this file; add to .gitignore)
FOUNDRY_TOKEN=your_service_account_token_here
FOUNDRY_URL=https://mss.usareur.army.mil
```

3. Initialize the authentication client:
```python
import os
from foundry import FoundryClient
from foundry.auth import ConfidentialClientAuth

# Load credentials from environment — never hardcode
token = os.environ["FOUNDRY_TOKEN"]
base_url = os.environ["FOUNDRY_URL"]

# Initialize client with token auth (service account pattern)
client = FoundryClient(
    auth=token,
    hostname=base_url,
)
```

4. Verify connectivity before proceeding with any operational query:
```python
def verify_connection(client: FoundryClient) -> bool:
    """
    Verify OSDK client can reach MSS before beginning operations.
    Returns True if healthy; raises on failure.
    """
    try:
        # Lightweight ping — does not pull operational data
        client.ontology.ontologies.list()
        return True
    except Exception as exc:
        raise RuntimeError(
            f"MSS OSDK connection failed. Check FOUNDRY_TOKEN and FOUNDRY_URL. "
            f"Contact C2DAO if credentials are expired. Error: {exc}"
        ) from exc
```

5. For TypeScript applications, initialize the OSDK client:
```typescript
import { createClient } from "@osdk/client";
import { createConfidentialOauthClient } from "@osdk/oauth";

// Load credentials from environment — never hardcode
const foundryUrl = process.env.FOUNDRY_URL!;
const clientId = process.env.OSDK_CLIENT_ID!;
const clientSecret = process.env.OSDK_CLIENT_SECRET!;

const auth = createConfidentialOauthClient(
  clientId,
  clientSecret,
  foundryUrl,
);

const client = createClient(
  foundryUrl,
  "<your-ontology-rid>",
  auth,
);
```

> **NOTE:** OAuth2 confidential client is the preferred pattern for deployed server-side TypeScript applications. It allows token refresh without re-deployment. Coordinate with C2DAO for client ID and secret provisioning.

---

### 2-3. Querying Objects — Fundamentals

**CONDITIONS:** OSDK client initialized and authenticated. Target Object Type is enrolled in your application's ontology. You have read access to the target Object Type.

**STANDARDS:** All queries include explicit pagination. Filter logic does not retrieve data beyond operational need (least-privilege data access). Error handling covers authentication failures, network errors, and empty result sets.

**EQUIPMENT:** Authenticated OSDK client (Python or TypeScript); target Object Type enrolled in application ontology; OSDK package installed in development environment.

**PROCEDURE — Basic object query (Python):**

```python
from foundry import FoundryClient
from foundry.models import ObjectSet

def get_unit_status_records(
    client: FoundryClient,
    unit_id: str,
) -> list[dict]:
    """
    Retrieve unit readiness status objects for a given unit ID.
    Applies filter to unit_id property — does not pull full object set.

    Args:
        client: Authenticated OSDK client
        unit_id: UIC string (e.g., "W12345")

    Returns:
        List of unit status dicts for downstream processing
    """
    results = []

    # Filter at query time — never pull all objects and filter in Python
    object_set = (
        client.ontology
        .objects["UnitStatus"]
        .filter({"property": "unitId", "type": "eq", "value": unit_id})
        .take(200)  # Explicit page size — never unbounded
    )

    for obj in object_set:
        results.append({
            "rid": obj.rid,
            "unit_id": obj.properties.get("unitId"),
            "readiness_level": obj.properties.get("readinessLevel"),
            "as_of_dtg": obj.properties.get("asOfDtg"),
            "reporting_officer": obj.properties.get("reportingOfficer"),
        })

    return results
```

**PROCEDURE — Basic object query (TypeScript):**

```typescript
import { client } from "./client"; // your initialized OSDK client
import { UnitStatus } from "@your-app/osdk";

interface UnitStatusRecord {
  rid: string;
  unitId: string | undefined;
  readinessLevel: string | undefined;
  asOfDtg: string | undefined;
}

async function getUnitStatusRecords(
  unitId: string,
): Promise<UnitStatusRecord[]> {
  const results: UnitStatusRecord[] = [];

  // Filter server-side — do not pull full object population
  for await (const obj of client(UnitStatus)
    .where(UnitStatus.unitId.eq(unitId))
    .asyncIter()) {
    results.push({
      rid: obj.$primaryKey,
      unitId: obj.unitId,
      readinessLevel: obj.readinessLevel,
      asOfDtg: obj.asOfDtg,
    });
  }

  return results;
}
```

---

### 2-4. Pagination

**BLUF:** Every OSDK query that returns more than one object must implement explicit pagination. Unbounded queries against large operational object populations will time out or degrade platform performance.

**CONDITIONS:** OSDK client initialized and authenticated. Target Object Type has more than one result in the expected query scope.

**STANDARDS:** All multi-object queries use explicit page sizes. No unbounded queries against operational Object Types. Application handles empty result sets and end-of-page conditions without error.

**EQUIPMENT:** Authenticated OSDK client (Python or TypeScript); target Object Type enrolled in application.

**PROCEDURE — Paginated query with page token (Python):**

```python
from typing import Generator

def paginated_equipment_query(
    client: FoundryClient,
    status_filter: str,
    page_size: int = 100,
) -> Generator[dict, None, None]:
    """
    Generator-based paginated query for equipment objects.
    Yields one object dict at a time to avoid building large in-memory lists.

    Args:
        client:        Authenticated OSDK client
        status_filter: Equipment status string (e.g., "FMC", "NMC")
        page_size:     Objects per page (max 200; default 100)

    Yields:
        Equipment object dicts
    """
    page_token = None

    while True:
        # Build the query with page parameters
        query_params = {
            "filter": {
                "property": "equipmentStatus",
                "type": "eq",
                "value": status_filter,
            },
            "pageSize": page_size,
        }
        if page_token:
            query_params["pageToken"] = page_token

        page = client.ontology.objects["Equipment"].list(**query_params)

        for obj in page.data:
            yield {
                "rid": obj.rid,
                "bumper_number": obj.properties.get("bumperNumber"),
                "equipment_status": obj.properties.get("equipmentStatus"),
                "owning_unit": obj.properties.get("owningUnit"),
                "last_pmcs_dtg": obj.properties.get("lastPmcsDtg"),
            }

        # Advance page or exit
        page_token = page.next_page_token
        if not page_token:
            break
```

> **NOTE:** Set `page_size` to 100 as a default for operational queries. Reduce to 25–50 if objects have many properties or linked objects. Never exceed 200 per page. Consult C2DAO guidance for Object Types marked as high-cardinality.

---

### 2-5. Filtering and Sorting

**CONDITIONS:** OSDK client initialized and authenticated. Target Object Type is enrolled in the application and accessible to the authenticated principal.

**STANDARDS:** Filters are applied server-side. OR filters are profiled against representative data before deployment. Query logic retrieves only data within operational need (least-privilege access).

**EQUIPMENT:** Authenticated OSDK TypeScript client; target Object Type definitions imported from generated OSDK package.

**PROCEDURE — Compound filters and sorting (TypeScript):**

```typescript
import { UnitStatus, Equipment } from "@your-app/osdk";

// Compound filter: multiple conditions (AND logic)
async function getNonMissionCapableEquipment(
  unitId: string,
  minDaysSinceLastMaintenance: number,
): Promise<Equipment[]> {
  const cutoffDate = new Date();
  cutoffDate.setDate(cutoffDate.getDate() - minDaysSinceLastMaintenance);

  const results: Equipment[] = [];

  for await (const obj of client(Equipment)
    .where({
      $and: [
        Equipment.owningUnit.eq(unitId),
        Equipment.equipmentStatus.eq("NMC"),
        Equipment.lastPmcsDtg.lt(cutoffDate.toISOString()),
      ],
    })
    .orderBy({ lastPmcsDtg: "asc" }) // Oldest maintenance first
    .asyncIter()) {
    results.push(obj);
  }

  return results;
}

// Filter with OR logic — use sparingly on large populations
async function getCriticalOrNmcEquipment(
  unitId: string,
): Promise<Equipment[]> {
  const results: Equipment[] = [];

  for await (const obj of client(Equipment)
    .where({
      $and: [
        Equipment.owningUnit.eq(unitId),
        {
          $or: [
            Equipment.equipmentStatus.eq("NMC"),
            Equipment.priority.eq("CRITICAL"),
          ],
        },
      ],
    })
    .asyncIter()) {
    results.push(obj);
  }

  return results;
}
```

> **CAUTION: OR filters on high-cardinality Object Types execute full scans on the affected properties. Profile with representative data before deploying OR-heavy filters to production. Prefer multiple targeted AND queries over broad OR scans when object populations exceed 10,000.**

---

### 2-6. Traversing Link Types

**CONDITIONS:** OSDK client initialized and authenticated. Parent Object Type and Link Type are enrolled in the application. Authenticated principal has read access to both sides of the link.

**STANDARDS:** Link traversal is batched where possible. Single-object link traversal is not used inside loops over large object populations. Result is bounded and does not load unbounded child sets into memory.

**EQUIPMENT:** Authenticated OSDK Python client; parent Object Type RID; Link Type name.

**PROCEDURE — Follow links from parent to child objects (Python):**

```python
def get_unit_with_equipment(
    client: FoundryClient,
    unit_rid: str,
) -> dict:
    """
    Retrieve a unit object and its linked equipment via the
    UnitToEquipment link type. Returns a structured dict.

    Link traversal adds a secondary query — do not call this
    in a loop over large unit populations without batching.
    """
    # Fetch the parent unit object
    unit = client.ontology.objects["Unit"].get(unit_rid)

    # Traverse the link to child equipment objects
    equipment_list = []
    for equip in unit.links["UnitToEquipment"].get_linked_objects():
        equipment_list.append({
            "rid": equip.rid,
            "bumper_number": equip.properties.get("bumperNumber"),
            "status": equip.properties.get("equipmentStatus"),
        })

    return {
        "unit_rid": unit.rid,
        "unit_name": unit.properties.get("unitName"),
        "uic": unit.properties.get("uic"),
        "equipment": equipment_list,
        "equipment_count": len(equipment_list),
    }
```

> **NOTE:** Link traversal is a separate API call per object. For bulk link traversal across many parent objects, use the batch link query pattern described in Chapter 3.

---

## CHAPTER 3 — OSDK ADVANCED PATTERNS

### 3-1. Action Execution via OSDK

**BLUF:** Actions are the approved mechanism for external applications to write state changes back into the MSS Ontology. Do not write to Ontology datasets directly. Use Actions.

**CONDITIONS:** Action is defined and deployed in the MSS Ontology by a -30 builder or -40 developer. Your OSDK application enrollment includes the Action in its API scope. The authenticated service account has permission to execute the Action.

**STANDARDS:** Action execution includes parameter validation before submission. Responses are handled for both success and error cases. All Action executions are logged at the application level for audit purposes.

**EQUIPMENT:** Authenticated OSDK client (Python or TypeScript); Action name and parameter schema obtained from -30 builder or Ontology documentation; application-level logger configured.

**PROCEDURE — Execute Action (Python):**

```python
import logging
from datetime import datetime, timezone
from foundry.models import ActionResponse

logger = logging.getLogger(__name__)

def submit_sitrep_entry(
    client: FoundryClient,
    unit_rid: str,
    readiness_level: str,
    personnel_strength: int,
    equipment_pct: float,
    reporting_officer: str,
    dtg: str | None = None,
) -> ActionResponse:
    """
    Submit a SITREP entry via the SubmitSitrep Action.
    Validates parameters before submission and logs result.

    Args:
        client:               Authenticated OSDK client
        unit_rid:             RID of the Unit object
        readiness_level:      C-rating string ("C1", "C2", "C3", "C4")
        personnel_strength:   Assigned strength as integer
        equipment_pct:        Equipment readiness as float 0.0-1.0
        reporting_officer:    Name/ID of submitting officer
        dtg:                  ISO8601 DTG string; defaults to now (UTC)

    Returns:
        ActionResponse from MSS

    Raises:
        ValueError: On invalid parameter values (pre-flight check)
        RuntimeError: On Action execution failure
    """
    # Pre-flight parameter validation — fail fast before hitting the API
    valid_c_ratings = {"C1", "C2", "C3", "C4"}
    if readiness_level not in valid_c_ratings:
        raise ValueError(
            f"Invalid readiness_level '{readiness_level}'. "
            f"Must be one of: {valid_c_ratings}"
        )

    if not 0 <= personnel_strength <= 10000:
        raise ValueError(
            f"personnel_strength {personnel_strength} out of range [0, 10000]"
        )

    if not 0.0 <= equipment_pct <= 1.0:
        raise ValueError(
            f"equipment_pct {equipment_pct} out of range [0.0, 1.0]"
        )

    # Default DTG to current UTC if not provided
    if dtg is None:
        dtg = datetime.now(timezone.utc).strftime("%Y%m%dT%H%MZ")

    # Execute Action — parameters must match Action parameter schema
    try:
        response = client.ontology.actions["SubmitSitrep"].apply(
            unit=unit_rid,
            readinessLevel=readiness_level,
            personnelStrength=personnel_strength,
            equipmentReadinessPct=equipment_pct,
            reportingOfficer=reporting_officer,
            reportingDtg=dtg,
        )

        logger.info(
            "SubmitSitrep action executed: unit=%s readiness=%s dtg=%s",
            unit_rid, readiness_level, dtg,
        )
        return response

    except Exception as exc:
        logger.error(
            "SubmitSitrep action failed: unit=%s error=%s",
            unit_rid, exc,
        )
        raise RuntimeError(
            f"SubmitSitrep action failed for unit {unit_rid}: {exc}"
        ) from exc
```

**PROCEDURE — Execute Action (TypeScript):**

```typescript
import { SubmitSitrep } from "@your-app/osdk";

interface SitrepPayload {
  unitRid: string;
  readinessLevel: "C1" | "C2" | "C3" | "C4";
  personnelStrength: number;
  equipmentReadinessPct: number;
  reportingOfficer: string;
  reportingDtg?: string;
}

async function submitSitrepEntry(
  payload: SitrepPayload,
): Promise<void> {
  // TypeScript type system enforces readiness level at compile time
  // Runtime validation for numeric ranges
  if (payload.personnelStrength < 0 || payload.personnelStrength > 10000) {
    throw new RangeError(
      `personnelStrength ${payload.personnelStrength} out of range [0, 10000]`,
    );
  }

  if (payload.equipmentReadinessPct < 0 || payload.equipmentReadinessPct > 1) {
    throw new RangeError(
      `equipmentReadinessPct must be between 0.0 and 1.0`,
    );
  }

  const dtg =
    payload.reportingDtg ?? new Date().toISOString();

  await client(SubmitSitrep).applyAction({
    unit: { $primaryKey: payload.unitRid },
    readinessLevel: payload.readinessLevel,
    personnelStrength: payload.personnelStrength,
    equipmentReadinessPct: payload.equipmentReadinessPct,
    reportingOfficer: payload.reportingOfficer,
    reportingDtg: dtg,
  });
}
```

---

### 3-2. Object Subscriptions — Real-Time Change Notifications

**BLUF:** OSDK subscriptions allow external applications to receive push notifications when Ontology objects change, eliminating polling loops against operational data.

**CONDITIONS:** Target Object Type supports subscriptions (confirm with C2DAO). Application server can maintain a persistent WebSocket connection to MSS. Network path from application server to MSS is stable.

**STANDARDS:** Subscription handlers are idempotent — duplicate events do not cause duplicate state changes. Subscription errors are caught and logged. Application recovers from dropped connections with backoff retry.

**EQUIPMENT:** Authenticated OSDK TypeScript client with subscription support; stable network path to MSS with WebSocket allowed; application-level logger and error handler configured.

**PROCEDURE — Subscribe to object changes (TypeScript):**

```typescript
import { UnitStatus } from "@your-app/osdk";

interface SubscriptionHandler {
  onUpdate: (obj: UnitStatus) => Promise<void>;
  onError: (error: Error) => void;
}

async function subscribeToUnitStatusChanges(
  unitIds: string[],
  handler: SubscriptionHandler,
): Promise<() => void> {
  /**
   * Subscribe to real-time UnitStatus object changes.
   * Returns an unsubscribe function — call it to clean up.
   *
   * Used by SITREP automation service to receive push updates
   * from MSS without polling.
   */
  const subscription = await client(UnitStatus)
    .where(UnitStatus.unitId.containsAnyTerm(unitIds))
    .subscribe({
      onChange: async ({ object, type }) => {
        if (type === "ADDED_OR_UPDATED") {
          try {
            // Handler must be idempotent — may receive same event twice
            await handler.onUpdate(object);
          } catch (err) {
            handler.onError(
              new Error(`Failed to process update for ${object.$primaryKey}: ${err}`),
            );
          }
        }
      },
      onOutOfDate: () => {
        // Subscription state is stale — re-query baseline then re-subscribe
        console.warn(
          "UnitStatus subscription out of date. Re-synchronizing baseline.",
        );
      },
      onError: (err) => {
        handler.onError(new Error(`Subscription error: ${err}`));
      },
    });

  // Return unsubscribe function for caller to invoke on shutdown
  return () => subscription.unsubscribe();
}
```

> **CAUTION: Subscription scope should be narrowed with filters when possible. An unfiltered subscription on a large operational Object Type (e.g., all Equipment in USAREUR-AF) will generate high event volume and can saturate application event queues. Filter to the AOR or unit population your application needs.**

---

### 3-3. Bulk Object Operations

**BLUF:** When processing multiple objects, use batch query patterns instead of per-object loops. Per-object queries (N+1 pattern) at operational scale will breach rate limits and degrade performance for all MSS users.

**CONDITIONS:** OSDK client initialized and authenticated. List of target object RIDs or filter criteria is known. Object population to process exceeds 10 objects (use single-object queries for smaller sets).

**STANDARDS:** No N+1 query pattern in production code. Batch size is bounded (50 RIDs per chunk default). Total result set is bounded before processing begins.

**EQUIPMENT:** Authenticated OSDK Python client; list of object RIDs or filter parameters.

**PROCEDURE — Bulk load by RID list (Python):**

```python
from itertools import islice
from typing import Iterator

def chunked(iterable, size: int) -> Iterator[list]:
    """Split an iterable into fixed-size chunks."""
    it = iter(iterable)
    while chunk := list(islice(it, size)):
        yield chunk

def bulk_get_equipment_by_rid(
    client: FoundryClient,
    rids: list[str],
    chunk_size: int = 50,
) -> dict[str, dict]:
    """
    Retrieve multiple equipment objects by RID using chunked batch queries.

    The OSDK does not support arbitrary IN-clause queries by default.
    This pattern chunks the RID list and queries by filter in batches.

    Args:
        client:     Authenticated OSDK client
        rids:       List of equipment object RIDs
        chunk_size: RIDs per batch (keep <= 50 for safety)

    Returns:
        Dict mapping RID -> equipment property dict
    """
    result_map: dict[str, dict] = {}

    for chunk in chunked(rids, chunk_size):
        # Batch query using rid filter for this chunk
        for obj in client.ontology.objects["Equipment"].filter(
            {"property": "__rid", "type": "in", "value": chunk}
        ):
            result_map[obj.rid] = {
                "bumper_number": obj.properties.get("bumperNumber"),
                "equipment_status": obj.properties.get("equipmentStatus"),
                "owning_unit": obj.properties.get("owningUnit"),
            }

    return result_map
```

---

### 3-4. Error Handling and Retry Patterns

**CONDITIONS:** OSDK client initialized. Application must handle transient network errors and rate-limit responses without losing data or causing duplicate state changes.

**STANDARDS:** All OSDK calls are wrapped in error handling. Retries use exponential backoff. Authentication failures (401/403) are not retried — they are logged and raised immediately. Maximum retry attempts are bounded.

**EQUIPMENT:** Authenticated OSDK Python client; logging configured to capture retry attempts and final failures.

**PROCEDURE — Retry with exponential backoff (Python):**

```python
import time
import logging
from typing import Callable, TypeVar

logger = logging.getLogger(__name__)
T = TypeVar("T")

def with_retry(
    func: Callable[[], T],
    max_attempts: int = 3,
    base_delay_seconds: float = 1.0,
    retryable_status_codes: set[int] | None = None,
) -> T:
    """
    Execute an OSDK call with exponential backoff retry.

    Retries on transient network errors and rate-limit responses (429).
    Does NOT retry on auth failures (401/403) or bad request (400).

    Args:
        func:                   Callable wrapping the OSDK operation
        max_attempts:           Maximum retry attempts (default 3)
        base_delay_seconds:     Initial retry delay; doubles each attempt
        retryable_status_codes: HTTP status codes to retry on (default: {429, 503})

    Returns:
        Result of func() on success

    Raises:
        Last exception after all retries exhausted
    """
    if retryable_status_codes is None:
        retryable_status_codes = {429, 503}

    last_exc: Exception | None = None

    for attempt in range(1, max_attempts + 1):
        try:
            return func()
        except Exception as exc:
            last_exc = exc

            # Check if this is a retryable error
            status_code = getattr(exc, "status_code", None)
            is_retryable = (
                status_code in retryable_status_codes
                or "timeout" in str(exc).lower()
                or "connection" in str(exc).lower()
            )

            if not is_retryable:
                logger.error("Non-retryable OSDK error: %s", exc)
                raise

            if attempt < max_attempts:
                delay = base_delay_seconds * (2 ** (attempt - 1))
                logger.warning(
                    "OSDK call failed (attempt %d/%d), retrying in %.1fs: %s",
                    attempt, max_attempts, delay, exc,
                )
                time.sleep(delay)
            else:
                logger.error(
                    "OSDK call failed after %d attempts: %s",
                    max_attempts, exc,
                )

    raise RuntimeError(
        f"OSDK operation failed after {max_attempts} attempts"
    ) from last_exc
```

---

## CHAPTER 4 — FOUNDRY PLATFORM SDK

### 4-1. What Is the Platform SDK

**BLUF:** The Foundry Platform SDK (Python) provides programmatic access to Foundry datasets, branches, transactions, and file resources. Use it when you need to read or write tabular data, manage dataset transactions, or access files stored in Foundry. Use the OSDK (Chapters 2–3) for Ontology object access.

The Platform SDK is not a general-purpose data lake client. All access must be authorized by the C2DAO data steward for the target dataset. Do not use the Platform SDK to bypass CBAC — the SDK enforces the same access controls as the Foundry UI.

> **CAUTION: Writing to production datasets via the Platform SDK without coordination with the owning data steward is not authorized. Always write to development branches and promote through the standard review process. Chapter 8 covers promotion workflows.**

---

### 4-2. Client Initialization and Authentication

**CONDITIONS:** Service account token and Foundry base URL are provisioned and stored in environment variables. Platform SDK Python package is installed in the development environment.

**STANDARDS:** Client is initialized from environment variables only. No credentials appear in source code. Connection is verified before any dataset operation begins.

**EQUIPMENT:** Approved development environment; `FOUNDRY_TOKEN` and `FOUNDRY_URL` environment variables set from C2DAO-approved credential store; Platform SDK Python package installed.

**PROCEDURE — Initialize the Platform SDK client (Python):**

```python
import os
from foundry import FoundryClient

def build_platform_client() -> FoundryClient:
    """
    Build and return an authenticated Foundry Platform SDK client.
    Credentials loaded from environment — never hardcoded.

    Required environment variables:
        FOUNDRY_TOKEN:  Service account or PAT token
        FOUNDRY_URL:    MSS base URL
    """
    token = os.environ.get("FOUNDRY_TOKEN")
    base_url = os.environ.get("FOUNDRY_URL")

    if not token or not base_url:
        raise EnvironmentError(
            "FOUNDRY_TOKEN and FOUNDRY_URL must be set in environment. "
            "See team credential store for approved service account values."
        )

    return FoundryClient(auth=token, hostname=base_url)
```

---

### 4-3. Dataset Operations — Reading

**CONDITIONS:** Platform SDK client initialized and authenticated. Dataset RID is known. Authenticated principal has read access to the target dataset and branch. Data steward authorization obtained for production reads in automated pipelines.

**STANDARDS:** Large dataset reads use column selection or row limits. Full dataset reads are not performed on production datasets without data steward coordination. Schema is validated before downstream processing.

**EQUIPMENT:** Authenticated Platform SDK Python client; dataset RID; target branch name; `pandas` and `pyarrow` packages installed.

**PROCEDURE — Read a Foundry dataset into a pandas DataFrame (Python):**

```python
import pandas as pd
from foundry import FoundryClient

def read_dataset(
    client: FoundryClient,
    dataset_rid: str,
    branch: str = "master",
    columns: list[str] | None = None,
) -> pd.DataFrame:
    """
    Read a Foundry dataset into a pandas DataFrame.

    Args:
        client:      Authenticated Platform SDK client
        dataset_rid: RID of the target dataset
        branch:      Branch to read from (default "master" = production)
        columns:     Column subset to read; reads all if None

    Returns:
        pandas DataFrame with dataset contents

    Notes:
        - For large datasets, use the row_limit or filter params
          to avoid loading full production datasets into memory.
        - Always confirm dataset schema with data steward before
          reading in production pipelines.
    """
    dataset = client.datasets.Dataset.get(dataset_rid)

    # Read via the Parquet/Arrow interface for performance
    df = dataset.read_table(
        branch_name=branch,
        columns=columns,
    )

    return df.to_pandas()


def read_dataset_with_limit(
    client: FoundryClient,
    dataset_rid: str,
    row_limit: int = 10000,
) -> pd.DataFrame:
    """
    Read a bounded row sample from a dataset.
    Use for validation, profiling, and dev/test workflows.
    Never use unlimited reads on large production datasets.
    """
    dataset = client.datasets.Dataset.get(dataset_rid)

    # Read first N rows only
    table = dataset.read_table(
        branch_name="master",
        start_transaction_rid=None,
        end_transaction_rid=None,
        row_limit=row_limit,
    )

    return table.to_pandas()
```

---

### 4-4. Dataset Operations — Writing with Transactions

**BLUF:** All writes to Foundry datasets use transactions. A transaction is an atomic unit of work — either all writes in a transaction commit or none do. Always open a transaction before writing and close it explicitly.

**Transaction types:**

| Type | Use Case | Behavior |
|---|---|---|
| `APPEND` | Add new rows to existing dataset | Does not modify existing data |
| `UPDATE` | Replace dataset contents | Replaces all rows (destructive — coordinate with steward) |
| `SNAPSHOT` | Replace full dataset atomically | Creates new snapshot; preferred for full-refresh pipelines |
| `DELETE` | Remove specific rows | Use sparingly; coordinate with data steward |

> **CAUTION:** APPEND transactions are NOT inherently idempotent. Each APPEND call adds data to the dataset without deduplication. To achieve idempotent writes, implement deduplication logic yourself using content hashes or surrogate keys before appending. Use SNAPSHOT transactions for full-dataset atomic replacement.

**CONDITIONS:** Platform SDK client initialized and authenticated. Target dataset RID is known. Authenticated principal has write access to the target branch. Data steward authorization obtained for any write to a shared staging or production dataset. Deduplication logic is implemented if APPEND transaction is used.

**STANDARDS:** All writes use transactions. Transactions are explicitly committed or aborted — no open transactions left on error. Writes target `develop` branch by default; writes to `master` require explicit steward coordination. APPEND transactions include deduplication logic to ensure idempotency.

**EQUIPMENT:** Authenticated Platform SDK Python client; dataset RID; target branch name; `pandas` and `pyarrow` packages installed.

**PROCEDURE — Write to dataset with APPEND transaction (Python):**

```python
import pandas as pd
import pyarrow as pa
from foundry import FoundryClient

def append_sitrep_records(
    client: FoundryClient,
    dataset_rid: str,
    records: list[dict],
    branch: str = "develop",
) -> str:
    """
    Append SITREP records to a staging dataset via APPEND transaction.

    Writes to the 'develop' branch by default — never write directly
    to master without C2DAO coordination and steward approval.

    Args:
        client:      Authenticated Platform SDK client
        dataset_rid: RID of the target staging dataset
        records:     List of dicts matching the dataset schema
        branch:      Target branch (default "develop")

    Returns:
        Transaction RID for audit logging

    Raises:
        ValueError: If records list is empty
        RuntimeError: On transaction failure
    """
    if not records:
        raise ValueError("records list is empty — nothing to append")

    df = pd.DataFrame(records)
    table = pa.Table.from_pandas(df)

    dataset = client.datasets.Dataset.get(dataset_rid)

    # Open transaction — all writes are atomic within this context
    transaction = dataset.start_transaction(
        branch_name=branch,
        transaction_type="APPEND",
    )

    try:
        # Write the Arrow table to the transaction
        transaction.write_table(table)

        # Commit the transaction — data is now visible on the branch
        transaction.commit()

        return transaction.rid

    except Exception as exc:
        # Abort on any error — do not leave open transactions
        try:
            transaction.abort()
        except Exception:
            pass  # Best-effort abort
        raise RuntimeError(
            f"Dataset write failed, transaction aborted: {exc}"
        ) from exc


def snapshot_dataset(
    client: FoundryClient,
    dataset_rid: str,
    new_data: pd.DataFrame,
    branch: str = "develop",
) -> str:
    """
    Replace full dataset contents via SNAPSHOT transaction.
    Use for full-refresh pipelines that replace prior data each run.

    WARNING: This replaces ALL existing data on the target branch.
    Coordinate with the data steward before using on shared datasets.
    """
    table = pa.Table.from_pandas(new_data)
    dataset = client.datasets.Dataset.get(dataset_rid)

    transaction = dataset.start_transaction(
        branch_name=branch,
        transaction_type="SNAPSHOT",
    )

    try:
        transaction.write_table(table)
        transaction.commit()
        return transaction.rid
    except Exception as exc:
        try:
            transaction.abort()
        except Exception:
            pass
        raise RuntimeError(
            f"Snapshot transaction failed, aborted: {exc}"
        ) from exc
```

---

### 4-5. File Resources

**CONDITIONS:** Platform SDK client initialized and authenticated. Target dataset RID is known. Authenticated principal has read or write access to the target dataset file store. File content is validated before upload.

**STANDARDS:** File uploads use APPEND transactions and are committed or aborted explicitly. File paths are well-defined logical paths — not arbitrary file system paths. Sensitive file content is not logged.

**EQUIPMENT:** Authenticated Platform SDK Python client; dataset RID; target branch name; file content as bytes.

**PROCEDURE — Read and write file resources in Foundry (Python):**

```python
import io
from foundry import FoundryClient

def upload_report_file(
    client: FoundryClient,
    dataset_rid: str,
    file_content: bytes,
    file_path: str,
    branch: str = "develop",
) -> None:
    """
    Upload a file (PDF, CSV, JSON) to a Foundry dataset's file store.

    Used to attach generated reports, exports, or reference files
    to a dataset resource without writing tabular data.

    Args:
        client:       Authenticated Platform SDK client
        dataset_rid:  RID of target dataset
        file_content: Raw bytes of the file to upload
        file_path:    Logical path within the dataset file store
        branch:       Target branch
    """
    dataset = client.datasets.Dataset.get(dataset_rid)

    transaction = dataset.start_transaction(
        branch_name=branch,
        transaction_type="APPEND",
    )

    try:
        transaction.put_file(
            logical_path=file_path,
            file_data=io.BytesIO(file_content),
        )
        transaction.commit()
    except Exception as exc:
        try:
            transaction.abort()
        except Exception:
            pass
        raise RuntimeError(f"File upload failed: {exc}") from exc


def download_reference_file(
    client: FoundryClient,
    dataset_rid: str,
    file_path: str,
) -> bytes:
    """
    Download a reference file from a Foundry dataset file store.

    Returns:
        Raw bytes of the file
    """
    dataset = client.datasets.Dataset.get(dataset_rid)
    file_handle = dataset.get_file(logical_path=file_path)
    return file_handle.read()
```

---

### 4-6. Branch Management

**CONDITIONS:** Platform SDK client initialized and authenticated. Dataset RID is known. Authenticated principal has branch management permissions on the target dataset.

**STANDARDS:** Development branches are created from `master`. Branch names follow the naming convention in NAMING_AND_GOVERNANCE_STANDARDS. Branches are not left open indefinitely after development work completes.

**EQUIPMENT:** Authenticated Platform SDK Python client; dataset RID; desired branch name.

**PROCEDURE — List branches and create a development branch (Python):**

```python
def get_or_create_dev_branch(
    client: FoundryClient,
    dataset_rid: str,
    branch_name: str,
) -> str:
    """
    Get an existing branch or create it from master.
    Standard pattern for setting up a development branch
    before writing to a dataset.

    Returns:
        Branch name (string) — usable in subsequent SDK calls
    """
    dataset = client.datasets.Dataset.get(dataset_rid)

    existing_branches = {b.name for b in dataset.list_branches()}

    if branch_name in existing_branches:
        return branch_name

    # Create from master — the development branch inherits production state
    dataset.create_branch(
        branch_name=branch_name,
        source_branch_name="master",
    )

    return branch_name
```

---

## CHAPTER 5 — TYPESCRIPT FUNCTIONS ON OBJECTS (FOO)

### 5-1. What Are Functions on Objects

**BLUF:** Functions on Objects (FOO) are TypeScript functions deployed within Foundry that compute derived properties, aggregate data, or perform transformations directly on Ontology objects at query time. FOO runs server-side in the Foundry compute layer — not in external apps.

FOO is the correct mechanism for:
- Computed properties on objects (e.g., readiness score derived from component statuses)
- Aggregations across object populations (e.g., total equipment count by unit and status)
- Bulk transformations that need access to linked objects
- Custom search logic not expressible via standard OSDK filters

FOO is not appropriate for:
- Long-running batch computations — use Pipeline Builder transforms
- External API calls — FOO runs in a sandboxed environment
- Stateful operations — FOO functions are stateless

> **NOTE:** FOO functions are deployed as Foundry code resources in a TypeScript repository. They are subject to the same CI/CD and governance requirements as any production code resource. Chapter 8 covers repository and deployment discipline.

---

### 5-2. FOO Repository Structure

**A standard FOO repository structure:**

```
my-foo-functions/
├── src/
│   ├── index.ts            # Function exports — all functions registered here
│   ├── readiness/
│   │   ├── readinessScore.ts
│   │   ├── equipmentAggregate.ts
│   │   └── __tests__/
│   │       ├── readinessScore.test.ts
│   │       └── equipmentAggregate.test.ts
│   └── utils/
│       ├── ratingHelpers.ts
│       └── dateHelpers.ts
├── package.json
├── tsconfig.json
└── foundry.json            # Foundry project configuration
```

---

### 5-3. Computed Property Functions

**CONDITIONS:** TypeScript FOO repository is configured per Section 5-2. Target Object Type is registered in the Foundry Ontology. Computation cost is assessed as acceptable for on-demand execution (see decision framework in Concepts Guide Section 5).

**STANDARDS:** FOO function returns a defined type. Null/undefined property values are handled without throwing. Function is stateless — no module-level state accumulated across calls. Unit test coverage meets minimum per Section 8-4.

**EQUIPMENT:** TypeScript development environment; `@foundry/functions-api` and `@foundry/ontology-api` packages; Jest test framework.

**PROCEDURE — Define a computed property FOO function (TypeScript):**

```typescript
import { Function, Double, String } from "@foundry/functions-api";
import {
  UnitStatus,
  Equipment,
  MaintenanceRecord,
} from "@foundry/ontology-api";

// Computed property: overall unit readiness score (0.0 - 1.0)
// Factors: personnel fill rate, equipment FMC rate, maintenance current
export class ReadinessFunctions {
  @Function()
  computeUnitReadinessScore(unit: UnitStatus): Double {
    /**
     * Compute a composite readiness score for a unit.
     * Score = (personnel fill * 0.4) + (equipment FMC * 0.4) + (maint current * 0.2)
     *
     * Returns 0.0 if any required property is missing.
     * This score feeds the Readiness Dashboard Workshop application.
     */
    const personnelFill = unit.personnelFillRate ?? 0;
    const equipmentFmc = unit.equipmentFmcRate ?? 0;
    const maintCurrent = unit.maintenanceCurrentPct ?? 0;

    // Weighted composite score
    const score =
      personnelFill * 0.4 + equipmentFmc * 0.4 + maintCurrent * 0.2;

    // Clamp to [0.0, 1.0] — defensive against data anomalies
    return Math.max(0.0, Math.min(1.0, score));
  }

  @Function()
  computeReadinessRating(unit: UnitStatus): String {
    /**
     * Convert numeric readiness score to C-rating string.
     * Thresholds align with FM 7-0 readiness standards.
     */
    const score = this.computeUnitReadinessScore(unit);

    if (score >= 0.9) return "C1";
    if (score >= 0.75) return "C2";
    if (score >= 0.5) return "C3";
    return "C4";
  }
}
```

---

### 5-4. Bulk Query Patterns

**BLUF:** FOO bulk query functions execute server-side against the full object population. Design them to minimize object property access and avoid N+1 link traversals in hot paths.

**CONDITIONS:** Object Type is registered in the Foundry Ontology. ObjectSet passed to the function is pre-filtered by the caller to the relevant population. Computation is assessed as scalable against production object volumes.

**STANDARDS:** Function accesses only the properties it needs. No N+1 link traversal inside object iteration loops. Function is profiled against production-scale data volumes before deployment. Returns empty/zero result for empty ObjectSet without error.

**EQUIPMENT:** TypeScript development environment; `@foundry/functions-api` and `@foundry/ontology-api` packages; production-scale test data for profiling.

**PROCEDURE — Aggregate function across multiple objects (TypeScript):**

```typescript
import {
  Function,
  FunctionsMap,
  Integer,
  Double,
} from "@foundry/functions-api";
import { Equipment, ObjectSet } from "@foundry/ontology-api";

export class EquipmentAggregateFunctions {
  @Function()
  countEquipmentByStatus(
    equipment: ObjectSet<Equipment>,
  ): FunctionsMap<string, Integer> {
    /**
     * Count equipment objects grouped by status (FMC, NMC, PMC, etc.).
     * Returns a map of status -> count.
     *
     * Called from Workshop aggregation widgets and OSDK analytics queries.
     * Runs server-side — efficient for large equipment populations.
     */
    const counts = new Map<string, number>();

    for (const equip of equipment) {
      const status = equip.equipmentStatus ?? "UNKNOWN";
      counts.set(status, (counts.get(status) ?? 0) + 1);
    }

    return counts;
  }

  @Function()
  computeFleetFmcRate(
    equipment: ObjectSet<Equipment>,
  ): Double {
    /**
     * Compute fleet-level FMC rate for a given equipment ObjectSet.
     * ObjectSet is pre-filtered by caller (e.g., by owning unit or type).
     *
     * Returns 0.0 for empty sets to avoid division-by-zero.
     */
    let total = 0;
    let fmcCount = 0;

    for (const equip of equipment) {
      total++;
      if (equip.equipmentStatus === "FMC") {
        fmcCount++;
      }
    }

    if (total === 0) return 0.0;
    return fmcCount / total;
  }
}
```

---

### 5-5. FOO Performance Patterns

**Critical rules for FOO performance:**

| Rule | Correct Pattern | Anti-Pattern |
|---|---|---|
| Avoid N+1 link traversal | Batch link loading where API supports it | Traversing links inside a loop over object population |
| Minimize property access | Access only needed properties | Reading all properties on every object |
| Return early | Exit on null/missing data immediately | Processing through null checks deep in nested logic |
| Use ObjectSet filters | Let Foundry pre-filter before FOO receives objects | Receiving full population and filtering in TypeScript |
| Stateless design | Compute from object state only | Caching or accumulating state across function calls |

**PROCEDURE — Performance-optimized bulk link aggregation (TypeScript):**

```typescript
import { Function, FunctionsMap, Integer } from "@foundry/functions-api";
import { Unit, Equipment, ObjectSet } from "@foundry/ontology-api";

export class UnitEquipmentFunctions {
  @Function()
  countNmcEquipmentPerUnit(
    units: ObjectSet<Unit>,
  ): FunctionsMap<Unit, Integer> {
    /**
     * For each unit in the set, count NMC equipment via the
     * UnitToEquipment link.
     *
     * Performance note: Uses bulk link loading via the ObjectSet API
     * rather than per-object traversal. Reduces round-trips.
     */
    const result = new Map<Unit, number>();

    for (const unit of units) {
      // Link traversal here is batched by the Foundry runtime
      // when iterating an ObjectSet — this is more efficient than
      // calling unit.unitToEquipment.get() in a separate loop
      const nmcCount = unit.unitToEquipment
        .filter((e) => e.equipmentStatus === "NMC")
        .count();

      result.set(unit, nmcCount);
    }

    return result;
  }
}
```

---

### 5-6. Testing FOO Functions

**CONDITIONS:** FOO function is implemented per Section 5-3 or 5-4. Jest test framework is configured in the repository. Mock object stubs can be constructed from known property values without Foundry connectivity.

**STANDARDS:** At least one test validates correct output for a known input. Edge cases covered: null/undefined properties, empty object sets, boundary values for numeric computations. Test coverage meets 80% line minimum per Section 8-4. Tests run locally without Foundry connectivity.

**EQUIPMENT:** TypeScript development environment; Jest configured; `@foundry/ontology-api` mock types.

**PROCEDURE — Unit test FOO functions (TypeScript, Jest):**

```typescript
import { ReadinessFunctions } from "../readiness/readinessScore";
import { UnitStatus } from "@foundry/ontology-api";

// Mock factory — create a minimal UnitStatus stub
function makeUnitStatusStub(
  personnelFillRate: number,
  equipmentFmcRate: number,
  maintenanceCurrentPct: number,
): UnitStatus {
  return {
    personnelFillRate,
    equipmentFmcRate,
    maintenanceCurrentPct,
  } as unknown as UnitStatus;
}

describe("ReadinessFunctions", () => {
  const fns = new ReadinessFunctions();

  describe("computeUnitReadinessScore", () => {
    test("returns 1.0 for fully capable unit", () => {
      const unit = makeUnitStatusStub(1.0, 1.0, 1.0);
      expect(fns.computeUnitReadinessScore(unit)).toBeCloseTo(1.0);
    });

    test("returns correct weighted composite score", () => {
      // 0.8 fill * 0.4 + 0.75 FMC * 0.4 + 0.9 maint * 0.2
      // = 0.32 + 0.30 + 0.18 = 0.80
      const unit = makeUnitStatusStub(0.8, 0.75, 0.9);
      expect(fns.computeUnitReadinessScore(unit)).toBeCloseTo(0.8);
    });

    test("returns 0.0 for fully degraded unit", () => {
      const unit = makeUnitStatusStub(0, 0, 0);
      expect(fns.computeUnitReadinessScore(unit)).toBeCloseTo(0.0);
    });

    test("clamps to 1.0 if properties exceed 1.0 (data anomaly)", () => {
      const unit = makeUnitStatusStub(1.5, 1.2, 1.1);
      expect(fns.computeUnitReadinessScore(unit)).toBeLessThanOrEqual(1.0);
    });
  });

  describe("computeReadinessRating", () => {
    test("assigns C1 for score >= 0.9", () => {
      const unit = makeUnitStatusStub(1.0, 1.0, 1.0);
      expect(fns.computeReadinessRating(unit)).toBe("C1");
    });

    test("assigns C4 for score < 0.5", () => {
      const unit = makeUnitStatusStub(0.2, 0.3, 0.1);
      expect(fns.computeReadinessRating(unit)).toBe("C4");
    });
  });
});
```

---

## CHAPTER 6 — ACTIONS WITH COMPLEX VALIDATION

### 6-1. Action Validation Architecture

**BLUF:** Actions in Foundry can include TypeScript validation functions that run before the Action executes. Complex validation logic, multi-step workflows, and conditional action flows require TypeScript — this is a TM-40L responsibility, not TM-30.

The three validation layers for complex Actions:

| Layer | Where | Who Writes | Purpose |
|---|---|---|---|
| Client-side (pre-submit) | External app or Workshop | -40L SWE | UX validation; catch obvious errors before API call |
| OSDK validation | Action parameter schema | Foundry runtime | Type enforcement; required fields |
| Server-side TypeScript validator | Foundry Function | -40L SWE | Business rules, cross-object validation, conditional logic |

> **NOTE:** Slate is Foundry's legacy application builder and is no longer the recommended path for new development. Use Workshop for internal Foundry applications, or OSDK-backed external applications for public-facing deployments. For client-side validation in new development, implement validation in your Workshop application or external OSDK application — not in a Slate app.

TypeScript server-side validators execute inside Foundry before the Action applies state changes. A validator returning an error prevents the Action from executing.

---

### 6-2. Writing TypeScript Action Validators

**CONDITIONS:** Action is defined in the Foundry Ontology by a -30 builder. Business rules for the Action are documented and reviewed by the responsible data steward. TypeScript FOO repository is configured per Section 5-2.

**STANDARDS:** Validation logic is separated from the Action function for testability. All business rules are enforced before the Action applies state changes. Throwing inside an `@ActionEditFunction` prevents execution. Unit test coverage meets 90% line minimum (validators are security-sensitive — higher bar per Section 8-4).

**EQUIPMENT:** TypeScript development environment; `@foundry/functions-api` and `@foundry/ontology-api` packages; Jest test framework; documented business rules from data steward.

**PROCEDURE — TypeScript Action validator for SITREP submission:**

```typescript
import {
  ActionEditFunction,
  ActionInput,
  BooleanType,
  StringType,
  Edits,
} from "@foundry/functions-api";
import { UnitStatus, Sitrep } from "@foundry/ontology-api";

interface SitrepValidationInput {
  unit: UnitStatus;
  readinessLevel: string;
  personnelStrength: number;
  equipmentReadinessPct: number;
  reportingOfficer: string;
  reportingDtg: string;
}

interface ValidationResult {
  valid: boolean;
  errors: string[];
}

// Pure validation function — no Foundry decorators needed
// Separate from the Action itself for testability
function validateSitrepInput(
  input: SitrepValidationInput,
  currentStatus: UnitStatus | null,
): ValidationResult {
  /**
   * Validate SITREP submission parameters against business rules.
   *
   * Rules enforced:
   * 1. C-rating string must be C1/C2/C3/C4
   * 2. Personnel strength must not exceed 110% of assigned
   * 3. Equipment readiness must be between 0.0 and 1.0
   * 4. Reporting DTG must not be more than 24h in the past
   * 5. Reporting officer must be non-empty
   * 6. Cannot submit a SITREP for a unit in DEACTIVATED status
   */
  const errors: string[] = [];

  // Rule 1: C-rating validation
  const validRatings = new Set(["C1", "C2", "C3", "C4"]);
  if (!validRatings.has(input.readinessLevel)) {
    errors.push(
      `Invalid readiness level '${input.readinessLevel}'. ` +
        `Must be C1, C2, C3, or C4.`,
    );
  }

  // Rule 2: Personnel strength ceiling
  const assignedStrength = currentStatus?.assignedStrength ?? 0;
  if (assignedStrength > 0 && input.personnelStrength > assignedStrength * 1.1) {
    errors.push(
      `Personnel strength ${input.personnelStrength} exceeds 110% of ` +
        `assigned strength ${assignedStrength}. Verify before submitting.`,
    );
  }

  // Rule 3: Equipment readiness bounds
  if (input.equipmentReadinessPct < 0 || input.equipmentReadinessPct > 1.0) {
    errors.push(
      `Equipment readiness ${input.equipmentReadinessPct} out of range [0.0, 1.0].`,
    );
  }

  // Rule 4: DTG recency check (no more than 24h stale)
  const reportDtg = new Date(input.reportingDtg);
  const now = new Date();
  const ageHours = (now.getTime() - reportDtg.getTime()) / (1000 * 60 * 60);
  if (ageHours > 24) {
    errors.push(
      `Reporting DTG is ${Math.round(ageHours)} hours old. ` +
        `SITREPs older than 24 hours require commander approval.`,
    );
  }

  // Rule 5: Reporting officer required
  if (!input.reportingOfficer || input.reportingOfficer.trim().length === 0) {
    errors.push("Reporting officer is required.");
  }

  // Rule 6: Unit status check
  if (currentStatus?.unitActivationStatus === "DEACTIVATED") {
    errors.push(
      `Unit is in DEACTIVATED status. SITREPs cannot be submitted for ` +
        `deactivated units. Contact G1 to update unit status.`,
    );
  }

  return { valid: errors.length === 0, errors };
}

// The Action function — registered with Foundry runtime
export class SitrepActionFunctions {
  @ActionEditFunction()
  submitSitrep(
    @ActionInput("unit") unit: UnitStatus,
    @ActionInput("readinessLevel") readinessLevel: string,
    @ActionInput("personnelStrength") personnelStrength: number,
    @ActionInput("equipmentReadinessPct") equipmentReadinessPct: number,
    @ActionInput("reportingOfficer") reportingOfficer: string,
    @ActionInput("reportingDtg") reportingDtg: string,
    @Edits(Sitrep) sitrep: Sitrep,
  ): void {
    const validation = validateSitrepInput(
      {
        unit,
        readinessLevel,
        personnelStrength,
        equipmentReadinessPct,
        reportingOfficer,
        reportingDtg,
      },
      unit, // Pass current unit status for cross-field validation
    );

    if (!validation.valid) {
      // Throwing in an ActionEditFunction prevents the action from applying
      throw new Error(
        `SITREP validation failed:\n${validation.errors.join("\n")}`,
      );
    }

    // Validation passed — apply edits to the Sitrep object
    sitrep.unit = unit;
    sitrep.readinessLevel = readinessLevel;
    sitrep.personnelStrength = personnelStrength;
    sitrep.equipmentReadinessPct = equipmentReadinessPct;
    sitrep.reportingOfficer = reportingOfficer;
    sitrep.reportingDtg = reportingDtg;
    sitrep.submittedAtUtc = new Date().toISOString();
    sitrep.status = "SUBMITTED";
  }
}
```

---

### 6-3. Multi-Step Action Flows

**BLUF:** Multi-step Actions with conditional paths (e.g., submit → route for review → approve/reject) require a state machine pattern in TypeScript. Design the state machine explicitly — do not encode state in property naming conventions.

**CONDITIONS:** All state transitions and business rules are documented before implementation. Action definitions for each transition step are configured in the Foundry Ontology. Object Types for the primary entity and any audit/review records are defined.

**STANDARDS:** State machine transitions are defined explicitly as a constant — no ad hoc transition logic embedded in conditional branches. Invalid transitions throw before any edits are applied. Audit record is created for every state change. Unit tests cover all valid transitions and all invalid transition attempts.

**EQUIPMENT:** TypeScript development environment; `@foundry/functions-api` and `@foundry/ontology-api` packages; state machine design document; Jest test framework.

**PROCEDURE — Multi-step EXORD processing action (TypeScript):**

```typescript
import {
  ActionEditFunction,
  ActionInput,
  Edits,
} from "@foundry/functions-api";
import { Exord, ExordReview } from "@foundry/ontology-api";

// Explicit state machine — all valid states and transitions defined here
type ExordStatus =
  | "DRAFT"
  | "SUBMITTED"
  | "UNDER_REVIEW"
  | "APPROVED"
  | "REJECTED"
  | "PUBLISHED";

const VALID_TRANSITIONS: Record<ExordStatus, ExordStatus[]> = {
  DRAFT: ["SUBMITTED"],
  SUBMITTED: ["UNDER_REVIEW"],
  UNDER_REVIEW: ["APPROVED", "REJECTED"],
  APPROVED: ["PUBLISHED"],
  REJECTED: ["DRAFT"], // Allow re-draft after rejection
  PUBLISHED: [], // Terminal state — no further transitions
};

function assertValidTransition(
  current: ExordStatus,
  next: ExordStatus,
): void {
  const allowed = VALID_TRANSITIONS[current] ?? [];
  if (!allowed.includes(next)) {
    throw new Error(
      `Invalid EXORD status transition: ${current} -> ${next}. ` +
        `Allowed transitions from ${current}: [${allowed.join(", ")}]`,
    );
  }
}

export class ExordActionFunctions {
  @ActionEditFunction()
  advanceExordStatus(
    @ActionInput("exord") exord: Exord,
    @ActionInput("targetStatus") targetStatus: string,
    @ActionInput("reviewerComment") reviewerComment: string,
    @ActionInput("reviewerName") reviewerName: string,
    @Edits(Exord) exordEdit: Exord,
    @Edits(ExordReview) review: ExordReview,
  ): void {
    const currentStatus = (exord.status ?? "DRAFT") as ExordStatus;
    const nextStatus = targetStatus as ExordStatus;

    // Validate transition — throws if invalid
    assertValidTransition(currentStatus, nextStatus);

    // Business rule: APPROVED requires a reviewer comment
    if (nextStatus === "APPROVED" && !reviewerComment?.trim()) {
      throw new Error(
        "Reviewer comment is required when approving an EXORD.",
      );
    }

    // Business rule: REJECTED requires a reviewer comment
    if (nextStatus === "REJECTED" && !reviewerComment?.trim()) {
      throw new Error(
        "Reviewer comment is required when rejecting an EXORD.",
      );
    }

    // Apply state transition
    exordEdit.status = nextStatus;
    exordEdit.lastModifiedUtc = new Date().toISOString();

    // Create review record for audit trail
    review.exord = exord;
    review.fromStatus = currentStatus;
    review.toStatus = nextStatus;
    review.reviewerName = reviewerName;
    review.reviewerComment = reviewerComment ?? "";
    review.reviewTimestampUtc = new Date().toISOString();
  }
}
```

---

## CHAPTER 7 — SLATE APPLICATIONS (LEGACY)

> **CAUTION:** Slate is a legacy application builder. Do not use Slate for new development. Use Workshop for internal Foundry applications. For public-facing portals, build an external application using the OSDK or Platform SDK.

### 7-1. What Is Slate

**BLUF:** Slate is a legacy Foundry-hosted environment for building custom HTML/CSS/JavaScript applications. This chapter is retained for maintenance of existing Slate applications only. All new application development must use Workshop (for internal Foundry users) or OSDK-backed external applications (for users without Foundry access or public-facing portals).

> **CAUTION:** Slate is a legacy application builder. Do not use Slate for new development. Use Workshop for internal Foundry applications. For public-facing portals, build an external application using the OSDK or Platform SDK.

Slate applications (legacy characteristics):
- Run inside the Foundry UI frame (same auth session as the user)
- Can call Foundry APIs including the OSDK, dataset query endpoints, and ontology endpoints
- Support full HTML5/CSS3/JavaScript including modern frameworks (React, Vue if bundled)
- Are deployed and version-controlled as Foundry code resources
- Inherit the user's CBAC permissions — they cannot access data the user cannot see

**Application type selection — current guidance:**

| Requirement | Current Approved Tool | Notes |
|---|---|---|
| Internal application for Foundry users | Workshop | No-code/low-code; see TM-20 and TM-30 |
| Public-facing portal or app for non-Foundry users | External application backed by OSDK or Platform SDK | Hosted on external infrastructure with proper authentication (OAuth2, service account) |
| Existing Slate app (maintenance only) | Slate | Do not extend Slate apps; plan migration to Workshop or OSDK external app |

**DEPRECATED — When to use Slate vs. external application (archived reference for existing apps):**

| Factor | Slate (LEGACY) | External Application (CURRENT) |
|---|---|---|
| Auth model | Inherits user's Foundry session — no separate auth | Requires separate credential management (service account or OAuth) |
| Deployment | Hosted within Foundry — no external infrastructure | Requires external hosting (on-prem server, container) |
| Access | Users must have Foundry access | Can serve users without Foundry accounts |
| CBAC | Enforced automatically by Foundry session | Must be implemented explicitly in application |
| Integration | Direct Foundry API access | OSDK / Platform SDK over HTTPS |

---

### 7-2. Slate Application Structure

> **CAUTION:** Slate is a legacy application builder. Do not use Slate for new development. Use Workshop for internal Foundry applications. For public-facing portals, build an external application using the OSDK or Platform SDK.

**Standard Slate project structure (maintenance reference only):**

```
my-slate-app/
├── index.html              # Entry point — rendered by Foundry Slate runtime
├── styles/
│   └── main.css
├── scripts/
│   ├── main.js             # Application entry
│   ├── api.js              # Foundry API abstraction layer
│   ├── components/
│   │   ├── readinessDashboard.js
│   │   └── sitrepForm.js
│   └── utils/
│       ├── dtgFormatter.js
│       └── ratingColors.js
├── assets/
│   └── usareur_seal.png
└── foundry.json
```

---

### 7-3. Foundry API Integration from Slate

> **CAUTION:** Slate is a legacy application builder. Do not use Slate for new development. Use Workshop for internal Foundry applications. For public-facing portals, build an external application using the OSDK or Platform SDK.

**CONDITIONS:** Existing Slate application is in maintenance (not new development). Foundry Slate runtime is accessible. `window.foundryContext` is populated by the Slate runtime with base URL and auth token. Target Object Type is accessible to the authenticated user.

**STANDARDS:** Auth tokens are used only in JavaScript scope — never rendered in HTML or logged. All user inputs are sanitized before inclusion in API filter parameters. Error messages exposed to users do not contain raw API error details or schema information.

**EQUIPMENT:** Existing Slate application codebase; Foundry development environment; browser developer tools for local debugging.

**PROCEDURE — Query Ontology objects from Slate JavaScript (maintenance reference only):**

```javascript
// api.js — Foundry API abstraction for Slate application

/**
 * Query UnitStatus objects filtered by AOR.
 * Uses the Foundry Slate context API for auth — no separate credentials needed.
 *
 * @param {string} aorFilter - AOR code string (e.g., "EUROPE-NORTH")
 * @returns {Promise<Array>} Array of unit status objects
 */
async function getUnitStatusByAor(aorFilter) {
  // Slate context provides the base URL and auth headers automatically
  const ontologyApiBase = `${window.foundryContext.baseUrl}/api/v1/ontologies`;
  const ontologyRid = window.foundryContext.ontologyRid;

  const response = await fetch(
    `${ontologyApiBase}/${ontologyRid}/objects/UnitStatus` +
      `?filter=${encodeURIComponent(
        JSON.stringify({
          type: "eq",
          field: "aorCode",
          value: aorFilter,
        }),
      )}&pageSize=100`,
    {
      method: "GET",
      headers: {
        Authorization: `Bearer ${window.foundryContext.authToken}`,
        "Content-Type": "application/json",
      },
    },
  );

  if (!response.ok) {
    throw new Error(
      `UnitStatus query failed: ${response.status} ${response.statusText}`,
    );
  }

  const data = await response.json();
  return data.data ?? [];
}

/**
 * Execute a SubmitSitrep Action from Slate.
 * Uses user's session token — Action enforces CBAC for the current user.
 *
 * @param {Object} params - SITREP parameters
 * @returns {Promise<void>}
 */
async function submitSitrepAction(params) {
  const ontologyApiBase = `${window.foundryContext.baseUrl}/api/v1/ontologies`;
  const ontologyRid = window.foundryContext.ontologyRid;

  const response = await fetch(
    `${ontologyApiBase}/${ontologyRid}/actions/SubmitSitrep/apply`,
    {
      method: "POST",
      headers: {
        Authorization: `Bearer ${window.foundryContext.authToken}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        parameters: {
          unit: { objectTypeApiName: "UnitStatus", primaryKey: params.unitRid },
          readinessLevel: params.readinessLevel,
          personnelStrength: params.personnelStrength,
          equipmentReadinessPct: params.equipmentReadinessPct,
          reportingOfficer: params.reportingOfficer,
          reportingDtg: params.reportingDtg,
        },
      }),
    },
  );

  if (!response.ok) {
    const errorBody = await response.json().catch(() => ({}));
    throw new Error(
      `SubmitSitrep action failed: ${response.status} — ` +
        `${errorBody.errorCode ?? "Unknown error"}: ${errorBody.message ?? ""}`,
    );
  }
}

export { getUnitStatusByAor, submitSitrepAction };
```

---

### 7-4. Slate Security Model

> **CAUTION:** Slate is a legacy application builder. Do not use Slate for new development. Use Workshop for internal Foundry applications. For public-facing portals, build an external application using the OSDK or Platform SDK.

**Critical security requirements for Slate applications (maintenance reference only):**

| Requirement | Implementation | Notes |
|---|---|---|
| Never expose auth tokens in DOM | Use `window.foundryContext.authToken` only in JS scope | Do not render tokens in HTML elements or log them |
| Validate all user inputs | Sanitize before including in API requests | Prevent injection into filter parameters |
| Error messages must not leak schema | Catch API errors and display safe user-facing messages | Do not render raw API error responses |
| Content Security Policy | Set CSP headers in Slate app configuration | Prevents XSS; required for all Slate apps in production |
| No external fetch from Slate | All API calls target the same Foundry origin | External fetch is blocked by CSP; do not attempt to circumvent |

**PROCEDURE — Secure input sanitization for Slate filter params:**

```javascript
/**
 * Sanitize user-provided filter string for use in Foundry API filter parameter.
 * Prevents injection through encoded or special-character filter strings.
 *
 * @param {string} input - Raw user input
 * @param {number} maxLength - Maximum allowed length
 * @returns {string} Sanitized string safe for filter use
 */
function sanitizeFilterInput(input, maxLength = 50) {
  if (typeof input !== "string") {
    throw new TypeError("Filter input must be a string");
  }

  // Strip characters not allowed in filter values (alphanumeric, hyphen, underscore, space)
  const sanitized = input.replace(/[^a-zA-Z0-9\-_ ]/g, "").trim();

  if (sanitized.length === 0) {
    throw new Error("Filter input is empty after sanitization");
  }

  if (sanitized.length > maxLength) {
    throw new Error(
      `Filter input too long: ${sanitized.length} chars (max ${maxLength})`,
    );
  }

  return sanitized;
}
```

---

## CHAPTER 8 — CI/CD AND CODE REPOSITORY DISCIPLINE

### 8-1. Repository Structure for Foundry Code Resources

**BLUF:** Foundry code resources — TypeScript FOO functions, Action validators, Slate apps — are developed in Git repositories with the same engineering discipline as any production software system. No code deploys to production outside of the approved CI/CD workflow.

**Standard repository layout for a Foundry code resource project:**

```
my-foundry-project/
├── .github/
│   └── workflows/
│       ├── ci.yml              # Lint, type-check, unit test on PR
│       └── promote.yml         # Branch promotion to Foundry on merge
├── src/
│   ├── functions/              # TypeScript FOO and Action functions
│   ├── slate/                  # Slate application code
│   └── tests/                  # All tests co-located with source
├── scripts/
│   ├── deploy_dev.sh           # Deploy to Foundry dev branch
│   └── promote_prod.sh         # Promote Foundry branch to production (gated)
├── .env.example                # Template — never commit .env
├── .gitignore                  # Must include .env, node_modules, dist/
├── foundry.json                # Foundry project configuration
├── package.json
├── tsconfig.json
└── README.md
```

> **CAUTION: `.env` files containing tokens must be in `.gitignore` before the repository's first commit. Retroactive removal from Git history does not invalidate the exposed credential — rotate the token immediately if committed. Report to unit S6/G6.**

---

### 8-2. Foundry Branch Workflow

**Standard branch strategy for Foundry code resources:**

```
main (production)
  |
  +-- develop (integration)
        |
        +-- feature/TASK-123-readiness-score-foo
        +-- feature/TASK-124-sitrep-validator
        +-- fix/TASK-125-pagination-bug
```

**Branch protection rules (configure in GitHub/GitLab and Foundry):**

| Branch | Required Reviews | Required Checks | Push Direct? |
|---|---|---|---|
| `main` (production) | 2 (tech lead + C2DAO rep) | All CI checks pass | No |
| `develop` (integration) | 1 (peer review) | Lint + unit tests pass | No |
| `feature/*` | 0 (WIP) | None (developer discretion) | Yes (developer) |
| `fix/*` | 1 (peer review) | Lint + unit tests pass | No |

**Foundry-side branch workflow mirrors Git workflow:**

```
Foundry: develop branch  <-->  Git: develop branch
Foundry: master branch   <-->  Git: main branch
```

All Foundry code resource changes go to the `develop` branch first. Promotion to `master` (production) requires the Git `main` branch merge AND a Foundry branch review/merge through the Foundry UI or Foundry CI integration.

---

### 8-3. CI/CD Pipeline Configuration

**CONDITIONS:** Git repository is configured with branch protection rules per Section 8-2. GitHub Actions (or equivalent CI system) is available for the repository. ESLint, TypeScript, and Jest are configured in `package.json`.

**STANDARDS:** CI runs on every pull request targeting `develop` or `main`. Lint, type-check, and unit test steps are all required to pass before merge is permitted. Secret scanning step is included to catch committed credentials. Coverage threshold is enforced (80% line minimum for unit tests).

**EQUIPMENT:** GitHub Actions; Node.js 20; `package.json` with `lint`, `type-check`, and `test` scripts configured; `.gitignore` with `.env` listed.

**PROCEDURE — Configure GitHub Actions CI pipeline:**

```yaml
# .github/workflows/ci.yml
name: CI — Lint, Type Check, Test

on:
  pull_request:
    branches: [develop, main]
  push:
    branches: [develop]

jobs:
  ci:
    runs-on: ubuntu-latest
    timeout-minutes: 15

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: "npm"

      - name: Install dependencies
        run: npm ci

      - name: Lint
        run: npm run lint
        # ESLint with @typescript-eslint — no errors allowed on PR

      - name: Type check
        run: npm run type-check
        # tsc --noEmit — type errors block merge

      - name: Unit tests
        run: npm run test -- --coverage --coverageThreshold='{"global":{"lines":80}}'
        # 80% line coverage minimum — enforced as merge gate
        env:
          CI: true

      - name: Check for committed secrets
        run: |
          # Fail if .env files or token patterns appear in committed files
          if git diff HEAD~1 --name-only | xargs grep -lE \
            'FOUNDRY_TOKEN|_SECRET|_PASSWORD|Bearer [a-zA-Z0-9]{20,}' \
            2>/dev/null; then
            echo "ERROR: Potential credential committed. Review and rotate."
            exit 1
          fi
```

---

### 8-4. Automated Testing Requirements

**Testing requirements by code resource type:**

| Resource Type | Required Test Types | Coverage Minimum | Notes |
|---|---|---|---|
| FOO functions | Unit tests | 80% line | Test all edge cases including null/missing properties |
| Action validators | Unit tests | 90% line | Validators are security-sensitive — higher bar |
| Slate JS | Unit tests for business logic | 70% line | DOM-dependent code tested via jsdom |
| Python pipelines | Unit + integration | 80% line | Integration tests run against Foundry dev branch |
| OSDK clients | Unit tests with mocks | 75% line | Mock OSDK client — do not test against production |

**PROCEDURE — Mock the OSDK client for unit tests (TypeScript):**

```typescript
// tests/mocks/osdkClientMock.ts
import { vi } from "vitest";

/**
 * Create a mock OSDK client for unit testing.
 * Prevents any actual calls to MSS during test runs.
 *
 * Usage:
 *   const mockClient = createMockOsdkClient({ unitStatusData: [...] });
 *   const result = await getUnitStatusRecords(mockClient, "W12345");
 */
export function createMockOsdkClient(fixtures: {
  unitStatusData?: Record<string, unknown>[];
}) {
  return {
    ontology: {
      objects: {
        UnitStatus: {
          filter: vi.fn().mockReturnValue({
            asyncIter: async function* () {
              for (const record of fixtures.unitStatusData ?? []) {
                yield record;
              }
            },
          }),
        },
      },
      actions: {
        SubmitSitrep: {
          apply: vi.fn().mockResolvedValue({ type: "SUCCESS" }),
        },
      },
    },
  };
}
```

---

### 8-5. Branch Promotion Workflow

**CONDITIONS:** All CI checks pass on the Git `develop` branch. Integration tests have been run against the Foundry dev environment. Peer review is complete. For Ontology or dataset changes, C2DAO data steward coordination is scheduled.

**STANDARDS:** All seven promotion steps are completed in sequence. No step is bypassed, including C2DAO review for schema/CBAC/marking changes. Post-promotion smoke test is executed within 30 minutes. Promotion is documented in the unit data ops log.

**EQUIPMENT:** Git repository access (`develop` and `main` branches); Foundry UI access for branch management; C2DAO ticketing system access; operations log.

**PROCEDURE — Promote Foundry develop branch to master (production):**

```
STEP 1: Verify CI passes on Git develop branch
  - All lint, type-check, and unit tests green
  - No open critical findings in code review

STEP 2: Conduct integration test against Foundry develop branch
  - Deploy code to Foundry develop branch (automated or manual)
  - Run integration test suite against Foundry dev environment
  - Verify all FOO functions and Action validators execute correctly
  - Spot-check at least three real Ontology objects

STEP 3: Peer review in Foundry code repository (UI)
  - Open branch review in Foundry repository viewer
  - Reviewer must be a different engineer than the author
  - Reviewer confirms: no hardcoded credentials, no debug logging of object data

STEP 4: Merge Git develop -> main (requires 2 approvals per branch rules)

STEP 5: C2DAO data steward review (for any changes affecting production datasets or Ontology)
  - Submit Foundry branch merge request via C2DAO ticketing system
  - C2DAO confirms: CBAC settings unchanged, no marking changes, UDRA alignment intact

STEP 6: Foundry develop -> master branch promotion (Foundry UI)
  - Performed only after Steps 1-5 complete
  - Promotes all code resources, FOO functions, and Action validators atomically
  - Monitor for 30 minutes post-promotion: check application health, query latency

STEP 7: Post-promotion verification
  - Execute smoke test suite against production
  - Confirm readiness dashboard loads and displays correct data
  - Confirm SubmitSitrep action executes end-to-end
  - Document promotion in unit data ops log
```

> **WARNING: Never bypass the C2DAO review step (Step 5) for promotions that modify Ontology schemas, CBAC assignments, or data markings. These changes affect every user and downstream system. Unauthorized schema changes in production are a reportable incident.**

---

## CHAPTER 9 — SECURITY AND COMPLIANCE

### 9-1. CBAC in External Applications

**BLUF:** Context-Based Access Control (CBAC) in Foundry ensures users only see data they are authorized to access. External applications consuming MSS via OSDK must preserve this access control — they must not aggregate, cache, or expose data beyond the authorization of the requesting user.

**Core CBAC rules for external application developers:**

| Rule | Requirement | Violation Example |
|---|---|---|
| No elevation | Service account cannot grant end users access beyond their Foundry permissions | App queries OSDK as service account and returns full object set to any web user |
| No caching beyond session | Cached OSDK responses expire with user session | Caching sensitive operational data in shared Redis without TTL |
| No aggregation bypass | Aggregate only over objects the user can see | Computing fleet-wide readiness from objects filtered to user's authorization |
| Audit log preservation | Application-level audit log must capture who queried what | Missing logging on sensitive object access |
| Marking propagation | If source object is marked CUI, display must indicate marking | Stripping CUI markings in report output |

---

### 9-2. Credential Management

**CONDITIONS:** External application requires authenticated access to MSS OSDK or Platform SDK. C2DAO has provisioned the appropriate credential type. AR 25-2 requirements are understood and being applied.

**STANDARDS:** All credentials are stored in approved storage patterns (preference order listed below). No credentials appear in source code, Dockerfile, docker-compose, log files, or version control history. Token rotation schedule is documented and executed.

**EQUIPMENT:** C2DAO-provisioned credentials; approved secrets manager (CI/CD secrets vault or Army-approved HashiCorp Vault); `.env` file (local dev only, in `.gitignore`); unit security log.

**PROCEDURE — Credential management for deployed external applications:**

```
APPROVED credential storage patterns (in order of preference):

1. Foundry OAuth2 Confidential Client (server-side token exchange)
   - Best for web applications with a server component
   - Token stays server-side; never exposed to browser
   - C2DAO provisions client_id and client_secret

2. Environment variable injection (CI/CD secrets)
   - Service account token stored in CI/CD secrets vault
   - Injected at deploy time as environment variable
   - Never appears in source code or container image

3. Army-approved secrets manager
   - HashiCorp Vault or equivalent approved by G6
   - Application reads secret at startup from secrets API
   - Requires AR 25-2 compliant implementation

NOT APPROVED:

- Hardcoded tokens in source code
- Tokens in Dockerfile or docker-compose.yml
- Tokens in configuration files committed to version control
- Tokens in log files or debug output
- Tokens shared over NIPR email
```

**PROCEDURE — Token rotation discipline:**

```
Token rotation schedule (align with AR 25-2 and local G6 guidance):

- Service account tokens: rotate every 90 days minimum
- PATs (developer use only): rotate every 30 days
- OAuth2 client secrets: rotate every 180 days minimum

Rotation procedure:
1. Provision new credential through C2DAO process
2. Update secrets manager / CI/CD secrets vault with new value
3. Redeploy application to pick up new credential
4. Verify application functions correctly with new credential
5. Revoke old credential in Foundry token management
6. Document rotation in unit security log
```

---

### 9-3. Marking Compliance in OSDK Queries

**BLUF:** Foundry data markings (CUI, FOUO, coalition restrictions) are enforced at the OSDK layer. However, your application is responsible for propagating these markings in display and output.

**CONDITIONS:** External application retrieves OSDK objects that may carry data markings (CUI, FOUO, coalition restrictions). Application presents data to end users in a UI or report output.

**STANDARDS:** Markings are extracted from every OSDK object response. Highest marking in a result set is determined and displayed as a page/section banner. No marking is stripped before display. CUI data displayed without markings constitutes a spillage event.

**EQUIPMENT:** Authenticated OSDK Python client; UI or report output layer; knowledge of applicable marking categories (CUI, FOUO, REL TO USA/NATO).

**PROCEDURE — Check and propagate markings (Python):**

```python
from dataclasses import dataclass, field
from enum import Enum

class DataMarking(Enum):
    UNCLASSIFIED = "U"
    FOUO = "FOUO"
    CUI = "CUI"
    CUI_REL_NATO = "CUI//REL TO USA, NATO"

@dataclass
class MarkedObject:
    """Wrapper for OSDK object with marking metadata preserved."""
    rid: str
    properties: dict
    markings: list[str] = field(default_factory=list)
    highest_marking: DataMarking = DataMarking.UNCLASSIFIED

def extract_object_with_markings(osdk_object) -> MarkedObject:
    """
    Extract object properties and markings from an OSDK object.
    Markings must be preserved — do not strip or ignore them.

    Applications displaying this data must show the appropriate
    marking banner based on highest_marking.
    """
    markings = [
        m.get("displayName", "")
        for m in (osdk_object.markings or [])
    ]

    # Determine highest marking level for display banner
    highest = DataMarking.UNCLASSIFIED
    if any("REL TO" in m or "NATO" in m for m in markings):
        highest = DataMarking.CUI_REL_NATO
    elif any("CUI" in m for m in markings):
        highest = DataMarking.CUI
    elif any("FOUO" in m for m in markings):
        highest = DataMarking.FOUO

    return MarkedObject(
        rid=osdk_object.rid,
        properties={
            k: v for k, v in osdk_object.properties.items()
        },
        markings=markings,
        highest_marking=highest,
    )

def format_display_banner(marking: DataMarking) -> str:
    """Return the correct classification banner for UI display."""
    banners = {
        DataMarking.UNCLASSIFIED: "UNCLASSIFIED",
        DataMarking.FOUO: "UNCLASSIFIED // FOR OFFICIAL USE ONLY",
        DataMarking.CUI: "CONTROLLED UNCLASSIFIED INFORMATION",
        DataMarking.CUI_REL_NATO:
            "CONTROLLED UNCLASSIFIED INFORMATION // REL TO USA, NATO",
    }
    return banners[marking]
```

> **WARNING: Applications that strip or do not display data markings are in violation of Army data handling policy (Army CIO Data Stewardship Policy, April 2024) and AR 25-2. CUI data displayed without markings constitutes a spillage event. Report to unit S2/S6 immediately.**

---

### 9-4. Audit Trail Requirements

**CONDITIONS:** External application executes OSDK queries or Action calls against sensitive Object Types. C2DAO has identified which Object Types require audit logging. Approved log destination is configured (SIEM, approved log aggregator, or local audit log file for dev).

**STANDARDS:** Every query against a sensitive Object Type is logged with user_id, object_type, filter parameters, and result count. Every Action execution is logged with user_id, action name, target RID, and success/failure. Object property values are NOT logged in audit records. Audit log is separate from application log.

**EQUIPMENT:** Python `logging` module; approved log destination (file or SIEM); C2DAO list of Object Types requiring audit logging.

**PROCEDURE — Application-level audit logging (Python):**

```python
import logging
import json
from datetime import datetime, timezone
from typing import Any

# Configure audit logger — write to separate audit log file, not application log
audit_logger = logging.getLogger("audit")
audit_logger.setLevel(logging.INFO)

# Audit log handler — write to approved log destination
# In production: configure to write to SIEM or approved log aggregator
audit_handler = logging.FileHandler("/var/log/mss_app/audit.log")
audit_handler.setFormatter(
    logging.Formatter("%(asctime)s %(message)s")
)
audit_logger.addHandler(audit_handler)

def audit_log_query(
    user_id: str,
    object_type: str,
    filter_params: dict[str, Any],
    result_count: int,
    application_name: str,
) -> None:
    """
    Log an OSDK query to the audit trail.

    Required for all queries against sensitive Object Types.
    Consult C2DAO for the list of Object Types requiring audit logging.

    DO NOT log object property values in the audit record —
    log only the query parameters and result count.
    """
    record = {
        "event": "OSDK_QUERY",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "user_id": user_id,
        "application": application_name,
        "object_type": object_type,
        "filter_params": filter_params,   # Query params only — no property values
        "result_count": result_count,
    }
    audit_logger.info(json.dumps(record))


def audit_log_action(
    user_id: str,
    action_name: str,
    target_object_rid: str,
    success: bool,
    error_message: str | None,
    application_name: str,
) -> None:
    """
    Log an Action execution to the audit trail.
    Required for all Action executions in external applications.
    """
    record = {
        "event": "OSDK_ACTION",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "user_id": user_id,
        "application": application_name,
        "action_name": action_name,
        "target_rid": target_object_rid,
        "success": success,
        "error_message": error_message,
    }
    audit_logger.info(json.dumps(record))
```

---

### 9-5. Integration Security — REST APIs and Webhooks

**CONDITIONS:** External application exposes an inbound webhook endpoint or calls outbound REST APIs. HMAC shared secret is provisioned through C2DAO-approved credential store. TLS certificates are in place on all endpoints.

**STANDARDS:** All inbound webhook payloads are signature-verified before processing. Timestamp check enforces maximum request age (default 5 minutes) to prevent replay attacks. All outbound HTTP calls enforce connect and read timeouts. Rate limiting is implemented. Egress is restricted to approved MSS endpoints.

**EQUIPMENT:** Inbound webhook endpoint with HTTPS; HMAC shared secret in environment variable; Python `hmac` and `hashlib` modules; approved firewall egress configuration from G6.

**Security requirements for REST/webhook integrations:**

| Requirement | Standard | Notes |
|---|---|---|
| TLS 1.2+ required | All HTTP communication over TLS 1.2 minimum | TLS 1.3 preferred for new integrations |
| Webhook signature verification | Verify HMAC signature on all inbound webhooks | Reject requests with invalid or missing signatures |
| Input validation at boundary | Validate all inbound data against expected schema | Do not trust inbound JSON field types |
| Rate limiting | Implement rate limiting on integration endpoints | Prevents abuse; coordinate with C2DAO for approved limits |
| Timeout enforcement | Set connect and read timeouts on all outbound calls | Prevent hung connections from blocking application threads |
| Allowlist egress | Restrict outbound connections to approved MSS endpoints | Implemented at firewall level; verify with G6 |

**PROCEDURE — Webhook signature verification (Python):**

```python
import hmac
import hashlib
import time

def verify_webhook_signature(
    payload_bytes: bytes,
    signature_header: str,
    secret: str,
    timestamp_header: str,
    max_age_seconds: int = 300,
) -> bool:
    """
    Verify HMAC-SHA256 signature on an inbound webhook payload.

    Rejects requests where:
    - Signature does not match (tampered payload or wrong secret)
    - Timestamp is older than max_age_seconds (replay attack prevention)

    Args:
        payload_bytes:    Raw request body bytes
        signature_header: X-Foundry-Signature header value
        secret:           Shared HMAC secret (from environment variable)
        timestamp_header: X-Foundry-Timestamp header value
        max_age_seconds:  Max acceptable age of request (default 5 min)

    Returns:
        True if valid; False if invalid (do not process payload if False)
    """
    # Replay attack check — reject stale requests
    try:
        request_timestamp = int(timestamp_header)
    except (ValueError, TypeError):
        return False

    age = int(time.time()) - request_timestamp
    if age > max_age_seconds or age < 0:
        return False

    # Compute expected signature: HMAC-SHA256(timestamp + "." + body)
    message = f"{timestamp_header}.".encode() + payload_bytes
    expected_signature = hmac.new(
        secret.encode(),
        message,
        hashlib.sha256,
    ).hexdigest()

    # Constant-time comparison — prevents timing attacks
    return hmac.compare_digest(
        f"sha256={expected_signature}",
        signature_header,
    )
```

---

## APPENDIX A — OSDK QUICK REFERENCE

### A-1. Python OSDK Common Patterns

| Operation | Pattern | Notes |
|---|---|---|
| List objects (filtered) | `client.ontology.objects["Type"].filter({...}).take(N)` | Always set explicit limit |
| Get single object by key | `client.ontology.objects["Type"].get(primary_key)` | Raises if not found |
| Execute action | `client.ontology.actions["ActionName"].apply(**params)` | Validate params before calling |
| Traverse link | `obj.links["LinkName"].get_linked_objects()` | Paginate if link has many children |
| Paginated list | `page = ...list(pageSize=N); page.next_page_token` | Loop until next_page_token is None |
| Subscribe to changes | OSDK subscriptions — use TypeScript SDK for subscriptions | Python subscription support varies by SDK version |

### A-2. TypeScript OSDK Common Patterns

| Operation | Pattern | Notes |
|---|---|---|
| Iterate all matching objects | `for await (const obj of client(Type).where(...).asyncIter())` | Handles pagination automatically |
| Fetch single object | `await client(Type).fetchOne(primaryKey)` | Throws if not found |
| Execute action | `await client(Action).applyAction({...})` | Return value varies by action type |
| Subscribe | `client(Type).where(...).subscribe({onChange, onError})` | Returns unsubscribe function |
| Compound filter | `.where({ $and: [Type.prop.eq(v1), Type.prop2.lt(v2)] })` | $and and $or supported |

### A-3. OSDK Error Codes

| Error Code | Meaning | Action |
|---|---|---|
| 400 Bad Request | Invalid filter, bad parameter format | Check query parameters and object type schema |
| 401 Unauthorized | Token expired or invalid | Rotate token; check FOUNDRY_TOKEN env var |
| 403 Forbidden | No CBAC access to object type | Contact data steward; verify enrollment scope |
| 404 Not Found | Object type or object does not exist | Verify object type API name; check enrollment |
| 429 Too Many Requests | Rate limit exceeded | Implement exponential backoff; reduce query frequency |
| 503 Service Unavailable | MSS platform degraded | Retry with backoff; check MSS status page |

---

## APPENDIX B — SWE SECURITY CHECKLIST

Complete this checklist before any code promotion to production. Document completion in the unit data ops log.

### B-1. Credential Hygiene

- [ ] No credentials, tokens, or passwords in any file committed to version control
- [ ] `.env` and any credential files are in `.gitignore`
- [ ] Service account credentials loaded from environment variables or approved secrets manager
- [ ] PATs are not used in deployed applications (developer use only)
- [ ] Token rotation schedule is documented and scheduled

### B-2. CBAC and Authorization

- [ ] External application does not elevate user permissions beyond their Foundry CBAC
- [ ] Service account queries are scoped to the minimum required Object Types
- [ ] OSDK application enrollment includes only Object Types and Actions needed (no overage)
- [ ] Application has been reviewed by C2DAO for CBAC compliance before go-live

### B-3. Data Handling

- [ ] OSDK query results are not cached beyond the user's session scope
- [ ] Data markings (CUI, FOUO, coalition) are displayed in application UI
- [ ] Application audit log captures all queries and action executions against sensitive objects
- [ ] No operational data in application debug logs or error messages exposed to end users

### B-4. Input Validation

- [ ] All user-supplied inputs are validated and sanitized before use in API queries
- [ ] Inbound webhook payloads are signature-verified before processing
- [ ] Application enforces timeout on all outbound HTTP calls

### B-5. CI/CD and Code Quality

- [ ] All unit tests pass in CI pipeline
- [ ] Code coverage meets minimums (validators ≥90%, FOO ≥80%, other ≥75%)
- [ ] No outstanding lint or type-check errors
- [ ] Peer review completed by engineer other than author
- [ ] C2DAO data steward review completed (for Ontology or dataset changes)

### B-6. Post-Deployment

- [ ] Smoke test executed against production after promotion
- [ ] No new errors in application logs within 30 minutes of deployment
- [ ] Readiness dashboards and SITREP functions verified end-to-end
- [ ] Rollback plan documented and communicated to team

---

## APPENDIX C — INTEGRATION PATTERNS REFERENCE

### C-1. Pattern: SITREP Automation Service

**Use case:** Automated SITREP generation — reads Unit objects from MSS Ontology, formats reports, pushes to EUCOM J3 portal.

**Architecture:**
```
EUCOM J3 Portal <-- SITREP Service --> MSS (OSDK)
                      |
                   Scheduler
                   (cron / task queue)
```

**Key implementation decisions:**
- Auth: Service account token (server-to-server, no user session needed)
- Trigger: Scheduled task every 6 hours OR subscription-triggered on UnitStatus change
- Output: Formatted report (PDF or JSON) pushed to external system REST API
- Error handling: Dead letter queue for failed submissions; alert to operations team
- CBAC: Service account scoped to read UnitStatus objects only; write to external system only

### C-2. Pattern: Readiness Dashboard (External)

**Use case:** V Corps readiness dashboard served to users who do not access Foundry directly.

**Architecture:**
```
Browser --> React Frontend --> Node.js BFF --> MSS (OSDK via OAuth2)
                                    |
                               Session Store
                               (Redis / memory)
```

**Key implementation decisions:**
- Auth: OAuth2 PKCE (user-delegated) — each user authenticates with their own Foundry identity
- CBAC: Enforced automatically — user sees only objects their CBAC allows
- Caching: OSDK responses cached per user session only; TTL 5 minutes; invalidated on logout
- Markings: Highest marking of any object in the response displayed in page header banner
- Audit logging: Every query logged with user_id, object_type, and result count

### C-3. Pattern: External System Feed (Inbound to MSS)

**Use case:** GCSS-Army equipment status feed → MSS Equipment Ontology (daily sync).

**Architecture:**
```
GCSS-Army --> Feed Processor --> Foundry Platform SDK (dataset write)
                  |                       |
             Transform + validate     Staging dataset
                                          |
                                  Pipeline Builder transform
                                          |
                                  Equipment Ontology objects
```

**Key implementation decisions:**
- Write target: Staging dataset (via Platform SDK APPEND transaction) — never write directly to Ontology. CAUTION: APPEND is not inherently idempotent; use surrogate keys to deduplicate before appending.
- Transform: Pipeline Builder transform (designed by -30 builder) reads staging → curated → Ontology
- Idempotency: Each record has a source system ID; INSERT OR IGNORE pattern prevents duplicates
- Error handling: Records failing validation written to error dataset; operations team alerted
- Schema validation: Inbound feed validated against expected schema before any write

### C-4. Pattern: Webhook Integration (MSS Outbound)

**Use case:** MSS triggers webhook to external alerting system when unit drops below C3 readiness.

**Architecture:**
```
MSS Ontology (Action) --> Webhook Endpoint --> External Alert System
         |                      |
   Action validator         Signature verify
                            Rate limit check
                            Payload validate
```

**Key implementation decisions:**
- Trigger: SubmitSitrep Action includes webhook call when readiness < C3
- Security: HMAC-SHA256 signature on every outbound webhook; verified by receiver
- Retry: Exponential backoff (3 attempts); failures logged and alerted to operations
- Payload: Minimal payload — object RID and event type only; receiver queries OSDK for full data
- Rate limiting: Maximum one webhook per unit per hour to prevent alert flooding

---

## GLOSSARY

**Action (Foundry)** — A defined operation that modifies Ontology object state. Actions enforce validation, authorization, and audit logging. External applications execute Actions via OSDK. Not to be confused with a direct dataset write.

**Action Validator** — TypeScript function deployed as a Foundry code resource that enforces business rules before an Action applies state changes. Written by -40L engineers; configured by -30 builders.

**APPEND Transaction** — A dataset write transaction type that adds rows to an existing dataset without modifying existing data. The standard write pattern for incremental data loads. APPEND transactions are NOT inherently idempotent — each call appends data without deduplication. Implement deduplication logic (content hashes or surrogate keys) before appending if idempotency is required. Use SNAPSHOT transactions for full-dataset atomic replacement.

**AOR (Area of Responsibility)** — Geographic and functional boundary within which a command exercises authority. Relevant to OSDK query filtering — most operational queries scope to a specific AOR.

**AR 25-2** — Army Regulation 25-2, Cybersecurity. Governs credential handling, system authorization, access control, and security incident reporting.

**Audit Trail** — Application-level log capturing who queried what data and when. Required for all queries against sensitive Object Types and all Action executions in external applications.

**BFF (Backend for Frontend)** — Server-side component of a web application that handles authentication and API calls on behalf of the browser frontend. The correct pattern for web apps consuming MSS via OSDK — keeps tokens server-side.

**Branch (Foundry)** — An isolated development environment within a Foundry project. Code changes are developed on a non-production branch and promoted to master (production) after review.

**CBAC (Context-Based Access Control)** — Foundry's access control model. Governs which users can read, write, and execute Actions on specific Object Types and datasets based on roles and markings. External applications must preserve CBAC — they cannot elevate user permissions.

**C2DAO (Command and Control Data Architecture Office)** — USAREUR-AF theater-level authority for MSS data architecture, OSDK enrollment, API access governance, and production promotion approvals.

**CI/CD (Continuous Integration / Continuous Deployment)** — Automated pipeline that runs tests, lint, and type checks on every commit and gates deployments on passing checks. Required for all Foundry code resources.

**CUI (Controlled Unclassified Information)** — An information handling category requiring specific access and marking controls. CUI markings on MSS objects must be displayed in any application that presents that data.

**DTG (Date-Time Group)** — Military date-time format: DDHHMMZMMMYYYY (e.g., 101435ZMAR2026). Used in SITREP timestamps and operational records throughout MSS.

**EUCOM (United States European Command)** — Geographic Combatant Command to which USAREUR-AF is the ASCC. MSS integrations with EUCOM systems are a primary TM-40L use case.

**EXORD (Execute Order)** — A command directive executing a plan. Referenced in multi-step Action workflows that manage EXORD state machine transitions.

**FMC (Fully Mission Capable)** — Equipment status indicating the item is capable of performing all assigned missions. A key metric in equipment readiness queries.

**FOO (Functions on Objects)** — TypeScript functions deployed within Foundry that compute derived properties or aggregations against Ontology objects at query time. Server-side, stateless, sandboxed.

**Foundry Platform SDK** — Python SDK providing programmatic access to Foundry datasets, branches, transactions, and file resources. Distinct from the OSDK (which accesses the Ontology).

**GCSS-Army (Global Combat Support System — Army)** — Army logistics management system. A common source for equipment and supply data ingested into MSS.

**G2** — Intelligence staff section (corps/division/brigade level). A primary consumer of ISR and all-source analysis data products on MSS.

**G6** — Signal/communications staff section. Responsible for Army network infrastructure and cybersecurity implementation. Relevant to credential provisioning and integration approvals.

**HMAC (Hash-based Message Authentication Code)** — Cryptographic signature mechanism used to verify webhook payload integrity and authenticity.

**ISR (Intelligence, Surveillance, Reconnaissance)** — The collection, processing, and dissemination of information. ISR tracking applications are a common TM-40L deliverable.

**Link Type (Foundry Ontology)** — A defined relationship between two Object Types. Traversing link types from external applications requires additional OSDK calls — use bulk patterns to avoid N+1 performance issues.

**Marking** — A metadata tag on a Foundry object indicating its handling category (e.g., CUI, FOUO, coalition restriction). Enforced by CBAC; must be propagated in application display.

**MPE (Mission Partner Environment)** — Network environment enabling data sharing between U.S. forces and coalition partners. Objects accessible on MPE require NAFv4 compliance review before TM-40L integration development.

**MSS (Maven Smart System)** — The USAREUR-AF enterprise AI/data platform built on Palantir Foundry. The platform against which all TM-40L development occurs.

**N+1 Query Problem** — A performance anti-pattern where an application executes one query to retrieve a list of objects, then one additional query per object to retrieve related data. Produces O(N) API calls. Solved with batch query patterns.

**NAFv4 (NATO Architecture Framework version 4)** — Coalition data architecture standard. Required for any integration accessible by coalition partners on MPE.

**NMC (Non-Mission Capable)** — Equipment status indicating the item cannot perform any assigned mission. Drives maintenance prioritization queries.

**Object Type (Foundry Ontology)** — A typed entity in the Foundry Ontology (e.g., Unit, Equipment, Sitrep). The primary unit of data access via the OSDK.

**OSDK (Ontology SDK)** — The approved programmatic interface for external applications to query Ontology objects and execute Actions. Available in Python and TypeScript. Enforces CBAC and markings on every query.

**OAuth2 PKCE** — OAuth 2.0 authorization flow using Proof Key for Code Exchange. Used for user-delegated authentication in single-page applications where secrets cannot be stored safely on the client.

**PAT (Personal Access Token)** — Developer credential for Foundry access. Authenticates as the issuing user. Approved for local development only — never in deployed applications.

**Pipeline Builder** — Foundry's visual ETL tool for building data transformation workflows. TM-30 scope for design; Platform SDK provides programmatic access to datasets produced by pipelines.

**PMC (Partially Mission Capable)** — Equipment status indicating the item can perform some but not all assigned missions.

**Promotion (Foundry branch)** — The process of merging a non-production branch (develop) to the production branch (master) after completing all review and testing gates. Requires C2DAO coordination for changes affecting production Ontology or datasets.

**Service Account** — A non-human identity provisioned for deployed applications. Service account tokens are the approved credential type for server-side external applications. Provisioned by C2DAO.

**SITREP (Situation Report)** — A formatted report summarizing the current status of a unit or operation. SITREP automation (reading from MSS, formatting, pushing to external systems) is a primary TM-40L use case.

**Slate** — A legacy Foundry environment for building custom HTML/CSS/JavaScript applications hosted within the Foundry platform. Applications inherit the user's Foundry session and CBAC. **Slate is deprecated — do not use for new development.** Use Workshop for internal Foundry applications. For public-facing portals, build an external application using the OSDK or Platform SDK.

**Snapshot Transaction** — A dataset write transaction type that replaces all existing data in a dataset atomically. Used for full-refresh pipelines. Requires data steward coordination before use on shared datasets.

**TLS (Transport Layer Security)** — Cryptographic protocol securing HTTPS connections. TLS 1.2 minimum required for all MSS integrations; TLS 1.3 preferred for new integrations.

**Transaction (Foundry Platform SDK)** — An atomic unit of work for writing to a Foundry dataset. All writes must be wrapped in a transaction. Transactions are committed (visible) or aborted (rolled back) — there is no partial commit.

**TypeScript** — A typed superset of JavaScript. The required language for FOO functions, Action validators, and Slate application logic. TM-40L prerequisite skill.

**UDRA v1.1** — Unified Data Reference Architecture, version 1.1 (February 2025). Defines domain ownership, federated governance, and integration standards for MSS. All TM-40L integrations must align.

**USAREUR-AF** — United States Army Europe and Africa. The Army Service Component Command to USEUCOM, headquartered in Wiesbaden, Germany. The operational context for all TM-40L development.

**V Corps** — Fifth Corps, the primary warfighting corps HQ in Europe. Major consumer of MSS readiness data products.

**VAUTI** — Visible, Accessible, Understandable, Trustable, Interoperable. The DoD Data Strategy (2020) framework for data product quality. All MSS data products and integrations must satisfy all five criteria.

**Webhook** — An HTTP callback that allows a system to push event notifications to an external receiver. Used in MSS integration patterns to trigger downstream processing on Ontology state changes.

---

*TM-40L, Maven Smart System (MSS), Software Engineer Technical Manual*
*Headquarters, United States Army Europe and Africa, Wiesbaden, Germany, 2026*
*Distribution authorized to U.S. Government agencies and their contractors only.*
