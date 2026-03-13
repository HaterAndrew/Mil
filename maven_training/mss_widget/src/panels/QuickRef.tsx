import React, { useState } from 'react'
import { URLS } from '../constants/urls'

interface Props {
  showPanel: (id: string) => void
}

export default function QuickRef({ showPanel }: Props) {
  const [tm40TableOpen, setTm40TableOpen] = useState(false)
  const [tm50TableOpen, setTm50TableOpen] = useState(false)

  function toggleTm40Table(e: React.MouseEvent) {
    e.stopPropagation()
    setTm40TableOpen(prev => !prev)
    setTm50TableOpen(false)
  }

  function toggleTm50Table(e: React.MouseEvent) {
    e.stopPropagation()
    setTm50TableOpen(prev => !prev)
    setTm40TableOpen(false)
  }

  function closeDropdowns() {
    setTm40TableOpen(false)
    setTm50TableOpen(false)
  }

  return (
    <div onClick={closeDropdowns}>
      {/* Card header */}
      <div className="qr-header">
        <span className="section-badge">QUICK REF</span>
        <span className="qr-title">MAVEN SMART SYSTEM &mdash; QUICK REFERENCE CARD</span>
      </div>

      <div className="callout info">
        <div className="callout-label">NEW TO MSS?</div>
        <div className="callout-body"><strong>Start with the Quick Start guide</strong> before reading TM-10. Operational in 30 minutes: log in via CAC, navigate to your unit&rsquo;s app, filter data, export a view. &rarr; <a href={URLS.QUICK_START} target="_blank" rel="noreferrer" style={{color:'var(--navy-mid)',fontWeight:700}}>QUICK_START.pdf</a> &nbsp;&bull;&nbsp; No account yet? Contact your unit data steward.</div>
      </div>

      <div className="callout bluf">
        <div className="callout-label">BLUF</div>
        <div className="callout-body">All personnel start at TM-10. Builders add TM-20; data-adjacent specialists continue to TM-30; technical roles select their TM-40 track below.</div>
      </div>

      <div className="qr-grid">

        {/* FIND YOUR MANUAL — full width */}
        <div className="qr-box gold-top qr-span3">
          <div className="qr-label">Find Your Manual</div>
          <div className="table-wrap">
            <table>
              <thead><tr><th>You Are&hellip;</th><th>Start Here</th><th>Open It</th></tr></thead>
              <tbody>
                <tr>
                  <td>Any personnel &mdash; viewing data for the first time</td>
                  <td>TM-10 &mdash; Maven User</td>
                  <td><button className="qr-link" onClick={(e) => { e.stopPropagation(); showPanel('tm10' as any) }}>TM-10 &rarr;</button></td>
                </tr>
                <tr>
                  <td>Staff building dashboards or simple pipelines (no coding)</td>
                  <td>TM-20 &mdash; Builder</td>
                  <td><button className="qr-link" onClick={(e) => { e.stopPropagation(); showPanel('tm20' as any) }}>TM-20 &rarr;</button></td>
                </tr>
                <tr>
                  <td>Data steward, frequent builder, or data-adjacent role (17/25-series, G2, analyst)</td>
                  <td>TM-30 &mdash; Advanced Builder</td>
                  <td><button className="qr-link" onClick={(e) => { e.stopPropagation(); showPanel('tm30' as any) }}>TM-30 &rarr;</button></td>
                </tr>
                <tr>
                  <td>Technical specialist or warfighting function developer &mdash; ORSA &bull; AI/ML Eng &bull; PM &bull; KM &bull; SWE</td>
                  <td>TM-40 Specialist Track</td>
                  <td>
                    <div className="qr-dropdown-wrap">
                      <button
                        className="qr-link qr-dropdown-btn"
                        aria-expanded={tm40TableOpen}
                        onClick={toggleTm40Table}
                      >TM-40 &#9662;</button>
                      {tm40TableOpen && (
                        <div className="qr-dropdown-menu open" id="dd-tm40-table">
                          <div className="qr-dropdown-section">Select Your Track</div>
                          <button className="qr-dropdown-item" onClick={(e) => { e.stopPropagation(); showPanel('tm40' as any); closeDropdowns() }}>TM-40G &mdash; ORSA</button>
                          <button className="qr-dropdown-item" onClick={(e) => { e.stopPropagation(); showPanel('tm40' as any); closeDropdowns() }}>TM-40H &mdash; AI Engineer</button>
                          <button className="qr-dropdown-item" onClick={(e) => { e.stopPropagation(); showPanel('tm40' as any); closeDropdowns() }}>TM-40I &mdash; ML Engineer</button>
                          <button className="qr-dropdown-item" onClick={(e) => { e.stopPropagation(); showPanel('tm40' as any); closeDropdowns() }}>TM-40J &mdash; Program Mgr</button>
                          <button className="qr-dropdown-item" onClick={(e) => { e.stopPropagation(); showPanel('tm40' as any); closeDropdowns() }}>TM-40K &mdash; Knowledge Mgr</button>
                          <button className="qr-dropdown-item" onClick={(e) => { e.stopPropagation(); showPanel('tm40' as any); closeDropdowns() }}>TM-40L &mdash; Software Eng</button>
                        </div>
                      )}
                    </div>
                  </td>
                </tr>
                <tr>
                  <td>Advanced specialist &mdash; post TM-40 completion</td>
                  <td>TM-50 Advanced Track</td>
                  <td>
                    <div className="qr-dropdown-wrap">
                      <button
                        className="qr-link qr-dropdown-btn"
                        aria-expanded={tm50TableOpen}
                        onClick={toggleTm50Table}
                      >TM-50 &#9662;</button>
                      {tm50TableOpen && (
                        <div className="qr-dropdown-menu open" id="dd-tm50-table">
                          <div className="qr-dropdown-section">Select Your Track</div>
                          <button className="qr-dropdown-item" onClick={(e) => { e.stopPropagation(); showPanel('tm50' as any); closeDropdowns() }}>TM-50G &mdash; ORSA Advanced</button>
                          <button className="qr-dropdown-item" onClick={(e) => { e.stopPropagation(); showPanel('tm50' as any); closeDropdowns() }}>TM-50H &mdash; AI Engineer Advanced</button>
                          <button className="qr-dropdown-item" onClick={(e) => { e.stopPropagation(); showPanel('tm50' as any); closeDropdowns() }}>TM-50I &mdash; ML Engineer Advanced</button>
                          <button className="qr-dropdown-item" onClick={(e) => { e.stopPropagation(); showPanel('tm50' as any); closeDropdowns() }}>TM-50J &mdash; Program Mgr Advanced</button>
                          <button className="qr-dropdown-item" onClick={(e) => { e.stopPropagation(); showPanel('tm50' as any); closeDropdowns() }}>TM-50K &mdash; Knowledge Mgr Advanced</button>
                          <button className="qr-dropdown-item" onClick={(e) => { e.stopPropagation(); showPanel('tm50' as any); closeDropdowns() }}>TM-50L &mdash; Software Eng Advanced</button>
                        </div>
                      )}
                    </div>
                  </td>
                </tr>
                <tr>
                  <td>O-5 / SGM+ &mdash; directing a data-capable formation</td>
                  <td>Data Literacy for Senior Leaders</td>
                  <td><button className="qr-link" onClick={(e) => { e.stopPropagation(); showPanel('doctrine' as any) }}>Draft Pubs &rarr;</button></td>
                </tr>
                <tr>
                  <td>All personnel &mdash; foundational data concepts before TM-10</td>
                  <td>Data Literacy Technical Reference</td>
                  <td><a className="qr-link" href={URLS.DATA_LITERACY_TECH} target="_blank" rel="noreferrer">PDF &rarr;</a></td>
                </tr>
                <tr>
                  <td>Anyone &mdash; unfamiliar term or concept</td>
                  <td>Glossary &mdash; Data &amp; Foundry</td>
                  <td><button className="qr-link" onClick={(e) => { e.stopPropagation(); showPanel('doctrine' as any) }}>Draft Pubs &rarr;</button></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        {/* COMMON DAILY TASKS — 1 col */}
        <div className="qr-box">
          <div className="qr-label">Common Daily Tasks</div>
          <div className="table-wrap">
            <table>
              <thead><tr><th>Task</th><th>How</th></tr></thead>
              <tbody>
                <tr><td>Find a record</td><td>Search bar or Filter Panel</td></tr>
                <tr><td>Filter the view</td><td>Select values in the Filter Panel</td></tr>
                <tr><td>Export data</td><td><strong>Export</strong> / <strong>Download</strong> button &rarr; CSV or Excel</td></tr>
                <tr><td>Submit or update a record</td><td>Click record &rarr; <strong>Action button</strong> &rarr; fill in &rarr; Submit</td></tr>
              </tbody>
            </table>
          </div>
        </div>

        {/* SECURITY — 2 cols */}
        <div className="qr-box red-top qr-span2">
          <div className="qr-label">Security &mdash; Do Not</div>
          <ul>
            <li>Do <strong>not</strong> export data to a personal device or unapproved storage</li>
            <li>Do <strong>not</strong> share your MSS <strong>credentials</strong> with anyone &mdash; URLs and screenshots are fine unless data is sensitive</li>
            <li>Do <strong>not</strong> enter classified information into MSS unless your instance is approved for that classification level</li>
            <li>Do <strong>not</strong> screenshot or share MSS screens containing data above your network&rsquo;s approved classification</li>
            <li>Do <strong>not</strong> use MSS on public or unsecured Wi-Fi</li>
            <li>If you see data you should not have access to &mdash; <strong>stop and report to your data steward immediately</strong></li>
          </ul>
        </div>

        {/* TROUBLESHOOTING + CONTACTS — full width */}
        <div className="qr-box teal-top qr-span3">
          <div className="qr-label">When It Breaks</div>
          <div className="qr-broken-grid">
            <div className="qr-broken-item"><strong>Can&rsquo;t log in</strong><br/>Check CAC is fully inserted; try a different port. No account? Request at <a href="https://mss.data.mil" target="_blank" rel="noreferrer" style={{color:'var(--navy-mid)',fontWeight:600}}>mss.data.mil</a> or through your data steward. Provisioning generally within 24 hrs; if not active after 24 hrs, contact your data steward.</div>
            <div className="qr-broken-item"><strong>App won&rsquo;t load</strong><br/>Hard-refresh (Ctrl+Shift+R). Clear cache. Try a different browser. Still broken &rarr; <button className="qr-link" onClick={(e) => { e.stopPropagation(); showPanel('support' as any) }}>Help Desk &rarr;</button></div>
            <div className="qr-broken-item"><strong>Button greyed out / no access</strong><br/>You&rsquo;re missing a role or write permission. Contact your data steward to request the correct access level.</div>
          </div>
          <div style={{marginTop:'12px',paddingTop:'10px',borderTop:'1px solid var(--border)',display:'grid',gridTemplateColumns:'repeat(3,1fr)',gap:'8px',fontSize:'11px',color:'var(--text-body)'}}>
            <div><strong style={{display:'block',marginBottom:'2px',textTransform:'uppercase',letterSpacing:'.05em',fontSize:'10px'}}>Data Steward</strong>Account access &bull; data issues &bull; permission requests</div>
            <div><strong style={{display:'block',marginBottom:'2px',textTransform:'uppercase',letterSpacing:'.05em',fontSize:'10px'}}>Help Desk</strong>App broken &bull; won&rsquo;t load &bull; technical errors &rarr; <button className="qr-link" onClick={(e) => { e.stopPropagation(); showPanel('support' as any) }}>Support &rarr;</button></div>
            <div><strong style={{display:'block',marginBottom:'2px',textTransform:'uppercase',letterSpacing:'.05em',fontSize:'10px'}}>ODT</strong>Training questions &bull; new app or pipeline requests</div>
          </div>
        </div>

      </div>{/* /qr-grid */}

      {/* Flow to Home */}
      <div className="specialist-cta" style={{marginTop:'32px'}}>
        <div className="specialist-cta-text">
          <div className="specialist-cta-label">Done with Quick Reference?</div>
          <div className="specialist-cta-title">Go to Home / Start Here</div>
          <div className="specialist-cta-sub">Find your training level, follow the full path, and navigate to your TM using the Home page overview.</div>
        </div>
        <button className="specialist-cta-btn" onClick={(e) => { e.stopPropagation(); showPanel('home' as any) }}>
          Home / Start Here <span className="btn-arrow">&#8594;</span>
        </button>
      </div>

      <div className="callout note mt-24">
        <div className="callout-label">NOT FINDING WHAT YOU NEED?</div>
        <div className="callout-body">
          Contact your unit data steward for additional publications, source files, or access to restricted materials.
          For technical support, visit the <button className="qr-link" onClick={(e) => { e.stopPropagation(); showPanel('support' as any) }}>Support page &rarr;</button>
          For task-level procedures, use the <button className="qr-link" onClick={(e) => { e.stopPropagation(); showPanel('taskindex' as any) }}>Task Index &rarr;</button>
        </div>
      </div>
    </div>
  )
}
