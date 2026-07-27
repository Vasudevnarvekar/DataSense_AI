import streamlit as st


def show_ai_summary(insights: dict):
    """
    Display high-level AI-generated dataset insights.
    """

    st.subheader("🤖 AI Dataset Summary")

    # ----------------------------
    # Basic Metrics
    # ----------------------------
    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", f"{insights['rows']:,}")
    col2.metric("Columns", insights["columns"])
    col3.metric("Memory Usage", f"{insights['memory_usage_mb']} MB")

    st.divider()

    # ----------------------------
    # Column Information
    # ----------------------------
    st.markdown("### 📊 Column Information")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Numerical",
        len(insights["numerical_columns"])
    )

    c2.metric(
        "Categorical",
        len(insights["categorical_columns"])
    )

    c3.metric(
        "Datetime",
        len(insights["datetime_columns"])
    )

    st.divider()

    # ----------------------------
    # Missing Values
    # ----------------------------
    with st.expander("🟡 Missing Values"):

        if insights["missing_columns"]:
            st.dataframe(
                insights["missing_columns"],
                use_container_width=True
            )
        else:
            st.success("No missing values found.")

    # ----------------------------
    # Duplicate Rows
    # ----------------------------
    with st.expander("🔁 Duplicate Rows"):

        duplicates = insights["duplicate_rows"]

        if duplicates:
            st.warning(f"{duplicates} duplicate rows found.")
        else:
            st.success("No duplicate rows found.")

    # ----------------------------
    # Constant Columns
    # ----------------------------
    with st.expander("📌 Constant Columns"):

        if insights["constant_columns"]:
            st.write(insights["constant_columns"])
        else:
            st.success("No constant columns found.")

    # ----------------------------
    # High Cardinality
    # ----------------------------
    with st.expander("🧩 High Cardinality Columns"):

        if insights["high_cardinality_columns"]:
            st.write(insights["high_cardinality_columns"])
        else:
            st.success("No high-cardinality columns found.")

    # ----------------------------
    # AI Recommendations
    # ----------------------------
    st.markdown("### 💡 AI Recommendations")

    if insights["recommendations"]:

        for rec in insights["recommendations"]:
            st.info(rec)

    else:
        st.success("No recommendations. Dataset looks clean!")