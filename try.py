# make confusion matrix from ground truth and prediction   file 

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




def get_confusion_matrix(ground_truth_file, prediction_file):
    ground_truth = pd.read_csv(ground_truth_file, sep=' ', header=None)
    prediction = pd.read_csv(prediction_file, sep=' ', header=None)
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
    


