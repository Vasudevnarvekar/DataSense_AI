import streamlit as st
import pandas as pd

from utils.data_profiler import detect_schema


def show_schema(df):
    """
    Display schema, column names and dataset information.
    """

    # ===================================================
    # Schema Detection
    # ===================================================

    st.subheader("🧠 Schema Detection")

    schema = detect_schema(df)

    schema_df = pd.DataFrame({
        "Column": list(schema.keys()),
        "Detected Type": list(schema.values())
    })

    st.dataframe(
        schema_df,
        use_container_width=True
    )

    # ===================================================
    # Column Names
    # ===================================================

    st.subheader("📌 Column Names")

    st.write(list(df.columns))

    # ===================================================
    # Dataset Information
    # ===================================================

    st.subheader("📋 Dataset Information")

    info_df = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str),
        "Missing Values": df.isnull().sum().values
    })

    st.dataframe(
        info_df,
        use_container_width=True
    )