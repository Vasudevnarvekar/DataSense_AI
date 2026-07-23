import streamlit as st

# Cleaning Components
from app.components.duplicate import show_duplicate_info
from app.components.missing_values import show_missing_values
from app.components.datatype_converter import show_datatype_converter
from app.components.outliers import show_outlier_detection
from app.components.download import show_download_section


def show_cleaning_dashboard():
    """
    Main Data Cleaning Dashboard
    """

    st.title("🧹 Data Cleaning Dashboard")

    # Check whether dataset is uploaded
    if "df" not in st.session_state:
        st.warning("Please upload a dataset first.")
        return

    # Original uploaded dataset
    df = st.session_state["df"]

    # Working copy used for cleaning
    cleaned_df = st.session_state.get("cleaned_df", df.copy())

    st.markdown("---")

    # ----------------------------
    # Duplicate Detection
    # ----------------------------
    cleaned_df = show_duplicate_info(cleaned_df)

    st.markdown("---")

    # ----------------------------
    # Missing Values
    # ----------------------------
    cleaned_df = show_missing_values(cleaned_df)

    st.markdown("---")

    # ----------------------------
    # Data Type Conversion
    # ----------------------------
    cleaned_df = show_datatype_converter(cleaned_df)

    st.markdown("---")

    # ----------------------------
    # Outlier Detection
    # ----------------------------
    cleaned_df = show_outlier_detection(cleaned_df)

    st.markdown("---")

    # Save cleaned dataframe
    st.session_state["cleaned_df"] = cleaned_df

    # Download Section
    show_download_section(cleaned_df)