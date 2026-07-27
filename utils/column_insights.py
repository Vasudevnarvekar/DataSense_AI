import pandas as pd
import streamlit as st
@st.cache_data

def generate_column_insights(df: pd.DataFrame):
    """
    Generate AI-style insights for every column in the dataset.

    Returns:
        dict
            {
                column_name: {
                    ...
                }
            }
    """

    insights = {}

    for column in df.columns:

        series = df[column]

        info = {
            "dtype": str(series.dtype),
            "missing_values": int(series.isna().sum())
        }

        # =====================================================
        # Numerical Columns
        # =====================================================

        if pd.api.types.is_numeric_dtype(series):

            clean = series.dropna()

            if len(clean) > 0:

                q1 = clean.quantile(0.25)
                q3 = clean.quantile(0.75)

                iqr = q3 - q1

                lower = q1 - 1.5 * iqr
                upper = q3 + 1.5 * iqr

                outliers = clean[(clean < lower) | (clean > upper)]

                skew = clean.skew()

                if skew > 1:
                    distribution = "Highly Right Skewed"
                elif skew > 0.5:
                    distribution = "Slightly Right Skewed"
                elif skew < -1:
                    distribution = "Highly Left Skewed"
                elif skew < -0.5:
                    distribution = "Slightly Left Skewed"
                else:
                    distribution = "Approximately Symmetric"

                info.update({
                    "type": "Numerical",
                    "mean": round(clean.mean(), 2),
                    "median": round(clean.median(), 2),
                    "std": round(clean.std(), 2),
                    "minimum": round(clean.min(), 2),
                    "maximum": round(clean.max(), 2),
                    "distribution": distribution,
                    "skewness": round(skew, 2),
                    "outliers": len(outliers)
                })

                insight = (
                    f"{column} has an average value of "
                    f"{round(clean.mean(),2)}. "
                    f"The distribution is {distribution.lower()} "
                    f"with {len(outliers)} detected outlier(s)."
                )

                info["insight"] = insight

        # =====================================================
        # Datetime Columns
        # =====================================================

        elif pd.api.types.is_datetime64_any_dtype(series):

            clean = series.dropna()

            if len(clean) > 0:

                start = clean.min()
                end = clean.max()

                info.update({
                    "type": "Datetime",
                    "start_date": str(start.date()),
                    "end_date": str(end.date()),
                    "duration_days": int((end - start).days)
                })

                info["insight"] = (
                    f"Data ranges from "
                    f"{start.date()} to {end.date()}."
                )

        # =====================================================
        # Categorical Columns
        # =====================================================

        else:

            clean = series.dropna()

            unique = clean.nunique()

            if unique > 0:

                top = clean.mode().iloc[0]
                freq = int(clean.value_counts().iloc[0])

                info.update({
                    "type": "Categorical",
                    "unique_values": unique,
                    "most_common": str(top),
                    "frequency": freq
                })

                info["insight"] = (
                    f"The most frequent value is "
                    f"'{top}', appearing {freq} times."
                )

        insights[column] = info

    return insights