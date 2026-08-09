import mlflow
import mlflow.sklearn

mlflow.set_tracking_uri("file:./mlruns")
mlflow.set_experiment("week8_mlsecops")

import pandas as pd
from scipy import stats

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

datasets = {
    "0": None,
    "5": "poisoned_data/iris_poisoned_5.csv",
    "10": "poisoned_data/iris_poisoned_10.csv",
    "50": "poisoned_data/iris_poisoned_50.csv"
}

for poison_level, file in datasets.items():

    if poison_level == "0":

        iris = load_iris()

        df = pd.DataFrame(
            iris.data,
            columns=iris.feature_names
        )

        df["target"] = iris.target

    else:

        df = pd.read_csv(file)

   #df = df[
    #    (df.iloc[:, 0] >= 0) &
    #    (df.iloc[:, 1] >= 0) &
    #    (df.iloc[:, 2] >= 0) &
    #    (df.iloc[:, 3] >= 0)
    #]

    X = df.drop("target", axis=1)
    y = df["target"]


    #z_scores = abs(stats.zscore(X))

    #mask = (z_scores < 3).all(axis=1)

    #X = X[mask]
    #y = y[mask]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestClassifier(
        random_state=42
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    accuracy = accuracy_score(y_test, preds)

    precision = precision_score(
        y_test,
        preds,
        average="weighted"
    )

    recall = recall_score(
        y_test,
        preds,
        average="weighted"
    )

    f1 = f1_score(
        y_test,
        preds,
        average="weighted"
    )

    with mlflow.start_run(
        run_name=f"poison_{poison_level}_mitigated"
    ):

        mlflow.log_param(
            "poison_level",
            poison_level
        )

        mlflow.log_param(
            "mitigation",
            "range_validation+zscore"
        )

        mlflow.log_metric(
            "accuracy",
            accuracy
        )

        mlflow.log_metric(
            "precision",
            precision
        )

        mlflow.log_metric(
            "recall",
            recall
        )

        mlflow.log_metric(
            "f1_score",
            f1
        )

        sample_input = X_train.head(5)

        mlflow.sklearn.log_model(
            model,
            "model",
            input_example=sample_input
        )

        print(
            f"Poison {poison_level}% | "
            f"Acc={accuracy:.4f} "
            f"Prec={precision:.4f} "
            f"Recall={recall:.4f} "
            f"F1={f1:.4f}"
        )
