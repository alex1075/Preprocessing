import cv2
import glob, os
from PIL import Image
import numpy as np
import random
import shutil
import decimal

#Grabs biggest dimension and scales the photo so that max dim is now 1280
def resizeTo(image, newhigh=1280, newwid=1280, inter=cv2.INTER_AREA):
    (height, width) = image.shape[:2]
    if height>width:
        newheight = newhigh
        heightratio = height/newheight
        newwidth = int(width/heightratio)
        resized = cv2.resize(image, dsize=(newwidth, newheight), interpolation=inter)
        return resized, newheight, newwidth
    elif width>height:
        newwidth = newwid
        widthratio = width/newwidth
        newheight = int(height/widthratio)
        resized = cv2.resize(image, dsize=(newwidth, newheight), interpolation=inter)
        return resized, newheight, newwidth
    else: 
        print('Error')


def normaliseImg(self, img):
    if np.max(img)==np.min(img):
        img_norm = (img - np.min(img)) / (np.max(img+1) - np.min(img-1))
    else:
        img_norm = (img - np.min(img)) / (np.max(img) - np.min(img))
    return (img_norm * 2) - 1

def softNormaliseImg(self, img):
    pmin = np.percentile(img, 1)
    img_norm = ((img - pmin)/(np.percentile(img, 99) - pmin))
    return (img+1)/2

def normaliseImgBack(self, img):    
    return (img+1)/2

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def rgb2gray(img):
    img = cv2.imread(img,0)
    return img

def merge_contours(cnts):
    # merge bounding boxes
    merged_cnts = []
    for cnt in cnts:
        x,y,w,h = cv2.boundingRect(cnt)
        merged_cnts.append(cnt)
    return merged_cnts

def randomSelect(pathtofolder, destfolder, num):
    file_list = os.listdir(pathtofolder)
    for i in range(num):
        a = random.choice(file_list)
        #file_list.remove(a)
        shutil.copy(pathtofolder + a, destfolder + a)


def remove_non_annotated(pathtofolder):
    images = os.listdir(pathtofolder)
    for image in images:    
        if image.endswith(".jpg"):
            # check file exists
            if os.path.isfile(pathtofolder + image[:-4] + '.txt'):
               print("Annotation file exists")
            else:
                os.remove(pathtofolder + image[:-4] + '.jpg')
                print("Annotation file does not exist")
                print("Image removed: " + image)

def change_annotation(i, j, x, y, height, width, path, image, save_name, save_path):
    # read annotation
    with open(path + image[:-4] + '.txt', 'r') as f:
        lines = f.readlines()
    # loop over lines
    for line in lines:
        # get line
        line = line.split(' ')
        # get coordinates
        classes = int(line[0])
        print("Class: " + str(classes))
        x1 = decimal.Decimal(line[1]) #centre x
        print("X1: " + str(x1))
        y1 = decimal.Decimal(line[2]) #centre y
        print("Y1: " + str(y1))
        x2 = decimal.Decimal(line[3]) #width
        print("X2: " + str(x2))
        y2 = decimal.Decimal(line[4]) #height
        print("Y2: " + str(y2))
        if int(x1 * width) in range(j, j + x, 1):
                if int(y1 * height) in range(i, i + y, 1):
                        # get new coordinates
                        x1 = decimal.Decimal(((x1 * width) - j ) / x)
                        y1 = decimal.Decimal(((y1 * height) - i) / y)
                        x2 = decimal.Decimal(str((x2 * width) / x))
                        y2 = decimal.Decimal(str((y2 * height) / y))
                        # write new coordinates
                        with open(save_path + save_name + '.txt', 'a') as f:
                            f.write(str(classes))
                            f.write(' ')
                            f.write(str(round(x1, 6)))
                            f.write(' ')
                            f.write(str(round(y1, 6)))
                            f.write(' ')
                            f.write(str(round(x2, 6)))
                            f.write(' ')
                            f.write(str(round(y2, 6)))
                            f.write('\n')
                else:
                    pass
        else:
            pass