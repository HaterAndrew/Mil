import { useState, useRef, useEffect } from 'react'
import { URLS } from '../constants/urls'

// PDFs not yet in the URLS constants — constructed from the same media set base
const BASE = 'https://mss.data.mil/mio/api/mediaSet/ri.mio.main.media-set.9c297238-56bf-46d4-881a-db21-dcee1c/file'

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
const EXAM_TM40M_PRE = `${BASE}/EXAM_TM40M_PRE.pdf`
const EXAM_TM40J_PRE = `${BASE}/EXAM_TM40J_PRE.pdf`
const EXAM_TM40K_PRE = `${BASE}/EXAM_TM40K_PRE.pdf`
const EXAM_TM40L_PRE = `${BASE}/EXAM_TM40L_PRE.pdf`
const EXAM_TM50G_PRE = `${BASE}/EXAM_TM50G_PRE.pdf`
const EXAM_TM50H_PRE = `${BASE}/EXAM_TM50H_PRE.pdf`
const EXAM_TM50M_PRE = `${BASE}/EXAM_TM50M_PRE.pdf`
const EXAM_TM50J_PRE = `${BASE}/EXAM_TM50J_PRE.pdf`
const EXAM_TM50K_PRE = `${BASE}/EXAM_TM50K_PRE.pdf`
const EXAM_TM50L_PRE = `${BASE}/EXAM_TM50L_PRE.pdf`

interface Props {
  showPanel: (id: string) => void
}

export default function Documents({ showPanel }: Props) {
  const [search, setSearch] = useState('')
  const contentRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    const root = contentRef.current
    if (!root) return
    const q = search.toLowerCase().trim()

    // Filter doc-card links and track-card links
    root.querySelectorAll<HTMLElement>('.doc-card').forEach(card => {
      const text = card.textContent?.toLowerCase() ?? ''
      card.style.display = q && !text.includes(q) ? 'none' : ''
    })

    // Filter table rows (doctrinal refs, reading lists)
    root.querySelectorAll<HTMLElement>('tbody tr').forEach(row => {
      const text = row.textContent?.toLowerCase() ?? ''
      row.style.display = q && !text.includes(q) ? 'none' : ''
    })

    // Auto-open details sections that have visible matches; collapse empty ones
    root.querySelectorAll<HTMLDetailsElement>('details').forEach(det => {
      if (!q) { det.removeAttribute('data-search-opened'); return }
      const hasVisible = det.querySelector('.doc-card:not([style*="display: none"]), tbody tr:not([style*="display: none"])') !== null
      if (hasVisible && !det.open) {
        det.open = true
        det.setAttribute('data-search-opened', '1')
      } else if (!hasVisible && det.getAttribute('data-search-opened') === '1') {
        det.open = false
        det.removeAttribute('data-search-opened')
      }
    })
  }, [search])

  return (
    <>
      <div className="section-header">
        <div className="section-badge">DOCUMENTS</div>
        <div className="section-title">All Training Publications</div>
        <div className="section-subtitle">Click any publication to open the PDF</div>
      </div>

      <div style={{position:'sticky',top:0,zIndex:100,background:'var(--navy)',padding:'12px 20px',display:'flex',alignItems:'center',gap:12,boxShadow:'0 2px 8px rgba(0,0,0,.25)',borderRadius:4,marginBottom:16}}>
        <label htmlFor="doc-search" style={{fontFamily:'Arial,Helvetica,sans-serif',fontSize:11,fontWeight:700,color:'#C8971A',letterSpacing:2,textTransform:'uppercase',whiteSpace:'nowrap'}}>Search:</label>
        <input
          id="doc-search"
          type="text"
          placeholder="Filter publications by title, track, or keyword..."
          autoComplete="off"
          value={search}
          onChange={e => setSearch(e.target.value)}
          style={{flex:1,padding:'8px 12px',background:'#163A6C',border:'1px solid #1E4A88',borderRadius:3,color:'#fff',fontFamily:"'Courier New',Courier,monospace",fontSize:14,outline:'none'}}
        />
        {search && (
          <button onClick={() => setSearch('')} style={{background:'none',border:'none',color:'#7A88A8',cursor:'pointer',fontSize:16,padding:'4px 8px'}} title="Clear search">&times;</button>
        )}
      </div>

      <div ref={contentRef}>

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
        <summary style={{fontSize:14,fontWeight:700,letterSpacing:'.08em',textTransform:'uppercase',color:'var(--navy)',cursor:'pointer',padding:'8px 0',borderBottom:'1px solid var(--gray-200)',marginBottom:12}}>TM-40 Technical Specialist Tracks (8 &mdash; click to expand)</summary>
        <div className="track-grid" style={{marginTop:12}}>
          <a className="track-card doc-card" href={URLS.TM40G} target="_blank" rel="noreferrer">
            <div className="track-card-hdr"><div className="track-tm">TM-40G &mdash; ORSA</div><div className="track-chip">Specialist</div></div>
            <div className="track-body"><div className="track-name">Operational Research Systems Analysis</div><div className="track-audience">ORSA specialists — quantitative methods, commander products</div><ul className="track-topics"><li>Regression, classification, forecasting</li><li>Monte Carlo COA analysis</li><li>Optimization and sensitivity analysis</li></ul></div>
          </a>
          <a className="track-card doc-card" href={URLS.TM40H} target="_blank" rel="noreferrer">
            <div className="track-card-hdr"><div className="track-tm">TM-40H &mdash; AI Engineer</div><div className="track-chip">Specialist</div></div>
            <div className="track-body"><div className="track-name">AI Engineering</div><div className="track-audience">AI engineers — AIP Logic, Agents, LLM integration</div><ul className="track-topics"><li>AIP Logic workflow design</li><li>Agent configuration</li><li>LLM integration patterns</li></ul></div>
          </a>
          <a className="track-card doc-card" href={URLS.TM40M} target="_blank" rel="noreferrer">
            <div className="track-card-hdr"><div className="track-tm">TM-40M &mdash; ML Engineer</div><div className="track-chip">Specialist</div></div>
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
          <a className="track-card doc-card" href={URLS.TM40N} target="_blank" rel="noreferrer">
            <div className="track-card-hdr"><div className="track-tm">TM-40N &mdash; UI/UX Designer</div><div className="track-chip">Specialist</div></div>
            <div className="track-body"><div className="track-name">UI/UX Design</div><div className="track-audience">Designers — Soldier Centered Design, Workshop UI, accessibility</div><ul className="track-topics"><li>User research, contextual inquiry</li><li>Information architecture, prototyping</li><li>Section 508, WCAG 2.1 AA</li></ul></div>
          </a>
          <a className="track-card doc-card" href={URLS.TM40O} target="_blank" rel="noreferrer">
            <div className="track-card-hdr"><div className="track-tm">TM-40O &mdash; Platform Engineer</div><div className="track-chip">Specialist</div></div>
            <div className="track-body"><div className="track-name">Platform Engineering</div><div className="track-audience">Platform engineers — Kubernetes, CI/CD, DevSecOps, IaC</div><ul className="track-topics"><li>K8s cluster operations</li><li>GitOps, container security</li><li>DDIL deployment, RMF/ATO</li></ul></div>
          </a>
        </div>
      </details>

      <details>
        <summary style={{fontSize:14,fontWeight:700,letterSpacing:'.08em',textTransform:'uppercase',color:'var(--navy)',cursor:'pointer',padding:'8px 0',borderBottom:'1px solid var(--gray-200)',marginBottom:12}}>TM-50 Advanced Technical Tracks (8 &mdash; click to expand)</summary>
        <div className="track-grid" style={{marginTop:12}}>
          <a className="track-card doc-card" href={URLS.TM50G} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-50G &mdash; ORSA Advanced</div><div className="track-chip">Advanced</div></div><div className="track-body"><div className="track-name">Advanced ORSA</div><div className="track-audience">Nonlinear programming, stochastic models, ABMS, campaign assessment</div></div></a>
          <a className="track-card doc-card" href={URLS.TM50H} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-50H &mdash; AI Engineer Advanced</div><div className="track-chip">Advanced</div></div><div className="track-body"><div className="track-name">Advanced AI Engineering</div><div className="track-audience">Multi-agent orchestration, RAG, red-team assessment, AI observability</div></div></a>
          <a className="track-card doc-card" href={URLS.TM50M} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-50M &mdash; ML Engineer Advanced</div><div className="track-chip">Advanced</div></div><div className="track-body"><div className="track-name">Advanced ML Engineering</div><div className="track-audience">AutoML, Transformer fine-tuning, GNNs, federated retraining, adversarial robustness</div></div></a>
          <a className="track-card doc-card" href={URLS.TM50J} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-50J &mdash; PM Advanced</div><div className="track-chip">Advanced</div></div><div className="track-body"><div className="track-name">Advanced Program Management</div><div className="track-audience">PI planning, cross-team governance, GO/SES briefing, Palantir partnership</div></div></a>
          <a className="track-card doc-card" href={URLS.TM50K} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-50K &mdash; KM Advanced</div><div className="track-chip">Advanced</div></div><div className="track-body"><div className="track-name">Advanced Knowledge Management</div><div className="track-audience">Federated KM architecture, NATO integration, STANAG 4778, knowledge graphs</div></div></a>
          <a className="track-card doc-card" href={URLS.TM50L} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-50L &mdash; SWE Advanced</div><div className="track-chip">Advanced</div></div><div className="track-body"><div className="track-name">Advanced Software Engineering</div><div className="track-audience">Scale, multi-tenancy, Kafka, OWASP, SAST, architecture review, platform governance</div></div></a>
          <a className="track-card doc-card" href={URLS.TM50N} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-50N &mdash; UI/UX Advanced</div><div className="track-chip">Advanced</div></div><div className="track-body"><div className="track-name">Advanced UI/UX Design</div><div className="track-audience">Design systems, DDIL-aware UI, DesignOps, enterprise accessibility</div></div></a>
          <a className="track-card doc-card" href={URLS.TM50O} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-50O &mdash; Platform Eng Advanced</div><div className="track-chip">Advanced</div></div><div className="track-body"><div className="track-name">Advanced Platform Engineering</div><div className="track-audience">Fleet management, SRE, RMF/ATO automation, cross-domain infrastructure</div></div></a>
        </div>
      </details>

      <details>
        <summary style={{fontSize:14,fontWeight:700,letterSpacing:'.08em',textTransform:'uppercase',color:'var(--navy)',cursor:'pointer',padding:'8px 0',borderBottom:'1px solid var(--gray-200)',marginBottom:12}}>Train the Trainer &mdash; T3 (2 courses + SOPs &mdash; click to expand)</summary>
        <div className="callout note" style={{marginTop:12,marginBottom:12}}>
          <div className="callout-label">NOTE &mdash; T3 PROGRAM</div>
          <div className="callout-body">T3-I (Instructor Certification) and T3-F (MSC Force Multiplier) sit <strong>outside</strong> the TM-10 to TM-50 numbering chain. T3-I requires TM-30 + C2DAO selection. T3-F requires TM-20 + CDR nomination. See the Commander's Guide for nomination procedures.</div>
        </div>
        <div className="track-grid" style={{marginTop:12}}>
          <a className="track-card doc-card" href={URLS.T3I} target="_blank" rel="noreferrer">
            <div className="track-card-hdr"><div className="track-tm">T3-I &mdash; Instructor Certification</div><div className="track-chip">5 days + practicum</div></div>
            <div className="track-body"><div className="track-name">Certify MSS Instructors</div><div className="track-audience">Prereq: TM-30 + C2DAO selection &bull; 3-tier hierarchy: Instructor &rarr; Senior &rarr; Master</div></div>
          </a>
          <a className="track-card doc-card" href={URLS.T3F} target="_blank" rel="noreferrer">
            <div className="track-card-hdr"><div className="track-tm">T3-F &mdash; MSC Force Multiplier</div><div className="track-chip">3 days</div></div>
            <div className="track-body"><div className="track-name">Unit Data Trainer (UDT)</div><div className="track-audience">Prereq: TM-20 + CDR nomination &bull; Delivers TM-10 locally at your MSC</div></div>
          </a>
        </div>
        <div className="card-grid card-grid-2" style={{marginTop:12}}>
          <a className="card doc-card" href={URLS.SYL_T3I} target="_blank" rel="noreferrer"><div className="card-label">SYLLABUS</div><div className="card-title">T3-I Syllabus</div><div className="card-body">Instructor Certification course syllabus.</div></a>
          <a className="card doc-card" href={URLS.SYL_T3F} target="_blank" rel="noreferrer"><div className="card-label">SYLLABUS</div><div className="card-title">T3-F Syllabus</div><div className="card-body">MSC Force Multiplier course syllabus.</div></a>
          <a className="card doc-card" href={URLS.INSTRUCTOR_TIERS} target="_blank" rel="noreferrer"><div className="card-label">SOP</div><div className="card-title">Instructor Tier Definitions</div><div className="card-body">4-tier structure: Instructor, Senior, Master, UDT.</div></a>
          <a className="card doc-card" href={URLS.SME_RUBRIC} target="_blank" rel="noreferrer"><div className="card-label">SOP</div><div className="card-title">C2DAO SME Designation Rubric</div><div className="card-body">Formal SME criteria per domain.</div></a>
          <a className="card doc-card" href={URLS.UDT_SOP} target="_blank" rel="noreferrer"><div className="card-label">SOP</div><div className="card-title">Unit Data Trainer SOP</div><div className="card-body">UDT employment, reporting, sustainment.</div></a>
          <a className="card doc-card" href={URLS.MTT_SOP} target="_blank" rel="noreferrer"><div className="card-label">SOP</div><div className="card-title">MTT Operations SOP</div><div className="card-body">Mobile Training Team rotation procedures.</div></a>
          <a className="card doc-card" href={URLS.SUCCESSOR_GUIDE} target="_blank" rel="noreferrer"><div className="card-label">GUIDE</div><div className="card-title">Successor Planning Guide</div><div className="card-body">Instructor and UDT succession planning.</div></a>
        </div>
      </details>

      <details>
        <summary style={{fontSize:14,fontWeight:700,letterSpacing:'.08em',textTransform:'uppercase',color:'var(--navy)',cursor:'pointer',padding:'8px 0',borderBottom:'1px solid var(--gray-200)',marginBottom:12}}>Concepts Guides (18 &mdash; click to expand)</summary>
        <div className="track-grid" style={{marginTop:12}}>
          <a className="track-card doc-card" href={URLS.CG_TM40A} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-40A Concepts Guide</div><div className="track-chip">Intelligence</div></div><div className="track-body"><div className="track-audience">Key concepts and terminology for the Intelligence WFF track.</div></div></a>
          <a className="track-card doc-card" href={URLS.CG_TM40B} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-40B Concepts Guide</div><div className="track-chip">Fires</div></div><div className="track-body"><div className="track-audience">Key concepts and terminology for the Fires WFF track.</div></div></a>
          <a className="track-card doc-card" href={URLS.CG_TM40C} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-40C Concepts Guide</div><div className="track-chip">Movement &amp; Maneuver</div></div><div className="track-body"><div className="track-audience">Key concepts and terminology for the Movement &amp; Maneuver WFF track.</div></div></a>
          <a className="track-card doc-card" href={URLS.CG_TM40D} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-40D Concepts Guide</div><div className="track-chip">Sustainment</div></div><div className="track-body"><div className="track-audience">Key concepts and terminology for the Sustainment WFF track.</div></div></a>
          <a className="track-card doc-card" href={URLS.CG_TM40E} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-40E Concepts Guide</div><div className="track-chip">Protection</div></div><div className="track-body"><div className="track-audience">Key concepts and terminology for the Protection WFF track.</div></div></a>
          <a className="track-card doc-card" href={URLS.CG_TM40F} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-40F Concepts Guide</div><div className="track-chip">Mission Command</div></div><div className="track-body"><div className="track-audience">Key concepts and terminology for the Mission Command WFF track.</div></div></a>
          <a className="track-card doc-card" href={URLS.CG_TM40G} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-40G Concepts Guide</div><div className="track-chip">ORSA</div></div><div className="track-body"><div className="track-audience">Key concepts and terminology for the ORSA specialist track.</div></div></a>
          <a className="track-card doc-card" href={URLS.CG_TM40H} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-40H Concepts Guide</div><div className="track-chip">AI Engineer</div></div><div className="track-body"><div className="track-audience">Key concepts and terminology for the AI Engineer track.</div></div></a>
          <a className="track-card doc-card" href={URLS.CG_TM40M} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-40M Concepts Guide</div><div className="track-chip">ML Engineer</div></div><div className="track-body"><div className="track-audience">Key concepts and terminology for the ML Engineer track.</div></div></a>
          <a className="track-card doc-card" href={URLS.CG_TM40J} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-40J Concepts Guide</div><div className="track-chip">Program Mgr</div></div><div className="track-body"><div className="track-audience">Key concepts and terminology for the Program Manager track.</div></div></a>
          <a className="track-card doc-card" href={URLS.CG_TM40K} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-40K Concepts Guide</div><div className="track-chip">Knowledge Mgr</div></div><div className="track-body"><div className="track-audience">Key concepts and terminology for the Knowledge Manager track.</div></div></a>
          <a className="track-card doc-card" href={URLS.CG_TM40L} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-40L Concepts Guide</div><div className="track-chip">Software Eng</div></div><div className="track-body"><div className="track-audience">Key concepts and terminology for the Software Engineer track.</div></div></a>
          <a className="track-card doc-card" href={URLS.CG_TM50G} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-50G Concepts Guide</div><div className="track-chip">ORSA Adv</div></div><div className="track-body"><div className="track-audience">Advanced concepts and terminology for TM-50G.</div></div></a>
          <a className="track-card doc-card" href={URLS.CG_TM50H} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-50H Concepts Guide</div><div className="track-chip">AI Eng Adv</div></div><div className="track-body"><div className="track-audience">Advanced concepts and terminology for TM-50H.</div></div></a>
          <a className="track-card doc-card" href={URLS.CG_TM50M} target="_blank" rel="noreferrer"><div className="track-card-hdr"><div className="track-tm">TM-50M Concepts Guide</div><div className="track-chip">MLE Adv</div></div><div className="track-body"><div className="track-audience">Advanced concepts and terminology for TM-50M.</div></div></a>
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
          <a className="card doc-card" href={URLS.EX40M} target="_blank" rel="noreferrer"><div className="card-label">EXERCISE</div><div className="card-title">TM-40M Exercise (ML Eng)</div><div className="card-body">ML Engineer practical exercise.</div></a>
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
          <a className="card doc-card" href={EXAM_TM40M_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-40M Pre-Assessment</div><div className="card-body">ML Engineer — pre-test.</div></a>
          <a className="card doc-card" href={EXAM_TM40J_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-40J Pre-Assessment</div><div className="card-body">Program Manager — pre-test.</div></a>
          <a className="card doc-card" href={EXAM_TM40K_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-40K Pre-Assessment</div><div className="card-body">Knowledge Manager — pre-test.</div></a>
          <a className="card doc-card" href={EXAM_TM40L_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-40L Pre-Assessment</div><div className="card-body">Software Engineer — pre-test.</div></a>
          <a className="card doc-card" href={EXAM_TM50G_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-50G Pre-Assessment</div><div className="card-body">Advanced ORSA — pre-test.</div></a>
          <a className="card doc-card" href={EXAM_TM50H_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-50H Pre-Assessment</div><div className="card-body">Advanced AI Engineer — pre-test.</div></a>
          <a className="card doc-card" href={EXAM_TM50M_PRE} target="_blank" rel="noreferrer"><div className="card-label">PRE-TEST</div><div className="card-title">TM-50M Pre-Assessment</div><div className="card-body">Advanced ML Engineer — pre-test.</div></a>
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
          <a className="card doc-card" href={URLS.SYL_TM40M} target="_blank" rel="noreferrer"><div className="card-label">SYLLABUS</div><div className="card-title">TM-40M Syllabus</div><div className="card-body">ML Engineers.</div></a>
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

      <details open style={{background:'#f4f5f8',border:'1px dashed var(--gray-200)',borderRadius:8,padding:'16px 16px 8px',marginTop:16}}>
        <summary style={{fontSize:14,fontWeight:700,letterSpacing:'.08em',textTransform:'uppercase',color:'var(--navy)',cursor:'pointer',padding:'8px 0',borderBottom:'1px solid var(--gray-200)',marginBottom:12}}>External Doctrinal &amp; Strategic References</summary>

        <div className="callout info" style={{marginTop:12,marginBottom:12}}>
          <div className="callout-label">REFERENCE ONLY</div>
          <div className="callout-body">Items below are <strong>not clickable links</strong>. They are external publications listed here for reference and citation. Obtain them through official Army, DoD, or NATO distribution channels.</div>
        </div>

        <div className="callout note" style={{marginTop:0,marginBottom:12}}>
          <div className="callout-label">CLASSIFICATION</div>
          <div className="callout-body">References are categorized as <strong>Doctrine</strong> (regulatory authority — ARs, FMs, DoD Directives, NATO STANAGs) or <strong>Strategic Guidance</strong> (authoritative but not regulatory — strategies, plans, frameworks). This distinction matters for compliance and citation.</div>
        </div>

        {/* Army Doctrine & Regulation */}
        <h3 style={{color:'var(--navy)',margin:'16px 0 8px',fontSize:14,letterSpacing:'.05em'}}>ARMY DOCTRINE &amp; REGULATION</h3>
        <table style={{width:'100%',borderCollapse:'collapse',fontSize:13,marginBottom:16}}>
          <thead><tr style={{background:'var(--navy)',color:'#fff',textAlign:'left'}}><th style={{padding:'6px 8px'}}>Publication</th><th style={{padding:'6px 8px'}}>Title</th><th style={{padding:'6px 8px'}}>Type</th><th style={{padding:'6px 8px'}}>Tracks</th></tr></thead>
          <tbody>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>ADP 3-0</td><td style={{padding:'5px 8px'}}>Operations</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>WFF (A–F)</td></tr>
            <tr><td style={{padding:'5px 8px'}}>ADP 3-19</td><td style={{padding:'5px 8px'}}>Fires</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40B</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>ADP 3-37</td><td style={{padding:'5px 8px'}}>Protection of the Force (Jul 2019)</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40E</td></tr>
            <tr><td style={{padding:'5px 8px'}}>ADP 3-90</td><td style={{padding:'5px 8px'}}>Offense and Defense</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40C</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>ADP 5-0</td><td style={{padding:'5px 8px'}}>The Operations Process</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40F, TM-40G</td></tr>
            <tr><td style={{padding:'5px 8px'}}>ADP 6-0</td><td style={{padding:'5px 8px'}}>Mission Command (Jul 2019)</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40F</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>ADP 7-0</td><td style={{padding:'5px 8px'}}>Training</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>Training Mgmt</td></tr>
            <tr><td style={{padding:'5px 8px'}}>AR 25-1</td><td style={{padding:'5px 8px'}}>Army Information Technology (Jul 2019)</td><td style={{padding:'5px 8px'}}>Regulation</td><td style={{padding:'5px 8px'}}>All</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>AR 25-2</td><td style={{padding:'5px 8px'}}>Army Cybersecurity (Apr 2019)</td><td style={{padding:'5px 8px'}}>Regulation</td><td style={{padding:'5px 8px'}}>TM-40H, TM-40M, TM-40L</td></tr>
            <tr><td style={{padding:'5px 8px'}}>AR 25-30</td><td style={{padding:'5px 8px'}}>Army Publishing Program</td><td style={{padding:'5px 8px'}}>Regulation</td><td style={{padding:'5px 8px'}}>TM-50H</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>AR 25-400-2</td><td style={{padding:'5px 8px'}}>Army Records Management</td><td style={{padding:'5px 8px'}}>Regulation</td><td style={{padding:'5px 8px'}}>TM-40K</td></tr>
            <tr><td style={{padding:'5px 8px'}}>AR 5-11</td><td style={{padding:'5px 8px'}}>Management of Army Models and Simulations</td><td style={{padding:'5px 8px'}}>Regulation</td><td style={{padding:'5px 8px'}}>TM-40G</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>AR 71-9</td><td style={{padding:'5px 8px'}}>Warfighting Analysis</td><td style={{padding:'5px 8px'}}>Regulation</td><td style={{padding:'5px 8px'}}>TM-40G</td></tr>
            <tr><td style={{padding:'5px 8px'}}>AR 350-1</td><td style={{padding:'5px 8px'}}>Army Training and Leader Development</td><td style={{padding:'5px 8px'}}>Regulation</td><td style={{padding:'5px 8px'}}>Training Mgmt</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>AR 525-2</td><td style={{padding:'5px 8px'}}>Force Protection</td><td style={{padding:'5px 8px'}}>Regulation</td><td style={{padding:'5px 8px'}}>TM-40E</td></tr>
            <tr><td style={{padding:'5px 8px'}}>AR 530-1</td><td style={{padding:'5px 8px'}}>Operations Security</td><td style={{padding:'5px 8px'}}>Regulation</td><td style={{padding:'5px 8px'}}>TM-40E</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>FM 2-0</td><td style={{padding:'5px 8px'}}>Intelligence (Oct 2023)</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40A</td></tr>
            <tr><td style={{padding:'5px 8px'}}>FM 3-0</td><td style={{padding:'5px 8px'}}>Operations (Mar 2025)</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>WFF (A–F)</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>FM 3-01</td><td style={{padding:'5px 8px'}}>U.S. Army Air and Missile Defense</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40B</td></tr>
            <tr><td style={{padding:'5px 8px'}}>FM 3-09</td><td style={{padding:'5px 8px'}}>Fire Support and Field Artillery Operations (Aug 2024)</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40B, TM-40C</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>FM 3-12</td><td style={{padding:'5px 8px'}}>Cyberspace and EW Operations</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40E, TM-40H, TM-40M, TM-40L</td></tr>
            <tr><td style={{padding:'5px 8px'}}>FM 3-27</td><td style={{padding:'5px 8px'}}>Army Global Ballistic Missile Defense</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40B</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>FM 3-55</td><td style={{padding:'5px 8px'}}>Information Collection</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40A</td></tr>
            <tr><td style={{padding:'5px 8px'}}>FM 3-60</td><td style={{padding:'5px 8px'}}>Targeting (Aug 2023)</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40B</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>FM 3-81</td><td style={{padding:'5px 8px'}}>Maneuver Enhancement Brigade</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40C</td></tr>
            <tr><td style={{padding:'5px 8px'}}>FM 3-90</td><td style={{padding:'5px 8px'}}>Offense and Defense (May 2023)</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40C</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>FM 4-0</td><td style={{padding:'5px 8px'}}>Sustainment (Aug 2024)</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40D</td></tr>
            <tr><td style={{padding:'5px 8px'}}>FM 1-0</td><td style={{padding:'5px 8px'}}>Human Resources Support</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40D</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>FM 5-0</td><td style={{padding:'5px 8px'}}>Planning and Orders Production (Nov 2024)</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40F, TM-40C</td></tr>
            <tr><td style={{padding:'5px 8px'}}>FM 6-0</td><td style={{padding:'5px 8px'}}>Commander's Activities (May 2022)</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40F, TM-40C</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>FM 7-0</td><td style={{padding:'5px 8px'}}>Training (Jun 2021)</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>Training Mgmt</td></tr>
            <tr><td style={{padding:'5px 8px'}}>ATP 2-01</td><td style={{padding:'5px 8px'}}>Collection Management (May 2023)</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40A</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>ATP 2-33.4</td><td style={{padding:'5px 8px'}}>Intelligence Analysis</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40A</td></tr>
            <tr><td style={{padding:'5px 8px'}}>ATP 2-22.9-1</td><td style={{padding:'5px 8px'}}>PAI/OSINT (Oct 2023)</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40A</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>ATP 3-01.81</td><td style={{padding:'5px 8px'}}>Counter-UAS</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40B</td></tr>
            <tr><td style={{padding:'5px 8px'}}>ATP 3-09.42</td><td style={{padding:'5px 8px'}}>Fire Support for M&amp;M</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40B</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>ATP 3-13.3</td><td style={{padding:'5px 8px'}}>Army Operations Security</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40E</td></tr>
            <tr><td style={{padding:'5px 8px'}}>ATP 3-90.4</td><td style={{padding:'5px 8px'}}>Combined Arms Mobility</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40C</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>ATP 5-0.1</td><td style={{padding:'5px 8px'}}>Army Design Methodology</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40F</td></tr>
            <tr><td style={{padding:'5px 8px'}}>ATP 5-0.3</td><td style={{padding:'5px 8px'}}>Multi-Service Tactics for Ops Assessment</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40G</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>ATP 6-01.1</td><td style={{padding:'5px 8px'}}>Techniques for Effective Knowledge Management</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40K, TM-50K</td></tr>
            <tr><td style={{padding:'5px 8px'}}>TC 6-0.2</td><td style={{padding:'5px 8px'}}>Battle Staff Operations</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40F</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>DA PAM 5-11</td><td style={{padding:'5px 8px'}}>Verification, Validation &amp; Accreditation</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40G</td></tr>
            <tr><td style={{padding:'5px 8px'}}>DA PAM 25-1-1</td><td style={{padding:'5px 8px'}}>IT Implementation Instructions</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40K, TM-40L</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>DA PAM 25-2-5</td><td style={{padding:'5px 8px'}}>Cybersecurity Technical Reference</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40H, TM-40M, TM-40L</td></tr>
            <tr><td style={{padding:'5px 8px'}}>DA PAM 25-40</td><td style={{padding:'5px 8px'}}>Army Publishing Program Procedures</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>Standards</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>DA PAM 25-403</td><td style={{padding:'5px 8px'}}>Army Records Information Management</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40K</td></tr>
            <tr><td style={{padding:'5px 8px'}}>DA PAM 600-3</td><td style={{padding:'5px 8px'}}>Officer Professional Development</td><td style={{padding:'5px 8px'}}>Doctrine</td><td style={{padding:'5px 8px'}}>TM-40G</td></tr>
          </tbody>
        </table>

        {/* DoD Directives & Instructions */}
        <h3 style={{color:'var(--navy)',margin:'16px 0 8px',fontSize:14,letterSpacing:'.05em'}}>DoD DIRECTIVES &amp; INSTRUCTIONS</h3>
        <table style={{width:'100%',borderCollapse:'collapse',fontSize:13,marginBottom:16}}>
          <thead><tr style={{background:'var(--navy)',color:'#fff',textAlign:'left'}}><th style={{padding:'6px 8px'}}>Publication</th><th style={{padding:'6px 8px'}}>Title</th><th style={{padding:'6px 8px'}}>Type</th><th style={{padding:'6px 8px'}}>Tracks</th></tr></thead>
          <tbody>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>DoDD 3000.09</td><td style={{padding:'5px 8px'}}>Autonomy in Weapon Systems (Jan 2023)</td><td style={{padding:'5px 8px'}}>Directive</td><td style={{padding:'5px 8px'}}>WFF (A–F)</td></tr>
            <tr><td style={{padding:'5px 8px'}}>DoDI 5000.87</td><td style={{padding:'5px 8px'}}>Software Acquisition Pathway (Oct 2020)</td><td style={{padding:'5px 8px'}}>Instruction</td><td style={{padding:'5px 8px'}}>TM-40L, TM-50L, TM-40J, TM-50J</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>Army Directive 2024-02</td><td style={{padding:'5px 8px'}}>Agile Software Dev &amp; Acquisition (Dec 2024)</td><td style={{padding:'5px 8px'}}>Directive</td><td style={{padding:'5px 8px'}}>TM-40L, TM-50L, TM-40J, TM-50J</td></tr>
            <tr><td style={{padding:'5px 8px'}}>Army Directive 2024-03</td><td style={{padding:'5px 8px'}}>Army Digital Engineering</td><td style={{padding:'5px 8px'}}>Directive</td><td style={{padding:'5px 8px'}}>TM-40H, TM-40M, TM-40L</td></tr>
          </tbody>
        </table>

        {/* TRADOC */}
        <h3 style={{color:'var(--navy)',margin:'16px 0 8px',fontSize:14,letterSpacing:'.05em'}}>TRADOC PUBLICATIONS</h3>
        <p style={{fontSize:12,color:'#666',margin:'0 0 8px'}}>Published at adminpubs.tradoc.army.mil, not armypubs.army.mil</p>
        <table style={{width:'100%',borderCollapse:'collapse',fontSize:13,marginBottom:16}}>
          <thead><tr style={{background:'var(--navy)',color:'#fff',textAlign:'left'}}><th style={{padding:'6px 8px'}}>Publication</th><th style={{padding:'6px 8px'}}>Title</th><th style={{padding:'6px 8px'}}>Type</th><th style={{padding:'6px 8px'}}>Tracks</th></tr></thead>
          <tbody>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>TR 350-70</td><td style={{padding:'5px 8px'}}>Army Learning Policy and Systems</td><td style={{padding:'5px 8px'}}>Regulation</td><td style={{padding:'5px 8px'}}>Training Mgmt</td></tr>
            <tr><td style={{padding:'5px 8px'}}>TP 350-70-3</td><td style={{padding:'5px 8px'}}>Faculty and Staff Development Program</td><td style={{padding:'5px 8px'}}>Pamphlet</td><td style={{padding:'5px 8px'}}>Training Mgmt</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>TP 350-70-7</td><td style={{padding:'5px 8px'}}>Army Educational Processes</td><td style={{padding:'5px 8px'}}>Pamphlet</td><td style={{padding:'5px 8px'}}>Training Mgmt</td></tr>
            <tr><td style={{padding:'5px 8px'}}>TP 350-70-14</td><td style={{padding:'5px 8px'}}>Training Development in Institutional Domain</td><td style={{padding:'5px 8px'}}>Pamphlet</td><td style={{padding:'5px 8px'}}>Training Mgmt</td></tr>
          </tbody>
        </table>

        {/* NATO Standards */}
        <h3 style={{color:'var(--navy)',margin:'16px 0 8px',fontSize:14,letterSpacing:'.05em'}}>NATO STANDARDS &amp; AGREEMENTS</h3>
        <table style={{width:'100%',borderCollapse:'collapse',fontSize:13,marginBottom:16}}>
          <thead><tr style={{background:'var(--navy)',color:'#fff',textAlign:'left'}}><th style={{padding:'6px 8px'}}>Publication</th><th style={{padding:'6px 8px'}}>Title</th><th style={{padding:'6px 8px'}}>Type</th><th style={{padding:'6px 8px'}}>Tracks</th></tr></thead>
          <tbody>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>ADatP-34 / NISP</td><td style={{padding:'5px 8px'}}>C3 Interoperability Standards and Profiles</td><td style={{padding:'5px 8px'}}>Standard</td><td style={{padding:'5px 8px'}}>TM-40K, TM-40L</td></tr>
            <tr><td style={{padding:'5px 8px'}}>STANAG 5636 / NCMS</td><td style={{padding:'5px 8px'}}>Core Metadata Specification</td><td style={{padding:'5px 8px'}}>STANAG</td><td style={{padding:'5px 8px'}}>TM-40K, TM-50K</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>STANAG 5643 (proposed)</td><td style={{padding:'5px 8px'}}>MIM Governance Standard</td><td style={{padding:'5px 8px'}}>STANAG</td><td style={{padding:'5px 8px'}}>TM-40K, TM-40L, TM-50K, TM-50L</td></tr>
            <tr><td style={{padding:'5px 8px'}}>ADatP-5644</td><td style={{padding:'5px 8px'}}>Web Service Messaging Profile (WSMP)</td><td style={{padding:'5px 8px'}}>Standard</td><td style={{padding:'5px 8px'}}>TM-40L, TM-50L</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>ADatP-36</td><td style={{padding:'5px 8px'}}>Friendly Force Information (FFI)</td><td style={{padding:'5px 8px'}}>Standard</td><td style={{padding:'5px 8px'}}>TM-40A, TM-40C</td></tr>
            <tr><td style={{padding:'5px 8px'}}>STANAG 5527</td><td style={{padding:'5px 8px'}}>FFT Systems Interoperability</td><td style={{padding:'5px 8px'}}>STANAG</td><td style={{padding:'5px 8px'}}>TM-40A</td></tr>
          </tbody>
        </table>

        {/* DoD Strategic Guidance */}
        <h3 style={{color:'#555',margin:'16px 0 8px',fontSize:14,letterSpacing:'.05em'}}>DoD &amp; ARMY STRATEGIC GUIDANCE <span style={{fontWeight:400,fontSize:11,color:'#888'}}>(not doctrine)</span></h3>
        <table style={{width:'100%',borderCollapse:'collapse',fontSize:13,marginBottom:16}}>
          <thead><tr style={{background:'#e8eaf0',color:'#333',textAlign:'left'}}><th style={{padding:'6px 8px'}}>Document</th><th style={{padding:'6px 8px'}}>Authority</th><th style={{padding:'6px 8px'}}>Date</th><th style={{padding:'6px 8px'}}>Tracks</th></tr></thead>
          <tbody>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>DoD Data Strategy</td><td style={{padding:'5px 8px'}}>OSD</td><td style={{padding:'5px 8px'}}>Oct 2020</td><td style={{padding:'5px 8px'}}>All</td></tr>
            <tr><td style={{padding:'5px 8px'}}>DoD Data, Analytics &amp; AI Adoption Strategy</td><td style={{padding:'5px 8px'}}>CDAO</td><td style={{padding:'5px 8px'}}>Nov 2023</td><td style={{padding:'5px 8px'}}>All</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>DoD Responsible AI Strategy</td><td style={{padding:'5px 8px'}}>CDAO</td><td style={{padding:'5px 8px'}}>Jun 2024</td><td style={{padding:'5px 8px'}}>TM-40H/M, TM-50H/M</td></tr>
            <tr><td style={{padding:'5px 8px'}}>DoD Zero Trust Reference Architecture v2.0</td><td style={{padding:'5px 8px'}}>DISA/NSA</td><td style={{padding:'5px 8px'}}>Jul 2022</td><td style={{padding:'5px 8px'}}>TM-30</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>DoD AI Cybersecurity Risk Mgmt Guide</td><td style={{padding:'5px 8px'}}>DoD CIO</td><td style={{padding:'5px 8px'}}>2024</td><td style={{padding:'5px 8px'}}>TM-40H/M, TM-50H/M</td></tr>
            <tr><td style={{padding:'5px 8px'}}>DoD Software Modernization Strategy</td><td style={{padding:'5px 8px'}}>OSD CIO</td><td style={{padding:'5px 8px'}}>Feb 2022</td><td style={{padding:'5px 8px'}}>TM-40L, TM-50L</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>JADC2 Strategy Summary</td><td style={{padding:'5px 8px'}}>Joint Staff</td><td style={{padding:'5px 8px'}}>Mar 2022</td><td style={{padding:'5px 8px'}}>WFF (A–F), TM-40G</td></tr>
            <tr><td style={{padding:'5px 8px'}}>JCOIE</td><td style={{padding:'5px 8px'}}>Joint Staff J-7</td><td style={{padding:'5px 8px'}}>Current</td><td style={{padding:'5px 8px'}}>TM-40F</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>Army Data Plan</td><td style={{padding:'5px 8px'}}>Army CIO</td><td style={{padding:'5px 8px'}}>Oct 2022</td><td style={{padding:'5px 8px'}}>All</td></tr>
            <tr><td style={{padding:'5px 8px'}}>Army Cloud Plan</td><td style={{padding:'5px 8px'}}>Army CIO</td><td style={{padding:'5px 8px'}}>Oct 2022</td><td style={{padding:'5px 8px'}}>TM-10, TM-20, TM-30</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>UDRA v1.1</td><td style={{padding:'5px 8px'}}>DASA(DES)</td><td style={{padding:'5px 8px'}}>Feb 2025</td><td style={{padding:'5px 8px'}}>TM-30, Specialist (G–O)</td></tr>
            <tr><td style={{padding:'5px 8px'}}>Army CIO Data Stewardship Memo</td><td style={{padding:'5px 8px'}}>Army CIO</td><td style={{padding:'5px 8px'}}>Apr 2024</td><td style={{padding:'5px 8px'}}>TM-10, TM-20, TM-30, TM-40K</td></tr>
          </tbody>
        </table>

        {/* NATO Strategic Guidance */}
        <h3 style={{color:'#555',margin:'16px 0 8px',fontSize:14,letterSpacing:'.05em'}}>NATO STRATEGIC GUIDANCE <span style={{fontWeight:400,fontSize:11,color:'#888'}}>(not doctrine)</span></h3>
        <table style={{width:'100%',borderCollapse:'collapse',fontSize:13,marginBottom:16}}>
          <thead><tr style={{background:'#e8eaf0',color:'#333',textAlign:'left'}}><th style={{padding:'6px 8px'}}>Document</th><th style={{padding:'6px 8px'}}>Date</th><th style={{padding:'6px 8px'}}>Tracks</th></tr></thead>
          <tbody>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>NATO Data Strategy for the Alliance</td><td style={{padding:'5px 8px'}}>Feb 2025</td><td style={{padding:'5px 8px'}}>TM-30, TM-40K, TM-50K</td></tr>
            <tr><td style={{padding:'5px 8px'}}>NATO Data Centric Reference Architecture v2</td><td style={{padding:'5px 8px'}}>2025</td><td style={{padding:'5px 8px'}}>TM-30</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>NATO Data Quality Framework for the Alliance</td><td style={{padding:'5px 8px'}}>Aug 2025</td><td style={{padding:'5px 8px'}}>TM-30</td></tr>
            <tr><td style={{padding:'5px 8px'}}>NATO Digital Transformation Implementation Strategy</td><td style={{padding:'5px 8px'}}>Oct 2024</td><td style={{padding:'5px 8px'}}>WFF (A–F)</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>NATO Warfighting Capstone Concept</td><td style={{padding:'5px 8px'}}>2021</td><td style={{padding:'5px 8px'}}>TM-40F</td></tr>
          </tbody>
        </table>
      </details>

      <details open style={{background:'#f4f5f8',border:'1px dashed var(--gray-200)',borderRadius:8,padding:'16px 16px 8px',marginTop:16}}>
        <summary style={{fontSize:14,fontWeight:700,letterSpacing:'.08em',textTransform:'uppercase',color:'var(--navy)',cursor:'pointer',padding:'8px 0',borderBottom:'1px solid var(--gray-200)',marginBottom:12}}>Professional Reading &amp; Lessons Learned (65+ articles)</summary>

        <div className="callout info" style={{marginTop:12,marginBottom:12}}>
          <div className="callout-label">REFERENCE ONLY</div>
          <div className="callout-body">Items below are <strong>not clickable links</strong>. They are curated articles from Army professional journals, military publications, and think tanks. Obtain them through the publishing organization or your unit library. Full reading lists are included as appendices in each TM publication.</div>
        </div>

        {/* Military Review */}
        <h3 style={{color:'var(--navy)',margin:'16px 0 8px',fontSize:13,letterSpacing:'.05em'}}>MILITARY REVIEW — Army University Press (14)</h3>
        <table style={{width:'100%',borderCollapse:'collapse',fontSize:13,marginBottom:16}}>
          <thead><tr style={{background:'#e8eaf0',color:'#333',textAlign:'left'}}><th style={{padding:'6px 8px'}}>Title</th><th style={{padding:'6px 8px'}}>Date</th><th style={{padding:'6px 8px'}}>Tracks</th></tr></thead>
          <tbody>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>Data-Centric at the Division: 3ID's One-Year Journey to Transform and Modernize</td><td style={{padding:'5px 8px'}}>Jan 2025</td><td style={{padding:'5px 8px'}}>All</td></tr>
            <tr><td style={{padding:'5px 8px'}}>Modernizing Military Decision-Making: Integrating AI into Army Planning</td><td style={{padding:'5px 8px'}}>Aug 2025</td><td style={{padding:'5px 8px'}}>TM-40F, TM-40H, TM-40G</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>The Military Needs Frontier Models</td><td style={{padding:'5px 8px'}}>Aug 2025</td><td style={{padding:'5px 8px'}}>TM-40H, TM-40M, TM-40L</td></tr>
            <tr><td style={{padding:'5px 8px'}}>Exploring AI-Enhanced Cyber and Information Operations Integration</td><td style={{padding:'5px 8px'}}>Mar-Apr 2025</td><td style={{padding:'5px 8px'}}>TM-40E, TM-40A, TM-40H</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>Authorities and the Multidomain Task Force</td><td style={{padding:'5px 8px'}}>Mar-Apr 2025</td><td style={{padding:'5px 8px'}}>TM-40A, TM-40B, TM-40F</td></tr>
            <tr><td style={{padding:'5px 8px'}}>Taking a Data-Centric Approach to Unit Readiness</td><td style={{padding:'5px 8px'}}>2024</td><td style={{padding:'5px 8px'}}>All, esp. TM-40G</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>Attaining Readiness by Developing a Data-Centric Culture</td><td style={{padding:'5px 8px'}}>2024</td><td style={{padding:'5px 8px'}}>All, esp. TM-40J</td></tr>
            <tr><td style={{padding:'5px 8px'}}>Sustaining Our People Advantage in Data-Centric Warfare</td><td style={{padding:'5px 8px'}}>2024</td><td style={{padding:'5px 8px'}}>All</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>AI as a Combat Multiplier: Using AI to Unburden Army Staffs</td><td style={{padding:'5px 8px'}}>Sep 2024</td><td style={{padding:'5px 8px'}}>TM-40H, TM-40F, TM-40G</td></tr>
            <tr><td style={{padding:'5px 8px'}}>Transforming the Multidomain Battlefield with AI</td><td style={{padding:'5px 8px'}}>2024</td><td style={{padding:'5px 8px'}}>TM-40H, TM-40M, TM-40A</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>The Coming Military AI Revolution</td><td style={{padding:'5px 8px'}}>May-Jun 2024</td><td style={{padding:'5px 8px'}}>TM-40H, TM-40M</td></tr>
            <tr><td style={{padding:'5px 8px'}}>AI in Modern Warfare: Strategic Innovation and Emerging Risks</td><td style={{padding:'5px 8px'}}>Sep-Oct 2024</td><td style={{padding:'5px 8px'}}>All</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>Advancing Counter-UAS Mission Command Systems</td><td style={{padding:'5px 8px'}}>May-Jun 2024</td><td style={{padding:'5px 8px'}}>TM-40E, TM-40F</td></tr>
            <tr><td style={{padding:'5px 8px'}}>The True Test of Mission Command</td><td style={{padding:'5px 8px'}}>Sep-Oct 2024</td><td style={{padding:'5px 8px'}}>TM-40F</td></tr>
          </tbody>
        </table>

        {/* Parameters */}
        <h3 style={{color:'var(--navy)',margin:'16px 0 8px',fontSize:13,letterSpacing:'.05em'}}>PARAMETERS — Army War College Quarterly (3)</h3>
        <table style={{width:'100%',borderCollapse:'collapse',fontSize:13,marginBottom:16}}>
          <thead><tr style={{background:'#e8eaf0',color:'#333',textAlign:'left'}}><th style={{padding:'6px 8px'}}>Title</th><th style={{padding:'6px 8px'}}>Date</th><th style={{padding:'6px 8px'}}>Tracks</th></tr></thead>
          <tbody>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>Responsibly Pursuing Generative AI for the War Fighter</td><td style={{padding:'5px 8px'}}>Winter 2025-26</td><td style={{padding:'5px 8px'}}>TM-40H, TM-40M, All</td></tr>
            <tr><td style={{padding:'5px 8px'}}>Integrating AI and ML into COP and COA Development</td><td style={{padding:'5px 8px'}}>2024-25</td><td style={{padding:'5px 8px'}}>TM-40G, TM-40H, TM-40F</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>Trusting AI: Integrating AI into the Army's Professional Ethic</td><td style={{padding:'5px 8px'}}>2024</td><td style={{padding:'5px 8px'}}>All</td></tr>
          </tbody>
        </table>

        {/* MIPB */}
        <h3 style={{color:'var(--navy)',margin:'16px 0 8px',fontSize:13,letterSpacing:'.05em'}}>MIPB — Military Intelligence Professional Bulletin (6)</h3>
        <table style={{width:'100%',borderCollapse:'collapse',fontSize:13,marginBottom:16}}>
          <thead><tr style={{background:'#e8eaf0',color:'#333',textAlign:'left'}}><th style={{padding:'6px 8px'}}>Title</th><th style={{padding:'6px 8px'}}>Date</th><th style={{padding:'6px 8px'}}>Tracks</th></tr></thead>
          <tbody>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>FRIDAY: Unlocking OSINT for a Data-Driven Army</td><td style={{padding:'5px 8px'}}>2025</td><td style={{padding:'5px 8px'}}>TM-40A, TM-40H, TM-40L</td></tr>
            <tr><td style={{padding:'5px 8px'}}>Intelligence Support to Information Advantage</td><td style={{padding:'5px 8px'}}>Jan-Jun 2026</td><td style={{padding:'5px 8px'}}>TM-40A, TM-40K</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>Using AI to Create Digital Enemy Commanders</td><td style={{padding:'5px 8px'}}>Jul-Dec 2025</td><td style={{padding:'5px 8px'}}>TM-40H, TM-40M, TM-40A</td></tr>
            <tr><td style={{padding:'5px 8px'}}>The Market Knows Best: Prediction Markets for National Security</td><td style={{padding:'5px 8px'}}>Jul-Dec 2025</td><td style={{padding:'5px 8px'}}>TM-40A, TM-40G</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>Army Transitioning to Support Deep Sensing in MDO</td><td style={{padding:'5px 8px'}}>Jul-Dec 2025</td><td style={{padding:'5px 8px'}}>TM-40A, TM-40B, TM-40C</td></tr>
            <tr><td style={{padding:'5px 8px'}}>Open-Source Intelligence Support to Targeting</td><td style={{padding:'5px 8px'}}>2024</td><td style={{padding:'5px 8px'}}>TM-40A, TM-40B</td></tr>
          </tbody>
        </table>

        {/* Field Artillery Bulletin */}
        <h3 style={{color:'var(--navy)',margin:'16px 0 8px',fontSize:13,letterSpacing:'.05em'}}>FIELD ARTILLERY BULLETIN — Line of Departure (6)</h3>
        <table style={{width:'100%',borderCollapse:'collapse',fontSize:13,marginBottom:16}}>
          <thead><tr style={{background:'#e8eaf0',color:'#333',textAlign:'left'}}><th style={{padding:'6px 8px'}}>Title</th><th style={{padding:'6px 8px'}}>Date</th><th style={{padding:'6px 8px'}}>Tracks</th></tr></thead>
          <tbody>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>The New Digital Kill Chain</td><td style={{padding:'5px 8px'}}>2025</td><td style={{padding:'5px 8px'}}>TM-40B, TM-40L</td></tr>
            <tr><td style={{padding:'5px 8px'}}>AI's New Frontier in War Planning</td><td style={{padding:'5px 8px'}}>2025</td><td style={{padding:'5px 8px'}}>TM-40B, TM-40H</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>Project Convergence: Revolutionizing Targeting in LSCO</td><td style={{padding:'5px 8px'}}>2025</td><td style={{padding:'5px 8px'}}>TM-40B, TM-40A, TM-40G</td></tr>
            <tr><td style={{padding:'5px 8px'}}>Enhancing Tactical Level Targeting With AI</td><td style={{padding:'5px 8px'}}>2024</td><td style={{padding:'5px 8px'}}>TM-40B, TM-40H, TM-40M</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>The Future of Strategic Fires Target Acquisition</td><td style={{padding:'5px 8px'}}>2024</td><td style={{padding:'5px 8px'}}>TM-40B, TM-40A</td></tr>
            <tr><td style={{padding:'5px 8px'}}>The Combat Aviation Brigade and Digital Call for Fire</td><td style={{padding:'5px 8px'}}>2024</td><td style={{padding:'5px 8px'}}>TM-40B, TM-40C</td></tr>
          </tbody>
        </table>

        {/* NCO Journal */}
        <h3 style={{color:'var(--navy)',margin:'16px 0 8px',fontSize:13,letterSpacing:'.05em'}}>NCO JOURNAL — Army University Press (3)</h3>
        <table style={{width:'100%',borderCollapse:'collapse',fontSize:13,marginBottom:16}}>
          <thead><tr style={{background:'#e8eaf0',color:'#333',textAlign:'left'}}><th style={{padding:'6px 8px'}}>Title</th><th style={{padding:'6px 8px'}}>Date</th><th style={{padding:'6px 8px'}}>Tracks</th></tr></thead>
          <tbody>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>Knowledge Management and The Old Guard</td><td style={{padding:'5px 8px'}}>Aug 2025</td><td style={{padding:'5px 8px'}}>TM-40K, TM-40F</td></tr>
            <tr><td style={{padding:'5px 8px'}}>From Data to Wisdom</td><td style={{padding:'5px 8px'}}>Feb 2025</td><td style={{padding:'5px 8px'}}>All</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>Artificial Intelligence and Future Warfare</td><td style={{padding:'5px 8px'}}>Sep 2025</td><td style={{padding:'5px 8px'}}>TM-40H, TM-40M, All</td></tr>
          </tbody>
        </table>

        {/* Army Sustainment */}
        <h3 style={{color:'var(--navy)',margin:'16px 0 8px',fontSize:13,letterSpacing:'.05em'}}>ARMY SUSTAINMENT — Army Logistics University (4)</h3>
        <table style={{width:'100%',borderCollapse:'collapse',fontSize:13,marginBottom:16}}>
          <thead><tr style={{background:'#e8eaf0',color:'#333',textAlign:'left'}}><th style={{padding:'6px 8px'}}>Title</th><th style={{padding:'6px 8px'}}>Date</th><th style={{padding:'6px 8px'}}>Tracks</th></tr></thead>
          <tbody>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>Army Sustainment Enterprise's Delayed Approach to Data Modernization</td><td style={{padding:'5px 8px'}}>Winter 2025</td><td style={{padding:'5px 8px'}}>TM-40D, TM-40K</td></tr>
            <tr><td style={{padding:'5px 8px'}}>Predictive Logistics: Reimagining Sustainment on the 2040 Battlefield</td><td style={{padding:'5px 8px'}}>Winter 2025</td><td style={{padding:'5px 8px'}}>TM-40D, TM-40H, TM-40M, TM-40G</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>Enabling Logistics in Contested Environments</td><td style={{padding:'5px 8px'}}>Spring 2025</td><td style={{padding:'5px 8px'}}>TM-40D, TM-40G</td></tr>
            <tr><td style={{padding:'5px 8px'}}>Advancing to Data-Driven Logistics Operations</td><td style={{padding:'5px 8px'}}>2024</td><td style={{padding:'5px 8px'}}>TM-40D, TM-40K</td></tr>
          </tbody>
        </table>

        {/* Army AL&T Magazine */}
        <h3 style={{color:'var(--navy)',margin:'16px 0 8px',fontSize:13,letterSpacing:'.05em'}}>ARMY AL&amp;T MAGAZINE (7)</h3>
        <table style={{width:'100%',borderCollapse:'collapse',fontSize:13,marginBottom:16}}>
          <thead><tr style={{background:'#e8eaf0',color:'#333',textAlign:'left'}}><th style={{padding:'6px 8px'}}>Title</th><th style={{padding:'6px 8px'}}>Date</th><th style={{padding:'6px 8px'}}>Tracks</th></tr></thead>
          <tbody>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>Accelerating the Army's AI Strategy</td><td style={{padding:'5px 8px'}}>2024-25</td><td style={{padding:'5px 8px'}}>TM-40H, TM-40J, All</td></tr>
            <tr><td style={{padding:'5px 8px'}}>Commoditizing AI/ML Models</td><td style={{padding:'5px 8px'}}>2024-25</td><td style={{padding:'5px 8px'}}>TM-40H, TM-40M, TM-40L</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>The Army's Data (Ad)Vantage</td><td style={{padding:'5px 8px'}}>2024</td><td style={{padding:'5px 8px'}}>All</td></tr>
            <tr><td style={{padding:'5px 8px'}}>The Software Advantage</td><td style={{padding:'5px 8px'}}>2024-25</td><td style={{padding:'5px 8px'}}>TM-40L, TM-40J</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>Army Intelligence</td><td style={{padding:'5px 8px'}}>2025</td><td style={{padding:'5px 8px'}}>TM-40A, TM-40H</td></tr>
            <tr><td style={{padding:'5px 8px'}}>Emerging Technology and Modernizing the Army</td><td style={{padding:'5px 8px'}}>2024-25</td><td style={{padding:'5px 8px'}}>All</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>Reality Check (AI/ML implementation)</td><td style={{padding:'5px 8px'}}>2024-25</td><td style={{padding:'5px 8px'}}>TM-40H, TM-40M, TM-40J</td></tr>
          </tbody>
        </table>

        {/* Army Communicator */}
        <h3 style={{color:'var(--navy)',margin:'16px 0 8px',fontSize:13,letterSpacing:'.05em'}}>ARMY COMMUNICATOR — Cyber CoE (3)</h3>
        <table style={{width:'100%',borderCollapse:'collapse',fontSize:13,marginBottom:16}}>
          <thead><tr style={{background:'#e8eaf0',color:'#333',textAlign:'left'}}><th style={{padding:'6px 8px'}}>Title</th><th style={{padding:'6px 8px'}}>Date</th><th style={{padding:'6px 8px'}}>Tracks</th></tr></thead>
          <tbody>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>Leading in Data Centricity, C2 Fix Best Practices</td><td style={{padding:'5px 8px'}}>Spring 2025</td><td style={{padding:'5px 8px'}}>TM-40E, TM-40F, TM-40L</td></tr>
            <tr><td style={{padding:'5px 8px'}}>Army Communicator Spring 2024</td><td style={{padding:'5px 8px'}}>Spring 2024</td><td style={{padding:'5px 8px'}}>TM-40E, TM-40L</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>Army Communicator January 2024 — ITN Suite</td><td style={{padding:'5px 8px'}}>Jan 2024</td><td style={{padding:'5px 8px'}}>TM-40E, TM-40C</td></tr>
          </tbody>
        </table>

        {/* From the Green Notebook */}
        <h3 style={{color:'var(--navy)',margin:'16px 0 8px',fontSize:13,letterSpacing:'.05em'}}>FROM THE GREEN NOTEBOOK (3)</h3>
        <table style={{width:'100%',borderCollapse:'collapse',fontSize:13,marginBottom:16}}>
          <thead><tr style={{background:'#e8eaf0',color:'#333',textAlign:'left'}}><th style={{padding:'6px 8px'}}>Title</th><th style={{padding:'6px 8px'}}>Date</th><th style={{padding:'6px 8px'}}>Tracks</th></tr></thead>
          <tbody>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>How To Be a Data Literate Leader — And Why It Matters</td><td style={{padding:'5px 8px'}}>Mar 2024</td><td style={{padding:'5px 8px'}}>All, TM-40K</td></tr>
            <tr><td style={{padding:'5px 8px'}}>Harnessing the Power of Knowledge Management</td><td style={{padding:'5px 8px'}}>Apr 2024</td><td style={{padding:'5px 8px'}}>TM-40K, TM-40F</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>Understanding Weapons of Math Destruction</td><td style={{padding:'5px 8px'}}>Jul 2024</td><td style={{padding:'5px 8px'}}>TM-40G, TM-40H, TM-40M</td></tr>
          </tbody>
        </table>

        {/* Infantry Magazine */}
        <h3 style={{color:'var(--navy)',margin:'16px 0 8px',fontSize:13,letterSpacing:'.05em'}}>INFANTRY MAGAZINE — Maneuver CoE (1)</h3>
        <table style={{width:'100%',borderCollapse:'collapse',fontSize:13,marginBottom:16}}>
          <thead><tr style={{background:'#e8eaf0',color:'#333',textAlign:'left'}}><th style={{padding:'6px 8px'}}>Title</th><th style={{padding:'6px 8px'}}>Date</th><th style={{padding:'6px 8px'}}>Tracks</th></tr></thead>
          <tbody>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>Moneyball for Gunnery — 1/4 ID BCT data analytics</td><td style={{padding:'5px 8px'}}>2024</td><td style={{padding:'5px 8px'}}>TM-40C, TM-40G</td></tr>
          </tbody>
        </table>

        {/* Small Wars Journal */}
        <h3 style={{color:'var(--navy)',margin:'16px 0 8px',fontSize:13,letterSpacing:'.05em'}}>SMALL WARS JOURNAL (4)</h3>
        <table style={{width:'100%',borderCollapse:'collapse',fontSize:13,marginBottom:16}}>
          <thead><tr style={{background:'#e8eaf0',color:'#333',textAlign:'left'}}><th style={{padding:'6px 8px'}}>Title</th><th style={{padding:'6px 8px'}}>Date</th><th style={{padding:'6px 8px'}}>Tracks</th></tr></thead>
          <tbody>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>Data as Firepower: Data Superiority as a Warfighting Concept</td><td style={{padding:'5px 8px'}}>Aug 2025</td><td style={{padding:'5px 8px'}}>All</td></tr>
            <tr><td style={{padding:'5px 8px'}}>Elevating Information: Why the Army Should Establish Information as a Core WfF</td><td style={{padding:'5px 8px'}}>Apr 2025</td><td style={{padding:'5px 8px'}}>TM-40A, TM-40F, TM-40K</td></tr>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>Accelerating Decision-Making: Integrating AI into the Modern Wargame</td><td style={{padding:'5px 8px'}}>Feb 2026</td><td style={{padding:'5px 8px'}}>TM-40G, TM-40H, TM-40F</td></tr>
            <tr><td style={{padding:'5px 8px'}}>AI-Enabled Wargaming at CGSC</td><td style={{padding:'5px 8px'}}>Jan 2026</td><td style={{padding:'5px 8px'}}>TM-40G, TM-40H, TM-40F</td></tr>
          </tbody>
        </table>

        {/* War on the Rocks */}
        <h3 style={{color:'var(--navy)',margin:'16px 0 8px',fontSize:13,letterSpacing:'.05em'}}>WAR ON THE ROCKS (1)</h3>
        <table style={{width:'100%',borderCollapse:'collapse',fontSize:13,marginBottom:16}}>
          <thead><tr style={{background:'#e8eaf0',color:'#333',textAlign:'left'}}><th style={{padding:'6px 8px'}}>Title</th><th style={{padding:'6px 8px'}}>Date</th><th style={{padding:'6px 8px'}}>Tracks</th></tr></thead>
          <tbody>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>The U.S. Army, AI, and Mission Command</td><td style={{padding:'5px 8px'}}>Mar 2025</td><td style={{padding:'5px 8px'}}>TM-40F, TM-40H</td></tr>
          </tbody>
        </table>

        {/* Modern War Institute */}
        <h3 style={{color:'var(--navy)',margin:'16px 0 8px',fontSize:13,letterSpacing:'.05em'}}>MODERN WAR INSTITUTE — West Point (1)</h3>
        <table style={{width:'100%',borderCollapse:'collapse',fontSize:13,marginBottom:16}}>
          <thead><tr style={{background:'#e8eaf0',color:'#333',textAlign:'left'}}><th style={{padding:'6px 8px'}}>Title</th><th style={{padding:'6px 8px'}}>Date</th><th style={{padding:'6px 8px'}}>Tracks</th></tr></thead>
          <tbody>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>Leadership, Lethality, and Data Literacy</td><td style={{padding:'5px 8px'}}>2024</td><td style={{padding:'5px 8px'}}>All</td></tr>
          </tbody>
        </table>

        {/* CALL */}
        <h3 style={{color:'var(--navy)',margin:'16px 0 8px',fontSize:13,letterSpacing:'.05em'}}>CALL — Center for Army Lessons Learned (1)</h3>
        <table style={{width:'100%',borderCollapse:'collapse',fontSize:13,marginBottom:16}}>
          <thead><tr style={{background:'#e8eaf0',color:'#333',textAlign:'left'}}><th style={{padding:'6px 8px'}}>Title</th><th style={{padding:'6px 8px'}}>Date</th><th style={{padding:'6px 8px'}}>Tracks</th></tr></thead>
          <tbody>
            <tr style={{background:'#f8f9fa'}}><td style={{padding:'5px 8px'}}>FY24 MCTP Key Observations</td><td style={{padding:'5px 8px'}}>Feb 2025</td><td style={{padding:'5px 8px'}}>All</td></tr>
          </tbody>
        </table>
      </details>

      <div className="callout note mt-24">
        <div className="callout-label">NOT FINDING WHAT YOU NEED?</div>
        <div className="callout-body">
          Contact your unit data steward for additional publications, source files, or access to restricted materials.
          For technical support, visit the <button className="qr-link" onClick={() => showPanel('support')}>Support page &rarr;</button>
          For task-level procedures, use the <button className="qr-link" onClick={() => showPanel('taskindex')}>Task Index &rarr;</button>
        </div>
      </div>

      </div>{/* /contentRef */}
    </>
  )
}
