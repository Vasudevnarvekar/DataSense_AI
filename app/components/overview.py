import streamlit as st

from utils.data_profiler import get_dataset_overview


def show_dataset_overview(df):
    """
    Display dataset overview metrics.
    """

    st.subheader("📊 Dataset Overview")

    overview = get_dataset_overview(df)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Rows",
        overview["rows"]
    )

    col2.metric(
        "Columns",
        overview["columns"]
    )

    col3.metric(
        "Total Cells",
        overview["total_cells"]
    )

    col4.metric(
        "Memory (MB)",
        overview["memory_usage_mb"]
    )