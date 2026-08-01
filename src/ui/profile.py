import streamlit as st
import pandas as pd

from src.profiler import analyze_columns
from src.ui.charts import show_charts
from src.ui.dashboard_cards import show_dashboard_cards
from src.ui.dataset_snapshot import show_dataset_snapshot
from src.ui.data_warnings import show_data_warnings
from src.ui.data_dictionary import show_data_dictionary

from src.type_detector import detect_column_types
from src.quality_score import calculate_quality_score
from src.ui.ai_recommendations import show_ai_recommendations
from src.ui.ai_summary import show_ai_summary
from src.ui.chat_assistant import show_chat_assistant
from src.ui.history import show_history

def show_profile(df, summary, health_score):

    # =====================================
    # Header
    # =====================================

    st.markdown("# 📊 Dashboard")
    st.caption("AI Powered Dataset Profiling")

    st.divider()

    # =====================================
    # Dashboard Cards
    # =====================================

    show_dashboard_cards(
        summary,
        health_score
    )

    st.divider()

    # =====================================
    # Quality Score
    # =====================================

    quality_score = calculate_quality_score(df)

    st.subheader("🎯 Data Quality Score")

    icon = "🟢"

    if quality_score < 80:
        icon = "🟡"

    if quality_score < 60:
        icon = "🔴"

    st.metric(
        f"{icon} Overall Score",
        f"{quality_score}%"
    )

    st.progress(
        quality_score / 100
    )

    st.divider()

    # =====================================
    # Dataset Snapshot
    # =====================================

    show_dataset_snapshot(df)

    st.divider()

    # =====================================
    # Smart Warnings
    # =====================================

    show_data_warnings(df)

    st.divider()

    # =====================================
    # Health
    # =====================================

    st.subheader("🩺 Dataset Health")

    c1, c2 = st.columns([1, 3])

    with c1:

        st.metric(
            "Health Score",
            f"{health_score}/100"
        )

    with c2:

        st.progress(
            health_score / 100
        )

        if health_score >= 90:

            st.success(
                "Excellent Dataset Quality"
            )

        elif health_score >= 70:

            st.warning(
                "Minor Cleaning Recommended"
            )

        else:

            st.error(
                "Poor Dataset Quality"
            )

    st.divider()

    # =====================================
    # Dataset Preview
    # =====================================

    st.subheader("👀 Dataset Preview")

    st.dataframe(
        df.head(20),
        use_container_width=True,
        height=420
    )

    st.divider()

    # =====================================
    # Column Intelligence
    # =====================================

    st.subheader("🧠 Column Intelligence")

    report = analyze_columns(df)

    st.dataframe(
        report,
        use_container_width=True,
        height=450
    )

    st.divider()

        # =====================================
    # Missing Values
    # =====================================

    st.subheader("📉 Missing Values")

    missing = (
        df.isna()
        .sum()
        .sort_values(ascending=False)
    )

    missing = missing[missing > 0]

    if len(missing) == 0:

        st.success(
            "🎉 No Missing Values Found"
        )

    else:

        st.bar_chart(
            missing
        )

    st.divider()

    # =====================================
    # Data Types
    # =====================================

    st.subheader("📊 Data Types")

    dtype_df = pd.DataFrame({
        "Datatype": df.dtypes.astype(str)
    })

    st.dataframe(
        dtype_df,
        use_container_width=True
    )

    st.divider()

    # =====================================
    # Interactive Charts
    # =====================================

    show_charts(df)

    st.divider()

    # =====================================
    # Smart Type Detection
    # =====================================

    st.subheader("🤖 Smart Data Type Detection")

    type_report = detect_column_types(df)

    st.dataframe(
        type_report,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # =====================================
    # Data Dictionary
    # =====================================

    show_data_dictionary(df)

    st.divider()

    st.success("✅ Dataset profiling completed successfully.")

    st.divider()

    show_ai_recommendations(df)

    st.divider()

    show_ai_summary(df)

    st.divider()

    st.divider()

    show_chat_assistant(df)

    st.divider()

show_history()