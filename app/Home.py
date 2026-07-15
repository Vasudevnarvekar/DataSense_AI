import os
import sys

# Get the project root directory
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add it to Python's import path
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
    print(sys.path)

import streamlit as st
import pandas as pd

from utils.file_loader import load_file

st.set_page_config(
    page_title="DataSense AI",
    page_icon="📊",
    layout="wide"
)

st.title("📊 DataSense AI")
st.write("Upload a CSV or Excel file to begin analysis.")

uploaded_file = st.file_uploader(
    "Choose a file",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    df = load_file(uploaded_file)

    st.success("File uploaded successfully!")

    st.subheader("Dataset Preview")

    st.dataframe(df)

    st.subheader("Dataset Shape")

    col1, col2 = st.columns(2)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])

    st.subheader("Column Names")

    st.write(list(df.columns))

    st.subheader("Dataset Information")

info_df = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str),
    "Missing Values": df.isnull().sum().values
})

st.dataframe(info_df)

st.subheader("Missing Values Summary")

missing = df.isnull().sum()

missing = missing[missing > 0]

if len(missing) == 0:
    st.success("No missing values found.")
else:
    st.dataframe(missing)