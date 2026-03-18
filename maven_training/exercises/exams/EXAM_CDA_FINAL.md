<!-- MAVEN TRAINING CORPUS — CDA REFERENCE MATERIAL
     Source: odt_workspace/docs/architecture/cda/final-exam.md
     Supports: TM-30, TM-40G (ORSA), TM-40H (AI Engineer), TM-40M (ML Engineer), TM-40J (Program Manager), TM-40K (Knowledge Manager), TM-40L (Software Engineer)
     Type: Exam
-->
---
sidebar_position: 10
title: "CDA Final Exam"
---

# CDA DATA ARCHITECTURE TRAINING — COMPREHENSIVE FINAL EXAMINATION

**Classification: UNCLASSIFIED**
**Exam Duration: 4 Hours (240 Minutes)**
**Total Points: 300**
**Passing Score: 240 / 300 (80%)**

> This examination covers all material from the three-track Data Architecture Training curriculum: **Intro To Data** (7 decks, 80 slides), **Data 101** (3 decks, 41 slides), and **Data 201** (7 decks, 63 slides). All 17 course decks and 184 slides are in scope. No references, notes, or electronic devices are permitted.

---

## SECTION I — FOUNDATIONS & FIRST PRINCIPLES (60 points)

*This section tests your mastery of doctrinal grounding, the cognitive hierarchy, the operational environment, and the philosophical basis for data architecture in the Army enterprise.*

---

### Part A — Multiple Choice (2 points each, 30 points total)

**Select the single best answer for each question.**

**1.** According to ADP 1 and Title 10 U.S. Code, the Army exists to:

- (A) Defend the homeland against all threats foreign and domestic
- (B) Fight and win the Nation's wars by providing prompt, sustained land dominance across the full range of military operations
- (C) Organize, train, and equip forces for joint and coalition operations in support of combatant commanders
- (D) Maintain readiness to deploy and sustain forces in support of national security objectives

**2.** ADP 3-13 defines three dimensions of the operational environment. A data practitioner's work primarily resides in which dimension?

- (A) The Human Dimension
- (B) The Physical Dimension
- (C) The Information Dimension
- (D) The Cyber Dimension

**3.** The cognitive hierarchy defined in ADP 3-13, arranged from the base upward, is:

- (A) Information → Data → Knowledge → Understanding → Decision
- (B) Data → Information → Knowledge → Understanding → Decision/Action
- (C) Data → Knowledge → Information → Understanding → Decision/Action
- (D) Observation → Data → Information → Judgment → Decision/Action

**4.** According to ADP 1-01 (Doctrine Primer), doctrine is defined as:

- (A) Standing orders issued by a commanding officer that govern unit operations and training standards
- (B) Fundamental principles, with supporting tactics, techniques, procedures, and terms and symbols, used for the conduct of operations and as a guide for actions
- (C) A body of regulatory guidance mandating specific systems and technologies for Army use
- (D) Codified lessons learned from combat operations maintained by the Center for Army Lessons Learned

**5.** The Army Data Orientation course uses the analogy of a rat running a maze to illustrate which concept?

- (A) The iterative nature of machine learning pipelines
- (B) That humans codify experience as doctrine, enabling institutional knowledge transfer across generations
- (C) The trial-and-error approach to building data pipelines without requirements
- (D) The complexity of navigating Army bureaucracy during enterprise modernization

**6.** Army CIO Leo Garciga described legacy business systems as:

- (A) "The foundation of Army digital transformation"
- (B) "The Achilles heel of every enterprise"
- (C) "Mission-critical assets requiring modernization"
- (D) "The bridge between legacy and modern architectures"

**7.** At the time of the Army Data Orientation briefing, how many legacy business systems was the Army consolidating, and how many had been shut down in two quarters?

- (A) ~500 systems; 50 killed
- (B) ~800 systems; 100 killed
- (C) ~1,200 systems; 200 killed
- (D) ~600 systems; 75 killed

**8.** The Doctrine-to-Decision chain presented in the Architecture Primer is:

- (A) Doctrine → Data Architecture → Ontology → Decisions
- (B) Doctrine → Ontology → Data Architecture → Decisions
- (C) Data → Ontology → Doctrine → Decisions
- (D) Mission → Technology → Ontology → Applications

**9.** The Stability Stack presented in the Architecture Primer orders layers from most stable to most volatile as:

- (A) Mission/Purpose → Systems/Technology → Activities → Concepts/Meaning
- (B) Systems/Technology → Activities → Mission/Purpose → Concepts/Meaning
- (C) Mission/Purpose → Activities → Concepts/Meaning → Systems/Technology
- (D) Concepts/Meaning → Mission/Purpose → Activities → Systems/Technology

**10.** The Architecture Primer presents a 200-year communication example (1820 courier, 1944 field radio, 1991 satellite comms, 2026 digital network) to demonstrate that:

- (A) Communication technology has improved exponentially over time
- (B) Each new technology required a complete redesign of Army doctrine
- (C) The mission never changed — only the mechanism did
- (D) Modern digital networks make previous communication methods obsolete

**11.** According to the course materials, what is the relationship between an ontology and Army doctrine?

- (A) Ontology replaces doctrine with machine-readable formats
- (B) An ontology is doctrine expressed in machine-readable form
- (C) Doctrine and ontology serve different purposes and should be maintained independently
- (D) Ontology is a subset of doctrine focused exclusively on data standards

**12.** The ADP 3-13 Foreword states: "Information is central to everything we do — it is the basis of __________, a fundamental element of __________, and the foundation for communicating thoughts, opinions, and ideas."

- (A) operations; warfighting
- (B) intelligence; command and control
- (C) readiness; force management
- (D) analysis; decision support

**13.** The "Legacy Mindset" vs. "Enterprise Mindset" comparison includes which of the following contrasts?

- (A) "Build the best custom system" → "Use commercial off-the-shelf only"
- (B) "Data belongs to my organization" → "Data is a shared Army asset"
- (C) "Automate everything" → "Keep manual processes for accountability"
- (D) "Centralize all systems at the Pentagon" → "Distribute systems to each installation"

**14.** The readiness reporting transformation described in the course materials states that since November 2025:

- (A) Unit readiness reviews shifted from live data to standardized PowerPoint briefings for consistency
- (B) The Total Army Readiness Review shifted from static presentations built through thousands of man-hours to live data reporting
- (C) Readiness data was moved from Foundry to the Defense Readiness Reporting System exclusively
- (D) Manual readiness assessments were replaced with AI-generated readiness predictions

**15.** According to the Architecture Primer, enterprise architecture "used to focus on systems" but modern architecture focuses on:

- (A) Cloud infrastructure
- (B) Agile delivery
- (C) Meaning
- (D) Artificial intelligence

---

### Part B — Short Answer (5 points each, 30 points total)

**Answer each question in 3-5 sentences. Be precise and reference specific course material.**

**16.** The course states that "every role in the data space serves this chain." Identify the chain being referenced, explain where a data practitioner operates within it, and articulate why errors at that level are catastrophic to all layers above.

**17.** The Army's enterprise consolidation effort involves moving from ~800 separate business systems to enterprise platforms. Describe the "Old Model" versus the "New Model" as presented in the Army Data Orientation course, including at least three specific contrasts from each model.

**18.** The Architecture Primer introduces the concept of a "hidden third layer" between activities and technology. Name this layer, explain why it is described as the "survival layer," and provide the specific insight from the course about what happens when systems die, platforms change, and vendors disappear.

**19.** Explain why the military has an inherent advantage in enterprise architecture according to the Architecture Primer. What four things does doctrine already define, and what is the Army's challenge — not creating a conceptual model, but what?

**20.** The Semantic Layer deck asserts that "skipping this layer guarantees rework. Not 'might.' Guaranteed." Explain the five purposes of the semantic layer and why the course describes velocity without meaning as "chaos delivered faster."

**21.** The Semantic Layer deck proposes a governance model based on pull requests rather than governance boards. Explain the three outcomes this creates and what information every pull request on the ontology must show.

---

## SECTION II — THE FIVE-LAYER DATA STACK & FOUNDRY ARCHITECTURE (50 points)

*This section tests your understanding of the 2026 Data Stack model, Palantir Foundry's capability mapping, and the four-layer Foundry architecture.*

---

### Part A — Multiple Choice (2 points each, 20 points total)

**22.** The five layers of the 2026 Data Stack, from bottom to top, are:

- (A) Data, Processing, Analytics, Visualization, Action
- (B) Infrastructure & Orchestration, Ingestion & Integration, Semantic & Modeling, Intelligence & Inference, Activation & Interface
- (C) Storage, Compute, Transform, Model, Serve
- (D) Collection, Processing, Analysis, Dissemination, Feedback

**23.** According to the 2026 Data Stack deck, which layer is described as "The Truth Layer"?

- (A) L1 — Infrastructure & Orchestration
- (B) L2 — Ingestion & Integration
- (C) L3 — Semantic & Modeling
- (D) L4 — Intelligence & Inference

**24.** The investment priority formula presented in the 2026 Data Stack is:

- (A) L4 + L5 > L1
- (B) L1 + L2 > L3
- (C) L2 + L3 > L5
- (D) L3 + L4 > L2

**25.** The "Weak Link Rule" states:

- (A) The weakest team member determines the project's success
- (B) Your stack is only as strong as its weakest layer
- (C) Security is only as strong as the weakest access point
- (D) Data quality is only as good as the weakest source system

**26.** According to the 2026 Data Stack, which layer is "the most common skill gap" where "LLMs can serve as a stop-gap for simple integrations, but production-grade pipelines still require deep expertise"?

- (A) L1 — Infrastructure
- (B) L2 — Ingestion & Integration
- (C) L3 — Semantic & Modeling
- (D) L5 — Activation & Interface

**27.** Palantir Foundry's Ontology Manager maps to which layer of the 2026 Data Stack?

- (A) L2 — Ingestion & Integration
- (B) L3 — Semantic & Modeling
- (C) L4 — Intelligence & Inference
- (D) L5 — Activation & Interface

**28.** The course identifies Foundry's primary competitive advantage as residing in which layer?

- (A) L1 — Apollo infrastructure
- (B) L2 — Pipeline Builder transforms
- (C) L3 — The Ontology layer
- (D) L5 — Slate and Workshop applications

**29.** The Four Layers deck identifies what as the "#1 cause of Foundry ontology failure"?

- (A) Insufficient data quality in source systems
- (B) Treating the Ontology like a database (Ontology-Dataset Confusion)
- (C) Inadequate pipeline performance
- (D) Poor application design in Workshop

**30.** In the Four Layers model, what is the correct statement about the relationship between datasets and pipelines?

- (A) Each pipeline contains multiple datasets within it
- (B) Datasets and pipelines alternate in a chain — each pipeline reads a dataset and writes a new dataset
- (C) Pipelines exist within the Ontology layer to transform semantic objects
- (D) Datasets feed directly into applications without intermediate pipeline processing

**31.** According to the Four Layers deck, the Ontology should point to:

- (A) Raw source datasets directly
- (B) The most recently updated dataset regardless of quality
- (C) The final clean dataset — it should never see raw source artifacts
- (D) Application-specific views optimized for each consuming app

---

### Part B — Scenario Analysis (10 points each, 30 points total)

**32.** A data engineer on your team creates a new Foundry object type called `GFEBSFinancialTransaction`. When questioned, they explain: "This is the data from GFEBS about financial transactions. I named it after the source so people know where it comes from." Using the Four Layers framework, the Definition Clarity Test, and the Category Error framework from the courses, write a detailed critique of this design decision. Your answer must:
- Identify which specific anti-pattern(s) this violates
- Explain which layer confusion is occurring
- Provide the corrected object type design with a proper name, definition, and at least four properties
- Explain what happens when GFEBS is eventually replaced by a new financial system
- Reference the specific test from the course materials that this object type fails

**33.** Your team is building a readiness dashboard in Workshop. A colleague proposes creating the following Foundry object types: `ReadinessDashboardMetrics`, `G3ReadinessView`, and `CommanderBriefingData`. Using specific course material, identify every problem with this proposal. Your answer must:
- Name each anti-pattern from the Object Type Cookbook that applies to each proposed type
- Explain why applications and AI should consume the Ontology but never redefine it
- Provide the correct architectural approach using the Four Layers model
- Explain what Workshop widgets should be used instead and why

**34.** A senior leader asks you: "We just spent millions on Foundry. Why do we need to invest in the semantic layer (L3) when we could build more dashboards (L5) that leadership can actually see?" Using the 2026 Data Stack, the Weak Link Rule, the investment priority formula, and the Decision Advantage compound effect, construct a rigorous argument for L3 investment. Your answer must include:
- The specific course quote about what happens when "brilliant L5 dashboards are built on shaky L3 semantics"
- The mathematical compound effect demonstration from the Decision Advantage deck
- The specific layer dependency chain and why L5 alone is described as "the most visible layer but least differentiating"
- At least two specific examples of how poor L3 causes downstream failures

---

## SECTION III — ONTOLOGY ENGINEERING (60 points)

*This section tests your deep understanding of ontology design principles, the three building blocks, the Definition Clarity Test, anti-patterns, and proper modeling practices.*

---

### Part A — Multiple Choice (2 points each, 20 points total)

**35.** An ontology is defined in the course as:

- (A) A database schema optimized for graph queries
- (B) A shared agreement about what things exist, what they mean, and how they relate to each other
- (C) A collection of linked datasets organized by source system
- (D) A visualization of data relationships used for documentation purposes

**36.** The three building blocks of every ontology are:

- (A) Tables, Views, and Indexes
- (B) Entities, Attributes, and Relationships
- (C) Object Types (nouns), Properties (adjectives), and Links (verbs)
- (D) Classes, Methods, and Interfaces

**37.** The Definition Clarity Test asks:

- (A) "Is this object type documented in the data dictionary?"
- (B) "Can you explain what this object type represents without mentioning a source system?"
- (C) "Does this object type have a primary key defined?"
- (D) "Has this object type been approved by the governance board?"

**38.** Which of the following definitions PASSES the Definition Clarity Test?

- (A) "This is the data from GCSS-Army about equipment"
- (B) "This is the DTMS training records table"
- (C) "Equipment is a persistent asset with a serial number, nomenclature, and status"
- (D) "This is the DRRS unit data we pulled last week"

**39.** The course describes the ontology as fundamentally different from a spreadsheet. Which contrast is accurate?

- (A) Spreadsheets hold definitions; ontologies hold data
- (B) Spreadsheets require organizational agreement; ontologies don't
- (C) The ontology is the agreement, not the data — it can be defined before any data exists
- (D) Ontologies are always more complex than spreadsheets

**40.** The Object Type Design deck demonstrates that baking unit names, exercise names, or date ranges into object type names leads to what the course calls:

- (A) The Normalization Problem
- (B) The Multiplication Problem
- (C) The Integration Problem
- (D) The Governance Problem

**41.** The Multiplication Problem formula from the Object Type Design deck is:

- (A) (number of source systems) × (number of applications) = object types
- (B) (number of units) × (exercises per year) = object types per year
- (C) (number of developers) × (sprints per year) = technical debt items
- (D) (number of pipelines) × (datasets per pipeline) = total datasets

**42.** The downstream cost estimated for one bad object type design decision is:

- (A) 100+ person-hours across all layers
- (B) 500+ person-hours across all layers
- (C) 1,000+ person-hours across all layers (Pipelines: 200+, Ontology: 100+, Applications: 300+, Consumers: 400+)
- (D) 5,000+ person-hours across all layers

**43.** Exercise context (e.g., JRTC 24-01) should be modeled in an object type as:

- (A) Part of the object type name to distinguish exercise data from operational data
- (B) A separate object type for each exercise with its own pipeline
- (C) A boolean property (`isExercise`) and a string property (`exerciseName`) on the canonical type
- (D) A separate Ontology namespace for exercise data

**44.** The seven-item checklist from the Object Type Design deck includes all of the following EXCEPT:

- (A) Can you define it without mentioning a source system?
- (B) Does a primary key authority exist?
- (C) Has the object type been tested with at least 1,000 rows of sample data?
- (D) Would this name still make sense in 5 years?

---

### Part B — Anti-Pattern Identification (4 points each, 24 points total)

**For each of the following object type names, identify the specific anti-pattern by its course-defined name, explain why it is wrong, and provide the corrected design.**

**45.** `SAPTable_MARA`

**46.** `HRPerson`, `PayrollPerson`, `BadgePerson` (three separate object types)

**47.** `DashboardMetrics`

**48.** `MonthlyStatusReportRow`

**49.** `Item`

**50.** `Asset` (with 200+ properties covering equipment, facilities, vehicles, software licenses, and intellectual property)

---

### Part C — Design Exercise (16 points)

**51.** You are tasked with modeling a "Maintenance Event" concept for the Army's equipment readiness tracking system. Design a complete object type proposal that demonstrates mastery of all ontology principles taught across the curriculum. Your answer must include:

**(a)** (3 points) A source-agnostic definition that passes the Definition Clarity Test.

**(b)** (3 points) A complete property list (minimum 8 properties) with data types, including the primary key. Justify your primary key choice using the four properties of a good primary key (unique, not null, immutable, stable).

**(c)** (4 points) At least four links to other object types with explicit cardinality (one-to-one, one-to-many, or many-to-many) and direction. For each link, explain why it is a link rather than a property.

**(d)** (3 points) Identify which of the Nine Canonical Object Type Varieties this concept belongs to, justify your classification using the Decision Tree from the Data 201 curriculum, and explain how this classification affects the lifecycle modeling.

**(e)** (3 points) Identify two controlled vocabularies (CVs) required by this object type, provide at least four terms for each CV, and explain why these values must be governed as CVs rather than free-text fields.

---

## SECTION IV — DATA MODELING FUNDAMENTALS (40 points)

*This section tests structural data modeling knowledge: keys, schemas, normalization, relationships, data quality, and enterprise modeling methodologies.*

---

### Part A — Multiple Choice (2 points each, 16 points total)

**52.** The four properties of a good primary key are:

- (A) Unique, Indexed, Computed, Versioned
- (B) Unique, Not Null, Immutable, Stable
- (C) Unique, Sequential, Auto-generated, Integer
- (D) Unique, Descriptive, Human-readable, Short

**53.** A foreign key is:

- (A) A column encrypted for security purposes
- (B) A column that points to the primary key of another table, creating relationships
- (C) A key imported from an external system
- (D) A secondary unique identifier within the same table

**54.** In Foundry's Ontology, foreign keys become:

- (A) Properties on the object type
- (B) Links between object types
- (C) Computed columns in pipelines
- (D) Indexes on datasets

**55.** The six dimensions of data quality are:

- (A) Speed, Volume, Variety, Veracity, Value, Velocity
- (B) Completeness, Accuracy, Consistency, Timeliness, Uniqueness, Validity
- (C) Precision, Recall, F1, Accuracy, AUC, Specificity
- (D) Integrity, Availability, Confidentiality, Authenticity, Non-repudiation, Accountability

**56.** Normalization is to __________ as denormalization is to __________.

- (A) OLAP; OLTP
- (B) OLTP (writes); OLAP (reads)
- (C) Small datasets; Large datasets
- (D) Modern systems; Legacy systems

**57.** The Kimball methodology, introduced in 1996 with "The Data Warehouse Toolkit," is characterized by:

- (A) Top-down, enterprise-wide 3NF normalized data warehouse
- (B) Bottom-up, star schema with fact tables and dimension tables
- (C) Hub-Link-Satellite architecture with insert-only loading
- (D) Domain-oriented decentralized data ownership

**58.** The Inmon methodology defines a data warehouse as:

- (A) A star schema optimized for business intelligence queries
- (B) A subject-oriented, integrated, time-variant, and non-volatile collection of data in support of management's decisions
- (C) An agile, auditable integration layer using hash keys for scalability
- (D) A fully denormalized One Big Table optimized for cloud data warehousing

**59.** Data Vault 2.0, developed by Dan Linstedt, uses three component types:

- (A) Facts, Dimensions, and Bridges
- (B) Hubs (business keys), Links (relationships), and Satellites (descriptive attributes with history)
- (C) Entities, Attributes, and Relations
- (D) Sources, Transforms, and Targets

---

### Part B — Comparative Analysis (8 points each, 24 points total)

**60.** Complete the following comparison table for the three major data modeling methodologies. For each cell, provide the specific answer from the course materials.

| Aspect | Kimball | Inmon | Data Vault |
|--------|---------|-------|------------|
| Approach | | | |
| Schema Type | | | |
| Focus | | | |
| Build Time | | | |
| Flexibility | | | |
| Complexity | | | |
| Best For | | | |

Then answer: The course states that "many organizations use a hybrid." Describe the specific hybrid approach recommended in the course materials, identifying which methodology serves as the integration layer, which serves for reporting, and which provides the governing principles.

**61.** The Enterprise Data Compass is described as "a signed, authoritative reference for data strategy." Answer the following:

**(a)** Who must sign the Enterprise Data Compass? (Provide both roles.)

**(b)** Who maintains the Enterprise Data Compass? (Provide the role and the experience level specified.)

**(c)** List five specific things the Enterprise Data Compass governs.

**(d)** Why must the Enterprise Data Compass be version-controlled?

**(e)** What is the role of the Principal Data Engineer/Architect in relation to the Enterprise Data Compass, and what four areas of responsibility does this role cover?

**62.** Explain the Normal Forms ladder (1NF through BCNF) in your own words, providing a military data example for each level that demonstrates what violation each normal form corrects. Your examples must use Army-relevant data (e.g., soldiers, units, equipment, training records) and show the before (violation) and after (corrected) state for each form.

---

## SECTION V — DECISION ADVANTAGE & OPERATIONAL APPLICATION (40 points)

*This section tests your understanding of decision advantage theory, the decision network model, compound effects, and operational application of data architecture to command decisions.*

---

### Part A — Multiple Choice (2 points each, 14 points total)

**63.** ADP 3-13 defines information advantage as:

- (A) Having more data than the adversary
- (B) A condition when a force holds the initiative in terms of situational understanding, decision making, and relevant actor behavior
- (C) Superior technology infrastructure enabling faster data processing
- (D) Complete knowledge of the enemy's capabilities and intentions

**64.** The Decision Advantage formula presented in the course is:

- (A) DA = Information × Technology × Speed
- (B) DA = Δ(Quality × Speed) of the Decision Cycle, Relative to Adversary
- (C) DA = (Friendly OODA Loop Speed) / (Enemy OODA Loop Speed)
- (D) DA = Data Quality + Processing Speed + Commander Experience

**65.** The three pillars of decision advantage from ADP 3-13 are:

- (A) Speed, Security, Surprise
- (B) Superior Understanding, Superior Decision Making, Superior Influence
- (C) Collect, Process, Disseminate
- (D) Observe, Orient, Decide, Act

**66.** The nine elements of a decision are organized into three functional layers. The Input Layer consists of:

- (A) Alternatives, Constraints, Uncertainty
- (B) Authority, Selection, Agency
- (C) Information, Awareness, Intent
- (D) Evaluation, Authority, Selection

**67.** According to the Decision Advantage deck, which node is described as "the most neglected and highest-value node in virtually every enterprise system"?

- (A) Information
- (B) Awareness
- (C) Evaluation
- (D) Selection

**68.** The compound effect calculation from the Decision Advantage deck demonstrates that a 15% improvement at each of five nodes in the decision chain results in:

- (A) A 75% total improvement (additive)
- (B) An overall chain quality increase from 12.0% to 30.7% (multiplicative)
- (C) A 2x improvement in decision speed
- (D) A 15% improvement in overall decision quality

**69.** The Decision Advantage deck states that "empty nodes are multipliers of __________":

- (A) Confusion
- (B) Delay
- (C) Zero
- (D) Risk

---

### Part B — Applied Analysis (13 points each, 26 points total)

**70.** The Decision Advantage deck presents a two-cycle model: the Friendly Decision Cycle and the Threat Decision Cycle. For each of the five steps in the Friendly cycle (Collect, Process, Understand, Decide, Act), identify:

**(a)** The corresponding counter-action the adversary uses against that step (from the course materials).

**(b)** One specific Foundry ontology element (object type, pipeline, or application) that strengthens each friendly step.

**(c)** How a failure at the "Understand" step (due to poor data architecture) cascades to make the "Decide" and "Act" steps ineffective, using the compound multiplication model from the course. Show your math using baseline quality percentages.

**71.** You are designing the Foundry ontology for a brigade-level decision support system. Using the Decision Advantage "Node Graph to Foundry Ontology" mapping, design a complete ontology coverage plan. For each of the following decision nodes, provide:

- The example object types the course recommends
- The pipeline/transform type required
- The "common gap" the course identifies for that node

Cover these six nodes: **Information**, **Awareness**, **Alternatives**, **Constraints**, **Uncertainty**, and **Selection**.

Then answer: The course identifies the Selection node as having "the most critical gap in virtually all fielded systems." What specific object type does the course recommend for the Selection node, and what six fields should it capture?

---

## SECTION VI — ADVANCED SEMANTIC ENGINEERING (Data 201) (50 points)

*This section tests mastery of the Data 201 curriculum: semantic modeling principles, RDF/OWL foundations, object type varieties, scope engineering, identity governance, and enterprise ontology design.*

---

### Part A — Multiple Choice (2 points each, 20 points total)

**72.** Gruber (1993) defined an ontology as:

- (A) "A formal representation of knowledge within a domain using classes and properties"
- (B) "A specification of a conceptualization — a designed artifact intended for knowledge sharing and reuse"
- (C) "A machine-readable dictionary of domain-specific terms and relationships"
- (D) "A graph database schema optimized for semantic queries"

**73.** The four evaluation criteria for an ontology (from Gruber's definition as taught in the course) are:

- (A) Completeness, Performance, Scalability, Usability
- (B) Clarity, Coherence, Extendibility, Minimal Encoding Bias
- (C) Accuracy, Precision, Recall, F1 Score
- (D) Correctness, Consistency, Availability, Partition Tolerance

**74.** The five W3C standards that form the "vendor-agnostic backbone" of semantic engineering are:

- (A) HTML, CSS, JavaScript, WebAssembly, HTTP
- (B) RDF, OWL 2, SKOS, SHACL, SPARQL
- (C) XML, JSON, YAML, CSV, Parquet
- (D) SQL, NoSQL, GraphQL, REST, gRPC

**75.** OWL operates under the Open-World Assumption, which means:

- (A) All data is publicly accessible and unclassified
- (B) Missing data does not equal false — if the ontology doesn't say something, it means we don't know yet
- (C) Any agent can add new axioms to the ontology without governance
- (D) The ontology is always incomplete and never reaches a final state

**76.** The practical combination recommended by the course is:

- (A) Use OWL for validation and SHACL for meaning
- (B) Use OWL for meaning (classes, properties, axioms, inference) and SHACL for contract tests (required fields, cardinality, datatypes)
- (C) Use SHACL for everything and avoid OWL entirely
- (D) Use RDF for meaning and OWL for serialization

**77.** The four OWL 2 profiles, matched to their primary use case, are:

- (A) EL (Scalable classification), QL (Query rewriting/OBDA), RL (Rule-based reasoning), Full DL (Maximum expressivity)
- (B) EL (Enterprise Large), QL (Query Language), RL (Relational Logic), Full DL (Data Lake)
- (C) EL (Event Logging), QL (Queue Logic), RL (Real-time Logic), Full DL (Deep Learning)
- (D) EL (Edge Layer), QL (Query Layer), RL (Reasoning Layer), Full DL (Full Data Layer)

**78.** The Nine Canonical Object Type Varieties are:

- (A) Entity, Event, Reference, Table, View, Index, Trigger, Function, Procedure
- (B) Entity, Event, Controlled Vocab, Capability, Relationship Object, Aggregate, Reference, Document, Temporal State
- (C) Person, Place, Thing, Event, Concept, Relationship, Attribute, Metric, Rule
- (D) Core, Extension, Abstract, Concrete, Composite, Leaf, Bridge, Hub, Satellite

**79.** The Identity Authority Matrix requires which columns for every entity type?

- (A) Entity Type, Source System, Table Name, Column Name
- (B) Entity Type, ID Authority, ID Format, Immutability, Governance Owner
- (C) Entity Type, Primary Key, Foreign Keys, Indexes
- (D) Entity Type, Data Owner, Data Steward, Classification Level

**80.** In record linkage theory as taught in the course, the three match categories and their thresholds are:

- (A) Exact (100%), Partial (50-99%), None (0-49%)
- (B) Matches (≥ 0.95), Possible Matches (0.70-0.95), Non-Matches (< 0.70)
- (C) High (≥ 0.90), Medium (0.50-0.90), Low (< 0.50)
- (D) Confirmed (≥ 0.99), Probable (0.80-0.99), Unlikely (< 0.80)

**81.** "Schema fit" vs. "scope fit" is a distinction introduced in the Scope Engineering deck. A type that passes schema fit but fails scope fit means:

- (A) The data structure is wrong but the population is complete
- (B) The properties and datatypes are correct, but the data only covers a fraction of the real-world population, time range, or geography needed
- (C) The ontology definition is unclear but the data is clean
- (D) The SHACL constraints validate but the OWL axioms are inconsistent

---

### Part B — Applied Semantic Engineering (10 points each, 30 points total)

**82.** The Scope Engineering deck introduces a six-dimension Data Scope Assessment framework. For each dimension below, define what it measures AND write one specific scope acceptance test (a "silent failure" test case that should "fail loudly") for a hypothetical `Unit` object type in an Army-wide operational readiness system:

1. Instance Coverage
2. Temporal Coverage
3. Geographic Scope
4. Classification Ceiling
5. Source Completeness
6. Refresh Cadence

Then answer: The Scope Engineering deck presents a decision flowchart for "Reuse vs Extend vs Create." What is the first question in this flowchart, and what does a "No" answer lead to?

**83.** The Identity Governance deck describes the "Source Record → Resolved Entity" pattern for multi-source identity resolution. Answer all of the following:

**(a)** Explain the three principles of the resolution architecture (Source Records Preserve Raw Truth, Resolved Entities Are Derived, Full Lineage Always Retained).

**(b)** Name and describe the four survivorship strategies for choosing canonical field values when sources conflict.

**(c)** Explain why `owl:sameAs` is described as dangerous in the Identity Governance deck and what alternative the course recommends for uncertain identity equivalence.

**(d)** Write SHACL constraints (in natural language, describing what each constraint enforces) for a `Person` entity that would enforce: exactly one `personId` matching the pattern `PER-NNNNNN`, at least one `fullName`, and at least one provenance link (`prov:wasDerivedFrom`).

**(e)** List five identity quality metrics that should be tracked operationally.

**84.** You are advising a coalition partner who is building a new defense ontology from scratch. They have no existing semantic layer. Using the complete Data 201 curriculum, write a prioritized implementation plan that covers:

**(a)** The five required deliverables for every type proposal (from the Architecture First Principles deck — name all five).

**(b)** How to select the appropriate OWL 2 profile for their use case (describe the four profiles and their trade-offs).

**(c)** How to use competency questions to define scope boundaries (provide three example competency questions for a military unit readiness domain and explain what scope requirements each implies).

**(d)** The governance model for ontology evolution (pull requests, not boards — describe the three outcomes).

**(e)** Why full-time stewardship is described as "non-negotiable" and what four things the steward must understand.

---

## SECTION VII — INTEGRATION & SYNTHESIS (Capstone) (Bonus: 20 points)

*This section requires you to synthesize knowledge from across all 17 decks. These questions have no single correct answer — they are graded on depth of reasoning, accurate citation of course material, and practical applicability.*

---

**85.** (10 points) **The Complete Chain.** Trace the complete path from a raw sensor reading on a piece of Army equipment to a commander's decision to reallocate maintenance resources. Your answer must touch every relevant concept from the curriculum:

- The cognitive hierarchy (ADP 3-13)
- The Doctrine-to-Decision chain
- The Five-Layer Data Stack (identify which layer handles each step)
- The Four Layers of Foundry (Source System → Dataset/Pipeline → Ontology → Application)
- The Decision Advantage network (identify which nodes are activated)
- At least three specific object types you would create, with definitions that pass the Clarity Test
- The specific Foundry tools (Pipeline Builder, Ontology Manager, Workshop, AIP) used at each stage

**86.** (10 points) **The Anti-Pattern Autopsy.** A fictional Army organization has been using Foundry for 18 months. They have:

- 347 object types (78% of which have source system names in them)
- 12 different definitions of "Unit" across different staff sections
- No controlled vocabularies — all classification fields are free-text strings
- No identity authority matrix — each team assigns their own IDs
- Exercise data mixed with operational data with no way to distinguish them
- 40+ "DashboardMetrics"-style object types created by individual Workshop developers
- Zero SHACL constraints or validation rules
- A match/merge confidence threshold of 0.50 (everything above 50% is auto-merged)

Using every relevant concept from the curriculum, write a comprehensive remediation plan. For each problem identified, cite the specific course material (deck name, principle, or framework) that addresses it, explain the downstream cost of not fixing it, and provide the specific corrective action. Prioritize your remediation steps and justify the ordering.

---

## ANSWER KEY REFERENCE

*Answers for Sections I-VI multiple choice:*

1-B, 2-C, 3-B, 4-B, 5-B, 6-B, 7-B, 8-B, 9-C, 10-C, 11-B, 12-B, 13-B, 14-B, 15-C, 22-B, 23-C, 24-C, 25-B, 26-B, 27-B, 28-C, 29-B, 30-B, 31-C, 35-B, 36-C, 37-B, 38-C, 39-C, 40-B, 41-B, 42-C, 43-C, 44-C, 52-B, 53-B, 54-B, 55-B, 56-B, 57-B, 58-B, 59-B, 63-B, 64-B, 65-B, 66-C, 67-D, 68-B, 69-C, 72-B, 73-B, 74-B, 75-B, 76-B, 77-A, 78-B, 79-B, 80-B, 81-B

---

**END OF EXAMINATION**

*This exam was generated from a comprehensive analysis of all 184 slides across 17 course decks in the CDA Data Architecture Training curriculum.*

*Exam Version: 1.0 | Generated: 2026-03-08*
