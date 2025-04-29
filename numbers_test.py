import os, cv2, re, csv
import pandas as pd
import matplotlib.pyplot as plt

def fist_run(folder):
    '''checks folder for not_fisrst_run.txt and creates it if it doesn't exist'''
    if os.path.exists(folder + 'not_first_run.txt') == False:
            os.system('touch ' + folder + 'not_first_run.txt')
            return True
    else:
        os.system('rm ' + folder + 'out/*.csv')
        return False
        

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

def pre(folder, file_name):
    filoo = open(folder + file_name, 'w')
    for image in os.listdir(folder):
        if image.endswith(".jpg"):
            filoo.write(folder + image + "\n")
    filoo.close()

def darknet_test(obj_data, yolo_cfg, weights, data_path, out_file):
    '''Runs the darknet detector test command'''
    os.system('darknet detector test ' + obj_data + ' ' + yolo_cfg + ' ' + weights + ' -dont_show -ext_output < ' + data_path  + ' > ' +  out_file +' 2>&1')

def split_results(results_file, image_list, x, name, path):
    '''Splits the results file into a list of lists'''
    cells = ('LYM:', 'MON:', 'NEU:', 'ERY:', 'PLT:', 'ECHY', 'WBC:', 'LYM-', 'MON-', 'NEU-', 'WBC-')
    with open(results_file, 'r') as f:
        lines = f.readlines()
    lengt = int(len(image_list) / x)
    chunks = [lines[x:x+lengt] for x in range(0, len(lines), lengt)]
    count = 0
    for chunk in chunks:
        count += 1
        save = []
        for line in chunk:
            if line.startswith(cells):
                lin = re.split(':|%|t|w|h', line)
                save.append([lin[0], int(lin[1])])
            df = pd.DataFrame(save, columns = ['Cell type', 'Confidence'])
            df.to_csv(name + str(count) + '.csv', index=False)
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
            line = f'{len_df,conf_df,len_ery,conf_ery,len_echy,conf_echy,len_plt,conf_plt,len_wbc,conf_wbc,len_lym,conf_lym,len_mon,conf_mon,len_neu,conf_neu,len_lyma,conf_lyma,len_mona,conf_mona,len_neua,conf_neua}\n'
            with open(path + name + '.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(line)

def read_results(results_file, obj_names, path):
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
    with open(path + 'results.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Image name', 'Cell type', 'Confidence'])
        for line in array:
            writer.writerow(line)         

def split_images_and_csv(image_list, csv_file, x):
    # Splitting the image list into smaller lists
    split_image_lists = [image_list[i:i + x] for i in range(0, len(image_list), x)]
    # Reading the CSV file
    with open(csv_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Assuming there's a header
        csv_data = list(csv_reader)

    # List to store smaller lists of CSV data
    split_csv_data_lists = []

    # Splitting the CSV data based on the smaller image lists
    for small_list in split_image_lists:
        # Filtering the CSV data for the current small list
        filtered_csv_data = [row for row in csv_data if row[0] in small_list]
        split_csv_data_lists.append(filtered_csv_data)

    return split_csv_data_lists

def interpret_smaller(list_of_lists, path):
    count = 0
    for list in list_of_lists:
        save = []
        for line in list:
            save.append([line[1], int(line[2])])
        df = pd.DataFrame(save, columns = ['Cell type', 'Confidence'])
        df.to_csv(path + str(count) + '.csv', index=False)
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
        line = [len_df,conf_df,len_ery,conf_ery,len_echy,conf_echy,len_plt,conf_plt,len_wbc,conf_wbc,len_lym,conf_lym,len_mon,conf_mon,len_neu,conf_neu,len_lyma,conf_lyma,len_mona,conf_mona,len_neua,conf_neua]
        with open(path + 'res.csv', 'a') as f:
            writer = csv.writer(f)
            # makes sure the header is only written once
            if count == 0:
                writer.writerow(['Total cells', 'Average confidence', 'Erythrocytes', 'Average confidence', 'Echinocytes', 'Average confidence', 'Platelets', 'Average confidence', 'White blood cells', 'Average confidence', 'Lymphocytes', 'Average confidence', 'Monocytes', 'Average confidence', 'Neutrophils', 'Average confidence', 'Lymphocytes (activated)', 'Average confidence', 'Monocytes (activated)', 'Average confidence', 'Neutrophils (activated)', 'Average confidence'])
                count += 1
            # writes the line to the csv
            writer.writerow(line)

def plot_the_plot(csv, title, path):
    '''Plots a bar chart of the results within the csv one bar per row)'''
    df = pd.read_csv(csv)
    plt.plot(df['Total cells'])
    plt.title(title)
    plt.xlabel('Row number')
    plt.ylabel('Total cell count')
    plt.savefig(path + title + 'plot.png')
    plt.clf()
    if df.loc[df['Erythrocytes'] != 0].empty == False:
        plt.plot(df['Erythrocytes'])
        plt.title(title + 'for Erthrocytes')
        plt.xlabel('Row number')
        plt.ylabel('Total Erythrocyte count')
        plt.savefig(path + title + 'for Erthrocytes plot.png')
        plt.clf()
    if df.loc[df['Echinocytes'] != 0].empty == False:
        plt.plot(df['Echinocytes'])
        plt.title(title + 'for Echinocytes')
        plt.xlabel('Row number')
        plt.ylabel('Total Echinocyte count')
        plt.savefig(path + title + 'for Echinocytes plot.png')
        plt.clf()    
    if df.loc[df['Platelets'] != 0].empty == False:
        plt.plot(df['Platelets'])
        plt.title(title + 'for Platelets')
        plt.xlabel('Row number')
        plt.ylabel('Total Platelet count')
        plt.savefig(path + title + 'for Platelets plot.png')
        plt.clf()
    if df.loc[df['White blood cells'] != 0].empty == False:
        plt.plot(df['White blood cells'])
        plt.title(title + 'for White blood cells')
        plt.xlabel('Row number')
        plt.ylabel('Total White blood cell count')
        plt.savefig(path + title + 'for White blood cells plot.png')
        plt.clf()    
    if df.loc[df['Lymphocytes'] != 0].empty == False:
        plt.plot(df['Lymphocytes'])
        plt.title(title + 'for Lymphocytes')
        plt.xlabel('Row number')
        plt.ylabel('Total Lymphocyte count')
        plt.savefig(path + title + 'for Lymphocytes plot.png')
        plt.clf()    
    if df.loc[df['Monocytes'] != 0].empty == False:
        plt.plot(df['Monocytes'])
        plt.title(title + 'for Monocytes')
        plt.xlabel('Row number')
        plt.ylabel('Total Monocyte count')
        plt.savefig(path + title + 'for Monocytes plot.png')
        plt.clf()
    if df.loc[df['Neutrophils'] != 0].empty == False:
        plt.plot(df['Neutrophils'])
        plt.title(title + 'for Neutrophils')
        plt.xlabel('Row number')
        plt.ylabel('Total Neutrophil count')
        plt.savefig(path + title + 'for Neutrophils plot.png')
        plt.clf()
    if df.loc[df['Lymphocytes (activated)'] != 0].empty == False:
        plt.plot(df['Lymphocytes (activated)'])
        plt.title(title + 'for Lymphocytes (activated)')
        plt.xlabel('Row number')
        plt.ylabel('Total Lymphocyte (activated) count')
        plt.savefig(path + title + 'for Lymphocytes (activated) plot.png')
        plt.clf()
    if df.loc[df['Monocytes (activated)'] != 0].empty == False:
        plt.plot(df['Monocytes (activated)'])
        plt.title(title + 'for Monocytes (activated)')
        plt.xlabel('Row number')
        plt.ylabel('Total Monocyte (activated) count')
        plt.savefig(path + title + 'for Monocytes (activated) plot.png')
        plt.clf()
    if df.loc[df['Neutrophils (activated)'] != 0].empty == False:
        plt.plot(df['Neutrophils (activated)'])
        plt.title(title + 'for Neutrophils (activated)')
        plt.xlabel('Row number')
        plt.ylabel('Total Neutrophil (activated) count')
        plt.savefig(path + title + 'for Neutrophils (activated) plot.png')
        plt.clf()
  
def get_images(folder):
    '''Returns a list of images in a folder'''
    images = []
    for image in os.listdir(folder):
        if image.endswith(".jpg"):
            images.append(folder + image)
    return images

if __name__ == '__main__':
    folder = '/home/as-hunt/test_1/'
    out_path = folder + 'out/'
    x = 250
    obj_data = '/home/as-hunt/Etra-Space/Diffy-10k/obj.data'
    yolo_cfg = '/home/as-hunt/Etra-Space/Diffy-10k/yolov4.cfg'
    weights = '/home/as-hunt/Etra-Space/Diffy-10k/backup/yolov4_10000.weights'
    obj_names = '/home/as-hunt/Etra-Space/Diffy-10k/obj.names'
    if fist_run(folder) == True:
        check_data(folder)
        pre(folder, 'test.txt')
        darknet_test(obj_data, yolo_cfg, weights, folder + 'test.txt', out_path + 'results.txt')
    read_results(out_path + 'results.txt', obj_names, out_path)
    interpret_smaller(split_images_and_csv(get_images(folder), out_path + 'results.csv', x), out_path)
    plot_the_plot(out_path + 'res.csv', f'Comparative plot for {x}', out_path)
    