import streamlit as st

from utils.data_profiler import (
    get_duplicate_info,
    get_statistical_summary
)


def show_statistics(df):
    """
    Display missing values, duplicate detection,
    and statistical summary.
    """

    # ==========================================
    # Missing Values Summary
    # ==========================================

    st.subheader("⚠️ Missing Values Summary")

    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if len(missing) == 0:
        st.success("No missing values found.")
    else:
        st.dataframe(
            missing.rename("Missing Values"),
            use_container_width=True
        )

    # ==========================================
    # Duplicate Detection
    # ==========================================

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

    # ==========================================
    # Statistical Summary
    # ==========================================

    st.subheader("📈 Statistical Summary")

    stats = get_statistical_summary(df)

    if stats is None:
        st.info("No numerical columns found.")
    else:
        st.dataframe(
            stats,
            use_container_width=True
        )