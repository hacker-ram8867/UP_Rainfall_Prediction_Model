import streamlit as st
from pathlib import Path
from utils.footer import show_footer

st.set_page_config(page_title="TRUERIZE Dashboard",page_icon="🌧️",layout="wide",initial_sidebar_state="expanded")

BASE_DIR=Path(__file__).resolve().parent
LOGO=BASE_DIR/"assets"/"logo.png"

with st.sidebar:
    if LOGO.exists():
        st.image(str(LOGO),use_container_width=True)
    st.title("🌧️ TRUERIZE")
    st.caption("Professional Machine Learning Platform")
    st.divider()
    st.subheader("Navigation")
    st.write("🏠 Home")
    st.write("🧹 Polars Configuration")
    st.write("✅ Data Validation")
    st.write("⚙️ Data Preprocessing")
    st.write("📊 Statistics & Drift")
    st.write("🤖 Model Training")
    st.write("🧠 Explainable AI")
    st.write("📄 Report Viewer")
    st.divider()
    st.success("Dashboard Ready")

left,right=st.columns([3,1])

with left:
    st.title("🌧️ TRUERIZE Dashboard")
    st.subheader("Professional End-to-End Machine Learning Platform")
    st.write("""
TRUERIZE is an end-to-end Machine Learning platform developed for Rainfall Prediction. The dashboard integrates Data Loading, Validation, Preprocessing, Statistics, Model Training, Explainable AI and Report Generation into a single workflow.
""")

with right:
    if LOGO.exists():
        st.image(str(LOGO),use_container_width=True)

st.divider()

st.header("Platform Overview")
st.write("""
The dashboard provides a complete Machine Learning workflow from raw dataset to final prediction. Every module can be executed independently while maintaining a structured pipeline.
""")

c1,c2,c3,c4=st.columns(4)

with c1:
    st.metric("Modules","6")
with c2:
    st.metric("Validation","3")
with c3:
    st.metric("Reports","10+")
with c4:
    st.metric("Pipeline","Ready")

st.success("Welcome to the TRUERIZE Dashboard.")
st.divider()

st.header("⭐ Platform Highlights")

c1,c2,c3=st.columns(3)

with c1:
    st.info("⚡ High Performance")
    st.write("- Fast Polars Processing")
    st.write("- Large Dataset Support")
    st.write("- Memory Efficient")
    st.write("- High Speed Execution")

with c2:
    st.success("✅ Reliable Validation")
    st.write("- Great Expectations")
    st.write("- Cerberus")
    st.write("- Pydantic")
    st.write("- Data Quality Reports")

with c3:
    st.warning("🧠 Explainable AI")
    st.write("- SHAP")
    st.write("- LIME")
    st.write("- Feature Importance")
    st.write("- Model Interpretation")

st.divider()

st.header("📊 Dashboard Statistics")

m1,m2,m3,m4=st.columns(4)

with m1:
    st.metric("Dataset Rows","565,210")

with m2:
    st.metric("Features","20")

with m3:
    st.metric("Target","PRECTOTCORR")

with m4:
    st.metric("Library","Scikit-Learn")

st.divider()

st.header("📦 Core Modules")

c1,c2,c3=st.columns(3)

with c1:
    st.subheader("🧹 Data Processing")
    st.write("• Dataset Loading")
    st.write("• Schema Detection")
    st.write("• Data Preview")
    st.write("• Fast Processing")

with c2:
    st.subheader("⚙️ Data Engineering")
    st.write("• Validation")
    st.write("• Cleaning")
    st.write("• Transformation")
    st.write("• Feature Engineering")

with c3:
    st.subheader("🤖 Machine Learning")
    st.write("• Model Training")
    st.write("• Evaluation")
    st.write("• Explainable AI")
    st.write("• Reports")

st.divider()

st.header("🔄 Machine Learning Workflow")

st.code("""
Dataset
   │
   ▼
Polars Configuration
   │
   ▼
Data Validation
   │
   ▼
Data Preprocessing
   │
   ▼
Statistics & Drift
   │
   ▼
Model Training
   │
   ▼
Explainable AI
   │
   ▼
Reports
""")

st.success("Complete Machine Learning workflow is available.")
st.divider()

st.header("🏗 Platform Architecture")

left,right=st.columns([2,1])

with left:
    st.write("""
TRUERIZE follows a modular architecture where every module
can run independently while passing outputs to the next stage
of the Machine Learning pipeline.
""")

    st.write("• Modular Design")
    st.write("• Reusable Components")
    st.write("• Scalable Workflow")
    st.write("• High Performance")
    st.write("• Easy Maintenance")

with right:
    st.table({
        "Layer":[
            "Data",
            "Validation",
            "Processing",
            "Statistics",
            "Training",
            "Explainability",
            "Reports"
        ],
        "Status":[
            "Ready",
            "Ready",
            "Ready",
            "Ready",
            "Ready",
            "Ready",
            "Ready"
        ]
    })

st.divider()

st.header("🎯 Dashboard Objectives")

o1,o2,o3,o4=st.columns(4)

with o1:
    st.success("📂 Data Management")

with o2:
    st.success("🛡 Validation")

with o3:
    st.success("🤖 Model Training")

with o4:
    st.success("🧠 Explainable AI")

st.divider()

st.header("💻 Technology Stack")

c1,c2,c3,c4=st.columns(4)

with c1:
    st.info("📊 Data")
    st.write("• Python")
    st.write("• Polars")
    st.write("• Pandas")
    st.write("• NumPy")

with c2:
    st.info("🛡 Validation")
    st.write("• Great Expectations")
    st.write("• Cerberus")
    st.write("• Pydantic")

with c3:
    st.info("🤖 Machine Learning")
    st.write("• Scikit-Learn")
    st.write("• Random Forest")
    st.write("• Joblib")

with c4:
    st.info("🧠 Explainability")
    st.write("• SHAP")
    st.write("• LIME")
    st.write("• HTML Reports")

st.divider()

st.header("✅ Validation Engines")

v1,v2,v3=st.columns(3)

with v1:
    st.success("Great Expectations")
    st.write("• Data Validation")
    st.write("• Expectation Suite")
    st.write("• HTML Reports")

with v2:
    st.success("Cerberus")
    st.write("• Schema Validation")
    st.write("• Error Detection")
    st.write("• Validation Reports")

with v3:
    st.success("Pydantic")
    st.write("• Type Checking")
    st.write("• Data Models")
    st.write("• Error Reporting")

st.divider()

st.header("📊 System Status")

left,right=st.columns([2,1])

with left:
    st.progress(100)
    st.table({
        "Module":[
            "Polars Configuration",
            "Data Validation",
            "Data Preprocessing",
            "Statistics & Drift",
            "Model Training",
            "Explainable AI",
            "Reports"
        ],
        "Status":[
            "Ready",
            "Ready",
            "Ready",
            "Ready",
            "Ready",
            "Ready",
            "Ready"
        ]
    })

with right:
    st.success("Dashboard Ready")
    st.metric("Modules","6")
    st.metric("Reports","10+")
    st.metric("Pipeline","100%")

st.divider()

st.header("📌 Quick Navigation")

q1,q2,q3=st.columns(3)

with q1:
    st.write("🏠 Home")
    st.write("🧹 Polars Configuration")
    st.write("✅ Data Validation")

with q2:
    st.write("⚙️ Data Preprocessing")
    st.write("📊 Statistics & Drift")
    st.write("🤖 Model Training")

with q3:
    st.write("🧠 Explainable AI")
    st.write("📄 Reports")
    st.write("📈 Dashboard")

st.divider()

st.header("🚀 Platform Capabilities")

c1,c2,c3=st.columns(3)

with c1:
    st.success("Fast Processing")
    st.write("• High-speed loading")
    st.write("• Data Cleaning")
    st.write("• Feature Engineering")
    st.write("• Large Dataset Support")

with c2:
    st.success("Reliable Validation")
    st.write("• Great Expectations")
    st.write("• Cerberus")
    st.write("• Pydantic")
    st.write("• Quality Assurance")

with c3:
    st.success("Explainable AI")
    st.write("• SHAP")
    st.write("• LIME")
    st.write("• Feature Importance")
    st.write("• Interactive Reports")

st.divider()

st.header("🎉 Dashboard Ready")

st.write("""
Welcome to the TRUERIZE Dashboard.

The complete Machine Learning workflow is ready to use.

Use the navigation menu to explore every module of the project.
""")

st.success("TRUERIZE Dashboard initialized successfully.")

st.header("📄 Generated Reports")

c1,c2,c3=st.columns(3)

with c1:
    st.info("Validation Reports")
    st.write("• Great Expectations")
    st.write("• Cerberus")
    st.write("• Pydantic")
    st.write("• Validation Summary")

with c2:
    st.info("Statistics Reports")
    st.write("• Summary Statistics")
    st.write("• Correlation Analysis")
    st.write("• Drift Detection")
    st.write("• Feature Analysis")

with c3:
    st.info("Model Reports")
    st.write("• Model Metrics")
    st.write("• Feature Importance")
    st.write("• SHAP Report")
    st.write("• LIME Report")

st.divider()

st.header("📈 Project Summary")

m1,m2,m3,m4=st.columns(4)

with m1:
    st.metric("Modules","6")

with m2:
    st.metric("Validation Engines","3")

with m3:
    st.metric("Reports","10+")

with m4:
    st.metric("Status","Ready")

st.divider()

st.header("🙏 Thank You")

st.write("""
Thank you for using the TRUERIZE Dashboard.

This dashboard provides a complete Machine Learning workflow for rainfall prediction, including:

• Data Loading
• Data Validation
• Data Preprocessing
• Statistics & Drift Analysis
• Model Training
• Explainable AI
• Professional Report Generation

Use the sidebar to navigate through each module and execute the complete pipeline.
""")

st.success("✅ TRUERIZE Dashboard is ready to use.")

st.info("""
Developed using:

• Streamlit
• Polars
• Pandas
• Scikit-Learn
• Great Expectations
• Cerberus
• Pydantic
• SHAP
• LIME
""")

show_footer()
