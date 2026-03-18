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

export default function Dashboards() {
  return (
    <>
      <div className="section-header">
        <span className="section-badge">DASHBOARDS</span>
        <span className="section-title">Analytics &amp; Operations Suite</span>
        <span className="section-subtitle">Streamlit applications &bull; Accessible on local network</span>
      </div>

      <div className="callout bluf">
        <div className="callout-label">BLUF</div>
        <div className="callout-body">These dashboards provide real-time analytics, operational management, and content quality tools for the MSS training program. Each runs as a standalone Streamlit application accessible on the local network. Contact ODT for access credentials and network configuration.</div>
      </div>

      {SECTIONS.map(section => (
        <div key={section.label}>
          <div className="dash-section-hdr">{section.label}</div>
          <div className="dash-grid">
            {section.apps.map(app => (
              <div key={app.name} className="dash-card">
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
