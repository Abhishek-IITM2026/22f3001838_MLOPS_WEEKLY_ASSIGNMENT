import pandas as pd

from sklearn.model_selection import train_test_split

df = pd.read_csv("data/iris.csv")

train_df, test_df = train_test_split(
    df,
    test_size=0.2,
    random_state=42
)

test_df.to_csv(
    "iris_test.csv",
    index=False
)

print("Test set saved")
