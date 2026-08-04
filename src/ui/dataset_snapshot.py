import streamlit as st


def info_card(title, value, icon, color):

    st.markdown(f"""
    <div style="
    background:white;
    border-radius:20px;
    padding:22px;
    border-top:5px solid {color};
    box-shadow:0 12px 30px rgba(0,0,0,.06);
    text-align:center;
    margin-bottom:15px;
    ">

    <div style="font-size:32px;">
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
    font-size:30px;
    font-weight:800;
    color:#111827;
    margin-top:10px;
    ">
    {value}
    </div>

    </div>
    """, unsafe_allow_html=True)


def show_dataset_snapshot(df):

    st.markdown("## 📋 Executive Dataset Snapshot")

    rows = df.shape[0]
    cols = df.shape[1]

    memory = round(
        df.memory_usage(deep=True).sum()/1024**2,
        2
    )

    numeric = len(
        df.select_dtypes(include="number").columns
    )

    categorical = len(
        df.select_dtypes(include="object").columns
    )

    missing = int(
        df.isna().sum().sum()
    )

    duplicate = int(
        df.duplicated().sum()
    )

    row1 = st.columns(4)

    with row1[0]:
        info_card(
            "Rows",
            f"{rows:,}",
            "📄",
            "#2563eb"
        )

    with row1[1]:
        info_card(
            "Columns",
            cols,
            "📑",
            "#7c3aed"
        )

    with row1[2]:
        info_card(
            "Memory",
            f"{memory} MB",
            "💾",
            "#0f766e"
        )

    with row1[3]:
        info_card(
            "Missing",
            missing,
            "❌",
            "#dc2626"
        )

    row2 = st.columns(3)

    with row2[0]:
        info_card(
            "Numeric",
            numeric,
            "🔢",
            "#2563eb"
        )

    with row2[1]:
        info_card(
            "Categorical",
            categorical,
            "🔤",
            "#9333ea"
        )

    with row2[2]:
        info_card(
            "Duplicates",
            duplicate,
            "🔁",
            "#ea580c"
        )

    st.divider()

    st.subheader("👀 Dataset Preview")

    st.dataframe(
        df.head(15),
        use_container_width=True,
        height=420
    )

    st.caption(
        "Showing the first 15 rows of the uploaded dataset."
    )