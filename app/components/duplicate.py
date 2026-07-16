import streamlit as st
def show_duplicate_info(df):
    
    st.subheader("🔁 Duplicate Detection")

    duplicate_info = get_duplicate_info(df)

    col1, col2 = st.columns(2)

    col1.metric(
        "Duplicate Rows",
        duplicate_info["duplicate_rows"]
    )

    col2.metric(
        "Duplicate %",
        f"{duplicate_info['duplicate_percentage']}%"
    )

    if duplicate_info["duplicate_rows"] == 0:
        st.success("No duplicate rows found.")
    else:
        st.warning(
            f"{duplicate_info['duplicate_rows']} duplicate rows detected."
        )
