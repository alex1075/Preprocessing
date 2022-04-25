import shutil
import cv2
import glob, os, datetime
from imutils import paths
import shutil

def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()

def detectAndMoveBlurr(path_to_folder='/Volumes/PHD/', threshold=100.0):
    file = open(path_to_folder + 'recap.txt', "w")
    file.write('Threshold: ' + str(threshold) + '\n')
    print('Detecting blurr')
    os.makedirs(path_to_folder + 'threshold_' + str(threshold), exist_ok=True)
   # loop over the input images
    for imagePath in paths.list_images(path_to_folder):
        # load the image, convert it to grayscale, and compute the
        # focus measure of the image using the Variance of Laplacian
        # method
        print("Checking image: " + imagePath)
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fm = variance_of_laplacian(gray)
        # if the focus measure is less than the supplied threshold,
        # then the image should be considered "blurry"
        if fm < threshold:
            print(imagePath)
            # file.write(fm + "<" + threshold + '\n')
            file.write('Below threshold' + imagePath + '\n')
            shutil.move(imagePath, path_to_folder + 'threshold_' + str(threshold))
            print("Moved " + imagePath)
            file.write('Moved ' + imagePath + ' to folder' + '\n')
    file.close()

def iterateBlurMove(path_to_folder='/Volumes/PHD/', start=0, end=100, step=5):
    for i in range(start, end, step):
        print('Threshold: ' + str(i))
        detectAndMoveBlurr(path_to_folder, threshold=i)