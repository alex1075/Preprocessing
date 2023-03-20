import os
import cv2
import shutil


def blur_bbox_etended(file, annotations, save_path):
    """Blurs the bounding boxes of the predictions.
    
    Args:
        img: The image to blur.
        predictions: The predictions from the model.
        
    Returns:
        The image with the bounding boxes blurred.
    """
    bbox = []
    print(file)
    temp = file.split('/')
    name = temp[-1]
    img = cv2.imread(file)
    for i in annotations:
        ll = float(i) * 416
        # print(ll)
        bbox. append(int(ll))
    # bbox = [int(i * 416) for i in annotations]
    # print(bbox)
    x = bbox[0]
    y = bbox[1]
    w = bbox[2]
    h = bbox[3]
    tx = x - (w/2) - 10
    ty = y + (h/2) + 10
    # print(int(ty))
    bx = x + (w/2) + 10
    by = y - (h/2) - 10
    # print(int(by))
    blur_x = int(tx)
    blur_y = int(ty)
    blur_width = int(w)
    blur_height = int(h)
    
    roi = img[int(by):int(ty), int(tx):int(bx)]
    # print(roi.shape)
    blur_image = cv2.GaussianBlur(roi,(85,85),0)
    
    img[int(by):int(ty), int(tx):int(bx)] = blur_image
    
    # image = cv2.rectangle(img, (int(tx), int(ty)), (int(bx), int(by)), (1,1,1), -1)
    cv2.imwrite(save_path + name, img)

def blur_bbox(file, annotations, save_path):
    """Blurs the bounding boxes of the predictions.
    
    Args:
        img: The image to blur.
        predictions: The predictions from the model.
        
    Returns:
        The image with the bounding boxes blurred.
    """
    bbox = []
    # print(file)
    temp = file.split('/')
    name = temp[-1]
    img = cv2.imread(file)
    for i in annotations:
        ll = float(i) * 416
        # print(ll)
        bbox. append(int(ll))
    # bbox = [int(i * 416) for i in annotations]
    # print(bbox)
    x = bbox[0]
    y = bbox[1]
    w = bbox[2]
    h = bbox[3]
    tx = x - (w/2) 
    ty = y + (h/2) 
    # print(int(ty))
    bx = x + (w/2) 
    by = y - (h/2) 
    # print(int(by))
    blur_x = int(tx)
    blur_y = int(ty)
    blur_width = int(w)
    blur_height = int(h)
    
    roi = img[int(by):int(ty), int(tx):int(bx)]
    # print(roi.shape)
    blur_image = cv2.GaussianBlur(roi,(85,85),0)
    
    img[int(by):int(ty), int(tx):int(bx)] = blur_image
    
    # image = cv2.rectangle(img, (int(tx), int(ty)), (int(bx), int(by)), (1,1,1), -1)
    cv2.imwrite(save_path + name, img)


def blur_class(input_folder, output_folder):
    try:
        shutil.copy(input_folder + "classes.txt", output_folder)
    except:
        pass
    try:
        shutil.copy(input_folder + "_darknet.labels", output_folder)
    except:
        pass
    for file in os.listdir(input_folder):
        if file.endswith(".jpg"):
            if os.path.isfile(input_folder + file[:-4] + '.txt'):
                annot = open(input_folder + file[:-4]+'.txt')
                # print(file)
                for line in annot:
                    # print(line)
                    li = line.split(' ')
                    if li[0] == '0':
                        # print("Class 0") 
                        annotation = [li[1], li[2], li[3], li[4][:-2]]
                        print(annotation)
                        try:
                            blur_bbox_etended(input_folder + file, annotation, output_folder)
                        except:    
                            blur_bbox(input_folder + file, annotation, output_folder)
                        try:
                            shutil.copy(input_folder + file[:-4]+'.txt', output_folder)
                        except:
                            pass
                    elif li[0] == '1':
                        # print("Class 1")
                        annotation = [li[1], li[2], li[3], li[4]]
                        try:
                            blur_bbox_etended(input_folder + file, annotation, output_folder)
                        except:    
                            blur_bbox(input_folder + file, annotation, output_folder)
                        try:
                            shutil.copy(input_folder + file[:-4]+'.txt', output_folder)
                        except:
                            pass
                    elif li[0] == '2':
                        # print("Class 2")
                        annotation = [li[1], li[2], li[3], li[4]]
                        try:
                            blur_bbox_etended(input_folder + file, annotation, output_folder)
                        except:    
                            blur_bbox(input_folder + file, annotation, output_folder)
                        try:
                            shutil.copy(input_folder + file[:-4]+'.txt', output_folder)
                        except:
                            pass
                    elif li[0] == '3':
                        # print("Class 3")
                        annotation = [li[1], li[2], li[3], li[4]]
                        try:
                            blur_bbox_etended(input_folder + file, annotation, output_folder)
                        except:    
                            blur_bbox(input_folder + file, annotation, output_folder)
                        try:
                            shutil.copy(input_folder + file[:-4]+'.txt', output_folder)
                        except:
                            pass
                    elif li[0] == '4':
                        # print("Class 4")
                        annotation = [li[1], li[2], li[3], li[4]]
                        try:
                            blur_bbox_etended(input_folder + file, annotation, output_folder)
                        except:    
                            blur_bbox(input_folder + file, annotation, output_folder)
                        try:
                            shutil.copy(input_folder + file[:-4]+'.txt', output_folder)
                        except:
                            pass
            else:
                pass
        else:
            pass

# blur_class("output/","output/")

def blur_out_x_class(input_folder, output_folder):
    try:
        shutil.copy(input_folder + "classes.txt", output_folder)
    except:
        pass
    try:
        shutil.copy(input_folder + "_darknet.labels", output_folder)
    except:
        pass
    for file in os.listdir(input_folder):
        if file.endswith(".jpg"):
            if os.path.isfile(input_folder + file[:-4] + '.txt'):
                annot = open(input_folder + file[:-4]+'.txt')
                print(file)
                for line in annot:
                    # print(line)
                    li = line.split(' ')
                    if li[0] == '0':
                        # print("Class 0") 
                        annotation = [li[1], li[2], li[3], li[4][:-2]]
                        # print(annotation)
                        try:
                            try:
                                blur_bbox_etended(output_folder + file, annotation, output_folder)
                            except:
                                blur_bbox(output_folder + file, annotation, output_folder)    
                        except:
                            try:
                                blur_bbox_etended(input_folder + file, annotation, output_folder)
                            except:    
                                blur_bbox(input_folder + file, annotation, output_folder)
                    elif li[0] == '1':
                        # print("Class 1")
                        annotation = [li[1], li[2], li[3], li[4]]
                        try:
                            try:
                                blur_bbox_etended(output_folder + file, annotation, output_folder)
                            except:
                                blur_bbox(output_folder + file, annotation, output_folder)    
                        except:
                            try:
                                blur_bbox_etended(input_folder + file, annotation, output_folder)
                            except:    
                                blur_bbox(input_folder + file, annotation, output_folder)
                    elif li[0] == '2':
                        # print("Class 2")
                        annotation = [li[1], li[2], li[3], li[4]]
                        try:
                            try:
                                blur_bbox_etended(output_folder + file, annotation, output_folder)
                            except:
                                blur_bbox(output_folder + file, annotation, output_folder)    
                        except:
                            try:
                                blur_bbox_etended(input_folder + file, annotation, output_folder)
                            except:    
                                blur_bbox(input_folder + file, annotation, output_folder)
                    elif li[0] == '3':
                        # print("Class 3")
                        annotation = [li[1], li[2], li[3], li[4]]
                        print(li[0], li[1], li[2], li[3], li[4])
                        cent_x = int(float(li[1]) * 416)
                        print(cent_x)
                        cent_y = int(float(li[2]) * 416)
                        print(cent_y)
                        width = int(float(li[3]) * 416)
                        print(width)
                        height = int(float(li[4][:-2]) * 416)
                        print(height)
                        x1 = int(cent_x - (width / 2))
                        y1 = int(cent_y - (height / 2))
                        x2 = int(cent_x + (width / 2))
                        y2 = int(cent_y + (height / 2))
                        print(x1, y1, x2, y2)
                        if x1 <= 5 or y1 <= 5:
                            print("Out of bounds")
                        elif x2 >= 411 or y2 >= 411:
                            print("Out of bounds")
                        else:
                                with open(output_folder + file[:-4] + '.txt', 'a') as f:
                                    f.write(str(li[0]))
                                    print(li[0])
                                    f.write(' ')
                                    f.write(str(li[1]))
                                    print(li[1])
                                    f.write(' ')
                                    f.write(str(li[2]))
                                    print(li[2])
                                    f.write(' ')
                                    f.write(str(li[3]))
                                    print(li[3])
                                    f.write(' ')
                                    f.write(str(li[4]))
                                    print(li[4])
                                    f.write('\n')
                    elif li[0] == '4':
                        # print("Class 4")
                        annotation = [li[1], li[2], li[3], li[4]]
                        try:
                            try:
                                blur_bbox_etended(output_folder + file, annotation, output_folder)
                            except:
                                blur_bbox(output_folder + file, annotation, output_folder)    
                        except:
                            try:
                                blur_bbox_etended(input_folder + file, annotation, output_folder)
                            except:    
                                blur_bbox(input_folder + file, annotation, output_folder)
            else:
                pass
        else:
            pass

blur_out_x_class("../Downloads/Oldies/train/","output/")
