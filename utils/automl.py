import pandas as pd
import math

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
# Classification
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
# Regression
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
# Metrics
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
from sklearn.model_selection import cross_val_score

def detect_problem_type(df: pd.DataFrame, target_column: str):
    """
    Detect whether the selected target column
    is suitable for Classification or Regression.
    """

    target = df[target_column]

    unique_values = target.nunique()
    dtype = target.dtype

    if dtype == "object":
        problem_type = "Classification"

    elif pd.api.types.is_bool_dtype(dtype):
        problem_type = "Classification"

    elif unique_values <= 20:
        problem_type = "Classification"

    else:
        problem_type = "Regression"

    return {
        "problem_type": problem_type,
        "dtype": str(dtype),
        "unique_values": unique_values,
    }


def get_feature_columns(df: pd.DataFrame, target_column: str):
    """
    Return all feature columns except target.
    """

    return [col for col in df.columns if col != target_column]


def build_preprocessor(X: pd.DataFrame):
    """
    Build preprocessing pipeline.
    """

    numeric_features = X.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    categorical_features = X.select_dtypes(
        include=["object", "category", "bool"]
    ).columns.tolist()

    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )

    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_pipeline, numeric_features),
            ("cat", categorical_pipeline, categorical_features),
        ]
    )

    return (
        preprocessor,
        numeric_features,
        categorical_features,
    )


def split_dataset(
    X,
    y,
    problem_type,
    test_size=0.2,
    random_state=42,
):
    """
    Split dataset into training and testing.
    """

    stratify = y if problem_type == "Classification" else None

    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=stratify,
    )
def get_classification_models():
    """
    Return all classification models.
    """

    return {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(random_state=42),
        "KNN": KNeighborsClassifier(),
        "SVM": SVC(probability=True),
    }

def get_regression_models():
    """
    Return all regression models.
    """

    return {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(random_state=42),
        "Random Forest": RandomForestRegressor(random_state=42),
        "KNN": KNeighborsRegressor(),
        "Ridge": Ridge(),
        "Lasso": Lasso(),
    }

def train_models(
    models,
    preprocessor,
    X_train,
    X_test,
    y_train,
    y_test,
    problem_type,
):
    """
    Train every model and compare performance.
    """

    results = []

    best_model = None
    best_pipeline = None
    best_predictions = None
    best_score = float("-inf")

    for name, model in models.items():

        try:

            pipeline = Pipeline(
                steps=[
                    ("preprocessor", preprocessor),
                    ("model", model),
                ]
            )

            pipeline.fit(X_train, y_train)

            predictions = pipeline.predict(X_test)
### Cross Validation
            if problem_type == "Classification":

                cv_scores = cross_val_score(
                    pipeline,
                    X_train,
                    y_train,
                    cv=5,
                    scoring="accuracy",
                )

            else:

                cv_scores = cross_val_score(
                    pipeline,
                    X_train,
                    y_train,
                    cv=5,
                    scoring="r2",
                )

            cv_mean = cv_scores.mean()
            # ---------------- Classification ----------------

            if problem_type == "Classification":

                accuracy = accuracy_score(y_test, predictions)

                precision = precision_score(
                    y_test,
                    predictions,
                    average="weighted",
                    zero_division=0,
                )

                recall = recall_score(
                    y_test,
                    predictions,
                    average="weighted",
                    zero_division=0,
                )

                f1 = f1_score(
                    y_test,
                    predictions,
                    average="weighted",
                    zero_division=0,
                )

                score = accuracy

                results.append({
                    "Model": name,
                    "Accuracy": round(accuracy, 4),
                    "CV Score": round(cv_mean, 4),
                    "Precision": round(precision, 4),
                    "Recall": round(recall, 4),
                    "F1 Score": round(f1, 4),
                })

            # ---------------- Regression ----------------

            else:

                mae = mean_absolute_error(y_test, predictions)

                mse = mean_squared_error(
                    y_test,
                    predictions,
                )

                rmse = math.sqrt(mse)

                r2 = r2_score(y_test, predictions)
                score = r2

                results.append({
                    "Model": name,
                    "MAE": round(mae, 4),
                    "RMSE": round(rmse, 4),
                    "R² Score": round(r2, 4),
                    "CV Score": round(cv_mean, 4),
                })

            # ---------------- Best Model ----------------

            if score > best_score:
                best_score = score
                best_model = name
                best_pipeline = pipeline
                best_predictions = predictions

        except Exception as e:
            raise RuntimeError(f"Model '{name}' failed: {e}")

    if len(results) == 0:
        raise ValueError("No models were trained successfully.")

    results_df = pd.DataFrame(results)

    if problem_type == "Classification":
        results_df = results_df.sort_values(
            by="Accuracy",
            ascending=False,
        )
    else:
        results_df = results_df.sort_values(
            by="R² Score",
            ascending=False,
        )

    return (
        results_df,
        best_model,
        best_pipeline,
        best_predictions,
    )