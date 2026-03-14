async function loadManifest(){
  const res = await fetch('manifest.json', {cache:'no-store'});
  return await res.json();
}

function qs(name){
  const url = new URL(window.location.href);
  return url.searchParams.get(name);
}

function el(tag, attrs={}, children=[]){
  const e = document.createElement(tag);
  for(const [k,v] of Object.entries(attrs)){
    if(k === 'class') e.className = v;
    else if(k === 'html') e.innerHTML = v;
    else e.setAttribute(k, v);
  }
  for(const c of children) e.appendChild(typeof c === 'string' ? document.createTextNode(c) : c);
  return e;
}

function clamp(n, min, max){ return Math.max(min, Math.min(max, n)); }

// Track name mapping for display
const TRACK_LABELS = {
  'Intro To Data': 'Primer',
  'Data 101': 'Data 101',
  'Data 201': 'Data 201'
};

const TRACK_ORDER = ['Intro To Data', 'Data 101', 'Data 201'];

function setupViewer(deck){
  const stageImg = document.getElementById('slideImg');
  const counter = document.getElementById('counter');
  const title = document.getElementById('deckTitle');
  const meta = document.getElementById('deckMeta');

  const dlPpt = document.getElementById('dlPpt');
  const dlPdf = document.getElementById('dlPdf');
  const openPpt = document.getElementById('openPpt');

  title.textContent = deck.title;
  meta.textContent = `${deck.count} slides • rendered from the source PPTX for 1:1 visual fidelity`;

  dlPpt.href = deck.pptx;
  openPpt.href = deck.pptx;
  if(deck.pdf){
    dlPdf.href = deck.pdf;
    dlPdf.style.display = 'inline-flex';
  } else {
    dlPdf.style.display = 'none';
  }

  let i = 0;

  function render(){
    i = clamp(i, 0, deck.slides.length-1);
    stageImg.src = deck.slides[i];
    counter.textContent = `${i+1} / ${deck.slides.length}`;
    history.replaceState(null, '', `deck.html?id=${encodeURIComponent(deck.id)}&s=${i+1}`);
  }

  function next(){ i++; render(); }
  function prev(){ i--; render(); }

  document.getElementById('nextBtn').addEventListener('click', next);
  document.getElementById('prevBtn').addEventListener('click', prev);
  document.getElementById('firstBtn').addEventListener('click', ()=>{i=0;render();});
  document.getElementById('lastBtn').addEventListener('click', ()=>{i=deck.slides.length-1;render();});

  document.getElementById('fsBtn').addEventListener('click', async ()=>{
    const stage = document.getElementById('stage');
    if(!document.fullscreenElement) await stage.requestFullscreen();
    else await document.exitFullscreen();
  });

  window.addEventListener('keydown', (e)=>{
    const k = e.key;
    if(k === 'ArrowRight' || k === ' ' || k === 'PageDown'){ e.preventDefault(); next(); }
    if(k === 'ArrowLeft' || k === 'PageUp'){ e.preventDefault(); prev(); }
    if(k === 'Home'){ e.preventDefault(); i=0; render(); }
    if(k === 'End'){ e.preventDefault(); i=deck.slides.length-1; render(); }
  });

  // Jump to slide from query param
  const s = parseInt(qs('s')||'1', 10);
  if(!Number.isNaN(s)) i = clamp(s-1, 0, deck.slides.length-1);
  render();
}

function renderDeckCard(d) {
  return el('div', {class:'card deck'}, [
    el('img', {src:d.thumb, alt:d.title}),
    el('div', {class:'deck-body'}, [
      el('div', {class:'deck-title'}, [d.title]),
      el('div', {class:'deck-meta'}, [`${d.count} slides • `, el('span',{class:'kbd'},['←']), ' / ', el('span',{class:'kbd'},['→']), ' to navigate']),
      el('div', {class:'actions'}, [
        el('a', {class:'btn primary', href:`deck.html?id=${encodeURIComponent(d.id)}`}, ['Open deck']),
        el('a', {class:'btn', href:d.pptx, download:''}, ['Download PPTX']),
        d.pdf ? el('a', {class:'btn', href:d.pdf, download:''}, ['Download PDF']) : el('span')
      ])
    ])
  ]);
}

async function initIndex(){
  const decks = await loadManifest();
  const host = document.getElementById('deckGrid');
  const filterBar = document.getElementById('filterBar');

  // Group decks by track
  const tracks = {};
  for(const d of decks){
    const track = d.track || 'Uncategorized';
    if(!tracks[track]) tracks[track] = [];
    tracks[track].push(d);
  }

  // Build filter buttons
  let activeFilter = 'all';

  function buildFilters(){
    filterBar.innerHTML = '';
    const allBtn = el('button', {class:'filter-btn' + (activeFilter === 'all' ? ' active' : ''), 'data-track':'all'}, ['All Tracks']);
    allBtn.addEventListener('click', ()=>{ activeFilter = 'all'; renderAll(); });
    filterBar.appendChild(allBtn);

    for(const track of TRACK_ORDER){
      if(!tracks[track]) continue;
      const label = TRACK_LABELS[track] || track;
      const count = tracks[track].length;
      const btn = el('button', {
        class:'filter-btn' + (activeFilter === track ? ' active' : ''),
        'data-track': track
      }, [`${label} (${count})`]);
      btn.addEventListener('click', ()=>{ activeFilter = track; renderAll(); });
      filterBar.appendChild(btn);
    }
  }

  function renderAll(){
    host.innerHTML = '';
    buildFilters();

    if(activeFilter === 'all'){
      // Render grouped by track
      for(const track of TRACK_ORDER){
        if(!tracks[track]) continue;
        const label = TRACK_LABELS[track] || track;
        const header = el('div', {class:'track-header'}, [
          el('div', {class:'track-label'}, [label]),
          el('div', {class:'track-count'}, [`${tracks[track].length} decks`])
        ]);
        host.appendChild(header);

        const grid = el('div', {class:'grid track-grid'});
        for(const d of tracks[track]){
          grid.appendChild(renderDeckCard(d));
        }
        host.appendChild(grid);
      }
    } else {
      // Render only selected track
      const trackDecks = tracks[activeFilter] || [];
      const grid = el('div', {class:'grid track-grid'});
      for(const d of trackDecks){
        grid.appendChild(renderDeckCard(d));
      }
      host.appendChild(grid);
    }
  }

  renderAll();
}

async function initDeck(){
  const decks = await loadManifest();
  const id = qs('id');
  const deck = decks.find(d=>d.id === id) || decks[0];
  setupViewer(deck);
}

export { initIndex, initDeck };
