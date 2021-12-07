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

def main():
    directory = r'C:\Users\udomc\Documents\aws\percentiled\100\cropped_image'
    #directory_new = r'C:\Users\udomc\Documents\aws\percentiled\10\sampled_images'
    files_name =  os.walk(directory)
    files = os.listdir(directory)
   

    
    for x in range(60):
        files = os.listdir(directory)
        sample_list = random.choices(files)
        print('select random')
        print(sample_list[0])
        for subdir, dirs, files in os.walk(directory):
            image_dir = os.path.join(subdir, sample_list[0])
            print('show image address')
            print(image_dir)
            image = cv2.imread(image_dir)
            # cv2.imshow('ROI', image)
            # cv2.waitKey()
            shutil.move(image_dir, "percentiled/100/sampled_cropped_images/{}".format(sample_list[0]))



if __name__== "__main__" :
    main()