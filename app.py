import streamlit as st

from src.profiler import (
    load_dataset,
    dataset_summary
)

from src.health import calculate_health_score

from src.ui.profile import show_profile
from src.ui.cleaning import show_cleaning
from src.ui.insights import show_insights
from src.ui.quality import show_quality
from src.ui.export import show_export
from src.ui.styles import load_css


# ============================================
# Page Configuration
# ============================================

st.set_page_config(
    page_title="CleanIQ",
    page_icon="🧹",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

# ============================================
# Sidebar
# ============================================

with st.sidebar:

    st.title("🧹 CleanIQ")

    st.markdown("### AI Data Quality Platform")

    st.divider()

    st.success("✅ Version 3.0")

    st.info(
        """
Developer

👨‍💻 Aaditya Malviya

MBA Business Analytics & AI
"""
    )

    st.divider()

    st.markdown("### 🚀 Features")

    st.markdown("""
- 📊 Dataset Profiling
- 🧹 Smart Cleaning
- 🤖 AI Insights
- 📈 Charts
- 🎯 ML Readiness
- 📄 PDF Report
- 💾 Export
""")

# ============================================
# Hero Banner
# ============================================

st.markdown(
    """
<div style="
background:linear-gradient(90deg,#2563eb,#7c3aed);
padding:35px;
border-radius:20px;
color:white;
">

<h1>🧹 CleanIQ</h1>

<h3>AI Powered Data Cleaning Platform</h3>

<p>
Upload • Analyze • Clean • Validate • Export
</p>

</div>
""",
    unsafe_allow_html=True
)

st.write("")

# ============================================
# Upload
# ============================================

st.subheader("📂 Upload Dataset")

uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

if uploaded_file is None:

    st.info(
        """
### Welcome to CleanIQ 👋

CleanIQ helps you

✅ Profile datasets

✅ Detect data quality issues

✅ Clean datasets

✅ Generate AI insights

✅ Export cleaned datasets

Upload your dataset to get started.
"""
    )

    st.stop()

# ============================================
# Load Dataset
# ============================================

df = load_dataset(uploaded_file)

summary = dataset_summary(df)

health_score = calculate_health_score(summary)

# ============================================
# Tabs
# ============================================

tab1, tab2, tab3, tab4, tab5 = st.tabs(

    [

        "📊 Profile",

        "🧹 Cleaning",

        "🧠 AI Insights",

        "🔍 Quality",

        "💾 Export"

    ]

)

with tab1:

    show_profile(
        df,
        summary,
        health_score
    )

with tab2:

    show_cleaning(df)

with tab3:

    show_insights(df)

with tab4:

    show_quality(df)

with tab5:

    show_export()