import io
import numpy as np
import decimal
from code.helper.annotations import *
from code.helper.utils import save_arrya_to_csv
import warnings
warnings.filterwarnings("ignore")

# n_labels = 5 # we have 4 labels from 0 to 3

gt = get_yolo_coordonates_txt_as_voc('ground_truth.txt', './')
pred_output = get_yolo_coordonates_txt_as_voc('predictons.txt', './')









# compare area of overlapp with bboxs and keep the best one from two lists using first item in list as comparator
# pred_new = []
pred_new = keep_only_best_overlapping_bboxes(gt, pred_output)
# pred_output.clear()
# for entry in pred_new:
#     pred_output.append(entry)



def make_individual_prediciton_txt(file, path):
    yolo_pt = []
    filoo = open(path + file, 'r')
    for line in filoo:
        # print(file)
        # print(line)
        lin = line.split(' ')
        # print(lin)
        image = lin[0]
        classes = lin[1]
        cent_x = float(lin[2])
        cent_y = float(lin[3])
        width = float(lin[4])
        height = float(lin[5][:-2])
        bbox = (cent_x, cent_y, width, height)
        f = io.open(image + '.txt', 'w')
        f.write(str(classes) + " " + str(cent_x) + " " + str(cent_y) + " " + str(width) + " " + str(height) +  '\n')
        f.close()

# make_individual_prediciton_txt('predictons.txt', './')



# remove_umnatched_gt(gt, pred_output)
print(gt)
# print(len(pred_output))
# print(pred_new)
save_arrya_to_csv(gt, './', 'ground_truth.csv')
save_arrya_to_csv(pred_new, './', 'predictions.csv')



