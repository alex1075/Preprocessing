import os
import numpy as np
import pybboxes as pbx
import decimal
from shapely.geometry import Polygon
import warnings
warnings.filterwarnings("ignore")
from sklearn.metrics import confusion_matrix


def confusion_matrix(pred_output, gt, n_labels):
    lbl_count = n_labels * gt + pred_output
    # print(lbl_count)
    count = np.bincount(lbl_count, minlength=n_labels ** 2)
    conf_matrix = count.reshape(np.flatten(n_labels, n_labels))
    return conf_matrix


def get_coordonates_from_gt_txt_as_voc(file, path): 
    yolo_gt = []
    filoo = open(path + file, 'r')
    for line in filoo:
        # print(file)
        # print(line)
        lin = line.split(' ')
        # print(lin)
        image = lin[0]
        classes = lin[1]
        cent_x = float(lin[2])
        cent_y = float(lin[3])
        width = float(lin[4])
        height = float(lin[5][:-2])
        bbox = (cent_x, cent_y, width, height)
        # print(bbox)
        yolo = pbx.convert_bbox(bbox, from_type="yolo", to_type="voc", image_size=(416, 416))
        x1, y1, x2, y2 = yolo
        # print(x1, y1, x2, y2)
        yolo_gt.append([image, classes, x1, y1, x2, y2])

    # print (yolo_gt)
    return yolo_gt

def get_coordonates_from_pt_txt_as_voc(file, path): 
    yolo_pt = []
    filoo = open(path + file, 'r')
    for line in filoo:
        # print(file)
        # print(line)
        lin = line.split(' ')
        # print(lin)
        image = lin[0]
        classes = lin[1]
        cent_x = float(lin[2])
        cent_y = float(lin[3])
        width = float(lin[4])
        height = float(lin[5][:-2])
        bbox = (cent_x, cent_y, width, height)
        # print(bbox)
        yolo = ()
        try:
            yolo = pbx.convert_bbox(bbox, from_type="yolo", to_type="voc", image_size=(416, 416), strict=False)
            x1, y1, x2, y2 = yolo
            if x1 < 0 or y1 < 0 or x2 > 416 or y2 > 416:
                # print('Error: bbox out of range')
                continue
            # print(x1, y1, x2, y2)
            yolo_pt.append([image, classes, x1, y1, x2, y2])
        except ValueError:
            # print("ValueError, box is not in the image. Passed")
            pass
    return yolo_pt

n_labels = 5 # we have 4 labels from 0 to 3
# gt = np.loadtxt('ground_truth.txt', delimiter=' ', usecols=[2, 3])
# pred_output = np.loadtxt('predicitons.txt', delimiter=' ', usecols=[2, 3])
gt = get_coordonates_from_gt_txt_as_voc('ground_truth.txt', './')
# print(gt)
pred_output = get_coordonates_from_pt_txt_as_voc('predictons.txt', './')
# print(pred_output)
print(len(gt))
print(len(pred_output))
# confusion_matrix(pred_output, gt, n_labels)
# print(confusion_matrix(pred_output, gt, n_labels))
# print(gt)


# def remove_unmatched_bboxes(gt, pred_output):
#     for item in gt:
#         if all(flag == item for (flag, _, _, _, _, _) in pred_output) is True:
#             pass
#         else:
#             print(item)
#             gt.remove(item)

        
# remove_unmatched_bboxes(gt, pred_output)
# print(len(gt))
# print(len(pred_output))


# check if two bounding boxes overlap (i.e. if they have any common area)
def overlap(rect1,rect2):
    p1 = Polygon([(rect1[0],rect1[1]), (rect1[1],rect1[1]),(rect1[2],rect1[3]),(rect1[2],rect1[1])])
    p2 = Polygon([(rect2[0],rect2[1]), (rect2[1],rect2[1]),(rect2[2],rect2[3]),(rect2[2],rect2[1])])
    # print(p1.intersects(p2))
    try:
        return(p1.intersects(p2))
    except:
        # print(p1)
        # print(p2)
        return False

def overlap_area(rect1,rect2):
    p1 = Polygon([(rect1[0],rect1[1]), (rect1[1],rect1[1]),(rect1[2],rect1[3]),(rect1[2],rect1[1])])
    p2 = Polygon([(rect2[0],rect2[1]), (rect2[1],rect2[1]),(rect2[2],rect2[3]),(rect2[2],rect2[1])])
    # print(p1.intersects(p2))
    try:
        # print(p1.intersection(p2).area)
        return(p1.intersection(p2).area)
    except:
        # print(p1)
        # print(p2)
        return 0


def keep_only_overlapping_bboxes(gt, pred_output):
    for entry in gt: 
        for entry2 in pred_output:
            if entry[0] == entry2[0]:
                if overlap((entry[2], entry[3], entry[4], entry[5]), (entry2[2], entry2[3], entry2[4], entry2[5])) is False:
                    # print('Error: bboxs are not overlapping')
                    # print(entry)
                    # print(entry2)
                    pred_output.remove(entry2)
                else:
                    # print('Bboxs are overlapping')
                    # print(entry)
                    # print(entry2)
                    pass
    #

keep_only_overlapping_bboxes(gt, pred_output)
print(len(gt))
print(len(pred_output))
# f = open('ground_truth.csv', 'w')
# for item in gt:
#     f.write("%s,%s,%s,%s,%s,%s\n" % (item[0], item[1], item[2], item[3], item[4], item[5]))
# f.close()
# f = open('predictions.csv', 'w')
# for item in pred_output:
#     f.write("%s,%s,%s,%s,%s,%s\n" % (item[0], item[1], item[2], item[3], item[4], item[5]))
# f.close()

def remove_umnatched_gt(gt, pred_output):
     for entry in pred_output:
        for entry2 in gt:
            if entry[0] == entry2[0]:
                if overlap((entry[2], entry[3], entry[4], entry[5]), (entry2[2], entry2[3], entry2[4], entry2[5])) is False:
                    # print('Error: bboxs are not overlapping')
                    # print(entry)
                    # print(entry2)
                    gt.remove(entry2)
                else:
                    # print('Bboxs are overlapping')
                    # print(entry)
                    # print(entry2)
                    pass

remove_umnatched_gt(gt, pred_output)
print(len(gt))
print(len(pred_output))

# test which bboxs are overlapping the most and keep them from teh two lists
def keep_best_overlapping_bboxes(gt, pred_output):
    for entry in gt: 
        box_area_1 = 0
        entry2_minus_1 = 0
        for entry2 in pred_output:
            box_area_2 = 0
            if entry[0] == entry2[0]:
                if overlap((entry[2], entry[3], entry[4], entry[5]), (entry2[2], entry2[3], entry2[4], entry2[5])) is False:
                    pass        
                else:
                    overlap_area((entry[2], entry[3], entry[4], entry[5]), (entry2[2], entry2[3], entry2[4], entry2[5]))
                    box_area_1 = overlap_area((entry[2], entry[3], entry[4], entry[5]), (entry2[2], entry2[3], entry2[4], entry2[5]))
                    if box_area_1 > box_area_2:
                        try:
                            pred_output.remove(entry2_minus_1)
                        except:
                            pass
                        entry2 = entry2_minus_1
                        box_area_2 = box_area_1
                    elif box_area_1 == box_area_2:
                        if entry[1] == entry2[1]:
                            try:
                                pred_output.remove(entry2_minus_1)
                            except:
                                pass
                            entry2 = entry2_minus_1
                            box_area_2 = box_area_1
                        else:
                            pred_output.remove(entry2)
                    elif box_area_1 < box_area_2:
                        pred_output.remove(entry2)


keep_best_overlapping_bboxes(gt, pred_output)

print(len(gt))
print(len(pred_output))


# def remove_unmatched_bboxes(gt, pred_output):
#     for item in pred_output:
#         if all(item[0] in gt) is True:
#             pass
#         else:
#             print(item)
#             pred_output.remove(item)

        
# remove_unmatched_bboxes(gt, pred_output)
print(len(gt))
print(len(pred_output))
