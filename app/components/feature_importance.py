import pandas as pd
import plotly.express as px
import streamlit as st


def show_feature_importance(
    trained_pipeline,
    feature_names,
):
    """
    Display feature importance for supported models.
    """

    model = trained_pipeline.named_steps["model"]

    if not hasattr(model, "feature_importances_"):
        st.info(
            "Feature importance is not available for this model."
        )
        return

    preprocessor = trained_pipeline.named_steps["preprocessor"]

    transformed_features = (
        preprocessor.get_feature_names_out()
    )

    importance_df = pd.DataFrame(
        {
            "Feature": transformed_features,
            "Importance": model.feature_importances_,
        }
    )

    importance_df = (
        importance_df.sort_values(
            "Importance",
            ascending=False,
        )
        .head(20)
    )

    st.subheader("⭐ Feature Importance")

    fig = px.bar(
        importance_df,
        x="Importance",
        y="Feature",
        orientation="h",
        text="Importance",
        title="Top Important Features",
    )

    fig.update_layout(
        yaxis={"categoryorder": "total ascending"}
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    st.dataframe(
        importance_df,
        use_container_width=True,
    )