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

s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY,
                      region_name="ap-southeast-1")

key = "poc/ChockChai4/270/ChokChai4_img_13-7954807_100-6031016_a187-21598902886774_s270_y0_f90_1.jpg"
key1= "poc/ChockChai4/270/ChokChai4_img_13-7954807_100-6031016_a187-21598902886774_s270_y0_f90_1.jpg"
#s3.Object('location-intelligence',key).copy_from(CopySource=f'{BUCKET_NAME}/{key}')

def get_bucket_path(image_name):
    temp = image_name.split("_")
    location = temp[0]
    slide = temp[5][1:]
    
    return location,slide

def main():
    conn = psycopg2.connect("dbname = li_poc user = pgsql_master password=arvbedrock1234# host=bedrock-mlplatform-nonprod-pgsql.cluster-cq6wq7ckjmhj.ap-southeast-1.rds.amazonaws.com port = 5432")
    cur = conn.cursor()

    train = pd.read_sql_query("Select obj_id, name, confidence, width, height, top, image_name From object_details where name like 'Car' or name like 'Van' or name like 'Truck' and confidence>76", conn)


    #train = train.sort_values(by=['confidence'])
    print(train)

    print(train['name'].value_counts())
    sum(train['name'].value_counts())


    # a = np.array(train['confidence'])
    # pyplot.plot(a)
    # print(len(a))
    # zero = np.percentile(a, 0)
    # print(zero)
    # tenth = np.percentile(a, 10) # return 50th percentile, e.g median.
    # print(tenth)
    # twenty = np.percentile(a, 20) # return 50th percentile, e.g median.
    # print(twenty)
    # thirty = np.percentile(a, 30) # return 50th percentile, e.g median.
    # print(thirty)
    # fourty = np.percentile(a, 40) # return 50th percentile, e.g median.
    # print(fourty)
    # fifty = np.percentile(a, 50) # return 50th percentile, e.g median.
    # print(fifty)
    # sixty = np.percentile(a, 60) # return 50th percentile, e.g median.
    # print(sixty)
    # seventy = np.percentile(a, 70) # return 50th percentile, e.g median.
    # print(seventy)
    # eighty = np.percentile(a, 80) # return 50th percentile, e.g median.
    # print(eighty)
    # ninety = np.percentile(a, 90) # return 50th percentile, e.g median.
    # print(ninety)
    # hundred = np.percentile(a, 100) # return 50th percentile, e.g median.
    # print(hundred)
    # count = 0

    # #len(train['obj_id'])
    # for idx in range(len(train['obj_id'])):
    
    #     location,slide = get_bucket_path(train['image_name'][idx])
    #     if location == "ChokChai4" :
    #         location = "ChockChai4"
    
    #     OBJECT_NAME =  "poc/%s/%s/%s" % ( location,slide,train['image_name'][idx])
    #     print(OBJECT_NAME)
    #     confi = train['confidence'][idx]

    #     if zero<= confi <= tenth:
    #         print('percentile tenth',confi)
    #         print(train['confidence'][idx])
    #         print(train['image_name'][idx])
    #         print(train['name'][idx])
    #         s3.meta.client.download_file('location-intelligence-storage', OBJECT_NAME, "percentiled/10/{}_{}_{}".format(train['confidence'][idx], train['name'][idx],train['image_name'][idx]))
            
    #         count+=1

    #     elif tenth< confi <= twenty:
    #         print('percentile twenty',confi)
    #         print(train['confidence'][idx])
    #         print(train['image_name'][idx])
    #         print(train['name'][idx])
    #         s3.meta.client.download_file('location-intelligence-storage', OBJECT_NAME, "percentiled/20/{}_{}_{}".format(train['confidence'][idx], train['name'][idx],train['image_name'][idx]))
    #         count+=1
    #             #101
    #     elif twenty< confi <= thirty:
    #         print('percentile thirty',confi)
    #         print(train['confidence'][idx])
    #         print(train['image_name'][idx])
    #         print(train['name'][idx])
    #         s3.meta.client.download_file('location-intelligence-storage', OBJECT_NAME, "percentiled/30/{}_{}_{}".format(train['confidence'][idx], train['name'][idx],train['image_name'][idx]))
            
    #         count+=1
    #             #109
    #     elif thirty< confi <= fourty:
    #         print('percentile fourty',confi)
    #         print(train['confidence'][idx])
    #         print(train['image_name'][idx])
    #         print(train['name'][idx])
    #         s3.meta.client.download_file('location-intelligence-storage', OBJECT_NAME, "percentiled/40/{}_{}_{}".format(train['confidence'][idx], train['name'][idx],train['image_name'][idx]))
            
    #         count+=1
            
    #     elif fourty< confi <= fifty:
    #         print('percentile fifty',confi)
    #         print(train['confidence'][idx])
    #         print(train['image_name'][idx])
    #         print(train['name'][idx])
    #         s3.meta.client.download_file('location-intelligence-storage', OBJECT_NAME, "percentiled/50/{}_{}_{}".format(train['confidence'][idx], train['name'][idx],train['image_name'][idx]))
            
    #         count+=1
    #     elif fifty< confi <= sixty:
    #         print('percentile sixty',confi)
    #         print(train['confidence'][idx])
    #         print(train['image_name'][idx])
    #         print(train['name'][idx])
    #         s3.meta.client.download_file('location-intelligence-storage', OBJECT_NAME, "percentiled/60/{}_{}_{}".format(train['confidence'][idx], train['name'][idx],train['image_name'][idx]))
            
    #         count+=1
    #     elif sixty< confi <= seventy:
    #         print('percentile seventy',confi)
    #         print(train['confidence'][idx])
    #         print(train['image_name'][idx])
    #         print(train['name'][idx])
    #         s3.meta.client.download_file('location-intelligence-storage', OBJECT_NAME, "percentiled/70/{}_{}_{}".format(train['confidence'][idx], train['name'][idx],train['image_name'][idx]))
            
    #         count+=1
    #     elif seventy< confi <= eighty:
    #         print('percentile eighty',confi)
    #         print(train['confidence'][idx])
    #         print(train['image_name'][idx])
    #         print(train['name'][idx])
    #         count+=1
    #         s3.meta.client.download_file('location-intelligence-storage', OBJECT_NAME, "percentiled/80/{}_{}_{}".format(train['confidence'][idx], train['name'][idx],train['image_name'][idx]))
            
    #     elif eighty< confi <= ninety:
    #         print('percentile ninety',confi)
    #         print(train['confidence'][idx])
    #         print(train['image_name'][idx])
    #         print(train['name'][idx])
    #         s3.meta.client.download_file('location-intelligence-storage', OBJECT_NAME, "percentiled/90/{}_{}_{}".format(train['confidence'][idx], train['name'][idx],train['image_name'][idx]))
            
    #         count+=1
    #     elif ninety< confi <= hundred:
    #         print('percentile hundred',confi)
    #         print(train['confidence'][idx])
    #         print(train['image_name'][idx])
    #         print(train['name'][idx])
    #         s3.meta.client.download_file('location-intelligence-storage', OBJECT_NAME, "percentiled/100/{}_{}_{}".format(train['confidence'][idx], train['name'][idx],train['image_name'][idx]))
            
    #         count+=1

    # print(count)

if __name__== "__main__" :
    main()
    