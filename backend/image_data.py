import json
import cv2
import uuid
import time
import os
import bs4 
import numpy as np
from matplotlib import pyplot as plt

# Use LabelMe to label images! Make sure it goes into assets!

def gatherCameraData():
    n = str(input("File path/name of pics: "))
    img_path = os.path.join('backend','assets', 'data', 'images', n)
    if not os.path.exists(img_path):
        os.mkdir(img_path)
        os.mkdir(os.path.join('backend','assets', 'data', 'labels', n))
    cam = cv2.VideoCapture(0)

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

# if you're gonna make a scraper 
def gatherWebData():
    return


