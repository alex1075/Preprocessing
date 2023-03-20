import os

# delete bounding boxes that are on the edge of the image
# this is done to avoid false positives
# this is done after the predictions are made

def del_edge_bbox_train(results_folder):
    for file in os.listdir(results_folder):
        if file.endswith('classes.txt'):
            pass
        elif file.endswith('.txt'):
            print(file)
            filoo = open(results_folder + file, 'r')
            lines = filoo.readlines()
            filoo.close()
            filoo = open(results_folder + file, 'w')
            for line in lines:
                lin = line.split(' ')
                if lin[0] == '\n':
                    pass
                else:
                    cent_x = float(lin[1])
                    cent_y = float(lin[2])
                    width = float(lin[3])
                    height = float(lin[4])
                    x1 = int(cent_x - (width / 2))
                    y1 = int(cent_y - (height / 2))
                    x2 = int(cent_x + (width / 2))
                    y2 = int(cent_y + (height / 2))

                    if x1 <= 5 or y1 <= 5 or x1 >= 411 or y1 >= 411:
                        pass
                    elif x2 <= 5 or y2 <= 5 or x2 >= 411 or y2 >= 411:
                        pass
                    else:
                        filoo.write(line)
            filoo.close()
            try:
                if os.stat(file).st_size == 0:
                    os.remove(file)
                    os.remove(file.replace('.txt', '.jpg'))
            except:
                pass
            try:
                if open(results_folder + file, 'r') == '\n':
                    os.remove(file)
                    os.remove(file.replace('.txt', '.jpg'))
            except:
                pass

def del_edge_bbox_test(results_folder):
    for file in os.listdir(results_folder):
        if file.endswith('.txt'):
            print(file)
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

del_edge_bbox_train('output/')