import os
import numpy as np 

def remove_empty_lines(filename):
    if not os.path.isfile(filename):
        print("{} does not exist ".format(filename))
        return
    with open(filename) as filehandle:
        lines = filehandle.readlines()

    with open(filename, 'w') as filehandle:
        lines = filter(lambda x: x.strip(), lines)
        filehandle.writelines(lines) 

gt_file = open('ground_truth.txt', 'w')
test_folder = '/mnt/c/Users/Alexander Hunt/data/test/'
for file in os.listdir(test_folder):
    if file.endswith('.txt'):
        if file == 'test.txt':
            pass
        else:
            img_name = file[:-4] + '.jpg'
            count = 0
            print(img_name)
            annot = open(test_folder + file, 'r')
            for line in annot:
                gt_file.write(img_name[:-4] + ' ' + line + '\n')
                count += 1
                print('Line ' + str(count) + ': ' + line)
                # print(annotation)    
            annot.close()

gt_file.close()
remove_empty_lines('ground_truth.txt')