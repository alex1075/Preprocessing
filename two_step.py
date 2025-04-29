import os, re, csv, cv2
import pandas as pd
import shutil
import matplotlib.pyplot as plt
        
def imgSizeCheck(image, path, x, y):
    img = cv2.imread(path + image)
    height, width, channels = img.shape
    if height << y:
        diff = y - height
        difftoo = x - width
        corrected_img = cv2.copyMakeBorder(img, 0, diff, 0, difftoo,  cv2.BORDER_CONSTANT, value=[0,0,0])
        cv2.imwrite(path + image[:-4] + ".jpg", corrected_img)
    elif width << x:
        diff = y - height
        difftoo = x - width
        corrected_img = cv2.copyMakeBorder(img, 0, diff, 0, difftoo,  cv2.BORDER_CONSTANT, value=[0,0,0])
        cv2.imshow(corrected_img)
        cv2.imwrite(path + image[:-4] + ".jpg", corrected_img)
    else:
        pass


   

def crop_image(x, y, path, image):
        save_path = path
        if image.endswith(".jpg"):
            img = cv2.imread(path + image)
            height, width, channels = img.shape
            for i in range(0, height, y):
                for j in range(0, width, x):
                    crop_img = img[i:i+y, j:j+x]
                    new_name = image[:-4] + '_' + str(i) + '_' + str(j)
                    cv2.imwrite(save_path + new_name + ".jpg", crop_img)
                img = cv2.imread(path + image)
            height, width, channels = img.shape
            for i in range(0, height, y):
                 for j in range(0, width, x):
                    crop = img[i:i+y, j:j+x]
                    cv2.imwrite(save_path + image[:-4] + '_' + str(i) + '_' + str(j) + '.jpg', crop)

def checkAllImg(path, x, y):
    images = os.listdir(path)
    for image in images:
        if image.endswith(".jpg"):
            imgSizeCheck(image, path, x, y)

def get_labels(obj_names):
    '''Returns a list of labels from the obj.names file'''
    labels = []
    with open(obj_names, 'r') as f:
        for line in f:
            labels.append(line.strip())
    return labels

def videos_to_images(path_to_video):
    '''Converts a video to a series of images'''
    vidcap = cv2.VideoCapture(path_to_video)
    success,image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite(path_to_video[:-4] + "frame%d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        count += 1
    os.remove(path_to_video)     

def convert_to_jpg(path_to_image):
    '''Converts a png image to jpg'''
    img = cv2.imread(path_to_image)
    cv2.imwrite(path_to_image[:-4] + '.jpg', img)
    os.remove(path_to_image)
 
def check_data(folder):
    list = os.listdir(folder)
    for i in list:
        if i.endswith('.png') or i.endswith('.PNG') or i.endswith('.tiff') or i.endswith('.TIFF') or i.endswith('.jpeg') or i.endswith('.JPEG') or i.endswith('.bmp') or i.endswith('.BMP'):
            convert_to_jpg(folder + i)          
        if i.endswith('.mp4') or i.endswith('.MP4') or i.endswith('.avi') or i.endswith('.AVI'):
            videos_to_images(folder + i)
    list2 = os.listdir(folder)
    for i in list2:
        if i.endswith('.jpg'):
            crop_image(416, 416, folder, i)
            os.remove(folder + i)
        else:
            pass
    checkAllImg(folder, 416, 416)    


def folder_exists(folder_path):
    if os.path.exists(folder_path):
        pass
    else:
        os.makedirs(folder_path)

def scan_through_detection_output(file_path='fintest/n1/1/out/results_1.csv', cell_types_to_filter=['LYM', 'NEU', 'MON'], target_dir='fintest/n1/1/out'):
    with open(file_path, 'r') as f:
        for line in f:
            li = line.split(',')
            if li[1] in cell_types_to_filter:
                shutil.copy(li[0], target_dir)
                print(f'Copying {li[0]} to {target_dir}')
            else:
                pass

def pre(folder, file_name):
    filoo = open(folder + file_name, 'w')
    for image in os.listdir(folder):
        if image.endswith(".jpg"):
            filoo.write(folder + image + "\n")
    filoo.close()

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
    conf_wbc = (round(float(df.loc[df['Cell type'] == 'LYM']['Confidence'].mean()), 2) + round(float(df.loc[df['Cell type'] == 'MON']['Confidence'].mean()), 2) + round(float(df.loc[df['Cell type'] == 'NEU']['Confidence'].mean()), 2) + round(float(df.loc[df['Cell type'] == 'LYM-']['Confidence'].mean()), 2) + round(float(df.loc[df['Cell type'] == 'MON-']['Confidence'].mean()), 2) + round(float(df.loc[df['Cell type'] == 'NEU-']['Confidence'].mean()), 2) / 6)
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
            f.write(f'Average confidence of all cells: {round(float(df["Confidence"].mean()), 2)} \n')    
    else:
        with open(path + 'output.txt', '+a') as f:
            f.write(f'WBCs: {wbc} \n')
            f.write(f'Total number of cells: {total_count} \n')
            f.write(f'Average confidence of all cells: {round(float(df["Confidence"].mean()), 2)} \n')            

# if __name__ == '__main__':

#         cells = ['LYM', 'NEU', 'MON']
#         differrential = True
#         # origin = f'/home/as-hunt/fintest/n{N}/{n}/out/'
#         origin = '/home/as-hunt/test_1/'
#         file = origin + 'out/results_2.csv'
#         target_dir = origin+ 'out/'
#         res_dir = origin + 'bact_res/'
#         print('1')
#         folder_exists(target_dir)
#         print('2')
#         folder_exists(res_dir)
#         print('3')
#         # check_data(origin)
#         print('4')
#         pre(origin, 'test.txt')
#         for run in range(1, 5, 1):
#                 # scan_through_detection_output(file, cells, target_dir)    
#                 ai_folder = f'/home/as-hunt/Etra-Space/LymNeu/{run}/'
#                 obj_data = ai_folder + 'obj.data'
#                 yolo_cfg = ai_folder + 'yolov4.cfg'
#                 weights = ai_folder + 'backup/yolov4_final.weights'
#                 obj_names = ai_folder + 'obj.names'
#                 out_file = res_dir + 'result.txt'        
#                 name = f'results_{run}'
#                 read_results(origin + 'out/result.txt', obj_names, res_dir, 'results_2')
#                 print(f'Scanning through {run}')
#                 print(f'Running darknet test on {run}')
#                 darknet_test(obj_data, yolo_cfg, weights, origin + 'test.txt', out_file)
#                 print(f'Reading results from {run}')
#                 read_results(out_file, obj_names, res_dir, name)
#                 print(f'Consolidating results from {run}')
#                 consolidate_results(res_dir, differrential, name)

if __name__ == '__main__':
    for i in range(1, 4, 1):
        n = i
        for j in range(1, 4, 1):
            N = j
            for n in range(1, 4, 1):
                run = n 
                cells = ['LYM', 'NEU', 'MON']
                differrential = True
                origin = f'/home/as-hunt/fintest/n{N}/{n}/out/'
                file = f'/home/as-hunt/fintest/n{N}/{n}/out/results_1.csv'
                target_dir = f'/home/as-hunt/fintest/n{N}/{n}/out/bact/'
                res_dir = f'/home/as-hunt/fintest/n{N}/{n}/out/bact_res/'
                folder_exists(target_dir)
                folder_exists(res_dir)
                pre(target_dir, 'test2.txt')
                scan_through_detection_output(file, cells, target_dir)    
                ai_folder = f'/home/as-hunt/Etra-Space/LymNeu/{run}/'
                obj_data = ai_folder + 'obj.data'
                yolo_cfg = ai_folder + 'yolov4.cfg'
                weights = ai_folder + 'backup/yolov4_final.weights'
                obj_names = ai_folder + 'obj.names'
                out_file = res_dir + 'results2.txt'        
                name = f'results2_{run}'
                darknet_test(obj_data, yolo_cfg, weights, target_dir + 'test2.txt', out_file)
                read_results(out_file, obj_names, res_dir, name)
                consolidate_results(res_dir, differrential, name)