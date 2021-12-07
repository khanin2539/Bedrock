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
import csv
import time

with open('./100/Test_Car_labels.csv', 'w',  encoding="utf-8") as f:
    directory = r'C:\Users\udomc\Documents\aws\100'
    #directory_new = r'C:\Users\udomc\Documents\aws\percentiled\10\sampled_images'
    writer = csv.writer(f)
    header = ['image_name', 'label']
    writer.writerow(header)
    files_name =  os.walk(directory)
    files = os.listdir(directory)
    files.sort()
    print(files[10:20])
    print(len(files))
    for x in range(len(files)):
        name = [files[x]]
        writer.writerow(name)
df = pd.read_csv("./100/Test_Car_labels.csv")
df.to_csv("./100/Test_Car_labels.csv", index=None)