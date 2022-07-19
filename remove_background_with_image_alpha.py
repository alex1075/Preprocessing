import cv2
import numpy as np



# remove backgroun of image using image of background
def background_removal_with_img(original_img, bacground_img, alpha=0.5):
    img = cv2.imread(original_img)
    # print(img)
    background = cv2.imread(bacground_img)
    # print(background)
    out = (alpha * ( img -  background ) + 128).clip(0,255)
    return out


# for i in np.arange(0, 4, 0.5):
#     print(i)
#     img = background_removal_with_img('data/test_1_416_416.jpg', 'backgrounds/background_416_416.jpg', i)
#     cv2.imwrite('test_background_removed_alpha_' + str(i) + '.jpg', img)

img = background_removal_with_img('data/test_1_416_416.jpg', 'backgrounds/background_416_416.jpg', 4)
cv2.imwrite('test_background_removed_alpha_4.jpg', img)
# print(img)