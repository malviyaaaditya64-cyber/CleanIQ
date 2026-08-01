import streamlit as st


def show_comparison(original_df, cleaned_df):

    st.markdown("## 📊 Before vs After Comparison")

    col1, col2, col3, col4 = st.columns(4)

    original_missing = int(original_df.isna().sum().sum())
    cleaned_missing = int(cleaned_df.isna().sum().sum())

    original_duplicates = int(original_df.duplicated().sum())
    cleaned_duplicates = int(cleaned_df.duplicated().sum())

    col1.metric(
        "Rows",
        cleaned_df.shape[0],
        cleaned_df.shape[0] - original_df.shape[0]
    )

    col2.metric(
        "Columns",
        cleaned_df.shape[1],
        cleaned_df.shape[1] - original_df.shape[1]
    )

    col3.metric(
        "Missing Values",
        cleaned_missing,
        cleaned_missing - original_missing
    )

    col4.metric(
        "Duplicate Rows",
        cleaned_duplicates,
        cleaned_duplicates - original_duplicates
    )

    st.divider()

    left, right = st.columns(2)

    with left:
        st.subheader("📂 Original Dataset")
        st.dataframe(
            original_df.head(10),
            use_container_width=True
        )

    with right:
        st.subheader("✨ Cleaned Dataset")
        st.dataframe(
            cleaned_df.head(10),
            use_container_width=True
        )