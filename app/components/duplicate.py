import streamlit as st


def show_duplicate_info(df):
    """
    Display duplicate information and remove duplicates.
    """

    st.subheader("🔁 Duplicate Detection")

    # Calculate duplicate information
    duplicate_rows = df.duplicated().sum()
    total_rows = len(df)

    duplicate_percentage = (
        round((duplicate_rows / total_rows) * 100, 2)
        if total_rows > 0 else 0
    )

    # Display metrics
    col1, col2 = st.columns(2)

    col1.metric("Duplicate Rows", duplicate_rows)
    col2.metric("Duplicate %", f"{duplicate_percentage}%")

    # If no duplicates exist
    if duplicate_rows == 0:
        st.success("✅ No duplicate rows found.")
        return df

    # Show warning
    st.warning(f"⚠️ {duplicate_rows} duplicate rows detected.")

    # Remove duplicate rows
    if st.button("🗑 Remove Duplicate Rows", key="remove_duplicates"):

        before_rows = len(df)

        # Remove duplicates
        df = df.drop_duplicates().reset_index(drop=True)

        removed_rows = before_rows - len(df)

        # Update session state
        st.session_state["cleaned_df"] = df

        # Success message
        st.success(f"✅ Removed {removed_rows} duplicate rows.")

        # Refresh the page
        st.rerun()

    return df