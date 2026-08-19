import pandas as pd

from scipy.stats import ks_2samp

df = pd.read_csv("data/iris.csv")

train_df = df.drop(
    "species",
    axis=1
)

production_df = train_df.copy()

# Simulate drift
production_df["petal_length"] += 2

print("\n=== DRIFT REPORT ===")

for col in train_df.columns:

    stat, p = ks_2samp(
        train_df[col],
        production_df[col]
    )

    print(
        f"{col} | p-value={p}"
    )

    if p < 0.05:
        print("DRIFT DETECTED")
    else:
        print("NO DRIFT")
