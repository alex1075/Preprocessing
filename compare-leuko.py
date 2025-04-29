import os, re, csv
import pandas as pd
import shutil

def scan_through_detection_output(file_path='bloodbact/n1/1/out/results.txt', cell_types_to_filter=['LYM', 'NEU', 'MON'], obj_names='/home/as-hunt/Etra-Space/Diffy-10k/1/obj.names', target_dir='bloodbact/n1/1/out', test=''):
    names = []
    with open(obj_names, 'r') as f:
        for line in f:
            names.append(line.strip())
    names.sort()        
    classes = []
    for item in cell_types_to_filter:
        classes.append(str(names.index(item)))
        print(f'Index of {item} is {names.index(item)}')
    leuko_txt = open(file_path[:-4] + '_leuko.txt', 'w')    
    with open(file_path, 'r') as f:
        for line in f:
            li = line.split(' ')
            if li[1] in classes:
                shutil.copy(test + li[0]+'.jpg', target_dir)
                print(f'Copying {li[0]} to {target_dir}')
                leuko_txt.write(''.join(li) + '\n')
                print(f'Writing {li} to {file_path[:-4] + "_leuko.txt"}')
            else:
                pass
    leuko_txt.close()

def folder_exists(folder_path):
    if os.path.exists(folder_path):
        pass
    else:
        os.makedirs(folder_path)

def darknet_test(obj_data, yolo_cfg, weights, data_path, out_file):
    '''Runs the darknet detector test command'''
    os.system('darknet detector test ' + obj_data + ' ' + yolo_cfg + ' ' + weights + ' -dont_show -ext_output < ' + data_path  + ' > ' +  out_file +' 2>&1')

def read_results(results_file, obj_names, path, name):
    arry = []
    array = []
    with open(obj_names, 'r') as f:
        for line in f:
            arry.append(line.rstrip())
    with open(results_file, 'r') as f:
        for line in f:
            if line[0:4] == '/hom':
                lin = re.split(':', line)
                li = filter(lambda a: '.jpg' in a, lin)
                l = list(li)[0]
                image_name = l
            elif (line[0:3] in arry) or (line[0:4] in arry ) == True:
                lin = re.split(':|%|t|w|h', line)
                classes = lin[0]
                confidence = int((lin[1]))
                array.append([image_name , str(classes) , str(int(confidence))])
            else:
                pass
    with open(path + name +'.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Image name', 'Cell type', 'Confidence'])
        for line in array:
            writer.writerow(line) 

def pre(folder, file_name):
    filoo = open(folder + file_name, 'w')
    for image in os.listdir(folder):
        if image.endswith(".jpg"):
            filoo.write(folder + image + "\n")
    filoo.close()

def consolidate_results(path, differrential = False, name = 'results'):
    '''Consolidates the results of a test into one txt file'''
    df = pd.read_csv(path + name + '.csv')
    lym = len(df.loc[df['Cell type'] == 'LYM'])
    mon = len(df.loc[df['Cell type'] == 'MON'])
    neu = len(df.loc[df['Cell type'] == 'NEU'])
    lyma = len(df.loc[df['Cell type'] == 'LYM-A'])
    mona = len(df.loc[df['Cell type'] == 'MON-A'])
    neua = len(df.loc[df['Cell type'] == 'NEU-A'])  
    wbc = lym + mon + neu + lyma + mona + neua
    # conf_wbc = (round(float(df.loc[df['Cell type'] == 'LYM']['Confidence'].mean()), 2) + round(float(df.loc[df['Cell type'] == 'MON']['Confidence'].mean()), 2) + round(float(df.loc[df['Cell type'] == 'NEU']['Confidence'].mean()), 2) + round(float(df.loc[df['Cell type'] == 'LYM-']['Confidence'].mean()), 2) + round(float(df.loc[df['Cell type'] == 'MON-']['Confidence'].mean()), 2) + round(float(df.loc[df['Cell type'] == 'NEU-']['Confidence'].mean()), 2) / 6)
    total_count = wbc
    if differrential == True:
        with open(path + 'output_'+name +'.txt', '+a') as f:
            f.write(f'WBCs: {wbc} \n')
            f.write(f'LYMs: {lym} \n')
            f.write(f'MONs: {mon} \n')
            f.write(f'NEUs: {neu} \n')
            f.write(f'LYM-A: {lyma} \n')
            f.write(f'MON-A: {mona} \n')
            f.write(f'NEU-A: {neua} \n')
            f.write(f'Total number of cells: {total_count} \n')
            try:
                f.write(f'Percent of LYM: {round((lym / total_count) * 100, 2)} \n')
                f.write(f'Percent of MON: {round((mon / total_count) * 100, 2)} \n')
                f.write(f'Percent of NEU: {round((neu / total_count) * 100, 2)} \n')
                f.write(f'Percent of LYM-A: {round((lyma / total_count) * 100, 2)} \n')
                f.write(f'Percent of MON-A: {round((mona / total_count) * 100, 2)} \n')
                f.write(f'Percent of NEU-A: {round((neua / total_count) * 100, 2)} \n')
            except ZeroDivisionError:
                pass
            # f.write(f'Average confidence of all cells: {round(float(df["Confidence"].mean()), 2)} \n')    
    else:
        with open(path + 'output.txt', '+a') as f:
            f.write(f'WBCs: {wbc} \n')
            f.write(f'Total number of cells: {total_count} \n')
            # f.write(f'Average confidence of all cells: {round(float(df["Confidence"].mean()), 2)} \n')                

if __name__ == '__main__':
    n=1
    N=1
    path = f'/home/as-hunt/Etra-Space/Diffy-10k/{n}/'
    ai_folder = f'/home/as-hunt/Etra-Space/Mono/{N}/'
    obj_names1 = path + 'obj.names'
    og_results = path + 'results.txt'
    target_dir = path + 'leuko/'
    obj_names2 = ai_folder + 'obj.names'
    obj_data = ai_folder + 'obj.data'
    yolo_cfg = ai_folder + 'yolov4.cfg'
    weights = ai_folder + 'backup/yolov4_final.weights'
    results = target_dir + 'results.txt'
    name = f'results{N}'
    cells = ['LYM', 'NEU', 'MON']
    folder_exists(target_dir)
    scan_through_detection_output(og_results, cells, obj_names1, target_dir, test= path + 'test/')
    pre(target_dir, 'test.txt')
    darknet_test(obj_data, yolo_cfg, weights, target_dir + 'test.txt', results)
    read_results(results, obj_names2, target_dir, name)
    consolidate_results(target_dir, True, name)
    consolidate_results(path, True, 'results')

