import cv2
import numpy as np

img = cv2.imread('functions - WIP/test_1.jpg',0)
kernel = np.ones((2,2),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
cv2.imshow('eroded',erosion)
cv2.waitKey()