from transform import four_point_transform
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2
import ocr
import opencv_threashhold
import os
import time
import mqtt

TimeDelay = 15

def readImg(imgDir,pts):
    image = cv2.imread(imgDir)
    warped1 = four_point_transform(image, pts)
    #cv2.imshow("img", warped1)
    #cv2.waitKey(0)
    cv2.imwrite('imgTemp.png',warped1)
    opencv_threashhold.threshold_img('imgTemp.png')
    #print(ocr.text_from_image_file("imgTemp.png", "eng"))
    data = float(ocr.text_from_image_file("imgTemp.png", "eng"))
    payload = pos[0] + ' = ' + str(data)
    print(payload)
    mqtt.pubMQTT(payload)
    os.remove('imgTemp.png')
    os.remove('th.png')


while True:
    f = open('config2.txt', "r")
    pts = np.array([[0,0],[0,0],[0,0],[0,0]])
    f.readline().split()
    varlist = []
    try:
        while True:
            pos = f.readline().split()
            if pos == []:
                break
            else :
                varlist.append(pos[0])
                pts[0] = np.fromstring(pos[1],dtype=int,sep=',')
                pts[1] = np.fromstring(pos[2],dtype=int,sep=',')
                pts[2] = np.fromstring(pos[3],dtype=int,sep=',')
                pts[3] = np.fromstring(pos[4],dtype=int,sep=',')
                #print(varlist)
                #print(pts)
                readImg('test2.jpg',pts)
               
    except:
        print("We cant read variable from image. We will try again.")

    
    f.close()
    for x in range(TimeDelay):
        print ("wait for %d seconds for read again" % (TimeDelay-x))
        time.sleep(1)