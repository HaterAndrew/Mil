
interface Props {
  showPanel: (id: string) => void
}

export default function TM20({ showPanel }: Props) {
  return (
    <>
      <div className="section-header">
        <span className="section-badge">SL 2</span>
        <span className="section-title">No-Code Builder Manual &mdash; All Staff</span>
        <span className="section-subtitle">Prerequisite: SL 1 &bull; No coding required</span>
      </div>

      <div className="callout bluf">
        <div className="callout-label">BLUF</div>
        <div className="callout-body">SL 2 teaches you how to ingest data, build Workshop applications, create Object Types and basic Actions, and manage projects &mdash; all using the graphical user interface. No coding required. Prerequisite: SL 1 complete.</div>
      </div>

      <h2>COMPETENCIES UPON COMPLETION</h2>
      <div className="card-grid">
        <div className="card">
          <div className="card-label">PROJECT MANAGEMENT (UI)</div>
          <div className="card-body">
            <ul>
              <li>Create and organize Foundry projects via the UI</li>
              <li>Set up folder structure: raw / staging / curated layers</li>
              <li>Manage project access and permissions via UI</li>
              <li>Follow USAREUR-AF naming conventions and builder standards</li>
            </ul>
          </div>
        </div>
        <div className="card">
          <div className="card-label">DATA INGEST (NO CODE)</div>
          <div className="card-body">
            <ul>
              <li>Ingest data using Pipeline Builder &mdash; visual, no code</li>
              <li>Configure connectors and file sources via UI</li>
              <li>Schedule pipeline runs via UI</li>
              <li>Understand raw / staging / curated dataset layers</li>
            </ul>
          </div>
        </div>
        <div className="card">
          <div className="card-label">ONTOLOGY (UI)</div>
          <div className="card-body">
            <ul>
              <li>Create Object Types and set primary keys via Ontology Manager UI</li>
              <li>Create Link Types between objects via UI</li>
              <li>Build basic Actions via Action Editor UI</li>
              <li>Test Object Types in Object Explorer before building apps</li>
            </ul>
          </div>
        </div>
        <div className="card">
          <div className="card-label">WORKSHOP APPLICATIONS</div>
          <div className="card-body">
            <ul>
              <li>Build and publish Workshop applications with dashboards, forms, and filters</li>
              <li>Select and configure appropriate widgets for each use case</li>
              <li>Apply access controls and publish to users</li>
            </ul>
          </div>
        </div>
        <div className="card">
          <div className="card-label">BRANCHING &amp; GOVERNANCE</div>
          <div className="card-body">
            <ul>
              <li>Use Foundry branching to build and promote via UI</li>
              <li>Distinguish development from production environments</li>
              <li>Apply USAREUR-AF builder standards</li>
            </ul>
            <p style={{marginTop:'8px',fontSize:'12px',color:'var(--gray-600)'}}><em>Branching = making a test copy of your work before going live. You build in the <strong>dev branch</strong> (your sandbox), test it, then publish to <strong>production</strong> (what users see).</em></p>
          </div>
        </div>
      </div>

      <h2>THE FOUNDRY DATA STACK</h2>
      <p>Data flows through layers. As an SL 2 builder, you work in the middle layers using visual tools. Never modify raw data — report data errors to your data steward instead.</p>
      <div className="stack-diagram">
        <div className="stack-layer layer-1">Workshop App / AIP Agent (consume)</div>
        <div className="stack-arrow">&#x25B2;</div>
        <div className="stack-layer layer-2">Ontology (Objects, Links, Actions)</div>
        <div className="stack-arrow">&#x25B2;</div>
        <div className="stack-layer layer-3">Curated Dataset (Pipeline Builder output)</div>
        <div className="stack-arrow">&#x25B2;</div>
        <div className="stack-layer layer-4">Staging Dataset (Pipeline Builder transforms)</div>
        <div className="stack-arrow">&#x25B2;</div>
        <div className="stack-layer layer-5">Raw Dataset &mdash; READ ONLY, never modify</div>
      </div>

      <h2>WORKSHOP WIDGET SELECTION</h2>
      <div className="table-wrap">
        <table>
          <thead><tr><th>You Need To&hellip;</th><th>Use This Widget</th></tr></thead>
          <tbody>
            <tr><td>Display many objects or records</td><td>Object Table</td></tr>
            <tr><td>Show details for one selected object</td><td>Object Detail</td></tr>
            <tr><td>Let users filter the data they see</td><td>Filter Panel / Dropdown</td></tr>
            <tr><td>Show a chart (bar, line, pie)</td><td>Chart Widget</td></tr>
            <tr><td>Show geographic data on a map</td><td>Map Widget</td></tr>
            <tr><td>Let users write or update data</td><td>Button + Action or Action Form</td></tr>
            <tr><td>Show a single key metric prominently</td><td>Metric Tile</td></tr>
            <tr><td>Navigate between app sections</td><td>Navigation / Tab Widget</td></tr>
          </tbody>
        </table>
      </div>

      <h2>ONTOLOGY SETUP ORDER (UI STEPS)</h2>
      <ol>
        <li>Confirm curated dataset exists and is populated (Pipeline Builder pipeline passing)</li>
        <li>Open <strong>Ontology Manager</strong> in the left sidebar</li>
        <li>Create Object Type &rarr; set primary key property &rarr; map properties from curated dataset</li>
        <li>Create Link Types between related Object Types (if needed)</li>
        <li>Publish ontology branch and test in <strong>Object Explorer</strong></li>
        <li>Build Workshop app only after Object Explorer confirms objects are visible</li>
      </ol>

      <h2>NAMING CONVENTIONS</h2>
      <div className="table-wrap">
        <table>
          <thead><tr><th>Object Type</th><th>Convention</th><th>Example</th></tr></thead>
          <tbody>
            <tr><td>Datasets (path)</td><td><code>/Project/AOR/source/raw|staging|curated</code></td><td><code>/USAREUR/EUR/personnel/curated/soldier_status</code></td></tr>
            <tr><td>Object Types</td><td><code>PascalCase</code></td><td><code>UnitStatus</code></td></tr>
            <tr><td>Properties (API name)</td><td><code>camelCase</code></td><td><code>unitName</code></td></tr>
            <tr><td>Properties (display name)</td><td>Title Case</td><td><code>Unit Name</code></td></tr>
            <tr><td>Link Types</td><td><code>PascalCase</code> verb form</td><td><code>HasEquipment</code></td></tr>
            <tr><td>Workshop app names</td><td>Unit + function + version</td><td><code>EUR-Personnel-Readiness-v2</code></td></tr>
          </tbody>
        </table>
      </div>

      <div className="callout caution mt-24">
        <div className="callout-label">CAUTION &mdash; SHARED RESOURCES</div>
        <div className="callout-body">Changes to shared datasets and Object Types affect all downstream applications and users. Before modifying a shared resource, coordinate with your data steward.</div>
      </div>

      <div className="training-section">
        <h2><span className="training-icon">SCHED</span> UPCOMING TRAINING &mdash; SL 2</h2>
        <div className="callout note">
          <div className="callout-label">ENROLLMENT</div>
          <div className="callout-body">SL 1 must be complete before attending SL 2. Contact the listed POC to reserve a seat. Bring completion certificate from SL 1 on day one.</div>
        </div>
        <div className="table-wrap">
          <table>
            <thead>
              <tr>
                <th>Dates</th>
                <th>Location</th>
                <th>Format</th>
                <th>POC</th>
                <th>Seats</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>21&ndash;25 APR 2026</strong></td>
                <td>Wiesbaden, Clay Kaserne, Bldg 3312, Rm 104</td>
                <td>In-Person</td>
                <td>SFC Chen</td>
                <td>7 / 15</td>
                <td><span className="seat-low">7 SEATS REMAINING</span></td>
              </tr>
              <tr>
                <td><strong>11&ndash;15 MAY 2026</strong></td>
                <td>Grafenw&ouml;hr, Bldg 244, Conf Rm B</td>
                <td>In-Person</td>
                <td>SSG Williams</td>
                <td>3 / 15</td>
                <td><span className="seat-low">3 SEATS REMAINING</span></td>
              </tr>
              <tr>
                <td><strong>22&ndash;26 JUN 2026</strong></td>
                <td>Stuttgart, Kelley Bks, Bldg 3357</td>
                <td>In-Person</td>
                <td>SFC Chen</td>
                <td>15 / 15</td>
                <td><span className="seat-open">OPEN</span></td>
              </tr>
              <tr>
                <td><strong>13&ndash;17 JUL 2026</strong></td>
                <td>Virtual (MS Teams)</td>
                <td>Virtual</td>
                <td>SSG Williams</td>
                <td>20 / 20</td>
                <td><span className="seat-open">OPEN</span></td>
              </tr>
            </tbody>
          </table>
        </div>
        <p style={{fontSize:'12px',color:'var(--gray-400)'}}>Duration: 5 days (40 hours). Course runs 0800&ndash;1700 each day. Prerequisite: SL 1 complete. All dates subject to change &mdash; confirm with POC 5 days prior.</p>
      </div>

      <div className="specialist-cta" style={{marginTop:'32px'}}>
        <div className="specialist-cta-text">
          <div className="specialist-cta-label">Next Level &mdash; After SL 2</div>
          <div className="specialist-cta-title">SL 3 &mdash; Advanced Builder Manual</div>
          <div className="specialist-cta-sub">For data-adjacent specialists: complex application design, advanced pipelines, Ontology architecture, AIP Logic, and C2DAO governance. Required prereq for all SL 4 tracks.</div>
        </div>
        <button className="specialist-cta-btn" onClick={() => showPanel('sl3')}>
          Continue to SL 3 <span className="btn-arrow">&#8594;</span>
        </button>
      </div>

      <div className="callout note mt-24">
        <div className="callout-label">NOT FINDING WHAT YOU NEED?</div>
        <div className="callout-body">
          Contact your unit data steward for additional publications, source files, or access to restricted materials.
          For technical support, visit the <button className="qr-link" onClick={() => showPanel('support')}>Support page &rarr;</button>
          For task-level procedures, use the <button className="qr-link" onClick={() => showPanel('taskindex')}>Task Index &rarr;</button>
        </div>
      </div>
    </>
  )
}
