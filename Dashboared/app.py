from pathlib import Path
import sys

import streamlit as st
import pandas as pd

# ---------------------------------------------------------------------
# Project Root
# ---------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# ---------------------------------------------------------------------
# Streamlit Config
# ---------------------------------------------------------------------
st.set_page_config(
    page_title="TRUERIZE Dashboard",
    page_icon="🌧️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------
# Directories
# ---------------------------------------------------------------------
BASE_DIR = Path(__file__).parent

LOGO = BASE_DIR / "assets" / "logo.png"

REPORT_DIR = ROOT / "reports"
OUTPUT_DIR = ROOT / "outputs"
MODEL_DIR = ROOT / "models"
DATA_DIR = ROOT / "data"
UPLOAD_DIR = ROOT / "uploads"
XAI_DIR = ROOT / "xai"
TEMP_DIR = ROOT / "temp"
LOG_DIR = ROOT / "logs"

for folder in (
    REPORT_DIR,
    OUTPUT_DIR,
    MODEL_DIR,
    DATA_DIR,
    UPLOAD_DIR,
    XAI_DIR,
    TEMP_DIR,
    LOG_DIR,
):
    folder.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------
# Session State
# ---------------------------------------------------------------------
defaults = {
    "raw_df": None,
    "clean_df": None,
    "model": None,
    "prediction": None,
    "shap_values": None,
    "lime_exp": None,
    "drift_results": None,
    "metrics": None,
    "feature_importance": None,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ---------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------
with st.sidebar:

    if LOGO.exists():
        st.image(LOGO, use_container_width=True)

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
    st.info("Use the navigation panel to execute each module.")

# ---------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------
left, right = st.columns([3, 1])

with left:
    st.title("🌧️ TRUERIZE Dashboard")
    st.subheader("Professional End-to-End Machine Learning Platform")

with right:
    if LOGO.exists():
        st.image(LOGO, use_container_width=True)

st.divider()

# ---------------------------------------------------------------------
# Overview
# ---------------------------------------------------------------------
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
        "Stage": [1, 2, 3, 4, 5, 6, 7],
        "Module": [
            "Polars Configuration",
            "Data Validation",
            "Data Preprocessing",
            "Statistics & Drift",
            "Model Training",
            "Explainable AI",
            "Report Viewer",
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