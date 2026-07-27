import streamlit as st


def show_column_insights(column_insights: dict):
    """
    Display AI-generated insights for each column.
    """

    st.header("🤖 AI Column Insights")

    for column, info in column_insights.items():

        with st.expander(f"📌 {column}", expanded=False):

            st.markdown(f"**Column Type:** {info.get('type', 'Unknown')}")
            st.markdown(f"**Data Type:** {info.get('dtype')}")

            col1, col2 = st.columns(2)

            col1.metric(
                "Missing Values",
                info.get("missing_values", 0)
            )

            # ----------------------------
            # Numerical
            # ----------------------------

            if info.get("type") == "Numerical":

                col2.metric(
                    "Outliers",
                    info.get("outliers", 0)
                )

                m1, m2, m3 = st.columns(3)

                m1.metric("Mean", info.get("mean"))
                m2.metric("Median", info.get("median"))
                m3.metric("Std Dev", info.get("std"))

                st.write(f"**Minimum:** {info.get('minimum')}")
                st.write(f"**Maximum:** {info.get('maximum')}")
                st.write(f"**Distribution:** {info.get('distribution')}")
                st.write(f"**Skewness:** {info.get('skewness')}")

            # ----------------------------
            # Categorical
            # ----------------------------

            elif info.get("type") == "Categorical":

                col2.metric(
                    "Unique Values",
                    info.get("unique_values", 0)
                )

                st.write(
                    f"**Most Common:** {info.get('most_common')}"
                )

                st.write(
                    f"**Frequency:** {info.get('frequency')}"
                )

            # ----------------------------
            # Datetime
            # ----------------------------

            elif info.get("type") == "Datetime":

                st.write(
                    f"**Start Date:** {info.get('start_date')}"
                )

                st.write(
                    f"**End Date:** {info.get('end_date')}"
                )

                st.write(
                    f"**Duration:** {info.get('duration_days')} days"
                )

            st.divider()

            st.success(info.get("insight", "No insight available."))