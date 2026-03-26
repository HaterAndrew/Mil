import { useState } from 'react'

interface Props {
  showPanel: (id: string) => void
}

// ── Role → Track mapping data ──────────────────────────────────────────────
interface TrackResult {
  label: string
  tm40: string
  tm40Panel: string
  tm50?: string
  description: string
  path: string[]      // ordered TM steps to reach this track
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
        result: {
          label: 'Maven User',
          tm40: 'SL 1',
          tm40Panel: 'sl1',
          description: 'SL 1 covers everything you need: CAC login, navigation, Workshop apps, data viewing, AI tools, and security.',
          path: ['SL 1'],
        },
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
        result: {
          label: 'Builder',
          tm40: 'SL 2',
          tm40Panel: 'sl2',
          description: 'SL 2 teaches Pipeline Builder (visual), Ontology Manager UI, and Workshop app creation — no code required.',
          path: ['SL 1', 'SL 2'],
        },
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
        result: {
          label: 'Advanced Builder',
          tm40: 'SL 3',
          tm40Panel: 'sl3',
          description: 'SL 3 covers complex app design, Ontology architecture, governance, and C2DAO standards.',
          path: ['SL 1', 'SL 2', 'SL 3'],
        },
      },
    ],
  },
  {
    id: 'wff',
    label: 'Warfighting Function',
    icon: '\u{1F396}',
    description: 'I\'m assigned to a specific WFF role — Intel, Fires, M&M, Sustainment, Protection, or Mission Command.',
    roles: [
      {
        label: 'G2/S2 — MI units, ISR analysts',
        description: 'Intelligence warfighting function — threat data, collection management, ISR dashboards.',
        result: { label: 'Intelligence', tm40: 'SL 4A', tm40Panel: 'specialists', description: 'WFF-specific MSS applications for intelligence operations — no coding required.', path: ['SL 1', 'SL 2', 'SL 3', 'SL 4A'] },
      },
      {
        label: 'FA officers/NCOs — Fire support coordinators',
        description: 'Fires warfighting function — targeting data, fire mission workflows.',
        result: { label: 'Fires', tm40: 'SL 4B', tm40Panel: 'specialists', description: 'WFF-specific MSS applications for fire support and targeting workflows.', path: ['SL 1', 'SL 2', 'SL 3', 'SL 4B'] },
      },
      {
        label: 'Maneuver units — G3/S3 data roles',
        description: 'Movement & Maneuver — operational movement tracking, maneuver data.',
        result: { label: 'Movement & Maneuver', tm40: 'SL 4C', tm40Panel: 'specialists', description: 'WFF-specific MSS applications for movement and maneuver operations.', path: ['SL 1', 'SL 2', 'SL 3', 'SL 4C'] },
      },
      {
        label: 'G4/S4 — Logistics, GCSS-A users',
        description: 'Sustainment — logistics pipelines, supply chain data, GCSS-A integration.',
        result: { label: 'Sustainment', tm40: 'SL 4D', tm40Panel: 'specialists', description: 'WFF-specific MSS applications for sustainment and logistics operations.', path: ['SL 1', 'SL 2', 'SL 3', 'SL 4D'] },
      },
      {
        label: 'Air defense, CBRN, engineer, force protection',
        description: 'Protection — force protection data, CBRN monitoring, engineer operations.',
        result: { label: 'Protection', tm40: 'SL 4E', tm40Panel: 'specialists', description: 'WFF-specific MSS applications for protection and force defense.', path: ['SL 1', 'SL 2', 'SL 3', 'SL 4E'] },
      },
      {
        label: 'G6/S6 — C2 systems, network managers',
        description: 'Mission Command — C2 data systems, network management, signal operations.',
        result: { label: 'Mission Command', tm40: 'SL 4F', tm40Panel: 'specialists', description: 'WFF-specific MSS applications for mission command and C2 systems.', path: ['SL 1', 'SL 2', 'SL 3', 'SL 4F'] },
      },
    ],
  },
  {
    id: 'technical',
    label: 'Technical Specialist',
    icon: '\u{1F4BB}',
    description: 'I build, engineer, or manage MSS solutions — ORSA, AI/ML, PM, KM, or SWE role.',
    roles: [
      {
        label: 'FA49 — Operations Research Analyst',
        description: 'ORSA — quantitative analysis, wargaming, optimization, statistical modeling.',
        result: { label: 'ORSA', tm40: 'SL 4G', tm40Panel: 'sl4', tm50: 'SL 5G', description: 'Quantitative analysis, optimization models, wargame data architecture on MSS.', path: ['SL 1', 'SL 2', 'SL 3', 'SL 4G'] },
      },
      {
        label: '17A/17C — AI/ML specialist or Cyber',
        description: 'AI Engineering — AIP Logic, Agent Studio, LLM integration, or cyber operations.',
        result: { label: 'AI Engineer', tm40: 'SL 4H', tm40Panel: 'sl4', tm50: 'SL 5H', description: 'AIP Logic workflows, Agent Studio, LLM integration, and AI red-teaming on MSS.', path: ['SL 1', 'SL 2', 'SL 3', 'SL 4H'] },
      },
      {
        label: 'ML engineer / Data scientist (GS/contractor)',
        description: 'ML Engineering — model training, deployment, MLOps, Code Workspaces.',
        result: { label: 'ML Engineer', tm40: 'SL 4M', tm40Panel: 'sl4', tm50: 'SL 5M', description: 'Model development, experiment tracking, deployment, and MLOps patterns on MSS.', path: ['SL 1', 'SL 2', 'SL 3', 'SL 4M'] },
      },
      {
        label: 'G8/S8 — Program Manager / Resource manager',
        description: 'Program Management — agile project management, backlogs, portfolio health.',
        result: { label: 'Program Manager', tm40: 'SL 4J', tm40Panel: 'sl4', tm50: 'SL 5J', description: 'Agile project structures, sprint management, and portfolio tracking on MSS.', path: ['SL 1', 'SL 2', 'SL 3', 'SL 4J'] },
      },
      {
        label: 'KMO / 37F — Knowledge Manager',
        description: 'Knowledge Management — AAR systems, lessons learned, doctrine repositories.',
        result: { label: 'Knowledge Manager', tm40: 'SL 4K', tm40Panel: 'sl4', tm50: 'SL 5K', description: 'AAR capture, lessons-learned pipelines, knowledge search, and doctrine management.', path: ['SL 1', 'SL 2', 'SL 3', 'SL 4K'] },
      },
      {
        label: '25D/25U — Software Engineer / IT specialist',
        description: 'Software Engineering — OSDK, TypeScript/Python, Foundry API, full-stack apps.',
        result: { label: 'Software Engineer', tm40: 'SL 4L', tm40Panel: 'sl4', tm50: 'SL 5L', description: 'OSDK development, Foundry API integration, full-stack MSS applications.', path: ['SL 1', 'SL 2', 'SL 3', 'SL 4L'] },
      },
      {
        label: 'G2/S2 quantitative analyst',
        description: 'Quant analysis — could be ORSA or KM depending on your unit role.',
        result: { label: 'ORSA or Knowledge Manager', tm40: 'SL 4G / SL 4K', tm40Panel: 'specialists', tm50: 'SL 5G / SL 5K', description: 'Talk to your supervisor — ORSA (SL 4G) for quantitative modeling or KM (SL 4K) for knowledge architecture.', path: ['SL 1', 'SL 2', 'SL 3', 'SL 4G or SL 4K'] },
      },
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
        result: {
          label: 'Senior Leader Executive Course',
          tm40: 'EXEC',
          tm40Panel: 'exec',
          description: '1-day executive course: principles, command responsibilities, and decision frameworks. Replaces SL 1 for O-5 / E-9+. No technical prerequisites.',
          path: ['EXEC'],
        },
      },
    ],
  },
]

// ── Component ──────────────────────────────────────────────────────────────
export default function FindMyTrack({ showPanel }: Props) {
  const [selectedCategory, setSelectedCategory] = useState<string | null>(null)
  const [selectedRole, setSelectedRole] = useState<number | null>(null)

  const category = CATEGORIES.find(c => c.id === selectedCategory)
  const role = category && selectedRole !== null ? category.roles[selectedRole] : null

  // If category has only one role, auto-select it
  const effectiveRole = category && category.roles.length === 1 ? category.roles[0] : role
  const effectiveResult = effectiveRole?.result

  function reset() {
    setSelectedCategory(null)
    setSelectedRole(null)
  }

  function selectCategory(id: string) {
    setSelectedCategory(id)
    setSelectedRole(null)
    // Auto-select if only one role in category
    const cat = CATEGORIES.find(c => c.id === id)
    if (cat && cat.roles.length === 1) {
      setSelectedRole(0)
    }
  }

  return (
    <div className="fmt-wizard">
      <div className="fmt-header">
        <div className="fmt-title">Find My Track</div>
        <div className="fmt-subtitle">Answer two questions to get your personalized training path.</div>
      </div>

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
              onClick={() => selectCategory(cat.id)}
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
                onClick={() => setSelectedRole(i)}
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

          {/* Visual path */}
          <div className="fmt-path">
            {effectiveResult.path.map((step, i) => (
              <span key={i} className="fmt-path-step">
                {i > 0 && <span className="fmt-path-arrow">{'\u2192'}</span>}
                <span className={`fmt-path-badge${i === effectiveResult.path.length - 1 ? ' final' : ''}`}>{step}</span>
              </span>
            ))}
          </div>

          <div className="fmt-result-actions">
            <button
              className="fmt-go-btn"
              onClick={() => showPanel(effectiveResult.tm40Panel)}
            >
              Go to {effectiveResult.tm40} {'\u2192'}
            </button>
            <button className="fmt-reset-btn" onClick={reset}>
              Start Over
            </button>
          </div>
        </div>
      )}
    </div>
  )
}
