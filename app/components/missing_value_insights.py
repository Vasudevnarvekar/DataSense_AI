import streamlit as st


def show_missing_value_insights(missing_value_insights):
    """
    Display AI-generated missing value insights.
    """

    st.header("🩹 Missing Value Intelligence")

    if not missing_value_insights:
        st.success("🎉 No missing values detected in the dataset.")
        return

    # ---------------------------------------
    # Summary Metrics
    # ---------------------------------------

    total_columns = len(missing_value_insights)

    total_missing = sum(
        item["missing_count"] for item in missing_value_insights
    )

    max_missing = max(
        item["missing_percentage"]
        for item in missing_value_insights
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Affected Columns", total_columns)
    col2.metric("Total Missing Values", total_missing)
    col3.metric("Highest Missing %", f"{max_missing}%")

    st.divider()

    # ---------------------------------------
    # Sort by Missing Percentage
    # ---------------------------------------

    missing_value_insights = sorted(
        missing_value_insights,
        key=lambda x: x["missing_percentage"],
        reverse=True
    )

    # ---------------------------------------
    # Column-wise Insights
    # ---------------------------------------

    for item in missing_value_insights:

        percentage = item["missing_percentage"]

        if percentage < 5:
            icon = "🟢"
            severity = "Low"

        elif percentage < 20:
            icon = "🟡"
            severity = "Medium"

        else:
            icon = "🔴"
            severity = "High"

        with st.expander(
            f"{icon} {item['column']}",
            expanded=False
        ):

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Missing Values",
                item["missing_count"]
            )

            c2.metric(
                "Missing %",
                f"{percentage}%"
            )

            c3.metric(
                "Severity",
                severity
            )

            st.write(f"**Data Type:** {item['dtype']}")

            st.write(
                f"**Recommended Strategy:** {item['strategy']}"
            )

            st.info(item["reason"])