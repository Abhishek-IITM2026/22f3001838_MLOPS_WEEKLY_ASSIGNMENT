import os
import joblib
import pandas as pd
import functions_framework
from google.cloud import storage
from io import BytesIO

storage_client = storage.Client()

def get_latest_model(bucket_name):
    """Fetches the latest model.joblib based on the timestamp folder."""
    bucket = storage_client.bucket(bucket_name)
    blobs = list(bucket.list_blobs(prefix="model/"))
    
    model_blobs = [b for b in blobs if b.name.endswith("model.joblib")]
    
    if not model_blobs:
        raise FileNotFoundError(f"No model.joblib found in bucket: {bucket_name}")
        
    latest_blob = sorted(model_blobs, key=lambda x: x.name)[-1]
    
    print(f"Downloading latest model: {latest_blob.name}")
    local_model_path = "/tmp/model.joblib"
    latest_blob.download_to_filename(local_model_path)
    
    return local_model_path

# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def process_data(cloud_event):
    # 1. Extract bucket and file name directly from the event payload
    data = cloud_event.data
    bucket_name = data["bucket"]
    file_name = data["name"]

    print(f"Event triggered for file: gs://{bucket_name}/{file_name}")

    # ---------------------------------------------------------
    # 2. INFINITE LOOP PREVENTION
    # Ignore the file if it is already an output file
    # ---------------------------------------------------------
    if file_name.startswith("outputs/") or "predicted_" in file_name:
        print(f"Skipping output file: {file_name}")
        return

    try:
        # 3. Download the newly uploaded CSV data
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(file_name)
        data_bytes = blob.download_as_bytes()
        df = pd.read_csv(BytesIO(data_bytes))
        
        # 4. Extract features
        features = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
        
        # 5. Load the latest trained model
        local_model_path = get_latest_model(bucket_name)
        model = joblib.load(local_model_path)
        
        # 6. Run Inference
        predictions = model.predict(features)
        df['predicted_species'] = predictions
        
        # 7. Save the output back to GCS in an 'outputs/' folder
        base_name = os.path.basename(file_name)
        out_name = f"outputs/predicted_{base_name}"
        
        out_blob = bucket.blob(out_name)
        out_blob.upload_from_string(df.to_csv(index=False), content_type="text/csv")
        
        print(f"Successfully uploaded predictions to gs://{bucket_name}/{out_name}")

    except Exception as e:
        print(f"Error processing {file_name}: {str(e)}")
        # Raise the error so it shows up as a failure in GCP logs
        raise e
