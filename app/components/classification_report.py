import pandas as pd
import streamlit as st
from sklearn.metrics import classification_report


def show_classification_report(
    y_test,
    predictions,
):
    """
    Display classification report.
    """

    st.divider()
    st.subheader("📄 Classification Report")

    report = classification_report(
        y_test,
        predictions,
        output_dict=True,
        zero_division=0,
    )

    report_df = pd.DataFrame(report).transpose()

    numeric_columns = report_df.select_dtypes(include="number").columns

    report_df[numeric_columns] = report_df[numeric_columns].round(4)

    st.dataframe(
        report_df,
        use_container_width=True,
    )