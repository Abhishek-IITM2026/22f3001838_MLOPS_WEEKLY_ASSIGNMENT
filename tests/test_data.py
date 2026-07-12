import pandas as pd
import numpy as np

DATA_PATH = "data/iris.csv"

EXPECTED_COLUMNS = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
    "species"
]


def test_dataset_exists():
    df = pd.read_csv(DATA_PATH)
    assert len(df) > 0


def test_schema():
    df = pd.read_csv(DATA_PATH)
    assert list(df.columns) == EXPECTED_COLUMNS


def test_no_missing_values():
    df = pd.read_csv(DATA_PATH)
    assert df.isnull().sum().sum() == 0


def test_numeric_columns():
    df = pd.read_csv(DATA_PATH)

    numeric = EXPECTED_COLUMNS[:-1]

    for col in numeric:
        assert np.issubdtype(df[col].dtype, np.number)


def test_species_values():
    df = pd.read_csv(DATA_PATH)

    expected = {"setosa", "versicolor", "virginica"}

    assert set(df["species"].unique()) == expected

def test_numeric_values():
    df = pd.read_csv(DATA_PATH)

    numeric = [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width"
    ]

    assert np.isfinite(df[numeric].to_numpy()).all()
