import streamlit as st


def show_business_insights(business_insights):
    """
    Display AI-generated business insights.
    """

    st.header("💼 Business Insights")

    if not business_insights:
        st.info("No business insights could be generated.")
        return

    st.metric("Total Insights", len(business_insights))

    st.divider()

    for i, insight in enumerate(business_insights, start=1):

        if "strong" in insight.lower():
            icon = "📈"

        elif "missinyg" in insight.lower():
            icon = "⚠️"

        elif "outlier" in insight.lower():
            icon = "🚨"

        elif "dominant" in insight.lower():
            icon = "👥"

        else:
            icon = "💡"

        st.info(f"**Insight {i}**\n\n{icon} {insight}")