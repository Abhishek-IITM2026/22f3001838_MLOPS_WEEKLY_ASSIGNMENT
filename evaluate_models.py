from google import genai
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report

PROJECT_ID = "project-32301d32-7dfb-43f1-b1a"
LOCATION = "us-central1"

V1_ENDPOINT = "projects/project-32301d32-7dfb-43f1-b1a/locations/us-central1/endpoints/3686869745874763776"
V2_ENDPOINT = "projects/project-32301d32-7dfb-43f1-b1a/locations/us-central1/endpoints/5597803362763407360"

client = genai.Client(
    vertexai=True,
    project=PROJECT_ID,
    location=LOCATION,
)

VALID = ["setosa", "versicolor", "virginica"]


def extract_species(text):
    text = text.lower()

    if "setosa" in text:
        return "setosa"

    if "versicolor" in text:
        return "versicolor"

    if "virginica" in text:
        return "virginica"

    return "invalid"


df = pd.read_csv("iris_test.csv")

actual = df["species"].str.lower().tolist()

v1_preds = []
v2_preds = []

print("Running V1...")

for _, row in df.iterrows():

    prompt = (
        f"Return ONLY one word: setosa, versicolor, or virginica.\n\n"
        f"sepal_length: {row.sepal_length}, "
        f"sepal_width: {row.sepal_width}, "
        f"petal_length: {row.petal_length}, "
        f"petal_width: {row.petal_width}"
    )

    response = client.models.generate_content(
        model=V1_ENDPOINT,
        contents=prompt
    )

    pred = extract_species(response.text)

    v1_preds.append(pred)

print("Running V2...")

for _, row in df.iterrows():

    prompt = (
        f"Return ONLY one word: setosa, versicolor, or virginica.\n\n"
        f"A flower specimen has a sepal length of {row.sepal_length} cm, "
        f"a sepal width of {row.sepal_width} cm, "
        f"a petal length of {row.petal_length} cm, "
        f"and a petal width of {row.petal_width} cm. "
        f"Identify the iris species."
    )

    response = client.models.generate_content(
        model=V2_ENDPOINT,
        contents=prompt
    )

    pred = extract_species(response.text)

    v2_preds.append(pred)

print("\n====================")
print("V1 ACCURACY")
print("====================")

print(accuracy_score(actual, v1_preds))

print(classification_report(actual, v1_preds))

v1_compliance = (
    sum(p in VALID for p in v1_preds)
    / len(v1_preds)
)

print("Format Compliance:", v1_compliance)

print("\n====================")
print("V2 ACCURACY")
print("====================")

print(accuracy_score(actual, v2_preds))

print(classification_report(actual, v2_preds))

v2_compliance = (
    sum(p in VALID for p in v2_preds)
    / len(v2_preds)
)

print("Format Compliance:", v2_compliance)
