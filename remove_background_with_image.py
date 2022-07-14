import cv2
import numpy as np
from code.helper.imageTools import increase_brightness

# remove backgroun of image using image of background
def background_removal_with_img(original_img, bacground_img):
    img = cv2.imread(original_img)
    kernel = np.ones((5,5),np.float32)/25
    background = cv2.filter2D(cv2.imread(bacground_img), -1, kernel)
    img = cv2.subtract(img, background)
    return img

img = background_removal_with_img('data/test_1_416_0.jpg', 'backgrounds/background_416_416.jpg')
cv2.imwrite('test_background_removed.jpg', img)
    