import os
import re
import cv2
import numpy as np
import decimal
import matplotlib.pyplot as plt
from add_bbox import *

# Import the results from the results.txt file
def import_and_filter_result_neo(input_file='/home/as-hunt/result.txt', results_file='results.txt', obj_names='/home/as-hunt/Etra-Space/white-thirds/obj.names'):
    '''Import's Yolo darknet detection results bouding boxes.

    This function does filters the result.txt file. 
    It removes bouding boxes that are outside the image and
    bouding boxes that are too close to the edge of the image.

      Args:
        input_file (str): The path to the results.txt file
        results_file (str): The path to the file to save the filtered results
        obj_names (str): The path to the obj.names file
        '''
    arry = []
    res = open(results_file, 'w')
    with open(obj_names, 'r') as f:
        for line in f:
            arry.append(line.rstrip())
    with open(input_file, 'r') as f:
        for line in f:
            if line[0:4] == '/hom':
                lin = re.split('/| ', line)
                li = filter(lambda a: '.jpg' in a, lin)
                l = list(li)[0][:-5]
                image_name = l
            elif (line[0:3] in arry) or (line[0:4] in arry ) == True:
                lin = re.split(':|%|t|w|h', line)
                if int(lin[4]) < 4:
                    pass
                elif int(lin[4]) > 412:
                    pass
                else:
                    if int(lin[6]) < 4:
                        pass
                    elif int(lin[6]) > 412:
                        pass
                    else:
                        classes = int(arry.index(lin[0]))
                        confidence = int((lin[1]))
                        if int(lin[4]) < 0:
                            left_x = 0
                        else:
                            left_x = int(lin[4])
                        if int(lin[6]) < 0:
                            top_y = 0
                        else:
                            top_y = int(lin[6])
                        width = int(lin[10])
                        height = int(lin[14][:-2])
                        bottom_y = top_y + height
                        right_x = left_x + width
                        if bottom_y < 0:
                            bottom_y = 0
                        if right_x > 416:
                            right_x = 416
                        if bottom_y < 4:
                            pass
                        elif bottom_y > 412:
                            pass
                        else:
                            if right_x > 412:
                                pass
                            elif right_x < 4:
                                pass
                            else:
                                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100) + ' \n')
            else:
                pass       

def import_results_neo(input_file='result.txt', results_file='results.txt', obj_names='/home/as-hunt/Etra-Space/white-thirds/obj.names'):
    '''Import's Yolo darknet detection results and filters bouding boxes that are outside of the image dimensions
    This function will use the index given to darknet when training the model to determine the class of the object
    
    Args:
        input_file (str): The path to the results file
        results_file (str): The path to the output file
        obj_names (str): The path to the obj.names file
        '''
    arry = []
    res = open(results_file, 'w')
    with open(obj_names, 'r') as f:
        for line in f:
            arry.append(line.rstrip())
    with open(input_file, 'r') as f:
        for line in f:
            if line[0:4] == '/hom':
                lin = re.split('/| ', line)
                li = filter(lambda a: '.jpg' in a, lin)
                l = list(li)[0][:-5]
                image_name = l
            elif (line[0:3] in arry) or (line[0:4] in arry ) == True:
                print(line[0:3])
                lin = re.split(':|%|t|w|h', line)
                classes = int(arry.index(lin[0]))
                confidence = int((lin[1]))
                if int(lin[4]) < 0:
                    left_x = 0
                else:
                    left_x = int(lin[4])
                if int(lin[6]) < 0:
                    top_y = 0
                else:
                    top_y = int(lin[6])
                width = int(lin[10])
                height = int(lin[14][:-2])
                bottom_y = top_y + height
                right_x = left_x + width
                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100) + ' \n')          
            else:
                pass             

def make_groud_truth(ground_truth_file='gt.txt', test_folder='/home/as-hunt/Etra-Space/new_data_sidless/valid/'):
    gt_file = open(ground_truth_file, 'w')
    for file in os.listdir(test_folder):
        if file.endswith('.txt'):
            if file == 'test.txt':
                pass
            elif file == 'classes.txt':
                pass
            elif file == 'train.txt':
                pass
            elif file == 'valid.txt':
                pass
            elif file == 'ground_truth.txt':
                pass
            elif file == 'result_run_1.txt':
                pass
            elif file == 'result_run_2.txt':
                pass
            else:
                img_name = file[:-4] 
                count = 0
                annot = open(test_folder + file, 'r+')
                for line in annot:
                    lin = re.split(' ', line)
                    # print(lin[1])
                    classes = lin[0]
                    center_x = lin[1]
                    center_y = lin[2]
                    width = lin[3]
                    height = lin[4]
                    if center_x == '0':
                        # print('center_x ('+ center_x +') is 0')
                        pass
                    elif center_y == '0':
                        # print('center_x ('+ center_y +') is 0')
                        pass
                    elif width == '0':
                        # print('widht ('+ width +') is 0')
                        pass
                    elif height == '0':
                        # print('height ('+ height +') is 0')
                        pass
                    else:
                        center_x = decimal.Decimal(center_x) * 416
                        center_y = decimal.Decimal(center_y) * 416
                        width = decimal.Decimal(width) * 416
                        height = decimal.Decimal(height) * 416
                        left_x = int(decimal.Decimal(center_x) - (width / 2))
                        top_y = int(decimal.Decimal(center_y) - (height / 2))
                        right_x = int(decimal.Decimal(center_x) + (width / 2))
                        bottom_y = int(decimal.Decimal(center_y) + (height / 2))
                        if left_x <= 6:
                            # print('left_x (' + str(left_x) + ') is less than 6')
                            pass
                        elif left_x >= 410:
                            # print('left_x (' + str(left_x) + ') is greater than 410')
                            pass
                        else:
                            if top_y <= 6:
                                # print('top_y (' + str(top_y) + ') is less than 6')
                                pass
                            elif top_y >= 410:
                                print('top_y (' + str(top_y) + ') is greater than 410')
                                pass
                            else:
                                if right_x <= 6:
                                    print('right_x (' + str(right_x) + ') is less than 6')
                                    pass
                                elif right_x >= 410:
                                    print('right_x (' + str(right_x) + ') is greater than 410')
                                    pass
                                else:
                                    if bottom_y <= 6:
                                        print('bottom_y (' + str(bottom_y) + ') is less than 6')
                                        pass
                                    elif bottom_y >= 410:
                                        print('bottom_y (' + str(bottom_y) + ') is greater than 410')
                                        pass
                                    else:
                                        gt_file.write(img_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' \n')
                                        count += 1
                                        # print('Line ' + str(count) + ': ' + img_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y))   

def make_groud_truth_unfiltered(ground_truth_file='gt.txt', test_folder='/home/as-hunt/Etra-Space/new_data_sidless/valid/'):
    gt_file = open(ground_truth_file, 'w')
    for file in os.listdir(test_folder):
        if file.endswith('.txt'):
            if file == 'test.txt':
                pass
            elif file == 'classes.txt':
                pass
            elif file == 'train.txt':
                pass
            elif file == 'valid.txt':
                pass
            elif file == 'ground_truth.txt':
                pass
            elif file == 'result_run_1.txt':
                pass
            elif file == 'result_run_2.txt':
                pass
            else:
                img_name = file[:-4] 
                count = 0
                annot = open(test_folder + file, 'r+')
                for line in annot:
                    lin = re.split(' ', line)
                    # print(lin[1])
                    classes = lin[0]
                    center_x = lin[1]
                    center_y = lin[2]
                    width = lin[3]
                    height = lin[4]
                    if center_x == '0':
                        # print('center_x ('+ center_x +') is 0')
                        pass
                    elif center_y == '0':
                        # print('center_x ('+ center_y +') is 0')
                        pass
                    elif width == '0':
                        # print('widht ('+ width +') is 0')
                        pass
                    elif height == '0':
                        # print('height ('+ height +') is 0')
                        pass
                    else:
                        center_x = decimal.Decimal(center_x) * 416
                        center_y = decimal.Decimal(center_y) * 416
                        width = decimal.Decimal(width) * 416
                        height = decimal.Decimal(height) * 416
                        left_x = int(decimal.Decimal(center_x) - (width / 2))
                        top_y = int(decimal.Decimal(center_y) + (height / 2))
                        right_x = int(decimal.Decimal(center_x) + (width / 2))
                        bottom_y = int(decimal.Decimal(center_y) - (height / 2))
                        gt_file.write(img_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' \n')
                        count += 1
                        # print('Line ' + str(count) + ': ' + img_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y))   


def count_classes(test_folder='/home/as-hunt/Etra-Space/new_data_sidless/valid/', chart=False, chart_name='chart.png', labs=['1', '2', '3']):
    class_1 = 0
    class_2 = 0
    class_3 = 0
    class_4 = 0
    class_5 = 0
    class_6 = 0
    for file in os.listdir(test_folder):
        if file.endswith('.txt'):
            if file == 'test.txt':
                pass
            elif file == 'classes.txt':
                pass
            elif file == 'train.txt':
                pass
            elif file == 'valid.txt':
                pass
            elif file == 'ground_truth.txt':
                pass
            elif file == 'result_run_1.txt':
                pass
            elif file == 'result_run_2.txt':
                pass
            elif file == '_darknet.labels':
                pass
            else:
                img_name = file[:-4] 
                count = 0
                annot = open(test_folder + file, 'r+')
                for line in annot:
                    lin = re.split(' ', line)
                    # print(lin[1])
                    classes = lin[0]
                    if classes == '0':
                        class_1 += 1
                    elif classes == '1':
                        class_2 += 1
                    elif classes == '2':
                        class_3 += 1
                    elif classes == '3':
                        class_4 += 1
                    elif classes == '4':
                        class_5 += 1
                    elif classes == '5':
                        class_6 += 1
    print('class_1: ' + str(class_1))
    print('class_2: ' + str(class_2))
    print('class_3: ' + str(class_3))
    print('class_4: ' + str(class_4))
    print('class_5: ' + str(class_5))
    print('class_6: ' + str(class_6))
    if chart == True:
        labels = labs
        plt.figure(figsize = (10,7))
        plt.title(chart_name[:-4])
        if len(labels) == 2:
            count = [class_1, class_2]
            fig, ax = plt.subplots()
            ax.pie(count, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        elif len(labels) == 3:
            count = [class_1, class_2, class_3]
            fig, ax = plt.subplots()
            ax.pie(count, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        elif len(labels) == 4:
            count = [class_1, class_2, class_3, class_4]
            fig, ax = plt.subplots()
            ax.pie(count, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        elif len(labels) == 5:
            count = [class_1, class_2, class_3, class_4, class_5]
            fig, ax = plt.subplots()
            ax.pie(count, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        elif len(labels) == 6:
            count = [class_1, class_2, class_3, class_4, class_5, class_6]
            fig, ax = plt.subplots()
            ax.pie(count, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.savefig(chart_name, bbox_inches='tight')    

count_classes(test_folder='/mnt/archive/new_data_sidless_no_rcc_1/train/', chart=False)


def count_classes_file(test_file='/home/as-hunt/Etra-Space/new_data_sidless/gt.txt', chart=False, chart_name='chart.png', labs=['1', '2', '3']):
    class_1 = 0
    class_2 = 0
    class_3 = 0
    class_4 = 0
    class_5 = 0
    class_6 = 0
    count = 0
    annot = open(test_file, 'r+')
    for line in annot:
       lin = re.split(' ', line)
       # print(lin[1])
       classes = lin[1]
       if classes == '0':
          class_1 += 1
       elif classes == '1':
          class_2 += 1
       elif classes == '2':
          class_3 += 1
       elif classes == '3':
          class_4 += 1
       elif classes == '4':
          class_5 += 1
       elif classes == '5':
          class_6 += 1
    print('class_1: ' + str(class_1))
    print('class_2: ' + str(class_2))
    print('class_3: ' + str(class_3))
    print('class_4: ' + str(class_4))
    print('class_5: ' + str(class_5))
    print('class_6: ' + str(class_6))
    if chart == True:
        labels = labs
        plt.figure(figsize = (10,7))
        plt.title(chart_name[:-4])
        if len(labels) == 2:
            count = [class_1, class_2]
            fig, ax = plt.subplots()
            ax.pie(count, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        elif len(labels) == 3:
            count = [class_1, class_2, class_3]
            fig, ax = plt.subplots()
            ax.pie(count, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        elif len(labels) == 4:
            count = [class_1, class_2, class_3, class_4]
            fig, ax = plt.subplots()
            ax.pie(count, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        elif len(labels) == 5:
            count = [class_1, class_2, class_3, class_4, class_5]
            fig, ax = plt.subplots()
            ax.pie(count, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        elif len(labels) == 6:
            count = [class_1, class_2, class_3, class_4, class_5, class_6]
            fig, ax = plt.subplots()
            ax.pie(count, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.savefig(chart_name, bbox_inches='tight')    


