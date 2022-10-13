import os
import numpy as np 
import decimal
import re


gt_file = open('gt.txt', 'w')
test_folder = '/home/as-hunt/Etra-Space/new_data_sidless/valid/'
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
            # print(img_name)
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
                    print('center_x ('+ width +') is 0')
                elif height == '0':
                    print('center_x ('+ height +') is 0')
                else:
                    center_x = decimal.Decimal(center_x) * 416
                    center_y = decimal.Decimal(center_y) * 416
                    width = decimal.Decimal(width) * 416
                    height = decimal.Decimal(height) * 416
                    left_x = int(decimal.Decimal(center_x) - (width / 2))
                    top_y = int(decimal.Decimal(center_y) + (height / 2))
                    right_x = int(decimal.Decimal(center_x) + (width / 2))
                    bottom_y = int(decimal.Decimal(center_y) - (height / 2))
                    if left_x <= 0:
                        print('left_x (' + str(left_x) + ') is less than 0')
                    elif left_x >= 416:
                        print('left_x (' + str(left_x) + ') is greater than 416')
                    else:
                        if top_y <= 0:
                            print('top_y (' + str(top_y) + ') is less than 0')
                        elif top_y >= 416:
                            print('top_y (' + str(top_y) + ') is greater than 416')
                        else:
                            if right_x <= 0:
                                print('right_x (' + str(right_x) + ') is less than 0')
                            elif right_x >= 416:
                                print('right_x (' + str(right_x) + ') is greater than 416')
                            else:
                                if bottom_y <= 0:
                                    print('bottom_y (' + str(bottom_y) + ') is less than 0')
                                elif bottom_y >= 416:
                                    print('bottom_y (' + str(bottom_y) + ') is greater than 416')
                                else:
                                    # print(img_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y))
                                    gt_file.write(img_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' \n')
                                    count += 1
                                    print('Line ' + str(count) + ': ' + img_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y))
                                    # print(annotation)    
            annot.close()

gt_file.close()
# remove_empty_lines('ground_truth.txt')

# def one_file_only(file='Mini/RCC_15_416_0_jpg.rf.6fae222d833a44aeafd40a550d3e5c82.txt'):
#     gt_file = open('test_gt.txt', 'w')
#     img_name = file[:-4] 
#     count = 0
#     # print(img_name)
#     annot = open(file, 'r')
#     for line in annot:
#                 lin = re.split(' ', line)
#                 print(lin[1])
#                 classes = lin[0]
#                 center_x = lin[1]
#                 center_y = lin[2]
#                 width = lin[3]
#                 height = lin[4]
#                 if center_x == '0':
#                     print('center_x ('+ center_x +') is 0')
#                 elif center_y == '0':
#                     print('center_x ('+ center_y +') is 0')
#                 elif width == '0':
#                     print('center_x ('+ width +') is 0')
#                 elif height == '0':
#                     print('center_x ('+ height +') is 0')
#                 else:
#                     center_x = decimal.Decimal(center_x) * 416
#                     center_y = decimal.Decimal(center_y) * 416
#                     width = decimal.Decimal(width) * 416
#                     height = decimal.Decimal(height) * 416
#                     left_x = int(decimal.Decimal(center_x) - (width / 2))
#                     top_y = int(decimal.Decimal(center_y) + (height / 2))
#                     right_x = int(decimal.Decimal(center_x) + (width / 2))
#                     bottom_y = int(decimal.Decimal(center_y) - (height / 2))
#                     if left_x <= 0:
#                         print('left_x (' + str(left_x) + ') is less than 0')
#                     elif left_x >= 416:
#                         print('left_x (' + str(left_x) + ') is greater than 416')
#                     else:
#                         if top_y <= 0:
#                             print('top_y (' + str(top_y) + ') is less than 0')
#                         elif top_y >= 416:
#                             print('top_y (' + str(top_y) + ') is greater than 416')
#                         else:
#                             if right_x <= 0:
#                                 print('right_x (' + str(right_x) + ') is less than 0')
#                             elif right_x >= 416:
#                                 print('right_x (' + str(right_x) + ') is greater than 416')
#                             else:
#                                 if bottom_y <= 0:
#                                     print('bottom_y (' + str(bottom_y) + ') is less than 0')
#                                 elif bottom_y >= 416:
#                                     print('bottom_y (' + str(bottom_y) + ') is greater than 416')
#                                 else:
#                                     # print(img_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y))
#                                     gt_file.write(img_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' \n')
#                                     count += 1
#                                     print('Line ' + str(count) + ': ' + img_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y))
#                                     # print(annotation)    
#     annot.close()

# one_file_only()