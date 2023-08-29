# chapter 1
# In this chapter we're gonna learn how to read and show image and video
import cv2
print("Package imported")
img = cv2.imread("resources/img4.jpg")
#cv2.imshow("output",img)
#cv2.waitKey(0)

# Reading video
#cap=cv2.VideoCapture("resources/vid1.mp4")
#diplaying video
#while True:
 #   success,img=cap.read()
  #  cv2.imshow("video",img)
   # if cv2.waitKey(1) & 0xFF == ord('q'):
     #   break
#Reading webcame
cap=cv2.VideoCapture(0)
       #this is the id like 3 for width and 4 for height and 10 for brightness
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
# diplaying webcam is same as video displaying
while True:
    success,img=cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break