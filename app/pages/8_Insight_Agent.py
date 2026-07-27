import os
import sys
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

from app.components.insight_overview import (
    render_dataset_overview
)

from app.components.insight_numeric import (
    render_numerical_insights
)

from app.components.insight_categorical import (
    render_categorical_insights
)
from app.components.insight_correlation import (
    render_correlation_insights
)
from utils.insight_engine import (
    get_dataset_overview,
    generate_overview_summary,
    generate_numerical_insights,
    generate_categorical_insights,
    generate_correlation_insights,
    generate_executive_summary
)

from app.components.insight_summary import (
    render_executive_summary
)
# ---------------------------------------------------
# Page Title
# ---------------------------------------------------

st.title("💡 Insight Generation Agent")

# ---------------------------------------------------
# Check Dataset
# ---------------------------------------------------

if "cleaned_df" not in st.session_state:
    st.warning("Please upload and clean a dataset first.")
    st.stop()

df = st.session_state["cleaned_df"]

# ---------------------------------------------------
# Generate Dataset Overview
# ---------------------------------------------------

overview = get_dataset_overview(df)

# ---------------------------------------------------
# Display Dataset Overview
# ---------------------------------------------------

render_dataset_overview(overview)

# ---------------------------------------------------
# Dataset Summary
# ---------------------------------------------------

st.divider()

st.subheader("📝 Dataset Summary")

summary = generate_overview_summary(overview)

st.markdown(summary)

# ---------------------------------------------------
# Numerical Insights
# ---------------------------------------------------

st.divider()

numeric_result = generate_numerical_insights(df)

if numeric_result:

    stats, insights = numeric_result

    render_numerical_insights(
        stats,
        insights
    )

# ---------------------------------------------------
# Categorical Insights
# ---------------------------------------------------

st.divider()

categorical_result = generate_categorical_insights(df)

if categorical_result is not None:

    render_categorical_insights(categorical_result)

# ---------------------------------------------------
# Correlation Insights
# ---------------------------------------------------

st.divider()

correlation_result = generate_correlation_insights(df)

if correlation_result is not None:

    corr_matrix, strongest_positive, strongest_negative = correlation_result

    render_correlation_insights(
        corr_matrix,
        strongest_positive,
        strongest_negative
    )

# ---------------------------------------------------
# Executive Summary
# ---------------------------------------------------

st.divider()

summary = generate_executive_summary(df)

render_executive_summary(summary)