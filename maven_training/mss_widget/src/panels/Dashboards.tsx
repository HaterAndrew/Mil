import { useCallback, useMemo, useRef, useState } from 'react'

interface DashApp {
  name: string
  icon: string
  port: number
  description: string
}

interface DashSection {
  label: string
  apps: DashApp[]
}

const LAUNCHER_URL = 'http://localhost:8400'

const SECTIONS: DashSection[] = [
  {
    label: 'Training Analytics',
    apps: [
      { name: 'Readiness Tracker',  icon: '\u{1F4CB}', port: 8501, description: 'Soldier training timelines, overdue flagging, printable records.' },
      { name: 'Exam Analytics',     icon: '\u{1F4CA}', port: 8502, description: 'Score distributions, cohort comparison, item discrimination, question improvement.' },
      { name: 'AAR Aggregator',     icon: '\u{1F4DD}', port: 8503, description: 'AAR trend analysis, priority matrix, keyword extraction, GO/NO-GO tracking.' },
      { name: 'Training Metrics',   icon: '\u{1F4C8}', port: 8511, description: 'Executive dashboard — aggregates all training data for CG/DCG briefings.' },
    ],
  },
  {
    label: 'Training Operations',
    apps: [
      { name: 'Progress Tracker',     icon: '\u{1F3AF}', port: 8504, description: 'Individual soldier progress, goal tracking, stalled-soldier alerts.' },
      { name: 'MTT Scheduler',        icon: '\u{1F4C5}', port: 8505, description: 'Mobile Training Team scheduling, resource allocation, calendar view.' },
      { name: 'Enrollment Manager',   icon: '\u{1F464}', port: 8508, description: 'Class enrollment, waitlists, rosters, and seat management.' },
      { name: 'Instructor Manager',   icon: '\u{1F9D1}', port: 8512, description: 'Instructor assignments, certifications, and availability tracking.' },
    ],
  },
  {
    label: 'Content & Quality',
    apps: [
      { name: 'Data Quality',        icon: '\u{2705}', port: 8510, description: 'Pipeline health monitoring, metric trending, active alerts.' },
      { name: 'XRef Validator',       icon: '\u{1F517}', port: 8506, description: 'Cross-reference validation — find broken links and stale references.' },
      { name: 'Curriculum Tracker',   icon: '\u{1F4DA}', port: 8513, description: 'Document version control, review cycles, freshness tracking.' },
      { name: 'Glossary Search',      icon: '\u{1F50D}', port: 8507, description: 'Full-text search across the MSS data foundry glossary.' },
      { name: 'Lessons Learned',      icon: '\u{1F4A1}', port: 8514, description: 'Lessons learned database — search, tag, and trend analysis.' },
    ],
  },
  {
    label: 'Distribution & Sync',
    apps: [
      { name: 'Offline Packager',    icon: '\u{1F4E6}', port: 8509, description: 'Build offline content packages for disconnected environments.' },
      { name: 'SharePoint Sync',     icon: '\u{2601}',  port: 8515, description: 'Sync training content to SharePoint for enterprise distribution.' },
    ],
  },
]

function getDashHost(): string {
  const host = window.location.hostname
  const proto = window.location.protocol
  const isLocal = proto === 'file:' || host === '' || host === 'localhost' || host === '127.0.0.1' ||
    /^10\./.test(host) || /^192\.168\./.test(host) ||
    /^172\.(1[6-9]|2\d|3[01])\./.test(host)
  if (isLocal && host && host !== 'localhost') return host
  return 'localhost'
}

function useIsLocal(): boolean {
  return useMemo(() => {
    const host = window.location.hostname
    const proto = window.location.protocol
    return proto === 'file:' || host === '' || host === 'localhost' || host === '127.0.0.1' ||
      /^10\./.test(host) || /^192\.168\./.test(host) ||
      /^172\.(1[6-9]|2\d|3[01])\./.test(host)
  }, [])
}

export default function Dashboards() {
  const isLocal = useIsLocal()
  const [activeApp, setActiveApp] = useState<DashApp | null>(null)
  const [loading, setLoading] = useState(false)
  const [iframeSrc, setIframeSrc] = useState('about:blank')
  const viewerRef = useRef<HTMLDivElement>(null)
  const dashHost = getDashHost()

  const openApp = useCallback((app: DashApp) => {
    setActiveApp(app)
    setLoading(true)
    setIframeSrc('about:blank')
    setTimeout(() => viewerRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' }), 50)

    const url = `http://${dashHost}:${app.port}`

    fetch(`${LAUNCHER_URL}/start`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ port: app.port }),
    })
      .then(() => {
        setTimeout(() => { setLoading(false); setIframeSrc(url) }, 2000)
      })
      .catch(() => {
        setLoading(false)
        setIframeSrc(url)
      })
  }, [dashHost])

  function closeViewer() {
    setActiveApp(null)
    setLoading(false)
    setIframeSrc('about:blank')
  }

  return (
    <>
      <div className="section-header">
        <span className="section-badge">DASHBOARDS</span>
        <span className="section-title">Analytics &amp; Operations Suite</span>
        <span className="section-subtitle">Streamlit applications &bull; Click any card to open</span>
      </div>

      <div className="callout bluf">
        <div className="callout-label">BLUF</div>
        <div className="callout-body">These dashboards provide real-time analytics, operational management, and content quality tools for the MSS training program. Click any card below to load the application. On the ODT local network, apps load live. On Cloudflare, apps require VPN to the ODT network.</div>
      </div>

      {!isLocal && (
        <div className="dash-remote-banner visible">
          <strong>Remote access:</strong> Dashboard apps run on the ODT local network. Connect to VPN before opening a dashboard.
        </div>
      )}

      {activeApp && (
        <div className="dash-viewer visible" ref={viewerRef}>
          <div className="dash-viewer-toolbar">
            <span className="dash-viewer-title">{activeApp.name}</span>
            <span className="dash-viewer-port">:{activeApp.port}</span>
            <a className="dash-viewer-open" href={`http://${dashHost}:${activeApp.port}`} target="_blank" rel="noopener">Open in new tab</a>
            <button className="dash-viewer-close" onClick={closeViewer}>Close</button>
          </div>
          {loading && (
            <div className="dash-viewer-loading">
              <div className="dash-loading-spinner" />
              <p>Starting application...</p>
            </div>
          )}
          {!loading && <iframe src={iframeSrc} style={{ width: '100%', height: 700, border: 'none' }} />}
        </div>
      )}

      {SECTIONS.map(section => (
        <div key={section.label}>
          <div className="dash-section-hdr">{section.label}</div>
          <div className="dash-grid">
            {section.apps.map(app => (
              <div
                key={app.name}
                className={`dash-card${activeApp?.port === app.port ? ' active' : ''}`}
                onClick={() => openApp(app)}
              >
                <div className="dash-card-hdr">
                  <span className="dash-card-icon">{app.icon}</span>
                  <span className="dash-card-name">{app.name}</span>
                  <span className="dash-card-port">:{app.port}</span>
                </div>
                <div className="dash-card-desc">{app.description}</div>
              </div>
            ))}
          </div>
        </div>
      ))}

      <div className="callout note mt-24">
        <div className="callout-label">ACCESS</div>
        <div className="callout-body">
          Dashboards run on the ODT local network. To access remotely, connect via VPN first. Each application is available at <code>http://&lt;host&gt;:&lt;port&gt;</code>. Contact your ODT representative for the current host address.
        </div>
      </div>
    </>
  )
}
