import cv2
import numpy as np

img = cv2.imread("media/cards.jpg")

width, height = 250,350 #typical playing cards size 

pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])#THESE ARE THE 4 points of Spades card(bottom)
#how the points were known? Using paint. You can see the pixels at bottom of paint screen at the 4 corners
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img, matrix,(width, height))


cv2.imshow("Image", img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)
