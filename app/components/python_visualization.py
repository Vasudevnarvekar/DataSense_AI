import matplotlib.pyplot as plt
import plotly.graph_objects as go
import streamlit as st


def render_visualizations(result):
    """
    Render Plotly or Matplotlib visualizations.
    """

    # Plotly Figure
    if isinstance(result, go.Figure):
        st.plotly_chart(
            result,
            use_container_width=True,
            key=f"plotly_{id(result)}"
        )

    # Matplotlib Figure
    elif plt.get_fignums():

        fig = plt.gcf()

        st.pyplot(fig)

        # Clear the figure after displaying
        plt.close(fig)