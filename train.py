import itertools
import mlflow
import mlflow.sklearn
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)
from mlflow.models.signature import infer_signature

# -----------------------
# Load Dataset
# -----------------------
df = pd.read_csv("data/iris.csv")

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# -----------------------
# MLflow Experiment
# -----------------------
mlflow.set_experiment("Iris_Classification")

# Hyperparameters to tune
max_depth_list = [2, 4, 6]
criterion_list = ["gini", "entropy"]

for max_depth, criterion in itertools.product(max_depth_list, criterion_list):

    run_name = f"depth_{max_depth}_{criterion}"

    with mlflow.start_run(run_name=run_name):

        # -----------------------
        # Train Model
        # -----------------------
        model = DecisionTreeClassifier(
            max_depth=max_depth,
            criterion=criterion,
            random_state=42
        )

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        # -----------------------
        # Evaluation Metrics
        # -----------------------
        accuracy = accuracy_score(y_test, predictions)
        precision = precision_score(
            y_test,
            predictions,
            average="macro"
        )
        recall = recall_score(
            y_test,
            predictions,
            average="macro"
        )
        f1 = f1_score(
            y_test,
            predictions,
            average="macro"
        )

        # -----------------------
        # Log Parameters
        # -----------------------
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_param("criterion", criterion)
        mlflow.log_param("random_state", 42)

        # -----------------------
        # Log Metrics
        # -----------------------
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)
        mlflow.log_metric("f1_score", f1)

        # -----------------------
        # Tags (Optional but useful)
        # -----------------------
        mlflow.set_tag("model", "DecisionTreeClassifier")
        mlflow.set_tag("dataset", "iris")

        # -----------------------
        # Model Signature
        # -----------------------
        signature = infer_signature(
            X_train,
            model.predict(X_train)
        )

        # -----------------------
        # Log Model
        # -----------------------
        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="model",
            registered_model_name="IRIS_Model",
            signature=signature,
            input_example=X_train.iloc[:5]
        )

        print("=" * 50)
        print(f"Run Name     : {run_name}")
        print(f"Max Depth    : {max_depth}")
        print(f"Criterion    : {criterion}")
        print(f"Accuracy     : {accuracy:.4f}")
        print(f"Precision    : {precision:.4f}")
        print(f"Recall       : {recall:.4f}")
        print(f"F1 Score     : {f1:.4f}")
