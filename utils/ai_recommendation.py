import pandas as pd
import numpy as np


def generate_ai_recommendations(df):
    """
    Generate AI recommendations for the dataset.
    Returns:
        recommendations (list)
        quality_score (int)
    """

    recommendations = []

    recommendations.extend(check_missing_values(df))
    recommendations.extend(check_duplicates(df))
    recommendations.extend(check_constant_columns(df))
    recommendations.extend(check_high_cardinality(df))
    recommendations.extend(check_correlation(df))
    recommendations.extend(check_outliers(df))
    recommendations.extend(check_skewness(df))
    recommendations.extend(check_encoding(df))
    recommendations.extend(check_scaling(df))

    quality_score = calculate_quality_score(df, recommendations)

    return recommendations, quality_score


# ----------------------------------------------------
# Missing Values
# ----------------------------------------------------

def check_missing_values(df):
    recommendations = []

    missing_percentage = (df.isnull().sum() / len(df)) * 100

    for column, percentage in missing_percentage.items():

        if percentage > 50:
            recommendations.append({
                "type": "warning",
                "priority": "High",
                "title": f"{column} has many missing values",
                "description": f"{percentage:.1f}% of the values are missing. Consider removing the column or using an appropriate imputation technique."
            })

        elif percentage > 20:
            recommendations.append({
                "type": "info",
                "priority": "Medium",
                "title": f"{column} contains missing values",
                "description": f"{percentage:.1f}% values are missing. Imputation is recommended."
            })

    return recommendations


# ----------------------------------------------------
# Duplicate Rows
# ----------------------------------------------------

def check_duplicates(df):

    recommendations = []

    duplicate_count = df.duplicated().sum()

    if duplicate_count > 0:
        recommendations.append({
            "type": "warning",
            "priority": "High",
            "title": "Duplicate rows detected",
            "description": f"The dataset contains {duplicate_count} duplicate rows. Consider removing them."
        })

    return recommendations


# ----------------------------------------------------
# Constant Columns
# ----------------------------------------------------

def check_constant_columns(df):

    recommendations = []

    for column in df.columns:

        if df[column].nunique(dropna=False) == 1:
            recommendations.append({
                "type": "warning",
                "priority": "High",
                "title": f"{column} is constant",
                "description": "This column contains only one unique value and provides no useful information."
            })

    return recommendations


# ----------------------------------------------------
# High Cardinality
# ----------------------------------------------------

def check_high_cardinality(df):

    recommendations = []

    categorical_columns = df.select_dtypes(include=["object", "category"]).columns

    for column in categorical_columns:

        unique_values = df[column].nunique()

        if unique_values > 50:

            recommendations.append({
                "type": "info",
                "priority": "Medium",
                "title": f"{column} has high cardinality",
                "description": f"{unique_values} unique values detected. Consider target encoding, frequency encoding, or treating it as an identifier."
            })

    return recommendations


# ----------------------------------------------------
# Encoding
# ----------------------------------------------------

def check_encoding(df):

    recommendations = []

    categorical_columns = df.select_dtypes(include=["object", "category"]).columns

    if len(categorical_columns):

        recommendations.append({
            "type": "info",
            "priority": "Low",
            "title": "Categorical columns detected",
            "description": "Categorical features will require encoding before machine learning."
        })

    return recommendations


# ----------------------------------------------------
# Scaling
# ----------------------------------------------------

def check_scaling(df):

    recommendations = []

    numerical_columns = df.select_dtypes(include=np.number)

    if len(numerical_columns.columns) > 1:

        recommendations.append({
            "type": "info",
            "priority": "Low",
            "title": "Feature scaling recommended",
            "description": "Numerical features have different ranges. Consider StandardScaler or MinMaxScaler before model training."
        })

    return recommendations


# ----------------------------------------------------
# Dataset Quality Score
# ----------------------------------------------------

def calculate_quality_score(df, recommendations):

    score = 100

    high = sum(r["priority"] == "High" for r in recommendations)
    medium = sum(r["priority"] == "Medium" for r in recommendations)
    low = sum(r["priority"] == "Low" for r in recommendations)

    score -= high * 10
    score -= medium * 5
    score -= low * 2

    return max(score, 0)

# ----------------------------------------------------
# Correlation Analysis
# ----------------------------------------------------

def check_correlation(df):

    recommendations = []

    numeric_df = df.select_dtypes(include=np.number)

    # Need at least 2 numerical columns
    if numeric_df.shape[1] < 2:
        return recommendations

    correlation_matrix = numeric_df.corr().abs()

    upper_triangle = correlation_matrix.where(
        np.triu(np.ones(correlation_matrix.shape), k=1).astype(bool)
    )

    for column in upper_triangle.columns:

        high_corr = upper_triangle[column][upper_triangle[column] > 0.90]

        for correlated_column in high_corr.index:

            recommendations.append({
                "type": "warning",
                "priority": "Medium",
                "title": "Highly correlated features detected",
                "description": (
                    f"'{correlated_column}' and '{column}' have a correlation "
                    f"of {upper_triangle.loc[correlated_column, column]:.2f}. "
                    "Consider removing one of them to reduce multicollinearity."
                )
            })

    return recommendations

# ----------------------------------------------------
# Outlier Detection (IQR)
# ----------------------------------------------------

def check_outliers(df):

    recommendations = []

    numerical_columns = df.select_dtypes(include=np.number).columns

    for column in numerical_columns:

        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1

        if iqr == 0:
            continue

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        outliers = df[(df[column] < lower) | (df[column] > upper)]

        outlier_percentage = (len(outliers) / len(df)) * 100

        if outlier_percentage > 5:

            recommendations.append({
                "type": "warning",
                "priority": "Medium",
                "title": f"Outliers detected in '{column}'",
                "description": (
                    f"{outlier_percentage:.1f}% of values appear to be outliers. "
                    "Review them before model training."
                )
            })

    return recommendations
# ----------------------------------------------------
# Skewness Analysis
# ----------------------------------------------------

def check_skewness(df):

    recommendations = []

    numerical_columns = df.select_dtypes(include=np.number).columns

    for column in numerical_columns:

        skewness = df[column].dropna().skew()

        if abs(skewness) > 1:

            direction = "right" if skewness > 0 else "left"

            recommendations.append({
                "type": "info",
                "priority": "Low",
                "title": f"Skewed distribution in '{column}'",
                "description": (
                    f"The column is highly {direction}-skewed "
                    f"(skewness = {skewness:.2f}). "
                    "Consider applying a transformation before model training."
                )
            })

    return recommendations