import os
import re
import cv2
import decimal

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
    else:
        print('We dont have a colour setup for that class')
    left_x = bbox[0]
    top_y = bbox[1]
    right_x = bbox[2]
    bottom_y = bbox[3]
    img = cv2.rectangle(image, (left_x,top_y), (right_x,bottom_y), colour, 2)
    return img

def iou(boxA, boxB):
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    # compute the area of intersection rectangle
    interArea = (xB - xA) * (yB - yA)
    interArea = abs(interArea)
    # compute the area of both the prediction and ground-truth
    # rectangles
    boxAArea = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    boxBArea = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])
    boxAArea = abs(boxAArea)
    boxBArea = abs(boxBArea)
    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    if float(boxAArea + boxBArea - interArea) <= 0:
        iou = 0
    elif float(boxAArea + boxBArea - interArea) >= 1:
        iou = 1
    else:
        iou = interArea / float(boxAArea + boxBArea - interArea)
        iou = abs(iou)

    # return the intersection over union value
    return iou

def iterate_over_images(list, path_to_images, save_directory):
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
                classes == 2
            elif classes == 1:
                classes == 3
        bbox_coordinates = [x1, y1, x2, y2]  
        print(bbox_coordinates)
        img = add_bbox(path_to_images + image+ '.jpg', bbox_coordinates, int(classes))
        cv2.imwrite(save_directory + image + '.jpg', img)


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
                        classes = 2
                        img = add_bbox(path_to_images + name+ '.jpg', bbox, int(classes))
                        cv2.imwrite(save_directory + name + '.jpg', img) 
                else:
                    print("no overlap")
                    if classes== 0:
                        classes = 3
                    elif classes == 1:
                        classes = 4
                    img = add_bbox(path_to_images + name+ '.jpg', bbox, int(classes))
                    cv2.imwrite(save_directory + name + '.jpg', img)
     
# get_prediction_mistakes('gt.txt', 'pd.txt', '/home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/valid/', '/home/as-hunt/workspace/')
# get_prediction_mistakes('gt.txt', 'pd.txt', '/home/as-hunt/workspace/', '/home/as-hunt/workspace/')

def get_prediction_mistakes_iterative(gt_file, pd_file, path_to_images, save_directory):
    gt = open(gt_file)
    gt_array = []
    pd = open(pd_file)
    pd_array = []
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
#                 print("Place is :" + str(place))
                if iou(bbox, bbax) >= 0.4:
                        print("overlap")
                        print(iou(bbox,bbax))
                        if classes == clisses:
                            print("Classes match! Success!")
                            gt_array.pop(place)
                            print("item removed")
                        else:
                            print("Classes do not match, detection error")
                            classes = 2
                            img = add_bbox(path_to_images + name+ '.jpg', bbox, int(classes))
                            cv2.imwrite(save_directory + name + '.jpg', img) 
                else:
                    print("no overlap")
                    if classes== 0:
                        classes = 3
                    elif classes == 1:
                        classes = 4
                    img = add_bbox(path_to_images + name+ '.jpg', bbox, int(classes))
                    cv2.imwrite(save_directory + name + '.jpg', img)
    for item in gt_array:
        print(item)
        name = item[0]
        bbox = item[1]
        classes = item[2]
        if classes== 0:
            classes = 5
        elif classes == 1:
            classes = 6
        img = add_bbox(path_to_images + name+ '.jpg', bbox, int(classes))
        cv2.imwrite(save_directory + name + '.jpg', img)