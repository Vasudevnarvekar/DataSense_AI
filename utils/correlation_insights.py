import pandas as pd
import streamlit as st

from utils.common import get_correlation_strength


@st.cache_data
def generate_correlation_insights(df: pd.DataFrame):
    """
    Generate AI insights from correlations between numerical columns.
    """

    numeric_df = df.select_dtypes(include="number")

    # Need at least two numerical columns
    if numeric_df.shape[1] < 2:
        return []

    corr_matrix = numeric_df.corr()

    insights = []
    processed = set()

    for col1 in corr_matrix.columns:
        for col2 in corr_matrix.columns:

            if col1 == col2:
                continue

            pair = tuple(sorted((col1, col2)))

            if pair in processed:
                continue

            processed.add(pair)

            corr = corr_matrix.loc[col1, col2]

            strength = get_correlation_strength(corr)

            direction = "Positive" if corr > 0 else "Negative"

            if strength == "Weak":
                insight = (
                    f"{col1} and {col2} have a weak correlation "
                    f"({corr:.2f}). The variables appear largely independent."
                )
            else:
                insight = (
                    f"{col1} and {col2} have a "
                    f"{strength.lower()} {direction.lower()} "
                    f"correlation ({corr:.2f})."
                )

            insights.append(
                {
                    "column_1": col1,
                    "column_2": col2,
                    "correlation": round(corr, 2),
                    "strength": strength,
                    "direction": direction,
                    "insight": insight,
                }
            )

    insights.sort(
        key=lambda x: abs(x["correlation"]),
        reverse=True,
    )

    return insights