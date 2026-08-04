import streamlit as st
import traceback
from src.ai_engine import generate_recommendations
from src.ml_readiness import calculate_ml_readiness
from src.quality_score import calculate_quality_score
from src.claude_chat import ask_claude



def show_insights(df):

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#0f172a,#2563eb,#7c3aed);
    padding:30px;
    border-radius:20px;
    color:white;
    margin-bottom:25px;
    ">

    <h1>🧠 AI Intelligence Center</h1>

    <p style="font-size:18px;">
    Executive AI Report • Dataset Intelligence • ML Readiness
    </p>

    </div>
    """, unsafe_allow_html=True)

    # ==========================================
    # Scores
    # ==========================================

    quality_score = calculate_quality_score(df)
    ml_score = calculate_ml_readiness(df)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "🎯 Quality Score",
            f"{quality_score}%"
        )

    with c2:
        st.metric(
            "🤖 ML Readiness",
            f"{ml_score}%"
        )

    with c3:
        st.metric(
            "📄 Rows",
            f"{df.shape[0]:,}"
        )

    with c4:
        st.metric(
            "📑 Columns",
            df.shape[1]
        )

    st.progress(quality_score / 100)

    st.divider()

    # ==========================================
    # Executive Summary
    # ==========================================

    st.markdown("## 📋 Executive Summary")

    missing = int(df.isna().sum().sum())
    duplicate = int(df.duplicated().sum())

    numeric = len(df.select_dtypes(include="number").columns)
    categorical = len(df.select_dtypes(include="object").columns)

    st.info(f"""
### 🤖 AI Summary

Dataset Size : **{df.shape[0]:,} rows**

Columns : **{df.shape[1]}**

Numeric Columns : **{numeric}**

Categorical Columns : **{categorical}**

Missing Values : **{missing}**

Duplicate Rows : **{duplicate}**

Overall Dataset Quality : **{quality_score}%**

Machine Learning Readiness : **{ml_score}%**
""")

    st.divider()


        # ==========================================
    # AI Recommendations
    # ==========================================

    st.markdown("## 💡 AI Recommendations")

    recommendations = generate_recommendations(df)

    good = 0
    warning = 0
    critical = 0

    for item in recommendations:

        if "🟢" in item or "✅" in item:
            good += 1

        elif "🟡" in item:
            warning += 1

        elif "🔴" in item:
            critical += 1

    a, b, c = st.columns(3)

    with a:
        st.metric("✅ Good", good)

    with b:
        st.metric("⚠️ Warning", warning)

    with c:
        st.metric("🚨 Critical", critical)

    st.divider()

    # ==========================================
    # Detailed Recommendations
    # ==========================================

    for rec in recommendations:

        if "🔴" in rec:
            st.error(rec)

        elif "🟡" in rec:
            st.warning(rec)

        elif "🟢" in rec or "✅" in rec:
            st.success(rec)

        else:
            st.info(rec)

    st.divider()

    # ==========================================
    # Business Intelligence
    # ==========================================

    st.markdown("## 📊 Business Intelligence")

    left, right = st.columns(2)

    with left:

        st.info(f"""
### 📈 Dataset Statistics

• Total Cells : **{df.shape[0] * df.shape[1]:,}**

• Memory Usage : **{round(df.memory_usage(deep=True).sum()/1024/1024,2)} MB**

• Numeric Columns : **{numeric}**

• Categorical Columns : **{categorical}**
""")

    with right:

        if ml_score >= 90:
            readiness = "🟢 Production Ready"

        elif ml_score >= 70:
            readiness = "🟡 Needs Minor Cleaning"

        else:
            readiness = "🔴 Not Ready"

        st.info(f"""
### 🤖 AI Assessment

Status : **{readiness}**

Quality Score : **{quality_score}%**

ML Readiness : **{ml_score}%**
""")

    st.divider()


        # ==========================================
    # AI Executive Report
    # ==========================================

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#0f172a,#1d4ed8,#7c3aed);
    padding:28px;
    border-radius:20px;
    color:white;
    margin-bottom:20px;
    ">

    <h2 style="color:white;">
    🧠 AI Executive Report
    </h2>

    <p style="font-size:18px;">
    CleanIQ has completed an AI-powered assessment of your dataset.
    </p>

    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🎯 Quality Score",
            f"{quality_score}%"
        )

    with col2:
        st.metric(
            "🤖 ML Readiness",
            f"{ml_score}%"
        )

    with col3:

        if quality_score >= 90:
            risk = "🟢 LOW"

        elif quality_score >= 70:
            risk = "🟡 MEDIUM"

        else:
            risk = "🔴 HIGH"

        st.metric(
            "⚠️ Risk Level",
            risk
        )

    st.progress(quality_score / 100)

    if quality_score >= 90:

        st.success(
            "✅ Dataset is production-ready for Machine Learning."
        )

    elif quality_score >= 70:

        st.warning(
            "⚠ Dataset is usable but additional cleaning is recommended."
        )

    else:

        st.error(
            "🚨 Dataset requires significant cleaning before Machine Learning."
        )

    st.divider()

    # ==========================================
    # Recommended Next Steps
    # ==========================================

    st.markdown("## 🚀 Recommended Next Steps")

    roadmap = [

        "🧹 Clean missing values and duplicate records",

        "📊 Explore feature distributions using interactive charts",

        "🏷️ Encode categorical columns before model training",

        "📏 Scale numerical features where required",

        "🤖 Train Machine Learning models",

        "📈 Evaluate model performance",

        "🚀 Deploy the final ML model"

    ]

    for step in roadmap:
        st.write(step)

    st.divider()

    # ==========================================
    # Final AI Status
    # ==========================================

    if quality_score >= 90 and ml_score >= 90:

        st.success(
            "🏆 Excellent! Your dataset is highly suitable for Machine Learning."
        )

    elif quality_score >= 70:

        st.warning(
            "⚠️ Dataset is usable but a few improvements are recommended before ML training."
        )

    else:

        st.error(
            "🚨 Dataset quality is low. Perform cleaning before building ML models."
        )

    st.divider()

    st.success("✅ AI Executive Analysis Completed Successfully")

    st.divider()

    

        # ==========================================
    # Ask CleanIQ
    # ==========================================

    st.markdown("## 💬 Ask CleanIQ")
    st.caption("Ask anything about your dataset.")

    st.markdown("### ⚡ Quick Questions")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        if st.button("📄 Rows"):
            st.session_state.chat_question = "rows"

    with c2:
        if st.button("❌ Missing"):
            st.session_state.chat_question = "missing values"

    with c3:
        if st.button("📑 Columns"):
            st.session_state.chat_question = "columns"

    with c4:
        if st.button("📊 Memory"):
            st.session_state.chat_question = "memory"

    default_question = st.session_state.get("chat_question", "")

    question = st.text_input(
        "Type your question",
        value=default_question,
        placeholder="Example: How many missing values?"
    )

    if question:

        with st.spinner("🤖 Claude Sonnet 5 is analyzing your dataset..."):

            try:

                response = ask_claude(df, question)

                st.chat_message("user").write(question)
                st.chat_message("assistant").write(response)

            except Exception as e:

                traceback.print_exc()
                st.exception(e)