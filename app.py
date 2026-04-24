import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Rayyan Ahmed | AI Engineer Portfolio",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- CUSTOM CSS WITH FUTURISTIC ENHANCEMENTS ---
def local_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Poppins:wght@400;600;700&family=Space+Mono:wght@400;700&display=swap');

    :root {
        --primary-color: #00d2ff;
        --secondary-color: #3a7bd5;
        --accent-color: #ff006e;
        --neon-purple: #b537f2;
        --neon-pink: #ff006e;
        --bg-color: #0a0e27;
        --card-bg: rgba(15, 25, 50, 0.6);
        --text-main: #f8fafc;
        --text-muted: #94a3b8;
        --accent-glow: rgba(0, 210, 255, 0.3);
    }

    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0f172a 100%);
        background-attachment: fixed;
        color: white;
        position: relative;
        overflow-x: hidden;
    }

    /* Animated Background Grid */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            linear-gradient(0deg, transparent 24%, rgba(0, 210, 255, 0.05) 25%, rgba(0, 210, 255, 0.05) 26%, transparent 27%, transparent 74%, rgba(0, 210, 255, 0.05) 75%, rgba(0, 210, 255, 0.05) 76%, transparent 77%, transparent),
            linear-gradient(90deg, transparent 24%, rgba(0, 210, 255, 0.05) 25%, rgba(0, 210, 255, 0.05) 26%, transparent 27%, transparent 74%, rgba(0, 210, 255, 0.05) 75%, rgba(0, 210, 255, 0.05) 76%, transparent 77%, transparent);
        background-size: 50px 50px;
        pointer-events: none;
        z-index: 0;
        animation: gridShift 20s linear infinite;
    }

    @keyframes gridShift {
        0% { transform: translateY(0); }
        100% { transform: translateY(50px); }
    }

    /* Floating Particles */
    .particle {
        position: fixed;
        pointer-events: none;
        z-index: 1;
    }

    /* Navbar */
    .nav-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background: linear-gradient(180deg, rgba(10, 14, 39, 0.95) 0%, rgba(10, 14, 39, 0.8) 100%);
        backdrop-filter: blur(20px);
        z-index: 1000;
        padding: 1.2rem 2rem;
        display: flex;
        justify-content: center;
        gap: 3rem;
        border-bottom: 2px solid rgba(0, 210, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 210, 255, 0.1);
    }

    .nav-link {
        color: var(--text-muted);
        text-decoration: none;
        font-weight: 700;
        font-size: 0.9rem;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        text-transform: uppercase;
        letter-spacing: 2px;
        position: relative;
        font-family: 'Space Mono', monospace;
    }

    .nav-link::before {
        content: '';
        position: absolute;
        bottom: -5px;
        left: 0;
        width: 0;
        height: 2px;
        background: linear-gradient(90deg, var(--primary-color), var(--neon-pink));
        transition: width 0.4s ease;
    }

    .nav-link:hover {
        color: var(--primary-color);
        text-shadow: 0 0 20px var(--primary-color), 0 0 40px rgba(0, 210, 255, 0.5);
        transform: translateY(-2px);
    }

    .nav-link:hover::before {
        width: 100%;
    }

    /* Hero Section */
    .hero-container {
        padding: 10rem 2rem 4rem 2rem;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        position: relative;
        z-index: 10;
    }

    .hero-badge {
        background: linear-gradient(135deg, rgba(0, 210, 255, 0.15), rgba(181, 55, 242, 0.15));
        color: var(--primary-color);
        padding: 0.7rem 1.5rem;
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 2rem;
        border: 2px solid rgba(0, 210, 255, 0.4);
        box-shadow: 0 0 20px rgba(0, 210, 255, 0.2), inset 0 0 20px rgba(0, 210, 255, 0.1);
        animation: badgePulse 3s ease-in-out infinite;
        font-family: 'Space Mono', monospace;
        letter-spacing: 1px;
    }

    @keyframes badgePulse {
        0%, 100% { 
            box-shadow: 0 0 20px rgba(0, 210, 255, 0.2), inset 0 0 20px rgba(0, 210, 255, 0.1);
            transform: scale(1);
        }
        50% { 
            box-shadow: 0 0 40px rgba(0, 210, 255, 0.4), inset 0 0 30px rgba(0, 210, 255, 0.2);
            transform: scale(1.05);
        }
    }

    .hero-title {
        font-family: 'Poppins', sans-serif;
        font-size: 4.5rem;
        font-weight: 900;
        margin-bottom: 1.5rem;
        background: linear-gradient(135deg, #00d2ff 0%, #b537f2 50%, #ff006e 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: titleGlow 3s ease-in-out infinite;
        text-shadow: 0 0 30px rgba(0, 210, 255, 0.3);
        letter-spacing: -1px;
    }

    @keyframes titleGlow {
        0%, 100% { filter: drop-shadow(0 0 20px rgba(0, 210, 255, 0.3)); }
        50% { filter: drop-shadow(0 0 40px rgba(181, 55, 242, 0.5)); }
    }

    .hero-subtitle {
        font-size: 1.3rem;
        color: var(--text-muted);
        max-width: 900px;
        margin: 0 auto 3rem auto;
        line-height: 1.8;
        text-align: center;
        animation: fadeInUp 1s ease-out 0.3s both;
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* Buttons */
    .btn-container {
        display: flex;
        justify-content: center;
        gap: 2rem;
    }

    .primary-btn {
        background: linear-gradient(135deg, var(--primary-color), var(--neon-purple));
        color: white;
        padding: 1rem 2.5rem;
        border-radius: 12px;
        text-decoration: none;
        font-weight: 700;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        box-shadow: 0 0 20px rgba(0, 210, 255, 0.4), 0 8px 20px rgba(0, 210, 255, 0.2);
        border: 2px solid rgba(0, 210, 255, 0.3);
        position: relative;
        overflow: hidden;
        font-family: 'Space Mono', monospace;
        letter-spacing: 1px;
    }

    .primary-btn::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.5s;
    }

    .primary-btn:hover {
        transform: translateY(-5px) scale(1.05);
        box-shadow: 0 0 40px rgba(0, 210, 255, 0.6), 0 15px 40px rgba(0, 210, 255, 0.3);
        border-color: var(--primary-color);
    }

    .primary-btn:hover::before {
        left: 100%;
    }

    .secondary-btn {
        background: rgba(0, 210, 255, 0.08);
        color: var(--primary-color);
        padding: 1rem 2.5rem;
        border-radius: 12px;
        text-decoration: none;
        font-weight: 700;
        border: 2px solid rgba(0, 210, 255, 0.4);
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        position: relative;
        overflow: hidden;
        font-family: 'Space Mono', monospace;
        letter-spacing: 1px;
    }

    .secondary-btn::after {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        background: rgba(0, 210, 255, 0.2);
        border-radius: 50%;
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }

    .secondary-btn:hover {
        background: rgba(0, 210, 255, 0.15);
        border-color: var(--primary-color);
        color: white;
        transform: translateY(-3px);
        box-shadow: 0 0 30px rgba(0, 210, 255, 0.3);
    }

    .secondary-btn:hover::after {
        width: 300px;
        height: 300px;
    }

    /* Section Headers */
    .section-header {
        margin: 8rem 0 4rem 0;
        text-align: center;
        position: relative;
        z-index: 10;
    }

    .section-title {
        font-size: 3rem;
        font-weight: 900;
        margin-bottom: 1.5rem;
        background: linear-gradient(135deg, #00d2ff 0%, #b537f2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -1px;
    }

    .section-divider {
        width: 80px;
        height: 4px;
        background: linear-gradient(90deg, var(--primary-color), var(--neon-purple), var(--neon-pink));
        margin: 0 auto;
        border-radius: 2px;
        box-shadow: 0 0 20px rgba(0, 210, 255, 0.5);
        animation: dividerExpand 2s ease-in-out infinite;
    }

    @keyframes dividerExpand {
        0%, 100% { width: 80px; }
        50% { width: 120px; }
    }

    /* Cards */
    .glass-card {
        background: linear-gradient(135deg, rgba(15, 25, 50, 0.7), rgba(30, 41, 59, 0.5));
        backdrop-filter: blur(15px);
        border: 2px solid rgba(0, 210, 255, 0.2);
        border-radius: 20px;
        padding: 2.5rem;
        margin-bottom: 2.5rem;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        position: relative;
        overflow: hidden;
        box-shadow: 0 8px 32px rgba(0, 210, 255, 0.1);
    }

    .glass-card::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 100%;
        height: 100%;
        background: radial-gradient(circle, rgba(0, 210, 255, 0.1) 0%, transparent 70%);
        transition: all 0.6s ease;
        opacity: 0;
    }

    .glass-card:hover {
        border-color: rgba(0, 210, 255, 0.5);
        transform: translateY(-8px) scale(1.02);
        background: linear-gradient(135deg, rgba(15, 25, 50, 0.9), rgba(30, 41, 59, 0.7));
        box-shadow: 0 0 40px rgba(0, 210, 255, 0.3), 0 15px 40px rgba(0, 210, 255, 0.15);
    }

    .glass-card:hover::before {
        opacity: 1;
        top: -25%;
        right: -25%;
    }

    /* Project Cards */
    .project-card {
        background: linear-gradient(135deg, rgba(15, 25, 50, 0.7), rgba(30, 41, 59, 0.5));
        border-radius: 20px;
        overflow: hidden;
        border: 2px solid rgba(0, 210, 255, 0.2);
        margin-bottom: 3rem;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        position: relative;
        box-shadow: 0 8px 32px rgba(0, 210, 255, 0.1);
    }
    
    .project-card:hover {
        border-color: rgba(0, 210, 255, 0.5);
        transform: translateY(-10px);
        box-shadow: 0 0 40px rgba(0, 210, 255, 0.3), 0 20px 40px rgba(0, 210, 255, 0.15);
    }

    .project-content {
        padding: 2rem;
        position: relative;
        z-index: 2;
    }

    .tag-container {
        display: flex;
        flex-wrap: wrap;
        gap: 0.7rem;
        margin-top: 1.5rem;
    }

    .tag {
        background: linear-gradient(135deg, rgba(0, 210, 255, 0.15), rgba(181, 55, 242, 0.15));
        color: var(--primary-color);
        padding: 0.5rem 1rem;
        border-radius: 50px;
        font-size: 0.8rem;
        font-weight: 700;
        border: 1px solid rgba(0, 210, 255, 0.3);
        transition: all 0.3s ease;
        font-family: 'Space Mono', monospace;
        letter-spacing: 0.5px;
    }

    .tag:hover {
        background: linear-gradient(135deg, rgba(0, 210, 255, 0.3), rgba(181, 55, 242, 0.3));
        box-shadow: 0 0 15px rgba(0, 210, 255, 0.3);
        transform: scale(1.1);
    }

    /* Video Sizing */
    .video-wrapper {
        width: 100%;
        max-width: 400px;
        margin: 0 auto;
        border-radius: 16px;
        overflow: hidden;
        border: 2px solid rgba(0, 210, 255, 0.3);
        box-shadow: 0 0 30px rgba(0, 210, 255, 0.2);
        transition: all 0.4s ease;
    }

    .video-wrapper:hover {
        box-shadow: 0 0 50px rgba(0, 210, 255, 0.4);
        transform: scale(1.05);
    }

    /* Footer */
    .footer {
        padding: 5rem 2rem;
        margin-top: 8rem;
        border-top: 2px solid rgba(0, 210, 255, 0.2);
        text-align: center;
        color: var(--text-muted);
        background: linear-gradient(180deg, transparent, rgba(0, 210, 255, 0.05));
        position: relative;
        z-index: 10;
    }

    .footer h3 {
        background: linear-gradient(135deg, #00d2ff, #b537f2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Glitch Effect */
    @keyframes glitch {
        0% { transform: translate(0); }
        20% { transform: translate(-2px, 2px); }
        40% { transform: translate(-2px, -2px); }
        60% { transform: translate(2px, 2px); }
        80% { transform: translate(2px, -2px); }
        100% { transform: translate(0); }
    }

    .glitch-text {
        animation: glitch 0.3s ease-in-out;
    }

    /* Responsive */
    @media (max-width: 768px) {
        .hero-title { font-size: 2.5rem; }
        .section-title { font-size: 2rem; }
        .nav-container { gap: 1rem; padding: 0.8rem; flex-wrap: wrap; }
        .nav-link { font-size: 0.7rem; letter-spacing: 0.5px; }
        .hero-subtitle { font-size: 1rem; }
    }

    /* Smooth Scrolling */
    html {
        scroll-behavior: smooth;
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
    }

    ::-webkit-scrollbar-track {
        background: rgba(0, 210, 255, 0.05);
    }

    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, var(--primary-color), var(--neon-purple));
        border-radius: 5px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, var(--neon-purple), var(--neon-pink));
        box-shadow: 0 0 20px rgba(0, 210, 255, 0.5);
    }

    </style>
    """, unsafe_allow_html=True)

local_css()

# --- NAVBAR ---
st.markdown("""
<div class="nav-container">
    <a href="#intro" class="nav-link">Intro</a>
    <a href="#experience" class="nav-link">Experience</a>
    <a href="#projects" class="nav-link">Projects</a>
    <a href="#education" class="nav-link">Education</a>
    <a href="#credentials" class="nav-link">Credentials</a>
</div>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("""
<div class="hero-container" id="intro">
    <div class="hero-badge">⚡ AVAILABLE FOR OPPORTUNITIES</div>
    <h1 class="hero-title">Rayyan Ahmed</h1>
    <p class="hero-subtitle">
        AI Engineer & Problem Solver specializing in <b>AI Development</b> and <b>AI Automation</b>. <br>
        Transforming complex data into intelligent, end-to-end AI products.
    </p>
</div>
""", unsafe_allow_html=True)

# --------

col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)

with col4:
    st.markdown(
        '<a href="https://www.linkedin.com/in/rayyan-ahmed-504725321/" target="_blank" class="secondary-btn">LinkedIn</a>',
        unsafe_allow_html=True
    )

with col5:
    st.markdown(
        '<a href="https://github.com/introverthacker11" target="_blank" class="secondary-btn">GitHub</a>',
        unsafe_allow_html=True
    )

with col6:
    try:
        with open("RayyanAhmedResume.pdf", "rb") as file:
            st.download_button(
                label="Download Resume",
                data=file,
                file_name="Rayyan_Ahmed_Resume.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    except:
        st.info("Resume file not found")

# --- INTRO SECTION ---
st.markdown('<div class="section-header"><h2 class="section-title">About Me</h2><div class="section-divider"></div></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    st.markdown("""
    <div class="glass-card">
        <p style="font-size: 1.1rem; line-height: 1.8; color: #cbd5e1; text-align: center;">
            I'm Rayyan, an AI Engineer dedicated to architecting end-to-end RAG systems, agentic workflows, and high-performance Generative AI applications. 
            What excites me most isn't just model deployment—it's diving into the mechanics of why they perform, from fine-tuning dynamics to the nuances of latent space. 
            I thrive on bridging deep theoretical research with practical, production-ready AI solutions.
            <br><br>
            I excel in building in the "gray area" where benchmarks are undefined. My most rewarding projects involve engineering through technical ambiguity—optimizing 
            local LLM inference or scaling complex data pipelines. I've found that true innovation in AI stems from a mix of rigorous curiosity and the persistence 
            to debug until a vision becomes a functional reality.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- skills -----------------

st.markdown(
    '<div class="section-header"><h2 class="section-title">Skills & Expertise</h2><div class="section-divider"></div></div>',
    unsafe_allow_html=True
)

# Expanded and Categorized Skills
skill_categories = {
    "Core AI & Modeling": [
        "Machine Learning", "Deep Learning", "Reinforcement Learning", 
        "Model Evaluation", "Research & Experimentation"
    ],
    "Generative AI & LLMs": [
        "Large Language Models (LLMs)", "Generative AI", "Prompt Engineering", 
        "RAG", "AI Agents", "Model Fine-Tuning"
    ],
    "NLP & Vision": [
        "Natural Language Processing (NLP)", "Computer Vision", 
        "Feature Engineering", "Data Preprocessing"
    ],
    "Data & Analytics": [
        "Data Analysis", "Data Visualization", "Statistical Analysis", 
        "Pandas / NumPy / SQL", "Scikit-learn"
    ],
    "Engineering & Ops": [
        "Python Development", "Streamlit / Web Dev", "MLOps", 
        "AI Model Deployment", "API Integration (REST / NASA)"
    ],
    "Tools & Frameworks": [
        "TensorFlow / Keras", "Git / GitHub", "Full Stack Development"
    ]
}

# Flattening the list for your existing grid logic, or you can iterate by category
all_skills = [item for sublist in skill_categories.values() for item in sublist]

col1, col2, col3, col4, col5, col6 = st.columns([1, 2, 2, 2, 2, 1])
skill_cols = [col2, col3, col4, col5]

for i, skill in enumerate(all_skills):
    with skill_cols[i % 4]:
        st.markdown(
            f"""
            <div class="glass-card" style="
                text-align: center;
                padding: 15px 8px;
                margin-bottom: 15px;
                font-size: 0.89rem;
                font-weight: 600;
                color: #e5e7eb;
                border: 2px solid rgba(0, 210, 255, 0.2);
                border-radius: 10px;
                background: linear-gradient(135deg, rgba(0, 210, 255, 0.08), rgba(181, 55, 242, 0.08));
                transition: all 0.3s ease;
                cursor: pointer;
            " onmouseover="this.style.boxShadow='0 0 20px rgba(0, 210, 255, 0.3)'; this.style.borderColor='rgba(0, 210, 255, 0.5)'; this.style.transform='scale(1.05)';" onmouseout="this.style.boxShadow='none'; this.style.borderColor='rgba(0, 210, 255, 0.2)'; this.style.transform='scale(1)';">
                {skill}
            </div>
            """,
            unsafe_allow_html=True
        )

# --- EXPERIENCE SECTION ---
st.markdown('<div id="experience" class="section-header"><h2 class="section-title">Experience</h2><div class="section-divider"></div></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    # TATA Group (Virtual)
    st.markdown("""
    <div class="glass-card">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
            <div>
                <h3 style="margin: 0; color: #fff; font-size: 1.3rem;">TATA Group (Virtual)</h3>
                <p style="margin: 0; color: var(--primary-color); font-weight: 700; font-size: 1rem;">Data Visualization Intern</p>
            </div>
            <span style="color: var(--text-muted); font-size: 0.9rem; font-family: 'Space Mono', monospace;">Sept 2024 – Oct 2024</span>
        </div>
        <ul style="color: #cbd5e1; line-height: 1.8; font-size: 0.95rem;">
            <li>Engineered data cleaning and transformation pipelines to handle complex, multi-source business datasets.</li>
            <li>Architected interactive dashboards using Power BI/Tableau to visualize core KPIs and revenue trends.</li>
            <li>Performed exploratory data analysis (EDA) to identify statistically significant patterns in global sales data.</li>
            <li>Developed technical visualizations to bridge the gap between raw data structures and executive business intelligence.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # British Airways (Virtual)
    st.markdown("""
    <div class="glass-card">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
            <div>
                <h3 style="margin: 0; color: #fff; font-size: 1.3rem;">British Airways (Virtual)</h3>
                <p style="margin: 0; color: var(--primary-color); font-weight: 700; font-size: 1rem;">Data Science Intern</p>
            </div>
            <span style="color: var(--text-muted); font-size: 0.9rem; font-family: 'Space Mono', monospace;">Oct 2024 – Nov 2024</span>
        </div>
        <ul style="color: #cbd5e1; line-height: 1.8; font-size: 0.95rem;">
            <li>Developed a web scraping pipeline using Python to extract and preprocess unstructured customer review data.</li>
            <li>Quantified customer satisfaction trends using NLTK/VADER sentiment analysis to identify service pain points.</li>
            <li>Engineered a predictive classification model to forecast customer booking behavior using advanced feature selection.</li>
            <li>Utilized Mutual Information (MI) scores to optimize model performance and identify key drivers of ticket conversions.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # NASA Space Apps
    st.markdown("""
    <div class="glass-card">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
            <div>
                <h3 style="margin: 0; color: #fff; font-size: 1.3rem;">NASA Space Apps Challenge</h3>
                <p style="margin: 0; color: var(--primary-color); font-weight: 700; font-size: 1rem;">ML & Data Science Team Member</p>
            </div>
            <span style="color: var(--text-muted); font-size: 0.9rem; font-family: 'Space Mono', monospace;">June 2025 – Sept 2025</span>
        </div>
        <ul style="color: #cbd5e1; line-height: 1.8; font-size: 0.95rem;">
            <li>Built a weather-focused ML solution in collaboration with teammates as part of the world's largest global hackathon.</li>
            <li>Project selected as a <b>Global Nominee</b>, ranking among the <b>top 1,900</b> out of 18500+ international projects globally.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- PROJECTS SECTION ---
st.markdown('<div id="projects" class="section-header"><h2 class="section-title">Projects</h2><div class="section-divider"></div></div>', unsafe_allow_html=True)

def project_item(title, desc, tags, video_path, github_url):
    col, col_text, col_vid, cool = st.columns([0.34, 1.5, 1, 0.34], gap="medium")
    with col_text:
        st.markdown(f"""
        <div class="project-content">
            <h3 style="color: #fff; margin-top: 0; font-size: 1.3rem;">{title}</h3>
            <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6;">{desc}</p>
            <div class="tag-container" style="margin-bottom: 1.5rem;">
                {''.join([f'<span class="tag">{tag}</span>' for tag in tags])}
            </div>
            <br>
            <a href="{github_url}" target="_blank" class="secondary-btn" 
            style="
                font-size: 0.95rem; 
                padding: 0.7rem 1.5rem; 
                text-decoration: none; 
                display: inline-block;
            ">
                View Source Code ↗
            </a>
        </div>
        """, unsafe_allow_html=True)
    with col_vid:
        st.markdown('<div class="video-wrapper">', unsafe_allow_html=True)
        try:
            st.video(video_path)
        except:
            st.info(f"Video: {title}")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("<hr style='border: 1px solid rgba(0, 210, 255, 0.2); margin: 2rem 0;'>", unsafe_allow_html=True)

# Project 1
project_item(
    "1️⃣ AI VisionLock",
    "AI VisionLock is a real-time single object tracking system that maintains accurate object localization across video frames, even under motion and partial occlusion.",
    ["CompVision", "OpenCV", "Template Matching", "Object Tracking", "Streamlit"],
    "video2_finaloutput.mp4",
    "https://github.com/introverthacker11/CompVision-AIVisionLock-ObjectTrackingSystem___r38"
)

# Project 2
project_item(
    "2️⃣ Face Verification System",
    "FaceVerify-AI is an AI-powered face verification system designed to provide secure and reliable identity authentication using computer vision and deep learning techniques.",
    ["CompVision", "OpenCV", "YOLOv8", "Deep Learning", "Python"],
    "faceVS.mp4",
    "https://github.com/introverthacker11/CompVision-FaceVerificationSystem___r35"
)

# Project 3
project_item(
    "3️⃣ UrbanSeg-AI",
    "UrbanSeg-AI is an AI-powered semantic and instance segmentation system for urban environments, capable of identifying roads, vehicles, buildings, and pedestrians in real time.",
    ["CompVision", "YOLOv8", "Instance Segmentation", "Python", "Streamlit"],
    "city view output.mp4",
    "https://github.com/introverthacker11/CompVision-UrbanSegAI___r37"
)

# Project 4
project_item(
    "4️⃣ SafeSight-AI",
    "SafeSight-AI is an AI-powered PPE detection and tracking system that identifies safety equipment such as helmets and vests in real time to improve workplace safety compliance.",
    ["CompVision", "YOLOv8", "PPE Detection", "Python", "Streamlit"],
    "ppe_detected.mp4",
    "https://github.com/introverthacker11/CompVision-SafeSightAI-PPE-DetectionSystem___r36"
)

# Project 5
project_item(
    "5️⃣ AI-GeoVisionID",
    "AI-GeoVisionID is a real-time face recognition system that detects and identifies world leaders from images and videos using deep facial embeddings, even under varying lighting and pose conditions.",
    ["Computer Vision", "YOLOv8", "ArcFace", "DeepFace", "OpenCV", "Streamlit", "Face Recognition"],
    "output_world_leaders_arrive.mp4",
    "https://github.com/introverthacker11/CompVision-AI-GeoVisionID-FaceRecognitionSystem"
)

# Project 6
project_item(
    "6️⃣ PSO-FinanceBot",
    "PSO-FinanceBot is a RAG-powered system for analyzing PSO annual reports (FY21–FY25). It uses a hybrid search approach, combining FAISS for semantic depth and BM25 for keyword precision, providing accurate financial insights via a local Llama 3.2 engine.",
    ["RAG", "Llama 3.2", "FAISS", "BM25", "LangChain", "Streamlit", "Python"],
    "pso_video.mp4",
    "https://github.com/introverthacker11/PSO-FinanceBot-RAG"
)

# Project 7
project_item(
    "7️⃣ AI-DataAnalyst-Agent",
    "An AI multi-tool agent leveraging the Model Context Protocol (MCP) and Llama 3.2 to perform dynamic data analysis, automated visualization, and statistical modeling on CSV/Excel files with fully local, secure Python execution.",
    ["MCP", "Llama 3.2", "Data Science", "Pandas", "Matplotlib", "Streamlit", "Ollama"],
    "ai_data_analyst.mp4",
    "https://github.com/introverthacker11/AI-DataAnalyst-MCP"
)

# --- EDUCATION SECTION ---
st.markdown('<div id="education" class="section-header"><h2 class="section-title">Education</h2><div class="section-divider"></div></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    st.markdown("""
    <div class="glass-card" style="text-align: center;">
        <h3 style="color: #fff; margin-bottom: 0.5rem; font-size: 1.3rem;">Dawood University of Engineering and Technology</h3>
        <p style="color: var(--primary-color); font-weight: 700; font-size: 1.2rem; margin-bottom: 1rem;">Bachelor of Science in Artificial Intelligence</p>
        <p style="color: var(--text-muted); margin-bottom: 1.5rem; font-family: 'Space Mono', monospace;">2022 — 2026</p>
    </div>
    """, unsafe_allow_html=True)

# --- CREDENTIALS SECTION ---
st.markdown('<div id="credentials" class="section-header"><h2 class="section-title">Credentials</h2><div class="section-divider"></div></div>', unsafe_allow_html=True)

cred_col1, cred_col2 = st.columns(2)
credentials = [
    {"title": "AI Prompt Engineering Specialist", "org": "Google · Coursera", "link": "https://www.coursera.org/account/accomplishments/specialization/90FPSDSJ86C6"},
    {"title": "LLM Fine-Tuning Specialist", "org": "IBM · Coursera", "link": "https://www.coursera.org/account/accomplishments/verify/3SSFD07A7F8J"},
    {"title": "Business Intelligence Professional", "org": "Google · Coursera", "link": "https://www.coursera.org/account/accomplishments/professional-cert/L838OXNUCGTF"}
]

for i, cred in enumerate(credentials):
    with cred_col1 if i % 2 == 0 else cred_col2:
        st.markdown(f"""
        <div class="glass-card" style="padding: 1.5rem;">
            <h4 style="margin: 0 0 0.5rem 0; color: #fff; font-size: 1.1rem;">{cred['title']}</h4>
            <p style="margin: 0 0 1rem 0; color: var(--primary-color); font-size: 0.9rem; font-family: 'Space Mono', monospace;">{cred['org']}</p>
            <a href="{cred['link']}" target="_blank" class="secondary-btn" style="padding: 0.4rem 1rem; font-size: 0.8rem; display: inline-block;">Verify</a>
        </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div class="footer">
    <div style="margin-bottom: 1.5rem;">
        <h3 style="margin-bottom: 0.5rem; font-size: 1.5rem;">Rayyan Ahmed</h3>
        <p style="color: var(--text-muted);">AI Engineer & Problem Solver</p>
    </div>
    <div style="display: flex; justify-content: center; gap: 2rem; margin-bottom: 2rem;">
        <a href="https://www.linkedin.com/in/rayyan-ahmed-504725321/" target="_blank" style="color: var(--primary-color); text-decoration: none; transition: all 0.3s ease; font-weight: 700;" onmouseover="this.style.textShadow='0 0 20px rgba(0, 210, 255, 0.5)'; this.style.transform='scale(1.1)';" onmouseout="this.style.textShadow='none'; this.style.transform='scale(1)';">LinkedIn</a>
        <a href="https://github.com/CodingRayyan" target="_blank" style="color: var(--primary-color); text-decoration: none; transition: all 0.3s ease; font-weight: 700;" onmouseover="this.style.textShadow='0 0 20px rgba(0, 210, 255, 0.5)'; this.style.transform='scale(1.1)';" onmouseout="this.style.textShadow='none'; this.style.transform='scale(1)';">GitHub</a>
        <a href="mailto:rayyanabeel22@gmail.com" style="color: var(--primary-color); text-decoration: none; transition: all 0.3s ease; font-weight: 700;" onmouseover="this.style.textShadow='0 0 20px rgba(0, 210, 255, 0.5)'; this.style.transform='scale(1.1)';" onmouseout="this.style.textShadow='none'; this.style.transform='scale(1)';">Email</a>
    </div>
    <p style="font-size: 0.8rem; color: var(--text-muted);">Website made by Rayyan Ahmed (Not AI).</p>
    <p style="font-size: 0.8rem; color: var(--text-muted);">© 2026 Rayyan Ahmed.</p>
</div>

""", unsafe_allow_html=True)
