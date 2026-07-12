from pathlib import Path

# ==============================
# BASE DIRECTORIES
# ==============================
REPORT_DIR = Path("reports")
MODEL_DIR = Path("models")
XAI_DIR = Path("xai")

# ==============================
# Great Expectations
# ==============================
GE_REPORT = REPORT_DIR / "raw_GE_report.html"
GE_SUITE = REPORT_DIR / "raw_GE_suite.html"

# ==============================
# Cerberus
# ==============================
CERBERUS_RAW = REPORT_DIR / "raw_cerberus.html"
CERBERUS_SUITE = REPORT_DIR / "raw_cerberus_suite.html"
CERBERUS_CLEAN = REPORT_DIR / "clean_cerberus.html"

# ==============================
# Pydantic
# ==============================
PYDANTIC_RAW = REPORT_DIR / "raw_pydantic.html"
PYDANTIC_SUITE = REPORT_DIR / "raw_pydantic_suite.html"
PYDANTIC_CLEAN = REPORT_DIR / "clean_pydantic.html"

# ==============================
# Preprocessing
# ==============================
MODEL_FEATURE_HTML = REPORT_DIR / "model_feature_report.html"
STATISTICS_TXT = REPORT_DIR / "statistics.txt"
DATASET_OUTPUT_HTML = REPORT_DIR / "dataset_output.html"
CLEAN_DATASET_CSV = REPORT_DIR / "clean_dataset.csv"

# ==============================
# Drift Reports
# ==============================
KS_DRIFT_TXT = REPORT_DIR / "ks_drift_report.txt"
KS_DRIFT_HTML = REPORT_DIR / "ks_drift_report.html"

# ==============================
# Model
# ==============================
MODEL_PATH = MODEL_DIR / "up_rainfall_random_forest.pkl"

# ==============================
# XAI Reports
# ==============================
SHAP_SUMMARY = XAI_DIR / "shap_summary.png"
LIME_REPORT = XAI_DIR / "lime_explanation.html"