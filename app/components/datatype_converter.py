import streamlit as st
import pandas as pd


def show_datatype_converter(df):
    """
    Convert dataframe column data types.
    """

    st.subheader("🔄 Data Type Conversion")

    # Display current data types
    dtype_df = pd.DataFrame({
        "Column": df.columns,
        "Current Data Type": df.dtypes.astype(str)
    })

    st.dataframe(dtype_df, use_container_width=True)

    # Select column
    selected_column = st.selectbox(
        "Select Column",
        df.columns,
        key="datatype_column"
    )

    # Target datatype
    target_dtype = st.selectbox(
        "Convert To",
        [
            "string",
            "int64",
            "float64",
            "category",
            "datetime"
        ],
        key="datatype_target"
    )

    # Apply conversion
    if st.button(
        "Apply Data Type Conversion",
        key="datatype_button"
    ):

        try:

            if target_dtype == "datetime":
                df[selected_column] = pd.to_datetime(
                    df[selected_column],
                    errors="coerce"
                )

            else:
                df[selected_column] = df[selected_column].astype(target_dtype)

            st.session_state["cleaned_df"] = df

            st.success(
                f"✅ '{selected_column}' converted to {target_dtype}."
            )

            st.rerun()

        except Exception as e:

            st.error(f"❌ Conversion failed: {e}")

    return df