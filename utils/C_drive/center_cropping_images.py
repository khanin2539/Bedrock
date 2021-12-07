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
print(label)
    
count = 0
for subdir, dirs, files in os.walk(directory):
    for file in files:
        print(label['label'][count])
        
        print(label)
        image_dir = os.path.join(subdir, file)
        
        print(file)
        path = os.path.normpath(subdir)
       
        image = cv2.imread(image_dir)
        # cv2.imshow('ROI_cropped', image)
        # cv2.waitKey()
        
        for y in range(len(label)):
          if file == label['image_name'][y]:
      ######################################
          # top right crop (height - width)
        ######################################
            cropped = image[0:130, 50:224]
            print(cropped.shape[0], cropped.shape[1] )
            print('top right crop')
            
            try:
                os.mkdir('centered-cropped_images/top_right_cropped')
                os.mkdir('centered-cropped_images/gaussian_blur_top_right')
                os.mkdir('centered-cropped_images/top_left_cropped_image')
                os.mkdir('centered-cropped_images/gaussian_blur_top_left')
                os.mkdir('centered-cropped_images/gaussian_blur_bottom_right')
                os.mkdir('centered-cropped_images/gaussian_blur_top_cropped')
                os.mkdir('centered-cropped_images/bottom_right')
                os.mkdir('centered-cropped_images/top_crop')
                print("Directory Created ")
            except FileExistsError:
                print("Directory  already exists")  

            # cv2.imshow('ROI_cropped', cropped)
            # cv2.waitKey()
            roi_filename = '../centered-cropped_images/top_right_cropped/top_right_cropped_{}'.format(label['image_name'][y])
            #os.mkdir('centered')
            cv2.imwrite(os.path.join(path ,roi_filename), cropped)
            
            if not cv2.imwrite(os.path.join(path ,roi_filename), cropped):
                raise Exception("Could not write image")

            ######################################
            # Use gaussian Blur
        
            blur = cv2.GaussianBlur(cropped,(15,15),0)
            print('top right blur')
            # cv2.imshow('ROI_cropped', blur)
            # cv2.waitKey()
            roi_filename = '../centered-cropped_images/gaussian_blur_top_right/gaussian_blur_{}'.format(label['image_name'][y])
            cv2.imwrite(os.path.join(path ,roi_filename), blur)
            
            if not cv2.imwrite(os.path.join(path ,roi_filename), blur):
                raise Exception("Could not write image")


          ######################################
            # top left crop (height - width)
          ######################################


            top_left_cropped_image = centerCrop_3(image, 224, 224)
            #ipyplot.plot_images([image,cropped_image], max_images=20, img_width=400)
            # cv2.imshow('ROI_cropped', top_left_cropped_image)
            # cv2.waitKey()
            roi_filename = '../centered-cropped_images/top_left_cropped_image/top_left_cropped_{}'.format(label['image_name'][y])

            cv2.imwrite(os.path.join(path ,roi_filename), top_left_cropped_image)
            
            
            if not cv2.imwrite(os.path.join(path ,roi_filename), top_left_cropped_image):
                raise Exception("Could not write image")

              ######################################
            # Use gaussian Blur
        
            blur = cv2.GaussianBlur(top_left_cropped_image,(15,15),0)
            # cv2.imshow('ROI_cropped', blur)
            # cv2.waitKey()
            roi_filename = '../centered-cropped_images/gaussian_blur_top_left/gaussian_blur_top_left_{}'.format(label['image_name'][y])
            cv2.imwrite(os.path.join(path ,roi_filename), blur)
            
            
            if not cv2.imwrite(os.path.join(path ,roi_filename), blur):
                raise Exception("Could not write image")

            
            
        ######################################
            # bottem right crop (height - width)
          ######################################

            bottom_right_cropped = image[60:200, 0:224]
            print(bottom_right_cropped.shape[0], bottom_right_cropped.shape[1] )
            # cv2.imshow('ROI_cropped', bottom_right_cropped)
            # cv2.waitKey()
            roi_filename = '../centered-cropped_images/bottom_right/bottom_right_{}'.format(label['image_name'][y])
            cv2.imwrite(os.path.join(path ,roi_filename), bottom_right_cropped)
            
            if not cv2.imwrite(os.path.join(path ,roi_filename), bottom_right_cropped):
                raise Exception("Could not write image")

              ######################################
            # Use gaussian Blur
        
            blur = cv2.GaussianBlur(bottom_right_cropped,(15,15),0)
            # cv2.imshow('ROI_cropped', blur)
            # cv2.waitKey()
            roi_filename = '../centered-cropped_images/gaussian_blur_bottom_right/gaussian_blur_bottom_right_{}'.format(label['image_name'][y])
            cv2.imwrite(os.path.join(path ,roi_filename), blur)
            
            if not cv2.imwrite(os.path.join(path ,roi_filename), blur):
                raise Exception("Could not write image")
          
          
        ######################################
            # Top crop (height - width) : Questionable 
            # because coupe and sedan are similar
            # test it whether the model can get patterns
          ######################################

            top_cropped = image[0:100, 0:200]
            print(top_cropped.shape[0], top_cropped.shape[1] )
            # cv2.imshow('ROI_cropped', top_cropped)
            # cv2.waitKey()
            roi_filename = '../centered-cropped_images/top_crop/top_cropped_{}'.format(label['image_name'][y])
            cv2.imwrite(os.path.join(path ,roi_filename), top_cropped)
            if not cv2.imwrite(os.path.join(path ,roi_filename), top_cropped):
                raise Exception("Could not write image")
            

            blur = cv2.GaussianBlur(top_cropped,(15,15),0)
            # cv2.imshow('ROI_cropped', blur)
            # cv2.waitKey()
            roi_filename = '../centered-cropped_images/gaussian_blur_top_cropped/gaussian_blur_top_cropped_{}'.format(label['image_name'][y])
            #label = label.append({'label': label['label'][count], 'image_name': 'gaussian_blur_top_cropped{}.jpg'.format(count) }, ignore_index=True)
            cv2.imwrite(os.path.join(path ,roi_filename), blur)
            
            if not cv2.imwrite(os.path.join(path ,roi_filename), blur):
                raise Exception("Could not write image")
            print(label)
          
            print('found it')
            label = label.append({'label': label['label'][y], 'image_name': 'top_right_cropped_{}'.format(label['image_name'][y]) }, ignore_index=True)
            label = label.append({'label': label['label'][y], 'image_name': 'gaussian_blur_top_cropped_{}'.format(label['image_name'][y]) }, ignore_index=True)
            label = label.append({'label': label['label'][y], 'image_name': 'top_cropped_{}'.format(label['image_name'][y]) }, ignore_index=True)
            label = label.append({'label': label['label'][y], 'image_name': 'gaussian_blur_bottom_right_{}'.format(label['image_name'][y]) }, ignore_index=True)
            label = label.append({'label': label['label'][y], 'image_name': 'bottom_right_{}'.format(label['image_name'][y]) }, ignore_index=True)
            label = label.append({'label': label['label'][y], 'image_name': 'gaussian_blur_top_left_{}'.format(label['image_name'][y]) }, ignore_index=True)
            label = label.append({'label': label['label'][y], 'image_name': 'top_left_cropped_{}'.format(label['image_name'][y]) }, ignore_index=True)
            label = label.append({'label': label['label'][y], 'image_name': 'gaussian_blur_{}'.format(label['image_name'][y]) }, ignore_index=True)

                    

        count+=1
        label.to_csv('anno_train_appended_1.csv', index = None)
    print(count)

            
# img = cv2.imread(path)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cropped_image = randomCrop(img, 800, 800)
# ipyplot.plot_images([img,cropped_image], max_images=20, img_width=400)
