import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px

def plot_histogram(df, column):
    """
    Generate an interactive histogram.
    """

    fig = px.histogram(
        df,
        x=column,
        nbins=30,
        title=f"Distribution of {column}",
        template="plotly_white"
    )

    fig.update_layout(
        height=500
    )

    return fig

def plot_boxplot(df, column):

    fig = px.box(
        df,
        x=column,
        title=f"Box Plot of {column}",
        template="plotly_white"
    )

    fig.update_layout(
        height=500
    )

    return fig

def plot_correlation_heatmap(df):
    """
    Generate a correlation heatmap for numerical columns.
    """

    numeric_df = df.select_dtypes(include=np.number)

    if numeric_df.shape[1] < 2:
        return None

    correlation = numeric_df.corr()

    fig, ax = plt.subplots(figsize=(8, 6))

    im = ax.imshow(correlation, cmap="coolwarm", aspect="auto")

    ax.set_xticks(range(len(correlation.columns)))
    ax.set_yticks(range(len(correlation.columns)))

    ax.set_xticklabels(correlation.columns, rotation=90)
    ax.set_yticklabels(correlation.columns)

    # Display correlation values
    for i in range(len(correlation.columns)):
        for j in range(len(correlation.columns)):
            ax.text(
                j,
                i,
                f"{correlation.iloc[i, j]:.2f}",
                ha="center",
                va="center",
                fontsize=8,
                color="black"
            )

    plt.colorbar(im)
    plt.title("Correlation Heatmap")
    plt.tight_layout()

    return fig

def plot_missing_values_heatmap(df):
    """
    Generate a heatmap showing missing values in the dataset.
    """

    missing = df.isnull()

    if missing.sum().sum() == 0:
        return None

    fig, ax = plt.subplots(figsize=(8, 2))

    im = ax.imshow(
        missing,
        aspect="auto",
        interpolation="nearest",
        cmap="Reds"
    )

    ax.set_title("Missing Values Heatmap")
    ax.set_xlabel("Columns")
    ax.set_ylabel("Rows")

    ax.set_xticks(range(len(df.columns)))
    ax.set_xticklabels(df.columns, rotation=90)

    plt.colorbar(im, label="Missing Value")
    plt.tight_layout()

    return fig
def plot_countplot(df, column):
    """
    Generate a count plot for a categorical column.
    """

    counts = df[column].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.bar(
        counts.index.astype(str),
        counts.values
    )

    ax.set_title(f"Count Plot of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Count")

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    return fig

def plot_scatter(df, x_column, y_column):

    fig = px.scatter(
        df,
        x=x_column,
        y=y_column,
        title=f"{x_column} vs {y_column}",
        template="plotly_white"
    )

    fig.update_layout(height=600)

    return fig

def plot_pie_chart(df, column):
    """
    Generate a pie chart for a categorical column.
    """

    counts = df[column].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(3, 3))

    ax.pie(
        counts.values,
        labels=counts.index.astype(str),
        autopct="%1.1f%%",
        startangle=90
    )

    ax.set_title(f"Pie Chart of {column}")

    plt.tight_layout()

    return fig