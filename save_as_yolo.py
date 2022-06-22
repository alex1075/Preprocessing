import numpy as np
import cv2
import errno
import os
import time
import YOLO_module, data_manager_module


# FILE_CFG = "cfg/yolov4.cfg"
FILE_CFG = "darknet/cfg/yolov4.cfg"
FILE_WEIGHTS = "darknet/yolov4_new_data_1.weights"
# FILE_WEIGHTS = "/Saved_weights/yolov4_new_data_1.weights"
# FILE_DATA = "/data/obj.data"
FILE_DATA = "darknet/data/obj.data"

# settings
THRESH_YOLO = 0.1
LETTER_BOX = True
#LETTER_BOX = False

WHITELIST = []

# DIRNAME_TEST = "data/test/"
DIRNAME_TEST = "darknet/data/test/"
TEXTNAME_TEST_SOURCE = os.path.join(DIRNAME_TEST,"test.txt")
dirnames_mkdir = []
dirname_test_parent = DIRNAME_TEST
while len(dirname_test_parent) != 0:
    if not os.path.isdir(dirname_test_parent):
        dirnames_mkdir.insert(0,dirname_test_parent)
    dirname_test_parent = os.path.dirname(dirname_test_parent)
for dirname in dirnames_mkdir:
    os.makedirs(dirname)
os.system("cp "+TEXTNAME_TEST_SOURCE+" "+DIRNAME_TEST)

TEXTNAME_TEST = os.path.join(DIRNAME_TEST, os.path.basename(TEXTNAME_TEST_SOURCE))
with open(TEXTNAME_TEST) as f:
    IMAGENAMES = f.read().splitlines()

with open(FILE_DATA) as f:
    data = f.read().splitlines()
for datum in data:
    if len(datum) == 0:
        continue
    if "#" == datum[0]:
        continue
    datum = datum.split("=")
    if datum[0].strip(" ") == "names":
        FILE_NAMES = datum[1].strip(" ")
        break
with open(FILE_NAMES) as f:
    NAMES_CLASS = f.read().splitlines()
DICT_CLASS = { NAMES_CLASS[i]:i for i in range(len(NAMES_CLASS))}

yolo = YOLO_module.YOLODetector(FILE_CFG,
                                FILE_WEIGHTS,
                                FILE_DATA,
                                THRESH_YOLO,
                                LETTER_BOX,
                                WHITELIST)

def yolo_output_to_yolo_train(results_yolo_output,height_image,width_image):
    results_train = []
    for result in results_yolo_output:
        coord_yolo_output = result[2]
        coord_yolo_train = [coord_yolo_output[0]/ width_image,
                            coord_yolo_output[1]/height_image,
                            coord_yolo_output[2]/ width_image,
                            coord_yolo_output[3]/height_image]

        coord_yolo_train = ["%.05f"%x for x in coord_yolo_train]

        label = DICT_CLASS[result[0]]
        results_train.append([label]+coord_yolo_train+["%.08f"%result[1]])
    return results_train

DIRNAME_SAVE = os.path.join(DIRNAME_TEST,"labels_prediction")
try:     os.makedirs(DIRNAME_SAVE)
except:  pass

for imagename in IMAGENAMES:
    time0 = time.time()

    print(imagename)
    image = cv2.imread(imagename)
    height_image, width_image = image.shape[:2]
    data = data_manager_module.DataManager(image=image)

    # YOLO
    yolo.detect(data)
    #print(data.info)
    results_yolo_output = yolo_output_to_yolo_train(data.info["results"],height_image,width_image)
    #print(results_output)
    with open(os.path.join( DIRNAME_SAVE, os.path.basename(imagename).replace("jpg","txt") ),"w") as f:
        for result in results_yolo_output:
            #print(" ".join([str(s) for s in result]))
            f.write(" ".join([str(s) for s in result])+"\n")

    #yolo.save(to_draw=False)
    #yolo.save(to_draw=True)

    #yolo._checkDrawLabels(data)
    #yolo.show(data=data,to_draw=True,time_wait=0)
    #cv2.imshow("image",cv2.resize(data.image_labeled,(500,500)))
    #cv2.waitKey(0)

    # prediction ends
    print(("duration%.6fs"%(time.time()-time0)))
del yolo