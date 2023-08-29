# Basic methods in OpenCv
import cv2
import numpy as np
#normal image importing
cv2.namedWindow("output", cv2.WINDOW_NORMAL)  #This code used to display the output window as normal
img=cv2.imread("resources/img4.jpg")
#converting normal image to grayscale image
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#converting normal image to blur image
blur=cv2.GaussianBlur(img,(111,111),0)
#edge Detector or canny edge detector
canny=cv2.Canny(img,50,50)
#dialation -it means gap image detector , which is used to thicker the image
kernel=np.ones((5,5),np.uint8)
dilation=cv2.dilate(canny,kernel,iterations=1)
#erosion-Is used to thinner the image and it is opposite to dilation
erosion=cv2.erode(dilation,kernel,iterations=1)
cv2.imshow("output",erosion)
cv2.waitKey(0)