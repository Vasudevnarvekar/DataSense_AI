import pandas as pd
import streamlit as st
@st.cache_data

def generate_business_insights(
    df,
    correlation_insights,
    outlier_insights,
    missing_value_insights,
):
    """
    Generate high-level business insights from the dataset.
    """

    insights = []

    # -----------------------------------
    # Dataset Size
    # -----------------------------------

    insights.append(
        f"The dataset contains {df.shape[0]} records and {df.shape[1]} features."
    )

    # -----------------------------------
    # Strong Correlations
    # -----------------------------------

    strong = [
        item
        for item in correlation_insights
        if abs(item["correlation"]) >= 0.70
    ]

    for item in strong[:5]:

        if item["direction"] == "Positive":

            insights.append(
                f"{item['column_1']} and {item['column_2']} show a strong positive relationship ({item['correlation']})."
            )

        else:

            insights.append(
                f"{item['column_1']} and {item['column_2']} show a strong negative relationship ({item['correlation']})."
            )

    # -----------------------------------
    # Missing Values
    # -----------------------------------

    for item in missing_value_insights:

        if item["missing_percentage"] >= 10:

            insights.append(
                f"{item['column']} has {item['missing_percentage']}% missing values. Consider handling this column before analysis."
            )

    # -----------------------------------
    # Outliers
    # -----------------------------------

    for item in outlier_insights:

        if item["percentage"] >= 5:

            insights.append(
                f"{item['column']} contains {item['percentage']}% outliers and should be reviewed before modeling."
            )

    # -----------------------------------
    # Dominant Categories
    # -----------------------------------

    categorical = df.select_dtypes(
        include=["object", "category"]
    )

    for col in categorical.columns:

        if categorical[col].dropna().empty:
            continue

        top = categorical[col].value_counts(normalize=True).iloc[0]

        if top >= 0.80:

            value = categorical[col].mode().iloc[0]

            insights.append(
                f"'{value}' accounts for {round(top * 100,1)}% of the '{col}' column, indicating a highly dominant category."
            )

    return insights