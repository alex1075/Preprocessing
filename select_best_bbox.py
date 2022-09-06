import os 
import cv2
import numpy as np
import decimal

def select_best_bbox(list_file, width=416, height=416):
    fill = open(list_file, 'r')
    bbox_list = []
    confidence_list = []
    for line in fill:
        # print(file)
        # print(line)
        lin = line.split(' ')
        # print(lin)
        image = lin[0]
        classes = str(lin[1])
        x1 = decimal.Decimal(lin[2])
        y1 = decimal.Decimal(lin[3])
        x2 = decimal.Decimal(lin[4])
        y2 = decimal.Decimal(lin[5])
        scores = float(decimal.Decimal(float(lin[6]*100)))
        x1 = decimal.Decimal(x1 * 416)
        y1 = decimal.Decimal(y1 * 416)
        x2 = decimal.Decimal(x2 * 416)
        y2 = decimal.Decimal(y2 * 416)
        x1 = round(x1)
        y1 = round(y1)
        x2 = round(x2)
        y2 = round(y2)
        # print(x1, y1, x2, y2)
        classId = np.argmax(scores)
        confidence = scores[classId]
        bbox_list.append((x1, y1, x2, y2))
        confidence_list.append(str(confidence))
    print(bbox_list)
    print(confidence_list)
    cv2.dnn.NMSBoxes(bbox_list, confidence, 0.5, 0.3)


if __name__ == '__main__':
    list_file = 'predictons.txt'
    select_best_bbox(list_file)