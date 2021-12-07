from boto3.session import Session
import boto3
import json
import os
# with open('secrets.json', 'r') as f:
#     env = json.load(f)
# # login with AWS key
ACCESS_KEY = "AKIAZQ7I5QVNSWAU4A6S"
SECRET_KEY = "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"
session = Session(aws_access_key_id=ACCESS_KEY,
                  aws_secret_access_key=SECRET_KEY,
                  region_name='ap-southeast-1')
#s3 = session.resource('s3')
#client = s3.meta.client
BUCKET_NAME = "location-intelligence-storage"
OBJECT_NAME = "sample-area"

client = boto3.client("s3",
                      aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY,
                      region_name="ap-southeast-1")

resp = client.select_object_content(
    Bucket=BUCKET_NAME,
    Key='MrtSutthisan_img_13-7816157_100-5736872_a349_s90_y75_f90_0.json',
    ExpressionType='SQL',
    Expression="""  SELECT s.name FROM s3object s  """,
    InputSerialization = {'JSON': {"FileHeaderInfo": "DOCUMENT"}, 'CompressionType': 'NONE'},
    OutputSerialization = {'CSV': {}, 
                           },
)
data = [event['Records']['Payload'].decode('utf-8')
        for event in resp['Payload'] if 'Records' in event
        ]
for x in data:
    print(x)

# def download_file(BUCKET_NAME, OBJECT_NAME):
#     files = client.list_objects_v2(Bucket=BUCKET_NAME,)['Contents']
#     files = [i['Key'] for i in files]
#     for file in files:
#         try:
#             client.download_file(BUCKET_NAME, file, file)
#         except:
#             os.makedirs(file, exist_ok=True)
# def upload_file(BUCKET_NAME, OBJECT_NAME):
#     for root,dirs,files in os.walk(OBJECT_NAME):
#         for file in files:
#             client.upload_file(os.path.join(root,file), BUCKET_NAME, os.path.join(root,file))
    
    
# def delete_file(BUCKET_NAME, OBJECT_NAME):
#     files = client.list_objects_v2(Bucket=BUCKET_NAME,)['Contents']
#     files = [i['Key'] for i in files]
#     for file in files:
#         client.delete_object(Bucket=BUCKET_NAME, Key=file)
#def get_car_pic(BUCKET_NAME, OBJECT_NAME):

# select path
BUCKET_NAME = "location-intelligence-storage"
OBJECT_NAME = "sample-area"
# download_file(BUCKET_NAME, OBJECT_NAME)
# upload_file(BUCKET_NAME, OBJECT_NAME)
# delete_file(BUCKET_NAME, OBJECT_NAME)























