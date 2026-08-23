import pandas as pd
import json

df = pd.read_csv("data/iris.csv")

with open("iris_v1.jsonl", "w") as f:
    for _, row in df.iterrows():
        record = {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {
                            "text":
                            f"sepal_length: {row['sepal_length']}, "
                            f"sepal_width: {row['sepal_width']}, "
                            f"petal_length: {row['petal_length']}, "
                            f"petal_width: {row['petal_width']}"
                        }
                    ]
                },
                {
                    "role": "model",
                    "parts": [
                        {
                            "text": row["species"]
                        }
                    ]
                }
            ]
        }

        f.write(json.dumps(record) + "\n")

print("iris_v1.jsonl created")
