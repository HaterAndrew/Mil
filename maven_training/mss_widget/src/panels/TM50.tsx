import { URLS } from '../constants/urls'

interface Props {
  showPanel: (id: string) => void
}

export default function TM50({ showPanel }: Props) {
  return (
    <>
      <div className="section-header">
        <span className="section-badge">SL 5</span>
        <span className="section-title">Advanced Developer Tracks</span>
        <span className="section-subtitle">Prerequisite: SL 4 (by track) &bull; Tracks SL 5G&ndash;O &bull; All 8 tracks available</span>
      </div>

      <div className="callout bluf">
        <div className="callout-label">BLUF &mdash; ADVANCED TRACKS</div>
        <div className="callout-body">The SL 5 series provides advanced-level instruction for each developer track, building directly on the corresponding SL 4 specialist manual (SL 4G&ndash;O). Intended for senior technical leads, platform architects, and senior developers designing enterprise-scale MSS capabilities. All 8 tracks are complete and available.</div>
      </div>

      <h2>SL 5 SERIES &mdash; PUBLICATIONS</h2>
      <div className="track-grid">
        <a className="track-card doc-card" href={URLS.SL5G} target="_blank" rel="noreferrer">
          <div className="track-card-hdr">
            <div className="track-tm">TM-50G (SL 5G) &mdash; ORSA Advanced</div>
            <div className="track-chip">Advanced</div>
          </div>
          <div className="track-body">
            <div className="track-name">Advanced ORSA</div>
            <div className="track-audience">Prerequisite: SL 4G</div>
            <ul className="track-topics">
              <li>Nonlinear programming, stochastic models</li>
              <li>Agent-based modeling (ABMS)</li>
              <li>Campaign wargame data architecture</li>
            </ul>
          </div>
        </a>
        <a className="track-card doc-card" href={URLS.SL5H} target="_blank" rel="noreferrer">
          <div className="track-card-hdr">
            <div className="track-tm">TM-50H (SL 5H) &mdash; AI Engineer Advanced</div>
            <div className="track-chip">Advanced</div>
          </div>
          <div className="track-body">
            <div className="track-name">Advanced AI Engineering</div>
            <div className="track-audience">Prerequisite: SL 4H</div>
            <ul className="track-topics">
              <li>Multi-agent orchestration &amp; shared state</li>
              <li>Advanced RAG, domain-adapted LLMs</li>
              <li>AI red-team assessment &amp; observability</li>
            </ul>
          </div>
        </a>
        <a className="track-card doc-card" href={URLS.SL5M} target="_blank" rel="noreferrer">
          <div className="track-card-hdr">
            <div className="track-tm">TM-50M (SL 5M) &mdash; ML Engineer Advanced</div>
            <div className="track-chip">Advanced</div>
          </div>
          <div className="track-body">
            <div className="track-name">Advanced ML Engineering</div>
            <div className="track-audience">Prerequisite: SL 4M</div>
            <ul className="track-topics">
              <li>Automated retraining pipelines</li>
              <li>Transformer fine-tuning, GNNs</li>
              <li>Federated retraining, adversarial robustness</li>
            </ul>
          </div>
        </a>
        <a className="track-card doc-card" href={URLS.SL5J} target="_blank" rel="noreferrer">
          <div className="track-card-hdr">
            <div className="track-tm">TM-50J (SL 5J) &mdash; PM Advanced</div>
            <div className="track-chip">Advanced</div>
          </div>
          <div className="track-body">
            <div className="track-name">Advanced Program Management</div>
            <div className="track-audience">Prerequisite: SL 4J</div>
            <ul className="track-topics">
              <li>PI planning, cross-team governance</li>
              <li>GO/SES briefing, Palantir partnership</li>
              <li>Technical debt at program scale</li>
            </ul>
          </div>
        </a>
        <a className="track-card doc-card" href={URLS.SL5K} target="_blank" rel="noreferrer">
          <div className="track-card-hdr">
            <div className="track-tm">TM-50K (SL 5K) &mdash; KM Advanced</div>
            <div className="track-chip">Advanced</div>
          </div>
          <div className="track-body">
            <div className="track-name">Advanced Knowledge Management</div>
            <div className="track-audience">Prerequisite: SL 4K</div>
            <ul className="track-topics">
              <li>Federated KM architecture, NATO integration</li>
              <li>STANAG 4778 conformance</li>
              <li>Knowledge graphs at scale</li>
            </ul>
          </div>
        </a>
        <a className="track-card doc-card" href={URLS.SL5L} target="_blank" rel="noreferrer">
          <div className="track-card-hdr">
            <div className="track-tm">TM-50L (SL 5L) &mdash; SWE Advanced</div>
            <div className="track-chip">Advanced</div>
          </div>
          <div className="track-body">
            <div className="track-name">Advanced Software Engineering</div>
            <div className="track-audience">Prerequisite: SL 4L</div>
            <ul className="track-topics">
              <li>Scale, multi-tenancy, event streaming</li>
              <li>OWASP, SAST, authorized pen testing</li>
              <li>Architecture review, platform governance</li>
            </ul>
          </div>
        </a>
        <a className="track-card doc-card" href={URLS.SL5N} target="_blank" rel="noreferrer">
          <div className="track-card-hdr">
            <div className="track-tm">TM-50N (SL 5N) &mdash; UI/UX Advanced</div>
            <div className="track-chip">Advanced</div>
          </div>
          <div className="track-body">
            <div className="track-name">Advanced UI/UX Design</div>
            <div className="track-audience">Prerequisite: SL 4N</div>
            <ul className="track-topics">
              <li>Design systems at scale, component libraries</li>
              <li>DDIL-aware and cross-domain UI design</li>
              <li>DesignOps, ResearchOps, accessibility at enterprise scale</li>
            </ul>
          </div>
        </a>
        <a className="track-card doc-card" href={URLS.SL5O} target="_blank" rel="noreferrer">
          <div className="track-card-hdr">
            <div className="track-tm">TM-50O (SL 5O) &mdash; Platform Eng Advanced</div>
            <div className="track-chip">Advanced</div>
          </div>
          <div className="track-body">
            <div className="track-name">Advanced Platform Engineering</div>
            <div className="track-audience">Prerequisite: SL 4O</div>
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
        <div className="callout-body">Each SL 5 track requires completion of the corresponding SL 4 track. Personnel should confirm SL 4 proficiency with their data steward before beginning SL 5 content. Contact the USAREUR-AF Operational Data Team for access questions.</div>
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
