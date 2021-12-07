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
s3.Object('location-intelligence',key).copy_from(CopySource=f'{BUCKET_NAME}/{key}')

def get_bucket_path(image_name):
    temp = image_name.split("_")
    location = temp[0]
    slide = temp[5][1:]
    
    return location,slide


conn = psycopg2.connect("dbname = ligisdb user = postgres password=postgres host=metmet.thddns.net port = 1200")
cur = conn.cursor()

train = pd.read_sql_query("Select obj_id, name, confidence, width, height, top, image_name From object_details where name like 'Car' and confidence>70", conn)

print(len(train['obj_id']))
#train = train.sort_values(by=['confidence'])
print(train)




# image = cv2.imread('1.png')
# bounding_boxes = [(17, 24, 47, 47),
#                   (74, 28, 47, 50),
#                   (125, 15, 51, 61),
#                   (184, 18, 53, 53),
#                   (247, 25, 44, 46),
#                   (296, 6, 65, 66)
# ]

# num = 0
# for box in bounding_boxes:
#     x,y,w,h = box
#     ROI = image[y:y+h, x:x+w]
#     cv2.imwrite('ROI_{}.png'.format(num), ROI)
#     num += 1
#     cv2.imshow('ROI', ROI)
#     cv2.waitKey()



for idx in range(1):
 
    location,slide = get_bucket_path(train['image_name'][idx])
    if location == "ChokChai4" :
        location = "ChockChai4"
   
    OBJECT_NAME =  "poc/%s/%s/%s" % ( location,slide,train['image_name'][idx])
    NEW_OBJECT_NAME = "poc/%s/%s/car/%s" %( location,slide,train['image_name'][idx])
    print(OBJECT_NAME)

    #s3.Object('location-intelligence-storage',NEW_OBJECT_NAME).copy_from(CopySource=f'{BUCKET_NAME}/{OBJECT_NAME}')
    
    
    