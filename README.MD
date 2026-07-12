# Project Overview

This repository contains the solution for the **MLOps Week 4 Assignment**. The objective is to implement a complete **Continuous Integration (CI)** pipeline for an Iris Classification Machine Learning project.

The project demonstrates:

- Data Validation using PyTest
- Model Evaluation using PyTest
- Dataset & Model Versioning using DVC
- Google Cloud Storage (GCS) as DVC Remote
- GitHub Actions based Continuous Integration
- Workload Identity Federation (WIF) for secure Google Cloud authentication
- Continuous Machine Learning (CML) based reporting

---

# Repository Structure

```
.
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── .dvc/
│
├── data/
│   ├── iris.csv
│   └── iris.csv.dvc
│
├── model/
│   └── model.joblib
│
├── tests/
│   ├── test_data.py
│   └── test_model.py
│
├── train.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Project Workflow

```
Dataset
   │
   ▼
DVC Remote (Google Cloud Storage)
   │
   ▼
GitHub Repository
   │
   ▼
GitHub Actions
   │
   ▼
Authenticate using Workload Identity Federation
   │
   ▼
dvc pull
   │
   ▼
Run PyTest
   │
   ▼
Generate Test Report
   │
   ▼
CML Pull Request Comment
```

---

# Technologies Used

- Python 3.12
- Scikit-Learn
- Pandas
- NumPy
- PyTest
- DVC
- Google Cloud Storage
- GitHub Actions
- CML
- Workload Identity Federation

---

# Clone Repository

```bash
git clone https://github.com/Abhishek-IITM2026/22f3001838_MLOPS_WEEKLY_ASSIGNMENT.git

cd 22f3001838_MLOPS_WEEKLY_ASSIGNMENT
```

---

# Create Virtual Environment

Linux / MacOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

Windows

```powershell
python -m venv .venv

.venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install --upgrade pip

pip install -r requirements.txt
```

---

# Configure DVC

Initialize DVC

```bash
dvc init
```

Verify Remote

```bash
cat .dvc/config
```

Expected

```ini
[core]
    remote = myremote

['remote "myremote"']
    url = gs://22f3001838-mlops-week2/dvcstore
```

---

# Pull Dataset and Model

```bash
dvc pull
```

Expected Output

```
Everything is up to date.
```

---

# Train Model

```bash
python train.py
```

or

```bash
python train.py 2
```

---

# Run Tests

Run complete test suite

```bash
pytest -v
```

Run Data Validation Tests

```bash
pytest tests/test_data.py -v
```

Run Model Evaluation Tests

```bash
pytest tests/test_model.py -v
```

Expected Output

```
=====================
8 passed
=====================
```

---

# Data Validation Tests

The following validations are implemented:

- Dataset exists
- Schema validation
- Missing value validation
- Numeric feature validation
- Species label validation
- Numeric value validation

---

# Model Evaluation Tests

The following validations are implemented:

- Model exists
- Model loads successfully
- Model prediction
- Accuracy threshold verification

---

# Continuous Integration

GitHub Actions automatically executes on:

- Every Push
- Every Pull Request

Workflow performs:

1. Checkout Repository
2. Setup Python
3. Install Dependencies
4. Authenticate to Google Cloud
5. Setup gcloud
6. Pull DVC Data
7. Execute PyTest
8. Generate Report
9. Publish CML Comment

---

# Workload Identity Federation

GitHub Actions authenticates to Google Cloud using **Workload Identity Federation** instead of Service Account JSON Keys.

Advantages:

- No long-lived credentials
- Improved security
- Recommended authentication method by Google Cloud

---

# Google Cloud Services Used

- Google Cloud Storage
- IAM
- Workload Identity Federation
- Cloud Shell

---

# DVC Remote

```
Google Cloud Storage

Bucket:
gs://22f3001838-mlops-week2

Directory:
dvcstore
```

---

# GitHub Actions Workflow

Location

```
.github/workflows/ci.yml
```

Main Steps

- Checkout Repository
- Setup Python
- Install Dependencies
- Authenticate Google Cloud
- DVC Pull
- Run Tests
- Generate Report
- CML Report

---

# CI Trigger

```yaml
on:
  push:
    branches:
      - "**"

  pull_request:
    branches:
      - "**"
```

---

# Example Workflow

```
Developer Push

        │

        ▼

GitHub Repository

        │

        ▼

GitHub Actions

        │

        ▼

Authenticate

        │

        ▼

DVC Pull

        │

        ▼

PyTest

        │

        ▼

Generate Report

        │

        ▼

Pull Request Comment
```

---

# Results

✔ Data Validation Tests Passed

✔ Model Evaluation Tests Passed

✔ DVC Integration Successful

✔ Google Cloud Authentication Successful

✔ GitHub Actions Successful

✔ CI Pipeline Successful

---

# Future Improvements

- Docker Containerization
- MLflow Integration
- Automated Model Deployment
- Continuous Training
- Monitoring using Vertex AI

---

# Author

**Abhishek Dutta**

Roll Number: **22f3001838**

IIT Madras BS Degree Programme

---

# License

This project has been developed for the **IIT Madras MLOps Weekly Assignment**.
