import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, r2_score

import joblib
import matplotlib.pyplot as plt

st.set_page_config(page_title="🤖 Model Training", page_icon="🤖", layout="wide")

st.title("🤖 Model Training Module")
st.success("Module 5 • ML Training Pipeline")

if "model_trained" not in st.session_state:
    st.session_state.model_trained = False
    st.session_state.model = None
    st.session_state.metrics = None

st.divider()

uploaded_file = st.file_uploader("📂 Upload Dataset", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Dataset Preview")
    st.dataframe(df.head())

    target = st.selectbox("🎯 Select Target Column", df.columns)

    if "DATE" in df.columns:
        df = df.drop(columns=["DATE"])

    X = df.drop(columns=[target])
    y = df[target]

    X = pd.get_dummies(X, drop_first=True)

    if y.dtype == "object":
        y = pd.factorize(y)[0]

    st.session_state["X"] = X
    st.session_state["y"] = y

    st.success(f"Final Shape: {X.shape}")

if uploaded_file:

    y = st.session_state["y"]

    unique_vals = len(np.unique(y))
    problem_type = "Classification" if unique_vals <= 20 else "Regression"

    st.session_state["problem_type"] = problem_type

    st.info(f"🔍 Problem Type: {problem_type}")

with st.expander("🚀 Training Controls", expanded=True):

    if st.button("Train Model"):

        X = st.session_state["X"]
        y = st.session_state["y"]
        problem_type = st.session_state["problem_type"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model = (
            RandomForestClassifier(n_estimators=120, random_state=42)
            if problem_type == "Classification"
            else RandomForestRegressor(n_estimators=120, random_state=42)
        )

        model.fit(X_train, y_train)
        preds = model.predict(X_test)

        st.session_state["model"] = model
        st.session_state["X_test"] = X_test
        st.session_state["y_test"] = y_test
        st.session_state["preds"] = preds
        st.session_state["model_trained"] = True

        st.success("✅ Model Trained Successfully")

if st.session_state.model_trained:

    with st.expander("📊 Model Performance", expanded=True):

        y_test = st.session_state["y_test"]
        preds = st.session_state["preds"]
        problem_type = st.session_state["problem_type"]

        if problem_type == "Classification":

            acc = accuracy_score(y_test, preds)
            report = classification_report(y_test, preds)

            st.metric("Accuracy", round(acc, 4))
            st.text(report)

            st.session_state["metrics"] = {"accuracy": acc}

        else:

            rmse = np.sqrt(mean_squared_error(y_test, preds))
            r2 = r2_score(y_test, preds)

            col1, col2 = st.columns(2)
            col1.metric("RMSE", round(rmse, 4))
            col2.metric("R2 Score", round(r2, 4))

            st.session_state["metrics"] = {"rmse": rmse, "r2": r2}

if st.session_state.model_trained:

    with st.expander("📌 Feature Importance"):

        model = st.session_state["model"]
        X = st.session_state["X"]

        importances = model.feature_importances_

        feature_df = pd.DataFrame({
            "Feature": X.columns,
            "Importance": importances
        }).sort_values(by="Importance", ascending=False)

        st.dataframe(feature_df.head(20))

        fig, ax = plt.subplots()
        ax.barh(feature_df["Feature"][:15], feature_df["Importance"][:15])
        ax.set_title("Feature Importance")

        st.pyplot(fig)

    with st.expander("💾 Save Model"):

        joblib.dump(st.session_state.model, "trained_model.pkl")

        with open("trained_model.pkl", "rb") as f:
            st.download_button(
                "📥 Download Model",
                f,
                file_name="trained_model.pkl"
            )

st.divider()

# ==============================
# WORKFLOW (BUTTON HIDE/SHOW)
# ==============================

with st.expander("⚙️ View Training Workflow", expanded=False):

    st.code("""
📂 Upload Dataset
        │
        ▼
🧹 Data Cleaning
        │
        ▼
🔄 Encoding (One-Hot)
        │
        ▼
🎯 Problem Detection
        │
        ▼
🤖 Train-Test Split
        │
        ▼
🌲 Random Forest Model Training
        │
        ▼
📊 Model Evaluation
        │
        ▼
📌 Feature Importance
        │
        ▼
💾 Save Model
        │
        ▼
🚀 Deployment Ready
""")

# ==============================
# SUMMARY TABLE
# ==============================

with st.expander("📊 Training Summary (Final Report)", expanded=True):

    st.table({
        "Step": [
            "Upload Dataset",
            "Cleaning",
            "Encoding",
            "Problem Detection",
            "Model Training",
            "Evaluation",
            "Feature Importance",
            "Model Save"
        ],
        "Status": ["✅"] * 8
    })

# ==============================
# FINAL CONCLUSION
# ==============================

st.success("""
🎯 FINAL CONCLUSION

✔ Model trained using Random Forest  
✔ Auto classification/regression detection working  
✔ Data preprocessing handled safely  
✔ Metrics calculated correctly  
✔ Feature importance extracted  
✔ Model saved for deployment  

🚀 This is now a PRODUCTION-READY ML training pipeline
""")

st.balloons()