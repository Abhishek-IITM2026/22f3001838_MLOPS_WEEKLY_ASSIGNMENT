import mlflow.pyfunc
import pandas as pd

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score

DATA_PATH = "data/iris.csv"

# Load the latest registered model from MLflow Model Registry
MODEL_URI = "models:/IRIS_Model/latest"


def test_model_exists():
    model = mlflow.pyfunc.load_model(MODEL_URI)
    assert model is not None


def test_model_accuracy():
    model = mlflow.pyfunc.load_model(MODEL_URI)

    df = pd.read_csv(DATA_PATH)

    X = df.drop(columns=["species"])
    y = df["species"]

    predictions = model.predict(X)

    accuracy = accuracy_score(y, predictions)
    precision = precision_score(
        y,
        predictions,
        average="macro"
    )

    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")

    assert accuracy >= 0.90
    assert precision >= 0.90
