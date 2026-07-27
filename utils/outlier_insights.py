import pandas as pd
import streamlit as st

from utils.common import (
    calculate_percentage,
    get_outlier_severity,
)


@st.cache_data
def generate_outlier_insights(df: pd.DataFrame):
    """
    Generate outlier analysis for all numerical columns.
    """

    insights = []

    numerical_columns = df.select_dtypes(include="number").columns

    for column in numerical_columns:

        series = df[column].dropna()

        if series.empty:
            continue

        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)

        iqr = q3 - q1

        lower_bound = q1 - (1.5 * iqr)
        upper_bound = q3 + (1.5 * iqr)

        outliers = series[
            (series < lower_bound)
            | (series > upper_bound)
        ]

        outlier_count = len(outliers)

        percentage = calculate_percentage(
            outlier_count,
            len(series)
        )

        severity = get_outlier_severity(percentage)

        # AI Recommendation
        if severity == "Low":

            recommendation = (
                "No significant outliers detected."
            )

        elif severity == "Moderate":

            recommendation = (
                "A few outliers are present. Review them before removing."
            )

        else:

            recommendation = (
                "High number of outliers detected. Consider capping, transformation, or investigating data quality before modeling."
            )

        insights.append(
            {
                "column": column,
                "outlier_count": outlier_count,
                "percentage": percentage,
                "severity": severity,
                "lower_bound": round(lower_bound, 2),
                "upper_bound": round(upper_bound, 2),
                "minimum": round(series.min(), 2),
                "maximum": round(series.max(), 2),
                "recommendation": recommendation,
            }
        )

    return insights