import streamlit as st
import pandas as pd

from utils.data_profiler import (
    get_data_quality_report,
    get_column_profile
)


def show_quality(df):
    """
    Display data quality report
    and column profile.
    """

    # ==========================================
    # Data Quality Report
    # ==========================================

    st.subheader("⭐ Data Quality Report")

    quality = get_data_quality_report(df)

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Quality Score",
        f"{quality['Quality Score']}%"
    )

    col2.metric(
        "Missing %",
        f"{quality['Missing %']}%"
    )

    col3.metric(
        "Duplicate %",
        f"{quality['Duplicate %']}%"
    )

    st.write("### Dataset Quality Details")

    quality_df = pd.DataFrame(
        quality.items(),
        columns=["Metric", "Value"]
    )

    st.dataframe(
        quality_df,
        use_container_width=True
    )

    # ==========================================
    # Column Profile
    # ==========================================

    st.subheader("📑 Column Profile")

    profile_df = get_column_profile(df)

    st.dataframe(
        profile_df,
        use_container_width=True
    )