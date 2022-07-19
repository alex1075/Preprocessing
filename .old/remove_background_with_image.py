import cv2
import numpy as np
from code.helper.imageTools import increase_brightness

# remove backgroun of image using image of background
def background_removal_with_img(original_img, bacground_img):
    img = cv2.imread(original_img)
    # img = increase_brightness(img, 100)
    kernel = np.ones((5,5),np.float32)/25
    background = cv2.filter2D(increase_brightness(cv2.imread(bacground_img)), -1, kernel)
    img = cv2.subtract(img, background)
    return img


img = cv2.imread('data/test_1_416_416.jpg', 1)
# converting to LAB color space
lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
l_channel, a, b = cv2.split(lab)

# Applying CLAHE to L-channel
# feel free to try different values for the limit and grid size:
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl = clahe.apply(l_channel)

# merge the CLAHE enhanced L-channel with the a and b channel
limg = cv2.merge((cl,a,b))

# Converting image from LAB Color model to BGR color spcae
enhanced_img = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

# Stacking the original image with the enhanced image
result = np.hstack((img, enhanced_img))
# cv2.imshow('Result', result)

img = background_removal_with_img(result, 'backgrounds/background_416_0.jpg')
cv2.imwrite('test_background_removed.jpg', img)

