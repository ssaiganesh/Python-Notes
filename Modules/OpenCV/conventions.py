import cv2
import numpy as np

img = cv2.imread("media/lambo.png")
print(img.shape)

# 462 is height 623 is width and 3 is the number of channels which is bgr

imgResize = cv2.resize(img, (300,200)) #can increase or decrease size 
print(imgResize.shape)

#in the openCV function of img, it was width , height

#BUT in cropped array, it is height , width

imgCropped = img[0:200, 200:500] #but this follows the img.shape array

cv2.imshow("Image", img)
cv2.imshow("Image Resized", imgResize)

cv2.waitKey(0)




