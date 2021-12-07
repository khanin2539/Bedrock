import pandas as pd
import psycopg2
date_format = "%Y-%m-%d"
import sys, os
import time
from boto3.session import Session
import boto3
import json
import os
import cv2
import numpy as np 
from matplotlib import pyplot

ACCESS_KEY = "AKIAZQ7I5QVNSWAU4A6S"
SECRET_KEY = "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"
BUCKET_NAME = "location-intelligence-storage"

# client = boto3.client("s3",
#                       aws_access_key_id=ACCESS_KEY,
#                       aws_secret_access_key=SECRET_KEY,
#                       region_name="ap-southeast-1")

# s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY,
#                       aws_secret_access_key=SECRET_KEY,
#                       region_name="ap-southeast-1")

key = "poc/ChockChai4/270/ChokChai4_img_13-7954807_100-6031016_a187-21598902886774_s270_y0_f90_1.jpg"
key1= "poc/ChockChai4/270/ChokChai4_img_13-7954807_100-6031016_a187-21598902886774_s270_y0_f90_1.jpg"
#s3.Object('location-intelligence',key).copy_from(CopySource=f'{BUCKET_NAME}/{key}')

def get_bucket_path(image_name):
    temp = image_name.split("_")
    location = temp[0]
    slide = temp[5][1:]
    
    return location,slide

def main():
    conn = psycopg2.connect("dbname = li_storage user = pgsql_master password=arvbedrock1234# host=bedrock-mlplatform-nonprod-pgsql.cluster-cq6wq7ckjmhj.ap-southeast-1.rds.amazonaws.com port = 5432")
    cur = conn.cursor()

    train = pd.read_sql_query("Select * From object_details where name like 'Car' and confidence >75", conn)


    #train = train.sort_values(by=['confidence']) and confidence >75
    #print(train)

    print(train['name'].value_counts())
    print(sum(train['name'].value_counts()))

    # for idx in range(len(train['obj_id'])):
    #     location,slide = get_bucket_path(train['image_name'][idx])
    #     if location == "ChokChai4" :
    #         location = "ChockChai4"

    #     OBJECT_NAME =  "google_streeet_view/%s/%s/%s" % ( location,slide,train['image_name'][idx])
    #     print(OBJECT_NAME)
    #     confi = train['confidence'][idx]


    BUCKET_NAME = 'location-intelligence'
    session = Session(aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY,
                      region_name='ap-southeast-1')
    s3 = session.resource('s3')
    client = s3.meta.client
    my_files = []
    response = client.list_objects_v2(Bucket=BUCKET_NAME)
    files = response['Contents']
    my_files = my_files + [i['Key']
                           for i in files if i['Key'].endswith(".jpg")]
    token = response['NextContinuationToken']
    while True:
        try:
            response = client.list_objects_v2(
                Bucket=BUCKET_NAME, ContinuationToken=token)
            files = response['Contents']
            my_files = my_files + [i['Key']
                                   for i in files if i['Key'].endswith(".jpg")]
            token = response['NextContinuationToken']
        except:
            break
    count = 0
    print(len(my_files))
    for x in range(sum(train['name'].value_counts())):
        image_names = my_files[x].split('/')[-1]
        print(image_names)
        for y in range(len(train['image_name'])):
            if image_names == train['image_name'][y]:
                print('found it')
                
                s3.meta.client.download_file(BUCKET_NAME, my_files[x], "11_15_2021_gsv_images/11_15_2021_gsv_images/3rd_round_get_images/{}_{}".format(train['obj_id'][y], image_names))
                print(count)
                count +=1
    print(count)
if __name__== "__main__" :
    main()
    