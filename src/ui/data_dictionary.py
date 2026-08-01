import streamlit as st
import pandas as pd


def show_data_dictionary(df):

    st.markdown("## 📚 Data Dictionary")

    dictionary = []

    for col in df.columns:

        dictionary.append(
            {
                "Column": col,
                "Data Type": str(df[col].dtype),
                "Non Null": df[col].count(),
                "Missing": df[col].isna().sum(),
                "Unique": df[col].nunique(),
                "Sample Value": str(df[col].dropna().iloc[0]) if df[col].count() > 0 else "-"
            }
        )

    dictionary_df = pd.DataFrame(dictionary)

    st.dataframe(
        dictionary_df,
        use_container_width=True,
        hide_index=True
    )

    csv = dictionary_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Download Data Dictionary",
        csv,
        "data_dictionary.csv",
        "text/csv",
        use_container_width=True
    )