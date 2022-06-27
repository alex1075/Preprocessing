import os
import numpy as np
from pybboxes import BoundingBox
import decimal

def confusion_matrix(pred_output, gt, n_labels):
    lbl_count = n_labels * gt + pred_output
    # print(lbl_count)
    count = np.bincount(lbl_count, minlength=n_labels ** 2)
    conf_matrix = count.reshape(np.flatten(n_labels, n_labels))
    return conf_matrix


def get_coordonates_from_gt_txt(file, path): 
    yolo_gt = []
    filoo = open(path + file, 'r')
    for line in filoo:
        # print(file)
        # print(line)
        lin = line.split(' ')
        # print(lin)
        image = lin[0]
        confidence = str(lin[1])
        x1 = round(decimal.Decimal(lin[2]), 6)
        y1 = round(decimal.Decimal(lin[3]), 6)
        x2 = round(decimal.Decimal(lin[4]), 6)
        y2 = round(decimal.Decimal(lin[5]), 6)
        # yolo_gt.append([str(x1), str(y1), str(x2), str(y2)])
        yolo_gt.append([confidence, str(x1)])
    # print (yolo_gt)
    return yolo_gt

def get_coordonates_from_pt_txt(file, path): 
    yolo_pt = []
    filoo = open(path + file, 'r')
    for line in filoo:
        # print(file)
        # print(line)
        lin = line.split(' ')
        # print(lin)
        image = lin[0]
        confidence = str(lin[1])
        x1 = round(decimal.Decimal(lin[2]), 6)
        y1 = round(decimal.Decimal(lin[3]), 6)
        x2 = round(decimal.Decimal(lin[4]), 6)
        y2 = round(decimal.Decimal(lin[5]), 6)
        # yolo_pt.append([str(x1), str(y1), str(x2), str(y2)])
        yolo_pt.append([confidence, str(x1)])
    return yolo_pt

n_labels = 5 # we have 4 labels from 0 to 3
# gt = np.loadtxt('ground_truth.txt', delimiter=' ', usecols=[2, 3])
# pred_output = np.loadtxt('predicitons.txt', delimiter=' ', usecols=[2, 3])
gt = get_coordonates_from_gt_txt('ground_truth.txt', './')
pred_output = get_coordonates_from_pt_txt('predicitons.txt', './')
confusion_matrix(pred_output, gt, n_labels)
print(confusion_matrix(pred_output, gt, n_labels))
# print(gt)