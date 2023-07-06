# make confusion matrix from ground_truth.txt and prediction.txt
import warnings
warnings.filterwarnings('ignore')
import os
import re
import cv2
import numpy as np
import decimal
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import fbeta_score
from add_bbox import *

def import_and_filter_results(input_file='/home/as-hunt/result.txt', results_file='results.txt'):
    res = open(results_file, 'w')
    with open(input_file, 'r') as f:
        for line in f:
            if line[0:4] == '/hom':
                lin = re.split('/| ', line)
                li = filter(lambda a: '.jpg' in a, lin)
                l = list(li)[0][:-5]
                # print(l)
                image_name = l
            elif line[0:4] == 'ERY:':
                print('ERY')
                lin = re.split(':|%|t|w|h', line)
                if int(lin[4]) < 4:
                    # pass
                    print(image_name + 'Error ERY: left_x (' + str(lin[4]) + ') is less than 6')
                elif int(lin[4]) > 412:
                    print(image_name + 'Error ERY: left_x (' + str(lin[4]) + ') is greater than 410')
                else:
                    if int(lin[6]) < 4:
                        print(image_name + 'Error ERY: top_y (' + str(lin[6]) + ') is less than 6')
                    elif int(lin[6]) > 412:
                        print(image_name + 'Error ERY: top_y (' + str(lin[6]) + ') is greater than 410')
                    else:
                        # print(lin)
                        classes = 0
                        confidence = int((lin[1]))
                        if int(lin[4]) < 0:
                            left_x = 0
                        else:
                            left_x = int(lin[4])
                        if int(lin[6]) < 0:
                            top_y = 0
                        else:
                            top_y = int(lin[6])
                        width = int(lin[10])
                        height = int(lin[14][:-2])
                        bottom_y = top_y + height
                        right_x = left_x + width
                        if bottom_y < 0:
                            bottom_y = 0
                        if right_x > 416:
                            right_x = 416
                        if bottom_y < 4:
                            print(image_name + 'Error ERY: bottom_y (' + str(bottom_y) + ') is less than 6')
                        elif bottom_y > 412:
                            print(image_name + 'Error ERY: bottom_y (' + str(bottom_y) + ') is greater than 410')
                        else:
                            if right_x > 412:
                                print(image_name + 'Error ERY: right_x (' + str(right_x) + ') is greater than 410')
                            elif right_x < 4:
                                print(image_name + 'Error ERY: right_x (' + str(right_x) + ') is less than 6')
                            else:
                                print(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100))
                                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100) + ' \n')
            elif line[0:4] == 'PLT:':
                print('PLT')
                lin = re.split(':|%|t|w|h', line)
                if int(lin[4]) < 4:
                    # pass
                    print(image_name + 'Error PLT: left_x (' + str(lin[4]) + ') is less than 6')
                elif int(lin[4]) > 412:
                    print(image_name + 'Error PLT: left_x (' + str(lin[4]) + ') is greater than 410')
                else:
                    if int(lin[6]) < 4:
                        print(image_name + 'Error PLT: top_y (' + str(lin[6]) + ') is less than 6')
                    elif int(lin[6]) > 412:
                        print(image_name + 'Error PLT: top_y (' + str(lin[6]) + ') is greater than 410')
                    else:
                        # print(lin)
                        classes = 1
                        confidence = int((lin[1]))
                        if int(lin[4]) < 0:
                            left_x = 0
                        else:
                            left_x = int(lin[4])
                        if int(lin[6]) < 0:
                            top_y = 0
                        else:
                            top_y = int(lin[6])
                        width = int(lin[10])
                        height = int(lin[14][:-2])
                        bottom_y = top_y + height
                        right_x = left_x + width
                        if bottom_y < 0:
                            bottom_y = 0
                        if right_x > 416:
                            right_x = 416
                        if bottom_y < 4:
                            print(image_name + 'Error PLT: bottom_y (' + str(bottom_y) + ') is less than 6')
                        elif bottom_y > 412:
                            print(image_name + 'Error PLT: bottom_y (' + str(bottom_y) + ') is greater than 410')
                        else:
                            if right_x > 412:
                                print(image_name + 'Error PLT: right_x (' + str(right_x) + ') is greater than 410')
                            elif right_x < 4:
                                print(image_name + 'Error PLT: right_x (' + str(right_x) + ') is less than 0')
                            else:
                                print(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100))
                                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100) + ' \n')                    
            elif line[0:4] == 'SIDE':
                print('SIDE')
                lin = re.split(':|%|t|w|h', line)
                if int(lin[4]) < 4:
                    # pass
                    print(image_name + 'Error SIDE: left_x (' + str(lin[4]) + ') is less than 6')
                elif int(lin[4]) > 412:
                    print(image_name + 'Error SIDE: left_x (' + str(lin[4]) + ') is greater than 410')
                else:
                    if int(lin[6]) < 4:
                        print(image_name + 'Error SIDE: top_y (' + str(lin[6]) + ') is less than 6')
                    elif int(lin[6]) > 412:
                        print(image_name + 'Error SIDE: top_y (' + str(lin[6]) + ') is greater than 410')
                    else:
                        # print(lin)
                        classes = 2
                        confidence = int((lin[1]))
                        if int(lin[4]) < 0:
                            left_x = 0
                        else:
                            left_x = int(lin[4])
                        if int(lin[6]) < 0:
                            top_y = 0
                        else:
                            top_y = int(lin[6])
                        width = int(lin[10])
                        height = int(lin[14][:-2])
                        bottom_y = top_y + height
                        right_x = left_x + width
                        if bottom_y < 0:
                            bottom_y = 0
                        if right_x > 416:
                            right_x = 416
                        if bottom_y < 4:
                            print(image_name + 'Error SIDE: bottom_y (' + str(bottom_y) + ') is less than 6')
                        elif bottom_y > 412:
                            print(image_name + 'Error SIDE: bottom_y (' + str(bottom_y) + ') is greater than 410')
                        else:
                            if right_x > 412:
                                print(image_name + 'Error SIDE: right_x (' + str(right_x) + ') is greater than 410')
                            elif right_x < 4:
                                print(image_name + 'Error SIDE: right_x (' + str(right_x) + ') is less than 0')
                            else:
                                print(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100))
                                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100) + ' \n')                    
            elif line[0:4] == 'WBC:':
                print('WBC')
                lin = re.split(':|%|t|w|h', line)
                if int(lin[4]) < 4:
                    # pass
                    print(image_name + 'Error WBC: left_x (' + str(lin[4]) + ') is less than 6')
                elif int(lin[4]) > 412:
                    print(image_name + 'Error WBC: left_x (' + str(lin[4]) + ') is greater than 410')
                else:
                    if int(lin[6]) < 4:
                        print(image_name + 'Error WBC: top_y (' + str(lin[6]) + ') is less than 6')
                    elif int(lin[6]) > 412:
                        print(image_name + 'Error WBC: top_y (' + str(lin[6]) + ') is greater than 410')
                    else:
                        # print(lin)
                        classes = 3
                        confidence = int((lin[1]))
                        if int(lin[4]) < 0:
                            left_x = 0
                        else:
                            left_x = int(lin[4])
                        if int(lin[6]) < 0:
                            top_y = 0
                        else:
                            top_y = int(lin[6])
                        width = int(lin[10])
                        height = int(lin[14][:-2])
                        bottom_y = top_y + height
                        right_x = left_x + width
                        if bottom_y < 0:
                            bottom_y = 0
                        if right_x > 416:
                            right_x = 416
                        if bottom_y < 4:
                            print(image_name + 'Error WBC: bottom_y (' + str(bottom_y) + ') is less than 6')
                        elif bottom_y > 412:
                            print(image_name + 'Error WBC: bottom_y (' + str(bottom_y) + ') is greater than 410')
                        else:
                            if right_x > 412:
                                print(image_name + 'Error WBC: right_x (' + str(right_x) + ') is greater than 410')
                            elif right_x < 4:
                                print(image_name + 'Error WBC: right_x (' + str(right_x) + ') is less than 0')
                            else:
                                print(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100))
                                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100) + ' \n')                    
            else:
                pass

def make_groud_truth(ground_truth_file='gt.txt', test_folder='/home/as-hunt/Etra-Space/new_data_sidless/valid/'):
    gt_file = open(ground_truth_file, 'w')
    for file in os.listdir(test_folder):
        if file.endswith('.txt'):
            if file == 'test.txt':
                pass
            elif file == 'classes.txt':
                pass
            elif file == 'train.txt':
                pass
            elif file == 'valid.txt':
                pass
            elif file == 'ground_truth.txt':
                pass
            elif file == 'result_run_1.txt':
                pass
            elif file == 'result_run_2.txt':
                pass
            else:
                img_name = file[:-4] 
                count = 0
                annot = open(test_folder + file, 'r+')
                for line in annot:
                    lin = re.split(' ', line)
                    print(lin[1])
                    classes = lin[0]
                    center_x = lin[1]
                    center_y = lin[2]
                    width = lin[3]
                    height = lin[4]
                    if center_x == '0':
                        print('center_x ('+ center_x +') is 0')
                    elif center_y == '0':
                        print('center_x ('+ center_y +') is 0')
                    elif width == '0':
                        print('widht ('+ width +') is 0')
                    elif height == '0':
                        print('height ('+ height +') is 0')
                    else:
                        center_x = decimal.Decimal(center_x) * 416
                        center_y = decimal.Decimal(center_y) * 416
                        width = decimal.Decimal(width) * 416
                        height = decimal.Decimal(height) * 416
                        left_x = int(decimal.Decimal(center_x) - (width / 2))
                        top_y = int(decimal.Decimal(center_y) + (height / 2))
                        right_x = int(decimal.Decimal(center_x) + (width / 2))
                        bottom_y = int(decimal.Decimal(center_y) - (height / 2))
                        if left_x <= 6:
                            print('left_x (' + str(left_x) + ') is less than 6')
                        elif left_x >= 410:
                            print('left_x (' + str(left_x) + ') is greater than 410')
                        else:
                            if top_y <= 6:
                                print('top_y (' + str(top_y) + ') is less than 6')
                            elif top_y >= 410:
                                print('top_y (' + str(top_y) + ') is greater than 410')
                            else:
                                if right_x <= 6:
                                    print('right_x (' + str(right_x) + ') is less than 6')
                                elif right_x >= 410:
                                    print('right_x (' + str(right_x) + ') is greater than 410')
                                else:
                                    if bottom_y <= 6:
                                        print('bottom_y (' + str(bottom_y) + ') is less than 6')
                                    elif bottom_y >= 410:
                                        print('bottom_y (' + str(bottom_y) + ') is greater than 410')
                                    else:
                                        gt_file.write(img_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' \n')
                                        count += 1
                                        print('Line ' + str(count) + ': ' + img_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y))   

def do_math(gt_file, pd_file, title):
    do_math_blood(gt_file, pd_file, title)

def do_math_blood(gt_file, pd_file, title):
    gt = open(gt_file, 'r')
    gt_array = []
    gt_len = 0
    gt_cm = []
    pud = open(pd_file, 'r')
    pd_len = 0
    pd_array = []
    pd_cm = []
    TP_ECHY = 0
    TP_ERY = 0
    FP_ECHY = 0
    FP_ERY = 0
    FN_ECHY = 0
    FN_ERY = 0
    MissClass_ECHY = 0
    MissClass_ERY = 0
    for line in pud:
        # print(line)
        li = line.split(' ')
        name = li[0]
        classes = li[1]
        bbox = [int(li[2]), int(li[3]), int(li[4]), int(li[5])]
        confidence = li[6]
        pd_array.append([name, bbox, classes, confidence])
        pd_len += 1
    for lune in gt:
        lu = lune.split(' ')
        nome = lu[0]
        clisses = lu[1]
        bbax = [int(lu[2]), int(lu[3]), int(lu[4]), int(lu[5])]
        gt_array.append([nome, bbax, clisses])
        gt_len += 1
    gt.close    
    
    for item in pd_array:
        # print(item[0])
        name = item[0]
        bbox = item[1]
        classes = item[2]
        confidence = item[3]
        for thing in gt_array:
            nome = thing[0]
            bbax = thing[1]
            clisses = thing[2]
            if name in thing[0]:
                # print("Found")
                place = gt_array.index(thing)
                if iou(bbox, bbax) >= 0.5:
                        # print("overlap")
                        # print(iou(bbox,bbax))
                        gt_cm.append(clisses)
                        pd_cm.append(classes)          
                        gt_array.pop(place)
                else:
                    pass
    for item in gt_array:
        # print(item)
        name = item[0]
        bbox = item[1]
        classes = item[2]
        if classes== '0':
            FN_ECHY += 1
        elif classes == '1':
            FN_ERY += 1
    # name = pd_file.split('/')
    path = '/home/as-hunt/Etra-Space/5-class-more/'
    name = 'Normalised Confusion Matrix ' + title + ' Post bbox matching'
    # print(gt_cm)
    # print(pd_cm)
    y_actu = pd.Series(gt_cm, name='Ground Truth')
    y_pred = pd.Series(pd_cm, name='Predicted')
    F1m = f1_score(y_actu, y_pred, average='macro')
    print("F1 macro: " + str(F1m))
    F1w = f1_score(y_actu, y_pred, average='weighted')
    print("F1 weighted: " + str(F1w))
    F1n = f1_score(y_actu, y_pred, average=None)
    print("F1 none: " + str(F1n))
    acc = accuracy_score(y_actu, y_pred)
    print("Accuracy score sklearn: " + str(acc))
    target_names = ['ERY', 'PLT', 'WBC']
    print(classification_report(y_actu, y_pred, target_names=target_names))
    precision_score_weighted = precision_score(y_actu, y_pred, average='weighted')
    print("Precision score weighted: " + str(precision_score_weighted))
    precision_score_macro = precision_score(y_actu, y_pred, average='macro')
    print("Precision score macro: " + str(precision_score_macro))
    precision_score_none = precision_score(y_actu, y_pred, average=None)
    print("Precision score none: " + str(precision_score_none))
    recall_score_weighted = recall_score(y_actu, y_pred, average='weighted')
    print("Recall score weighted: " + str(recall_score_weighted))
    recall_score_macro = recall_score(y_actu, y_pred, average='macro')
    print("Recall score macro: " + str(recall_score_macro))
    recall_score_none = recall_score(y_actu, y_pred, average=None)
    print("Recall score none: " + str(recall_score_none))
    fbeta05_score_weighted = fbeta_score(y_actu, y_pred, average='weighted', beta=0.5)
    print("F0.5 measure weighted: " + str(fbeta05_score_weighted))
    fbeta05_score_macro = fbeta_score(y_actu, y_pred, average='macro', beta=0.5)
    print("F0.5 measure macro: " + str(fbeta05_score_macro))
    fbeta05_score_none = fbeta_score(y_actu, y_pred, average=None, beta=0.5)
    print("F0.5 measure none: " + str(fbeta05_score_none))
    fbeta2_score_weighted = fbeta_score(y_actu, y_pred, average='weighted', beta=2)
    print("F2 measure weighted: " + str(fbeta2_score_weighted))
    fbeta2_score_macro = fbeta_score(y_actu, y_pred, average='macro', beta=2)
    print("F2 measure macro: " + str(fbeta2_score_macro))
    fbeta2_score_none = fbeta_score(y_actu, y_pred, average=None, beta=2)
    print("F2 measure none: " + str(fbeta2_score_none))
    df_confusion = pd.crosstab(y_actu, y_pred)
    df_conf_norm = df_confusion.div(df_confusion.sum(axis=1), axis="index")
    plt.title(title)
    sns.set(font_scale=1.4) # for label size
    sns.heatmap(df_conf_norm, cmap='viridis_r', annot=True, annot_kws={"size": 16}) # font size
    tick_marks = np.arange(len(df_conf_norm.columns))
    plt.savefig(path + name + '.png')
    plt.clf()
    name = 'Confusion Matrix ' + title + ' Post bbox matching'
    plt.title(title)
    sns.set(font_scale=1.4) # for label size
    sns.heatmap(df_confusion, cmap='viridis_r', annot=True, annot_kws={"size": 16}) # font size
    tick_marks = np.arange(len(df_confusion.columns))
    plt.savefig(path + name + '.png')