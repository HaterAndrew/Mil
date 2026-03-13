
interface Props {
  showPanel: (id: string) => void
}

export default function Doctrine({ showPanel }: Props) {
  return (
    <>
      <div className="section-header">
        <span className="section-badge">DRAFT PUBS</span>
        <span className="section-title">Draft Data Literacy Publications</span>
        <span className="section-subtitle">DRAFT &mdash; Not yet approved for distribution &bull; Foundational data literacy content &bull; Platform-agnostic</span>
      </div>

      <div className="callout caution">
        <div className="callout-label">CAUTION &mdash; DRAFT PUBLICATIONS</div>
        <div className="callout-body">These publications are in draft status and have not been approved for official distribution. Do not distribute outside the USAREUR-AF training program without authorization from the USAREUR-AF Operational Data Team.</div>
      </div>

      <div className="callout bluf">
        <div className="callout-label">BLUF</div>
        <div className="callout-body">Before touching MSS, understand <em>why</em> data matters. Data Literacy for Senior Leaders is written for commanders and senior leaders. Data Literacy Technical Reference is the comprehensive reference for all personnel. Neither publication is platform-specific.</div>
      </div>

      <div className="card-grid card-grid-2">
        <div className="card gold-top">
          <div className="card-label">SENIOR LEADERS (O-5+ / SGM+)</div>
          <div className="card-title">Data Literacy for Senior Leaders</div>
          <div className="card-body">
            <p>Written for commanders, senior NCOs, and senior civilians. Covers command responsibilities, evaluating data products, directing a data-capable formation, and decision frameworks.</p>
            <p><strong>Format:</strong> Short (~20&ndash;30pp). Principles, not procedures. Chapter/paragraph numbered.</p>
            <p><strong>Key topics:</strong> Commander&rsquo;s data responsibilities &bull; Evaluating analytical products &bull; Standing up MSS capability &bull; Data governance and stewardship</p>
          </div>
        </div>
        <div className="card">
          <div className="card-label">ALL PERSONNEL</div>
          <div className="card-title">Data Literacy Reference</div>
          <div className="card-body">
            <p>Comprehensive platform-agnostic data literacy reference. Recommended prior reading before TM-10.</p>
            <p><strong>Format:</strong> Long (~50&ndash;100pp). Examples, vignettes, detailed explanations, annexes.</p>
            <p><strong>Key topics:</strong> Data types and structures &bull; Pipeline concepts &bull; Data quality &bull; Analysis fundamentals &bull; Security and classification &bull; Operational data integration &bull; Governance</p>
          </div>
        </div>
      </div>

      <h2>FULL PUBLICATIONS INDEX</h2>
      <div className="table-wrap">
        <table>
          <thead><tr><th>Publication</th><th>Audience</th><th>Purpose</th><th>When to Read</th></tr></thead>
          <tbody>
            <tr><td colSpan={4} style={{background:'var(--navy-pale)',fontWeight:700,fontSize:'11px',letterSpacing:'.06em',textTransform:'uppercase',color:'var(--navy)'}}>Foundation &mdash; All Personnel</td></tr>
            <tr><td><strong>Data Literacy (SL)</strong></td><td>O-5+ / SGM+, Sr Civilians</td><td>Principles, command responsibilities</td><td>Before directing MSS use</td></tr>
            <tr><td><strong>Data Literacy</strong></td><td>All personnel</td><td>Comprehensive data literacy reference</td><td>Before TM-10 (recommended)</td></tr>
            <tr><td><strong>TM-10</strong></td><td>All personnel</td><td>Operate MSS as end user</td><td>Before first MSS access</td></tr>
            <tr><td><strong>TM-20</strong></td><td>All staff</td><td>Build pipelines, Ontology, Workshop via UI &mdash; no code</td><td>After TM-10</td></tr>
            <tr><td><strong>TM-30</strong></td><td>Data-adjacent specialists</td><td>Design complex apps; governance; C2DAO standards</td><td>After TM-10 + TM-20</td></tr>
            <tr><td colSpan={4} style={{background:'var(--navy-pale)',fontWeight:700,fontSize:'11px',letterSpacing:'.06em',textTransform:'uppercase',color:'var(--navy)'}}>TM-40 &mdash; Warfighting Function Tracks (by WFF assignment)</td></tr>
            <tr><td><strong>TM-40A</strong></td><td>G2/S2, MI, ISR</td><td>Intelligence WFF MSS integration</td><td>After TM-20</td></tr>
            <tr><td><strong>TM-40B</strong></td><td>FA, fire support</td><td>Fires WFF MSS integration</td><td>After TM-20</td></tr>
            <tr><td><strong>TM-40C</strong></td><td>Maneuver, G3/S3</td><td>Movement &amp; Maneuver WFF MSS integration</td><td>After TM-20</td></tr>
            <tr><td><strong>TM-40D</strong></td><td>G4/S4, logistics</td><td>Sustainment WFF MSS integration</td><td>After TM-20</td></tr>
            <tr><td><strong>TM-40E</strong></td><td>Air defense, CBRN, force protection</td><td>Protection WFF MSS integration</td><td>After TM-20</td></tr>
            <tr><td><strong>TM-40F</strong></td><td>G6/S6, C2, networks</td><td>Mission Command WFF MSS integration</td><td>After TM-20</td></tr>
            <tr><td colSpan={4} style={{background:'var(--navy-pale)',fontWeight:700,fontSize:'11px',letterSpacing:'.06em',textTransform:'uppercase',color:'var(--navy)'}}>TM-40 &mdash; Technical Specialist Tracks (by role/MOS)</td></tr>
            <tr><td><strong>TM-40G</strong></td><td>ORSA / FA49</td><td>Statistical modeling, simulation, wargame analytics</td><td>After TM-30</td></tr>
            <tr><td><strong>TM-40H</strong></td><td>AI Engineers</td><td>AIP Logic authoring, Agent Studio, LLM integration</td><td>After TM-30</td></tr>
            <tr><td><strong>TM-40I</strong></td><td>ML Engineers</td><td>Code Workspaces, model training, MLOps</td><td>After TM-30</td></tr>
            <tr><td><strong>TM-40J</strong></td><td>PMs / G8</td><td>PM dashboards, milestone tracking, portfolio analysis</td><td>After TM-30</td></tr>
            <tr><td><strong>TM-40K</strong></td><td>KMs / KMOs</td><td>Knowledge repositories, AIP summarization, lessons learned</td><td>After TM-30</td></tr>
            <tr><td><strong>TM-40L</strong></td><td>SWEs</td><td>OSDK, full-stack Foundry apps, TypeScript Functions</td><td>After TM-30</td></tr>
            <tr><td colSpan={4} style={{background:'var(--navy-pale)',fontWeight:700,fontSize:'11px',letterSpacing:'.06em',textTransform:'uppercase',color:'var(--navy)'}}>TM-50 &mdash; Advanced Technical Tracks (by role/MOS)</td></tr>
            <tr><td><strong>TM-50G&ndash;L</strong></td><td>Senior developers (all tracks)</td><td>Advanced versions of each TM-40 specialist track</td><td>After TM-40 (by track)</td></tr>
          </tbody>
        </table>
      </div>

      <h2>CORE DATA LITERACY CONCEPTS</h2>
      <div className="card-grid">
        <div className="card">
          <div className="card-label">DATA TYPES</div>
          <div className="card-body">Structured (tables, rows, columns) &bull; Semi-structured (JSON, XML) &bull; Unstructured (documents, images). MSS ingests all three types from Army source systems.</div>
        </div>
        <div className="card">
          <div className="card-label">DATA PIPELINE</div>
          <div className="card-body">Raw &rarr; Staging &rarr; Curated &rarr; Ontology &rarr; Application. Each layer adds quality, structure, and meaning. Never modify raw data &mdash; it is the source of truth.</div>
        </div>
        <div className="card">
          <div className="card-label">DATA QUALITY</div>
          <div className="card-body">Accuracy, completeness, consistency, timeliness, uniqueness. Bad decisions follow bad data. Report quality issues to your data steward rather than working around them.</div>
        </div>
        <div className="card">
          <div className="card-label">DATA GOVERNANCE</div>
          <div className="card-body">Ownership, stewardship, access control, classification markings. Every dataset has an owner. Every user has a role. Access is audited. Misuse is tracked and prosecuted.</div>
        </div>
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
