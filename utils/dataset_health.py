import pandas as pd
import streamlit as st
@st.cache_data

def calculate_dataset_health(
    df,
    correlation_insights,
    outlier_insights,
    missing_value_insights,
):
    """
    Calculate an overall dataset health score.
    """

    score = 100

    # -------------------------
    # Missing Values
    # -------------------------

    total_missing = sum(
        item["missing_count"]
        for item in missing_value_insights
    )

    missing_percentage = (
        total_missing / (df.shape[0] * df.shape[1])
    ) * 100

    score -= min(missing_percentage * 2, 25)

    # -------------------------
    # Duplicates
    # -------------------------

    duplicates = df.duplicated().sum()

    duplicate_percentage = (
        duplicates / len(df)
    ) * 100

    score -= min(duplicate_percentage * 2, 20)

    # -------------------------
    # Outliers
    # -------------------------

    avg_outlier_percentage = 0

    if outlier_insights:

        avg_outlier_percentage = sum(
            item["percentage"]
            for item in outlier_insights
        ) / len(outlier_insights)

    score -= min(avg_outlier_percentage, 20)

    # -------------------------
    # High Correlations
    # -------------------------

    strong_corr = sum(
        1
        for item in correlation_insights
        if abs(item["correlation"]) >= 0.90
    )

    score -= min(strong_corr * 2, 15)

    score = max(0, round(score))

    # -------------------------
    # Rating
    # -------------------------

    if score >= 90:
        rating = "Excellent"

    elif score >= 75:
        rating = "Good"

    elif score >= 60:
        rating = "Fair"

    else:
        rating = "Poor"

    # -------------------------
    # Recommendation
    # -------------------------

    if rating == "Excellent":

        recommendation = (
            "Dataset is ready for analysis and machine learning."
        )

    elif rating == "Good":

        recommendation = (
            "Minor preprocessing is recommended before modeling."
        )

    elif rating == "Fair":

        recommendation = (
            "Dataset requires additional cleaning before analysis."
        )

    else:

        recommendation = (
            "Significant preprocessing is required."
        )

    return {
        "score": score,
        "rating": rating,
        "duplicates": duplicates,
        "missing_percentage": round(
            missing_percentage,
            2
        ),
        "average_outlier_percentage": round(
            avg_outlier_percentage,
            2
        ),
        "strong_correlations": strong_corr,
        "recommendation": recommendation,
    }