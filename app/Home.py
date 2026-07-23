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

from utils.file_loader import load_file

from app.components.dataset_preview import show_dataset_preview
from app.components.overview import show_dataset_overview
from app.components.schema import show_schema
from app.components.statistics import show_statistics
from app.components.quality import show_quality
from app.components.recommendations import show_ai_recommendations

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
# Upload New Dataset Button
# ---------------------------------------------------

if "df" in st.session_state:
    if st.button("🗑️ Load New Dataset"):
        for key in ["df", "cleaned_df", "file_name"]:
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

    # Store dataset
    st.session_state["df"] = df
    st.session_state["cleaned_df"] = df.copy()
    st.session_state["file_name"] = uploaded_file.name

# ---------------------------------------------------
# Display Dataset
# ---------------------------------------------------

if "df" in st.session_state:

    df = st.session_state["df"]

    st.success(
        f"✅ Dataset Loaded: {st.session_state.get('file_name', 'Uploaded File')}"
    )

    show_dataset_preview(df)
    show_dataset_overview(df)
    show_schema(df)
    show_statistics(df)
    show_quality(df)
    show_ai_recommendations(df)

else:
    st.info("👆 Please upload a CSV or Excel file to begin.")