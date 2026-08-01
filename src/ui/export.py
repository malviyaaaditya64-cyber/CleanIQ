import streamlit as st
import pandas as pd
import io

from src.report_generator import generate_pdf


def show_export():

    st.markdown("# 💾 Export Center")
    st.caption("Export your cleaned dataset and reports")

    st.divider()

    if "cleaned_df" not in st.session_state:

        st.warning("⚠ Please clean a dataset first.")
        return

    cleaned_df = st.session_state["cleaned_df"]

    # =====================================
    # Dataset Summary
    # =====================================

    summary = {
        "Rows": cleaned_df.shape[0],
        "Columns": cleaned_df.shape[1],
        "Missing Values": int(cleaned_df.isna().sum().sum()),
        "Duplicate Rows": int(cleaned_df.duplicated().sum())
    }

    health_score = 100
    quality_score = 100

    # =====================================
    # CSV
    # =====================================

    csv = cleaned_df.to_csv(index=False).encode("utf-8")

    # =====================================
    # Excel
    # =====================================

    excel_buffer = io.BytesIO()

    with pd.ExcelWriter(excel_buffer, engine="openpyxl") as writer:

        cleaned_df.to_excel(
            writer,
            index=False,
            sheet_name="Cleaned Dataset"
        )

    excel_data = excel_buffer.getvalue()

    # =====================================
    # PDF
    # =====================================

    pdf_file = "CleanIQ_Report.pdf"

    generate_pdf(
        summary,
        health_score,
        quality_score,
        pdf_file
    )

    # =====================================
    # Download Buttons
    # =====================================

    st.subheader("📥 Download Files")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.download_button(
            "📄 CSV",
            csv,
            "cleaned_dataset.csv",
            "text/csv",
            use_container_width=True,
            type="primary"
        )

    with c2:

        st.download_button(
            "📊 Excel",
            excel_data,
            "cleaned_dataset.xlsx",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )

    with c3:

        with open(pdf_file, "rb") as pdf:

            st.download_button(
                "📕 PDF Report",
                pdf.read(),
                "CleanIQ_Report.pdf",
                "application/pdf",
                use_container_width=True
            )

    st.divider()

    # =====================================
    # Preview
    # =====================================

    st.subheader("👀 Cleaned Dataset Preview")

    st.dataframe(
        cleaned_df.head(20),
        use_container_width=True,
        height=420
    )

    st.divider()

    # =====================================
    # Export Summary
    # =====================================

    st.subheader("📋 Export Summary")

    st.write(f"**Rows:** {summary['Rows']:,}")
    st.write(f"**Columns:** {summary['Columns']}")
    st.write(f"**Missing Values:** {summary['Missing Values']}")
    st.write(f"**Duplicate Rows:** {summary['Duplicate Rows']}")

    st.divider()

    st.success("✅ Export completed successfully.")