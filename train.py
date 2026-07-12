import sys
import pandas as pd
import numpy as np
import joblib
import os
from sklearn.tree import DecisionTreeClassifier

# Get iteration number from command line (default to 1)
iteration = int(sys.argv[1]) if len(sys.argv) > 1 else 1

# 1. Load YOUR base data
# Ensure your target column is appropriately named in your CSV. 
# We'll assume the last column is the target for this example.
df = pd.read_csv('data/iris.csv')

# 2. Augment data (add 20 noisy rows per iteration beyond the first)
if iteration > 1:
    np.random.seed(iteration)
    noise = df.sample(n=20 * iteration, replace=True)
    # Add slight numeric noise to the feature columns (all but the last column)
    noise.iloc[:, :-1] += np.random.normal(0, 0.5, size=(len(noise), df.shape[1] - 1))
    df = pd.concat([df, noise], ignore_index=True)

# Ensure directories exist
os.makedirs('data', exist_ok=True)
os.makedirs('model', exist_ok=True)

# 3. Save augmented data (Overwriting the local file so DVC can track the change)
df.to_csv('data/iris.csv', index=False)

# 4. Train model (Assuming the target column is the last column)
X, y = df.iloc[:, :-1], df.iloc[:, -1]
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X, y)

# 5. Save model
model_path = 'model/model.joblib'
joblib.dump(clf, model_path)

print(f"Iteration {iteration} complete | Data size: {len(df)} rows | Saved model to: {model_path}")
