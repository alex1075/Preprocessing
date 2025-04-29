# make confusion matrix from ground_truth.txt and prediction.txt
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import fbeta_score
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import jaccard_score
from add_bbox import *
from import_results import *

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
    df_confusion = pd.crosstab(y_actu, y_pred, dropna=False)
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
    df_confusion = pd.crosstab(y_actu, y_pred, dropna=False)
    df_conf_norm = df_confusion.div(df_confusion.sum(axis=1), axis="index")
    return df_conf_norm



# print("Confusion Matrix:")
# print(get_confusion_matrix('/home/as-hunt/ground_truth.csv', '/home/as-hunt/predictions.csv'))
# print("Normalised Confusion Matrix:")
# print(get_normalised_confusion_matrix('/home/as-hunt/ground_truth.csv', '/home/as-hunt/predictions.csv'))


def plot_confusion_matrix(ground_truth_file, prediction_file, title='Confusion matrix'):
    df_confusion = get_confusion_matrix(ground_truth_file, prediction_file)
    # print(df_confusion[1])
  #  plt.figure(figsize = (10,7))
    plt.title(title)
    sns.set(font_scale=1.4) # for label size
    sns.heatmap(df_confusion, cmap='coolwarm', annot=True, annot_kws={"size": 16}) # font size
    tick_marks = np.arange(len(df_confusion.columns))
    plt.savefig(title + '.png')

def plot_normalised_confusion_matrix(ground_truth_file, prediction_file, title='Normalised Confusion matrix'):
    df_confusion = get_normalised_confusion_matrix(ground_truth_file, prediction_file)
    # print(df_confusion[1])
  #  plt.figure(figsize = (10,7))
    plt.title(title)
    sns.set(font_scale=1.4) # for label size
    sns.heatmap(df_confusion, cmap='coolwarm', annot=True, annot_kws={"size": 16}) # font size
    tick_marks = np.arange(len(df_confusion.columns))
    plt.savefig(title + '.png')

# plot_normalised_confusion_matrix('/home/as-hunt/ground_truth.csv', '/home/as-hunt/predictions.csv', title='Normalised Confusion Matrix')



def do_math_4(gt_file, pd_file, title):
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
    TP_PLT = 0
    TP_WBC = 0
    FP_ECHY = 0
    FP_PLT = 0
    FP_ERY = 0
    FP_WBC = 0
    FN_ECHY = 0
    FN_ERY = 0
    FN_PLT = 0
    FN_WBC = 0
    MissClass_ECHY = 0
    MissClass_ECHY_as_ERY = 0
    MissClass_ECHY_as_PLT = 0
    MissClass_ECHY_as_WBC = 0
    MissClass_ERY = 0
    MissClass_ERY_as_ECHY = 0
    MissClass_ERY_as_PLT = 0
    MissClass_ERY_as_WBC = 0
    MissClass_PLT = 0
    MissClass_PLT_as_ECHY = 0
    MissClass_PLT_as_ERY = 0
    MissClass_PLT_as_WBC = 0
    MissClass_WBC = 0
    MissClass_WBC_as_ECHY = 0
    MissClass_WBC_as_ERY = 0
    MissClass_WBC_as_PLT = 0
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
                            elif classes == '2':
                                TP_PLT += 1
                                # print("TP_WBC: ", TP_WBC)
                            elif classes == '3':
                                TP_WBC += 1
                                # print("TP_WBC: ", TP_WBC)    
                            gt_array.pop(place)
                            # print("item removed")
                        else:
                            # print("Classes do not match, detection error")
                            if classes == '0':
                                if clisses == '1':
                                    MissClass_ERY_as_ECHY += 1
                                elif clisses == '2':
                                    MissClass_PLT_as_ECHY += 1
                                elif clisses == '3':
                                    MissClass_WBC_as_ECHY += 1
                            elif classes == '1':
                                if clisses == '0':
                                    MissClass_ECHY_as_ERY += 1
                                elif clisses == '2':
                                    MissClass_PLT_as_WBC += 1
                                elif clisses == '3':
                                    MissClass_WBC_as_ERY += 1
                            elif classes == '2':
                                if clisses == '0':
                                    MissClass_ECHY_as_PLT += 1
                                elif clisses == '1':
                                    MissClass_ERY_as_PLT += 1
                                elif clisses == '3':
                                    MissClass_WBC_as_PLT += 1
                            elif classes == '3':
                                if clisses == '0':
                                    MissClass_ECHY_as_WBC += 1
                                elif clisses == '1':
                                    MissClass_ERY_as_WBC += 1
                                elif clisses == '2':
                                    MissClass_PLT_as_WBC += 1                   
                            gt_array.pop(place)
                else:
                    # print("no overlap")
                    if classes== '0':
                        FP_ECHY += 1
                    elif classes == '1':
                        FP_ERY += 1
                    elif classes == '2':
                        FP_PLT += 1
                    elif classes == '3':
                        FP_WBC += 1
    for item in gt_array:
        # print(item)
        name = item[0]
        bbox = item[1]
        classes = item[2]
        if classes== '0':
            FN_ECHY += 1
        elif classes == '1':
            FN_ERY += 1
        elif classes == '2':
            FN_PLT += 1
        elif classes == '3':
            FN_WBC += 1
    FNECHY = FN_ECHY + MissClass_ECHY_as_ERY + MissClass_ECHY_as_PLT + MissClass_ECHY_as_WBC
    FNERY = FN_ERY + MissClass_ERY_as_ECHY + MissClass_ERY_as_PLT + MissClass_ERY_as_WBC
    FNPLT = FN_PLT + MissClass_PLT_as_ECHY + MissClass_PLT_as_ERY + MissClass_PLT_as_WBC
    FNWBC = FN_WBC + MissClass_WBC_as_ECHY + MissClass_WBC_as_ERY + MissClass_WBC_as_PLT
    FPERY = FP_ERY + MissClass_ECHY_as_ERY + MissClass_PLT_as_ERY + MissClass_WBC_as_ERY
    FPECHY = FP_ECHY + MissClass_ERY_as_ECHY + MissClass_PLT_as_ECHY + MissClass_WBC_as_ECHY
    FPPLT = FP_PLT + MissClass_ECHY_as_PLT + MissClass_ERY_as_PLT + MissClass_WBC_as_PLT
    FPWBC = FP_WBC + MissClass_ECHY_as_WBC + MissClass_ERY_as_WBC + MissClass_PLT_as_WBC
    print("True Positives ECHY: " + str(TP_ECHY))
    print("True Positives ERY: " + str(TP_ERY))
    print("True Positives PLT: " + str(TP_PLT))
    print("True Positives WBC: " + str(TP_WBC))
    TP = TP_ECHY + TP_ERY + TP_WBC + TP_PLT
    print("True Positives: " + str(TP))
    print("False Positives ECHY: " + str(FP_ECHY))
    print("False Positives ERY: " + str(FP_ERY))
    print("False Positives PLT: " + str(FP_PLT))
    print("False Positives WBC: " + str(FP_WBC))
    FP = FPECHY + FPERY + FPWBC + FPPLT
    print("False Positives: " + str(FP))
    print("False Negatives ECHY: " + str(FN_ECHY))
    print("False Negatives ERY: " + str(FN_ERY))
    print("False Negatives PLT: " + str(FN_PLT))
    print("False Negatives WBC: " + str(FN_WBC))
    FN = FNECHY + FNERY + FNWBC + FNPLT
    print("False Negatives: " + str(FN))
    print("MissClass ECHY: " + str(MissClass_ECHY))
    print("MissClass ERY: " + str(MissClass_ERY))
    print("MissClass PLT: " + str(MissClass_PLT))
    print("MissClass WBC: " + str(MissClass_WBC))
    predicted = pd_len
    print("Predicted: " + str(predicted))
    actual = gt_len
    if TP_ECHY + FPECHY != 0:
        precision_ECHY = TP_ECHY / (TP_ECHY + FPECHY)
        print("Precision ECHY: " + str(precision_ECHY))
    else:
        print("Precision ECHY: 0")
    if TP_ERY + FPERY != 0:
        precision_ERY = TP_ERY / (TP_ERY + FPERY)
        print("Precision ERY: " + str(precision_ERY))
    else:
        print("Precision ERY: 0")
    if TP_PLT + FPPLT != 0:
        precision_PLT = TP_PLT / (TP_PLT + FPPLT)
        print("Precision PLT: " + str(precision_PLT))
    else:
        print("Precision PLT: 0")  
        precision_PLT = 0      
    if TP_WBC + FPWBC != 0:
        precision_WBC = TP_WBC / (TP_WBC + FPWBC)
        print("Precision WBC: " + str(precision_WBC))
    else:
        print("Precision WBC: 0")
    if TP_ECHY + FNECHY != 0:
        recall_ECHY = TP_ECHY / (TP_ECHY + FNECHY)
        print("Recall ECHY: " + str(recall_ECHY))
    else:
        print("Recall ECHY: 0")
    if TP_ERY + FNERY != 0:
        recall_ERY = TP_ERY / (TP_ERY + FNERY)
        print("Recall ERY: " + str(recall_ERY))
    else:
        print("Recall ERY: 0")
    if TP_PLT + FNPLT != 0:
        recall_PLT = TP_PLT / (TP_PLT + FNPLT)
        print("Recall PLT: " + str(recall_PLT))
    else:
        print("Recall PLT: 0")    
    if TP_WBC + FNWBC != 0:
        recall_WBC = TP_WBC / (TP_WBC + FNWBC)
        print("Recall WBC: " + str(recall_WBC))
    else:
        print("Recall WBC: 0")
    accuracy = (TP ) / (TP + FP + FN)
    print("Actual: " + str(actual))
    print("Accuracy: " + str(round(accuracy, 3)))
    if TP + FP + FN != 0:
        F1 = (TP)/(TP+ ((FP + FN)/2))
        print("F1: " + str(round(F1, 3)))
    else:
        print("F1: 0")
    if TP + FP != 0:
        precision = TP / (TP + FP)
        print("Precision: " + str(round(precision, 3)))
    else:
        print("Precision: 0")
    if TP + FN != 0:
        recall = TP / (TP + FN)
        print("Recall: " + str(round(recall, 3)))
    # if TP_ECHY + FP_ECHY + FN_ECHY != 0:
    #     F1_ECHY = 2 * (precision_ECHY * recall_ECHY) / (precision_ECHY + recall_ECHY)
    #     print("F1 ECHY: " + str(F1_ECHY))
    # else:
    #     print("F1 ECHY: 0")
    # if TP_ERY + FP_ERY + FN_ERY != 0:
    #     F1_ERY = 2 * (precision_ERY * recall_ERY) / (precision_ERY + recall_ERY)
    #     print("F1 ERY: " + str(F1_ERY))
    # else:
    #     print("F1 ERY: 0")
    # if precision_PLT + recall_PLT != 0:
    #     F1_PLT = 2 * (precision_PLT * recall_PLT) / (precision_PLT + recall_PLT)
    #     print("F1 PLT: " + str(F1_PLT))
    # else:
    #     print("F1 PLT: 0")
    # if TP_WBC + FP_WBC + FN_WBC != 0:
    #     F1_WBC = 2 * (precision_WBC * recall_WBC) / (precision_WBC + recall_WBC)
    #     print("F1 WBC: " + str(F1_WBC))
    # else:
    #     print("F1 WBC: 0")
    print("MissClass: " + str(MissClass_ECHY_as_ERY + MissClass_ECHY_as_PLT + MissClass_ECHY_as_WBC + MissClass_ERY_as_ECHY + MissClass_ERY_as_PLT + MissClass_ERY_as_WBC + MissClass_PLT_as_ECHY + MissClass_PLT_as_ERY + MissClass_PLT_as_WBC + MissClass_WBC_as_ECHY + MissClass_WBC_as_ERY + MissClass_WBC_as_PLT))
    # name = pd_file.split('/')
    path = '/home/as-hunt/Etra-Space/'
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
    # target_names = ['Echinocyte', 'Erythrocyte', 'Leukocyte']
    # target_names = ['Echinocyte', 'Erythrocyte', 'Platelet']
    target_names = ['Echinocyte', 'Erythrocyte', 'Platelet', 'Leukocyte']
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
    df_confusion = pd.crosstab(y_actu, y_pred, dropna=False)
    df_conf_norm = df_confusion.div(df_confusion.sum(axis=1), axis="index")
  #  plt.figure(figsize = (10,7))
    plt.title(title)
    sns.set(font_scale=1.4) # for label size
    sns.heatmap(df_conf_norm, cmap='coolwarm', annot=True, annot_kws={"size": 16}, xticklabels=target_names, yticklabels=target_names) # font size
    tick_marks = np.arange(len(df_conf_norm.columns))
    plt.savefig(path + name + '.png', bbox_inches='tight')
    plt.clf()
    name = 'Confusion Matrix ' + title + ' Post bbox matching'
  #  plt.figure(figsize = (10,7))
    plt.title(title)
    sns.set(font_scale=1.4) # for label size
    sns.heatmap(df_confusion, cmap='coolwarm', annot=True, annot_kws={"size": 16}, xticklabels=target_names, yticklabels=target_names) # font size
    tick_marks = np.arange(len(df_confusion.columns))
    plt.savefig(path + name + '.png', bbox_inches='tight')
    count_classes_file(gt_file, True, title + '_split.png', target_names)


def do_math_two(gt_file, pd_file, title):
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
                                if clisses == '1':
                                    MissClass_ERY += 1
                            elif classes == '1':
                                if clisses == '0':
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
    FN_ECHY = FN_ECHY + MissClass_ECHY
    FN_ERY = FN_ERY + MissClass_ERY
    FP_ERY = FP_ERY + MissClass_ECHY
    FP_ECHY = FP_ECHY + MissClass_ERY        
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
    accuracy = (TP ) / (TP + FP + FN)
    print("Actual: " + str(actual))
    print("Accuracy: " + str(round(accuracy, 3)))
    if TP + FP + FN != 0:
        F1 = (TP)/(TP+ ((FP + FN)/2))
        print("F1: " + str(round(F1, 3)))
    else:
        print("F1: 0")
    if TP + FP != 0:
        precision = TP / (TP + FP)
        print("Precision: " + str(round(precision, 3)))
    else:
        print("Precision: 0")
    if TP + FN != 0:
        recall = TP / (TP + FN)
        print("Recall: " + str(round(recall, 3)))
    print("MissClass: " + str(MissClass_ECHY + MissClass_ERY))
    # name = pd_file.split('/')
    path = '/home/as-hunt/Etra-Space/Mono/'
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
    target_names = ['Monocyte', 'Monocyte Activated']
    print(y_actu, y_pred)
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
    df_confusion = pd.crosstab(y_actu, y_pred, dropna=False)
    df_conf_norm = df_confusion.div(df_confusion.sum(axis=1), axis="index")
  #  plt.figure(figsize = (10,7))
    plt.title(title)
    sns.set(font_scale=1.4) # for label size
    sns.heatmap(df_conf_norm, cmap='coolwarm', annot=True, annot_kws={"size": 16}, xticklabels=target_names, yticklabels=target_names) # font size
    tick_marks = np.arange(len(df_conf_norm.columns))
    plt.savefig(path + name + '.png', bbox_inches='tight')
    plt.clf()
    name = 'Confusion Matrix ' + title + ' Post bbox matching'
  #  plt.figure(figsize = (10,7))
    plt.title(title)
    sns.set(font_scale=1.4) # for label size
    sns.heatmap(df_confusion, cmap='coolwarm', annot=True, annot_kws={"size": 16}, xticklabels=target_names, yticklabels=target_names) # font size
    tick_marks = np.arange(len(df_confusion.columns))
    plt.savefig(path + name + '.png', bbox_inches='tight')
    count_classes_file(gt_file, True, title + '_split.png', target_names)

def do_math_three(gt_file, pd_file, title):
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
                                if clisses == '1':
                                    MissClass_ERY += 1
                            elif classes == '1':
                                if clisses == '0':
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
    FN_ECHY = FN_ECHY + MissClass_ECHY
    FN_ERY = FN_ERY + MissClass_ERY
    FP_ERY = FP_ERY + MissClass_ECHY
    FP_ECHY = FP_ECHY + MissClass_ERY        
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
    accuracy = (TP ) / (TP + FP + FN)
    print("Actual: " + str(actual))
    print("Accuracy: " + str(round(accuracy, 3)))
    if TP + FP + FN != 0:
        F1 = (TP)/(TP+ ((FP + FN)/2))
        print("F1: " + str(round(F1, 3)))
    else:
        print("F1: 0")
    if TP + FP != 0:
        precision = TP / (TP + FP)
        print("Precision: " + str(round(precision, 3)))
    else:
        print("Precision: 0")
    if TP + FN != 0:
        recall = TP / (TP + FN)
        print("Recall: " + str(round(recall, 3)))
    print("MissClass: " + str(MissClass_ECHY + MissClass_ERY))
    # name = pd_file.split('/')
    path = '/home/as-hunt/Etra-Space/'
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
    target_names = ['Erythrocyte', 'Platelet', 'Leukocyte']
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
    df_confusion = pd.crosstab(y_actu, y_pred, dropna=False)
    df_conf_norm = df_confusion.div(df_confusion.sum(axis=1), axis="index")
  #  plt.figure(figsize = (10,7))
    plt.title(title)
    sns.set(font_scale=1.4) # for label size
    sns.heatmap(df_conf_norm, cmap='coolwarm', annot=True, annot_kws={"size": 16}, xticklabels=target_names, yticklabels=target_names) # font size
    tick_marks = np.arange(len(df_conf_norm.columns))
    plt.savefig(path + name + '.png', bbox_inches='tight')
    plt.clf()
    name = 'Confusion Matrix ' + title + ' Post bbox matching'
  #  plt.figure(figsize = (10,7))
    plt.title(title)
    sns.set(font_scale=1.4) # for label size
    sns.heatmap(df_confusion, cmap='coolwarm', annot=True, annot_kws={"size": 16}, xticklabels=target_names, yticklabels=target_names) # font size
    tick_marks = np.arange(len(df_confusion.columns))
    plt.savefig(path + name + '.png', bbox_inches='tight')
    count_classes_file(gt_file, True, title + '_split.png', target_names)

def do_math_all(gt_file, pd_file, title):   
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
    TP_PLT = 0
    TP_WBC = 0
    TP_SIDE = 0
    FP_ECHY = 0
    FP_PLT = 0
    FP_ERY = 0
    FP_WBC = 0
    FP_SIDE = 0
    FN_ECHY = 0
    FN_ERY = 0
    FN_PLT = 0
    FN_WBC = 0
    FN_SIDE = 0
    MissClass_ECHY_as_ERY = 0
    MissClass_ECHY_as_PLT = 0
    MissClass_ECHY_as_WBC = 0
    MissClass_ECHY_as_SIDE = 0
    MissClass_ERY_as_ECHY = 0
    MissClass_ERY_as_PLT = 0
    MissClass_ERY_as_WBC = 0
    MissClass_ERY_as_SIDE = 0
    MissClass_PLT_as_ECHY = 0
    MissClass_PLT_as_ERY = 0
    MissClass_PLT_as_WBC = 0
    MissClass_PLT_as_SIDE = 0
    MissClass_WBC_as_ECHY = 0
    MissClass_WBC_as_ERY = 0
    MissClass_WBC_as_PLT = 0
    MissClass_WBC_as_SIDE = 0
    MissClass_SIDE_as_ECHY = 0
    MissClass_SIDE_as_ERY = 0
    MissClass_SIDE_as_PLT = 0
    MissClass_SIDE_as_WBC = 0
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
                if iou(bbox, bbax) >= 0.5:
                        gt_cm.append(clisses)
                        pd_cm.append(classes)
                        if classes == clisses:
                            if classes == '0':
                                TP_ECHY += 1
                            elif classes == '1':
                                TP_ERY += 1
                            elif classes == '2':
                                TP_PLT += 1
                            elif classes == '3':
                                TP_SIDE += 1
                            elif classes == '4':
                                TP_WBC += 1     
                            gt_array.pop(place)
                        else:
                            if classes == '0':
                                if clisses == '1':
                                    MissClass_ERY_as_ECHY += 1
                                elif clisses == '2':
                                    MissClass_PLT_as_ECHY += 1
                                elif clisses == '3':
                                    MissClass_SIDE_as_ECHY += 1
                                elif clisses == '4':
                                    MissClass_WBC_as_ECHY += 1
                            elif classes == '1':
                                if clisses == '0':
                                    MissClass_ECHY_as_ERY += 1
                                elif clisses == '2':
                                    MissClass_PLT_as_WBC += 1
                                elif clisses == '3':
                                    MissClass_SIDE_as_ERY += 1
                                elif clisses == '4':
                                    MissClass_WBC_as_ERY += 1
                            elif classes == '2':
                                if clisses == '0':
                                    MissClass_ECHY_as_PLT += 1
                                elif clisses == '1':
                                    MissClass_ERY_as_PLT += 1
                                elif clisses == '3':
                                    MissClass_SIDE_as_PLT += 1
                                elif clisses == '4':
                                    MissClass_WBC_as_PLT += 1
                            elif classes == '3':
                                if clisses == '0':
                                    MissClass_ECHY_as_SIDE += 1
                                elif clisses == '1':
                                    MissClass_ERY_as_SIDE += 1
                                elif clisses == '2':
                                    MissClass_PLT_as_SIDE += 1 
                                elif clisses == '4':
                                    MissClass_WBC_as_SIDE += 1
                            elif classes == '4':
                                if clisses == '0':
                                    MissClass_ECHY_as_WBC += 1
                                elif clisses == '1':
                                    MissClass_ERY_as_WBC += 1
                                elif clisses == '2':
                                    MissClass_PLT_as_WBC += 1
                                elif clisses == '3':
                                    MissClass_SIDE_as_WBC += 1
                            gt_array.pop(place)
                else:
                    if classes== '0':
                        FP_ECHY += 1
                    elif classes == '1':
                        FP_ERY += 1
                    elif classes == '2':
                        FP_PLT += 1
                    elif classes == '3':
                        FP_SIDE += 1
                    elif classes == '4':
                        FP_WBC += 1
    for item in gt_array:
        name = item[0]
        bbox = item[1]
        classes = item[2]
        if classes== '0':
            FN_ECHY += 1
        elif classes == '1':
            FN_ERY += 1
        elif classes == '2':
            FN_PLT += 1
        elif classes == '3':
            FN_WBC += 1
    path = '/home/as-hunt/'
    name = 'Normalised Confusion Matrix ' + title + ' Post bbox matching'
    y_actu = pd.Series(gt_cm, name='Ground Truth')
    y_pred = pd.Series(pd_cm, name='Predicted')
    try:
        F1m = f1_score(y_actu, y_pred, average='macro')
    except:
        F1m = 0
    print("F1 macro: " + str(F1m))
    try:
        F1w = f1_score(y_actu, y_pred, average='weighted')
    except:
        F1w = 0
    print("F1 weighted: " + str(F1w))
    try:
        F1n = f1_score(y_actu, y_pred, average=None)
    except:
        F1n = 0
    print("F1 none: " + str(F1n))
    try:
        acc = accuracy_score(y_actu, y_pred)
    except:
        acc = 0
    print("Accuracy score sklearn: " + str(acc))
    target_names = ['Lymphocyte', 'Lymphocyte Activated', 'Monocyte', 'Neutrophil']
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
    df_confusion = pd.crosstab(y_actu, y_pred, dropna=False)
    df_conf_norm = df_confusion.div(df_confusion.sum(axis=1), axis="index")
  #  plt.figure(figsize = (10,7))
    plt.title(title)
    sns.set(font_scale=1.4) # for label size
    sns.heatmap(df_conf_norm, cmap='coolwarm', annot=True, annot_kws={"size": 16}, xticklabels=target_names, yticklabels=target_names) # font size
    tick_marks = np.arange(len(df_conf_norm.columns))
    plt.savefig(path + name + '.png', bbox_inches='tight')
    plt.clf()
    name = 'Confusion Matrix ' + title + ' Post bbox matching'
  #  plt.figure(figsize = (10,7))
    plt.title(title)
    sns.set(font_scale=1.4) # for label size
    sns.heatmap(df_confusion, cmap='coolwarm', annot=True, annot_kws={"size": 16}, xticklabels=target_names, yticklabels=target_names) # font size
    tick_marks = np.arange(len(df_confusion.columns))
    plt.savefig(path + name + '.png', bbox_inches='tight')
    count_classes_file(gt_file, True, title + '_split.png', target_names)

def do_math_leuko(gt_file, pd_file, title, savefig=True):
    gt = open(gt_file, 'r')
    gt_array = []
    gt_len = 0
    gt_cm = []
    pud = open(pd_file, 'r')
    pd_len = 0
    pd_array = []
    pd_cm = []
    TP_LYM = 0
    TP_MON = 0
    TP_NEU = 0
    FP_LYM = 0
    FP_MON = 0
    FP_NEU = 0
    FN_LYM = 0
    FN_MON = 0
    FN_NEU = 0
    MissClass_LYM_as_MON = 0
    MissClass_LYM_as_NEU = 0
    MissClass_MON_as_LYM = 0
    MissClass_MON_as_NEU = 0
    MissClass_NEU_as_LYM = 0
    MissClass_NEU_as_MON = 0
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
                if iou(bbox, bbax) >= 0.5:
                        gt_cm.append(clisses)
                        pd_cm.append(classes)
                        if classes == clisses:
                            if classes == '0':
                                TP_LYM += 1
                            elif classes == '1':
                                TP_MON += 1
                            elif classes == '2':
                                TP_NEU += 1
                            gt_array.pop(place)
                        else:
                            if classes == '0': # LYM prediction
                                if clisses == '1': # MON ground truth
                                    MissClass_MON_as_LYM += 1
                                elif clisses == '2':
                                    MissClass_NEU_as_LYM += 1
                            elif classes == '1': # MON prediction
                                if clisses == '0': # LYM ground truth
                                    MissClass_LYM_as_MON += 1
                                elif clisses == '2':
                                    MissClass_NEU_as_MON += 1
                            elif classes == '2': # NEU prediction
                                if clisses == '0': # LYM ground truth
                                    MissClass_LYM_as_NEU += 1
                                elif clisses == '1':
                                    MissClass_MON_as_NEU += 1
                            gt_array.pop(place)
                else:
                    if classes== '0':
                        FP_LYM += 1
                    elif classes == '1':
                        FP_MON += 1
                    elif classes == '2':
                        FP_NEU += 1
    for item in gt_array:
        name = item[0]
        bbox = item[1]
        classes = item[2]
        if classes== '0':
            FN_LYM += 1
        elif classes == '1':
            FN_MON += 1
        elif classes == '2':
            FN_NEU += 1
    FNLYM = FN_LYM + MissClass_LYM_as_MON + MissClass_LYM_as_NEU
    MissClass_LYM = MissClass_LYM_as_MON + MissClass_LYM_as_NEU
    MissClass_MON = MissClass_MON_as_LYM + MissClass_MON_as_NEU
    FNMON = FN_MON + MissClass_MON_as_LYM + MissClass_MON_as_NEU
    FNNEU = FN_NEU + MissClass_NEU_as_LYM + MissClass_NEU_as_MON
    MissClass_NEU = MissClass_NEU_as_LYM + MissClass_NEU_as_MON
    FPLYM = FP_LYM + MissClass_MON_as_LYM + MissClass_NEU_as_LYM
    FPNEU = FP_NEU + MissClass_LYM_as_NEU + MissClass_MON_as_NEU
    FPMON = FP_MON + MissClass_LYM_as_MON + MissClass_NEU_as_MON
    # print("True Positives LYM: " + str(TP_LYM))
    # print("True Positives MON: " + str(TP_MON))
    # print("True Positives NEU: " + str(TP_NEU))
    TP = TP_LYM + TP_MON + TP_NEU
    # print("True Positives: " + str(TP))
    # print("False Positives LYM: " + str(FPLYM))
    # print("False Positives MON: " + str(FPMON))
    # print("False Positives NEU: " + str(FPNEU))
    FP = FPLYM + FPMON + FPNEU
    # print("False Positives: " + str(FP))
    # print("False Negatives LYM: " + str(FNLYM))
    # print("False Negatives MON: " + str(FNMON))
    # print("False Negatives NEU: " + str(FNNEU))
    FN = FNLYM + FNMON + FNNEU
    # print("False Negatives: " + str(FN))
    # print("MissClass LYM: " + str(MissClass_LYM))
    # print("MissClass MON: " + str(MissClass_MON))
    # print("MissClass NEU: " + str(MissClass_NEU))
    predicted = pd_len
    # print("Predicted: " + str(predicted))
    actual = gt_len
    accuracy = (TP) / (TP + FP + FN)
    # print("Actual: " + str(actual))
    # print("Accuracy: " + str(round(accuracy, 3)))
    # if TP + FP + FN != 0:
    #     F1 = (TP)/(TP+ ((FP + FN)/2))
    #     # print("F1: " + str(round(F1, 3)))
    # else:
    # #     # print("F1: 0")
    # if TP + FP != 0:
    #     precision = TP / (TP + FP)
    #     # print("Precision: " + str(round(precision, 3)))
    # else:
    #     # print("Precision: 0")
    #     pass
    # if TP + FN != 0:
    #     recall = TP / (TP + FN)
    # else:
    #     pass    
        # print("Recall: " + str(round(recall, 3)))
    # print("MissClass: " + str((MissClass_LYM + MissClass_MON + MissClass_NEU)))
    path = '/home/as-hunt/'
    name = 'Normalised Confusion Matrix ' + title + ' Post bbox matching'
    y_actu = pd.Series(gt_cm, name='Ground Truth')
    y_pred = pd.Series(pd_cm, name='Predicted')
    try:
        F1m = f1_score(y_actu, y_pred, average='macro')
        if math.isnan(F1m)==True:
            F1m =  '0'
        elif F1m  == '-0.0':
            F1m =  '0'    
    except:
        F1m =  '0'
    print("F1 macro: " + str(F1m))
    try:
        F1w = f1_score(y_actu, y_pred, average='weighted')
        if math.isnan(F1w)==True:
            F1w =  '0'
        elif F1w == '0.0':        
            F1w =  '0'
    except:
        F1w =  '0'
    print("F1 weighted: " + str(F1w))
    F1n = f1_score(y_actu, y_pred, average=None)
    # print("F1 none: " + str(F1n))
    try:
        acc = accuracy_score(y_actu, y_pred)
        if math.isnan(acc)==True:
            acc =  '0'
        elif acc  == '-0.0':
            acc =  '0'
    except:
        acc =  '0'
    print("Accuracy score sklearn: " + str(acc))
    target_names = ['Lymphocyte', 'Lymphocyte activated', 'Monocytes', 'Monocytes activated','Neutrophils', 'Neutrophils activated']
    try:
        print(classification_report(y_actu, y_pred, target_names=target_names))
    except:
        print("Classification report failed")
    try:
        precision_score_weighted = precision_score(y_actu, y_pred, average='weighted')
        if math.isnan(precision_score_weighted)==True:
            precision_score_weighted =  '0'
        elif precision_score_weighted  == '-0.0':
            precision_score_weighted =  '0'    
    except:
        precision_score_weighted =  '0'
    print("Precision score weighted: " + str(precision_score_weighted))
    try:
        precision_score_macro = precision_score(y_actu, y_pred, average='macro')
        if math.isnan(precision_score_macro)==True:
            precision_score_macro =  '0'
        elif precision_score_macro  == '-0.0':
            precision_score_macro =  '0'
    except:
        precision_score_macro =  '0'
    print("Precision score macro: " + str(precision_score_macro))
    precision_score_none = precision_score(y_actu, y_pred, average=None)
    print("Precision score none: " + str(precision_score_none))
    try:
        recall_score_weighted = recall_score(y_actu, y_pred, average='weighted')
        if math.isnan(recall_score_weighted)==True:
            recall_score_weighted =  '0'
        elif recall_score_weighted  == '-0.0':
            recall_score_weighted =  '0'
    except:
        recall_score_weighted =  '0'
    print("Recall score weighted: " + str(recall_score_weighted))
    try:
        recall_score_macro = recall_score(y_actu, y_pred, average='macro')
        if math.isnan(recall_score_macro)==True:
            recall_score_macro =  '0'
        elif recall_score_macro  == '-0.0': 
            recall_score_macro =  '0'
    except:
        recall_score_macro =  '0'
    print("Recall score macro: " + str(recall_score_macro))
    recall_score_none = recall_score(y_actu, y_pred, average=None)
    print("Recall score none: " + str(recall_score_none))
    try:
        fbeta05_score_weighted = fbeta_score(y_actu, y_pred, average='weighted', beta=0.5)
        if math.isnan(fbeta05_score_weighted)==True:
            fbeta05_score_weighted =  '0'
        elif fbeta05_score_weighted  == '-0.0':
            fbeta05_score_weighted =  '0'
    except:
        fbeta05_score_weighted =  '0'
    print("F0.5 measure weighted: " + str(fbeta05_score_weighted))
    try:
        fbeta05_score_macro = fbeta_score(y_actu, y_pred, average='macro', beta=0.5)
        if math.isnan(fbeta05_score_macro)==True:
            fbeta05_score_macro =  '0'
        elif fbeta05_score_macro  == '-0.0':
            fbeta05_score_macro =  '0'
    except:
        fbeta05_score_macro =  '0'
    print("F0.5 measure macro: " + str(fbeta05_score_macro))
    fbeta05_score_none = fbeta_score(y_actu, y_pred, average=None, beta=0.5)
    print("F0.5 measure none: " + str(fbeta05_score_none))
    try:
        fbeta2_score_weighted = fbeta_score(y_actu, y_pred, average='weighted', beta=2)
        if math.isnan(fbeta2_score_weighted)==True:
            fbeta2_score_weighted =  '0'
        elif fbeta2_score_weighted  == '-0.0':
            fbeta2_score_weighted =  '0'
    except:
        fbeta2_score_weighted =  '0'
    print("F2 measure weighted: " + str(fbeta2_score_weighted))
    try:
        fbeta2_score_macro = fbeta_score(y_actu, y_pred, average='macro', beta=2)
        if math.isnan(fbeta2_score_macro)==True:
            fbeta2_score_macro =  '0'
        elif fbeta2_score_macro  == '-0.0':
            fbeta2_score_macro =  '0'
    except:
        fbeta2_score_macro =  '0'
    print("F2 measure macro: " + str(fbeta2_score_macro))
    fbeta2_score_none = fbeta_score(y_actu, y_pred, average=None, beta=2)
    print("F2 measure none: " + str(fbeta2_score_none))
    try:
        df_confusion = pd.crosstab(y_actu, y_pred, dropna=False)
        df_conf_norm = df_confusion.div(df_confusion.sum(axis=1), axis="index")
    #  plt.figure(figsize = (10,7))
        plt.title(title)
        sns.set(font_scale=1.4) # for label size
        sns.heatmap(df_conf_norm, cmap='coolwarm', annot=True, annot_kws={"size": 16}, xticklabels=target_names, yticklabels=target_names) # font size
        tick_marks = np.arange(len(df_conf_norm.columns))
        if savefig == True:
            plt.savefig(path + name + '.png', bbox_inches='tight')
        plt.clf()
        name = 'Confusion Matrix ' + title + ' Post bbox matching'
    #  plt.figure(figsize = (10,7))
        plt.title(title)
        sns.set(font_scale=1.4) # for label size
        sns.heatmap(df_confusion, cmap='coolwarm', annot=True, annot_kws={"size": 16}, xticklabels=target_names, yticklabels=target_names) # font size
        tick_marks = np.arange(len(df_confusion.columns))
        if savefig == True:
            plt.savefig(path + name + '.png', bbox_inches='tight')
            count_classes_file(gt_file, True, title + '_split.png', target_names)
    except:
        pass
    return F1w, F1m, acc, precision_score_weighted, precision_score_macro, recall_score_weighted, recall_score_macro, fbeta05_score_weighted, fbeta05_score_macro, fbeta2_score_weighted, fbeta2_score_macro
    
def do_math_leukall(gt_file, pd_file, title, savefig=False):
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
    TP_PLT = 0
    TP_LYM = 0
    TP_MON = 0
    TP_NEU = 0
    FP_ECHY = 0
    FP_PLT = 0
    FP_ERY = 0
    FP_LYM = 0
    FP_MON = 0
    FP_NEU = 0
    FN_ECHY = 0
    FN_ERY = 0
    FN_PLT = 0
    FN_LYM = 0
    FN_MON = 0
    FN_NEU = 0
    MissClass_ECHY_as_ERY = 0
    MissClass_ECHY_as_PLT = 0
    MissClass_ECHY_as_LYM = 0
    MissClass_ECHY_as_MON = 0
    MissClass_ECHY_as_NEU = 0
    MissClass_ERY_as_ECHY = 0
    MissClass_ERY_as_PLT = 0
    MissClass_ERY_as_LYM = 0
    MissClass_ERY_as_MON = 0
    MissClass_ERY_as_NEU = 0
    MissClass_PLT_as_ECHY = 0
    MissClass_PLT_as_ERY = 0
    MissClass_PLT_as_LYM = 0
    MissClass_PLT_as_MON = 0
    MissClass_PLT_as_NEU = 0
    MissClass_LYM_as_ECHY = 0
    MissClass_LYM_as_ERY = 0
    MissClass_LYM_as_PLT = 0
    MissClass_LYM_as_MON = 0
    MissClass_LYM_as_NEU = 0
    MissClass_MON_as_ECHY = 0
    MissClass_MON_as_ERY = 0
    MissClass_MON_as_PLT = 0
    MissClass_MON_as_LYM = 0
    MissClass_MON_as_NEU = 0
    MissClass_NEU_as_ECHY = 0
    MissClass_NEU_as_ERY = 0
    MissClass_NEU_as_PLT = 0
    MissClass_NEU_as_LYM = 0
    MissClass_NEU_as_MON = 0
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
                if iou(bbox, bbax) >= 0.5:
                        gt_cm.append(clisses)
                        pd_cm.append(classes)
                        if classes == clisses:
                            if classes == '0':
                                TP_ECHY += 1
                            elif classes == '1':
                                TP_ERY += 1
                            elif classes == '2':
                                TP_LYM += 1
                            elif classes == '3':
                                TP_MON += 1
                            elif classes == '4':
                                TP_NEU += 1
                            elif classes == '5':
                                TP_PLT += 1         
                            gt_array.pop(place)
                        else:
                            if classes == '0': # ECHY prediction
                                if clisses == '1': # ERY ground truth
                                    MissClass_ERY_as_ECHY += 1
                                elif clisses == '2':
                                    MissClass_LYM_as_ECHY += 1
                                elif clisses == '3':
                                    MissClass_MON_as_ECHY += 1
                                elif clisses == '4':
                                    MissClass_NEU_as_ECHY += 1
                                elif clisses == '5':
                                    MissClass_PLT_as_ECHY += 1    
                            elif classes == '1': # ERY prediction
                                if clisses == '0': # ECHY ground truth
                                    MissClass_ECHY_as_ERY += 1
                                elif clisses == '2':
                                    MissClass_LYM_as_ERY += 1
                                elif clisses == '3':
                                    MissClass_MON_as_ERY += 1
                                elif clisses == '4':
                                    MissClass_NEU_as_ERY += 1
                                elif clisses == '5':
                                    MissClass_PLT_as_ERY += 1
                            elif classes == '2': # LYM prediction
                                if clisses == '0': # ECHY ground truth
                                    MissClass_ECHY_as_LYM += 1
                                elif clisses == '1':
                                    MissClass_ERY_as_LYM += 1
                                elif clisses == '3':
                                    MissClass_MON_as_LYM += 1
                                elif clisses == '4':
                                    MissClass_NEU_as_LYM += 1
                                elif clisses == '5':
                                    MissClass_PLT_as_LYM += 1
                            elif classes == '3': # MON prediction
                                if clisses == '0': # ECHY ground truth
                                    MissClass_ECHY_as_MON += 1
                                elif clisses == '1':
                                    MissClass_ERY_as_MON += 1
                                elif clisses == '2':
                                    MissClass_LYM_as_MON += 1 
                                elif clisses == '4':
                                    MissClass_NEU_as_MON += 1
                                elif clisses == '5':
                                    MissClass_PLT_as_MON += 1    
                            elif classes == '4': # NEU prediction
                                if clisses == '0': # ECHY ground truth
                                    MissClass_ECHY_as_NEU += 1
                                elif clisses == '1':
                                    MissClass_ERY_as_NEU += 1
                                elif clisses == '2':
                                    MissClass_LYM_as_NEU += 1
                                elif clisses == '3':
                                    MissClass_MON_as_NEU += 1
                                elif clisses == '5':
                                    MissClass_PLT_as_NEU += 1
                            elif classes == '5': # PLT prediction
                                if clisses == '0': # ECHY ground truth
                                    MissClass_ECHY_as_PLT += 1
                                elif clisses == '1':
                                    MissClass_ERY_as_PLT += 1
                                elif clisses == '2':
                                    MissClass_LYM_as_PLT += 1
                                elif clisses == '3':
                                    MissClass_MON_as_PLT += 1
                                elif clisses == '4':
                                    MissClass_NEU_as_PLT += 1
                            gt_array.pop(place)
                else:
                    if classes== '0':
                        FP_ECHY += 1
                    elif classes == '1':
                        FP_ERY += 1
                    elif classes == '2':
                        FP_LYM += 1
                    elif classes == '3':
                        FP_MON += 1
                    elif classes == '4':
                        FP_NEU += 1
                    elif classes == '5':
                        FP_PLT += 1
    for item in gt_array:
        name = item[0]
        bbox = item[1]
        classes = item[2]
        if classes== '0':
            FN_ECHY += 1
        elif classes == '1':
            FN_ERY += 1
        elif classes == '2':
            FN_LYM += 1
        elif classes == '3':
            FN_MON += 1
        elif classes == '4':
            FN_NEU += 1
        elif classes == '5':
            FN_PLT += 1
    # FNECHY = FN_ECHY + MissClass_ECHY_as_ERY + MissClass_ECHY_as_PLT + MissClass_ECHY_as_LYM + MissClass_ECHY_as_MON + MissClass_ECHY_as_NEU 
    # MissClass_ECHY = MissClass_ECHY_as_ERY + MissClass_ECHY_as_PLT + MissClass_ECHY_as_LYM + MissClass_ECHY_as_MON + MissClass_ECHY_as_NEU
    # FNERY = FN_ERY + MissClass_ERY_as_ECHY + MissClass_ERY_as_PLT + MissClass_ERY_as_LYM + MissClass_ERY_as_MON + MissClass_ERY_as_NEU
    # MissClass_ERY = MissClass_ERY_as_ECHY + MissClass_ERY_as_PLT + MissClass_ERY_as_LYM + MissClass_ERY_as_MON + MissClass_ERY_as_NEU
    # FNPLT = FN_PLT + MissClass_PLT_as_ECHY + MissClass_PLT_as_ERY + MissClass_PLT_as_LYM + MissClass_PLT_as_MON + MissClass_PLT_as_NEU
    # MissClass_PLT = MissClass_PLT_as_ECHY + MissClass_PLT_as_ERY + MissClass_PLT_as_LYM + MissClass_PLT_as_MON + MissClass_PLT_as_NEU
    # FNLYM = FN_LYM + MissClass_LYM_as_ECHY + MissClass_LYM_as_ERY + MissClass_LYM_as_PLT + MissClass_LYM_as_MON + MissClass_LYM_as_NEU
    # MissClass_LYM = MissClass_LYM_as_ECHY + MissClass_LYM_as_ERY + MissClass_LYM_as_PLT + MissClass_LYM_as_MON + MissClass_LYM_as_NEU
    # MissClass_MON = MissClass_MON_as_ECHY + MissClass_MON_as_ERY + MissClass_MON_as_PLT + MissClass_MON_as_LYM + MissClass_MON_as_NEU
    # FNMON = FN_MON + MissClass_MON_as_ECHY + MissClass_MON_as_ERY + MissClass_MON_as_PLT + MissClass_MON_as_LYM + MissClass_MON_as_NEU
    # FNNEU = FN_NEU + MissClass_NEU_as_ECHY + MissClass_NEU_as_ERY + MissClass_NEU_as_PLT + MissClass_NEU_as_LYM + MissClass_NEU_as_MON
    # MissClass_NEU = MissClass_NEU_as_ECHY + MissClass_NEU_as_ERY + MissClass_NEU_as_PLT + MissClass_NEU_as_LYM + MissClass_NEU_as_MON
    # FPERY = FP_ERY + MissClass_ECHY_as_ERY + MissClass_PLT_as_ERY + MissClass_LYM_as_ERY + MissClass_MON_as_ERY + MissClass_NEU_as_ERY
    # FPECHY = FP_ECHY + MissClass_ERY_as_ECHY + MissClass_PLT_as_ECHY + MissClass_LYM_as_ECHY + MissClass_MON_as_ECHY + MissClass_NEU_as_ECHY
    # FPPLT = FP_PLT + MissClass_ECHY_as_PLT + MissClass_ERY_as_PLT + MissClass_LYM_as_PLT + MissClass_MON_as_PLT + MissClass_NEU_as_PLT
    # FPLYM = FP_LYM + MissClass_ECHY_as_LYM + MissClass_ERY_as_LYM + MissClass_PLT_as_LYM + MissClass_MON_as_LYM + MissClass_NEU_as_LYM
    # FPNEU = FP_NEU + MissClass_ECHY_as_NEU + MissClass_ERY_as_NEU + MissClass_PLT_as_NEU + MissClass_LYM_as_NEU + MissClass_MON_as_NEU
    # FPMON = FP_MON + MissClass_ECHY_as_MON + MissClass_ERY_as_MON + MissClass_PLT_as_MON + MissClass_LYM_as_MON + MissClass_NEU_as_MON
    # print("True Positives ECHY: " + str(TP_ECHY))
    # print("True Positives ERY: " + str(TP_ERY))
    # print("True Positives LYM: " + str(TP_LYM))
    # print("True Positives MON: " + str(TP_MON))
    # print("True Positives NEU: " + str(TP_NEU))
    # print("True Positives PLT: " + str(TP_PLT))
    # TP = TP_ECHY + TP_ERY + TP_PLT + TP_LYM + TP_MON + TP_NEU
    # print("True Positives: " + str(TP))
    # print("False Positives ECHY: " + str(FPECHY))
    # print("False Positives ERY: " + str(FPERY))
    # print("False Positives LYM: " + str(FPLYM))
    # print("False Positives MON: " + str(FPMON))
    # print("False Positives NEU: " + str(FPNEU))
    # print("False Positives PLT: " + str(FPPLT))
    # FP = FPECHY + FPERY + FPPLT + FPLYM + FPMON + FPNEU
    # print("False Positives: " + str(FP))
    # print("False Negatives ECHY: " + str(FNECHY))
    # print("False Negatives ERY: " + str(FNERY))
    # print("False Negatives LYM: " + str(FNLYM))
    # print("False Negatives MON: " + str(FNMON))
    # print("False Negatives NEU: " + str(FNNEU))
    # print("False Negatives PLT: " + str(FNPLT))
    # FN = FNECHY + FNERY + FNPLT + FNLYM + FNMON + FNNEU
    # print("False Negatives: " + str(FN))
    # print("MissClass ECHY: " + str(MissClass_ECHY))
    # print("MissClass ERY: " + str(MissClass_ERY))
    # print("MissClass LYM: " + str(MissClass_LYM))
    # print("MissClass MON: " + str(MissClass_MON))
    # print("MissClass NEU: " + str(MissClass_NEU))
    # print("MissClass PLT: " + str(MissClass_PLT))
    # predicted = pd_len
    # print("Predicted: " + str(predicted))
    # actual = gt_len
    # accuracy = (TP) / (TP + FP + FN)
    # print("Actual: " + str(actual))
    # print("Accuracy: " + str(round(accuracy, 3)))
    # if TP + FP + FN != 0:
    #     F1 = (TP)/(TP+ ((FP + FN)/2))
    #     print("F1: " + str(round(F1, 3)))
    # else:
    #     print("F1: 0")
    # if TP + FP != 0:
    #     precision = TP / (TP + FP)
    #     print("Precision: " + str(round(precision, 3)))
    # else:
    #     print("Precision: 0")
    # if TP + FN != 0:
    #     recall = TP / (TP + FN)
    #     print("Recall: " + str(round(recall, 3)))
    # print("MissClass: " + str((MissClass_ECHY + MissClass_ERY + MissClass_PLT + MissClass_LYM + MissClass_MON + MissClass_NEU)))
    path = '/home/as-hunt/'
    name = 'Normalised Confusion Matrix ' + title + ' Post bbox matching'
    y_actu = pd.Series(gt_cm, name='Ground Truth')
    y_pred = pd.Series(pd_cm, name='Predicted')
    try:
        F1m = f1_score(y_actu, y_pred, average='macro')
        if math.isnan(F1m)==True:
            F1m =  '0'
        elif F1m  == '-0.0':
            F1m =  '0'    
    except:
        F1m =  '0'
    print("F1 macro: " + str(F1m))
    try:
        F1w = f1_score(y_actu, y_pred, average='weighted')
        if math.isnan(F1w)==True:
            F1w =  '0'
        elif F1w == '0.0':        
            F1w =  '0'
    except:
        F1w =  '0'
    print("F1 weighted: " + str(F1w))
    F1n = f1_score(y_actu, y_pred, average=None)
    print("F1 none: " + str(F1n))
    try:
        acc = accuracy_score(y_actu, y_pred)
        if math.isnan(acc)==True:
            acc =  '0'
        elif acc  == '-0.0':
            acc =  '0'
    except:
        acc =  '0'
    print("Accuracy score sklearn: " + str(acc))
    target_names = ['Echinocytes', 'Erythorcytes', 'Lymphocyte', 'Monocytes', 'Neutrophils', 'Platelets']
    try:
        print(classification_report(y_actu, y_pred, target_names=target_names))
    except:
        print("Classification report failed")
    try:
        precision_score_weighted = precision_score(y_actu, y_pred, average='weighted')
        if math.isnan(precision_score_weighted)==True:
            precision_score_weighted =  '0'
        elif precision_score_weighted  == '-0.0':
            precision_score_weighted =  '0'    
    except:
        precision_score_weighted =  '0'
    print("Precision score weighted: " + str(precision_score_weighted))
    try:
        precision_score_macro = precision_score(y_actu, y_pred, average='macro')
        if math.isnan(precision_score_macro)==True:
            precision_score_macro =  '0'
        elif precision_score_macro  == '-0.0':
            precision_score_macro =  '0'
    except:
        precision_score_macro =  '0'
    print("Precision score macro: " + str(precision_score_macro))
    precision_score_none = precision_score(y_actu, y_pred, average=None)
    print("Precision score none: " + str(precision_score_none))
    try:
        recall_score_weighted = recall_score(y_actu, y_pred, average='weighted')
        if math.isnan(recall_score_weighted)==True:
            recall_score_weighted =  '0'
        elif recall_score_weighted  == '-0.0':
            recall_score_weighted =  '0'
    except:
        recall_score_weighted =  '0'
    print("Recall score weighted: " + str(recall_score_weighted))
    try:
        recall_score_macro = recall_score(y_actu, y_pred, average='macro')
        if math.isnan(recall_score_macro)==True:
            recall_score_macro =  '0'
        elif recall_score_macro  == '-0.0': 
            recall_score_macro =  '0'
    except:
        recall_score_macro =  '0'
    print("Recall score macro: " + str(recall_score_macro))
    recall_score_none = recall_score(y_actu, y_pred, average=None)
    print("Recall score none: " + str(recall_score_none))
    try:
        fbeta05_score_weighted = fbeta_score(y_actu, y_pred, average='weighted', beta=0.5)
        if math.isnan(fbeta05_score_weighted)==True:
            fbeta05_score_weighted =  '0'
        elif fbeta05_score_weighted  == '-0.0':
            fbeta05_score_weighted =  '0'
    except:
        fbeta05_score_weighted =  '0'
    print("F0.5 measure weighted: " + str(fbeta05_score_weighted))
    try:
        fbeta05_score_macro = fbeta_score(y_actu, y_pred, average='macro', beta=0.5)
        if math.isnan(fbeta05_score_macro)==True:
            fbeta05_score_macro =  '0'
        elif fbeta05_score_macro  == '-0.0':
            fbeta05_score_macro =  '0'
    except:
        fbeta05_score_macro =  '0'
    print("F0.5 measure macro: " + str(fbeta05_score_macro))
    fbeta05_score_none = fbeta_score(y_actu, y_pred, average=None, beta=0.5)
    print("F0.5 measure none: " + str(fbeta05_score_none))
    try:
        fbeta2_score_weighted = fbeta_score(y_actu, y_pred, average='weighted', beta=2)
        if math.isnan(fbeta2_score_weighted)==True:
            fbeta2_score_weighted =  '0'
        elif fbeta2_score_weighted  == '-0.0':
            fbeta2_score_weighted =  '0'
    except:
        fbeta2_score_weighted =  '0'
    print("F2 measure weighted: " + str(fbeta2_score_weighted))
    try:
        fbeta2_score_macro = fbeta_score(y_actu, y_pred, average='macro', beta=2)
        if math.isnan(fbeta2_score_macro)==True:
            fbeta2_score_macro =  '0'
        elif fbeta2_score_macro  == '-0.0':
            fbeta2_score_macro =  '0'
    except:
        fbeta2_score_macro =  '0'
    print("F2 measure macro: " + str(fbeta2_score_macro))
    fbeta2_score_none = fbeta_score(y_actu, y_pred, average=None, beta=2)
    print("F2 measure none: " + str(fbeta2_score_none))
    try:
        df_confusion = pd.crosstab(y_actu, y_pred, dropna=False)
        df_conf_norm = df_confusion.div(df_confusion.sum(axis=1), axis="index")
    #  plt.figure(figsize = (10,7))
        plt.title(title)
        sns.set(font_scale=1.4) # for label size
        sns.heatmap(df_conf_norm, cmap='coolwarm', annot=True, annot_kws={"size": 16}, xticklabels=target_names, yticklabels=target_names) # font size
        tick_marks = np.arange(len(df_conf_norm.columns))
        if savefig == True:
            plt.savefig(path + name + '.png', bbox_inches='tight')
        plt.clf()
        name = 'Confusion Matrix ' + title + ' Post bbox matching'
    #  plt.figure(figsize = (10,7))
        plt.title(title)
        sns.set(font_scale=1.4) # for label size
        sns.heatmap(df_confusion, cmap='coolwarm', annot=True, annot_kws={"size": 16}, xticklabels=target_names, yticklabels=target_names) # font size
        tick_marks = np.arange(len(df_confusion.columns))
        if savefig == True:
            plt.savefig(path + name + '.png', bbox_inches='tight')
            count_classes_file(gt_file, True, title + '_split.png', target_names)
    except:
        pass
    return F1w, F1m, acc, precision_score_weighted, precision_score_macro, recall_score_weighted, recall_score_macro, fbeta05_score_weighted, fbeta05_score_macro, fbeta2_score_weighted, fbeta2_score_macro
    
  
def do_math_uni(gt_file, pd_file, title):   
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
    TP_PLT = 0
    TP_WBC = 0
    TP_SIDE = 0
    FP_ECHY = 0
    FP_PLT = 0
    FP_ERY = 0
    FP_WBC = 0
    FP_SIDE = 0
    FN_ECHY = 0
    FN_ERY = 0
    FN_PLT = 0
    FN_WBC = 0
    FN_SIDE = 0
    MissClass_ECHY_as_ERY = 0
    MissClass_ECHY_as_PLT = 0
    MissClass_ECHY_as_WBC = 0
    MissClass_ECHY_as_SIDE = 0
    MissClass_ERY_as_ECHY = 0
    MissClass_ERY_as_PLT = 0
    MissClass_ERY_as_WBC = 0
    MissClass_ERY_as_SIDE = 0
    MissClass_PLT_as_ECHY = 0
    MissClass_PLT_as_ERY = 0
    MissClass_PLT_as_WBC = 0
    MissClass_PLT_as_SIDE = 0
    MissClass_WBC_as_ECHY = 0
    MissClass_WBC_as_ERY = 0
    MissClass_WBC_as_PLT = 0
    MissClass_WBC_as_SIDE = 0
    MissClass_SIDE_as_ECHY = 0
    MissClass_SIDE_as_ERY = 0
    MissClass_SIDE_as_PLT = 0
    MissClass_SIDE_as_WBC = 0
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
                if iou(bbox, bbax) >= 0.5:
                        gt_cm.append(clisses)
                        pd_cm.append(classes)
                        if classes == clisses:
                            if classes == '0':
                                TP_ECHY += 1
                            elif classes == '1':
                                TP_ERY += 1
                            elif classes == '2':
                                TP_PLT += 1
                            elif classes == '3':
                                TP_SIDE += 1
                            elif classes == '4':
                                TP_WBC += 1     
                            gt_array.pop(place)
                        else:
                            if classes == '0':
                                if clisses == '1':
                                    MissClass_ERY_as_ECHY += 1
                                elif clisses == '2':
                                    MissClass_PLT_as_ECHY += 1
                                elif clisses == '3':
                                    MissClass_SIDE_as_ECHY += 1
                                elif clisses == '4':
                                    MissClass_WBC_as_ECHY += 1
                            elif classes == '1':
                                if clisses == '0':
                                    MissClass_ECHY_as_ERY += 1
                                elif clisses == '2':
                                    MissClass_PLT_as_WBC += 1
                                elif clisses == '3':
                                    MissClass_SIDE_as_ERY += 1
                                elif clisses == '4':
                                    MissClass_WBC_as_ERY += 1
                            elif classes == '2':
                                if clisses == '0':
                                    MissClass_ECHY_as_PLT += 1
                                elif clisses == '1':
                                    MissClass_ERY_as_PLT += 1
                                elif clisses == '3':
                                    MissClass_SIDE_as_PLT += 1
                                elif clisses == '4':
                                    MissClass_WBC_as_PLT += 1
                            elif classes == '3':
                                if clisses == '0':
                                    MissClass_ECHY_as_SIDE += 1
                                elif clisses == '1':
                                    MissClass_ERY_as_SIDE += 1
                                elif clisses == '2':
                                    MissClass_PLT_as_SIDE += 1 
                                elif clisses == '4':
                                    MissClass_WBC_as_SIDE += 1
                            elif classes == '4':
                                if clisses == '0':
                                    MissClass_ECHY_as_WBC += 1
                                elif clisses == '1':
                                    MissClass_ERY_as_WBC += 1
                                elif clisses == '2':
                                    MissClass_PLT_as_WBC += 1
                                elif clisses == '3':
                                    MissClass_SIDE_as_WBC += 1
                            gt_array.pop(place)
                else:
                    if classes== '0':
                        FP_ECHY += 1
                    elif classes == '1':
                        FP_ERY += 1
                    elif classes == '2':
                        FP_PLT += 1
                    elif classes == '3':
                        FP_SIDE += 1
                    elif classes == '4':
                        FP_WBC += 1
    for item in gt_array:
        name = item[0]
        bbox = item[1]
        classes = item[2]
        if classes== '0':
            FN_ECHY += 1
        elif classes == '1':
            FN_ERY += 1
        elif classes == '2':
            FN_PLT += 1
        elif classes == '3':
            FN_WBC += 1
    FNECHY = FN_ECHY + MissClass_ECHY_as_ERY + MissClass_ECHY_as_PLT + MissClass_ECHY_as_WBC + MissClass_ECHY_as_SIDE
    MissClass_ECHY = MissClass_ECHY_as_ERY + MissClass_ECHY_as_PLT + MissClass_ECHY_as_WBC + MissClass_ECHY_as_SIDE
    FNERY = FN_ERY + MissClass_ERY_as_ECHY + MissClass_ERY_as_PLT + MissClass_ERY_as_WBC + MissClass_ERY_as_SIDE
    MissClass_ERY = MissClass_ERY_as_ECHY + MissClass_ERY_as_PLT + MissClass_ERY_as_WBC + MissClass_ERY_as_SIDE
    FNPLT = FN_PLT + MissClass_PLT_as_ECHY + MissClass_PLT_as_ERY + MissClass_PLT_as_WBC + MissClass_PLT_as_SIDE
    MissClass_PLT = MissClass_PLT_as_ECHY + MissClass_PLT_as_ERY + MissClass_PLT_as_WBC + MissClass_PLT_as_SIDE
    FNWBC = FN_WBC + MissClass_WBC_as_ECHY + MissClass_WBC_as_ERY + MissClass_WBC_as_PLT + MissClass_WBC_as_SIDE
    MissClass_WBC = MissClass_WBC_as_ECHY + MissClass_WBC_as_ERY + MissClass_WBC_as_PLT + MissClass_WBC_as_SIDE
    MissClass_SIDE = MissClass_SIDE_as_ECHY + MissClass_SIDE_as_ERY + MissClass_SIDE_as_PLT + MissClass_SIDE_as_WBC
    FNSIDE = FN_SIDE + MissClass_SIDE_as_ECHY + MissClass_SIDE_as_ERY + MissClass_SIDE_as_PLT + MissClass_SIDE_as_WBC
    FPERY = FP_ERY + MissClass_ECHY_as_ERY + MissClass_PLT_as_ERY + MissClass_WBC_as_ERY + MissClass_SIDE_as_ERY
    FPECHY = FP_ECHY + MissClass_ERY_as_ECHY + MissClass_PLT_as_ECHY + MissClass_WBC_as_ECHY + MissClass_SIDE_as_ECHY
    FPPLT = FP_PLT + MissClass_ECHY_as_PLT + MissClass_ERY_as_PLT + MissClass_WBC_as_PLT + MissClass_SIDE_as_PLT
    FPWBC = FP_WBC + MissClass_ECHY_as_WBC + MissClass_ERY_as_WBC + MissClass_PLT_as_WBC + MissClass_SIDE_as_WBC
    FPSIDE = FP_SIDE + MissClass_ECHY_as_SIDE + MissClass_ERY_as_SIDE + MissClass_PLT_as_SIDE + MissClass_WBC_as_SIDE
    print("True Positives ECHY: " + str(TP_ECHY))
    print("True Positives ERY: " + str(TP_ERY))
    print("True Positives PLT: " + str(TP_PLT))
    print("True Positives SIDE: " + str(TP_SIDE))
    print("True Positives WBC: " + str(TP_WBC))
    TP = TP_ECHY + TP_ERY + TP_WBC + TP_PLT
    print("True Positives: " + str(TP))
    print("False Positives ECHY: " + str(FP_ECHY))
    print("False Positives ERY: " + str(FP_ERY))
    print("False Positives PLT: " + str(FP_PLT))
    print("False Positives SIDE: " + str(FP_SIDE))
    print("False Positives WBC: " + str(FP_WBC))
    FP = FPECHY + FPERY + FPWBC + FPPLT
    print("False Positives: " + str(FP))
    print("False Negatives ECHY: " + str(FN_ECHY))
    print("False Negatives ERY: " + str(FN_ERY))
    print("False Negatives PLT: " + str(FN_PLT))
    print("False Negatives SIDE: " + str(FN_SIDE))
    print("False Negatives WBC: " + str(FN_WBC))
    FN = FNECHY + FNERY + FNWBC + FNPLT
    print("False Negatives: " + str(FN))
    print("MissClass ECHY: " + str(MissClass_ECHY))
    print("MissClass ERY: " + str(MissClass_ERY))
    print("MissClass PLT: " + str(MissClass_PLT))
    print("MissClass SIDE: " + str(MissClass_SIDE))
    print("MissClass WBC: " + str(MissClass_WBC))
    print("MissClass: " + str((MissClass_ECHY + MissClass_ERY + MissClass_PLT + MissClass_SIDE + MissClass_WBC)))
    path = '/home/as-hunt/'
    name = 'Normalised Confusion Matrix ' + title + ' Post bbox matching'
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
    target_names = ['Erythrocyte', 'Platelet', 'Leukocyte']
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
    df_confusion = pd.crosstab(y_actu, y_pred, dropna=False)
    df_conf_norm = df_confusion.div(df_confusion.sum(axis=1), axis="index")
  #  plt.figure(figsize = (10,7))
    plt.title(title)
    sns.set(font_scale=1.4) # for label size
    sns.heatmap(df_conf_norm, cmap='coolwarm', annot=True, annot_kws={"size": 16}, xticklabels=target_names, yticklabels=target_names) # font size
    tick_marks = np.arange(len(df_conf_norm.columns))
    plt.savefig(path + name + '.png', bbox_inches='tight')
    plt.clf()
    name = 'Confusion Matrix ' + title + ' Post bbox matching'
  #  plt.figure(figsize = (10,7))
    plt.title(title)
    sns.set(font_scale=1.4) # for label size
    sns.heatmap(df_confusion, cmap='coolwarm', annot=True, annot_kws={"size": 16}, xticklabels=target_names, yticklabels=target_names) # font size
    tick_marks = np.arange(len(df_confusion.columns))
    plt.savefig(path + name + '.png', bbox_inches='tight')  
    count_classes_file(gt_file, True, title + '_split.png', target_names)

def do_math(gt_file, pd_file, title, path, save_txt=False, obj_name='/home/as-hunt/Etra-Space/white-thirds/obj.names', save_png=False):
    '''This function takes in a ground truth file and a prediction file and returns AI metrics for the model
    Optionally, it also outputs a confusion matrix and a text file with the results of the confusion matrix
    
    _____________________________________________________________
    Args:

    gt_file: ground truth file
    pd_file: prediction file
    
    title: title of the output files
    path: path to save the output files
    
    save_txt: boolean, whether or not to save the text file
    save_png: boolean, whether or not to save the png file
    
    obj_name: path to the obj.names file to use for the confusion matrix
    ______________________________________________________________
    '''
    gt = open(gt_file, 'r')
    gt_array = []
    gt_len = 0
    gt_cm = []
    pud = open(pd_file, 'r')
    pd_len = 0
    pd_array = []
    pd_cm = []
    target_names = []
    temp = []
    with open(obj_name, 'r') as f:
        for line in f:
            temp.append(line.strip())
    for item in temp:
        if item == 'ECHY':
            target_names.append('Echinocyte')
            temp.remove(item)
        elif item == 'ERY':
            target_names.append('Erythrocyte')
            temp.remove(item)
        elif item == 'LYM':
            target_names.append('Lymphocyte')
            temp.remove(item)
        elif item == 'MON':
            target_names.append('Monocyte')
            temp.remove(item)
        elif item == 'NEU':
            target_names.append('Neutrophil')
            temp.remove(item)
        elif item == 'PLT':
            target_names.append('Platelet')
            temp.remove(item)
        elif item == 'WBC':
            target_names.append('White Blood Cell')
            temp.remove(item)            
    target_names.sort()        
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
                if iou(bbox, bbax) >= 0.5:
                        gt_cm.append(clisses)
                        pd_cm.append(classes)
                        gt_array.pop(place)
                else:
                    pass
    y_actu = pd.Series(gt_cm, name='Ground Truth')
    y_pred = pd.Series(pd_cm, name='Predicted')
    try:
        F1m = f1_score(y_actu, y_pred, average='macro')
        if math.isnan(F1m)==True:
            F1m =  '0'
        elif F1m  == '-0.0':
            F1m =  '0'    
    except:
        F1m =  '0'
    try:
        F1w = f1_score(y_actu, y_pred, average='weighted')
        if math.isnan(F1w)==True:
            F1w =  '0'
        elif F1w == '0.0':        
            F1w =  '0'
    except:
        F1w =  '0'
    F1n = f1_score(y_actu, y_pred, average=None)
    try:
        acc = accuracy_score(y_actu, y_pred)
        if math.isnan(acc)==True:
            acc =  '0'
        elif acc  == '-0.0':
            acc =  '0'
    except:
        acc =  '0'
    try:
        the_report = classification_report(y_actu, y_pred, target_names=target_names)
    except:
        the_report = 'Classification report failed'
    try:
        precision_score_weighted = precision_score(y_actu, y_pred, average='weighted')
        if math.isnan(precision_score_weighted)==True:
            precision_score_weighted =  '0'
        elif precision_score_weighted  == '-0.0':
            precision_score_weighted =  '0'    
    except:
        precision_score_weighted =  '0'
    try:
        precision_score_macro = precision_score(y_actu, y_pred, average='macro')
        if math.isnan(precision_score_macro)==True:
            precision_score_macro =  '0'
        elif precision_score_macro  == '-0.0':
            precision_score_macro =  '0'
    except:
        precision_score_macro =  '0'
    precision_score_none = precision_score(y_actu, y_pred, average=None)
    try:
        recall_score_weighted = recall_score(y_actu, y_pred, average='weighted')
        if math.isnan(recall_score_weighted)==True:
            recall_score_weighted =  '0'
        elif recall_score_weighted  == '-0.0':
            recall_score_weighted =  '0'
    except:
        recall_score_weighted =  '0'
    try:
        recall_score_macro = recall_score(y_actu, y_pred, average='macro')
        if math.isnan(recall_score_macro)==True:
            recall_score_macro =  '0'
        elif recall_score_macro  == '-0.0': 
            recall_score_macro =  '0'
    except:
        recall_score_macro =  '0'
    recall_score_none = recall_score(y_actu, y_pred, average=None)
    try:
        fbeta05_score_weighted = fbeta_score(y_actu, y_pred, average='weighted', beta=0.5)
        if math.isnan(fbeta05_score_weighted)==True:
            fbeta05_score_weighted =  '0'
        elif fbeta05_score_weighted  == '-0.0':
            fbeta05_score_weighted =  '0'
    except:
        fbeta05_score_weighted =  '0'
    try:
        fbeta05_score_macro = fbeta_score(y_actu, y_pred, average='macro', beta=0.5)
        if math.isnan(fbeta05_score_macro)==True:
            fbeta05_score_macro =  '0'
        elif fbeta05_score_macro  == '-0.0':
            fbeta05_score_macro =  '0'
    except:
        fbeta05_score_macro =  '0'
    fbeta05_score_none = fbeta_score(y_actu, y_pred, average=None, beta=0.5)
    try:
        fbeta2_score_weighted = fbeta_score(y_actu, y_pred, average='weighted', beta=2)
        if math.isnan(fbeta2_score_weighted)==True:
            fbeta2_score_weighted =  '0'
        elif fbeta2_score_weighted  == '-0.0':
            fbeta2_score_weighted =  '0'
    except:
        fbeta2_score_weighted =  '0'
    try:
        fbeta2_score_macro = fbeta_score(y_actu, y_pred, average='macro', beta=2)
        if math.isnan(fbeta2_score_macro)==True:
            fbeta2_score_macro =  '0'
        elif fbeta2_score_macro  == '-0.0':
            fbeta2_score_macro =  '0'
    except:
        fbeta2_score_macro =  '0'
    fbeta2_score_none = fbeta_score(y_actu, y_pred, average=None, beta=2)
    try:
        name = 'Normalise Confusion Matrix ' + title + ' Post bbox matching normalised'
        df_confusion = pd.crosstab(y_actu, y_pred, dropna=False)
        df_conf_norm = df_confusion.div(df_confusion.sum(axis=1), axis="index")
        plt.title(title)
        sns.set(font_scale=1.4) # for label size
        sns.heatmap(df_conf_norm, cmap='coolwarm', annot=True, annot_kws={"size": 16}, xticklabels=target_names, yticklabels=target_names) # font size
        tick_marks = np.arange(len(df_conf_norm.columns))
        if save_png == True:
            plt.savefig(path + name + '.png', bbox_inches='tight')
        plt.clf()
        name = 'Confusion Matrix ' + title + ' Post bbox matching'
        plt.title(title)
        sns.set(font_scale=1.4) # for label size
        sns.heatmap(df_confusion, cmap='coolwarm', annot=True, annot_kws={"size": 16}, xticklabels=target_names, yticklabels=target_names) # font size
        tick_marks = np.arange(len(df_confusion.columns))
        if save_png == True:
            plt.savefig(path + name + '.png', bbox_inches='tight')
            count_classes_file(gt_file, True, title + '_split.png', target_names)
    except:
        pass
    if save_txt == True:
        file = open(path + title + '.txt', 'w')
        file.write("F1 macro: " + str(F1m) + '\n')
        file.write("F1 weighted: " + str(F1w) + '\n')
        file.write("F1 none: " + str(F1n) + '\n')
        file.write("Accuracy score sklearn: " + str(acc) + '\n')
        file.write(the_report + '\n')
        file.write("Precision score weighted: " + str(precision_score_weighted) + '\n')
        file.write("Precision score macro: " + str(precision_score_macro) + '\n')
        file.write("Precision score none: " + str(precision_score_none) + '\n')
        file.write("Recall score weighted: " + str(recall_score_weighted) + '\n')
        file.write("Recall score macro: " + str(recall_score_macro) + '\n')
        file.write("Recall score none: " + str(recall_score_none) + '\n')
        file.write("Fbeta05 score weighted: " + str(fbeta05_score_weighted) + '\n')
        file.write("Fbeta05 score macro: " + str(fbeta05_score_macro) + '\n')
        file.write("Fbeta05 score none: " + str(fbeta05_score_none) + '\n')
        file.write("Fbeta2 score weighted: " + str(fbeta2_score_weighted) + '\n')
        file.write("Fbeta2 score macro: " + str(fbeta2_score_macro) + '\n')
        file.write("Fbeta2 score none: " + str(fbeta2_score_none) + '\n')
        file.close()
    return F1w, F1m, acc, precision_score_weighted, precision_score_macro, recall_score_weighted, recall_score_macro, fbeta05_score_weighted, fbeta05_score_macro, fbeta2_score_weighted, fbeta2_score_macro    