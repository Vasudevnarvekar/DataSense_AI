import streamlit as st


def show_automl_summary(
    problem_type,
    best_model,
    results_df,
    X_train,
    X_test,
    selected_features,
):
    """
    Display AutoML Summary Dashboard.
    """

    st.divider()
    st.subheader("📋 AutoML Summary")

    best_result = results_df.iloc[0]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🏆 Best Model",
            best_model,
        )

    with col2:

        if problem_type == "Classification":
            st.metric(
                "🎯 Best Accuracy",
                f"{best_result['Accuracy']:.4f}",
            )
        else:
            st.metric(
                "📈 Best R² Score",
                f"{best_result['R² Score']:.4f}",
            )

    with col3:
        st.metric(
            "🤖 Models Trained",
            len(results_df),
        )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Training Samples",
            len(X_train),
        )

    with col2:
        st.metric(
            "Testing Samples",
            len(X_test),
        )

    with col3:
        st.metric(
            "Selected Features",
            len(selected_features),
        )