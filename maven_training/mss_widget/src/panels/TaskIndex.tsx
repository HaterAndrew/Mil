import React, { useState, useMemo } from "react";

// ── TYPES ──────────────────────────────────────────────────────
interface TmRef {
  id: string;
  label: string;
}

interface Task {
  task: string;
  tms: TmRef[];
  chapter: string;
  cat: string[];
}

interface Section {
  id: string;
  label: string;
}

interface Props {
  showPanel: (id: string) => void;
}

// ── CONSTANTS ─────────────────────────────────────────────────
const MEDIA_BASE =
  "https://mss.data.mil/mio/api/mediaSet/ri.mio.main.media-set.9c297238-56bf-46d4-881a-db21-dcee1c/file/";

const PDF: Record<string, string> = {
  "tm-10":  `${MEDIA_BASE}TM_10_MAVEN_USER.pdf`,
  "tm-20":  `${MEDIA_BASE}TM_20_BUILDER.pdf`,
  "tm-30":  `${MEDIA_BASE}TM_30_ADVANCED_BUILDER.pdf`,
  "tm-40g": `${MEDIA_BASE}TM_40G_ORSA.pdf`,
  "tm-40h": `${MEDIA_BASE}TM_40H_AI_ENGINEER.pdf`,
  "tm-40i": `${MEDIA_BASE}TM_40I_ML_ENGINEER.pdf`,
  "tm-40j": `${MEDIA_BASE}TM_40J_PROGRAM_MANAGER.pdf`,
  "tm-40k": `${MEDIA_BASE}TM_40K_KNOWLEDGE_MANAGER.pdf`,
  "tm-40l": `${MEDIA_BASE}TM_40L_SOFTWARE_ENGINEER.pdf`,
  "tm-50g": `${MEDIA_BASE}TM_50G_ORSA_ADVANCED.pdf`,
  "tm-50h": `${MEDIA_BASE}TM_50H_AI_ENGINEER_ADVANCED.pdf`,
  "tm-50i": `${MEDIA_BASE}TM_50I_ML_ENGINEER_ADVANCED.pdf`,
  "tm-50j": `${MEDIA_BASE}TM_50J_PROGRAM_MANAGER_ADVANCED.pdf`,
  "tm-50k": `${MEDIA_BASE}TM_50K_KNOWLEDGE_MANAGER_ADVANCED.pdf`,
  "tm-50l": `${MEDIA_BASE}TM_50L_SOFTWARE_ENGINEER_ADVANCED.pdf`,
};

const SECTIONS: Section[] = [
  { id: "setup",      label: "Setup & Access" },
  { id: "navigation", label: "Navigation & Browsing" },
  { id: "data",       label: "Data Viewing, Analysis & Export" },
  { id: "build",      label: "No-Code Building (Pipelines & Workshop)" },
  { id: "ontology",   label: "Ontology & Data Modeling" },
  { id: "aip",        label: "AIP & AI Workflows" },
  { id: "code",       label: "Code, SDK & Transforms" },
  { id: "ml",         label: "Machine Learning" },
  { id: "pm",         label: "Program Management" },
  { id: "km",         label: "Knowledge Management" },
  { id: "governance", label: "Governance & Security" },
  { id: "advanced",   label: "Advanced / Expert" },
];

const FILTER_PILLS: { filter: string; label: string }[] = [
  { filter: "all",        label: "All" },
  { filter: "setup",      label: "Setup & Access" },
  { filter: "navigation", label: "Navigation" },
  { filter: "data",       label: "Data & Analysis" },
  { filter: "build",      label: "No-Code Building" },
  { filter: "ontology",   label: "Ontology & Modeling" },
  { filter: "aip",        label: "AIP & AI" },
  { filter: "code",       label: "Code & SDK" },
  { filter: "ml",         label: "Machine Learning" },
  { filter: "pm",         label: "Program Mgmt" },
  { filter: "km",         label: "Knowledge Mgmt" },
  { filter: "governance", label: "Governance & Security" },
  { filter: "advanced",   label: "Advanced / Expert" },
];

const TASKS: Task[] = [
  // ── SETUP & ACCESS ──────────────────────────────────────────
  { task: "Set up account before first login", tms: [{id:"tm-10",label:"TM-10"}], chapter: "Ch 2", cat: ["setup"] },
  { task: "Log in to MSS with CAC", tms: [{id:"tm-10",label:"TM-10"}], chapter: "Ch 2", cat: ["setup"] },
  { task: "Log out of MSS", tms: [{id:"tm-10",label:"TM-10"}], chapter: "Ch 2", cat: ["setup"] },
  { task: "Verify your own markings and access level", tms: [{id:"tm-10",label:"TM-10"}], chapter: "Ch 6", cat: ["setup","governance"] },
  { task: "Configure new ORSA Code Workspace", tms: [{id:"tm-40g",label:"TM-40G"}], chapter: "Ch 2", cat: ["setup","code"] },
  { task: "Create and configure Code Workspace", tms: [{id:"tm-40i",label:"TM-40I"}], chapter: "Ch 2", cat: ["setup","code"] },
  { task: "Manage packages in Code Workspace", tms: [{id:"tm-40g",label:"TM-40G"},{id:"tm-40i",label:"TM-40I"}], chapter: "Ch 2", cat: ["setup","code"] },
  { task: "Manage compute and environment resources", tms: [{id:"tm-40i",label:"TM-40I"}], chapter: "Ch 2", cat: ["setup","code"] },
  { task: "Configure project access and permissions", tms: [{id:"tm-20",label:"TM-20"}], chapter: "Ch 2", cat: ["setup","governance"] },

  // ── NAVIGATION ──────────────────────────────────────────────
  { task: "Navigate the MSS home screen", tms: [{id:"tm-10",label:"TM-10"}], chapter: "Ch 2", cat: ["navigation"] },
  { task: "Find a resource using search", tms: [{id:"tm-10",label:"TM-10"}], chapter: "Ch 2", cat: ["navigation"] },
  { task: "Navigate using Compass file browser", tms: [{id:"tm-10",label:"TM-10"}], chapter: "Ch 2", cat: ["navigation"] },
  { task: "Bookmark a frequently used resource", tms: [{id:"tm-10",label:"TM-10"}], chapter: "Ch 2", cat: ["navigation"] },
  { task: "Open a Workshop application", tms: [{id:"tm-10",label:"TM-10"}], chapter: "Ch 3", cat: ["navigation"] },
  { task: "Navigate between modules and pages", tms: [{id:"tm-10",label:"TM-10"}], chapter: "Ch 3", cat: ["navigation"] },
  { task: "Create a project and manage folder structure", tms: [{id:"tm-20",label:"TM-20"}], chapter: "Ch 2", cat: ["navigation","setup"] },

  // ── DATA VIEWING & EXPORT ────────────────────────────────────
  { task: "Read and interpret a dashboard", tms: [{id:"tm-10",label:"TM-10"}], chapter: "Ch 3", cat: ["data"] },
  { task: "Apply filters to a dashboard", tms: [{id:"tm-10",label:"TM-10"}], chapter: "Ch 3", cat: ["data"] },
  { task: "View and read a dataset", tms: [{id:"tm-10",label:"TM-10"}], chapter: "Ch 4", cat: ["data"] },
  { task: "Export data from a Workshop application", tms: [{id:"tm-10",label:"TM-10"}], chapter: "Ch 4", cat: ["data"] },
  { task: "Verify data currency and source", tms: [{id:"tm-10",label:"TM-10"}], chapter: "Ch 4", cat: ["data"] },
  { task: "Submit data using an action form", tms: [{id:"tm-10",label:"TM-10"}], chapter: "Ch 4", cat: ["data"] },
  { task: "Execute an action button", tms: [{id:"tm-10",label:"TM-10"}], chapter: "Ch 4", cat: ["data"] },
  { task: "Use Contour for no-code analysis", tms: [{id:"tm-10",label:"TM-10"},{id:"tm-20",label:"TM-20"}], chapter: "Ch 5", cat: ["data"] },
  { task: "Use Quiver to explore ontology objects", tms: [{id:"tm-10",label:"TM-10"},{id:"tm-20",label:"TM-20"}], chapter: "Ch 5", cat: ["data"] },
  { task: "Build saved analysis in Contour", tms: [{id:"tm-20",label:"TM-20"}], chapter: "Ch 6", cat: ["data"] },
  { task: "Build complex aggregations in Contour", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 5", cat: ["data"] },
  { task: "Create pivot tables in Contour", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 5", cat: ["data"] },
  { task: "Calculate derived metrics in Contour", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 5", cat: ["data"] },
  { task: "Build multi-object Quiver dashboards", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 5", cat: ["data"] },
  { task: "Connect to Foundry datasets in notebook", tms: [{id:"tm-40i",label:"TM-40I"}], chapter: "Ch 2", cat: ["data","code"] },
  { task: "Write output datasets back to Foundry", tms: [{id:"tm-40g",label:"TM-40G"},{id:"tm-40i",label:"TM-40I"}], chapter: "Ch 2", cat: ["data","code"] },
  { task: "Build readiness forecast dashboard in Quiver", tms: [{id:"tm-40g",label:"TM-40G"}], chapter: "Ch 5", cat: ["data"] },
  { task: "Build analytical Contour workbook for COA support", tms: [{id:"tm-40g",label:"TM-40G"}], chapter: "Ch 5", cat: ["data"] },

  // ── NO-CODE PIPELINE BUILDING ────────────────────────────────
  { task: "Create a Pipeline Builder pipeline", tms: [{id:"tm-20",label:"TM-20"}], chapter: "Ch 3", cat: ["build"] },
  { task: "Connect a data source in Pipeline Builder", tms: [{id:"tm-20",label:"TM-20"}], chapter: "Ch 3", cat: ["build"] },
  { task: "Transform data: filter, select, rename columns", tms: [{id:"tm-20",label:"TM-20"}], chapter: "Ch 3", cat: ["build"] },
  { task: "Join datasets on a shared key", tms: [{id:"tm-20",label:"TM-20"}], chapter: "Ch 3", cat: ["build"] },
  { task: "Aggregate and summarize data", tms: [{id:"tm-20",label:"TM-20"}], chapter: "Ch 3", cat: ["build"] },
  { task: "Append or union multiple datasets", tms: [{id:"tm-20",label:"TM-20"}], chapter: "Ch 3", cat: ["build"] },
  { task: "Deduplicate rows and handle nulls", tms: [{id:"tm-20",label:"TM-20"}], chapter: "Ch 3", cat: ["build"] },
  { task: "Perform multi-source joins (inner/outer/left)", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 3", cat: ["build"] },
  { task: "Execute group-by aggregation", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 3", cat: ["build"] },
  { task: "Create calculated/derived columns", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 3", cat: ["build"] },
  { task: "Perform pivot and unpivot operations", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 3", cat: ["build"] },
  { task: "Partition datasets by region or classification", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 3", cat: ["build","governance"] },
  { task: "Handle null value logic", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 3", cat: ["build"] },

  // ── WORKSHOP (UI BUILDING) ───────────────────────────────────
  { task: "Build a Workshop application with widgets", tms: [{id:"tm-20",label:"TM-20"}], chapter: "Ch 5", cat: ["build"] },
  { task: "Configure dashboard charts and metric tiles", tms: [{id:"tm-20",label:"TM-20"}], chapter: "Ch 5", cat: ["build"] },
  { task: "Build tables with filtering and sorting", tms: [{id:"tm-20",label:"TM-20"}], chapter: "Ch 5", cat: ["build"] },
  { task: "Build form widgets for data entry", tms: [{id:"tm-20",label:"TM-20"}], chapter: "Ch 5", cat: ["build"] },
  { task: "Create object set widgets", tms: [{id:"tm-20",label:"TM-20"}], chapter: "Ch 5", cat: ["build"] },
  { task: "Configure filter controls", tms: [{id:"tm-20",label:"TM-20"}], chapter: "Ch 5", cat: ["build"] },
  { task: "Create application variables", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 2", cat: ["build"] },
  { task: "Connect widgets to variables", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 2", cat: ["build"] },
  { task: "Implement variable chaining", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 2", cat: ["build"] },
  { task: "Configure cascading dropdowns", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 2", cat: ["build"] },
  { task: "Apply conditional visibility rules", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 2", cat: ["build"] },
  { task: "Configure conditional widget content", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 2", cat: ["build"] },
  { task: "Build multi-page application architecture", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 2", cat: ["build"] },
  { task: "Design complex tables with computed columns", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 2", cat: ["build"] },
  { task: "Configure nested filters and dynamic object sets", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 2", cat: ["build"] },
  { task: "Configure advanced map widgets", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 2", cat: ["build"] },
  { task: "Build sprint board in Workshop", tms: [{id:"tm-40j",label:"TM-40J"}], chapter: "Ch 4", cat: ["build","pm"] },
  { task: "Build commander-facing project dashboard", tms: [{id:"tm-40j",label:"TM-40J"}], chapter: "Ch 4", cat: ["build","pm"] },
  { task: "Build SME directory application", tms: [{id:"tm-40k",label:"TM-40K"}], chapter: "Ch 4", cat: ["build","km"] },
  { task: "Build knowledge browser application", tms: [{id:"tm-40k",label:"TM-40K"}], chapter: "Ch 3", cat: ["build","km"] },
  { task: "Build a Slate application", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 7", cat: ["build","code"] },
  { task: "Integrate Foundry API from Slate", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 7", cat: ["build","code"] },

  // ── ONTOLOGY & DATA MODELING ─────────────────────────────────
  { task: "Create an Object Type via Ontology UI", tms: [{id:"tm-20",label:"TM-20"}], chapter: "Ch 4", cat: ["ontology"] },
  { task: "Add and configure properties on Object Type", tms: [{id:"tm-20",label:"TM-20"}], chapter: "Ch 4", cat: ["ontology"] },
  { task: "Configure primary key on Object Type", tms: [{id:"tm-20",label:"TM-20"}], chapter: "Ch 4", cat: ["ontology"] },
  { task: "Create a Link Type between Object Types", tms: [{id:"tm-20",label:"TM-20"},{id:"tm-30",label:"TM-30"}], chapter: "Ch 4", cat: ["ontology"] },
  { task: "Create and configure Actions", tms: [{id:"tm-20",label:"TM-20"},{id:"tm-30",label:"TM-30"}], chapter: "Ch 4", cat: ["ontology"] },
  { task: "Design Object Type from operational requirements", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 4", cat: ["ontology"] },
  { task: "Design Link Types and relationships", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 4", cat: ["ontology"] },
  { task: "Configure action validation rules", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 4", cat: ["ontology"] },
  { task: "Implement bi-directional link management", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 4", cat: ["ontology"] },
  { task: "Design knowledge ontology", tms: [{id:"tm-40k",label:"TM-40K"}], chapter: "Ch 2", cat: ["ontology","km"] },
  { task: "Design project tracker ontology", tms: [{id:"tm-40j",label:"TM-40J"}], chapter: "Ch 4", cat: ["ontology","pm"] },
  { task: "Design program tracking ontology", tms: [{id:"tm-50j",label:"TM-50J"}], chapter: "Ch 3", cat: ["ontology","pm","advanced"] },
  { task: "Design theater-level ontology", tms: [{id:"tm-50k",label:"TM-50K"}], chapter: "Ch 2", cat: ["ontology","km","advanced"] },
  { task: "Traverse link types between objects", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 2", cat: ["ontology","code"] },
  { task: "Execute actions via OSDK", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 2", cat: ["ontology","code"] },
  { task: "Build computed property functions", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 5", cat: ["ontology","code"] },
  { task: "Manage ontology CI/CD", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 6", cat: ["ontology","governance","advanced"] },
  { task: "Publish predictions as ontology object property", tms: [{id:"tm-40i",label:"TM-40I"}], chapter: "Ch 4", cat: ["ontology","ml"] },

  // ── AIP & AI WORKFLOWS ───────────────────────────────────────
  { task: "Use AIP Logic workflow", tms: [{id:"tm-10",label:"TM-10"}], chapter: "Ch 5", cat: ["aip"] },
  { task: "Interact with AIP Agent chat interface", tms: [{id:"tm-10",label:"TM-10"}], chapter: "Ch 5", cat: ["aip"] },
  { task: "Configure AIP Logic workflows", tms: [{id:"tm-30",label:"TM-30"},{id:"tm-40h",label:"TM-40H"}], chapter: "Ch 6", cat: ["aip"] },
  { task: "Set up natural language query interface", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 6", cat: ["aip"] },
  { task: "Design AI-assisted data workflows", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 6", cat: ["aip"] },
  { task: "Configure AIP for advanced knowledge management", tms: [{id:"tm-40k",label:"TM-40K"},{id:"tm-50k",label:"TM-50K"}], chapter: "Ch 5", cat: ["aip","km"] },
  { task: "Conduct large-scale lessons synthesis with AI", tms: [{id:"tm-50k",label:"TM-50K"}], chapter: "Ch 4", cat: ["aip","km","advanced"] },
  { task: "Implement AI-assisted doctrine development", tms: [{id:"tm-50k",label:"TM-50K"}], chapter: "Ch 4", cat: ["aip","km","advanced"] },
  { task: "Design multi-agent orchestration system", tms: [{id:"tm-50h",label:"TM-50H"}], chapter: "Ch 2", cat: ["aip","advanced"] },
  { task: "Implement orchestration patterns", tms: [{id:"tm-50h",label:"TM-50H"}], chapter: "Ch 2", cat: ["aip","advanced"] },
  { task: "Design shared state management for agents", tms: [{id:"tm-50h",label:"TM-50H"}], chapter: "Ch 2", cat: ["aip","advanced"] },
  { task: "Implement circuit breakers and failure isolation", tms: [{id:"tm-50h",label:"TM-50H"}], chapter: "Ch 2", cat: ["aip","advanced"] },
  { task: "Domain adapt LLM for Army writing style", tms: [{id:"tm-50h",label:"TM-50H"}], chapter: "Ch 3", cat: ["aip","advanced"] },
  { task: "Implement advanced RAG for intelligence fusion", tms: [{id:"tm-50h",label:"TM-50H"}], chapter: "Ch 3", cat: ["aip","advanced"] },
  { task: "Conduct AI red-team assessment", tms: [{id:"tm-50h",label:"TM-50H"}], chapter: "Ch 4", cat: ["aip","governance","advanced"] },
  { task: "Implement AI observability for production system", tms: [{id:"tm-50h",label:"TM-50H"}], chapter: "Ch 5", cat: ["aip","advanced"] },
  { task: "Build multi-modal ingestion pipeline", tms: [{id:"tm-50h",label:"TM-50H"}], chapter: "Ch 5", cat: ["aip","advanced"] },
  { task: "Conduct AI production readiness review", tms: [{id:"tm-50h",label:"TM-50H"}], chapter: "Ch 6", cat: ["aip","advanced"] },
  { task: "Subscribe to real-time object changes", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 2", cat: ["aip","code"] },

  // ── CODE, SDK & TRANSFORMS ───────────────────────────────────
  { task: "Query objects via OSDK fundamentals", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 2", cat: ["code"] },
  { task: "Implement pagination for object queries", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 2", cat: ["code"] },
  { task: "Filter and sort objects via OSDK", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 2", cat: ["code"] },
  { task: "Perform bulk object operations", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 2", cat: ["code"] },
  { task: "Implement error handling and retries", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 2", cat: ["code"] },
  { task: "Initialize Platform SDK", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 3", cat: ["code"] },
  { task: "Read datasets via Platform SDK", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 3", cat: ["code"] },
  { task: "Write datasets with transactions", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 3", cat: ["code"] },
  { task: "Manage file resources via SDK", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 3", cat: ["code"] },
  { task: "Manage branches programmatically", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 3", cat: ["code"] },
  { task: "Build Functions on Objects (FOO)", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 5", cat: ["code"] },
  { task: "Optimize FOO performance", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 5", cat: ["code"] },
  { task: "Test FOO functions", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 5", cat: ["code"] },
  { task: "Design action validation architecture", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 6", cat: ["code"] },
  { task: "Write TypeScript action validators", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 6", cat: ["code"] },
  { task: "Implement multi-step action flows", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 6", cat: ["code"] },
  { task: "Implement REST API integrations", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 9", cat: ["code"] },
  { task: "Manage webhook integrations", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 9", cat: ["code"] },
  { task: "Build feature engineering transform", tms: [{id:"tm-40i",label:"TM-40I"}], chapter: "Ch 3", cat: ["code","ml"] },
  { task: "Build feature store entry", tms: [{id:"tm-40i",label:"TM-40I"}], chapter: "Ch 3", cat: ["code","ml"] },
  { task: "Version control in Code Workspaces", tms: [{id:"tm-40i",label:"TM-40I"}], chapter: "Ch 2", cat: ["code"] },
  { task: "Scale Platform SDK authentication", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 2", cat: ["code","advanced"] },
  { task: "Scale dataset operations", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 2", cat: ["code","advanced"] },
  { task: "Automate branch management", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 2", cat: ["code","advanced"] },
  { task: "Optimize OSDK queries", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 4", cat: ["code","advanced"] },
  { task: "Implement caching strategies", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 4", cat: ["code","advanced"] },
  { task: "Optimize indexing and search", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 4", cat: ["code","advanced"] },
  { task: "Integrate REST APIs at scale", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 5", cat: ["code","advanced"] },
  { task: "Implement gRPC integration patterns", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 5", cat: ["code","advanced"] },
  { task: "Implement event streaming (Kafka / Kinesis)", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 5", cat: ["code","advanced"] },
  { task: "Deploy containers on MSS", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 6", cat: ["code","advanced"] },
  { task: "Manage technical debt at scale", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 8", cat: ["code","advanced"] },

  // ── MACHINE LEARNING ─────────────────────────────────────────
  { task: "Train scikit-learn model with experiment tracking", tms: [{id:"tm-40i",label:"TM-40I"}], chapter: "Ch 3", cat: ["ml"] },
  { task: "Hyperparameter tuning with Optuna", tms: [{id:"tm-40i",label:"TM-40I"}], chapter: "Ch 3", cat: ["ml"] },
  { task: "Train PyTorch model on Foundry data", tms: [{id:"tm-40i",label:"TM-40I"}], chapter: "Ch 3", cat: ["ml"] },
  { task: "Compute and document model evaluation report", tms: [{id:"tm-40i",label:"TM-40I"}], chapter: "Ch 3", cat: ["ml"] },
  { task: "Conduct bias and fairness assessment", tms: [{id:"tm-40i",label:"TM-40I"},{id:"tm-50i",label:"TM-50I"}], chapter: "Ch 3", cat: ["ml"] },
  { task: "Deploy batch inference as Foundry transform", tms: [{id:"tm-40i",label:"TM-40I"}], chapter: "Ch 4", cat: ["ml"] },
  { task: "Implement inference caching and freshness indicators", tms: [{id:"tm-40i",label:"TM-40I"}], chapter: "Ch 4", cat: ["ml"] },
  { task: "Implement model versioning", tms: [{id:"tm-40i",label:"TM-40I"}], chapter: "Ch 4", cat: ["ml"] },
  { task: "Implement drift detection", tms: [{id:"tm-40i",label:"TM-40I"}], chapter: "Ch 4", cat: ["ml"] },
  { task: "Configure retraining triggers", tms: [{id:"tm-40i",label:"TM-40I"}], chapter: "Ch 4", cat: ["ml"] },
  { task: "Complete model card documentation", tms: [{id:"tm-40i",label:"TM-40I"}], chapter: "Ch 5", cat: ["ml","governance"] },
  { task: "Manage production model incident", tms: [{id:"tm-40i",label:"TM-40I"}], chapter: "Ch 5", cat: ["ml"] },
  { task: "Build linear regression readiness model", tms: [{id:"tm-40g",label:"TM-40G"}], chapter: "Ch 3", cat: ["ml"] },
  { task: "Build readiness drop risk classifier", tms: [{id:"tm-40g",label:"TM-40G"}], chapter: "Ch 3", cat: ["ml"] },
  { task: "Analyze unit readiness trend", tms: [{id:"tm-40g",label:"TM-40G"}], chapter: "Ch 3", cat: ["ml","data"] },
  { task: "Build ARIMA readiness forecast", tms: [{id:"tm-40g",label:"TM-40G"}], chapter: "Ch 3", cat: ["ml"] },
  { task: "Logistics demand forecasting (Class IX)", tms: [{id:"tm-40g",label:"TM-40G"}], chapter: "Ch 3", cat: ["ml"] },
  { task: "Design and implement automated retraining pipeline", tms: [{id:"tm-50i",label:"TM-50I"}], chapter: "Ch 2", cat: ["ml","advanced"] },
  { task: "Fine-tune Transformer for SITREP classification", tms: [{id:"tm-50i",label:"TM-50I"}], chapter: "Ch 2", cat: ["ml","advanced"] },
  { task: "Build GNN for unit readiness propagation", tms: [{id:"tm-50i",label:"TM-50I"}], chapter: "Ch 3", cat: ["ml","advanced"] },
  { task: "Implement federated retraining coordination", tms: [{id:"tm-50i",label:"TM-50I"}], chapter: "Ch 3", cat: ["ml","advanced"] },
  { task: "Implement platform-level interpretability infrastructure", tms: [{id:"tm-50i",label:"TM-50I"}], chapter: "Ch 4", cat: ["ml","advanced"] },
  { task: "Conduct bias audit for personnel readiness model", tms: [{id:"tm-50i",label:"TM-50I"}], chapter: "Ch 4", cat: ["ml","advanced"] },
  { task: "Optimize production inference pipeline", tms: [{id:"tm-50i",label:"TM-50I"}], chapter: "Ch 5", cat: ["ml","advanced"] },
  { task: "Conduct adversarial robustness evaluation", tms: [{id:"tm-50i",label:"TM-50I"}], chapter: "Ch 5", cat: ["ml","advanced"] },
  { task: "Design shared feature store for MSS ML program", tms: [{id:"tm-50i",label:"TM-50I"}], chapter: "Ch 6", cat: ["ml","advanced"] },

  // ── PROGRAM MANAGEMENT ───────────────────────────────────────
  { task: "Execute Scrum framework for MSS projects", tms: [{id:"tm-40j",label:"TM-40J"}], chapter: "Ch 2", cat: ["pm"] },
  { task: "Write and manage user stories", tms: [{id:"tm-40j",label:"TM-40J"}], chapter: "Ch 2", cat: ["pm"] },
  { task: "Define acceptance criteria", tms: [{id:"tm-40j",label:"TM-40J"}], chapter: "Ch 2", cat: ["pm"] },
  { task: "Size stories and measure velocity", tms: [{id:"tm-40j",label:"TM-40J"}], chapter: "Ch 2", cat: ["pm"] },
  { task: "Run sprint ceremonies (planning, standup, review, retro)", tms: [{id:"tm-40j",label:"TM-40J"}], chapter: "Ch 2", cat: ["pm"] },
  { task: "Execute Kanban for operational support work", tms: [{id:"tm-40j",label:"TM-40J"}], chapter: "Ch 2", cat: ["pm"] },
  { task: "Manage ML/AI project lifecycle phases", tms: [{id:"tm-40j",label:"TM-40J"}], chapter: "Ch 3", cat: ["pm"] },
  { task: "Elicit requirements from stakeholders", tms: [{id:"tm-40j",label:"TM-40J"}], chapter: "Ch 4", cat: ["pm"] },
  { task: "Manage stakeholder expectations", tms: [{id:"tm-40j",label:"TM-40J"}], chapter: "Ch 4", cat: ["pm"] },
  { task: "Configure automated status alerts", tms: [{id:"tm-40j",label:"TM-40J"}], chapter: "Ch 5", cat: ["pm"] },
  { task: "Manage risk register for data projects", tms: [{id:"tm-40j",label:"TM-40J"}], chapter: "Ch 6", cat: ["pm"] },
  { task: "Manage dependencies between teams", tms: [{id:"tm-40j",label:"TM-40J"},{id:"tm-50j",label:"TM-50J"}], chapter: "Ch 6", cat: ["pm"] },
  { task: "Plan release milestones", tms: [{id:"tm-40j",label:"TM-40J"}], chapter: "Ch 7", cat: ["pm"] },
  { task: "Define 'production ready' for a data product", tms: [{id:"tm-40j",label:"TM-40J"}], chapter: "Ch 7", cat: ["pm"] },
  { task: "Implement change control for production systems", tms: [{id:"tm-40j",label:"TM-40J"}], chapter: "Ch 8", cat: ["pm","governance"] },
  { task: "Execute program increment (PI) planning", tms: [{id:"tm-50j",label:"TM-50J"}], chapter: "Ch 2", cat: ["pm","advanced"] },
  { task: "Run cross-team sprint ceremonies", tms: [{id:"tm-50j",label:"TM-50J"}], chapter: "Ch 2", cat: ["pm","advanced"] },
  { task: "Brief GO/SES leadership on program status", tms: [{id:"tm-50j",label:"TM-50J"}], chapter: "Ch 3", cat: ["pm","advanced"] },
  { task: "Implement core delivery metrics", tms: [{id:"tm-50j",label:"TM-50J"}], chapter: "Ch 5", cat: ["pm","advanced"] },
  { task: "Manage technical debt at program scale", tms: [{id:"tm-50j",label:"TM-50J"}], chapter: "Ch 6", cat: ["pm","advanced"] },
  { task: "Execute build vs. buy vs. configure decisions", tms: [{id:"tm-50j",label:"TM-50J"}], chapter: "Ch 7", cat: ["pm","advanced"] },
  { task: "Manage Palantir partnership / task order", tms: [{id:"tm-50j",label:"TM-50J"}], chapter: "Ch 7", cat: ["pm","advanced"] },
  { task: "Design data program team structure", tms: [{id:"tm-50j",label:"TM-50J"}], chapter: "Ch 8", cat: ["pm","advanced"] },
  { task: "Plan for personnel turbulence", tms: [{id:"tm-50j",label:"TM-50J"}], chapter: "Ch 8", cat: ["pm","advanced"] },
  { task: "Establish program governance", tms: [{id:"tm-50j",label:"TM-50J"}], chapter: "Ch 9", cat: ["pm","governance","advanced"] },

  // ── KNOWLEDGE MANAGEMENT ─────────────────────────────────────
  { task: "Configure lessons-learned intake pipeline", tms: [{id:"tm-40k",label:"TM-40K"}], chapter: "Ch 3", cat: ["km"] },
  { task: "Configure SOP review notification workflow", tms: [{id:"tm-40k",label:"TM-40K"}], chapter: "Ch 5", cat: ["km"] },
  { task: "Design federated KM architecture", tms: [{id:"tm-50k",label:"TM-50K"}], chapter: "Ch 2", cat: ["km","advanced"] },
  { task: "Design federated repository patterns", tms: [{id:"tm-50k",label:"TM-50K"}], chapter: "Ch 2", cat: ["km","advanced"] },
  { task: "Implement classification-level parallel architecture", tms: [{id:"tm-50k",label:"TM-50K"}], chapter: "Ch 2", cat: ["km","governance","advanced"] },
  { task: "Implement multi-unit knowledge federation", tms: [{id:"tm-50k",label:"TM-50K"}], chapter: "Ch 3", cat: ["km","advanced"] },
  { task: "Integrate NATO knowledge management", tms: [{id:"tm-50k",label:"TM-50K"}], chapter: "Ch 5", cat: ["km","advanced"] },
  { task: "Ensure STANAG 4778 conformance", tms: [{id:"tm-50k",label:"TM-50K"}], chapter: "Ch 5", cat: ["km","governance","advanced"] },
  { task: "Integrate coalition knowledge sharing", tms: [{id:"tm-50k",label:"TM-50K"}], chapter: "Ch 5", cat: ["km","advanced"] },
  { task: "Design knowledge graph architecture", tms: [{id:"tm-50k",label:"TM-50K"}], chapter: "Ch 6", cat: ["km","advanced"] },
  { task: "Implement KM metrics and effectiveness measurement", tms: [{id:"tm-50k",label:"TM-50K"}], chapter: "Ch 7", cat: ["km","advanced"] },
  { task: "Report KM value to senior leaders", tms: [{id:"tm-50k",label:"TM-50K"}], chapter: "Ch 7", cat: ["km","advanced"] },
  { task: "Conduct knowledge risk assessment", tms: [{id:"tm-50k",label:"TM-50K"}], chapter: "Ch 8", cat: ["km","advanced"] },
  { task: "Lead KM community of practice", tms: [{id:"tm-50k",label:"TM-50K"}], chapter: "Ch 8", cat: ["km","advanced"] },
  { task: "Conduct KM architecture audit", tms: [{id:"tm-50k",label:"TM-50K"}], chapter: "Ch 8", cat: ["km","advanced"] },

  // ── ORSA ANALYSIS ─────────────────────────────────────────────
  { task: "Conduct Monte Carlo COA risk analysis", tms: [{id:"tm-40g",label:"TM-40G"}], chapter: "Ch 4", cat: ["data"] },
  { task: "Conduct Tornado sensitivity analysis", tms: [{id:"tm-40g",label:"TM-40G"}], chapter: "Ch 4", cat: ["data"] },
  { task: "Optimize personnel assignment across units", tms: [{id:"tm-40g",label:"TM-40G"}], chapter: "Ch 4", cat: ["data"] },
  { task: "Design exercise data collection architecture", tms: [{id:"tm-40g",label:"TM-40G"}], chapter: "Ch 5", cat: ["data"] },
  { task: "Build exercise aggregation pipeline", tms: [{id:"tm-40g",label:"TM-40G"}], chapter: "Ch 5", cat: ["data","build"] },
  { task: "Generate post-exercise report", tms: [{id:"tm-40g",label:"TM-40G"}], chapter: "Ch 5", cat: ["data"] },
  { task: "Conduct sensitivity analysis for commander brief", tms: [{id:"tm-40g",label:"TM-40G"}], chapter: "Ch 5", cat: ["data"] },
  { task: "Apply nonlinear programming on MSS", tms: [{id:"tm-50g",label:"TM-50G"}], chapter: "Ch 2", cat: ["data","advanced"] },
  { task: "Conduct multi-objective optimization for COA comparison", tms: [{id:"tm-50g",label:"TM-50G"}], chapter: "Ch 2", cat: ["data","advanced"] },
  { task: "Build two-stage stochastic program for theater logistics", tms: [{id:"tm-50g",label:"TM-50G"}], chapter: "Ch 3", cat: ["data","advanced"] },
  { task: "Build logistics network resiliency ABMS", tms: [{id:"tm-50g",label:"TM-50G"}], chapter: "Ch 4", cat: ["data","advanced"] },
  { task: "Design campaign wargame data architecture on MSS", tms: [{id:"tm-50g",label:"TM-50G"}], chapter: "Ch 5", cat: ["data","advanced"] },
  { task: "Build campaign assessment dashboard on MSS", tms: [{id:"tm-50g",label:"TM-50G"}], chapter: "Ch 5", cat: ["data","advanced"] },

  // ── GOVERNANCE & SECURITY ─────────────────────────────────────
  { task: "Respond to misrouted or higher classification data", tms: [{id:"tm-10",label:"TM-10"}], chapter: "Ch 6", cat: ["governance"] },
  { task: "Audit data lineage and dependencies", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 7", cat: ["governance"] },
  { task: "Implement data quality workflows", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 7", cat: ["governance"] },
  { task: "Configure access control granularly", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 7", cat: ["governance"] },
  { task: "Use Foundry branching via UI", tms: [{id:"tm-20",label:"TM-20"},{id:"tm-30",label:"TM-30"}], chapter: "Ch 7", cat: ["governance"] },
  { task: "Create a development branch", tms: [{id:"tm-20",label:"TM-20"},{id:"tm-30",label:"TM-30"}], chapter: "Ch 7", cat: ["governance"] },
  { task: "Request and merge a branch", tms: [{id:"tm-20",label:"TM-20"},{id:"tm-30",label:"TM-30"}], chapter: "Ch 7", cat: ["governance"] },
  { task: "Promote changes to production environment", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 7", cat: ["governance"] },
  { task: "Enforce naming conventions", tms: [{id:"tm-20",label:"TM-20"},{id:"tm-30",label:"TM-30"}], chapter: "Ch 8", cat: ["governance"] },
  { task: "Document pipeline and Ontology changes", tms: [{id:"tm-20",label:"TM-20"}], chapter: "Ch 7", cat: ["governance"] },
  { task: "Complete data quality checklist", tms: [{id:"tm-20",label:"TM-20"}], chapter: "Ch 7", cat: ["governance"] },
  { task: "Complete C2DAO governance checklist", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 8", cat: ["governance"] },
  { task: "Conduct peer review of changes", tms: [{id:"tm-30",label:"TM-30"}], chapter: "Ch 8", cat: ["governance"] },
  { task: "Implement attribute-based access control (CBAC)", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 8", cat: ["governance","code"] },
  { task: "Manage credentials securely", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 8", cat: ["governance","code"] },
  { task: "Implement marking compliance (classification)", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 8", cat: ["governance"] },
  { task: "Implement audit trail requirements", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 8", cat: ["governance"] },
  { task: "Configure CI/CD pipeline", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 8", cat: ["governance","code"] },
  { task: "Implement automated testing", tms: [{id:"tm-40l",label:"TM-40L"}], chapter: "Ch 8", cat: ["governance","code"] },
  { task: "Design CI/CD pipeline architecture", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 6", cat: ["governance","code","advanced"] },
  { task: "Implement pre-commit hooks", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 6", cat: ["governance","code","advanced"] },
  { task: "Enforce automated testing standards", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 6", cat: ["governance","code","advanced"] },
  { task: "Implement OWASP Top 10 mitigations", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 7", cat: ["governance","code","advanced"] },
  { task: "Prevent injection attacks", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 7", cat: ["governance","code","advanced"] },
  { task: "Manage secrets securely", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 7", cat: ["governance","code","advanced"] },
  { task: "Implement SAST (static application security testing)", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 7", cat: ["governance","code","advanced"] },
  { task: "Conduct authorized penetration testing", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 7", cat: ["governance","advanced"] },
  { task: "Execute architecture review", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 8", cat: ["governance","advanced"] },
  { task: "Enforce platform governance", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 8", cat: ["governance","advanced"] },
  { task: "Manage platform upgrades", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 8", cat: ["governance","advanced"] },
  { task: "Implement tenant isolation in code", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 4", cat: ["governance","code","advanced"] },
  { task: "Implement classification-aware design", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 4", cat: ["governance","code","advanced"] },
  { task: "Design coalition interoperability patterns", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 4", cat: ["governance","code","advanced"] },
  { task: "Manage compute costs", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 4", cat: ["governance","advanced"] },
  { task: "Profile performance with tools", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 4", cat: ["governance","code","advanced"] },
  { task: "Onboard new developers", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 8", cat: ["governance","advanced"] },
  { task: "Conduct code review", tms: [{id:"tm-50l",label:"TM-50L"}], chapter: "Ch 8", cat: ["governance","code","advanced"] },
  { task: "Implement change control at program scale", tms: [{id:"tm-50j",label:"TM-50J"}], chapter: "Ch 9", cat: ["governance","pm","advanced"] },
  { task: "Build organizational buy-in for data culture change", tms: [{id:"tm-50j",label:"TM-50J"}], chapter: "Ch 3", cat: ["governance","pm","advanced"] },
];

// ── HELPERS ───────────────────────────────────────────────────
/** Escape special regex characters in a search term. */
function escapeRegex(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

/** Split task text into segments for highlight rendering. */
function highlightText(text: string, query: string): React.ReactNode {
  if (!query) return text;
  const regex = new RegExp(`(${escapeRegex(query)})`, "gi");
  const parts = text.split(regex);
  return parts.map((part, i) =>
    regex.test(part) ? (
      <mark key={i} className="ti-mark">{part}</mark>
    ) : (
      part
    )
  );
}

// ── COMPONENT ─────────────────────────────────────────────────
const TaskIndex: React.FC<Props> = ({ showPanel: _showPanel }) => {
  const [searchTerm, setSearchTerm] = useState("");
  const [activeFilter, setActiveFilter] = useState("all");

  const q = searchTerm.trim().toLowerCase();

  // Derive filtered task set
  const filteredTasks = useMemo(() => {
    return TASKS.filter((t) => {
      const inCategory =
        activeFilter === "all" || t.cat.includes(activeFilter);
      const inSearch =
        !q ||
        t.task.toLowerCase().includes(q) ||
        t.tms.some((tm) => tm.label.toLowerCase().includes(q));
      return inCategory && inSearch;
    });
  }, [q, activeFilter]);

  const totalVisible = filteredTasks.length;
  const countLabel =
    totalVisible === TASKS.length
      ? `${TASKS.length} tasks`
      : `${totalVisible} / ${TASKS.length}`;

  return (
    <>
      <style>{`
        /* ── TASK INDEX LOCAL STYLES (ti- prefix) ─────────────── */
        .ti-search-bar {
          background: #071628;
          border-top: 1px solid #1E4A88;
          padding: 14px 28px;
          display: flex;
          align-items: center;
          gap: 12px;
          position: sticky;
          top: 0;
          z-index: 100;
          box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }
        .ti-search-bar label {
          font-family: Arial, Helvetica, sans-serif;
          font-size: 11px;
          font-weight: 700;
          color: #C8971A;
          letter-spacing: 2px;
          text-transform: uppercase;
          white-space: nowrap;
        }
        .ti-search-input {
          flex: 1;
          padding: 8px 12px;
          background: #163A6C;
          border: 1px solid #1E4A88;
          border-radius: 3px;
          color: #FFFFFF;
          font-family: 'Courier New', Courier, monospace;
          font-size: 14px;
          outline: none;
          transition: border-color 0.15s;
        }
        .ti-search-input:focus {
          border-color: #C8971A;
        }
        .ti-search-input::placeholder {
          color: #7A88A8;
        }
        .ti-result-count {
          font-family: Arial, Helvetica, sans-serif;
          font-size: 11px;
          color: #7A88A8;
          white-space: nowrap;
          min-width: 80px;
          text-align: right;
        }

        /* Filter pills */
        .ti-filter-bar {
          background: #0C2340;
          border-bottom: 1px solid #163A6C;
          padding: 8px 28px;
          display: flex;
          gap: 6px;
          flex-wrap: wrap;
          align-items: center;
        }
        .ti-filter-bar-label {
          font-family: Arial, Helvetica, sans-serif;
          font-size: 10px;
          font-weight: 700;
          color: #7A88A8;
          letter-spacing: 1px;
          text-transform: uppercase;
          margin-right: 4px;
        }
        .ti-pill {
          padding: 3px 10px;
          border-radius: 12px;
          font-family: Arial, Helvetica, sans-serif;
          font-size: 11px;
          font-weight: 600;
          cursor: pointer;
          border: 1px solid #1E4A88;
          transition: all 0.12s;
          background: #163A6C;
          color: #C4CAE0;
          user-select: none;
        }
        .ti-pill:hover {
          border-color: #C8971A;
          color: #E0B840;
        }
        .ti-pill.ti-pill-active {
          background: #C8971A;
          color: #071628;
          border-color: #C8971A;
          font-weight: 700;
        }

        /* Content area */
        .ti-content {
          max-width: 1200px;
          margin: 0 auto;
          padding: 20px 28px 48px;
        }
        .ti-no-results {
          text-align: center;
          padding: 60px 20px;
          color: #7A88A8;
          font-family: Arial, Helvetica, sans-serif;
        }
        .ti-no-results h2 {
          font-size: 18px;
          margin-bottom: 8px;
          color: #485878;
        }

        /* Section headers */
        .ti-section-hdr {
          font-family: Arial, Helvetica, sans-serif;
          font-size: 11px;
          font-weight: 700;
          letter-spacing: 3px;
          text-transform: uppercase;
          color: #9A7010;
          padding: 18px 0 8px;
          border-bottom: 1px solid #E0E4EF;
          margin-bottom: 6px;
        }

        /* Task grid */
        .ti-task-grid {
          display: grid;
          grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
          gap: 6px;
          margin-bottom: 4px;
        }

        /* Task card — base (non-link) */
        .ti-task-card {
          background: #FFFFFF;
          border: 1px solid #E0E4EF;
          border-left: 3px solid #C4CAE0;
          border-radius: 3px;
          padding: 8px 12px;
          display: flex;
          align-items: flex-start;
          gap: 10px;
          transition: border-color 0.1s, box-shadow 0.1s;
          cursor: default;
          text-decoration: none;
          color: inherit;
        }
        .ti-task-card:hover {
          border-left-color: #C8971A;
          box-shadow: 0 1px 5px rgba(0,0,0,0.12);
        }
        a.ti-task-card:hover .ti-task-text {
          color: #1E4A88;
        }

        .ti-task-text {
          flex: 1;
          font-size: 13px;
          color: #0A1628;
          line-height: 1.4;
        }
        .ti-task-meta {
          display: flex;
          flex-direction: column;
          align-items: flex-end;
          gap: 3px;
          flex-shrink: 0;
        }

        /* TM badges */
        .ti-tm-badge {
          display: inline-block;
          padding: 1px 6px;
          border-radius: 3px;
          font-family: Arial, Helvetica, sans-serif;
          font-size: 10px;
          font-weight: 700;
          white-space: nowrap;
          text-decoration: none;
        }
        .ti-tm-10  { background: #E8F5E9; color: #1B5E20; border: 1px solid #A5D6A7; }
        .ti-tm-20  { background: #E3F2FD; color: #0D47A1; border: 1px solid #90CAF9; }
        .ti-tm-30  { background: #EDE7F6; color: #4527A0; border: 1px solid #CE93D8; }
        .ti-tm-40g { background: #FFF3E0; color: #E65100; border: 1px solid #FFCC80; }
        .ti-tm-40h { background: #FCE4EC; color: #880E4F; border: 1px solid #F48FB1; }
        .ti-tm-40i { background: #E0F7FA; color: #006064; border: 1px solid #80DEEA; }
        .ti-tm-40j { background: #F3E5F5; color: #6A1B9A; border: 1px solid #CE93D8; }
        .ti-tm-40k { background: #FFF8E1; color: #F57F17; border: 1px solid #FFE082; }
        .ti-tm-40l { background: #E8EAF6; color: #283593; border: 1px solid #9FA8DA; }
        .ti-tm-50g { background: #FBE9E7; color: #BF360C; border: 1px solid #FFAB91; }
        .ti-tm-50h { background: #F8BBD0; color: #880E4F; border: 1px solid #F48FB1; }
        .ti-tm-50i { background: #B2EBF2; color: #006064; border: 1px solid #80DEEA; }
        .ti-tm-50j { background: #E1BEE7; color: #4A148C; border: 1px solid #CE93D8; }
        .ti-tm-50k { background: #FFE0B2; color: #E65100; border: 1px solid #FFCC80; }
        .ti-tm-50l { background: #C5CAE9; color: #1A237E; border: 1px solid #9FA8DA; }

        .ti-chapter-ref {
          font-family: Arial, Helvetica, sans-serif;
          font-size: 9px;
          color: #7A88A8;
          white-space: nowrap;
        }

        /* Highlight */
        .ti-mark {
          background: #FDF5DC;
          color: #071628;
          border-radius: 2px;
          padding: 0 1px;
        }
      `}</style>

      {/* Search bar */}
      <div className="ti-search-bar">
        <label htmlFor="ti-search-input">Search:</label>
        <input
          id="ti-search-input"
          className="ti-search-input"
          type="text"
          placeholder="Type a task, keyword, or topic..."
          autoComplete="off"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
        <div className="ti-result-count">{countLabel}</div>
      </div>

      {/* Filter pills */}
      <div className="ti-filter-bar">
        <span className="ti-filter-bar-label">Filter:</span>
        {FILTER_PILLS.map((p) => (
          <div
            key={p.filter}
            className={`ti-pill${activeFilter === p.filter ? " ti-pill-active" : ""}`}
            onClick={() => setActiveFilter(p.filter)}
          >
            {p.label}
          </div>
        ))}
      </div>

      {/* Content */}
      <div className="ti-content">
        {totalVisible === 0 ? (
          <div className="ti-no-results">
            <h2>No matching tasks found.</h2>
            <p>Try a different keyword or clear the filter.</p>
          </div>
        ) : (
          SECTIONS.map((sec) => {
            const secTasks = filteredTasks.filter((t) =>
              t.cat.includes(sec.id)
            );
            if (secTasks.length === 0) return null;

            return (
              <React.Fragment key={sec.id}>
                <div className="ti-section-hdr">{sec.label}</div>
                <div className="ti-task-grid">
                  {secTasks.map((t, idx) => {
                    const singlePdf =
                      t.tms.length === 1 ? PDF[t.tms[0].id] : null;

                    const cardContent = (
                      <>
                        <div className="ti-task-text">
                          {highlightText(t.task, q)}
                        </div>
                        <div className="ti-task-meta">
                          {t.tms.map((tm) => (
                            <a
                              key={tm.id}
                              className={`ti-tm-badge ti-${tm.id}`}
                              href={PDF[tm.id]}
                              target="_blank"
                              rel="noreferrer"
                              title={`Open ${tm.label} PDF`}
                              onClick={(e) => e.stopPropagation()}
                            >
                              {tm.label}
                            </a>
                          ))}
                          <div className="ti-chapter-ref">{t.chapter}</div>
                        </div>
                      </>
                    );

                    // Single-TM tasks: entire card is a link
                    if (singlePdf) {
                      return (
                        <a
                          key={`${sec.id}-${idx}`}
                          className="ti-task-card"
                          href={singlePdf}
                          target="_blank"
                          rel="noreferrer"
                          style={{ textDecoration: "none", color: "inherit" }}
                        >
                          {cardContent}
                        </a>
                      );
                    }

                    // Multi-TM tasks: non-interactive card div
                    return (
                      <div key={`${sec.id}-${idx}`} className="ti-task-card">
                        {cardContent}
                      </div>
                    );
                  })}
                </div>
              </React.Fragment>
            );
          })
        )}
      </div>
    </>
  );
};

export default TaskIndex;
