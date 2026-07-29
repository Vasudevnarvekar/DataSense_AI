import os
import sys

# ---------------------------------------------------
# Add Project Root to Python Path
# ---------------------------------------------------

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# ---------------------------------------------------
# Imports
# ---------------------------------------------------

import streamlit as st
from utils.column_insights import generate_column_insights
from app.components.column_insights import show_column_insights
from utils.file_loader import load_file
from utils.insight_generator import generate_dataset_insights
from utils.correlation_insights import generate_correlation_insights
from app.components.correlation_insights import show_correlation_insights
from utils.outlier_insights import generate_outlier_insights
from app.components.outlier_insights import show_outlier_insights
from utils.missing_value_insights import generate_missing_value_insights
from app.components.missing_value_insights import show_missing_value_insights
from utils.business_insights import generate_business_insights
from app.components.business_insights import show_business_insights
from utils.dataset_health import calculate_dataset_health
from app.components.dataset_health import show_dataset_health

from app.components.dataset_preview import show_dataset_preview
from app.components.overview import show_dataset_overview
from app.components.schema import show_schema
from app.components.statistics import show_statistics
from app.components.quality import show_quality
from app.components.recommendations import show_ai_recommendations
from app.components.visualizations import show_visualizations
from app.components.ai_summary import show_ai_summary

# ---------------------------------------------------
# Streamlit Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="DataSense AI",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# Title
# ---------------------------------------------------

st.title("📊 DataSense AI")
st.write("Upload a CSV or Excel file to begin analysis.")

# ---------------------------------------------------
# Load New Dataset Button
# ---------------------------------------------------

if "df" in st.session_state:
    if st.button("🗑️ Load New Dataset"):

        keys_to_clear = [
            # Dataset
            "df",
            "cleaned_df",
            "file_name",

            # Step 10 - AutoML
            "target_column",
            "feature_columns",
            "problem_type",
            "trained_models",
            "best_model",
            "model_results",
        ]

        for key in keys_to_clear:
            st.session_state.pop(key, None)

        st.rerun()
# ---------------------------------------------------
# File Upload
# ---------------------------------------------------

uploaded_file = st.file_uploader(
    "Choose a CSV or Excel file",
    type=["csv", "xlsx"]
)

# ---------------------------------------------------
# Process Uploaded File
# ---------------------------------------------------

if uploaded_file is not None:

    df = load_file(uploaded_file)

    st.session_state["df"] = df
    st.session_state["cleaned_df"] = df.copy()
    st.session_state["file_name"] = uploaded_file.name

# ---------------------------------------------------
# Display Dataset
# ---------------------------------------------------

if "cleaned_df" in st.session_state:

    # Always work with the latest cleaned dataset
    df = st.session_state["cleaned_df"]

    st.success(
        f"✅ Dataset Loaded: {st.session_state.get('file_name', 'Uploaded File')}"
    )

    # ---------------------------------------------------
    # Dataset Preview
    # ---------------------------------------------------

    show_dataset_preview(df)

    # ---------------------------------------------------
    # Dataset Overview
    # ---------------------------------------------------

    show_dataset_overview(df)

    # ---------------------------------------------------
    # Schema Detection
    # ---------------------------------------------------

    show_schema(df)

    # ---------------------------------------------------
    # Statistical Summary
    # ---------------------------------------------------

    show_statistics(df)

    # ---------------------------------------------------
    # Data Quality Report
    # ---------------------------------------------------

    show_quality(df)

    # ---------------------------------------------------
    # AI Recommendations
    # ---------------------------------------------------

    show_ai_recommendations(df)

    # ---------------------------------------------------
    # Interactive Visualizations
    # ---------------------------------------------------

    show_visualizations(df)

    # ---------------------------------------------------
    # AI Dataset Summary (Step 7)
    # ---------------------------------------------------

    insights = generate_dataset_insights(df)
    show_ai_summary(insights)

    column_insights = generate_column_insights(df)
    show_column_insights(column_insights)

    correlation_insights = generate_correlation_insights(df)
    show_correlation_insights(correlation_insights)

    outlier_insights = generate_outlier_insights(df)
    show_outlier_insights(outlier_insights)

    missing_value_insights = generate_missing_value_insights(df)
    show_missing_value_insights(missing_value_insights)

    business_insights = generate_business_insights(
        df,
        correlation_insights,
        outlier_insights,
        missing_value_insights,
    )
    show_business_insights(business_insights)

    health = calculate_dataset_health(
        df,
        correlation_insights,
        outlier_insights,
        missing_value_insights,
    )
    show_dataset_health(health)
# ---------------------------------------------------
# No Dataset Uploaded
# ---------------------------------------------------

else:
    st.info("👆 Please upload a CSV or Excel file to begin.")

