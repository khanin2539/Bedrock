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
    car_label = pd.read_csv('4th_car_label.csv')
    
    #print(car_label['image_name'].value_counts())
    print(car_label['label'].value_counts())
    print(car_label['label'].isna().sum())
    
    
    with open('car_type_8000.txt') as f:
        lines = f.readlines()
        print('hey')
        idx=0
        for x in range(len(lines)):
            print('hi')
            manifest_split = lines[x].split(r",")
            
            if len(manifest_split)==1:
                print('no label yet!')
                continue

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
                print(label[0])
                print(img_name)

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

            print(idx)   
           # print(car_label['image_name'])
            car_label['label'][x] = label[0]
            car_label['image_name'][x] = img_name
            #print(car_label['label'][x])
           
                
    print(car_label)
    print(car_label['label'].value_counts())
    print(car_label['label'].isna().sum())

    car_label.to_csv("4th_car_label.csv", index=None)


if __name__== "__main__" :
    main()