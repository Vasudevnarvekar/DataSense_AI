import streamlit as st


def show_outlier_insights(outlier_insights):
    """
    Display AI-generated outlier insights.
    """

    st.header("🚨 Outlier Intelligence")

    if not outlier_insights:
        st.info("No numerical columns available for outlier analysis.")
        return

    # -----------------------------------
    # Summary Metrics
    # -----------------------------------

    total_columns = len(outlier_insights)

    columns_with_outliers = sum(
        1
        for item in outlier_insights
        if item["outlier_count"] > 0
    )

    max_outliers = max(
        item["outlier_count"]
        for item in outlier_insights
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Numerical Columns",
        total_columns,
    )

    col2.metric(
        "Columns with Outliers",
        columns_with_outliers,
    )

    col3.metric(
        "Highest Outlier Count",
        max_outliers,
    )

    st.divider()

    # -----------------------------------
    # Sort by Outlier Count
    # -----------------------------------

    outlier_insights = sorted(
        outlier_insights,
        key=lambda x: x["outlier_count"],
        reverse=True,
    )

    # -----------------------------------
    # Individual Column Insights
    # -----------------------------------

    for item in outlier_insights:

        if item["severity"] == "Low":
            icon = "🟢"

        elif item["severity"] == "Moderate":
            icon = "🟡"

        else:
            icon = "🔴"

        with st.expander(
            f"{icon} {item['column']}",
            expanded=False,
        ):

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Outliers",
                item["outlier_count"],
            )

            c2.metric(
                "Percentage",
                f"{item['percentage']}%",
            )

            c3.metric(
                "Severity",
                item["severity"],
            )

            st.write(f"**Lower Bound:** {item['lower_bound']}")
            st.write(f"**Upper Bound:** {item['upper_bound']}")
            st.write(f"**Minimum Value:** {item['minimum']}")
            st.write(f"**Maximum Value:** {item['maximum']}")

            st.success(item["recommendation"])