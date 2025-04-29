import os
import shutil

def combine_yolo_datasets(dataset1_path, dataset2_path, combined_path):
    # Create the combined dataset directory if it doesn't exist
    if not os.path.exists(combined_path):
        os.makedirs(combined_path)

    classes_1 = [line.rstrip() for line in open(dataset1_path + 'classes.txt', 'r')]
    classes_2 = [line.rstrip() for line in open(dataset2_path + 'classes.txt', 'r')]
    print('Classes in dataset 1:', classes_1)
    print('Classes in dataset 2:', classes_2)
    combine_classes = sorted(list(set(classes_1 + classes_2)))
    print('Combined classes:', combine_classes)
    with open(combined_path + 'classes.txt', 'w') as file:
        for cls in combine_classes:
            file.write(cls + '\n')

    # Copy the images and update the labels from dataset1 to the combined dataset
    for filename in os.listdir(dataset1_path):
        if filename.endswith('.jpg'):
            shutil.copy(dataset1_path + filename, combined_path + filename)
            # print(dataset1_path + filename[:-4] + '.txt')
            with open(dataset1_path + filename[:-4] + '.txt', 'r') as file:
                lines = file.readlines()
                for i in range(len(lines)):
                    line_parts = lines[i].split(' ')
                    # print(str(classes_1[int(line_parts[0])]) + ' -> ' + str(combine_classes.index(classes_1[int(line_parts[0])])))
                    lines[i] = str(combine_classes.index(classes_1[int(line_parts[0])])) + ' ' + line_parts[1] + ' ' + line_parts[2] + ' ' +line_parts[3] + ' ' + line_parts[4]
            with open(combined_path + filename[:-4] + '.txt', 'w') as file:
                for line in lines:
                    file.write(line)

    # Copy the images and labels from dataset2 to the combined dataset
    # for filename in os.listdir(dataset2_path):
    #     if filename.endswith('.jpg'):
    #         shutil.copy(dataset2_path + filename, combined_path + filename)
    #         # print(dataset2_path + filename[:-4] + '.txt')
    #         with open(dataset2_path + filename[:-4] + '.txt', 'r') as file:
    #             lines = file.readlines()
    #             for i in range(len(lines)):
    #                 line_parts = lines[i].split(' ')
    #                 # print(str(classes_2[int(line_parts[0])]) + ' -> ' + str(combine_classes.index(classes_2[int(line_parts[0])])))
    #                 lines[i] = str(combine_classes.index(classes_2[int(line_parts[0])])) + ' ' + line_parts[1] + ' ' + line_parts[2] + ' ' +line_parts[3] + ' ' + line_parts[4]
    #         with open(combined_path + filename[:-4] + '.txt', 'w') as file:
    #             for line in lines:
    #                 file.write(line)

    print('Combined dataset created at', combined_path)

if __name__ == '__main__':
    dataset_1 = '/home/as-hunt/mono/'
    dataset_2 = '/home/as-hunt/leukostim2/'
    output_path = '/home/as-hunt/out2/'
    combine_yolo_datasets(dataset_1, dataset_2, output_path)