import React, { useState } from 'react'
import { URLS } from '../constants/urls'

interface Props {
  showPanel: (id: string) => void
}

// ── Find My Track data (merged from FindMyTrack.tsx) ─────────────────────────
interface TrackResult {
  label: string
  tm40: string
  tm40Panel: string
  tm50?: string
  description: string
  path: string[]
}

interface RoleOption {
  label: string
  description: string
  result: TrackResult
}

interface RoleCategory {
  id: string
  label: string
  icon: string
  description: string
  roles: RoleOption[]
}

const CATEGORIES: RoleCategory[] = [
  {
    id: 'consumer',
    label: 'Data Consumer',
    icon: '\u{1F4CA}',
    description: 'I use MSS dashboards, views, and reports to inform decisions.',
    roles: [
      {
        label: 'Any Soldier, officer, or Civilian using MSS to view data',
        description: 'You access MSS to consume operational data — dashboards, reports, filtered views.',
        result: { label: 'Maven User', tm40: 'SL 1', tm40Panel: 'sl1', description: 'SL 1 covers everything you need: CAC login, navigation, Workshop apps, data viewing, AI tools, and security.', path: ['SL 1'] },
      },
    ],
  },
  {
    id: 'builder',
    label: 'No-Code Builder',
    icon: '\u{1F6E0}',
    description: 'I build dashboards, forms, or pipelines without writing code.',
    roles: [
      {
        label: 'Staff officer / NCO building dashboards or forms',
        description: 'You create Workshop apps, simple pipelines, or forms for your section.',
        result: { label: 'Builder', tm40: 'SL 2', tm40Panel: 'sl2', description: 'SL 2 teaches Pipeline Builder (visual), Ontology Manager UI, and Workshop app creation — no code required.', path: ['SL 1', 'SL 2'] },
      },
    ],
  },
  {
    id: 'advanced',
    label: 'Advanced Builder',
    icon: '\u{1F9E9}',
    description: 'I design complex apps, manage ontology architecture, or enforce governance.',
    roles: [
      {
        label: 'Data-adjacent specialist (17/25-series, G2, data analyst)',
        description: 'You go beyond basic building — complex app design, Ontology architecture, governance, C2DAO standards.',
        result: { label: 'Advanced Builder', tm40: 'SL 3', tm40Panel: 'sl3', description: 'SL 3 covers complex app design, Ontology architecture, governance, and C2DAO standards.', path: ['SL 1', 'SL 2', 'SL 3'] },
      },
    ],
  },
  {
    id: 'wff',
    label: 'Warfighting Function',
    icon: '\u{1F396}',
    description: 'I\'m assigned to a specific WFF role — Intel, Fires, M&M, Sustainment, Protection, or Mission Command.',
    roles: [
      { label: 'G2/S2 — MI units, ISR analysts', description: 'Intelligence warfighting function — threat data, collection management, ISR dashboards.', result: { label: 'Intelligence', tm40: 'SL 4A', tm40Panel: 'specialists', description: 'WFF-specific MSS applications for intelligence operations — no coding required.', path: ['SL 1', 'SL 2', 'SL 3', 'SL 4A'] } },
      { label: 'FA officers/NCOs — Fire support coordinators', description: 'Fires warfighting function — targeting data, fire mission workflows.', result: { label: 'Fires', tm40: 'SL 4B', tm40Panel: 'specialists', description: 'WFF-specific MSS applications for fire support and targeting workflows.', path: ['SL 1', 'SL 2', 'SL 3', 'SL 4B'] } },
      { label: 'Maneuver units — G3/S3 data roles', description: 'Movement & Maneuver — operational movement tracking, maneuver data.', result: { label: 'Movement & Maneuver', tm40: 'SL 4C', tm40Panel: 'specialists', description: 'WFF-specific MSS applications for movement and maneuver operations.', path: ['SL 1', 'SL 2', 'SL 3', 'SL 4C'] } },
      { label: 'G4/S4 — Logistics, GCSS-A users', description: 'Sustainment — logistics pipelines, supply chain data, GCSS-A integration.', result: { label: 'Sustainment', tm40: 'SL 4D', tm40Panel: 'specialists', description: 'WFF-specific MSS applications for sustainment and logistics operations.', path: ['SL 1', 'SL 2', 'SL 3', 'SL 4D'] } },
      { label: 'Air defense, CBRN, engineer, force protection', description: 'Protection — force protection data, CBRN monitoring, engineer operations.', result: { label: 'Protection', tm40: 'SL 4E', tm40Panel: 'specialists', description: 'WFF-specific MSS applications for protection and force defense.', path: ['SL 1', 'SL 2', 'SL 3', 'SL 4E'] } },
      { label: 'G6/S6 — C2 systems, network managers', description: 'Mission Command — C2 data systems, network management, signal operations.', result: { label: 'Mission Command', tm40: 'SL 4F', tm40Panel: 'specialists', description: 'WFF-specific MSS applications for mission command and C2 systems.', path: ['SL 1', 'SL 2', 'SL 3', 'SL 4F'] } },
    ],
  },
  {
    id: 'technical',
    label: 'Technical Specialist',
    icon: '\u{1F4BB}',
    description: 'I build, engineer, or manage MSS solutions — ORSA, AI/ML, PM, KM, or SWE role.',
    roles: [
      { label: 'FA49 — Operations Research Analyst', description: 'ORSA — quantitative analysis, wargaming, optimization, statistical modeling.', result: { label: 'ORSA', tm40: 'SL 4G', tm40Panel: 'sl4', tm50: 'SL 5G', description: 'Quantitative analysis, optimization models, wargame data architecture on MSS.', path: ['SL 1', 'SL 2', 'SL 3', 'SL 4G'] } },
      { label: '17A/17C — AI/ML specialist or Cyber', description: 'AI Engineering — AIP Logic, Agent Studio, LLM integration, or cyber operations.', result: { label: 'AI Engineer', tm40: 'SL 4H', tm40Panel: 'sl4', tm50: 'SL 5H', description: 'AIP Logic workflows, Agent Studio, LLM integration, and AI red-teaming on MSS.', path: ['SL 1', 'SL 2', 'SL 3', 'SL 4H'] } },
      { label: 'ML engineer / Data scientist (GS/contractor)', description: 'ML Engineering — model training, deployment, MLOps, Code Workspaces.', result: { label: 'ML Engineer', tm40: 'SL 4M', tm40Panel: 'sl4', tm50: 'SL 5M', description: 'Model development, experiment tracking, deployment, and MLOps patterns on MSS.', path: ['SL 1', 'SL 2', 'SL 3', 'SL 4M'] } },
      { label: 'G8/S8 — Program Manager / Resource manager', description: 'Program Management — agile project management, backlogs, portfolio health.', result: { label: 'Program Manager', tm40: 'SL 4J', tm40Panel: 'sl4', tm50: 'SL 5J', description: 'Agile project structures, sprint management, and portfolio tracking on MSS.', path: ['SL 1', 'SL 2', 'SL 3', 'SL 4J'] } },
      { label: 'KMO / 37F — Knowledge Manager', description: 'Knowledge Management — AAR systems, lessons learned, doctrine repositories.', result: { label: 'Knowledge Manager', tm40: 'SL 4K', tm40Panel: 'sl4', tm50: 'SL 5K', description: 'AAR capture, lessons-learned pipelines, knowledge search, and doctrine management.', path: ['SL 1', 'SL 2', 'SL 3', 'SL 4K'] } },
      { label: '25D/25U — Software Engineer / IT specialist', description: 'Software Engineering — OSDK, TypeScript/Python, Foundry API, full-stack apps.', result: { label: 'Software Engineer', tm40: 'SL 4L', tm40Panel: 'sl4', tm50: 'SL 5L', description: 'OSDK development, Foundry API integration, full-stack MSS applications.', path: ['SL 1', 'SL 2', 'SL 3', 'SL 4L'] } },
      { label: 'G2/S2 quantitative analyst', description: 'Quant analysis — could be ORSA or KM depending on your unit role.', result: { label: 'ORSA or Knowledge Manager', tm40: 'SL 4G / SL 4K', tm40Panel: 'specialists', tm50: 'SL 5G / SL 5K', description: 'Talk to your supervisor — ORSA (SL 4G) for quantitative modeling or KM (SL 4K) for knowledge architecture.', path: ['SL 1', 'SL 2', 'SL 3', 'SL 4G or SL 4K'] } },
    ],
  },
  {
    id: 'leader',
    label: 'Senior Leader',
    icon: '\u{2B50}',
    description: 'I\'m O-5+ / SGM+ directing a data-capable formation.',
    roles: [
      {
        label: 'Commander / Senior leader (O-5+ / SGM+)',
        description: 'You direct data-capable formations. You need the strategic picture, not the hands-on tools.',
        result: { label: 'Senior Leader Executive Course', tm40: 'EXEC', tm40Panel: 'exec', description: '1-day executive course: principles, command responsibilities, and decision frameworks. Replaces SL 1 for O-5 / E-9+. No technical prerequisites.', path: ['EXEC'] },
      },
    ],
  },
]

// ── Component ─────────────────────────────────────────────────────────────────
export default function QuickRef({ showPanel }: Props) {
  const [tm40TableOpen, setTm40TableOpen] = useState(false)
  const [tm50TableOpen, setTm50TableOpen] = useState(false)

  // Find My Track state
  const [fmtOpen, setFmtOpen] = useState(false)
  const [selectedCategory, setSelectedCategory] = useState<string | null>(null)
  const [selectedRole, setSelectedRole] = useState<number | null>(null)

  const category = CATEGORIES.find(c => c.id === selectedCategory)
  const role = category && selectedRole !== null ? category.roles[selectedRole] : null
  const effectiveRole = category && category.roles.length === 1 ? category.roles[0] : role
  const effectiveResult = effectiveRole?.result

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

  function selectCategory(id: string) {
    setSelectedCategory(id)
    setSelectedRole(null)
    const cat = CATEGORIES.find(c => c.id === id)
    if (cat && cat.roles.length === 1) setSelectedRole(0)
    if (!fmtOpen) setFmtOpen(true)
  }

  function resetFmt() {
    setSelectedCategory(null)
    setSelectedRole(null)
  }

  return (
    <div onClick={closeDropdowns}>
      {/* Card header */}
      <div className="qr-header">
        <span className="section-badge">MSS TRAINING HUB</span>
        <span className="qr-title">MAVEN SMART SYSTEM &mdash; USAREUR-AF</span>
        <span className="section-subtitle">Version 3.0 &bull; March 2026</span>
      </div>

      <div className="callout info">
        <div className="callout-label">NEW TO MSS?</div>
        <div className="callout-body"><strong>Start with the Quick Start guide</strong> before reading the SL 1 manual. Operational in 30 minutes: log in via CAC, navigate to your unit&rsquo;s app, filter data, export a view. &rarr; <a href={URLS.QUICK_START} target="_blank" rel="noreferrer" style={{color:'var(--navy-mid)',fontWeight:700}}>QUICK_START.pdf</a> &nbsp;&bull;&nbsp; No account yet? Contact your unit data steward.</div>
      </div>

      <div className="callout bluf">
        <div className="callout-label">BLUF</div>
        <div className="callout-body">All personnel start at SL 1. Builders add SL 2; data-adjacent specialists continue to SL 3; technical roles select their SL 4 track. Use &ldquo;Find My Track&rdquo; below or browse the reference table.</div>
      </div>

      {/* Quick-nav button row */}
      <div className="qr-nav-row">
        <button className="qr-nav-btn" onClick={(e) => { e.stopPropagation(); showPanel('schedule') }}>Training Schedule</button>
        <button className="qr-nav-btn" onClick={(e) => { e.stopPropagation(); showPanel('specialists') }}>Specialist Tracks</button>
        <button className="qr-nav-btn" onClick={(e) => { e.stopPropagation(); showPanel('documents') }}>All Documents</button>
        <button className="qr-nav-btn" onClick={(e) => { e.stopPropagation(); showPanel('taskindex') }}>Task Index</button>
        <button className="qr-nav-btn" onClick={(e) => { e.stopPropagation(); showPanel('dashboards') }}>Dashboards</button>
        <button className="qr-nav-btn" onClick={(e) => { e.stopPropagation(); showPanel('support') }}>Support</button>
      </div>

      {/* ── FIND MY TRACK (inline, collapsible) ─────────────────── */}
      <div className="fmt-section">
        <button
          className={`fmt-toggle${fmtOpen ? ' open' : ''}`}
          onClick={(e) => { e.stopPropagation(); setFmtOpen(o => !o) }}
        >
          <span className="fmt-toggle-icon">&#9889;</span>
          <span className="fmt-toggle-text">Find My Track</span>
          <span className="fmt-toggle-sub">&mdash; answer two questions to get your personalized training path</span>
          <span className="fmt-toggle-arrow">{fmtOpen ? '\u25B2' : '\u25BC'}</span>
        </button>

        {fmtOpen && (
          <div className="fmt-wizard">
            {/* Step 1: Category */}
            <div className="fmt-step">
              <div className="fmt-step-label">
                <span className="fmt-step-num">1</span>
                What best describes your role?
              </div>
              <div className="fmt-categories">
                {CATEGORIES.map(cat => (
                  <button
                    key={cat.id}
                    className={`fmt-cat-btn${selectedCategory === cat.id ? ' active' : ''}`}
                    onClick={(e) => { e.stopPropagation(); selectCategory(cat.id) }}
                  >
                    <span className="fmt-cat-icon">{cat.icon}</span>
                    <span className="fmt-cat-label">{cat.label}</span>
                    <span className="fmt-cat-desc">{cat.description}</span>
                  </button>
                ))}
              </div>
            </div>

            {/* Step 2: Specific role (if category has multiple) */}
            {category && category.roles.length > 1 && (
              <div className="fmt-step">
                <div className="fmt-step-label">
                  <span className="fmt-step-num">2</span>
                  Which role matches you best?
                </div>
                <div className="fmt-roles">
                  {category.roles.map((r, i) => (
                    <button
                      key={i}
                      className={`fmt-role-btn${selectedRole === i ? ' active' : ''}`}
                      onClick={(e) => { e.stopPropagation(); setSelectedRole(i) }}
                    >
                      <span className="fmt-role-label">{r.label}</span>
                      <span className="fmt-role-desc">{r.description}</span>
                    </button>
                  ))}
                </div>
              </div>
            )}

            {/* Result */}
            {effectiveResult && (
              <div className="fmt-result">
                <div className="fmt-result-header">
                  <div className="fmt-result-badge">YOUR TRAINING PATH</div>
                  <div className="fmt-result-track">{effectiveResult.label}</div>
                  <div className="fmt-result-tm">{effectiveResult.tm40}{effectiveResult.tm50 ? ` \u2192 ${effectiveResult.tm50}` : ''}</div>
                </div>
                <div className="fmt-result-desc">{effectiveResult.description}</div>
                <div className="fmt-path">
                  {effectiveResult.path.map((step, i) => (
                    <span key={i} className="fmt-path-step">
                      {i > 0 && <span className="fmt-path-arrow">{'\u2192'}</span>}
                      <span className={`fmt-path-badge${i === effectiveResult.path.length - 1 ? ' final' : ''}`}>{step}</span>
                    </span>
                  ))}
                </div>
                <div className="fmt-result-actions">
                  <button className="fmt-go-btn" onClick={(e) => { e.stopPropagation(); showPanel(effectiveResult.tm40Panel) }}>
                    Go to {effectiveResult.tm40} {'\u2192'}
                  </button>
                  <button className="fmt-reset-btn" onClick={(e) => { e.stopPropagation(); resetFmt() }}>
                    Start Over
                  </button>
                </div>
              </div>
            )}
          </div>
        )}
      </div>

      {/* ── REFERENCE GRID ──────────────────────────────────────── */}
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
                  <td>TM-10 (SL 1) &mdash; Maven User</td>
                  <td><button className="qr-link" onClick={(e) => { e.stopPropagation(); showPanel('sl1') }}>SL 1 &rarr;</button></td>
                </tr>
                <tr>
                  <td>Staff building dashboards or simple pipelines (no coding)</td>
                  <td>TM-20 (SL 2) &mdash; Builder</td>
                  <td><button className="qr-link" onClick={(e) => { e.stopPropagation(); showPanel('sl2') }}>SL 2 &rarr;</button></td>
                </tr>
                <tr>
                  <td>Data steward, frequent builder, or data-adjacent role (17/25-series, G2, analyst)</td>
                  <td>TM-30 (SL 3) &mdash; Advanced Builder</td>
                  <td><button className="qr-link" onClick={(e) => { e.stopPropagation(); showPanel('sl3') }}>SL 3 &rarr;</button></td>
                </tr>
                <tr>
                  <td>Technical specialist or warfighting function developer &mdash; ORSA &bull; AI/ML Eng &bull; PM &bull; KM &bull; SWE</td>
                  <td>TM-40 (SL 4) Specialist Track</td>
                  <td>
                    <div className="qr-dropdown-wrap">
                      <button
                        className="qr-link qr-dropdown-btn"
                        aria-expanded={tm40TableOpen}
                        onClick={toggleTm40Table}
                      >SL 4 &#9662;</button>
                      {tm40TableOpen && (
                        <div className="qr-dropdown-menu open" id="dd-tm40-table">
                          <div className="qr-dropdown-section">Select Your Track</div>
                          <button className="qr-dropdown-item" onClick={(e) => { e.stopPropagation(); showPanel('sl4'); closeDropdowns() }}>SL 4G &mdash; ORSA</button>
                          <button className="qr-dropdown-item" onClick={(e) => { e.stopPropagation(); showPanel('sl4'); closeDropdowns() }}>SL 4H &mdash; AI Engineer</button>
                          <button className="qr-dropdown-item" onClick={(e) => { e.stopPropagation(); showPanel('sl4'); closeDropdowns() }}>SL 4M &mdash; ML Engineer</button>
                          <button className="qr-dropdown-item" onClick={(e) => { e.stopPropagation(); showPanel('sl4'); closeDropdowns() }}>SL 4J &mdash; Program Mgr</button>
                          <button className="qr-dropdown-item" onClick={(e) => { e.stopPropagation(); showPanel('sl4'); closeDropdowns() }}>SL 4K &mdash; Knowledge Mgr</button>
                          <button className="qr-dropdown-item" onClick={(e) => { e.stopPropagation(); showPanel('sl4'); closeDropdowns() }}>SL 4L &mdash; Software Eng</button>
                        </div>
                      )}
                    </div>
                  </td>
                </tr>
                <tr>
                  <td>Advanced specialist &mdash; post SL 4 completion</td>
                  <td>TM-50 (SL 5) Advanced Track</td>
                  <td>
                    <div className="qr-dropdown-wrap">
                      <button
                        className="qr-link qr-dropdown-btn"
                        aria-expanded={tm50TableOpen}
                        onClick={toggleTm50Table}
                      >SL 5 &#9662;</button>
                      {tm50TableOpen && (
                        <div className="qr-dropdown-menu open" id="dd-tm50-table">
                          <div className="qr-dropdown-section">Select Your Track</div>
                          <button className="qr-dropdown-item" onClick={(e) => { e.stopPropagation(); showPanel('sl5'); closeDropdowns() }}>SL 5G &mdash; ORSA Advanced</button>
                          <button className="qr-dropdown-item" onClick={(e) => { e.stopPropagation(); showPanel('sl5'); closeDropdowns() }}>SL 5H &mdash; AI Engineer Advanced</button>
                          <button className="qr-dropdown-item" onClick={(e) => { e.stopPropagation(); showPanel('sl5'); closeDropdowns() }}>SL 5M &mdash; ML Engineer Advanced</button>
                          <button className="qr-dropdown-item" onClick={(e) => { e.stopPropagation(); showPanel('sl5'); closeDropdowns() }}>SL 5J &mdash; Program Mgr Advanced</button>
                          <button className="qr-dropdown-item" onClick={(e) => { e.stopPropagation(); showPanel('sl5'); closeDropdowns() }}>SL 5K &mdash; Knowledge Mgr Advanced</button>
                          <button className="qr-dropdown-item" onClick={(e) => { e.stopPropagation(); showPanel('sl5'); closeDropdowns() }}>SL 5L &mdash; Software Eng Advanced</button>
                        </div>
                      )}
                    </div>
                  </td>
                </tr>
                <tr>
                  <td>O-5 / SGM+ &mdash; directing a data-capable formation</td>
                  <td>EXEC &mdash; Senior Leader Exec Course</td>
                  <td><button className="qr-link" onClick={(e) => { e.stopPropagation(); showPanel('exec') }}>EXEC &rarr;</button></td>
                </tr>
                <tr>
                  <td>All personnel &mdash; foundational data concepts before SL 1</td>
                  <td>Data Literacy Technical Reference</td>
                  <td><a className="qr-link" href={URLS.DATA_LITERACY_TECH} target="_blank" rel="noreferrer">PDF &rarr;</a></td>
                </tr>
                <tr>
                  <td>Anyone &mdash; unfamiliar term or concept</td>
                  <td>Glossary &mdash; Data &amp; Foundry</td>
                  <td><button className="qr-link" onClick={(e) => { e.stopPropagation(); showPanel('doctrine') }}>Draft Pubs &rarr;</button></td>
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
            <div className="qr-broken-item"><strong>App won&rsquo;t load</strong><br/>Hard-refresh (Ctrl+Shift+R). Clear cache. Try a different browser. Still broken &rarr; <button className="qr-link" onClick={(e) => { e.stopPropagation(); showPanel('support') }}>Help Desk &rarr;</button></div>
            <div className="qr-broken-item"><strong>Button greyed out / no access</strong><br/>You&rsquo;re missing a role or write permission. Contact your data steward to request the correct access level.</div>
          </div>
          <div style={{marginTop:'12px',paddingTop:'10px',borderTop:'1px solid var(--border)',display:'grid',gridTemplateColumns:'repeat(3,1fr)',gap:'8px',fontSize:'11px',color:'var(--text-body)'}}>
            <div><strong style={{display:'block',marginBottom:'2px',textTransform:'uppercase',letterSpacing:'.05em',fontSize:'10px'}}>Data Steward</strong>Account access &bull; data issues &bull; permission requests</div>
            <div><strong style={{display:'block',marginBottom:'2px',textTransform:'uppercase',letterSpacing:'.05em',fontSize:'10px'}}>Help Desk</strong>App broken &bull; won&rsquo;t load &bull; technical errors &rarr; <button className="qr-link" onClick={(e) => { e.stopPropagation(); showPanel('support') }}>Support &rarr;</button></div>
            <div><strong style={{display:'block',marginBottom:'2px',textTransform:'uppercase',letterSpacing:'.05em',fontSize:'10px'}}>ODT</strong>Training questions &bull; new app or pipeline requests</div>
          </div>
        </div>

      </div>{/* /qr-grid */}

      {/* ── TRAINING PATH (from Home) ───────────────────────────── */}
      <h2 style={{marginTop:32}}>TRAINING PATH</h2>

      {/* Data Literacy: outside the main pipeline — dashed border callout */}
      <div style={{border:'2px dashed var(--gray-200)',borderRadius:'6px',padding:'14px 16px 10px',marginBottom:'16px',background:'var(--off-white)'}}>
        <div style={{fontFamily:'var(--font-ui)',fontSize:'9px',fontWeight:700,letterSpacing:'2px',textTransform:'uppercase',color:'var(--gray-400)',marginBottom:'10px'}}>OUTSIDE THE PIPELINE &mdash; BACKGROUND READING (NOT REQUIRED BEFORE SL 1, BUT RECOMMENDED)</div>
        <div className="path-flow" style={{marginBottom:0}}>
          <div className="path-step">
            <div className="path-connector">
              <div className="path-dot optional" style={{fontSize:'10px',width:'34px',height:'34px'}}>SL</div>
              <div className="path-line dashed"></div>
            </div>
            <div className="path-content" style={{cursor:'pointer'}} onClick={() => showPanel('exec')}>
              <div className="path-tm">EXEC &mdash; SENIOR LEADER EXEC COURSE (O-5+ / SGM+)</div>
              <div className="path-name">Senior Leader Executive Course <span style={{fontSize:'11px',color:'var(--navy-mid)'}}>&#8594; TM-EXEC</span></div>
              <div className="path-audience">1-day course; replaces SL 1 for senior leaders; principles, command responsibilities, decision frameworks</div>
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
            <div className="path-audience"><strong>WFF Tracks (SL 4A&ndash;F):</strong> Intel &bull; Fires &bull; M&amp;M &bull; Sustainment &bull; Protection &bull; Mission Command<br/><strong>Technical Tracks (SL 4G&ndash;O):</strong> ORSA &bull; AI Eng &bull; MLE &bull; PM &bull; KM &bull; SWE &bull; UX &bull; Platform Eng &mdash; Advanced versions at SL 5G&ndash;O</div>
          </div>
        </div>
      </div>

      {/* Parallel Tracks — outside the main pipeline */}
      <div style={{border:'2px dashed var(--gray-200)',borderRadius:'6px',padding:'14px 16px 10px',marginTop:'16px',marginBottom:'16px',background:'var(--off-white)'}}>
        <div style={{fontFamily:'var(--font-ui)',fontSize:'9px',fontWeight:700,letterSpacing:'2px',textTransform:'uppercase',color:'var(--gray-400)',marginBottom:'10px'}}>PARALLEL TRACKS &mdash; OUTSIDE THE SL 1 &rarr; SL 5 PIPELINE</div>
        <div className="path-flow" style={{marginBottom:0}}>
          <div className="path-step">
            <div className="path-connector">
              <div className="path-dot optional" style={{fontSize:'9px',width:'34px',height:'34px'}}>SL</div>
              <div className="path-line dashed"></div>
            </div>
            <div className="path-content" style={{cursor:'pointer'}} onClick={() => showPanel('exec')}>
              <div className="path-tm">SENIOR LEADER EXECUTIVE COURSE &mdash; O-5+ / SGM+</div>
              <div className="path-name">Senior Leader Executive Course <span style={{fontSize:'11px',color:'var(--navy-mid)'}}>&#8594; TM-EXEC</span></div>
              <div className="path-audience">Directing and resourcing a data-capable formation; no technical prereqs</div>
            </div>
          </div>
          <div className="path-spacer"></div>
          <div className="path-step">
            <div className="path-connector">
              <div className="path-dot optional" style={{fontSize:'9px',width:'34px',height:'34px'}}>FBC</div>
              <div className="path-line dashed"></div>
            </div>
            <div className="path-content" style={{cursor:'pointer'}} onClick={() => showPanel('fbc')}>
              <div className="path-tm">FOUNDRY BOOTCAMP PROGRAM &mdash; PREREQ: SL 2</div>
              <div className="path-name">Foundry Bootcamp (FBC) <span style={{fontSize:'11px',color:'var(--navy-mid)'}}>&#8594; FBC</span></div>
              <div className="path-audience">Intensive hands-on sprint; parallel to SL 3, not a prereq for SL 4</div>
            </div>
          </div>
          <div className="path-spacer"></div>
          <div className="path-step">
            <div className="path-connector">
              <div className="path-dot optional" style={{fontSize:'9px',width:'34px',height:'34px'}}>T3-I</div>
              <div className="path-line dashed"></div>
            </div>
            <div className="path-content" style={{cursor:'pointer'}} onClick={() => showPanel('documents')}>
              <div className="path-tm">INSTRUCTOR CERTIFICATION &mdash; PREREQ: SL 3 + C2DAO SELECTION</div>
              <div className="path-name">T3-I Instructor Certification <span style={{fontSize:'11px',color:'var(--navy-mid)'}}>&#8594; Documents</span></div>
              <div className="path-audience">5-day classroom + practicum; certifies MSS instructors (Instructor &rarr; Senior &rarr; Master)</div>
            </div>
          </div>
          <div className="path-spacer"></div>
          <div className="path-step">
            <div className="path-connector">
              <div className="path-dot optional" style={{fontSize:'9px',width:'34px',height:'34px'}}>T3-F</div>
            </div>
            <div className="path-content" style={{cursor:'pointer'}} onClick={() => showPanel('documents')}>
              <div className="path-tm">MSC FORCE MULTIPLIER &mdash; PREREQ: SL 2 + CDR NOMINATION</div>
              <div className="path-name">T3-F Unit Data Trainer (UDT) <span style={{fontSize:'11px',color:'var(--navy-mid)'}}>&#8594; Documents</span></div>
              <div className="path-audience">Half day; trains UDTs who deliver SL 1 locally at each MSC</div>
            </div>
          </div>
        </div>
      </div>

      {/* Foundation CTA */}
      <div className="specialist-cta">
        <div className="specialist-cta-text">
          <div className="specialist-cta-label">Start Your Training</div>
          <div className="specialist-cta-title">Foundation &mdash; SL 1 &rarr; SL 2 &rarr; SL 3</div>
          <div className="specialist-cta-sub">All personnel begin here. SL 1 gets you operational; SL 2 builds no-code skills; SL 3 unlocks specialist tracks.</div>
        </div>
        <button className="specialist-cta-btn" onClick={(e) => { e.stopPropagation(); showPanel('sl1') }}>
          Start with SL 1 <span className="btn-arrow">&#8594;</span>
        </button>
      </div>

      <div className="callout info mt-24">
        <div className="callout-label">TRAIN THE TRAINER (T3) &mdash; INSTRUCTOR &amp; UDT PATHWAY</div>
        <div className="callout-body">
          Two courses sit <strong>outside</strong> the SL 1 to SL 5 chain:<br/><br/>
          <strong>T3-I (Instructor Certification):</strong> Prereq SL 3 + C2DAO selection. 5-day classroom + supervised practicum. Certifies MSS instructors (Instructor &rarr; Senior &rarr; Master).<br/>
          <strong>T3-F (MSC Force Multiplier):</strong> Prereq SL 2 + CDR nomination. Half day. Trains Unit Data Trainers (UDTs) who deliver SL 1 locally at each MSC.<br/><br/>
          See <button className="qr-link" onClick={(e) => { e.stopPropagation(); showPanel('documents') }}>All Documents &rarr;</button> for T3 publications, syllabi, and SOPs.
        </div>
      </div>

      <div className="callout note mt-24">
        <div className="callout-label">MSS ACCOUNT ACCESS</div>
        <div className="callout-body">MSS access requires a provisioned account. Submit your request through your unit data steward or at <strong><a href="https://mss.data.mil" target="_blank" rel="noreferrer" style={{color:'var(--navy-mid)'}}>mss.data.mil</a></strong>. Provisioning generally completes within 24 hours; if access is not active after 24 hours, contact your data steward directly.</div>
      </div>

      <div className="callout note mt-24">
        <div className="callout-label">NOT FINDING WHAT YOU NEED?</div>
        <div className="callout-body">
          Contact your unit data steward for additional publications, source files, or access to restricted materials.
          For technical support, visit the <button className="qr-link" onClick={(e) => { e.stopPropagation(); showPanel('support') }}>Support page &rarr;</button>
          For task-level procedures, use the <button className="qr-link" onClick={(e) => { e.stopPropagation(); showPanel('taskindex') }}>Task Index &rarr;</button>
        </div>
      </div>
    </div>
  )
}
