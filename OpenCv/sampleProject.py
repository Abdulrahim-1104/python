#workouting the project of image matching
import cv2
import numpy as np
cv2.namedWindow("0",cv2.WINDOW_NORMAL)
cv2.namedWindow("1",cv2.WINDOW_NORMAL)
cv2.namedWindow("2",cv2.WINDOW_NORMAL)
cv2.resizeWindow("1",640,280)
cv2.resizeWindow("2",640,280)
cv2.resizeWindow("0",800,800)
img1 = cv2.imread("resources/orginal500.jpg",0)
img2 = cv2.imread("resources/500.jpg",0)
img2 = cv2.equalizeHist(img2)
orb = cv2.ORB_create(nfeatures=1000)
kp1,des1 = orb.detectAndCompute(img1,None)
kp2,des2 = orb.detectAndCompute(img2,None)
imgKp1 = cv2.drawKeypoints(img1,kp1,None)
imgKp2 = cv2.drawKeypoints(img2,kp2,None)
bf=cv2.BFMatcher()
matches=bf.knnMatch(des1,des2,k=2)
good=[]
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])
print(len(good))
img3=cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None)
cv2.imshow("0",img3)
cv2.imshow("1",imgKp1)
cv2.imshow("2",imgKp2)
cv2.waitKey(0)