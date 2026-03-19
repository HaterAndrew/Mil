import { URLS } from '../constants/urls'

interface Props {
  showPanel: (id: string) => void
}

export default function Specialists({ showPanel }: Props) {
  return (
    <>
      <div className="section-header">
        <span className="section-badge">SPECIALIST TRACKS</span>
        <span className="section-title">TM-40 &amp; TM-50 Series &mdash; WFF &amp; Technical Tracks</span>
        <span className="section-subtitle">WFF tracks (A&ndash;F): TM-30 req. &bull; Technical tracks (G&ndash;O): TM-30 req.</span>
      </div>

      <div className="callout bluf">
        <div className="callout-label">BLUF</div>
        <div className="callout-body">TM-40 has two track types: <strong>Warfighting Function tracks (TM-40A&ndash;F)</strong> for WFF-assigned roles (Intelligence, Fires, M&amp;M, Sustainment, Protection, Mission Command) &mdash; prerequisite TM-30, no coding required &mdash; and <strong>Technical Specialist tracks (TM-40G&ndash;O)</strong> for personnel who build and engineer MSS solutions (ORSA, AI Eng, MLE, PM, KM, SWE, UX Designer, Platform Eng) &mdash; prerequisite TM-30. Advanced versions (TM-50G&ndash;O) are available after completing the corresponding TM-40 technical track.</div>
      </div>

      <h2>TRACK SELECTION BY MOS / ROLE</h2>
      <div className="table-wrap">
        <table>
          <thead>
            <tr><th>Role / MOS</th><th>Recommended Track</th><th>Advanced</th></tr>
          </thead>
          <tbody>
            <tr><td colSpan={3} style={{background:'var(--navy-pale)',fontWeight:700,fontSize:11,letterSpacing:'.06em',textTransform:'uppercase',color:'var(--navy)'}}>Warfighting Function Tracks (TM-40A&ndash;F)</td></tr>
            <tr><td>G2/S2 &mdash; MI units, ISR analysts</td><td><strong>TM-40A (Intelligence)</strong></td><td>&mdash;</td></tr>
            <tr><td>FA officers/NCOs &mdash; Fire support</td><td><strong>TM-40B (Fires)</strong></td><td>&mdash;</td></tr>
            <tr><td>Maneuver units &mdash; G3/S3 data roles</td><td><strong>TM-40C (Movement &amp; Maneuver)</strong></td><td>&mdash;</td></tr>
            <tr><td>G4/S4 &mdash; Logistics, GCSS-A</td><td><strong>TM-40D (Sustainment)</strong></td><td>&mdash;</td></tr>
            <tr><td>Air defense, CBRN, force protection</td><td><strong>TM-40E (Protection)</strong></td><td>&mdash;</td></tr>
            <tr><td>G6/S6 &mdash; C2 systems, networks</td><td><strong>TM-40F (Mission Command)</strong></td><td>&mdash;</td></tr>
            <tr><td colSpan={3} style={{background:'var(--navy-pale)',fontWeight:700,fontSize:11,letterSpacing:'.06em',textTransform:'uppercase',color:'var(--navy)'}}>Technical Specialist Tracks (TM-40G&ndash;O)</td></tr>
            <tr><td>FA49 &mdash; Operations Research Analyst</td><td><strong>TM-40G (ORSA)</strong></td><td>TM-50G</td></tr>
            <tr><td>G2/S2 quantitative analyst</td><td><strong>TM-40G (ORSA)</strong> or TM-40K (KM)</td><td>TM-50G / TM-50K</td></tr>
            <tr><td>17A/17C &mdash; Cyber officer/NCO</td><td><strong>TM-40L (SWE)</strong> or TM-40H (AI Eng)</td><td>TM-50L / TM-50H</td></tr>
            <tr><td>25D &mdash; IT specialist</td><td><strong>TM-40L (SWE)</strong></td><td>TM-50L</td></tr>
            <tr><td>AI/ML engineer (GS/contractor)</td><td><strong>TM-40H (AI Eng)</strong> or TM-40M (MLE)</td><td>TM-50H / TM-50M</td></tr>
            <tr><td>Data scientist (GS/contractor)</td><td><strong>TM-40G (ORSA)</strong> or TM-40M (MLE)</td><td>TM-50G / TM-50M</td></tr>
            <tr><td>G8/S8 &mdash; Resource manager</td><td><strong>TM-40J (PM)</strong></td><td>TM-50J</td></tr>
            <tr><td>Program Manager (PM / GS)</td><td><strong>TM-40J (PM)</strong></td><td>TM-50J</td></tr>
            <tr><td>KMO / Knowledge Officer / 37F</td><td><strong>TM-40K (KM)</strong></td><td>TM-50K</td></tr>
            <tr><td>Civil Affairs</td><td><strong>TM-40J (PM)</strong> or TM-40K (KM)</td><td>TM-50J / TM-50K</td></tr>
            <tr><td>UI/UX Designer (GS/contractor)</td><td><strong>TM-40N (UI/UX)</strong></td><td>TM-50N</td></tr>
            <tr><td>Human Factors / User Researcher</td><td><strong>TM-40N (UI/UX)</strong></td><td>TM-50N</td></tr>
            <tr><td>DevOps / Platform Engineer (GS/contractor)</td><td><strong>TM-40O (Platform)</strong></td><td>TM-50O</td></tr>
            <tr><td>25D &mdash; IT specialist (infra focus)</td><td><strong>TM-40O (Platform)</strong></td><td>TM-50O</td></tr>
          </tbody>
        </table>
      </div>

      <div className="specialists-section-hdr">TM-40 SERIES &mdash; WARFIGHTING FUNCTION TRACKS</div>
      <div className="track-grid">
        <div className="track-card">
          <div className="track-card-hdr"><span className="track-tm">TM-40A &mdash; Intelligence</span><span className="track-chip">TM-30 Req.</span></div>
          <div className="track-body">
            <div className="track-name">Intelligence Warfighting Function</div>
            <div className="track-audience">G2/S2 &bull; MI units &bull; ISR analysts</div>
            <div className="track-prereq">Prereq: TM-30 &bull; <a href={URLS.TM40A} target="_blank" rel="noreferrer" style={{color:'var(--navy)',fontSize:11}}>Open PDF &rarr;</a></div>
          </div>
        </div>
        <div className="track-card">
          <div className="track-card-hdr"><span className="track-tm">TM-40B &mdash; Fires</span><span className="track-chip">TM-30 Req.</span></div>
          <div className="track-body">
            <div className="track-name">Fires Warfighting Function</div>
            <div className="track-audience">FA officers/NCOs &bull; Fire support coordinators</div>
            <div className="track-prereq">Prereq: TM-30 &bull; <a href={URLS.TM40B} target="_blank" rel="noreferrer" style={{color:'var(--navy)',fontSize:11}}>Open PDF &rarr;</a></div>
          </div>
        </div>
        <div className="track-card">
          <div className="track-card-hdr"><span className="track-tm">TM-40C &mdash; Movement &amp; Maneuver</span><span className="track-chip">TM-30 Req.</span></div>
          <div className="track-body">
            <div className="track-name">Movement &amp; Maneuver WFF</div>
            <div className="track-audience">Maneuver units &bull; G3/S3 data roles</div>
            <div className="track-prereq">Prereq: TM-30 &bull; <a href={URLS.TM40C} target="_blank" rel="noreferrer" style={{color:'var(--navy)',fontSize:11}}>Open PDF &rarr;</a></div>
          </div>
        </div>
        <div className="track-card">
          <div className="track-card-hdr"><span className="track-tm">TM-40D &mdash; Sustainment</span><span className="track-chip">TM-30 Req.</span></div>
          <div className="track-body">
            <div className="track-name">Sustainment Warfighting Function</div>
            <div className="track-audience">Logistics &bull; G4/S4 &bull; GCSS-A users</div>
            <div className="track-prereq">Prereq: TM-30 &bull; <a href={URLS.TM40D} target="_blank" rel="noreferrer" style={{color:'var(--navy)',fontSize:11}}>Open PDF &rarr;</a></div>
          </div>
        </div>
        <div className="track-card">
          <div className="track-card-hdr"><span className="track-tm">TM-40E &mdash; Protection</span><span className="track-chip">TM-30 Req.</span></div>
          <div className="track-body">
            <div className="track-name">Protection Warfighting Function</div>
            <div className="track-audience">Air defense &bull; CBRN &bull; Engineer &bull; Force protection</div>
            <div className="track-prereq">Prereq: TM-30 &bull; <a href={URLS.TM40E} target="_blank" rel="noreferrer" style={{color:'var(--navy)',fontSize:11}}>Open PDF &rarr;</a></div>
          </div>
        </div>
        <div className="track-card">
          <div className="track-card-hdr"><span className="track-tm">TM-40F &mdash; Mission Command</span><span className="track-chip">TM-30 Req.</span></div>
          <div className="track-body">
            <div className="track-name">Mission Command Warfighting Function</div>
            <div className="track-audience">G6/S6 &bull; C2 systems &bull; Network managers</div>
            <div className="track-prereq">Prereq: TM-30 &bull; <a href={URLS.TM40F} target="_blank" rel="noreferrer" style={{color:'var(--navy)',fontSize:11}}>Open PDF &rarr;</a></div>
          </div>
        </div>
      </div>

      <div className="specialists-section-hdr">TM-40 SERIES &mdash; TECHNICAL SPECIALIST TRACKS (Level 1)</div>

      <div className="track-grid">
        <div className="track-card">
          <div className="track-card-hdr"><span className="track-tm">TM-40G &mdash; ORSA</span><span className="track-chip">TM-30 Req.</span></div>
          <div className="track-body">
            <div className="track-name">Operations Research &amp; Systems Analysis</div>
            <div className="track-audience">FA49 &bull; G2/S2 quant analysts &bull; Wargame analysts</div>
            <div className="track-prereq">Prereq: TM-30 &bull; Advanced: TM-50G &bull; <button className="panel-nav-btn" style={{padding:'4px 10px',fontSize:10}} onClick={() => showPanel('tm40' as any)}>View TM-40 Series &rarr;</button></div>
          </div>
        </div>
        <div className="track-card">
          <div className="track-card-hdr"><span className="track-tm">TM-40H &mdash; AI Engineer</span><span className="track-chip">TM-30 Req.</span></div>
          <div className="track-body">
            <div className="track-name">AIP Logic, Agent Studio &amp; LLM Integration</div>
            <div className="track-audience">AI/ML specialists &bull; 17A/17C</div>
            <div className="track-prereq">Prereq: TM-30 &bull; Advanced: TM-50H &bull; <button className="panel-nav-btn" style={{padding:'4px 10px',fontSize:10}} onClick={() => showPanel('tm40' as any)}>View TM-40 Series &rarr;</button></div>
          </div>
        </div>
        <div className="track-card">
          <div className="track-card-hdr"><span className="track-tm">TM-40M &mdash; ML Engineer</span><span className="track-chip">TM-30 Req.</span></div>
          <div className="track-body">
            <div className="track-name">Model Development, Validation &amp; Deployment</div>
            <div className="track-audience">ML engineers &bull; Data scientists (GS/contractor)</div>
            <div className="track-prereq">Prereq: TM-30 &bull; Advanced: TM-50M &bull; <button className="panel-nav-btn" style={{padding:'4px 10px',fontSize:10}} onClick={() => showPanel('tm40' as any)}>View TM-40 Series &rarr;</button></div>
          </div>
        </div>
        <div className="track-card">
          <div className="track-card-hdr"><span className="track-tm">TM-40J &mdash; Program Manager</span><span className="track-chip">TM-30 Req.</span></div>
          <div className="track-body">
            <div className="track-name">Pipeline Mgmt, Milestones &amp; Portfolio Health</div>
            <div className="track-audience">G8/S8 &bull; PMs &bull; Civil Affairs</div>
            <div className="track-prereq">Prereq: TM-30 &bull; Advanced: TM-50J &bull; <button className="panel-nav-btn" style={{padding:'4px 10px',fontSize:10}} onClick={() => showPanel('tm40' as any)}>View TM-40 Series &rarr;</button></div>
          </div>
        </div>
        <div className="track-card">
          <div className="track-card-hdr"><span className="track-tm">TM-40K &mdash; Knowledge Manager</span><span className="track-chip">TM-30 Req.</span></div>
          <div className="track-body">
            <div className="track-name">Forms, Lessons Learned &amp; Institutional Memory</div>
            <div className="track-audience">KMOs &bull; 37F &bull; Civil Affairs</div>
            <div className="track-prereq">Prereq: TM-30 &bull; Advanced: TM-50K &bull; <button className="panel-nav-btn" style={{padding:'4px 10px',fontSize:10}} onClick={() => showPanel('tm40' as any)}>View TM-40 Series &rarr;</button></div>
          </div>
        </div>
        <div className="track-card">
          <div className="track-card-hdr"><span className="track-tm">TM-40L &mdash; Software Engineer</span><span className="track-chip">TM-30 Req.</span></div>
          <div className="track-body">
            <div className="track-name">Python/TypeScript, OSDK &amp; Code Transforms</div>
            <div className="track-audience">17A/17C &bull; 25D &bull; GS/contractor SWEs</div>
            <div className="track-prereq">Prereq: TM-30 &bull; Advanced: TM-50L &bull; <button className="panel-nav-btn" style={{padding:'4px 10px',fontSize:10}} onClick={() => showPanel('tm40' as any)}>View TM-40 Series &rarr;</button></div>
          </div>
        </div>
      </div>

      <div className="specialists-section-hdr">TM-50 SERIES &mdash; ADVANCED TRACKS (Level 2)</div>
      <div className="callout info">
        <div className="callout-label">NOTE</div>
        <div className="callout-body">TM-50 tracks are advanced-level continuations requiring the corresponding TM-40 track as a prerequisite. They cover expert-level techniques, production architecture, and operational integration at scale.</div>
      </div>
      <div className="panel-nav-btns" style={{marginTop:12}}>
        <button className="panel-nav-btn" onClick={() => showPanel('tm50' as any)}>Open TM-50 Series Full Reference &#8594;</button>
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
