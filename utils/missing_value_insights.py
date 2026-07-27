import pandas as pd
import streamlit as st
@st.cache_data

def generate_missing_value_insights(df: pd.DataFrame):
    """
    Generate AI recommendations for handling missing values.
    """

    insights = []

    total_rows = len(df)

    for column in df.columns:

        missing = int(df[column].isna().sum())

        if missing == 0:
            continue

        percentage = round((missing / total_rows) * 100, 2)

        dtype = str(df[column].dtype)

        # ----------------------------
        # Numerical Columns
        # ----------------------------

        if pd.api.types.is_numeric_dtype(df[column]):

            skew = df[column].dropna().skew()

            if abs(skew) < 0.5:
                strategy = "Mean Imputation"
                reason = (
                    "The data is approximately symmetric, "
                    "so the mean is an appropriate choice."
                )

            else:
                strategy = "Median Imputation"
                reason = (
                    "The data is skewed or may contain outliers, "
                    "so the median is more robust."
                )

        # ----------------------------
        # Datetime Columns
        # ----------------------------

        elif pd.api.types.is_datetime64_any_dtype(df[column]):

            strategy = "Forward Fill"
            reason = (
                "Datetime columns often represent sequential data, "
                "making forward fill a reasonable default."
            )

        # ----------------------------
        # Categorical Columns
        # ----------------------------

        else:

            strategy = "Mode Imputation"
            reason = (
                "Categorical values are typically best filled "
                "using the most frequent category."
            )

        insights.append({

            "column": column,

            "missing_count": missing,

            "missing_percentage": percentage,

            "dtype": dtype,

            "strategy": strategy,

            "reason": reason

        })

    return insights