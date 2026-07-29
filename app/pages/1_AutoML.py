import os
import sys

# ---------------------------------------------------
# Add Project Root to Python Path
# ---------------------------------------------------

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# ---------------------------------------------------
# Imports
# ---------------------------------------------------

import streamlit as st

from utils.automl import (
    detect_problem_type,
    get_feature_columns,
    build_preprocessor,
    split_dataset,
    get_classification_models,
    get_regression_models,
    train_models,
)
from app.components.automl_results import show_model_results
from app.components.feature_importance import show_feature_importance
from app.components.prediction import show_prediction_section
from app.components.confusion_matrix import show_confusion_matrix
from app.components.classification_report import show_classification_report
from app.components.download_model import show_model_download
from app.components.automl_summary import show_automl_summary
# ---------------------------------------------------
# Streamlit Config
# ---------------------------------------------------

st.set_page_config(
    page_title="AutoML",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AutoML")

st.write(
    "Train Machine Learning models automatically without writing code."
)

# ---------------------------------------------------
# Check Dataset
# ---------------------------------------------------

if "cleaned_df" not in st.session_state:
    st.warning("Please upload and clean a dataset first.")
    st.stop()

df = st.session_state["cleaned_df"]

# ---------------------------------------------------
# Dataset Information
# ---------------------------------------------------

st.success("Dataset Loaded Successfully")

col1, col2 = st.columns(2)

with col1:
    st.metric("Rows", df.shape[0])

with col2:
    st.metric("Columns", df.shape[1])

st.divider()

# ---------------------------------------------------
# Target Selection
# ---------------------------------------------------

st.subheader("Target Selection")

previous_target = st.session_state.get("previous_target")

target_column = st.selectbox(
    "Select Target Column",
    df.columns,
    key="target_column"
)

# Clear previous training results if target changed
if previous_target != target_column:

    for key in [
        "model_results",
        "best_model",
        "trained_pipeline",
    ]:
        st.session_state.pop(key, None)

    st.session_state["previous_target"] = target_column
# ---------------------------------------------------
# Detect Problem Type
# ---------------------------------------------------

result = detect_problem_type(df, target_column)

problem_type = result["problem_type"]

st.session_state["problem_type"] = problem_type

# ---------------------------------------------------
# Problem Details
# ---------------------------------------------------

st.subheader("Problem Detection")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Problem Type", problem_type)

with col2:
    st.metric("Datatype", result["dtype"])

with col3:
    st.metric("Unique Values", result["unique_values"])

st.divider()

# ---------------------------------------------------
# Feature Selection
# ---------------------------------------------------

st.subheader("Feature Selection")

available_features = get_feature_columns(
    df,
    target_column
)

selected_features = st.multiselect(
    "Select Feature Columns",
    options=available_features,
    default=available_features,
    key="feature_columns",
)

if len(selected_features) == 0:
    st.warning("Please select at least one feature.")
    st.stop()

# ---------------------------------------------------
# Build Dataset
# ---------------------------------------------------
# Remove rows where target is missing
train_df = df[selected_features + [target_column]].dropna(subset=[target_column])

X = train_df[selected_features]
y = train_df[target_column]
removed_rows = len(df) - len(train_df)
if removed_rows > 0:
    st.warning(
        f"Removed {removed_rows} rows because the selected target column "
        f"contains missing values."
    )
st.write("Target Column:", target_column)
st.write("Missing values in target:", y.isna().sum())
st.write("Target dtype:", y.dtype)
st.write(y.head(10))

# Debug: Check missing values in target
st.write("Missing values in target:", y.isna().sum())
# ---------------------------------------------------
# Build Preprocessor
# ---------------------------------------------------

(
    preprocessor,
    numeric_features,
    categorical_features,
) = build_preprocessor(X)

# ---------------------------------------------------
# Feature Summary
# ---------------------------------------------------

st.subheader("Feature Summary")

col1, col2 = st.columns(2)

with col1:
    st.write("### Numerical Features")

    if numeric_features:
        st.write(numeric_features)
    else:
        st.info("No numerical features found.")

with col2:
    st.write("### Categorical Features")

    if categorical_features:
        st.write(categorical_features)
    else:
        st.info("No categorical features found.")

st.divider()

# ---------------------------------------------------
# Train/Test Split
# ---------------------------------------------------

st.subheader("Train/Test Split")

col1, col2 = st.columns(2)

with col1:
    test_size = st.slider(
        "Test Size",
        min_value=0.10,
        max_value=0.40,
        value=0.20,
        step=0.05,
    )

with col2:
    random_state = st.number_input(
        "Random State",
        min_value=0,
        value=42,
        step=1,
    )

# ---------------------------------------------------
# Split Dataset
# ---------------------------------------------------

X_train, X_test, y_train, y_test = split_dataset(
    X,
    y,
    problem_type,
    test_size=test_size,
    random_state=random_state,
)

# ---------------------------------------------------
# Store Session State
# ---------------------------------------------------

st.session_state["X"] = X
st.session_state["y"] = y

st.session_state["preprocessor"] = preprocessor

st.session_state["X_train"] = X_train
st.session_state["X_test"] = X_test

st.session_state["y_train"] = y_train
st.session_state["y_test"] = y_test

# ---------------------------------------------------
# Dataset Split Summary
# ---------------------------------------------------

st.success("Dataset prepared successfully.")

col1, col2 = st.columns(2)

with col1:
    st.metric("Training Samples", len(X_train))

with col2:
    st.metric("Testing Samples", len(X_test))

st.divider()

st.divider()

st.subheader("Model Training")

if st.button("🚀 Train Models", use_container_width=True):

    with st.spinner("Training models..."):

        if problem_type == "Classification":
            models = get_classification_models()
        else:
            models = get_regression_models()

        (
            results_df,
            best_model,
            best_pipeline,
            best_predictions,
        ) = train_models(
            models=models,
            preprocessor=preprocessor,
            X_train=X_train,
            X_test=X_test,
            y_train=y_train,
            y_test=y_test,
            problem_type=problem_type,
        )

        st.session_state["model_results"] = results_df
        st.session_state["best_model"] = best_model
        st.session_state["trained_pipeline"] = best_pipeline
        st.session_state["best_predictions"] = best_predictions

st.divider()

if (
    "model_results" in st.session_state
    and "best_model" in st.session_state
):

    show_model_results(
        results_df=st.session_state["model_results"],
        problem_type=problem_type,
        best_model=st.session_state["best_model"],
    )
else:
    st.info("👆 Select a target column and click **Train Models** to generate results.")

if (
    "trained_pipeline" in st.session_state
    and "X" in st.session_state
):

    show_feature_importance(
        st.session_state["trained_pipeline"],
        st.session_state["X"].columns,
    )
if (
    "trained_pipeline" in st.session_state
    and "X" in st.session_state
):

    show_prediction_section(
        pipeline=st.session_state["trained_pipeline"],
        X=st.session_state["X"],
    )
if (
    problem_type == "Classification"
    and "best_predictions" in st.session_state
):

    show_confusion_matrix(
        y_test=st.session_state["y_test"],
        predictions=st.session_state["best_predictions"],
    )
if (
    problem_type == "Classification"
    and "best_predictions" in st.session_state
):

    show_classification_report(
        y_test=st.session_state["y_test"],
        predictions=st.session_state["best_predictions"],
    )
if (
    "trained_pipeline" in st.session_state
    and "best_model" in st.session_state
):

    show_model_download(
        pipeline=st.session_state["trained_pipeline"],
        model_name=st.session_state["best_model"],
    )
if (
    "model_results" in st.session_state
    and "best_model" in st.session_state
):

    show_automl_summary(
        problem_type=problem_type,
        best_model=st.session_state["best_model"],
        results_df=st.session_state["model_results"],
        X_train=st.session_state["X_train"],
        X_test=st.session_state["X_test"],
        selected_features=selected_features,
    )
# ---------------------------------------------------
# Dataset Preview
# ---------------------------------------------------

st.subheader("Dataset Preview")

st.dataframe(
    df.head(),
    use_container_width=True
)