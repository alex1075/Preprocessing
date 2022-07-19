import cv2
import numpy as np



# remove backgroun of image using image of background
def background_removal_with_alpha(original_img, bacground_img, alpha=0.5):
    img = cv2.imread(original_img)
    # print(img[0,0])
    background = cv2.imread(bacground_img)
    # print(background[0,0])
    out = (alpha * ( img -  background ) + 128).clip(0,255)
    # out = (alpha * ( img[0,0] -  background[0,0] ) + 128).clip(0,255)
    out = np.around(out, decimals=0).clip(0,255)
    out = out.astype(np.uint8)
    return out



img = background_removal_with_alpha('data/test_1_416_416.jpg', 'backgrounds/background_416_416.jpg', 1.5)
cv2.imwrite('test_background_removed_alpha_test_nparound.jpg', img)
# print(img)