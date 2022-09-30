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
def add_bbox_to_image(image_path, classes, bbox_coordinates, confidence):
    image = cv2.imread(image_path)
    if classes == 0:
        color = (0, 0, 255)
    elif classes == 1:
        color = (0, 255, 0)
    # elif classes == 2:
    #     color = (255, 0, 0)
    # elif classes == 3:
    #     color = (0, 0, 0)
    # elif classes == 4:
    #     color = (255, 255, 0)
    # elif classes == 5:
    #     color = (0, 255, 255)
    # else:
    #     color = (255, 255, 255)
    x = bbox_coordinates[0]*416
    y = bbox_coordinates[1]*416
    w = bbox_coordinates[2]*416
    h = bbox_coordinates[3]*416
    x1 = int(x-(w/2))
    y1 = int(y+(h/2))
    x2 = int(x+(w/2))
    y2 = int(y-(h/2))
    # x1 = int(x)
    # y1 = int(y)
    # x2 = int(w)
    # y2 = int(y)
    # x1 = int(x)
    # y1 = int(y)
    # x2 = int(x+(w))
    # y2 = int(y+(h))
    print(x1)
    print(y1)
    print(x2)
    print(y2)
    image = cv2.rectangle(image, (x1, y1), (x2,y2), color, 2)
    print(confidence)
    # cv2.putText(image, str(confidence), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
    # cv2.putText(image, '.', (x2, y2), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    cv2.imshow('image', image)
    cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # return image

def iterate_over_images(list, path_to_images, save_directory):
    fill = open(list, 'r')
    for line in fill:
        # print(file)
        print(line)
        lin = line.split(' ')
        # print(lin)
        image = lin[0]
        classes = str(lin[1])
        x1 = int(lin[2])
        y1 = int(lin[3])
        x2 = int(lin[4])
        y2 = int(lin[5])
        confidence = lin[6]
        # x1 = decimal.Decimal(x1 * 416)
        # y1 = decimal.Decimal(y1 * 416)
        # x2 = decimal.Decimal(x2 * 416)
        # y2 = decimal.Decimal(y2 * 416)
        # x1 = round(x1)
        # y1 = round(y1)
        # x2 = round(x2)
        # y2 = round(y2)
        print(image)
        print(classes)
        bbox_coordinates = [x1, y1, x2, y2]  
        print(bbox_coordinates)
        img = add_bbox_to_image(path_to_images + image+ '.jpg', int(classes), bbox_coordinates, confidence)
        cv2.imwrite(save_directory + image + '.jpg', img)


# iterate_over_images('/home/as-hunt/test_pd.txt', '/home/as-hunt/', '/home/as-hunt/')
# iterate_over_images('/home/as-hunt/test_gt.txt', '/home/as-hunt/', '/home/as-hunt/')
# add_bbox_to_image('/Users/alexanderhunt/Preprocessing/output/test_2_832_1248.jpg', 0, [0.109378,0.034854,0.098556,0.079325], 2)

with open('/Users/alexanderhunt/Preprocessing/output/test_2_832_1248.txt', 'r') as f:
    for line in f:
        line = line.split(' ')
        x1 = line[1]
        x2 = line[2]
        x3 = line[3]
        x4 = line[4]
     
        