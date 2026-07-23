import streamlit as st
import pandas as pd


def show_outlier_detection(df):
    """
    Detect and remove outliers using the IQR method.
    """

    st.subheader("📊 Outlier Detection")

    # Get numeric columns
    numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()

    if not numeric_columns:
        st.info("No numeric columns available for outlier detection.")
        return df

    # Select column
    selected_column = st.selectbox(
        "Select Numeric Column",
        numeric_columns,
        key="outlier_column"
    )

    # Calculate IQR
    Q1 = df[selected_column].quantile(0.25)
    Q3 = df[selected_column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - (1.5 * IQR)
    upper_bound = Q3 + (1.5 * IQR)

    outlier_mask = (
        (df[selected_column] < lower_bound) |
        (df[selected_column] > upper_bound)
    )

    outlier_count = outlier_mask.sum()

    col1, col2 = st.columns(2)

    col1.metric("Outliers", outlier_count)
    col2.metric("Column", selected_column)

    if outlier_count == 0:
        st.success("✅ No outliers detected.")
        return df

    st.warning(f"⚠️ {outlier_count} outliers detected.")

    # Show bounds (optional but useful)
    with st.expander("View Detection Details"):
        st.write(f"Lower Bound: **{lower_bound:.2f}**")
        st.write(f"Upper Bound: **{upper_bound:.2f}**")

    # Remove button
    if st.button(
        "🗑 Remove Outliers",
        key="remove_outliers"
    ):

        before_rows = len(df)

        df = df[~outlier_mask].reset_index(drop=True)

        removed_rows = before_rows - len(df)

        st.session_state["cleaned_df"] = df

        st.success(
            f"✅ Removed {removed_rows} outlier rows."
        )

        st.rerun()

    return df