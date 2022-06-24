import os
import numpy as np

def confusion_matrix(pred_output, gt, n_labels):
    lbl_count = n_labels * gt + pred_output
    print(lbl_count)
    count = np.bincount(lbl_count, minlength=n_labels** 2)
    conf_matrix = count.reshape(n_labels, n_labels)
    return conf_matrix


n_labels = 4 # we have 4 labels from 0 to 3
gt = np.array([0,0,1,1,2,2,3])
pred_output = np.array([1 ,0,1,1,2,1,2])
confusion_matrix(pred_output, gt, n_labels)


