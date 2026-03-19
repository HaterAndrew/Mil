import { URLS } from '../constants/urls'

interface Props {
  showPanel: (id: string) => void
}

export default function TM50({ showPanel }: Props) {
  return (
    <>
      <div className="section-header">
        <span className="section-badge">TM-50</span>
        <span className="section-title">Advanced Developer Tracks</span>
        <span className="section-subtitle">Prerequisite: TM-40 (by track) &bull; Tracks TM-50G&ndash;O &bull; All 8 tracks available</span>
      </div>

      <div className="callout bluf">
        <div className="callout-label">BLUF &mdash; ADVANCED TRACKS</div>
        <div className="callout-body">The TM-50 series provides advanced-level instruction for each developer track, building directly on the corresponding TM-40 specialist manual (TM-40G&ndash;O). Intended for senior technical leads, platform architects, and senior developers designing enterprise-scale MSS capabilities. All 8 tracks are complete and available.</div>
      </div>

      <h2>TM-50 SERIES &mdash; PUBLICATIONS</h2>
      <div className="track-grid">
        <a className="track-card doc-card" href={URLS.TM50G} target="_blank" rel="noreferrer">
          <div className="track-card-hdr">
            <div className="track-tm">TM-50G &mdash; ORSA Advanced</div>
            <div className="track-chip">Advanced</div>
          </div>
          <div className="track-body">
            <div className="track-name">Advanced ORSA</div>
            <div className="track-audience">Prerequisite: TM-40G</div>
            <ul className="track-topics">
              <li>Nonlinear programming, stochastic models</li>
              <li>Agent-based modeling (ABMS)</li>
              <li>Campaign wargame data architecture</li>
            </ul>
          </div>
        </a>
        <a className="track-card doc-card" href={URLS.TM50H} target="_blank" rel="noreferrer">
          <div className="track-card-hdr">
            <div className="track-tm">TM-50H &mdash; AI Engineer Advanced</div>
            <div className="track-chip">Advanced</div>
          </div>
          <div className="track-body">
            <div className="track-name">Advanced AI Engineering</div>
            <div className="track-audience">Prerequisite: TM-40H</div>
            <ul className="track-topics">
              <li>Multi-agent orchestration &amp; shared state</li>
              <li>Advanced RAG, domain-adapted LLMs</li>
              <li>AI red-team assessment &amp; observability</li>
            </ul>
          </div>
        </a>
        <a className="track-card doc-card" href={URLS.TM50M} target="_blank" rel="noreferrer">
          <div className="track-card-hdr">
            <div className="track-tm">TM-50M &mdash; ML Engineer Advanced</div>
            <div className="track-chip">Advanced</div>
          </div>
          <div className="track-body">
            <div className="track-name">Advanced ML Engineering</div>
            <div className="track-audience">Prerequisite: TM-40M</div>
            <ul className="track-topics">
              <li>Automated retraining pipelines</li>
              <li>Transformer fine-tuning, GNNs</li>
              <li>Federated retraining, adversarial robustness</li>
            </ul>
          </div>
        </a>
        <a className="track-card doc-card" href={URLS.TM50J} target="_blank" rel="noreferrer">
          <div className="track-card-hdr">
            <div className="track-tm">TM-50J &mdash; PM Advanced</div>
            <div className="track-chip">Advanced</div>
          </div>
          <div className="track-body">
            <div className="track-name">Advanced Program Management</div>
            <div className="track-audience">Prerequisite: TM-40J</div>
            <ul className="track-topics">
              <li>PI planning, cross-team governance</li>
              <li>GO/SES briefing, Palantir partnership</li>
              <li>Technical debt at program scale</li>
            </ul>
          </div>
        </a>
        <a className="track-card doc-card" href={URLS.TM50K} target="_blank" rel="noreferrer">
          <div className="track-card-hdr">
            <div className="track-tm">TM-50K &mdash; KM Advanced</div>
            <div className="track-chip">Advanced</div>
          </div>
          <div className="track-body">
            <div className="track-name">Advanced Knowledge Management</div>
            <div className="track-audience">Prerequisite: TM-40K</div>
            <ul className="track-topics">
              <li>Federated KM architecture, NATO integration</li>
              <li>STANAG 4778 conformance</li>
              <li>Knowledge graphs at scale</li>
            </ul>
          </div>
        </a>
        <a className="track-card doc-card" href={URLS.TM50L} target="_blank" rel="noreferrer">
          <div className="track-card-hdr">
            <div className="track-tm">TM-50L &mdash; SWE Advanced</div>
            <div className="track-chip">Advanced</div>
          </div>
          <div className="track-body">
            <div className="track-name">Advanced Software Engineering</div>
            <div className="track-audience">Prerequisite: TM-40L</div>
            <ul className="track-topics">
              <li>Scale, multi-tenancy, event streaming</li>
              <li>OWASP, SAST, authorized pen testing</li>
              <li>Architecture review, platform governance</li>
            </ul>
          </div>
        </a>
        <a className="track-card doc-card" href={URLS.TM50N} target="_blank" rel="noreferrer">
          <div className="track-card-hdr">
            <div className="track-tm">TM-50N &mdash; UI/UX Advanced</div>
            <div className="track-chip">Advanced</div>
          </div>
          <div className="track-body">
            <div className="track-name">Advanced UI/UX Design</div>
            <div className="track-audience">Prerequisite: TM-40N</div>
            <ul className="track-topics">
              <li>Design systems at scale, component libraries</li>
              <li>DDIL-aware and cross-domain UI design</li>
              <li>DesignOps, ResearchOps, accessibility at enterprise scale</li>
            </ul>
          </div>
        </a>
        <a className="track-card doc-card" href={URLS.TM50O} target="_blank" rel="noreferrer">
          <div className="track-card-hdr">
            <div className="track-tm">TM-50O &mdash; Platform Eng Advanced</div>
            <div className="track-chip">Advanced</div>
          </div>
          <div className="track-body">
            <div className="track-name">Advanced Platform Engineering</div>
            <div className="track-audience">Prerequisite: TM-40O</div>
            <ul className="track-topics">
              <li>Multi-cluster fleet management, SRE practices</li>
              <li>RMF/ATO automation, continuous compliance</li>
              <li>Cross-domain infrastructure, developer experience engineering</li>
            </ul>
          </div>
        </a>
      </div>

      <div className="callout note mt-24">
        <div className="callout-label">NOTE &mdash; PREREQUISITES</div>
        <div className="callout-body">Each TM-50 track requires completion of the corresponding TM-40 track. Personnel should confirm TM-40 proficiency with their data steward before beginning TM-50 content. Contact the USAREUR-AF Operational Data Team for access questions.</div>
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
