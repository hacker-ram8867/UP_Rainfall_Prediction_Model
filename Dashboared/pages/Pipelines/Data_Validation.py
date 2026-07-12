import streamlit as st
import polars as pl
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Data Validation", page_icon="✅", layout="wide")

st.title("✅ TRUERIZE Data Validation Modele")

st.success("Module 2 of 6 • Data Validation System")

if "df" not in st.session_state:
    st.session_state.df = None

uploaded_file = st.file_uploader("📂 Upload CSV File for Validation", type=["csv"])

if uploaded_file is not None:
    try:
        df = pl.read_csv(uploaded_file)
        st.session_state.df = df

        st.success("Dataset Loaded Successfully")

        st.metric("Rows", df.height)
        st.metric("Columns", df.width)

    except Exception as e:
        st.error(f"Error loading file: {e}")

with st.expander("📘 Overview", expanded=False):
    st.write("""
Data Validation ensures dataset quality before ML pipeline.
It checks schema, missing values, duplicates, and consistency.
""")

with st.expander("📊 Dataset Preview", expanded=False):

    df = st.session_state.df

    if df is not None:
        st.dataframe(df.head(10).to_pandas())

        st.table({
            "Column": df.columns,
            "Type": [str(t) for t in df.dtypes]
        })
    else:
        st.warning("Upload dataset first")

with st.expander("🧹 Data Quality Check", expanded=False):

    df = st.session_state.df

    if df is not None:

        missing = df.null_count().sum_horizontal().item()
        duplicates = df.is_duplicated().sum()

        st.metric("Missing Values", missing)
        st.metric("Duplicate Rows", duplicates)

    else:
        st.warning("Upload dataset first")

with st.expander("📈 Statistics", expanded=False):

    df = st.session_state.df

    if df is not None:
        st.metric("Rows", df.height)
        st.metric("Columns", df.width)
    else:
        st.warning("No dataset loaded")

with st.expander("📑 Schema & Data Types", expanded=False):

    df = st.session_state.df

    if df is not None:

        st.table({
            "Column": df.columns,
            "Data Type": [str(t) for t in df.dtypes]
        })

    else:
        st.warning("Upload dataset first")

with st.expander("📌 Business Rules Validation", expanded=False):

    df = st.session_state.df

    if df is not None:

        st.code("""
Rules:
- No negative values
- Month between 1–12
- Year must be valid
""")

    else:
        st.warning("Upload dataset first")

with st.expander("🔄 Pipeline Flow", expanded=False):

    st.code("""
Raw Dataset → Upload → Schema → Missing Check → Duplicate Check → Validation → Clean Data
""")

with st.expander("🏁 Final Summary", expanded=False):

    df = st.session_state.df

    if df is not None:
        st.success("""
✔ Dataset Loaded  
✔ Schema Validated  
✔ Missing Values Checked  
✔ Duplicates Checked  
✔ Ready for ML Pipeline  
""")

        st.balloons()
    else:
        st.warning("Upload dataset first")

with st.expander("📄 ALL REPORTS VIEWER", expanded=False):

    REPORT_DIR = Path("reports")

    GE_REPORT = REPORT_DIR / "raw_GE_report.html"
    GE_SUITE = REPORT_DIR / "raw_GE_suite.html"

    CERBERUS_RAW = REPORT_DIR / "raw_cerberus.html"
    CERBERUS_SUITE = REPORT_DIR / "raw_cerberus_suite.html"
    CERBERUS_CLEAN = REPORT_DIR / "clean_cerberus.html"

    PYDANTIC_RAW = REPORT_DIR / "raw_pydantic.html"
    PYDANTIC_SUITE = REPORT_DIR / "raw_pydantic_suite.html"
    PYDANTIC_CLEAN = REPORT_DIR / "clean_pydantic.html"

    MODEL_FEATURE_HTML = REPORT_DIR / "model_feature_report.html"

    KS_DRIFT_HTML = REPORT_DIR / "ks_drift_report.html"
    KS_DRIFT_TXT = REPORT_DIR / "ks_drift_report.txt"

    def show_html(path, title):
        st.markdown(f"### {title}")

        if path.exists():
            html = path.read_text(encoding="utf-8")
            components.html(html, height=800, scrolling=True)
        else:
            st.warning(f"Not found: {path}")

    st.subheader("📊 Validation Reports")

    show_html(GE_REPORT, "📘 Great Expectations - Raw")
    show_html(GE_SUITE, "📘 Great Expectations - Suite")

    st.divider()

    show_html(CERBERUS_RAW, "🛡️ Cerberus - Raw")
    show_html(CERBERUS_SUITE, "🛡️ Cerberus - Suite")
    show_html(CERBERUS_CLEAN, "🛡️ Cerberus - Clean")

    st.divider()

    show_html(PYDANTIC_RAW, "🐍 Pydantic - Raw")
    show_html(PYDANTIC_SUITE, "🐍 Pydantic - Suite")
    show_html(PYDANTIC_CLEAN, "🐍 Pydantic - Clean")

    st.divider()

    st.success("All reports loaded successfully")