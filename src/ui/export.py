import streamlit as st
import pandas as pd
import io

from src.report_generator import generate_pdf


def show_export():

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#0f172a,#2563eb,#7c3aed);
    padding:30px;
    border-radius:20px;
    color:white;
    margin-bottom:25px;
    ">

    <h1>💾 Export Center</h1>

    <p style="font-size:18px;">
    Download Cleaned Dataset • Reports • Excel • CSV
    </p>

    </div>
    """, unsafe_allow_html=True)

    if "cleaned_df" not in st.session_state:

        st.warning("⚠ Please clean a dataset first.")
        return

    cleaned_df = st.session_state["cleaned_df"]

    summary = {

        "Rows": cleaned_df.shape[0],

        "Columns": cleaned_df.shape[1],

        "Missing Values": int(cleaned_df.isna().sum().sum()),

        "Duplicate Rows": int(cleaned_df.duplicated().sum())

    }

    st.markdown("## 📊 Export Overview")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("📄 Rows", f"{summary['Rows']:,}")

    with c2:
        st.metric("📑 Columns", summary["Columns"])

    with c3:
        st.metric("❌ Missing", summary["Missing Values"])

    with c4:
        st.metric("🔁 Duplicate", summary["Duplicate Rows"])

    st.divider()

    health_score = 100
    quality_score = 100

    csv = cleaned_df.to_csv(
        index=False
    ).encode("utf-8")

    excel_buffer = io.BytesIO()

    with pd.ExcelWriter(
        excel_buffer,
        engine="openpyxl"
    ) as writer:

        cleaned_df.to_excel(
            writer,
            index=False,
            sheet_name="Cleaned Dataset"
        )

    excel_data = excel_buffer.getvalue()

    pdf_file = "CleanIQ_Report.pdf"

    generate_pdf(
        summary,
        health_score,
        quality_score,
        pdf_file
    )

    st.markdown("## 📥 Download Center")

    col1, col2, col3 = st.columns(3)

    with col1:

         st.download_button(
            "📄 Download CSV",
            data=csv,
            file_name="CleanIQ_Cleaned_Dataset.csv",
            mime="text/csv",
            use_container_width=True,
            type="primary"
        )

    with col2:

        st.download_button(
            "📊 Download Excel",
            data=excel_data,
            file_name="CleanIQ_Cleaned_Dataset.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )

    with col3:

        with open(pdf_file, "rb") as pdf:

            st.download_button(
                "📕 Download PDF Report",
                data=pdf.read(),
                file_name="CleanIQ_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )

    st.divider()

    # ======================================
    # Dataset Preview
    # ======================================

    st.markdown("## 👀 Cleaned Dataset Preview")

    st.dataframe(
        cleaned_df.head(25),
        use_container_width=True,
        height=450
    )

    st.divider()

    # ======================================
    # Export Statistics
    # ======================================

    st.markdown("## 📋 Export Statistics")

    left, right = st.columns(2)

    with left:

        st.info(f"""
### 📊 Dataset Summary

- 📄 Rows : **{summary['Rows']:,}**
- 📑 Columns : **{summary['Columns']}**
- ❌ Missing Values : **{summary['Missing Values']}**
- 🔁 Duplicate Rows : **{summary['Duplicate Rows']}**
""")

    with right:

        st.info("""
### 📦 Available Export Formats

✅ CSV Dataset

✅ Excel Workbook

✅ Professional PDF Report

✅ Ready for Machine Learning

✅ Portfolio Ready
""")

    st.divider()

    st.success("✅ Export completed successfully. Your cleaned dataset is ready for download.")