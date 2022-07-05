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



def get_confusion_matrix(ground_truth_file, prediction_file):
    ground_truth = pd.read_csv(ground_truth_file, sep=',', header=None)
    prediction = pd.read_csv(prediction_file, sep=',', header=None)
    ground_truth.columns = ['image', 'classes', 'x1', 'y1', 'x2', 'y2']
    prediction.columns = ['image', 'classes', 'x1', 'y1', 'x2', 'y2']
    ground_truth_df = pd.DataFrame(columns=['image', 'classes', 'x1', 'y1', 'x2', 'y2'])
    prediction_df = pd.DataFrame(columns=['image', 'classes', 'x1', 'y1', 'x2', 'y2'])
    for i in range(len(ground_truth)):
        ground_truth_df = ground_truth_df.append(ground_truth.iloc[i])
    for i in range(len(prediction)):
        prediction_df = prediction_df.append(prediction.iloc[i])
    ground_truth_df = ground_truth_df.reset_index(drop=True)
    prediction_df = prediction_df.reset_index(drop=True)
    confusionMatrix = pd.crosstab(ground_truth_df['classes'], prediction_df['classes'], rownames=['Actual'], colnames=['Predicted'])
    return confusionMatrix

# make classification report from ground_truth.csv and prediction.csv using sklearn.classification_report
def get_classification_report(ground_truth_file, prediction_file):
    ground_truth = pd.read_csv(ground_truth_file, sep=',', header=None)
    prediction = pd.read_csv(prediction_file, sep=',', header=None)
    ground_truth.columns = ['image', 'classes', 'x1', 'y1', 'x2', 'y2']
    prediction.columns = ['image', 'classes', 'x1', 'y1', 'x2', 'y2']
    ground_truth_df = pd.DataFrame(columns=['image', 'classes', 'x1', 'y1', 'x2', 'y2'])
    prediction_df = pd.DataFrame(columns=['image', 'classes', 'x1', 'y1', 'x2', 'y2'])
    for i in range(len(ground_truth)):
        ground_truth_df = ground_truth_df.append(ground_truth.iloc[i])
    for i in range(len(prediction)):
        prediction_df = prediction_df.append(prediction.iloc[i])
    ground_truth_df = ground_truth_df.reset_index(drop=True)
    prediction_df = prediction_df.reset_index(drop=True)
    classificationReport = classification_report(ground_truth_df['classes'], prediction_df['classes'])
    return classificationReport

# f1 score from ground_truth.csv and prediction.csv using sklearn.f1_score
def get_f1_score(ground_truth_file, prediction_file):
    ground_truth = pd.read_csv(ground_truth_file, sep=',', header=None)
    prediction = pd.read_csv(prediction_file, sep=',', header=None)
    ground_truth.columns = ['image', 'classes', 'x1', 'y1', 'x2', 'y2']
    prediction.columns = ['image', 'classes', 'x1', 'y1', 'x2', 'y2']
    ground_truth_df = pd.DataFrame(columns=['image', 'classes', 'x1', 'y1', 'x2', 'y2'])
    prediction_df = pd.DataFrame(columns=['image', 'classes', 'x1', 'y1', 'x2', 'y2'])            
    for i in range(len(ground_truth)):
        ground_truth_df = ground_truth_df.append(ground_truth.iloc[i])
    for i in range(len(prediction)):
        prediction_df = prediction_df.append(prediction.iloc[i])
    ground_truth_df = ground_truth_df.reset_index(drop=True)
    prediction_df = prediction_df.reset_index(drop=True)
    f1Score = f1_score(ground_truth_df['classes'], prediction_df['classes'], average='weighted')
    return f1Score

print("Confusion Matrix:")
print(get_confusion_matrix('ground_truth.csv', 'predictions.csv'))
print("Classification report:")
print(get_classification_report('ground_truth.csv', 'predictions.csv'))
# print("F1 score:")
# print(get_f1_score('ground_truth.csv', 'predictions.csv'))