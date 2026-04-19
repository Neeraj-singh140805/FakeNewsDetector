import streamlit as st
import time
from main import run_pipeline
import streamlit.components.v1 as components

def inject_antigravity_particles():
    components.html("""
    <script>
    const parentDoc = window.parent.document;
    if (!parentDoc.getElementById('tsparticles-script')) {
        const script = parentDoc.createElement('script');
        script.id = 'tsparticles-script';
        script.src = 'https://cdn.jsdelivr.net/npm/tsparticles@3.3.0/tsparticles.bundle.min.js';
        parentDoc.head.appendChild(script);
        
        const container = parentDoc.createElement('div');
        container.id = 'tsparticles-wrapper';
        container.style.position = 'fixed';
        container.style.top = '0';
        container.style.left = '0';
        container.style.width = '100vw';
        container.style.height = '100vh';
        container.style.zIndex = '-1';
        container.style.pointerEvents = 'none';
        parentDoc.body.prepend(container);

        const initScript = parentDoc.createElement('script');
        initScript.textContent = `
            const initParticles = () => {
                if (window.tsParticles) {
                    window.tsParticles.load({
                        id: "tsparticles-wrapper",
                        options: {
                            background: { color: { value: "transparent" } },
                            fpsLimit: 120,
                            particles: {
                                color: { value: ["#8b5cf6", "#0ea5e9", "#2dd4bf", "#f43f5e"] },
                                links: { color: "#8b5cf6", distance: 150, enable: true, opacity: 0.3, width: 1 },
                                move: { enable: true, speed: 1.5, direction: "none", outModes: "out" },
                                number: { value: 100, density: { enable: true, area: 800 } },
                                opacity: { value: { min: 0.2, max: 0.6 } },
                                size: { value: { min: 1, max: 3 } }
                            },
                            interactivity: {
                                events: {
                                    onHover: { enable: true, mode: "grab" },
                                    onClick: { enable: true, mode: "push" }
                                },
                                modes: {
                                    grab: { distance: 200, links: { opacity: 0.8 } },
                                    push: { quantity: 4 }
                                }
                            }
                        }
                    });
                } else {
                    setTimeout(initParticles, 100);
                }
            };
            initParticles();
        `;
        parentDoc.head.appendChild(initScript);
    }
    </script>
    """, height=0, width=0)

inject_antigravity_particles()

# ──────────────────────────────────────────
# PAGE CONFIG
# ──────────────────────────────────────────
st.set_page_config(
    page_title="TruthLens AI | Premium Fact Verification",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ──────────────────────────────────────────
# CSS STYLING (DRIBBBLE-WORTHY LUXURY AI)
# ──────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600&display=swap');

:root {
--bg-dark: #050508;
--brand-blue: #2563eb;
--brand-cyan: #06b6d4;
--brand-violet: #8b5cf6;
--brand-emerald: #10b981;
--brand-rose: #f43f5e;

--glass-bg: rgba(20, 20, 30, 0.4);
--glass-border: rgba(255, 255, 255, 0.08);
--glass-glow: 0 8px 32px 0 rgba(139, 92, 246, 0.15);

--text-primary: #ffffff;
--text-secondary: #94a3b8;
}

html, body, .stApp {
background-color: var(--bg-dark);
color: var(--text-primary);
font-family: 'Inter', sans-serif;
overflow-x: hidden;
}

/* ──────────────────────────────────
ANIMATED BACKGROUND & ORBS
────────────────────────────────── */
.background-container {
position: fixed;
top: 0; left: 0; width: 100vw; height: 100vh;
z-index: -2;
overflow: hidden;
background: radial-gradient(circle at 50% 0%, #1a1a2e 0%, var(--bg-dark) 60%);
}
.orb-1 {
position: absolute; width: 600px; height: 600px;
border-radius: 50%; opacity: 0.15; filter: blur(90px);
background: var(--brand-blue);
top: -200px; left: -100px;
animation: float1 15s ease-in-out infinite alternate;
}
.orb-2 {
position: absolute; width: 500px; height: 500px;
border-radius: 50%; opacity: 0.15; filter: blur(90px);
background: var(--brand-violet);
bottom: -100px; right: 10%;
animation: float2 18s ease-in-out infinite alternate;
}
.orb-3 {
position: absolute; width: 400px; height: 400px;
border-radius: 50%; opacity: 0.1; filter: blur(80px);
background: var(--brand-cyan);
top: 40%; left: 50%;
transform: translate(-50%, -50%);
animation: float3 20s linear infinite;
}

@keyframes float1 { 0% { transform: translate(0, 0); } 100% { transform: translate(100px, 50px); } }
@keyframes float2 { 0% { transform: translate(0, 0); } 100% { transform: translate(-80px, -50px); } }
@keyframes float3 { 0% { transform: translate(-50%, -50%) rotate(0deg) scale(1); } 50% { transform: translate(-50%, -50%) rotate(180deg) scale(1.1); } 100% { transform: translate(-50%, -50%) rotate(360deg) scale(1); } }

/* Grid overlay */
.perspective-container {
position: fixed;
top: 0; left: 0; width: 100vw; height: 100vh;
z-index: -1;
overflow: hidden;
pointer-events: none;
}
.moving-grid {
position: absolute;
bottom: 0; left: -50vw;
width: 200vw; height: 100vh;
background-image: 
linear-gradient(rgba(139, 92, 246, 0.5) 2px, transparent 2px),
linear-gradient(90deg, rgba(139, 92, 246, 0.5) 2px, transparent 2px);
background-size: 80px 80px;
transform-origin: bottom center;
transform: perspective(800px) rotateX(60deg) translateY(0);
animation: gridMove 2s linear infinite;
-webkit-mask-image: linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,1) 60%);
mask-image: linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,1) 60%);
}
@keyframes gridMove {
0% { transform: perspective(800px) rotateX(60deg) translateY(0); }
100% { transform: perspective(800px) rotateX(60deg) translateY(80px); }
}


/* Hide Streamlit exact elements */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1rem !important; padding-left: 5rem !important; padding-right: 5rem !important; max-width: 1400px; margin: 0 auto; }

/* ──────────────────────────────────
TOP NAVIGATION
────────────────────────────────── */
.top-nav {
display: flex; justify-content: space-between; align-items: center;
padding: 1.5rem 0; margin-bottom: 3rem;
border-bottom: 1px solid rgba(255,255,255,0.05);
}
.nav-logo {
font-family: 'Plus Jakarta Sans', sans-serif;
font-size: 1.4rem; font-weight: 800; letter-spacing: -0.5px;
background: linear-gradient(135deg, #fff, #94a3b8);
-webkit-background-clip: text; -webkit-text-fill-color: transparent;
display: flex; align-items: center; gap: 8px;
}
.nav-status {
font-size: 0.75rem; font-weight: 600; color: var(--brand-emerald);
background: rgba(16, 185, 129, 0.1); padding: 4px 12px; border-radius: 50px;
border: 1px solid rgba(16, 185, 129, 0.2);
display: flex; align-items: center; gap: 6px;
}
.nav-status span { width: 6px; height: 6px; background: var(--brand-emerald); border-radius: 50%; box-shadow: 0 0 8px var(--brand-emerald); animation: pulse 2s infinite; }

@keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.4; } 100% { opacity: 1; } }

/* ──────────────────────────────────
HERO SECTION
────────────────────────────────── */
.hero-wrapper {
position: relative;
padding: 2rem 0 4rem;
display: flex;
flex-direction: column;
align-items: center;
text-align: center;
z-index: 10;
}

.premium-badge {
display: inline-flex;
align-items: center;
padding: 4px 16px;
background: rgba(255, 255, 255, 0.03);
border: 1px solid rgba(255, 255, 255, 0.1);
border-radius: 100px;
font-family: 'Inter', sans-serif;
font-size: 0.75rem;
font-weight: 600;
letter-spacing: 1px;
color: var(--text-secondary);
text-transform: uppercase;
margin-bottom: 2rem;
backdrop-filter: blur(10px);
box-shadow: 0 4px 20px rgba(0,0,0,0.2);
}
.premium-badge span {
background: linear-gradient(90deg, var(--brand-cyan), var(--brand-violet));
-webkit-background-clip: text; -webkit-text-fill-color: transparent;
margin-right: 6px;
}

.hero-title {
font-family: 'Plus Jakarta Sans', sans-serif;
font-size: clamp(3rem, 6vw, 5.5rem);
font-weight: 800;
line-height: 1.1;
letter-spacing: -2px;
margin-bottom: 1.5rem;
}
.hero-title .highlight {
background: linear-gradient(135deg, #ffffff 0%, #a5b4fc 100%);
-webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.hero-title .gradient-text {
background: linear-gradient(to right, #0ea5e9, #8b5cf6);
-webkit-background-clip: text; -webkit-text-fill-color: transparent;
}

.hero-subtitle {
font-size: 1.15rem;
color: var(--text-secondary);
max-width: 650px;
margin: 0 auto 3rem;
line-height: 1.6;
font-weight: 400;
}

/* ──────────────────────────────────
INPUT CONSOLE / CENTER PANEL
────────────────────────────────── */
.input-console-wrapper {
width: 100%;
max-width: 800px;
position: relative;
z-index: 20;
}

.glass-console {
background: var(--glass-bg);
border: 1px solid var(--glass-border);
border-radius: 24px;
padding: 24px;
backdrop-filter: blur(24px);
box-shadow: 0 24px 80px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.1);
position: relative;
transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.glass-console:hover {
box-shadow: 0 30px 90px rgba(139, 92, 246, 0.15), inset 0 1px 0 rgba(255,255,255,0.2);
}
.glass-console::before {
content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 2px;
background: linear-gradient(90deg, transparent, rgba(139, 92, 246, 0.8), transparent);
animation: scan-line 3s linear infinite;
z-index: 10; pointer-events: none;
}
@keyframes scan-line { 0% { top: 0%; opacity: 0; } 10% { opacity: 1; } 90% { opacity: 1; } 100% { top: 100%; opacity: 0; } }

.console-header {
display: flex; justify-content: space-between; align-items: center;
margin-bottom: 16px; padding: 0 8px;
}
.console-label {
font-size: 0.75rem; font-weight: 600; color: var(--text-secondary);
text-transform: uppercase; letter-spacing: 1.5px;
display: flex; align-items: center; gap: 8px;
}
.console-actions { display: flex; gap: 12px; }
.action-chip {
font-size: 0.7rem; color: var(--text-secondary);
background: rgba(255,255,255,0.05); padding: 4px 10px; border-radius: 6px;
}

/* Textarea overrides */
.stTextArea textarea {
background: rgba(0,0,0,0.2) !important;
border: 1px solid rgba(255,255,255,0.05) !important;
border-radius: 16px !important;
color: #fff !important;
font-family: 'Inter', sans-serif !important;
font-size: 1.05rem !important;
line-height: 1.6 !important;
padding: 1.2rem !important;
min-height: 160px !important;
transition: all 0.3s ease !important;
}
.stTextArea textarea:focus {
border-color: rgba(139, 92, 246, 0.5) !important;
box-shadow: 0 0 0 4px rgba(139, 92, 246, 0.1) !important;
background: rgba(0,0,0,0.3) !important;
}

/* Button overrides - Magic styling */
.stButton > button {
background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%) !important;
color: white !important;
border: none !important;
border-radius: 14px !important;
font-family: 'Plus Jakarta Sans', sans-serif !important;
font-size: 1rem !important;
font-weight: 700 !important;
letter-spacing: 0.5px !important;
padding: 0.8rem 2rem !important;
width: 100% !important;
height: 54px !important;
cursor: pointer;
box-shadow: 0 10px 25px rgba(139, 92, 246, 0.3), inset 0 1px 1px rgba(255,255,255,0.2) !important;
transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
position: relative;
overflow: hidden;
}
.stButton > button::before {
content: ''; position: absolute; top: 0; left: -100%; width: 50%; height: 100%;
background: linear-gradient(to right, transparent, rgba(255,255,255,0.3), transparent);
transform: skewX(-20deg); transition: 0.5s;
}
.stButton > button:hover::before { left: 150%; }
.stButton > button:hover {
transform: translateY(-2px) !important;
box-shadow: 0 20px 35px rgba(139, 92, 246, 0.4), inset 0 1px 1px rgba(255,255,255,0.3) !important;
}
.stButton > button:active { transform: translateY(1px) !important; }

/* ──────────────────────────────────
FLOATING ENVIRONMENT CARDS
────────────────────────────────── */
.floating-card {
position: absolute;
background: rgba(15, 15, 25, 0.6);
border: 1px solid rgba(255,255,255,0.06);
border-radius: 16px;
padding: 1rem 1.2rem;
backdrop-filter: blur(16px);
box-shadow: 0 15px 35px rgba(0,0,0,0.2);
display: flex; align-items: center; gap: 12px;
z-index: 5;
animation: float-element 6s ease-in-out infinite alternate;
overflow: hidden;
}
.floating-card::after {
content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%;
background: conic-gradient(from 0deg, transparent 0%, rgba(139, 92, 246, 0.15) 20%, transparent 40%);
animation: radar-spin 4s linear infinite;
z-index: -1;
}
@keyframes radar-spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

.fc-1 { top: 20%; left: 0%; animation-delay: 0s; transform: rotate(-3deg); }
.fc-2 { bottom: 15%; right: 0%; animation-delay: 1s; transform: rotate(2deg); }
.fc-3 { top: 50%; right: 5%; animation-delay: 2s; transform: rotate(5deg); }

.fc-icon {
width: 38px; height: 38px; border-radius: 10px;
display: flex; align-items: center; justify-content: center; font-size: 1.2rem;
}
.fc-icon.blue { background: rgba(59, 130, 246, 0.15); color: #60a5fa; border: 1px solid rgba(59, 130, 246, 0.3); }
.fc-icon.violet { background: rgba(139, 92, 246, 0.15); color: #a78bfa; border: 1px solid rgba(139, 92, 246, 0.3); }
.fc-icon.emerald { background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); }

.fc-content { display: flex; flex-direction: column; text-align: left; }
.fc-title { font-size: 0.75rem; font-weight: 600; color: var(--text-secondary); text-transform: uppercase; }
.fc-val { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1rem; font-weight: 700; color: #fff; }

@keyframes float-element { 0% { transform: translateY(0px) rotate(auto); } 100% { transform: translateY(-15px) rotate(auto); } }

/* ──────────────────────────────────
RESULTS DASHBOARD (POST-EXECUTION)
────────────────────────────────── */
.result-section {
margin-top: 2rem;
animation: revealUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
@keyframes revealUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }

/* Verification Hero Card */
.verdict-hero {
background: var(--glass-bg);
border-radius: 24px;
padding: 3rem;
text-align: center;
position: relative;
overflow: hidden;
backdrop-filter: blur(20px);
margin-bottom: 2rem;
display: flex; flex-direction: column; align-items: center; justify-content: center;
}
.verdict-hero.v-real { 
border: 1px solid rgba(16, 185, 129, 0.3); 
box-shadow: 0 20px 60px rgba(16, 185, 129, 0.08), inset 0 0 80px rgba(16, 185, 129, 0.05);
}
.verdict-hero.v-fake { 
border: 1px solid rgba(244, 63, 94, 0.3); 
box-shadow: 0 20px 60px rgba(244, 63, 94, 0.08), inset 0 0 80px rgba(244, 63, 94, 0.05);
}

.verdict-label {
font-size: 0.75rem; font-weight: 700; letter-spacing: 3px; text-transform: uppercase;
color: var(--text-secondary); margin-bottom: 1rem;
}
.verdict-main {
font-family: 'Plus Jakarta Sans', sans-serif;
font-size: 4.5rem; font-weight: 900; letter-spacing: -2px; line-height: 1;
text-transform: uppercase; margin-bottom: 1rem;
}
.v-real .verdict-main { color: #34d399; text-shadow: 0 0 30px rgba(52, 211, 153, 0.4); }
.v-fake .verdict-main { color: #fb7185; text-shadow: 0 0 30px rgba(251, 113, 133, 0.4); }

.verdict-meta {
display: flex; gap: 24px; margin-top: 1.5rem;
}
.meta-badge {
background: rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.1);
padding: 8px 16px; border-radius: 50px; font-size: 0.85rem; font-weight: 500;
}

/* Layout structural cards */
.dashboard-grid {
display: grid; grid-template-columns: 1fr 1.2fr; gap: 1.5rem;
}
.dash-card {
background: rgba(20, 20, 25, 0.5);
border: 1px solid rgba(255,255,255,0.06);
border-radius: 20px;
padding: 2rem;
backdrop-filter: blur(10px);
}
.dc-header {
display: flex; align-items: center; gap: 12px; margin-bottom: 1.5rem;
font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.1rem; font-weight: 700; color: #fff;
}
.dc-icon {
width: 32px; height: 32px; border-radius: 8px; background: rgba(255,255,255,0.1);
display: flex; align-items: center; justify-content: center;
}

/* Metric Bars */
.metric-row { margin-bottom: 1rem; }
.metric-top { display: flex; justify-content: space-between; font-size: 0.85rem; font-weight: 500; margin-bottom: 6px; color: var(--text-secondary); }
.metric-val { color: #fff; font-weight: 600; }
.metric-bar-bg { height: 6px; background: rgba(255,255,255,0.05); border-radius: 10px; overflow: hidden; }
.metric-bar-fill { height: 100%; border-radius: 10px; transition: width 1s cubic-bezier(0.4, 0, 0.2, 1); }

/* Evidence Chips */
.evidence-card {
background: rgba(0,0,0,0.2);
border: 1px solid rgba(255,255,255,0.05);
border-radius: 14px; padding: 1.2rem; margin-bottom: 1rem;
transition: all 0.2s ease;
}
.evidence-card:hover { background: rgba(255,255,255,0.03); border-color: rgba(139, 92, 246, 0.3); transform: translateX(5px); }
.ev-title { font-weight: 600; color: #fff; margin-bottom: 8px; font-size: 0.95rem; line-height: 1.4; display: flex; align-items: flex-start; gap: 10px; }
.ev-desc { font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6; margin-left: 28px; margin-bottom: 10px; }
.ev-footer { display: flex; justify-content: space-between; margin-left: 28px; font-size: 0.75rem; }
.ev-source { color: var(--brand-violet); font-weight: 600; padding: 2px 8px; background: rgba(139, 92, 246, 0.1); border-radius: 4px; }
.ev-link a { color: var(--text-secondary); text-decoration: none; display: flex; align-items: center; gap: 4px; }
.ev-link a:hover { color: #fff; }

/* Explanation box */
.ai-reasoning {
background: linear-gradient(180deg, rgba(37, 99, 235, 0.05) 0%, transparent 100%);
border-left: 3px solid var(--brand-blue);
padding: 1.5rem; border-radius: 0 12px 12px 0;
font-size: 0.95rem; line-height: 1.8; color: #e2e8f0;
}
</style>

<!-- BACKGROUND ELEMENTS -->
<div class="background-container">
<div class="orb-1"></div>
<div class="orb-2"></div>
<div class="orb-3"></div>
</div>
<div class="perspective-container">
<div class="moving-grid"></div>
</div>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────
# TOP NAV
# ──────────────────────────────────────────
st.markdown("""
<div class="top-nav">
<div class="nav-logo">
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M12 16v-4"></path><path d="M12 8h.01"></path></svg>
TruthLens AI
</div>
<div class="nav-status"><span></span> NEURAL NETWORK ONLINE</div>
</div>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────
# HERO SECTION
# ──────────────────────────────────────────
st.markdown("""
<div class="hero-wrapper">
<div class="premium-badge">
<span>✦</span> AGENTIC AI · RAG · ML VERIFICATION
</div>

<h1 class="hero-title">
<span class="highlight">Intelligence</span> that separates<br>
fact from <span class="gradient-text">fiction.</span>
</h1>

<p class="hero-subtitle">
Deploy a world-class AI agent to cross-examine claims across live news databases, analyze linguistic manipulation, and deliver deep neural verification in seconds.
</p>

<!-- FLOATING BACKGROUND CARDS -->
<div class="floating-card fc-1">
<div class="fc-icon blue">🛡️</div>
<div class="fc-content">
<span class="fc-title">Trust Model</span>
<span class="fc-val">Scikit-Learn V1</span>
</div>
</div>

<div class="floating-card fc-2">
<div class="fc-icon emerald">⚡</div>
<div class="fc-content">
<span class="fc-title">Cross-Verification</span>
<span class="fc-val">100+ Live Sources</span>
</div>
</div>

<div class="floating-card fc-3">
<div class="fc-icon violet">🧠</div>
<div class="fc-content">
<span class="fc-title">Language Scan</span>
<span class="fc-val">Deep Lexical</span>
</div>
</div>
</div>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────
# MAIN INPUT CONSOLE
# ──────────────────────────────────────────
col_space_l, col_center, col_space_r = st.columns([1, 2.5, 1])

with col_center:
    st.markdown('<div class="input-console-wrapper"><div class="glass-console">', unsafe_allow_html=True)
    
    st.markdown("""
<div class="console-header">
<div class="console-label"><span>✧</span> ANALYSIS CONSOLE</div>
<div class="console-actions">
<span class="action-chip">Autoscan: ON</span>
<span class="action-chip">Deep RAG: ON</span>
</div>
</div>
""", unsafe_allow_html=True)

    query = st.text_area(
        "Analyze Claim",
        height=140,
        label_visibility="collapsed",
        placeholder="Drop a headline, article text, or controversial claim here. The agent will handle the rest..."
    )
    
    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)
    
    analyze_btn = st.button("INITIATE VERIFICATION")
    
    st.markdown('</div></div>', unsafe_allow_html=True)


# ──────────────────────────────────────────
# DASHBOARD CONTROLLERS & DATA RENDERS
# ──────────────────────────────────────────
def _render_metric(label: str, val: float, max_v: float, color: str):
    pct = min(val / max_v, 1.0) * 100 if max_v else 0
    st.markdown(f"""
<div class="metric-row">
<div class="metric-top">
<span>{label}</span>
<span class="metric-val">{val}</span>
</div>
<div class="metric-bar-bg">
<div class="metric-bar-fill" style="width: {pct}%; background: {color};"></div>
</div>
</div>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────
# EXECUTION LOGIC
# ──────────────────────────────────────────
if analyze_btn:
    if not query.strip():
        st.markdown("""
<div style="text-align:center; margin-top: 2rem;">
<div style="display:inline-block; background:rgba(244,63,94,0.1); color:#f43f5e; border:1px solid rgba(244,63,94,0.3); padding:12px 24px; border-radius:12px; font-weight:600;">
⚠️ Input required for analysis. Please provide text.
</div>
</div>
""", unsafe_allow_html=True)
    else:
        st.markdown("<br>", unsafe_allow_html=True)
        with st.spinner("Agent initializing deep network scan..."):
            time.sleep(0.5) 
            result = run_pipeline(query)
            
        if result.get("error"):
            st.error(result["error"])
        else:
            ml_data = result.get("ml", {})
            verdict = ml_data.get("verdict", "UNKNOWN").upper()
            credibility = ml_data.get("credibility", 0)
            confidence = result.get("confidence", 0)
            metrics = result.get("metrics", {})
            docs = result.get("docs", [])
            answer = result.get("answer", "No analysis mapped.")

            is_real = (verdict == "REAL")
            v_class = "v-real" if is_real else "v-fake"
            
            st.markdown('<div class="result-section">', unsafe_allow_html=True)
            
            # 1. VERDICT HERO
            st.markdown(f"""
<div class="verdict-hero {v_class}">
<div class="verdict-label">Final Verification Output</div>
<div class="verdict-main">{verdict}</div>
<div style="color:var(--text-secondary); max-width: 600px; line-height:1.6;">
System has evaluated linguistic markers, semantic intent, and cross-referenced claims across the live RAG document index.
</div>
<div class="verdict-meta">
<div class="meta-badge">Credibility Base: <b style="color:#fff">{credibility}%</b></div>
<div class="meta-badge">Agent Confidence: <b style="color:#fff">{confidence}%</b></div>
</div>
</div>
""", unsafe_allow_html=True)
            
            # 2. DUAL COLUMNS
            col_a, col_b = st.columns([1, 1.2], gap="large")
            
            with col_a:
                st.markdown("""
<div class="dash-card">
<div class="dc-header">
<div class="dc-icon">📊</div> Linguistic Matrix
</div>
""", unsafe_allow_html=True)
                
                _render_metric("Sensationalism Index", metrics.get("Sensationalism", 0), 10, "#f43f5e")
                _render_metric("Clickbait Density", metrics.get("Clickbait", 0), 5, "#f59e0b")
                _render_metric("Exaggeration Level", metrics.get("Exaggeration", 0), 10, "#eab308")
                _render_metric("Visual Emphasis", metrics.get("VisualEmphasis", 0), 10, "#a855f7")
                _render_metric("Emotional Intensity", round(metrics.get("EmotionalIntensity", 0)*100, 1), 100, "#3b82f6")
                
                st.markdown("</div>", unsafe_allow_html=True)
                
                # Reasoning block
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown("""
<div class="dash-card">
<div class="dc-header">
<div class="dc-icon">🧠</div> Neural Reasoning Trace
</div>
<div class="ai-reasoning">
{}
</div>
</div>
""".format(answer), unsafe_allow_html=True)

            with col_b:
                st.markdown(f"""
<div class="dash-card">
<div class="dc-header">
<div class="dc-icon">🌐</div> Live Evidence Extracted ({len(docs)} Sources)
</div>
""", unsafe_allow_html=True)
                
                if not docs:
                    st.info("No corroborating documents found in active search.")
                else:
                    for i, doc in enumerate(docs, 1):
                        title = doc.get("title", "Untitled Source")
                        content = doc.get("content", "")
                        source = doc.get("source", "Unknown Authority")
                        url = doc.get("url", "#")
                        snippet = content[:140] + "..." if content else "No snippet available."
                        
                        st.markdown(f"""
<div class="evidence-card">
<div class="ev-title">
<span style="background:rgba(255,255,255,0.1); padding:2px 8px; border-radius:4px; font-size:0.7rem; color:#94a3b8;">{i}</span>
{title}
</div>
<div class="ev-desc">{snippet}</div>
<div class="ev-footer">
<span class="ev-source">{source}</span>
<span class="ev-link"><a href="{url}" target="_blank">View Original ↗</a></span>
</div>
</div>
""", unsafe_allow_html=True)
                        
                st.markdown("</div>", unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><br><br><br>", unsafe_allow_html=True)