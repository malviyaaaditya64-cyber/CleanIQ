import streamlit as st
import pandas as pd
from src.ui.activity_log import add_activity


def show_column_operations(df):

    st.markdown("## 🛠 Column Operations")

    column = st.selectbox(
        "Select Column",
        df.columns
    )

    operation = st.selectbox(
        "Choose Operation",
        [
            "Rename Column",
            "Drop Column",
            "Convert Data Type",
            "Fill Missing Values"
        ]
    )

    if operation == "Rename Column":

        new_name = st.text_input("New Column Name")

        if st.button("Rename"):

            df.rename(
                columns={
                    column: new_name
                },
                inplace=True
            )

            st.success("Column renamed successfully.")
            add_activity("Rename Column")

    elif operation == "Drop Column":

        if st.button("Drop Column"):

            df.drop(
                columns=[column],
                inplace=True
            )

            st.success("Column removed successfully.")
            add_activity("Drop Column")

    elif operation == "Convert Data Type":

        dtype = st.selectbox(
            "Data Type",
            [
                "int",
                "float",
                "str"
            ]
        )

        if st.button("Convert"):

            try:

                df[column] = df[column].astype(dtype)

                st.success("Conversion completed.")
                add_activity("Convert Data Type")

            except Exception as e:

                st.error(e)

    elif operation == "Fill Missing Values":

        method = st.selectbox(
            "Method",
            [
                "Mean",
                "Median",
                "Mode"
            ]
        )

        if st.button("Fill Missing"):

            if method == "Mean":

                df[column].fillna(
                    df[column].mean(),
                    inplace=True
                )

            elif method == "Median":

                df[column].fillna(
                    df[column].median(),
                    inplace=True
                )

            else:

                df[column].fillna(
                    df[column].mode()[0],
                    inplace=True
                )

            st.success("Missing values filled.")
            add_activity("Fill Missing Values")

    return df