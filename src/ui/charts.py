import streamlit as st
import pandas as pd
import plotly.express as px


def show_charts(df):

    st.markdown("## 📊 Interactive Data Visualization")

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        st.warning("No numeric columns found.")
        return

    # -----------------------------
    # Correlation Heatmap
    # -----------------------------
    st.subheader("🔥 Correlation Heatmap")

    corr = numeric_df.corr(numeric_only=True)

    fig = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        aspect="auto"
    )

    fig.update_layout(height=650)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # -----------------------------
    # Histogram
    # -----------------------------
    st.subheader("📈 Histogram")

    column = st.selectbox(
        "Select Numeric Column",
        numeric_df.columns,
        key="histogram_column"
    )

    fig = px.histogram(
        df,
        x=column,
        nbins=30,
        title=f"{column} Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # -----------------------------
    # Box Plot
    # -----------------------------
    st.subheader("📦 Box Plot")

    box_col = st.selectbox(
        "Select Column",
        numeric_df.columns,
        key="boxplot_column"
    )

    fig = px.box(
        df,
        y=box_col,
        points="outliers"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # -----------------------------
    # Missing Values
    # -----------------------------
    st.subheader("❌ Missing Values")

    missing = (
        df.isna()
        .sum()
        .reset_index()
    )

    missing.columns = [
        "Column",
        "Missing"
    ]

    missing = missing[
        missing["Missing"] > 0
    ]

    if missing.empty:

        st.success("No Missing Values Found.")

    else:

        fig = px.bar(
            missing,
            x="Column",
            y="Missing",
            color="Missing"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    # -----------------------------
    # Datatype Distribution
    # -----------------------------
    st.subheader("🧩 Data Type Distribution")

    dtype_df = (
        df.dtypes
        .astype(str)
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
        hole=0.5
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    
    st.divider()

    # -----------------------------
    # Scatter Plot Explorer
    # -----------------------------
    st.subheader("📌 Scatter Plot Explorer")

    if len(numeric_df.columns) >= 2:

        col1, col2 = st.columns(2)

        with col1:

            x_axis = st.selectbox(
                "Select X-axis",
                numeric_df.columns,
                key="scatter_x"
            )

        with col2:

            y_axis = st.selectbox(
                "Select Y-axis",
                numeric_df.columns,
                index=min(1, len(numeric_df.columns)-1),
                key="scatter_y"
            )

        fig = px.scatter(
            df,
            x=x_axis,
            y=y_axis,
            title=f"{x_axis} vs {y_axis}",
            opacity=0.75
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.info("Scatter plot requires at least 2 numeric columns.")