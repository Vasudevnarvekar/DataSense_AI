import streamlit as st

from app.components.python_examples import SAMPLE_CODES


def render_python_editor():
    """
    Render the Python code editor and
    return the user's code.
    """

    st.subheader("🐍 Python Code Editor")

    selected_code = st.selectbox(
        "Choose Sample Python Code",
        list(SAMPLE_CODES.keys())
    )

    code = st.text_area(
        "Python Code",
        value=SAMPLE_CODES[selected_code],
        height=250
    )

    return code