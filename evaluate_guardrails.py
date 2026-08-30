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

BASELINE_ACCURACY = 0.9130434782608695

client = genai.Client(
    vertexai=True,
    project=PROJECT_ID,
    location=LOCATION,
)

df = pd.read_csv("iris_test.csv")

actual = df["species"].str.lower().tolist()

preds = []

blocked_legitimate = 0

for _, row in df.iterrows():

    prompt = (
    	f"Return ONLY one word: setosa, versicolor, or virginica.\n\n"
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

guarded_accuracy = accuracy_score(
    actual,
    preds
)

false_positive_rate = (
    blocked_legitimate
    /
    len(df)
)

accuracy_delta = (
    BASELINE_ACCURACY
    -
    guarded_accuracy
)

print("\nAccuracy:", guarded_accuracy)

print(
    "False Positive Rate:",
    false_positive_rate
)

print(
    "Accuracy Delta:",
    accuracy_delta
)

if false_positive_rate > 0.1:
    raise Exception(
        f"False Positive Rate too high: {false_positive_rate}"
    )
