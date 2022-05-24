import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('functions - WIP/test_1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.ADAPTIVE_THRESH_MEAN_C)

# noise removal
kernel = np.ones((1,1),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 1)

# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=4)

# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,3)
ret, sure_fg = cv2.threshold(dist_transform,0.5*dist_transform.max(),255,0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)

# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

# Now, mark the region of unknown with zero
markers[unknown==255] = 0

markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(gray,cmap = 'gray')
plt.title('Grey'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sure_fg,cmap = 'gray')
plt.title('Foreground'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(sure_bg,cmap = 'gray')
plt.title('Background'), plt.xticks([]), plt.yticks([])

plt.show()