from pycm import *
import numpy

y_actu = numpy.array([2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2])
y_pred = numpy.array([0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2])

cm = ConfusionMatrix(actual_vector=y_actu, predict_vector=y_pred) # Create CM From Data
print(cm.classes) # Print Classes
print(cm.table) # Print Confusion Matrix
print(cm)

cm.print_matrix() # Print Confusion Matrix
cm.print_normalized_matrix()

cm.print_matrix(one_vs_all=True,class_name=0)   # One-Vs-All, new in version 1.4

cm = ConfusionMatrix(y_actu, y_pred, classes=[1,0,2])  # classes, new in version 3.2
cm.print_matrix()

cm = ConfusionMatrix(y_actu, y_pred, classes=[1,0,4]) # classes, new in version 3.2
cm.print_matrix()


