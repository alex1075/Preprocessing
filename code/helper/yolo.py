import os
import tqdm
from multiprocessing import Process

cwd = os.getcwd()

#         self.results_folder = '/mnt/c/Users/Alexander Hunt/results/'
#         self.result_OTH = '/mnt/C/Users/Alexander Hunt/results/comp4_det_test_OTR.txt'
#         self.result_PLT = '/mnt/C/Users/Alexander Hunt/results/comp4_det_test_PLT.txt'
#         self.result_RBC = '/mnt/C/Users/Alexander Hunt/results/comp4_det_test_RBC.txt'
#         self.result_RBC_sidew = '/mnt/C/Users/Alexander Hunt/results/comp4_det_test_RBC_sidew.txt'
#         self.result_RBC_overlap = '/mnt/C/Users/Alexander Hunt/results/comp4_det_test_RBC_overlap.txt'
def yolo_train(weights_file='cfg/yolov4.conv.137', config_file='cfg/yolov4.cfg', data_file='data/obj.data', GPU=1, dont_show=True, mAP=True):
    args = ''
    if dont_show == True:
        args = ' --dont_show'
    else:
        pass
    if mAP == True:
        args = ' --map'
    else:
        pass
    cfg = open(cwd + config_file, 'r')
    for line in cfg:
        if 'max_batches' in line:
            lin = line.split(' = ')
            max_batches = int(lin[1])
    step = 0
    output = os.system('cd .. && ./darknet/darknet detector train ' + data_file + ' ' + config_file + ' ' + weights_file + args)
    progress = tqdm.tqdm(range(max_batches), f"Training, currently on step {step} of {max_batches}", unit="B", unit_scale=True, unit_divisor=1024)
    for line in output:
        if line[1:].isnumeric() == True:
            step += 1
            progress.update(step)
            print(line)
    # print(output)
    return output

def yolo_test(weights_file='cfg/yolov4.conv.137', config_file='cfg/yolov4.cfg', data_file='data/obj.data', GPU=1, dont_show=True, mAP=True):
    args = ''
    if dont_show == True:
        args = ' --dont_show'
    else:
        pass
    if mAP == True:
        args = ' --map'
    else:
        pass
    output = os.system('cd .. && ./darknet/darknet detector test ' + data_file + ' ' + config_file + ' ' + weights_file + args)
    print(output)

def yolo_valid(weights_file='cfg/yolov4.conv.137', config_file='cfg/yolov4.cfg', data_file='data/obj.data', GPU=1, dont_show=True, mAP=True):
    args = ''
    if dont_show == True:
        args = ' --dont_show'
    else:
        pass
    if mAP == True:
        args = ' --map'
    else:
        pass
    output = os.system('cd .. && ./darknet/darknet detector valid ' + data_file + ' ' + config_file + ' ' + weights_file + args)
    print(output)

