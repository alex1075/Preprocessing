import numpy as np
import re
import progressbar
import time

def bb_intersection_over_union(boxA, boxB):
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    # compute the area of intersection rectangle
    # interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
    interArea = max(0, abs(xB - xA + 1)) * max(0, abs(yB - yA + 1))
    # print(interArea)
    # compute the area of both the prediction and ground-truth
    # rectangles
    boxAArea = abs(boxA[2] - boxA[0] + 1) * abs(boxA[3] - boxA[1] + 1)
    boxBArea = abs(boxB[2] - boxB[0] + 1) * abs(boxB[3] - boxB[1] + 1)
    # print(boxAArea)
    # print(boxBArea)
    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = interArea / float(boxAArea + boxBArea - interArea)

    # return the intersection over union value
    return iou

def bb_iou(boxA, boxB):
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    # compute the area of intersection rectangle
    interArea = (xB - xA) * (yB - yA)
    interArea = abs(interArea)
    # compute the area of both the prediction and ground-truth
    # rectangles
    boxAArea = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    boxBArea = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])
    boxAArea = abs(boxAArea)
    boxBArea = abs(boxBArea)
    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    if float(boxAArea + boxBArea - interArea) == 0:
        iou = 0
    else:
        iou = interArea / float(boxAArea + boxBArea - interArea)
        iou = abs(iou)

    # return the intersection over union value
    return iou

def get_iou(ground_truth, pred):
    # coordinates of the area of intersection.
    ix1 = np.maximum(ground_truth[0], pred[0])
    iy1 = np.maximum(ground_truth[1], pred[1])
    ix2 = np.minimum(ground_truth[2], pred[2])
    iy2 = np.minimum(ground_truth[3], pred[3])
    
    # Intersection height and width.
    i_height = np.maximum(iy2 - iy1 + 1, np.array(0.))
    print(i_height)
    i_width = np.maximum(ix2 - ix1 + 1, np.array(0.))
    print(i_width)
    
    area_of_intersection = i_height * i_width
    print(area_of_intersection)
    
    # Ground Truth dimensions.
    gt_height = ground_truth[3] - ground_truth[1] + 1
    print(gt_height)
    gt_width = ground_truth[2] - ground_truth[0] + 1
    print(gt_width)
    
    # Prediction dimensions.
    pd_height = pred[3] - pred[1] + 1
    print(pd_height)
    pd_width = pred[2] - pred[0] + 1
    print(pd_width)
    
    area_of_union = gt_height * gt_width + pd_height * pd_width - area_of_intersection
    print(area_of_union)
    
    iou = area_of_intersection / area_of_union
    print(iou)
    
    return iou

SMOOTH = 1e-6

def iou_numpy(outputs: np.array, labels: np.array):
      outputs = outputs.squeeze(1)

      intersection = (outputs & labels).sum((1, 2))
      union = (outputs | labels).sum((1, 2))

      iou = (intersection + SMOOTH) / (union + SMOOTH)

      thresholded = np.ceil(np.clip(20 * (iou - 0.5), 0, 10)) / 10

      return thresholded  # Or thresholded.mean()

# iterate over boubding boxes in grounth_truth.txt and filtered_results.txt
# and calculate the iou for each pair of boxes
# if the iou is greater than 0.5, the box is considered a true positive
def calculate_iou():
    gt = open("gt.txt", "r")
    gt_lines = len(gt.readlines())
    fr = open("filtered_pd.txt", "r")
    fr_lines = len(fr.readlines())
    gt = open("gt.txt", "r")
    fr = open("filtered_results.txt", "r")
    print(gt_lines)
    print(fr_lines)
    true_positives = 0
    false_positives = 0
    for line in fr:
        lin = line.split()
        # print(lin)
        for line in gt:
            fr = line.split()
            
            # print(fr[:-1])
            # print(lin[0])
            # print(fr[0])
            if lin[0] == fr[0]:
                print("match")
                # print(lin[0])
                # print(fr[0])
                li = [int(lin[2]), int(lin[3]), int(lin[4]), int(lin[5])]
                fi = [int(fr[2]), int(fr[3]), int(fr[4]), int(fr[5])]
                iou = bb_intersection_over_union(li, fi)
                print(iou)
                if iou > 0.5:
                    true_positives += 1
                    print(True)
                else:
                    false_positives += 1
                    print(False)
            else:
                # print("no match")
                pass
    print('True positives: ', true_positives)
    print('False positives: ', false_positives)

def neo_calculate_iou():
    gt = open("gt.txt", "r")
    fr = open("filtered_pd.txt", "r")
    gt_lines = len(gt.readlines())
    fr_lines = len(fr.readlines())
    print(gt_lines)
    print(fr_lines)
    print(gt_lines * fr_lines)
    ground = []
    filtered = []
    true_positives = 0
    false_positives = 0
    for line in fr:
        lin = line.split()
        filtered.append(lin)
    for line in gt:
        fr = line.split()
        ground.append(fr)
    matches = 0
    for i in filtered:
        # print(i[0])
        for j in ground:
            # print(j[0])
            # print(lin[0])
            # print(fr[0])
            if i[0] == j[0]:
                # print(lin[0])
                # print(fr[0])
                # print("match")
                matches += 1
                li = [int(i[2]), int(i[3]), int(i[4]), int(i[5])]
                fi = [int(j[2]), int(j[3]), int(j[4]), int(j[5])]
                # print(li)

                # print(fi)
                iou = bb_intersection_over_union(li, fi)
                if iou > 0.5:
                    true_positives += 1
                #     print(True)
                else:
                    false_positives += 1
                    # print(False)
            else:
                # print("no match")
                pass
    print('True positives: ', true_positives)
    print('False positives: ', false_positives)
    print('Matches: ', matches)
    print(true_positives + false_positives)
    # print(matches)

def new_calculate_iou():
    gt = open("gt.txt", "r")
    fr = open("filtered_pd.txt", "r")
    gt_lines = len(gt.readlines())
    fr_lines = len(fr.readlines())
    print(gt_lines)
    print(fr_lines)
    total_count = gt_lines * fr_lines
    print(gt_lines * fr_lines)
    gt = open("gt.txt", "r")
    fr = open("filtered_pd.txt", "r")
    ground = []
    filtered = []
    true_positives = 0
    false_positives = 0
    count = 0
    for line in fr:
        lin = line.split()
        filtered.append(lin)
    for line in gt:
        fr = line.split()
        ground.append(fr)
    matches = 0
    widgets = [' [',
         progressbar.Timer(format= 'elapsed time: %(elapsed)s'),
         '] ',
           progressbar.Bar('/'),' (',
           progressbar.ETA(), ') ',
          ]
    bar = progressbar.ProgressBar(max_value=543150, 
                              widgets=widgets).start()
    for i in filtered:
        # print(i[0])
        count += 1
        for j in ground:
            count += 1
            if re.search('|'.join(j), i[0]):
                # print("match")
                matches += 1
                bar.update(count)
                li = [int(i[2]), int(i[3]), int(i[4]), int(i[5])]
                fi = [int(j[2]), int(j[3]), int(j[4]), int(j[5])]
                # print(li)

                # print(fi)
                iou = bb_iou(li, fi)
                # print(iou)
                if iou > 0.75:
                    true_positives += 1
                #     print(True)
                else:
                    false_positives += 1
                    # print(False)
            else:
                # print("no match")
                pass
    print('True positives: ', true_positives)
    print('False positives: ', false_positives)
    print('Matches: ', matches)
    print(true_positives + false_positives)
    # print(matches)


if __name__ == '__main__':
    # calculate_iou()
    new_calculate_iou()