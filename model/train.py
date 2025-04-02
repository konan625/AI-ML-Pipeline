import pandas as pd
from prophet import Prophet
import joblib
from minio import Minio

#Load data
def load_data(file_path):
    return pd.read_csv(file_path)

#Train the model
def train_model(data):
    model = Prophet()
    model.fit(data)
    return model

#Save model locally and update on minio
def save_model(model,local_path,bucket_name, object_name):
    #Save locally
    joblib.dump(model,local_path)
    print(f"Model saved locally at {local_path}")

    #update on minio
    client = Minio(
        "localhost:9000",
        access_key='minioadmin',
        secret_key='minioadmin',
        secure=False
    )

    client.fput_object(bucket_name,object_name,local_path)
    print(f"Model updated to minio bucket {bucket_name} as {object_name}")


#main function
if __name__=="__main__":
    #paths and configurations
    data_path = "./data.csv"
    model_local_path = "trained_model.pkl"
    minio_bucket = "trained-models"
    minio_object = "prophet_model.pkl"


    #load data
    data = load_data(data_path)

    #train model
    model = train_model(data)   

    #save and upload model
    save_model(model,model_local_path,minio_bucket,minio_object)