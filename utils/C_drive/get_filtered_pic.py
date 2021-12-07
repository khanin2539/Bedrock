import pandas as pd
import psycopg2
date_format = "%Y-%m-%d"
import sys, os
import time
from boto3.session import Session
import boto3
import json
import math
import os
import cv2
import numpy as np 
ACCESS_KEY = "AKIAZQ7I5QVNSWAU4A6S"
SECRET_KEY = "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"
BUCKET_NAME = "location-intelligence-storage"
def get_bucket_path(image_name):
        temp = image_name.split("_")
        location = temp[0]
        slide = temp[5][1:]
        
        return location,slide
def main():


    client = boto3.client("s3",
                        aws_access_key_id=ACCESS_KEY,
                        aws_secret_access_key=SECRET_KEY,
                        region_name="ap-southeast-1")

    s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY,
                        aws_secret_access_key=SECRET_KEY,
                        region_name="ap-southeast-1")

                    

    conn = psycopg2.connect("dbname = ligisdb user = postgres password=postgres host=metmet.thddns.net port = 1200")
    cur = conn.cursor()
    pic_cors =  pd.read_sql_query("Select * From object_details where name like 'Car' or name like 'Van'  OR name like 'Truck'", conn)
    directory = r'C:\Users\udomc\Documents\aws\percentiled'
    
    count = 0
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            image_dir = os.path.join(subdir, file)
            print(file)
            path = os.path.normpath(subdir)
            path_list = path.split(os.sep)
            print(path_list[6])
            
            
            print(file)
           

            print('pic_cors:',pic_cors)
            if pic_cors is None:
                print('empty dataframe aa')
            image = cv2.imread(image_dir)
            
            image_x = (image.shape[1])
            image_y = (image.shape[0])
            print('imagex, y:', image_x, image_y)
            # cv2.imshow('ROI', image)
            # cv2.waitKey()
            split_img_name = file.split(r"_")
            image_name = split_img_name[2]+'_'+split_img_name[3]+'_'+split_img_name[4]+'_'+split_img_name[5]+'_'+split_img_name[6]+'_'+split_img_name[7]+'_'+split_img_name[8]+'_'+split_img_name[9]+'_'+split_img_name[10]
            print(split_img_name)
            print(image_name)
            if split_img_name[1] == 'Van' or split_img_name[1] == 'Truck':
                print('not a Car instance')
                continue
            for i in range(len(pic_cors['width'])):
                #print('length: ',len(pic_cors['width']))
                if(pic_cors['width'][i]==None):
                    print('not in the database')
                    continue
                if(math.isnan(pic_cors['width'][i])):
                    continue
                if image_name == pic_cors['image_name'][i]:
                    print('its a match')
                    print(type(pic_cors['width'][i]))
                    width = int(pic_cors['width'][i]*image_x)
                    height = int(pic_cors['height'][i]*image_y)
                    left = int(pic_cors['left'][i]*image_x)
                    top = int(pic_cors['top'][i]*image_y)
                    bounding_boxes = (left, top, width, height)
                    x,y,w,h = bounding_boxes
                    print(x, y)
                    ROI = image[y:y+h, x:x+w]
                #print(ROI)
                #print('ROI: ', ROI)
                
                    print(i)
                    roi_filename = 'percentiled/{}/cropped_image/ROI_{}_{}.jpg'.format(path_list[6], file, i)
               
                
                    cv2.imwrite(roi_filename, ROI)
                
                    if not cv2.imwrite(roi_filename, ROI):
                        raise Exception("Could not write image")
                    count+=1
    print(count)

             
if __name__== "__main__" :
    main()

    
    
    