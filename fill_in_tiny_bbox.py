import cv2
import os 
import decimal

def fill_in_bbox(image, x1, y1, x2, y2):
    # get image shape and size
    image = cv2.imread(image)
    # height, width, channels = image.shape
    if x1 < 0:
        img = cv2.rectangle(image, (0, y1), (x2, y2), (128,128,128), -1)
    else: 
        img = image
    if y1 < 0:
        img = cv2.rectangle(image, (x1, 0), (x2, y2), (128,128,128), -1)
    else: 
        img = image
    if x2 > 416:
        img = cv2.rectangle(image, (width, y1), (width, y2), (128,128,128), -1)
    else: 
        img = image
    if y2 > 416:
        img = cv2.rectangle(image, (x1, height), (x2, height), (128,128,128), -1)
    else: 
        img = image
    return img

def interate_images(list, path):
    fill = open(list, 'r')
    for line in fill:
        # print(file)
        print(line)
        lin = line.split(' ')
        # print(lin)
        image = lin[0]
        classes = str(lin[1])
        x1 = decimal.Decimal(lin[2])
        y1 = decimal.Decimal(lin[3])
        x2 = decimal.Decimal(lin[4])
        y2 = decimal.Decimal(lin[5])
        confidence = decimal.Decimal(lin[6])
        x1 = decimal.Decimal(x1 * 416)
        y1 = decimal.Decimal(y1 * 416)
        x2 = decimal.Decimal(x2 * 416)
        y2 = decimal.Decimal(y2 * 416)
        x1 = round(x1)
        y1 = round(y1)
        x2 = round(x2)
        y2 = round(y2)
        print(x1, y1, x2, y2)
        img = fill_in_bbox(path+"/"+image+'.jpg', x1, y1, x2, y2)
        cv2.imwrite(path+image, img)

if __name__ == '__main__':
    interate_images('predictons.txt', 'image_bbox/')