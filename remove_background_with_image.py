import cv2
import numpy as np

# remove backgroun of image using image of background
def background_removal_with_img(original_img, bacground_img):
    img = cv2.imread(original_img)
    kernel = np.ones((5,5),np.float32)/25
    background = cv2.filter2D(cv2.imread(bacground_img), -1, kernel)
    img = cv2.subtract(img, background)
    return img

img = background_removal_with_img('mini_valdi/test_1_416_416bd0627650bc1953369b0e2bf0703fd55.jpg', 'backgrounds/Image__2022-07-07__09-45-20_0_1248.jpg')
cv2.imwrite('test_background_removed.jpg', img)
    