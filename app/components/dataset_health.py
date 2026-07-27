import streamlit as st


def show_dataset_health(health):
    """
    Display the overall dataset health score.
    """

    st.header("🏥 Dataset Health Score")

    score = health["score"]

    # ----------------------------
    # Health Indicator
    # ----------------------------

    if score >= 90:
        color = "🟢"
    elif score >= 75:
        color = "🟡"
    elif score >= 60:
        color = "🟠"
    else:
        color = "🔴"

    st.metric(
        label="Overall Health Score",
        value=f"{score}/100"
    )

    st.success(f"{color} **Overall Rating:** {health['rating']}")

    st.divider()

    # ----------------------------
    # Detailed Metrics
    # ----------------------------

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Duplicate Rows",
            health["duplicates"]
        )

        st.metric(
            "Missing Data %",
            f"{health['missing_percentage']}%"
        )

    with col2:
        st.metric(
            "Average Outlier %",
            f"{health['average_outlier_percentage']}%"
        )

        st.metric(
            "Strong Correlations",
            health["strong_correlations"]
        )

    st.divider()

    st.subheader("💡 Recommendation")

    st.info(health["recommendation"])