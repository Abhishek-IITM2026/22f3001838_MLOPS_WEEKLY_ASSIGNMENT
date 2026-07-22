# MLflow Integration for IRIS Classification Pipeline

This repository contains an end-to-end Machine Learning pipeline for the **IRIS Classification** dataset with **MLflow Experiment Tracking**, **MLflow Model Registry**, **DVC Dataset Versioning**, and **GitHub Actions CI** integration.

The project demonstrates how MLflow can be used to manage experiments, compare different hyperparameter configurations, register trained models, and automate testing through GitHub Actions.

---

## Project Overview

The objective of this project is to build a reproducible Machine Learning workflow by integrating modern MLOps tools.

The pipeline performs the following tasks:

- Loads the IRIS dataset
- Trains a Decision Tree classifier
- Performs hyperparameter tuning
- Logs parameters and evaluation metrics using MLflow
- Registers trained models in the MLflow Model Registry
- Uses DVC to version only the dataset
- Loads the latest registered model during evaluation
- Executes automated testing through GitHub Actions

---

## Project Structure

```text
.
├── data/
│   ├── iris.csv
│   └── iris.csv.dvc
│
├── tests/
│   ├── test_data.py
│   └── test_model.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── train.py
├── requirements.txt
├── dvc.yaml
├── mlflow.db
├── mlruns/
└── README.md
```

---

# Technologies Used

- Python
- Scikit-Learn
- MLflow
- DVC
- Git
- GitHub Actions
- Google Cloud Shell

---

# Pipeline Workflow

The complete pipeline works in the following sequence:

```
              DVC
               │
               ▼
       Load IRIS Dataset
               │
               ▼
      Train/Test Split
               │
               ▼
 Hyperparameter Tuning
               │
               ▼
 Train Decision Tree Models
               │
               ▼
 Evaluate Performance
               │
               ▼
 Log Parameters & Metrics
        using MLflow
               │
               ▼
 Register Model
     in MLflow Registry
               │
               ▼
 Load Latest Model
     for Evaluation
               │
               ▼
 Run Unit Tests
               │
               ▼
 GitHub Actions CI
```

---

# Input Dataset

The project uses the classic **IRIS dataset** containing four numerical features:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

Target classes:

- Iris-setosa
- Iris-versicolor
- Iris-virginica

---

# Hyperparameter Tuning

The training pipeline performs exhaustive search over the following parameters:

```python
max_depth = [2, 4, 6]
criterion = ["gini", "entropy"]
```

This generates six different experiments.

---

# MLflow Integration

Each experiment automatically creates a new MLflow run.

The following information is logged:

## Parameters

- max_depth
- criterion
- random_state

## Metrics

- Accuracy
- Precision
- Recall
- F1 Score

## Model Artifact

The trained model is automatically registered in the MLflow Model Registry as

```
IRIS_Model
```

Every execution creates a new registered model version.

---

# DVC Integration

DVC is responsible only for versioning the dataset.

Tracked:

```
data/iris.csv
```

The trained model is **not** tracked by DVC.

Model versioning is completely managed by MLflow.

---

# Running the Project

## Clone Repository

```bash
git clone <repository-url>
cd <repository-name>
```

---

## Create Virtual Environment

```bash
python3 -m venv .venv
```

Activate

Linux/Mac

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Pull Dataset using DVC

```bash
dvc pull
```

---

## Train Model

```bash
python train.py
```

This performs

- hyperparameter tuning
- model training
- metric evaluation
- MLflow logging
- model registration

---

# Launch MLflow UI

```bash
mlflow ui --host 0.0.0.0 --port 5000
```

Open

```
http://localhost:5000
```

or use the Cloud Shell Preview URL.

---

# Running Tests

```bash
pytest -v
```

The evaluation pipeline loads the latest model directly from the MLflow Model Registry.

```python
MODEL_URI = "models:/IRIS_Model/latest"
```

---

# GitHub Actions

Whenever changes are pushed to GitHub, the workflow automatically performs the following steps:

1. Checkout repository
2. Install Python dependencies
3. Pull dataset using DVC
4. Reset MLflow tracking store
5. Train the model
6. Register model in MLflow
7. Execute all test cases

---

# Challenges Faced

During GitHub Actions execution, MLflow initially failed because the tracking directory contained absolute artifact paths from the development environment.

This was resolved by resetting the MLflow tracking store before every workflow execution.

```yaml
- name: Reset MLflow Tracking
  run: |
    rm -rf mlruns
    rm -f mlflow.db
```

This ensures that GitHub Actions creates a fresh tracking store during every CI run.

---

# Project Features

- End-to-End ML Pipeline
- MLflow Experiment Tracking
- Hyperparameter Tuning
- MLflow Model Registry
- DVC Dataset Versioning
- Automated Testing
- GitHub Actions Continuous Integration
- Reproducible Machine Learning Workflow

---

# Future Improvements

- Deploy the registered model using Vertex AI
- Integrate a remote MLflow Tracking Server
- Add model monitoring
- Automate retraining pipeline
- Support additional machine learning algorithms

---

# Author

**Abhishek Dutta**

IIT Madras BS Degree in Data Science and Applications

Roll Number: **22f3001838**

---

# License

This project is developed for academic purposes as part of the IIT Madras MLOps coursework.
