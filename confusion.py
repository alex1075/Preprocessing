# make confusion matrix from ground_truth.txt and prediction.txt
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import numpy as np
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

def do_math(gt_file, pd_file, title):
    do_math_all(gt_file, pd_file, title)

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
    path = '/home/as-hunt/Etra-Space/4balanced/'
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
    # target_names = ['ECHY', 'ERY', 'WBC']
    # target_names = ['ECHY', 'ERY', 'PLT']
    target_names = ['ECHY', 'ERY', 'PLT', 'WBC']
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
    path = '/home/as-hunt/Balanced/'
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
    target_names = ['ECHY', 'ERY']
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
    if TP_SIDE + FPSIDE != 0:
        precision_SIDE = TP_SIDE / (TP_SIDE + FPSIDE)
    else:
       print("Precision SIDE: 0")          
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
    if TP_SIDE + FNSIDE != 0:
        recall_SIDE = TP_SIDE / (TP_SIDE + FNSIDE)
    else:
        print("Recall SIDE: 0")    
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
    print("MissClass: " + str((MissClass_ECHY + MissClass_ERY + MissClass_PLT + MissClass_SIDE + MissClass_WBC)))
    path = '/home/as-hunt/Etra-Space/5-class/'
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
    target_names = ['ECHY', 'ERY', 'PLT', 'SIDE', 'WBC']
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