import shutil
import os
import random

def split_images_and_annotations(source_folder, destination_folders):
    '''Splits images and annotations from one main folder to multiple destination folders
    Args:
        source_folder: the folder containing the images and annotations
        destination_folders: a list of folders to copy the images and annotations to

    Returns:
        None
    '''
    # Create destination folders if they don't exist
    for folder in destination_folders:
        os.makedirs(folder, exist_ok=True)
    # Get a list of all image files in the source folder
    image_files = [f for f in os.listdir(source_folder) if f.endswith('.jpg')]
    for file in os.listdir(source_folder):
        if file == 'classes.txt': 
            classes = True
            break
        elif file == '_darknet.labels':
            shutil.copy(source_folder + '/' + file, source_folder + '/classes.txt')
            classes = True
            break
        else:
            classes = False
    # Shuffle the image files randomly
    random.shuffle(image_files)
    # Calculate the number of images in each split
    split_size = len(image_files) // len(destination_folders)
    # Copy images and annotations to the destination folders
    for i, folder in enumerate(destination_folders):
        start_index = i * split_size
        end_index = (i + 1) * split_size if i < len(destination_folders) - 1 else len(image_files)
        for j in range(start_index, end_index):
            image_file = image_files[j]
            annotation_file = image_file.replace('.jpg', '.txt')
            source_image_path = os.path.join(source_folder, image_file)
            source_annotation_path = os.path.join(source_folder, annotation_file)
            destination_image_path = os.path.join(folder, image_file)
            destination_annotation_path = os.path.join(folder, annotation_file)
            shutil.copy(source_image_path, destination_image_path)
            shutil.copy(source_annotation_path, destination_annotation_path)
            if classes == True:
                shutil.copy(source_folder + '/classes.txt', folder + '/classes.txt')

def combine_folders(source_folders, destination_folder):
    ''' Combines multiple folders into one
    Args:
        source_folders: a list of folders to copy the images and annotations from
        destination_folder: the folder to copy the images and annotations to

    Returns:
        None    
    '''
    # Create destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)
    # Iterate over each source folder
    for source_folder in source_folders:
        # Get a list of all image files in the source folder
        image_files = [f for f in os.listdir(source_folder) if f.endswith('.jpg')]
        for file in os.listdir(source_folder):
             if file == 'classes.txt': 
                 shutil.copy(source_folder + '/' + file, destination_folder + '/classes.txt')
             elif file == '_darknet.labels':
                shutil.copy(source_folder + '/' + file, destination_folder + '/classes.txt')
             else:
                 pass
        # Copy images and annotations to the destination folder
        for image_file in image_files:
            annotation_file = image_file.replace('.jpg', '.txt')
            source_image_path = os.path.join(source_folder, image_file)
            source_annotation_path = os.path.join(source_folder, annotation_file)
            destination_image_path = os.path.join(destination_folder, image_file)
            destination_annotation_path = os.path.join(destination_folder, annotation_file)
            shutil.copy(source_image_path, destination_image_path)
            shutil.copy(source_annotation_path, destination_annotation_path)

def split_to_X_folders(source_folder, destination_folder, number=int):
    '''Split a folder into X folders
    Args:
        source_folder: the folder to split
        destination_folder: the folder to copy the images and annotations to
        number: the number of folders to split into

    Returns:
        None
    '''
    destination_folders = [f"{destination_folder}/f{i+1}" for i in range(number)]
    split_images_and_annotations(source_folder, destination_folders)            

def combine_three_folders(source_folders, destination_folder, n1=int, n2=int, n3=int, n4=int, n5=int, n6=int, n7=int, n8=int, n9=int, n10=int):
    '''Combine X folders into one
    Args:
        source_folders: a list of folders to copy the images and annotations from
        destination_folder: the folder to copy the images and annotations to
        number: the number of folders to combine

    Returns:
        None
    '''
    source_folders = [f"{source_folders}/f{n1}", f"{source_folders}/f{n2}", f"{source_folders}/f{n3}"]
    combine_folders(source_folders, destination_folder)    

def train_5_fold_validation(folder_with_all_data, save_path, upper_range=10000, model="/home/as-hunt/Etra-Space/cfg/yolov4.conv.137", args=" -mjpeg_port 8090 -clear -dont_show"):
    # folder_with_all_data = check_full_path(folder_with_all_data)
    # save_path = check_full_path(save_path)
    split_to_X_folders(folder_with_all_data, folder_with_all_data, 5)
    for i in range(1, 6, 1):
        print(i)
        try:
            os.mkdir(save_path + str(i))
        except: 
            pass    
        if i == 1:
            n1, n2, n3 = 1, 2, 3
            print(folder_with_all_data + f'f{n1}')
            combine_three_folders(folder_with_all_data, save_path + '1/train/', n1, n2, n3)
            shutil.copytree(folder_with_all_data + 'f4/', save_path + '1/valid/', dirs_exist_ok=True)
            shutil.copytree(folder_with_all_data + 'f5/', save_path + '1/test/', dirs_exist_ok=True)
            shutil.copy(save_path + '1/train/classes.txt', save_path + '1/obj.names')
        elif i == 2:
            n1, n2, n3 = 2, 3, 4
            combine_three_folders(folder_with_all_data, save_path + '2/train/', n1, n2, n3)
            shutil.copytree(folder_with_all_data + 'f5/', save_path + '2/valid/', dirs_exist_ok=True)
            shutil.copytree(folder_with_all_data + 'f1/', save_path + '2/test/', dirs_exist_ok=True)
            shutil.copy(save_path + '2/train/classes.txt', save_path + '2/obj.names')
        elif i == 3:
            n1, n2, n3 = 3, 4, 5
            combine_three_folders(folder_with_all_data, save_path + '3/train/', n1, n2, n3)
            shutil.copytree(folder_with_all_data + 'f1/', save_path + '3/valid/', dirs_exist_ok=True)
            shutil.copytree(folder_with_all_data + 'f2/', save_path + '3/test/', dirs_exist_ok=True)
            shutil.copy(save_path + '3/train/classes.txt', save_path + '3/obj.names')
        elif i == 4:
            n1, n2, n3 = 4, 5, 1
            combine_three_folders(folder_with_all_data, save_path + '4/train/', n1, n2, n3)
            shutil.copytree(folder_with_all_data + 'f2/', save_path + '4/valid/', dirs_exist_ok=True)
            shutil.copytree(folder_with_all_data + 'f3/', save_path + '4/test/', dirs_exist_ok=True)
            shutil.copy(save_path + '4/train/classes.txt', save_path + '4/obj.names')
        elif i == 5:
            n1, n2, n3 = 5, 1, 2
            print(folder_with_all_data + f'f{n1}')
            combine_three_folders(folder_with_all_data, save_path + '5/train/', n1, n2, n3)
            shutil.copytree(folder_with_all_data + 'f3/', save_path + '5/valid/', dirs_exist_ok=True)
            shutil.copytree(folder_with_all_data + 'f4/', save_path + '5/test/', dirs_exist_ok=True)
            shutil.copy(save_path + '5/train/classes.txt', save_path + '5/obj.names')    

def train_5_fold_val_compact(folder_with_all_data, save_path, upper_range=10000, model="/home/as-hunt/Etra-Space/cfg/yolov4.conv.137", args=" -mjpeg_port 8090 -clear -dont_show"):
    # folder_with_all_data = check_full_path(folder_with_all_data)
    # save_path = check_full_path(save_path)
    split_to_X_folders(folder_with_all_data, folder_with_all_data, 5)
    for i in range(1, 6, 1):
        print(i)
        try:
            os.mkdir(save_path + str(i))
        except: 
            pass    
        if i == 1:
            n1, n2, n3, n4, n5 = 1, 2, 3, 4, 5
        elif i == 2:
            n1, n2, n3, n4, n5 = 2, 3, 4, 5, 1
        elif i == 3:
            n1, n2, n3, n4, n5 = 3, 4, 5, 1, 2
        elif i == 4:
            n1, n2, n3, n4, n5 = 4, 5, 1, 2, 3
        elif i == 5:
            n1, n2, n3, n4, n5 = 5, 1, 2, 3, 4
        print(folder_with_all_data + f'f{n1}')
        combine_three_folders(folder_with_all_data, save_path + f'{n1}/train/', n1, n2, n3)
        shutil.copytree(folder_with_all_data + f'f{n4}/', save_path + f'{n1}/valid/', dirs_exist_ok=True)
        shutil.copytree(folder_with_all_data + f'f{n5}/', save_path + f'{n1}/test/', dirs_exist_ok=True)
        shutil.copy(save_path + f'{n1}/train/classes.txt', save_path + f'{n1}/obj.names')     

if __name__ == "__main__":
    # Replace these paths with the folders you want to combine and the destination folder
    source_folder = "/home/as-hunt/prob-mon/"
    destination = "/home/as-hunt/test/"
    train_5_fold_val_(source_folder, destination)