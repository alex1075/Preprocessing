import numpy as np
import cv2



im = cv2.imread('test_1.jpg',cv2.IMREAD_COLOR)
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for data in contours:
    print("The contours have this data %r" %data)
cnt = contours[4]
x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('output',im)
while True:
    if cv2.waitKey(6) & 0xff == 27:
        break