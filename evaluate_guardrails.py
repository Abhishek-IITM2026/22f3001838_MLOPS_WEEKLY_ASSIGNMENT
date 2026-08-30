from google import genai
import pandas as pd
from sklearn.metrics import accuracy_score

from guardrails import (
    input_guardrail,
    output_guardrail
)

PROJECT_ID = "project-32301d32-7dfb-43f1-b1a"

LOCATION = "us-central1"

ENDPOINT = "projects/project-32301d32-7dfb-43f1-b1a/locations/us-central1/endpoints/3686869745874763776"

client = genai.Client(
    vertexai=True,
    project=PROJECT_ID,
    location=LOCATION,
)

df = pd.read_csv("iris_test.csv")

actual = df["species"].tolist()

preds = []

blocked_legitimate = 0

for _, row in df.iterrows():

    prompt = (
        f"sepal_length: {row.sepal_length}, "
        f"sepal_width: {row.sepal_width}, "
        f"petal_length: {row.petal_length}, "
        f"petal_width: {row.petal_width}"
    )

    result = input_guardrail(prompt)

    if result["blocked"]:

        blocked_legitimate += 1

        preds.append("invalid")

        continue

    response = client.models.generate_content(
        model=ENDPOINT,
        contents=prompt
    )

    pred = output_guardrail(
        response.text
    )

    preds.append(pred)

accuracy = accuracy_score(
    actual,
    preds
)

false_positive_rate = (
    blocked_legitimate
    /
    len(df)
)

print("\nAccuracy:", accuracy)

print(
    "False Positive Rate:",
    false_positive_rate
)
