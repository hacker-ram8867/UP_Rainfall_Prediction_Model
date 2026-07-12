# ==========================================================
# TRUERIZE PACKAGE (CLEAN FIXED VERSION)
# ==========================================================

import os
import sys
import json
import warnings
import webbrowser
import importlib
from pathlib import Path

warnings.filterwarnings("ignore")

# ==========================================================
# DATA STACK
# ==========================================================

import pandas as pd
import numpy as np
import polars as pl
import streamlit as st
import streamlit.components.v1 as components

# ==========================================================
# FLASK (SAFE IMPORT)
# ==========================================================

try:
    from flask import Flask, render_template, render_template_string
    from .dashboard import app as _app
    _dashboard_available = True
except Exception:
    Flask = None
    render_template = None
    render_template_string = None
    _app = None
    _dashboard_available = False


# ✅ SAFE DASHBOARD RUNNER (NO NAME CLASH)
def run_dashboard(host="127.0.0.1", port=5000):
    """
    Run Truerize dashboard safely.
    """
    if not _dashboard_available:
        print("❌ Dashboard not available. Check dashboard.py")
        return

    _app.run(host=host, port=port, debug=False, use_reloader=False)


# ==========================================================
# NOTEBOOK DISPLAY
# ==========================================================

from IPython.display import display, HTML, Image

# ==========================================================
# PYDANTIC
# ==========================================================

from pydantic import BaseModel, Field, ValidationError, ConfigDict

# ==========================================================
# CERBERUS
# ==========================================================

from cerberus import Validator

# ==========================================================
# ML (SAFE IMPORTS)
# ==========================================================

try:
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import (
        RandomForestRegressor,
        GradientBoostingRegressor,
        ExtraTreesRegressor
    )
    from sklearn.linear_model import LinearRegression, LogisticRegression
    from sklearn.metrics import (
        mean_absolute_error,
        mean_squared_error,
        r2_score,
        accuracy_score
    )
except Exception:
    train_test_split = None
    RandomForestRegressor = None
    GradientBoostingRegressor = None
    ExtraTreesRegressor = None
    LinearRegression = None
    LogisticRegression = None
    mean_absolute_error = None
    mean_squared_error = None
    r2_score = None
    accuracy_score = None

# ==========================================================
# BOOSTING
# ==========================================================

try:
    from xgboost import XGBRegressor
except Exception:
    XGBRegressor = None

try:
    from lightgbm import LGBMRegressor
except Exception:
    LGBMRegressor = None

# ==========================================================
# STATS
# ==========================================================

try:
    from scipy.stats import ks_2samp
except Exception:
    ks_2samp = None

# ==========================================================
# STORAGE
# ==========================================================

try:
    import joblib
except Exception:
    joblib = None

# ==========================================================
# XAI
# ==========================================================

try:
    import shap
except Exception:
    shap = None

try:
    from lime.lime_tabular import LimeTabularExplainer
except Exception:
    LimeTabularExplainer = None

# ==========================================================
# VISUALIZATION
# ==========================================================

try:
    import matplotlib.pyplot as plt
except Exception:
    plt = None

try:
    import seaborn as sns
except Exception:
    sns = None

try:
    from matplotlib.ticker import PercentFormatter
except Exception:
    PercentFormatter = None


# ==========================================================
# HELPERS
# ==========================================================

def save_and_open_html(path, html, open_browser=True):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")

    if open_browser:
        try:
            webbrowser.open(path.resolve().as_uri())
        except Exception:
            pass

    return path


def missing_libraries():
    libs = {
        "scikit-learn": train_test_split,
        "xgboost": XGBRegressor,
        "lightgbm": LGBMRegressor,
        "scipy": ks_2samp,
        "joblib": joblib,
        "matplotlib": plt,
        "seaborn": sns,
        "shap": shap,
        "lime": LimeTabularExplainer,
    }
    return [name for name, lib in libs.items() if lib is None]


# ==========================================================
# CONFIG
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_PATH = BASE_DIR / "UP_data_predict.csv"

REPORT_DIR = BASE_DIR / "reports"
OUTPUT_DIR = BASE_DIR / "outputs"
MODEL_DIR = OUTPUT_DIR / "models"
XAI_DIR = OUTPUT_DIR / "xai_report"

for folder in (REPORT_DIR, OUTPUT_DIR, MODEL_DIR, XAI_DIR):
    folder.mkdir(parents=True, exist_ok=True)

# ==========================================================
# CONSTANTS
# ==========================================================

SEED = 42
TARGET = "PRECTOTCORR"

EXPECTED_COLUMNS = [
    "YEAR", "MO", "DY",
    "RH2M", "T2MDEW", "QV2M", "PS",
    "WS50M", "PRECTOTCORR",
    "T2MWET", "WD50M",
    "T2M_MAX", "T2M_MIN",
    "ALLSKY_SFC_UV_INDEX",
    "TS", "PSC", "WSC",
    "DISTRICT", "LATITUDE", "LONGITUDE"
]

NUMERIC_COLUMNS = [c for c in EXPECTED_COLUMNS if c != "DISTRICT"]

__version__ = "3.0.0"


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [
    "os", "sys", "json", "warnings", "webbrowser", "importlib", "Path",
    "pd", "np", "pl",
    "Flask", "render_template", "render_template_string",
    "display", "HTML", "Image",
    "BaseModel", "Field", "ValidationError", "ConfigDict",
    "Validator",
    "train_test_split",
    "RandomForestRegressor",
    "GradientBoostingRegressor",
    "ExtraTreesRegressor",
    "LinearRegression",
    "LogisticRegression",
    "mean_absolute_error",
    "mean_squared_error",
    "r2_score",
    "accuracy_score",
    "XGBRegressor",
    "LGBMRegressor",
    "ks_2samp",
    "joblib",
    "shap",
    "LimeTabularExplainer",
    "plt",
    "st"
    "sns",
    "PercentFormatter",
    "save_and_open_html",
    "missing_libraries",
    "BASE_DIR",
    "DATASET_PATH",
    "REPORT_DIR",
    "OUTPUT_DIR",
    "MODEL_DIR",
    "XAI_DIR",
    "SEED",
    "TARGET",
    "EXPECTED_COLUMNS",
    "NUMERIC_COLUMNS",
    "run_dashboard",
    "__version__",
]

print("Loaded:", __file__)
print("Has st:", "st" in globals())

try:
    print("st =", st)
except Exception as e:
    print("ERROR:", e)