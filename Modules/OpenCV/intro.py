import cv2

print("Package Imported")


#FOR IMAGES

"""  
img = cv2.imread("media/lena.png")

cv2.imshow("Output", img)  #appear and disappears immediately hence have to give delay

cv2.waitKey(0) #0 means infinite delay , 

# 1000 means 1000 ms that is 1 second. 
"""
"""
#FOR VIDEOS
cap = cv2.VideoCapture("media/test_video.mp4")
while True:
    success, img = cap.read() 
    #success is booelan shows us if successfully read, and img is the variable where the video is saved under in code 
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'): 
        break
    #delays and waits for key press q to break the loop
"""

#For WebCam
cap = cv2.VideoCapture(0) #if webcam linked to laptop, 1 if more than 1 webcam
cap.set(3, 640) #width is id no 3. 
cap.set(4,480) #height is id no 4. 
cap.set(10,100) #brightness is id no 10.
while True:
    success, img = cap.read() 
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'): 
        break