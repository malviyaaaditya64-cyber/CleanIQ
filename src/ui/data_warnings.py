import streamlit as st


def show_data_warnings(df):

    st.markdown("## 🚨 Smart Data Warnings")

    warnings = []

    # Missing Values
    missing = int(df.isna().sum().sum())

    if missing > 0:
        warnings.append(
            f"⚠ Dataset contains {missing} missing values."
        )

    # Duplicate Rows
    duplicates = int(df.duplicated().sum())

    if duplicates > 0:
        warnings.append(
            f"⚠ Dataset contains {duplicates} duplicate rows."
        )

    # Constant Columns
    constant_cols = [
        col for col in df.columns
        if df[col].nunique(dropna=False) == 1
    ]

    if constant_cols:
        warnings.append(
            f"⚠ Constant Columns: {', '.join(constant_cols)}"
        )

    # High Missing Columns
    high_missing = []

    for col in df.columns:

        percent = (df[col].isna().sum() / len(df)) * 100

        if percent > 50:
            high_missing.append(col)

    if high_missing:
        warnings.append(
            f"🔴 More than 50% missing values in: {', '.join(high_missing)}"
        )

    if not warnings:

        st.success("🎉 No major data quality issues detected.")

    else:

        for item in warnings:
            st.warning(item)