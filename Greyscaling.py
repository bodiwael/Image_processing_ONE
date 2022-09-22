import cv2
import numpy as np
import matplotlib.pyplot as plt

bear = cv2.imread('bear1.jpeg')

cup = cv2.imread('cup.jpeg')

def Greyscaling(image):
    
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('Grey', grey)
    
Greyscaling(bear)

cv2.waitKey(0)

cv2.destroyAllWindows()