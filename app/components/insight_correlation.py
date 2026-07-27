import streamlit as st


def render_correlation_insights(
    corr_matrix,
    strongest_positive,
    strongest_negative
):
    """
    Display correlation insights.
    """

    st.subheader("🔗 Correlation Insights")

    # ---------------------------------------------------
    # Handle datasets with insufficient correlation data
    # ---------------------------------------------------

    if strongest_positive is None or strongest_negative is None:

        st.info(
            "Not enough numerical data is available to generate correlation insights."
        )

        st.write("### Correlation Matrix")

        st.dataframe(
            corr_matrix,
            use_container_width=True
        )

        return

    # ---------------------------------------------------
    # Strongest Correlations
    # ---------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.success(
            f"""
### Strongest Positive Correlation

**Feature 1:** {strongest_positive['Feature 1']}

**Feature 2:** {strongest_positive['Feature 2']}

**Correlation:** {strongest_positive['Correlation']:.3f}
"""
        )

    with col2:

        st.info(
            f"""
### Strongest Negative Correlation

**Feature 1:** {strongest_negative['Feature 1']}

**Feature 2:** {strongest_negative['Feature 2']}

**Correlation:** {strongest_negative['Correlation']:.3f}
"""
        )

    # ---------------------------------------------------
    # Correlation Matrix
    # ---------------------------------------------------

    st.write("### 📊 Correlation Matrix")

    st.dataframe(
        corr_matrix,
        use_container_width=True
    )