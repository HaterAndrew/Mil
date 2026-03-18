# Palantir Public Documentation — Reference Index

> Source: https://www.palantir.com/docs/foundry/
> Scraped: 2026-03-17
> Purpose: Cross-reference against MSS training curriculum

---

## 1. Ontology (https://www.palantir.com/docs/foundry/ontology/overview/)

### Core Concepts
- **Ontology** = operational layer bridging digital assets (datasets, virtual tables, models) with real-world entities
- **Object Types**: entity categories with configurable properties
- **Link Types**: relationships between objects
- **Properties**: base types, derived properties, reducers, conditional/value formatting
- **Structs**: reusable composite data structures with automapping
- **Shared Properties**: properties reused across multiple object types
- **Value Types**: custom, versioned, permissioned data types with constraints
- **Interfaces**: object polymorphism — consistent modeling of objects sharing a common shape

### Actions & Functions
- **Action Types**: capture operator input, orchestrate decisions; configurable parameters, submission criteria, validation, side effects, webhooks, media uploads, inline edits, permissions
- **Functions**: TypeScript v1/v2 or Python; ontology edits, transactions, object operations, aggregations, API integration, unit testing, instrumentation

### Applications Powered by Ontology
Object Explorer, Object Views, Vertex (graph), Machinery (process mining), Foundry Rules, Maps, Dynamic Scheduling

---

## 2. Data Integration (https://www.palantir.com/docs/foundry/data-integration/overview/)

### Core Components
- **Data Connection**: agents, syncs, webhooks; 200+ connector types
- **Sync Types**: batch, streaming, file-based, media set
- **Pipeline Builder**: visual no-code transformation; hundreds of built-in functions
- **Code-Based Transforms**: Python, Java, SQL, R in code repositories
- **Streaming**: Apache Flink for real-time processing

### Storage Formats
Datasets, media sets, virtual tables, Iceberg tables, time series, geospatial, unstructured

### Advanced
- HyperAuto (SDDI) for automated integration
- CDC for incremental updates
- Private Link for secure cloud connectivity
- Full data lineage tracking

### Connectors
SAP, Salesforce, NetSuite, AWS, Azure, GCP, Snowflake, BigQuery, Databricks, JDBC/ODBC, REST APIs, and 200+ others

---

## 3. AIP (https://www.palantir.com/docs/foundry/aip/overview/)

### AIP Logic
- Block-based AI workflow construction
- Ontology + developer toolchain integration
- Metrics, observability, automation
- Branching logic
- Evaluation suites for testing output

### AIP Agent Studio
- Application state management
- Retrieval context (multiple types) with citations
- Tools and command integration
- Agents-as-Functions
- Marketplace distribution
- Foundry API access
- Workshop widget embedding

### Document Intelligence
- Extraction strategy deployment to Python transforms
- Navigation, mode/skill systems

### AIP Evals
- Logic function evaluation suites
- Intermediate parameter testing
- Ontology edit evaluation
- Experiment execution
- Results dataset writing
- Metrics dashboards

### LLM Support
- Multiple LLM providers
- LLM-provider compatible APIs
- Custom model registration via function interfaces
- Vision-language model support

---

## 4. Security & Governance (https://www.palantir.com/docs/foundry/security/overview/)

### Access Control Architecture
- **Dual control**: mandatory + discretionary
- **Organizations & Spaces**: mandatory silos between user/resource groups
- **Role-Based Controls**: granular row/column-level based on user attributes
- **Marking-Based Access**: mandatory controls for PII, financial, classified data

### Enterprise Standards
- Mandatory encryption (transit + rest)
- MFA
- Audit logging
- SSO
- Transparency: users can reason about who has access to what and why

---

## TM Track Cross-Reference

| TM Track | Relevant Doc Sections |
|----------|----------------------|
| TM-10 | Ontology basics, Object Explorer, Maps |
| TM-20 | Pipeline Builder, Data Connection, basic transforms |
| TM-30 | Code-based transforms, Functions, Ontology design, Interfaces, Structs |
| TM-40A-F | Maps, domain-specific ontology patterns |
| TM-40G | Time series, analytics, aggregations |
| TM-40H | AIP Logic, Agent Studio, Evals, LLM integration, Document Intelligence |
| TM-40J | Security & governance, Organizations, Audit logs, Resource mgmt |
| TM-40K | Ontology management, Data lineage, Value types, Foundry Rules |
| TM-40L | Code repos, OSDK, Functions (TS/Python), Compute Modules, Streaming |
| TM-40M | Modeling, Transforms Python, Spark, LLM service |
| TM-50G-M | All above at advanced depth |

---

*Operational Data Team — USAREUR-AF*
*Scraped: 2026-03-17*
