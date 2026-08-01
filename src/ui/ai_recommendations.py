import streamlit as st


def show_ai_recommendations(df):

    st.markdown("## 🤖 AI Recommendations")

    recommendations = []

    # Missing Values
    if df.isna().sum().sum() > 0:
        recommendations.append(
            "Fill missing values using Mean, Median or Mode."
        )

    # Duplicate Rows
    if df.duplicated().sum() > 0:
        recommendations.append(
            "Remove duplicate rows to improve data quality."
        )

    # Object Columns
    cat_cols = df.select_dtypes(include="object").columns

    if len(cat_cols) > 0:
        recommendations.append(
            "Encode categorical columns before Machine Learning."
        )

    # Numeric Columns
    num_cols = df.select_dtypes(include="number").columns

    if len(num_cols) > 0:
        recommendations.append(
            "Scale numeric columns before model training."
        )

    # Date Columns
    for col in df.columns:

        if "date" in col.lower():

            recommendations.append(
                f"Convert '{col}' to datetime format."
            )

    if len(recommendations) == 0:

        st.success("🎉 Dataset looks ready for Machine Learning.")

    else:

        for rec in recommendations:

            st.info("💡 " + rec)