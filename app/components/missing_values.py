import streamlit as st
import pandas as pd


def show_missing_values(df):
    """
    Display and handle missing values.
    """

    st.subheader("📝 Missing Value Handling")

    # ----------------------------
    # Missing value summary
    # ----------------------------

    total_missing = df.isna().sum().sum()

    missing_percentage = (
        round((total_missing / (df.shape[0] * df.shape[1])) * 100, 2)
        if df.size > 0 else 0
    )

    col1, col2 = st.columns(2)

    col1.metric("Total Missing Values", total_missing)
    col2.metric("Missing %", f"{missing_percentage}%")

    if total_missing == 0:
        st.success("✅ No missing values found.")
        return df

    # ----------------------------
    # Missing values by column
    # ----------------------------

    missing_columns = df.columns[df.isna().any()].tolist()

    st.write("### Columns with Missing Values")

    summary = pd.DataFrame({
        "Column": missing_columns,
        "Missing Values": [
            df[col].isna().sum()
            for col in missing_columns
        ]
    })

    st.dataframe(summary, use_container_width=True)

    # ----------------------------
    # Select column
    # ----------------------------

    selected_column = st.selectbox(
        "Select Column",
        missing_columns
    )

    # ----------------------------
    # Cleaning Method
    # ----------------------------

    method = st.selectbox(
        "Handling Method",
        [
            "Mean",
            "Median",
            "Mode",
            "Custom Value",
            "Drop Rows"
        ]
    )

    custom_value = None

    if method == "Custom Value":
        custom_value = st.text_input("Enter Custom Value")

    # ----------------------------
    # Apply Button
    # ----------------------------

    if st.button(
        "Apply Missing Value Handling",
        key="missing_button"
    ):

        if method == "Mean":
            df[selected_column] = df[selected_column].fillna(
                df[selected_column].mean()
            )

        elif method == "Median":
            df[selected_column] = df[selected_column].fillna(
                df[selected_column].median()
            )

        elif method == "Mode":
            df[selected_column] = df[selected_column].fillna(
                df[selected_column].mode()[0]
            )

        elif method == "Custom Value":
            df[selected_column] = df[selected_column].fillna(
                custom_value
            )

        elif method == "Drop Rows":
            df = df.dropna(subset=[selected_column])

        st.session_state["cleaned_df"] = df

        st.success("✅ Missing values handled successfully.")

        st.rerun()

    return df