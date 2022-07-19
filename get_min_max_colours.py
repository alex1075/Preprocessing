import cv2
import numpy as np

# load image 
img = cv2.imread('data/test_1_416_416.jpg')
red_channel = img[:,:,2]

print(np.min(red_channel))
print(np.max(red_channel))