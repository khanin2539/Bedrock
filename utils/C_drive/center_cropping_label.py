import cv2
import ipyplot
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
import numpy as np 

def centerCrop(img, width, height):
    assert img.shape[0] >= height
    assert img.shape[1] >= width
    h, w, _ = img.shape
    h //= 2
    w //= 2
    print(h, w)
    
    img = img[h - height//2:h+height//2, w - width//2:w + width//2, :]
    return img



def centerCrop_3(img, width, height):
    assert img.shape[0] >= height
    assert img.shape[1] >= width
    h, w, _ = img.shape
    h //= 2
    w //= 2
    print(h, w)

    
    img = img[h - height//2:h+height//8, w - width//2:w + width//4]
    print(img.shape[0], img.shape[1] )
    return img

directory = r'C:\Users\udomc\Documents\aws\car_type_stanford_csv/cropped_image_224'
label = pd.read_csv('anno_train_appended.csv')
label_main = label
label_top_right_cropped= label
label_gaussian_blur_top_cropped= label
label_top_cropped= label
label_gaussian_blur_bottom_right= label
label_bottom_right= label
label_gaussian_blur_top_left= label
label_top_left_cropped= label
label_gaussian_blur= label
print(label)
    
count = 0
for subdir, dirs, files in os.walk(directory):
    for file in files:
        
        
        #print(label)
        #image_dir = os.path.join(subdir, file)
        
        print(file)
        #path = os.path.normpath(subdir)
       
        #image = cv2.imread(image_dir)
        # cv2.imshow('ROI_cropped', image)
        # cv2.waitKey()
        
        for y in range(len(label)):
          if file == label['image_name'][y]:
            
            print('found it')
            label_main = label_main.append({'label': label['label'][y], 'image_name': 'top_right_cropped_{}'.format(label['image_name'][y]) }, ignore_index=True)
            label_top_right_cropped = label_top_right_cropped.append({'label': label['label'][y], 'image_name': 'top_right_cropped_{}'.format(label['image_name'][y]) }, ignore_index=True)
            label_main = label_main.append({'label': label['label'][y], 'image_name': 'gaussian_blur_top_cropped_{}'.format(label['image_name'][y]) }, ignore_index=True)
            label_gaussian_blur_top_cropped = label_gaussian_blur_top_cropped.append({'label': label['label'][y], 'image_name': 'gaussian_blur_top_cropped_{}'.format(label['image_name'][y]) }, ignore_index=True)
            label_main = label_main.append({'label': label['label'][y], 'image_name': 'top_cropped_{}'.format(label['image_name'][y]) }, ignore_index=True)
            label_top_cropped = label_top_cropped.append({'label': label['label'][y], 'image_name': 'top_cropped_{}'.format(label['image_name'][y]) }, ignore_index=True)
            label_main = label_main.append({'label': label['label'][y], 'image_name': 'gaussian_blur_bottom_right_{}'.format(label['image_name'][y]) }, ignore_index=True)
            label_gaussian_blur_bottom_right = label_gaussian_blur_bottom_right.append({'label': label['label'][y], 'image_name': 'gaussian_blur_bottom_right_{}'.format(label['image_name'][y]) }, ignore_index=True)
            label_main = label_main.append({'label': label['label'][y], 'image_name': 'bottom_right_{}'.format(label['image_name'][y]) }, ignore_index=True)
            label_bottom_right = label_bottom_right.append({'label': label['label'][y], 'image_name': 'bottom_right_{}'.format(label['image_name'][y]) }, ignore_index=True)
                

            label_main = label_main.append({'label': label['label'][y], 'image_name': 'gaussian_blur_top_left_{}'.format(label['image_name'][y]) }, ignore_index=True)
            label_gaussian_blur_top_left = label_gaussian_blur_top_left.append({'label': label['label'][y], 'image_name': 'gaussian_blur_top_left_{}'.format(label['image_name'][y]) }, ignore_index=True)
            

            label_main = label_main.append({'label': label['label'][y], 'image_name': 'top_left_cropped_{}'.format(label['image_name'][y]) }, ignore_index=True)
            label_top_left_cropped = label_top_left_cropped.append({'label': label['label'][y], 'image_name': 'top_left_cropped_{}'.format(label['image_name'][y]) }, ignore_index=True)
            
            
            label_main = label_main.append({'label': label['label'][y], 'image_name': 'gaussian_blur_{}'.format(label['image_name'][y]) }, ignore_index=True)
            label_gaussian_blur = label_gaussian_blur.append({'label': label['label'][y], 'image_name': 'gaussian_blur_{}'.format(label['image_name'][y]) }, ignore_index=True)
            print(len(label_main['image_name']))
            print(len(label_top_right_cropped['image_name']))
            print(len(label_gaussian_blur_top_cropped['image_name']))
            print(len(label_top_cropped['image_name']))
            print(len(label_gaussian_blur_bottom_right['image_name']))
            print(len(label_bottom_right['image_name']))
            print(len(label_gaussian_blur_top_left['image_name']))
            print(len(label_top_left_cropped['image_name']))
            print(len(label_gaussian_blur['image_name']))



    label_main.to_csv('anno_train_appended_1.csv', index = None)
    label_top_right_cropped.to_csv('label_top_right_cropped.csv', index = None)
    label_gaussian_blur_top_cropped.to_csv('label_gaussian_blur_top_cropped.csv', index = None)
    label_top_cropped.to_csv('label_top_cropped.csv', index = None)
    label_gaussian_blur_bottom_right.to_csv('label_gaussian_blur_bottom_right.csv', index = None)
    label_bottom_right.to_csv('label_bottom_right.csv', index = None)
    label_gaussian_blur_top_left.to_csv('label_gaussian_blur_top_left.csv', index = None)
    label_top_left_cropped.to_csv('label_top_left_cropped.csv', index = None)
    label_gaussian_blur.to_csv('label_gaussian_blur.csv', index = None)


            
# img = cv2.imread(path)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cropped_image = randomCrop(img, 800, 800)
# ipyplot.plot_images([img,cropped_image], max_images=20, img_width=400)
