import streamlit as st

from src.auto_fix import auto_fix_dataset
from src.ui.column_operations import show_column_operations
from src.ui.comparison_dashboard import show_comparison_dashboard
from src.ui.activity_log import add_activity


def show_cleaning(df):

    st.markdown("# 🧹 Smart Cleaning Center")
    st.caption("Interactive AI Powered Data Cleaning")

    st.divider()

    st.subheader("⚙️ Select Cleaning Operations")

    remove_duplicates = st.checkbox(
        "Remove Duplicate Rows",
        value=True
    )

    fill_missing = st.checkbox(
        "Fill Missing Values",
        value=True
    )

    trim_spaces = st.checkbox(
        "Trim Extra Spaces",
        value=True
    )

    standardize_text = st.checkbox(
        "Standardize Text",
        value=True
    )

    optimize_types = st.checkbox(
        "Optimize Data Types",
        value=True
    )

    remove_empty = st.checkbox(
        "Remove Empty Rows",
        value=True
    )

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Rows",
        df.shape[0]
    )

    c2.metric(
        "Columns",
        df.shape[1]
    )

    c3.metric(
        "Missing",
        int(df.isna().sum().sum())
    )

    c4.metric(
        "Duplicates",
        int(df.duplicated().sum())
    )

    st.divider()

    if st.button(
        "🚀 Start Smart Cleaning",
        use_container_width=True,
        type="primary"
    ):

        with st.spinner("Cleaning Dataset..."):

            cleaned_df, report = auto_fix_dataset(
                df,
                remove_duplicates=remove_duplicates,
                fill_missing=fill_missing,
                trim_spaces=trim_spaces,
                standardize_text=standardize_text,
                optimize_types=optimize_types,
                remove_empty=remove_empty
            )

            st.session_state["cleaned_df"] = cleaned_df

            st.success("✅ Dataset cleaned successfully.")

            st.divider()

            st.subheader("📋 Cleaning Report")

            for item in report:

                st.success(item)

            st.divider()

            st.subheader("📊 Before vs After")

            cc1, cc2, cc3, cc4 = st.columns(4)

            cc1.metric(
                "Rows",
                df.shape[0],
                cleaned_df.shape[0] - df.shape[0]
            )

            cc2.metric(
                "Columns",
                df.shape[1],
                cleaned_df.shape[1] - df.shape[1]
            )

            cc3.metric(
                "Missing",
                int(df.isna().sum().sum()),
                int(cleaned_df.isna().sum().sum()) - int(df.isna().sum().sum())
            )

            cc4.metric(
                "Duplicates",
                int(df.duplicated().sum()),
                int(cleaned_df.duplicated().sum()) - int(df.duplicated().sum())
            )

            st.divider()

            show_comparison_dashboard(
                df,
                cleaned_df
            )

            st.divider()

            st.subheader("👀 Cleaned Dataset Preview")

            st.dataframe(
                cleaned_df.head(20),
                use_container_width=True,
                height=400
            )

            st.divider()

            show_column_operations(cleaned_df)

            add_activity("Smart Dataset Cleaning")

    else:

        st.info(
            "Select the cleaning options above and click **Start Smart Cleaning**."
        )

    