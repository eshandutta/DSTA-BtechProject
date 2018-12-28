import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

font={'family':'serif',
      'color':'darkred',
      'weight':'normal',
      'size':16,
      }
img = cv.imread('LeafMold.jpg',0)

ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

circles = cv.HoughCircles(thresh2,cv.HOUGH_GRADIENT,1,20,param1=200,param2=10,minRadius=0,maxRadius=30)

count=0
for i in circles[0,:]:
    count=count+1
comment="Leaf is not Healthy."
DiseaseSeptoria="The Disease is Septoria Leaf Spot"
SolutionSeptoria="Apply Chlorothalonil."

DiseaseLeafMold="The Disease is Leaf Mold"
SolutionLeafMold="Apply Baking Soda"


plt.subplot(2,3,1),plt.imshow(thresh2,'gray')
plt.xticks([]),plt.yticks([])
plt.subplot(2,3,2),plt.imshow(thresh3,'gray')
plt.xticks([]),plt.yticks([])
plt.subplot(2,3,3),plt.imshow(thresh4,'gray')
plt.xticks([]),plt.yticks([])
plt.subplot(2,3,4),plt.imshow(thresh5,'gray')
plt.xticks([]),plt.yticks([])


if count > 5 and count <60:
    plt.text(2,220,comment,fontdict=font)
    plt.text(2,270,DiseaseSeptoria,fontdict=font)
    plt.text(2,320,SolutionSeptoria,fontdict=font)
    plt.text(2,370,count,fontdict=font)
else:
    plt.text(2,550,comment,fontdict=font)
    plt.text(2,600,DiseaseLeafMold,fontdict=font)
    plt.text(2,650,SolutionLeafMold,fontdict=font)
    #plt.text(2,700,count,fontdict=font)
plt.show()

cv.waitKey(0) % 0xFF
cv.destroyAllWindows()

