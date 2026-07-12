from pathlib import Path
import sys
import os
import warnings
import random
import webbrowser

import streamlit as st

warnings.filterwarnings("ignore")

ROOT = Path(__file__).resolve().parent.parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def optional_import(module_name, alias=None):
    try:
        module = __import__(module_name, fromlist=["*"])
        return module
    except ModuleNotFoundError:
        st.error(
            f"Required package '{module_name}' is not installed.\n"
            f"Please add it to requirements.txt and redeploy."
        )
        st.stop()


# Required Packages
joblib = optional_import("joblib")
np = optional_import("numpy")
pd = optional_import("pandas")
pl = optional_import("polars")
px = optional_import("plotly.express")
plt = optional_import("matplotlib.pyplot")
shap = optional_import("shap")

Validator = optional_import("cerberus").Validator

pydantic = optional_import("pydantic")
BaseModel = pydantic.BaseModel
Field = pydantic.Field

LimeTabularExplainer = optional_import(
    "lime.lime_tabular"
).LimeTabularExplainer

sk_model_selection = optional_import("sklearn.model_selection")
train_test_split = sk_model_selection.train_test_split

sk_preprocessing = optional_import("sklearn.preprocessing")
LabelEncoder = sk_preprocessing.LabelEncoder

sk_ensemble = optional_import("sklearn.ensemble")
RandomForestRegressor = sk_ensemble.RandomForestRegressor

sk_metrics = optional_import("sklearn.metrics")
mean_absolute_error = sk_metrics.mean_absolute_error
mean_squared_error = sk_metrics.mean_squared_error
r2_score = sk_metrics.r2_score

ks_2samp = optional_import("scipy.stats").ks_2samp

import streamlit.components.v1 as components
st.set_page_config(page_title="🌧️ UP Rainfall Prediction System",page_icon="🌧️",layout="wide",initial_sidebar_state="expanded")
BASE_DIR=ROOT
DATA_DIR=BASE_DIR/"data"
UPLOAD_DIR=BASE_DIR/"uploads"
OUTPUT_DIR=BASE_DIR/"outputs"
REPORT_DIR=BASE_DIR/"reports"
MODEL_DIR=BASE_DIR/"models"
ASSET_DIR=BASE_DIR/"assets"
CSS_DIR=ASSET_DIR/"css"
IMAGE_DIR=ASSET_DIR/"images"
XAI_DIR=BASE_DIR/"xai"
TEMP_DIR=BASE_DIR/"temp"
LOG_DIR=BASE_DIR/"logs"
for folder in[DATA_DIR,UPLOAD_DIR,OUTPUT_DIR,REPORT_DIR,MODEL_DIR,ASSET_DIR,CSS_DIR,IMAGE_DIR,XAI_DIR,TEMP_DIR,LOG_DIR]:folder.mkdir(parents=True,exist_ok=True)
DATASET_PATH=DATA_DIR/"UP_data_predict.csv"
TARGET="PRECTOTCORR"
SEED=42
APP_NAME="UP Rainfall Prediction System"
APP_VERSION="1.0.0"
random.seed(SEED)
np.random.seed(SEED)
GE_REPORT=REPORT_DIR/"raw_GE_report.html"
GE_SUITE=REPORT_DIR/"raw_GE_suite.html"
CERBERUS_REPORT=REPORT_DIR/"raw_cerberus_report.html"
CERBERUS_SUITE=REPORT_DIR/"raw_cerberus_suite.html"
PYDANTIC_REPORT=REPORT_DIR/"raw_pydantic_report.html"
PYDANTIC_SUITE=REPORT_DIR/"raw_pydantic_suite.html"
PREPROCESS_REPORT=REPORT_DIR/"preprocessing_report.html"
STATISTICS_REPORT=REPORT_DIR/"statistics_report.html"
DRIFT_REPORT=REPORT_DIR/"drift_detection_report.html"
MODEL_REPORT=REPORT_DIR/"random_forest_report.html"
PREDICTION_REPORT=REPORT_DIR/"prediction_report.html"
SHAP_REPORT=REPORT_DIR/"shap_report.html"
LIME_REPORT=REPORT_DIR/"lime_report.html"
MODEL_FILE=MODEL_DIR/"random_forest.pkl"
FEATURE_FILE=MODEL_DIR/"feature_columns.pkl"
SCALER_FILE=MODEL_DIR/"scaler.pkl"
ENCODER_FILE=MODEL_DIR/"label_encoders.pkl"
STATE={"uploaded":False,"raw_df":None,"configured_df":None,"validated_df":None,"clean_df":None,"train_df":None,"test_df":None,"X_train":None,"X_test":None,"y_train":None,"y_test":None,"model":None,"prediction":None,"prediction_history":[],"statistics":None,"drift":None,"metrics":None,"feature_importance":None,"shap_values":None,"lime_exp":None}
for key,value in STATE.items():
    if key not in st.session_state:st.session_state[key]=value
st.title("🌧️ UP Rainfall Prediction System")
st.caption("End-to-End Machine Learning Pipeline")
EXPECTED_COLUMNS=["YEAR","MO","DY","RH2M","T2MDEW","QV2M","PS","WS50M","PRECTOTCORR","T2MWET","WD50M","T2M_MAX","T2M_MIN","ALLSKY_SFC_UV_INDEX","TS","PSC","WSC","DISTRICT","LATITUDE","LONGITUDE"]
NUMERIC_COLUMNS=["YEAR","MO","DY","RH2M","T2MDEW","QV2M","PS","WS50M","PRECTOTCORR","T2MWET","WD50M","T2M_MAX","T2M_MIN","ALLSKY_SFC_UV_INDEX","TS","PSC","WSC","LATITUDE","LONGITUDE"]
CATEGORICAL_COLUMNS=["DISTRICT"]
FEATURE_COLUMNS=[col for col in EXPECTED_COLUMNS if col!=TARGET]
RANGE_RULES={"MO":(1,12),"DY":(1,31),"RH2M":(0,100),"WD50M":(0,360),"LATITUDE":(20,32),"LONGITUDE":(75,85),"PRECTOTCORR":(0,np.inf)}
PIPELINE=["Dataset Upload","Polars Configuration","Great Expectations","Cerberus","Pydantic","Data Preprocessing","Statistics","Drift Detection","Random Forest","Prediction","SHAP","LIME","Reports Viewer"]
st.sidebar.title("🌧️ Rainfall ML")
uploaded_file=st.sidebar.file_uploader("📂 Upload Dataset",type=["csv"])
if uploaded_file is not None:
    raw_df=pd.read_csv(uploaded_file)
    raw_df.to_csv(UPLOAD_DIR/"uploaded_dataset.csv",index=False)
    st.session_state["raw_df"]=raw_df
    st.session_state["uploaded"]=True
    st.sidebar.success("✅ Dataset Uploaded")
elif DATASET_PATH.exists():
    raw_df=pd.read_csv(DATASET_PATH)
    st.session_state["raw_df"]=raw_df
    st.session_state["uploaded"]=True
    st.sidebar.info("📂 Default Dataset Loaded")
else:
    st.warning("⚠️ Upload Dataset")
    st.stop()
raw_df=st.session_state["raw_df"]

rows,cols=raw_df.shape
memory=round(raw_df.memory_usage(deep=True).sum()/1024**2,2)
missing=int(raw_df.isna().sum().sum())
duplicates=int(raw_df.duplicated().sum())
numeric=len(NUMERIC_COLUMNS)
categorical=len(CATEGORICAL_COLUMNS)
st.success(f"✅ Dataset Loaded Successfully ({rows:,} Rows × {cols} Columns)")
c1,c2,c3,c4,c5,c6=st.columns(6)
c1.metric("Rows",f"{rows:,}")
c2.metric("Columns",cols)
c3.metric("Missing",f"{missing:,}")
c4.metric("Duplicates",f"{duplicates:,}")
c5.metric("Numeric",numeric)
c6.metric("Memory",f"{memory} MB")
tab1,tab2,tab3=st.tabs(["📄 Preview","📊 Columns","📋 Summary"])
with tab1:
    preview_rows=st.slider("Preview Rows",5,100,10)
    st.dataframe(raw_df.head(preview_rows),use_container_width=True,hide_index=True)
with tab2:
    column_info=pd.DataFrame({"Column":raw_df.columns,"Data Type":[str(i) for i in raw_df.dtypes],"Missing":raw_df.isna().sum().values,"Unique":raw_df.nunique().values})
    st.dataframe(column_info,use_container_width=True,hide_index=True)
with tab3:
    summary=pd.DataFrame({"Property":["Rows","Columns","Numeric Columns","Categorical Columns","Missing Cells","Duplicate Rows","Memory (MB)","Target"],"Value":[f"{rows:,}",cols,numeric,categorical,f"{missing:,}",f"{duplicates:,}",memory,TARGET]})
    st.dataframe(summary,use_container_width=True,hide_index=True)
st.session_state["dataset_summary"]=summary
st.session_state["column_info"]=column_info
missing_df=raw_df.isna().sum().reset_index()
missing_df.columns=["Column","Missing"]
missing_df["Percentage"]=(missing_df["Missing"]/len(raw_df)*100).round(2)
dtype_df=pd.DataFrame({"Column":raw_df.columns,"Data Type":[str(i) for i in raw_df.dtypes]})
dtype_count=dtype_df["Data Type"].value_counts().reset_index()
dtype_count.columns=["Data Type","Count"]
col1,col2=st.columns(2)
with col1:
    st.subheader("📊 Missing Values")
    st.dataframe(missing_df,use_container_width=True,height=350,hide_index=True)
with col2:
    st.subheader("📑 Data Types")
    st.dataframe(dtype_count,use_container_width=True,height=350,hide_index=True)
chart_df=missing_df[missing_df["Missing"]>0]
if len(chart_df)>0:
    fig=px.bar(chart_df,x="Column",y="Missing",text="Missing",title="Missing Values")
    fig.update_layout(xaxis_tickangle=-45,height=450)
    st.plotly_chart(fig,use_container_width=True)
else:
    st.success("✅ No Missing Values Found")
csv_data=raw_df.to_csv(index=False).encode()
d1,d2,d3=st.columns(3)
with d1:
    st.download_button("⬇ Download Dataset",csv_data,"UP_data_predict.csv","text/csv",use_container_width=True)
with d2:
    if st.button("💾 Save Dataset",use_container_width=True):
        raw_df.to_csv(OUTPUT_DIR/"dataset_backup.csv",index=False)
        st.success("Dataset Saved Successfully")
with d3:
    st.metric("Dataset Size",f"{round(len(csv_data)/1024/1024,2)} MB")
st.session_state["missing_summary"]=missing_df
st.session_state["dtype_summary"]=dtype_count
st.success("✅ Dataset Analysis Completed Successfully")

def status_badge(status):
    color="#16a34a" if str(status).upper()=="PASS" else "#dc2626"
    return f'<span style="background:{color};color:white;padding:4px 10px;border-radius:20px;font-size:12px;font-weight:bold;">{status}</span>'
def gx_doc_page(title,subtitle,project,columns,overview,column_rules,footer):
    toc="".join([f'<li><a href="#{c}">{c}</a></li>' for c in columns])
    sections=""
    for col in columns:
        rules=column_rules.get(col,[])
        body="".join([f"<li>{r}</li>" for r in rules])
        sections+=f'<section id="{col}" class="card"><h2>{col}</h2><ul>{body}</ul></section>'
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>{title}</title><style>body{{margin:0;font-family:Arial,sans-serif;background:#0f172a;color:#e5e7eb;display:flex}}aside{{width:280px;height:100vh;overflow:auto;background:#111827;padding:20px;position:fixed}}aside h2{{color:#38bdf8}}aside ul{{padding:0;list-style:none}}aside li{{margin:8px 0}}aside a{{color:#e5e7eb;text-decoration:none}}main{{margin-left:300px;padding:30px;width:100%}}.card{{background:#1e293b;padding:20px;border-radius:12px;margin-bottom:20px}}table{{width:100%;border-collapse:collapse}}td{{border:1px solid #334155;padding:10px}}h1{{color:#38bdf8}}h2{{color:#f8fafc}}</style></head><body><aside><h2>{project}</h2><ul>{toc}</ul></aside><main><div class="card"><h1>{title}</h1><h3>{subtitle}</h3>{overview}</div>{sections}<div class="card">{footer}</div></main></body></html>"""
def save_html(path,html):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(html,encoding="utf-8")
    return path
def open_html(path):
    webbrowser.open(path.resolve().as_uri())
st.success("✅ Documentation Engine Loaded Successfully")

st.header("🧹 Polars Configuration")
configured_pl=pl.from_pandas(raw_df)
configured_pl=configured_pl.with_columns([pl.col(col).cast(pl.Float64,strict=False) for col in NUMERIC_COLUMNS if col in configured_pl.columns])
configured_df=configured_pl.to_pandas()
configured_df.columns=[c.strip().upper() for c in configured_df.columns]
configured_df=configured_df[[c for c in EXPECTED_COLUMNS if c in configured_df.columns]]
configured_df.to_csv(OUTPUT_DIR/"polars_configured_dataset.csv",index=False)
st.session_state["configured_df"]=configured_df
before_mem=round(raw_df.memory_usage(deep=True).sum()/1024**2,2)
after_mem=round(configured_df.memory_usage(deep=True).sum()/1024**2,2)
c1,c2,c3,c4,c5=st.columns(5)
c1.metric("Rows",f"{len(configured_df):,}")
c2.metric("Columns",len(configured_df.columns))
c3.metric("Original",f"{before_mem} MB")
c4.metric("Configured",f"{after_mem} MB")
c5.metric("Saved","Yes")
schema_df=pd.DataFrame({"Column":configured_df.columns,"Data Type":[str(i) for i in configured_df.dtypes],"Missing":configured_df.isna().sum().values,"Unique":configured_df.nunique().values})
summary_df=pd.DataFrame({"Property":["Rows","Columns","Numeric Columns","Categorical Columns","Memory Before (MB)","Memory After (MB)","Memory Saved (MB)","Target"],"Value":[len(configured_df),len(configured_df.columns),len(NUMERIC_COLUMNS),len(CATEGORICAL_COLUMNS),before_mem,after_mem,round(before_mem-after_mem,2),TARGET]})
tab1,tab2=st.tabs(["📋 Schema","📊 Summary"])
with tab1:
    st.dataframe(schema_df,use_container_width=True,height=500,hide_index=True)
with tab2:
    st.dataframe(summary_df,use_container_width=True,height=350,hide_index=True)
schema_df.to_csv(OUTPUT_DIR/"polars_schema.csv",index=False)
summary_df.to_csv(OUTPUT_DIR/"polars_summary.csv",index=False)
st.session_state["schema_df"]=schema_df
st.session_state["polars_summary"]=summary_df
st.download_button("⬇ Download Configured Dataset",configured_df.to_csv(index=False).encode(),"polars_configured_dataset.csv","text/csv",use_container_width=True)
overview=f"""<table><tr><td><b>Rows</b></td><td>{len(configured_df):,}</td></tr><tr><td><b>Columns</b></td><td>{len(configured_df.columns)}</td></tr><tr><td><b>Memory Before</b></td><td>{before_mem} MB</td></tr><tr><td><b>Memory After</b></td><td>{after_mem} MB</td></tr><tr><td><b>Memory Saved</b></td><td>{round(before_mem-after_mem,2)} MB</td></tr></table>"""
column_rules={}
for col in configured_df.columns:
    column_rules[col]=[f"Data Type : <b>{configured_df[col].dtype}</b>",f"Missing : <b>{configured_df[col].isna().sum()}</b>",f"Unique : <b>{configured_df[col].nunique()}</b>"]
html=gx_doc_page("Polars Configuration","Configuration Report","UP Rainfall Prediction System",list(configured_df.columns),overview,column_rules,"Dataset configured successfully using Polars.")
report_path=REPORT_DIR/"polars_configuration_report.html"
save_html(report_path,html)
with open(report_path,"r",encoding="utf-8") as f:
    components.html(f.read(),height=700,scrolling=True)
with open(report_path,"rb") as f:
    st.download_button("⬇ Download Polars Report",f,"polars_configuration_report.html","text/html",use_container_width=True)
st.session_state["polars_report"]=report_path
st.success("✅ Polars Configuration Completed Successfully")

st.header("📄 Great Expectations Validation")
configured_df=st.session_state.get("configured_df",pd.DataFrame()).copy()
if configured_df.empty:
    st.error("Configured dataset not found.")
    st.stop()
REPORT_DIR.mkdir(parents=True,exist_ok=True)
OUTPUT_DIR.mkdir(parents=True,exist_ok=True)
def save_html(path,html):
    path.parent.mkdir(parents=True,exist_ok=True)
    with open(path,"w",encoding="utf-8") as f:
        f.write(html)
def validate_ge(df):
    records=[]
    if len(df)==0:
        records.append({"Column":"DATASET","Expectation":"Dataset must not be empty","Observed":0,"Status":"FAIL"})
    else:
        records.append({"Column":"DATASET","Expectation":"Dataset must not be empty","Observed":len(df),"Status":"PASS"})
    unexpected=[c for c in df.columns if c not in EXPECTED_COLUMNS]
    records.append({"Column":"DATASET","Expectation":"No unexpected columns","Observed":len(unexpected),"Status":"PASS" if len(unexpected)==0 else "FAIL"})
    for col in EXPECTED_COLUMNS:
        if col not in df.columns:
            records.append({"Column":col,"Expectation":"Column Exists","Observed":"Missing","Status":"FAIL"})
            continue
        records.append({"Column":col,"Expectation":"Column Exists","Observed":"Present","Status":"PASS"})
        missing=int(df[col].isna().sum())
        records.append({"Column":col,"Expectation":"No Missing Values","Observed":missing,"Status":"PASS" if missing==0 else "FAIL"})
        if col in NUMERIC_COLUMNS:
            numeric=pd.to_numeric(df[col],errors="coerce")
            invalid=int(numeric.isna().sum())
            records.append({"Column":col,"Expectation":"Numeric Values","Observed":invalid,"Status":"PASS" if invalid==0 else "FAIL"})
        if col in RANGE_RULES:
            low,high=RANGE_RULES[col]
            numeric=pd.to_numeric(df[col],errors="coerce")
            outside=int((((numeric<low)|(numeric>high)).fillna(False)).sum())
            records.append({"Column":col,"Expectation":f"Range {low} - {high}","Observed":outside,"Status":"PASS" if outside==0 else "FAIL"})
    return pd.DataFrame(records)
ge_results=validate_ge(configured_df)
st.session_state["ge_results"]=ge_results
passed=(ge_results["Status"]=="PASS").sum()
failed=(ge_results["Status"]=="FAIL").sum()
total_checks=len(ge_results)
success_rate=round((passed/total_checks)*100,2) if total_checks>0 else 0
summary=pd.DataFrame({"Metric":["Rows","Columns","Checks","Passed","Failed","Success Rate"],"Value":[len(configured_df),len(configured_df.columns),total_checks,passed,failed,f"{success_rate}%"]})
st.subheader("📊 Validation Summary")
c1,c2,c3,c4=st.columns(4)
c1.metric("Checks",total_checks)
c2.metric("Passed",passed)
c3.metric("Failed",failed)
c4.metric("Success %",success_rate)
st.subheader("📋 Validation Results")
st.dataframe(ge_results,use_container_width=True,height=600,hide_index=True)
st.subheader("📈 Summary")
st.dataframe(summary,use_container_width=True,hide_index=True)
ge_results.to_csv(OUTPUT_DIR/"ge_validation.csv",index=False)
summary.to_csv(OUTPUT_DIR/"ge_summary.csv",index=False)
with open(OUTPUT_DIR/"ge_validation.csv","rb") as f:
    st.download_button("⬇ Download Validation",f,"ge_validation.csv","text/csv",key="ge_validation_csv")
with open(OUTPUT_DIR/"ge_summary.csv","rb") as f:
    st.download_button("⬇ Download Summary",f,"ge_summary.csv","text/csv",key="ge_summary_csv")
st.session_state["ge_summary"]=summary
st.success("✅ Great Expectations Validation Completed")

def ge_badge(text,color="#6b7280"):
    return f'<span style="display:inline-block;padding:4px 10px;margin:2px;border-radius:6px;background:{color};color:#fff;font-size:13px;font-weight:600;">{text}</span>'
def ge_datadocs(title,suite_name,dataset,overview,expectations,column_docs):
    toc=""
    for col in column_docs:
        anchor=col.replace(" ","_").replace("/","_")
        toc+=f'<li><a href="#{anchor}">{col}</a></li>'
    cols=""
    for col,items in column_docs.items():
        anchor=col.replace(" ","_").replace("/","_")
        rules=""
        for item in items:
            rules+=f"<li>{item}</li>"
        cols+=f'<section id="{anchor}" class="column-card"><h2>{col}</h2><ul>{rules}</ul></section>'
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>{title}</title><style>*{{margin:0;padding:0;box-sizing:border-box}}body{{background:#181c22;color:#ecf0f1;font-family:Segoe UI,Arial,sans-serif}}.wrapper{{display:flex}}.sidebar{{position:fixed;left:0;top:0;width:360px;height:100vh;background:#1d2228;border-right:1px solid #30363d;overflow:auto}}.content{{margin-left:360px;width:calc(100% - 360px)}}.header{{background:#181c22;padding:36px 60px;border-bottom:1px solid #30363d}}.header h1{{font-size:28px;font-weight:700}}.breadcrumb{{font-size:16px;color:#c9d1d9;margin-bottom:18px}}.left-title{{padding:42px 32px 18px;font-size:26px;font-weight:700}}.left-desc{{padding:0 32px 30px;font-size:18px;line-height:1.5;color:#d0d7de}}.card{{margin:24px;background:#24292f;border:1px solid #30363d;border-radius:8px}}.card h3{{padding:18px;font-size:18px;border-bottom:1px solid #30363d}}.card-body{{padding:18px}}.btn{{display:block;text-align:center;background:#ffc107;color:#111;text-decoration:none;padding:14px;border-radius:6px;font-size:16px;font-weight:700}}.toc{{list-style:none;max-height:650px;overflow:auto}}.toc li{{padding:10px 18px;border-bottom:1px solid #30363d}}.toc a{{color:#c9d1d9;text-decoration:none;font-size:17px}}.main{{padding:34px 48px}}.panel{{background:#ffffff;color:#111827;border-radius:8px;padding:18px 28px;font-size:20px;margin-bottom:24px}}.info-title{{font-size:20px;font-weight:700;margin:20px 0}}.info-table{{width:100%;border-collapse:collapse;margin-bottom:24px}}.info-table td{{border:1px solid #3b424c;padding:14px;font-size:17px}}.note{{background:#24292f;padding:16px;margin:20px 0;border-left:5px solid #58a6ff}}.column-card{{background:#24292f;padding:24px;border-radius:8px;margin:26px 0}}.column-card h2{{background:#f3f4f6;color:#111827;padding:18px;border-radius:6px;margin-bottom:18px}}.column-card ul{{padding-left:28px}}.column-card li{{margin:10px 0;font-size:17px}}.expect{{font-size:18px;line-height:1.8}}</style></head><body><div class="wrapper"><div class="sidebar"><div class="left-title">Validation Results</div><div class="left-desc">Validation results for the UP rainfall prediction dataset.</div><div class="card"><h3>Actions</h3><div class="card-body"><a class="btn">How to Edit This Suite</a></div></div><div class="card"><h3>Table of Contents</h3><ul class="toc"><li><a href="#overview">Overview</a></li>{toc}</ul></div></div><div class="content"><div class="header"><div class="breadcrumb">Home / Validation Results / {suite_name}</div><h1>{title}</h1></div><div class="main"><div id="overview" class="panel"><h2>Overview</h2></div><div class="info-title">Info</div><table class="info-table"><tr><td><b>Expectation Suite Name</b></td><td>{suite_name}</td></tr><tr><td><b>Great Expectations Version</b></td><td>1.14.0 Style Documentation</td></tr><tr><td><b>Dataset</b></td><td>{dataset}</td></tr></table><div class="info-title">Table Level Expectations</div><div class="expect">{expectations}</div><div class="note">{overview}</div>{cols}</div></div></div></body></html>"""
expectation_text=f"""<ul><li>Dataset must contain these columns : {''.join([ge_badge(c) for c in EXPECTED_COLUMNS])}</li><li>Dataset must contain at least {ge_badge('1','#16a34a')} row. Current : {ge_badge(f'{len(configured_df):,}')}</li><li>Prediction target : {ge_badge(TARGET,'#2563eb')}</li><li>No unexpected columns are allowed.</li><li>Numeric columns must contain numeric values.</li><li>Required columns must not contain missing values.</li></ul>"""
overview_html=f"""<b>Validation Summary</b><br><br>Total Checks : <b>{total_checks}</b><br>Passed : <b>{passed}</b><br>Failed : <b>{failed}</b><br>Success Rate : <b>{success_rate}%</b><br>Rows : <b>{len(configured_df):,}</b><br>Columns : <b>{len(configured_df.columns)}</b>"""
column_docs={}
for col in EXPECTED_COLUMNS:
    if col in configured_df.columns:
        status="PASS" if ge_results[(ge_results["Column"]==col)&(ge_results["Status"]=="FAIL")].empty else "FAIL"
        docs=[]
        docs.append(f"Validation Status : {ge_badge(status,'#16a34a' if status=='PASS' else '#dc2626')}")
        docs.append(f"Data Type : <b>{configured_df[col].dtype}</b>")
        docs.append(f"Missing Values : <b>{configured_df[col].isna().sum()}</b>")
        docs.append(f"Unique Values : <b>{configured_df[col].nunique()}</b>")
        if col in NUMERIC_COLUMNS:
            docs.append(f"Minimum Value : <b>{configured_df[col].min()}</b>")
            docs.append(f"Maximum Value : <b>{configured_df[col].max()}</b>")
            docs.append("Expectation : Numeric values only.")
        else:
            docs.append("Expectation : String values.")
        docs.append("Expectation : Column must exist.")
        docs.append("Expectation : No missing values.")
        if col in RANGE_RULES:
            docs.append(f"Expectation : Range {RANGE_RULES[col][0]} to {RANGE_RULES[col][1]}.")
        column_docs[col]=docs
GE_REPORT=REPORT_DIR/"raw_GE_report.html"
report_html=ge_datadocs("Validation Results","up_data_prediction_suite_raw","UP_data_predict.csv",overview_html,expectation_text,column_docs)
save_html(GE_REPORT,report_html)
st.subheader("📄 Great Expectations Report")
with open(GE_REPORT,"r",encoding="utf-8") as f:
    report_page=f.read()
components.html(report_page,height=900,scrolling=True)
with open(GE_REPORT,"rb") as f:
    st.download_button("⬇ Download GE Report",f,"raw_GE_report.html","text/html",key="ge_report_html")
suite_docs={}
for col in EXPECTED_COLUMNS:
    rules=[]
    rules.append("Column Must Exist")
    rules.append("No Missing Values")
    if col in NUMERIC_COLUMNS:
        rules.append("Must Be Numeric")
    if col in RANGE_RULES:
        rules.append(f"Range : {RANGE_RULES[col][0]} - {RANGE_RULES[col][1]}")
    if col in CATEGORICAL_COLUMNS:
        rules.append("Must Be String")
    suite_docs[col]=rules
suite_overview=f"<b>Expectation Suite</b><br><br>Dataset : <b>UP_data_predict.csv</b><br>Columns : <b>{len(EXPECTED_COLUMNS)}</b><br>Numeric Columns : <b>{len(NUMERIC_COLUMNS)}</b><br>Categorical Columns : <b>{len(CATEGORICAL_COLUMNS)}</b><br>Target : <b>{TARGET}</b>"
GE_SUITE=REPORT_DIR/"raw_GE_suite.html"
suite_html=ge_datadocs("Expectation Suite","up_data_prediction_suite_raw","UP_data_predict.csv",suite_overview,expectation_text,suite_docs)
save_html(GE_SUITE,suite_html)
st.subheader("📘 Great Expectations Suite")
with open(GE_SUITE,"r",encoding="utf-8") as f:
    suite_page=f.read()
components.html(suite_page,height=900,scrolling=True)
with open(GE_SUITE,"rb") as f:
    st.download_button("⬇ Download GE Suite",f,"raw_GE_suite.html","text/html",key="ge_suite_html")

st.header("🛡️ Cerberus Validation")
validated_df=st.session_state.get("validated_df")
if validated_df is None or validated_df.empty:
    validated_df=st.session_state.get("configured_df")
if validated_df is None or validated_df.empty:
    st.error("Validated dataset not found.")
    st.stop()
validated_df=validated_df.copy()
clean_df=st.session_state.get("clean_df")
if clean_df is None or clean_df.empty:
    clean_df=validated_df.copy()
else:
    clean_df=clean_df.copy()
CERBERUS_SCHEMA={"YEAR":{"type":"integer","required":True},"MO":{"type":"integer","required":True,"min":1,"max":12},"DY":{"type":"integer","required":True,"min":1,"max":31},"DISTRICT":{"type":"string","required":True,"empty":False}}
for col in NUMERIC_COLUMNS:
    if col not in CERBERUS_SCHEMA:
        CERBERUS_SCHEMA[col]={"type":"float","required":True}
validator=Validator(CERBERUS_SCHEMA,allow_unknown=False)
def validate_dataset(df,max_rows=5000):
    records=[]
    passed=0
    failed=0
    data=df.head(max_rows)
    for idx,row in data.iterrows():
        record=row.to_dict()
        for col in NUMERIC_COLUMNS:
            if col in record and pd.notna(record[col]):
                try:
                    record[col]=float(record[col])
                except:
                    pass
        for col in["YEAR","MO","DY"]:
            if col in record and pd.notna(record[col]):
                try:
                    record[col]=int(record[col])
                except:
                    pass
        valid=validator.validate(record)
        if valid:
            passed+=1
            records.append({"Row":idx+1,"Status":"PASS","Reason":"Valid"})
        else:
            failed+=1
            reason="<br>".join([f"{k} : {v}" for k,v in validator.errors.items()])
            records.append({"Row":idx+1,"Status":"FAIL","Reason":reason})
    result=pd.DataFrame(records)
    total=len(result)
    summary={"Total":total,"Passed":passed,"Failed":failed,"Success":round((passed/total)*100,2) if total>0 else 0}
    return result,summary
raw_result,raw_summary=validate_dataset(validated_df)
clean_result,clean_summary=validate_dataset(clean_df)
st.subheader("📄 Raw Cerberus Validation")
st.dataframe(raw_result,use_container_width=True,height=500,hide_index=True)
c1,c2,c3,c4=st.columns(4)
c1.metric("Rows",raw_summary["Total"])
c2.metric("Passed",raw_summary["Passed"])
c3.metric("Failed",raw_summary["Failed"])
c4.metric("Success %",raw_summary["Success"])
st.subheader("🧹 Clean Cerberus Validation")
st.dataframe(clean_result,use_container_width=True,height=500,hide_index=True)
c1,c2,c3,c4=st.columns(4)
c1.metric("Rows",clean_summary["Total"])
c2.metric("Passed",clean_summary["Passed"])
c3.metric("Failed",clean_summary["Failed"])
c4.metric("Success %",clean_summary["Success"])
raw_result.to_csv(OUTPUT_DIR/"raw_cerberus.csv",index=False)
clean_result.to_csv(OUTPUT_DIR/"clean_cerberus.csv",index=False)
st.session_state["raw_cerberus"]=raw_result
st.session_state["clean_cerberus"]=clean_result
st.download_button("⬇ Download Raw Validation",raw_result.to_csv(index=False).encode(),"raw_cerberus.csv","text/csv",key="raw_cerberus_csv")
st.download_button("⬇ Download Clean Validation",clean_result.to_csv(index=False).encode(),"clean_cerberus.csv","text/csv",key="clean_cerberus_csv")
st.success("✅ Cerberus Validation Completed")

def cerberus_template(title,summary,table):
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>{title}</title><style>body{{margin:0;background:#f3f4f6;font-family:Segoe UI,Arial,sans-serif}}.container{{padding:32px}}.header{{background:#24384f;color:#fff;padding:36px;border-radius:18px;margin-bottom:24px}}.header h1{{margin:0;font-size:34px;font-weight:700}}.header p{{margin-top:24px;font-size:20px}}table{{width:100%;border-collapse:collapse;background:#fff}}th{{background:#2d435b;color:#fff;padding:16px;font-size:18px;text-align:left}}td{{padding:14px;border-bottom:1px solid #e5e7eb;font-size:18px;vertical-align:top}}tr:hover{{background:#f8fafc}}.pass{{color:#16a34a;font-weight:700}}.fail{{color:#dc2626;font-weight:700}}</style></head><body><div class="container"><div class="header"><h1>{title}</h1><p>Total : {summary['Total']:,} | Passed : {summary['Passed']:,} | Failed : {summary['Failed']:,} | Success % : {summary['Success']}</p></div>{table}</div></body></html>"""
def cerberus_table(df):
    rows=""
    for _,r in df.iterrows():
        cls="pass" if r["Status"]=="PASS" else "fail"
        rows+=f"<tr><td>{r['Row']}</td><td class='{cls}'>{r['Status']}</td><td>{r['Reason']}</td></tr>"
    return f"<table><thead><tr><th>Row</th><th>Status</th><th>Reason</th></tr></thead><tbody>{rows}</tbody></table>"
def cerberus_schema_template(df):
    rows=""
    for col in df.columns:
        rule=CERBERUS_SCHEMA.get(col,{})
        rows+=f"<tr><td>{col}</td><td>{df[col].dtype}</td><td>{rule}</td></tr>"
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>Cerberus Schema</title><style>body{{margin:0;background:#f3f4f6;font-family:Segoe UI,Arial,sans-serif}}.container{{padding:32px}}.header{{background:#24384f;color:#fff;padding:36px;border-radius:18px;margin-bottom:24px}}.header h1{{margin:0;font-size:34px}}.header p{{margin-top:24px;font-size:20px}}table{{width:100%;border-collapse:collapse;background:#fff}}th{{background:#2d435b;color:#fff;padding:16px;text-align:left;font-size:18px}}td{{padding:14px;border-bottom:1px solid #e5e7eb;font-size:18px;vertical-align:top}}</style></head><body><div class="container"><div class="header"><h1>Cerberus Schema</h1><p>Columns : {len(df.columns)}</p></div><table><thead><tr><th>Column</th><th>Data Type</th><th>Validation Rule</th></tr></thead><tbody>{rows}</tbody></table></div></body></html>"""
raw_html=cerberus_template("Cerberus Validation (Raw)",raw_summary,cerberus_table(raw_result))
clean_html=cerberus_template("Cerberus Validation (Clean)",clean_summary,cerberus_table(clean_result))
schema_html=cerberus_schema_template(clean_df)

RAW_CERBERUS_REPORT=REPORT_DIR/"raw_cerberus.html"
CLEAN_CERBERUS_REPORT=REPORT_DIR/"clean_cerberus.html"
CERBERUS_SUITE=REPORT_DIR/"raw_cerberus_suite.html"
save_html(RAW_CERBERUS_REPORT,raw_html)
save_html(CLEAN_CERBERUS_REPORT,clean_html)
save_html(CERBERUS_SUITE,schema_html)
st.subheader("📄 Raw Cerberus Report")
with open(RAW_CERBERUS_REPORT,"r",encoding="utf-8") as f:
    raw_page=f.read()
components.html(raw_page,height=700,scrolling=True)
with open(RAW_CERBERUS_REPORT,"rb") as f:
    st.download_button("⬇ Download Raw Cerberus Report",f,"raw_cerberus.html","text/html",key="raw_cerberus_report_html")
st.subheader("📄 Clean Cerberus Report")
with open(CLEAN_CERBERUS_REPORT,"r",encoding="utf-8") as f:
    clean_page=f.read()
components.html(clean_page,height=700,scrolling=True)
with open(CLEAN_CERBERUS_REPORT,"rb") as f:
    st.download_button("⬇ Download Clean Cerberus Report",f,"clean_cerberus.html","text/html",key="clean_cerberus_report_html")
st.subheader("📘 Cerberus Schema")
with open(CERBERUS_SUITE,"r",encoding="utf-8") as f:
    schema_page=f.read()
components.html(schema_page,height=700,scrolling=True)
with open(CERBERUS_SUITE,"rb") as f:
    st.download_button("⬇ Download Cerberus Schema",f,"raw_cerberus_suite.html","text/html",key="cerberus_schema_html")
summary=pd.DataFrame({"Metric":["Total Rows","Passed","Failed","Success Rate"],"Value":[raw_summary["Total"],raw_summary["Passed"],raw_summary["Failed"],f"{raw_summary['Success']} %"]})
st.subheader("📊 Cerberus Summary")
st.dataframe(summary,use_container_width=True,hide_index=True)
summary.to_csv(OUTPUT_DIR/"cerberus_summary.csv",index=False)
with open(OUTPUT_DIR/"cerberus_summary.csv","rb") as f:
    st.download_button("⬇ Download Cerberus Summary",f,"cerberus_summary.csv","text/csv",key="cerberus_summary_csv")
st.session_state["raw_cerberus_report"]=RAW_CERBERUS_REPORT
st.session_state["clean_cerberus_report"]=CLEAN_CERBERUS_REPORT
st.session_state["cerberus_schema"]=CERBERUS_SUITE
st.session_state["raw_cerberus"]=raw_result
st.session_state["clean_cerberus"]=clean_result
st.session_state["cerberus_summary"]=summary
st.success("✅ Cerberus Validation Completed")
st.success("✅ Raw Cerberus Report Generated")
st.success("✅ Clean Cerberus Report Generated")
st.success("✅ Cerberus Schema Generated")
st.balloons()


st.header("🧩 Pydantic Validation")
validated_df=st.session_state.get("validated_df")
if validated_df is None or validated_df.empty:
    validated_df=st.session_state.get("configured_df")
if validated_df is None or validated_df.empty:
    st.error("Validated dataset not found.")
    st.stop()
validated_df=validated_df.copy()
clean_df=st.session_state.get("clean_df")
if clean_df is None or clean_df.empty:
    clean_df=validated_df.copy()
else:
    clean_df=clean_df.copy()
class RainfallRecord(BaseModel):
    YEAR:int
    MO:int=Field(ge=1,le=12)
    DY:int=Field(ge=1,le=31)
    RH2M:float
    T2MDEW:float
    QV2M:float
    PS:float
    WS50M:float
    PRECTOTCORR:float
    T2MWET:float
    WD50M:float
    T2M_MAX:float
    T2M_MIN:float
    ALLSKY_SFC_UV_INDEX:float
    TS:float
    PSC:float
    WSC:float
    DISTRICT:str
def validate_pydantic(df,max_rows=5000):
    records=[]
    passed=0
    failed=0
    data=df.head(max_rows)
    for idx,row in data.iterrows():
        try:
            RainfallRecord(**row.to_dict())
            passed+=1
            records.append({"Row":idx+1,"Status":"PASS","Reason":"Valid"})
        except Exception as e:
            failed+=1
            records.append({"Row":idx+1,"Status":"FAIL","Reason":str(e)})
    result=pd.DataFrame(records)
    total=len(result)
    summary={"Total":total,"Passed":passed,"Failed":failed,"Success":round((passed/total)*100,2) if total>0 else 0}
    return result,summary
raw_result,raw_summary=validate_pydantic(validated_df)
clean_result,clean_summary=validate_pydantic(clean_df)
st.subheader("📄 Raw Pydantic Validation")
st.dataframe(raw_result,use_container_width=True,height=500,hide_index=True)
c1,c2,c3,c4=st.columns(4)
c1.metric("Rows",raw_summary["Total"])
c2.metric("Passed",raw_summary["Passed"])
c3.metric("Failed",raw_summary["Failed"])
c4.metric("Success %",raw_summary["Success"])
st.subheader("🧹 Clean Pydantic Validation")
st.dataframe(clean_result,use_container_width=True,height=500,hide_index=True)
c1,c2,c3,c4=st.columns(4)
c1.metric("Rows",clean_summary["Total"])
c2.metric("Passed",clean_summary["Passed"])
c3.metric("Failed",clean_summary["Failed"])
c4.metric("Success %",clean_summary["Success"])
raw_result.to_csv(OUTPUT_DIR/"raw_pydantic.csv",index=False)
clean_result.to_csv(OUTPUT_DIR/"clean_pydantic.csv",index=False)
st.session_state["raw_pydantic"]=raw_result
st.session_state["clean_pydantic"]=clean_result
st.download_button("⬇ Download Raw Validation",raw_result.to_csv(index=False).encode(),"raw_pydantic.csv","text/csv",key="raw_pydantic_csv")
st.download_button("⬇ Download Clean Validation",clean_result.to_csv(index=False).encode(),"clean_pydantic.csv","text/csv",key="clean_pydantic_csv")
st.success("✅ Pydantic Validation Completed")

def pydantic_template(title,summary,table):
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>{title}</title><style>body{{margin:0;background:#f3f4f6;font-family:Segoe UI,Arial,sans-serif}}.container{{padding:32px}}.header{{background:#24384f;color:#fff;padding:36px;border-radius:18px;margin-bottom:24px}}.header h1{{margin:0;font-size:34px;font-weight:700}}.header p{{margin-top:24px;font-size:20px}}table{{width:100%;border-collapse:collapse;background:#fff}}th{{background:#2d435b;color:#fff;padding:16px;font-size:18px;text-align:left}}td{{padding:14px;border-bottom:1px solid #e5e7eb;font-size:18px;vertical-align:top}}tr:hover{{background:#f8fafc}}.pass{{color:#16a34a;font-weight:700}}.fail{{color:#dc2626;font-weight:700}}</style></head><body><div class="container"><div class="header"><h1>{title}</h1><p>Total : {summary['Total']:,} | Passed : {summary['Passed']:,} | Failed : {summary['Failed']:,} | Success % : {summary['Success']}</p></div>{table}</div></body></html>"""
def pydantic_table(df):
    rows=""
    for _,r in df.iterrows():
        cls="pass" if r["Status"]=="PASS" else "fail"
        rows+=f"<tr><td>{r['Row']}</td><td class='{cls}'>{r['Status']}</td><td>{r['Reason']}</td></tr>"
    return f"<table><thead><tr><th>Row</th><th>Status</th><th>Reason</th></tr></thead><tbody>{rows}</tbody></table>"
def pydantic_schema_template(df):
    rows=""
    for col in df.columns:
        dtype=str(df[col].dtype)
        if col in NUMERIC_COLUMNS:
            rule="float"
        elif col in CATEGORICAL_COLUMNS:
            rule="string"
        else:
            rule="required"
        rows+=f"<tr><td>{col}</td><td>{dtype}</td><td>{rule}</td></tr>"
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>Pydantic Schema</title><style>body{{margin:0;background:#f3f4f6;font-family:Segoe UI,Arial,sans-serif}}.container{{padding:32px}}.header{{background:#24384f;color:#fff;padding:36px;border-radius:18px;margin-bottom:24px}}.header h1{{margin:0;font-size:34px}}.header p{{margin-top:24px;font-size:20px}}table{{width:100%;border-collapse:collapse;background:#fff}}th{{background:#2d435b;color:#fff;padding:16px;text-align:left;font-size:18px}}td{{padding:14px;border-bottom:1px solid #e5e7eb;font-size:18px}}</style></head><body><div class="container"><div class="header"><h1>Pydantic Schema</h1><p>Columns : {len(df.columns)}</p></div><table><thead><tr><th>Column</th><th>Data Type</th><th>Validation Rule</th></tr></thead><tbody>{rows}</tbody></table></div></body></html>"""
raw_html=pydantic_template("Pydantic Validation (Raw)",raw_summary,pydantic_table(raw_result))
clean_html=pydantic_template("Pydantic Validation (Clean)",clean_summary,pydantic_table(clean_result))
schema_html=pydantic_schema_template(clean_df)

RAW_PYDANTIC_REPORT=REPORT_DIR/"raw_pydantic.html"
CLEAN_PYDANTIC_REPORT=REPORT_DIR/"clean_pydantic.html"
PYDANTIC_SUITE=REPORT_DIR/"raw_pydantic_suite.html"
save_html(RAW_PYDANTIC_REPORT,raw_html)
save_html(CLEAN_PYDANTIC_REPORT,clean_html)
save_html(PYDANTIC_SUITE,schema_html)
st.subheader("📄 Raw Pydantic Report")
with open(RAW_PYDANTIC_REPORT,"r",encoding="utf-8") as f:
    raw_page=f.read()
components.html(raw_page,height=700,scrolling=True)
with open(RAW_PYDANTIC_REPORT,"rb") as f:
    st.download_button("⬇ Download Raw Pydantic Report",f,"raw_pydantic.html","text/html",key="raw_pydantic_report_html")
st.subheader("📄 Clean Pydantic Report")
with open(CLEAN_PYDANTIC_REPORT,"r",encoding="utf-8") as f:
    clean_page=f.read()
components.html(clean_page,height=700,scrolling=True)
with open(CLEAN_PYDANTIC_REPORT,"rb") as f:
    st.download_button("⬇ Download Clean Pydantic Report",f,"clean_pydantic.html","text/html",key="clean_pydantic_report_html")
st.subheader("📘 Pydantic Schema")
with open(PYDANTIC_SUITE,"r",encoding="utf-8") as f:
    schema_page=f.read()
components.html(schema_page,height=700,scrolling=True)
with open(PYDANTIC_SUITE,"rb") as f:
    st.download_button("⬇ Download Pydantic Schema",f,"raw_pydantic_suite.html","text/html",key="pydantic_schema_html")

summary=pd.DataFrame({"Metric":["Total Rows","Passed","Failed","Success Rate"],"Value":[raw_summary["Total"],raw_summary["Passed"],raw_summary["Failed"],f"{raw_summary['Success']} %"]})
st.subheader("📊 Pydantic Summary")
st.dataframe(summary,use_container_width=True,hide_index=True)
summary.to_csv(OUTPUT_DIR/"pydantic_summary.csv",index=False)
with open(OUTPUT_DIR/"pydantic_summary.csv","rb") as f:
    st.download_button("⬇ Download Pydantic Summary",f,"pydantic_summary.csv","text/csv",key="pydantic_summary_csv")
st.session_state["raw_pydantic_report"]=RAW_PYDANTIC_REPORT
st.session_state["clean_pydantic_report"]=CLEAN_PYDANTIC_REPORT
st.session_state["pydantic_schema"]=PYDANTIC_SUITE
st.session_state["raw_pydantic"]=raw_result
st.session_state["clean_pydantic"]=clean_result
st.session_state["pydantic_summary"]=summary
st.success("✅ Pydantic Validation Completed")
st.success("✅ Raw Pydantic Report Generated")
st.success("✅ Clean Pydantic Report Generated")
st.success("✅ Pydantic Schema Generated")
st.balloons()

st.header("⚙️ Data Preprocessing")
validated_df=st.session_state.get("validated_df")
if validated_df is None or validated_df.empty:
    validated_df=st.session_state.get("configured_df")
if validated_df is None or validated_df.empty:
    st.error("Validated dataset not found.")
    st.stop()
validated_df=validated_df.copy()
clean_df=validated_df.copy()
clean_df.columns=[str(col).strip().upper() for col in clean_df.columns]
clean_df=clean_df.drop_duplicates().reset_index(drop=True)
for col in NUMERIC_COLUMNS:
    if col in clean_df.columns:
        clean_df[col]=pd.to_numeric(clean_df[col],errors="coerce")
        clean_df[col]=clean_df[col].fillna(clean_df[col].median())
label_encoders={}
for col in CATEGORICAL_COLUMNS:
    if col in clean_df.columns:
        clean_df[col]=clean_df[col].fillna("UNKNOWN").astype(str)
        encoder=LabelEncoder()
        clean_df[col]=encoder.fit_transform(clean_df[col])
        label_encoders[col]=encoder
joblib.dump(label_encoders,ENCODER_FILE)
clean_df=clean_df[EXPECTED_COLUMNS]
clean_df.to_csv(OUTPUT_DIR/"clean_dataset.csv",index=False)
st.session_state["clean_df"]=clean_df
st.session_state["label_encoders"]=label_encoders
before_rows=len(validated_df)
after_rows=len(clean_df)
removed=before_rows-after_rows
missing_before=int(validated_df.isna().sum().sum())
missing_after=int(clean_df.isna().sum().sum())
c1,c2,c3,c4=st.columns(4)
c1.metric("Original Rows",f"{before_rows:,}")
c2.metric("Clean Rows",f"{after_rows:,}")
c3.metric("Duplicates Removed",removed)
c4.metric("Missing Values",missing_after)
st.dataframe(clean_df.head(100),use_container_width=True,height=600,hide_index=True)
summary_df=pd.DataFrame({"Metric":["Original Rows","Clean Rows","Duplicates Removed","Missing Before","Missing After","Numeric Columns","Categorical Columns"],"Value":[before_rows,after_rows,removed,missing_before,missing_after,len(NUMERIC_COLUMNS),len(CATEGORICAL_COLUMNS)]})
st.subheader("📊 Preprocessing Summary")
st.dataframe(summary_df,use_container_width=True,hide_index=True)
summary_df.to_csv(OUTPUT_DIR/"preprocessing_summary.csv",index=False)
st.session_state["preprocessing_summary"]=summary_df
st.download_button("⬇ Download Clean Dataset",clean_df.to_csv(index=False).encode(),"clean_dataset.csv","text/csv",key="clean_dataset_csv")
with open(OUTPUT_DIR/"preprocessing_summary.csv","rb") as f:
    st.download_button("⬇ Download Summary",f,"preprocessing_summary.csv","text/csv",key="preprocessing_summary_csv")
st.success("✅ Data Preprocessing Completed Successfully")

overview=f"""<table><tr><td><b>Original Rows</b></td><td>{before_rows:,}</td></tr><tr><td><b>Clean Rows</b></td><td>{after_rows:,}</td></tr><tr><td><b>Duplicates Removed</b></td><td>{removed:,}</td></tr><tr><td><b>Missing Before</b></td><td>{missing_before:,}</td></tr><tr><td><b>Missing After</b></td><td>{missing_after:,}</td></tr><tr><td><b>Numeric Columns</b></td><td>{len(NUMERIC_COLUMNS)}</td></tr><tr><td><b>Categorical Columns</b></td><td>{len(CATEGORICAL_COLUMNS)}</td></tr></table>"""
column_rules={}
for col in clean_df.columns:
    rules=[]
    rules.append(f"Data Type : <b>{clean_df[col].dtype}</b>")
    rules.append(f"Missing Values : <b>{clean_df[col].isna().sum()}</b>")
    rules.append(f"Unique Values : <b>{clean_df[col].nunique()}</b>")
    if col in NUMERIC_COLUMNS:
        rules.append(f"Mean : <b>{round(clean_df[col].mean(),4)}</b>")
        rules.append(f"Median : <b>{round(clean_df[col].median(),4)}</b>")
        rules.append(f"Minimum : <b>{round(clean_df[col].min(),4)}</b>")
        rules.append(f"Maximum : <b>{round(clean_df[col].max(),4)}</b>")
    else:
        rules.append("Encoded as categorical feature.")
    column_rules[col]=rules
html=gx_doc_page("Preprocessing Report","Data Preprocessing Documentation","UP Rainfall Prediction System",list(clean_df.columns),overview,column_rules,f"Dataset preprocessing completed successfully. Final dataset contains <b>{after_rows:,}</b> cleaned records.")
save_html(PREPROCESS_REPORT,html)
st.subheader("📄 Preprocessing Report")
with open(PREPROCESS_REPORT,"r",encoding="utf-8") as f:
    report_html=f.read()
components.html(report_html,height=700,scrolling=True)
with open(PREPROCESS_REPORT,"rb") as f:
    st.download_button("⬇ Download Preprocessing Report",f,"preprocessing_report.html","text/html",key="preprocessing_report_html")
st.session_state["preprocessing_report"]=PREPROCESS_REPORT
st.success("✅ Preprocessing Report Generated Successfully")

st.header("📊 Statistics")
stats_df=clean_df.describe(include="all").transpose().reset_index().rename(columns={"index":"Column"})
stats_df.to_csv(OUTPUT_DIR/"dataset_statistics.csv",index=False)
st.dataframe(stats_df,use_container_width=True,height=600,hide_index=True)
st.session_state["statistics"]=stats_df
rows,cols=clean_df.shape
missing=int(clean_df.isna().sum().sum())
duplicates=int(clean_df.duplicated().sum())
memory=round(clean_df.memory_usage(deep=True).sum()/1024**2,2)
c1,c2,c3,c4=st.columns(4)
c1.metric("Rows",f"{rows:,}")
c2.metric("Columns",cols)
c3.metric("Missing Values",missing)
c4.metric("Memory Usage",f"{memory} MB")
with open(OUTPUT_DIR/"dataset_statistics.csv","rb") as f:
    st.download_button("⬇ Download Statistics",f,"dataset_statistics.csv","text/csv",key="dataset_statistics_csv")
st.success("✅ Dataset Statistics Generated Successfully")
overview=f"""<table><tr><td><b>Rows</b></td><td>{rows:,}</td></tr><tr><td><b>Columns</b></td><td>{cols}</td></tr><tr><td><b>Missing Values</b></td><td>{missing:,}</td></tr><tr><td><b>Duplicate Rows</b></td><td>{duplicates:,}</td></tr><tr><td><b>Memory Usage</b></td><td>{memory} MB</td></tr></table>"""
column_rules={}
for col in clean_df.columns:
    rules=[]
    rules.append(f"Data Type : <b>{clean_df[col].dtype}</b>")
    rules.append(f"Count : <b>{clean_df[col].count()}</b>")
    rules.append(f"Unique Values : <b>{clean_df[col].nunique()}</b>")
    if col in NUMERIC_COLUMNS:
        rules.append(f"Mean : <b>{round(clean_df[col].mean(),4)}</b>")
        rules.append(f"Std : <b>{round(clean_df[col].std(),4)}</b>")
        rules.append(f"Minimum : <b>{round(clean_df[col].min(),4)}</b>")
        rules.append(f"Median : <b>{round(clean_df[col].median(),4)}</b>")
        rules.append(f"Maximum : <b>{round(clean_df[col].max(),4)}</b>")
    column_rules[col]=rules

html=gx_doc_page("Statistics Report","Dataset Statistics Documentation","UP Rainfall Prediction System",list(clean_df.columns),overview,column_rules,f"Statistical analysis completed successfully for <b>{len(clean_df.columns)}</b> columns.")
save_html(STATISTICS_REPORT,html)
st.subheader("📄 Statistics Report")
with open(STATISTICS_REPORT,"r",encoding="utf-8") as f:
    report_html=f.read()
components.html(report_html,height=700,scrolling=True)
with open(STATISTICS_REPORT,"rb") as f:
    st.download_button("⬇ Download Statistics Report",f,"statistics_report.html","text/html",key="statistics_report_html")
summary=pd.DataFrame({"Metric":["Rows","Columns","Missing Values","Duplicate Rows","Memory Usage"],"Value":[rows,cols,missing,duplicates,f"{memory} MB"]})
st.subheader("📊 Statistics Summary")
st.dataframe(summary,use_container_width=True,hide_index=True)
summary.to_csv(OUTPUT_DIR/"statistics_summary.csv",index=False)
with open(OUTPUT_DIR/"statistics_summary.csv","rb") as f:
    st.download_button("⬇ Download Statistics Summary",f,"statistics_summary.csv","text/csv",key="statistics_summary_csv")
st.session_state["statistics"]=stats_df
st.session_state["statistics_summary"]=summary
st.session_state["statistics_report"]=STATISTICS_REPORT
st.success("✅ Dataset Statistics Generated Successfully")
st.success("✅ Statistics Report Generated Successfully")
st.balloons()

st.header("📈 Data Drift Detection")
reference_df=configured_df.copy()
current_df=clean_df.copy()
drift_results=[]
drift_passed=0
drift_failed=0
for col in NUMERIC_COLUMNS:
    if col in reference_df.columns and col in current_df.columns:
        ref=pd.to_numeric(reference_df[col],errors="coerce").dropna()
        cur=pd.to_numeric(current_df[col],errors="coerce").dropna()
        if len(ref)>0 and len(cur)>0:
            statistic,pvalue=ks_2samp(ref,cur)
            status="PASS" if pvalue>=0.05 else "FAIL"
            if status=="PASS":
                drift_passed+=1
            else:
                drift_failed+=1
            drift_results.append({"Column":col,"KS Statistic":round(statistic,4),"P Value":round(pvalue,6),"Status":status})
drift_df=pd.DataFrame(drift_results)
drift_summary={"Columns":len(drift_df),"Passed":drift_passed,"Failed":drift_failed,"Success":round((drift_passed/len(drift_df))*100,2) if len(drift_df)>0 else 0}
st.subheader("📄 Drift Detection Results")
st.dataframe(drift_df,use_container_width=True,hide_index=True)
summary=pd.DataFrame({"Metric":["Columns Tested","Passed","Failed","Success Rate"],"Value":[drift_summary["Columns"],drift_summary["Passed"],drift_summary["Failed"],f"{drift_summary['Success']} %"]})
st.subheader("📊 Drift Summary")
st.dataframe(summary,use_container_width=True,hide_index=True)
drift_df.to_csv(OUTPUT_DIR/"drift_detection.csv",index=False)
summary.to_csv(OUTPUT_DIR/"drift_summary.csv",index=False)
with open(OUTPUT_DIR/"drift_detection.csv","rb") as f:
    st.download_button("⬇ Download Drift Results",f,"drift_detection.csv","text/csv",key="drift_results_csv")
with open(OUTPUT_DIR/"drift_summary.csv","rb") as f:
    st.download_button("⬇ Download Drift Summary",f,"drift_summary.csv","text/csv",key="drift_summary_csv")
st.session_state["drift_results"]=drift_df
st.session_state["drift_summary"]=summary
st.success("✅ Data Drift Detection Completed")

def drift_badge(text,color="#6b7280"):
    return f'<span style="display:inline-block;padding:4px 10px;margin:2px;border-radius:6px;background:{color};color:white;font-size:13px;font-weight:600;">{text}</span>'
def drift_template(title,overview,column_docs):
    toc=""
    for col in column_docs:
        anchor=col.replace(" ","_").replace("/","_")
        toc+=f'<li><a href="#{anchor}">{col}</a></li>'
    cols=""
    for col,items in column_docs.items():
        anchor=col.replace(" ","_").replace("/","_")
        rules=""
        for item in items:
            rules+=f"<li>{item}</li>"
        cols+=f'<section id="{anchor}" class="column-card"><h2>{col}</h2><ul>{rules}</ul></section>'
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>{title}</title><style>*{{margin:0;padding:0;box-sizing:border-box}}body{{background:#181c22;color:#ecf0f1;font-family:Segoe UI,Arial,sans-serif}}.wrapper{{display:flex}}.sidebar{{position:fixed;left:0;top:0;width:340px;height:100vh;background:#1d2228;border-right:1px solid #30363d;overflow:auto}}.content{{margin-left:340px;width:calc(100% - 340px)}}.header{{padding:36px 50px;border-bottom:1px solid #30363d}}.header h1{{font-size:30px}}.left-title{{padding:35px;font-size:24px;font-weight:700}}.card{{margin:20px;background:#24292f;border-radius:8px;padding:20px}}.toc{{list-style:none;max-height:650px;overflow:auto}}.toc li{{padding:10px;border-bottom:1px solid #30363d}}.toc a{{color:#c9d1d9;text-decoration:none}}.main{{padding:35px}}.panel{{background:#fff;color:#111827;padding:20px;border-radius:8px;margin-bottom:25px}}.column-card{{background:#24292f;padding:20px;border-radius:8px;margin:20px 0}}.column-card h2{{background:#f3f4f6;color:#111827;padding:15px;border-radius:6px;margin-bottom:15px}}.column-card li{{margin:8px 0}}</style></head><body><div class="wrapper"><div class="sidebar"><div class="left-title">Drift Detection</div><div class="card"><h3>Columns</h3><ul class="toc"><li><a href="#overview">Overview</a></li>{toc}</ul></div></div><div class="content"><div class="header"><h1>{title}</h1></div><div class="main"><div id="overview" class="panel">{overview}</div>{cols}</div></div></div></body></html>"""
overview_html=f"<b>Total Columns :</b> {drift_summary['Columns']}<br><b>Passed :</b> {drift_summary['Passed']}<br><b>Failed :</b> {drift_summary['Failed']}<br><b>Success Rate :</b> {drift_summary['Success']} %"
column_docs={}
for _,row in drift_df.iterrows():
    docs=[]
    docs.append(f"Status : {drift_badge(row['Status'],'#16a34a' if row['Status']=='PASS' else '#dc2626')}")
    docs.append(f"KS Statistic : <b>{row['KS Statistic']}</b>")
    docs.append(f"P Value : <b>{row['P Value']}</b>")
    docs.append("Decision : No Drift Detected" if row["Status"]=="PASS" else "Decision : Drift Detected")
    column_docs[row["Column"]]=docs
drift_html=drift_template("Data Drift Detection Report",overview_html,column_docs)
DRIFT_REPORT=REPORT_DIR/"drift_detection_report.html"
save_html(DRIFT_REPORT,drift_html)
st.subheader("📄 Data Drift Detection Report")
with open(DRIFT_REPORT,"r",encoding="utf-8") as f:
    report_page=f.read()
components.html(report_page,height=700,scrolling=True)
with open(DRIFT_REPORT,"rb") as f:
    st.download_button("⬇ Download Drift Report",f,"drift_detection_report.html","text/html",key="drift_report_html")
    
st.subheader("📊 Drift Detection Summary")
st.dataframe(drift_df,use_container_width=True,height=500,hide_index=True)
summary=pd.DataFrame({"Metric":["Columns Tested","Passed","Failed","Success Rate"],"Value":[drift_summary["Columns"],drift_summary["Passed"],drift_summary["Failed"],f"{drift_summary['Success']} %"]})
st.dataframe(summary,use_container_width=True,hide_index=True)
summary.to_csv(OUTPUT_DIR/"drift_summary.csv",index=False)
with open(OUTPUT_DIR/"drift_summary.csv","rb") as f:
    st.download_button("⬇ Download Drift Summary",f,"drift_summary.csv","text/csv",key="download_drift_summary_csv")
st.session_state["drift_results"]=drift_df
st.session_state["drift_summary_df"]=summary
st.success("✅ Data Drift Detection Completed")
st.success("✅ drift_detection.csv Generated")
st.success("✅ drift_summary.csv Generated")

st.header("🤖 Model Training")
clean_df=st.session_state.get("clean_df")
if clean_df is None or clean_df.empty:
    st.error("Clean dataset not found.")
    st.stop()
clean_df=clean_df.copy()
if TARGET not in clean_df.columns:
    st.error(f"Target column '{TARGET}' not found.")
    st.stop()
X=clean_df.drop(columns=[TARGET])
y=clean_df[TARGET]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=SEED)
st.session_state["X_train"]=X_train
st.session_state["X_test"]=X_test
st.session_state["y_train"]=y_train
st.session_state["y_test"]=y_test
model=RandomForestRegressor(n_estimators=200,random_state=SEED,n_jobs=-1)
with st.spinner("Training Random Forest Model..."):
    model.fit(X_train,y_train)
joblib.dump(model,MODEL_FILE)
st.session_state["model"]=model
train_pred=model.predict(X_train)
test_pred=model.predict(X_test)
st.session_state["train_predictions"]=train_pred
st.session_state["test_predictions"]=test_pred
c1,c2,c3,c4=st.columns(4)
c1.metric("Training Rows",f"{len(X_train):,}")
c2.metric("Testing Rows",f"{len(X_test):,}")
c3.metric("Features",X_train.shape[1])
c4.metric("Target",TARGET)
st.success("✅ Random Forest Model Trained Successfully")
st.success("✅ Model Saved Successfully")

train_mae=mean_absolute_error(y_train,train_pred)
test_mae=mean_absolute_error(y_test,test_pred)
train_mse=mean_squared_error(y_train,train_pred)
test_mse=mean_squared_error(y_test,test_pred)
train_rmse=np.sqrt(train_mse)
test_rmse=np.sqrt(test_mse)
train_r2=r2_score(y_train,train_pred)
test_r2=r2_score(y_test,test_pred)
metrics_df=pd.DataFrame({"Metric":["Train MAE","Test MAE","Train MSE","Test MSE","Train RMSE","Test RMSE","Train R²","Test R²"],"Value":[round(train_mae,4),round(test_mae,4),round(train_mse,4),round(test_mse,4),round(train_rmse,4),round(test_rmse,4),round(train_r2,4),round(test_r2,4)]})
st.subheader("📊 Model Performance")
st.dataframe(metrics_df,use_container_width=True,hide_index=True)
c1,c2,c3,c4=st.columns(4)
c1.metric("Train R²",round(train_r2,4))
c2.metric("Test R²",round(test_r2,4))
c3.metric("Train RMSE",round(train_rmse,4))
c4.metric("Test RMSE",round(test_rmse,4))
metrics_df.to_csv(OUTPUT_DIR/"model_metrics.csv",index=False)
prediction_df=pd.DataFrame({"Actual":y_test.values,"Predicted":test_pred,"Residual":y_test.values-test_pred})
prediction_df.to_csv(OUTPUT_DIR/"test_predictions.csv",index=False)
st.session_state["metrics"]=metrics_df
st.session_state["prediction_df"]=prediction_df
with open(OUTPUT_DIR/"model_metrics.csv","rb") as f:
    st.download_button("⬇ Download Model Metrics",f,"model_metrics.csv","text/csv",key="model_metrics_csv")
with open(OUTPUT_DIR/"test_predictions.csv","rb") as f:
    st.download_button("⬇ Download Predictions",f,"test_predictions.csv","text/csv",key="test_predictions_csv")
st.success("✅ Model Evaluation Completed")

summary=pd.DataFrame({"Metric":["Training Rows","Testing Rows","Features","Train MAE","Test MAE","Train RMSE","Test RMSE","Train R²","Test R²"],"Value":[len(X_train),len(X_test),X_train.shape[1],round(train_mae,4),round(test_mae,4),round(train_rmse,4),round(test_rmse,4),round(train_r2,4),round(test_r2,4)]})
st.subheader("📊 Model Training Summary")
st.dataframe(summary,use_container_width=True,hide_index=True)
summary.to_csv(OUTPUT_DIR/"model_training_summary.csv",index=False)
with open(OUTPUT_DIR/"model_training_summary.csv","rb") as f:
    st.download_button("⬇ Download Training Summary",f,"model_training_summary.csv","text/csv",key="model_training_summary_csv")
st.session_state["trained_model"]=model
st.session_state["model_report"]=MODEL_REPORT
st.session_state["model_metrics"]=metrics_df
st.session_state["training_summary"]=summary
st.session_state["prediction_results"]=prediction_df
st.success("✅ Random Forest Model Training Completed")
st.success("✅ Model Evaluation Completed")
st.success("✅ Model Metrics Generated")
st.success("✅ Model Report Generated")
st.success("✅ Predictions Generated")

st.header("🔍 SHAP & 💡 LIME Explainability")
model=st.session_state.get("trained_model")
X_train=st.session_state.get("X_train")
X_test=st.session_state.get("X_test")
if model is None:
    st.error("Trained model not found.")
    st.stop()
if X_train is None or X_train.empty:
    st.error("Training data not found.")
    st.stop()
if X_test is None or X_test.empty:
    st.error("Testing data not found.")
    st.stop()
X_train=X_train.copy()
X_test=X_test.copy()
with st.spinner("Generating SHAP values..."):
    explainer=shap.TreeExplainer(model)
    shap_values=explainer.shap_values(X_test)
    if hasattr(shap_values,"values"):
        shap_array=shap_values.values
    else:
        shap_array=shap_values
with st.spinner("Generating LIME explanation..."):
    lime_explainer=LimeTabularExplainer(training_data=X_train.values,feature_names=X_train.columns.tolist(),mode="regression",random_state=SEED)
    sample_index=0
    lime_exp=lime_explainer.explain_instance(X_test.iloc[sample_index].values,model.predict,num_features=10)
c1,c2,c3,c4=st.columns(4)
c1.metric("Training Samples",len(X_train))
c2.metric("Testing Samples",len(X_test))
c3.metric("Features",X_train.shape[1])
c4.metric("Sample",sample_index+1)
st.subheader("📊 SHAP Summary Plot")
plt.figure(figsize=(12,6))
shap.summary_plot(shap_array,X_test,show=False)
plt.tight_layout()
st.pyplot(plt.gcf())
plt.close()
st.subheader("📈 SHAP Feature Importance")
plt.figure(figsize=(12,6))
shap.summary_plot(shap_array,X_test,plot_type="bar",show=False)
plt.tight_layout()
st.pyplot(plt.gcf())
plt.close()
importance=pd.DataFrame({"Feature":X_train.columns,"Importance":np.abs(shap_array).mean(axis=0)})
importance=importance.sort_values("Importance",ascending=False).reset_index(drop=True)
st.subheader("🏆 Feature Importance")
st.dataframe(importance,use_container_width=True,hide_index=True)
st.subheader("💡 LIME Explanation")
lime_list=lime_exp.as_list()
lime_df=pd.DataFrame(lime_list,columns=["Feature","Contribution"])
st.dataframe(lime_df,use_container_width=True,hide_index=True)
summary=pd.DataFrame({"Metric":["Training Samples","Testing Samples","Features","Top SHAP Feature","LIME Sample"],"Value":[len(X_train),len(X_test),X_train.shape[1],importance.iloc[0]["Feature"],sample_index+1]})
st.subheader("📊 Explainability Summary")
st.dataframe(summary,use_container_width=True,hide_index=True)
importance.to_csv(OUTPUT_DIR/"shap_feature_importance.csv",index=False)
summary.to_csv(OUTPUT_DIR/"explainability_summary.csv",index=False)
with open(OUTPUT_DIR/"shap_feature_importance.csv","rb") as f:
    st.download_button("⬇ Download SHAP Importance",f,"shap_feature_importance.csv","text/csv",key="download_shap_importance")
with open(OUTPUT_DIR/"explainability_summary.csv","rb") as f:
    st.download_button("⬇ Download Explainability Summary",f,"explainability_summary.csv","text/csv",key="download_explainability_summary")
st.session_state["shap_importance"]=importance
st.session_state["explainability_summary"]=summary
st.success("✅ SHAP Analysis Completed")
st.success("✅ LIME Explanation Generated")

st.subheader("📊 Explainability Summary")
st.dataframe(summary,use_container_width=True,hide_index=True)
summary.to_csv(OUTPUT_DIR/"explainability_summary.csv",index=False)
with open(OUTPUT_DIR/"explainability_summary.csv","rb") as f:
    st.download_button("⬇ Download Explainability Summary",f,"explainability_summary.csv","text/csv",key="explainability_summary_csv")
st.session_state["shap_values"]=shap_values
st.session_state["shap_importance"]=importance
st.session_state["lime_explanation"]=lime_exp
st.session_state["explainability_summary"]=summary
st.session_state["shap_summary_plot"]=SHAP_SUMMARY_PLOT
st.session_state["shap_bar_plot"]=SHAP_BAR_PLOT
st.session_state["lime_report"]=LIME_REPORT
st.session_state["xai_report"]=XAI_REPORT
st.success("✅ SHAP Explainability Completed")
st.success("✅ LIME Explainability Completed")
st.success("✅ SHAP Summary Plot Generated")
st.success("✅ SHAP Feature Importance Generated")
st.success("✅ LIME Explanation Generated")
st.success("✅ SHAP & LIME Report Generated")
st.success("✅ Explainability Summary Generated")

st.header("📋 Final XAI Report")
clean_df=st.session_state.get("clean_df")
metrics_df=st.session_state.get("model_metrics")
importance=st.session_state.get("shap_importance")
summary_df=st.session_state.get("explainability_summary")
if clean_df is None or clean_df.empty:
    st.error("Clean dataset not found.")
    st.stop()
if metrics_df is None or metrics_df.empty:
    st.error("Model metrics not found.")
    st.stop()
if importance is None or importance.empty:
    st.error("SHAP importance not found.")
    st.stop()
clean_df=clean_df.copy()
metrics_df=metrics_df.copy()
importance=importance.copy()
summary_df=summary_df.copy()
project_summary=pd.DataFrame({"Category":["Dataset","Rows","Columns","Target","Model","Validation","Explainability"],"Value":["UP_data_predict.csv",len(clean_df),len(clean_df.columns),TARGET,"Random Forest Regressor","Great Expectations + Cerberus + Pydantic","SHAP + LIME"]})
st.subheader("📊 Project Overview")
st.dataframe(project_summary,use_container_width=True,hide_index=True)
st.subheader("🏆 Top 20 Important Features")
st.dataframe(importance.head(20),use_container_width=True,height=500,hide_index=True)
project_summary.to_csv(OUTPUT_DIR/"project_summary.csv",index=False)
importance.head(20).to_csv(OUTPUT_DIR/"top_feature_importance.csv",index=False)
with open(OUTPUT_DIR/"project_summary.csv","rb") as f:
    st.download_button("⬇ Download Project Summary",f,"project_summary.csv","text/csv",key="project_summary_csv")
with open(OUTPUT_DIR/"top_feature_importance.csv","rb") as f:
    st.download_button("⬇ Download Top Features",f,"top_feature_importance.csv","text/csv",key="top_features_csv")
st.success("✅ Final Project Summary Generated")

def final_xai_report(title,project_summary,metrics_df,importance,summary_df):
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>{title}</title><style>body{{margin:0;background:#f3f4f6;font-family:Segoe UI,Arial,sans-serif}}.container{{padding:32px}}.header{{background:#24384f;color:#fff;padding:36px;border-radius:18px;margin-bottom:24px}}.header h1{{margin:0;font-size:36px;font-weight:700}}.card{{background:#fff;padding:24px;border-radius:12px;margin-bottom:24px;box-shadow:0 2px 10px rgba(0,0,0,.08)}}h2{{color:#24384f}}table{{width:100%;border-collapse:collapse}}th{{background:#2d435b;color:#fff;padding:14px;text-align:left;font-size:17px}}td{{padding:12px;border-bottom:1px solid #e5e7eb;font-size:16px}}</style></head><body><div class="container"><div class="header"><h1>{title}</h1><p>UP Rainfall Prediction System - Final Explainable AI Report</p></div><div class="card"><h2>Project Summary</h2>{project_summary.to_html(index=False)}</div><div class="card"><h2>Model Performance</h2>{metrics_df.to_html(index=False)}</div><div class="card"><h2>Top 20 SHAP Features</h2>{importance.head(20).to_html(index=False)}</div><div class="card"><h2>Explainability Summary</h2>{summary_df.to_html(index=False)}</div></div></body></html>"""
FINAL_XAI_REPORT=REPORT_DIR/"final_xai_report.html"
html=final_xai_report("Final Explainable AI Report",project_summary,metrics_df,importance,summary_df)
save_html(FINAL_XAI_REPORT,html)
st.subheader("📄 Final Explainable AI Report")
with open(FINAL_XAI_REPORT,"r",encoding="utf-8") as f:
    report_html=f.read()
components.html(report_html,height=800,scrolling=True)
with open(FINAL_XAI_REPORT,"rb") as f:
    st.download_button("⬇ Download Final XAI Report",f,"final_xai_report.html","text/html",key="final_xai_report_html")
st.success("✅ Final XAI Report Generated Successfully")

st.subheader("📊 Final Model Results")
st.dataframe(metrics_df,use_container_width=True,hide_index=True)
st.subheader("🏆 Top 20 Important Features")
st.dataframe(importance.head(20),use_container_width=True,height=500,hide_index=True)
final_summary=pd.DataFrame({"Metric":["Dataset","Rows","Columns","Target","Model","Train R²","Test R²","Top Feature"],"Value":["UP_data_predict.csv",len(clean_df),len(clean_df.columns),TARGET,"Random Forest Regressor",round(train_r2,4),round(test_r2,4),importance.iloc[0]["Feature"]]})
st.subheader("📋 Final Project Summary")
st.dataframe(final_summary,use_container_width=True,hide_index=True)
final_summary.to_csv(OUTPUT_DIR/"final_project_summary.csv",index=False)
with open(OUTPUT_DIR/"final_project_summary.csv","rb") as f:
    st.download_button("⬇ Download Final Project Summary",f,"final_project_summary.csv","text/csv",key="final_project_summary_csv")
st.session_state["final_project_summary"]=final_summary

st.session_state["final_xai_report"]=FINAL_XAI_REPORT
st.session_state["project_summary"]=project_summary
st.session_state["model_metrics"]=metrics_df
st.session_state["feature_importance"]=importance
st.session_state["explainability_summary"]=summary_df
st.success("✅ Dataset Validation Completed")
st.success("✅ Great Expectations Report Generated")
st.success("✅ Cerberus Validation Completed")
st.success("✅ Pydantic Validation Completed")
st.success("✅ Data Preprocessing Completed")
st.success("✅ Statistics Report Generated")
st.success("✅ Data Drift Detection Completed")
st.success("✅ Random Forest Model Training Completed")
st.success("✅ SHAP Explainability Completed")
st.success("✅ LIME Explainability Completed")
st.success("✅ Final Explainable AI Report Generated")
st.success("✅ UP Rainfall Prediction Pipeline Completed Successfully")
st.info("🎉 All reports, models, summaries and explainability artifacts have been generated successfully. You can download them from the sections above.")