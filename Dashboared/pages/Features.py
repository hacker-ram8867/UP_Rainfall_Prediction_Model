import streamlit as st
from pathlib import Path
from utils.footer import show_footer

st.set_page_config(page_title="Features | TRUERIZE",page_icon="⭐",layout="wide",initial_sidebar_state="expanded")

BASE_DIR=Path(__file__).resolve().parent.parent
LOGO=BASE_DIR/"assets"/"logo.png"

with st.sidebar:
    if LOGO.exists():
        st.image(str(LOGO),use_container_width=True)
    st.title("⭐ Features")
    st.success("Platform Capabilities")
    st.info("Explore all features available in the TRUERIZE Machine Learning Platform.")

left,right=st.columns([3,1])

with left:
    st.title("⭐ TRUERIZE Platform Features")
    st.write("""
TRUERIZE is an end-to-end Machine Learning platform for Rainfall Prediction. It provides Data Engineering, Data Validation, Data Preprocessing, Statistics, Drift Detection, Model Training, Explainable AI and Professional Reporting in one dashboard.
""")

with right:
    if LOGO.exists():
        st.image(str(LOGO),use_container_width=True)

with st.expander("📋 Platform Overview"):
    st.write("""
TRUERIZE combines every stage of the Machine Learning lifecycle into one integrated dashboard. Every module can be executed independently while maintaining a structured workflow.
""")
    st.write("• Data Engineering")
    st.write("• Data Validation")
    st.write("• Data Preprocessing")
    st.write("• Statistics & Drift")
    st.write("• Model Training")
    st.write("• Explainable AI")
    st.write("• Report Generation")

with st.expander("⭐ Core Features"):
    c1,c2,c3=st.columns(3)
    with c1:
        st.subheader("🧹 Data Engineering")
        st.write("• Fast Loading")
        st.write("• Schema Detection")
        st.write("• Data Cleaning")
        st.write("• Feature Engineering")
    with c2:
        st.subheader("📊 Analytics")
        st.write("• Statistics")
        st.write("• Drift Detection")
        st.write("• Correlation Analysis")
        st.write("• Interactive Reports")
    with c3:
        st.subheader("🤖 Machine Learning")
        st.write("• Model Training")
        st.write("• Model Evaluation")
        st.write("• Explainable AI")
        st.write("• Deployment")

with st.expander("📈 Dashboard Statistics"):
    c1,c2,c3,c4=st.columns(4)
    with c1:
        st.metric("Modules","6")
    with c2:
        st.metric("Validation","3")
    with c3:
        st.metric("Reports","10+")
    with c4:
        st.metric("Workflow","Complete")

with st.expander("⚡ Advanced Features"):

    c1,c2,c3=st.columns(3)

    with c1:
        st.subheader("⚡ High Performance")
        st.write("• Polars Processing")
        st.write("• Pandas Integration")
        st.write("• Fast Execution")
        st.write("• Memory Efficient")
        st.write("• Large Dataset Support")

    with c2:
        st.subheader("🔒 Reliable Validation")
        st.write("• Great Expectations")
        st.write("• Cerberus")
        st.write("• Pydantic")
        st.write("• Data Quality Checks")
        st.write("• Validation Reports")

    with c3:
        st.subheader("📊 Interactive Analytics")
        st.write("• Descriptive Statistics")
        st.write("• Correlation Analysis")
        st.write("• Drift Detection")
        st.write("• Feature Analysis")
        st.write("• Interactive Visualizations")

with st.expander("🧠 Explainable Artificial Intelligence"):

    left,right=st.columns(2)

    with left:
        st.subheader("SHAP Analysis")
        st.write("""
SHAP explains the contribution of every feature to the model prediction.
It helps understand global feature importance and improves model transparency.
""")

    with right:
        st.subheader("LIME Analysis")
        st.write("""
LIME explains individual predictions by showing which features influence a specific prediction, making the model easier to interpret.
""")

with st.expander("📄 Reporting System"):

    r1,r2,r3=st.columns(3)

    with r1:
        st.subheader("Validation Reports")
        st.write("• Great Expectations")
        st.write("• Cerberus")
        st.write("• Pydantic")
        st.write("• HTML Reports")

    with r2:
        st.subheader("Statistics Reports")
        st.write("• Summary Statistics")
        st.write("• Drift Detection")
        st.write("• Correlation")
        st.write("• Feature Analysis")

    with r3:
        st.subheader("Machine Learning Reports")
        st.write("• Model Metrics")
        st.write("• SHAP Report")
        st.write("• LIME Report")
        st.write("• Final XAI Report")

with st.expander("✅ Platform Benefits"):

    c1,c2=st.columns(2)

    with c1:
        st.subheader("Dashboard Benefits")
        st.write("• Professional User Interface")
        st.write("• Modular Architecture")
        st.write("• Interactive Navigation")
        st.write("• High Performance")
        st.write("• Scalable Workflow")
        st.write("• Easy Maintenance")

    with c2:
        st.subheader("Machine Learning Benefits")
        st.write("• Reliable Data Validation")
        st.write("• Automated Processing")
        st.write("• Intelligent Analytics")
        st.write("• Explainable AI")
        st.write("• Professional Reports")
        st.write("• Production Ready")

with st.expander("🔄 Complete Machine Learning Workflow"):

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
HTML Reports
""")

    st.success("Every stage of the Machine Learning workflow is connected and can be executed independently.")

with st.expander("🚀 Why Choose TRUERIZE"):

    c1,c2,c3=st.columns(3)

    with c1:
        st.subheader("High Productivity")
        st.write("• Complete ML Workflow")
        st.write("• Single Dashboard")
        st.write("• Fast Execution")
        st.write("• Easy Navigation")

    with c2:
        st.subheader("Reliable Results")
        st.write("• Multiple Validation Engines")
        st.write("• High Data Quality")
        st.write("• Consistent Outputs")
        st.write("• Trusted Predictions")

    with c3:
        st.subheader("Scalable Platform")
        st.write("• Modular Design")
        st.write("• Reusable Components")
        st.write("• Enterprise Ready")
        st.write("• Easy Maintenance")

with st.expander("📊 Platform Summary"):

    m1,m2,m3,m4=st.columns(4)

    with m1:
        st.metric("Modules","6")

    with m2:
        st.metric("Validation Engines","3")

    with m3:
        st.metric("Generated Reports","10+")

    with m4:
        st.metric("Pipeline","Ready")

    st.success("All platform features are available and ready to use.")

with st.expander("💻 Technology Stack"):

    c1,c2,c3,c4=st.columns(4)

    with c1:
        st.subheader("📊 Data Processing")
        st.write("• Python")
        st.write("• Polars")
        st.write("• Pandas")
        st.write("• NumPy")

    with c2:
        st.subheader("🛡 Data Validation")
        st.write("• Great Expectations")
        st.write("• Cerberus")
        st.write("• Pydantic")

    with c3:
        st.subheader("🤖 Machine Learning")
        st.write("• Scikit-Learn")
        st.write("• Random Forest")
        st.write("• Joblib")

    with c4:
        st.subheader("🧠 Explainable AI")
        st.write("• SHAP")
        st.write("• LIME")
        st.write("• Feature Importance")

with st.expander("🛡 Validation Engines"):

    v1,v2,v3=st.columns(3)

    with v1:
        st.subheader("Great Expectations")
        st.write("• Expectation Suites")
        st.write("• Data Validation")
        st.write("• HTML Reports")
        st.write("• Data Documentation")

    with v2:
        st.subheader("Cerberus")
        st.write("• Schema Validation")
        st.write("• Rule Validation")
        st.write("• Error Detection")
        st.write("• Validation Reports")

    with v3:
        st.subheader("Pydantic")
        st.write("• Type Validation")
        st.write("• Data Models")
        st.write("• Field Constraints")
        st.write("• Error Reporting")

with st.expander("📄 Generated Reports"):

    c1,c2,c3=st.columns(3)

    with c1:
        st.subheader("Validation Reports")
        st.write("• Great Expectations Report")
        st.write("• Cerberus Report")
        st.write("• Pydantic Report")
        st.write("• Validation Summary")

    with c2:
        st.subheader("Statistics Reports")
        st.write("• Summary Statistics")
        st.write("• Correlation Analysis")
        st.write("• Drift Detection")
        st.write("• Feature Analysis")

    with c3:
        st.subheader("Model Reports")
        st.write("• Model Metrics")
        st.write("• SHAP Report")
        st.write("• LIME Report")
        st.write("• Final XAI Report")

with st.expander("📈 Platform Performance"):

    m1,m2,m3,m4=st.columns(4)

    with m1:
        st.metric("Modules","6")

    with m2:
        st.metric("Reports","10+")

    with m3:
        st.metric("Validation","100%")

    with m4:
        st.metric("Status","Ready")

    st.success("All dashboard components are functioning correctly.")

with st.expander("🚀 Platform Capabilities"):

    c1,c2,c3=st.columns(3)

    with c1:
        st.subheader("Data Engineering")
        st.write("• Fast Data Loading")
        st.write("• Schema Detection")
        st.write("• Data Cleaning")
        st.write("• Feature Engineering")
        st.write("• Missing Value Handling")
        st.write("• Duplicate Detection")

    with c2:
        st.subheader("Machine Learning")
        st.write("• Random Forest")
        st.write("• Train/Test Split")
        st.write("• Model Evaluation")
        st.write("• Hyperparameter Tuning")
        st.write("• Feature Importance")
        st.write("• Model Export")

    with c3:
        st.subheader("Explainable AI")
        st.write("• SHAP Analysis")
        st.write("• LIME Analysis")
        st.write("• Prediction Explanation")
        st.write("• Feature Importance")
        st.write("• Interactive Reports")
        st.write("• HTML Outputs")

with st.expander("🧭 Quick Navigation"):

    c1,c2,c3=st.columns(3)

    with c1:
        st.subheader("Data Pipeline")
        st.write("🏠 Home")
        st.write("🧹 Polars Configuration")
        st.write("✅ Data Validation")

    with c2:
        st.subheader("Processing")
        st.write("⚙️ Data Preprocessing")
        st.write("📊 Statistics & Drift")
        st.write("🤖 Model Training")

    with c3:
        st.subheader("Final Stage")
        st.write("🧠 Explainable AI")
        st.write("📄 Report Viewer")
        st.write("⭐ Features")

with st.expander("📋 Platform Summary"):

    st.write("""
TRUERIZE is a complete Machine Learning platform that combines
Data Engineering, Validation, Preprocessing, Statistics,
Machine Learning, Explainable AI and Professional Reporting
into one integrated dashboard.
""")

    m1,m2,m3,m4=st.columns(4)

    with m1:
        st.metric("Modules","6")

    with m2:
        st.metric("Validation Engines","3")

    with m3:
        st.metric("Reports","10+")

    with m4:
        st.metric("Pipeline","Ready")

    st.success("The TRUERIZE platform is fully configured and ready to use.")

with st.expander("🙏 Thank You"):

    st.write("""
Thank you for exploring the TRUERIZE Machine Learning Platform.

Use the sidebar to navigate through every module and execute
the complete Machine Learning workflow from data loading
to Explainable AI and report generation.
""")

    st.info("""
Frameworks Used

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