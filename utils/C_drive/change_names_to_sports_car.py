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

car_names = pd.read_csv('bd_car_label_sports_added_number.csv')
car_library = pd.read_csv('anno_test.csv')
print(car_names)
print(car_library)

#change other unique cars to generic car types 
# for x in range(len(car_names['BD_Label'])):
#     if car_names['BD_Label'][x]=='Type-S' or car_names['BD_Label'][x]=='SS' or car_names['BD_Label'][x]=='SRT8' or car_names['BD_Label'][x]=='GS' or car_names['BD_Label'][x]=='ZR1':
#         car_names['BD_Label'][x] = 'Sports Car'
#     if car_names['BD_Label'][x]=='IPL' or car_names['BD_Label'][x]=='XKR'  or car_names['BD_Label'][x]=='R':
#         car_names['BD_Label'][x] = 'Coupe'
#     if car_names['BD_Label'][x]=='Cab' or car_names['BD_Label'][x]=='SuperCab':
#         car_names['BD_Label'][x] = 'Pickup'
#     if car_names['BD_Label'][x]=='Abarth':
#         car_names['BD_Label'][x] = 'Hatchback'

# change car type strings to numbers
# for x in range(len(car_names['BD_Label'])):
#     if car_names['BD_Label'][x]== 'Convertible':
#         car_names['Name_label'][x] = 1
#     elif car_names['BD_Label'][x]== 'Coupe':
#         car_names['Name_label'][x] = 2
#     elif car_names['BD_Label'][x]== 'Hatchback':
#         car_names['Name_label'][x] = 3
#     elif car_names['BD_Label'][x]== 'Minivan':
#         car_names['Name_label'][x] = 4
#     elif car_names['BD_Label'][x]== 'Pickup':
#         car_names['Name_label'][x] = 5
#     elif car_names['BD_Label'][x]== 'Sedan':
#         car_names['Name_label'][x] = 6
#     elif car_names['BD_Label'][x]== 'Sports Car':
#         car_names['Name_label'][x] = 7
#     elif car_names['BD_Label'][x]== 'SUV':
#         car_names['Name_label'][x] = 8
#     elif car_names['BD_Label'][x]== 'Van':
#         car_names['Name_label'][x] = 9
#     elif car_names['BD_Label'][x]== 'Wagon':
#         car_names['Name_label'][x] = 10
count = 0
for x in range(len(car_library)):
    print(car_library['label'][x])
    for y in range(len(car_names)):
        if car_library['label'][x] == car_names['original_label'][y]:
            #print('found it')
            car_library['new_label'][x] = car_names['Name_label'][y]
            count+=1
print(count)
print(car_library)
car_library.to_csv('anno_test_appended.csv', index = None)
