import streamlit as st


def show_chat_assistant(df):

    st.markdown("## 🤖 Ask CleanIQ")

    question = st.text_input(
        "Ask something about your dataset..."
    )

    if not question:
        return

    q = question.lower()

    if "missing" in q:

        st.success(
            f"Dataset has {int(df.isna().sum().sum())} missing values."
        )

    elif "duplicate" in q:

        st.success(
            f"Dataset has {int(df.duplicated().sum())} duplicate rows."
        )

    elif "rows" in q:

        st.success(
            f"Dataset contains {df.shape[0]} rows."
        )

    elif "columns" in q:

        st.success(
            f"Dataset contains {df.shape[1]} columns."
        )

    elif "numeric" in q:

        cols = list(
            df.select_dtypes(include="number").columns
        )

        st.write(cols)

    elif "categorical" in q:

        cols = list(
            df.select_dtypes(include="object").columns
        )

        st.write(cols)

    else:

        st.info(
            "I cannot answer that yet. More AI capabilities coming soon."
        )