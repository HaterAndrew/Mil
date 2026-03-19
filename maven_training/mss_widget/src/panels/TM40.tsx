import { useState } from 'react'
import { URLS } from '../constants/urls'

interface Props {
  showPanel: (id: string) => void
}

export default function TM40({ showPanel }: Props) {
  const [wffOpen, setWffOpen] = useState(true)

  return (
    <>
      <div className="section-header">
        <span className="section-badge">TM-40</span>
        <span className="section-title">Technical Specialist Tracks &mdash; Developer Manuals</span>
        <span className="section-subtitle">Prerequisite: TM-30 &bull; Eight tracks by role &bull; Advanced versions at TM-50</span>
      </div>

      <div className="callout bluf">
        <div className="callout-label">BLUF</div>
        <div className="callout-body">The TM-40 Technical Specialist tracks (TM-40G&ndash;O) cover developer-level capabilities requiring coding, advanced tooling, or specialized technical expertise &mdash; prerequisite: TM-30 complete. For Warfighting Function tracks (TM-40A&ndash;F), use the HOME tab track selector or navigate to the Specialist Tracks tab.</div>
      </div>

      <div className="track-grid">

        <div className="track-card">
          <div className="track-card-hdr">
            <span className="track-tm">TM-40G &mdash; ORSA Track</span>
            <span className="track-chip">TM-30 Required</span>
          </div>
          <div className="track-body">
            <div className="track-name">Operations Research &amp; Systems Analysis</div>
            <div className="track-audience">FA49 &bull; G2/S2 quantitative analysts &bull; Wargame analysts</div>
            <ul className="track-topics">
              <li>Configure Code Workspaces (Python/R) within Foundry</li>
              <li>Statistical modeling: regression, classification, validation for readiness/logistics</li>
              <li>Time series forecasting with ARIMA/SARIMA patterns</li>
              <li>Monte Carlo simulation for COA comparison and risk quantification</li>
              <li>Linear programming for resource allocation and scheduling optimization</li>
              <li>Wargame/exercise data collection architecture and aggregation pipelines</li>
              <li>Analytical decision support products (Quiver/Contour) to commander standard</li>
              <li>Communicate uncertainty: confidence intervals, sensitivity analysis, briefing standards</li>
            </ul>
            <div className="track-prereq">Prereq: TM-30 &bull; Advanced: TM-50G</div>
          </div>
        </div>

        <div className="track-card">
          <div className="track-card-hdr">
            <span className="track-tm">TM-40H &mdash; AI Engineer Track</span>
            <span className="track-chip">TM-30 Required</span>
          </div>
          <div className="track-body">
            <div className="track-name">AIP Logic, Agent Studio &amp; LLM Integration</div>
            <div className="track-audience">AI/ML specialists &bull; 17A/17C</div>
            <ul className="track-topics">
              <li>Author AIP Logic workflows: prompt engineering, chain design, output handling</li>
              <li>Build and configure AIP Agent Studio agents with tools, memory, and orchestration</li>
              <li>Implement LLM integration patterns: ontology data grounding, RAG, context construction</li>
              <li>Apply AI safety requirements: human-in-the-loop gates, output validation, OPSEC</li>
              <li>Write Python transforms that prepare data for AI consumption</li>
              <li>Connect AIP Logic workflows to Object Types and Actions</li>
              <li>Test and red-team AI outputs; evaluate quality against defined standards</li>
              <li>Deploy and monitor AIP Logic workflows in production</li>
            </ul>
            <div className="track-prereq">Prereq: TM-30 &bull; Advanced: TM-50H</div>
          </div>
        </div>

        <div className="track-card">
          <div className="track-card-hdr">
            <span className="track-tm">TM-40M &mdash; ML Engineer Track</span>
            <span className="track-chip">TM-30 Required</span>
          </div>
          <div className="track-body">
            <div className="track-name">Code Workspaces, Model Training &amp; Deployment</div>
            <div className="track-audience">ML engineers &bull; Data scientists building/deploying models on MSS</div>
            <ul className="track-topics">
              <li>Configure Code Workspaces for model development (GPU, packages, environment management)</li>
              <li>Build and evaluate ML models within the Foundry environment</li>
              <li>Manage model versioning, experiment tracking, and reproducibility</li>
              <li>Deploy models to production and integrate with Ontology Objects and Actions</li>
              <li>Implement MLOps patterns: monitoring, drift detection, retraining triggers</li>
              <li>Apply responsible AI practices and model documentation standards for operational use</li>
            </ul>
            <div className="track-prereq">Prereq: TM-30 &bull; Advanced: TM-50M</div>
          </div>
        </div>

        <div className="track-card">
          <div className="track-card-hdr">
            <span className="track-tm">TM-40J &mdash; Program Manager Track</span>
            <span className="track-chip">TM-30 Required</span>
          </div>
          <div className="track-body">
            <div className="track-name">Agile Project Management for Data &amp; AI Capabilities</div>
            <div className="track-audience">PMs &bull; Product owners &bull; G8/S8 &bull; Technical team leads</div>
            <ul className="track-topics">
              <li>Stand up Agile project structures (backlog, sprint cadence, ceremonies) for data and AI builds</li>
              <li>Write user stories and acceptance criteria that TM-40G&ndash;O developers can execute without ambiguity</li>
              <li>Manage the ML/AI project lifecycle: six phases from Problem Definition through Sustainment</li>
              <li>Translate commander requirements into prioritized, sprint-ready backlogs</li>
              <li>Specify project tracking systems (sprint boards, status dashboards) for TM-40L implementation</li>
              <li>Build and maintain risk registers; manage dependency blockers across specialist tracks</li>
              <li>Conduct production readiness reviews against the Definition of Done before release</li>
              <li>Execute change management plans for new MSS capability rollout to operational units</li>
            </ul>
            <div className="track-prereq">Prereq: TM-30 &bull; Advanced: TM-50J</div>
          </div>
        </div>

        <div className="track-card">
          <div className="track-card-hdr">
            <span className="track-tm">TM-40K &mdash; Knowledge Manager Track</span>
            <span className="track-chip">TM-30 Required</span>
          </div>
          <div className="track-body">
            <div className="track-name">Knowledge Repositories, AIP Summarization &amp; Lessons Learned</div>
            <div className="track-audience">KMOs &bull; 37F &bull; S2/S3 KM roles &bull; AAR facilitators</div>
            <ul className="track-topics">
              <li>Design knowledge architecture for AAR, lessons learned, doctrine, and SOP repositories</li>
              <li>Build AAR capture systems using Workshop forms and Object Type pipelines</li>
              <li>Design and operate lessons-learned ingestion and tagging pipelines</li>
              <li>Use AIP Logic for knowledge summarization, search augmentation, and theme extraction</li>
              <li>Build full-text and semantic search systems over knowledge repositories</li>
              <li>Manage doctrine and SOP version control within Foundry</li>
              <li>Build personnel expertise mapping (skills/experience registries)</li>
              <li>Design knowledge transfer and unit continuity processes using MSS</li>
            </ul>
            <div className="track-prereq">Prereq: TM-30 &bull; Advanced: TM-50K</div>
          </div>
        </div>

        <div className="track-card">
          <div className="track-card-hdr">
            <span className="track-tm">TM-40L &mdash; Software Engineer Track</span>
            <span className="track-chip">TM-30 Required</span>
          </div>
          <div className="track-body">
            <div className="track-name">OSDK, Full-Stack Foundry Applications &amp; Platform SDK</div>
            <div className="track-audience">SWEs &bull; 17A/17C &bull; 25D</div>
            <ul className="track-topics">
              <li>Authenticate and query the Foundry Ontology via OSDK (TypeScript/Python)</li>
              <li>Execute Actions, subscribe to Object changes, handle pagination and filtering via OSDK</li>
              <li>Use Foundry Platform SDK for dataset operations, file management, and branch management</li>
              <li>Build TypeScript Functions on Objects (computed properties, bulk query patterns)</li>
              <li>Write and test complex Action validators with TypeScript</li>
              <li>Build Slate applications integrated with the Foundry API</li>
              <li>Apply USAREUR-AF code review and deployment standards for MSS applications</li>
            </ul>
            <div className="track-prereq">Prereq: TM-30 &bull; Advanced: TM-50L</div>
          </div>
        </div>

        <div className="track-card">
          <div className="track-card-hdr">
            <span className="track-tm">TM-40N &mdash; UI/UX Designer Track</span>
            <span className="track-chip">TM-30 Required</span>
          </div>
          <div className="track-body">
            <div className="track-name">Soldier Centered Design, Workshop &amp; Slate UI</div>
            <div className="track-audience">UI/UX designers &bull; Human factors &bull; GS/contractor designers</div>
            <ul className="track-topics">
              <li>Conduct user research in operational and classified environments (interview, contextual inquiry, usability testing)</li>
              <li>Design information architectures for data-dense operational displays</li>
              <li>Build interactive prototypes from low-fidelity sketches through high-fidelity mockups</li>
              <li>Design Workshop layouts: widget selection, dashboard hierarchy, responsive patterns</li>
              <li>Apply visual design standards for tactical displays: classification marking, contrast, field conditions</li>
              <li>Ensure Section 508 / WCAG 2.1 AA accessibility compliance</li>
            </ul>
            <div className="track-prereq">Prereq: TM-30 &bull; Advanced: TM-50N</div>
          </div>
        </div>

        <div className="track-card">
          <div className="track-card-hdr">
            <span className="track-tm">TM-40O &mdash; Platform Engineer Track</span>
            <span className="track-chip">TM-30 Required</span>
          </div>
          <div className="track-body">
            <div className="track-name">Kubernetes, CI/CD, DevSecOps &amp; Infrastructure as Code</div>
            <div className="track-audience">Platform engineers &bull; DevOps &bull; SysAdmins &bull; 25D</div>
            <ul className="track-topics">
              <li>Architect and operate Kubernetes clusters for MSS workloads</li>
              <li>Implement Infrastructure as Code with GitOps workflows and continuous reconciliation</li>
              <li>Design CI/CD pipelines: automated build, test, scan, and deploy for MSS applications</li>
              <li>Harden containers using DoD Iron Bank images, vulnerability scanning, and SHA256 digest pinning</li>
              <li>Deploy across classification boundaries and DDIL environments (air-gapped, edge clusters)</li>
              <li>Manage RMF/ATO lifecycle from the infrastructure perspective, STIG compliance</li>
            </ul>
            <div className="track-prereq">Prereq: TM-30 &bull; Advanced: TM-50O</div>
          </div>
        </div>

      </div>

      <details style={{marginTop:20}} open={wffOpen} onToggle={e => setWffOpen((e.target as HTMLDetailsElement).open)}>
        <summary style={{cursor:'pointer',fontSize:11,color:'var(--text-muted,#888)',letterSpacing:'.06em',textTransform:'uppercase',userSelect:'none',listStyle:'none',display:'flex',alignItems:'center',gap:6}}>
          <span style={{fontSize:14}}>&#9662;</span> Warfighting Function Tracks (TM-40A&ndash;F)
        </summary>
        <table className="data-table" style={{marginTop:10,fontSize:12,width:'auto'}}>
          <thead><tr><th>Designation</th><th>Track</th><th>Publication</th></tr></thead>
          <tbody>
            <tr><td>TM-40A</td><td>Intelligence</td><td><a href={URLS.TM40A} target="_blank" rel="noreferrer">TM_40A_INTELLIGENCE.pdf</a></td></tr>
            <tr><td>TM-40B</td><td>Fires</td><td><a href={URLS.TM40B} target="_blank" rel="noreferrer">TM_40B_FIRES.pdf</a></td></tr>
            <tr><td>TM-40C</td><td>Movement &amp; Maneuver</td><td><a href={URLS.TM40C} target="_blank" rel="noreferrer">TM_40C_MOVEMENT_MANEUVER.pdf</a></td></tr>
            <tr><td>TM-40D</td><td>Sustainment</td><td><a href={URLS.TM40D} target="_blank" rel="noreferrer">TM_40D_SUSTAINMENT.pdf</a></td></tr>
            <tr><td>TM-40E</td><td>Protection</td><td><a href={URLS.TM40E} target="_blank" rel="noreferrer">TM_40E_PROTECTION.pdf</a></td></tr>
            <tr><td>TM-40F</td><td>Mission Command</td><td><a href={URLS.TM40F} target="_blank" rel="noreferrer">TM_40F_MISSION_COMMAND.pdf</a></td></tr>
          </tbody>
        </table>
      </details>

      <div className="specialist-cta" style={{marginTop:32}}>
        <div className="specialist-cta-text">
          <div className="specialist-cta-label">Next Level &mdash; After TM-40</div>
          <div className="specialist-cta-title">TM-50 &mdash; Advanced Developer Tracks</div>
          <div className="specialist-cta-sub">Expert-level continuation of each TM-40 specialist track. For senior technical leads, platform architects, and developers building enterprise-scale MSS capabilities.</div>
        </div>
        <button className="specialist-cta-btn" onClick={() => showPanel('tm50' as any)}>
          Continue to TM-50 <span className="btn-arrow">&#8594;</span>
        </button>
      </div>

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
