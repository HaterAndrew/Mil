/** Course-portal adapter -- mounts at /training/* in the GDAP Portal. */
import { useState, useEffect, useCallback } from "react";
import { Routes, Route, useSearchParams, Link } from "react-router-dom";
import manifest from "./nav-manifest.json";

interface Deck { id: string; pptx: string; title: string; slides: string[]; thumb: string; count: number; pdf?: string }
const BASE = import.meta.env.BASE_URL + "architecture/cda/apps/course-portal";
const btn: React.CSSProperties = { padding: "8px 12px", borderRadius: 4, border: "1px solid rgba(56,189,248,.12)", background: "rgba(255,255,255,.04)", color: "#e2e8f0", cursor: "pointer", fontSize: 13, fontWeight: 600, fontFamily: "'IBM Plex Mono',monospace", textDecoration: "none" };

function useManifest() {
  const [decks, set] = useState<Deck[]>([]);
  useEffect(() => { fetch(`${BASE}/manifest.json`, { cache: "no-store" }).then((r) => r.json()).then(set).catch(console.error); }, []);
  return decks;
}

function DeckIndex() {
  const decks = useManifest();
  return (
    <div style={{ maxWidth: 1200, margin: "0 auto", padding: "20px 18px 44px" }}>
      <h1 style={{ fontSize: 24, fontWeight: 700, marginBottom: 8, color: "#e2e8f0" }}>Slide Library</h1>
      <p style={{ color: "#94a3b8", marginBottom: 20, fontSize: 14 }}>Interactive decks with PPTX downloads.</p>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill,minmax(340px,1fr))", gap: 14 }}>
        {decks.map((d) => (
          <div key={d.id} style={{ border: "1px solid rgba(56,189,248,.12)", borderRadius: 4, overflow: "hidden", background: "rgba(255,255,255,.03)" }}>
            <img src={`${BASE}/${d.thumb}`} alt={d.title} style={{ width: "100%", height: 180, objectFit: "cover" }} />
            <div style={{ padding: 14 }}>
              <div style={{ fontWeight: 800, fontSize: 16, marginBottom: 8, color: "#e2e8f0" }}>{d.title}</div>
              <div style={{ fontSize: 12, color: "#94a3b8", marginBottom: 12 }}>{d.count} slides</div>
              <div style={{ display: "flex", gap: 10 }}>
                <Link to={`/training/deck?id=${encodeURIComponent(d.id)}`} style={{ ...btn, border: "1px solid rgba(56,189,248,.35)", background: "rgba(56,189,248,.10)" }}>Open</Link>
                <a href={`${BASE}/${d.pptx}`} download style={btn}>PPTX</a>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function DeckViewer() {
  const [sp] = useSearchParams();
  const decks = useManifest();
  const deck = decks.find((d) => d.id === sp.get("id")) || decks[0];
  const [s, setS] = useState(0);
  const max = deck ? deck.slides.length - 1 : 0;
  const clamp = (n: number) => Math.max(0, Math.min(n, max));
  useEffect(() => { if (deck) setS(clamp(parseInt(sp.get("s") || "1", 10) - 1)); }, [deck]);
  const onKey = useCallback((e: KeyboardEvent) => {
    if (["ArrowRight", " ", "PageDown"].includes(e.key)) { e.preventDefault(); setS((v) => clamp(v + 1)); }
    if (["ArrowLeft", "PageUp"].includes(e.key)) { e.preventDefault(); setS((v) => clamp(v - 1)); }
    if (e.key === "Home") { e.preventDefault(); setS(0); }
    if (e.key === "End") { e.preventDefault(); setS(max); }
  }, [max]);
  useEffect(() => { window.addEventListener("keydown", onKey); return () => window.removeEventListener("keydown", onKey); }, [onKey]);
  if (!deck) return <div style={{ padding: 24, color: "#94a3b8" }}>Loading...</div>;
  return (
    <div style={{ maxWidth: 1200, margin: "0 auto", padding: "20px 18px" }}>
      <div style={{ marginBottom: 12, display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <div><Link to="/training" style={{ color: "#38bdf8", textDecoration: "none" }}>All decks</Link> <span style={{ color: "#ffffff33" }}>|</span> <b style={{ color: "#e2e8f0" }}>{deck.title}</b></div>
        <span style={{ fontSize: 12, color: "#94a3b8" }}>{s + 1}/{deck.slides.length}</span>
      </div>
      <div style={{ background: "rgba(0,0,0,.25)", border: "1px solid rgba(56,189,248,.12)", borderRadius: 4, minHeight: "60vh", display: "flex", alignItems: "center", justifyContent: "center" }}>
        <img src={`${BASE}/${deck.slides[s]}`} alt={`Slide ${s + 1}`} style={{ width: "100%", display: "block" }} />
      </div>
      <div style={{ display: "flex", gap: 10, marginTop: 12, flexWrap: "wrap" }}>
        {["First","Prev","Next","Last"].map((l, i) => <button key={l} onClick={() => setS(i < 2 ? (i === 0 ? 0 : clamp(s - 1)) : (i === 2 ? clamp(s + 1) : max))} style={btn}>{l}</button>)}
        <a href={`${BASE}/${deck.pptx}`} download style={btn}>PPTX</a>
        {deck.pdf && <a href={`${BASE}/${deck.pdf}`} download style={btn}>PDF</a>}
      </div>
    </div>
  );
}

export function TrainingModule() {
  return (
    <div className="training-module" style={{ width: "100%", height: "100%" }}>
      <Routes><Route index element={<DeckIndex />} /><Route path="deck" element={<DeckViewer />} /></Routes>
    </div>
  );
}
export const trainingManifest = manifest;
export default TrainingModule;
