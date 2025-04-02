import pandas as pd
from prophet import Prophet
import joblib
from minio import Minio

#load the model from minio
def load_model(local_path,bucket_name,object_name):
    client = Minio(
        "localhost:9000",
        access_key="minioadmin",
        secret_key="minioadmin",
        secure=False
    )
    client.fget_object(bucket_name,object_name,local_path)
    print(f"Model downloaded from Minio bucket {bucket_name} as {object_name}")


    # Load the model using joblib
    model = joblib.load(local_path)
    return model  # Return the loaded model


#Generate predictions
def generate_forecast(model,periods):
    future = model.make_future_dataframe(periods=periods)
    forcast = model.predict(future)
    return forcast[['ds','yhat','yhat_lower','yhat_upper']]


#Save predcitions locally and uplaod to minio
def save_predictions(predictions,local_path,bucket_name,object_name):
    predictions.to_csv(local_path, index=False)
    print(f"Predictions saved locally at {local_path}")


    client = Minio(
        "localhost:9000",
        access_key="minioadmin",
        secret_key="minioadmin",
        secure=False
    )

    client.fput_object(bucket_name,object_name,local_path)
    print(f"Predictions uploaded to Minio bucket {bucket_name} as {object_name}")


#Main function
if __name__ =="__main__":
    model_local_path = "trained_model.pkl"
    minio_bucket = "trained-models"
    minio_object = "prophet_model.pkl"
    predictions_local_path = "predictions.csv"
    predictions_minio_bucket = "predictions"
    predictions_minio_object = "forecast.csv"

    #loading the model
    model = load_model(model_local_path,minio_bucket,minio_object)

    #generate predictions
    forecast = generate_forecast(model,periods=12)

    #save and upload predictions
    save_predictions(forecast,predictions_local_path,predictions_minio_bucket,predictions_minio_object)