import streamlit as st


def show_comparison_dashboard(original_df, cleaned_df):

    st.markdown("## 📈 Before vs After Dashboard")

    original_missing = int(original_df.isna().sum().sum())
    cleaned_missing = int(cleaned_df.isna().sum().sum())

    original_duplicates = int(original_df.duplicated().sum())
    cleaned_duplicates = int(cleaned_df.duplicated().sum())

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Missing Values",
            original_missing,
            cleaned_missing - original_missing
        )

    with col2:
        st.metric(
            "Duplicate Rows",
            original_duplicates,
            cleaned_duplicates - original_duplicates
        )

    st.divider()

    left, right = st.columns(2)

    with left:
        st.subheader("Original Dataset")
        st.dataframe(
            original_df.head(10),
            use_container_width=True
        )

    with right:
        st.subheader("Cleaned Dataset")
        st.dataframe(
            cleaned_df.head(10),
            use_container_width=True
        )