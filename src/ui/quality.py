import streamlit as st
import pandas as pd

from src.quality_score import calculate_quality_score
from src.ml_readiness import calculate_ml_readiness


def show_quality(df):

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#0f172a,#2563eb,#7c3aed);
    padding:30px;
    border-radius:20px;
    color:white;
    margin-bottom:25px;
    ">

    <h1>🔍 Data Quality Dashboard</h1>

    <p style="font-size:18px;">
    AI Powered Dataset Validation • Quality Assessment • ML Readiness
    </p>

    </div>
    """, unsafe_allow_html=True)

    # ==========================================
    # Calculate Scores
    # ==========================================

    quality_score = calculate_quality_score(df)
    ml_score = calculate_ml_readiness(df)

    missing = int(df.isna().sum().sum())
    duplicate = int(df.duplicated().sum())

    numeric = len(df.select_dtypes(include="number").columns)
    categorical = len(df.select_dtypes(include="object").columns)

    # ==========================================
    # Executive KPI Cards
    # ==========================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "🎯 Quality",
            f"{quality_score}%"
        )

    with c2:
        st.metric(
            "🤖 ML Ready",
            f"{ml_score}%"
        )

    with c3:
        st.metric(
            "❌ Missing",
            missing
        )

    with c4:
        st.metric(
            "🔁 Duplicates",
            duplicate
        )

    st.progress(quality_score / 100)

    st.divider()

    # ==========================================
    # Executive Summary
    # ==========================================

    st.markdown("## 📋 Executive Summary")

    st.info(f"""
### 🤖 AI Dataset Assessment

Rows : **{df.shape[0]:,}**

Columns : **{df.shape[1]}**

Numeric Columns : **{numeric}**

Categorical Columns : **{categorical}**

Quality Score : **{quality_score}%**

ML Readiness : **{ml_score}%**
""")

    st.divider()


        # ==========================================
    # Risk Level
    # ==========================================

    st.markdown("## 🚦 Dataset Risk Analysis")

    if quality_score >= 90:

        st.success("🟢 Low Risk Dataset")

    elif quality_score >= 70:

        st.warning("🟡 Medium Risk Dataset")

    else:

        st.error("🔴 High Risk Dataset")

    st.divider()

    # ==========================================
    # Dataset Statistics
    # ==========================================

    st.markdown("## 📊 Dataset Statistics")

    stats = pd.DataFrame({

        "Metric": [

            "Rows",
            "Columns",
            "Missing Values",
            "Duplicate Rows",
            "Numeric Columns",
            "Categorical Columns",
            "Memory Usage (MB)"

        ],

        "Value": [

            df.shape[0],
            df.shape[1],
            missing,
            duplicate,
            numeric,
            categorical,
            round(df.memory_usage(deep=True).sum()/1024/1024, 2)

        ]

    })

    st.dataframe(
        stats,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # ==========================================
    # Validation Dashboard
    # ==========================================

    st.markdown("## ✅ Validation Results")

    left, right = st.columns(2)

    with left:

        if missing == 0:
            st.success("✅ No Missing Values")
        else:
            st.warning(f"⚠ {missing} Missing Values Found")

        if duplicate == 0:
            st.success("✅ No Duplicate Rows")
        else:
            st.warning(f"⚠ {duplicate} Duplicate Rows Found")

    with right:

        st.info(f"""
### 📋 AI Validation

Quality Score : **{quality_score}%**

ML Readiness : **{ml_score}%**

Dataset Status :

**{"Production Ready" if quality_score >= 90 else "Needs Cleaning"}**
""")

    st.divider()


        # ==========================================
    # AI Quality Report
    # ==========================================

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#0f172a,#1d4ed8,#7c3aed);
    padding:28px;
    border-radius:20px;
    color:white;
    margin-bottom:20px;
    ">

    <h2 style="color:white;">
    🧠 AI Quality Report
    </h2>

    <p style="font-size:18px;">
    CleanIQ has completed a comprehensive quality assessment of your dataset.
    </p>

    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🎯 Quality Score",
            f"{quality_score}%"
        )

    with col2:
        st.metric(
            "🤖 ML Readiness",
            f"{ml_score}%"
        )

    with col3:

        if quality_score >= 90:
            status = "🟢 Excellent"

        elif quality_score >= 70:
            status = "🟡 Good"

        else:
            status = "🔴 Poor"

        st.metric(
            "🏆 Dataset Status",
            status
        )

    st.progress(quality_score / 100)

    st.divider()

    # ==========================================
    # Quality Improvement Suggestions
    # ==========================================

    st.markdown("## 🚀 Quality Improvement Suggestions")

    suggestions = []

    if missing > 0:
        suggestions.append("🧹 Handle missing values before training ML models.")

    if duplicate > 0:
        suggestions.append("🔁 Remove duplicate records.")

    if numeric == 0:
        suggestions.append("📊 Add numeric features for better analysis.")

    if categorical > 10:
        suggestions.append("🏷️ Consider encoding categorical columns.")

    if len(suggestions) == 0:
        suggestions.append("🎉 Dataset quality looks excellent. No major issues detected.")

    for item in suggestions:
        st.write(item)

    st.divider()

    # ==========================================
    # Final AI Verdict
    # ==========================================

    if quality_score >= 90 and ml_score >= 90:

        st.success(
            "🏆 Excellent! Your dataset is production-ready for Machine Learning."
        )

    elif quality_score >= 70:

        st.warning(
            "⚠️ Your dataset is good, but a little more cleaning will improve model performance."
        )

    else:

        st.error(
            "🚨 Dataset quality is low. Perform cleaning before using it for analytics or Machine Learning."
        )

    st.divider()

    st.success("✅ Data Quality Assessment Completed Successfully.")