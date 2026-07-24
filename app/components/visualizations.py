import streamlit as st

from utils.visualization import (
    plot_histogram,
    plot_boxplot,
    plot_correlation_heatmap,
    plot_missing_values_heatmap,
    plot_countplot,
    plot_scatter,
    plot_pie_chart
)


if "selected_chart" not in st.session_state:
    st.session_state.selected_chart = "Histogram"


def show_visualizations(df):

    st.header("📊 Visualization Dashboard")
    st.caption("Click a visualization card to open it in full size.")

    # ---------------------------------------
    # Dashboard Cards
    # ---------------------------------------

    row1 = st.columns(3)

    with row1[0]:
        st.info("📈 Histogram")
        if st.button("Open", key="hist", use_container_width=True):
            st.session_state.selected_chart = "Histogram"

    with row1[1]:
        st.info("📦 Box Plot")
        if st.button("Open", key="box", use_container_width=True):
            st.session_state.selected_chart = "Box Plot"

    with row1[2]:
        st.info("🔥 Correlation Heatmap")
        if st.button("Open", key="corr", use_container_width=True):
            st.session_state.selected_chart = "Correlation"

    row2 = st.columns(3)

    with row2[0]:
        st.info("📉 Scatter Plot")
        if st.button("Open", key="scatter", use_container_width=True):
            st.session_state.selected_chart = "Scatter"

    with row2[1]:
        st.info("🥧 Pie Chart")
        if st.button("Open", key="pie", use_container_width=True):
            st.session_state.selected_chart = "Pie"

    with row2[2]:
        st.info("📊 Count Plot")
        if st.button("Open", key="count", use_container_width=True):
            st.session_state.selected_chart = "Count"

    st.info("🧩 Missing Values Heatmap")

    if st.button("Open", key="missing", use_container_width=True):
        st.session_state.selected_chart = "Missing"

    st.divider()

    # ---------------------------------------
    # Selected Visualization
    # ---------------------------------------

    st.subheader(f"📌 {st.session_state.selected_chart}")

    numeric_columns = df.select_dtypes(include="number").columns
    categorical_columns = df.select_dtypes(include=["object", "category"]).columns

    # Histogram
    if st.session_state.selected_chart == "Histogram":

        if len(numeric_columns) == 0:
            st.info("No numerical columns available.")
            return

        column = st.selectbox(
            "Select Numerical Column",
            numeric_columns,
            key="hist_col"
        )

        st.plotly_chart(
            plot_histogram(df, column),
            use_container_width=True
        )

    # Box Plot
    elif st.session_state.selected_chart == "Box Plot":

        if len(numeric_columns) == 0:
            st.info("No numerical columns available.")
            return

        column = st.selectbox(
            "Select Numerical Column",
            numeric_columns,
            key="box_col"
        )

        st.plotly_chart(
            plot_boxplot(df, column),
            use_container_width=True
          )

    # Correlation Heatmap
    elif st.session_state.selected_chart == "Correlation":

        fig = plot_correlation_heatmap(df)

        if fig:
            st.pyplot(fig)
        else:
            st.info("At least two numerical columns are required.")

    # Scatter Plot
    elif st.session_state.selected_chart == "Scatter":

        if len(numeric_columns) < 2:
            st.info("At least two numerical columns are required.")
            return

        col1, col2 = st.columns(2)

        with col1:
            x = st.selectbox(
                "X Axis",
                numeric_columns,
                key="scatter_x"
            )

        with col2:
            y = st.selectbox(
                "Y Axis",
                numeric_columns,
                index=1,
                key="scatter_y"
            )

        st.plotly_chart(
            plot_scatter(df, column),
            use_container_width=True
        )

    # Pie Chart
    elif st.session_state.selected_chart == "Pie":

        if len(categorical_columns) == 0:
            st.info("No categorical columns available.")
            return

        column = st.selectbox(
            "Select Categorical Column",
            categorical_columns,
            key="pie_col"
        )

        st.pyplot(plot_pie_chart(df, column))

    # Count Plot
    elif st.session_state.selected_chart == "Count":

        if len(categorical_columns) == 0:
            st.info("No categorical columns available.")
            return

        column = st.selectbox(
            "Select Categorical Column",
            categorical_columns,
            key="count_col"
        )

        st.pyplot(plot_countplot(df, column))

    # Missing Values Heatmap
    elif st.session_state.selected_chart == "Missing":

        fig = plot_missing_values_heatmap(df)

        if fig:
            st.pyplot(fig)
        else:
            st.success("✅ No missing values found.")