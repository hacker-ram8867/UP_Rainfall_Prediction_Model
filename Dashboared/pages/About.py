import streamlit as st
from pathlib import Path
from utils.footer import show_footer

st.set_page_config(page_title="About | TRUERIZE",page_icon="ℹ️",layout="wide",initial_sidebar_state="expanded")

BASE_DIR=Path(__file__).resolve().parent.parent
LOGO=BASE_DIR/"assets"/"logo.png"

with st.sidebar:
    if LOGO.exists():
        st.image(str(LOGO),use_container_width=True)
    st.title("ℹ️ About")
    st.success("Professional ML Platform")
    st.info("Learn more about the TRUERIZE platform and its vision.")

left,right=st.columns([3,1])

with left:
    st.title("ℹ️ About TRUERIZE")
    st.write("""
TRUERIZE is an end-to-end Machine Learning platform designed for Data Engineering, Data Validation, Data Preprocessing, Statistics, Drift Detection, Model Training, Explainable AI and Professional Reporting.
""")

with right:
    if LOGO.exists():
        st.image(str(LOGO),use_container_width=True)

with st.expander("🏢 Company Overview"):
    st.write("""
TRUERIZE integrates Data Engineering, Validation, Analytics, Machine Learning, Explainable AI and Professional Reporting into a single dashboard.
""")
    st.write("• Unified Machine Learning Platform")
    st.write("• Modular Architecture")
    st.write("• Interactive Dashboard")
    st.write("• Reliable Validation")
    st.write("• Scalable Design")
    st.write("• Professional Reports")

with st.expander("🎯 Vision • Mission • Goal"):

    c1,c2,c3=st.columns(3)

    with c1:
        st.subheader("🌍 Vision")
        st.write("• Intelligent AI Solutions")
        st.write("• Transparent Models")
        st.write("• Scalable Systems")
        st.write("• Data-Driven Decisions")

    with c2:
        st.subheader("🎯 Mission")
        st.write("• Reliable Machine Learning")
        st.write("• Interactive Analytics")
        st.write("• Explainable AI")
        st.write("• Professional Dashboards")

    with c3:
        st.subheader("🚀 Goal")
        st.write("• One Unified Platform")
        st.write("• Complete ML Workflow")
        st.write("• Automation")
        st.write("• Enterprise Ready")

with st.expander("⭐ Core Values"):

    c1,c2,c3,c4=st.columns(4)

    with c1:
        st.success("Innovation")

    with c2:
        st.success("Quality")

    with c3:
        st.success("Transparency")

    with c4:
        st.success("Continuous Improvement")

with st.expander("🏗 Platform Architecture"):

    left,right=st.columns([2,1])

    with left:

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

    with right:

        st.table({
            "Layer":[
                "Data",
                "Validation",
                "Processing",
                "Analytics",
                "Machine Learning",
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

with st.expander("💻 Technology Stack"):

    c1,c2,c3,c4=st.columns(4)

    with c1:
        st.subheader("Programming")
        st.write("• Python")
        st.write("• Polars")
        st.write("• Pandas")
        st.write("• NumPy")

    with c2:
        st.subheader("Validation")
        st.write("• Great Expectations")
        st.write("• Cerberus")
        st.write("• Pydantic")

    with c3:
        st.subheader("Machine Learning")
        st.write("• Scikit-Learn")
        st.write("• Random Forest")
        st.write("• Joblib")

    with c4:
        st.subheader("Explainable AI")
        st.write("• SHAP")
        st.write("• LIME")
        st.write("• Interactive Reports")

with st.expander("🚀 Platform Capabilities"):

    c1,c2,c3=st.columns(3)

    with c1:
        st.subheader("Data Engineering")
        st.write("• Fast Dataset Loading")
        st.write("• Data Validation")
        st.write("• Data Cleaning")
        st.write("• Feature Engineering")
        st.write("• Quality Assurance")

    with c2:
        st.subheader("Analytics")
        st.write("• Summary Statistics")
        st.write("• Distribution Analysis")
        st.write("• Drift Detection")
        st.write("• Correlation Analysis")
        st.write("• Interactive Reports")

    with c3:
        st.subheader("AI Platform")
        st.write("• Model Training")
        st.write("• Model Evaluation")
        st.write("• Feature Importance")
        st.write("• Explainable AI")
        st.write("• Professional Visualization")

with st.expander("📖 Development Principles"):

    c1,c2=st.columns(2)

    with c1:
        st.subheader("Software Engineering")
        st.write("• Clean Architecture")
        st.write("• Modular Components")
        st.write("• Reusable Code")
        st.write("• Interactive Interface")
        st.write("• Easy Navigation")
        st.write("• Professional UI")

    with c2:
        st.subheader("Machine Learning")
        st.write("• Reliable Validation")
        st.write("• Scalable Design")
        st.write("• Explainable AI")
        st.write("• Professional Reports")
        st.write("• Production Ready")
        st.write("• Enterprise Ready")

with st.expander("🌟 Project Highlights"):

    st.subheader("Key Features")

    st.write("• Modern Dashboard Interface")
    st.write("• Interactive Machine Learning Workflow")
    st.write("• Automated Data Validation")
    st.write("• Professional Data Processing")
    st.write("• Statistical Analysis")
    st.write("• Drift Detection")
    st.write("• Random Forest Training")
    st.write("• SHAP Explainability")
    st.write("• LIME Explainability")
    st.write("• Professional Reports")
    st.write("• Modular Architecture")
    st.write("• Enterprise Ready Design")

with st.expander("🛣 Future Roadmap"):

    c1,c2,c3=st.columns(3)

    with c1:
        st.metric("Cloud Deployment","Planned")
        st.write("• Cloud Integration")
        st.write("• Secure Deployment")
        st.write("• Multi-user Support")

    with c2:
        st.metric("Real-Time Monitoring","Planned")
        st.write("• Live Predictions")
        st.write("• Dashboard Monitoring")
        st.write("• Performance Tracking")

    with c3:
        st.metric("API Integration","Planned")
        st.write("• REST API")
        st.write("• Third-party Integration")
        st.write("• Automation Support")

with st.expander("📊 Platform Summary"):

    c1,c2,c3,c4=st.columns(4)

    with c1:
        st.metric("Modules","6")

    with c2:
        st.metric("Validation Engines","3")

    with c3:
        st.metric("Reports","10+")

    with c4:
        st.metric("Pipeline","Ready")

    st.success("TRUERIZE provides a complete Machine Learning platform from data ingestion to Explainable AI.")

with st.expander("🎉 About TRUERIZE"):

    st.write("""
TRUERIZE is a modern Machine Learning platform developed to simplify the complete analytics workflow.

The platform combines Data Engineering, Validation, Data Preprocessing, Statistics, Drift Detection, Machine Learning, Explainable AI and Professional Reporting into one easy-to-use dashboard.

It is designed with a modular architecture, allowing every component to work independently while remaining connected within a structured pipeline.
""")

    st.success("Thank you for exploring the TRUERIZE platform.")

show_footer()