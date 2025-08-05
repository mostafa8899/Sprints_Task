import streamlit as st
import requests
import time
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Enhanced page configuration
st.set_page_config(
    page_title="NeoAI Insight Engine",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .main {
        font-family: 'Inter', sans-serif;
    }
    
    .hero-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    }
    
    .hero-title {
        color: white;
        font-size: 3.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .hero-subtitle {
        color: rgba(255,255,255,0.9);
        font-size: 1.2rem;
        text-align: center;
        font-weight: 400;
    }
    
    .glass-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        margin: 0.5rem;
    }
    
    .keyword-chip {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        margin: 0.3rem;
        font-weight: 500;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 0.75rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.6) !important;
    }
    
    .sidebar-content {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1rem;
        border-radius: 15px;
        color: white;
        margin-bottom: 1rem;
    }
    
    .status-success {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 1rem 0;
    }
    
    .status-error {
        background: linear-gradient(135deg, #ff6b6b 0%, #ffa500 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 1rem 0;
    }
    
    .report-container {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin: 1rem 0;
    }
    
    .loading-container {
        text-align: center;
        padding: 2rem;
    }
    
    .pulse {
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-container">
    <div class="hero-title">🧠 NeoAI Insight Engine</div>
    <div class="hero-subtitle">Transform real-world AI trends into cutting-edge research proposals using powerful LLMs</div>
</div>
""", unsafe_allow_html=True)

# Sidebar with enhanced styling
with st.sidebar:
    st.markdown("""
    <div class="sidebar-content">
        <h3 style="margin-top: 0;">⚙️ Configuration</h3>
        <p>Customize your AI research experience</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Model selection with enhanced UI
    st.markdown("### 🤖 AI Model Selection")
    model_options = {
        "llama3-8b-8192": "🦙 Llama 3 8B - Fast & Efficient",
        "llama3-70b-8192": "🦙 Llama 3 70B - Most Powerful", 
        "mixtral-8x7b-32768": "🌪️ Mixtral 8x7B - Balanced",
        "gemma-7b-it": "💎 Gemma 7B - Specialized"
    }
    
    selected_model = st.selectbox(
        "Choose your AI model:",
        options=list(model_options.keys()),
        format_func=lambda x: model_options[x],
        index=0
    )
    
    # Settings
    st.markdown("### ⚡ Advanced Settings")
    max_keywords = st.slider("Max Keywords to Extract", 3, 10, 5)
    temperature = st.slider("Creativity Level", 0.1, 1.0, 0.7, 0.1)
    
    # Statistics
    st.markdown("### 📊 Session Stats")
    if 'reports_generated' not in st.session_state:
        st.session_state.reports_generated = 0
    if 'total_time' not in st.session_state:
        st.session_state.total_time = 0
    
    st.metric("Reports Generated", st.session_state.reports_generated)
    st.metric("Total Processing Time", f"{st.session_state.total_time:.1f}s")

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    # Enhanced input section
    st.markdown("### 🔍 Research Topic Input")
    
    # Suggested topics
    suggested_topics = [
        "AI ethics and bias mitigation",
        "Quantum machine learning",
        "Federated learning privacy",
        "Neuromorphic computing",
        "AI for climate change",
        "Explainable AI (XAI)",
        "Edge AI optimization",
        "AI in healthcare diagnostics"
    ]
    
    topic_col1, topic_col2 = st.columns(2)
    with topic_col1:
        st.markdown("**💡 Suggested Topics:**")
        for i in range(0, len(suggested_topics), 2):
            if st.button(suggested_topics[i], key=f"topic_{i}"):
                st.session_state.research_query = suggested_topics[i]
    
    with topic_col2:
        st.markdown("**&nbsp;**")  # Spacing
        for i in range(1, len(suggested_topics), 2):
            if i < len(suggested_topics):
                if st.button(suggested_topics[i], key=f"topic_{i}"):
                    st.session_state.research_query = suggested_topics[i]
    
    # Research query input
    query = st.text_input(
        "Enter your AI research topic:",
        value=st.session_state.get('research_query', 'AI ethics'),
        placeholder="Type your research topic here...",
        help="Enter a specific AI research area you want to explore"
    )

with col2:
    # Real-time clock
    st.markdown("### 🕒 Current Time")
    current_time = datetime.now().strftime("%H:%M:%S")
    st.markdown(f"<div class='metric-card'><h2>{current_time}</h2></div>", unsafe_allow_html=True)
    
    # Model info
    st.markdown("### 🔧 Model Info")
    model_info = {
        "llama3-8b-8192": {"speed": "⚡ Fast", "quality": "⭐⭐⭐"},
        "llama3-70b-8192": {"speed": "🐌 Slow", "quality": "⭐⭐⭐⭐⭐"},
        "mixtral-8x7b-32768": {"speed": "⚡ Medium", "quality": "⭐⭐⭐⭐"},
        "gemma-7b-it": {"speed": "⚡ Fast", "quality": "⭐⭐⭐"}
    }
    
    info = model_info.get(selected_model, {"speed": "⚡ Fast", "quality": "⭐⭐⭐"})
    st.markdown(f"**Speed:** {info['speed']}")
    st.markdown(f"**Quality:** {info['quality']}")

# Enhanced backend call function
@st.cache_data(show_spinner=False, ttl=300)
def call_backend(query, model):
    try:
        res = requests.post(
            "http://localhost:8000/generate/", 
            json={"query": query, "model": model},
            timeout=45
        )
        return res.json() if res.status_code == 200 else None
    except Exception as e:
        return {"error": str(e)}

# Generate button with enhanced styling
st.markdown("---")
generate_col1, generate_col2, generate_col3 = st.columns([1, 2, 1])

with generate_col2:
    if st.button("🚀 Generate AI Research Report", use_container_width=True):
        if query.strip():
            start_time = time.time()
            
            # Enhanced loading animation
            with st.container():
                st.markdown("""
                <div class="loading-container">
                    <div class="pulse">
                        <h3>🤖 AI Agents at Work...</h3>
                        <p>Analyzing trends • Extracting insights • Generating proposals</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Progress bar
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                # Simulate progress updates
                for i in range(100):
                    progress_bar.progress(i + 1)
                    if i < 30:
                        status_text.text("🔍 Collecting data from news sources...")
                    elif i < 60:
                        status_text.text("🧠 Extracting keywords and insights...")
                    elif i < 90:
                        status_text.text("📝 Generating research proposals...")
                    else:
                        status_text.text("✨ Finalizing your report...")
                    time.sleep(0.02)
                
                # Clear progress indicators
                progress_bar.empty()
                status_text.empty()
                
                # Make API call
                data = call_backend(query, selected_model)
                elapsed_time = time.time() - start_time
                
                # Update session stats
                st.session_state.reports_generated += 1
                st.session_state.total_time += elapsed_time
            
            if data and "error" not in data:
                # Success message
                st.markdown(f"""
                <div class="status-success">
                    <h3>✅ Report Generated Successfully!</h3>
                    <p>Completed in {elapsed_time:.2f} seconds</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Results section
                st.markdown("---")
                
                # Keywords section with enhanced styling
                st.markdown("### 🔑 Extracted Keywords")
                keyword_cols = st.columns(3)
                
                keywords_html = ""
                for i, (kw, score) in enumerate(data["keywords"]):
                    keywords_html += f'<span class="keyword-chip">{kw} ({score})</span>'
                
                st.markdown(f'<div style="text-align: center; margin: 1rem 0;">{keywords_html}</div>', 
                           unsafe_allow_html=True)
                
                # Keyword visualization
                if data["keywords"]:
                    keyword_df = pd.DataFrame(data["keywords"], columns=['Keyword', 'Score'])
                    fig = px.bar(
                        keyword_df, 
                        x='Score', 
                        y='Keyword',
                        orientation='h',
                        title="Keyword Importance Scores",
                        color='Score',
                        color_continuous_scale='Viridis'
                    )
                    fig.update_layout(
                        plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor='rgba(0,0,0,0)',
                        font_color='white'
                    )
                    st.plotly_chart(fig, use_container_width=True)
                
                # Research report section
                st.markdown("### 📄 AI Research Report")
                st.markdown(f"""
                <div class="report-container">
                    {data["report"]}
                </div>
                """, unsafe_allow_html=True)
                
                # Download section
                col1, col2, col3 = st.columns(3)
                with col2:
                    st.download_button(
                        "📥 Download Report",
                        data["report"],
                        file_name=f"neoai_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                        mime="text/markdown",
                        use_container_width=True
                    )
                
                # Report metrics
                word_count = len(data["report"].split())
                char_count = len(data["report"])
                
                metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
                with metric_col1:
                    st.metric("Keywords Found", len(data["keywords"]))
                with metric_col2:
                    st.metric("Word Count", word_count)
                with metric_col3:
                    st.metric("Characters", char_count)
                with metric_col4:
                    st.metric("Generation Time", f"{elapsed_time:.1f}s")
                
            else:
                # Error handling
                error_msg = data.get("error", "Unknown error occurred") if data else "Failed to connect to backend"
                st.markdown(f"""
                <div class="status-error">
                    <h3>⚠️ Generation Failed</h3>
                    <p>{error_msg}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Troubleshooting tips
                with st.expander("🔧 Troubleshooting Tips"):
                    st.markdown("""
                    - Ensure the backend server is running (`python api.py`)
                    - Check if your API keys are properly configured
                    - Verify your internet connection
                    - Try a different model or simpler query
                    """)
        else:
            st.warning("Please enter a research topic before generating a report.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; opacity: 0.7;">
    <p>🧠 NeoAI Insight Engine | Powered by Advanced AI Models</p>
    <p>Built with ❤️ using Streamlit, FastAPI, and Cutting-edge LLMs</p>
</div>
""", unsafe_allow_html=True)