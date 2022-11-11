# make confusion matrix from ground_truth.txt and prediction.txt
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os
import re
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score
from sklearn.metrics import precision_recall_fscore_support
from add_bbox import *

sns.set_palette('viridis')

def get_the_csv(ground_truth_file, prediction_file):
    # reading the given csv file 
    # and creating dataframe
    ground_truth = pd.read_csv(ground_truth_file,
                      delimiter = ' ')
    # store dataframe into csv file
    ground_truth.to_csv(ground_truth_file[:-4]+'.csv',
               index = None)    
    prediction = pd.read_csv(prediction_file,
                        delimiter = ' ')
    prediction.to_csv(prediction_file[:-4]+'.csv',
                index = None)
    

def get_confusion_matrix(ground_truth_file, prediction_file):
    filoo = open( ground_truth_file, 'r')
    actual = []
    for line in filoo:
        lin = line.split(',')
        # print(lin)
        image = lin[0]
        classes = (lin[1])
        actual.append(classes)
    filoo.close()
    filoo = open( prediction_file, 'r')
    predicted = []
    for line in filoo:
        lin = line.split(',')
        # print(lin)
        image = lin[0]
        classes = (lin[1])
        predicted.append(classes)
    filoo.close()
    y_actu = pd.Series(actual, name='Actual')
    y_pred = pd.Series(predicted, name='Predicted')
    df_confusion = pd.crosstab(y_actu, y_pred)
    # df_confusion = pd.crosstab(y_actu, y_pred, rownames=['Actual'], colnames=['Predicted'], margins=True)
    return df_confusion


def get_normalised_confusion_matrix(ground_truth_file, prediction_file):
    filoo = open( ground_truth_file, 'r')
    actual = []
    for line in filoo:
        lin = line.split(',')
        # print(lin)
        image = lin[0]
        classes = (lin[1])
        actual.append(classes)
    filoo.close()
    filoo = open( prediction_file, 'r')
    predicted = []
    for line in filoo:
        lin = line.split(',')
        # print(lin)
        image = lin[0]
        classes = (lin[1])
        predicted.append(classes)
    filoo.close()
    y_actu = pd.Series(actual, name='Actual')
    y_pred = pd.Series(predicted, name='Predicted')
    df_confusion = pd.crosstab(y_actu, y_pred)
    df_conf_norm = df_confusion.div(df_confusion.sum(axis=1), axis="index")
    return df_conf_norm



# print("Confusion Matrix:")
# print(get_confusion_matrix('/home/as-hunt/ground_truth.csv', '/home/as-hunt/predictions.csv'))
# print("Normalised Confusion Matrix:")
# print(get_normalised_confusion_matrix('/home/as-hunt/ground_truth.csv', '/home/as-hunt/predictions.csv'))


def plot_confusion_matrix(ground_truth_file, prediction_file, title='Confusion matrix'):
    df_confusion = get_confusion_matrix(ground_truth_file, prediction_file)
    # print(df_confusion[1])
    plt.title(title)
    sns.set(font_scale=1.4) # for label size
    sns.heatmap(df_confusion, cmap='viridis_r', annot=True, annot_kws={"size": 16}) # font size
    tick_marks = np.arange(len(df_confusion.columns))
    plt.savefig(title + '.png')

def plot_normalised_confusion_matrix(ground_truth_file, prediction_file, title='Normalised Confusion matrix'):
    df_confusion = get_normalised_confusion_matrix(ground_truth_file, prediction_file)
    # print(df_confusion[1])
    plt.title(title)
    sns.set(font_scale=1.4) # for label size
    sns.heatmap(df_confusion, cmap='viridis_r', annot=True, annot_kws={"size": 16}) # font size
    tick_marks = np.arange(len(df_confusion.columns))
    plt.savefig(title + '.png')

# plot_normalised_confusion_matrix('/home/as-hunt/ground_truth.csv', '/home/as-hunt/predictions.csv', title='Normalised Confusion Matrix')

def do_math(gt_file, pd_file):
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
                        if classes == clisses:
                            # print("Classes match! Success!")
                            # print("Classes: ", classes)
                            if classes == '0':
                                TP_ECHY += 1
                                # print("TP_ECHY: ", TP_ECHY)
                            elif classes == '1':
                                TP_ERY += 1
                                # print("TP_ERY: ", TP_ERY)
                            gt_array.pop(place)
                            # print("item removed")
                        else:
                            # print("Classes do not match, detection error")
                            if classes == '0':
                                MissClass_ERY += 1
                            elif classes == '1':
                                MissClass_ECHY += 1
                            gt_array.pop(place)
                else:
                    # print("no overlap")
                    if classes== '0':
                        FP_ECHY += 1
                    elif classes == '1':
                        FP_ERY += 1
    for item in gt_array:
        # print(item)
        name = item[0]
        bbox = item[1]
        classes = item[2]
        if classes== '0':
            FN_ECHY += 1
        elif classes == '1':
            FN_ERY += 1
    print("True Positives ECHY: " + str(TP_ECHY))
    print("True Positives ERY: " + str(TP_ERY))
    TP = TP_ECHY + TP_ERY
    print("True Positives: " + str(TP))
    print("False Positives ECHY: " + str(FP_ECHY))
    print("False Positives ERY: " + str(FP_ERY))
    FP = FP_ECHY + FP_ERY
    print("False Positives: " + str(FP))
    print("False Negatives ECHY: " + str(FN_ECHY))
    print("False Negatives ERY: " + str(FN_ERY))
    FN = FN_ECHY + FN_ERY
    print("False Negatives: " + str(FN))
    print("MissClass ECHY: " + str(MissClass_ECHY))
    print("MissClass ERY: " + str(MissClass_ERY))
    predicted = pd_len
    print("Predicted: " + str(predicted))
    actual = gt_len
    print("Actual: " + str(actual))
    print("Accuracy: " + str(TP/actual))
    print("Precision ECHY: " + str(TP_ECHY/(TP_ECHY + FP_ECHY)))
    print("Precision ERY: " + str(TP_ERY/(TP_ERY + FP_ERY)))
    print("Recall ECHY: " + str(TP_ECHY/(TP_ECHY + FN_ECHY)))
    print("Recall ERY: " + str(TP_ERY/(TP_ERY + FN_ERY)))
    print("F1 ECHY: " + str((2*TP_ECHY)/(2*TP_ECHY + FP_ECHY + FN_ECHY)))
    print("F1 ERY: " + str((2*TP_ERY)/(2*TP_ERY + FP_ERY + FN_ERY)))
    print("F1: " + str((2*TP)/(2*TP + FP + FN)))
    name = pd_file.split('/')
    title = 'Normalised Confusion Matrix ' + name[1][:-4] + ' Post bbox matching'
    # print(gt_cm)
    # print(pd_cm)
    y_actu = pd.Series(gt_cm, name='Ground Truth')
    y_pred = pd.Series(pd_cm, name='Predicted')
    df_confusion = pd.crosstab(y_actu, y_pred)
    df_conf_norm = df_confusion.div(df_confusion.sum(axis=1), axis="index")
    plt.title(title)
    sns.set(font_scale=1.4) # for label size
    sns.heatmap(df_conf_norm, cmap='viridis_r', annot=True, annot_kws={"size": 16}) # font size
    tick_marks = np.arange(len(df_conf_norm.columns))
    plt.savefig(name[0] + '/' + title + '.png')
    plt.clf()
    title = 'Confusion Matrix ' + name[1][:-4] + ' Post bbox matching'
    plt.title(title)
    sns.set(font_scale=1.4) # for label size
    sns.heatmap(df_confusion, cmap='viridis_r', annot=True, annot_kws={"size": 16}) # font size
    tick_marks = np.arange(len(df_confusion.columns))
    plt.savefig(name[0] + '/' + title + '.png')

