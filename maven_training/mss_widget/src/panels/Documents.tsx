import { URLS } from '../constants/urls'

// PDFs not yet in the URLS constants — constructed from the same media set base
const BASE = 'https://mss.data.mil/mio/api/mediaSet/ri.mio.main.media-set.9c297238-56bf-46d4-881a-db21-dcee1c/file'

// WFF Concepts Guides (A–F) — not yet in urls.ts
const CG_TM40A = `${BASE}/CONCEPTS_GUIDE_TM40A_INTELLIGENCE.pdf`
const CG_TM40B = `${BASE}/CONCEPTS_GUIDE_TM40B_FIRES.pdf`
const CG_TM40C = `${BASE}/CONCEPTS_GUIDE_TM40C_MOVEMENT_MANEUVER.pdf`
const CG_TM40D = `${BASE}/CONCEPTS_GUIDE_TM40D_SUSTAINMENT.pdf`
const CG_TM40E = `${BASE}/CONCEPTS_GUIDE_TM40E_PROTECTION.pdf`
const CG_TM40F = `${BASE}/CONCEPTS_GUIDE_TM40F_MISSION_COMMAND.pdf`

// Exam pre-tests — not yet in urls.ts
const EXAM_TM10_PRE  = `${BASE}/EXAM_TM10_PRE.pdf`
const EXAM_TM20_PRE  = `${BASE}/EXAM_TM20_PRE.pdf`
const EXAM_TM30_PRE  = `${BASE}/EXAM_TM30_PRE.pdf`
const EXAM_TM40A_PRE = `${BASE}/EXAM_TM40A_PRE.pdf`
const EXAM_TM40B_PRE = `${BASE}/EXAM_TM40B_PRE.pdf`
const EXAM_TM40C_PRE = `${BASE}/EXAM_TM40C_PRE.pdf`
const EXAM_TM40D_PRE = `${BASE}/EXAM_TM40D_PRE.pdf`
const EXAM_TM40E_PRE = `${BASE}/EXAM_TM40E_PRE.pdf`
const EXAM_TM40F_PRE = `${BASE}/EXAM_TM40F_PRE.pdf`
const EXAM_TM40G_PRE = `${BASE}/EXAM_TM40G_PRE.pdf`
const EXAM_TM40H_PRE = `${BASE}/EXAM_TM40H_PRE.pdf`
const EXAM_TM40I_PRE = `${BASE}/EXAM_TM40I_PRE.pdf`
const EXAM_TM40J_PRE = `${BASE}/EXAM_TM40J_PRE.pdf`
const EXAM_TM40K_PRE = `${BASE}/EXAM_TM40K_PRE.pdf`
const EXAM_TM40L_PRE = `${BASE}/EXAM_TM40L_PRE.pdf`
const EXAM_TM50G_PRE = `${BASE}/EXAM_TM50G_PRE.pdf`
const EXAM_TM50H_PRE = `${BASE}/EXAM_TM50H_PRE.pdf`
const EXAM_TM50I_PRE = `${BASE}/EXAM_TM50I_PRE.pdf`
const EXAM_TM50J_PRE = `${BASE}/EXAM_TM50J_PRE.pdf`
const EXAM_TM50K_PRE = `${BASE}/EXAM_TM50K_PRE.pdf`
const EXAM_TM50L_PRE = `${BASE}/EXAM_TM50L_PRE.pdf`

interface Props {
  showPanel: (id: string) => void
}

export default function Documents({ showPanel }: Props) {
  return (
    <>
      <div className="section-header">
        <div className="section-badge">DOCUMENTS</div>
        <div className="section-title">All Training Publications</div>
        <div className="section-subtitle">Click any publication to open the PDF</div>
      </div>

      <h2>Reference Documents</h2>
      <div className="card-grid card-grid-2">
        <a className="card gold-top doc-card" href={URLS.DATA_LITERACY_SL} target="_blank" rel="noreferrer">
          <div className="card-label">DATA LIT — SENIOR LEADERS</div>
          <div className="card-title">Data Literacy for Leaders</div>
          <div className="card-body">Senior leader version — strategic principles, decision frameworks. Commanders and O6+.</div>
        </a>
        <a className="card doc-card" href={URLS.DATA_LITERACY_TECH} target="_blank" rel="noreferrer">
          <div className="card-label">DATA LITERACY</div>
          <div className="card-title">Data Literacy — Comprehensive Reference</div>
          <div className="card-body">Full data literacy reference, examples, vignettes, and annexes. Platform-agnostic.</div>
        </a>
        <a className="card doc-card" href={URLS.GLOSSARY} target="_blank" rel="noreferrer">
          <div className="card-label">GLOSSARY</div>
          <div className="card-title">Data &amp; Foundry Term Glossary</div>
          <div className="card-body">Combined data concepts and Foundry/MSS term equivalency. v1.3.</div>
        </a>
        <a className="card doc-card" href={URLS.NAMING_STANDARDS} target="_blank" rel="noreferrer">
          <div className="card-label">STANDARDS</div>
          <div className="card-title">Naming &amp; Governance Standards</div>
          <div className="card-body">Codified naming conventions, governance checklists — 10 sections, 2 appendices.</div>
        </a>
        <a className="card doc-card" href={URLS.CHEATSHEET} target="_blank" rel="noreferrer">
          <div className="card-label">QUICK REF</div>
          <div className="card-title">MSS Quick Reference Cheatsheet</div>
          <div className="card-body">At-a-glance reference card for common MSS tasks and patterns.</div>
        </a>
        <a className="card doc-card" href={URLS.MTP} target="_blank" rel="noreferrer">
          <div className="card-label">MTP</div>
          <div className="card-title">Mission Training Plan — MSS</div>
          <div className="card-body">TLOs, ELOs, Go/No-Go criteria, schedule templates. 961 lines.</div>
        </a>
      </div>

      <h2>Technical Manuals — Foundation (All Staff)</h2>
      <div className="card-grid">
        <a className="card gold-top doc-card" href={URLS.TM10} target="_blank" rel="noreferrer">
          <div className="card-label">TM-10</div>
          <div className="card-title">Maven User</div>
          <div className="card-body">Operate MSS, consume data, use dashboards and AIP. Required for all staff.</div>
        </a>
        <a className="card gold-top doc-card" href={URLS.TM20} target="_blank" rel="noreferrer">
          <div className="card-label">TM-20</div>
          <div className="card-title">No-Code Builder</div>
          <div className="card-body">Pipeline Builder, Workshop, basic Ontology. All staff with build responsibilities.</div>
        </a>
        <a className="card gold-top doc-card" href={URLS.TM30} target="_blank" rel="noreferrer">
          <div className="card-label">TM-30</div>
          <div className="card-title">Advanced No-Code Builder</div>
          <div className="card-body">Advanced Workshop, complex pipelines, AIP Logic. Data-adjacent MOS (17/25-series, G2).</div>
        </a>
      </div>

      <details>
        <summary style={{fontSize:14,fontWeight:700,letterSpacing:'.08em',textTransform:'uppercase',color:'var(--navy)',cursor:'pointer',padding:'8px 0',borderBottom:'1px solid var(--gray-200)',marginBottom:12}}>TM-40 Warfighting Function Tracks (6 &mdash; click to expand)</summary>
        <div className="card-grid card-grid-2" style={{marginTop:12}}>
          <a className="card doc-card" href={URLS.TM40A} target="_blank" rel="noreferrer">
            <div className="card-label">TM-40A &mdash; INTELLIGENCE</div>
            <div className="card-title">Intelligence Warfighting Function</div>
            <div className="card-body">MSS integration for intelligence operations and data products.</div>
          </a>
          <a className="card doc-card" href={URLS.TM40B} target="_blank" rel="noreferrer">
            <div className="card-label">TM-40B &mdash; FIRES</div>
            <div className="card-title">Fires Warfighting Function</div>
            <div className="card-body">MSS integration for fires coordination and targeting data.</div>
          </a>
          <a className="card doc-card" href={URLS.TM40C} target="_blank" rel="noreferrer">
            <div className="card-label">TM-40C &mdash; MOVEMENT &amp; MANEUVER</div>
            <div className="card-title">Movement &amp; Maneuver WFF</div>
            <div className="card-body">MSS integration for maneuver and mobility data products.</div>
          </a>
          <a className="card doc-card" href={URLS.TM40D} target="_blank" rel="noreferrer">
            <div className="card-label">TM-40D &mdash; SUSTAINMENT</div>
            <div className="card-title">Sustainment Warfighting Function</div>
            <div className="card-body">MSS integration for logistics and sustainment data.</div>
          </a>
          <a className="card doc-card" href={URLS.TM40E} target="_blank" rel="noreferrer">
            <div className="card-label">TM-40E &mdash; PROTECTION</div>
            <div className="card-title">Protection Warfighting Function</div>
            <div className="card-body">MSS integration for force protection data and reporting.</div>
          </a>
          <a className="card doc-card" href={URLS.TM40F} target="_blank" rel="noreferrer">
            <div className="card-label">TM-40F &mdash; MISSION COMMAND</div>
            <div className="card-title">Mission Command WFF</div>
            <div className="card-body">MSS integration for mission command, C2, and operational reporting.</div>
          </a>
        </div>
      </details>

      <details>
        <summary style={{fontSize:14,fontWeight:700,letterSpacing:'.08em',textTransform:'uppercase',color:'var(--navy)',cursor:'pointer',padding:'8px 0',borderBottom:'1px solid var(--gray-200)',marginBottom:12}}>TM-40 Technical Specialist Tracks (6 &mdash; click to expand)</summary>
        <div className="track-grid" style={{marginTop:12}}>
          <a className="track-card doc-card" href={URLS.TM40G} target="_blank" rel="noreferrer">
            <div className="track-card-hdr"><div className="track-tm">TM-40G &mdash; ORSA</div><div className="track-chip">Specialist</div></div>
            <div className="track-body"><div className="track-name">Operational Research Systems Analysis</div><div className="track-audience">ORSA specialists — quantitative methods, commander products</div><ul className="track-topics"><li>Regression, classification, forecasting</li><li>Monte Carlo COA analysis</li><li>Optimization and sensitivity analysis</li></ul></div>
          </a>
          <a className="track-card doc-card" href={URLS.TM40H} target="_blank" rel="noreferrer">
            <div className="track-card-hdr"><div className="track-tm">TM-40H &mdash; AI Engineer</div><div className="track-chip">Specialist</div></div>
            <div className="track-body"><div className="track-name">AI Engineering</div><div className="track-audience">AI engineers — AIP Logic, Agents, LLM integration</div><ul className="track-topics"><li>AIP Logic workflow design</li><li>Agent configuration</li><li>LLM integration patterns</li></ul></div>
          </a>
          <a className="track-card doc-card" href={URLS.TM40I} target="_blank" rel="noreferrer">
            <div className="track-card-hdr"><div className="track-tm">TM-40I &mdash; ML Engineer</div><div className="track-chip">Specialist</div></div>
            <div className="track-body"><div className="track-name">Machine Learning Engineering</div><div className="track-audience">ML engineers — model training, validation, deployment</div><ul className="track-topics"><li>Feature engineering, experiment tracking</li><li>Batch inference, model versioning</li><li>Drift detection, retraining pipelines</li></ul></div>
          </a>
          <a className="track-card doc-card" href={URLS.TM40J} target="_blank" rel="noreferrer">
            <div className="track-card-hdr"><div className="track-tm">TM-40J &mdash; Program Manager</div><div className="track-chip">Specialist</div></div>
            <div className="track-body"><div className="track-name">Data Program Management</div><div className="track-audience">PMs — pipelines, milestones, portfolio health</div><ul className="track-topics"><li>Scrum / Kanban for data projects</li><li>ML/AI project lifecycle</li><li>Risk register, release planning</li></ul></div>
          </a>
          <a className="track-card doc-card" href={URLS.TM40K} target="_blank" rel="noreferrer">
            <div className="track-card-hdr"><div className="track-tm">TM-40K &mdash; Knowledge Manager</div><div className="track-chip">Specialist</div></div>
            <div className="track-body"><div className="track-name">Knowledge Management</div><div className="track-audience">KMs — forms, lessons learned, institutional memory</div><ul className="track-topics"><li>Knowledge ontology design</li><li>Lessons-learned intake pipeline</li><li>SOP review workflows</li></ul></div>
          </a>
          <a className="track-card doc-card" href={URLS.TM40L} target="_blank" rel="noreferrer">
            <div className="track-card-hdr"><div className="track-tm">TM-40L &mdash; Software Engineer</div><div className="track-chip">Specialist</div></div>
            <div className="track-body"><div className="track-name">Software Engineering</div><div className="track-audience">SWEs — Python/TypeScript, OSDK, code transforms</div><ul className="track-topics"><li>OSDK &amp; Platform SDK</li><li>Functions on Objects, Actions</li><li>CI/CD, security, Slate</li></ul></div>
          </a>
        </div>
      </details>

      <details>
        <summary style={{fontSize:14,fontWeight:700,letterSpacing:'.08em',textTransform:'uppercase',color:'var(--navy)',cursor:'pointer',padding:'8px 0',borderBottom:'1px solid var(--gray-200)',marginBottom:12}}>TM-50 Advanced Technical Tracks (6 &mdash; click to expand)</summary>
        <div className="track-grid" style={{marginTop:12}}>
          <a className="track-card doc-card" href={URLS.TM50G} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-50G &mdash; ORSA Advanced</div><div className="track-chip">Advanced</div></div><div className="track-body"><div className="track-name">Advanced ORSA</div><div className="track-audience">Nonlinear programming, stochastic models, ABMS, campaign assessment</div></div></a>
          <a className="track-card doc-card" href={URLS.TM50H} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-50H &mdash; AI Engineer Advanced</div><div className="track-chip">Advanced</div></div><div className="track-body"><div className="track-name">Advanced AI Engineering</div><div className="track-audience">Multi-agent orchestration, RAG, red-team assessment, AI observability</div></div></a>
          <a className="track-card doc-card" href={URLS.TM50I} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-50I &mdash; ML Engineer Advanced</div><div className="track-chip">Advanced</div></div><div className="track-body"><div className="track-name">Advanced ML Engineering</div><div className="track-audience">AutoML, Transformer fine-tuning, GNNs, federated retraining, adversarial robustness</div></div></a>
          <a className="track-card doc-card" href={URLS.TM50J} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-50J &mdash; PM Advanced</div><div className="track-chip">Advanced</div></div><div className="track-body"><div className="track-name">Advanced Program Management</div><div className="track-audience">PI planning, cross-team governance, GO/SES briefing, Palantir partnership</div></div></a>
          <a className="track-card doc-card" href={URLS.TM50K} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-50K &mdash; KM Advanced</div><div className="track-chip">Advanced</div></div><div className="track-body"><div className="track-name">Advanced Knowledge Management</div><div className="track-audience">Federated KM architecture, NATO integration, STANAG 4778, knowledge graphs</div></div></a>
          <a className="track-card doc-card" href={URLS.TM50L} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-50L &mdash; SWE Advanced</div><div className="track-chip">Advanced</div></div><div className="track-body"><div className="track-name">Advanced Software Engineering</div><div className="track-audience">Scale, multi-tenancy, Kafka, OWASP, SAST, architecture review, platform governance</div></div></a>
        </div>
      </details>

      <details>
        <summary style={{fontSize:14,fontWeight:700,letterSpacing:'.08em',textTransform:'uppercase',color:'var(--navy)',cursor:'pointer',padding:'8px 0',borderBottom:'1px solid var(--gray-200)',marginBottom:12}}>Concepts Guides (18 &mdash; click to expand)</summary>
        <div className="track-grid" style={{marginTop:12}}>
          <a className="track-card doc-card" href={CG_TM40A} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-40A Concepts Guide</div><div className="track-chip">Intelligence</div></div><div className="track-body"><div className="track-audience">Key concepts and terminology for the Intelligence WFF track.</div></div></a>
          <a className="track-card doc-card" href={CG_TM40B} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-40B Concepts Guide</div><div className="track-chip">Fires</div></div><div className="track-body"><div className="track-audience">Key concepts and terminology for the Fires WFF track.</div></div></a>
          <a className="track-card doc-card" href={CG_TM40C} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-40C Concepts Guide</div><div className="track-chip">Movement &amp; Maneuver</div></div><div className="track-body"><div className="track-audience">Key concepts and terminology for the Movement &amp; Maneuver WFF track.</div></div></a>
          <a className="track-card doc-card" href={CG_TM40D} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-40D Concepts Guide</div><div className="track-chip">Sustainment</div></div><div className="track-body"><div className="track-audience">Key concepts and terminology for the Sustainment WFF track.</div></div></a>
          <a className="track-card doc-card" href={CG_TM40E} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-40E Concepts Guide</div><div className="track-chip">Protection</div></div><div className="track-body"><div className="track-audience">Key concepts and terminology for the Protection WFF track.</div></div></a>
          <a className="track-card doc-card" href={CG_TM40F} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-40F Concepts Guide</div><div className="track-chip">Mission Command</div></div><div className="track-body"><div className="track-audience">Key concepts and terminology for the Mission Command WFF track.</div></div></a>
          <a className="track-card doc-card" href={URLS.CG_TM40G} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-40G Concepts Guide</div><div className="track-chip">ORSA</div></div><div className="track-body"><div className="track-audience">Key concepts and terminology for the ORSA specialist track.</div></div></a>
          <a className="track-card doc-card" href={URLS.CG_TM40H} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-40H Concepts Guide</div><div className="track-chip">AI Engineer</div></div><div className="track-body"><div className="track-audience">Key concepts and terminology for the AI Engineer track.</div></div></a>
          <a className="track-card doc-card" href={URLS.CG_TM40I} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-40I Concepts Guide</div><div className="track-chip">ML Engineer</div></div><div className="track-body"><div className="track-audience">Key concepts and terminology for the ML Engineer track.</div></div></a>
          <a className="track-card doc-card" href={URLS.CG_TM40J} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-40J Concepts Guide</div><div className="track-chip">Program Mgr</div></div><div className="track-body"><div className="track-audience">Key concepts and terminology for the Program Manager track.</div></div></a>
          <a className="track-card doc-card" href={URLS.CG_TM40K} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-40K Concepts Guide</div><div className="track-chip">Knowledge Mgr</div></div><div className="track-body"><div className="track-audience">Key concepts and terminology for the Knowledge Manager track.</div></div></a>
          <a className="track-card doc-card" href={URLS.CG_TM40L} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-40L Concepts Guide</div><div className="track-chip">Software Eng</div></div><div className="track-body"><div className="track-audience">Key concepts and terminology for the Software Engineer track.</div></div></a>
          <a className="track-card doc-card" href={URLS.CG_TM50G} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-50G Concepts Guide</div><div className="track-chip">ORSA Adv</div></div><div className="track-body"><div className="track-audience">Advanced concepts and terminology for TM-50G.</div></div></a>
          <a className="track-card doc-card" href={URLS.CG_TM50H} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-50H Concepts Guide</div><div className="track-chip">AI Eng Adv</div></div><div className="track-body"><div className="track-audience">Advanced concepts and terminology for TM-50H.</div></div></a>
          <a className="track-card doc-card" href={URLS.CG_TM50I} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-50I Concepts Guide</div><div className="track-chip">MLE Adv</div></div><div className="track-body"><div className="track-audience">Advanced concepts and terminology for TM-50I.</div></div></a>
          <a className="track-card doc-card" href={URLS.CG_TM50J} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-50J Concepts Guide</div><div className="track-chip">PM Adv</div></div><div className="track-body"><div className="track-audience">Advanced concepts and terminology for TM-50J.</div></div></a>
          <a className="track-card doc-card" href={URLS.CG_TM50K} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-50K Concepts Guide</div><div className="track-chip">KM Adv</div></div><div className="track-body"><div className="track-audience">Advanced concepts and terminology for TM-50K.</div></div></a>
          <a className="track-card doc-card" href={URLS.CG_TM50L} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-50L Concepts Guide</div><div className="track-chip">SWE Adv</div></div><div className="track-body"><div className="track-audience">Advanced concepts and terminology for TM-50L.</div></div></a>
        </div>
      </details>

      <details>
        <summary style={{fontSize:14,fontWeight:700,letterSpacing:'.08em',textTransform:'uppercase',color:'var(--navy)',cursor:'pointer',padding:'8px 0',borderBottom:'1px solid var(--gray-200)',marginBottom:12}}>Practical Exercises (9 &mdash; click to expand)</summary>
        <div className="card-grid" style={{marginTop:12}}>
          <a className="card doc-card" href={URLS.EX10} target="_blank" rel="noreferrer"><div className="card-label">EXERCISE</div><div className="card-title">TM-10 Practical Exercise</div><div className="card-body">Operator basics — hands-on exercise.</div></a>
          <a className="card doc-card" href={URLS.EX20} target="_blank" rel="noreferrer"><div className="card-label">EXERCISE</div><div className="card-title">TM-20 Practical Exercise</div><div className="card-body">No-code builder — hands-on exercise.</div></a>
          <a className="card doc-card" href={URLS.EX30} target="_blank" rel="noreferrer"><div className="card-label">EXERCISE</div><div className="card-title">TM-30 Practical Exercise</div><div className="card-body">Advanced builder — hands-on exercise.</div></a>
          <a className="card doc-card" href={URLS.EX40G} target="_blank" rel="noreferrer"><div className="card-label">EXERCISE</div><div className="card-title">TM-40G Exercise (ORSA)</div><div className="card-body">ORSA specialist practical exercise.</div></a>
          <a className="card doc-card" href={URLS.EX40H} target="_blank" rel="noreferrer"><div className="card-label">EXERCISE</div><div className="card-title">TM-40H Exercise (AI Eng)</div><div className="card-body">AI Engineer practical exercise.</div></a>
          <a className="card doc-card" href={URLS.EX40I} target="_blank" rel="noreferrer"><div className="card-label">EXERCISE</div><div className="card-title">TM-40I Exercise (ML Eng)</div><div className="card-body">ML Engineer practical exercise.</div></a>
          <a className="card doc-card" href={URLS.EX40J} target="_blank" rel="noreferrer"><div className="card-label">EXERCISE</div><div className="card-title">TM-40J Exercise (PM)</div><div className="card-body">Program Manager practical exercise.</div></a>
          <a className="card doc-card" href={URLS.EX40K} target="_blank" rel="noreferrer"><div className="card-label">EXERCISE</div><div className="card-title">TM-40K Exercise (KM)</div><div className="card-body">Knowledge Manager practical exercise.</div></a>
          <a className="card doc-card" href={URLS.EX40L} target="_blank" rel="noreferrer"><div className="card-label">EXERCISE</div><div className="card-title">TM-40L Exercise (SWE)</div><div className="card-body">Software Engineer practical exercise.</div></a>
        </div>
      </details>

      <details>
        <summary style={{fontSize:14,fontWeight:700,letterSpacing:'.08em',textTransform:'uppercase',color:'var(--navy)',cursor:'pointer',padding:'8px 0',borderBottom:'1px solid var(--gray-200)',marginBottom:12}}>Pre-Assessment Tests (21 &mdash; click to expand)</summary>
        <div className="callout note" style={{marginTop:12,marginBottom:12}}>
          <div className="callout-label">NOTE &mdash; PRE-TESTS</div>
          <div className="callout-body">Pre-assessment tests are administered before the start of each course. They establish a knowledge baseline and help instructors identify gaps. Post-assessments are administered by the instructor and are not included here.</div>
        </div>
        <div className="card-grid" style={{marginTop:4}}>
          <a className="card doc-card" href={EXAM_TM10_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-10 Pre-Assessment</div><div className="card-body">Maven User — foundation pre-test.</div></a>
          <a className="card doc-card" href={EXAM_TM20_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-20 Pre-Assessment</div><div className="card-body">No-Code Builder — pre-test.</div></a>
          <a className="card doc-card" href={EXAM_TM30_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-30 Pre-Assessment</div><div className="card-body">Advanced Builder — pre-test.</div></a>
          <a className="card doc-card" href={EXAM_TM40A_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-40A Pre-Assessment</div><div className="card-body">Intelligence WFF track — pre-test.</div></a>
          <a className="card doc-card" href={EXAM_TM40B_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-40B Pre-Assessment</div><div className="card-body">Fires WFF track — pre-test.</div></a>
          <a className="card doc-card" href={EXAM_TM40C_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-40C Pre-Assessment</div><div className="card-body">Movement &amp; Maneuver WFF track — pre-test.</div></a>
          <a className="card doc-card" href={EXAM_TM40D_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-40D Pre-Assessment</div><div className="card-body">Sustainment WFF track — pre-test.</div></a>
          <a className="card doc-card" href={EXAM_TM40E_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-40E Pre-Assessment</div><div className="card-body">Protection WFF track — pre-test.</div></a>
          <a className="card doc-card" href={EXAM_TM40F_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-40F Pre-Assessment</div><div className="card-body">Mission Command WFF track — pre-test.</div></a>
          <a className="card doc-card" href={EXAM_TM40G_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-40G Pre-Assessment</div><div className="card-body">ORSA specialist — pre-test.</div></a>
          <a className="card doc-card" href={EXAM_TM40H_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-40H Pre-Assessment</div><div className="card-body">AI Engineer — pre-test.</div></a>
          <a className="card doc-card" href={EXAM_TM40I_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-40I Pre-Assessment</div><div className="card-body">ML Engineer — pre-test.</div></a>
          <a className="card doc-card" href={EXAM_TM40J_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-40J Pre-Assessment</div><div className="card-body">Program Manager — pre-test.</div></a>
          <a className="card doc-card" href={EXAM_TM40K_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-40K Pre-Assessment</div><div className="card-body">Knowledge Manager — pre-test.</div></a>
          <a className="card doc-card" href={EXAM_TM40L_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-40L Pre-Assessment</div><div className="card-body">Software Engineer — pre-test.</div></a>
          <a className="card doc-card" href={EXAM_TM50G_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-50G Pre-Assessment</div><div className="card-body">Advanced ORSA — pre-test.</div></a>
          <a className="card doc-card" href={EXAM_TM50H_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-50H Pre-Assessment</div><div className="card-body">Advanced AI Engineer — pre-test.</div></a>
          <a className="card doc-card" href={EXAM_TM50I_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-50I Pre-Assessment</div><div className="card-body">Advanced ML Engineer — pre-test.</div></a>
          <a className="card doc-card" href={EXAM_TM50J_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-50J Pre-Assessment</div><div className="card-body">Advanced Program Manager — pre-test.</div></a>
          <a className="card doc-card" href={EXAM_TM50K_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-50K Pre-Assessment</div><div className="card-body">Advanced Knowledge Manager — pre-test.</div></a>
          <a className="card doc-card" href={EXAM_TM50L_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-50L Pre-Assessment</div><div className="card-body">Advanced Software Engineer — pre-test.</div></a>
        </div>
      </details>

      <details>
        <summary style={{fontSize:14,fontWeight:700,letterSpacing:'.08em',textTransform:'uppercase',color:'var(--navy)',cursor:'pointer',padding:'8px 0',borderBottom:'1px solid var(--gray-200)',marginBottom:12}}>Course Syllabi (15 &mdash; click to expand)</summary>
        <div className="card-grid" style={{marginTop:12}}>
          <a className="card doc-card" href={URLS.SYL_TM10} target="_blank" rel="noreferrer"><div className="card-label">SYLLABUS</div><div className="card-title">TM-10 Syllabus</div><div className="card-body">Maven User — all staff.</div></a>
          <a className="card doc-card" href={URLS.SYL_TM20} target="_blank" rel="noreferrer"><div className="card-label">SYLLABUS</div><div className="card-title">TM-20 Syllabus</div><div className="card-body">No-Code Builder — all staff.</div></a>
          <a className="card doc-card" href={URLS.SYL_TM30} target="_blank" rel="noreferrer"><div className="card-label">SYLLABUS</div><div className="card-title">TM-30 Syllabus</div><div className="card-body">Advanced No-Code Builder — data-adjacent MOS.</div></a>
          <a className="card doc-card" href={URLS.SYL_TM40A} target="_blank" rel="noreferrer"><div className="card-label">SYLLABUS</div><div className="card-title">TM-40A Syllabus</div><div className="card-body">Intelligence warfighting function track.</div></a>
          <a className="card doc-card" href={URLS.SYL_TM40B} target="_blank" rel="noreferrer"><div className="card-label">SYLLABUS</div><div className="card-title">TM-40B Syllabus</div><div className="card-body">Fires warfighting function track.</div></a>
          <a className="card doc-card" href={URLS.SYL_TM40C} target="_blank" rel="noreferrer"><div className="card-label">SYLLABUS</div><div className="card-title">TM-40C Syllabus</div><div className="card-body">Movement &amp; Maneuver warfighting function track.</div></a>
          <a className="card doc-card" href={URLS.SYL_TM40D} target="_blank" rel="noreferrer"><div className="card-label">SYLLABUS</div><div className="card-title">TM-40D Syllabus</div><div className="card-body">Sustainment warfighting function track.</div></a>
          <a className="card doc-card" href={URLS.SYL_TM40E} target="_blank" rel="noreferrer"><div className="card-label">SYLLABUS</div><div className="card-title">TM-40E Syllabus</div><div className="card-body">Protection warfighting function track.</div></a>
          <a className="card doc-card" href={URLS.SYL_TM40F} target="_blank" rel="noreferrer"><div className="card-label">SYLLABUS</div><div className="card-title">TM-40F Syllabus</div><div className="card-body">Mission Command warfighting function track.</div></a>
          <a className="card doc-card" href={URLS.SYL_TM40G} target="_blank" rel="noreferrer"><div className="card-label">SYLLABUS</div><div className="card-title">TM-40G Syllabus</div><div className="card-body">ORSA specialists.</div></a>
          <a className="card doc-card" href={URLS.SYL_TM40H} target="_blank" rel="noreferrer"><div className="card-label">SYLLABUS</div><div className="card-title">TM-40H Syllabus</div><div className="card-body">AI Engineers.</div></a>
          <a className="card doc-card" href={URLS.SYL_TM40I} target="_blank" rel="noreferrer"><div className="card-label">SYLLABUS</div><div className="card-title">TM-40I Syllabus</div><div className="card-body">ML Engineers.</div></a>
          <a className="card doc-card" href={URLS.SYL_TM40J} target="_blank" rel="noreferrer"><div className="card-label">SYLLABUS</div><div className="card-title">TM-40J Syllabus</div><div className="card-body">Program Managers.</div></a>
          <a className="card doc-card" href={URLS.SYL_TM40K} target="_blank" rel="noreferrer"><div className="card-label">SYLLABUS</div><div className="card-title">TM-40K Syllabus</div><div className="card-body">Knowledge Managers.</div></a>
          <a className="card doc-card" href={URLS.SYL_TM40L} target="_blank" rel="noreferrer"><div className="card-label">SYLLABUS</div><div className="card-title">TM-40L Syllabus</div><div className="card-body">Software Engineers.</div></a>
        </div>
      </details>

      <details>
        <summary style={{fontSize:14,fontWeight:700,letterSpacing:'.08em',textTransform:'uppercase',color:'var(--navy)',cursor:'pointer',padding:'8px 0',borderBottom:'1px solid var(--gray-200)',marginBottom:12}}>Lesson Plans (5 &mdash; click to expand)</summary>
        <div className="card-grid" style={{marginTop:12}}>
          <a className="card doc-card" href={URLS.LP_TM10} target="_blank" rel="noreferrer"><div className="card-label">LESSON PLAN</div><div className="card-title">TM-10 Lesson Plans</div><div className="card-body">Instructor lesson plans for TM-10 Maven User.</div></a>
          <a className="card doc-card" href={URLS.LP_TM20} target="_blank" rel="noreferrer"><div className="card-label">LESSON PLAN</div><div className="card-title">TM-20 Lesson Plan Outlines</div><div className="card-body">Instructor lesson plan outlines for TM-20 Builder.</div></a>
          <a className="card doc-card" href={URLS.LP_TM30} target="_blank" rel="noreferrer"><div className="card-label">LESSON PLAN</div><div className="card-title">TM-30 Lesson Plan Outlines</div><div className="card-body">Instructor lesson plan outlines for TM-30 Advanced Builder.</div></a>
          <a className="card doc-card" href={URLS.LP_TM40_SPECIALIST} target="_blank" rel="noreferrer"><div className="card-label">LESSON PLAN</div><div className="card-title">TM-40 Specialist Lesson Plans</div><div className="card-body">Instructor lesson plan outlines for all TM-40 specialist tracks.</div></a>
          <a className="card doc-card" href={URLS.LP_TEMPLATE} target="_blank" rel="noreferrer"><div className="card-label">TEMPLATE</div><div className="card-title">Lesson Plan Template</div><div className="card-body">Blank lesson plan template for course development.</div></a>
        </div>
      </details>

      <details>
        <summary style={{fontSize:14,fontWeight:700,letterSpacing:'.08em',textTransform:'uppercase',color:'var(--navy)',cursor:'pointer',padding:'8px 0',borderBottom:'1px solid var(--gray-200)',marginBottom:12}}>Administrative &amp; Institutional (10 &mdash; click to expand)</summary>
        <div className="card-grid" style={{marginTop:12}}>
          <a className="card doc-card" href={URLS.POI} target="_blank" rel="noreferrer"><div className="card-label">POI</div><div className="card-title">Program of Instruction</div><div className="card-body">MSS curriculum Program of Instruction.</div></a>
          <a className="card doc-card" href={URLS.TEO} target="_blank" rel="noreferrer"><div className="card-label">TEO</div><div className="card-title">Training &amp; Evaluation Outline</div><div className="card-body">MSS training and evaluation outline.</div></a>
          <a className="card doc-card" href={URLS.ENROLLMENT_SOP} target="_blank" rel="noreferrer"><div className="card-label">SOP</div><div className="card-title">Enrollment SOP</div><div className="card-body">Standard operating procedure for course enrollment.</div></a>
          <a className="card doc-card" href={URLS.CURRICULUM_SOP} target="_blank" rel="noreferrer"><div className="card-label">SOP</div><div className="card-title">Curriculum Maintenance SOP</div><div className="card-body">Procedures for maintaining and updating curriculum.</div></a>
          <a className="card doc-card" href={URLS.ANNUAL_SCHEDULE} target="_blank" rel="noreferrer"><div className="card-label">SCHEDULE</div><div className="card-title">Annual Training Schedule</div><div className="card-body">Full-year MSS training schedule.</div></a>
          <a className="card doc-card" href={URLS.POLICY_LETTER} target="_blank" rel="noreferrer"><div className="card-label">POLICY</div><div className="card-title">Policy Letter</div><div className="card-body">Command policy letter governing MSS training.</div></a>
          <a className="card doc-card" href={URLS.COMPLETION_CERT} target="_blank" rel="noreferrer"><div className="card-label">TEMPLATE</div><div className="card-title">Completion Certificate</div><div className="card-body">Course completion certificate template.</div></a>
          <a className="card doc-card" href={URLS.AAR_TEMPLATE} target="_blank" rel="noreferrer"><div className="card-label">TEMPLATE</div><div className="card-title">AAR Template</div><div className="card-body">After Action Review template for training events.</div></a>
          <a className="card doc-card" href={URLS.FACULTY_DEV_PLAN} target="_blank" rel="noreferrer"><div className="card-label">PLAN</div><div className="card-title">Faculty Development Plan</div><div className="card-body">Instructor and facilitator development plan.</div></a>
          <a className="card doc-card" href={URLS.CAD} target="_blank" rel="noreferrer"><div className="card-label">CAD</div><div className="card-title">Course Administrative Data</div><div className="card-body">Course administrative data sheet.</div></a>
        </div>
      </details>

      <div className="callout note mt-24">
        <div className="callout-label">NOT FINDING WHAT YOU NEED?</div>
        <div className="callout-body">
          Contact your unit data steward for additional publications, source files, or access to restricted materials.
          For technical support, visit the <button className="qr-link" onClick={() => showPanel('support' as any)}>Support page &rarr;</button>
          For task-level procedures, use the <button className="qr-link" onClick={() => showPanel('taskindex' as any)}>Task Index &rarr;</button>
        </div>
      </div>
    </>
  )
}
