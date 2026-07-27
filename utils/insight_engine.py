import numpy as np
import pandas as pd


def get_dataset_overview(df: pd.DataFrame) -> dict:
    """
    Generate dataset overview insights.
    """

    total_rows = df.shape[0]
    total_columns = df.shape[1]

    numerical_columns = len(
        df.select_dtypes(include="number").columns
    )

    categorical_columns = len(
        df.select_dtypes(exclude="number").columns
    )

    missing_values = int(df.isnull().sum().sum())

    duplicate_rows = int(df.duplicated().sum())

    memory_usage = round(
        df.memory_usage(deep=True).sum() / (1024 * 1024),
        2
    )

    return {
        "Total Rows": total_rows,
        "Total Columns": total_columns,
        "Numerical Columns": numerical_columns,
        "Categorical Columns": categorical_columns,
        "Missing Values": missing_values,
        "Duplicate Rows": duplicate_rows,
        "Memory Usage (MB)": memory_usage
    }


def generate_overview_summary(overview: dict) -> str:
    """
    Generate a human-readable dataset summary.
    """

    summary = f"""
The uploaded dataset contains **{overview['Total Rows']:,} rows**
and **{overview['Total Columns']} columns**.

It includes **{overview['Numerical Columns']} numerical columns**
and **{overview['Categorical Columns']} categorical columns**.

There are **{overview['Missing Values']} missing values**
and **{overview['Duplicate Rows']} duplicate rows**.

The dataset occupies approximately
**{overview['Memory Usage (MB)']} MB** of memory.
"""

    return summary


def generate_numerical_insights(df: pd.DataFrame):
    """
    Generate insights for numerical columns.
    """

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        return None

    stats = numeric_df.describe().T

    stats["Variance"] = numeric_df.var()

    stats["Skewness"] = numeric_df.skew()

    insights = {
        "Highest Mean": stats["mean"].idxmax(),
        "Lowest Mean": stats["mean"].idxmin(),
        "Highest Variance": stats["Variance"].idxmax(),
        "Lowest Variance": stats["Variance"].idxmin(),
        "Most Skewed": stats["Skewness"].abs().idxmax()
    }

    return stats, insights


def generate_categorical_insights(df: pd.DataFrame):
    """
    Generate insights for categorical columns.
    """

    categorical_df = df.select_dtypes(exclude="number")

    if categorical_df.empty:
        return None

    insights = []

    for column in categorical_df.columns:

        value_counts = categorical_df[column].value_counts(
            dropna=False
        )

        insights.append({
            "Column": column,
            "Unique Values": categorical_df[column].nunique(
                dropna=False
            ),
            "Most Frequent": value_counts.index[0],
            "Frequency": int(value_counts.iloc[0]),
            "Missing Values": int(
                categorical_df[column].isnull().sum()
            )
        })

    return pd.DataFrame(insights)


def generate_correlation_insights(df: pd.DataFrame):
    """
    Generate correlation insights for numerical columns.
    """

    numeric_df = df.select_dtypes(include="number")

    # Need at least two numerical columns
    if numeric_df.shape[1] < 2:
        return None

    corr_matrix = numeric_df.corr(
        numeric_only=True
    )

    # Remove self-correlations
    corr_pairs = (
        corr_matrix.where(
            ~np.eye(
                corr_matrix.shape[0],
                dtype=bool
            )
        )
        .stack()
        .reset_index()
    )

    corr_pairs.columns = [
        "Feature 1",
        "Feature 2",
        "Correlation"
    ]

    # Remove duplicate feature pairs
    corr_pairs["Pair"] = corr_pairs.apply(
        lambda row: tuple(
            sorted(
                [
                    row["Feature 1"],
                    row["Feature 2"]
                ]
            )
        ),
        axis=1
    )

    corr_pairs = (
        corr_pairs
        .drop_duplicates("Pair")
        .drop(columns="Pair")
    )

    # Handle datasets where no valid correlations exist
    if corr_pairs.empty:
        return corr_matrix, None, None

    strongest_positive = corr_pairs.loc[
        corr_pairs["Correlation"].idxmax()
    ]

    strongest_negative = corr_pairs.loc[
        corr_pairs["Correlation"].idxmin()
    ]

    return (
        corr_matrix,
        strongest_positive,
        strongest_negative
    )
def generate_executive_summary(df: pd.DataFrame) -> str:
    """
    Generate an executive summary of the dataset.
    """

    overview = get_dataset_overview(df)

    numeric_result = generate_numerical_insights(df)

    summary = []

    summary.append(
        f"The dataset contains **{overview['Total Rows']:,} rows** "
        f"and **{overview['Total Columns']} columns**."
    )

    summary.append(
        f"It includes **{overview['Numerical Columns']} numerical** "
        f"and **{overview['Categorical Columns']} categorical** columns."
    )

    if overview["Missing Values"] == 0:
        summary.append(
            "The dataset has **no missing values**, indicating good data quality."
        )
    else:
        summary.append(
            f"The dataset contains **{overview['Missing Values']} missing values**."
        )

    if overview["Duplicate Rows"] == 0:
        summary.append(
            "No duplicate records were detected."
        )
    else:
        summary.append(
            f"The dataset contains **{overview['Duplicate Rows']} duplicate rows**."
        )

    if numeric_result:

        stats, insights = numeric_result

        summary.append(
            f"**{insights['Highest Mean']}** has the highest average value."
        )

        summary.append(
            f"**{insights['Highest Variance']}** shows the highest variability."
        )

        summary.append(
            f"**{insights['Most Skewed']}** is the most skewed numerical feature."
        )

    summary.append(
        "Overall, the dataset appears suitable for exploratory data analysis and predictive modeling."
    )

    return "\n\n".join(summary)