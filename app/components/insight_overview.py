import streamlit as st


def render_dataset_overview(overview):
    """
    Display dataset overview metrics.
    """

    st.subheader("📋 Dataset Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", overview["Total Rows"])
    col2.metric("Columns", overview["Total Columns"])
    col3.metric("Memory (MB)", overview["Memory Usage (MB)"])

    col1, col2, col3 = st.columns(3)

    col1.metric("Numerical", overview["Numerical Columns"])
    col2.metric("Categorical", overview["Categorical Columns"])
    col3.metric("Missing Values", overview["Missing Values"])

    st.metric("Duplicate Rows", overview["Duplicate Rows"])