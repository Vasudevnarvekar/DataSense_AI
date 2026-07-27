import os
import sys
import pandas as pd
import streamlit as st

# ---------------------------------------------------
# Add Project Root to Python Path
# ---------------------------------------------------

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# ---------------------------------------------------
# Imports
# ---------------------------------------------------

from utils.python_engine import execute_python_code
from app.components.python_editor import render_python_editor
from app.components.python_output import render_python_output
from app.components.python_visualization import render_visualizations

# ---------------------------------------------------
# Page Title
# ---------------------------------------------------

st.title("🐍 Python Code Execution Agent")

# ---------------------------------------------------
# Check Dataset
# ---------------------------------------------------

if "cleaned_df" not in st.session_state:
    st.warning("Please upload and clean a dataset first.")
    st.stop()

df = st.session_state["cleaned_df"]

# ---------------------------------------------------
# Dataset Information
# ---------------------------------------------------

st.subheader("📋 Dataset Information")

col1, col2 = st.columns(2)

with col1:
    st.metric("Rows", df.shape[0])

with col2:
    st.metric("Columns", df.shape[1])

st.write("### Available Columns")
st.write(", ".join(df.columns))

# ---------------------------------------------------
# Python Editor
# ---------------------------------------------------

code = render_python_editor()

# ---------------------------------------------------
# Run Python Code
# ---------------------------------------------------

if st.button("▶ Run Python Code"):

    success, output, result = execute_python_code(code, df)

    render_python_output(
        success,
        output,
        result
    )

    if success:
        render_visualizations(result)