import streamlit as st
import plotly.figure_factory as ff
from sklearn.metrics import confusion_matrix


def show_confusion_matrix(
    y_test,
    predictions,
):
    """
    Display Confusion Matrix for classification models.
    """

    st.divider()
    st.subheader("📊 Confusion Matrix")

    cm = confusion_matrix(
        y_test,
        predictions,
    )

    labels = sorted(y_test.unique())

    fig = ff.create_annotated_heatmap(
        z=cm,
        x=labels,
        y=labels,
        colorscale="Blues",
        showscale=True,
    )

    fig.update_layout(
        xaxis_title="Predicted",
        yaxis_title="Actual",
        height=500,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )