import streamlit as st


def show_history():

    st.markdown("## 📜 Activity History")

    if "activity_log" not in st.session_state:

        st.info("No activity recorded yet.")
        return

    for i, activity in enumerate(
        reversed(st.session_state["activity_log"]),
        start=1
    ):

        st.write(f"**{i}.** {activity}")