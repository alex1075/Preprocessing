import cv2
import numpy as np


image = cv2.imread('test_4.jpeg')

alpha = 1.5 # Contrast control (1.0-3.0)
beta = 0 # Brightness control (0-100)

adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

cv2.imshow('original', image)
cv2.imshow('adjusted', adjusted)
cv2.waitKey()

imgray = cv2.cvtColor(adjusted,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for data in contours:
    print("The contours have this data %r" %data)
cv2.drawContours(adjusted,contours,-1,(0,255,0),3)
cv2.imshow('output',adjusted)
while True:
    if cv2.waitKey(6) & 0xff == 27:
        break