import cv2
import numpy as np
#creating an image with mumpy matrix
img=np.zeros((512,512),np.uint8)
#putting text on image         orgin          font              scale color    thick
cv2.putText(img,"Hello World",(100,100),cv2.FONT_HERSHEY_COMPLEX,2,(255,150,0),3)
cv2.imshow("output",img)
cv2.waitKey(0)