import os
import sys
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
from import_results import *
from add_bbox import *

def get_info(data_path, model_path, model_name):
    cfg = model_path + 'yolov4_10.cfg'
    weights = model_path + 'backup/' + model_name
    data = model_path + 'obj.data'
    temp_path = data_path + 'temp/'
    if os.path.exists(temp_path) == True:
        pass
    else:
        os.mkdir(temp_path)
    if os.path.exists(data_path + 'test.txt') == True:
        os.remove(data_path + 'test.txt')
    else:
        filoo = open(data_path + 'test.txt', 'w')
        for image in os.listdir(data_path):
            if image.endswith(".jpg"):
                # print(image)
                filoo.write(data_path + image + "\n")
        filoo.close()
    os.system('darknet detector test ' + data + ' ' + cfg + ' ' + weights + ' -dont_show -ext_output < ' + data_path + 'test.txt' + ' > ' + temp_path + 'result.txt 2>&1')
    results = open(temp_path + 'result.txt', 'r')
    lines = results.readlines()
    # print(lines)
    save = []
    cells = ('LYM:', 'MON:', 'NEU:', 'ERY:', 'PLT:', 'ECHY', 'WBC:')
    for line in lines:
        if line[0:4] in cells:
            # print(line)
            # print(line[0], line[1])
            lin = re.split(':|%|t|w|h', line)
            save.append([lin[0], int(lin[1])])
        else:
            pass    
    df = pd.DataFrame(save, columns=['Cell type', 'Confidence'])    
    # print(df)    
    os.remove(data_path + 'test.txt')
    df.to_csv(data_path + 'results.csv', index=False)
    ery = df.loc[df['Cell type'] == 'ERY']
    echy = df.loc[df['Cell type'] == 'ECHY']
    plt = df.loc[df['Cell type'] == 'PLT']
    wbc = df.loc[df['Cell type'] == 'WBC']
    lym = df.loc[df['Cell type'] == 'LYM']
    mon = df.loc[df['Cell type'] == 'MON']
    neu = df.loc[df['Cell type'] == 'NEU']
    print('Counted ' + str(len(df)) + ' cells')
    print('Overall average confidence: ' + str(round(float(df['Confidence'].mean()), 2)))
    if len(ery) != 0:
        print('Counted ' + str(len(ery)) + ' erythrocytes')
        print('Average confidence: ' + str(round(float(ery['Confidence'].mean()), 2)))
    if len(echy) != 0:
        print('Counted ' + str(len(echy)) + ' echinocytes')
        print('Average confidence: ' + str(round(float(echy['Confidence'].mean()), 2)))
    if len(plt) != 0:
        print('Counted ' + str(len(plt)) + ' platelets')
        print('Average confidence: ' + str(round(float(plt['Confidence'].mean()), 2)))
    if len(wbc) != 0:
        print('Counted ' + str(len(wbc)) + ' white blood cells')
        print('Average confidence: ' + str(round(float(wbc['Confidence'].mean()), 2)))
    if len(lym) != 0:
        print('Counted ' + str(len(lym)) + ' lymphocytes')
        print('Average confidence: ' + str(round(float(lym['Confidence'].mean()), 2)))
    if len(mon) != 0:
        print('Counted ' + str(len(mon)) + ' monocytes')
        print('Average confidence: ' + str(round(float(mon['Confidence'].mean()), 2)))
    if len(neu) != 0:
        print('Counted ' + str(len(neu)) + ' neutrophils')
        print('Average confidence: ' + str(round(float(neu['Confidence'].mean()), 2)))
    if len(wbc) != 0:
        import_and_filder_results(temp_path + 'result.txt', temp_path + 'results.txt')
    else:
        import_and_filder_result_2(temp_path + 'result.txt', temp_path + 'results.txt')   
    with open(temp_path + 'results.txt') as f:
        for line in f:
            item = line.split()
            mv = [float(item[2]), float(item[3]), float(item[4]), float(item[5])]
            mv = [i / 416 for i in mv]
            with open(temp_path + item[0] + '.txt', 'a') as g:
                 g.write(str(item[1]) + ' ' + str(mv[0]) + ' ' + str(mv[1]) + ' ' + str(mv[2]) + ' ' + str(mv[3]) + '\n')
    os.remove(temp_path + 'results.txt')           
    os.remove(temp_path + 'result.txt')

if __name__ == "__main__":
    get_info(sys.argv[1], sys.argv[2], sys.argv[3])