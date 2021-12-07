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


conn = psycopg2.connect("dbname = ligisdb user = postgres password=postgres host=metmet.thddns.net port = 1200")
cur = conn.cursor()

train = pd.read_sql_query("Select obj_id, name, confidence, width, height, top, image_name From object_details where name like 'Car' ", conn)

train_sports = pd.read_sql_query("Select obj_id, name, confidence, width, height, top, image_name From object_details where name like 'Sports Car' ", conn)
train_sedan = pd.read_sql_query("Select obj_id, name, confidence, width, height, top, image_name From object_details where name like 'Sedan' ", conn)
train_coupe = pd.read_sql_query("Select obj_id, name, confidence, width, height, top, image_name From object_details where name like 'Coupe' ", conn)

train_all = pd.read_sql_query("Select obj_id, name, confidence, width, height, top, image_name From object_details where name like 'Car' OR name like 'Van'  OR name like 'Truck'", conn)
train_van = pd.read_sql_query("Select obj_id, name, confidence, width, height, top, image_name From object_details where name like 'Van' ", conn)
train_truck = pd.read_sql_query("Select obj_id, name, confidence, width, height, top, image_name From object_details where name like 'Truck' ", conn)
# train_check = pd.read_sql_query("Select obj_id, name, confidence, width, height, top, image_name From object_details where image_name like 'MrtSutthisan_img_13-7969025_100-5728328_a82_s90_y75_f90_0.jpg' ", conn)
# train = pd.read_sql_query("Select obj_id, name, confidence, width, height, top, image_name From object_details where name like 'Car' or name like 'Van'  OR name like 'Truck'", conn)
#Car yea
#Coupe Yea
#Sports Car Yea
#SUV nah
#MPV nah
#Van Yeah
#Sedan yea
#Pickup Nah
# print(train_check)
# a = np.array(train_check['confidence'])
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
# print(len(train_check['confidence']))
# count = 0
#print(train_check['confidence'])
# for x in range(len(range(20))):
#     print(train.iloc[x])
#     count+=1
    #print(x)
    # confi = x

    # if zero<= confi <= tenth:
    #         print('percentile tenth',confi)
    #         count+=1

    # if tenth< confi <= twenty:
    #         print('percentile twenty',confi)
    #         count+=1
    #         #101
    # elif twenty< confi <= thirty:
    #         print('percentile thirty',confi)
    #         count+=1
    #         #109
    # elif thirty< confi <= fourty:
    #         print('percentile fourty',confi)
    #         count+=1
        
    # elif fourty< confi <= fifty:
    #         print('percentile fifty',confi)
    #         count+=1
    # elif fifty< confi <= sixty:
    #         print('percentile sixty',confi)
    #         count+=1
    # elif sixty< confi <= seventy:
    #         print('percentile seventy',confi)
    #         count+=1
    # elif seventy< confi <= eighty:
    #         print('percentile eighty',confi)
    #         count+=1
    # elif eighty< confi <= ninety:
    #         print('percentile ninety',confi)
    #         count+=1
    # elif ninety< confi <= hundred:
    #         print('percentile hundred',confi)
    #         count+=1
#print(count)
# print(len(train_all['image_name']))
# unique_all = np.unique(train_all['image_name'])
# print(len(unique_all))

unique_sports = np.unique(train_sports['image_name'])
print('unique Sports Car image:', len(unique_sports))

unique_coupe = np.unique(train_coupe['image_name'])
print('unique Coupe image:', len(unique_coupe))

print('numbers of car image:', len(train['image_name']))
unique_car = np.unique(train['image_name'])
print('unique car image :', len(unique_car))

unique_sedan = np.unique(train_sedan['image_name'])
print('unique sedan image :', len(unique_sedan))
print('\n All Car, Van and Truck image :', len(train_all['image_name']))
unique_all = np.unique(train_all['image_name'])
print('unique car, van and truck image :', len(unique_all))

unique_van = np.unique(train_van['image_name'])
print('unique van image :', len(unique_van))
unique_truck = np.unique(train_truck['image_name'])
print('unique truck image :', len(unique_truck))

#print(len(train['obj_id']))
#train = train.sort_values(by=['confidence'])
#print(train)

#print((train['image_name']))
# car_list = []
# sports_car_list = []

# count = 0
# print('\nChecking Sports Car Image number')
# for x in unique_sports:
    
#     for y in unique_car:
#         if x==y:
           
#             count+=1
# print('Number of same name counts:', count)
# count_1=0
# print('\nChecking Coupe Image number')
# for x in unique_coupe:
    
#     for y in unique_car:
#         if x==y:
           
#             count_1+=1
# print('Number of same name counts:', count_1)
# count_1=0

# count_2=0
# print('\nChecking Sedan Image number')
# for x in unique_sedan:
    
#     for y in unique_car:
#         if x==y:
           
#             count_2+=1
# print('Number of same name counts:', count_2)
# count_2=0

count = 0
print('\nChecking Sports Car Image number')
for x in unique_sports:
    
    for y in unique_all:
        if x==y:
           
            count+=1
print('Number of same name counts:', count)
count_1=0
print('\nChecking Coupe Image number')
for x in unique_coupe:
    
    for y in unique_all:
        if x==y:
           
            count_1+=1
print('Number of same name counts:', count_1)
count_1=0

count_2=0
print('\nChecking Sedan Image number')
for x in unique_sedan:
    
    for y in unique_all:
        if x==y:
           
            count_2+=1
print('Number of same name counts:', count_2)
count_2=0


print('\n total images are:', len(train_all['image_name']))
    
    