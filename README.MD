# IRIS Classification Pipeline with DVC and Google Cloud Storage

## Overview

This project demonstrates an end-to-end Machine Learning workflow using:

- Git for source code version control
- DVC (Data Version Control) for dataset and model versioning
- Google Cloud Storage (GCS) as the DVC remote storage
- Google Cloud Compute Engine for cloud execution
- Scikit-learn for training an IRIS classification model

The objective is to build a fully reproducible ML pipeline where:
- Git stores code and lightweight metadata.
- DVC stores datasets and trained models.
- Google Cloud Storage acts as the remote storage backend.

---

# Project Structure

```
.
├── data/
│   └── iris.csv
├── model/
│   └── model.joblib
├── train.py
├── requirements.txt
├── .gitignore
├── .dvc/
├── .dvcignore
├── data/iris.csv.dvc
├── model/model.joblib.dvc
└── README.md
```

---

# Prerequisites

- Python 3.10+
- Git
- Google Cloud SDK
- Google Cloud Project
- Google Cloud Storage Bucket
- DVC with GCS support

---

# Step 1: Clone the Repository

```bash
git clone https://github.com/<username>/<repository>.git
```

Move into the project directory.

```bash
cd <repository>
```

---

# Step 2: Create a Python Virtual Environment

```bash
python3 -m venv .env
```

Activate the environment.

```bash
source .env/bin/activate
```

---

# Step 3: Install Dependencies

Upgrade pip.

```bash
pip install --upgrade pip
```

Install project dependencies.

```bash
pip install -r requirements.txt
```

Install DVC with Google Cloud Storage support.

```bash
pip install "dvc[gs]"
```

---

# Step 4: Authenticate Google Cloud

Login.

```bash
gcloud auth login
```

Set your project.

```bash
gcloud config set project PROJECT_ID
```

Verify.

```bash
gcloud config list
```

---

# Step 5: Configure DVC Remote

Verify the configured remote.

```bash
dvc remote list
```

Example output

```
storage gs://your-bucket-name
```

If the remote is missing, add it.

```bash
dvc remote add -d storage gs://your-bucket-name
```

---

# Step 6: Download Dataset and Model

Download all DVC tracked files.

```bash
dvc pull
```

or restore from the local cache.

```bash
dvc checkout
```

---

# Step 7: Verify Dataset

Check the dataset.

```bash
head data/iris.csv
```

Count rows.

```bash
wc -l data/iris.csv
```

---

# Step 8: Train the Model

Run the training script.

```bash
python train.py
```

The trained model will be saved as

```
model/model.joblib
```

---

# Step 9: Track Dataset with DVC

If the dataset changes,

```bash
dvc add data/iris.csv
```

---

# Step 10: Track Model with DVC

```bash
dvc add model/model.joblib
```

---

# Step 11: Push Data to Google Cloud Storage

```bash
dvc push
```

---

# Step 12: Commit Changes to Git

Add project files.

```bash
git add .
```

Commit.

```bash
git commit -m "Update ML pipeline"
```

Push to GitHub.

```bash
git push origin main
```

---

# Step 13: Switch Between Versions

View Git history.

```bash
git log --oneline
```

Checkout an older commit.

```bash
git checkout <commit-hash>
```

Restore dataset and model.

```bash
dvc checkout
```

or

```bash
dvc pull
```

Verify the restored dataset.

```bash
wc -l data/iris.csv
```

---

# Step 14: Return to the Latest Version

```bash
git checkout main
```

Restore the latest files.

```bash
dvc checkout
```

---

# DVC Commands

Initialize DVC

```bash
dvc init
```

Track dataset

```bash
dvc add data/iris.csv
```

Track model

```bash
dvc add model/model.joblib
```

Push files

```bash
dvc push
```

Pull files

```bash
dvc pull
```

Restore files

```bash
dvc checkout
```

List remote

```bash
dvc remote list
```

---

# Git Commands

Clone repository

```bash
git clone <repository-url>
```

Check repository status

```bash
git status
```

Commit changes

```bash
git commit -m "message"
```

Push changes

```bash
git push origin main
```

View commit history

```bash
git log --oneline
```

Switch commits

```bash
git checkout <commit-hash>
```

---

# Technologies Used

- Python
- Scikit-learn
- Git
- DVC
- Google Cloud Platform
- Google Cloud Storage
- Google Compute Engine

---

# Reproducibility

A reviewer can reproduce the project by executing the following commands:

```bash
git clone https://github.com/<username>/<repository>.git

cd <repository>

python3 -m venv .env

source .env/bin/activate

pip install -r requirements.txt

pip install "dvc[gs]"

dvc pull

python train.py
```

The repository contains only code and DVC metadata. All large datasets and trained models are stored in Google Cloud Storage and retrieved using DVC.
