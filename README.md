# Week 9 - Explainability, Fairness and Drift in the IRIS Pipeline

## Objective

This assignment demonstrates Responsible AI practices by integrating:

- Fairness Analysis using Fairlearn
- Explainability using SHAP
- Drift Detection using Statistical Tests
- Model Governance using a Model Card

The work was performed on Google Cloud Platform (GCP) as part of the IIT Madras MLOps course.

---

# Project Structure

```text
.
├── data/
│   └── iris.csv
│
├── fairness_analysis.py
├── shap_analysis.py
├── drift_detection.py
├── MODEL_CARD.md
│
├── setosa_summary.png
├── versicolor_summary.png
├── virginica_summary.png
│
└── README.md
```

---

# Dataset

The IRIS dataset contains:

- sepal_length
- sepal_width
- petal_length
- petal_width
- species

A synthetic sensitive attribute called `location` is added for fairness auditing.

Location values:

```python
0
1
```

The location feature is NOT used for training.

It is only used for fairness evaluation.

---

# Task 1: Sensitive Attribute Creation

A new column called `location` was introduced.

```python
df["location"] = np.random.randint(
    0,
    2,
    size=len(df)
)
```

Why?

- Simulates demographic groups
- Enables fairness analysis
- Prevents leakage because it is excluded from model training

Training features:

```python
X = df.drop(
    ["species", "location"],
    axis=1
)
```

---

# Task 2: Fairness Analysis

File:

```bash
fairness_analysis.py
```

Library used:

```python
from fairlearn.metrics import MetricFrame
```

Metrics evaluated:

- Accuracy
- Precision
- Recall

Run:

```bash
python fairness_analysis.py
```

Example Output:

```text
=== OVERALL ===

accuracy     1.0
precision    1.0
recall       1.0

=== BY LOCATION ===

location
0   accuracy=1.0
1   accuracy=1.0
```

Interpretation:

- Both groups perform equally.
- No measurable bias exists.
- This is expected because location was randomly assigned.

---

# Task 3: Explainability using SHAP

File:

```bash
shap_analysis.py
```

Library used:

```python
import shap
```

Run:

```bash
python shap_analysis.py
```

Generated files:

```text
setosa_summary.png
versicolor_summary.png
virginica_summary.png
```

---

## Understanding SHAP

SHAP values explain how each feature contributes to a prediction.

### SHAP Value

- Positive value → pushes prediction toward a class
- Negative value → pushes prediction away from a class

### Colors

- Red → high feature value
- Blue → low feature value

---

## Virginica Interpretation

From the SHAP summary plot:

### Features pushing toward Virginica

- High petal_length
- High petal_width

These appear as:

- Red dots
- Right side of the plot

### Features pushing away from Virginica

- Low petal_length
- Low petal_width

These appear as:

- Blue dots
- Left side of the plot

Conclusion:

The model primarily identifies Virginica using petal measurements.

---

# Task 4: Data Drift Detection

File:

```bash
drift_detection.py
```

Production drift simulated by modifying:

```python
production_df["petal_length"] += 2
```

Run:

```bash
python drift_detection.py
```

Example Output:

```text
=== DRIFT REPORT ===

sepal_length
NO DRIFT

sepal_width
NO DRIFT

petal_length
DRIFT DETECTED

petal_width
NO DRIFT
```

---

## Statistical Method

Kolmogorov-Smirnov Test

```python
from scipy.stats import ks_2samp
```

Decision Rule:

```python
p-value < 0.05
```

Result:

- petal_length distribution changed significantly
- Drift detected successfully

---

# Data Drift vs Concept Drift

## Data Drift

Input feature distributions change.

Example:

```text
Petal Length:
Training Mean = 3.7
Production Mean = 5.7
```

Detected using:

- KS Test
- Distribution plots
- Statistical monitoring

---

## Concept Drift

Relationship between features and labels changes.

Example:

```text
Same flower measurements
Different species labels
```

Requires:

- Ground truth labels
- Continuous model evaluation

---

# Task 5: Model Governance

Model governance was documented using:

```text
MODEL_CARD.md
```

The model card includes:

- Intended Use
- Training Data
- Performance
- Fairness Results
- Known Limitations
- Governance Notes

---

# How to Execute

Activate environment:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install fairlearn shap matplotlib scipy scikit-learn pandas
```

Run Fairness Analysis:

```bash
python fairness_analysis.py
```

Run SHAP Analysis:

```bash
python shap_analysis.py
```

Run Drift Detection:

```bash
python drift_detection.py
```

---

# Generated Outputs

## Fairness

Console output showing:

- Accuracy
- Precision
- Recall

for each location group.

---

## Explainability

Generated SHAP plots:

```text
setosa_summary.png
versicolor_summary.png
virginica_summary.png
```

---

## Drift Detection

Console report:

```text
DRIFT DETECTED
NO DRIFT
```

for each feature.

---

# Key Learnings

### Fairness

- Models can be audited using sensitive attributes.
- Performance should be compared across groups.

### Explainability

- SHAP explains feature contributions.
- Petal measurements are most important for IRIS classification.

### Drift Monitoring

- Production data changes over time.
- Drift can degrade model performance.

### Governance

- Model cards improve transparency.
- Responsible AI requires documentation and monitoring.

---

# Technologies Used

- Python
- Scikit-learn
- Fairlearn
- SHAP
- Pandas
- NumPy
- SciPy
- Matplotlib
- Google Cloud Platform (GCP)

---

# Author

Abhishek Dutta

IIT Madras MLOps Program

Week 9 Assignment – Explainability, Fairness and Drift in the IRIS Pipeline
