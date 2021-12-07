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
    directory = r'C:\Users\udomc\Documents\aws'
    car_label = pd.read_csv('Car_labels.csv')
    
    with open('car_type.txt') as f:
        lines = f.readlines()
        idx=0
        for x in range(len(lines)):
         
            manifest_split = lines[x].split(r",")
            if len(manifest_split)==8:
                #print(manifest_split)
                split_img_name = manifest_split[0].split(r'/')
                img_name = split_img_name[6].split(r'"')
                img_name = img_name[0]
               

                #print(manifest_split[4])
                label = manifest_split[4].split((r':'))
                #print(label[2])
                label = label[2].split(r'"')
                label = label[1].split(r"'")
                #print(label[0])

            #for 2 labels
            elif len(manifest_split)==11:
                manifest_split = lines[45].split(r",")
                #print(manifest_split)
                split_img_name = manifest_split[0].split(r'/')
                img_name = split_img_name[6].split(r'"')
                img_name = img_name[0]
                

                #print(manifest_split[6])
                label = manifest_split[6].split((r':'))
                #print(label[2])
                label = label[2].split(r'"')
                label = label[1].split(r"'")
                #print(label[0])

            idx+=1
            print(idx)
            #print('image name from json:', img_name)
            idx_df = 0
            for y in range(len(car_label['image_name'])):
                #print('image from df', y)
                if img_name==car_label['image_name'][y]:
                    print('found it')
                    print(img_name)
                    print(label[0])
                    print(car_label['image_name'][y])
                    car_label['label'][y] = label[0]
                    print(car_label['label'][y])
                    print('index at', idx_df)
                idx_df+=1
                
    print(car_label)
    car_label.to_csv("Car_label.csv", index=None)
    



if __name__== "__main__" :
    main()