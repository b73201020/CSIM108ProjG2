#Install OpenCV 3 with Python 3 on Windows
#https://www.solarianprogrammer.com/2016/09/17/install-opencv-3-with-python-3-on-windows/

import numpy
import cv2
print(numpy.__version__)
print(cv2.__version__)

from cv2 import *
# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
s, img = cam.read()
if s:    # frame captured without any errors
    namedWindow("cam-test",WINDOW_AUTOSIZE)
    imshow("cam-test",img)
    waitKey(0)
    destroyWindow("cam-test")
    imwrite("filename1.jpg",img) #save image