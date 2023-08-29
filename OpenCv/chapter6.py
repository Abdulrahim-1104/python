#joining an image in horizondal and vertical
import cv2
import numpy as np
cv2.namedWindow("ver", cv2.WINDOW_NORMAL)
cv2.namedWindow("hor", cv2.WINDOW_NORMAL)
#starting
img=cv2.imread("resources/img4.jpg")
ver=np.hstack((img,img))
hor=np.vstack((img,img))
cv2.imshow("ver",ver)
cv2.imshow("hor",hor)
cv2.waitKey(0)
