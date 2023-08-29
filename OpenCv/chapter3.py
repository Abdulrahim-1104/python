# Resizing the image and Cropping the image
import cv2
img=cv2.imread("resources/img2.jpg")
print(img.shape)
#resizing the image
resizer=cv2.resize(img,(600,100))
#cropping the image
crop=img[0:200,200:400]
cv2.imshow("output",crop)
cv2.waitKey(0)