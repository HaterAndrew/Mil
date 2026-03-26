import { URLS } from '../constants/urls'

interface Props {
  showPanel: (id: string) => void
}

export default function Specialists({ showPanel }: Props) {
  return (
    <>
      <div className="section-header">
        <span className="section-badge">SPECIALIST TRACKS</span>
        <span className="section-title">SL 4 &amp; SL 5 Series &mdash; WFF &amp; Technical Tracks</span>
        <span className="section-subtitle">WFF tracks (A&ndash;F): SL 3 req. &bull; Technical tracks (G&ndash;O): SL 3 req.</span>
      </div>

      <div className="callout bluf">
        <div className="callout-label">BLUF</div>
        <div className="callout-body">SL 4 has two track types: <strong>Warfighting Function tracks (SL 4A&ndash;F)</strong> for WFF-assigned roles (Intelligence, Fires, M&amp;M, Sustainment, Protection, Mission Command) &mdash; prerequisite SL 3, no coding required &mdash; and <strong>Technical Specialist tracks (SL 4G&ndash;O)</strong> for personnel who build and engineer MSS solutions (ORSA, AI Eng, MLE, PM, KM, SWE, UX Designer, Platform Eng) &mdash; prerequisite SL 3. Advanced versions (SL 5G&ndash;O) are available after completing the corresponding SL 4 technical track.</div>
      </div>

      <h2>TRACK SELECTION BY MOS / ROLE</h2>
      <div className="table-wrap">
        <table>
          <thead>
            <tr><th>Role / MOS</th><th>Recommended Track</th><th>Advanced</th></tr>
          </thead>
          <tbody>
            <tr><td colSpan={3} style={{background:'var(--navy-pale)',fontWeight:700,fontSize:11,letterSpacing:'.06em',textTransform:'uppercase',color:'var(--navy)'}}>Warfighting Function Tracks (SL 4A&ndash;F)</td></tr>
            <tr><td>G2/S2 &mdash; MI units, ISR analysts</td><td><strong>SL 4A (Intelligence)</strong></td><td>&mdash;</td></tr>
            <tr><td>FA officers/NCOs &mdash; Fire support</td><td><strong>SL 4B (Fires)</strong></td><td>&mdash;</td></tr>
            <tr><td>Maneuver units &mdash; G3/S3 data roles</td><td><strong>SL 4C (Movement &amp; Maneuver)</strong></td><td>&mdash;</td></tr>
            <tr><td>G4/S4 &mdash; Logistics, GCSS-A</td><td><strong>SL 4D (Sustainment)</strong></td><td>&mdash;</td></tr>
            <tr><td>Air defense, CBRN, force protection</td><td><strong>SL 4E (Protection)</strong></td><td>&mdash;</td></tr>
            <tr><td>G6/S6 &mdash; C2 systems, networks</td><td><strong>SL 4F (Mission Command)</strong></td><td>&mdash;</td></tr>
            <tr><td colSpan={3} style={{background:'var(--navy-pale)',fontWeight:700,fontSize:11,letterSpacing:'.06em',textTransform:'uppercase',color:'var(--navy)'}}>Technical Specialist Tracks (SL 4G&ndash;O)</td></tr>
            <tr><td>FA49 &mdash; Operations Research Analyst</td><td><strong>SL 4G (ORSA)</strong></td><td>SL 5G</td></tr>
            <tr><td>G2/S2 quantitative analyst</td><td><strong>SL 4G (ORSA)</strong> or SL 4K (KM)</td><td>SL 5G / SL 5K</td></tr>
            <tr><td>17A/17C &mdash; Cyber officer/NCO</td><td><strong>SL 4L (SWE)</strong> or SL 4H (AI Eng)</td><td>SL 5L / SL 5H</td></tr>
            <tr><td>25D &mdash; IT specialist</td><td><strong>SL 4L (SWE)</strong></td><td>SL 5L</td></tr>
            <tr><td>AI/ML engineer (GS/contractor)</td><td><strong>SL 4H (AI Eng)</strong> or SL 4M (MLE)</td><td>SL 5H / SL 5M</td></tr>
            <tr><td>Data scientist (GS/contractor)</td><td><strong>SL 4G (ORSA)</strong> or SL 4M (MLE)</td><td>SL 5G / SL 5M</td></tr>
            <tr><td>G8/S8 &mdash; Resource manager</td><td><strong>SL 4J (PM)</strong></td><td>SL 5J</td></tr>
            <tr><td>Program Manager (PM / GS)</td><td><strong>SL 4J (PM)</strong></td><td>SL 5J</td></tr>
            <tr><td>KMO / Knowledge Officer / 37F</td><td><strong>SL 4K (KM)</strong></td><td>SL 5K</td></tr>
            <tr><td>Civil Affairs</td><td><strong>SL 4J (PM)</strong> or SL 4K (KM)</td><td>SL 5J / SL 5K</td></tr>
            <tr><td>UI/UX Designer (GS/contractor)</td><td><strong>SL 4N (UI/UX)</strong></td><td>SL 5N</td></tr>
            <tr><td>Human Factors / User Researcher</td><td><strong>SL 4N (UI/UX)</strong></td><td>SL 5N</td></tr>
            <tr><td>DevOps / Platform Engineer (GS/contractor)</td><td><strong>SL 4O (Platform)</strong></td><td>SL 5O</td></tr>
            <tr><td>25D &mdash; IT specialist (infra focus)</td><td><strong>SL 4O (Platform)</strong></td><td>SL 5O</td></tr>
          </tbody>
        </table>
      </div>

      <div className="specialists-section-hdr">SL 4 SERIES &mdash; WARFIGHTING FUNCTION TRACKS</div>
      <div className="track-grid">
        <div className="track-card">
          <div className="track-card-hdr"><span className="track-tm">TM-40A (SL 4A) &mdash; Intelligence</span><span className="track-chip">SL 3 Req.</span></div>
          <div className="track-body">
            <div className="track-name">Intelligence Warfighting Function</div>
            <div className="track-audience">G2/S2 &bull; MI units &bull; ISR analysts</div>
            <div className="track-prereq">Prereq: SL 3 &bull; <a href={URLS.SL4A} target="_blank" rel="noreferrer" style={{color:'var(--navy)',fontSize:11}}>Open PDF &rarr;</a></div>
          </div>
        </div>
        <div className="track-card">
          <div className="track-card-hdr"><span className="track-tm">TM-40B (SL 4B) &mdash; Fires</span><span className="track-chip">SL 3 Req.</span></div>
          <div className="track-body">
            <div className="track-name">Fires Warfighting Function</div>
            <div className="track-audience">FA officers/NCOs &bull; Fire support coordinators</div>
            <div className="track-prereq">Prereq: SL 3 &bull; <a href={URLS.SL4B} target="_blank" rel="noreferrer" style={{color:'var(--navy)',fontSize:11}}>Open PDF &rarr;</a></div>
          </div>
        </div>
        <div className="track-card">
          <div className="track-card-hdr"><span className="track-tm">TM-40C (SL 4C) &mdash; Movement &amp; Maneuver</span><span className="track-chip">SL 3 Req.</span></div>
          <div className="track-body">
            <div className="track-name">Movement &amp; Maneuver WFF</div>
            <div className="track-audience">Maneuver units &bull; G3/S3 data roles</div>
            <div className="track-prereq">Prereq: SL 3 &bull; <a href={URLS.SL4C} target="_blank" rel="noreferrer" style={{color:'var(--navy)',fontSize:11}}>Open PDF &rarr;</a></div>
          </div>
        </div>
        <div className="track-card">
          <div className="track-card-hdr"><span className="track-tm">TM-40D (SL 4D) &mdash; Sustainment</span><span className="track-chip">SL 3 Req.</span></div>
          <div className="track-body">
            <div className="track-name">Sustainment Warfighting Function</div>
            <div className="track-audience">Logistics &bull; G4/S4 &bull; GCSS-A users</div>
            <div className="track-prereq">Prereq: SL 3 &bull; <a href={URLS.SL4D} target="_blank" rel="noreferrer" style={{color:'var(--navy)',fontSize:11}}>Open PDF &rarr;</a></div>
          </div>
        </div>
        <div className="track-card">
          <div className="track-card-hdr"><span className="track-tm">TM-40E (SL 4E) &mdash; Protection</span><span className="track-chip">SL 3 Req.</span></div>
          <div className="track-body">
            <div className="track-name">Protection Warfighting Function</div>
            <div className="track-audience">Air defense &bull; CBRN &bull; Engineer &bull; Force protection</div>
            <div className="track-prereq">Prereq: SL 3 &bull; <a href={URLS.SL4E} target="_blank" rel="noreferrer" style={{color:'var(--navy)',fontSize:11}}>Open PDF &rarr;</a></div>
          </div>
        </div>
        <div className="track-card">
          <div className="track-card-hdr"><span className="track-tm">TM-40F (SL 4F) &mdash; Mission Command</span><span className="track-chip">SL 3 Req.</span></div>
          <div className="track-body">
            <div className="track-name">Mission Command Warfighting Function</div>
            <div className="track-audience">G6/S6 &bull; C2 systems &bull; Network managers</div>
            <div className="track-prereq">Prereq: SL 3 &bull; <a href={URLS.SL4F} target="_blank" rel="noreferrer" style={{color:'var(--navy)',fontSize:11}}>Open PDF &rarr;</a></div>
          </div>
        </div>
      </div>

      <div className="specialists-section-hdr">SL 4 SERIES &mdash; TECHNICAL SPECIALIST TRACKS (Level 1)</div>

      <div className="track-grid">
        <div className="track-card">
          <div className="track-card-hdr"><span className="track-tm">TM-40G (SL 4G) &mdash; ORSA</span><span className="track-chip">SL 3 Req.</span></div>
          <div className="track-body">
            <div className="track-name">Operations Research &amp; Systems Analysis</div>
            <div className="track-audience">FA49 &bull; G2/S2 quant analysts &bull; Wargame analysts</div>
            <div className="track-prereq">Prereq: SL 3 &bull; Advanced: SL 5G &bull; <button className="panel-nav-btn" style={{padding:'4px 10px',fontSize:10}} onClick={() => showPanel('sl4')}>View SL 4 Series &rarr;</button></div>
          </div>
        </div>
        <div className="track-card">
          <div className="track-card-hdr"><span className="track-tm">TM-40H (SL 4H) &mdash; AI Engineer</span><span className="track-chip">SL 3 Req.</span></div>
          <div className="track-body">
            <div className="track-name">AIP Logic, Agent Studio &amp; LLM Integration</div>
            <div className="track-audience">AI/ML specialists &bull; 17A/17C</div>
            <div className="track-prereq">Prereq: SL 3 &bull; Advanced: SL 5H &bull; <button className="panel-nav-btn" style={{padding:'4px 10px',fontSize:10}} onClick={() => showPanel('sl4')}>View SL 4 Series &rarr;</button></div>
          </div>
        </div>
        <div className="track-card">
          <div className="track-card-hdr"><span className="track-tm">TM-40M (SL 4M) &mdash; ML Engineer</span><span className="track-chip">SL 3 Req.</span></div>
          <div className="track-body">
            <div className="track-name">Model Development, Validation &amp; Deployment</div>
            <div className="track-audience">ML engineers &bull; Data scientists (GS/contractor)</div>
            <div className="track-prereq">Prereq: SL 3 &bull; Advanced: SL 5M &bull; <button className="panel-nav-btn" style={{padding:'4px 10px',fontSize:10}} onClick={() => showPanel('sl4')}>View SL 4 Series &rarr;</button></div>
          </div>
        </div>
        <div className="track-card">
          <div className="track-card-hdr"><span className="track-tm">TM-40J (SL 4J) &mdash; Program Manager</span><span className="track-chip">SL 3 Req.</span></div>
          <div className="track-body">
            <div className="track-name">Pipeline Mgmt, Milestones &amp; Portfolio Health</div>
            <div className="track-audience">G8/S8 &bull; PMs &bull; Civil Affairs</div>
            <div className="track-prereq">Prereq: SL 3 &bull; Advanced: SL 5J &bull; <button className="panel-nav-btn" style={{padding:'4px 10px',fontSize:10}} onClick={() => showPanel('sl4')}>View SL 4 Series &rarr;</button></div>
          </div>
        </div>
        <div className="track-card">
          <div className="track-card-hdr"><span className="track-tm">TM-40K (SL 4K) &mdash; Knowledge Manager</span><span className="track-chip">SL 3 Req.</span></div>
          <div className="track-body">
            <div className="track-name">Forms, Lessons Learned &amp; Institutional Memory</div>
            <div className="track-audience">KMOs &bull; 37F &bull; Civil Affairs</div>
            <div className="track-prereq">Prereq: SL 3 &bull; Advanced: SL 5K &bull; <button className="panel-nav-btn" style={{padding:'4px 10px',fontSize:10}} onClick={() => showPanel('sl4')}>View SL 4 Series &rarr;</button></div>
          </div>
        </div>
        <div className="track-card">
          <div className="track-card-hdr"><span className="track-tm">TM-40L (SL 4L) &mdash; Software Engineer</span><span className="track-chip">SL 3 Req.</span></div>
          <div className="track-body">
            <div className="track-name">Python/TypeScript, OSDK &amp; Code Transforms</div>
            <div className="track-audience">17A/17C &bull; 25D &bull; GS/contractor SWEs</div>
            <div className="track-prereq">Prereq: SL 3 &bull; Advanced: SL 5L &bull; <button className="panel-nav-btn" style={{padding:'4px 10px',fontSize:10}} onClick={() => showPanel('sl4')}>View SL 4 Series &rarr;</button></div>
          </div>
        </div>
      </div>

      <div className="specialists-section-hdr">SL 5 SERIES &mdash; ADVANCED TRACKS (Level 2)</div>
      <div className="callout info">
        <div className="callout-label">NOTE</div>
        <div className="callout-body">SL 5 tracks are advanced-level continuations requiring the corresponding SL 4 track as a prerequisite. They cover expert-level techniques, production architecture, and operational integration at scale.</div>
      </div>
      <div className="panel-nav-btns" style={{marginTop:12}}>
        <button className="panel-nav-btn" onClick={() => showPanel('sl5')}>Open SL 5 Series Full Reference &#8594;</button>
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
