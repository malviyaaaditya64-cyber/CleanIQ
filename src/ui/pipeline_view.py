import streamlit as st
import pandas as pd


def show_pipeline(manager):

    st.markdown("## ⚙️ Cleaning Pipeline")

    if len(manager.get_pipeline()) == 0:

        st.info("No operations performed yet.")

        return

    df = pd.DataFrame(manager.get_pipeline())

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )