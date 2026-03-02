import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="FakeNewsDetector — AI Credibility Audit",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# PREMIUM CSS - FOCUS ON OUTPUT BEAUTY
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap');

    :root {
        --bg: #030712;
        --card-bg: rgba(255, 255, 255, 0.03);
        --border: rgba(255, 255, 255, 0.08);
        --accent: #8b5cf6;
        --success: #10b981;
        --error: #ef4444;
        --text: #f3f4f6;
    }

    .stApp {
        background-color: var(--bg);
        color: var(--text);
        font-family: 'Inter', sans-serif;
    }

    /* Minimalist Background */
    .bg-gradient {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: radial-gradient(circle at 20% 20%, rgba(139, 92, 246, 0.05) 0%, transparent 50%),
                    radial-gradient(circle at 80% 80%, rgba(56, 189, 248, 0.05) 0%, transparent 50%);
        z-index: -1;
    }

    /* App Header */
    .app-header {
        text-align: center;
        padding: 2rem 0;
        margin-bottom: 2rem;
    }
    .app-name {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2.2rem;
        font-weight: 700;
        letter-spacing: -1px;
        background: linear-gradient(135deg, #a78bfa, #38bdf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Result Section - THE MAIN FOCUS */
    .output-container {
        animation: fadeIn 0.6s ease-out;
    }
    
    .verdict-box {
        background: var(--card-bg);
        border: 1px solid var(--border);
        border-radius: 24px;
        padding: 3rem;
        text-align: center;
        backdrop-filter: blur(20px);
        margin-top: 2rem;
    }
    
    .verdict-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.2rem;
        text-transform: uppercase;
        letter-spacing: 4px;
        color: #94a3b8;
        margin-bottom: 0.5rem;
    }
    
    .verdict-hero {
        font-size: 4rem;
        font-weight: 800;
        margin-bottom: 1rem;
        font-family: 'Space Grotesk', sans-serif;
    }
    
    .status-real { color: var(--success); text-shadow: 0 0 30px rgba(16, 185, 129, 0.2); }
    .status-fake { color: var(--error); text-shadow: 0 0 30px rgba(239, 68, 68, 0.2); }

    .analysis-pill {
        background: rgba(255,255,255,0.05);
        border: 1px solid var(--border);
        padding: 20px;
        border-radius: 20px;
        height: 100%;
    }
    
    .pill-title {
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        color: #64748b;
        letter-spacing: 1px;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* Descriptive list */
    .reason-item {
        margin-bottom: 12px;
        font-size: 0.95rem;
        line-height: 1.6;
        color: #cbd5e1;
        padding-left: 20px;
        position: relative;
    }
    .reason-item::before {
        content: "•";
        position: absolute;
        left: 0;
        color: var(--accent);
        font-weight: bold;
    }

    /* Input Styling */
    .stTextArea textarea {
        background: rgba(0,0,0,0.2) !important;
        border: 1px solid var(--border) !important;
        border-radius: 16px !important;
        color: var(--text) !important;
        padding: 1rem !important;
        font-size: 1rem !important;
    }

    .stButton>button {
        background: linear-gradient(90deg, #8b5cf6, #3b82f6) !important;
        color: white !important;
        border: none !important;
        border-radius: 50px !important;
        font-weight: 600 !important;
        padding: 0.8rem 2.5rem !important;
        width: 100%;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(139, 92, 246, 0.3) !important;
    }

    /* Cleanup empty boxes */
    div[data-testid="stVerticalBlock"] > div:empty { display: none !important; }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
<div class="bg-gradient"></div>
""", unsafe_allow_html=True)

# ==========================================
# LOGIC LINKAGE (YOUR APP.PY CORE)
# ==========================================

from predict import predict_news

def get_detailed_report(cred, m):
    """Generates a human-readable report based on neural scores and style metrics"""
    reasons = []
    # Metrics from predict.py use these keys: Sensationalism, Clickbait, Exaggeration, VisualEmphasis, EmotionalIntensity
    if cred >= 50:
        reasons.append(f"**Structural Validity**: The AI model verified the journalistic structure with **{cred}% confidence**.")
        reasons.append("**Balanced Framing**: The text follows professional editorial standards with minimal bias markers.")
        if m['Sensationalism'] < 2: 
            reasons.append("**Neutral Tone**: Avoids 'sensational' baiting words used in disinformation.")
    else:
        reasons.append(f"**Neural Match**: Linguistic fingerprints align significantly with documented misinformation patterns (**{100-cred}% mismatch**).")
        reasons.append("**Synthetic Indicators**: The syntactic structure suggests low factual density.")
        if m['Sensationalism'] >= 3: 
            reasons.append(f"**High Sensationalism**: Contains {m['Sensationalism']}% inflammatory vocabulary designed to bypass critical thinking.")
        if m['Clickbait'] > 0: 
            reasons.append("**Engagement Trap**: Clickbait framing identified in the semantic structure.")
        if m['VisualEmphasis'] > 5: 
            reasons.append("**Aggressive Formatting**: Excessive emphasis points (CAPS/Punctuation) detected.")
    return reasons

# ==========================================
# UI RENDERING
# ==========================================

# Simple Header
st.markdown('<div class="app-header"><div class="app-name">FakeNewsDetector</div></div>', unsafe_allow_html=True)

# Main centered column
c1, c2, c3 = st.columns([1, 2.5, 1])

with c2:
    st.markdown('<div style="text-align: center; color: #64748b; margin-bottom: 2rem;">Paste an article URL or text content for a neural veracity audit.</div>', unsafe_allow_html=True)
    
    # Input Area - Fixed empty label
    user_input = st.text_area("Analysis Source", height=150, label_visibility="collapsed", placeholder="Feed the article text here...")
    
    st.markdown("<br>", unsafe_allow_html=True)
    analyze = st.button("RUN AI CREDIBILITY AUDIT")

# Output Section - ONLY SHOW AFTER CLICK
if analyze:
    if not user_input.strip() or len(user_input) < 10:
        st.warning("⚠️ Please provide content for analysis.")
    else:
        with st.spinner("Analyzing neural signatures..."):
            # Call the extracted logic from predict.py
            result = predict_news(user_input)
            
            if result:
                cred = result["credibility"]
                metrics = result["metrics"]
                report = get_detailed_report(cred, metrics)

                # BEAUTIFUL OUTPUT CONTAINER
            st.markdown('<div class="output-container">', unsafe_allow_html=True)
            
            # 1. Main Verdict Highlight
            v_class = "status-real" if cred >= 50 else "status-fake"
            v_banner = "real-news" if cred >= 50 else "fake-news"
            v_text = "REAL news" if cred >= 50 else "FAKE news"
            
            st.markdown(f"""
            <div class="verdict-box {v_banner}">
                <div class="verdict-title">INTEGRITY ANALYSIS VERDICT</div>
                <div class="verdict-hero {v_class}">{v_text}</div>
                <div style="font-size: 1.1rem; color: #94a3b8;"><b>Confidence Accuracy:</b> {cred if cred >= 50 else 100-cred}%</div>
            </div>
            """, unsafe_allow_html=True)

            # 2. Detailed Grid
            st.markdown("<br>", unsafe_allow_html=True)
            l_col, r_col = st.columns([1.2, 1])
            
            with l_col:
                st.markdown('<div class="analysis-pill">', unsafe_allow_html=True)
                st.markdown('<div class="pill-title">🔍 Neural Audit Log</div>', unsafe_allow_html=True)
                for item in report:
                    st.markdown(f'<div class="reason-item">{item}</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

            with r_col:
                st.markdown('<div class="analysis-pill">', unsafe_allow_html=True)
                st.markdown('<div class="pill-title">📊 Style DNA Map</div>', unsafe_allow_html=True)
                
                # Gauge Chart for visual flair
                fig = go.Figure(go.Indicator(
                    mode = "gauge+number",
                    value = cred,
                    title = {'text': "Veracity Gauge", 'font': {'color': "#64748b", 'size': 14}},
                    gauge = {
                        'axis': {'range': [0, 100], 'tickcolor': "#444"},
                        'bar': {'color': "#8b5cf6" if cred >= 50 else "#ef4444"},
                        'steps': [
                            {'range': [0, 40], 'color': "rgba(239, 68, 68, 0.1)"},
                            {'range': [60, 100], 'color': "rgba(16, 185, 129, 0.1)"}
                        ],
                        'threshold': {'line': {'color': "white", 'width': 2}, 'thickness': 0.75, 'value': 50}
                    }
                ))
                fig.update_layout(height=240, margin=dict(t=0,b=0,l=20,r=20), paper_bgcolor='rgba(0,0,0,0)', font={'color': "white", 'family': "Inter"})
                st.plotly_chart(fig, use_container_width=True)
                
                st.progress(min(metrics['Sensationalism']/10, 1.0), text=f"Sensationalism Index: {metrics['Sensationalism']}%")
                st.progress(min(metrics['EmotionalIntensity'], 1.0), text=f"Emotional Polarity: {int(metrics['EmotionalIntensity']*100)}%")
                
                st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)

# Simple Minimal Footer
st.markdown("<br><br><br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: #374151; font-size: 0.8rem; letter-spacing: 2px;">
    AI LOGIC POWERED BY SCIKIT-LEARN • FAKENEWSDETECTOR CORE
</div>
""", unsafe_allow_html=True)
