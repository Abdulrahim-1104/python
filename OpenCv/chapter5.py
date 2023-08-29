import cv2
import numpy as np
# War Perspective
#92,215  953,135  257,2494 1205,1338
#importing a image
img=cv2.imread("resources\cards.jpg")
#creating the points for the specfic image in orginal image
#                left top   right top  left down  right down
pts1=np.float32([[521,445],[1365,361],[693,1705],[1633,1557]])
#creating the points for the output image size
pts2=np.float32([[0,0],[250,0],[0,350],[250,350]])
#creaing a matrix image for that image because warpperspective method need a matrix thats why
matrix = cv2.getPerspectiveTransform(pts1,pts2)
#finally creating a war perspective which means a specific image
image=cv2.warpPerspective(img,matrix,(250,350))
#displaying
cv2.imshow("ouput",image)
cv2.waitKey(0)