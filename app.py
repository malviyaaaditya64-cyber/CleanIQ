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
from src.claude_chat import ask_claude

print("=" * 60)
print("MODULE :", ask_claude.__module__)
print("FILE   :", ask_claude.__code__.co_filename)
print("=" * 60)

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

# -----------------------------
# Session State
# -----------------------------

if "theme" not in st.session_state:
    st.session_state.theme = "light"

if "uploaded" not in st.session_state:
    st.session_state.uploaded = False

st.markdown(
    """
<style>

.block-container{
    padding-top:1.5rem;
    padding-bottom:1rem;
    max-width:1400px;
}

</style>
""",
    unsafe_allow_html=True,
)

# ============================================
# Premium Sidebar
# ============================================

with st.sidebar:

    st.markdown("# 🧹 CleanIQ")

    st.caption("AI Powered Data Quality Platform")

    st.divider()

    st.success("🟢 AI Status : Ready")

    st.info("""
### 👨‍💻 Developer

**Aaditya Malviya**

MBA Business Analytics & AI
""")

    st.markdown("### 🚀 Features")

    st.markdown("""
✅ Dataset Profiling

✅ Smart Cleaning

✅ AI Insights

✅ Charts & Analytics

✅ ML Readiness

✅ PDF Report

✅ Export Center
""")

    st.divider()

    st.markdown("### ⚙️ Version")

    st.success("Version 3.0")
# ============================================
# Premium Hero Section
# ============================================

st.markdown("""
<div style="
background:linear-gradient(135deg,#0f172a,#2563eb,#7c3aed);
padding:40px;
border-radius:24px;
color:white;
margin-bottom:25px;
box-shadow:0 20px 50px rgba(37,99,235,.25);
">

<div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;">

<div>

<h1 style="
margin:0;
font-size:48px;
color:white;
">
🧹 CleanIQ
</h1>

<p style="
font-size:20px;
margin-top:10px;
opacity:.95;
">
AI Powered Data Cleaning Platform
</p>

<p style="
font-size:16px;
opacity:.85;
">
Upload • Analyze • Clean • Validate • Export • AI Insights
</p>

</div>

<div style="
background:rgba(255,255,255,.15);
padding:18px 26px;
border-radius:18px;
text-align:center;
min-width:220px;
backdrop-filter:blur(12px);
">

<h3 style="margin:0;color:white;">
🤖 AI STATUS
</h3>

<h2 style="margin:10px 0;color:#7CFFB2;">
READY
</h2>

<p style="margin:0;">
Version 3.0
</p>

</div>

</div>

<hr style="
margin:30px 0;
border:.5px solid rgba(255,255,255,.2);
">

<div style="
display:flex;
justify-content:space-around;
text-align:center;
flex-wrap:wrap;
">

<div>
<h2 style="color:white;">⚡ Fast</h2>
<p>One Click Cleaning</p>
</div>

<div>
<h2 style="color:white;">🧠 Smart</h2>
<p>AI Recommendations</p>
</div>

<div>
<h2 style="color:white;">📊 Analytics</h2>
<p>Executive Dashboard</p>
</div>

<div>
<h2 style="color:white;">📄 Export</h2>
<p>CSV • Excel • PDF</p>
</div>

</div>

</div>
""", unsafe_allow_html=True)

# ============================================
# Upload
# ============================================

st.markdown("""
<h2 style="margin-bottom:5px;">
📂 Upload Your Dataset
</h2>

<p style="color:gray;font-size:17px;">
Upload a CSV or Excel file to start AI-powered data profiling, cleaning and quality analysis.
</p>
""", unsafe_allow_html=True)


st.markdown("""
<div style="
background:white;
border:2px dashed #2563eb;
border-radius:20px;
padding:20px;
margin-bottom:15px;
box-shadow:0 10px 25px rgba(0,0,0,.05);
">

<h3 style="margin:0;color:#2563eb;">
📂 Drag & Drop Your Dataset
</h3>

<p style="margin-top:10px;color:#666;">
Supported formats:
<b>CSV</b> • <b>Excel (.xlsx)</b>
</p>

</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv", "xlsx"],
    label_visibility="collapsed"
)

if uploaded_file is not None:

    st.success(f"✅ Uploaded File : {uploaded_file.name}")

    file_size = round(uploaded_file.size / (1024 * 1024), 2)

    c1, c2 = st.columns(2)

    with c1:
        st.metric("📁 File Name", uploaded_file.name)

    with c2:
        st.metric("💾 File Size", f"{file_size} MB")

    st.divider()

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
st.success("✅ Dataset uploaded successfully!")
st.markdown(f"""
<div style="
background:linear-gradient(135deg,#ffffff,#f8fbff);
padding:25px;
border-radius:20px;
box-shadow:0 10px 25px rgba(0,0,0,.08);
border-left:6px solid #2563eb;
margin-bottom:20px;
">

<h2 style="margin:0;color:#111827;">
📊 Dataset Loaded Successfully
</h2>

<p style="font-size:17px;color:#555;margin-top:10px;">
<b>File :</b> {uploaded_file.name}
</p>

<p style="font-size:17px;color:#555;">
🚀 CleanIQ is now analyzing your dataset...
</p>

</div>
""", unsafe_allow_html=True)

summary = dataset_summary(df)

health_score = calculate_health_score(summary)
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.info(f"""
### 📄 Rows

**{len(df):,}**
""")

with c2:
    st.info(f"""
### 📑 Columns

**{len(df.columns)}**
""")

with c3:
    memory = round(
        df.memory_usage(deep=True).sum()/1024/1024,
        2
    )

    st.info(f"""
### 💾 Memory

**{memory} MB**
""")

with c4:

    st.info(f"""
### ❤️ Health

**{health_score}%**
""")

st.divider()

st.markdown("## 📋 Dataset Preview")

st.dataframe(
    df.head(10),
    use_container_width=True,
    height=320
)

st.write("")



st.markdown("## 📊 Executive Dashboard")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "📄 Total Rows",
        f"{summary['Rows']:,}",
        delta=None
    )

with c2:
    st.metric(
        "📑 Total Columns",
        summary["Columns"]
    )

with c3:
    color = "🟢" if health_score >= 90 else "🟡" if health_score >= 70 else "🔴"

    st.metric(
        "❤️ Dataset Health",
        f"{health_score}%",
        delta=color
    )

with c4:

    status = (
        "Excellent"
        if health_score >= 90
        else "Good"
        if health_score >= 70
        else "Needs Cleaning"
    )

    st.metric(
        "🤖 AI Status",
        status
    )

st.progress(health_score / 100)

if health_score >= 90:

    st.success("🎉 Your dataset is production ready.")

elif health_score >= 70:

    st.warning("⚠ Minor cleaning recommended before ML.")

else:

    st.error("🚨 Dataset requires cleaning before analysis.")

st.divider()

# ============================================
# Tabs
# ============================================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Dataset Profile",
    "🧹 Smart Cleaning",
    "🧠 AI Insights",
    "📈 Data Quality",
    "📤 Export Center"
])

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

    st.divider()

st.markdown(
    """
<div style="text-align:center;padding:20px;color:#808080;font-size:14px;">
Built with ❤️ using <b>Python</b> & <b>Streamlit</b><br>
© 2026 CleanIQ | Developed by <b>Aaditya Malviya</b>
</div>
""",
    unsafe_allow_html=True,
)

from src.claude_chat import ask_claude

print("MODULE :", ask_claude.__module__)
print("FILE   :", ask_claude.__code__.co_filename)