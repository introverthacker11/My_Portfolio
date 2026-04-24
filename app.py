import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Rayyan Ahmed | AI Engineer Portfolio",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- CUSTOM CSS ---
def local_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Poppins:wght@400;600;700&display=swap');

    :root {
        --primary-color: #00d2ff;
        --secondary-color: #3a7bd5;
        --bg-color: #0f172a;
        --card-bg: rgba(30, 41, 59, 0.7);
        --text-main: #f8fafc;
        --text-muted: #94a3b8;
        --accent-glow: rgba(0, 210, 255, 0.3);
    }

    .stApp {
        background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
                      url("https://t4.ftcdn.net/jpg/02/22/68/39/360_F_222683930_mXWfHnOk9spCYOyEhqXNSWbWhZd4dFKF.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: white;
    }

    /* Navbar */
    .nav-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background: rgba(15, 23, 42, 0.8);
        backdrop-filter: blur(12px);
        z-index: 1000;
        padding: 1rem 2rem;
        display: flex;
        justify-content: center;
        gap: 2rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }

    .nav-link {
        color: var(--text-muted);
        text-decoration: none;
        font-weight: 600;
        font-size: 0.9rem;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .nav-link:hover {
        color: var(--primary-color);
        text-shadow: 0 0 10px var(--accent-glow);
    }

    /* Hero Section */
    .hero-container {
        padding: 8rem 2rem 4rem 2rem;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .hero-badge {
        background: rgba(0, 210, 255, 0.1);
        color: var(--primary-color);
        padding: 0.5rem 1.2rem;
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(0, 210, 255, 0.3);
    }

    .hero-title {
        font-family: 'Poppins', sans-serif;
        font-size: 4rem;
        font-weight: 800;
        margin-bottom: 1rem;
        background: linear-gradient(to right, #fff, #94a3b8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        font-size: 1.2rem;
        color: var(--text-muted);
        max-width: 800px;
        margin: 0 auto 2.5rem auto;
        line-height: 1.6;
        text-align: center;
    }

    /* Buttons */
    .btn-container {
        display: flex;
        justify-content: center;
        gap: 1.5rem;
    }

    .primary-btn {
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        color: white;
        padding: 0.8rem 2rem;
        border-radius: 12px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 210, 255, 0.3);
    }

    .primary-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0, 210, 255, 0.5);
    }

    .secondary-btn {
        background: rgba(255, 255, 255, 0.05);
        color: white;
        padding: 0.8rem 2rem;
        border-radius: 12px;
        text-decoration: none;
        font-weight: 600;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }

    .secondary-btn:hover {
        background: rgba(255, 255, 255, 0.1);
        border-color: var(--primary-color);
    }

    /* Section Headers */
    .section-header {
        margin: 6rem 0 3rem 0;
        text-align: center;
    }

    .section-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }

    .section-divider {
        width: 60px;
        height: 4px;
        background: var(--primary-color);
        margin: 0 auto;
        border-radius: 2px;
    }

    /* Cards */
    .glass-card {
        background: var(--card-bg);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        transition: all 0.3s ease;
    }

    .glass-card:hover {
        border-color: rgba(0, 210, 255, 0.3);
        transform: translateY(-5px);
        background: rgba(30, 41, 59, 0.9);
    }

    /* Project Cards */
    .project-card {
        background: var(--card-bg);
        border-radius: 20px;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.05);
        margin-bottom: 2rem;
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        border-color: rgba(0, 210, 255, 0.3);
    }

    .project-content {
        padding: 1.5rem;
    }

    .tag-container {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-top: 1rem;
    }

    .tag {
        background: rgba(0, 210, 255, 0.1);
        color: var(--primary-color);
        padding: 0.3rem 0.8rem;
        border-radius: 50px;
        font-size: 0.75rem;
        font-weight: 600;
    }

    /* Video Sizing */
    .video-wrapper {
        width: 100%;
        max-width: 400px; /* Reduced size */
        margin: 0 auto;
        border-radius: 12px;
        overflow: hidden;
    }

    /* Footer */
    .footer {
        padding: 4rem 2rem;
        margin-top: 6rem;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        color: var(--text-muted);
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    @media (max-width: 768px) {
        .hero-title { font-size: 2.5rem; }
        .nav-container { gap: 1rem; padding: 1rem; }
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
    <div class="hero-badge">AVAILABLE FOR OPPORTUNITIES</div>
    <h1 class="hero-title">Rayyan Ahmed</h1>
    <p class="hero-subtitle">
        AI Engineer & Problem Solver specializing in <b>AI Development</b> and <b>AI Automation</b>. <br>
        Transforming complex data into intelligent, end-to-end AI products.
    </p>
</div>
""", unsafe_allow_html=True)

# --------

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

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
    with open("RayyanAhmedResume.pdf", "rb") as file:
        st.download_button(
            label="Download Resume",
            data=file,
            file_name="Rayyan_Ahmed_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )

# --- INTRO SECTION ---
st.markdown('<div class="section-header"><h2 class="section-title">About Me</h2><div class="section-divider"></div></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    st.markdown("""
    <div class="glass-card">
        <p style="font-size: 1.1rem; line-height: 1.8; color: #cbd5e1; text-align: center;">
            I’m Rayyan, an AI Engineer dedicated to architecting end-to-end RAG systems, agentic workflows, and high-performance Generative AI applications. 
            What excites me most isn’t just model deployment—it’s diving into the mechanics of why they perform, from fine-tuning dynamics to the nuances of latent space. 
            I thrive on bridging deep theoretical research with practical, production-ready AI solutions.
            <br><br>
            I excel in building in the "gray area" where benchmarks are undefined. My most rewarding projects involve engineering through technical ambiguity—optimizing 
            local LLM inference or scaling complex data pipelines. I’ve found that true innovation in AI stems from a mix of rigorous curiosity and the persistence 
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
                font-weight: 410;
                color: #e5e7eb;
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 10px;
                background: rgba(220, 220, 220, 0.04);
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
    # TATA Group (Virtual)
    st.markdown("""
    <div class="glass-card">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
            <div>
                <h3 style="margin: 0; color: #fff;">TATA Group (Virtual)</h3>
                <p style="margin: 0; color: var(--primary-color); font-weight: 600;">Data Visualization Intern</p>
            </div>
            <span style="color: var(--text-muted); font-size: 0.9rem;">Sept 2024 – Oct 2024</span>
        </div>
        <ul style="color: #cbd5e1; line-height: 1.6;">
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
                <h3 style="margin: 0; color: #fff;">British Airways (Virtual)</h3>
                <p style="margin: 0; color: var(--primary-color); font-weight: 600;">Data Science Intern</p>
            </div>
            <span style="color: var(--text-muted); font-size: 0.9rem;">Oct 2024 – Nov 2024</span>
        </div>
        <ul style="color: #cbd5e1; line-height: 1.6;">
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
                <h3 style="margin: 0; color: #fff;">NASA Space Apps Challenge</h3>
                <p style="margin: 0; color: var(--primary-color); font-weight: 600;">ML & Data Science Team Member</p>
            </div>
            <span style="color: var(--text-muted); font-size: 0.9rem;">June 2025 – Sept 2025</span>
        </div>
        <ul style="color: #cbd5e1; line-height: 1.6;">
            <li>Built a weather-focused ML solution in collaboration with teammates as part of the world’s largest global hackathon.</li>
            <li>Project selected as a <b>Global Nominee</b>, ranking among the <b>top 1,900<b> out of 18500+ international projects globally.</li>
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
            <h3 style="color: #fff; margin-top: 0;">{title}</h3>
            <p style="color: #cbd5e1; font-size: 0.95rem;">{desc}</p>
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
                background: rgba(255, 255, 255, 0.08); /* Semi-transparent background */
                backdrop-filter: blur(4px);            /* Slight blur for that glass look */
                opacity: 0.9;                          /* Overall element opacity */
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
    st.markdown("<hr style='border: 0.5px solid rgba(255,255,255,0.1); margin: 2rem 0;'>", unsafe_allow_html=True)

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
        <h3 style="color: #fff; margin-bottom: 0.5rem;">Dawood University of Engineering and Technology</h3>
        <p style="color: var(--primary-color); font-weight: 700; font-size: 1.2rem; margin-bottom: 1rem;">Bachelor of Science in Artificial Intelligence</p>
        <p style="color: var(--text-muted); margin-bottom: 1.5rem;">2022 — 2026</p>
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
            <h4 style="margin: 0 0 0.5rem 0; color: #fff;">{cred['title']}</h4>
            <p style="margin: 0 0 1rem 0; color: var(--primary-color); font-size: 0.9rem;">{cred['org']}</p>
            <a href="{cred['link']}" target="_blank" class="secondary-btn" style="padding: 0.4rem 1rem; font-size: 0.8rem; display: inline-block;">Verify</a>
        </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div class="footer">
    <div style="margin-bottom: 1.5rem;">
        <h3 style="color: #fff; margin-bottom: 0.5rem;">Rayyan Ahmed</h3>
        <p>AI Engineer & Problem Solver</p>
    </div>
    <div style="display: flex; justify-content: center; gap: 2rem; margin-bottom: 2rem;">
        <a href="https://www.linkedin.com/in/rayyan-ahmed-504725321/" target="_blank" style="color: var(--primary-color); text-decoration: none;">LinkedIn</a>
        <a href="https://github.com/CodingRayyan" target="_blank" style="color: var(--primary-color); text-decoration: none;">GitHub</a>
        <a href="mailto:rayyanabeel22@gmail.com"
           style="color: var(--primary-color); text-decoration: none;">Email</a>
    </div>
    <p style="font-size: 0.8rem;">Website made by Rayyan Ahmed (Not AI).</p>
    <p style="font-size: 0.8rem;">© 2026 Rayyan Ahmed.</p>
</div>

""", unsafe_allow_html=True)
