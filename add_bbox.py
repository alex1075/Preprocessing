import os
import re
import gc
import random
import string
import cv2
import decimal
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns    
import pandas as pd
from matplotlib.colors import ListedColormap

gc.collect()
gc.set_threshold(0)

def add_bbox(image, bbox, classes):
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
    # print(classes)
    classes = int(classes)
    img = cv2.imread(image)
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
    # print(left_x, top_y, right_x, bottom_y)
    # print(colour)
    img = cv2.rectangle(img, (left_x,top_y), (right_x,bottom_y), colour, 2)
    # print(image)
    cv2.imwrite(image, img)
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
        print(float(boxAArea + boxBArea - I))
        iou = 1
    else:
        iou = interArea / float(boxAArea + boxBArea - I)
        iou = abs(iou)
    # return the intersection over union value
    return iou

def get_iou(bb1, bb2):
    """
    Calculate the Intersection over Union (IoU) of two bounding boxes.

    Parameters
    ----------
    bb1 : dict
        Keys: {'x1', 'x2', 'y1', 'y2'}
        The (x1, y1) position is at the top left corner,
        the (x2, y2) position is at the bottom right corner
    bb2 : dict
        Keys: {'x1', 'x2', 'y1', 'y2'}
        The (x, y) position is at the top left corner,
        the (x2, y2) position is at the bottom right corner

    Returns
    -------
    float
        in [0, 1]
    """
    # print(bb1)
    # print(bb2)
    assert bb1[0] <= bb1[2]

    assert bb1[1] <= bb1[3]
    assert bb2[0] <= bb2[2]
    assert bb2[1] <= bb2[3]


    # determine the coordinates of the intersection rectangle
    x_left = max(bb1[0], bb2[0])
    y_top = max(bb1[1], bb2[1])
    x_right = min(bb1[2], bb2[2])
    y_bottom = min(bb1[3], bb2[3])

    if x_right < x_left or y_bottom < y_top:
        return 0.0

    # The intersection of two axis-aligned bounding boxes is always an
    # axis-aligned bounding box.
    # NOTE: We MUST ALWAYS add +1 to calculate area when working in
    # screen coordinates, since 0,0 is the top left pixel, and w-1,h-1
    # is the bottom right pixel. If we DON'T add +1, the result is wrong.
    intersection_area = (x_right - x_left + 1) * (y_bottom - y_top + 1)

    # compute the area of both AABBs
    bb1_area = (bb1[2] - bb1[0] + 1) * (bb1[3] - bb1[1] + 1)
    bb2_area = (bb2[2] - bb2[0] + 1) * (bb2[3] - bb2[1] + 1)

    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = intersection_area / float(bb1_area + bb2_area - intersection_area)
    # print(iou)
    assert iou >= 0.0
    assert iou <= 1.0
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

def bb_intersection_over_union(boxA, boxB):
	# determine the (x, y)-coordinates of the intersection rectangle
	xA = max(boxA[0], boxB[0])
	yA = max(boxA[1], boxB[1])
	xB = min(boxA[2], boxB[2])
	yB = min(boxA[3], boxB[3])
	# compute the area of intersection rectangle
	interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
	# compute the area of both the prediction and ground-truth
	# rectangles
	boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
	boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
	# compute the intersection over union by taking the intersection
	# area and dividing it by the sum of prediction + ground-truth
	# areas - the interesection area
	iou = interArea / float(boxAArea + boxBArea - interArea)
	# return the intersection over union value
	return iou

def iou(bbox1, bbox2):
    return get_iou(bbox1, bbox2)


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
        print(path_to_images + image + '.jpg')
        img = add_bbox(path_to_images + image + '_' + name + '.jpg', bbox_coordinates, int(classes))
        cv2.imwrite(save_directory + image + '_' + name + '.jpg', img)

iterate_over_images('/home/as-hunt/Etra-Space/Mono/4/gt.txt', '/home/as-hunt/Etra-Space/Mono/4/test/', '/home/as-hunt/leuko-out/', 'labelled')
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
     
# get_prediction_mistakes('/home/as-hunt/Etra-Space/Diffy-10k/1/gt.txt', '/home/as-hunt/Etra-Space/Diffy-10k/1/results.txt', '/home/as-hunt/Etra-Space/Diffy-10k/1/test/', '/home/as-hunt/workspace/')
# get_prediction_mistakes('/home/as-hunt/Etra-Space/Diffy-10k/1/gt.txt', '/home/as-hunt/Etra-Space/Diffy-10k/1/results.txt', '/home/as-hunt/workspace/', '/home/as-hunt/workspace/')
# get_prediction_mistakes('/home/as-hunt/Etra-Space/Diffy-10k/1/gt.txt', '/home/as-hunt/Etra-Space/Diffy-10k/1/results.txt', '/home/as-hunt/workspace/', '/home/as-hunt/workspace/')
# get_prediction_mistakes('/home/as-hunt/Etra-Space/Diffy-10k/1/gt.txt', '/home/as-hunt/Etra-Space/Diffy-10k/1/results.txt', '/home/as-hunt/workspace/', '/home/as-hunt/workspace/')
# get_prediction_mistakes('/home/as-hunt/Etra-Space/Diffy-10k/1/gt.txt', '/home/as-hunt/Etra-Space/Diffy-10k/1/results.txt', '/home/as-hunt/workspace/', '/home/as-hunt/workspace/')
# get_prediction_mistakes('/home/as-hunt/Etra-Space/Diffy-10k/1/gt.txt', '/home/as-hunt/Etra-Space/Diffy-10k/1/results.txt', '/home/as-hunt/workspace/', '/home/as-hunt/workspace/')

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

# get_prediction_mistakes_iterative('/home/as-hunt/Etra-Space/Diffy-10k/1/gt.txt', '/home/as-hunt/Etra-Space/Diffy-10k/1/results.txt', '/home/as-hunt/Etra-Space/Diffy-10k/1/test/', '/home/as-hunt/workspace/')


def normalize(df):
    result = df.copy()
    for feature_name in df.columns:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result

def plot_bbox_area(gt_file, pd_file, save_name='areas.png'):
    names = []
    values = []
    gtchaart = []
    pdchaart = []
    areas = []
    gt_array = []
    pd_array = []
    dfp = []
    classesp = []
    classesg = []
    combined = []
    tagp = []
    tagg = []
    ious = []
    dfg = []
    listed = open(pd_file, 'r')
    losted = open(gt_file, 'r')
    for line in listed:
        li = line.split(' ')
        name = li[0]
        classes = li[1]
        bbox = [int(li[2]), int(li[3]), int(li[4]), int(li[5])]
        confidence = li[6]
        pd_array.append([name, bbox, classes, confidence])
    for lune in losted:
        lu = lune.split(' ')
        nome = lu[0]
        clisses = lu[1]
        bbax = [int(lu[2]), int(lu[3]), int(lu[4]), int(lu[5])]
        gt_array.append([nome, bbax, clisses])
    for item in pd_array:
        name = item[0]
        bbox = item[1]
        classes = item[2]
        confidence = item[3]
        for thing in gt_array:
            nome = thing[0]
            bbax = thing[1]
            clisses = thing[2]
            if name in thing[0]:
                place = gt_array.index(thing)
                # print(iou(bbox, bbax))
                if iou(bbax, bbox) >= 0.5:
                    pdchaart.append([classes, (abs(int(bbox[2]) - int(bbox[0])) * abs(int(bbox[3]) - int(bbox[1])))])
                    gtchaart.append([clisses, (abs(int(bbax[2]) - int(bbax[0])) * abs(int(bbax[3]) - int(bbax[1])))])
                    classesp.append(classes)
                    classesg.append(clisses)    
                    # combined.append([(abs(int(bbox[2]) - int(bbox[0])) * abs(int(bbox[3]) - int(bbox[1]))), (abs(int(bbax[2]) - int(bbax[0])) * abs(int(bbax[3]) - int(bbax[1])))])     
                    dfp.append(float(abs(int(bbox[2]) - int(bbox[0])) * abs(int(bbox[3]) - int(bbox[1]))))
                    dfg.append(float(abs(int(bbax[2]) - int(bbax[0])) * abs(int(bbax[3]) - int(bbax[1]))))
                    tagp.append('PD')
                    tagg.append('GT')
                    if classes == clisses:
                        match = True
                        combined.append([(abs(int(bbax[2]) - int(bbax[0])) * abs(int(bbax[3]) - int(bbax[1]))), (abs(int(bbox[2]) - int(bbox[0])) * abs(int(bbox[3]) - int(bbox[1]))), float(classes), float(clisses), match, float(iou(bbax, bbox))])
                    else:   
                        match = False
                        combined.append([(abs(int(bbax[2]) - int(bbax[0])) * abs(int(bbax[3]) - int(bbax[1]))), (abs(int(bbox[2]) - int(bbox[0])) * abs(int(bbox[3]) - int(bbox[1]))), float(classes), float(clisses), match, float(iou(bbax, bbox))])
                    gt_array.pop(place)
    for item in areas:   
        names.append(item[0]) 
        values.append(item[1])
    fig, axs = plt.subplots(1, figsize=(9, 3), sharey=True)
    cl0 = []
    cl1 = []
    cl2 = []
    cl3 = []
    cl4 = []
    cl5 = []
    gcl0 = []
    gcl1 = []
    gcl2 = []
    gcl3 = []
    gcl4 = []
    gcl5 = []
    for item in pdchaart:
        # print(item)
        if item[0] == '0':
            cl0.append(item[1])
        elif item[0] == '1':
            cl1.append(item[1])
        elif item[0] == '2':
            cl2.append(item[1])
        elif item[0] == '3':
            cl3.append(item[1])
        elif item[0] == '4':  
            cl4.append(item[1])
        elif item[0] == '5':
            cl5.append(item[1])          
    for item in gtchaart:
        # print(item)
        if item[0] == '0':
            gcl0.append(item[1])
        elif item[0] == '1':
            gcl1.append(item[1])
        elif item[0] == '2':
            gcl2.append(item[1])
        elif item[0] == '3':
            gcl3.append(item[1])
        elif item[0] == '4':  
            gcl4.append(item[1])
        elif item[0] == '5':
            gcl5.append(item[1])    
    fig, axs = plt.subplots(2, 2)        
    # fig.tight_layout()
    # fig = plt.gcf()
    fig.set_size_inches(16, 10)
    # fig.add_gridspec(2, 3)

    fig.savefig('test2png.png', dpi=100)
    
    df = pd.DataFrame({'Class':classesp, 'Area':dfp, 'Dataset':tagp}, columns=["Class", "Area", "Dataset"])
    for i in range(len(classesg)):
        new_row = {'Class': classesg[i], 'Area': dfg[i], 'Dataset': tagg[i]}
        df = df._append(new_row, ignore_index=True)
    # print(df)
    sns.violinplot(data=df, cut=0, x='Class', y='Area', inner='box', scale='count', hue="Dataset", split=True, ax=axs[0, 0])
    # axs[0,0].set_xticklabels(["Echinocyte", "Erythrocyte", "Lymphocyte", "Monocyte", "Neutrophil", "Platelet"])
    axs[0, 0].set_title('Bbox Area Plotting per Class')

    # plt.savefig(save_name+'_2.png', bbox_inches='tight')
    # plt.clf()
    du = pd.DataFrame(combined, columns=["x", "y", 'PD_class', 'GT_class', 'Match', 'IoU'])
    sns.scatterplot(data=du, x="x", y="y", ax=axs[1, 0], hue='Match', palette=["Red", "Blue",])
    axs[1, 0].set_title('Ground Truth Bbox by Predicted Bbox Areas coloured by Match of Classes')
    axs[1, 0].set(xlabel='Ground Truth Areas (pixels)', ylabel='Predicted Areas (pixels)')
    sns.scatterplot(data=du, x="x", y="y", ax=axs[0,1], hue='PD_class', palette=["Red", "Blue", "Green", "Purple", "Yellow", "Cyan"])
    axs[0, 1].set_title('Ground Truth Bbox by Predicted Bbox Areas coloured by Prediction Classes')
    axs[0, 1].set(xlabel='Ground Truth Areas (pixels)', ylabel='Predicted Areas (pixels)')
    sns.scatterplot(data=du, x="x", y="y", ax=axs[1, 1], hue='GT_class', palette=["Red", "Blue", "Green", "Purple", "Yellow", "Cyan"])
    axs[1, 1].set_title('Ground Truth Bbox by Predicted Bbox Areas coloured by Ground Truth Classes')
    axs[1, 1].set(xlabel='Ground Truth Areas (pixels)', ylabel='Predicted Areas (pixels)')
    plt.savefig(save_name+'_details.png', bbox_inches='tight')
    # plt.clf()
    # print(du)
    # du.to_csv(save_name+'_2.csv')
    plt.clf()
    x = du['x']
    y = du['y']
    z = du['IoU']
    w = du['PD_class']
    plt.rcParams["figure.figsize"] = [16, 10]
    plt.rcParams["figure.autolayout"] = True
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    cmap = ListedColormap(sns.color_palette("husl", 256).as_hex())
    sc = ax.scatter(x, y, z, c=w ,cmap='viridis')
    plt.legend(*sc.legend_elements(), bbox_to_anchor=(1.05, 1), loc=2)
    ax.view_init(40, 60)
    print(du)
    plt.savefig(save_name+'_33.png', bbox_inches='tight')
  
def bbox_area(bbox):
    return abs(int(bbox[2]) - int(bbox[0])) * abs(int(bbox[3]) - int(bbox[1]))
  
def export_errors(gt_file, pd_file, path1, path2, save_name='Error_'):
    gt_array = []
    pd_array = []
    listed = open(pd_file, 'r')
    losted = open(gt_file, 'r')
    for line in listed:
        li = line.split(' ')
        name = li[0]
        classes = li[1]
        bbox = [int(li[2]), int(li[3]), int(li[4]), int(li[5])]
        confidence = li[6]
        pd_array.append([name, bbox, classes, confidence])
    for lune in losted:
        lu = lune.split(' ')
        nome = lu[0]
        clisses = lu[1]
        bbax = [int(lu[2]), int(lu[3]), int(lu[4]), int(lu[5])]
        gt_array.append([nome, bbax, clisses])



    for item in pd_array:
        name = item[0]
        bbox = item[1]
        classes = item[2]
        confidence = item[3]
        for thing in gt_array:
            nome = thing[0]
            bbax = thing[1]
            clisses = thing[2]
            if name in thing[0]:
                place = gt_array.index(thing)
                # print(iou(bbox, bbax))
                if iou(bbax, bbox) >= 0.5:
                    if classes == clisses:
                       print("Classes match! Success!")
                    #    pass
                       print(name)
                       path = path1
                       print(path)
                       # Add function to add bbox on image
                       save_name = path + 'Match_' + name + '.png'
                       print(save_name)
                       gt_image = path2 + name + '.jpg'
                       pd_image = path2 + nome + '.jpg'
                       print(classes)
                       print(clisses)
                       print(gt_image, bbax, clisses)
                       labelled_gt_image = add_bbox(gt_image, bbax, clisses)
                       labelled_pd_image = add_bbox(pd_image, bbox, classes)
                       fig, axs = plt.subplots(1, 2)
                       axs[0].imshow(labelled_gt_image)
                       axs[0].set_title('Ground Truth')
                       axs[1].imshow(labelled_pd_image)
                       axs[1].set_title('Prediction')
                       plt.figtext(0.20, 0.15, 'Red - Lymphocyte, Green - Monocyte Blue - Neutrophil')
                       plt.savefig(save_name , bbox_inches='tight')
                    else:   
                        print(name)
                        path = path1
                        print(path)
                        # Add function to add bbox on image
                        save_name = path + 'Error_' + name + '.png'
                        print(save_name)
                        gt_image = path2 + name + '.jpg'
                        pd_image = path2 + nome + '.jpg'
                        print(classes)
                        print(clisses)
                        print(gt_image, bbax, clisses)
                        labelled_gt_image = add_bbox(gt_image, bbax, clisses)
                        labelled_pd_image = add_bbox(pd_image, bbox, classes)
                        fig, axs = plt.subplots(1, 2)
                        axs[0].imshow(labelled_gt_image)
                        axs[0].set_title('Ground Truth')
                        axs[1].imshow(labelled_pd_image)
                        axs[1].set_title('Prediction')
                        # plt.figtext(0.20, 0.15, 'Red - Lymphocyte, Green - Monocyte Blue - Neutrophil')
                        plt.savefig(save_name , bbox_inches='tight')

                    gt_array.pop(place) 

# export_errors('/home/as-hunt/Etra-Space/Diffy-10k/1/gt.txt', '/home/as-hunt/Etra-Space/Diffy-10k/1/results.txt', '/home/as-hunt/Etra-Space/Diffy-10k/1/test/', '/home/as-hunt/Etra-Space/Diffy-10k/1/test/')



def export_errors_neo(gt_file, pd_file, path1, path2):
    from collections import defaultdict
    import tqdm

    gt_dict = defaultdict(list)
    pd_dict = defaultdict(list)

    with open(pd_file, 'r') as listed:
        for line in listed:
            li = line.split(' ')
            name = li[0]
            classes = li[1]
            bbox = [int(li[2]), int(li[3]), int(li[4]), int(li[5])]
            confidence = li[6]
            pd_dict[name].append([bbox, classes, confidence])

    for name, pd_entries in tqdm.tqdm(pd_dict.items()):
        # check for duplicate bbox per image using iou and remove the one with the biggest area
        pd_entries = sorted(pd_entries, key=lambda x: x[2], reverse=True)
        pd_dict[name] = pd_entries
        # print(pd_entries[0])
        for i in range(len(pd_entries)):
            for j in range(i+1, len(pd_entries)):
                try:
                    if iou(pd_entries[i][0], pd_entries[j][0]) >= 0.5:
                        if bbox_area(pd_entries[i][0]) > bbox_area(pd_entries[j][0]):
                            pd_entries.pop(j)
                            print('pop')
                        else:
                            pd_entries.pop(i)
                            print('pop')
                except:
                    pass

    with open(gt_file, 'r') as losted:
        for line in losted:
            li = line.split(' ')
            name = li[0]
            classes = li[1]
            bbox = [int(li[2]), int(li[3]), int(li[4]), int(li[5])]
            gt_dict[name].append([bbox, classes])

    # check for identical ground truth bbox per image and remove duplicates
    for name, gt_entries in tqdm.tqdm(gt_dict.items()):
        gt_entries = sorted(gt_entries, key=lambda x: x[1], reverse=True)
        gt_dict[name] = gt_entries
        for i in range(len(gt_entries)):
            for j in range(i+1, len(gt_entries)):
                try:    
                    if iou(gt_entries[i][0], gt_entries[j][0]) >= 0.5:
                        if bbox_area(gt_entries[i][0]) > bbox_area(gt_entries[j][0]):
                            gt_entries.pop(j)
                            print('pop')
                        else:
                            gt_entries.pop(i) 
                            print('pop')
                except:
                    pass

    for name, pd_entries in tqdm.tqdm(pd_dict.items()):
        match = False
        annots = 0
        gt_entries = gt_dict.get(name, [])
        for pd_entry in pd_entries:
            pd_bbox, pd_classes, confidence = pd_entry
            for gt_entry in gt_entries:
                gt_bbox, gt_classes = gt_entry
                if iou(gt_bbox, pd_bbox) >= 0.5:
                    if pd_classes == gt_classes:
                        # print("Classes match! Success!")
                        match = True
                        # print(name)
                        labelled_gt_image = add_bbox(path1 + name + '.jpg', gt_bbox, gt_classes)
                        labelled_pd_image = add_bbox(path1 + name + '.jpg', pd_bbox, pd_classes)
                        annots += 1
                    else:
                        # print("Classes do not match, detection error")
                        match = False
                        # print(name)
                        labelled_gt_image = add_bbox(path1 + name + '.jpg', gt_bbox, gt_classes)
                        labelled_pd_image = add_bbox(path1 + name + '.jpg', pd_bbox, pd_classes)
                        annots += 1
        fig, axs = plt.subplots(1, 2)
        axs[0].imshow(labelled_gt_image)
        axs[0].set_title('Ground Truth')
        axs[1].imshow(labelled_pd_image)
        axs[1].set_title('Prediction')
        # print('Annotations: ', annots)
        if match == False:
              save_name = path2 + 'Error_' + name + '.png'  
              plt.savefig(save_name , bbox_inches='tight')   
              # clear figure
              plt.close()    
        else:
              save_name = path2 + 'Match_' + name + '.png'
              plt.savefig(save_name , bbox_inches='tight')
              plt.close()
        

# export_errors_neo('/home/as-hunt/Etra-Space/Diffy-10k/1/gt.txt', '/home/as-hunt/Etra-Space/Diffy-10k/1/results.txt', '/home/as-hunt/Etra-Space/Diffy-10k/1/test/', '/home/as-hunt/workspace/')


# write a function that plots the predicted bounding boxes on a plot (width x height) coloured by class

def plot_bboxes_dimentions(pd_file, obj_names, save_name='prediction.png'):
    from dimentions import pixel_size, margin_error_um
    target_names = ['Echinocyte', 'Erythrocyte', 'Lymphocyte', 'Neutrophil', 'Monocyte', 'Platelet']
    values = [] 
    pd_array = []
    with open(pd_file, 'r') as liste:
        for line in liste:
            li = line.split(' ')
            name = li[0]
            classes = li[1]
            bbox = [int(li[2]), int(li[3]), int(li[4]), int(li[5])]
            confidence = li[6]
            pd_array.append([name, bbox, classes, confidence])
    # check for duplicate bbox per image using iou and remove the one with the highest confidence
    print('1')
    # for item in pd_array:
    #     name = item[0]
    #     bbox = item[1]
    #     classes = item[2]
    #     confidence = item[3]
    #     for thing in pd_array:
    #         nome = thing[0]
    #         bbax = thing[1]
    #         clisses = thing[2]
    #         if name in thing[0]:
    #             place = pd_array.index(thing)
    #             if iou(bbax, bbox) >= 0.5:
    #                 if confidence > thing[3]:
    #                     pd_array.pop(place)
    #                 else:
    #                     try:
    #                         pd_array.pop(pd_array.index(item))
    #                     except:
    #                         pass    
    # work out the width and heigh of each predicted object 
    print('2')
    for item in pd_array:
        # print(item)
        name = item[0]
        bbox = item[1]
        classes = target_names[int(item[2])]
        confidence = item[3]
        width = abs(int(bbox[2]) - int(bbox[0]))
        height = abs(int(bbox[3]) - int(bbox[1]))
        width = abs(float((width * pixel_size) - (margin_error_um / 2)))
        height = abs(float((height * pixel_size) - (margin_error_um / 2)))
        if width <= 0.8:
            pass
        else:
            if height <= 0.9:
                pass
            else:
                values.append([width, height, classes])
    #plot the width and height of each predicted object
    print('3')
    import seaborn as sns
    import pandas as pd
    df = pd.DataFrame(values, columns=["Width", "Height", "Class"])
    plt.figsize=(53, 30)
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x="Width", y="Height", hue="Class", s=2)
    ax.set_title('Predicted Cell Width and Height')
    ax.set_xlabel('Width (µm)')
    ax.set_ylabel('Height (µm)')
    plt.legend(title='Cell Type', fontsize='small', title_fontsize='small', markerscale=4, loc='lower right')
    resolution_value = 1200
    plt.savefig(save_name, bbox_inches='tight', dpi=resolution_value)
    plt.close()

plot_bboxes_dimentions('/home/as-hunt/Etra-Space/Diffy-10k/1/results.txt', '/home/as-hunt/Etra-Space/Diffy-10k/1/obj.names', 'areas.tiff')    

def convertRGB_toCYMK(image_in):
    from PIL import Image
    Image.open(image_in).convert('CMYK').save(image_in)


convertRGB_toCYMK('areas.tiff')    