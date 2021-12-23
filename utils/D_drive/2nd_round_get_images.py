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


def get_bucket_path(image_name):
    temp = image_name.split("_")
    location = temp[0]
    slide = temp[5][1:]
    
    return location,slide

def main():
    conn = psycopg2.connect("dbname = li_storage user= pgsql_master password=arvbedrock1234# host=bedrock-mlplatform-nonprod-pgsql.cluster-cq6wq7ckjmhj.ap-southeast-1.rds.amazonaws.com port = 5432")
    cur = conn.cursor()

    train = pd.read_sql_query("Select * From object_details where name like 'Car' and confidence >75", conn)


    #train = train.sort_values(by=['confidence']) and confidence >75
    #print(train)

    print(train['name'].value_counts())
    print(sum(train['name'].value_counts()))
    print(len(train['image_name'].unique()))

    

    BUCKET_NAME = 'location-intelligence'
    session = Session(aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY,
                      region_name='ap-southeast-1')
    s3 = session.resource('s3')
    client = s3.meta.client
    my_files = []
    response = client.list_objects_v2(Bucket=BUCKET_NAME, Prefix="google_street_view/image")
    files = response['Contents']
    my_files = my_files + [i['Key']
                           for i in files if i['Key'].endswith(".jpg")]
    
   
    try:
        token = response['NextContinuationToken']
        while True:
            response = client.list_objects_v2(
                Bucket=BUCKET_NAME, ContinuationToken=token)
            files = response['Contents']
            my_files = my_files + [i['Key']
                                    for i in files if i['Key'].endswith(".jpg")]
            token = response['NextContinuationToken']
    except:
        pass
    count = 0
    bad_count = 0
    #print(len(my_files))
    
    print('len my files:',len(my_files))
    print(len(train['image_name'].unique())) # 7035
    train_len = train['image_name']
    name_list=train['image_name'].tolist()
    print('name_list:',len(name_list)) # 15044
    for x in range(len(my_files)):
        print(my_files[x])
        image_names = my_files[x].split('/')[-1]
        print(image_names)
        # if x ==len(train['image_name'].unique()):
        #     break
        if image_names in name_list:
                print('found it')
                
                
                s3.meta.client.download_file(BUCKET_NAME, my_files[x], "11_15_2021_8th_test_corrupted/{}".format(image_names))
                print(count)
                count +=1
                if count ==len(train['image_name'].unique()):
                    break
        else:
            print('not found')
            print(image_names)
            bad_count+=1
    print('good count:', count)
    print('bad count:',bad_count)
if __name__== "__main__" :
    main()
    