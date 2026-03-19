
import { URLS } from '../constants/urls'

interface Props {
  showPanel: (id: string) => void
}

export default function BSP({ showPanel }: Props) {
  return (
    <>
      <div className="section-header">
        <span className="section-badge" style={{background:'rgba(200,151,26,0.18)',color:'var(--gold)'}}>BSP</span>
        <span className="section-title">Builder Sprint &mdash; Applied Build Event</span>
        <span className="section-subtitle">Prerequisite: TM-20 + command-validated project &bull; Quarterly &bull; Outside TM chain &bull; No TM credit granted</span>
      </div>

      <div className="callout bluf">
        <div className="callout-label">BLUF</div>
        <div className="callout-body">The Builder Sprint is a quarterly 5-day supervised build event. You bring a validated operational problem; you build a solution; SMEs are available for consultation. Minimal instruction &mdash; this is not a course. You leave with a functional product and a handoff package. BSP does not replace TM-30 and does not grant credit toward TM-40 enrollment.</div>
      </div>

      <div className="callout info">
        <div className="callout-label">PUBLICATION</div>
        <div className="callout-body"><strong>BSP &mdash; Builder Sprint Participant Guide</strong> &mdash; Full reference document. &nbsp;<a href={URLS.BSP_GUIDE} target="_blank" rel="noopener noreferrer" style={{color:'var(--navy)',fontWeight:700,fontSize:'14px'}}>Open PDF &rarr;</a></div>
      </div>

      <div className="callout warning">
        <div className="callout-label">NOTE</div>
        <div className="callout-body">BSP is <strong>outside the TM-10 through TM-50 training chain.</strong> Completion does not count as TM-30 or any other TM credit. If you need structured platform instruction, enroll in TM-30. BSP is for builders with TM-20 skills and a real problem to solve.</div>
      </div>

      <h2>WHO ATTENDS</h2>
      <div className="card-grid">
        <div className="card">
          <div className="card-label">REQUIRED</div>
          <div className="card-body">
            <ul>
              <li><strong>TM-20 Go on file</strong> &mdash; hard requirement, no exceptions</li>
              <li><strong>Command-approved Project Brief</strong> &mdash; submitted to C2DAO &ge;14 days before Day 1</li>
              <li>Supervisor signature on enrollment request</li>
            </ul>
          </div>
        </div>
        <div className="card">
          <div className="card-label">PROJECT REQUIREMENTS</div>
          <div className="card-body">
            <ul>
              <li>Specific output: named dashboard, pipeline, Ontology type, or Quiver/Contour product</li>
              <li>Named consumer &mdash; a real person or role who will use the product</li>
              <li>All data sources accessible <em>before</em> Day 1</li>
              <li>No code required &mdash; Python / TypeScript / OSDK = TM-40 track, not BSP</li>
              <li>5-day feasibility: functional prototype reachable within sprint</li>
            </ul>
          </div>
        </div>
      </div>

      <h2>SPRINT WEEK STRUCTURE</h2>
      <div className="table-wrap">
        <table>
          <thead><tr><th>Day</th><th>Activity</th></tr></thead>
          <tbody>
            <tr><td>Day 1</td><td>In-brief: scope review, environment check, kickoff (0800&ndash;0900). Build (0900&ndash;1700).</td></tr>
            <tr><td>Days 2&ndash;4</td><td>Daily standup (0800, 15 min). Build (0815&ndash;1700). SME available throughout.</td></tr>
            <tr><td>Day 5</td><td>Product demo / peer review (0800&ndash;1000). Go/No-Go determination (1000&ndash;1200). Out-brief and handoff (1300&ndash;1500).</td></tr>
          </tbody>
        </table>
      </div>

      <h2>GO STANDARD</h2>
      <div className="table-wrap">
        <table>
          <thead><tr><th>Standard</th><th>Criterion</th></tr></thead>
          <tbody>
            <tr><td>Functional product</td><td>The product does what your Project Brief says it will do &mdash; your named consumer can use it</td></tr>
            <tr><td>Documentation</td><td>Naming conventions followed; product description explains purpose and data sources</td></tr>
            <tr><td>Handoff package</td><td>Complete by end of Day 5 &mdash; product description, data sources, limitations, maintenance guidance, promotion status, POC</td></tr>
            <tr><td>Governance</td><td>Product in a branch; promotion plan documented or production promotion initiated</td></tr>
          </tbody>
        </table>
      </div>

      <h2>ENROLLMENT</h2>
      <div className="card-grid">
        <div className="card">
          <div className="card-label">TIMELINE</div>
          <div className="card-body">
            <ul>
              <li><strong>T-21 days:</strong> Enrollment request submitted</li>
              <li><strong>T-14 days:</strong> Project Brief approved by C2DAO</li>
              <li><strong>T-10 days:</strong> Sprint workspace provisioned</li>
              <li><strong>T-5 days:</strong> Candidate confirms access</li>
              <li><strong>Day 1:</strong> Sprint begins</li>
            </ul>
          </div>
        </div>
        <div className="card">
          <div className="card-label">CADENCE</div>
          <div className="card-body">
            <ul>
              <li>4 sprint events per fiscal year (quarterly)</li>
              <li>4&ndash;16 participants per sprint</li>
              <li>1 SME per &le;8 participants</li>
              <li>Annual schedule published each October</li>
            </ul>
          </div>
        </div>
      </div>

      <div className="callout info">
        <div className="callout-label">DOCUMENTS</div>
        <div className="callout-body">
          Participant Guide: <a href={URLS.BSP_GUIDE} target="_blank" rel="noopener noreferrer" style={{color:'var(--navy)',fontWeight:700}}>BSP_GUIDE.pdf</a> &nbsp;&bull;&nbsp;
          Coordinator Package: <a href={URLS.BSP_SPRINT_PACKAGE} target="_blank" rel="noopener noreferrer" style={{color:'var(--navy)',fontWeight:700}}>BSP_SPRINT_PACKAGE.pdf</a> &nbsp;&bull;&nbsp;
          SOP: <a href={URLS.BUILDER_SPRINT_SOP} target="_blank" rel="noopener noreferrer" style={{color:'var(--navy)',fontWeight:700}}>BUILDER_SPRINT_SOP.pdf</a> &nbsp;&bull;&nbsp;
          Environment Setup: <a href={URLS.BSP_ENVIRONMENT_SETUP} target="_blank" rel="noopener noreferrer" style={{color:'var(--navy)',fontWeight:700}}>BSP_ENVIRONMENT_SETUP.pdf</a> &nbsp;&bull;&nbsp;
          Project Brief form: <strong>CAD Appendix D</strong>
        </div>
      </div>

      <div className="callout note mt-24">
        <div className="callout-label">NOT FINDING WHAT YOU NEED?</div>
        <div className="callout-body">
          Contact your unit data steward for additional publications, source files, or access to restricted materials.
          For technical support, visit the <button className="qr-link" onClick={() => showPanel('support')}>Support page &rarr;</button>
        </div>
      </div>
    </>
  )
}
