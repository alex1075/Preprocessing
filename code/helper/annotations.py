from code.helper.rectangle import *
import numpy as np
import pybboxes as pbx
import decimal


def get_yolo_coordonates_txt_as_voc(file, path): 
    """Requires a txt file with a list of images, classes, cent_x, cent_y, width, height
    Returns a array of arrays with the coordinates converted to voc format assumining the 
    image size is 416x416 pixels wide"""
    annotations = []
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
        # print(bbox)
        try:
            yolo = pbx.convert_bbox(bbox, from_type="yolo", to_type="voc", image_size=(416, 416), strict=False)
            x1, y1, x2, y2 = yolo
            if x1 < 0 or y1 < 0 or x2 > 416 or y2 > 416:
                # print('Error: bbox out of range')
                continue
            # print(x1, y1, x2, y2)
            annotations.append([image, classes, x1, y1, x2, y2])
        except ValueError:
            print("ValueError, box is not in the image. Passed")
            pass
    # print (yolo_gt)
    return annotations
    

def keep_only_overlapping_bboxes(gt, pred_output):
    """Pass two arrays of arrays, 
    gt => ground truth
    pred_output => prediction output
    Checks if the bboxes are overlapping, if not, remove the bbox from the prediction output
    """
    for entry in gt: 
        for entry2 in pred_output:
            if entry[0] == entry2[0]:
                if overlap((entry[2], entry[3], entry[4], entry[5]), (entry2[2], entry2[3], entry2[4], entry2[5])) is False:
                    # print('Error: bboxs are not overlapping')
                    # print(entry)
                    # print(entry2)
                    pred_output.remove(entry2)
                else:
                    # print('Bboxs are overlapping')
                    # print(entry)
                    # print(entry2)
                    pass

def keep_only_best_overlapping_bboxes(gt, pred_output):
    """Pass two arrays of arrays, 
    gt => ground truth
    pred_output => prediction output
    Checks if the bboxes are overlapping using the image as point to compare from, 
    then selects the best bbox from pred_output to keep for each annotation and 
    returns a array of arrays with the coordinates
    """
    compare_areas = []
    new_pred_list = []
    for instance in gt:
        for pred in pred_output:
            print(pred)
            if instance[0] == pred[0]:
                ov_aread = overlap_area((instance[2], instance[3], instance[4], instance[5]), (pred[2], pred[3], pred[4], pred[5]))
                compare_areas.append([ov_aread, pred])
            else:
                print(compare_areas)
                if any(compare_areas) is True:
                    print('True')
                    compare_areas.sort(key=lambda x: x[0], reverse=True)
                    item = compare_areas[0]
                    it = item[1]
                    print(item[1:])
                    print([it])
                    new_pred_list.append(it)
                compare_areas.clear()
    print(pred)
    new_pred_list.append(pred_output)
    print("Ground truth length:" + str(len(gt)))
    print("Prediction length:" + str(len(pred_output)))
    print("New prediction length:" + str(len(new_pred_list)))
    return new_pred_list