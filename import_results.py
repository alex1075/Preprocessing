import os
import re
import cv2
import numpy as np
import decimal
import matplotlib.pyplot as plt
from add_bbox import *

# Import the results from the results.txt file
def import_results(input_file='result.txt', results_file='results.txt'):
    res = open(results_file, 'w')
    with open(input_file, 'r') as f:
        for line in f:
            if line[0:4] == '/hom':
                lin = re.split('/| ', line)
                li = filter(lambda a: '.jpg' in a, lin)
                l = list(li)[0][:-5]
                print(l)
                image_name = l
            elif line[0:4] == 'ERY:':
                lin = re.split(':|%|t|w|h', line)
                # print(lin)
                classes = 1
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
                # print(res)
                bottom_y = top_y + height
                right_x = left_x + width
                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100) + ' \n')
            elif line[0:4] == 'ECHY':
                lin = re.split(':|%|t|w|h', line)
                # print(lin)
                classes = 0
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
                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100) + ' \n')                # print(res)
            elif line[0:4] == 'PLT:':
                lin = re.split(':|%|t|w|h', line)
                # print(lin)
                classes = 2
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
                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100) + ' \n')                # print(res)    
            elif line[0:4] == 'SIDE':
                lin = re.split(':|%|t|w|h', line)
                # print(lin)
                classes = 3
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
                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100) + ' \n')                # print(res)    
            elif line[0:4] == 'WBC:':
                lin = re.split(':|%|t|w|h', line)
                # print(lin)
                classes = 4
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
                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100) + ' \n')                # print(res)
            else:
                pass

def import_results_2(input_file='result.txt', results_file='results.txt'):
    res = open(results_file, 'w')
    with open(input_file, 'r') as f:
        for line in f:
            if line[0:4] == '/hom':
                lin = re.split('/| ', line)
                li = filter(lambda a: '.jpg' in a, lin)
                l = list(li)[0][:-5]
                print(l)
                image_name = l
            elif line[0:4] == 'ERY:':
                lin = re.split(':|%|t|w|h', line)
                # print(lin)
                classes = 1
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
                # print(res)
                bottom_y = top_y + height
                right_x = left_x + width
                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100) + ' \n')            
            elif line[0:4] == 'ECHY':
                lin = re.split(':|%|t|w|h', line)
                # print(lin)
                classes = 0
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
                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100) + ' \n')                # print(res)
            elif line[0:4] == 'PLT:':
                lin = re.split(':|%|t|w|h', line)
                # print(lin)
                classes = 5
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
                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100) + ' \n')                # print(res)    
            elif line[0:4] == 'LYM:':
                lin = re.split(':|%|t|w|h', line)
                # print(lin)
                classes = 2
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
                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100) + ' \n')                # print(res)    
            elif line[0:4] == 'MON:':
                lin = re.split(':|%|t|w|h', line)
                # print(lin)
                classes = 3
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
                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100) + ' \n')                # print(res)
            elif line[0:4] == 'NEU:':
                lin = re.split(':|%|t|w|h', line)
                # print(lin)
                classes = 4
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
                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100) + ' \n')                # print(res)
            else:
                pass

def import_results_leuko(input_file='result.txt', results_file='results.txt'):
    res = open(results_file, 'w')
    with open(input_file, 'r') as f:
        for line in f:
            if line[0:4] == '/hom':
                lin = re.split('/| ', line)
                li = filter(lambda a: '.jpg' in a, lin)
                l = list(li)[0][:-5]
                # print(l)
                image_name = l
            elif line[0:4] == 'LYM:':
                lin = re.split(':|%|t|w|h', line)
                # print(lin)
                classes = 0
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
                # print(res)
                bottom_y = top_y + height
                right_x = left_x + width
                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100) + ' \n')
            elif line[0:4] == 'MON:':
                lin = re.split(':|%|t|w|h', line)
                # print(lin)
                classes = 1
                confidence = int((lin[1]))
                if int(lin[4]) < 0:
                    left_x = 1
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
                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100) + ' \n')                # print(res)
            elif line[0:4] == 'NEU:':
                lin = re.split(':|%|t|w|h', line)
                # print(lin)
                classes = 2
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
                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100) + ' \n')                # print(res) 
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


def cleanup(file):
    lines_seen = set() # holds lines already seen
    with open(file, 'r+') as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i not in lines_seen:
                f.write(i)
                lines_seen.add(i)
        f.truncate()

def import_and_filder_results(input_file='/home/as-hunt/result.txt', results_file='results.txt'): 
      res = open(results_file, 'w')
      with open(input_file, 'r') as f:
        for line in f:
            if line[0:4] == '/hom':
                lin = re.split('/| ', line)
                li = filter(lambda a: '.jpg' in a, lin)
                l = list(li)[0][:-5]
                # print(l)
                image_name = l
            elif line[0:4] == 'ERY:':
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
                        classes = 1
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
            elif line[0:4] == 'ECHY':
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
                        # print(lin)
                        classes = 0
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
            elif line[0:4] == 'PLT:':
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
                        classes = 2
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
            elif line[0:4] == 'WBC:':
                lin = re.split(':|%|t|w|h', line)
                if int(lin[4]) < 4:
                    # pass
                    pass
                elif int(lin[4]) > 412:
                    pass
                else:
                    if int(lin[6]) < 4:
                        pass
                    elif int(lin[6]) > 412:
                        pass
                    else:
                        # print(lin)
                        classes = 3
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
                                pass
                                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100) + ' \n')                    
            else:
                pass



def import_and_filder_results_3(input_file='/home/as-hunt/result.txt', results_file='results.txt'): 
      res = open(results_file, 'w')
      with open(input_file, 'r') as f:
        for line in f:
            if line[0:4] == '/hom':
                lin = re.split('/| ', line)
                li = filter(lambda a: '.jpg' in a, lin)
                l = list(li)[0][:-5]
                # print(l)
                image_name = l
            elif line[0:4] == 'ERY:':
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
                        classes = 1
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
            elif line[0:4] == 'ECHY':
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
                        # print(lin)
                        classes = 0
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
            elif line[0:4] == 'PLT:':
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
                        classes = 2
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
                pass



# Run the import_and_filder_results function
# import_and_filder_results()

def second_stage_NMS(predictions_file):
    comparators = []
    save = []
    with open(predictions_file, 'r') as file:
        for line in file:
            li = line.split(' ')
            image = li[0]
            classes = str(li[1])
            x1 = str(li[2])
            y1 = str(li[3])
            x2 = str(li[4])
            y2 = str(li[5])
            confidence = li[6]
            comparators.append([image + ',' + classes +',' + str(x1) +',' +str(y1) +',' + str(x2) +',' + str(y2) + ',' +confidence])
    print(comparators)
    for item in comparators:
        print(item)
        with open(predictions_file, 'r+') as file:
            for line in file:
                li = line.split(' ')
                image = li[0]
                classes = str(li[1])
                x1 = str(li[2])
                y1 = str(li[3])
                x2 = str(li[4])
                y2 = str(li[5])
                confidence = li[6]
                if item[0] == image:
                    bbox1 = item[2:5]
                    bbox2 = li[2:5]
                    if iou(bbox1, bbox2) <= 0.9:
                        if confidence > item[6]:
                            save.append(image + ' ' + classes + ' ' + x1 + ' ' + y1 + ' ' + x2 + ' ' + y2 + ' ' + confidence)
                        elif confidence < item[6]:
                            save.append(item[0] + ' ' + item[1] + ' ' + item[2] + ' ' + item[3] + ' ' + item[4] + ' ' + item[5] + ' ' + item[6])
                        elif confidence == item[6]:
                            save.append(item[0] + ' ' + item[1] + ' ' + item[2] + ' ' + item[3] + ' ' + item[4] + ' ' + item[5] + ' ' + item[6])
                    else:
                        pass
    print(save)
    
def import_and_filder_result_2(input_file='/home/as-hunt/result.txt', results_file='results.txt'):
    res = open(results_file, 'w')
    with open(input_file, 'r') as f:
        for line in f:
            if line[0:4] == '/hom':
                lin = re.split('/| ', line)
                li = filter(lambda a: '.jpg' in a, lin)
                l = list(li)[0][:-5]
                # print(l)
                image_name = l
            elif line[0:4] == 'ERY:':
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
                        classes = 1
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
            elif line[0:4] == 'ECHY':
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
                        # print(lin)
                        classes = 0
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
            elif line[0:4] == 'PLT:':
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
                        classes = 5
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
            elif line[0:4] == 'LYM:':
                lin = re.split(':|%|t|w|h', line)
                if int(lin[4]) < 4:
                    # pass
                    pass
                elif int(lin[4]) > 412:
                    pass
                else:
                    if int(lin[6]) < 4:
                        pass
                    elif int(lin[6]) > 412:
                        pass
                    else:
                        # print(lin)
                        classes = 2
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
                                pass
                                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100) + ' \n')                    
            elif line[0:4] == 'MON:':
                lin = re.split(':|%|t|w|h', line)
                if int(lin[4]) < 4:
                    # pass
                    pass
                elif int(lin[4]) > 412:
                    pass
                else:
                    if int(lin[6]) < 4:
                        pass
                    elif int(lin[6]) > 412:
                        pass
                    else:
                        # print(lin)
                        classes = 3
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
            elif line[0:4] == 'NEU:':
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
                        # print(lin)
                        classes = 4
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

import_results_2('/home/as-hunt/Etra-Space/differential/result.txt', '/home/as-hunt/Etra-Space/differential/results.txt')