interface Props {
  showPanel: (id: string) => void
}

export default function Schedule({ showPanel }: Props) {
  return (
    <>
      <div className="section-header">
        <div className="section-badge">SCHEDULE</div>
        <div className="section-title">Upcoming Training &mdash; SL 1 / SL 2 / SL 3</div>
        <div className="section-subtitle">Foundation courses &bull; Contact POC to enroll</div>
      </div>

      {/* ── SL 1 ── */}
      <div style={{marginBottom:36}}>
        <div style={{display:'flex',alignItems:'center',gap:12,padding:'11px 16px',background:'var(--navy)',borderLeft:'5px solid var(--gold-dark)',borderRadius:'3px 3px 0 0'}}>
          <span style={{fontFamily:'var(--font-ui)',fontSize:13,fontWeight:700,color:'var(--gold)',letterSpacing:.5,whiteSpace:'nowrap'}}>SL 1</span>
          <span style={{fontFamily:'var(--font-ui)',fontSize:13,fontWeight:700,color:'#FFFFFF'}}>Maven User Manual &mdash; All Personnel</span>
          <span style={{marginLeft:'auto',fontFamily:'var(--font-mono)',fontSize:10,color:'rgba(200,151,26,0.7)',whiteSpace:'nowrap'}}>1 day (8 hrs) &bull; No prereq</span>
        </div>
        <div className="table-wrap" style={{borderTop:'none',borderRadius:'0 0 3px 3px'}}>
          <table>
            <thead>
              <tr><th>Dates</th><th>Location</th><th>Format</th><th>POC</th><th>Seats Avail.</th><th>Status</th></tr>
            </thead>
            <tbody>
              <tr>
                <td>14 APR 2026</td>
                <td>Wiesbaden, Clay Kaserne, Bldg 3312, Rm 104</td>
                <td>In-Person</td><td>SSG Johnson</td><td>20 / 20</td>
                <td><span className="seat-open">Open</span></td>
              </tr>
              <tr>
                <td>05 MAY 2026</td>
                <td>Grafenw&ouml;hr, Bldg 244, Conf Rm B</td>
                <td>In-Person</td><td>SFC Davis</td><td>8 / 20</td>
                <td><span className="seat-low">8 Remaining</span></td>
              </tr>
              <tr>
                <td>18 JUN 2026</td>
                <td>Stuttgart, Kelley Bks, Bldg 3357</td>
                <td>In-Person</td><td>SSG Martinez</td><td>20 / 20</td>
                <td><span className="seat-open">Open</span></td>
              </tr>
              <tr>
                <td>09 JUL 2026</td>
                <td>Virtual (MS Teams)</td>
                <td>Virtual</td><td>SSG Johnson</td><td>30 / 30</td>
                <td><span className="seat-open">Open</span></td>
              </tr>
            </tbody>
          </table>
        </div>
        <div className="callout note" style={{marginTop:8,marginBottom:0}}>
          <div className="callout-label">Enrollment</div>
          <div className="callout-body">Contact listed POC to reserve a seat. Ensure your MSS account request is submitted at least 5 business days before course start. Virtual sessions require MS Teams access and a headset.</div>
        </div>
      </div>

      {/* ── SL 2 ── */}
      <div style={{marginBottom:36}}>
        <div style={{display:'flex',alignItems:'center',gap:12,padding:'11px 16px',background:'var(--navy)',borderLeft:'5px solid var(--gold-dark)',borderRadius:'3px 3px 0 0'}}>
          <span style={{fontFamily:'var(--font-ui)',fontSize:13,fontWeight:700,color:'var(--gold)',letterSpacing:.5,whiteSpace:'nowrap'}}>SL 2</span>
          <span style={{fontFamily:'var(--font-ui)',fontSize:13,fontWeight:700,color:'#FFFFFF'}}>No-Code Builder Manual &mdash; All Staff</span>
          <span style={{marginLeft:'auto',fontFamily:'var(--font-mono)',fontSize:10,color:'rgba(200,151,26,0.7)',whiteSpace:'nowrap'}}>5 days (40 hrs) &bull; Prereq: SL 1</span>
        </div>
        <div className="table-wrap" style={{borderTop:'none',borderRadius:'0 0 3px 3px'}}>
          <table>
            <thead>
              <tr><th>Dates</th><th>Location</th><th>Format</th><th>POC</th><th>Seats Avail.</th><th>Status</th></tr>
            </thead>
            <tbody>
              <tr>
                <td>21&ndash;25 APR 2026</td>
                <td>Wiesbaden, Clay Kaserne, Bldg 3312, Rm 104</td>
                <td>In-Person</td><td>SFC Chen</td><td>7 / 15</td>
                <td><span className="seat-low">7 Remaining</span></td>
              </tr>
              <tr>
                <td>11&ndash;15 MAY 2026</td>
                <td>Grafenw&ouml;hr, Bldg 244, Conf Rm B</td>
                <td>In-Person</td><td>SSG Williams</td><td>3 / 15</td>
                <td><span className="seat-low">3 Remaining</span></td>
              </tr>
              <tr>
                <td>22&ndash;26 JUN 2026</td>
                <td>Stuttgart, Kelley Bks, Bldg 3357</td>
                <td>In-Person</td><td>SFC Chen</td><td>15 / 15</td>
                <td><span className="seat-open">Open</span></td>
              </tr>
              <tr>
                <td>13&ndash;17 JUL 2026</td>
                <td>Virtual (MS Teams)</td>
                <td>Virtual</td><td>SSG Williams</td><td>20 / 20</td>
                <td><span className="seat-open">Open</span></td>
              </tr>
            </tbody>
          </table>
        </div>
        <div className="callout note" style={{marginTop:8,marginBottom:0}}>
          <div className="callout-label">Enrollment</div>
          <div className="callout-body">SL 1 must be complete before attending SL 2. Bring your SL 1 completion certificate on day one.</div>
        </div>
      </div>

      {/* ── SL 3 ── */}
      <div style={{marginBottom:36}}>
        <div style={{display:'flex',alignItems:'center',gap:12,padding:'11px 16px',background:'var(--navy)',borderLeft:'5px solid var(--gold-dark)',borderRadius:'3px 3px 0 0'}}>
          <span style={{fontFamily:'var(--font-ui)',fontSize:13,fontWeight:700,color:'var(--gold)',letterSpacing:.5,whiteSpace:'nowrap'}}>SL 3</span>
          <span style={{fontFamily:'var(--font-ui)',fontSize:13,fontWeight:700,color:'#FFFFFF'}}>Advanced Builder Manual &mdash; Data-Adjacent Specialists</span>
          <span style={{marginLeft:'auto',fontFamily:'var(--font-mono)',fontSize:10,color:'rgba(200,151,26,0.7)',whiteSpace:'nowrap'}}>5 days (40 hrs) &bull; Prereq: SL 1 + SL 2</span>
        </div>
        <div className="table-wrap" style={{borderTop:'none',borderRadius:'0 0 3px 3px'}}>
          <table>
            <thead>
              <tr><th>Dates</th><th>Location</th><th>Format</th><th>POC</th><th>Seats Avail.</th><th>Status</th></tr>
            </thead>
            <tbody>
              <tr>
                <td>28 APR &ndash; 02 MAY 2026</td>
                <td>Wiesbaden, Clay Kaserne, Bldg 3312, Rm 104</td>
                <td>In-Person</td><td>CW3 Thompson</td><td>4 / 10</td>
                <td><span className="seat-low">4 Remaining</span></td>
              </tr>
              <tr>
                <td>15&ndash;19 JUN 2026</td>
                <td>Virtual (MS Teams)</td>
                <td>Virtual</td><td>CW2 Rodriguez</td><td>15 / 15</td>
                <td><span className="seat-open">Open</span></td>
              </tr>
              <tr>
                <td>17&ndash;21 AUG 2026</td>
                <td>Wiesbaden, Clay Kaserne, Bldg 3312, Rm 104</td>
                <td>In-Person</td><td>CW3 Thompson</td><td>10 / 10</td>
                <td><span className="seat-open">Open</span></td>
              </tr>
            </tbody>
          </table>
        </div>
        <div className="callout note" style={{marginTop:8,marginBottom:0}}>
          <div className="callout-label">Enrollment</div>
          <div className="callout-body">SL 1 and SL 2 must be complete before attending SL 3. Class size is limited — contact POC early. Bring all prior completion certificates on day one.</div>
        </div>
      </div>

      {/* ── Footer note ── */}
      <div className="callout bluf">
        <div className="callout-label">Schedule Notes</div>
        <div className="callout-body">
          All dates subject to change. Confirm attendance with POC at least 5 business days prior.
          Courses run 0800&ndash;1700 each day. For Specialist Track (SL 4/5) scheduling,
          contact the USAREUR-AF Operational Data Team directly.
        </div>
      </div>

      <p style={{marginTop:14,fontFamily:'var(--font-mono)',fontSize:10,color:'var(--gray-400)',textAlign:'right'}}>
        Last updated: MAR 2026 &mdash; USAREUR-AF Operational Data Team
      </p>

      <div className="callout note mt-24">
        <div className="callout-label">Not finding what you need?</div>
        <div className="callout-body">
          Contact your unit data steward for enrollment assistance or specialist track scheduling.
          For technical support, visit the{' '}
          <button className="qr-link" onClick={() => showPanel('support')}>Support page &rarr;</button>
        </div>
      </div>
    </>
  )
}
