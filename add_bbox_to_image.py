import os
import cv2
import decimal

"""
Classes:
0 - OTR
1 - PLT
2 - RBC
3 - RBC_overlap
4 - RBC_sidew
"""

# Take image from list in directory and add rectangle using bbox coordinates 
def add_bbox_to_image(image_path, classes, bbox_coordinates):
    image = cv2.imread(image_path)
    if classes == 0:
        color = (0, 0, 255)
    elif classes == 1:
        color = (0, 255, 0)
    elif classes == 2:
        color = (255, 0, 0)
    elif classes == 3:
        color = (0, 0, 0)
    elif classes == 4:
        color = (255, 255, 0)
    # elif classes == 5:
    #     color = (0, 255, 255)
    # else:
    #     color = (255, 255, 255)
    x1 = bbox_coordinates[0]
    y1 = bbox_coordinates[1]
    x2 = bbox_coordinates[2]
    y2 = bbox_coordinates[3]
    img = cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
    # cv2.imshow('image', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return img

def iterate_over_images(list, path_to_images, save_directory):
    fill = open(list, 'r')
    for line in fill:
        # print(file)
        print(line)
        lin = line.split(' ')
        # print(lin)
        image = lin[0]
        confidence = str(lin[1])
        x1 = decimal.Decimal(lin[2])
        y1 = decimal.Decimal(lin[3])
        x2 = decimal.Decimal(lin[4])
        y2 = decimal.Decimal(lin[5])
        # x1 = decimal.Decimal(x1 * 416)
        # y1 = decimal.Decimal(y1 * 416)
        # x2 = decimal.Decimal(x2 * 416)
        # y2 = decimal.Decimal(y2 * 416)
        # x1 = round(x1)
        # y1 = round(y1)
        # x2 = round(x2)
        # y2 = round(y2)
        print(image)
        print(confidence)
        bbox_coordinates = [x1, y1, x2, y2]  
        print(bbox_coordinates)
        img = add_bbox_to_image(path_to_images + image+ '.jpg', int(confidence), bbox_coordinates)
        cv2.imwrite(save_directory + image + '.jpg', img)


iterate_over_images('/home/as-hunt/Preprocessing/best_bbox.txt', '/home/as-hunt/Preprocessing/image_bboxes/', '/home/as-hunt/Preprocessing/image_bboxes/')
