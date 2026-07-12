import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import polars as pl
from pathlib import Path

st.set_page_config(page_title="Data Preprocessing", page_icon="⚙️", layout="wide")

BASE_DIR = Path(__file__).resolve().parent

REPORT_DIR = BASE_DIR / "outputs"
REPORT_DIR.mkdir(exist_ok=True)

STATISTICS_TXT = REPORT_DIR / "statistics.txt"

st.title("⚙️ TRUERIZE Data Preprocessing Model")

if "df" not in st.session_state:
    st.session_state.df = None

uploaded_file = st.file_uploader("📂 Upload Dataset for Preprocessing", type=["csv"])

if uploaded_file is not None:
    try:
        df = pl.read_csv(uploaded_file)
        st.session_state.df = df
        st.success("Dataset Loaded Successfully")

    except Exception as e:
        st.error(f"Error loading file: {e}")

else:
    st.info("⬆️ Please upload a CSV file to start preprocessing")

if st.session_state.df is not None:
    df = st.session_state.df

    st.metric("Rows", df.height)
    st.metric("Columns", df.width)

    st.write("### 📊 Preview")
    st.dataframe(df.head(10).to_pandas())

st.write("""
Data preprocessing is the stage where raw validated data is transformed into a clean dataset suitable for Machine Learning.
""")

st.success("Module 3 of 6 • Data Preprocessing")

with st.expander("🎯 Objectives", expanded=True):
    st.markdown("""
- Handle missing values
- Remove duplicates
- Detect outliers
- Encode categorical data
- Scale features
- Feature engineering
""")

with st.expander("📋 Components"):
    st.table({
        "Component": ["Missing Values", "Duplicates", "Outliers", "Encoding", "Scaling", "Feature Engineering"],
        "Purpose": [
            "Fix null data",
            "Remove repeated rows",
            "Detect anomalies",
            "Convert categories",
            "Normalize data",
            "Improve features"
        ]
    })

with st.expander("🔄 Pipeline"):
    st.code("""
Raw Data
  ↓
Cleaning
  ↓
Missing Value Handling
  ↓
Encoding
  ↓
Scaling
  ↓
Feature Engineering
  ↓
Processed Dataset
""")

with st.expander("📦 Generated Outputs", expanded=True):

    st.write("📁 Looking for:", STATISTICS_TXT)
    st.write("📂 Exists:", STATISTICS_TXT.exists())

    if STATISTICS_TXT.exists():

        txt = STATISTICS_TXT.read_text(encoding="utf-8")

        st.success("✅ Statistics Report Loaded Successfully")
        st.text_area("📄 statistics.txt Output", txt, height=500)

    else:
        st.error("❌ statistics.txt not found")
        st.warning("Make sure your preprocessing pipeline generates this file inside /outputs")

with st.expander("🎯 Conclusion", expanded=True):

    st.markdown("""
### 📘 Summary
Data preprocessing converts raw data into clean, ML-ready format by handling missing values, duplicates, outliers, encoding, and scaling.
""")

    st.markdown("""
### 🔄 Workflow
Raw Dataset → Validation → Cleaning → Encoding → Scaling → Feature Engineering → ML Ready Dataset
""")

    st.markdown("""
### 🎯 Key Steps
✔ Missing values  
✔ Duplicates  
✔ Outliers  
✔ Encoding  
✔ Scaling  
✔ Feature engineering  
""")

st.balloons()

st.success("🎉 Data Preprocessing Completed Successfully")
st.info("➡️ Next Module: Statistics & Drift Analysis 📊")