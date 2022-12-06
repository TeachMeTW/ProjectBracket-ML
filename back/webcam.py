import json
import cv2
import uuid
import time
import os
import bs4 
import numpy as np
from matplotlib import pyplot as plt
import os
import glob
import pandas as pd
import json
import pickle

# Use LabelMe to label images! Make sure it goes into assets!

def gatherCameraData():
   
    img_path = os.path.join('back','assets', 'unsorted', 'images', 'unlabeled')
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    cam = cv2.VideoCapture(0)
    cam.set(3, 1920)
    cam.set(4, 1080)
    cv2.namedWindow("test")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            imgName = os.path.join(img_path,f'{str(uuid.uuid1())}.jpg')
            cv2.imwrite(imgName, frame)
            cv2.imshow('frame', frame)
            print("{} written!".format(imgName))
            img_counter += 1
    cv2.destroyAllWindows()
    return       

def autocam():
    img_path = os.path.join('back','assets', 'unsorted', 'images', 'unlabeled')
    cap = cv2.VideoCapture(0)
    cap.set(3, 1920)
    cap.set(4, 1080)
    print('Collecting images')
    time.sleep(5)
    for imgnum in range(50):
        print('Collecting image {}'.format(imgnum))
        ret, frame = cap.read()
        imgName = os.path.join(img_path,f'{str(uuid.uuid1())}.jpg')
        cv2.imwrite(imgName, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

autocam()
