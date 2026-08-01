import streamlit as st


def show_dashboard_cards(summary, health_score):

    st.markdown("## 📌 Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📄 Rows",
            f"{summary['Rows']:,}"
        )

    with col2:
        st.metric(
            "📑 Columns",
            summary["Columns"]
        )

    with col3:
        st.metric(
            "🩺 Health",
            f"{health_score}%"
        )

    with col4:
        st.metric(
            "❌ Missing",
            summary["Missing Values"]
        )

    col5, col6, col7, col8 = st.columns(4)

    with col5:
        st.metric(
            "🔁 Duplicates",
            summary["Duplicate Rows"]
        )

    with col6:
        st.metric(
            "💾 Memory",
            f"{summary['Memory Usage (MB)']} MB"
        )

    with col7:
        st.metric(
            "🔢 Numeric",
            summary["Numeric Columns"]
        )

    with col8:
        st.metric(
            "🔤 Categorical",
            summary["Categorical Columns"]
        )