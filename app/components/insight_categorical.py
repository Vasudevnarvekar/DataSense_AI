import streamlit as st


def render_categorical_insights(df):
    """
    Display categorical insights.
    """

    st.subheader("🗂️ Categorical Insights")

    st.dataframe(
        df,
        use_container_width=True
    )