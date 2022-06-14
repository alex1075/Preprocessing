import os
import shutil
import numpy
import cv2
import decimal

def change_annotation(i, j, x, y, height, width, path, image,save_path):
        if x2 in range(j, y, 0.0001):
                if y2 in range(i, x, 0.0001):
           
                        # read annotation
                        with open(path + image[:-4] + '.txt', 'r') as f:
                                lines = f.readlines()
                        # loop over lines
                        for line in lines:
                         # get line
                         line = line.split(' ')
                         # get coordinates
                         classes = int(line[0])
                        print("Classes: " + str(classes))
                        x1 = decimal.Decimal(line[1])
                        print("X1: " + str(x1))
                        y1 = decimal.Decimal(line[2])
                        print("Y1: " + str(y1))
                        x2 = decimal.Decimal(line[3])
                        print("X2: " + str(x2))
                        y2 = decimal.Decimal(line[4])
                        print("Y2: " + str(y2))
                        # get new coordinates
                        x1 = decimal.Decimal(((x1 * height) - x ) / x)
                        y1 = decimal.Decimal(((y1 * width) - y) / y)
                        # write new coordinates
                        with open(save_path + image[:-4] + '.txt', 'a') as f:
                            f.write(str(classes))
                            f.write(' ')
                            f.write(str(round(x1, 6)))
                            f.write(' ')
                            f.write(str(round(y1, 6)))
                            f.write(' ')
                            f.write(str(round(x2, 6)))
                            f.write(' ')
                            f.write(str(round(y2, 6)))
                            f.write('\n')
                else:
                        pass    
        else:
                pass    

