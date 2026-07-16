import streamlit as st

from utils.data_profiler import get_ai_recommendation


def show_ai_recommendations(df):
    """
    Display AI-generated
    dataset recommendations.
    """

    st.subheader("🤖 AI Dataset Health Report")

    recommendations = get_ai_recommendation(df)

    for recommendation in recommendations:
        st.write(recommendation)