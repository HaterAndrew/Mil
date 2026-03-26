import { URLS } from '../constants/urls'

interface Props {
  showPanel: (id: string) => void
}

export default function Home({ showPanel }: Props) {
  return (
    <>
      <div className="section-header">
        <span className="section-badge">HOME</span>
        <span className="section-title">MSS Training Curriculum &mdash; USAREUR-AF</span>
        <span className="section-subtitle">Version 3.1 &bull; March 2026</span>
      </div>

      <div className="callout info">
        <div className="callout-label">NEW TO MSS?</div>
        <div className="callout-body"><strong>Start with the Quick Start guide</strong> before reading the Skill Level (SL) 1 manual. It gets you operational in 30 minutes: log in, navigate, filter data, and export a view. &rarr; <a href={URLS.QUICK_START} target="_blank" rel="noreferrer" style={{color:'var(--navy)',fontWeight:700}}>QUICK_START.pdf</a></div>
      </div>

      <div className="callout bluf">
        <div className="callout-label">BLUF</div>
        <div className="callout-body">The MSS curriculum is organized by Skill Level (SL) per DA PAM 611-21. All personnel start at SL 1. Builders add SL 2. Data specialists continue to SL 3. Technical roles proceed to the appropriate SL 4 track. Use the sidebar to navigate to your specific guidance.</div>
      </div>

      <div className="specialist-cta" style={{marginBottom:20}}>
        <div className="specialist-cta-text">
          <div className="specialist-cta-label">Not sure where to start?</div>
          <div className="specialist-cta-title">Find My Track</div>
          <div className="specialist-cta-sub">Answer two quick questions and get your personalized training path — no reading required.</div>
        </div>
        <button className="specialist-cta-btn" onClick={() => showPanel('findmytrack')}>
          Find My Track <span className="btn-arrow">&#8594;</span>
        </button>
      </div>

      <h2>STEP 1 &mdash; FIND YOUR LEVEL</h2>
      <div className="table-wrap">
        <table>
          <thead>
            <tr><th>You Are&hellip;</th><th>Start Here</th><th>Then</th><th>Tab</th></tr>
          </thead>
          <tbody>
            <tr>
              <td>Any Soldier, officer, or Civilian &mdash; using MSS to access and consume data</td>
              <td><strong><button className="qr-link" onClick={() => showPanel('sl1')}>SL 1 (User)</button></strong></td>
              <td>&mdash;</td>
              <td><span className="chip chip-navy" style={{cursor:'pointer'}} onClick={() => showPanel('sl1')}>SL 1</span></td>
            </tr>
            <tr>
              <td>All staff &mdash; building dashboards, forms, or pipelines without coding</td>
              <td><strong><button className="qr-link" onClick={() => showPanel('sl1')}>SL 1</button></strong></td>
              <td><button className="qr-link" onClick={() => showPanel('sl2')}>SL 2 (Builder)</button></td>
              <td><span className="chip chip-navy" style={{cursor:'pointer'}} onClick={() => showPanel('sl2')}>SL 2</span></td>
            </tr>
            <tr>
              <td>Data-adjacent specialist &mdash; 17/25-series, G2, data analyst</td>
              <td><strong><button className="qr-link" onClick={() => showPanel('sl1')}>SL 1</button> &rarr; <button className="qr-link" onClick={() => showPanel('sl2')}>SL 2</button></strong></td>
              <td><button className="qr-link" onClick={() => showPanel('sl3')}>SL 3 (Advanced)</button></td>
              <td><span className="chip chip-gold" style={{cursor:'pointer'}} onClick={() => showPanel('sl3')}>SL 3</span></td>
            </tr>
            <tr>
              <td>Technical specialist &mdash; ORSA, AI/ML, MLE, PM, KM, SWE, UI/UX, Platform roles (SL 4G&ndash;O)</td>
              <td><strong><button className="qr-link" onClick={() => showPanel('sl1')}>SL 1</button> &rarr; <button className="qr-link" onClick={() => showPanel('sl2')}>SL 2</button> &rarr; <button className="qr-link" onClick={() => showPanel('sl3')}>SL 3</button></strong></td>
              <td><button className="qr-link" onClick={() => showPanel('sl4')}>SL 4 specialist track</button></td>
              <td><span className="chip chip-gold" style={{cursor:'pointer'}} onClick={() => showPanel('specialists')}>SL 4</span></td>
            </tr>
            <tr>
              <td>WFF specialist &mdash; assigned Intel, Fires, M&amp;M, Sustainment, Protection, or Mission Command role (SL 4A&ndash;F)</td>
              <td><strong><button className="qr-link" onClick={() => showPanel('sl1')}>SL 1</button> &rarr; <button className="qr-link" onClick={() => showPanel('sl2')}>SL 2</button> &rarr; <button className="qr-link" onClick={() => showPanel('sl3')}>SL 3</button></strong></td>
              <td><button className="qr-link" onClick={() => showPanel('specialists')}>SL 4 WFF track</button></td>
              <td><span className="chip chip-gold" style={{cursor:'pointer'}} onClick={() => showPanel('specialists')}>SL 4</span></td>
            </tr>
            <tr>
              <td>Senior leader (O-5+ / SGM+) directing a data-capable formation</td>
              <td><strong><button className="qr-link" onClick={() => showPanel('doctrine')}>Data Literacy (SL)</button></strong></td>
              <td>Optional: Data Literacy</td>
              <td><span className="chip chip-gray" style={{cursor:'pointer'}} onClick={() => showPanel('doctrine')}>DRAFT PUBS</span></td>
            </tr>
            <tr>
              <td>Anyone wanting data literacy background before touching MSS</td>
              <td><strong><button className="qr-link" onClick={() => showPanel('doctrine')}>Data Literacy</button></strong></td>
              <td>SL 1</td>
              <td><span className="chip chip-gray" style={{cursor:'pointer'}} onClick={() => showPanel('doctrine')}>DRAFT PUBS</span></td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>STEP 2 &mdash; FOLLOW THE TRAINING PATH</h2>

      {/* Data Literacy: outside the main pipeline — dashed border callout */}
      <div style={{border:'2px dashed var(--gray-200)',borderRadius:'6px',padding:'14px 16px 10px',marginBottom:'16px',background:'var(--off-white)'}}>
        <div style={{fontFamily:'var(--font-ui)',fontSize:'9px',fontWeight:700,letterSpacing:'2px',textTransform:'uppercase',color:'var(--gray-400)',marginBottom:'10px'}}>OUTSIDE THE PIPELINE &mdash; BACKGROUND READING (NOT REQUIRED BEFORE SL 1, BUT RECOMMENDED)</div>
        <div className="path-flow" style={{marginBottom:0}}>
          <div className="path-step">
            <div className="path-connector">
              <div className="path-dot optional" style={{fontSize:'10px',width:'34px',height:'34px'}}>SL</div>
              <div className="path-line dashed"></div>
            </div>
            <div className="path-content" style={{cursor:'pointer'}} onClick={() => showPanel('doctrine')}>
              <div className="path-tm">DATA LIT (SL) &mdash; OPTIONAL (O-5+ / SGM+)</div>
              <div className="path-name">Data Literacy for Senior Leaders <span style={{fontSize:'11px',color:'var(--navy-mid)'}}>&#8594; Draft Pubs</span></div>
              <div className="path-audience">Principles, command responsibilities, decision frameworks</div>
            </div>
          </div>
          <div className="path-spacer"></div>
          <div className="path-step">
            <div className="path-connector">
              <div className="path-dot optional" style={{fontSize:'10px',width:'34px',height:'34px'}}>ALL</div>
            </div>
            <div className="path-content" style={{cursor:'pointer'}} onClick={() => showPanel('doctrine')}>
              <div className="path-tm">DATA LITERACY &mdash; RECOMMENDED (ALL PERSONNEL)</div>
              <div className="path-name">Data Literacy Reference <span style={{fontSize:'11px',color:'var(--navy-mid)'}}>&#8594; Draft Pubs</span></div>
              <div className="path-audience">Platform-agnostic data literacy; recommended before SL 1</div>
            </div>
          </div>
        </div>
      </div>

      <div className="path-flow">
        <div className="path-step">
          <div className="path-connector">
            <div className="path-dot">1</div>
            <div className="path-line"></div>
          </div>
          <div className="path-content" style={{cursor:'pointer'}} onClick={() => showPanel('sl1')}>
            <div className="path-tm">SL 1 &mdash; REQUIRED FOR ALL PERSONNEL</div>
            <div className="path-name">Maven User Manual <span style={{fontSize:'11px',color:'var(--navy-mid)'}}>&#8594; TM-10</span></div>
            <div className="path-audience">CAC login, navigation, Workshop apps, data viewing, AI tools, security</div>
          </div>
        </div>
        <div className="path-spacer"></div>

        <div className="path-step">
          <div className="path-connector">
            <div className="path-dot">2</div>
            <div className="path-line"></div>
          </div>
          <div className="path-content" style={{cursor:'pointer'}} onClick={() => showPanel('sl2')}>
            <div className="path-tm">SL 2 &mdash; ALL STAFF (NO-CODE BUILDER)</div>
            <div className="path-name">Builder Manual <span style={{fontSize:'11px',color:'var(--navy-mid)'}}>&#8594; TM-20</span></div>
            <div className="path-audience">Pipeline Builder (visual), Ontology Manager UI, Workshop app builder</div>
          </div>
        </div>
        <div className="path-spacer"></div>

        <div className="path-step">
          <div className="path-connector">
            <div className="path-dot">3</div>
            <div className="path-line"></div>
          </div>
          <div className="path-content" style={{cursor:'pointer'}} onClick={() => showPanel('sl3')}>
            <div className="path-tm">SL 3 &mdash; DATA-ADJACENT SPECIALISTS</div>
            <div className="path-name">Advanced Builder Manual <span style={{fontSize:'11px',color:'var(--navy-mid)'}}>&#8594; TM-30</span></div>
            <div className="path-audience">Complex app design, Ontology architecture, governance, C2DAO standards</div>
          </div>
        </div>
        <div className="path-spacer"></div>

        <div className="path-step">
          <div className="path-connector">
            <div className="path-dot">4</div>
          </div>
          <div className="path-content" style={{cursor:'pointer'}} onClick={() => showPanel('specialists')}>
            <div className="path-tm">SL 4 &mdash; TWO TRACK TYPES (BY ROLE)</div>
            <div className="path-name">Specialist &amp; Warfighting Function Tracks <span style={{fontSize:'11px',color:'var(--navy-mid)'}}>&#8594; Specialist Tracks</span></div>
            <div className="path-audience"><strong>WFF Tracks (SL 4A&ndash;F):</strong> Intel &bull; Fires &bull; M&amp;M &bull; Sustainment &bull; Protection &bull; Mission Command<br/><strong>Technical Tracks (SL 4G&ndash;O):</strong> ORSA &bull; AI Eng &bull; MLE &bull; PM &bull; KM &bull; SWE &mdash; Advanced versions at SL 5G&ndash;O</div>
          </div>
        </div>
      </div>

      <div className="callout info">
        <div className="callout-label">SL 4 TRACK SELECTION &mdash; BY MOS / ROLE</div>
        <div className="callout-body">
          <strong style={{display:'block',marginBottom:'4px'}}>Warfighting Function Tracks (SL 4A&ndash;F):</strong>
          <strong>Intelligence (SL 4A):</strong> G2/S2, MI units, ISR analysts<br/>
          <strong>Fires (SL 4B):</strong> FA officers/NCOs, fire support coordinators<br/>
          <strong>Movement &amp; Maneuver (SL 4C):</strong> Maneuver units, G3/S3 data roles<br/>
          <strong>Sustainment (SL 4D):</strong> Logistics, G4/S4, GCSS-A users<br/>
          <strong>Protection (SL 4E):</strong> Air defense, CBRN, engineer, force protection<br/>
          <strong>Mission Command (SL 4F):</strong> G6/S6, C2 systems, network managers<br/><br/>
          <strong style={{display:'block',marginBottom:'4px'}}>Technical Specialist Tracks (SL 4G&ndash;O):</strong>
          <strong>ORSA (SL 4G):</strong> FA49, G2/S2 quant analysts, wargame specialists<br/>
          <strong>AI Engineer (SL 4H):</strong> AI/ML specialists, 17A/17C<br/>
          <strong>ML Engineer (SL 4M):</strong> ML engineers, data scientists (GS/contractor)<br/>
          <strong>Program Manager (SL 4J):</strong> G8/S8, PMs, resource managers<br/>
          <strong>Knowledge Manager (SL 4K):</strong> KMOs, 37F, institutional memory leads<br/>
          <strong>Software Engineer (SL 4L):</strong> 17A/17C, 25D/25U, GS/contractor SWEs<br/>
          <strong>UI/UX Designer (SL 4N):</strong> UI/UX designers, human factors, GS/contractor designers<br/>
          <strong>Platform Engineer (SL 4O):</strong> DevOps, platform engineers, SysAdmins, 25D (infra focus)<br/><br/>
          <em>Not listed? Ask your commander &mdash; you may be assigned a track based on unit needs.</em><br/>
          Full mapping: <button className="qr-link" onClick={() => showPanel('specialists')}>Specialist Tracks &rarr;</button>
        </div>
      </div>

      <div className="callout note mt-24">
        <div className="callout-label">NOTE &mdash; MSS ACCOUNT ACCESS</div>
        <div className="callout-body">MSS access requires a provisioned account. Submit your request through your unit data steward or at <strong><a href="https://mss.data.mil" target="_blank" rel="noreferrer" style={{color:'var(--navy-mid)'}}>mss.data.mil</a></strong>. Provisioning generally completes within 24 hours; if access is not active after 24 hours, contact your data steward directly. Do not wait until the start of a deployment or exercise.</div>
      </div>

      {/* Specialist Tracks CTA */}
      <div className="specialist-cta">
        <div className="specialist-cta-text">
          <div className="specialist-cta-label">Advanced &amp; Technical Tracks</div>
          <div className="specialist-cta-title">Specialist Tracks &mdash; SL 4 &amp; SL 5 Series</div>
          <div className="specialist-cta-sub">Role-specific developer manuals for ORSA, AI Engineer, ML Engineer, Program Manager, Knowledge Manager, and Software Engineer. Prerequisite: SL 3 complete.</div>
        </div>
        <button className="specialist-cta-btn" onClick={() => showPanel('specialists')}>
          Access Specialist Tracks <span className="btn-arrow">&#8594;</span>
        </button>
      </div>

      <div className="callout info mt-24">
        <div className="callout-label">TRAIN THE TRAINER (T3) &mdash; INSTRUCTOR &amp; UDT PATHWAY</div>
        <div className="callout-body">
          Two courses sit <strong>outside</strong> the SL 1 to SL 5 chain:<br/><br/>
          <strong>T3-I (Instructor Certification):</strong> Prereq SL 3 + C2DAO selection. 5-day classroom + supervised practicum. Certifies MSS instructors (Instructor &rarr; Senior &rarr; Master).<br/>
          <strong>T3-F (MSC Force Multiplier):</strong> Prereq SL 2 + CDR nomination. 3 days. Trains Unit Data Trainers (UDTs) who deliver SL 1 locally at each MSC.<br/><br/>
          See <button className="qr-link" onClick={() => showPanel('documents')}>All Documents &rarr;</button> for T3 publications, syllabi, and SOPs.
        </div>
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
