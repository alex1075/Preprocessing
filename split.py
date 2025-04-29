import os
import shutil
import random

def split_images_and_annotations(source_folder, destination_folders):
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
    print('Classes: ', classes)               
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

# if __name__ == "__main__":
#     source_folder = "/home/as-hunt/prob-neu"
#     destination_folders = [f"/home/as-hunt/prob-neu/f{i+1}" for i in range(5)]
#     split_images_and_annotations(source_folder, destination_folders)


def combine_folders(source_folders, destination_folder):
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
    destination_folders = [f"{destination_folder}/f{i+1}" for i in range(number)]
    split_images_and_annotations(source_folder, destination_folders)

if __name__ == "__main__":
    # Replace these paths with the folders you want to combine and the destination folder
    source_folders_to_combine = ["/home/as-hunt/prob-neu/f1", "/home/as-hunt/prob-neu/f2", "/home/as-hunt/prob-neu/f3"]
    destination_combined_folder = "/home/as-hunt/prob-neu/train"

    combine_folders(source_folders_to_combine, destination_combined_folder)