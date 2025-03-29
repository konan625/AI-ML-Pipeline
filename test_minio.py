from minio import Minio
from minio.error import S3Error

#making a minio client
client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False # it will be set to true if we are using https
)

#bucket_name
bucket_name="raw-data"

#check if bucket exists or not
if not client.bucket_exists(bucket_name):
    client.make_bucket(bucket_name)
    print(f"Bucket '{bucket_name}' created")
else:
    print(f"Bucket '{bucket_name}' already exists")


#file
file_path = "airline-passengers.csv"
object_name = "test.csv"

try:
    client.fput_object(bucket_name,object_name,file_path)
    print(f"File '{file_path}' uploaded to {bucket_name} as {object_name}")
except S3Error as e:
    print(f"Error uploading file: {e}")


#downloading the file
download_path="download_test.csv"
client.fget_object(bucket_name,object_name,download_path)
print(f"file {object_name} downloaded from minio")