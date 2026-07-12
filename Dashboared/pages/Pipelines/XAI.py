import streamlit as st
from pathlib import Path
import pandas as pd
import numpy as np
import joblib
import shap
import matplotlib.pyplot as plt
from lime.lime_tabular import LimeTabularExplainer

st.set_page_config(
    page_title="🧠 XAI Dashboard",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Explainable AI (SHAP + LIME) Dashboard")
st.success("Module 6 & 7 • XAI System")

BASE_DIR = Path("Desktop/TRUERIZE/final one/up_rainfall_prediction/ram_project_fixed")
OUTPUT_DIR = BASE_DIR / "outputs"
XAI_DIR = OUTPUT_DIR / "xai_report"

SHAP_SUMMARY = XAI_DIR / "shap_summary.png"
LIME_REPORT = XAI_DIR / "lime_explanation.html"

st.divider()

with st.expander("📖 Overview", expanded=True):
    st.write("SHAP explains global model behavior, while LIME explains individual predictions.")

with st.expander("🎯 Objectives"):
    st.markdown("""
- Explain ML predictions  
- Improve transparency  
- Detect feature importance  
- Support decision making  
""")

with st.expander("⚙️ SHAP Workflow (Click to View)"):
    st.code("""
Model → Dataset → SHAP Explainer → SHAP Values → Summary Plot → Feature Importance
""")

with st.expander("⚙️ LIME Workflow (Click to View)"):
    st.code("""
Dataset → Sample Selection → LIME Explainer → Local Prediction → Feature Impact → HTML Report
""")

st.header("📊 SHAP Analysis")

uploaded_model = st.file_uploader("📂 Upload Model (.pkl)", type=["pkl"])
uploaded_data = st.file_uploader("📂 Upload Dataset (.csv)", type=["csv"])

if uploaded_model and uploaded_data:

    model = joblib.load(uploaded_model)
    df = pd.read_csv(uploaded_data)

    st.dataframe(df.head())

    target = st.selectbox("🎯 Target Column", df.columns)

    X = df.drop(columns=[target]).copy()

    if "DATE" in X.columns:
        X.drop(columns=["DATE"], inplace=True)

    X = pd.get_dummies(X)

    sample = X.sample(min(300, len(X)), random_state=42)

    if st.button("🧠 Run SHAP"):

        explainer = shap.Explainer(model, sample)
        shap_values = explainer(sample)

        XAI_DIR.mkdir(parents=True, exist_ok=True)

        plt.figure()
        shap.summary_plot(shap_values, sample, show=False)
        plt.savefig(SHAP_SUMMARY, bbox_inches="tight")
        plt.close()

        st.session_state["shap_values"] = shap_values
        st.session_state["X_sample"] = sample

        st.success("SHAP Generated")

if "shap_values" in st.session_state:

    st.subheader("📈 SHAP Summary Plot")
    st.image(SHAP_SUMMARY)

    importance = np.abs(st.session_state["shap_values"].values).mean(axis=0)

    feature_df = pd.DataFrame({
        "Feature": st.session_state["X_sample"].columns,
        "Importance": importance
    }).sort_values(by="Importance", ascending=False)

    st.subheader("📊 Feature Importance")
    st.dataframe(feature_df.head(20))
    st.bar_chart(feature_df.set_index("Feature").head(20))
    st.divider()
st.header("💡 LIME Analysis")

uploaded_model = st.file_uploader("📂 Upload Model (.pkl) - LIME", type=["pkl"])
uploaded_data = st.file_uploader("📂 Upload Dataset (.csv) - LIME", type=["csv"])

if uploaded_model and uploaded_data:

    model = joblib.load(uploaded_model)
    df = pd.read_csv(uploaded_data)

    target = st.selectbox("🎯 Target Column (LIME)", df.columns)

    X = df.drop(columns=[target]).copy()

    if "DATE" in X.columns:
        X.drop(columns=["DATE"], inplace=True)

    X = pd.get_dummies(X)

    index = st.number_input("Select Row", 0, len(X)-1, 0)

    sample = X.iloc[index]

    explainer = LimeTabularExplainer(
        training_data=np.array(X),
        feature_names=X.columns.tolist(),
        mode="regression"
    )

    if st.button("💡 Run LIME"):

        exp = explainer.explain_instance(
            sample.values,
            model.predict,
            num_features=10
        )

        st.session_state["lime_exp"] = exp
        st.session_state["sample"] = sample

        XAI_DIR.mkdir(parents=True, exist_ok=True)
        exp.save_to_file(str(LIME_REPORT))

        st.success("LIME Generated")

if "lime_exp" in st.session_state:

    st.subheader("🔮 Prediction Output")
    pred = st.session_state["lime_exp"]
    st.write("Explanation Ready")

    exp_df = pd.DataFrame(
        st.session_state["lime_exp"].as_list(),
        columns=["Feature", "Impact"]
    )

    st.subheader("📊 Feature Impact")
    st.dataframe(exp_df)
    st.bar_chart(exp_df.set_index("Feature"))

    st.subheader("📄 LIME HTML Report")
    st.components.v1.html(LIME_REPORT.read_text(), height=600)

st.divider()

st.header("⚖️ SHAP vs LIME")

st.table(pd.DataFrame({
    "Property": ["Scope", "Type", "Output"],
    "SHAP": ["Global + Local", "Game Theory", "Plots"],
    "LIME": ["Local", "Surrogate Model", "HTML"]
}))

st.success("""
✔ SHAP = Global Explanation  
✔ LIME = Local Explanation  
✔ Together = Full XAI System  
""")

st.balloons()

st.divider()

st.header("🎯 Final Conclusion – Explainable AI (SHAP + LIME + XAI)")

with st.expander("📌 Overall Summary", expanded=True):
    st.write("""
Explainable Artificial Intelligence (XAI) plays a very important role in modern Machine Learning systems.

In this project, we used SHAP and LIME to understand how the trained model makes predictions and to improve model transparency and trust.
""")

with st.expander("🧠 SHAP Conclusion"):
    st.write("""
SHAP (SHapley Additive exPlanations) provides a GLOBAL + LOCAL explanation of the model.

✔ It shows how each feature contributes to predictions  
✔ It is based on game theory (Shapley values)  
✔ It helps identify the most important features  
✔ It explains the overall behavior of the machine learning model  
✔ It is very reliable for production-level interpretability  

👉 In simple terms:  
SHAP tells us WHY the model behaves the way it does across the entire dataset.
""")

with st.expander("💡 LIME Conclusion"):
    st.write("""
LIME (Local Interpretable Model-agnostic Explanations) provides LOCAL explanation for a single prediction.

✔ It explains one data instance at a time  
✔ It builds a simple interpretable model around a prediction  
✔ It shows which features influenced a specific output  
✔ It is model-independent (works with any ML model)  
✔ It is very useful for debugging individual predictions  

👉 In simple terms:  
LIME tells us WHY a SINGLE prediction was made for a specific input.
""")

with st.expander("⚖️ SHAP vs LIME Understanding"):
    st.write("""
✔ SHAP = Global understanding of model behavior  
✔ LIME = Local explanation for individual prediction  

Together they provide:

✔ Full model transparency  
✔ Better trust in AI decisions  
✔ Strong debugging capability  
✔ Feature-level understanding  
✔ Production-ready explainability system  
""")

with st.expander("🚀 Final XAI Insight"):
    st.success("""
By combining SHAP and LIME, we achieve a complete Explainable AI system:

✔ SHAP explains the model globally  
✔ LIME explains individual predictions  
✔ Together they make AI transparent, trustworthy, and interpretable  

This helps in real-world deployment where understanding model decisions is as important as accuracy.
""")

st.balloons()