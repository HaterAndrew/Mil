<!-- MAVEN TRAINING CORPUS — CDA REFERENCE MATERIAL
     Source: odt_workspace/docs/architecture/cda/doctrine/canon/conditions-indicators-thresholds.md
     Supports: TM-40G (ORSA), TM-40H (AI Engineer), TM-40M (ML Engineer)
     Type: Canon
-->
---
sidebar_position: 3
title: "Conditions, Indicators & Thresholds"
---

# Conditions, Indicators, and Thresholds – structured approach

1. How to structure a **Condition**
2. How to structure **Indicators**
3. How to structure **Thresholds**
4. Your examples, but encoded in that structure

---

## 1. Condition – structure it so the "sentence" is assembled, not typed

Instead of one big free-text box, model a condition as **slots + enums** that the UI composes into a sentence.

### 1.1 Condition core fields

```yaml
Condition:
  id: COND-001
  category:        # ENUM
  domain:          # ENUM
  subject_type:    # ENUM
  subject_ref:     # FK to AOI/Unit/Route/etc
  state_type:      # ENUM
  risk_direction:  # ENUM
  time_horizon:    # ENUM
  main_metric_id:  # FK to Indicator/Metric
  logic_profile:   # ENUM
  description_text # OPTIONAL, constrained free text
```

### 1.2 Suggested enums (for dropdowns)

**category** (what part of the end state):

* `SECURITY`
* `GOVERNANCE`
* `ESSENTIAL_SERVICES`
* `TERRAIN_CONTROL`
* `FORCE_GENERATION`
* `FREEDOM_OF_MOVEMENT`
* `INFORMATION_ENVIRONMENT`
* `CIVIL_SUPPORT`

**domain** (where it "lives"):

* `PHYSICAL`
* `INFORMATION`
* `COGNITIVE`
* `CYBER`
* `EMS`

**subject_type**:

* `ROUTE`
* `URBAN_AREA`
* `KEY_TERRAIN`
* `POPULATION_GROUP`
* `SECURITY_FORCE`
* `INFRASTRUCTURE_SITE`
* `GOVERNMENT_BODY`
* `SERVICE_SYSTEM`  # e.g. power, water, comms

**state_type** (the state of the environment, NOT action verbs):

* `SECURE`
* `OPEN`
* `FUNCTIONAL`
* `DEGRADED`
* `NEUTRALIZED`
* `CONTAINED`
* `INDEPENDENTLY_CAPABLE`
* `STABLE`
* `DENIED`        # for adversary
* `PERMISSIVE`    # for friendly ops

**risk_direction**:

* `IMPROVING`
* `DETERIORATING`
* `STABLE`
* `UNKNOWN`

**time_horizon**:

* `IMMEDIATE`      # 0–72h
* `NEAR_TERM`      # < 30 days
* `MID_TERM`       # 30–180 days
* `LONG_TERM`      # > 180 days

**logic_profile** (how indicators combine):

* `SINGLE_METRIC`
* `ALL_INDICATORS_REQUIRED`   # logical AND
* `ANY_INDICATOR_SUFFICIENT`  # logical OR
* `WEIGHTED_SCORE`            # MOE-style

### 1.3 Validation rules for Conditions (form-level)

These are the guardrails you asked for.

1. **No actions**

   * Reject conditions where description_text contains patterns like:

     * `"conduct"` `"execute"` `"deploy"` `"train"` `"advise"` `"attack"`
   * Force the user to pick **state_type** instead.

2. **Single subject**

   * Only **one** `subject_type` and `subject_ref` allowed.
   * If the user tries to encode "MSR Red **and** MSR Blue," force them to create two conditions:

     * `ROUTE: MSR Red`
     * `ROUTE: MSR Blue`

3. **Binary / threshold based**

   * Require at least one `main_metric_id` **and** at least one linked Threshold (see section 3).
   * Condition cannot be saved without a **machine-readable** threshold.

4. **Independent (no bundle)**

   * Disallow "and/or" in description_text:

     * Regex check rejects `\b(and|or)\b` unless in a predefined allowed phrase.
   * UI hint: "If you need AND/OR, create multiple Conditions."

5. **Measurable**

   * At least one linked Indicator with:

     * numeric or categorical data type
     * defined data source
     * threshold attached.

---

## 2. Indicators – pre-defined, typed, and re-usable

Indicators should be **library objects** you select, not free text.

### 2.1 Indicator structure

```yaml
Indicator:
  id: IND-001
  name:              # controlled phrase
  metric_code:       # short code, e.g. "ATTACKS_PER_WEEK"
  data_type:         # ENUM
  unit:              # ENUM
  aggregation:       # ENUM
  source_type:       # ENUM
  source_ref:        # optional FK
  collection_frequency: # ENUM
  level:             # ENUM (TACTICAL/OPERATIONAL/STRATEGIC)
```

### 2.2 Suggested enums

**data_type**:

* `INTEGER`
* `FLOAT`
* `PERCENTAGE`
* `BOOLEAN`
* `ENUM_CATEGORY`
* `RATIO`

**unit**:

* `NONE`
* `COUNT`
* `PERCENT`
* `KM`
* `MINUTE`
* `HOUR`
* `DAY`
* `CHECKPOINTS`
* `INCIDENTS`
* `VEHICLES`

**aggregation**:

* `AVERAGE`
* `SUM`
* `MAX`
* `MIN`
* `MEDIAN`
* `RATE_PER_TIME`

**source_type**:

* `ISR_FEED`
* `PATROL_REPORTS`
* `MOVEMENT_TRACKING_SYSTEM`
* `POLICE_REPORTS`
* `OSINT`
* `HOST_NATION_REPORTING`
* `PLATFORM_DATASET`  # for Foundry / DB

**collection_frequency**:

* `REAL_TIME`
* `HOURLY`
* `DAILY`
* `WEEKLY`
* `BIWEEKLY`
* `MONTHLY`

**level**:

* `TACTICAL`
* `OPERATIONAL`
* `STRATEGIC`

### 2.3 Validation rules for Indicators

* **No free text names** in forms:

  * `name` selected from a **pre-approved list**.
  * Admins can add new ones via a separate "Indicator Catalog" workflow, not ad hoc in the condition form.
* **Must have a numeric or discrete shape**:

  * `data_type` + `unit` required.
* **Must have a source**:

  * `source_type` required; optionally `source_ref` (dataset ID, report series, etc.).

---

## 3. Thresholds – treat them like small expressions, not sentences

Thresholds are where you prove the "binary / measurable" part.
Again: no free prose, just an expression builder.

### 3.1 Threshold structure

```yaml
Threshold:
  id: THR-001
  indicator_id:   # FK → Indicator
  operator:       # ENUM
  value:          # numeric or category code
  unit_override:  # optional if different view
  time_window:    # duration label
  evaluation_span: # e.g., "ROLLING_14_DAYS"
  sustainment_requirement: # e.g., "CONSECUTIVE", "NON_CONSECUTIVE"
  interpretation: # ENUM
```

**operator**:

* `LT`   # less than
* `LE`   # less than or equal
* `GT`
* `GE`
* `EQ`
* `NE`
* `IN_SET`      # for categorical
* `NOT_IN_SET`

**time_window**:

* `PER_DAY`
* `PER_WEEK`
* `PER_MONTH`
* `ROLLING_7_DAYS`
* `ROLLING_14_DAYS`
* `ROLLING_30_DAYS`

**sustainment_requirement**:

* `NONE`          # snapshot
* `CONSECUTIVE`
* `NON_CONSECUTIVE`

**interpretation**:

* `CONDITION_ACHIEVED`
* `CONDITION_NOT_ACHIEVED`
* `CONDITION_AT_RISK`

### 3.2 Validation rules for Thresholds

* `value` must match `Indicator.data_type` (numeric vs categorical).
* `unit_override` must be compatible with the indicator's unit (no minutes on a % indicator).
* Threshold must be linked to **exactly one** indicator.

---

## 4. Your examples, encoded without free text

### 4.1 Condition: "MSR Red is secure and open."

**Condition record**

```yaml
Condition:
  id: COND-ROUTE-MSR-RED-SECURE
  category: FREEDOM_OF_MOVEMENT
  domain: PHYSICAL
  subject_type: ROUTE
  subject_ref: "MSR Red"        # FK to AOI/Route table
  state_type: SECURE
  risk_direction: IMPROVING
  time_horizon: NEAR_TERM
  main_metric_id: IND-ATTACKS-MSR-RED
  logic_profile: ALL_INDICATORS_REQUIRED
  description_text: "MSR Red remains open and secure for friendly logistics use."
```

**Indicators**

```yaml
Indicator:
  - id: IND-ATTACKS-MSR-RED
    name: "Number of attacks on MSR Red"
    metric_code: "ATTACKS_PER_WEEK_MSR_RED"
    data_type: INTEGER
    unit: INCIDENTS
    aggregation: SUM
    source_type: PATROL_REPORTS
    collection_frequency: DAILY
    level: OPERATIONAL

  - id: IND-TRANSIT-TIME-MSR-RED
    name: "Average convoy transit time on MSR Red"
    metric_code: "CONVOY_TRANSIT_MINUTES_MSR_RED"
    data_type: FLOAT
    unit: MINUTE
    aggregation: AVERAGE
    source_type: MOVEMENT_TRACKING_SYSTEM
    collection_frequency: DAILY
    level: OPERATIONAL

  - id: IND-ROUTE-CLEARANCE-MSR-RED
    name: "Route clearance operations per week on MSR Red"
    metric_code: "ROUTE_CLEARANCE_FREQ_MSR_RED"
    data_type: INTEGER
    unit: COUNT
    aggregation: SUM
    source_type: PATROL_REPORTS
    collection_frequency: WEEKLY
    level: TACTICAL

  - id: IND-CHECKPOINTS-MSR-RED
    name: "Operational checkpoints on MSR Red"
    metric_code: "CHECKPOINTS_OPERATIONAL_MSR_RED"
    data_type: INTEGER
    unit: CHECKPOINTS
    aggregation: MIN
    source_type: HOST_NATION_REPORTING
    collection_frequency: DAILY
    level: TACTICAL
```

**Thresholds (from your text)**

```yaml
Threshold:
  - id: THR-ATTACKS-MSR-RED
    indicator_id: IND-ATTACKS-MSR-RED
    operator: LT
    value: 2
    time_window: ROLLING_14_DAYS
    sustainment_requirement: CONSECUTIVE
    interpretation: CONDITION_ACHIEVED

  - id: THR-TRANSIT-TIME-MSR-RED
    indicator_id: IND-TRANSIT-TIME-MSR-RED
    operator: LT
    value: 45
    time_window: PER_TRIP
    sustainment_requirement: NONE
    interpretation: CONDITION_ACHIEVED

  - id: THR-CHECKPOINTS-MSR-RED
    indicator_id: IND-CHECKPOINTS-MSR-RED
    operator: GE
    value: 4
    time_window: PER_DAY
    sustainment_requirement: CONSECUTIVE
    interpretation: CONDITION_ACHIEVED
```

The condition is **ACHIEVED** if all associated thresholds with `interpretation=CONDITION_ACHIEVED` are true.

---

### 4.2 Condition: "Host-nation police can independently conduct daily law-enforcement operations."

**Condition**

```yaml
Condition:
  id: COND-HN-POLICE-INDEPENDENT
  category: SECURITY
  domain: PHYSICAL
  subject_type: SECURITY_FORCE
  subject_ref: "Host-nation police – AO Main City"
  state_type: INDEPENDENTLY_CAPABLE
  risk_direction: STABLE
  time_horizon: MID_TERM
  main_metric_id: IND-HN-OPERATIONS-PER-DAY
  logic_profile: ALL_INDICATORS_REQUIRED
  description_text: "Host-nation police independently conduct routine law-enforcement operations in AO Main City."
```

**Indicator examples**

* Number of **independent** HN patrols per day
* Percentage of incidents resolved without coalition intervention
* Number of functional HN police stations in AO
* Ratio of HN-led to coalition-led operations

Each one is a structured `Indicator` + `Threshold`, not free text.

---

## 5. How this looks in a form (practically)

Instead of a big "Describe the condition" box, your form would have:

1. **Dropdowns:**

   * Category, Domain, Subject Type, State Type, Time Horizon
2. **Lookup fields:**

   * Subject Reference (AOI, route, unit from existing tables)
3. **Indicator selector:**

   * Multi-select from "Indicator catalog"
4. **Threshold builder for each Indicator:**

   * Operator (dropdown)
   * Numeric value (number field)
   * Unit (dropdown, auto-filled from Indicator)
   * Time window (dropdown)
   * Sustainment requirement (dropdown)
5. **Optional text:**

   * Short narrative description (with banned words & regex validation)

Free text is **only**:

* Short description (tight length + regex filters)
* Maybe a comments/notes field that doesn't drive logic
