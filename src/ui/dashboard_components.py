import streamlit as st


# ==========================================
# HERO SECTION
# ==========================================

def hero_section():

    st.markdown(
        """
        <div style="
            background:linear-gradient(135deg,#2563eb,#7c3aed);
            padding:38px;
            border-radius:24px;
            color:white;
            margin-bottom:28px;
            box-shadow:0 20px 45px rgba(37,99,235,.22);
        ">

            <div style="
                display:flex;
                justify-content:space-between;
                align-items:center;
            ">

                <div>

                    <h1 style="
                        color:white;
                        margin:0;
                        font-size:44px;
                        font-weight:800;
                    ">
                        🧹 CleanIQ
                    </h1>

                    <p style="
                        margin-top:12px;
                        font-size:22px;
                        font-weight:600;
                    ">
                        AI Powered Data Cleaning Platform
                    </p>

                    <p style="
                        opacity:.9;
                        font-size:16px;
                    ">
                        Upload • Analyze • Clean • Validate • Export
                    </p>

                </div>

                <div style="
                    background:rgba(255,255,255,.18);
                    padding:12px 18px;
                    border-radius:50px;
                    font-weight:700;
                    backdrop-filter:blur(10px);
                ">
                    ● LIVE
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ==========================================
# SECTION TITLE
# ==========================================

def section_title(title, subtitle=""):

    st.markdown(
        f"""
        <div style="margin-top:10px;margin-bottom:18px;">

            <h2 style="
                margin-bottom:5px;
                font-weight:800;
            ">
                {title}
            </h2>

            <p style="
                color:#6b7280;
                margin-top:0;
            ">
                {subtitle}
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ==========================================
# EMPTY STATE
# ==========================================

def empty_state():

    st.markdown(
        """
        <div style="
            background:white;
            border-radius:22px;
            padding:45px;
            text-align:center;
            border:1px solid #e5e7eb;
            box-shadow:0 12px 30px rgba(0,0,0,.05);
        ">

            <h2>
                👋 Welcome to CleanIQ
            </h2>

            <p style="
                color:#6b7280;
                font-size:17px;
            ">
                Upload a CSV or Excel dataset to begin intelligent profiling,
                automatic cleaning, AI recommendations and export.
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ==========================================
# FOOTER
# ==========================================

def footer():

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <hr>

        <center>

        <p style="
            color:#6b7280;
            font-size:14px;
        ">

        Built with ❤️ using Python • Streamlit • Pandas

        </p>

        </center>

        """,
        unsafe_allow_html=True,
    )