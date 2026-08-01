import streamlit as st

from src.ai_engine import generate_recommendations
from src.ml_readiness import calculate_ml_readiness
from src.quality_score import calculate_quality_score


def show_insights(df):

    st.markdown("# 🧠 AI Insights")
    st.caption("AI Powered Dataset Intelligence")

    st.divider()

    # =====================================
    # Scores
    # =====================================

    quality_score = calculate_quality_score(df)
    ml_score = calculate_ml_readiness(df)

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "🎯 Quality Score",
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

    # =====================================
    # Dataset Summary
    # =====================================

    st.subheader("📋 Dataset Summary")

    st.success(
        f"""
Dataset contains **{df.shape[0]:,} rows** and **{df.shape[1]} columns**.

• Numeric Columns : {len(df.select_dtypes(include='number').columns)}

• Categorical Columns : {len(df.select_dtypes(include='object').columns)}

• Missing Values : {int(df.isna().sum().sum())}

• Duplicate Rows : {int(df.duplicated().sum())}
"""
    )

    st.divider()

    # =====================================
    # Recommendations
    # =====================================

    st.subheader("💡 AI Recommendations")

    recommendations = generate_recommendations(df)

    good = 0
    warning = 0
    critical = 0

    for item in recommendations:

        if "🟢" in item or "✅" in item:
            good += 1

        elif "🟡" in item:
            warning += 1

        elif "🔴" in item:
            critical += 1

    c1, c2, c3 = st.columns(3)

    c1.metric("✅ Good", good)
    c2.metric("⚠ Warnings", warning)
    c3.metric("🚨 Critical", critical)

    st.divider()

    for rec in recommendations:

        if "🔴" in rec:
            st.error(rec)

        elif "🟡" in rec:
            st.warning(rec)

        elif "🟢" in rec:
            st.info(rec)

        else:
            st.success(rec)

    st.divider()

    # =====================================
    # Next Steps
    # =====================================

    st.subheader("🚀 Suggested Next Steps")

    steps = [
        "🧹 Clean missing values and duplicates.",
        "📊 Explore feature distributions using charts.",
        "🏷️ Encode categorical columns before ML.",
        "📏 Scale numeric features if required.",
        "🤖 Train Machine Learning models after cleaning."
    ]

    for step in steps:
        st.write(step)

    st.divider()

    st.success("✅ AI analysis completed successfully.")