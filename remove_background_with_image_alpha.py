import cv2
import numpy as np



# remove backgroun of image using image of background
def background_removal_with_img(original_img, bacground_img, alpha=0.5):
    img = cv2.imread(original_img)
    background = cv2.imread(bacground_img)
    out = alpha * ( img -  background ) + (128, 128, 128)
    return out



# for i in np.arange(0, 4, 0.5):
#     print(i)
#     img = background_removal_with_img('data/test_1_416_416.jpg', 'backgrounds/background_416_416.jpg', i)
#     cv2.imwrite('test_background_removed_alpha_' + str(i) + '.jpg', img)

img = background_removal_with_img('data/test_1_416_416.jpg', 'backgrounds/background_416_416.jpg', 4)
cv2.imwrite('test_background_removed_alpha_40.jpg', img)