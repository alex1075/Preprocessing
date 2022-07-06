import os

class yolo:
    """An attempt to incorporate darknet as a class"""
    def dont_show(state):
        if state == True:
            return True
        else:  
            return False
    
    def mAP(state):
        if state ==  True:
            return True
        else:
            return False
    
    def __init__(self, weights_file, config_file, data_file, dont_show=True, mAP=True):
        self.weights_file = weights_file
        self.config_file = config_file
        self.dont_show
        self.data_file = data_file
        self.train = 'cd .. && ./darknet/darknet detector train ' + self.data_file + ' ' + self.config_file + ' ' + self.weights_file 
        self.valid = 'cd .. && ./darknet/darknet detector valid ' + self.data_file + ' ' + self.config_file + ' ' + self.weights_file
        self.command = 'cd .. && ./darknet/darknet detector ' + self.data_file + ' ' + self.config_file + ' ' + self.weights_file
        self.results_folder = '/mnt/c/Users/Alexander Hunt/results/'
        self.result_OTH = '/mnt/C/Users/Alexander Hunt/results/comp4_det_test_OTR.txt'
        self.result_PLT = '/mnt/C/Users/Alexander Hunt/results/comp4_det_test_PLT.txt'
        self.result_RBC = '/mnt/C/Users/Alexander Hunt/results/comp4_det_test_RBC.txt'
        self.result_RBC_sidew = '/mnt/C/Users/Alexander Hunt/results/comp4_det_test_RBC_sidew.txt'
        self.result_RBC_overlap = '/mnt/C/Users/Alexander Hunt/results/comp4_det_test_RBC_overlap.txt'
