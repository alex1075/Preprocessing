import os
from unicodedata import name
import cv2
import numpy as np



# remove backgroun of image using image of background
def background_removal_with_alpha(original_img, bacground_img, alpha=0.5):
    img = cv2.imread(original_img)
    print(img.dtype)
    print(img[0,0])
    background = cv2.imread(bacground_img)
    print(background.dtype)
    img = img.astype('f')
    background = background.astype('f')
    print(background[0,0])
    out = (alpha * ( img -  background ) + 128).clip(0, 255)
    # out = (alpha * ( img[0,0] -  background[0,0] ) + 128)
    out = np.around(out, decimals=0)
    out = out.astype(np.uint8)
    return out



# img = background_removal_with_alpha('data/test_1_416_416.jpg', 'backgrounds/background_416_416.jpg', 0.5)
# cv2.imwrite('test_background_removed_alpha_0ad-5.jpg', img)
# print(img.dtype)
# print(img)

def batchBackgroundRemove(path_to_folder='output/', background_folder='backgrounds/', outfolder='data_2/', alpha=2):
    list_img=[img for img in os.listdir(path_to_folder) if img.endswith('.jpg')==True]
    list_background=[img for img in os.listdir(background_folder) if img.endswith('.jpg')==True]
    list_txt=[img for img in os.listdir(path_to_folder) if img.endswith('.txt')==True]
    for img in list_img:
        index = img.split('_')
        name = index[0] + '_' + index[1]
        first_chop = index[2]
        second_chop = index[3]
        condition = 'background''_' + str(first_chop) + '_' + str(second_chop)
        img_path = outfolder + img
        background_element = [x for x in list_background if x==condition]
        background = str(background_element[0])
        img = background_removal_with_alpha(path_to_folder+img, background_folder+background, alpha)
        cv2.imwrite(img_path, img)
        print('Matched ' + img_path + ' with ' + background)
        annotation_condition  = name + '_' + str(first_chop) + '_' + str(second_chop)[:-4] + '.txt'
        annotation_file = [x for x in list_txt if x==annotation_condition]
        annotation = str(annotation_file[0])
        print('Matched ' + annotation + ' with ' + annotation_condition)
        os.system('cp ' + path_to_folder + annotation + ' ' + outfolder + annotation)
    classes_file = [x for x in list_txt if x=='classes.txt']
    classes = str(classes_file[0])
    os.system('cp ' + path_to_folder + classes + ' ' + outfolder + classes)
    
    
        

batchBackgroundRemove()