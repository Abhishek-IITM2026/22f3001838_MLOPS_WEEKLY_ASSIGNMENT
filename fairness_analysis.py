import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from fairlearn.metrics import MetricFrame
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

# Load DVC-managed dataset
df = pd.read_csv("data/iris.csv")

# Create sensitive attribute
df["location"] = np.random.randint(
    0,
    2,
    size=len(df)
)

# Exclude location from training
X = df.drop(
    ["species", "location"],
    axis=1
)

y = df["species"]

location = df["location"]

X_train, X_test, y_train, y_test, loc_train, loc_test = train_test_split(
    X,
    y,
    location,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    random_state=42
)

model.fit(X_train, y_train)

preds = model.predict(X_test)

metrics = {
    "accuracy": accuracy_score,
    "precision": lambda y_true, y_pred:
        precision_score(
            y_true,
            y_pred,
            average="weighted"
        ),
    "recall": lambda y_true, y_pred:
        recall_score(
            y_true,
            y_pred,
            average="weighted"
        )
}

mf = MetricFrame(
    metrics=metrics,
    y_true=y_test,
    y_pred=preds,
    sensitive_features=loc_test
)

print("\n=== OVERALL ===")
print(mf.overall)

print("\n=== BY LOCATION ===")
print(mf.by_group)
