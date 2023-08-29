import cv2
import numpy as np
# detecting a color in an image
def empty(a):
    pass
#Window arrangement
cv2.namedWindow("output",cv2.WINDOW_NORMAL)
cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar",640,240)
#creaing a trackbar for hsv min and max
cv2.createTrackbar("Hue Min","Trackbar",0,179,empty)
cv2.createTrackbar("Hue Max","Trackbar",137,179,empty)
cv2.createTrackbar("Sat Min","Trackbar",77,255,empty)
cv2.createTrackbar("Sat Max","Trackbar",255,255,empty)
cv2.createTrackbar("Val Min","Trackbar",210,255,empty)
cv2.createTrackbar("Val Max","Trackbar",255,255,empty)
while True:
    # importing image
    img = cv2.imread("resources/img5.jpg")
    # creaing an HSV image
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hMin = cv2.getTrackbarPos("Hue Min","Trackbar")
    hMax = cv2.getTrackbarPos("Hue Max","Trackbar")
    sMin = cv2.getTrackbarPos("Sat Min", "Trackbar")
    sMax = cv2.getTrackbarPos("Sat Max", "Trackbar")
    vMin = cv2.getTrackbarPos("Val Min", "Trackbar")
    vMax = cv2.getTrackbarPos("Val Max", "Trackbar")
    #creating a lower value array for mask image
    lower=np.array([hMin,sMin,vMin])
    #creating a upper value array for mask image
    upper=np.array([hMax,sMax,vMax])
    print(lower)
    print(upper)
    #creating a mask image
    mask=cv2.inRange(imgHsv,lower,upper)
    #creating an new image by the combination of mask image and orginal image
    imgResult=cv2.bitwise_and(img,img,mask=mask)
    #cv2.imshow("output",imgHsv)
    #cv2.imshow("output",mask)
    cv2.imshow("output",imgResult)
    cv2.waitKey(1)