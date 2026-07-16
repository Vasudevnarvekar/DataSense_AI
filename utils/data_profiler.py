import pandas as pd


def get_dataset_overview(df: pd.DataFrame) -> dict:
    """
    Generate basic dataset information.
    """

    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "total_cells": df.shape[0] * df.shape[1],
        "memory_usage_mb": round(
            df.memory_usage(deep=True).sum() / (1024 * 1024),
            2
        )
    }

def detect_schema(df: pd.DataFrame) -> dict:
    """
    Detect column types.
    """

    schema = {}

    for column in df.columns:

        dtype = df[column].dtype

        if pd.api.types.is_numeric_dtype(dtype):
            schema[column] = "Numerical"

        elif pd.api.types.is_datetime64_any_dtype(dtype):
            schema[column] = "Datetime"

        elif pd.api.types.is_bool_dtype(dtype):
            schema[column] = "Boolean"

        else:

            unique_ratio = (
                df[column].nunique() /
                len(df)
            )

            if unique_ratio < 0.05:
                schema[column] = "Categorical"
            else:
                schema[column] = "Text"

    return schema

def get_duplicate_info(df):
    """
    Returns duplicate row information.
    """

    duplicate_count = df.duplicated().sum()

    return {
        "duplicate_rows": duplicate_count,
        "duplicate_percentage": round(
            (duplicate_count / len(df)) * 100,
            2
        )
    }
def get_statistical_summary(df):
    """
    Returns descriptive statistics for numerical columns only.
    """

    numeric_df = df.select_dtypes(include=["number"])

    if numeric_df.empty:
        return None

    return numeric_df.describe().transpose()
def get_data_quality_report(df):
    """
    Generate a basic data quality report.
    """

    total_rows = len(df)
    total_columns = len(df.columns)

    total_missing = df.isnull().sum().sum()

    total_cells = total_rows * total_columns

    missing_percentage = round(
        (total_missing / total_cells) * 100,
        2
    )

    duplicate_rows = df.duplicated().sum()

    duplicate_percentage = round(
        (duplicate_rows / total_rows) * 100,
        2
    )

    numerical_columns = len(
        df.select_dtypes(include="number").columns
    )

    categorical_columns = len(
        df.select_dtypes(include=["object", "category"]).columns
    )

    # Basic Quality Score
    quality_score = max(
        0,
        round(
            100
            - missing_percentage
            - duplicate_percentage,
            2,
        ),
    )

    return {
        "Total Missing": total_missing,
        "Missing %": missing_percentage,
        "Duplicate Rows": duplicate_rows,
        "Duplicate %": duplicate_percentage,
        "Numerical Columns": numerical_columns,
        "Categorical Columns": categorical_columns,
        "Quality Score": quality_score,
    }
def get_column_profile(df):
    """
    Generate profile for every column.
    """

    profile = []

    for col in df.columns:

        profile.append({

            "Column": col,

            "Data Type": str(df[col].dtype),

            "Missing Values": df[col].isnull().sum(),

            "Unique Values": df[col].nunique(),

            "Memory (KB)": round(
                df[col].memory_usage(deep=True) / 1024,
                2
            )
        })

    return pd.DataFrame(profile)
def get_ai_recommendation(df):
    """
    Generate AI-based recommendation about dataset quality.
    """

    missing = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()

    recommendations = []

    if missing == 0:
        recommendations.append("✅ No missing values detected.")
    else:
        recommendations.append(
            f"⚠️ {missing} missing values detected. Data cleaning is recommended."
        )

    if duplicates == 0:
        recommendations.append("✅ No duplicate rows found.")
    else:
        recommendations.append(
            f"⚠️ {duplicates} duplicate rows detected. Consider removing duplicates."
        )

    numeric_cols = len(df.select_dtypes(include="number").columns)

    if numeric_cols == 0:
        recommendations.append(
            "⚠️ No numerical columns available for statistical analysis."
        )
    else:
        recommendations.append(
            f"✅ {numeric_cols} numerical columns detected."
        )

    return recommendations