import { useState, useEffect, useRef, useCallback } from 'react'
import usareurSvg from './assets/USAREUR_Insignia.svg'

// Panel components — imported below
import PanelQuickRef from './panels/QuickRef'
import PanelTM10 from './panels/TM10'
import PanelTM20 from './panels/TM20'
import PanelTM30 from './panels/TM30'
import PanelSpecialists from './panels/Specialists'
import PanelTM40 from './panels/TM40'
import PanelTM50 from './panels/TM50'
import PanelDoctrine from './panels/Doctrine'
import PanelDocuments from './panels/Documents'
import PanelTaskIndex from './panels/TaskIndex'
import PanelSupport from './panels/Support'
import PanelSchedule from './panels/Schedule'
import PanelDashboards from './panels/Dashboards'
import PanelFBC from './panels/FBC'
import PanelSL from './panels/SL'
import PanelFindMyTrack from './panels/FindMyTrack'

type PanelId =
  | 'quickref' | 'schedule' | 'dashboards' | 'findmytrack'
  | 'tm10' | 'tm20' | 'tm30' | 'fbc' | 'sl'
  | 'specialists' | 'tm40' | 'tm50'
  | 'doctrine' | 'documents' | 'taskindex' | 'support'

// ── Star Field ────────────────────────────────────────────────────────────────
function useStarField(canvasRef: React.RefObject<HTMLCanvasElement | null>) {
  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return
    const ctx = canvas.getContext('2d')!
    if (!ctx) return

    type Star = {
      x: number; y: number; r: number; base: number; alpha: number
      phase: number; speed: number; color: string; glow: boolean
    }

    let stars: Star[] = []
    let W = 0, H = 0, raf = 0

    function resize() {
      W = canvas!.width  = canvas!.offsetWidth
      H = canvas!.height = canvas!.offsetHeight
    }

    function mkStar(): Star {
      const tier = Math.random()
      const r = tier < 0.15 ? (1.6 + Math.random() * 1.0)
              : tier < 0.50 ? (0.9 + Math.random() * 0.7)
              :               (0.3 + Math.random() * 0.5)
      const hue = 200 + Math.floor(Math.random() * 20)
      const sat = 30  + Math.floor(Math.random() * 30)
      return {
        x: Math.random() * W, y: Math.random() * H,
        r, base: 0.15 + Math.random() * 0.65, alpha: 0,
        phase: Math.random() * Math.PI * 2,
        speed: 0.0004 + Math.random() * 0.0014,
        color: `hsl(${hue},${sat}%,90%)`,
        glow: r > 1.4,
      }
    }

    function buildStars(n: number) {
      stars = []
      for (let i = 0; i < n; i++) stars.push(mkStar())
    }

    function draw(ts: number) {
      ctx.clearRect(0, 0, W, H)
      for (const s of stars) {
        s.alpha = s.base + Math.sin(s.phase + ts * s.speed) * (s.base * 0.55)
        ctx.globalAlpha = Math.max(0, Math.min(1, s.alpha))
        if (s.glow) {
          const grad = ctx.createRadialGradient(s.x, s.y, 0, s.x, s.y, s.r * 5)
          grad.addColorStop(0, s.color)
          grad.addColorStop(1, 'transparent')
          ctx.globalAlpha = s.alpha * 0.25
          ctx.beginPath(); ctx.arc(s.x, s.y, s.r * 5, 0, Math.PI * 2)
          ctx.fillStyle = grad; ctx.fill()
          ctx.globalAlpha = Math.max(0, Math.min(1, s.alpha))
        }
        ctx.beginPath(); ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2)
        ctx.fillStyle = s.color; ctx.fill()
      }
      ctx.globalAlpha = 1
      raf = requestAnimationFrame(draw)
    }

    function onResize() {
      cancelAnimationFrame(raf)
      resize(); buildStars(260)
      raf = requestAnimationFrame(draw)
    }

    window.addEventListener('resize', onResize)
    resize(); buildStars(260); raf = requestAnimationFrame(draw)

    return () => {
      window.removeEventListener('resize', onResize)
      cancelAnimationFrame(raf)
    }
  }, [canvasRef])
}

// ── App ───────────────────────────────────────────────────────────────────────
export default function App() {
  const [splashVisible, setSplashVisible] = useState(true)
  const [splashFading, setSplashFading]   = useState(false)
  const [activePanel, setActivePanel]     = useState<PanelId>('quickref')
  const [sidebarCollapsed, setSidebarCollapsed] = useState(false)
  const [mobileSidebarOpen, setMobileSidebarOpen] = useState(false)
  const [grpFoundationOpen, setGrpFoundationOpen] = useState(true)
  const [grpFbcOpen, setGrpFbcOpen] = useState(false)
  const [grpSlOpen, setGrpSlOpen] = useState(false)
  const [grpSpecialistsOpen, setGrpSpecialistsOpen] = useState(false)
  const [grpResourcesOpen, setGrpResourcesOpen] = useState(false)

  const canvasRef  = useRef<HTMLCanvasElement>(null)
  const contentRef = useRef<HTMLDivElement>(null)

  useStarField(canvasRef)

  const showPanel = useCallback((id: string) => {
    setActivePanel(id as PanelId)
    setMobileSidebarOpen(false)
    contentRef.current?.scrollTo(0, 0)
    window.scrollTo(0, 0)
  }, [])

  function enterHub() {
    setSplashFading(true)
    showPanel('quickref')
    setTimeout(() => setSplashVisible(false), 720)
  }

  const panel = (id: PanelId) => (
    <div id={`panel-${id}`} className={`panel${activePanel === id ? ' active' : ''}`}>
      {activePanel === id && getPanelContent(id)}
    </div>
  )

  function getPanelContent(id: PanelId) {
    switch (id) {
      case 'quickref':    return <PanelQuickRef    showPanel={showPanel} />
      case 'tm10':        return <PanelTM10         showPanel={showPanel} />
      case 'tm20':        return <PanelTM20         showPanel={showPanel} />
      case 'tm30':        return <PanelTM30         showPanel={showPanel} />
      case 'fbc':         return <PanelFBC          showPanel={showPanel} />
      case 'sl':          return <PanelSL           showPanel={showPanel} />
      case 'specialists': return <PanelSpecialists  showPanel={showPanel} />
      case 'tm40':        return <PanelTM40         showPanel={showPanel} />
      case 'tm50':        return <PanelTM50         showPanel={showPanel} />
      case 'doctrine':    return <PanelDoctrine     showPanel={showPanel} />
      case 'documents':   return <PanelDocuments    showPanel={showPanel} />
      case 'taskindex':   return <PanelTaskIndex    showPanel={showPanel} />
      case 'support':      return <PanelSupport      showPanel={showPanel} />
      case 'schedule':     return <PanelSchedule     showPanel={showPanel} />
      case 'dashboards':   return <PanelDashboards />
      case 'findmytrack':  return <PanelFindMyTrack showPanel={showPanel} />
    }
  }

  function navItem(id: PanelId, label: string, icon = '◾') {
    return (
      <button
        className={`snav-item${activePanel === id ? ' active' : ''}`}
        onClick={() => showPanel(id)}
      >
        <span className="snav-item-icon">{icon}</span>
        <span className="snav-item-label">{label}</span>
      </button>
    )
  }

  return (
    <>
      {/* ── Splash ─────────────────────────────────────────── */}
      {splashVisible && (
        <div id="splash" className={splashFading ? 'fade-out' : ''}>
          <canvas id="starCanvas" ref={canvasRef} />
          <div className="splash-glow" />
          <div className="splash-scanline" />
          <div className="hud-frame">
            <div className="hud-bl" />
            <div className="hud-br" />
          </div>
          <div className="splash-data splash-data-tl">USAREUR-AF ODT<br/>EUCOM AOR</div>
          <div className="splash-data splash-data-tr">VER 3.1 / MAR 2026<br/>MSS TRAINING HUB</div>
          <div className="splash-data splash-data-bl">DIST: UNLIMITED</div>
          <div className="splash-data splash-data-br">TM-10 THRU TM-50<br/>Data Lit (SL) · Data Literacy</div>
          <div className="splash-body">
            <div className="splash-content">
              <div className="splash-crest-wrap">
                <img className="splash-crest" src={usareurSvg} alt="USAREUR-AF Insignia" />
              </div>
              <div className="splash-eyebrow">Operational Data Team</div>
              <div className="splash-hq">Headquarters &bull; United States Army Europe and Africa</div>
              <div className="splash-rule" />
              <div className="splash-title">Maven Smart System</div>
              <div className="splash-sub">Training &amp; Information Hub</div>
              <div style={{marginTop:6,fontSize:10,letterSpacing:'.14em',color:'rgba(255,180,0,0.55)',textTransform:'uppercase'}}>alpha</div>
              <div className="splash-tms">
                TM-10 &nbsp;&middot;&nbsp; TM-20 &nbsp;&middot;&nbsp; TM-30 &nbsp;&middot;&nbsp;
                TM-40A&ndash;O &nbsp;&middot;&nbsp; TM-50G&ndash;O &nbsp;&middot;&nbsp; Data Lit (SL) &nbsp;&middot;&nbsp; Data Literacy
              </div>
              <div className="splash-rule-sm" />
              <button className="splash-enter" onClick={enterHub}>
                <div className="splash-enter-glow" />
                <div className="splash-enter-inner">
                  <span className="splash-enter-text">Access Training Hub</span>
                  <span className="splash-enter-arrow">&#8594;</span>
                </div>
              </button>
              <div className="splash-meta">
                Version 3.1 &mdash; March 2026<br/>
                DRAFT &mdash; Not yet approved for distribution
              </div>
            </div>
          </div>
          <div className="splash-statusbar">
            <span>SYS: MSS TRAINING HUB</span>
            <span>VER: 3.1.0</span>
            <span>LOC: EUCOM AOR</span>
            <span>STATUS: READY</span>
          </div>
        </div>
      )}

      {/* ── Header ─────────────────────────────────────────── */}
      <header>
        <div className="header-inner">
          <button
            className="header-hamburger"
            aria-label="Open navigation"
            onClick={() => setMobileSidebarOpen(true)}
          >&#9776;</button>
          <img className="crest" src={usareurSvg} alt="USAREUR-AF Insignia" />
          <div className="header-text">
            <div className="header-command">Headquarters &bull; United States Army Europe and Africa</div>
            <div className="header-title">Maven Smart System</div>
            <div className="header-subtitle">Training &amp; Information Hub &nbsp;&mdash;&nbsp; USAREUR-AF Operational Data Team</div>
          </div>
          <div className="header-meta">
            <div className="badge">MSS TRAINING HUB</div><br/>
            VERSION 3.1 &mdash; MARCH 2026<br/>
            DIST: UNLIMITED
          </div>
        </div>
      </header>

      <div className="header-strip">
        <div className="header-strip-inner">
          <span>TM-10 &bull; TM-20 &bull; TM-30 &bull; TM-40A&ndash;O &bull; TM-50G&ndash;O &bull; Data Lit (SL) &bull; Data Literacy</span>
          <span>DRAFT &mdash; NOT YET APPROVED FOR DISTRIBUTION &nbsp;&bull;&nbsp; alpha</span>
        </div>
      </div>

      {/* ── App shell ──────────────────────────────────────── */}
      <div className="app-shell">

        {/* Mobile overlay */}
        <div
          className={`sidebar-overlay${mobileSidebarOpen ? ' visible' : ''}`}
          onClick={() => setMobileSidebarOpen(false)}
        />

        {/* Sidebar */}
        <nav className={`sidebar${sidebarCollapsed ? ' collapsed' : ''}${mobileSidebarOpen ? ' mobile-open' : ''}`}>
          <div className="sidebar-top">
            <button
              className="sidebar-toggle-btn"
              aria-label="Toggle sidebar"
              onClick={() => setSidebarCollapsed(c => !c)}
            >&#8249;</button>
          </div>

          <div className="sidebar-nav">
            {/* Quick Reference pinned */}
            <button
              className={`snav-pinned${activePanel === 'quickref' ? ' active' : ''}`}
              onClick={() => showPanel('quickref')}
            >
              <span className="snav-pinned-icon">&#9636;</span>
              <span className="snav-pinned-label">Quick Reference</span>
            </button>

            <button
              className={`snav-item${activePanel === 'schedule' ? ' active' : ''}`}
              style={{borderLeft:'3px solid var(--gold-dark)',paddingLeft:11,marginTop:2}}
              onClick={() => showPanel('schedule')}
            >
              <span className="snav-item-icon" style={{color:'var(--gold)'}}>&#128197;</span>
              <span className="snav-item-label" style={{color:'var(--gold-light)'}}>Training Schedule</span>
            </button>

            <div className="snav-divider" />

            {/* Foundation group */}
            <div className={`snav-group${grpFoundationOpen ? '' : ' collapsed'}`}>
              <button
                className="snav-group-hdr"
                style={{color:'var(--gold-light)',fontWeight:700}}
                onClick={() => setGrpFoundationOpen(o => !o)}
              >
                Foundation TMs
                <span className="snav-group-arrow">&#8964;</span>
              </button>
              <div className="snav-group-items">
                {navItem('tm10', 'TM-10 — Maven User', '◾')}
                {navItem('tm20', 'TM-20 — Builder', '◾')}
                {navItem('tm30', 'TM-30 — Advanced Builder', '◾')}
              </div>
            </div>

            {/* Foundry Bootcamp (FBC) group */}
            <div className={`snav-group${grpFbcOpen ? '' : ' collapsed'}`}>
              <button
                className="snav-group-hdr"
                style={{color:'rgba(200,151,26,0.75)'}}
                onClick={() => setGrpFbcOpen(o => !o)}
              >
                Foundry Bootcamp (FBC)
                <span className="snav-group-arrow">&#8964;</span>
              </button>
              <div className="snav-group-items">
                {navItem('fbc', 'Foundry Bootcamp — Overview', '◾')}
              </div>
            </div>

            {/* Senior Leader (TM-SL) group */}
            <div className={`snav-group${grpSlOpen ? '' : ' collapsed'}`}>
              <button
                className="snav-group-hdr"
                style={{color:'rgba(200,151,26,0.75)'}}
                onClick={() => setGrpSlOpen(o => !o)}
              >
                Senior Leader (TM-SL)
                <span className="snav-group-arrow">&#8964;</span>
              </button>
              <div className="snav-group-items">
                {navItem('sl', 'Exec Course — Overview', '◾')}
              </div>
            </div>

            {/* Specialist tracks group */}
            <div className={`snav-group${grpSpecialistsOpen ? '' : ' collapsed'}`}>
              <button
                className="snav-group-hdr"
                style={{color:'rgba(200,151,26,0.5)'}}
                onClick={() => setGrpSpecialistsOpen(o => !o)}
              >
                Specialist Tracks
                <span className="snav-group-arrow">&#8964;</span>
              </button>
              <div className="snav-group-items">
                {navItem('specialists', 'Track Overview', '◾')}
                {navItem('tm40', 'TM-40 Specialist', '◾')}
                {navItem('tm50', 'TM-50 Advanced', '◾')}
              </div>
            </div>

            {/* Resources group */}
            <div className={`snav-group${grpResourcesOpen ? '' : ' collapsed'}`}>
              <button
                className="snav-group-hdr"
                onClick={() => setGrpResourcesOpen(o => !o)}
              >
                Resources
                <span className="snav-group-arrow">&#8964;</span>
              </button>
              <div className="snav-group-items">
                {navItem('doctrine', 'Doctrine / Data Lit', '◾')}
                {navItem('documents', 'All Documents', '◾')}
                {navItem('taskindex', 'Task Index', '◾')}
                {navItem('dashboards', 'Dashboards', '◾')}
                <a href="../DEPENDENCY_MAP.html" target="_blank" rel="noopener" className="snav-item" title="Corpus dependency map (admin tool)">&#9881; Dependency Map</a>
                {navItem('support', 'Support', '◾')}
              </div>
            </div>

            {/* Train the Trainer (T3) — greyed out placeholder */}
            <div className="snav-group collapsed" style={{opacity:0.4,pointerEvents:'none'}}>
              <button
                className="snav-group-hdr"
                style={{color:'var(--gray-400)',cursor:'default'}}
              >
                Train the Trainer (T3)
                <span style={{fontSize:9,marginLeft:6,color:'var(--gray-400)'}}>COMING SOON</span>
              </button>
              <div className="snav-group-items">
                <button className="snav-item" disabled style={{cursor:'default'}}>
                  <span className="snav-item-icon">&#9642;</span>
                  <span className="snav-item-label">T3-I &mdash; Instructor Cert</span>
                </button>
                <button className="snav-item" disabled style={{cursor:'default'}}>
                  <span className="snav-item-icon">&#9642;</span>
                  <span className="snav-item-label">T3-F &mdash; Force Multiplier</span>
                </button>
              </div>
            </div>
          </div>
        </nav>

        {/* Content area */}
        <div className="content-area" ref={contentRef}>
          <main>
            {panel('quickref')}
            {panel('schedule')}
            {panel('tm10')}
            {panel('tm20')}
            {panel('tm30')}
            {panel('fbc')}
            {panel('sl')}
            {panel('specialists')}
            {panel('tm40')}
            {panel('tm50')}
            {panel('doctrine')}
            {panel('documents')}
            {panel('taskindex')}
            {panel('dashboards')}
            {panel('findmytrack')}
            {panel('support')}
          </main>

          <footer>
            <strong>USAREUR-AF Operational Data Team</strong><br/>
            Maven Smart System Training Hub &mdash; Version 3.1 &mdash; March 2026<br/>
            DRAFT &mdash; Not yet approved for distribution &bull; DIST: UNLIMITED
          </footer>

        </div>
      </div>
    </>
  )
}
