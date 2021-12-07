
# importing PIL Module
from PIL import Image
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
# # open the original image
# original_img = Image.open("original.png")
 
 
# # Flip the original image horizontally
# horz_img = original_img.transpose(method=Image.FLIP_LEFT_RIGHT)
# horz_img.save("horizontal.png")
 
def main():
    directory = r'C:\Users\udomc\Documents\aws\percentiled\Car_dataset\test_image'
    #directory_new = r'C:\Users\udomc\Documents\aws\percentiled\10\sampled_images'
    files_name =  os.walk(directory)
    files = os.listdir(directory)
    # get all files from current directory
    print(files)

    
    for x in range(60):
        # get each file name
        print(files[x])
        for subdir, dirs, files in os.walk(directory):
            # get one image
            image_dir = os.path.join(subdir, files[x])
            print('show image address')
            print(image_dir)
            image = cv2.imread(image_dir)
            cv2.imshow('ROI', image)
            cv2.waitKey()
            with Image.open(image_dir) as im:
                horz_img = im.transpose(method=Image.FLIP_LEFT_RIGHT)
                #horz_img     = horz_img.rotate(45)
                horz_img.save("percentiled/Car_dataset/test_image_{}.jpg".format(x))
                
            

 
# # open the original image
# original_img = Image.open("original.png")
 
 
# # Flip the original image horizontally
# horz_img = original_img.transpose(method=Image.FLIP_LEFT_RIGHT)
# horz_img.save("horizontal.png")
 
# # close all our files object
# original_img.close()
# horz_img.close()


if __name__== "__main__" :
    main()


# close all our files object
