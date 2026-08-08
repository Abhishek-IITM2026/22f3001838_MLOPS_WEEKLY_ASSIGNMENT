import pandas as pd
import numpy as np
import os

from sklearn.datasets import load_iris

os.makedirs("poisoned_data", exist_ok=True)

iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["target"] = iris.target


def poison_dataset(df, percentage):

    poisoned = df.copy()

    n_poison = int(len(df) * percentage)

    indices = np.random.choice(
        poisoned.index,
        n_poison,
        replace=False
    )

    poisoned.loc[
        indices,
        iris.feature_names
    ] = np.random.uniform(
        low=0,
        high=10,
        size=(n_poison, 4)
    )

    poisoned.loc[
        indices,
        "target"
    ] = np.random.randint(
        0,
        3,
        size=n_poison
    )

    return poisoned


poison_dataset(df, 0.05).to_csv(
    "poisoned_data/iris_poisoned_5.csv",
    index=False
)

poison_dataset(df, 0.10).to_csv(
    "poisoned_data/iris_poisoned_10.csv",
    index=False
)

poison_dataset(df, 0.50).to_csv(
    "poisoned_data/iris_poisoned_50.csv",
    index=False
)

print("Poisoned datasets created.")
