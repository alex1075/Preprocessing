import os
import re
import random
import string
import cv2
import decimal
import numpy as np

"""
Classes:
0 - Red
1 - Green
2 - Blue
3 - Purple
4 - Yellow
5 - Cyan
6 - Orange
"""

def add_bbox(image, bbox, classes):
    image = cv2.imread(image)
    if classes == 0:
        colour = (0,0,255) #red
    elif classes == 1:
        colour = (0,255,0) #green
    elif classes == 2:
        colour = (255,0,0) #blue
    elif classes == 3:
        colour = (255,0,255) #fushia 
    elif classes == 4:
        colour = (255,255,0) #yellow
    elif classes == 5:
        colour = (0,255,255) #cyan
    elif classes == 6:
        colour = (255,172,28) #orange
    elif classes == 7:
        colour = (255,255,255) #white
    elif classes == 8:
        colour = (0,0,0) #black
    elif classes == 9:
        colour = (235,92,135) #pink
    elif classes == 10:
        colour = (91,5,145) #purple
    elif classes == 11:
        colour = (173,241,33) #lime
    elif classes == 12:
        colour = (137,73,80) #brown 
    else:
        print('We dont have a colour setup for that class')
    left_x = bbox[0]
    top_y = bbox[1]
    right_x = bbox[2]
    bottom_y = bbox[3]
    img = cv2.rectangle(image, (left_x,top_y), (right_x,bottom_y), colour, 2)
    return img

def iou_1(boxA, boxB):
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])
    # compute the area of intersection rectangle
    if xA < xB and yA < yB:
        I = (xB - xA) * (yB - yA)
    else:
        I = 0
    # compute the area of both the prediction and ground-truth
    # rectangles
    boxAArea = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    boxBArea = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])
    boxAArea = abs(boxAArea)
    boxBArea = abs(boxBArea)
    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    interArea = I
    if float(boxAArea + boxBArea - I) <= 0:
        iou = 0
    elif float(boxAArea + boxBArea - I) >= 1:
        iou = 1
    else:
        iou = interArea / float(boxAArea + boxBArea - I)
        iou = abs(iou)
    # return the intersection over union value
    return iou

def iou_2(boxG, boxP):
    boxA = (min(boxG[0], boxG[2]), min(boxG[1], boxG[3]), max(boxG[0], boxG[2]), max(boxG[1], boxG[3]))
    boxB = (min(boxP[0], boxP[2]), min(boxP[1], boxP[3]), max(boxP[0], boxP[2]), max(boxP[1], boxP[3]))
    Bg = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    Bp = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])
    if xA < xB and yA < yB:
        I = (xB - xA) * (yB - yA)
    else:
        I = 0
    U = Bg + Bp - I
    return I/U

def iou(bbox1, bbox2):
    return iou_1(bbox1, bbox2)


def iterate_over_images(list, path_to_images, save_directory, name):
    fill = open(list, 'r')
    for line in fill:
        lin = line.split(' ')
        image = lin[0]
        classes = str(lin[1])
        x1 = int(lin[2])
        y1 = int(lin[3])
        x2 = int(lin[4])
        y2 = int(lin[5])
        confidence = lin[6]
        if list == 'pd.txt':
            print('pd file')
            if classes == 0:
                classes == 4
            elif classes == 1:
                classes == 5
        elif list[0] == 'r':
            if classes == 0:
                classes == 4
            elif classes == 1:
                classes == 5

        bbox_coordinates = [x1, y1, x2, y2]  
        print(bbox_coordinates)
        img = add_bbox(path_to_images + image + '.jpg', bbox_coordinates, int(classes))
        cv2.imwrite(save_directory + image + '_' + name + '.jpg', img)

def reiterate_over_images(list, path_to_images, save_directory, name):
    fill = open(list, 'r')
    for line in fill:
        lin = line.split(' ')
        image = lin[0]
        classes = str(lin[1])
        x1 = int(lin[2])
        y1 = int(lin[3])
        x2 = int(lin[4])
        y2 = int(lin[5])
        confidence = lin[6]
        if list == 'pd.txt':
            print('pd file')
            if classes == 0:
                classes == 4
            elif classes == 1:
                classes == 5
        elif list[0] == 'r':
            if classes == 0:
                classes == 4
            elif classes == 1:
                classes == 5

        bbox_coordinates = [x1, y1, x2, y2]  
        print(bbox_coordinates)
        img = add_bbox(path_to_images + image + '_' + name + '.jpg', bbox_coordinates, int(classes))
        cv2.imwrite(save_directory + image + '_' + name + '.jpg', img)

# iterate_over_images('/home/as-hunt/results.txt', '/home/as-hunt/ni/', '/home/as-hunt/')
# iterate_over_images('/home/as-hunt/results.txt', '/home/as-hunt/', '/home/as-hunt/')


def get_prediction_mistakes(gt_file, pd_file, path_to_images, save_directory):
    gt = open(gt_file)
    pd = open(pd_file)
    for line in pd:
        li = line.split(' ')
        name = li[0]
        classes = li[1]
        bbox = [int(li[2]), int(li[3]), int(li[4]), int(li[5])]
        confidence = li[6]
        print(name)
        for lune in gt:
            lu = lune.split(' ')
            if lu[0] == name:
                print("Image match")
                nome = lu[0]
                clisses = lu[1]
                bbax = [int(lu[2]), int(lu[3]), int(lu[4]), int(lu[5])]
                canfidence = lu[6]
                if iou(bbox, bbax) >= 0.5:
                    print("overlap")
                    print(iou(bbox,bbax))
                    if classes == clisses:
                        print("Classes match! Success!")
                    else:
                        print("Classes do not match, detection error")
                        classes = 3
                        img = add_bbox(path_to_images + name+ '.jpg', bbox, int(classes))
                        cv2.imwrite(save_directory + name + '.jpg', img) 
                else:
                    print("no overlap")
                    if classes== 0:
                        classes = 4
                    elif classes == 1:
                        classes = 5
                    elif classes == 2:
                        classes = 6    
                    img = add_bbox(path_to_images + name+ '.jpg', bbox, int(classes))
                    cv2.imwrite(save_directory + name + '.jpg', img)
     
# get_prediction_mistakes('gt.txt', 'pd.txt', '/home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/valid/', '/home/as-hunt/workspace/')
# get_prediction_mistakes('gt.txt', 'pd.txt', '/home/as-hunt/workspace/', '/home/as-hunt/workspace/')

def get_prediction_mistakes_iterative(gt_file, pd_file, path_to_images, save_directory):
    gt = open(gt_file)
    gt_array = []
    pd = open(pd_file)
    pd_array = []
    matches = []
    for line in pd:
        li = line.split(' ')
        name = li[0]
        classes = li[1]
        bbox = [int(li[2]), int(li[3]), int(li[4]), int(li[5])]
        confidence = li[6]
        pd_array.append([name, bbox, classes, confidence])
    for lune in gt:
        lu = lune.split(' ')
        nome = lu[0]
        clisses = lu[1]
        bbax = [int(lu[2]), int(lu[3]), int(lu[4]), int(lu[5])]
        gt_array.append([nome, bbax, clisses])
    length = len(gt_array)    
    for item in pd_array:
        print(item[0])
        name = item[0]
        bbox = item[1]
        classes = item[2]
        confidence = item[3]
        for thing in gt_array:
            nome = thing[0]
            bbax = thing[1]
#             print(bbax)
            clisses = thing[2]
            if name in thing[0]:
                print("Found")
                place = gt_array.index(thing)
                print("Place is :" + str(place))
                if iou(bbox, bbax) >= 0.4:
                        print("overlap")
                        print(iou(bbox,bbax))
                        matches.append([name, bbox, classes])
                        if classes == clisses:
                            print("Classes match! Success!")
                            print("item removed")
                            print(gt_array[place])
                            gt_array.remove(thing)
                        else:
                            print("Classes do not match, detection error")
                            classes = 4
                            img = add_bbox(path_to_images + name+ '.jpg', bbox, int(classes))
                            cv2.imwrite(save_directory + name + '.jpg', img) 
                else:
                    print("no overlap")
                    if classes== 0:
                        classes = 5
                    elif classes == 1:
                        classes = 6
                    elif classes == 2:
                        classes = 7
                    elif classes == 3:
                        classes = 8
                    img = add_bbox(path_to_images + name+ '.jpg', bbox, int(classes))
                    cv2.imwrite(save_directory + name + '.jpg', img)
    print("length of gt array is " + str(len(gt_array)))
    print(length)                        
    for item in gt_array:
        if item[0] not in matches:
            print('No matches for '+ item[0])
            name = item[0]
            bbox = item[1]
            classes = item[2]
            if classes== 0:
                classes = 9
            elif classes == 1:
                classes = 10
            elif classes == 2:
                classes = 11
            elif classes == 3:
                classes = 12
            img = add_bbox(path_to_images + name+ '.jpg', bbox, int(classes))
            cv2.imwrite(save_directory + name + '.jpg', img)