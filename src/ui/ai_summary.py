import streamlit as st


def show_ai_summary(df):

    st.markdown("## 🤖 AI Dataset Summary")

    rows = df.shape[0]
    cols = df.shape[1]

    missing = int(df.isna().sum().sum())
    duplicates = int(df.duplicated().sum())

    numeric = len(df.select_dtypes(include="number").columns)
    categorical = len(df.select_dtypes(include="object").columns)

    summary = f"""
This dataset contains **{rows:,} rows** and **{cols} columns**.

It has **{numeric} numeric columns** and **{categorical} categorical columns**.

There are **{missing} missing values** and **{duplicates} duplicate rows**.

Overall, the dataset is suitable for analysis after applying the recommended cleaning steps.
"""

    st.success(summary)