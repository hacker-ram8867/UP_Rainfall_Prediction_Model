UP Data Prediction Project
==========================

Files:
- Todays_task_updated_UP_data_prediction.ipynb: updated notebook code for UP_data_predict.csv.
- truerize/: local helper package used by the notebook for imports, report saving, and browser display.
- reports/raw_GE_report.html and reports/raw_GE_suite.html: Great Expectations-style validation output.
- reports/raw_cerberus.html and reports/raw_cerberus_suite.html: Cerberus validation/schema output.
- reports/raw_pydantic.html and reports/raw_pydantic_suite.html: Pydantic validation/schema output.
- reports/ks_drift_report.html: train/test drift report.
- reports/model_feature_report.html: rainfall feature relationship report.

Place UP_data_predict.csv in the same folder as the notebook, or keep it in:
C:\Users\brama\Downloads\UP_data_predict.csv

The notebook has fallbacks for validation display. For full model, SHAP, and LIME outputs,
run it in a Jupyter environment with scikit-learn, scipy, matplotlib, shap, and lime installed.
