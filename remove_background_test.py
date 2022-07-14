import cv2
import numpy as np
from code.helper.imageTools import increase_brightness

# Read image
img = cv2.imread('data/test_1_416_0.jpg')
bacground = increase_brightness(cv2.imread('backgrounds/background_416_416.jpg'), 1000)
# revome background from img
img = cv2.absdiff(img, bacground)
# convert to uint8

# save image
# cv2.imwrite('predictions/test_1_416_416bd0627650bc1953369b0e2bf0703fd55.jpg', img)
cv2.imshow('img', img)
cv2.waitKey(0)
