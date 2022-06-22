import os
from re import I
from turtle import width
import cv2
import albumentations as A

transform = A.Compose([
        A.HorizontalFlip(p=0.5),
        A.RandomBrightnessContrast(p=0.2)
], bbox_params=A.BboxParams(format='yolo'))

img = cv2.imread('/Users/alexanderhunt/Preprocessing/test_dataset/test_1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
