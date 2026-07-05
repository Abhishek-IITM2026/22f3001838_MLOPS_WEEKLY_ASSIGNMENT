# Integrating Feast Feature Store into the IRIS Pipeline

**Course:** MLOps  
**Week:** 3  
**Student:** Abhishek Dutta  
**Roll Number:** 22f3001838

---

# Project Overview

This project integrates the **Feast Feature Store** into the IRIS Machine Learning pipeline to ensure that the same feature definitions are used during both model training and inference, thereby eliminating training-serving skew.

The implementation uses:

- Feast Feature Store
- Google Cloud Platform (GCP)
- Google Colab
- Google Cloud Storage (GCS)
- Scikit-learn
- Decision Tree Classifier

---

# Repository Structure

```
22f3001838_MLOPS_WEEKLY_ASSIGNMENT
│
├── data/
│   └── iris_data_adapted_for_feast.csv
│
├── feast_repo/
│   └── feature_repo/
│       ├── data/
│       │   ├── iris_data_adapted_for_feast.csv
│       │   └── iris_data_adapted_for_feast.parquet
│       │
│       ├── feature_definitions.py
│       ├── feature_store.yaml
│       ├── registry.db
│       ├── online_store.db
│       └── __init__.py
│
├── model/
│   └── model.joblib
│
├── Feast_IRIS_Pipeline.ipynb
├── requirements.txt
└── README.md
```

> Replace `Feast_IRIS_Pipeline.ipynb` with your notebook's actual filename.

---

# Features

- Feast Feature Repository
- Entity Definition
- Feature View
- Offline Feature Retrieval
- Online Feature Retrieval
- Decision Tree Model Training
- Feast Materialization
- Online Prediction
- Optional BigQuery Backend

---

# Prerequisites

- Python 3.10+
- Google Colab (recommended)
- Git
- Google Cloud SDK (optional)
- Feast

---

# Installation

Clone the repository

```bash
git clone https://github.com/<YOUR_GITHUB_USERNAME>/22f3001838_MLOPS_WEEKLY_ASSIGNMENT.git
```

Go into the repository

```bash
cd 22f3001838_MLOPS_WEEKLY_ASSIGNMENT
```

Checkout the Week 3 branch

```bash
git checkout week_3
```

Install the required packages

```bash
pip install -r requirements.txt
```

or

```bash
pip install feast pandas pyarrow scikit-learn joblib
```

---

# Running the Feast IRIS Pipeline

## Step 1 – Open the notebook

Open the provided Jupyter notebook in **Google Colab**.

---

## Step 2 – Prepare the dataset

Convert the IRIS CSV dataset into Parquet.

```python
import pandas as pd

df = pd.read_csv("data/iris_data_adapted_for_feast.csv")

df["event_timestamp"] = pd.to_datetime(df["event_timestamp"], utc=True)
df["created_timestamp"] = pd.to_datetime(df["created_timestamp"], utc=True)

df.to_parquet(
    "feast_repo/feature_repo/data/iris_data_adapted_for_feast.parquet",
    index=False,
)
```

---

## Step 3 – Register the Feast Feature Repository

```bash
cd feast_repo/feature_repo
feast apply
```

Expected output

```
Created project feast_repo
Created entity iris_id
Created feature view iris_features
```

---

## Step 4 – Materialize Features

Materialize the features into the online store.

Example:

```bash
feast materialize \
2025-09-17T00:00:00+00:00 \
2025-09-19T00:00:00+00:00
```

---

## Step 5 – Verify the Feature Store

```python
import feast

fs = feast.FeatureStore(
    repo_path="feast_repo/feature_repo"
)

print(fs.list_feature_views())
```

---

## Step 6 – Train the Model

Run the notebook cells that:

- Retrieve historical features using

```python
get_historical_features()
```

- Train a Decision Tree classifier
- Save the trained model as

```
model/model.joblib
```

---

## Step 7 – Online Prediction

Run the notebook cells that:

- Retrieve features using

```python
get_online_features()
```

- Load the trained model
- Predict the IRIS species

Example output

```
iris_id    prediction

1001       versicolor
1002       versicolor
1003       versicolor
```

---

# Optional BigQuery Backend

The project can be extended by replacing the local FileSource with a BigQuerySource.

Required changes:

- Upload the feature dataset to BigQuery.
- Replace `FileSource` with `BigQuerySource` in `feature_definitions.py`.
- Update `feature_store.yaml` to use BigQuery as the offline store.
- Re-run:

```bash
feast apply
```

and

```bash
feast materialize ...
```

---

# Technologies Used

- Python
- Feast
- Pandas
- Scikit-learn
- PyArrow
- Joblib
- Google Colab
- Google Cloud Platform
- Git

---

# Assignment Tasks Completed

| Task | Status |
|------|--------|
| Initialize Feast Repository |
| Define Entity |
| Define Data Source |
| Define Feature View |
| Apply Feast Definitions |
| Materialize Features |
| Historical Feature Retrieval |
| Train Decision Tree Model |
| Online Feature Retrieval |
| Online Prediction |
| BigQuery Backend | Optional |

---

# Author

**Abhishek Dutta**

**IIT Madras BS Degree Programme**

**Roll Number:** 22f3001838
