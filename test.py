import cv2
import numpy as np
from code.helper.imageTools import *
# Read image
src = cv2.imread("functions - WIP/test_1.jpg", cv2.IMREAD_GRAYSCALE)
src = cv2.medianBlur(src,5)
src = cv2.adaptiveThreshold(src,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
scr = unsharp_mask(np.uint8(src))
# Set threshold and maxValue
thresh = 127 
maxValue = 255
# set an initial minimal contour size
minContourSize = 250
# create a window  (needed for use with trackbar)
cv2.namedWindow("Contour")

def setMinSize(val):
        # set the minimal contour size and find/draw contours
        global minContourSize
        minContourSize = val
        doContours()

def doContours():
        # create a copy of the image (needed for use with trackbar)
        res = src.copy()
        # find contours - external only
        
        countours,hierarchy=cv2.findContours(dst,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        # create an empty mask
        mask = np.zeros(src.shape[:2],dtype=np.uint8)
        # draw filled boundingrects if the contour is large enough
        for c in countours:
                if cv2.contourArea(c) > minContourSize:
                        x,y,w,h  = cv2.boundingRect(c)
                        cv2.rectangle(mask,(x,y),(x+w,y+h),(255),-1)

        # find the contours on the mask (with solid drawn shapes) and draw outline on input image
        countours,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        for c in countours:
                        cv2.drawContours(res,[c],0,(255,255,255),2)
        # show image
        cv2.imshow("Contour",res)

# create a trackbar to set the minContourSize - initial is set at 250,
# maximum value is currently set at 1500, you can increase it if you like
cv2.createTrackbar("minContourSize", "Contour",250,1500,setMinSize)
# Basic threshold example
th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY)
# Find Contours
doContours()
# waitkey to prevent program for exiting by itself
cv2.waitKey(0)
cv2.destroyAllWindows()

