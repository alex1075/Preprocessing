import os

# delete bounding boxes that are on the edge of the image
# this is done to avoid false positives
# this is done after the predictions are made

def del_edge_bbox_train(results_folder):
    for file in os.listdir(results_folder):
        if file.endswith('classes.txt'):
            pass
        elif file.endswith('.txt'):
            filoo = open(results_folder + file, 'r')
            lines = filoo.readlines()
            filoo.close()
            filoo = open(results_folder + file, 'w')
            for line in lines:
                lin = line.split(' ')
                x1 = float(lin[1])
                y1 = float(lin[2])
                x2 = float(lin[3])
                y2 = float(lin[4])
                if x1 <= 0.005 or y1 <= 0.005 or x1 >= 0.995 or y1 >= 0.995:
                    pass
                else:
                    filoo.write(line)
            filoo.close()

def del_edge_bbox_test(results_folder):
    for file in os.listdir(results_folder):
        if file.endswith('.txt'):
            filoo = open(results_folder + file, 'r')
            lines = filoo.readlines()
            filoo.close()
            filoo = open(results_folder + file, 'w')
            for line in lines:
                lin = line.split(' ')
                x1 = float(lin[2])
                y1 = float(lin[3])
                x2 = float(lin[4])
                y2 = float(lin[5])
                if x1 == 0 or y1 == 0 or x2 == 416 or y2 == 416:
                    pass
                else:
                    filoo.write(line)
            filoo.close()

del_edge_bbox_train('/home/as-hunt/Etra-Space/3-class-sideless/valid/')