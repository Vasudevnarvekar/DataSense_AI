import streamlit as st


def render_numerical_insights(stats, insights):
    """
    Display numerical insights.
    """

    st.subheader("📊 Numerical Insights")

    col1, col2 = st.columns(2)

    with col1:
        st.success(f"Highest Mean : **{insights['Highest Mean']}**")
        st.success(f"Highest Variance : **{insights['Highest Variance']}**")
        st.success(f"Most Skewed : **{insights['Most Skewed']}**")

    with col2:
        st.info(f"Lowest Mean : **{insights['Lowest Mean']}**")
        st.info(f"Lowest Variance : **{insights['Lowest Variance']}**")

    st.write("### Statistical Summary")

    st.dataframe(stats, use_container_width=True)