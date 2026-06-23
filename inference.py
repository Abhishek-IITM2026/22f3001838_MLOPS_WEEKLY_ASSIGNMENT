import os
import sys
import argparse
import pandas as pd
import joblib
from google.cloud import storage

PROJECT_ID = "project-65113c9e-530b-4341-830"
BUCKET_NAME = "mlops-course-project-65113c9e-530b-4341-830-unique-week1"
BUCKET_URI = f"gs://{BUCKET_NAME}"
TARGET_COLUMN = "species"

def download_from_gcs(bucket_name, source_blob_name, destination_file_name):
    if source_blob_name.startswith("gs://"):
        source_blob_name = source_blob_name.replace(f"gs://{bucket_name}/", "")
        
    storage_client = storage.Client(project=PROJECT_ID)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    
    blob.download_to_filename(destination_file_name)
    print(f"Downloaded 'gs://{bucket_name}/{source_blob_name}' to local '{destination_file_name}'.")

def run_inference(eval_data_path, timestamp):
    model_gcs_path = f"artifacts/{timestamp}/model.joblib"
    local_model_path = f"downloaded_model_{timestamp}.joblib"
    local_dataset_path = "downloaded_eval_dataset.csv"

    download_from_gcs(BUCKET_NAME, model_gcs_path, local_model_path)
    download_from_gcs(BUCKET_NAME, eval_data_path, local_dataset_path)

    loaded_model = joblib.load(local_model_path)
    eval_data = pd.read_csv(local_dataset_path)

    if TARGET_COLUMN in eval_data.columns:
        X_eval = eval_data.drop(columns=[TARGET_COLUMN])
        y_actual = eval_data[TARGET_COLUMN]
    else:
        X_eval = eval_data
        y_actual = None

    predictions = loaded_model.predict(X_eval)

    eval_data['predictions'] = predictions
    print("\nPredictions sample:")
    print(eval_data[['predictions']].head())
    
    if y_actual is not None:
        from sklearn.metrics import accuracy_score
        accuracy = accuracy_score(y_actual, predictions)
        print(f"\nModel Accuracy on {eval_data_path}: {accuracy:.4f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run ML Inference dynamically using a specified bucket dataset and model timestamp.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("dataset", type=str, nargs="?", help="Path to the evaluation CSV file inside the bucket")
    parser.add_argument("timestamp", type=str, nargs="?", help="The exact timestamp of the model run")
    
    if len(sys.argv) == 1:
        parser.print_help()
        print("\n--- Interactive Mode ---")
        dataset_arg = input(f"Enter dataset path or link (e.g., iris.csv or {BUCKET_URI}/iris.csv): ").strip()
        timestamp_arg = input("Enter the model timestamp: ").strip()
    else:
        args = parser.parse_args()
        dataset_arg = args.dataset
        timestamp_arg = args.timestamp
        
        if not dataset_arg:
            dataset_arg = input(f"Enter dataset path: ").strip()
        if not timestamp_arg:
            timestamp_arg = input("Enter the model timestamp: ").strip()

    run_inference(dataset_arg, timestamp_arg)