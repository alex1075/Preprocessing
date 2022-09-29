import os 
import cv2
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
        scores = float((lin[6]))
        x1 = decimal.Decimal(x1 * 416)
        y1 = decimal.Decimal(y1 * 416)
        x2 = decimal.Decimal(x2 * 416)
        y2 = decimal.Decimal(y2 * 416)
        x1 = round(x1)
        y1 = round(y1)
        x2 = round(x2)
        y2 = round(y2)
        # print(x1, y1, x2, y2)
        bbox_list.append((x1, y1, x2, y2))
        confidence_list.append(scores)
    print(bbox_list)
    print(confidence_list)
    selected = cv2.dnn.NMSBoxes(bbox_list, confidence_list, 0.5, 0.3)
    # keep bbox using selected as index
    kept_bbox = []
    kept_confidence = []
    print(selected)
    for i in selected:
        i 
        print(i)
        kept_bbox.append(bbox_list[i])
        kept_confidence.append(confidence_list[i])
    print(kept_bbox)
    print(kept_confidence)
    # write to file
    with open('best_bbox.txt', 'w') as f:
        for i in range(len(kept_bbox)):
            f.write(image + ' ' + classes + ' ' + str(kept_bbox[i][0]) + ' ' + str(kept_bbox[i][1]) + ' ' + str(kept_bbox[i][2]) + ' ' + str(kept_bbox[i][3]) + ' ' + str(kept_confidence[i]) + '\n')


if __name__ == '__main__':
    list_file = 'predictions.txt'
    select_best_bbox(list_file)

# use cv2.dnn.NMSBoxes to select the best bounding box
    
