import cv2
#import cv2.cv as cv
import numpy as np

pic= cv2.imread('anthracnose2.jpg', 0)

blur = cv2.GaussianBlur(pic,(3,3),0)

th1 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,30)

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(th1,kernel,iterations = 1)

cv2.imwrite('modified2_blur.jpg',blur)
cv2.imwrite('modified2_th1.jpg',th1)
cv2.imwrite('modified2_kernel.jpg',kernel)
cv2.imwrite('modified2_erosion.jpg',erosion)
cv2.waitKey(0) % 0xFF
cv2.destroyAllWindows()
