import streamlit as st

def show_dataset_preview(df):
    """
    Display uploaded dataset preview.
    """
    st.subheader("📄 Dataset Preview")

    st.dataframe(
        df,
        use_container_width=True
    )