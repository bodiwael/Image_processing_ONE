import cv2

import numpy as np

img = cv2.imread("image3.png")

img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_canny = cv2.Canny(img, 25 , 255)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

low_dark_red = np.array([150, 10, 0]).reshape((1,1,3))

high_dark_red = np.array([255, 255, 255]).reshape((1,1,3))

lower_yellow = np.array([22, 93, 0]).reshape((1,1,3))

upper_yellow = np.array([45, 255, 255]).reshape((1,1,3))

red_mask = cv2.inRange(img_hsv, low_dark_red, high_dark_red)

yellow_mask = cv2.inRange(img_hsv, lower_yellow, upper_yellow)

cont, _ = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

c = max(cont, key = cv2.contourArea)

x,y,w,h = cv2.boundingRect(c)

if ((h > 50) & (w > 50)):
    
    print("detected")

    cont_img  = cv2.drawContours(img, cont, -1 , 255 , 3)
    
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255 , 0), 1)
    
    cv2.imshow("cont", cont_img)
    
cv2.imshow("Final", img)
    
cv2.imshow("HSV", red_mask)

cv2.imshow("HSVV", yellow_mask)

cv2.imshow("Original", img)

cv2.waitKey(0)

cv2.destroyAllWindows()
