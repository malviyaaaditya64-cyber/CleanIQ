import streamlit as st


def load_css():

    st.markdown(
        """
<style>

/* ===============================
   Main App
================================ */

.stApp{
    background:linear-gradient(
        135deg,
        #f8fafc,
        #eef4ff
    );
}

/* ===============================
   Main Container
================================ */

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    max-width:1400px;
}

/* ===============================
   Buttons
================================ */

.stButton>button{

    width:100%;
    height:52px;

    border:none;

    border-radius:14px;

    background:linear-gradient(
        90deg,
        #2563eb,
        #4f46e5
    );

    color:white;

    font-size:16px;

    font-weight:700;

    transition:.25s;
}

.stButton>button:hover{

    transform:translateY(-2px);

    box-shadow:0 10px 25px rgba(37,99,235,.25);

    cursor:pointer;
}

/* ===============================
   Metrics
================================ */

div[data-testid="stMetric"]{

    background:white;

    border-radius:18px;

    padding:18px;

    border:1px solid #e5e7eb;

    box-shadow:0 6px 20px rgba(0,0,0,.08);
}

/* ===============================
   DataFrames
================================ */

div[data-testid="stDataFrame"]{

    border-radius:16px;

    overflow:hidden;

    border:1px solid #dbe4ee;

    box-shadow:0 4px 15px rgba(0,0,0,.05);
}

/* ===============================
   File Uploader
================================ */

div[data-testid="stFileUploader"]{

    border:2px dashed #2563eb;

    border-radius:18px;

    padding:20px;

    background:white;
}

/* ===============================
   Sidebar
================================ */

section[data-testid="stSidebar"]{

    background:#111827;

    color:white;
}

section[data-testid="stSidebar"] *{

    color:white;
}

/* ===============================
   Tabs
================================ */

button[data-baseweb="tab"]{

    border-radius:10px;

    font-weight:600;
}

/* ===============================
   Divider
================================ */

hr{

    margin-top:25px;

    margin-bottom:25px;
}

/* ===============================
   Success
================================ */

div[data-testid="stAlert"]{

    border-radius:14px;
}

</style>
        """,
        unsafe_allow_html=True
    )