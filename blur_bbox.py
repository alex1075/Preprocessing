import os
import cv2
import shutil


def blur_bbox(file, annotations, save_path):
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
        print(ll)
        bbox. append(int(ll))
    # bbox = [int(i * 416) for i in annotations]
    print(bbox)
    x = bbox[0]
    y = bbox[1]
    w = bbox[2]
    h = bbox[3]
    tx = x - (w/2) 
    ty = y + (h/2)
    print(int(ty))
    bx = x + (w/2) 
    by = y - (h/2) 
    print(int(by))
    blur_x = int(tx)
    blur_y = int(ty)
    blur_width = int(w)
    blur_height = int(h)
    
    roi = img[int(by):int(ty), int(tx):int(bx)]
    print(roi.shape)
    blur_image = cv2.GaussianBlur(roi,(85,85),0)
    
    img[int(by):int(ty), int(tx):int(bx)] = blur_image
    
    # image = cv2.rectangle(img, (int(tx), int(ty)), (int(bx), int(by)), (1,1,1), -1)
    cv2.imwrite(save_path + name, img)



def blur_class(input_folder, output_folder):
    try:
        shutil.copy(input_folder + "classes.txt", output_folder)
    except:
        pass
    for file in os.listdir(input_folder):
        if file.endswith(".jpg"):
            if os.path.isfile(input_folder + file[:-4] + '.txt'):
                annot = open(input_folder + file[:-4]+'.txt')
                print(file)
                for line in annot:
                    print(line)
                    li = line.split(' ')
                    if li[0] == '0':
                        print("Class 0") 
                        annotation = [li[1], li[2], li[3], li[4][:-2]]
                        print(annotation)
                        blur_bbox(input_folder + file, annotation, output_folder)
                        try:
                            shutil.copy(input_folder + file[:-4]+'.txt', output_folder)
                        except:
                            pass
                    elif li[0] == '1':
                        print("Class 1")
                        annotation = [li[1], li[2], li[3], li[4]]
                        blur_bbox(input_folder + file, annotation, output_folder)
                        try:
                            shutil.copy(input_folder + file[:-4]+'.txt', output_folder)
                        except:
                            pass
                    elif li[0] == '2':
                        print("Class 2")
                        annotation = [li[1], li[2], li[3], li[4]]
                        blur_bbox(input_folder + file, annotation, output_folder)
                        try:
                            shutil.copy(input_folder + file[:-4]+'.txt', output_folder)
                        except:
                            pass
                    elif li[0] == '3':
                        print("Class 3")
                        annotation = [li[1], li[2], li[3], li[4]]
                        blur_bbox(input_folder + file, annotation, output_folder)
                        try:
                            shutil.copy(input_folder + file[:-4]+'.txt', output_folder)
                        except:
                            pass
                    elif li[0] == '4':
                        print("Class 4")
                        annotation = [li[1], li[2], li[3], li[4]]
                        blur_bbox(input_folder + file, annotation, output_folder)
                        try:
                            shutil.copy(input_folder + file[:-4]+'.txt', output_folder)
                        except:
                            pass
            else:
                pass

        else:
            pass

blur_class("output/","output/")