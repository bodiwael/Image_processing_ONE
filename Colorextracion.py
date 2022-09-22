import cv2
import numpy as np

def callback(x):
    
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('image')

lowH = 0
highH = 179

lowS = 0
highS = 255
lowV = 0
highV = 255

cv2.createTrackbar('lowH','image',lowH,179,callback)
cv2.createTrackbar('highH','image',highH,179,callback)

cv2.createTrackbar('lowS','image',lowS,255,callback)
cv2.createTrackbar('highS','image',highS,255,callback)

cv2.createTrackbar('lowV','image',lowV,255,callback)
cv2.createTrackbar('highV','image',highV,255,callback)



while True:
    # grab the frame
    ret, frame = cap.read()

    # get trackbar positions
    lowH = cv2.getTrackbarPos('lowH', 'image')
    highH = cv2.getTrackbarPos('highH', 'image')
    lowS = cv2.getTrackbarPos('lowS', 'image')
    highS = cv2.getTrackbarPos('highS', 'image')
    lowV = cv2.getTrackbarPos('lowV', 'image')
    highV = cv2.getTrackbarPos('highV', 'image')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_hsv = np.array([lowH, lowS, lowV])
    higher_hsv = np.array([highH, highS, highV])
    mask = cv2.inRange(hsv, lower_hsv, higher_hsv)

    frame = cv2.bitwise_and(frame, frame, mask=mask)

    # show thresholded image
    cv2.imshow('image', frame)
    k = cv2.waitKey(1000) & 0xFF # large wait time to remove freezing
    if k == 113 or k == 27:
        break