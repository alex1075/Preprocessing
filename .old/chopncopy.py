import os
import cv2
import shutil
import decimal



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

#cv2.copyMakeBorder(src, top, bottom, left, right, bordertype, )




# crop images in chunks of size (x,y) and adapt annotations
def crop_images(x, y, path, save_path):
    shutil.copy(path + "classes.txt", save_path)
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
                    change_annotation(i, j, x, y, height, width, path, image, new_name, save_path)
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
                

def checkAllImg(path, x, y):
    images = os.listdir(path)
    for image in images:
        if image.endswith(".jpg"):
            imgSizeCheck(image, path, x, y)

# crop_images(416, 416, 'test_dataset/', 'output/')
# remove_non_annotated('output/')
checkAllImg('output/', 416, 416)
# imgSizeCheck('test_1_0_2912.jpg', 'output/', 416, 416)
