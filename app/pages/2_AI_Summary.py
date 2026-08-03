import os
import sys

# -------------------------------------------------------
# Add Project Root
# -------------------------------------------------------

PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# -------------------------------------------------------

import streamlit as st

from services.ai_summary import AISummaryService


st.set_page_config(
    page_title="AI Summary",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Dataset Summary")

st.markdown(
    """
Generate an AI-powered summary of your cleaned dataset.
"""
)

# -------------------------------------------------------
# Check Dataset
# -------------------------------------------------------

if "cleaned_df" not in st.session_state:

    st.warning(
        "Please upload and clean a dataset first."
    )

    st.stop()

df = st.session_state["cleaned_df"]

# -------------------------------------------------------
# Dataset Information
# -------------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Rows",
        df.shape[0]
    )

with col2:

    st.metric(
        "Columns",
        df.shape[1]
    )

st.divider()

# -------------------------------------------------------
# Generate Summary
# -------------------------------------------------------

if st.button(
    "🚀 Generate AI Summary",
    use_container_width=True
):

    with st.spinner(
        "Analyzing dataset..."
    ):

        summary = AISummaryService.generate_summary(df)

    st.success("Summary Generated Successfully!")

    st.divider()

    icons = {
        "Dataset Overview": "📊",
        "Data Quality Assessment": "🧹",
        "Key Observations": "📈",
        "Business Insights": "💼",
        "Potential Risks": "⚠️",
        "Recommendations": "✅"
    }

    for title, content in summary.items():

        with st.container():

            st.subheader(
                f"{icons.get(title,'📄')} {title}"
            )

            st.write(content)

            st.divider()