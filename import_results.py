import os
import re
import cv2
import numpy as np
import decimal

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
                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(width) + ' ' + str(height) + ' ' + str(confidence / 100) + ' \n')
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
                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(width) + ' ' + str(height) + ' ' + str(confidence / 100) + ' \n')
                # print(res)
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
                annot = open(test_folder + file, 'r')
                for line in annot:
                    lin = re.split(' ', line)
                    print(lin[1])
                    classes = lin[0]
                    center_x = lin[1]
                    center_y = lin[2]
                    width = lin[3]
                    height = lin[4]
                    if center_x == '0':
                        print('center_x ('+ center_x +') is 0')
                    elif center_y == '0':
                        print('center_x ('+ center_y +') is 0')
                    elif width == '0':
                        print('widht ('+ width +') is 0')
                    elif height == '0':
                        print('height ('+ height +') is 0')
                    else:
                        center_x = decimal.Decimal(center_x) * 416
                        center_y = decimal.Decimal(center_y) * 416
                        width = decimal.Decimal(width) * 416
                        height = decimal.Decimal(height) * 416
                        left_x = int(decimal.Decimal(center_x) - (width / 2))
                        top_y = int(decimal.Decimal(center_y) + (height / 2))
                        right_x = int(decimal.Decimal(center_x) + (width / 2))
                        bottom_y = int(decimal.Decimal(center_y) - (height / 2))
                        if left_x <= 6:
                            print('left_x (' + str(left_x) + ') is less than 6')
                        elif left_x >= 410:
                            print('left_x (' + str(left_x) + ') is greater than 410')
                        else:
                            if top_y <= 6:
                                print('top_y (' + str(top_y) + ') is less than 6')
                            elif top_y >= 410:
                                print('top_y (' + str(top_y) + ') is greater than 410')
                            else:
                                if right_x <= 6:
                                    print('right_x (' + str(right_x) + ') is less than 6')
                                elif right_x >= 410:
                                    print('right_x (' + str(right_x) + ') is greater than 410')
                                else:
                                    if bottom_y <= 6:
                                        print('bottom_y (' + str(bottom_y) + ') is less than 6')
                                    elif bottom_y >= 410:
                                        print('bottom_y (' + str(bottom_y) + ') is greater than 410')
                                    else:
                                        gt_file.write(img_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' \n')
                                        count += 1
                                        print('Line ' + str(count) + ': ' + img_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y))   
                annot.close()
    gt_file.close()

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
                if int(lin[4]) <= 6:
                    # pass
                    print('Error: left_x (' + str(lin[4]) + ') is less than 6')
                elif int(lin[4]) >= 410:
                    print('Error: left_x (' + str(lin[4]) + ') is greater than 410')
                else:
                    if int(lin[6]) <= 6:
                        print('Error: top_y (' + str(lin[6]) + ') is less than 6')
                    elif int(lin[6]) >= 410:
                        print('Error: top_y (' + str(lin[6]) + ') is greater than 410')
                    else:
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
                        bottom_y = top_y + height
                        right_x = left_x + width
                        if bottom_y < 0:
                            bottom_y = 0
                        if right_x > 416:
                            right_x = 416
                        if bottom_y <= 6:
                            print('Error : bottom_y (' + str(bottom_y) + ') is less than 6')
                        elif bottom_y >= 410:
                            print('Error : bottom_y (' + str(bottom_y) + ') is greater than 410')
                        else:
                            if right_x >= 410:
                                print('Error : right_x (' + str(right_x) + ') is greater than 410')
                            elif right_x <= 6:
                                print('Error : right_x (' + str(right_x) + ') is less than 6')
                            else:
                                print(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100))
                                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100) + ' \n')
            elif line[0:4] == 'ECHY':
                lin = re.split(':|%|t|w|h', line)
                if int(lin[4]) <= 6:
                    # pass
                    print('Error: left_x (' + str(lin[4]) + ') is less than 6')
                elif int(lin[4]) >= 410:
                    print('Error: left_x (' + str(lin[4]) + ') is greater than 410')
                else:
                    if int(lin[6]) <= 6:
                        print('Error: top_y (' + str(lin[6]) + ') is less than 6')
                    elif int(lin[6]) >= 416:
                        print('Error: top_y (' + str(lin[6]) + ') is greater than 410')
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
                        if bottom_y <= 6:
                            print('Error : bottom_y (' + str(bottom_y) + ') is less than 6')
                        elif bottom_y >= 410:
                            print('Error : bottom_y (' + str(bottom_y) + ') is greater than 410')
                        else:
                            if right_x >= 410:
                                print('Error : right_x (' + str(right_x) + ') is greater than 410')
                            elif right_x <= 6:
                                print('Error : right_x (' + str(right_x) + ') is less than 0')
                            else:
                                print(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100))
                                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100) + ' \n')
            else:
                pass

# Run the import_and_filder_results function
# import_and_filder_results()
