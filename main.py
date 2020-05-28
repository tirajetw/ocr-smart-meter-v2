from transform import four_point_transform
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2
import ocr
import opencv_threashhold
import os
import time
#import serial   
import mqtt

cnt = 0
msg = ''
payload = ''
pts = np.array([[0,0],[0,0],[0,0],[0,0]])
data = [0,0,0,0,0,0,0,0]
dec = 0
varlist = []
TimeDelay = 15

def hex2serial(data):
    #port = serial.Serial('/dev/ttyS0',9600)
    hexdata = hex(data)
    print(hexdata) #type : str
    #port.write((hexdata.encode()))
    return hexdata

def convert(list): 
    # Converting integer list to string list 
    # and joining the list using join() 
    res = int("".join(map(str, list))) 
      
    return res 

def readImg(imgDir,pts):
    image = cv2.imread(imgDir)
    warped1 = four_point_transform(image, pts)
    #cv2.imshow("img", warped1)
    #cv2.waitKey(0)
    cv2.imwrite('imgTemp.png',warped1)
    opencv_threashhold.threshold_img('imgTemp.png')
    #print(ocr.text_from_image_file("imgTemp.png", "eng"))
    data[dec] = int(ocr.text_from_image_file("th.png", "eng"))
    msg = pos[0] + ' = ' + str(data[dec])
    print(msg)
    #os.remove('imgTemp.png')
    
while True:
    os.system('raspistill -o img.jpg')
    f = open('config.txt', "r")
    f.readline().split()
    while True:
        try:
            pos = f.readline().split()

            if pos == []:
                print("finish!")
                break
            else :
                varlist.append(pos[0])
                pts[0] = np.fromstring(pos[1],dtype=int,sep=',')
                pts[1] = np.fromstring(pos[2],dtype=int,sep=',')
                pts[2] = np.fromstring(pos[3],dtype=int,sep=',')
                pts[3] = np.fromstring(pos[4],dtype=int,sep=',')
                #print(varlist)
                #print(pts)
                dec += 1
                readImg('test.jpg',pts)
                os.remove('th.png')
                os.remove('imgTemp.png')

        except:
            print('We cant read variable from image. We will try again.')
    print(data)
    print(convert(data))
    mqtt.pubMQTT(hex2serial(convert(data)))
    dec = 0
    data = [0,0,0,0,0,0,0,0]
    f.close()
    for x in range(TimeDelay):
        print ("wait for %d seconds for read again" % (TimeDelay-x))
        time.sleep(1)