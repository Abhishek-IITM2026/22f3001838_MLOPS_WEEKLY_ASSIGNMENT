import joblib
import pandas as pd

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score

MODEL_PATH = "model/model.joblib"
DATA_PATH = "data/iris.csv"


def test_model_exists():
    model = joblib.load(MODEL_PATH)
    assert model is not None


def test_model_accuracy():

    model = joblib.load(MODEL_PATH)

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
