import streamlit as st


def load_css():

    st.markdown("""
<style>

/* ===================================================
GOOGLE FONT
=================================================== */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

html,
body,
[class*="css"]{

    font-family:'Inter',sans-serif;

}


/* ===================================================
APP BACKGROUND
=================================================== */

.stApp{

    background:
    linear-gradient(
        135deg,
        #f5f7ff 0%,
        #eef4ff 35%,
        #ffffff 70%,
        #f8fafc 100%
    );

}


/* ===================================================
MAIN CONTAINER
=================================================== */

.block-container{

    max-width:1450px;

    padding-top:2rem;

    padding-left:2.8rem;

    padding-right:2.8rem;

    padding-bottom:3rem;

}


/* ===================================================
SIDEBAR
=================================================== */

section[data-testid="stSidebar"]{

    background:rgba(255,255,255,.82);

    backdrop-filter:blur(18px);

    border-right:1px solid rgba(0,0,0,.05);

    box-shadow:8px 0 35px rgba(0,0,0,.06);

}

section[data-testid="stSidebar"] *{

    color:#111827;

}


/* ===================================================
HEADINGS
=================================================== */

h1{

    font-size:44px !important;

    font-weight:800 !important;

    color:#111827;

}

h2{

    font-size:32px !important;

    font-weight:700 !important;

}

h3{

    font-size:24px !important;

    font-weight:700 !important;

}


/* ===================================================
METRIC CARDS
=================================================== */

div[data-testid="metric-container"]{

    background:rgba(255,255,255,.92);

    border-radius:22px;

    padding:22px;

    border:1px solid rgba(37,99,235,.10);

    box-shadow:
        0 12px 30px rgba(0,0,0,.06);

    transition:.25s;

}

div[data-testid="metric-container"]:hover{

    transform:translateY(-6px);

    box-shadow:
        0 20px 40px rgba(37,99,235,.15);

}


/* ===================================================
BUTTONS
=================================================== */

.stButton>button{

    width:100%;

    height:54px;

    border:none;

    border-radius:16px;

    font-size:16px;

    font-weight:700;

    color:white;

    background:
    linear-gradient(
        90deg,
        #2563eb,
        #4f46e5,
        #7c3aed
    );

    box-shadow:
        0 12px 28px rgba(37,99,235,.25);

    transition:.3s;

}

.stButton>button:hover{

    transform:translateY(-3px);

    box-shadow:
        0 18px 40px rgba(37,99,235,.35);

        /* ===================================================
DATAFRAME
=================================================== */

div[data-testid="stDataFrame"]{

    border-radius:20px;

    overflow:hidden;

    border:1px solid rgba(37,99,235,.10);

    box-shadow:
        0 10px 25px rgba(0,0,0,.06);

}


/* ===================================================
FILE UPLOADER
=================================================== */

section[data-testid="stFileUploader"]{

    background:rgba(255,255,255,.95);

    border:2px dashed #2563eb;

    border-radius:22px;

    padding:20px;

    box-shadow:
        0 12px 25px rgba(37,99,235,.08);

}


/* ===================================================
TABS
=================================================== */

button[data-baseweb="tab"]{

    border-radius:12px;

    font-weight:700;

    font-size:15px;

    transition:.25s;

}

button[data-baseweb="tab"]:hover{

    background:#eef4ff;

}


/* ===================================================
ALERTS
=================================================== */

div[data-baseweb="notification"]{

    border-radius:16px;

}


/* ===================================================
HORIZONTAL LINE
=================================================== */

hr{

    margin-top:30px;

    margin-bottom:30px;

    border:none;

    height:1px;

    background:#e5e7eb;

}


/* ===================================================
SCROLLBAR
=================================================== */

::-webkit-scrollbar{

    width:10px;

}

::-webkit-scrollbar-track{

    background:#edf2f7;

}

::-webkit-scrollbar-thumb{

    background:linear-gradient(
        180deg,
        #2563eb,
        #7c3aed
    );

    border-radius:30px;

}


/* ===================================================
ANIMATION
=================================================== */

@keyframes fadeUp{

    from{

        opacity:0;

        transform:translateY(18px);

    }

    to{

        opacity:1;

        transform:translateY(0);

    }

}

.block-container{

    animation:fadeUp .45s ease;

}

</style>
""", unsafe_allow_html=True)


