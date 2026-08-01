import streamlit as st
import pandas as pd

from src.quality_score import calculate_quality_score
from src.ml_readiness import calculate_ml_readiness


def show_quality(df):

    st.markdown("# 🔍 Data Quality Dashboard")
    st.caption("AI Powered Data Quality Assessment")

    st.divider()

    # ==========================================
    # Scores
    # ==========================================

    quality_score = calculate_quality_score(df)
    ml_score = calculate_ml_readiness(df)

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "🎯 Data Quality Score",
            f"{quality_score}%"
        )

        st.progress(
            quality_score / 100
        )

    with c2:

        st.metric(
            "🤖 ML Readiness",
            f"{ml_score}%"
        )

        st.progress(
            ml_score / 100
        )

    st.divider()

    # ==========================================
    # Risk Level
    # ==========================================

    st.subheader("🚦Dataset Risk Level")

    if quality_score >= 90:

        st.success("🟢 Low Risk Dataset")

    elif quality_score >= 70:

        st.warning("🟡 Medium Risk Dataset")

    else:

        st.error("🔴 High Risk Dataset")

    st.divider()

    # ==========================================
    # Statistics
    # ==========================================

    stats = pd.DataFrame({

        "Metric": [

            "Rows",
            "Columns",
            "Missing Values",
            "Duplicate Rows",
            "Numeric Columns",
            "Categorical Columns"

        ],

        "Value": [

            df.shape[0],
            df.shape[1],
            int(df.isna().sum().sum()),
            int(df.duplicated().sum()),
            len(df.select_dtypes(include="number").columns),
            len(df.select_dtypes(include="object").columns)

        ]

    })

    st.subheader("📋 Dataset Statistics")

    st.dataframe(
        stats,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # ==========================================
    # Quality Checks
    # ==========================================

    checks = []

    if df.isna().sum().sum() == 0:
        checks.append("✅ No Missing Values")
    else:
        checks.append("⚠ Missing Values Found")

    if df.duplicated().sum() == 0:
        checks.append("✅ No Duplicate Rows")
    else:
        checks.append("⚠ Duplicate Rows Found")

    if len(df.columns) > 0:
        checks.append("✅ Dataset Loaded Successfully")

    st.subheader("📑 Validation Results")

    for item in checks:
        st.write(item)

    st.divider()

    st.success("✅ Quality assessment completed successfully.")