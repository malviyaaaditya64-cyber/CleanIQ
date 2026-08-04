import streamlit as st


def card(title, value, icon, color):

    st.markdown(f"""
    <div style="

    background:white;

    border-radius:22px;

    padding:22px;

    box-shadow:0 15px 35px rgba(0,0,0,.08);

    border-top:6px solid {color};

    transition:.3s;

    margin-bottom:15px;

    ">

    <div style="font-size:34px;">
    {icon}
    </div>

    <div style="
    color:#6b7280;
    font-size:15px;
    margin-top:8px;
    ">
    {title}
    </div>

    <div style="
    font-size:34px;
    font-weight:800;
    color:#111827;
    margin-top:8px;
    ">
    {value}
    </div>

    </div>
    """, unsafe_allow_html=True)


def show_dashboard_cards(summary, health_score):

    st.markdown("## 📊 Executive Dashboard")

    row1 = st.columns(4)

    with row1[0]:
        card(
            "Rows",
            f"{summary['Rows']:,}",
            "📄",
            "#2563eb"
        )

    with row1[1]:
        card(
            "Columns",
            summary["Columns"],
            "📑",
            "#7c3aed"
        )

    with row1[2]:
        card(
            "Health Score",
            f"{health_score}%",
            "🩺",
            "#16a34a"
        )

    with row1[3]:
        card(
            "Missing Values",
            summary["Missing Values"],
            "❌",
            "#dc2626"
        )

    row2 = st.columns(4)

    with row2[0]:
        card(
            "Duplicates",
            summary["Duplicate Rows"],
            "🔁",
            "#ea580c"
        )

    with row2[1]:
        card(
            "Memory",
            f"{summary['Memory Usage (MB)']} MB",
            "💾",
            "#0f766e"
        )

    with row2[2]:
        card(
            "Numeric",
            summary["Numeric Columns"],
            "🔢",
            "#4338ca"
        )

    with row2[3]:
        card(
            "Categorical",
            summary["Categorical Columns"],
            "🔤",
            "#9333ea"
        )