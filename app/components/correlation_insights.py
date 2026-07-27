import streamlit as st


def show_correlation_insights(correlation_insights):
    """
    Display AI-generated correlation insights.
    """

    st.header("📊 Correlation Intelligence")

    if not correlation_insights:
        st.info("Not enough numerical columns to perform correlation analysis.")
        return

    # -------------------------------------
    # Filter by Strength
    # -------------------------------------

    filter_option = st.selectbox(
        "Filter by Correlation Strength",
        ["All", "Strong", "Moderate", "Weak"],
        key="correlation_filter",
    )

    if filter_option == "All":
        filtered = correlation_insights
    else:
        filtered = [
            item
            for item in correlation_insights
            if item["strength"] == filter_option
        ]

    st.write(f"Showing **{len(filtered)}** correlation pairs.")

    st.divider()

    # -------------------------------------
    # Display Insights
    # -------------------------------------

    for item in filtered:

        if item["strength"] == "Strong":
            icon = "🟢"
        elif item["strength"] == "Moderate":
            icon = "🟡"
        else:
            icon = "⚪"

        with st.expander(
            f"{icon} {item['column_1']} ↔ {item['column_2']}",
            expanded=False,
        ):

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Correlation",
                item["correlation"],
            )

            col2.metric(
                "Strength",
                item["strength"],
            )

            col3.metric(
                "Direction",
                item["direction"],
            )

            st.success(item["insight"])