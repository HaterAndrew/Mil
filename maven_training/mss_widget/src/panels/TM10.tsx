
interface Props {
  showPanel: (id: string) => void
}

export default function TM10({ showPanel }: Props) {
  return (
    <>
      <div className="section-header">
        <span className="section-badge">TM-10</span>
        <span className="section-title">Maven User Manual &mdash; All Personnel</span>
        <span className="section-subtitle">No technical background required &bull; Prerequisite: None</span>
      </div>

      <div className="callout bluf">
        <div className="callout-label">BLUF</div>
        <div className="callout-body">TM-10 teaches you how to log in, navigate MSS, read dashboards, submit data through forms, use AI tools, and stay within authorized boundaries. Required for all USAREUR-AF personnel before operating MSS. <strong>Request your account before your first class &mdash; submit at <a href="https://mss.data.mil" target="_blank" rel="noreferrer" style={{color:'var(--navy-dark)'}}>mss.data.mil</a> or through your data steward. Provisioning generally completes within 24 hours.</strong></div>
      </div>

      <div className="callout caution">
        <div className="callout-label">CAUTION &mdash; REQUEST YOUR ACCOUNT FIRST</div>
        <div className="callout-body">You cannot log in without a provisioned account. <strong>Do not wait until the first day of class.</strong> Request your account at <a href="https://mss.data.mil" target="_blank" rel="noreferrer" style={{color:'var(--caution-amber)',fontWeight:700}}>mss.data.mil</a> or through your unit data steward &mdash; provisioning generally completes within 24 hours. If access is not active after 24 hours, contact your data steward. Steps are in Section 1 below.</div>
      </div>

      <h2>1. GETTING ACCESS &mdash; DO THIS FIRST</h2>
      <ol>
        <li>Find your <strong>unit data steward</strong> (data stewards may be embedded in your unit, assigned at battalion, brigade, or division level, or positioned within a directorate at the ASCC &mdash; ask your chain of command if you&rsquo;re unsure who to contact).</li>
        <li>Ask them to submit an MSS account request with your name, unit, MOS, and required access level.</li>
        <li>MSS admin team provisions your account and assigns <strong>markings</strong> (markings = the data categories and classification levels you&rsquo;re authorized to see).</li>
        <li>You receive notification when account is active — typically 3&ndash;5 business days.</li>
        <li>Receive the MSS portal URL from your unit data steward. This is your login link.</li>
      </ol>
      <div className="callout note mt-24">
        <div className="callout-label">NOTE &mdash; DATA STEWARD</div>
        <div className="callout-body">Your <strong>data steward</strong> manages MSS access and data quality for your organization. They may be embedded in your unit, assigned at a higher echelon, or positioned within a directorate at the ASCC. They are your first point of contact for account requests, access problems, and data errors. If you don&rsquo;t know who they are, ask your chain of command.</div>
      </div>

      <h2>2. WHAT IS MSS?</h2>
      <p>MSS is a secure, web-based platform where your unit&rsquo;s data lives and can be analyzed and acted upon. Think of it as a shared operations center for data: information from logistics, personnel, readiness, and other systems is collected, organized, and made accessible through applications your unit uses every day.</p>
      <p>MSS is built on the Palantir Foundry platform, authorized for Army use under the Maven Smart System program.</p>
      <div className="callout note">
        <div className="callout-label">NOTE &mdash; WHAT IS FOUNDRY?</div>
        <div className="callout-body">Palantir Foundry is a commercial data platform that Army headquarters selected to run MSS. You do not need to know how it works &mdash; just how to use it. The word &ldquo;Foundry&rdquo; may appear in help documentation and system menus; it refers to the same platform as MSS.</div>
      </div>

      <div className="card-grid">
        <div className="card">
          <div className="card-label">MSS DOES</div>
          <div className="card-body">
            <ul>
              <li>Stores data from Army systems in a single, organized location</li>
              <li>Makes data visible through applications and dashboards</li>
              <li>Enables units to update records, report status, and track readiness</li>
              <li>Provides analysis tools for authorized personnel</li>
              <li>Supports AI-assisted analysis through authorized tools</li>
            </ul>
          </div>
        </div>
        <div className="card red-top">
          <div className="card-label">MSS IS NOT</div>
          <div className="card-body">
            <ul>
              <li>Not a replacement for official systems of record (DCPDS, GCSS-A, MEDPROS, etc.)</li>
              <li>Not classified by default &mdash; classification depends on data markings</li>
              <li>Not a public system &mdash; access is controlled and audited</li>
            </ul>
          </div>
        </div>
        <div className="card gold-top">
          <div className="card-label">USAREUR-AF MISSION AREAS</div>
          <div className="card-body">
            <ul>
              <li><strong>Personnel Readiness</strong> &mdash; soldier readiness status</li>
              <li><strong>Logistics</strong> &mdash; equipment availability &amp; maintenance</li>
              <li><strong>Operational Reporting</strong> &mdash; SITREPs and updates</li>
              <li><strong>Planning</strong> &mdash; orders, unit positions, task org</li>
              <li><strong>C2</strong> &mdash; unit status across the AOR</li>
            </ul>
          </div>
        </div>
      </div>

      <h2>3. SECURITY RESPONSIBILITIES</h2>

      <div className="callout warning">
        <div className="callout-label">WARNING</div>
        <div className="callout-body">Unauthorized access to, disclosure of, or modification of data in MSS may constitute a violation of 18 U.S.C. &sect; 1030 (Computer Fraud and Abuse Act) and applicable Army regulations. Violations may result in disciplinary action, loss of access, and criminal prosecution.</div>
      </div>

      <ol>
        <li>Use only your own credentials. Do not share your CAC, PIN, or access tokens.</li>
        <li>Access only data you are authorized to view.</li>
        <li>Report misrouted data immediately. If you see data at a higher classification than your clearance &mdash; STOP and report it.</li>
        <li>Do not export data without authorization. Exports are logged.</li>
        <li>Log out when done. Do not leave an MSS session unattended on an unlocked workstation.</li>
        <li>Report security incidents immediately to your supervisor and unit security officer.</li>
      </ol>

      <h2>4. TASKS</h2>

      <div className="task-block">
        <div className="task-header">TASK: ACCESS THE MAVEN SMART SYSTEM</div>
        <div className="task-meta">
          <div className="task-meta-item">
            <div className="task-meta-label">Conditions</div>
            <div className="task-meta-value">Provisioned MSS account, CAC reader, approved workstation and browser</div>
          </div>
          <div className="task-meta-item">
            <div className="task-meta-label">Standards</div>
            <div className="task-meta-value">Successfully authenticate with CAC and reach the MSS home screen</div>
          </div>
          <div className="task-meta-item">
            <div className="task-meta-label">Equipment</div>
            <div className="task-meta-value">CAC, CAC reader, workstation, MSS portal URL (from unit data steward)</div>
          </div>
        </div>
        <div className="task-body">
          <ol className="task-steps">
            <li>Insert your CAC into the CAC reader.</li>
            <li>Open an approved web browser (Chrome or Firefox recommended).</li>
            <li>Navigate to the MSS portal URL provided by your unit data steward.</li>
            <li>When prompted, select your <strong>authentication certificate</strong> (not email certificate).</li>
            <li>Enter your CAC PIN when prompted.</li>
            <li>MSS home screen loads &mdash; you are now logged in.</li>
          </ol>
          <div className="callout caution mb-8">
            <div className="callout-label">CAUTION</div>
            <div className="callout-body">Do not save your PIN in the browser. Do not allow the browser to remember your login. MSS sessions may contain sensitive information.</div>
          </div>
        </div>
      </div>

      <div className="task-block">
        <div className="task-header">TASK: NAVIGATE THE MSS HOME SCREEN</div>
        <div className="task-meta">
          <div className="task-meta-item">
            <div className="task-meta-label">Conditions</div>
            <div className="task-meta-value">Logged into MSS</div>
          </div>
          <div className="task-meta-item">
            <div className="task-meta-label">Standards</div>
            <div className="task-meta-value">Identify all major navigation elements; locate search, notifications, and profile</div>
          </div>
        </div>
        <div className="task-body">
          <div className="table-wrap">
            <table>
              <thead><tr><th>Element</th><th>Location</th><th>Purpose</th></tr></thead>
              <tbody>
                <tr><td>Search bar</td><td>Top center</td><td>Find datasets, applications, and projects</td></tr>
                <tr><td>Notification bell</td><td>Top right</td><td>System alerts, workflow updates</td></tr>
                <tr><td>User profile icon</td><td>Top right</td><td>Account settings, markings (your authorized data categories), logout</td></tr>
                <tr><td>Compass (file explorer)</td><td>Left sidebar</td><td>Browse all MSS resources</td></tr>
                <tr><td>Home button (logo)</td><td>Top left</td><td>Return to home screen from anywhere</td></tr>
                <tr><td>Pinned items</td><td>Home main area</td><td>Shortcuts to frequently used resources</td></tr>
                <tr><td>Recent activity</td><td>Home main area</td><td>Recently visited datasets and apps</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <h2>5. REPORTING PROBLEMS</h2>
      <div className="table-wrap">
        <table>
          <thead><tr><th>Problem Type</th><th>Who to Contact</th></tr></thead>
          <tbody>
            <tr><td>Cannot log in</td><td>MSS Help Desk</td></tr>
            <tr><td>Cannot access a project</td><td>Unit data steward</td></tr>
            <tr><td>Data appears incorrect</td><td>Unit data steward (do not correct it yourself)</td></tr>
            <tr><td>System error or crash</td><td>MSS Help Desk (provide error code and screenshot)</td></tr>
            <tr><td>Security incident</td><td>Supervisor and unit security officer &mdash; IMMEDIATELY</td></tr>
            <tr><td>Application not working</td><td>MSS Help Desk</td></tr>
          </tbody>
        </table>
      </div>

      <div className="training-section">
        <h2><span className="training-icon">SCHED</span> UPCOMING TRAINING &mdash; TM-10</h2>
        <div className="callout note">
          <div className="callout-label">ENROLLMENT</div>
          <div className="callout-body">Contact the listed POC to reserve a seat. Bring your CAC and ensure your MSS account request is submitted at least 5 business days before the course start date. Virtual sessions require MS Teams access and a headset.</div>
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
                <td><strong>14 APR 2026</strong></td>
                <td>Wiesbaden, Clay Kaserne, Bldg 3312, Rm 104</td>
                <td>In-Person</td>
                <td>SSG Johnson</td>
                <td>20 / 20</td>
                <td><span className="seat-open">OPEN</span></td>
              </tr>
              <tr>
                <td><strong>05 MAY 2026</strong></td>
                <td>Grafenw&ouml;hr, Bldg 244, Conf Rm B</td>
                <td>In-Person</td>
                <td>SFC Davis</td>
                <td>8 / 20</td>
                <td><span className="seat-low">8 SEATS REMAINING</span></td>
              </tr>
              <tr>
                <td><strong>18 JUN 2026</strong></td>
                <td>Stuttgart, Kelley Bks, Bldg 3357</td>
                <td>In-Person</td>
                <td>SSG Martinez</td>
                <td>20 / 20</td>
                <td><span className="seat-open">OPEN</span></td>
              </tr>
              <tr>
                <td><strong>09 JUL 2026</strong></td>
                <td>Virtual (MS Teams)</td>
                <td>Virtual</td>
                <td>SSG Johnson</td>
                <td>30 / 30</td>
                <td><span className="seat-open">OPEN</span></td>
              </tr>
            </tbody>
          </table>
        </div>
        <p style={{fontSize:'12px',color:'var(--gray-400)'}}>Duration: 1 day (8 hours). Course runs 0800&ndash;1700. All dates subject to change &mdash; confirm with POC 5 days prior.</p>
      </div>

      <div className="specialist-cta" style={{marginTop:'32px'}}>
        <div className="specialist-cta-text">
          <div className="specialist-cta-label">Next Level &mdash; After TM-10</div>
          <div className="specialist-cta-title">TM-20 &mdash; No-Code Builder Manual</div>
          <div className="specialist-cta-sub">Learn to ingest data, build Workshop applications, create Object Types, and manage projects &mdash; all without coding. Required prereq for all builder roles.</div>
        </div>
        <button className="specialist-cta-btn" onClick={() => showPanel('tm20' as any)}>
          Continue to TM-20 <span className="btn-arrow">&#8594;</span>
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
