import os, glob
import cv2
import numpy as np
import imgaug as ia
import imgaug.augmenters as iaa
from code.helper.utils import *

# Changes the images by cropping randomly through them
def getRandomCrop(self, img, crop_height, crop_width):
        max_x = np.shape(img)[1] - crop_width
        max_y = np.shape(img)[0] - crop_height
        x = np.random.randint(1, max_x-1)
        y = np.random.randint(1, max_y-1)
        crop = img[y:y+crop_height, x:x+crop_width]
        # Apply augmentation to sample        
        seq = iaa.Sequential([
            iaa.Fliplr(0.5),
            iaa.Flipud(0.5),
        ])  
        crop = seq.augment_image(crop)
        return np.expand_dims(crop, axis=-1)

# Change the contrast of an image (positive values to increase, negative values to decrease)
def imageContrastIncrease(self, img, intensity):
        ones = np.ones((img.shape[0], img.shape[0]))
        contrast_increase = ones*intensity
        increased = np.multiply(img,contrast_increase)
        if np.max(increased)>1:
            increased = np.clip(increased, -1, 1)
        return np.array(increased, dtype='float')

# Play with brightness
def imageBrightnessDecrease(self, img, intensity):
    img = np.array(img)
    print(np.max(img))
    print(img.shape)
    ones = np.ones((img.shape[0],img.shape[0]))
    brightness_decrease = ones*intensity
    decreased = img-brightness_decrease
    if np.min(decreased)<0:
        decreased = np.clip(decreased, -1, 1)
    return np.array(decreased, dtype='float')


def imageBrightnessIncrease(self, img, intensity):
    img = np.array(img)
    print(np.max(img))
    print(img.shape)
    ones = np.ones((img.shape[0],img.shape[0]))
    brightness_increase = ones*intensity
    increased = img-brightness_increase
    if np.min(increased)<0:
        decreased = np.clip(increased, -1, 1)
    return np.array(increased, dtype='float')

# Add gaussian blur to images.
def gaussianBlur(self, img, Intensity=1):
    ImageArray = img
    kernel = np.ones((3, 3), np.float32)
    kernel[0] = [1,2,1]
    kernel[1] = [2,4,2]
    kernel[2] = kernel[0]
    kernel = (kernel * Intensity)/16
    blurred = cv2.filter2D(ImageArray, -1, kernel)
    return blurred

# Randomly crop out a section of an image dependng on the requred size
def getRandomCrop(image, crop_height, crop_width):
    max_x = image.shape[1] - crop_width
    max_y = image.shape[0] - crop_height
    x = np.random.randint(0, max_x)
    y = np.random.randint(0, max_y)
    crop = image[y: y + crop_height, x: x + crop_width]
    return crop

# Sharpen image using an unsharp mask
def unsharp_mask(image, kernel_size=(5, 5), sigma=1.0, amount=1.0, threshold=0):
    """Return a sharpened version of the image, using an unsharp mask."""
    blurred = cv2.GaussianBlur(image, kernel_size, sigma)
    sharpened = float(amount + 1) * image - float(amount) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)
    if threshold > 0:
        low_contrast_mask = np.absolute(image - blurred) < threshold
        np.copyto(sharpened, image, where=low_contrast_mask)
    return sharpened

def sobel_img(image, kernel_size=5):
    sobelx = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=kernel_size)
    sobely = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=kernel_size)
    sa = cv2.addWeighted(sobelx,1,sobely,1,0)
    sar = np.uint8(sa)
    return sar

def imgSizeCheck(image, path, x, y):
    img = cv2.imread(path + image)
    # get image dimensions
    height, width, channels = img.shape
    # cv2.imshow('Original', img)
    # cv2.waitKey(0)
    if height << y:
        diff = y - height
        difftoo = x - width
        corrected_img = cv2.copyMakeBorder(img, 0, diff, 0, difftoo,  cv2.BORDER_CONSTANT, value=[0,0,0])
        print("Added black border to image.")
        # cv2.imshow('Corrected', corrected_img)
        # cv2.waitKey(0)
        cv2.imwrite(path + image[:-4] + ".jpg", corrected_img)
    elif width << x:
        diff = y - height
        difftoo = x - width
        corrected_img = cv2.copyMakeBorder(img, 0, diff, 0, difftoo,  cv2.BORDER_CONSTANT, value=[0,0,0])
        print("Added black border to image.")
        cv2.imshow(corrected_img)
        cv2.imwrite(path + image[:-4] + ".jpg", corrected_img)
    else:
        print("No change to image.")
        # pass

# crop images in chunks of size (x,y) and adapt annotations
def crop_images(x, y, path, save_path, annotations=True):
    if annotations == True:
        shutil.copy(path + "classes.txt", save_path)
    else:
        pass
    # get all images in path
    images = os.listdir(path)
    # print(images)
        # loop over images
    for image in images:
        # read image
        if image.endswith(".jpg"):
            img = cv2.imread(path + image)
            # get image dimensions
            height, width, channels = img.shape
            # loop over image
            for i in range(0, height, y):
                for j in range(0, width, x):
                    # crop image
                    crop_img = img[i:i+y, j:j+x]
                    # set new name
                    new_name = image[:-4] + '_' + str(i) + '_' + str(j)
                    # save image
                    cv2.imwrite(save_path + new_name + ".jpg", crop_img)
                    # adapt annotation
                    if annotations == True:
                        change_annotation(i, j, x, y, height, width, path, image, new_name, save_path)
                    else:
                        pass
                img = cv2.imread(path + image)
                # print(img)
            # get image dimensions
            height, width, channels = img.shape
            # loop over height
            for i in range(0, height, y):
              # loop over width
                 for j in range(0, width, x):
                    # crop image
                    crop = img[i:i+y, j:j+x]
                   # save image
                    cv2.imwrite(save_path + image[:-4] + '_' + str(i) + '_' + str(j) + '.jpg', crop)
        else:
            pass

def checkAllImg(path, x, y):
    images = os.listdir(path)
    for image in images:
        if image.endswith(".jpg"):
            imgSizeCheck(image, path, x, y)

def del_top_n_bottom_parts(path, save_path, annotations=True):
    if annotations==True:
        os.system('cd' + path + ' && rm *_1248_*.txt *_1664_*.txt *_0_*.txt *_0_*.jpg *_1248_*.jpg *_1664_*.jpg')
    else:
        os.system('cd' + path + ' && rm *_0_*.jpg *_1248_*.jpg *_1664_*.jpg')


def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

# remove backgroun of image using image of background
def background_removal_with_alpha(original_img, bacground_img, alpha=0.5):
    img = cv2.imread(original_img)
    background = cv2.imread(bacground_img)
    img = img.astype('f')
    background = background.astype('f')
    out = (alpha * ( img -  background ) + 128).clip(0, 255)
    out = np.around(out, decimals=0)
    out = out.astype(np.uint8)
    return out