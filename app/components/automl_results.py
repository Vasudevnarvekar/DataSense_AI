import streamlit as st
import plotly.express as px


def show_model_results(results_df, problem_type, best_model):
    """
    Display AutoML model comparison dashboard.
    """

    st.header("📊 Model Performance Dashboard")

    # ----------------------------
    # Metrics
    # ----------------------------

    if problem_type == "Classification":

        best_accuracy = results_df.iloc[0]["Accuracy"]

        col1, col2 = st.columns(2)

        with col1:
            st.metric("🏆 Best Model", best_model)

        with col2:
            st.metric(
                "🎯 Best Accuracy",
                f"{best_accuracy:.4f}",
            )

        fig = px.bar(
            results_df,
            x="Model",
            y="Accuracy",
            text="Accuracy",
            title="Model Accuracy Comparison",
        )

    else:

        best_r2 = results_df.iloc[0]["R² Score"]

        col1, col2 = st.columns(2)

        with col1:
            st.metric("🏆 Best Model", best_model)

        with col2:
            st.metric(
                "📈 Best R² Score",
                f"{best_r2:.4f}",
            )

        fig = px.bar(
            results_df,
            x="Model",
            y="R² Score",
            text="R² Score",
            title="Regression Model Comparison",
        )

    fig.update_traces(textposition="outside")

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    st.subheader("Detailed Results")

    st.dataframe(
        results_df,
        use_container_width=True,
    )