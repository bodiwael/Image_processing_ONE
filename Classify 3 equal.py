import cv2

img = cv2.imread('image1.png')

height = img.shape[0]

width = img.shape[1]

width_cutoff = width // 3

left = img[:, :width_cutoff]

center = img[:, width_cutoff:width_cutoff*2]

right = img[:, width_cutoff*2:]

cv2.imshow("h1", left)

cv2.imshow("h2", center)

cv2.imshow("h3", right)

cv2.waitKey(0)

cv2.destroyAllWindows()