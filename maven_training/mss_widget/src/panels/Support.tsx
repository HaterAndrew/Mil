
interface Props {
  showPanel: (id: string) => void
}

export default function Support({ showPanel }: Props) {
  return (
    <>
      <div className="section-header">
        <span className="section-badge">SUPPORT</span>
        <span className="section-title">Getting Help &mdash; USAREUR-AF</span>
      </div>

      <div className="callout bluf">
        <div className="callout-label">BLUF</div>
        <div className="callout-body">Know who to call before you have a problem. Route issues correctly from the start. Collect information before calling for help &mdash; it speeds resolution significantly.</div>
      </div>

      <div className="callout warning">
        <div className="callout-label">WARNING &mdash; SECURITY INCIDENTS</div>
        <div className="callout-body">If you suspect a security violation, report immediately to your supervisor and unit security officer. Do not investigate or resolve it yourself. Preserve the screen state; do not close the window or clear the browser.</div>
      </div>

      <h2>CONTACT ROUTING</h2>
      <div className="table-wrap">
        <table>
          <thead><tr><th>Issue</th><th>Route To</th><th>Priority</th></tr></thead>
          <tbody>
            <tr><td>Cannot log in / CAC issues</td><td>MSS Help Desk</td><td>Normal</td></tr>
            <tr><td>No access to a project or dataset</td><td>Unit data steward</td><td>Normal</td></tr>
            <tr><td>Data appears incorrect</td><td>Unit data steward (do not self-correct)</td><td>Normal</td></tr>
            <tr><td>System error, crash, or outage</td><td>MSS Help Desk + screenshot + error code</td><td>Normal</td></tr>
            <tr><td>Application broken or not loading</td><td>MSS Help Desk</td><td>Normal</td></tr>
            <tr><td>Building question / how-to</td><td>Unit data lead or USAREUR-AF data team</td><td>Normal</td></tr>
            <tr><td>Governance / C2DAO question</td><td>USAREUR-AF C2DAO</td><td>Normal</td></tr>
            <tr><td><strong>Security incident</strong></td><td><strong>Supervisor + unit security officer</strong></td><td><strong>IMMEDIATE</strong></td></tr>
          </tbody>
        </table>
      </div>

      <h2>BEFORE CALLING FOR HELP &mdash; COLLECT THIS INFORMATION</h2>
      <ul>
        <li>Your username and unit</li>
        <li>Name of the application, dataset, or pipeline you were using</li>
        <li>Exact error message (screenshot preferred)</li>
        <li>Time the error occurred (local or Zulu &mdash; state which)</li>
        <li>Steps that led to the error in order</li>
        <li>Browser and workstation you are using</li>
      </ul>

      <h2>PREREQUISITES BEFORE FIRST LOGIN</h2>
      <ol>
        <li><strong>Annual Cyber Awareness Training</strong> &mdash; required for all DoD personnel; must be current</li>
        <li><strong>MSS User Onboarding Brief</strong> &mdash; provided by unit data steward</li>
        <li><strong>Account request approved</strong> &mdash; submit at <a href="https://mss.data.mil" target="_blank" rel="noreferrer" style={{color:'var(--navy-mid)',fontWeight:600}}>mss.data.mil</a> or through your unit data steward; provisioning generally completes within 24 hours. If access is not active after 24 hours, contact your data steward directly.</li>
      </ol>

      <h2>USAREUR-AF DATA TEAM</h2>
      <div className="card-grid">
        <div className="card gold-top">
          <div className="card-label">LOCATION &amp; HIGHER HQ</div>
          <div className="card-title">EUCOM Theater &mdash; Europe &amp; Africa</div>
          <div className="card-body">Headquarters, United States Army Europe and Africa<br/>USAREUR-AF Operational Data Team<br/>Army AI/Data Accelerator (C2DAO)</div>
        </div>
        <div className="card">
          <div className="card-label">PUBLICATIONS</div>
          <div className="card-body">All training publications are maintained by the USAREUR-AF Operational Data Team. Contact your unit data steward for access to source files and this application. Version 3.0 &mdash; March 2026.</div>
        </div>
        <div className="card">
          <div className="card-label">FEEDBACK &amp; CORRECTIONS</div>
          <div className="card-body">Route corrections through your unit data steward to the USAREUR-AF Operational Data Team. Include: publication name, section, and description of the issue.</div>
        </div>
      </div>

      <div className="callout note mt-24">
        <div className="callout-label">NOTE &mdash; DISTRIBUTION</div>
        <div className="callout-body">These are DRAFT documents — not yet approved for distribution. Do not distribute outside your organization without consulting your data steward.</div>
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
