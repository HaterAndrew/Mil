
import { URLS } from '../constants/urls'

interface Props {
  showPanel: (id: string) => void
}

export default function EXEC({ showPanel }: Props) {
  return (
    <>
      <div className="section-header">
        <span className="section-badge" style={{background:'rgba(200,151,26,0.18)',color:'var(--gold)'}}>EXEC</span>
        <span className="section-title">Senior Leader Executive Course</span>
        <span className="section-subtitle">Audience: O-5+ / E-9+ &bull; 1 day &bull; No prerequisites &bull; Terminal &mdash; outside the SL pipeline</span>
      </div>

      <div className="callout bluf">
        <div className="callout-label">BLUF</div>
        <div className="callout-body">TM-EXEC gives battalion commanders, command sergeants major, and equivalent senior leaders the operational understanding of MSS required to lead formations that depend on data-driven decision-making. You will not build anything. You will learn what the platform produces, how data products affect your formation, and how to direct your staff&rsquo;s use of data as a command function. TM-EXEC replaces SL 1 for O-5 / E-9+ personnel. It is terminal &mdash; no progression to SL 2 or beyond.</div>
      </div>

      <div className="callout info">
        <div className="callout-label">PUBLICATION</div>
        <div className="callout-body"><strong>TM-EXEC &mdash; Senior Leader Executive Course</strong> &mdash; Full reference document. &nbsp;<a href={URLS.TM_EXEC} target="_blank" rel="noopener noreferrer" style={{color:'var(--navy)',fontWeight:700,fontSize:'14px'}}>Open PDF &rarr;</a></div>
      </div>

      <div className="callout warning">
        <div className="callout-label">NOTE</div>
        <div className="callout-body">TM-EXEC is <strong>outside the SL 1 through SL 5 training chain.</strong> It does NOT grant SL 1 credit. If a senior leader wants hands-on platform qualification, they should enroll in SL 1 and proceed through the standard pipeline.</div>
      </div>

      <h2>WHAT THIS COURSE COVERS</h2>
      <div className="card-grid">
        <div className="card gold-top">
          <div className="card-label">YOU WILL LEARN</div>
          <div className="card-body">
            <ul>
              <li>What MSS does for your formation and why it matters</li>
              <li>How to evaluate data products &mdash; operationally, not technically</li>
              <li>How to guide your formation&rsquo;s data posture through resourcing, prioritization, and governance</li>
              <li>What questions to ask about data freshness, source integrity, and product quality</li>
              <li>The training pipeline that qualifies your data workforce (SL 1 through SL 5)</li>
            </ul>
          </div>
        </div>
        <div className="card">
          <div className="card-label">THIS COURSE IS NOT</div>
          <div className="card-body">
            <ul>
              <li>A platform navigation course &mdash; you will see MSS, not operate it</li>
              <li>A data literacy primer &mdash; you already understand why data matters</li>
              <li>A substitute for SL 1 in the standard pipeline</li>
              <li>A qualification to build, modify, or administer anything on the platform</li>
            </ul>
          </div>
        </div>
      </div>

      <h2>DAILY SCHEDULE</h2>
      <div className="table-wrap">
        <table>
          <thead><tr><th>Time</th><th>Block</th><th>Content</th></tr></thead>
          <tbody>
            <tr><td>0800&ndash;0830</td><td>1</td><td>Course introduction; senior leader role in the data environment</td></tr>
            <tr><td>0830&ndash;0930</td><td>2</td><td>Why MSS exists &mdash; strategic context, CG guidance (Ch 1)</td></tr>
            <tr><td>0930&ndash;1030</td><td>3</td><td>The platform and what it produces &mdash; five-layer architecture, data product types, live walkthrough (Ch 2)</td></tr>
            <tr><td>1030&ndash;1045</td><td>&mdash;</td><td>Break</td></tr>
            <tr><td>1045&ndash;1200</td><td>4</td><td>How data products impact your formation &mdash; data as command function, failure patterns, Commander&rsquo;s Data PIRs (Ch 3)</td></tr>
            <tr><td>1200&ndash;1300</td><td>&mdash;</td><td>Lunch</td></tr>
            <tr><td>1300&ndash;1345</td><td>5</td><td>The training pipeline &mdash; SL 1 through SL 5, FBC, resourcing decisions (Ch 4)</td></tr>
            <tr><td>1345&ndash;1430</td><td>6</td><td>Governance &mdash; the governance chain, VAUTI framework, red flags (Ch 5)</td></tr>
            <tr><td>1430&ndash;1445</td><td>&mdash;</td><td>Break</td></tr>
            <tr><td>1445&ndash;1530</td><td>7</td><td>How data projects work &mdash; agile overview, roadmap vs POAM (Ch 6)</td></tr>
            <tr><td>1530&ndash;1615</td><td>8</td><td>Working with data professionals &mdash; engagement practices, terminology (Ch 7)</td></tr>
            <tr><td>1615&ndash;1700</td><td>9</td><td>Asking the right questions &mdash; diagnostic questions for products, workforce, and AI (Ch 8&ndash;9)</td></tr>
          </tbody>
        </table>
      </div>

      <h2>DOCUMENTS</h2>
      <div className="callout info">
        <div className="callout-label">TM-EXEC PUBLICATIONS</div>
        <div className="callout-body">
          Course Manual: <a href={URLS.TM_EXEC} target="_blank" rel="noopener noreferrer" style={{color:'var(--navy)',fontWeight:700}}>TM_EXEC_SENIOR_LEADER.pdf</a> &nbsp;&bull;&nbsp;
          Concepts Guide: <a href={URLS.CG_TM_EXEC} target="_blank" rel="noopener noreferrer" style={{color:'var(--navy)',fontWeight:700}}>CONCEPTS_GUIDE_TM_EXEC.pdf</a> &nbsp;&bull;&nbsp;
          Syllabus: <a href={URLS.SYL_TM_EXEC} target="_blank" rel="noopener noreferrer" style={{color:'var(--navy)',fontWeight:700}}>SYLLABUS_TM_EXEC.pdf</a>
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
