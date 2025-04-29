import os, cv2, re, csv, argparse 
import pandas as pd
import matplotlib.pyplot as plt

def fist_run(folder):
    '''checks folder for not_fisrst_run.txt and creates it if it doesn't exist'''
    if os.path.exists(folder + 'not_first_run.txt') == False:
            # os.system('touch ' + folder + 'not_first_run.txt')
            return True
    else:
        os.system('rm ' + folder + 'out/*.csv')
        return False

def check_if_folder_exists(folder):
    '''Checks if a folder exists and creates it if it doesn't'''
    if os.path.exists(folder) == False:
        os.system('mkdir ' + folder)

def crop_images(x, y, path, save_path):
    images = os.listdir(path)
    for image in images:
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
        os.system('rm ' + path + image)        

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
        cv2.imwrite(path + image[:-4] + ".jpg", corrected_img)
    else:
        pass

def get_labels(obj_names):
    '''Returns a list of labels from the obj.names file'''
    labels = []
    with open(obj_names, 'r') as f:
        for line in f:
            labels.append(line.strip())
    return labels

def checkAllImg(path, x, y):
    images = os.listdir(path)
    for image in images:
        if image.endswith(".jpg"):
            imgSizeCheck(image, path, x, y)

def videos_to_images(path_to_video):
    '''Converts a video to a series of images'''
    vidcap = cv2.VideoCapture(path_to_video)
    success,image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite(path_to_video[:-4] + "frame%d.jpg" % count, image)
        success,image = vidcap.read()
        count += 1
    os.remove(path_to_video)     

def convert_to_jpg(path_to_image):
    '''Converts a png image to jpg'''
    img = cv2.imread(path_to_image)
    cv2.imwrite(path_to_image[:-4] + '.jpg', img)
    os.remove(path_to_image)

def convert_tiff_to_jpg(path_to_image):
    print(path_to_image)
    '''Converts a png image to jpg'''
    img = cv2.imread(path_to_image)
    cv2.imwrite(path_to_image[:-5] + '.jpg', img)
    os.remove(path_to_image)
 
def check_data(folder):
    list = os.listdir(folder)
    for i in list:
        if i.endswith('.png') or i.endswith('.PNG') or i.endswith('.jpeg') or i.endswith('.JPEG') or i.endswith('.bmp') or i.endswith('.BMP'):
            convert_to_jpg(folder + i)          
        if i.endswith('.tiff') or i.endswith('.TIFF'):
            convert_tiff_to_jpg(folder + i)    
        if i.endswith('.mp4') or i.endswith('.MP4') or i.endswith('.avi') or i.endswith('.AVI'):
            videos_to_images(folder + i)

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
    ery = len(df.loc[df['Cell type'] == 'ERY'])
    echy = len(df.loc[df['Cell type'] == 'ECHY'])
    plt = len(df.loc[df['Cell type'] == 'PLT'])
    wbc = len(df.loc[df['Cell type'] == 'WBC'])
    lym = len(df.loc[df['Cell type'] == 'LYM'])
    mon = len(df.loc[df['Cell type'] == 'MON'])
    neu = len(df.loc[df['Cell type'] == 'NEU'])
    lyma = len(df.loc[df['Cell type'] == 'LYM-A'])
    mona = len(df.loc[df['Cell type'] == 'MON-A'])
    neua = len(df.loc[df['Cell type'] == 'NEU-A'])  
    if wbc != 0 and lym != 0 and mon != 0 and neu != 0 and lyma != 0 and mona != 0 and neua != 0:  
        raise ValueError('WBC and WBC subtypes detected. Check which obj.names file is being used.')
    if wbc == 0:
        wbc = lym + mon + neu + lyma + mona + neua
        conf_wbc = (round(float(df.loc[df['Cell type'] == 'LYM']['Confidence'].mean()), 2) + round(float(df.loc[df['Cell type'] == 'MON']['Confidence'].mean()), 2) + round(float(df.loc[df['Cell type'] == 'NEU']['Confidence'].mean()), 2) + round(float(df.loc[df['Cell type'] == 'LYM-']['Confidence'].mean()), 2) + round(float(df.loc[df['Cell type'] == 'MON-']['Confidence'].mean()), 2) + round(float(df.loc[df['Cell type'] == 'NEU-']['Confidence'].mean()), 2) / 6)
    else:
        conf_wbc = round(float(df.loc[df['Cell type'] == 'WBC']['Confidence'].mean()), 2)
    ery = ery + echy
    total_count = ery + plt + wbc
    conf_ery = (round(float(df.loc[df['Cell type'] == 'ERY']['Confidence'].mean()), 2) + round(float(df.loc[df['Cell type'] == 'ECHY']['Confidence'].mean()), 2) / 2)
    conf_plt = round(float(df.loc[df['Cell type'] == 'PLT']['Confidence'].mean()), 2)
    try:
        ratio_ery_plt = round((ery / plt), 2)
    except ZeroDivisionError:
        ratio_ery_plt = 0
    try:
        ratio_plt_wbc = round((plt / wbc), 2)
    except ZeroDivisionError:
        ratio_plt_wbc = 0
    try:
        ratio_ery_wbc = round((ery / wbc), 2)
    except ZeroDivisionError:
        ratio_ery_wbc = 0
    try:
        ratio_wbc_ery = round((wbc / ery), 2)
    except ZeroDivisionError:
        ratio_wbc_ery = 0
    try:
        ratio_wbc_plt = round((wbc / plt), 2)
    except ZeroDivisionError:
        ratio_wbc_plt = 0
    if differrential == True:
        with open(path + 'output_'+name +'.txt', '+a') as f:
            f.write(f'RBCs: {ery} \n')
            f.write(f'PLTs: {plt} \n')
            f.write(f'WBCs: {wbc} \n')
            f.write(f'LYMs: {lym} \n')
            f.write(f'MONs: {mon} \n')
            f.write(f'NEUs: {neu} \n')
            f.write(f'LYM-A: {lyma} \n')
            f.write(f'MON-A: {mona} \n')
            f.write(f'NEU-A: {neua} \n')
            f.write(f'Ratio of RBCs to WBCs: {ratio_ery_wbc} \n')
            f.write(f'Ratio of WBCs to PLTs: {ratio_wbc_plt} \n')
            f.write(f'Ratio of RBCs to PLTs: {ratio_ery_plt} \n')
            f.write(f'Ratio of PLTs to WBCs: {ratio_plt_wbc} \n')
            f.write(f'Ratio of WBCs to RBCs: {ratio_wbc_ery} \n')
            f.write(f'Total number of cells: {total_count} \n')
            f.write(f'Percent of RBCs: {round((ery / total_count) * 100, 2)} \n')
            f.write(f'Percent of PLTs: {round((plt / total_count) * 100, 2)} \n')
            f.write(f'Percent of WBCs: {round((wbc / total_count) * 100, 2)} \n')
            f.write(f'Percent of LYM: {round((lym / total_count) * 100, 2)} \n')
            f.write(f'Percent of MON: {round((mon / total_count) * 100, 2)} \n')
            f.write(f'Percent of NEU: {round((neu / total_count) * 100, 2)} \n')
            f.write(f'Percent of LYM-A: {round((lyma / total_count) * 100, 2)} \n')
            f.write(f'Percent of MON-A: {round((mona / total_count) * 100, 2)} \n')
            f.write(f'Percent of NEU-A: {round((neua / total_count) * 100, 2)} \n')
            f.write(f'Average confidence of RBCs: {conf_ery} \n')
            f.write(f'Average confidence of PLTs: {conf_plt} \n')
            f.write(f'Average confidence of WBCs: {conf_wbc} \n')
            f.write(f'Average confidence of all cells: {round(float(df["Confidence"].mean()), 2)} \n')    
    else:
        with open(path + 'output.txt', '+a') as f:
            f.write(f'RBCs: {ery} \n')
            f.write(f'PLTs: {plt} \n')
            f.write(f'WBCs: {wbc} \n')
            f.write(f'Ratio of RBCs to WBCs: {ratio_ery_wbc} \n')
            f.write(f'Ratio of WBCs to PLTs: {ratio_wbc_plt} \n')
            f.write(f'Ratio of RBCs to PLTs: {ratio_ery_plt} \n')
            f.write(f'Ratio of PLTs to WBCs: {ratio_plt_wbc} \n')
            f.write(f'Ratio of WBCs to RBCs: {ratio_wbc_ery} \n')
            f.write(f'Total number of cells: {total_count} \n')
            f.write(f'Percent of RBCs: {round((ery / total_count) * 100, 2)} \n')
            f.write(f'Percent of PLTs: {round((plt / total_count) * 100, 2)} \n')
            f.write(f'Percent of WBCs: {round((wbc / total_count) * 100, 2)} \n')
            f.write(f'Average confidence of RBCs: {conf_ery} \n')
            f.write(f'Average confidence of PLTs: {conf_plt} \n')
            f.write(f'Average confidence of WBCs: {conf_wbc} \n')
            f.write(f'Average confidence of all cells: {round(float(df["Confidence"].mean()), 2)} \n')

def ensure_directory_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

if __name__ == '__main__':
    run = 1
    folder = '/home/as-hunt/bloodbact/n3/3/'
    ai_folder = f'/home/as-hunt/Etra-Space/Diffy-10k/{run}/'
    obj_data = ai_folder + 'obj.data'
    yolo_cfg = ai_folder + 'yolov4.cfg'
    weights = ai_folder + 'backup/yolov4_final.weights'
    obj_names = ai_folder + 'obj.names'
    out_file = folder + 'out/results.txt'
    data_path = folder + 'data.txt'
    path = folder + 'out/'
    file_name = 'data.txt'
    name = f'results_{run}'
    differrential = True
    if fist_run(folder) == True:
        print('First run')
        ensure_directory_exists(path)
        check_data(folder)
        print('Data checked')
        crop_images(416, 416, folder, folder)
        print('Images cropped')
        checkAllImg(folder, 416, 416)
        print('Images checked')
        pre(folder, 'data.txt')
        print('Data prepared')
        darknet_test(obj_data, yolo_cfg, weights, data_path, out_file)
        print('Test run')
    read_results(out_file, obj_names, path, name)
    print('Results read')
    consolidate_results(path, differrential, name)

# if __name__ == '__main__':
#     ai_folder_root = '/home/as-hunt/Etra-Space/Diffy-10k/'
#     folder_root = '/home/as-hunt/erythrocytopenia/'
#     for i in range(0, 21, 1):
#         for j in range(1, 5, 1):
#             print(f'Run on sample {i} with AI {j}')
#             folder = f'{folder_root}/{i}/'
#             ai_folder = f'{ai_folder_root}/{j}/'
#             obj_data = ai_folder + 'obj.data'
#             yolo_cfg = ai_folder + 'yolov4.cfg'
#             weights = ai_folder + 'backup/yolov4_final.weights'
#             obj_names = ai_folder + 'obj.names'
#             out_file = folder + 'out/results.txt'
#             data_path = folder + 'data.txt'
#             path = folder + 'out/'
#             file_name = 'data.txt'
#             name = f'results_{j}'
#             differrential = True
#             if fist_run(folder) == True:
#                 check_if_folder_exists(path)
#                 print('First run')
#                 check_data(folder)
#                 print('Data checked')
#                 crop_images(416, 416, folder, folder)
#                 print('Images cropped')
#                 checkAllImg(folder, 416, 416)
#                 print('Images checked')
#                 pre(folder, 'data.txt')
#                 print('Data prepared')
#                 darknet_test(obj_data, yolo_cfg, weights, data_path, out_file)
#                 print('Test run')
#             read_results(out_file, obj_names, path, name)
#             print('Results read')
#             consolidate_results(path, differrential, name)