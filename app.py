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
        --card-bg: rgba(15, 25, 50, 0.7);
        --text-main: #f8fafc;
        --text-muted: #94a3b8;
        --accent-glow: rgba(0, 210, 255, 0.3);
    }

    * {
        margin: 0;
        padding: 0;
    }

    /* CUSTOM BACKGROUND IMAGE */
    html, body, [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), 
                          url("https://static.vecteezy.com/system/resources/thumbnails/072/972/723/small/digital-technology-abstract-background-with-glowing-circuit-board-pattern-representing-modern-connectivity-and-future-innovation-in-dark-blue-color-photo.jpeg") !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        color: white !important;
    }

    [data-testid="stAppViewContainer"] {
        color: white;
    }

    /* Navbar */
    .nav-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background: linear-gradient(180deg, rgba(10, 14, 39, 0.98) 0%, rgba(10, 14, 39, 0.85) 100%);
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
        color: #94a3b8;
        text-decoration: none;
        font-weight: 700;
        font-size: 0.9rem;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        text-transform: uppercase;
        letter-spacing: 2px;
        position: relative;
        font-family: 'Space Mono', monospace;
        padding: 0.5rem 0;
    }

    .nav-link::before {
        content: '';
        position: absolute;
        bottom: -5px;
        left: 0;
        width: 0;
        height: 2px;
        background: linear-gradient(90deg, #00d2ff, #ff006e);
        transition: width 0.4s ease;
    }

    .nav-link:hover {
        color: #00d2ff;
        text-shadow: 0 0 20px #00d2ff, 0 0 40px rgba(0, 210, 255, 0.5);
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
        color: #00d2ff;
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
        letter-spacing: -1px;
    }

    @keyframes titleGlow {
        0%, 100% { filter: drop-shadow(0 0 20px rgba(0, 210, 255, 0.3)); }
        50% { filter: drop-shadow(0 0 40px rgba(181, 55, 242, 0.5)); }
    }

    .hero-subtitle {
        font-size: 1.3rem;
        color: #f8fafc;
        max-width: 900px;
        margin: 0 auto 3rem auto;
        line-height: 1.8;
        text-align: center;
        text-shadow: 0 2px 4px rgba(0,0,0,0.5);
    }

    /* Buttons Styling */
    .secondary-btn, div.stDownloadButton > button {
        background: rgba(0, 210, 255, 0.1) !important;
        color: #00d2ff !important;
        padding: 0.8rem 2rem !important;
        border-radius: 12px !important;
        text-decoration: none !important;
        font-weight: 700 !important;
        border: 2px solid rgba(0, 210, 255, 0.4) !important;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
        font-family: 'Space Mono', monospace !important;
        letter-spacing: 1px !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        height: auto !important;
        width: auto !important;
        cursor: pointer !important;
        line-height: 1.2 !important;
    }

    .secondary-btn:hover, div.stDownloadButton > button:hover {
        background: rgba(0, 210, 255, 0.25) !important;
        border-color: #00d2ff !important;
        color: white !important;
        transform: translateY(-3px) !important;
        box-shadow: 0 0 30px rgba(0, 210, 255, 0.4) !important;
    }

    /* Force Download Button to look like others */
    div.stDownloadButton > button {
        margin: 0 !important;
        font-size: 0.9rem !important;
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
        background: linear-gradient(90deg, #00d2ff, #b537f2, #ff006e);
        margin: 0 auto;
        border-radius: 2px;
        box-shadow: 0 0 20px rgba(0, 210, 255, 0.5);
    }

    /* Cards */
    .glass-card {
        background: linear-gradient(135deg, rgba(15, 25, 50, 0.85), rgba(30, 41, 59, 0.7));
        backdrop-filter: blur(15px);
        border: 2px solid rgba(0, 210, 255, 0.2);
        border-radius: 20px;
        padding: 2.5rem;
        margin-bottom: 2.5rem;
        transition: all 0.4s ease;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }

    .glass-card:hover {
        border-color: rgba(0, 210, 255, 0.5);
        transform: translateY(-5px);
        box-shadow: 0 0 40px rgba(0, 210, 255, 0.2);
    }

    .tag {
        background: linear-gradient(135deg, rgba(0, 210, 255, 0.2), rgba(181, 55, 242, 0.2));
        color: #00d2ff;
        padding: 0.5rem 1rem;
        border-radius: 50px;
        font-size: 0.8rem;
        font-weight: 700;
        border: 1px solid rgba(0, 210, 255, 0.3);
        font-family: 'Space Mono', monospace;
    }

    .video-wrapper {
        border-radius: 16px;
        overflow: hidden;
        border: 2px solid rgba(0, 210, 255, 0.3);
        box-shadow: 0 0 30px rgba(0, 210, 255, 0.2);
    }

    .footer {
        padding: 5rem 2rem;
        margin-top: 8rem;
        border-top: 2px solid rgba(0, 210, 255, 0.2);
        text-align: center;
        background: rgba(10, 14, 39, 0.9);
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Responsive */
    @media (max-width: 768px) {
        .hero-title { font-size: 2.5rem; }
        .nav-container { gap: 1rem; padding: 0.8rem; flex-wrap: wrap; }
        .nav-link { font-size: 0.7rem; }
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

# --- BUTTONS ---
col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 1, 1, 1, 1, 1, 1])

with col3:
    st.markdown(
        '<a href="https://www.linkedin.com/in/rayyan-ahmed-504725321/" target="_blank" class="secondary-btn">LinkedIn</a>',
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        '<a href="https://github.com/introverthacker11" target="_blank" class="secondary-btn">GitHub</a>',
        unsafe_allow_html=True
    )

with col5:
    try:
        with open("RayyanAhmedResume.pdf", "rb") as file:
            st.download_button(
                label="Resume",
                data=file,
                file_name="Rayyan_Ahmed_Resume.pdf",
                mime="application/pdf",
            )
    except:
        st.info("Resume not found")

st.write("")  # Spacer

# --- ABOUT SECTION ---
st.markdown('<div class="section-header"><h2 class="section-title">About Me</h2><div class="section-divider"></div></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    st.markdown("""
    <div class="glass-card">
        <p style="font-size: 1.1rem; line-height: 1.8; color: #e2e8f0; text-align: center;">
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

# --- SKILLS SECTION ---
st.markdown(
    '<div class="section-header"><h2 class="section-title">Skills & Expertise</h2><div class="section-divider"></div></div>',
    unsafe_allow_html=True
)

skill_categories = {
    "Core AI": ["Machine Learning", "Deep Learning", "Reinforcement Learning", "Model Evaluation"],
    "Gen AI": ["LLMs", "Generative AI", "Prompt Engineering", "RAG", "AI Agents", "Fine-Tuning"],
    "NLP & Vision": ["NLP", "Computer Vision", "Feature Engineering", "Data Preprocessing"],
    "Data": ["Data Analysis", "Visualization", "SQL", "Pandas", "Scikit-learn"],
    "Engineering": ["Python", "Streamlit", "MLOps", "Model Deployment", "APIs"],
    "Tools": ["TensorFlow", "Keras", "Git", "Full Stack"]
}

all_skills = [item for sublist in skill_categories.values() for item in sublist]
col1, col2, col3, col4, col5, col6 = st.columns([1, 2, 2, 2, 2, 1])
skill_cols = [col2, col3, col4, col5]

for i, skill in enumerate(all_skills):
    with skill_cols[i % 4]:
        st.markdown(
            f"""
            <div class="glass-card" style="
                text-align: center; padding: 12px 5px; margin-bottom: 12px;
                font-size: 0.85rem; font-weight: 600; color: #e5e7eb;
                border: 1px solid rgba(0, 210, 255, 0.3); border-radius: 10px;
                background: rgba(0, 210, 255, 0.05);
            ">
                {skill}
            </div>
            """,
            unsafe_allow_html=True
        )

# --- EXPERIENCE SECTION ---
st.markdown('<div id="experience" class="section-header"><h2 class="section-title">Experience</h2><div class="section-divider"></div></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    experiences = [
        {
          "title": "AI Model Developer",
          "company": "Techware Hub",
          "date": "Dec 2025 - Feb 2026",
          "points": [
            "Engineered end-to-end AI solutions using Python across Machine Learning, Computer Vision, and Natural Language Processing domains.",
            "Developed and integrated Large Language Models (LLMs) with Retrieval-Augmented Generation (RAG) pipelines for intelligent data-driven applications.",
            "Built and orchestrated workflows using LangChain and Agentic AI architectures for autonomous task execution.",
            "Designed data processing and visualization pipelines to support model training and insight generation."
          ]
        },

        {
          "title": "ML & Data Science Team Member",
          "company": "NASA Official Space Apps Challenge 2025 - (Project selected in the top 1,900 out of 18,500+ international submissions)",
          "date": "July 2025 – Sept 2025",
          "points": [
            "Developed a weather-focused ML solution using NASA POWER API for real-world climate data ingestion.",
            "Performed data gathering and cleaning using Excel and SQL, followed by preprocessing for model readiness.",
            "Applied Pandas and Seaborn for data visualization and exploratory analysis.",
            "Built machine learning models for training and predictive insights.",
            "Deployed the solution using Streamlit for interactive user access.",
          ]
        },

        {
          "title": "Data Science Intern",
          "company": "British Airways (Virtual)",
          "date": "Oct 2024 – Nov 2024",
          "points": [
            "Developed a web scraping pipeline using Python to collect customer review data.",
            "Performed data cleaning and preprocessing to ensure data quality and consistency.",
            "Conducted exploratory data analysis (EDA) to uncover trends and patterns.",
            "Applied sentiment analysis using NLTK and VADER to quantify customer satisfaction.",
            "Built machine learning models (Random Forest, XGBoost) for predictive analysis.",
            "Used Mutual Information for feature selection to improve model performance."
          ]
        },

        {
          "title": "Data Visualization Intern",
          "company": "TATA Group (Virtual)",
          "date": "Sept 2024 – Oct 2024",
          "points": [
            "Performed data cleaning and transformation, followed by EDA to uncover key business insights from complex datasets.",
            "Developed data visualizations and built interactive dashboards using Power BI and Tableau for business intelligence reporting."
          ]
        },
        
    ]
    
    for exp in experiences:
        st.markdown(f"""
        <div class="glass-card">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
                <div>
                    <h3 style="margin: 0; color: #fff; font-size: 1.3rem;">{exp['company']}</h3>
                    <p style="margin: 0; color: #00d2ff; font-weight: 700;">{exp['title']}</p>
                </div>
                <span style="color: #94a3b8; font-family: 'Space Mono', monospace;">{exp['date']}</span>
            </div>
            <ul style="color: #cbd5e1; line-height: 1.6;">
                {''.join([f'<li>{p}</li>' for p in exp['points']])}
            </ul>
        </div>
        """, unsafe_allow_html=True)

# --- PROJECTS SECTION ---
st.markdown('<div id="projects" class="section-header"><h2 class="section-title">Projects</h2><div class="section-divider"></div></div>', unsafe_allow_html=True)

def project_item(title, desc, tags, video_path, github_url):
    col, col_text, col_vid, cool = st.columns([0.2, 1.5, 1, 0.2], gap="medium")
    with col_text:
        st.markdown(f"""
        <div class="project-content">
            <h3 style="color: #fff; margin-top: 0;">{title}</h3>
            <p style="color: #cbd5e1; font-size: 0.95rem;">{desc}</p>
            <div class="tag-container" style="margin-bottom: 1.5rem;">
                {''.join([f'<span class="tag">{tag}</span>' for tag in tags])}
            </div>
            <a href="{github_url}" target="_blank" class="secondary-btn">View Code ↗</a>
        </div>
        """, unsafe_allow_html=True)
    with col_vid:
        st.markdown('<div class="video-wrapper">', unsafe_allow_html=True)
        try:
            st.video(video_path)
        except:
            st.info(f"Video: {title}")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("<hr style='border: 1px solid rgba(0, 210, 255, 0.1); margin: 3rem 0;'>", unsafe_allow_html=True)

projects = [
    ("1️⃣ AI VisionLock", "Real-time object tracking system.", ["CompVision", "OpenCV", "Tracking"], "video2_finaloutput.mp4", "https://github.com/introverthacker11/CompVision-AIVisionLock-ObjectTrackingSystem___r38"),
    ("2️⃣ Face Verification", "Secure identity authentication system.", ["YOLOv8", "Deep Learning"], "faceVS.mp4", "https://github.com/introverthacker11/CompVision-FaceVerificationSystem___r35"),
    ("3️⃣ UrbanSeg-AI", "Semantic segmentation for urban environments.", ["YOLOv8", "Segmentation"], "city view output.mp4", "https://github.com/introverthacker11/CompVision-UrbanSegAI___r37"),
    ("4️⃣ SafeSight-AI", "PPE detection and tracking system.", ["YOLOv8", "Safety"], "ppe_detected.mp4", "https://github.com/introverthacker11/CompVision-SafeSightAI-PPE-DetectionSystem___r36"),
    ("5️⃣ AI-GeoVisionID", "Real-time world leader face recognition.", ["ArcFace", "DeepFace"], "output_world_leaders_arrive.mp4", "https://github.com/introverthacker11/CompVision-AI-GeoVisionID-FaceRecognitionSystem"),
    ("6️⃣ PSO-FinanceBot", "RAG-powered financial report analyzer.", ["RAG", "Llama 3.2", "FAISS"], "pso_video.mp4", "https://github.com/introverthacker11/PSO-FinanceBot-RAG"),
    ("7️⃣ AI-DataAnalyst", "MCP-based automated data analysis agent.", ["MCP", "Llama 3.2", "Pandas"], "ai_data_analyst.mp4", "https://github.com/introverthacker11/AI-DataAnalyst-MCP")
]

for p in projects:
    project_item(*p)

# --- EDUCATION & CREDENTIALS ---
st.markdown('<div id="education" class="section-header"><h2 class="section-title">Education</h2><div class="section-divider"></div></div>', unsafe_allow_html=True)
st.markdown("""
<div class="glass-card" style="text-align: center; max-width: 800px; margin: 0 auto;">
    <h3 style="color: #fff;">Dawood University of Engineering and Technology</h3>
    <p style="color: #00d2ff; font-weight: 700; font-size: 1.2rem;">Bachelor of Science in Artificial Intelligence</p>
    <p style="color: #94a3b8; font-family: 'Space Mono', monospace;">2022 — 2026</p>
</div>
""", unsafe_allow_html=True)

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
            <h4 style="margin: 0 0 0.5rem 0; color: #fff;">{cred['title']}</h4>
            <p style="margin: 0 0 1rem 0; color: #00d2ff; font-size: 0.9rem;">{cred['org']}</p>
            <a href="{cred['link']}" target="_blank" class="secondary-btn" style="padding: 0.4rem 1rem; font-size: 0.8rem;">Verify</a>
        </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div class="footer">
    <h3 style="margin-bottom: 0.5rem;">Rayyan Ahmed</h3>
    <p style="color: #94a3b8; margin-bottom: 2rem;">AI Engineer & Problem Solver</p>
    <div style="display: flex; justify-content: center; gap: 2rem; margin-bottom: 2rem;">
        <a href="https://www.linkedin.com/in/rayyan-ahmed-504725321/" target="_blank" style="color: #00d2ff; text-decoration: none; font-weight: 700;">LinkedIn</a>
        <a href="https://github.com/CodingRayyan" target="_blank" style="color: #00d2ff; text-decoration: none; font-weight: 700;">GitHub</a>
    </div>
    <p style="font-size: 0.8rem; color: #94a3b8;">© 2026 Rayyan Ahmed.</p>
</div>
""", unsafe_allow_html=True)
