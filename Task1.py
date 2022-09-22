import cv2

import numpy

import matplotlib.pyplot as plt

cat1 = cv2.imread('cat1.jpeg')

cat1 = cv2.resize(cat1, (250,250))

cat2 = cv2.imread('cat2.jpeg')

cat2 = cv2.resize(cat2, (250,250))

dog1 = cv2.imread('dog1.jpeg')

dog1 = cv2.resize(dog1, (250,250))

dog2 = cv2.imread('dog2.jpeg')

dog2 = cv2.resize(dog2, (250,250))

def Image_concatenations():

    verticalAppendedCat = numpy.vstack((cat1,cat2))

    verticalAppendedDog = numpy.vstack((dog1,dog2))

    horizontalAppendedImg = numpy.hstack((verticalAppendedCat,verticalAppendedDog))
     
    cv2.imshow('Final', horizontalAppendedImg)

def Feature_Matching():
    
    query_img_bw = cv2.cvtColor(cat1,cv2.COLOR_BGR2GRAY)
    train_img_bw = cv2.cvtColor(cat2, cv2.COLOR_BGR2GRAY)

    orb = cv2.ORB_create()

    queryKeypoints, queryDescriptors = orb.detectAndCompute(query_img_bw,None)
    trainKeypoints, trainDescriptors = orb.detectAndCompute(train_img_bw,None)


    matcher = cv2.BFMatcher()
    matches = matcher.match(queryDescriptors,trainDescriptors)


    final_img = cv2.drawMatches(cat1, queryKeypoints,
    cat2, trainKeypoints, matches[:20],None)

    final_img = cv2.resize(final_img, (1000,650))

    cv2.imshow("Matches", final_img)

def Thresholding():
    
    threshold = 64
    
    im = cv2.cvtColor(cat1, cv2.COLOR_RGB2YCR_CB)
    
    for row in cat1:
        
        for col in row:
        
            if col[0] > threshold:
            
                col[0] = threshold
                
    image = cv2.cvtColor(im, cv2.COLOR_YCR_CB2RGB)
    
    cv2.imshow("motorist_filtered", image)

def sharpening():
    
    kernel = numpy.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
    
    image_sharp = cv2.filter2D(src=cat2, ddepth=-1, kernel=kernel)
    
    cv2.imshow("Image Sharp", image_sharp)

def Edge_Detection():
    
    t_lower = 50  # Lower Threshold
    
    t_upper = 150  # Upper threshold
  
    # Applying the Canny Edge filter
    edge = cv2.Canny(dog1, t_lower, t_upper)
    
    cv2.imshow("Edge", edge)
    
Image_concatenations()

Feature_Matching()

Thresholding()

sharpening()

Edge_Detection()

cv2.waitKey(0)

cv2.destroyAllWindows()