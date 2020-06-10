import cv2
import numpy as np

img = cv2.imread("media/lena.png")
kernel = np.ones((5,5),dtype = np.uint8) # 5 x 5 arrays of ones. and uint8 ranges from 0 to 255

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray , (7,7),0) #has to be odd numbers, 3x3 , 5x5 or in this case 7x7
imgCanny = cv2.Canny(img, 150, 200)
imgDilation = cv2.dilate(imgCanny,kernel, iterations = 1) #increases thickness of lines of the canny image, iterations is how much thickness
imgEroded = cv2.erode(imgDilation,kernel, iterations = 1)


cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDilation)  #making border white and thicker  
cv2.imshow("Eroded Image", imgEroded)  #opposite of dilation, making it thinner
cv2.waitKey(0)  