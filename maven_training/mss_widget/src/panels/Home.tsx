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
        <span className="section-subtitle">Version 3.0 &bull; March 2026</span>
      </div>

      <div className="callout info">
        <div className="callout-label">NEW TO MSS?</div>
        <div className="callout-body"><strong>Start with the Quick Start guide</strong> before reading TM-10. It gets you operational in 30 minutes: log in, navigate, filter data, and export a view. &rarr; <a href={URLS.QUICK_START} target="_blank" rel="noreferrer" style={{color:'var(--navy)',fontWeight:700}}>QUICK_START.pdf</a></div>
      </div>

      <div className="callout bluf">
        <div className="callout-label">BLUF</div>
        <div className="callout-body">Find your level below and follow the training path. All personnel start at TM-10. Builders add TM-20. Data specialists continue to TM-30. Technical roles proceed to the appropriate TM-40 track. Use the sidebar to navigate to your specific guidance.</div>
      </div>

      <h2>STEP 1 &mdash; FIND YOUR LEVEL</h2>
      <div className="table-wrap">
        <table>
          <thead>
            <tr><th>You Are&hellip;</th><th>Start Here</th><th>Then</th><th>Tab</th></tr>
          </thead>
          <tbody>
            <tr>
              <td>Any Soldier, officer, or civilian &mdash; using MSS to access and consume data</td>
              <td><strong><button className="qr-link" onClick={() => showPanel('tm10' as any)}>TM-10 (User)</button></strong></td>
              <td>&mdash;</td>
              <td><span className="chip chip-navy" style={{cursor:'pointer'}} onClick={() => showPanel('tm10' as any)}>TM-10</span></td>
            </tr>
            <tr>
              <td>All staff &mdash; building dashboards, forms, or pipelines without coding</td>
              <td><strong><button className="qr-link" onClick={() => showPanel('tm10' as any)}>TM-10</button></strong></td>
              <td><button className="qr-link" onClick={() => showPanel('tm20' as any)}>TM-20 (Builder)</button></td>
              <td><span className="chip chip-navy" style={{cursor:'pointer'}} onClick={() => showPanel('tm20' as any)}>TM-20</span></td>
            </tr>
            <tr>
              <td>Data-adjacent specialist &mdash; 17/25-series, G2, data analyst</td>
              <td><strong><button className="qr-link" onClick={() => showPanel('tm10' as any)}>TM-10</button> &rarr; <button className="qr-link" onClick={() => showPanel('tm20' as any)}>TM-20</button></strong></td>
              <td><button className="qr-link" onClick={() => showPanel('tm30' as any)}>TM-30 (Advanced)</button></td>
              <td><span className="chip chip-gold" style={{cursor:'pointer'}} onClick={() => showPanel('tm30' as any)}>TM-30</span></td>
            </tr>
            <tr>
              <td>Technical specialist &mdash; ORSA, AI/ML, MLE, PM, KM, SWE roles (TM-40G&ndash;L)</td>
              <td><strong><button className="qr-link" onClick={() => showPanel('tm10' as any)}>TM-10</button> &rarr; <button className="qr-link" onClick={() => showPanel('tm20' as any)}>TM-20</button> &rarr; <button className="qr-link" onClick={() => showPanel('tm30' as any)}>TM-30</button></strong></td>
              <td><button className="qr-link" onClick={() => showPanel('tm40' as any)}>TM-40 specialist track</button></td>
              <td><span className="chip chip-gold" style={{cursor:'pointer'}} onClick={() => showPanel('specialists' as any)}>TM-40</span></td>
            </tr>
            <tr>
              <td>WFF specialist &mdash; assigned Intel, Fires, M&amp;M, Sustainment, Protection, or Mission Command role (TM-40A&ndash;F)</td>
              <td><strong><button className="qr-link" onClick={() => showPanel('tm10' as any)}>TM-10</button> &rarr; <button className="qr-link" onClick={() => showPanel('tm20' as any)}>TM-20</button> &rarr; <button className="qr-link" onClick={() => showPanel('tm30' as any)}>TM-30</button></strong></td>
              <td><button className="qr-link" onClick={() => showPanel('specialists' as any)}>TM-40 WFF track</button></td>
              <td><span className="chip chip-gold" style={{cursor:'pointer'}} onClick={() => showPanel('specialists' as any)}>TM-40</span></td>
            </tr>
            <tr>
              <td>Senior leader (O-5+ / SGM+) directing a data-capable formation</td>
              <td><strong><button className="qr-link" onClick={() => showPanel('doctrine' as any)}>Data Literacy (SL)</button></strong></td>
              <td>Optional: Data Literacy</td>
              <td><span className="chip chip-gray" style={{cursor:'pointer'}} onClick={() => showPanel('doctrine' as any)}>DRAFT PUBS</span></td>
            </tr>
            <tr>
              <td>Anyone wanting data literacy background before touching MSS</td>
              <td><strong><button className="qr-link" onClick={() => showPanel('doctrine' as any)}>Data Literacy</button></strong></td>
              <td>TM-10</td>
              <td><span className="chip chip-gray" style={{cursor:'pointer'}} onClick={() => showPanel('doctrine' as any)}>DRAFT PUBS</span></td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>STEP 2 &mdash; FOLLOW THE TRAINING PATH</h2>

      {/* Data Literacy: outside the main pipeline — dashed border callout */}
      <div style={{border:'2px dashed var(--gray-200)',borderRadius:'6px',padding:'14px 16px 10px',marginBottom:'16px',background:'var(--off-white)'}}>
        <div style={{fontFamily:'var(--font-ui)',fontSize:'9px',fontWeight:700,letterSpacing:'2px',textTransform:'uppercase',color:'var(--gray-400)',marginBottom:'10px'}}>OUTSIDE THE PIPELINE &mdash; BACKGROUND READING (NOT REQUIRED BEFORE TM-10, BUT RECOMMENDED)</div>
        <div className="path-flow" style={{marginBottom:0}}>
          <div className="path-step">
            <div className="path-connector">
              <div className="path-dot optional" style={{fontSize:'10px',width:'34px',height:'34px'}}>SL</div>
              <div className="path-line dashed"></div>
            </div>
            <div className="path-content" style={{cursor:'pointer'}} onClick={() => showPanel('doctrine' as any)}>
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
            <div className="path-content" style={{cursor:'pointer'}} onClick={() => showPanel('doctrine' as any)}>
              <div className="path-tm">DATA LITERACY &mdash; RECOMMENDED (ALL PERSONNEL)</div>
              <div className="path-name">Data Literacy Reference <span style={{fontSize:'11px',color:'var(--navy-mid)'}}>&#8594; Draft Pubs</span></div>
              <div className="path-audience">Platform-agnostic data literacy; recommended before TM-10</div>
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
          <div className="path-content" style={{cursor:'pointer'}} onClick={() => showPanel('tm10' as any)}>
            <div className="path-tm">TM-10 &mdash; REQUIRED FOR ALL PERSONNEL</div>
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
          <div className="path-content" style={{cursor:'pointer'}} onClick={() => showPanel('tm20' as any)}>
            <div className="path-tm">TM-20 &mdash; ALL STAFF (NO-CODE BUILDER)</div>
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
          <div className="path-content" style={{cursor:'pointer'}} onClick={() => showPanel('tm30' as any)}>
            <div className="path-tm">TM-30 &mdash; DATA-ADJACENT SPECIALISTS</div>
            <div className="path-name">Advanced Builder Manual <span style={{fontSize:'11px',color:'var(--navy-mid)'}}>&#8594; TM-30</span></div>
            <div className="path-audience">Complex app design, Ontology architecture, governance, C2DAO standards</div>
          </div>
        </div>
        <div className="path-spacer"></div>

        <div className="path-step">
          <div className="path-connector">
            <div className="path-dot">4</div>
          </div>
          <div className="path-content" style={{cursor:'pointer'}} onClick={() => showPanel('specialists' as any)}>
            <div className="path-tm">TM-40 &mdash; TWO TRACK TYPES (BY ROLE)</div>
            <div className="path-name">Specialist &amp; Warfighting Function Tracks <span style={{fontSize:'11px',color:'var(--navy-mid)'}}>&#8594; Specialist Tracks</span></div>
            <div className="path-audience"><strong>WFF Tracks (TM-40A&ndash;F):</strong> Intel &bull; Fires &bull; M&amp;M &bull; Sustainment &bull; Protection &bull; Mission Command<br/><strong>Technical Tracks (TM-40G&ndash;L):</strong> ORSA &bull; AI Eng &bull; MLE &bull; PM &bull; KM &bull; SWE &mdash; Advanced versions at TM-50G&ndash;L</div>
          </div>
        </div>
      </div>

      <div className="callout info">
        <div className="callout-label">TM-40 TRACK SELECTION &mdash; BY MOS / ROLE</div>
        <div className="callout-body">
          <strong style={{display:'block',marginBottom:'4px'}}>Warfighting Function Tracks (TM-40A&ndash;F):</strong>
          <strong>Intelligence (TM-40A):</strong> G2/S2, MI units, ISR analysts<br/>
          <strong>Fires (TM-40B):</strong> FA officers/NCOs, fire support coordinators<br/>
          <strong>Movement &amp; Maneuver (TM-40C):</strong> Maneuver units, G3/S3 data roles<br/>
          <strong>Sustainment (TM-40D):</strong> Logistics, G4/S4, GCSS-A users<br/>
          <strong>Protection (TM-40E):</strong> Air defense, CBRN, engineer, force protection<br/>
          <strong>Mission Command (TM-40F):</strong> G6/S6, C2 systems, network managers<br/><br/>
          <strong style={{display:'block',marginBottom:'4px'}}>Technical Specialist Tracks (TM-40G&ndash;L):</strong>
          <strong>ORSA (TM-40G):</strong> FA49, G2/S2 quant analysts, wargame specialists<br/>
          <strong>AI Engineer (TM-40H):</strong> AI/ML specialists, 17A/17C<br/>
          <strong>ML Engineer (TM-40I):</strong> ML engineers, data scientists (GS/contractor)<br/>
          <strong>Program Manager (TM-40J):</strong> G8/S8, PMs, resource managers<br/>
          <strong>Knowledge Manager (TM-40K):</strong> KMOs, 37F, institutional memory leads<br/>
          <strong>Software Engineer (TM-40L):</strong> 17A/17C, 25D/25U, GS/contractor SWEs<br/><br/>
          <em>Not listed? Ask your commander &mdash; you may be assigned a track based on unit needs.</em><br/>
          Full mapping: <button className="qr-link" onClick={() => showPanel('specialists' as any)}>Specialist Tracks &rarr;</button>
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
          <div className="specialist-cta-title">Specialist Tracks &mdash; TM-40 &amp; TM-50 Series</div>
          <div className="specialist-cta-sub">Role-specific developer manuals for ORSA, AI Engineer, ML Engineer, Program Manager, Knowledge Manager, and Software Engineer. Prerequisite: TM-30 complete.</div>
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
