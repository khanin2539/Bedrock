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


def main():
# to_upload_to_s3: uploaded 2058 images 1st round

    conn = psycopg2.connect("dbname = li_storage user = pgsql_master password=arvbedrock1234# host=bedrock-mlplatform-nonprod-pgsql.cluster-cq6wq7ckjmhj.ap-southeast-1.rds.amazonaws.com port = 5432")
    cur = conn.cursor()

    train = pd.read_sql_query("Select * From object_details where name like 'Car' and confidence >75", conn)
    print(train)
    #print(train['left'].value_counts())
    print((len(train['image_name'].unique())))
    print(sum(train['left'].value_counts()))
    print(sum(train['height'].value_counts()))
    print(sum(train['width'].value_counts()))

    directory = r'D:\bedrock\11_15_2021_8th'
    
    count = 0
    bad_count = 0
    for subdir, dirs, files in os.walk(directory):
        for idx, file in enumerate(files):
            #get image file
            image_dir = os.path.join(subdir, file)
            print(image_dir)
            
            path = os.path.normpath(subdir)
            

            
            print(file)
            
  
            
            image_name = file.split(r'_')[1:]
            image_name = '_'.join(image_name)
            image_name = file
            image_name = image_name.split(r'_')[1:]
            image_name = '_'.join(image_name)
            print(image_name)

            
            image = cv2.imread(image_dir)
            
            image_x = (image.shape[1])
            image_y = (image.shape[0])
            print('imagex, y:', image_x, image_y)
            
            for i in range(len(train['image_name'])):
                # get a match from df
                #print('name: ',train['image_name'][i])


                if(train['width'][i]==None):

                    print('not in the database')
                    # bad_count +=1
                    # print('bad_count because none:', bad_count)
                    

                    continue
                if(math.isnan(train['width'][i])):
                    # bad_count +=1
                    # print('bad_count because nan:', bad_count)
                    

                    continue

                if image_name == train['image_name'][i]:
                    # found a match
                    
                    print('its a match')
                    print('image name from file:', image_name)
                    print('image name from df:', train['image_name'][i])
                    print('object id:', train['obj_id'][i])
                    # cv2.imshow('ROI', image)
                    # cv2.waitKey()
                    #print(type(train['width'][i]))

                    # then get the bounding box
                    width = int(train['width'][i]*image_x)
                    height = int(train['height'][i]*image_y)
                    left = int(train['left'][i]*image_x)
                    top = int(train['top'][i]*image_y)
                    bounding_boxes = (left, top, width, height)
                    x,y,w,h = bounding_boxes
                    print(x, y)
                    if x==0 and y==0:
                        print('width not applicable')
                        bad_count +=1
                        print('bad_count because x=0:', bad_count)
                        continue
                    ROI = image[y:y+h, x:x+w]
                    new_image_name = train['obj_id'][i]+'_'+image_name
                    print('new image name:', new_image_name)
                    # cv2.imshow('ROI_edited', ROI)
                    # cv2.waitKey()
                    print(image_name)
                    roi_filename = 'D:/bedrock/11_15_2021_8th_test_corrupted_cropped/{}'.format( new_image_name)

                    
                
                    #cv2.imwrite(roi_filename, ROI)
                
                    if not cv2.imwrite(roi_filename, ROI):
                        bad_count +=1
                        print('bad_count becasue cant write image:', bad_count)
                        raise Exception("Could not write image")
                        
                    count+=1
                    print('good_count:', count)
    print('good_count:', count)
    print('bad_count:', bad_count)
    #11_15_2021_5th_cropped
    #passed: 9811
    #failed: 1064

    
             
if __name__== "__main__" :
    main()

    
    
    