# Stress Testing, Observability & Scaling the IRIS Pipeline

## Overview

This project demonstrates a complete Machine Learning Operations (MLOps) workflow for deploying, validating, monitoring, and scaling an IRIS Classification API on Google Kubernetes Engine (GKE).

The project extends the CI/CD pipeline from the previous assignment by integrating automated stress testing, Kubernetes Horizontal Pod Autoscaling (HPA), Google Cloud Monitoring, and Google Cloud Logging.

After every successful deployment, GitHub Actions automatically builds the Docker image, pushes it to Google Artifact Registry, deploys the latest version to GKE, and performs an automated stress test using `wrk`.

---

# Objectives

- Deploy a containerized Flask API on GKE
- Configure GitHub Actions for CI/CD
- Push Docker images to Artifact Registry
- Configure Horizontal Pod Autoscaler
- Perform stress testing using wrk
- Observe scaling behaviour
- Monitor CPU and memory usage
- Inspect application logs
- Compare performance under different scaling configurations

---

# Technology Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.12 |
| Framework | Flask |
| Machine Learning | Scikit-learn |
| Experiment Tracking | MLflow |
| Data Versioning | DVC |
| Containerization | Docker |
| Container Registry | Google Artifact Registry |
| Orchestration | Kubernetes |
| Cloud Platform | Google Cloud Platform |
| Cluster | Google Kubernetes Engine |
| CI/CD | GitHub Actions |
| Load Testing | wrk |
| Monitoring | Google Cloud Monitoring |
| Logging | Google Cloud Logging |

---

# Repository Structure

```
week_7
│
├── app.py
├── train.py
├── Dockerfile
├── deployment.yaml
├── service.yaml
├── hpa.yaml
├── requirements.txt
├── model/
│     model.joblib
│
└── .github/
      workflows/
            ci.yml
```

---

# Project Architecture

```
Developer
     │
     ▼
GitHub Repository
     │
     ▼
GitHub Actions
     │
     ├── Install Dependencies
     ├── Run Tests
     ├── Train Model
     ├── Build Docker Image
     ├── Push Image to Artifact Registry
     ├── Deploy to GKE
     └── Execute Stress Test
                │
                ▼
Google Kubernetes Engine
        │
        ▼
IRIS Prediction API
        │
        ▼
Horizontal Pod Autoscaler
        │
        ▼
Cloud Monitoring & Cloud Logging
```

---

# Prerequisites

- Python 3.12
- Docker
- Git
- Google Cloud SDK
- kubectl
- wrk
- Google Cloud Project
- GKE Cluster
- Artifact Registry Repository

---

# Clone Repository

```bash
git clone https://github.com/<username>/<repository>.git

cd <repository>
```

---

# Create Virtual Environment

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

# Install Dependencies

```bash
pip install --upgrade pip

pip install -r requirements.txt
```

---

# Train Model

```bash
python train.py
```

The script:

- Loads the IRIS dataset
- Trains Decision Tree Classifier
- Logs experiments using MLflow
- Stores model as

```
model/model.joblib
```

---

# Run API Locally

```bash
python app.py
```

Default endpoint

```
http://127.0.0.1:5000
```

Prediction

```bash
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{"features":[5.1,3.5,1.4,0.2]}'
```

---

# Build Docker Image

```bash
docker build -t iris-api .
```

Run container

```bash
docker run -p 5000:5000 iris-api
```

---

# Kubernetes Deployment

Deploy application

```bash
kubectl apply -f deployment.yaml
```

Deploy service

```bash
kubectl apply -f service.yaml
```

Verify deployment

```bash
kubectl get deployments

kubectl get pods

kubectl get svc
```

---

# Horizontal Pod Autoscaler

Create HPA

```bash
kubectl apply -f hpa.yaml
```

Verify

```bash
kubectl get hpa
```

Configuration

```
Minimum Replicas : 1

Maximum Replicas : 3

CPU Target : 50%
```

---

# GitHub Actions Workflow

The workflow performs the following automatically:

1. Checkout Repository
2. Setup Python
3. Install Dependencies
4. Authenticate with Google Cloud
5. Pull DVC Data
6. Train Model
7. Execute Unit Tests
8. Generate Test Report
9. Build Docker Image
10. Push Image to Artifact Registry
11. Deploy Latest Image to GKE
12. Wait for Rollout
13. Install wrk
14. Perform Automated Stress Test

---

# Stress Testing

Install

```bash
sudo apt install wrk
```

POST request script

```lua
wrk.method="POST"

wrk.headers["Content-Type"]="application/json"

wrk.body='{"features":[5.1,3.5,1.4,0.2]}'
```

Execute

```bash
wrk -t4 -c1000 -d60s -s post.lua http://<EXTERNAL_IP>/predict
```

Example Output

```
Requests/sec : 240

Latency : 623 ms

Socket Timeouts : 525
```

---

# Bottleneck Analysis

### Scenario 1

```
Max Replicas : 3

Connections : 1000
```

Observed

- Lower latency
- Higher throughput
- Additional Pods created
- Better request handling

---

### Scenario 2

```
Max Replicas : 1

Connections : 2000
```

Observed

- CPU saturation
- High latency
- Increased socket timeout
- Lower requests/sec
- Service bottleneck

---

# Monitoring

Google Cloud Monitoring was used to observe

- CPU Utilization
- Memory Usage
- Pod Scaling
- Cluster Resources
- Workload Metrics

---

# Logging

Google Cloud Logging was used to inspect

- Container Logs
- Flask Logs
- Pod Logs
- Runtime Errors
- Request Processing

---

# Useful Kubernetes Commands

```bash
kubectl get pods

kubectl get svc

kubectl get deployments

kubectl get hpa

kubectl top pods

kubectl top nodes

kubectl logs <pod>

kubectl describe pod <pod>

kubectl rollout status deployment/iris-api

kubectl rollout history deployment/iris-api
```

---

# GitHub Actions

Push changes

```bash
git add .

git commit -m "Week 7 Assignment"

git push origin week_7
```

The workflow automatically

- Builds Docker Image
- Pushes Image
- Deploys to GKE
- Executes Stress Test

---

# Performance Summary

| Configuration | Throughput | Latency | Result |
|--------------|-----------|---------|--------|
| 3 Replicas / 1000 Connections | High | Lower | Stable |
| 1 Replica / 2000 Connections | Low | High | Bottleneck Observed |

---

# Key Learnings

- Docker containerization
- Kubernetes deployments
- Google Kubernetes Engine
- Google Artifact Registry
- GitHub Actions CI/CD
- Workload Identity Federation
- Horizontal Pod Autoscaler
- Stress Testing with wrk
- Cloud Monitoring
- Cloud Logging
- Production deployment workflow
- Observability and scalability of ML APIs

---

# Future Improvements

- Canary Deployments
- Blue-Green Deployment
- Prometheus Metrics
- Grafana Dashboards
- Distributed Tracing
- HTTPS with Ingress
- Custom Metrics Autoscaling
- Automated Rollbacks

---


# Author

**Abhishek Dutta**

IIT Madras  
Diploma in Programming

GitHub: https://github.com/Abhishek-IITM2026

---

# License

This repository has been developed as part of the IIT Madras MLOps course for academic and educational purposes.
