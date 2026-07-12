from pathlib import Path
import sys
import streamlit as st
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import truerize

st.set_page_config(
    page_title="TRUERIZE Dashboard",
    page_icon="🌧️",
    layout="wide",
    initial_sidebar_state="expanded"
)

BASE_DIR = Path(__file__).parent

LOGO = BASE_DIR / "assets" / "logo.png"

REPORT_DIR = BASE_DIR.parent / "reports"
OUTPUT_DIR = BASE_DIR.parent / "outputs"
MODEL_DIR = BASE_DIR.parent / "models"
DATA_DIR = BASE_DIR.parent / "data"
UPLOAD_DIR = BASE_DIR.parent / "uploads"
XAI_DIR = BASE_DIR.parent / "xai"
TEMP_DIR = BASE_DIR.parent / "temp"
LOG_DIR = BASE_DIR.parent / "logs"

for folder in [
    REPORT_DIR,
    OUTPUT_DIR,
    MODEL_DIR,
    DATA_DIR,
    UPLOAD_DIR,
    XAI_DIR,
    TEMP_DIR,
    LOG_DIR,
]:
    folder.mkdir(parents=True, exist_ok=True)

if "raw_df" not in st.session_state:
    st.session_state.raw_df = None

if "clean_df" not in st.session_state:
    st.session_state.clean_df = None

if "model" not in st.session_state:
    st.session_state.model = None

if "prediction" not in st.session_state:
    st.session_state.prediction = None

if "shap_values" not in st.session_state:
    st.session_state.shap_values = None

if "lime_exp" not in st.session_state:
    st.session_state.lime_exp = None

if "drift_results" not in st.session_state:
    st.session_state.drift_results = None

if "metrics" not in st.session_state:
    st.session_state.metrics = None

if "feature_importance" not in st.session_state:
    st.session_state.feature_importance = None

with st.sidebar:

    if LOGO.exists():
        st.image(str(LOGO), use_container_width=True)

    st.title("🌧️ TRUERIZE")
    st.caption("End-to-End Machine Learning Dashboard")

    st.divider()

    st.subheader("Navigation")

    pages = [
        ("app.py", "🏠 Home"),
        ("pages/1_Polars_Configuration.py", "🧹 Polars Configuration"),
        ("pages/2_Data_Validation.py", "✅ Data Validation"),
        ("pages/3_Data_Preprocessing.py", "⚙️ Data Preprocessing"),
        ("pages/4_Statistics_Drift.py", "📊 Statistics & Drift"),
        ("pages/5_Model_Training.py", "🤖 Model Training"),
        ("pages/6_XAI.py", "🧠 Explainable AI"),
        ("pages/7_Report_Viewer.py", "📄 Report Viewer"),
    ]

    for page, label in pages:
        try:
            st.page_link(page, label=label)
        except Exception:
            pass

    st.divider()

    st.success("✅ Pipeline Ready")
    st.info("Use the navigation panel to execute every module.")

left, right = st.columns([3, 1])

with left:
    st.title("🌧️ TRUERIZE Dashboard")
    st.subheader("Professional End-to-End Machine Learning Platform")

with right:
    if LOGO.exists():
        st.image(str(LOGO), use_container_width=True)

st.divider()

st.header("Dashboard Overview")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Pipeline Modules", "7")
c2.metric("Validation Engines", "3")
c3.metric("Reports", "15+")
c4.metric("Status", "Ready")

st.divider()

st.success("Welcome to TRUERIZE Dashboard")

pipeline = pd.DataFrame(
    {
        "Stage": [1,2,3,4,5,6,7],
        "Module": [
            "Polars",
            "Validation",
            "Preprocessing",
            "Statistics",
            "Drift",
            "Training",
            "Explainable AI",
        ],
        "Status": ["Ready"] * 7,
    }
)

st.dataframe(
    pipeline,
    use_container_width=True,
    hide_index=True,
)

st.success("🎉 Dashboard Loaded Successfully")