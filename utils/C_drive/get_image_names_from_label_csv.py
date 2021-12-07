

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
import random
import shutil
import time

def main():
    directory = r'D:\bedrock\try_cropped\224'
    car_label = pd.read_csv('11_20_2021_car_labels.csv')
    
    #print(car_label['image_name'].value_counts())
    print(car_label['label'].value_counts())
    print(car_label['label'].isna().sum())
    time.sleep(3)
    
    count = 0
    for subdir, dirs, files in os.walk(directory):
        for idx, file in enumerate(files):
            image_dir = os.path.join(subdir, file)
            print(image_dir)
            
            path = os.path.normpath(subdir)
            

            not_found_list = []
            print(file)

            for x in range(len(car_label['image_name'])):
                if file==car_label['image_name'][x]:
                    print('found it')
                    count+=1

                    image_dir = os.path.join(subdir, file)
                    print('show image address')
                    print(image_dir)
                    image = cv2.imread(image_dir)
                    # cv2.imshow('ROI', image)
                    # cv2.waitKey()
                    shutil.move(image_dir, "D:/bedrock/try_cropped/224/labeled_images/{}".format(file))
                else:
                    not_found_list.append(file)
                    continue

    print(count)
    print(not_found_list)



if __name__== "__main__" :
    main()