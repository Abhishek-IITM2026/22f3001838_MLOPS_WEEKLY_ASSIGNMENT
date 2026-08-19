import shap
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("data/iris.csv")

X = df.drop("species", axis=1)
y = df["species"]

model = RandomForestClassifier(
    random_state=42
)

model.fit(X, y)

explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(X)

class_names = [
    "setosa",
    "versicolor",
    "virginica"
]

for i, class_name in enumerate(class_names):

    shap.summary_plot(
        shap_values[:, :, i],
        X,
        show=False
    )

    plt.title(
        f"SHAP Summary - {class_name}"
    )

    plt.savefig(
        f"{class_name}_summary.png"
    )

    plt.close()

print("SHAP plots generated.")
