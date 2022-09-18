import cv2
import uuid
import time
import os

# for scraper
import bs4 

def gatherCameraData():
    img_path = os.path.join('ProjectBracket-ML','backend','assets', 'data', 'images')
    
    # CHANGE THIS NUMBER BASED ON HOW MANY IMAGES YOU'RE GONNA TAKE
    # I think we're gonna tie this to a user input but for now its like this
    img_number = 5

    captureImage = cv2.VideoCapture(0)
    for imgFrame in range(img_number):
        print('Collecting frame {}'.format(imgFrame))
        ret, f = captureImage.read()
        imgName = os.path.join(img_path,f'{str(uuid.uuid1())}.jpg')
        cv2.imwrite(imgName, f)
        cv2.imshow('frame', f)
        time.sleep(0.5)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    captureImage.release()
    cv2.destroyAllWindows()
    return

# if you're gonna make a scraper 
def gatherWebData():
    return