import cv2
import numpy as np
 
img = cv2.imread('anthracnose.jpg',cv2.IMREAD_GRAYSCALE)



filter = cv2.Canny(img,100,200)
 
cv2.imshow('Original',img)


cv2.imshow('Canny Filter',filter)


 
cv2.waitKey(0)
