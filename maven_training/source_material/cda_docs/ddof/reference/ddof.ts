/**
 * DDOF - Defense Data Orchestration Framework Ontology
 * 
 * This ontology models the complete lifecycle of data products
 * as they pass through the six-phase DDOF process, including:
 * - Requirements and problem framing
 * - Data provisioning and sources
 * - Quality assessment (VAULTIS-A)
 * - Governance controls
 * - Phase gates and approvals
 * - ADC registration and operations
 * 
 * Aligned with Genesis Mission directives and Secretary of Army priorities.
 * 
 * Core entities (DataProduct, Requirement, DataSource, Role, Person) are
 * defined as interfaces to support multiple implementations and coalition
 * interoperability patterns.
 */

import {
  defineOntology,
  defineValueType,
  defineSharedPropertyType,
  defineInterface,
  defineObject,
  defineLink,
  defineInterfaceLinkConstraint,
  defineCreateObjectAction,
  defineModifyObjectAction,
  defineDeleteObjectAction,
  defineCreateInterfaceObjectAction,
  defineModifyInterfaceObjectAction,
} from "@osdk/maker";

await defineOntology("mil.army.ddof.", async () => {

  // ============================================================================
  // VALUE TYPES (Enums)
  // ============================================================================

  const classificationEnum = defineValueType({
    apiName: "Classification",
    displayName: "Security Classification",
    description: "DoD security classification levels",
    type: {
      type: "string",
      constraints: [{
        constraint: {
          allowedValues: [
            "UNCLASSIFIED",
            "CUI",
            "CONFIDENTIAL", 
            "SECRET",
            "TOP_SECRET"
          ],
        },
        failureMessage: "Must be a valid DoD classification level",
      }],
    },
    version: "1.0.0",
  });

  const productStatusEnum = defineValueType({
    apiName: "ProductStatus",
    displayName: "Data Product Status",
    description: "Lifecycle status of a data product",
    type: {
      type: "string",
      constraints: [{
        constraint: {
          allowedValues: [
            "DRAFT",
            "IN_DEVELOPMENT",
            "ACTIVE",
            "PENDING_RETIREMENT",
            "RETIRED"
          ],
        },
        failureMessage: "Must be a valid product status",
      }],
    },
    version: "1.0.0",
  });

  const phaseNameEnum = defineValueType({
    apiName: "PhaseName",
    displayName: "DDOF Phase Name",
    description: "The six phases of the DDOF lifecycle",
    type: {
      type: "string",
      constraints: [{
        constraint: {
          allowedValues: [
            "PROBLEM_FRAMING",
            "DATA_PROVISIONING",
            "DATA_WRANGLING",
            "DEVELOPMENT",
            "TEST_EVALUATION",
            "OPERATIONS"
          ],
        },
        failureMessage: "Must be a valid DDOF phase",
      }],
    },
    version: "1.0.0",
  });

  const phaseStatusEnum = defineValueType({
    apiName: "PhaseStatus",
    displayName: "Phase Instance Status",
    description: "Execution status of a phase for a specific product",
    type: {
      type: "string",
      constraints: [{
        constraint: {
          allowedValues: [
            "NOT_STARTED",
            "IN_PROGRESS",
            "PASSED",
            "FAILED",
            "BLOCKED"
          ],
        },
        failureMessage: "Must be a valid phase status",
      }],
    },
    version: "1.0.0",
  });

  const controlTypeEnum = defineValueType({
    apiName: "GovernanceControlType",
    displayName: "Governance Control Type",
    description: "Types of required governance controls per Phase 4",
    type: {
      type: "string",
      constraints: [{
        constraint: {
          allowedValues: [
            "ABAC",
            "RBAC",
            "AUDIT_LOGGING",
            "DATA_LINEAGE",
            "CLASSIFICATION_MARKING",
            "OWNERSHIP_DISPLAY"
          ],
        },
        failureMessage: "Must be a valid governance control type",
      }],
    },
    version: "1.0.0",
  });

  const testTypeEnum = defineValueType({
    apiName: "TestType",
    displayName: "Test Type",
    description: "Types of Phase 5 testing activities",
    type: {
      type: "string",
      constraints: [{
        constraint: {
          allowedValues: [
            "FUNCTIONAL",
            "DATA_QUALITY",
            "SECURITY",
            "UAT"
          ],
        },
        failureMessage: "Must be a valid test type",
      }],
    },
    version: "1.0.0",
  });

  const auditEventTypeEnum = defineValueType({
    apiName: "AuditEventType",
    displayName: "Audit Event Type",
    description: "Types of audit events per Genesis Directive 3",
    type: {
      type: "string",
      constraints: [{
        constraint: {
          allowedValues: [
            "ACCESS",
            "CHANGE",
            "APPROVAL",
            "DENIAL",
            "GATE_PASS",
            "GATE_FAIL",
            "OVERRIDE"
          ],
        },
        failureMessage: "Must be a valid audit event type",
      }],
    },
    version: "1.0.0",
  });

  const roleNameEnum = defineValueType({
    apiName: "DDOFRoleName",
    displayName: "DDOF Role Name",
    description: "Standard DDOF roles per the playbook",
    type: {
      type: "string",
      constraints: [{
        constraint: {
          allowedValues: [
            "DECISION_MAKER",
            "C2DAO",
            "FUNCTIONAL_DATA_MANAGER",
            "DATA_ENGINEER",
            "DATA_SCIENTIST_ORSA",
            "KNOWLEDGE_MANAGER"
          ],
        },
        failureMessage: "Must be a valid DDOF role",
      }],
    },
    version: "1.0.0",
  });

  // ============================================================================
  // SHARED PROPERTY TYPES
  // ============================================================================

  const classificationProperty = defineSharedPropertyType({
    apiName: "classification",
    type: "string",
    displayName: "Classification",
    description: "Security classification level",
  });

  const descriptionProperty = defineSharedPropertyType({
    apiName: "entityDescription",
    type: {
      type: "string",
      isLongText: true,
    },
    displayName: "Description",
    description: "Detailed description text",
  });

  const timestampProperty = defineSharedPropertyType({
    apiName: "eventTimestamp",
    type: "timestamp",
    displayName: "Timestamp",
    description: "When an event occurred",
  });

  const notesProperty = defineSharedPropertyType({
    apiName: "notes",
    type: {
      type: "string",
      isLongText: true,
    },
    displayName: "Notes",
    description: "Additional notes or comments",
  });

  // ============================================================================
  // CORE INTERFACES (Cross-cutting Concerns)
  // ============================================================================

  const auditableInterface = defineInterface({
    apiName: "IAuditable",
    displayName: "Auditable",
    description: "Interface for entities that maintain audit trails per Genesis Directive 3",
    properties: {
      createdAt: "timestamp",
      createdBy: "string",
      modifiedAt: "timestamp",
      modifiedBy: "string",
    },
  });

  const governedInterface = defineInterface({
    apiName: "IGoverned",
    displayName: "Governed",
    description: "Interface for entities subject to DDOF governance controls",
    properties: {
      classification: "string",
      ownerPersonId: "string",
    },
  });

  const lifecycleManagedInterface = defineInterface({
    apiName: "ILifecycleManaged",
    displayName: "Lifecycle Managed",
    description: "Interface for entities that pass through DDOF phases",
    properties: {
      currentPhase: "string",
      currentPhaseStatus: "string",
    },
  });

  const qualityAssessedInterface = defineInterface({
    apiName: "IQualityAssessed",
    displayName: "Quality Assessed",
    description: "Interface for entities assessed against VAULTIS-A",
    properties: {
      vaultisScore: {
        required: false,
        propertyDefinition: "double",
      },
      lastAssessmentDate: {
        required: false,
        propertyDefinition: "timestamp",
      },
    },
  });

  // ============================================================================
  // DOMAIN INTERFACES (Core DDOF Entities)
  // ============================================================================

  // ----- PERSON INTERFACE -----

  const personInterface = defineInterface({
    apiName: "IPerson",
    displayName: "Person",
    description: "Interface for individuals filling DDOF roles",
    icon: {
      locator: "user",
      color: "#EC4899",
    },
    properties: {
      personId: "string",
      personName: "string",
      rank: {
        required: false,
        propertyDefinition: "string",
      },
      organization: "string",
      email: "string",
      phone: {
        required: false,
        propertyDefinition: "string",
      },
    },
    extends: [auditableInterface],
  });

  // ----- ROLE INTERFACE -----

  const roleInterface = defineInterface({
    apiName: "IRole",
    displayName: "Role",
    description: "Interface for DDOF roles with defined responsibilities",
    icon: {
      locator: "user-cog",
      color: "#EC4899",
    },
    properties: {
      roleId: "string",
      roleName: "string",
      echelon: "string",
      primaryFunction: "string",
      roleDescription: {
        required: false,
        propertyDefinition: {
          type: "string",
          isLongText: true,
        },
      },
    },
  });

  // ----- DATA SOURCE INTERFACE -----

  const dataSourceInterface = defineInterface({
    apiName: "IDataSource",
    displayName: "Data Source",
    description: "Interface for authoritative data sources accessed in Phase 2",
    icon: {
      locator: "database",
      color: "#06B6D4",
    },
    properties: {
      sourceId: "string",
      sourceName: "string",
      sourceSystem: "string",
      isAuthoritative: "boolean",
      classification: "string",
      accessMethod: "string",
      refreshFrequency: "string",
      sourceDescription: {
        required: false,
        propertyDefinition: {
          type: "string",
          isLongText: true,
        },
      },
      pointOfContact: {
        required: false,
        propertyDefinition: "string",
      },
    },
    extends: [auditableInterface],
  });

  // ----- REQUIREMENT INTERFACE -----

  const requirementInterface = defineInterface({
    apiName: "IRequirement",
    displayName: "Requirement",
    description: "Interface for operational needs driving data products, validated in Phase 1",
    icon: {
      locator: "clipboard-list",
      color: "#8B5CF6",
    },
    properties: {
      requirementId: "string",
      problemStatement: "string",
      operationalContext: {
        required: false,
        propertyDefinition: {
          type: "string",
          isLongText: true,
        },
      },
      missionNeed: "string",
      metlTask: {
        required: false,
        propertyDefinition: "string",
      },
      analyticalApproach: "string",
      targetIocDate: "timestamp",
      // SMART criteria
      isSpecific: "boolean",
      isMeasurable: "boolean",
      isAchievable: "boolean",
      isRelevant: "boolean",
      isTimeBound: "boolean",
      requestedByPersonId: {
        required: false,
        propertyDefinition: "string",
      },
    },
    extends: [auditableInterface],
  });

  // ----- DATA PRODUCT INTERFACE -----

  const dataProductInterface = defineInterface({
    apiName: "IDataProduct",
    displayName: "Data Product",
    description: "Interface for data products moving through the DDOF lifecycle",
    icon: {
      locator: "box",
      color: "#3B82F6",
    },
    properties: {
      productId: "string",
      productName: "string",
      productDescription: {
        required: false,
        propertyDefinition: {
          type: "string",
          isLongText: true,
        },
      },
      classification: "string",
      status: "string",
      currentPhase: "string",
      currentPhaseStatus: "string",
      // Quality
      vaultisScore: {
        required: false,
        propertyDefinition: "double",
      },
      lastAssessmentDate: {
        required: false,
        propertyDefinition: "timestamp",
      },
      // Dates
      iocDate: {
        required: false,
        propertyDefinition: "timestamp",
      },
      focDate: {
        required: false,
        propertyDefinition: "timestamp",
      },
      lastAccessDate: {
        required: false,
        propertyDefinition: "timestamp",
      },
      // Operations
      refreshFrequency: {
        required: false,
        propertyDefinition: "string",
      },
      accessMethod: {
        required: false,
        propertyDefinition: "string",
      },
      // Foreign keys
      requirementId: {
        required: false,
        propertyDefinition: "string",
      },
      ownerPersonId: {
        required: false,
        propertyDefinition: "string",
      },
      sponsorPersonId: {
        required: false,
        propertyDefinition: "string",
      },
    },
    extends: [auditableInterface, governedInterface, lifecycleManagedInterface, qualityAssessedInterface],
  });

  // ============================================================================
  // OBJECT TYPES - Reference Data
  // ============================================================================

  // ----- PHASE REFERENCE DATA -----

  const phase = defineObject({
    apiName: "Phase",
    displayName: "DDOF Phase",
    pluralDisplayName: "DDOF Phases",
    description: "One of six sequential DDOF lifecycle phases (reference data)",
    titlePropertyApiName: "phaseName",
    primaryKeyPropertyApiName: "phaseNumber",
    icon: {
      locator: "layers",
      color: "#10B981",
    },
    properties: {
      phaseNumber: {
        type: "integer",
        displayName: "Phase Number",
        description: "Phase number 1-6",
      },
      phaseName: {
        type: "string",
        displayName: "Phase Name",
        description: "Name of the phase",
      },
      standardDurationDays: {
        type: "integer",
        displayName: "Standard Duration (Days)",
        description: "Standard timeline in days",
      },
      maxDurationDays: {
        type: "integer",
        displayName: "Maximum Duration (Days)",
        description: "Maximum allowed duration in days",
      },
      keyOutput: {
        type: "string",
        displayName: "Key Output",
        description: "Primary deliverable from this phase",
      },
      phaseDescription: {
        type: {
          type: "string",
          isLongText: true,
        },
        displayName: "Description",
        description: "Detailed description of phase activities",
      },
    },
  });

  // ----- QUALITY GATE REFERENCE DATA -----

  const qualityGate = defineObject({
    apiName: "QualityGate",
    displayName: "Quality Gate",
    pluralDisplayName: "Quality Gates",
    description: "Mandatory checkpoint between phases with exit criteria",
    titlePropertyApiName: "gateName",
    primaryKeyPropertyApiName: "gateId",
    icon: {
      locator: "shield-check",
      color: "#F59E0B",
    },
    properties: {
      gateId: {
        type: "string",
        displayName: "Gate ID",
      },
      gateNumber: {
        type: "integer",
        displayName: "Gate Number",
        description: "Gate 1-6 corresponding to phases",
      },
      gateName: {
        type: "string",
        displayName: "Gate Name",
      },
      isEnforced: {
        type: "boolean",
        displayName: "Is Enforced",
        description: "Always true per DDOF policy - gates are mandatory",
      },
      phaseNumber: {
        type: "integer",
        displayName: "Guards Phase",
        description: "Phase number this gate guards exit from",
      },
    },
  });

  const exitCriterion = defineObject({
    apiName: "ExitCriterion",
    displayName: "Exit Criterion",
    pluralDisplayName: "Exit Criteria",
    description: "Individual criterion that must be met to pass a gate",
    titlePropertyApiName: "criterionDescription",
    primaryKeyPropertyApiName: "criterionId",
    icon: {
      locator: "check-circle",
      color: "#F59E0B",
    },
    properties: {
      criterionId: {
        type: "string",
        displayName: "Criterion ID",
      },
      gateId: {
        type: "string",
        displayName: "Gate ID",
        description: "Gate this criterion belongs to",
      },
      criterionDescription: {
        type: "string",
        displayName: "Description",
        description: "What must be verified",
      },
      verificationMethod: {
        type: "string",
        displayName: "Verification Method",
        description: "How to verify this criterion",
      },
      isMandatory: {
        type: "boolean",
        displayName: "Is Mandatory",
        description: "Can gate pass without this criterion?",
      },
      sortOrder: {
        type: "integer",
        displayName: "Sort Order",
        description: "Display order within gate",
      },
    },
  });

  // ============================================================================
  // OBJECT TYPES - Implementing Domain Interfaces
  // ============================================================================

  // ----- ROLE OBJECT -----

  const role = defineObject({
    apiName: "Role",
    displayName: "DDOF Role",
    pluralDisplayName: "DDOF Roles",
    description: "Standard DDOF role with defined responsibilities",
    titlePropertyApiName: "roleName",
    primaryKeyPropertyApiName: "roleId",
    icon: {
      locator: "user-cog",
      color: "#EC4899",
    },
    properties: {
      roleId: {
        type: "string",
        displayName: "Role ID",
      },
      roleName: {
        type: "string",
        displayName: "Role Name",
      },
      echelon: {
        type: "string",
        displayName: "Typical Echelon",
        description: "Typical rank/grade for this role",
      },
      primaryFunction: {
        type: "string",
        displayName: "Primary Function",
        description: "Key responsibility of this role",
      },
      roleDescription: {
        type: {
          type: "string",
          isLongText: true,
        },
        displayName: "Description",
      },
    },
    implementsInterfaces: [
      {
        implements: roleInterface,
        propertyMapping: [
          { interfaceProperty: "roleId", mapsTo: "roleId" },
          { interfaceProperty: "roleName", mapsTo: "roleName" },
          { interfaceProperty: "echelon", mapsTo: "echelon" },
          { interfaceProperty: "primaryFunction", mapsTo: "primaryFunction" },
          { interfaceProperty: "roleDescription", mapsTo: "roleDescription" },
        ],
      },
    ],
  });

  // ----- PERSON OBJECT -----

  const person = defineObject({
    apiName: "Person",
    displayName: "Person",
    pluralDisplayName: "People",
    description: "Individual filling DDOF role(s)",
    titlePropertyApiName: "personName",
    primaryKeyPropertyApiName: "personId",
    icon: {
      locator: "user",
      color: "#EC4899",
    },
    properties: {
      personId: {
        type: "string",
        displayName: "Person ID",
      },
      personName: {
        type: "string",
        displayName: "Name",
      },
      rank: {
        type: "string",
        displayName: "Rank",
        description: "Military rank if applicable",
      },
      organization: {
        type: "string",
        displayName: "Organization",
        description: "Unit or organization",
      },
      email: {
        type: "string",
        displayName: "Email",
      },
      phone: {
        type: "string",
        displayName: "Phone",
      },
      // Audit fields
      createdAt: { type: "timestamp", displayName: "Created At" },
      createdBy: { type: "string", displayName: "Created By" },
      modifiedAt: { type: "timestamp", displayName: "Modified At" },
      modifiedBy: { type: "string", displayName: "Modified By" },
    },
    implementsInterfaces: [
      {
        implements: personInterface,
        propertyMapping: [
          { interfaceProperty: "personId", mapsTo: "personId" },
          { interfaceProperty: "personName", mapsTo: "personName" },
          { interfaceProperty: "rank", mapsTo: "rank" },
          { interfaceProperty: "organization", mapsTo: "organization" },
          { interfaceProperty: "email", mapsTo: "email" },
          { interfaceProperty: "phone", mapsTo: "phone" },
          { interfaceProperty: "createdAt", mapsTo: "createdAt" },
          { interfaceProperty: "createdBy", mapsTo: "createdBy" },
          { interfaceProperty: "modifiedAt", mapsTo: "modifiedAt" },
          { interfaceProperty: "modifiedBy", mapsTo: "modifiedBy" },
        ],
      },
    ],
  });

  // ----- DATA SOURCE OBJECT -----

  const dataSource = defineObject({
    apiName: "DataSource",
    displayName: "Data Source",
    pluralDisplayName: "Data Sources",
    description: "Authoritative data source accessed in Phase 2",
    titlePropertyApiName: "sourceName",
    primaryKeyPropertyApiName: "sourceId",
    icon: {
      locator: "database",
      color: "#06B6D4",
    },
    properties: {
      sourceId: {
        type: "string",
        displayName: "Source ID",
      },
      sourceName: {
        type: "string",
        displayName: "Source Name",
      },
      sourceSystem: {
        type: "string",
        displayName: "Source System",
        description: "System of origin (e.g., GCSS-A, DCGS-A)",
      },
      isAuthoritative: {
        type: "boolean",
        displayName: "Is Authoritative",
        description: "Verified as Authoritative Data Source (ADS)",
      },
      classification: {
        type: "string",
        displayName: "Classification",
      },
      accessMethod: {
        type: "string",
        displayName: "Access Method",
        description: "API, file, database connection",
      },
      refreshFrequency: {
        type: "string",
        displayName: "Refresh Frequency",
        description: "How often source data updates",
      },
      sourceDescription: {
        type: {
          type: "string",
          isLongText: true,
        },
        displayName: "Description",
      },
      pointOfContact: {
        type: "string",
        displayName: "Point of Contact",
      },
      // Audit fields
      createdAt: { type: "timestamp", displayName: "Created At" },
      createdBy: { type: "string", displayName: "Created By" },
      modifiedAt: { type: "timestamp", displayName: "Modified At" },
      modifiedBy: { type: "string", displayName: "Modified By" },
    },
    implementsInterfaces: [
      {
        implements: dataSourceInterface,
        propertyMapping: [
          { interfaceProperty: "sourceId", mapsTo: "sourceId" },
          { interfaceProperty: "sourceName", mapsTo: "sourceName" },
          { interfaceProperty: "sourceSystem", mapsTo: "sourceSystem" },
          { interfaceProperty: "isAuthoritative", mapsTo: "isAuthoritative" },
          { interfaceProperty: "classification", mapsTo: "classification" },
          { interfaceProperty: "accessMethod", mapsTo: "accessMethod" },
          { interfaceProperty: "refreshFrequency", mapsTo: "refreshFrequency" },
          { interfaceProperty: "sourceDescription", mapsTo: "sourceDescription" },
          { interfaceProperty: "pointOfContact", mapsTo: "pointOfContact" },
          { interfaceProperty: "createdAt", mapsTo: "createdAt" },
          { interfaceProperty: "createdBy", mapsTo: "createdBy" },
          { interfaceProperty: "modifiedAt", mapsTo: "modifiedAt" },
          { interfaceProperty: "modifiedBy", mapsTo: "modifiedBy" },
        ],
      },
    ],
  });

  // ----- REQUIREMENT OBJECT -----

  const requirement = defineObject({
    apiName: "Requirement",
    displayName: "Requirement",
    pluralDisplayName: "Requirements",
    description: "Operational need driving a data product, validated in Phase 1",
    titlePropertyApiName: "problemStatement",
    primaryKeyPropertyApiName: "requirementId",
    icon: {
      locator: "clipboard-list",
      color: "#8B5CF6",
    },
    properties: {
      requirementId: {
        type: "string",
        displayName: "Requirement ID",
      },
      problemStatement: {
        type: "string",
        displayName: "Problem Statement",
        description: "SMART problem statement",
      },
      operationalContext: {
        type: {
          type: "string",
          isLongText: true,
        },
        displayName: "Operational Context",
        description: "Mission context for this requirement",
      },
      missionNeed: {
        type: "string",
        displayName: "Mission Need",
        description: "Tied operational need",
      },
      metlTask: {
        type: "string",
        displayName: "METL Task",
        description: "Associated Mission Essential Task",
      },
      analyticalApproach: {
        type: "string",
        displayName: "Analytical Approach",
        description: "Technical methodology selected",
      },
      targetIocDate: {
        type: "timestamp",
        displayName: "Target IOC Date",
        description: "Required delivery date",
      },
      // SMART criteria tracking
      isSpecific: {
        type: "boolean",
        displayName: "Is Specific",
        description: "SMART: Specific criterion met",
      },
      isMeasurable: {
        type: "boolean",
        displayName: "Is Measurable",
        description: "SMART: Measurable criterion met",
      },
      isAchievable: {
        type: "boolean",
        displayName: "Is Achievable",
        description: "SMART: Achievable criterion met",
      },
      isRelevant: {
        type: "boolean",
        displayName: "Is Relevant",
        description: "SMART: Relevant criterion met",
      },
      isTimeBound: {
        type: "boolean",
        displayName: "Is Time-Bound",
        description: "SMART: Time-bound criterion met",
      },
      requestedByPersonId: {
        type: "string",
        displayName: "Requested By",
        description: "Decision Maker who requested",
      },
      // Audit fields
      createdAt: { type: "timestamp", displayName: "Created At" },
      createdBy: { type: "string", displayName: "Created By" },
      modifiedAt: { type: "timestamp", displayName: "Modified At" },
      modifiedBy: { type: "string", displayName: "Modified By" },
    },
    implementsInterfaces: [
      {
        implements: requirementInterface,
        propertyMapping: [
          { interfaceProperty: "requirementId", mapsTo: "requirementId" },
          { interfaceProperty: "problemStatement", mapsTo: "problemStatement" },
          { interfaceProperty: "operationalContext", mapsTo: "operationalContext" },
          { interfaceProperty: "missionNeed", mapsTo: "missionNeed" },
          { interfaceProperty: "metlTask", mapsTo: "metlTask" },
          { interfaceProperty: "analyticalApproach", mapsTo: "analyticalApproach" },
          { interfaceProperty: "targetIocDate", mapsTo: "targetIocDate" },
          { interfaceProperty: "isSpecific", mapsTo: "isSpecific" },
          { interfaceProperty: "isMeasurable", mapsTo: "isMeasurable" },
          { interfaceProperty: "isAchievable", mapsTo: "isAchievable" },
          { interfaceProperty: "isRelevant", mapsTo: "isRelevant" },
          { interfaceProperty: "isTimeBound", mapsTo: "isTimeBound" },
          { interfaceProperty: "requestedByPersonId", mapsTo: "requestedByPersonId" },
          { interfaceProperty: "createdAt", mapsTo: "createdAt" },
          { interfaceProperty: "createdBy", mapsTo: "createdBy" },
          { interfaceProperty: "modifiedAt", mapsTo: "modifiedAt" },
          { interfaceProperty: "modifiedBy", mapsTo: "modifiedBy" },
        ],
      },
    ],
  });

  // ----- DATA PRODUCT OBJECT -----

  const dataProduct = defineObject({
    apiName: "DataProduct",
    displayName: "Data Product",
    pluralDisplayName: "Data Products",
    description: "Data product moving through the DDOF lifecycle",
    titlePropertyApiName: "productName",
    primaryKeyPropertyApiName: "productId",
    icon: {
      locator: "box",
      color: "#3B82F6",
    },
    properties: {
      productId: {
        type: "string",
        displayName: "Product ID",
      },
      productName: {
        type: "string",
        displayName: "Product Name",
        description: "Name for ADC registration",
      },
      productDescription: {
        type: {
          type: "string",
          isLongText: true,
        },
        displayName: "Description",
      },
      classification: {
        type: "string",
        displayName: "Classification",
        description: "Security classification level",
      },
      status: {
        type: "string",
        displayName: "Status",
        description: "Product lifecycle status",
      },
      currentPhase: {
        type: "string",
        displayName: "Current Phase",
        description: "Current DDOF phase (1-6)",
      },
      currentPhaseStatus: {
        type: "string",
        displayName: "Current Phase Status",
      },
      // Quality
      vaultisScore: {
        type: "double",
        displayName: "VAULTIS-A Score",
        description: "Aggregate quality score",
      },
      lastAssessmentDate: {
        type: "timestamp",
        displayName: "Last Assessment Date",
      },
      // Dates
      iocDate: {
        type: "timestamp",
        displayName: "IOC Date",
        description: "Initial Operational Capability achieved",
      },
      focDate: {
        type: "timestamp",
        displayName: "FOC Date",
        description: "Full Operational Capability achieved",
      },
      lastAccessDate: {
        type: "timestamp",
        displayName: "Last Access Date",
        description: "For retirement tracking (90/180 day rules)",
      },
      // Operations
      refreshFrequency: {
        type: "string",
        displayName: "Refresh Frequency",
        description: "Data refresh schedule",
      },
      accessMethod: {
        type: "string",
        displayName: "Access Method",
        description: "How users access the product",
      },
      // Foreign keys
      requirementId: {
        type: "string",
        displayName: "Requirement ID",
        description: "Linked requirement",
      },
      ownerPersonId: {
        type: "string",
        displayName: "Owner (FDM)",
        description: "Functional Data Manager",
      },
      sponsorPersonId: {
        type: "string",
        displayName: "Sponsor (DM)",
        description: "Decision Maker sponsor",
      },
      // Audit fields
      createdAt: { type: "timestamp", displayName: "Created At" },
      createdBy: { type: "string", displayName: "Created By" },
      modifiedAt: { type: "timestamp", displayName: "Modified At" },
      modifiedBy: { type: "string", displayName: "Modified By" },
    },
    implementsInterfaces: [
      {
        implements: dataProductInterface,
        propertyMapping: [
          { interfaceProperty: "productId", mapsTo: "productId" },
          { interfaceProperty: "productName", mapsTo: "productName" },
          { interfaceProperty: "productDescription", mapsTo: "productDescription" },
          { interfaceProperty: "classification", mapsTo: "classification" },
          { interfaceProperty: "status", mapsTo: "status" },
          { interfaceProperty: "currentPhase", mapsTo: "currentPhase" },
          { interfaceProperty: "currentPhaseStatus", mapsTo: "currentPhaseStatus" },
          { interfaceProperty: "vaultisScore", mapsTo: "vaultisScore" },
          { interfaceProperty: "lastAssessmentDate", mapsTo: "lastAssessmentDate" },
          { interfaceProperty: "iocDate", mapsTo: "iocDate" },
          { interfaceProperty: "focDate", mapsTo: "focDate" },
          { interfaceProperty: "lastAccessDate", mapsTo: "lastAccessDate" },
          { interfaceProperty: "refreshFrequency", mapsTo: "refreshFrequency" },
          { interfaceProperty: "accessMethod", mapsTo: "accessMethod" },
          { interfaceProperty: "requirementId", mapsTo: "requirementId" },
          { interfaceProperty: "ownerPersonId", mapsTo: "ownerPersonId" },
          { interfaceProperty: "sponsorPersonId", mapsTo: "sponsorPersonId" },
          { interfaceProperty: "createdAt", mapsTo: "createdAt" },
          { interfaceProperty: "createdBy", mapsTo: "createdBy" },
          { interfaceProperty: "modifiedAt", mapsTo: "modifiedAt" },
          { interfaceProperty: "modifiedBy", mapsTo: "modifiedBy" },
        ],
      },
    ],
  });

  // ============================================================================
  // OBJECT TYPES - Lifecycle & Governance Records
  // ============================================================================

  // ----- PHASE INSTANCE -----

  const phaseInstance = defineObject({
    apiName: "PhaseInstance",
    displayName: "Phase Instance",
    pluralDisplayName: "Phase Instances",
    description: "Execution of a phase for a specific data product",
    titlePropertyApiName: "instanceId",
    primaryKeyPropertyApiName: "instanceId",
    icon: {
      locator: "play-circle",
      color: "#10B981",
    },
    properties: {
      instanceId: {
        type: "string",
        displayName: "Instance ID",
      },
      productId: {
        type: "string",
        displayName: "Product ID",
      },
      phaseNumber: {
        type: "integer",
        displayName: "Phase Number",
      },
      startDate: {
        type: "timestamp",
        displayName: "Start Date",
      },
      endDate: {
        type: "timestamp",
        displayName: "End Date",
      },
      status: {
        type: "string",
        displayName: "Status",
        description: "InProgress, Passed, Failed, Blocked",
      },
      extensionApproved: {
        type: "boolean",
        displayName: "Extension Approved",
        description: "C2DAO granted extension",
      },
      extensionJustification: {
        type: {
          type: "string",
          isLongText: true,
        },
        displayName: "Extension Justification",
      },
      durationDays: {
        type: "integer",
        displayName: "Duration (Days)",
        description: "Actual duration of this phase instance",
      },
      // Audit fields
      createdAt: { type: "timestamp", displayName: "Created At" },
      createdBy: { type: "string", displayName: "Created By" },
      modifiedAt: { type: "timestamp", displayName: "Modified At" },
      modifiedBy: { type: "string", displayName: "Modified By" },
    },
    implementsInterfaces: [
      {
        implements: auditableInterface,
        propertyMapping: [
          { interfaceProperty: "createdAt", mapsTo: "createdAt" },
          { interfaceProperty: "createdBy", mapsTo: "createdBy" },
          { interfaceProperty: "modifiedAt", mapsTo: "modifiedAt" },
          { interfaceProperty: "modifiedBy", mapsTo: "modifiedBy" },
        ],
      },
    ],
  });

  // ----- GATE EVALUATION -----

  const gateEvaluation = defineObject({
    apiName: "GateEvaluation",
    displayName: "Gate Evaluation",
    pluralDisplayName: "Gate Evaluations",
    description: "Evaluation of a quality gate for a specific data product",
    titlePropertyApiName: "evaluationId",
    primaryKeyPropertyApiName: "evaluationId",
    icon: {
      locator: "clipboard-check",
      color: "#F59E0B",
    },
    properties: {
      evaluationId: {
        type: "string",
        displayName: "Evaluation ID",
      },
      productId: {
        type: "string",
        displayName: "Product ID",
      },
      gateId: {
        type: "string",
        displayName: "Gate ID",
      },
      evaluationDate: {
        type: "timestamp",
        displayName: "Evaluation Date",
      },
      passed: {
        type: "boolean",
        displayName: "Passed",
      },
      overrideApplied: {
        type: "boolean",
        displayName: "Override Applied",
        description: "C2DAO override used",
      },
      overrideJustification: {
        type: {
          type: "string",
          isLongText: true,
        },
        displayName: "Override Justification",
      },
      approverPersonId: {
        type: "string",
        displayName: "Approver",
        description: "C2DAO who approved",
      },
      evaluationNotes: {
        type: {
          type: "string",
          isLongText: true,
        },
        displayName: "Notes",
      },
      // Audit fields
      createdAt: { type: "timestamp", displayName: "Created At" },
      createdBy: { type: "string", displayName: "Created By" },
    },
    implementsInterfaces: [
      {
        implements: auditableInterface,
        propertyMapping: [
          { interfaceProperty: "createdAt", mapsTo: "createdAt" },
          { interfaceProperty: "createdBy", mapsTo: "createdBy" },
          { interfaceProperty: "modifiedAt", mapsTo: "createdAt" },
          { interfaceProperty: "modifiedBy", mapsTo: "createdBy" },
        ],
      },
    ],
  });

  // ----- VAULTIS ASSESSMENT -----

  const vaultisAssessment = defineObject({
    apiName: "VAULTISAssessment",
    displayName: "VAULTIS-A Assessment",
    pluralDisplayName: "VAULTIS-A Assessments",
    description: "Quality assessment against the VAULTIS-A framework",
    titlePropertyApiName: "assessmentId",
    primaryKeyPropertyApiName: "assessmentId",
    icon: {
      locator: "award",
      color: "#84CC16",
    },
    properties: {
      assessmentId: {
        type: "string",
        displayName: "Assessment ID",
      },
      productId: {
        type: "string",
        displayName: "Product ID",
      },
      assessmentDate: {
        type: "timestamp",
        displayName: "Assessment Date",
      },
      // Individual dimension scores (DDOF Playbook v2.2 VAULTIS-A definitions)
      visibleScore: {
        type: "double",
        displayName: "Visible Score",
        description: "Clearly marked and discoverable (target 100% visibility in catalog/product)",
      },
      accessibleScore: {
        type: "double",
        displayName: "Accessible Score",
        description: "Usable by authorized personnel (target 99% access rate for authorized users)",
      },
      understandableScore: {
        type: "double",
        displayName: "Understandable Score",
        description: "Clearly documented and interpretable (target complete metadata and user guide)",
      },
      linkedScore: {
        type: "double",
        displayName: "Linked Score",
        description: "Relationships maintained (target 100% linkage to sources/products)",
      },
      trustedScore: {
        type: "double",
        displayName: "Trusted Score",
        description: "Provenance and quality validated (target 95%+ accuracy, sponsor sign-off)",
      },
      interoperableScore: {
        type: "double",
        displayName: "Interoperable Score",
        description: "Usable across platforms/systems (target 90%+ compatibility with approved platforms)",
      },
      secureScore: {
        type: "double",
        displayName: "Secure Score",
        description: "Protected per classification (target 100% compliance with security policy)",
      },
      auditableScore: {
        type: "double",
        displayName: "Auditable Score",
        description: "Complete lineage available (target full provenance and access logs)",
      },
      // Aggregate
      aggregateScore: {
        type: "double",
        displayName: "Aggregate Score",
        description: "Overall VAULTIS-A score",
      },
      passesThreshold: {
        type: "boolean",
        displayName: "Passes Threshold",
        description: "Meets 85% minimum for gate passage",
      },
      assessorPersonId: {
        type: "string",
        displayName: "Assessor",
      },
      assessmentNotes: {
        type: {
          type: "string",
          isLongText: true,
        },
        displayName: "Assessment Notes",
      },
      // Audit fields
      createdAt: { type: "timestamp", displayName: "Created At" },
      createdBy: { type: "string", displayName: "Created By" },
    },
  });

  // ----- GOVERNANCE CONTROL -----

  const governanceControl = defineObject({
    apiName: "GovernanceControl",
    displayName: "Governance Control",
    pluralDisplayName: "Governance Controls",
    description: "Required governance control implemented on a data product",
    titlePropertyApiName: "controlType",
    primaryKeyPropertyApiName: "controlId",
    icon: {
      locator: "lock",
      color: "#EF4444",
    },
    properties: {
      controlId: {
        type: "string",
        displayName: "Control ID",
      },
      productId: {
        type: "string",
        displayName: "Product ID",
      },
      controlType: {
        type: "string",
        displayName: "Control Type",
        description: "ABAC, Audit, Lineage, Classification, Ownership",
      },
      controlDescription: {
        type: "string",
        displayName: "Description",
      },
      isImplemented: {
        type: "boolean",
        displayName: "Is Implemented",
      },
      verificationDate: {
        type: "timestamp",
        displayName: "Verification Date",
      },
      verifiedByPersonId: {
        type: "string",
        displayName: "Verified By",
      },
      implementationNotes: {
        type: {
          type: "string",
          isLongText: true,
        },
        displayName: "Implementation Notes",
      },
      // Audit fields
      createdAt: { type: "timestamp", displayName: "Created At" },
      createdBy: { type: "string", displayName: "Created By" },
      modifiedAt: { type: "timestamp", displayName: "Modified At" },
      modifiedBy: { type: "string", displayName: "Modified By" },
    },
  });

  // ----- ADC REGISTRATION -----

  const adcRegistration = defineObject({
    apiName: "ADCRegistration",
    displayName: "ADC Registration",
    pluralDisplayName: "ADC Registrations",
    description: "Army Data Catalog registration record",
    titlePropertyApiName: "registrationId",
    primaryKeyPropertyApiName: "registrationId",
    icon: {
      locator: "book-open",
      color: "#6366F1",
    },
    properties: {
      registrationId: {
        type: "string",
        displayName: "Registration ID",
      },
      productId: {
        type: "string",
        displayName: "Product ID",
      },
      registrationDate: {
        type: "timestamp",
        displayName: "Registration Date",
      },
      catalogUrl: {
        type: "string",
        displayName: "Catalog URL",
        description: "ADC entry URL",
      },
      metadataComplete: {
        type: "boolean",
        displayName: "Metadata Complete",
        description: "All required fields populated",
      },
      lineageDocumented: {
        type: "boolean",
        displayName: "Lineage Documented",
        description: "Full provenance recorded",
      },
      registeredByPersonId: {
        type: "string",
        displayName: "Registered By",
      },
      // Audit fields
      createdAt: { type: "timestamp", displayName: "Created At" },
      createdBy: { type: "string", displayName: "Created By" },
      modifiedAt: { type: "timestamp", displayName: "Modified At" },
      modifiedBy: { type: "string", displayName: "Modified By" },
    },
  });

  // ----- TEST RESULT -----

  const testResult = defineObject({
    apiName: "TestResult",
    displayName: "Test Result",
    pluralDisplayName: "Test Results",
    description: "Results from Phase 5 testing activities",
    titlePropertyApiName: "testId",
    primaryKeyPropertyApiName: "testId",
    icon: {
      locator: "beaker",
      color: "#14B8A6",
    },
    properties: {
      testId: {
        type: "string",
        displayName: "Test ID",
      },
      productId: {
        type: "string",
        displayName: "Product ID",
      },
      testType: {
        type: "string",
        displayName: "Test Type",
        description: "Functional, DataQuality, Security, UAT",
      },
      testDate: {
        type: "timestamp",
        displayName: "Test Date",
      },
      passed: {
        type: "boolean",
        displayName: "Passed",
      },
      defectsFound: {
        type: "integer",
        displayName: "Defects Found",
      },
      criticalDefects: {
        type: "integer",
        displayName: "Critical Defects",
      },
      testerPersonId: {
        type: "string",
        displayName: "Tester",
      },
      testNotes: {
        type: {
          type: "string",
          isLongText: true,
        },
        displayName: "Test Notes",
      },
      // For UAT
      sponsorSignoff: {
        type: "boolean",
        displayName: "Sponsor Sign-off",
        description: "End-user validation received",
      },
      signoffDate: {
        type: "timestamp",
        displayName: "Sign-off Date",
      },
      // Audit fields
      createdAt: { type: "timestamp", displayName: "Created At" },
      createdBy: { type: "string", displayName: "Created By" },
    },
  });

  // ----- AUDIT EVENT -----

  const auditEvent = defineObject({
    apiName: "AuditEvent",
    displayName: "Audit Event",
    pluralDisplayName: "Audit Events",
    description: "Immutable audit trail entry per Genesis Directive 3",
    titlePropertyApiName: "eventId",
    primaryKeyPropertyApiName: "eventId",
    icon: {
      locator: "scroll",
      color: "#78716C",
    },
    properties: {
      eventId: {
        type: "string",
        displayName: "Event ID",
      },
      productId: {
        type: "string",
        displayName: "Product ID",
      },
      eventType: {
        type: "string",
        displayName: "Event Type",
        description: "Access, Change, Approval, Denial, Gate events",
      },
      eventTimestamp: {
        type: "timestamp",
        displayName: "Timestamp",
      },
      actorPersonId: {
        type: "string",
        displayName: "Actor",
        description: "Who performed the action",
      },
      action: {
        type: "string",
        displayName: "Action",
        description: "What was done",
      },
      outcome: {
        type: "string",
        displayName: "Outcome",
        description: "Result of action",
      },
      isAccessDenial: {
        type: "boolean",
        displayName: "Is Access Denial",
        description: "Fail-closed denial logged (per Genesis)",
      },
      targetEntityType: {
        type: "string",
        displayName: "Target Entity Type",
      },
      targetEntityId: {
        type: "string",
        displayName: "Target Entity ID",
      },
      eventDetails: {
        type: {
          type: "string",
          isLongText: true,
        },
        displayName: "Event Details",
      },
    },
    // Audit events are append-only stream data
    datasources: [{
      type: "stream",
      retentionPeriod: "P2555D", // 7 years retention for compliance
    }],
  });

  // ============================================================================
  // INTERFACE LINK CONSTRAINTS
  // ============================================================================

  // Person relationships via interface
  const dataProductToOwner = defineInterfaceLinkConstraint({
    apiName: "dataProductToOwner",
    from: dataProductInterface,
    toOne: personInterface,
  });

  const dataProductToSponsor = defineInterfaceLinkConstraint({
    apiName: "dataProductToSponsor",
    from: dataProductInterface,
    toOne: personInterface,
  });

  const dataProductToRequirement = defineInterfaceLinkConstraint({
    apiName: "dataProductToRequirement",
    from: dataProductInterface,
    toOne: requirementInterface,
  });

  const requirementToRequestor = defineInterfaceLinkConstraint({
    apiName: "requirementToRequestor",
    from: requirementInterface,
    toOne: personInterface,
  });

  const dataProductToDataSources = defineInterfaceLinkConstraint({
    apiName: "dataProductToDataSources",
    from: dataProductInterface,
    toMany: dataSourceInterface,
  });

  const personToRoles = defineInterfaceLinkConstraint({
    apiName: "personToRoles",
    from: personInterface,
    toMany: roleInterface,
  });

  // ============================================================================
  // OBJECT LINK TYPES
  // ============================================================================

  // DataProduct to concrete objects
  const productToPhaseInstances = defineLink({
    apiName: "productToPhaseInstances",
    one: {
      object: dataProduct,
      metadata: {
        apiName: "phaseInstances",
        displayName: "Phase Instance",
        pluralDisplayName: "Phase Instances",
      },
    },
    toMany: {
      object: phaseInstance,
      metadata: {
        apiName: "dataProduct",
        displayName: "Data Product",
        pluralDisplayName: "Data Products",
      },
    },
    manyForeignKeyProperty: "productId",
  });

  const phaseInstanceToPhase = defineLink({
    apiName: "phaseInstanceToPhase",
    one: {
      object: phase,
      metadata: {
        apiName: "phaseInstances",
        displayName: "Phase Instance",
        pluralDisplayName: "Phase Instances",
      },
    },
    toMany: {
      object: phaseInstance,
      metadata: {
        apiName: "phase",
        displayName: "Phase",
        pluralDisplayName: "Phases",
      },
    },
    manyForeignKeyProperty: "phaseNumber",
  });

  const productToGateEvaluations = defineLink({
    apiName: "productToGateEvaluations",
    one: {
      object: dataProduct,
      metadata: {
        apiName: "gateEvaluations",
        displayName: "Gate Evaluation",
        pluralDisplayName: "Gate Evaluations",
      },
    },
    toMany: {
      object: gateEvaluation,
      metadata: {
        apiName: "dataProduct",
        displayName: "Data Product",
        pluralDisplayName: "Data Products",
      },
    },
    manyForeignKeyProperty: "productId",
  });

  const gateEvaluationToGate = defineLink({
    apiName: "gateEvaluationToGate",
    one: {
      object: qualityGate,
      metadata: {
        apiName: "evaluations",
        displayName: "Evaluation",
        pluralDisplayName: "Evaluations",
      },
    },
    toMany: {
      object: gateEvaluation,
      metadata: {
        apiName: "qualityGate",
        displayName: "Quality Gate",
        pluralDisplayName: "Quality Gates",
      },
    },
    manyForeignKeyProperty: "gateId",
  });

  const gateEvaluationToApprover = defineLink({
    apiName: "gateEvaluationToApprover",
    one: {
      object: person,
      metadata: {
        apiName: "approvedGateEvaluations",
        displayName: "Approved Gate Evaluation",
        pluralDisplayName: "Approved Gate Evaluations",
      },
    },
    toMany: {
      object: gateEvaluation,
      metadata: {
        apiName: "approver",
        displayName: "Approver",
        pluralDisplayName: "Approvers",
      },
    },
    manyForeignKeyProperty: "approverPersonId",
  });

  const gateToCriteria = defineLink({
    apiName: "gateToCriteria",
    one: {
      object: qualityGate,
      metadata: {
        apiName: "exitCriteria",
        displayName: "Exit Criterion",
        pluralDisplayName: "Exit Criteria",
      },
    },
    toMany: {
      object: exitCriterion,
      metadata: {
        apiName: "qualityGate",
        displayName: "Quality Gate",
        pluralDisplayName: "Quality Gates",
      },
    },
    manyForeignKeyProperty: "gateId",
  });

  const gateToPhase = defineLink({
    apiName: "gateToPhase",
    one: {
      object: phase,
      metadata: {
        apiName: "qualityGate",
        displayName: "Quality Gate",
        pluralDisplayName: "Quality Gates",
      },
    },
    toMany: {
      object: qualityGate,
      metadata: {
        apiName: "phase",
        displayName: "Phase",
        pluralDisplayName: "Phases",
      },
    },
    manyForeignKeyProperty: "phaseNumber",
  });

  const productToAssessments = defineLink({
    apiName: "productToAssessments",
    one: {
      object: dataProduct,
      metadata: {
        apiName: "vaultisAssessments",
        displayName: "VAULTIS-A Assessment",
        pluralDisplayName: "VAULTIS-A Assessments",
      },
    },
    toMany: {
      object: vaultisAssessment,
      metadata: {
        apiName: "dataProduct",
        displayName: "Data Product",
        pluralDisplayName: "Data Products",
      },
    },
    manyForeignKeyProperty: "productId",
  });

  const productToControls = defineLink({
    apiName: "productToControls",
    one: {
      object: dataProduct,
      metadata: {
        apiName: "governanceControls",
        displayName: "Governance Control",
        pluralDisplayName: "Governance Controls",
      },
    },
    toMany: {
      object: governanceControl,
      metadata: {
        apiName: "dataProduct",
        displayName: "Data Product",
        pluralDisplayName: "Data Products",
      },
    },
    manyForeignKeyProperty: "productId",
  });

  const productToRegistration = defineLink({
    apiName: "productToRegistration",
    one: {
      object: dataProduct,
      metadata: {
        apiName: "adcRegistration",
        displayName: "ADC Registration",
        pluralDisplayName: "ADC Registrations",
      },
    },
    toMany: {
      object: adcRegistration,
      metadata: {
        apiName: "dataProduct",
        displayName: "Data Product",
        pluralDisplayName: "Data Products",
      },
    },
    manyForeignKeyProperty: "productId",
  });

  const productToTestResults = defineLink({
    apiName: "productToTestResults",
    one: {
      object: dataProduct,
      metadata: {
        apiName: "testResults",
        displayName: "Test Result",
        pluralDisplayName: "Test Results",
      },
    },
    toMany: {
      object: testResult,
      metadata: {
        apiName: "dataProduct",
        displayName: "Data Product",
        pluralDisplayName: "Data Products",
      },
    },
    manyForeignKeyProperty: "productId",
  });

  const productToAuditEvents = defineLink({
    apiName: "productToAuditEvents",
    one: {
      object: dataProduct,
      metadata: {
        apiName: "auditEvents",
        displayName: "Audit Event",
        pluralDisplayName: "Audit Events",
      },
    },
    toMany: {
      object: auditEvent,
      metadata: {
        apiName: "dataProduct",
        displayName: "Data Product",
        pluralDisplayName: "Data Products",
      },
    },
    manyForeignKeyProperty: "productId",
  });

  const personToAuditEvents = defineLink({
    apiName: "personToAuditEvents",
    one: {
      object: person,
      metadata: {
        apiName: "performedAuditEvents",
        displayName: "Performed Audit Event",
        pluralDisplayName: "Performed Audit Events",
      },
    },
    toMany: {
      object: auditEvent,
      metadata: {
        apiName: "actor",
        displayName: "Actor",
        pluralDisplayName: "Actors",
      },
    },
    manyForeignKeyProperty: "actorPersonId",
  });

  // ============================================================================
  // ACTIONS - Interface-based for flexibility
  // ============================================================================

  // DataProduct actions (interface-based)
  const createDataProduct = defineCreateInterfaceObjectAction({
    interfaceType: dataProductInterface,
  });

  const modifyDataProduct = defineModifyInterfaceObjectAction({
    interfaceType: dataProductInterface,
  });

  // Requirement actions (interface-based)
  const createRequirement = defineCreateInterfaceObjectAction({
    interfaceType: requirementInterface,
  });

  const modifyRequirement = defineModifyInterfaceObjectAction({
    interfaceType: requirementInterface,
  });

  // Person actions (interface-based)
  const createPerson = defineCreateInterfaceObjectAction({
    interfaceType: personInterface,
  });

  const modifyPerson = defineModifyInterfaceObjectAction({
    interfaceType: personInterface,
  });

  // DataSource actions (interface-based)
  const createDataSource = defineCreateInterfaceObjectAction({
    interfaceType: dataSourceInterface,
  });

  const modifyDataSource = defineModifyInterfaceObjectAction({
    interfaceType: dataSourceInterface,
  });

  // Role actions (interface-based)
  const createRole = defineCreateInterfaceObjectAction({
    interfaceType: roleInterface,
  });

  const modifyRole = defineModifyInterfaceObjectAction({
    interfaceType: roleInterface,
  });

  // Concrete object actions
  const createPhaseInstance = defineCreateObjectAction({
    objectType: phaseInstance,
  });

  const modifyPhaseInstance = defineModifyObjectAction({
    objectType: phaseInstance,
  });

  const createGateEvaluation = defineCreateObjectAction({
    objectType: gateEvaluation,
  });

  const createVAULTISAssessment = defineCreateObjectAction({
    objectType: vaultisAssessment,
  });

  const createGovernanceControl = defineCreateObjectAction({
    objectType: governanceControl,
  });

  const modifyGovernanceControl = defineModifyObjectAction({
    objectType: governanceControl,
  });

  const createTestResult = defineCreateObjectAction({
    objectType: testResult,
  });

  const createADCRegistration = defineCreateObjectAction({
    objectType: adcRegistration,
  });

  const modifyADCRegistration = defineModifyObjectAction({
    objectType: adcRegistration,
  });

}, "./generated-ontology");
