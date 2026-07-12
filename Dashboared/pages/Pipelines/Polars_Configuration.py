import streamlit as st
import polars as pl

st.set_page_config(page_title="Polars Configuration", page_icon="🧹", layout="wide")

st.title("🧹 Polars Configuration Model")

if "df" not in st.session_state:
    st.session_state.df = None

with st.expander("📂 DATA LOADING (UPLOAD DATASET)", expanded=False):

    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

    if uploaded_file is not None:
        try:
            df = pl.read_csv(uploaded_file)
            st.session_state.df = df

            st.success("Dataset Uploaded Successfully")

            st.metric("Rows", df.height)
            st.metric("Columns", df.width)

            st.dataframe(df.head(10).to_pandas())

        except Exception as e:
            st.error(f"Error reading file: {e}")

    else:
        st.info("⬆️ Please upload a CSV file")

with st.expander("📖 OVERVIEW & POLARS", expanded=False):

    st.write("Polars is a fast DataFrame library written in Rust.")

    st.info("Optimized for speed, memory efficiency, and multi-threading")

with st.expander("📊 PANDAS VS POLARS", expanded=False):

    st.table({
        "Feature": ["Speed", "Memory", "Execution"],
        "Pandas": ["Medium", "High", "Single Thread"],
        "Polars": ["Very Fast", "Low", "Multi Thread"]
    })

    st.code("pip install polars")

with st.expander("📊 DATA EXPLORATION", expanded=False):

    df = st.session_state.df

    if df is not None:

        st.dataframe(df.head(10).to_pandas())

        st.table({
            "Index": list(range(1, len(df.columns) + 1)),
            "Column": df.columns,
            "Type": [str(t) for t in df.dtypes]
        })

    else:
        st.warning("⚠️ Please upload dataset first")

with st.expander("🧹 CLEANING + TRANSFORMATION", expanded=False):

    df = st.session_state.df

    if df is not None:

        missing = df.null_count().sum_horizontal().item()
        duplicates = df.is_duplicated().sum()

        st.metric("Missing Values", missing)
        st.metric("Duplicate Rows", duplicates)

        st.info("Encoding → Scaling → Feature Engineering")

    else:
        st.warning("⚠️ Load dataset first")

with st.expander("🚀 FULL PIPELINE + ANALYSIS", expanded=False):

    df = st.session_state.df

    st.subheader("Polars Workflow")

    st.code("""
RAW DATA → LOAD → CLEAN → TRANSFORM → ANALYZE → ML READY
""")

    if df is not None:

        st.metric("Rows", df.height)
        st.metric("Columns", df.width)

        st.write("### Column Summary")

        st.table({
            "Column": df.columns,
            "Type": [str(t) for t in df.dtypes]
        })

        st.success("✔ Pipeline Ready")

    else:
        st.warning("⚠️ No dataset loaded")

    st.balloons()