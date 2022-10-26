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

# plot_confusion_matrix('/home/as-hunt/ground_truth.csv', '/home/as-hunt/predictions.csv', title='Confusion Matrix')

def plot_normalised_confusion_matrix(ground_truth_file, prediction_file, title='Normalised Confusion matrix'):
    df_confusion = get_normalised_confusion_matrix(ground_truth_file, prediction_file)
    # print(df_confusion[1])
    plt.title(title)
    sns.set(font_scale=1.4) # for label size
    sns.heatmap(df_confusion, cmap='viridis_r', annot=True, annot_kws={"size": 16}) # font size
    tick_marks = np.arange(len(df_confusion.columns))
    plt.savefig(title + '.png')

# plot_normalised_confusion_matrix('/home/as-hunt/ground_truth.csv', '/home/as-hunt/predictions.csv', title='Normalised Confusion Matrix')