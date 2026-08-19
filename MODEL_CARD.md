# Model Card: IRIS Flower Classification Model

## Model Details

- Model Type: Random Forest Classifier
- Framework: Scikit-learn
- Purpose: Classify Iris flowers into Setosa, Versicolor, and Virginica species.
- Training Environment: Google Cloud Platform (GCP)
- Repository Branch: week_9

---

## Training Data

Dataset: IRIS Dataset

Features:
- sepal_length
- sepal_width
- petal_length
- petal_width

Target:
- species

Classes:
- Setosa
- Versicolor
- Virginica

Sensitive Attribute Used for Fairness Audit:
- location (randomly assigned values 0 or 1)

Note:
The location attribute was NOT used during model training. It was introduced only for fairness evaluation.

---

## Intended Use

This model is intended for educational purposes to demonstrate:

- Classification
- Explainability using SHAP
- Fairness assessment using Fairlearn
- Drift detection
- ML governance concepts

The model is not intended for real-world decision-making systems.

---

## Performance Metrics

### Overall Performance

| Metric | Value |
|----------|----------|
| Accuracy | 1.00 |
| Precision | 1.00 |
| Recall | 1.00 |

### Fairness Metrics by Location

| Location | Accuracy | Precision | Recall |
|------------|------------|------------|------------|
| 0 | 1.00 | 1.00 | 1.00 |
| 1 | 1.00 | 1.00 | 1.00 |

Observation:

No measurable performance gap was observed between location groups.

---

## Explainability Findings

SHAP analysis was performed for all three classes.

Virginica predictions were primarily influenced by:

- High petal_length
- High petal_width

Features pushing predictions away from Virginica:

- Low petal_length
- Low petal_width

Interpretation:

Samples with larger petal measurements strongly increase the probability of being classified as Virginica.

---

## Drift Monitoring

A simulated production dataset was created by shifting the petal_length feature.

Drift Detection Results:

| Feature | Drift Status |
|-----------|-----------|
| sepal_length | No Drift |
| sepal_width | No Drift |
| petal_length | Drift Detected |
| petal_width | No Drift |

Implication:

Changes in petal_length distribution may reduce model reliability in production and should trigger monitoring alerts.

---

## Fairness Considerations

- Sensitive attribute: location
- Location was excluded from training.
- Fairlearn MetricFrame was used to compare subgroup performance.
- No significant bias was detected in this experiment.

---

## Known Limitations

- Small dataset (150 samples).
- Sensitive attribute was randomly generated and does not represent real demographics.
- Results should not be interpreted as evidence of real-world fairness.
- Drift analysis used simulated drift rather than live production data.

---

## Governance and Accountability

Author: Abhishek Dutta

Assignment:
Explainability, Fairness, and Drift in the IRIS Pipeline (Week 9)

Review Date:
August 2026
