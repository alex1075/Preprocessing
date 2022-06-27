# make confusion matrix 
#def confusion_matrix(pred_output, gt, n_labels):
#     lbl_count = n_labels * gt + pred_output
#     print(lbl_count)
#     count = np.bincount(lbl_count, minlength=n_labels** 2)
#     conf_matrix = count.reshape(n_labels, n_labels)
#     return conf_matrix
#
#
# n_labels = 5 # we have 4 labels from 0 to 3
# gt = np.loadtxt('ground_truth.txt', delimiter=' ', usecols=[1,2,3,4,5])
# pred_output = np.loadtxt('predicitons.txt', delimiter=' ', usecols=[1,2,3,4,5])
# confusion_matrix(pred_output, gt, n_labels)
#
#
