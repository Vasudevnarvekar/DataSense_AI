import pandas as pd
import streamlit as st


def show_prediction_section(
    pipeline,
    X: pd.DataFrame,
):
    """
    Render prediction form dynamically based on feature types.
    """

    st.divider()
    st.subheader("🔮 Predict New Data")

    user_input = {}

    for column in X.columns:

        # Numerical columns
        if pd.api.types.is_numeric_dtype(X[column]):

            value = st.number_input(
                label=column,
                value=float(X[column].median()),
            )

        # Categorical columns
        else:

            options = X[column].dropna().unique().tolist()

            value = st.selectbox(
                label=column,
                options=options,
            )

        user_input[column] = value

    input_df = pd.DataFrame([user_input])

    st.divider()

    if st.button(
        "🚀 Predict",
        use_container_width=True,
    ):

        prediction = pipeline.predict(input_df)

        st.success("Prediction Completed")

        predicted_value = prediction[0]

        # Round regression output
        if isinstance(predicted_value, float):
            predicted_value = round(predicted_value, 2)

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Prediction",
                predicted_value,
            )

        # Show prediction probability (only if supported)
        if hasattr(pipeline, "predict_proba"):

            try:

                probabilities = pipeline.predict_proba(input_df)

                confidence = probabilities.max() * 100

                with col2:
                    st.metric(
                        "Confidence",
                        f"{confidence:.2f}%"
                    )

            except Exception:
                pass