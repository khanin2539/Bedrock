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

def get_bucket_path(image_name):
        temp = image_name.split("_")
        location = temp[0]
        slide = temp[5][1:]
        
        return location,slide
def main():


    conn = psycopg2.connect("dbname = li_poc user = pgsql_master password=arvbedrock1234# host=bedrock-mlplatform-nonprod-pgsql.cluster-cq6wq7ckjmhj.ap-southeast-1.rds.amazonaws.com port = 5432")
    cur = conn.cursor()

    train = pd.read_sql_query("Select * From object_details where name like 'Car' and confidence >75", conn)
    print(train)

    directory = r'C:\Users\udomc\Documents\aws\11_15_2021_gsv_images\11_15_2021_gsv_images'
    
    count = 0
    for subdir, dirs, files in os.walk(directory):
        for idx, file in enumerate(files):
            image_dir = os.path.join(subdir, file)
            
            path = os.path.normpath(subdir)
            

            
            print(file)
            #print(idx)
            image_name = file.split(r'_')[1:]
            image_name = '_'.join(image_name)
            #print(image_name)
            image = cv2.imread(image_dir)
            
            image_x = (image.shape[1])
            image_y = (image.shape[0])
            #print('imagex, y:', image_x, image_y)
            # cv2.imshow('ROI', image)
            # cv2.waitKey()
            for i in range(len(train['image_name'])):
                #print('name: ',train['image_name'][i])

                if(train['width'][i]==None):

                    print('not in the database')

                    continue
                if(math.isnan(train['width'][i])):

                    continue

                if image_name == train['image_name'][i]:
                    print('its a match')
                    #print(type(train['width'][i]))
                    width = int(train['width'][i]*image_x)
                    height = int(train['height'][i]*image_y)
                    left = int(train['left'][i]*image_x)
                    top = int(train['top'][i]*image_y)
                    bounding_boxes = (left, top, width, height)
                    x,y,w,h = bounding_boxes
                    #print(x, y)
                    if x==0:
                        print('width not applicable')
                        continue
                    ROI = image[y:y+h, x:x+w]
                    # cv2.imshow('ROI_edited', ROI)
                    # cv2.waitKey()
                    roi_filename = '11_15_2021_gsv_images/11_15_2021_gsv_images/cropped_11_15_2021_gsv_images/ROI_{}_{}'.format(i,image_name)
                    
                
                    cv2.imwrite(roi_filename, ROI)
                
                    if not cv2.imwrite(roi_filename, ROI):
                        raise Exception("Could not write image")
                    count+=1
                    print(count)
    print(count)

    
             
if __name__== "__main__" :
    main()

    
    
    