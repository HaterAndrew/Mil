
interface Props {
  showPanel: (id: string) => void
}

export default function TM30({ showPanel }: Props) {
  return (
    <>
      <div className="section-header">
        <span className="section-badge">TM-30</span>
        <span className="section-title">Advanced Builder Manual &mdash; Data-Adjacent Specialists</span>
        <span className="section-subtitle">Prerequisite: TM-10 + TM-20 &bull; 17/25-series &bull; G2 &bull; Data analysts</span>
      </div>

      <div className="callout bluf">
        <div className="callout-label">BLUF</div>
        <div className="callout-body">TM-30 is for personnel who design and own MSS solutions. This level covers complex application design, advanced Pipeline Builder, Ontology architecture, AIP Logic configuration, data governance, and C2DAO standards. All work is done via the UI; coding is escalated to TM-40 developers.</div>
      </div>

      <div className="callout caution">
        <div className="callout-label">CAUTION</div>
        <div className="callout-body">Modifications to shared datasets or Object Types at TM-30 level affect all downstream applications and users across the formation, including coalition partners. Coordinate with your unit data steward and the USAREUR-AF C2DAO before publishing any changes to production resources.</div>
      </div>

      <div className="callout note">
        <div className="callout-label">NOTE &mdash; IS THIS YOUR LEVEL?</div>
        <div className="callout-body">TM-30 covers advanced no-code building &mdash; application design, pipeline architecture, governance. If your role requires <strong>coding, ML, or ORSA</strong>, TM-30 is a prerequisite to a specialist track. <button className="qr-link" onClick={() => showPanel('specialists' as any)}>View Specialist Tracks (TM-40/50) &rarr;</button></div>
      </div>

      <h2>COMPETENCIES UPON COMPLETION</h2>
      <div className="card-grid">
        <div className="card">
          <div className="card-label">ADVANCED WORKSHOP DESIGN</div>
          <div className="card-body">
            <ul>
              <li>Design multi-page Workshop applications with conditional logic and variable passing</li>
              <li>Build dynamic layouts: show/hide panels based on user selections</li>
              <li>Design navigation flows and inter-page parameter handoff</li>
              <li>Publish and manage application versions</li>
            </ul>
          </div>
        </div>
        <div className="card">
          <div className="card-label">ADVANCED PIPELINE BUILDER</div>
          <div className="card-body">
            <ul>
              <li>Build multi-source join pipelines with complex aggregations (visual)</li>
              <li>Design scheduled and triggered pipeline runs</li>
              <li>Review and interpret data lineage graphs</li>
              <li>Escalate to TM-40 when code transforms are required</li>
            </ul>
          </div>
        </div>
        <div className="card">
          <div className="card-label">ONTOLOGY ARCHITECTURE</div>
          <div className="card-body">
            <ul>
              <li>Design Object Type and Link Type models via Ontology Manager UI</li>
              <li>Architecture thinking: model for downstream app requirements, not just source data</li>
              <li>Design Action workflows with validation and approval logic via UI</li>
              <li>Coordinate ontology changes with all downstream application owners</li>
            </ul>
          </div>
        </div>
        <div className="card">
          <div className="card-label">ADVANCED ANALYSIS</div>
          <div className="card-body">
            <ul>
              <li>Conduct advanced Contour analysis: complex aggregations, pivots, calculated columns, saved views</li>
              <li>Build advanced Quiver dashboards with multi-object analysis and linked views</li>
              <li>Create reusable analysis templates for unit use</li>
            </ul>
          </div>
        </div>
        <div className="card">
          <div className="card-label">AIP LOGIC &amp; CONFIGURATION</div>
          <div className="card-body">
            <ul>
              <li>Configure AIP Logic workflows via the UI (not author them &mdash; that is TM-40H)</li>
              <li>Connect AIP agents to Workshop applications</li>
              <li>Review and validate AI workflow outputs before production deployment</li>
            </ul>
          </div>
        </div>
        <div className="card">
          <div className="card-label">GOVERNANCE &amp; PRODUCTION</div>
          <div className="card-body">
            <ul>
              <li>Manage branching and production promotion via UI</li>
              <li>Apply USAREUR-AF C2DAO governance standards and naming conventions</li>
              <li>Manage governance workflows with data stewards</li>
              <li>Ensure coalition-facing products have C2DAO coordination and NAFv4 compliance review</li>
            </ul>
          </div>
        </div>
      </div>

      <h2>TM-30 vs TM-40 &mdash; WHAT YOU OWN VS WHAT YOU ESCALATE</h2>
      <div className="table-wrap">
        <table>
          <thead><tr><th>You Own At TM-30 (UI)</th><th>Escalate to TM-40 When&hellip;</th></tr></thead>
          <tbody>
            <tr><td>Application design and UX</td><td>Custom Python/PySpark transforms needed</td></tr>
            <tr><td>Ontology model design (via UI)</td><td>Functions on Objects (TypeScript) required</td></tr>
            <tr><td>Advanced Pipeline Builder (visual)</td><td>Incremental watermark or code logic needed</td></tr>
            <tr><td>AIP Logic configuration</td><td>Custom AIP Logic workflow authoring needed</td></tr>
            <tr><td>Governance coordination</td><td>External application (OSDK) needed</td></tr>
            <tr><td>Production promotion via UI</td><td>CI/CD pipeline automation needed</td></tr>
          </tbody>
        </table>
      </div>

      <h2>C2DAO GOVERNANCE GATES &mdash; HARD STOPS</h2>
      <div className="table-wrap">
        <table>
          <thead><tr><th>Requirement</th><th>TM-30 Action</th><th>Hard Gate?</th></tr></thead>
          <tbody>
            <tr><td>New shared Object Type or dataset</td><td>Coordinate with C2DAO before publishing to production</td><td>Yes</td></tr>
            <tr><td>Coalition / MPE-facing data product</td><td>C2DAO coordination + NAFv4 compliance review</td><td>Yes &mdash; do not skip</td></tr>
            <tr><td>Schema change to existing shared resource</td><td>Notify all downstream owners; coordinate with steward</td><td>Yes</td></tr>
            <tr><td>New AIP Logic workflow on operational data</td><td>Authorization review before deployment</td><td>Yes</td></tr>
            <tr><td>Access permission changes</td><td>Submit through formal request to unit data steward</td><td>Yes</td></tr>
          </tbody>
        </table>
      </div>

      <div className="training-section">
        <h2><span className="training-icon">SCHED</span> UPCOMING TRAINING &mdash; TM-30</h2>
        <div className="callout note">
          <div className="callout-label">ENROLLMENT</div>
          <div className="callout-body">TM-10 and TM-20 must be complete before attending TM-30. Class size is limited. Contact POC early &mdash; seats fill quickly. Bring TM-10 and TM-20 completion certificates on day one.</div>
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
                <td><strong>28 APR &ndash; 02 MAY 2026</strong></td>
                <td>Wiesbaden, Clay Kaserne, Bldg 3312, Rm 104</td>
                <td>In-Person</td>
                <td>CW3 Thompson</td>
                <td>4 / 10</td>
                <td><span className="seat-low">4 SEATS REMAINING</span></td>
              </tr>
              <tr>
                <td><strong>15&ndash;19 JUN 2026</strong></td>
                <td>Virtual (MS Teams)</td>
                <td>Virtual</td>
                <td>CW2 Rodriguez</td>
                <td>15 / 15</td>
                <td><span className="seat-open">OPEN</span></td>
              </tr>
              <tr>
                <td><strong>17&ndash;21 AUG 2026</strong></td>
                <td>Wiesbaden, Clay Kaserne, Bldg 3312, Rm 104</td>
                <td>In-Person</td>
                <td>CW3 Thompson</td>
                <td>10 / 10</td>
                <td><span className="seat-open">OPEN</span></td>
              </tr>
            </tbody>
          </table>
        </div>
        <p style={{fontSize:'12px',color:'var(--gray-400)'}}>Duration: 5 days (40 hours). Course runs 0800&ndash;1700 each day. Prerequisites: TM-10 and TM-20 complete. All dates subject to change &mdash; confirm with POC 5 days prior.</p>
      </div>

      <div className="specialist-cta">
        <div className="specialist-cta-text">
          <div className="specialist-cta-label">Next Level &mdash; After TM-30</div>
          <div className="specialist-cta-title">Specialist Tracks &mdash; TM-40 &amp; TM-50 Series</div>
          <div className="specialist-cta-sub">Six role-specific tracks for ORSA, AI Engineer, ML Engineer, Program Manager, Knowledge Manager, and Software Engineer. Select your track based on MOS/role.</div>
        </div>
        <button className="specialist-cta-btn" onClick={() => showPanel('specialists' as any)}>
          Access Specialist Tracks <span className="btn-arrow">&#8594;</span>
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
