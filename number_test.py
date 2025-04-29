import os, re, cv2, csv, shutil, pandas as pd, matplotlib.pyplot as plt, tqdm
from import_results import import_results_neo
from add_bbox import iou


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
        cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        count += 1
    os.remove(path_to_video)     

def convert_to_jpg(path_to_image):
    '''Converts a png image to jpg'''
    img = cv2.imread(path_to_image)
    cv2.imwrite(path_to_image[:-4] + '.jpg', img)
    os.remove(path_to_image)

def folder_check(folder):
    '''Checks if a folder exists, if not, creates it'''
    if not os.path.exists(folder):
        os.makedirs(folder)
 
def check_data(folder):
    list = os.listdir(folder)
    for i in list:
        if i.endswith('.png') or i.endswith('.PNG') or i.endswith('.tiff') or i.endswith('.TIFF') or i.endswith('.jpeg') or i.endswith('.JPEG') or i.endswith('.bmp') or i.endswith('.BMP'):
            convert_to_jpg(folder + i)          
        if i.endswith('.mp4') or i.endswith('.MP4') or i.endswith('.avi') or i.endswith('.AVI'):
            videos_to_images(folder + i)

def pre(folder, file_name):
    filoo = open(folder + file_name, 'w')
    for image in os.listdir(folder):
        if image.endswith(".jpg"):
            print(image)
            filoo.write(folder + image + "\n")
    filoo.close()

def split_images_and_annotations(source_folder, destination_folders):
    '''Splits images from one main folder to multiple destination folders
    Args:
        source_folder: the folder containing the images and annotations
        destination_folders: a list of folders to copy the images and annotations to
    '''
    # Create destination folders if they don't exist
    for folder in destination_folders:
        os.makedirs(folder, exist_ok=True)
    # Get a list of all image files in the source folder
    image_files = [f for f in os.listdir(source_folder) if f.endswith('.jpg')]          
    # Shuffle the image files randomly
    # Calculate the number of images in each split
    split_size = len(image_files) // len(destination_folders)
    # Copy images and annotations to the destination folders
    for i, folder in enumerate(destination_folders):
        start_index = i * split_size
        end_index = (i + 1) * split_size if i < len(destination_folders) - 1 else len(image_files)
        for j in range(start_index, end_index):
            image_file = image_files[j]
            source_image_path = os.path.join(source_folder, image_file)
            destination_image_path = os.path.join(folder, image_file)
            shutil.copy(source_image_path, destination_image_path)

def split_to_X_folders(source_folder, destination_folder, number=int):
    '''Split a folder into X folders
    Args:
        source_folder: the folder to split
        destination_folder: the folder to copy the images and annotations to
        number: the number of folders to split into
    '''
    destination_folders = [f"{destination_folder}/f{i+1}" for i in range(number)]
    split_images_and_annotations(source_folder, destination_folders)   

def darknet_test(obj_data, yolo_cfg, weights, data_path, out_file):
    '''Runs the darknet detector test command'''
    os.system('darknet detector test ' + obj_data + ' ' + yolo_cfg + ' ' + weights + ' -dont_show -ext_output < ' + data_path + 'test.txt' + ' > ' +  out_file +' 2>&1')

def check_all_annotations_for_duplicates(annotation_file):
    start = []
    with open(annotation_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line == '\n':
                pass
            else:
                l = line.split(' ')
                image_name, classes, left_x, top_y, right_x, bottom_y, confidence = l[0], l[1], l[2], l[3], l[4], l[5], l[6]
                start.append([image_name, classes, left_x, top_y, right_x, bottom_y, confidence])
    for item in tqdm.tqdm(start, desc='Checking for duplicates'):
        with open(annotation_file, 'a+') as f:
            lines = f.readlines()
            for line in lines:
                l = lines.split(' ')
                if item[0] == l[0]:
                    bbox_1 = [int(item[2]), int(item[3]), int(item[4]), int(item[5])]
                    bbox_2 = [int(l[2]), int(l[3]), int(l[4]), int(l[5])]
                    if iou(bbox_1, bbox_2) > 0.5:
                        if item[6] > l[6]:
                            lines.remove(line)
                        elif item[6] < l[6]:
                            start.remove(item)
                        elif item[6] == l[6]:
                            start.remove(item)
    with open(annotation_file, 'w') as f:
        for item in start:
            f.write(item[0] + ' ' + item[1] + ' ' + item[2] + ' ' + item[3] + ' ' + item[4] + ' ' + item[5] + ' ' + item[6] + ' \n')    

def split_to__folders(folder, out_path, x, *args, **kwargs):
    '''Splits a folder of images into x folders'''
    folder_check(out_path)
    for i in range(x):
        folder_check(out_path + 'folder' + str(i) + '/')
    check_data(folder)
    # split the images into x folders
    count = 0
    image_list = [image for image in os.listdir(folder) if image.endswith(".jpg")]
    number_of_split = int(len(image_list) / x)
    split_to_X_folders(folder, out_path, number_of_split)
    return number_of_split

def math(result, names, folder, i):
    '''Does math on the results'''
    # get the labels
    labels = get_labels(names)
    # get the results
    results = open(result, 'r')
    lines = results.readlines()
    save = []
    cells = ('LYM:', 'MON:', 'NEU:', 'ERY:', 'PLT:', 'ECHY', 'WBC:', 'LYM-', 'MON-', 'NEU-', 'WBC-')
    for line in tqdm.tqdm(lines, desc='Processing results'):
        if line[0:4] in cells:
            lin = re.split(':|%|t|w|h', line)
            save.append([lin[0], int(lin[1])])
        else:
            pass
    df = pd.DataFrame(save, columns=['Cell type', 'Confidence'])
    df.to_csv(folder + f'results_{i}.csv', index=False)
    ery = df.loc[df['Cell type'] == 'ERY']
    echy = df.loc[df['Cell type'] == 'ECHY']
    plt = df.loc[df['Cell type'] == 'PLT']
    wbc = df.loc[df['Cell type'] == 'WBC']
    lym = df.loc[df['Cell type'] == 'LYM']
    mon = df.loc[df['Cell type'] == 'MON']
    neu = df.loc[df['Cell type'] == 'NEU']
    lyma = df.loc[df['Cell type'] == 'LYM-']
    mona = df.loc[df['Cell type'] == 'MON-']
    neua = df.loc[df['Cell type'] == 'NEU-']
    wbca = df.loc[df['Cell type'] == 'WBC-']
    if os.path.exists(os.getcwd() + '/report.txt') == True:
        os.remove(os.getcwd() + '/report.txt')
    with open(os.getcwd() + '/report.txt', 'x') as f:
        f.write('Counted ' + str(len(df)) + ' cells\n')
        f.write('Overall average confidence: ' + str(round(float(df['Confidence'].mean()), 2)) + '\n')
        if len(ery) != 0:
            f.write('Counted ' + str(len(ery)) + ' erythrocytes\n')
            f.write('Average confidence: ' + str(round(float(ery['Confidence'].mean()), 2)) + '\n')
        if len(echy) != 0:
            f.write('Counted ' + str(len(echy)) + ' echinocytes\n')
            f.write('Average confidence: ' + str(round(float(echy['Confidence'].mean()), 2)) + '\n')
        if len(plt) != 0:
            f.write('Counted ' + str(len(plt)) + ' platelets\n')
            f.write('Average confidence: ' + str(round(float(plt['Confidence'].mean()), 2)) + '\n')
        if len(wbc) != 0:
            f.write('Counted ' + str(len(wbc)) + ' white blood cells\n')
            f.write('Average confidence: ' + str(round(float(wbc['Confidence'].mean()), 2)) + '\n')
        if len(lym) != 0:
            f.write('Counted ' + str(len(lym)) + ' lymphocytes\n')
            f.write('Average confidence: ' + str(round(float(lym['Confidence'].mean()), 2)) + '\n')
        if len(mon) != 0:
            f.write('Counted ' + str(len(mon)) + ' monocytes\n')
            f.write('Average confidence: ' + str(round(float(mon['Confidence'].mean()), 2)) + '\n')
        if len(neu) != 0:
            f.write('Counted ' + str(len(neu)) + ' neutrophils\n')
            f.write('Average confidence: ' + str(round(float(neu['Confidence'].mean()), 2)) + '\n')
        if len(lyma) != 0:
            f.write('Counted ' + str(len(lyma)) + ' activated lymphocytes\n')
            f.write('Average confidence: ' + str(round(float(lyma['Confidence'].mean()), 2)) + '\n')
        if len(mona) != 0:
            f.write('Counted ' + str(len(mona)) + ' activated monocytes\n')
            f.write('Average confidence: ' + str(round(float(mona['Confidence'].mean()), 2)) + '\n')
        if len(neua) != 0:
            f.write('Counted ' + str(len(neua)) + ' activated neutrophils\n')
            f.write('Average confidence: ' + str(round(float(neua['Confidence'].mean()), 2)) + '\n')
        if len(wbca) != 0:
            f.write('Counted ' + str(len(wbca)) + ' activated white blood cells\n')
            f.write('Average confidence: ' + str(round(float(wbca['Confidence'].mean()), 2)) + '\n')
        # append a line at the end of a results.csv file
        with open(folder + f'results_{i}.csv', 'a+') as f:
            len_df = len(df)
            conf_df = round(float(df['Confidence'].mean()), 2)
            if len(ery) != 0:
                len_ery = len(ery)
                conf_ery = round(float(ery['Confidence'].mean()), 2)
            else:
                len_ery = 0
                conf_ery = 0
            if len(echy) != 0:
                len_echy = len(echy)
                conf_echy = round(float(echy['Confidence'].mean()), 2)
            else:
                len_echy = 0
                conf_echy = 0
            if len(plt) != 0:
                len_plt = len(plt)
                conf_plt = round(float(plt['Confidence'].mean()), 2)
            else:
                len_plt = 0
                conf_plt = 0
            if len(wbc) != 0:
                len_wbc = len(wbc)
                conf_wbc = round(float(wbc['Confidence'].mean()), 2)
            else:
                len_wbc = 0
                conf_wbc = 0
            if len(lym) != 0:
                len_lym = len(lym)
                conf_lym = round(float(lym['Confidence'].mean()), 2)
            else:
                len_lym = 0
                conf_lym = 0
            if len(mon) != 0:
                len_mon = len(mon)
                conf_mon = round(float(mon['Confidence'].mean()), 2)
            else:
                len_mon = 0
                conf_mon = 0
            if len(neu) != 0:
                len_neu = len(neu)
                conf_neu = round(float(neu['Confidence'].mean()), 2)
            else:
                len_neu = 0
                conf_neu = 0
            if len(lyma) != 0:
                len_lyma = len(lyma)
                conf_lyma = round(float(lyma['Confidence'].mean()), 2)
            else:
                len_lyma = 0
                conf_lyma = 0
            if len(mona) != 0:
                len_mona = len(mona)
                conf_mona = round(float(mona['Confidence'].mean()), 2)
            else:
                len_mona = 0
                conf_mona = 0
            if len(neua) != 0:
                len_neua = len(neua)
                conf_neua = round(float(neua['Confidence'].mean()), 2)
            else:
                len_neua = 0
                conf_neua = 0
            line = f'{len_df},{conf_df},{len_ery},{conf_ery},{len_echy},{conf_echy},{len_plt},{conf_plt},{len_wbc},{conf_wbc},{len_lym},{conf_lym},{len_mon},{conf_mon},{len_neu},{conf_neu},{len_lyma},{conf_lyma},{len_mona},{conf_mona},{len_neua},{conf_neua}\n'
            writer = csv.writer(f)
            writer.writerow(line)
            
def plot_the_plot(csv, title, path):
    '''Plots the plot'''
    df = pd.read_csv(csv)
    df.plot(x='Total number of cells', y='Overall confidence', kind='scatter', title=title)
    plt.savefig(path + title + '.png')


def do_the_tests(folder, out_path, x, obj_data, yolo_cfg, weights, *args, **kwargs):
    '''Runs the darknet detector test command on each folder'''
    split = split_to__folders(folder, out_path, x)
    df = pd.DataFrame(columns=['Total number of cells', 'Overall confidence', 'Number of erythrocytes', 'Erythrocyte confidence', 'Number of echinocytes', 'Echinocytes confidence', 'Number of platelets', 'Platelet confidence', 'Number of white blood cells', 'White blood cell confidence', 'Number of lymphocytes', 'Lymphocyte confidence', 'Number of monocytes', 'Monocyte confidence', 'Number of neutrophils', 'Neutrophil confidence', 'Number of activated lymphocytes', 'Activated lymphocyte confidence', 'Number of activated monocytes', 'Activated monocyte confidence', 'Number of activated neutrophils', 'Activated neutrophil confidence'])
    for i in tqdm.tqdm(range(0, split, 1), desc='Running tests'):
        darknet_test(obj_data, yolo_cfg, weights, out_path + 'folder' + str(i) + '/', out_path + 'folder' + str(i) + '/result.txt')
        import_results_neo(out_path + 'folder' + str(i) + '/result.txt', out_path + 'folder' + str(i) + '/results.txt')
        check_all_annotations_for_duplicates(out_path + 'folder' + str(i) + '/results.txt')
        math(out_path + 'folder' + str(i) + '/results.txt', obj_data, out_path + 'folder' + str(i) + '/', i)
    plot_the_plot(out_path + 'results.csv', f'Inference when split by {x}', out_path)    

if __name__ == '__main__':
    folder = '/home/as-hunt/test/'
    out_path = folder + 'out/'
    x = 10_000
    obj_data = '/home/as-hunt/Etra-Space/Diffy-10k/obj.data'
    yolo_cfg = '/home/as-hunt/Etra-Space/Diffy-10k/yolov4.cfg'
    weights = '/home/as-hunt/Etra-Space/Diffy-10k/backup/yolov4_10000.weights'
    do_the_tests(folder, out_path, x, obj_data, yolo_cfg, weights)
