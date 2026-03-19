<!-- MAVEN TRAINING CORPUS — CDA REFERENCE MATERIAL
     Source: odt_workspace/docs/architecture/cda/doctrine/overview.md
     Supports: TM-30, TM-40G (ORSA), TM-40K (Knowledge Manager), TM-40L (Software Engineer)
     Type: Doctrine
-->
---
sidebar_position: 1
title: "Doctrine Overview"
---

# Doctrine-Driven Development Guide

Doctrine-driven development turns the "Three-Generation Dilemma" observed at the Joint Readiness Training Center into a software design requirement. This repository packages the lessons captured by Col. Richard Davis and Lt. Col. Jonathan Graebener into an ontology and pipeline pattern that closes the gap between junior tacticians, field grade integrators, and commanders. Every digital product we build in Palantir Foundry must reinforce disciplined doctrine, ensure synchronized planning, and surface assessments that drive resourcing decisions.

---

## Why This Matters

- **Observed failure pattern:** JRTC rotations repeatedly show that staffs struggle to synchronize detailed planning in contested, decisive-action environments. Symptoms include incomplete COAs, weak MDMP execution, missing operational graphics, and poor integration of CBRN and cyber considerations.
- **Root cause:** Differences in doctrinal fluency across company grade, field grade, and command levels produce divergent planning languages. When commanders shortcut MDMP under time pressure, junior staff officers cannot deliver the detail required for mission success.
- **Desired outcome:** A shared doctrinal lexicon, enforced through data models and tooling, that keeps the commander driving the operations process while field grade officers bridge understanding and junior leaders internalize standards.

---

## Doctrine-Aligned Problem Frame

| Generation | Doctrinal Role | Observed Gap | Required Data Support |
|------------|----------------|--------------|-----------------------|
| Company Grade | Execute troop leading procedures and branch doctrine two echelons up | Limited doctrinal vocabulary and inconsistent MDMP participation | Access to authoritative tasks, actions, effects, and conditions tied to higher-echelon plans |
| Field Grade | Bridge commander intent with staff execution; enforce MDMP | Insufficient tooling to visualize commander activities and assess staff proficiency | Ontology constructs that encode understand, visualize, describe, direct, lead, assess |
| Commanders | Drive operations process; set doctrinal tone | Time pressure leading to ad hoc processes and incomplete guidance | Dashboards that expose doctrinal compliance, decision points, and assessment products |

---

## Foundry Ontology Blueprint

- **Core object types:**
  - `Mission`, `Operation`, `Task`, `Effect`, `Condition` to enforce MDMP outputs.
  - `Unit`, `Capability_Element`, `Readiness_State` with P-S-R-T decomposition to link operations and force posture.
  - `Doctrine_Publication`, `Training_Product`, `Force_Design_Decision`, `PPBE_Program`, `Budget_Line` to connect operational lessons to institutional change.
- **Key relationships:**
  - `Mission` **drives** `Task`; `Task` **produces** `Effect`; `Effect` **leads to** `Condition` (operational traceability).
  - `Unit` **executes** `Task`; `Unit` **requires** `Resource_Allocation`; `Resource_Allocation` **funds** `Capability_Element` (readiness and PPBE linkage).
  - `Assessment_Event` **evaluates** `Task` via MOP/MOE; results **inform** `Doctrine_Publication` updates and **generate** `Demand_Signal` for resourcing.
- **Temporal modeling:** All links capture `valid_from` and `valid_to` timestamps with bitemporal audit trails. State transitions (`Readiness_State_Transition`, `Plan_Phase_Shift`) are modeled as explicit event objects.

---

## Pipeline Pattern

1. **Ingest:** Collect operational reports (e.g., JRTC OC/T observations), readiness data, PPBE documents. Validate source provenance and doctrinal terminology.
2. **Doctrine Enforcement:** Normalize inputs against authoritative doctrine taxonomies (JP 5-0, ADP 5-0). Reject or flag non-doctrinal constructs.
3. **Integration:** Merge operational actions with readiness and resource contexts using the ontology relationships above. Enforce identity vs. classification discipline.
4. **Assessment:** Compute MOP/MOE indicators, detect planning shortfalls (missing COA completeness, absent CBRN planning), and surface commander decision points.
5. **Feedback:** Route confirmed lessons to `Doctrine_Publication` change proposals, `Training_Product` updates, and PPBE `Demand_Signal` adjustments. Track closure of doctrinal gaps over time.

---

## Usage Playbook

- **Commanders:** Consume dashboards that expose MDMP completion, doctrinal vocabulary adherence, and decision support triggers. Require back briefs recorded as structured data.
- **Field Grade Officers:** Curate the ontology, enforce time standards, and mentor staff through data-backed MDMP rehearsals. Use assessment outputs to drive leader development sessions.
- **Company Grade Officers:** Leverage troop leading procedure aids auto-populated from `Task` and `Effect` objects. Submit after-action observations that tie directly to doctrine references.
- **Analysts & Engineers:** Extend Foundry pipelines only when new constructs map to documented doctrine. Propose schema changes with references and red-team for identity/time violations.

---

## Contributing

1. Fork or branch the repo on `main`.
2. Propose ontology or pipeline changes with doctrinal citations and time-modeling implications.
3. Include automated checks that flag non-doctrinal terminology and incomplete MDMP artifacts.
4. Document assessment logic (MOP/MOE) and demonstrate linkage to resourcing outcomes before merging.

---

## References

- Davis, R. J., & Graebener, J. P. "Bridging the Three-Generational Gap," Military Review Online Exclusive, January 2021.
- JP 5-0, Joint Planning.
- ADP 5-0, The Operations Process.
- DRRS Concept of Operations and PPBE Regulation.
