# Week 10 - LLMOps with Gemini Fine-Tuning

## Objective

Fine-tune Gemini models on two representations of the IRIS dataset and compare their performance.

---

## Dataset Versions

### Version 1

Raw feature representation.

Example:

sepal_length: 5.1, sepal_width: 3.5, petal_length: 1.4, petal_width: 0.2

Output:

setosa

### Version 2

Natural language representation.

Example:

A flower specimen has a sepal length of 5.1 cm, sepal width of 3.5 cm, petal length of 1.4 cm and petal width of 0.2 cm. Identify the iris species.

Output:

This is Iris setosa.

---

## Fine-Tuning

Two Gemini fine-tuning jobs were created:

- iris_v1
- iris_v2

Both used identical hyperparameters.

---

## Evaluation Results

| Metric | V1 | V2 |
|----------|----------|----------|
| Accuracy | 91.30% | 89.13% |
| Format Compliance | 100% | 100% |

### Conclusion

The raw feature representation slightly outperformed the natural language representation on the IRIS classification task.

Both models maintained perfect format compliance.
