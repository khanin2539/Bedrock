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

car_names = pd.read_csv('names.csv')
print(car_names['Car_label'][0:10])
split_len = set()
car_type = set()
NaN = np.nan
car_names['BD_Label'] = NaN
for x in range(len(car_names['Car_label'])):
    split_car = car_names['Car_label'][x].split(r' ')
    print(split_car)
    length = len(split_car)
    print(length)
    split_len.add(length)
    if length==4:
        print(split_car[2])
        car_type.add(split_car[2])
        car_names['BD_Label'][x] = split_car[2]

    if length==5:
        print(split_car[2]+' '+split_car[3])
        car_type.add(split_car[3])
        car_names['BD_Label'][x] = split_car[3]
print(car_type)
print(split_len)
print(car_names)
#car_names.to_csv('bd_car_label.csv', index = None)

# split_car = car_names['Car_label'].split(r' ')
# print(split_car)