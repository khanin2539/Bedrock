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

                    

    bb_pics = pd.read_csv('car_type_stanford_csv/anno_test.csv')
    print(bb_pics)
    directory = r'D:\cars_test\cars_test'

    
    count = 0
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            image_dir = os.path.join(subdir, file)
            print(image_dir)
            print(file)
            path = os.path.normpath(subdir)
            path_list = path.split(os.sep)
            
            image = cv2.imread(image_dir)
            cv2.imshow('ROI', image)
            cv2.waitKey()
            image_x = (image.shape[1])
            image_y = (image.shape[0])
           
    #         for i in range(len(bb_pics['image_name'])):
    #             if file==bb_pics['image_name'][i]:
    #                 count+=1
    #                 print('found it')
    #                 print(bb_pics['image_name'][i])

    #                 print(bb_pics['x2'][i])
    #                 print(bb_pics['x1'][i])
    #                 print(bb_pics['y2'][i])
    #                 print(bb_pics['y1'][i])
    #                 print('imagex, y:', image_x, image_y)
    #                 # cv2.imshow('ROI', image)
    #                 # cv2.waitKey()
    #                 width = bb_pics['y1'][i]
    #                 height = bb_pics['y2'][i]
    #                 left = bb_pics['x1'][i]
    #                 top = bb_pics['x2'][i]
    #                 bounding_boxes = (left, top, width, height)
    #                 x,y,w,h = bounding_boxes
    #                 print(x, y)
    #                 ROI = image[y:y+h, x:x+w]
    #                 roi_filename = 'car_type_stanford_csv/cropped_image/{}'.format(file)
    #                 cv2.imwrite(roi_filename, ROI)


    # print(count)



    #         split_img_name = file.split(r"_")
    #         image_name = split_img_name[2]+'_'+split_img_name[3]+'_'+split_img_name[4]+'_'+split_img_name[5]+'_'+split_img_name[6]+'_'+split_img_name[7]+'_'+split_img_name[8]+'_'+split_img_name[9]+'_'+split_img_name[10]
    #         print(split_img_name)
    #         print(image_name)
    #         if split_img_name[1] == 'Van' or split_img_name[1] == 'Truck':
    #             print('not a Car instance')
    #             continue
    #         for i in range(len(pic_cors['width'])):
    #             #print('length: ',len(pic_cors['width']))
    #             if(pic_cors['width'][i]==None):
    #                 print('not in the database')
    #                 continue
    #             if(math.isnan(pic_cors['width'][i])):
    #                 continue
    #             if image_name == pic_cors['image_name'][i]:
    #                 print('its a match')
    #                 print(type(pic_cors['width'][i]))
    #                 width = int(pic_cors['width'][i]*image_x)
    #                 height = int(pic_cors['height'][i]*image_y)
    #                 left = int(pic_cors['left'][i]*image_x)
    #                 top = int(pic_cors['top'][i]*image_y)
    #                 bounding_boxes = (left, top, width, height)
    #                 x,y,w,h = bounding_boxes
    #                 print(x, y)
    #                 ROI = image[y:y+h, x:x+w]
    #             #print(ROI)
    #             #print('ROI: ', ROI)
                
    #                 print(i)
    #                 roi_filename = 'percentiled/{}/cropped_image/ROI_{}_{}.jpg'.format(path_list[6], file, i)
               
                
    #                 cv2.imwrite(roi_filename, ROI)
                
    #                 if not cv2.imwrite(roi_filename, ROI):
    #                     raise Exception("Could not write image")
    #                 count+=1
    # print(count)

             
if __name__== "__main__" :
    main()

    
    
    