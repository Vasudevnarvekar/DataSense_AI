import pandas as pd
import streamlit as st
@st.cache_data

def generate_dataset_insights(df: pd.DataFrame):
    """
    Generate high-level insights about the dataset.
    Returns a dictionary containing summary statistics and recommendations.
    """

    insights = {}

    # ----------------------------
    # Basic Information
    # ----------------------------
    insights["rows"] = df.shape[0]
    insights["columns"] = df.shape[1]

    insights["memory_usage_mb"] = round(
        df.memory_usage(deep=True).sum() / (1024 ** 2), 2
    )

    # ----------------------------
    # Column Types
    # ----------------------------
    numerical_cols = df.select_dtypes(include="number").columns.tolist()

    categorical_cols = df.select_dtypes(
        include=["object", "category", "bool"]
    ).columns.tolist()

    datetime_cols = df.select_dtypes(
        include=["datetime64[ns]", "datetimetz"]
    ).columns.tolist()

    insights["numerical_columns"] = numerical_cols
    insights["categorical_columns"] = categorical_cols
    insights["datetime_columns"] = datetime_cols

    # ----------------------------
    # Missing Values
    # ----------------------------
    missing = df.isnull().sum()

    insights["missing_columns"] = {
        col: int(count)
        for col, count in missing.items()
        if count > 0
    }

    insights["total_missing"] = int(missing.sum())

    # ----------------------------
    # Duplicate Rows
    # ----------------------------
    insights["duplicate_rows"] = int(df.duplicated().sum())

    # ----------------------------
    # Constant Columns
    # ----------------------------
    constant_columns = [
        col
        for col in df.columns
        if df[col].nunique(dropna=False) <= 1
    ]

    insights["constant_columns"] = constant_columns

    # ----------------------------
    # High Cardinality Columns
    # ----------------------------
    high_cardinality = []

    for col in categorical_cols:
        if df[col].nunique() > 50:
            high_cardinality.append(col)

    insights["high_cardinality_columns"] = high_cardinality

    # ----------------------------
    # Recommendations
    # ----------------------------
    recommendations = []

    if insights["duplicate_rows"] > 0:
        recommendations.append(
            "Remove duplicate rows before further analysis."
        )

    if insights["total_missing"] > 0:
        recommendations.append(
            "Handle missing values using suitable imputation techniques."
        )

    if constant_columns:
        recommendations.append(
            "Consider removing constant columns."
        )

    if high_cardinality:
        recommendations.append(
            "High-cardinality categorical columns may require special encoding."
        )

    insights["recommendations"] = recommendations

    return insights