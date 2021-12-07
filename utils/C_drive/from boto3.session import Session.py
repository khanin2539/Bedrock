from boto3.session import Session
import json
import os
with open('secrets.json', 'r') as f:
    env = json.load(f)
# login with AWS key
ACCESS_KEY = env['ACCESS_KEY']
SECRET_KEY = env['SECRET_KEY']
session = Session(aws_access_key_id=ACCESS_KEY,
                  aws_secret_access_key=SECRET_KEY,
                  region_name='ap-southeast-1')
s3 = session.resource('s3')
client = s3.meta.client

def download_file(BUCKET_NAME, OBJECT_NAME):
    files = client.list_objects_v2(Bucket=BUCKET_NAME,)['Contents']
    files = [i['Key'] for i in files]
    for file in files:
        try:
            client.download_file(BUCKET_NAME, file, file)
        except:
            os.makedirs(file, exist_ok=True)
def upload_file(BUCKET_NAME, OBJECT_NAME):
    for root,dirs,files in os.walk(OBJECT_NAME):
        for file in files:
            client.upload_file(os.path.join(root,file), BUCKET_NAME, os.path.join(root,file))
    
    
def delete_file(BUCKET_NAME, OBJECT_NAME):
    files = client.list_objects_v2(Bucket=BUCKET_NAME,)['Contents']
    files = [i['Key'] for i in files]
    for file in files:
        client.delete_object(Bucket=BUCKET_NAME, Key=file)
        
# select path
BUCKET_NAME = "location-intelligence-storage"
OBJECT_NAME = "sample-area"
# download_file(BUCKET_NAME, OBJECT_NAME)
# upload_file(BUCKET_NAME, OBJECT_NAME)
# delete_file(BUCKET_NAME, OBJECT_NAME)























