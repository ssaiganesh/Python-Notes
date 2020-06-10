import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#print(img)
#img[:] =255,0,0 #this was used for cropping as well. 
#color part will only be in the range given 200:300

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
#in the above code, img.shape[1] is the height
# img.shape[0] is the width 

cv2.rectangle(img,(0,0),(250,350),(0,0,255),2) 
#2 is thickness, same for 3 in line, 5 in circle, 3 in text

#cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)
#to fill rectangle

cv2.circle(img, (400,50), 30,(255,255,0), 5)


cv2.putText(img, " OPENCV ", (300, 200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,150,0),3) #the 1 is scale, 3 is the thickness
#(300,200) is the grid location

#print(img.shape)

cv2.imshow("image", img)

cv2.waitKey(0)