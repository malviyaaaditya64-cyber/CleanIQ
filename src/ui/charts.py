import streamlit as st
import plotly.express as px


def show_charts(df):

    st.markdown("## 📊 Interactive Data Visualization")

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        st.warning("No numeric columns found.")
        return

    # ==========================================
    # Correlation Heatmap
    # ==========================================

    st.subheader("🔥 Correlation Heatmap")

    corr = numeric_df.corr()

    fig = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        aspect="auto"
    )

    fig.update_layout(
        height=650,
        template="plotly_white",
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(size=14),
        margin=dict(l=20, r=20, t=50, b=20)
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ==========================================
    # Histogram
    # ==========================================

    st.subheader("📈 Histogram")

    column = st.selectbox(
        "Select Numeric Column",
        numeric_df.columns,
        key="histogram"
    )

    fig = px.histogram(
        df,
        x=column,
        nbins=30,
        color_discrete_sequence=["#2563eb"],
        title=f"{column} Distribution"
    )

    fig.update_layout(template="plotly_white")

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ==========================================
    # Box Plot
    # ==========================================

    st.subheader("📦 Box Plot")

    box_col = st.selectbox(
        "Select Column",
        numeric_df.columns,
        key="boxplot"
    )

    fig = px.box(
        df,
        y=box_col,
        points="outliers",
        color_discrete_sequence=["#7c3aed"]
    )

    fig.update_layout(template="plotly_white")

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ==========================================
    # Missing Values
    # ==========================================

    st.subheader("❌ Missing Values")

    missing = df.isna().sum().reset_index()
    missing.columns = ["Column", "Missing"]

    missing = missing[missing["Missing"] > 0]

    if missing.empty:

        st.success("🎉 No Missing Values Found")

    else:

        fig = px.bar(
            missing,
            x="Column",
            y="Missing",
            color="Missing",
            color_continuous_scale="Reds"
        )

        fig.update_layout(template="plotly_white")

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ==========================================
    # Data Type Distribution
    # ==========================================

    st.subheader("🧩 Data Type Distribution")

    dtype_df = (
        df.dtypes.astype(str)
        .value_counts()
        .reset_index()
    )

    dtype_df.columns = [
        "Datatype",
        "Count"
    ]

    fig = px.pie(
        dtype_df,
        names="Datatype",
        values="Count",
        hole=0.65,
        color_discrete_sequence=px.colors.qualitative.Set3
    )

    fig.update_layout(template="plotly_white")

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ==========================================
    # Scatter Plot
    # ==========================================

    st.subheader("📌 Scatter Plot Explorer")

    if len(numeric_df.columns) >= 2:

        col1, col2 = st.columns(2)

        with col1:

            x_axis = st.selectbox(
                "X Axis",
                numeric_df.columns,
                key="scatter_x"
            )

        with col2:

            y_axis = st.selectbox(
                "Y Axis",
                numeric_df.columns,
                index=1,
                key="scatter_y"
            )

        fig = px.scatter(
            df,
            x=x_axis,
            y=y_axis,
            opacity=0.8,
            color_discrete_sequence=["#2563eb"],
            title=f"{x_axis} vs {y_axis}"
        )

        fig.update_layout(template="plotly_white")

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.info("Scatter Plot requires at least 2 numeric columns.")