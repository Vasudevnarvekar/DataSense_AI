import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import matplotlib.figure


def render_python_output(success, output, result):
    """
    Display Python execution output except charts.
    """

    if not success:
        st.error("❌ Error while executing Python code")
        st.code(output)
        return

    st.success("✅ Python Code Executed Successfully")

    if output:
        st.code(output)

    if result is None:
        return

    # Don't render charts here
    if isinstance(result, (go.Figure, matplotlib.figure.Figure)):
        return

    if isinstance(result, pd.DataFrame):
        st.dataframe(result, use_container_width=True)

    elif isinstance(result, pd.Series):
        st.dataframe(result)

    else:
        st.write(result)