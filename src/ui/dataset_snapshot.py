import streamlit as st
import pandas as pd


def show_dataset_snapshot(df):

    st.markdown("## 📋 Dataset Snapshot")

    snapshot = pd.DataFrame({
        "Property": [
            "Rows",
            "Columns",
            "Memory Usage (MB)",
            "Numeric Columns",
            "Categorical Columns",
            "Missing Values",
            "Duplicate Rows"
        ],
        "Value": [
            df.shape[0],
            df.shape[1],
            round(df.memory_usage(deep=True).sum()/1024**2, 2),
            len(df.select_dtypes(include="number").columns),
            len(df.select_dtypes(include="object").columns),
            int(df.isna().sum().sum()),
            int(df.duplicated().sum())
        ]
    })

    st.dataframe(
        snapshot,
        use_container_width=True,
        hide_index=True
    )