import streamlit as st

from src.auto_fix import auto_fix_dataset
from src.ui.column_operations import show_column_operations
from src.ui.comparison_dashboard import show_comparison_dashboard
from src.ui.activity_log import add_activity


def show_cleaning(df):

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#0f172a,#2563eb,#7c3aed);
    padding:30px;
    border-radius:20px;
    color:white;
    margin-bottom:25px;
    ">

    <h1>🧹 Smart Cleaning Center</h1>

    <p style="font-size:18px;">
    AI Powered Automated Data Cleaning & Quality Improvement
    </p>

    </div>
    """, unsafe_allow_html=True)

    # ======================================
    # Dataset Summary
    # ======================================

    st.markdown("## 📊 Current Dataset Status")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "📄 Rows",
            f"{df.shape[0]:,}"
        )

    with c2:
        st.metric(
            "📑 Columns",
            df.shape[1]
        )

    with c3:
        st.metric(
            "❌ Missing Values",
            int(df.isna().sum().sum())
        )

    with c4:
        st.metric(
            "🔁 Duplicate Rows",
            int(df.duplicated().sum())
        )

    st.divider()

    # ======================================
    # Cleaning Options
    # ======================================

    st.markdown("## ⚙️ AI Cleaning Options")

    left, right = st.columns(2)

    with left:

        remove_duplicates = st.checkbox(
            "🗑️ Remove Duplicate Rows",
            value=True
        )

        fill_missing = st.checkbox(
            "🩹 Fill Missing Values",
            value=True
        )

        trim_spaces = st.checkbox(
            "✂️ Trim Extra Spaces",
            value=True
        )

    with right:

        standardize_text = st.checkbox(
            "🔤 Standardize Text",
            value=True
        )

        optimize_types = st.checkbox(
            "⚡ Optimize Data Types",
            value=True
        )

        remove_empty = st.checkbox(
            "🧹 Remove Empty Rows",
            value=True
        )

    st.divider()

    st.markdown("### 🚀 Ready to Clean?")

    if st.button(
        "🚀 Start AI Smart Cleaning",
        use_container_width=True,
        type="primary"
    ):

        progress = st.progress(0)

        with st.spinner("Cleaning dataset..."):

            progress.progress(20)

            cleaned_df, report = auto_fix_dataset(
                df,
                remove_duplicates=remove_duplicates,
                fill_missing=fill_missing,
                trim_spaces=trim_spaces,
                standardize_text=standardize_text,
                optimize_types=optimize_types,
                remove_empty=remove_empty
            )

            progress.progress(60)

            st.session_state["cleaned_df"] = cleaned_df

            progress.progress(100)

            st.success("✅ Smart Cleaning Completed Successfully")

            st.divider()


                        # ======================================
            # Cleaning Report
            # ======================================

            st.markdown("## 📋 Cleaning Report")

            for item in report:
                st.success(item)

            st.divider()

            # ======================================
            # Before vs After
            # ======================================

            st.markdown("## 📈 Before vs After Comparison")

            b1, b2, b3, b4 = st.columns(4)

            before_missing = int(df.isna().sum().sum())
            after_missing = int(cleaned_df.isna().sum().sum())

            before_duplicates = int(df.duplicated().sum())
            after_duplicates = int(cleaned_df.duplicated().sum())

            with b1:
                st.metric(
                    "Rows",
                    df.shape[0],
                    cleaned_df.shape[0] - df.shape[0]
                )

            with b2:
                st.metric(
                    "Columns",
                    df.shape[1],
                    cleaned_df.shape[1] - df.shape[1]
                )

            with b3:
                st.metric(
                    "Missing",
                    before_missing,
                    after_missing - before_missing
                )

            with b4:
                st.metric(
                    "Duplicates",
                    before_duplicates,
                    after_duplicates - before_duplicates
                )

            st.divider()

            show_comparison_dashboard(
                df,
                cleaned_df
            )

            st.divider()

            # ======================================
            # Cleaned Dataset Preview
            # ======================================

            st.markdown("## 👀 Cleaned Dataset Preview")

            st.dataframe(
                cleaned_df.head(25),
                use_container_width=True,
                height=420
            )

            st.divider()

            # ======================================
            # Column Operations
            # ======================================

            show_column_operations(cleaned_df)

            st.divider()

            # ======================================
            # Download
            # ======================================

            csv = cleaned_df.to_csv(index=False).encode("utf-8")

            st.download_button(
                "⬇️ Download Cleaned Dataset",
                csv,
                file_name="CleanIQ_Cleaned_Dataset.csv",
                mime="text/csv",
                use_container_width=True
            )

            add_activity("Smart Dataset Cleaning Completed")

    else:

        st.info(
            "👆 Select cleaning options and click **Start AI Smart Cleaning** to clean your dataset."
        )

    