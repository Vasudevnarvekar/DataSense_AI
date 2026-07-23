import streamlit as st


def show_download_section(df):
    """
    Display download section for cleaned dataset.
    """

    st.subheader("⬇️ Download Cleaned Dataset")

    rows, cols = df.shape

    col1, col2 = st.columns(2)

    col1.metric("Rows", rows)
    col2.metric("Columns", cols)

    memory_usage = df.memory_usage(deep=True).sum() / (1024 * 1024)

    st.caption(f"Dataset Size: {memory_usage:.2f} MB")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Cleaned CSV",
        data=csv,
        file_name="cleaned_dataset.csv",
        mime="text/csv",
        use_container_width=True
    )