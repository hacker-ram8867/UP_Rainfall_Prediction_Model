import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import utils.report_links as reports

st.set_page_config(page_title="📊 Statistics & Drift Analysis",page_icon="📊",layout="wide")

st.title("📊 Statistics & Drift Analysis")

st.write("Statistics and Drift Analysis is the fourth stage of the Machine Learning pipeline. This module analyzes the characteristics of the dataset using descriptive statistics and monitors whether incoming data has changed compared to the training dataset. Detecting data drift helps maintain model performance and prediction reliability.")

st.success("Module 4 of 6 • Statistics & Drift Analysis")

st.divider()

with st.expander("📖 Overview",expanded=True):
    st.write("""
Statistics describe the characteristics of a dataset by calculating measures such as mean, median, variance and standard deviation. Drift Analysis compares the training dataset with new incoming data to determine whether feature distributions have changed over time.
""")
    st.table({
        "Component":["Statistics","Distribution Analysis","KS Test","Drift Detection"],
        "Purpose":["Describe dataset","Analyze feature distribution","Compare distributions","Detect data drift"]
    })

with st.expander("🎯 Objectives"):
    st.markdown("""
- Calculate descriptive statistics
- Analyze feature distributions
- Compare training and testing datasets
- Detect feature drift
- Identify distribution changes
- Generate statistical reports
- Generate drift reports
- Monitor model reliability
""")

with st.expander("❓ Why Statistics & Drift Analysis?"):
    st.write("""
Machine Learning models assume that incoming data follows the same distribution as the training dataset. When data distributions change, model accuracy decreases. Statistics and Drift Analysis detect these changes early and help maintain reliable predictions.
""")
    st.table({
        "Problem":["Changing Distribution","Feature Drift","Poor Predictions","Model Performance Drop"],
        "Solution":["Statistics","KS Test","Distribution Comparison","Drift Monitoring"]
    })

with st.expander("🎯 Main Goals"):
    st.write("""
The main goal of Statistics and Drift Analysis is to understand the dataset, compare distributions, detect drift and ensure the Machine Learning model continues to perform accurately on new incoming data.
""")
    st.table({
        "Goal":["Understand Dataset","Detect Drift","Compare Distributions","Support Model Monitoring"],
        "Description":["Statistical Analysis","Identify Data Changes","Training vs New Data","Reliable Predictions"]
    })

st.success("✅ Part 1 Completed Successfully")

with st.expander("🔄 Statistics Pipeline"):
    st.code("""
Training Dataset
        │
        ▼
Incoming Dataset
        │
        ▼
Statistical Analysis
        │
        ▼
Distribution Analysis
        │
        ▼
Kolmogorov-Smirnov Test
        │
        ▼
Drift Detection
        │
        ▼
Generate TXT Report
        │
        ▼
Generate HTML Report
""")
    st.table({
        "Stage":["Load Dataset","Statistics","Distribution","KS Test","Drift Detection","Reports"],
        "Purpose":["Read Data","Calculate Metrics","Compare Features","Detect Distribution Changes","Identify Drift","Generate Outputs"]
    })

with st.expander("⚙️ Statistics Workflow"):
    st.write("The workflow analyzes dataset statistics before performing feature-wise drift detection.")
    st.code("""
Dataset
    │
    ▼
Calculate Mean
    │
    ▼
Calculate Median
    │
    ▼
Calculate Variance
    │
    ▼
Distribution Analysis
    │
    ▼
KS Test
    │
    ▼
Generate Reports
""")
    workflow_df={
    "Workflow":["Dataset","Statistics","Distribution","KS Test","Reports"],
    "Result":["Loaded","Calculated","Compared","Completed","Generated"]
    }
    st.table(workflow_df)

with st.expander("🏗️ Statistics Architecture"):
    st.code("""
Training Dataset
        │
        ▼
Statistics Engine
        │
        ▼
Distribution Analyzer
        │
        ▼
KS Drift Detector
        │
        ▼
TXT Report
        │
        ▼
HTML Report
        │
        ▼
Model Monitoring
""")
    architecture_df={
    "Module":["Statistics","Distribution","KS Test","Drift Detection","Reports"],
    "Purpose":["Describe Dataset","Compare Features","Detect Drift","Identify Changes","TXT & HTML Outputs"]
    }
    st.table(architecture_df)

with st.expander("📊 Statistics Components"):
    component_df={
    "Component":["Mean","Median","Mode","Variance","Standard Deviation","Minimum","Maximum","Quartiles"],
    "Purpose":["Average","Middle Value","Most Frequent","Spread","Variability","Lowest Value","Highest Value","Distribution"]
    }
    st.table(component_df)

st.success("✅ Part 2 Completed Successfully")

with st.expander("📈 Descriptive Statistics"):
    st.write("Descriptive statistics summarize the numerical characteristics of the dataset and help understand the overall data distribution before Machine Learning.")
    statistics_df={
    "Statistic":["Mean","Median","Mode","Minimum","Maximum","Range","Variance","Standard Deviation","Quartiles"],
    "Purpose":["Average Value","Middle Value","Most Frequent","Lowest Value","Highest Value","Difference","Measure Spread","Measure Variability","Distribution Analysis"]
    }
    st.table(statistics_df)

with st.expander("📉 Distribution Analysis"):
    st.write("Distribution analysis studies how feature values are spread across the dataset and identifies skewness, symmetry and abnormal distributions.")
    distribution_df={
    "Analysis":["Normal Distribution","Skewed Distribution","Uniform Distribution","Outlier Detection","Feature Comparison"],
    "Purpose":["Bell Curve","Asymmetrical Data","Equal Frequency","Detect Extreme Values","Compare Features"]
    }
    st.table(distribution_df)

with st.expander("🚨 Drift Detection"):
    st.write("Data drift occurs when the distribution of incoming data changes compared to the training dataset. Detecting drift helps maintain Machine Learning reliability.")
    drift_df={
    "Drift Type":["Feature Drift","Distribution Drift","Statistical Drift","Data Drift"],
    "Description":["Feature Distribution Changed","Population Changed","Statistics Changed","Overall Dataset Changed"]
    }
    st.table(drift_df)

with st.expander("📋 Kolmogorov-Smirnov (KS) Test"):
    st.write("The Kolmogorov-Smirnov Test compares the cumulative distributions of the training dataset and incoming dataset to determine whether significant drift exists.")
    ks_df={
    "Metric":["KS Statistic","P-Value","Threshold","Decision"],
    "Purpose":["Distribution Difference","Statistical Significance","Drift Limit","Pass / Fail"]
    }
    st.table(ks_df)

st.success("✅ Part 3 Completed Successfully")

with st.expander("📄 Generated Outputs"):
    output_df={
    "Output":["KS Drift Report","KS Drift HTML Report"],
    "Format":["TXT","HTML"],
    "Status":["✅ Generated","✅ Generated"]
    }
    st.table(output_df)
    st.subheader("📂 Output Locations")
    st.code(str(reports.KS_DRIFT_TXT))
    st.code(str(reports.KS_DRIFT_HTML))

with st.expander("📂 Generated Reports"):
    st.subheader("📄 KS Drift TXT Report")
    if reports.KS_DRIFT_TXT.exists():
        txt=reports.KS_DRIFT_TXT.read_text(encoding="utf-8")
        st.success("✅ KS Drift TXT Report Loaded Successfully")
        st.text_area("KS Drift Report",txt,height=500)
    else:
        st.error("❌ KS Drift TXT Report Not Found")
    st.divider()
    st.subheader("🌐 KS Drift HTML Report")
    if reports.KS_DRIFT_HTML.exists():
        html=reports.KS_DRIFT_HTML.read_text(encoding="utf-8")
        st.success("✅ KS Drift HTML Report Loaded Successfully")
        components.html(html,height=900,scrolling=True)
    else:
        st.error("❌ KS Drift HTML Report Not Found")

st.success("✅ Part 4 Completed Successfully")

st.success("✅ Part 5 Started Successfully")

with st.expander("📊 Statistics & Drift Summary"):
    st.write("This section summarizes the overall statistics and drift behavior of the dataset across all features. It helps in quickly understanding whether the dataset is stable or has significant distribution changes.")

    summary_df = {
        "Aspect": ["Dataset Stability", "Feature Drift", "Distribution Shift", "Model Risk", "Data Quality"],
        "Observation": ["Stable / Unstable", "Low / High Drift", "No / Significant Shift", "Low / Medium / High", "Good / Needs Attention"]
    }

    st.table(summary_df)

    st.info("📌 This summary is derived from KS test results and statistical comparisons across datasets.")

with st.expander("📚 Best Practices"):
    st.write("Follow these best practices to ensure reliable statistics and drift detection in production ML systems.")

    best_practices_df = {
        "Practice": [
            "Always compare training vs incoming data",
            "Monitor KS statistic regularly",
            "Set proper drift thresholds",
            "Log all statistical changes",
            "Re-train model when drift is high",
            "Validate data before inference",
            "Automate drift reporting"
        ],
        "Benefit": [
            "Ensures consistency",
            "Early drift detection",
            "Better decision control",
            "Traceability",
            "Maintains accuracy",
            "Prevents bad predictions",
            "Saves manual effort"
        ]
    }

    st.table(best_practices_df)

st.success("✅ Part 5 Completed Successfully")

st.success("🚀 Part 6 Started Successfully")

with st.expander("🎯 Conclusion", expanded=True):
    st.write("""
Statistics and Drift Analysis plays a critical role in maintaining Machine Learning model reliability. 
It ensures that the incoming data behaves similarly to the training data and detects any changes early.

By using descriptive statistics, distribution analysis, and KS testing, we can continuously monitor data quality and model stability in production systems.
""")

    st.markdown("""
### 🔑 Key Takeaways
- Statistics help understand dataset structure  
- Drift detection ensures model reliability  
- KS test identifies distribution changes  
- Reports help track data behavior over time  
- Essential for production ML pipelines  
""")

st.divider()

st.subheader("📂 Final Report Viewer")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📄 TXT Report")
    if reports.KS_DRIFT_TXT.exists():
        st.success("TXT Report Available")
        st.code(reports.KS_DRIFT_TXT.read_text(encoding="utf-8"), language="text")
    else:
        st.warning("TXT Report Missing")

with col2:
    st.markdown("### 🌐 HTML Report")
    if reports.KS_DRIFT_HTML.exists():
        st.success("HTML Report Available")
        components.html(reports.KS_DRIFT_HTML.read_text(encoding="utf-8"), height=800, scrolling=True)
    else:
        st.warning("HTML Report Missing")

st.divider()

st.info("📊 Module 4 Completed: Statistics & Drift Analysis")

st.success("🎉 Pipeline Step Finished Successfully")