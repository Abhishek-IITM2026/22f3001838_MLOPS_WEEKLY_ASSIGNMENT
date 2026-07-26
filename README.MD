# IRIS Classification MLOps Pipeline

## IIT Madras – MLOps Weekly Assignment (Week 6)

---

# Project Overview

This project demonstrates a complete end-to-end Machine Learning Operations (MLOps) pipeline for the IRIS Flower Classification problem.

The objective is to automate the entire machine learning lifecycle, beginning with data versioning and model training, followed by experiment tracking, continuous integration, containerization, continuous deployment, and cloud-based serving of predictions.

The project integrates several modern MLOps tools and practices including:

- MLflow for experiment tracking and model registry
- DVC for dataset versioning
- Flask for serving the machine learning model
- Docker for containerization
- GitHub Actions for Continuous Integration and Continuous Deployment
- Google Artifact Registry for storing Docker images
- Google Kubernetes Engine (GKE) for application deployment

---

# Objectives

The objectives of this project are:

- Develop an IRIS flower classification model.
- Track machine learning experiments using MLflow.
- Version datasets using DVC.
- Build a REST API for inference using Flask.
- Containerize the application using Docker.
- Automate testing using GitHub Actions.
- Store Docker images in Google Artifact Registry.
- Deploy the application on Google Kubernetes Engine.
- Build a complete CI/CD pipeline for automated deployment.

---

# Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python 3.12 |
| Machine Learning | Scikit-Learn |
| Experiment Tracking | MLflow |
| Data Versioning | DVC |
| REST API | Flask |
| Containerization | Docker |
| Container Registry | Google Artifact Registry |
| Orchestration | Kubernetes (GKE) |
| CI/CD | GitHub Actions |
| Cloud Platform | Google Cloud Platform |
| Version Control | Git & GitHub |

---

# Repository Structure

```text
22f3001838_MLOPS_WEEKLY_ASSIGNMENT
│
├── app.py
├── train.py
├── Dockerfile
├── deployment.yaml
├── service.yaml
├── requirements.txt
├── dvc.yaml
├── dvc.lock
│
├── data/
│   └── iris.csv
│
├── model/
│   └── model.joblib
│
├── tests/
│   ├── test_data.py
│   └── test_model.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
└── README.md
```

---

# Project Workflow

```text
                    Git Push
                        │
                        ▼
               GitHub Actions
                        │
          ┌─────────────┴─────────────┐
          │                           │
          ▼                           ▼
   Run Unit Tests              Train Model
          │                           │
          └─────────────┬─────────────┘
                        ▼
                 MLflow Logging
                        │
                        ▼
               Build Docker Image
                        │
                        ▼
          Push Image to Artifact Registry
                        │
                        ▼
      Deploy to Google Kubernetes Engine
                        │
                        ▼
             Flask Prediction API
```

---

# Dataset

The project uses the IRIS dataset available in Scikit-Learn.

### Features

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

### Target Classes

- Iris Setosa
- Iris Versicolor
- Iris Virginica

---

# Machine Learning Pipeline

The training pipeline consists of the following stages:

1. Load the IRIS dataset.
2. Split the dataset into training and testing sets.
3. Train a Decision Tree classifier.
4. Evaluate model accuracy.
5. Log parameters and metrics using MLflow.
6. Register the trained model.
7. Save the trained model as `model.joblib`.

---

# Experiment Tracking using MLflow

MLflow is used for:

- Tracking experiments
- Logging parameters
- Logging evaluation metrics
- Registering trained models
- Managing model versions

Each training run records:

- Accuracy
- Hyperparameters
- Model artifacts
- Execution details

---

# Data Version Control (DVC)

DVC is used to manage dataset versions.

Advantages include:

- Dataset reproducibility
- Version control for large files
- Easy collaboration
- Pipeline reproducibility

Useful commands:

```bash
dvc add data/iris.csv
dvc push
dvc pull
```

---

# Flask Inference API

The trained model is exposed through a Flask REST API.

### Endpoint

```
POST /predict
```

### Sample Request

```json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

### Sample Response

```json
{
  "prediction": "setosa"
}
```

---

# Docker Containerization

The application is packaged into a Docker image.

Build the image:

```bash
docker build -t iris-api .
```

Run the container:

```bash
docker run -p 5000:5000 iris-api
```

The Docker image contains:

- Flask application
- Trained model
- Python dependencies
- REST API

---

# Google Artifact Registry

Docker images are stored in Google Artifact Registry.

Repository:

```
us-central1-docker.pkg.dev/project-32301d32-7dfb-43f1-b1a/iris-repo
```

Push an image:

```bash
docker push us-central1-docker.pkg.dev/project-32301d32-7dfb-43f1-b1a/iris-repo/iris-api
```

---

# Google Kubernetes Engine

The application is deployed on Google Kubernetes Engine.

Deploy the application:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

Verify deployment:

```bash
kubectl get deployments
kubectl get pods
kubectl get svc
```

Check deployment rollout:

```bash
kubectl rollout status deployment/iris-api
```

---

# Continuous Integration

The GitHub Actions workflow automatically performs:

- Repository checkout
- Python environment setup
- Dependency installation
- DVC data retrieval
- Model training
- Unit testing
- Report generation

---

# Continuous Deployment

After successful completion of the CI pipeline, the workflow automatically:

1. Authenticates with Google Cloud.
2. Configures Docker authentication.
3. Builds the Docker image.
4. Pushes the image to Artifact Registry.
5. Connects to Google Kubernetes Engine.
6. Updates the Kubernetes deployment.
7. Applies Kubernetes manifests.
8. Verifies successful rollout.

---

# CI/CD Architecture

```text
Developer
    │
    ▼
Git Push
    │
    ▼
GitHub Actions
    │
    ├── Unit Tests
    ├── Model Training
    ├── Docker Build
    ├── Docker Push
    └── Kubernetes Deployment
                │
                ▼
Google Artifact Registry
                │
                ▼
Google Kubernetes Engine
                │
                ▼
Flask Prediction API
```

---

# Running the Project Locally

Clone the repository:

```bash
git clone https://github.com/Abhishek-IITM2026/22f3001838_MLOPS_WEEKLY_ASSIGNMENT.git
```

Navigate to the project:

```bash
cd 22f3001838_MLOPS_WEEKLY_ASSIGNMENT
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Train the model:

```bash
python train.py
```

Run the API:

```bash
python app.py
```

---

# Testing the API

```bash
curl http://localhost:5000/predict \
-H "Content-Type: application/json" \
-d '{"features":[5.1,3.5,1.4,0.2]}'
```

Expected response:

```json
{
  "prediction": "setosa"
}
```

---

# Learning Outcomes

This project provided practical experience with:

- Machine Learning model deployment
- MLflow experiment tracking
- Dataset versioning using DVC
- REST API development with Flask
- Docker containerization
- Kubernetes deployments
- Google Artifact Registry
- Google Kubernetes Engine
- GitHub Actions
- Continuous Integration
- Continuous Deployment
- Secure cloud authentication using Workload Identity Federation

---

# Author

**Abhishek Dutta**

IIT Madras  
Diploma in Programming

GitHub: https://github.com/Abhishek-IITM2026

---

# License

This repository has been developed as part of the IIT Madras MLOps course for academic and educational purposes.
