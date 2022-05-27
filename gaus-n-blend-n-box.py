import cv2
import numpy as np
from matplotlib import pyplot as plt


imag = cv2.imread('functions - WIP/test_4.jpeg',0)
Blu = cv2.medianBlur(imag,5)

sob = cv2.adaptiveThreshold(Blu,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)

plt.subplot(2,1,1),plt.imshow(imag,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,3),plt.imshow(Blu,cmap = 'gray')
# plt.title('Median Blur'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,4),plt.imshow(sob,cmap = 'gray')
# plt.title('Adaptive Mean Thresholding'), plt.xticks([]), plt.yticks([])

arr = np.uint8(sob)
# plt.show()
print(sob.shape)
print(arr.shape)
ret,thresh = cv2.threshold(arr,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    if w >= 10 and h >= 10:
        arr = cv2.rectangle(arr,(x,y),(x+w,y+h),(0,255,0),2)
print("Number of contours:" + str(len(contours)))

# cv2.imshow("result",arr)
# cv2.waitKey(0)

plt.subplot(2,1,2),plt.imshow(arr,cmap = 'gray')
plt.title('Boxed'), plt.xticks([]), plt.yticks([])

plt.show()
