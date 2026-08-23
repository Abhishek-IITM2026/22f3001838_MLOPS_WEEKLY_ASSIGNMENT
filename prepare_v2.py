import pandas as pd
import json

df = pd.read_csv("data/iris.csv")

with open("iris_v2.jsonl", "w") as f:
    for _, row in df.iterrows():

        prompt = (
            f"A flower specimen has a sepal length of {row['sepal_length']} cm, "
            f"a sepal width of {row['sepal_width']} cm, "
            f"a petal length of {row['petal_length']} cm, "
            f"and a petal width of {row['petal_width']} cm. "
            f"Identify the iris species."
        )

        record = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": prompt}]
                },
                {
                    "role": "model",
                    "parts": [
                        {
                            "text": f"This is Iris {row['species']}."
                        }
                    ]
                }
            ]
        }

        f.write(json.dumps(record) + "\n")

print("iris_v2.jsonl created")
