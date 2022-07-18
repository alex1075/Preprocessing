from colorthief import ColorThief
import cv2
import numpy as np

color_thief = ColorThief('data/test_1_416_0.jpg')
# get the dominant color
dominant_color = color_thief.get_color(quality=1)
print(dominant_color)

# blank_image = np.zeros((416,416,3), np.uint8)
# blank_image[:] = dominant_color
# # cv2.imshow('img', blank_image)
# # cv2.waitKey(0)

# # remove backgroun of image using image of background
# def background_removal(original_img):
#     img = cv2.imread(original_img)
#     color_thief = ColorThief(original_img)
#     dominant_color = color_thief.get_color(quality=1)
#     background_img = np.zeros((416,416,3), np.uint8)
#     background_img[:] = dominant_color
#     kernel = np.ones((5,5),np.float32)/25
#     background = cv2.filter2D(background_img, -1, kernel)
#     img = cv2.subtract(img, background_img)
#     # img = cv2.absdiff(img, background)
#     return img

# img = cv2.imread('data/test_1_416_0.jpg', 1)
# # converting to LAB color space
# lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
# l_channel, a, b = cv2.split(lab)

# # Applying CLAHE to L-channel
# # feel free to try different values for the limit and grid size:
# clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
# cl = clahe.apply(l_channel)

# # merge the CLAHE enhanced L-channel with the a and b channel
# limg = cv2.merge((cl,a,b))

# # Converting image from LAB Color model to BGR color spcae
# enhanced_img = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

# # Stacking the original image with the enhanced image
# result = np.hstack((img, enhanced_img))
# img = result
# color_thief = ColorThief(result)
# dominant_color = color_thief.get_color(quality=1)
# background_img = np.zeros((416,416,3), np.uint8)
# background_img[:] = dominant_color
# kernel = np.ones((5,5),np.float32)/25
# background = cv2.filter2D(background_img, -1, kernel)
# img = cv2.subtract(img, background_img)
# from code.helper.imageTools import increase_brightness
# # img = increase_brightness(img, 100)
# cv2.imwrite('test_background_removed.jpg', img)