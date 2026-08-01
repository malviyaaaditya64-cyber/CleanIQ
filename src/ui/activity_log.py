import streamlit as st
from datetime import datetime


def add_activity(action):

    if "activity_log" not in st.session_state:

        st.session_state["activity_log"] = []

    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    st.session_state["activity_log"].append(
        f"{timestamp}  |  {action}"
    )