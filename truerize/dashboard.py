from pathlib import Path
import os

from flask import (
    Flask,
    render_template,
    abort,
    send_from_directory
)

# ==========================================================
# PATHS
# ==========================================================

PACKAGE_DIR = Path(__file__).resolve().parent

PROJECT_DIR = PACKAGE_DIR.parent

TEMPLATE_DIR = PACKAGE_DIR / "templates"

STATIC_DIR = PACKAGE_DIR / "static"

REPORT_DIR = PROJECT_DIR / "reports"

OUTPUT_DIR = PROJECT_DIR / "outputs"

# ==========================================================
# FLASK
# ==========================================================

app = Flask(
    __name__,
    template_folder=str(TEMPLATE_DIR),
    static_folder=str(STATIC_DIR)
)

# ==========================================================
# PIPELINES
# ==========================================================

PIPELINES = [

    {
        "id":"polars",
        "title":"Polars Configuration",
        "description":"High-performance dataframe using Polars."
    },

    {
        "id":"great_expectations",
        "title":"Great Expectations",
        "description":"Validate dataset quality."
    },

    {
        "id":"cerberus",
        "title":"Cerberus",
        "description":"Schema validation."
    },

    {
        "id":"pydantic",
        "title":"Pydantic",
        "description":"Python data validation."
    },

    {
        "id":"preprocessing",
        "title":"Preprocessing",
        "description":"Cleaning, Encoding and Scaling."
    },

    {
        "id":"statistics",
        "title":"Statistics",
        "description":"EDA and Statistical Analysis."
    },

    {
        "id":"drift",
        "title":"Drift Detection",
        "description":"Dataset Drift Detection."
    },

    {
        "id":"models",
        "title":"Model Training",
        "description":"Machine Learning Models."
    },

    {
        "id":"shap",
        "title":"SHAP",
        "description":"Global Explainability."
    },

    {
        "id":"lime",
        "title":"LIME",
        "description":"Local Explainability."
    }

]

# ==========================================================
# HTML REPORTS
# ==========================================================

def get_reports():

    reports=[]

    if REPORT_DIR.exists():

        for file in sorted(REPORT_DIR.glob("*.html")):

            reports.append({

                "name":file.stem.replace("_"," ").title(),

                "file":file.name

            })

    return reports


# ==========================================================
# OUTPUT FILES
# ==========================================================

def get_outputs():

    outputs=[]

    if OUTPUT_DIR.exists():

        for root,dirs,files in os.walk(OUTPUT_DIR):

            for f in files:

                p=Path(root)/f

                outputs.append({

                    "name":f,

                    "path":str(p.relative_to(PROJECT_DIR))

                })

    return outputs

# ==========================================================
# HOME
# ==========================================================

@app.route("/")
def dashboard():

    return render_template(

        "dashboard.html",

        pipelines=PIPELINES,

        reports=get_reports(),

        outputs=get_outputs()

    )

# ==========================================================
# PIPELINE
# ==========================================================

@app.route("/pipeline/<pipeline>")

def pipeline(pipeline):

    obj=None

    for p in PIPELINES:

        if p["id"]==pipeline:

            obj=p

            break

    if obj is None:

        abort(404)

    return render_template(

        "pipeline.html",

        pipeline=obj,

        reports=get_reports()

    )

# ==========================================================
# REPORTS
# ==========================================================

@app.route("/reports")

def reports():

    return render_template(

        "reports.html",

        reports=get_reports()

    )

# ==========================================================
# REPORT VIEW
# ==========================================================

@app.route("/report/<filename>")

def report_view(filename):

    file=REPORT_DIR/filename

    if not file.exists():

        abort(404)

    return render_template(

        "report_view.html",

        filename=filename

    )

# ==========================================================
# SERVE HTML REPORT
# ==========================================================

@app.route("/reports/file/<filename>")

def report_file(filename):

    return send_from_directory(

        REPORT_DIR,

        filename

    )

# ==========================================================
# ABOUT
# ==========================================================

@app.route("/about")

def about():

    return render_template(

        "about.html",

        pipelines=PIPELINES

    )

# ==========================================================
# RUN
# ==========================================================

if __name__=="__main__":

    app.run(

        host="127.0.0.1",

        port=5000,

        debug=True

    )

# ==========================================================
# HOME PAGE
# ==========================================================

@app.route("/")
def home():

    stats = dashboard_stats()

    return render_template(

        "dashboard.html",

        pipelines=PIPELINES,

        reports=get_html_reports(),

        outputs=get_output_files(),

        stats=stats

    )


# ==========================================================
# PIPELINE PAGE
# ==========================================================

@app.route("/pipeline/<pipeline_id>")
def pipeline(pipeline_id):

    pipeline = next(

        (p for p in PIPELINES if p["id"] == pipeline_id),

        None

    )

    if pipeline is None:

        abort(404)

    reports = get_html_reports()

    outputs = get_output_files()

    return render_template(

        "pipeline.html",

        pipeline=pipeline,

        reports=reports,

        outputs=outputs

    )


# ==========================================================
# REPORTS PAGE
# ==========================================================

@app.route("/reports")
def reports():

    reports = get_html_reports()

    return render_template(

        "reports.html",

        reports=reports

    )


# ==========================================================
# REPORT VIEW PAGE
# ==========================================================

@app.route("/report/<filename>")
def report_view(filename):

    file_path = REPORT_DIR / filename

    if not file_path.exists():

        abort(404)

    return render_template(

        "report_view.html",

        filename=filename

    )


# ==========================================================
# SERVE REPORT FILE
# ==========================================================

@app.route("/reports/file/<filename>")
def report_file(filename):

    return send_from_directory(

        REPORT_DIR,

        filename

    )


# ==========================================================
# ABOUT PAGE
# ==========================================================

@app.route("/about")
def about():

    return render_template(

        "about.html",

        pipelines=PIPELINES

    )

# ==========================================================
# ERROR HANDLERS
# ==========================================================

@app.errorhandler(404)
def page_not_found(error):

    return (

        render_template(

            "about.html",

            title="404 - Page Not Found",

            pipelines=PIPELINES,

            error="The page you requested does not exist."

        ),

        404

    )


@app.errorhandler(500)
def internal_server_error(error):

    return (

        render_template(

            "about.html",

            title="500 - Internal Server Error",

            pipelines=PIPELINES,

            error="Something went wrong on the server."

        ),

        500

    )


# ==========================================================
# CONTEXT PROCESSOR
# Available in every HTML template
# ==========================================================

@app.context_processor
def global_context():

    return {

        "project_name": "TRUERIZE",

        "framework": "Flask",

        "version": "1.0.0",

        "pipelines": PIPELINES

    }


# ==========================================================
# MAIN
# ==========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("               TRUERIZE DASHBOARD")
    print("=" * 60)

    print(f"Templates : {TEMPLATE_DIR}")
    print(f"Static    : {STATIC_DIR}")
    print(f"Reports   : {REPORT_DIR}")
    print(f"Outputs   : {OUTPUT_DIR}")

    print(f"Pipelines : {len(PIPELINES)}")
    print(f"Reports   : {len(get_html_reports())}")
    print(f"Outputs   : {len(get_output_files())}")

    print("\nDashboard Running...")
    print("URL : http://127.0.0.1:5000")
    print("=" * 60)

    # SAFE FLASK RUN (IMPORTANT FIX)
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,          # must be False for Jupyter stability
        use_reloader=False    # prevents double execution
    )