import os
import sys

# Get project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import streamlit as st
import pandas as pd

from utils.file_loader import load_file

from utils.data_profiler import (
    get_dataset_overview,
    detect_schema,
    get_duplicate_info,
    get_statistical_summary,
    get_data_quality_report,
    get_column_profile,
    get_ai_recommendation
)
# ---------------------------------------------------
# Streamlit Page Configuration
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

    # Load file
    df = load_file(uploaded_file)

    st.success("✅ File uploaded successfully!")

    # ===================================================
    # Dataset Preview
    # ===================================================

    st.subheader("📄 Dataset Preview")
    st.dataframe(df)

    # ===================================================
    # Dataset Overview
    # ===================================================

    st.subheader("📊 Dataset Overview")

    overview = get_dataset_overview(df)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", overview["rows"])
    col2.metric("Columns", overview["columns"])
    col3.metric("Total Cells", overview["total_cells"])
    col4.metric("Memory (MB)", overview["memory_usage_mb"])

    # ===================================================
    # Schema Detection
    # ===================================================

    st.subheader("🧠 Schema Detection")

    schema = detect_schema(df)

    schema_df = pd.DataFrame({
        "Column": list(schema.keys()),
        "Detected Type": list(schema.values())
    })

    st.dataframe(schema_df)

    # ===================================================
    # Column Names
    # ===================================================

    st.subheader("📌 Column Names")
    st.write(list(df.columns))

    # ===================================================
    # Dataset Information
    # ===================================================

    st.subheader("📋 Dataset Information")

    info_df = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str),
        "Missing Values": df.isnull().sum().values
    })

    st.dataframe(info_df)

    # ===================================================
    # Missing Values Summary
    # ===================================================

    st.subheader("⚠️ Missing Values Summary")

    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if len(missing) == 0:
        st.success("No missing values found.")
    else:
        st.dataframe(
            missing.rename("Missing Values")
        )

    # ===================================================
    # Duplicate Detection
    # ===================================================

    st.subheader("🔁 Duplicate Detection")

    duplicate_info = get_duplicate_info(df)

    col1, col2 = st.columns(2)

    col1.metric(
        "Duplicate Rows",
        duplicate_info["duplicate_rows"]
    )

    col2.metric(
        "Duplicate %",
        f"{duplicate_info['duplicate_percentage']}%"
    )

    if duplicate_info["duplicate_rows"] == 0:
        st.success("No duplicate rows found.")
    else:
        st.warning(
            f"{duplicate_info['duplicate_rows']} duplicate rows detected."
        )

    # ===================================================
    # Statistical Summary
    # ===================================================

    st.subheader("📈 Statistical Summary")

    stats = get_statistical_summary(df)

    if stats is None:
        st.info("No numerical columns found.")
    else:
        st.dataframe(stats)
# ===================================================
# Data Quality Report
# ===================================================

    st.subheader("⭐ Data Quality Report")

    quality = get_data_quality_report(df)

    col1, col2, col3 = st.columns(3)

    col1.metric("Quality Score", f"{quality['Quality Score']}%")
    col2.metric("Missing %", f"{quality['Missing %']}%")
    col3.metric("Duplicate %", f"{quality['Duplicate %']}%")

    st.write("### Dataset Quality Details")

    quality_df = pd.DataFrame(
      quality.items(),
      columns=["Metric", "Value"]
    )

    st.dataframe(quality_df, use_container_width=True)
    # ===================================================
    # Column Profile
    # ===================================================

    st.subheader("📑 Column Profile")

    profile_df = get_column_profile(df)

    st.dataframe(
    profile_df,
    use_container_width=True
    )
    # ===================================================
    # AI Dataset Health Report
    # ===================================================

    st.subheader("🤖 AI Dataset Health Report")

    recommendations = get_ai_recommendation(df)

    for recommendation in recommendations:
        st.write(recommendation)