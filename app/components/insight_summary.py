import streamlit as st


def render_executive_summary(summary: str):
    """
    Display executive summary.
    """

    st.subheader("📄 Executive Summary")

    st.success(summary)