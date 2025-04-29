import os, cv2, random
import numpy as np
from dimentions import pixel_area_um, margin_error_um

def distinguish_RBCs_from_nucleated_cells(contours, img_gray):
    # Calculate the mean gray value of all located single cells images
    Mg = np.mean(img_gray)
    
    RBCs = []
    nucleated_cells = []
    
    for contour in contours:
        # Calculate the mean gray value of each single cell image
        mask = np.zeros_like(img_gray)
        cv2.drawContours(mask, [contour], 0, 255, -1)
        G = np.mean(img_gray[mask == 255])
        
        # Calculate the ratio of G to Mg
        ratio = G / Mg
        
        # If the ratio is greater than 0.8, it's an RBC, else a nucleated cell
        if ratio > 0.8:
            RBCs.append(contour)
        else:
            nucleated_cells.append(contour)
    
    return RBCs, nucleated_cells

def calculate_RBC_area(contour, Smean, Pmean):
    # Calculate the minimum enclosing circle https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8822214/
    (x, y), r = cv2.minEnclosingCircle(contour)
    
    # Calculate the area of the minimum enclosing circle
    Sr = np.pi * r * r
    
    # Calculate the area of the selected RBC
    Si = Sr * Pmean * Pmean
    
    return Si, Sr

def process_outer_contours(outer_contours, Smean, Pmean, a=0.3, b=5):
    # Calculate Smean
    areas = [cv2.contourArea(contour) for contour in outer_contours]
    pending_contour_index = np.argmax(areas)
    Smean = np.mean(np.delete(areas, pending_contour_index))
    
    effective_contours = []
    RBCs = []
    
    for contour in outer_contours:
        # Skip pending contour
        if contour is outer_contours[pending_contour_index]:
            continue
        
        # Calculate area of contour
        area = cv2.contourArea(contour)
        
        # Check if contour is effective
        if a * Smean < area < b * Smean:
            effective_contours.append(contour)
            
            # Check if it's a single cell or multiple cells merging
            if area > b * Smean:
                RBCs.append(contour)
    
    return effective_contours, RBCs

def extract_outer_contours(image):
    # Assuming you already have a processed binary image where cell regions are highlighted
    # Use the findContours method to extract contours
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def extract_area(contour):
    # Calculate the minimum enclosing circle
    (x, y), r = cv2.minEnclosingCircle(contour)
    
    # Calculate the area of the minimum enclosing circle
    Sr = np.pi * r * r
    
    # Calculate the area of the selected RBC
    Si = Sr * Pmean * Pmean
    
    return Si, Sr

def read_image(image_path):
    img = cv2.imread(image_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img, img_gray

def convert_to_um(area):
    return area * pixel_area_um

def process_image(image_path):
    img, img_gray = read_image(image_path)
    outer_contours = extract_outer_contours(img_gray)
    # print(outer_contours)
    RBC_areas = []
    for contour in outer_contours:
        Si, Sr = calculate_RBC_area(contour, Smean=100, Pmean=0.9)
        RBC_areas.append(Si)
    average_RBC_area = np.mean(RBC_areas)
    average_RBC_area = round(convert_to_um(average_RBC_area), 4)
    return average_RBC_area

def process_folder(folder_path):
    image_paths = [os.path.join(folder_path, image_name) for image_name in os.listdir(folder_path)]
    average_RBC_areas = []
    for image_path in image_paths:
        average_RBC_area = process_image(image_path)
        average_RBC_areas.append(average_RBC_area)
    return average_RBC_areas


def separate_rbcs(results_file, classes, save_directory, error_margin=0):
    """
    Crop images of a specific class from a list of images with annotations with a margin of error.

    Args:
    - images_annotations: A list of tuples containing image paths and corresponding annotations
                          (image, class, top_x, top_y, bottom_x, bottom_y).
    - class_to_crop: The class label for which images will be cropped.
    - save_directory: Directory where cropped images will be saved.
    - margin: Margin of error to expand the bounding box (in pixels). Default is 0.

    Returns:
    - None
    """
    # Create output directory if it doesn't exist
    os.makedirs(save_directory, exist_ok=True)
    images_annotations = open(results_file, 'r').readlines()
    for image_path, image_class, top_x, top_y, bottom_x, bottom_y in images_annotations:
        if image_class == classes:
            # Read image
            image = cv2.imread(image_path)
            if image is None:
                print(f"Error: Unable to read image {image_path}")
                continue            
            # Expand bounding box with margin
            top_x = max(0, top_x - margin_error_um)
            top_y = max(0, top_y - margin_error_um)
            bottom_x = min(image.shape[1], bottom_x + margin_error_um)
            bottom_y = min(image.shape[0], bottom_y + margin_error_um)
            # Crop image
            cropped_image = image[top_y:bottom_y, top_x:bottom_x]
            # Generate output filename
            filename = os.path.basename(image_path)
            output_path = os.path.join(save_directory, f"{classes}_{random.randint(0, 1000000)}_{filename}")
            # Save cropped image
            cv2.imwrite(output_path, cropped_image)
            print(f"Image cropped and saved to: {output_path}")

def darknet_test(obj_data, yolo_cfg, weights, data_path, out_file):
    '''Runs the darknet detector test command'''
    os.system('darknet detector test ' + obj_data + ' ' + yolo_cfg + ' ' + weights + ' -dont_show -ext_output < ' + data_path  + ' > ' +  out_file +' 2>&1')

def import_and_filter_result_neo(input_file='/home/as-hunt/result.txt', results_file='results.txt', obj_names='/home/as-hunt/Etra-Space/white-thirds/obj.names'):
    '''Import's Yolo darknet detection results bouding boxes.

    This function does filters the result.txt file. 
    It removes bouding boxes that are outside the image and
    bouding boxes that are too close to the edge of the image.

      Args:
        input_file (str): The path to the results.txt file
        results_file (str): The path to the file to save the filtered results
        obj_names (str): The path to the obj.names file
        '''
    arry = []
    res = open(results_file, 'w')
    with open(obj_names, 'r') as f:
        for line in f:
            arry.append(line.rstrip())
    with open(input_file, 'r') as f:
        for line in f:
            if line[0:4] == '/hom':
                lin = res.split('/| ', line)
                li = filter(lambda a: '.jpg' in a, lin)
                l = list(li)[0][:-5]
                image_name = l
            elif (line[0:3] in arry) or (line[0:4] in arry ) == True:
                lin = re.split(':|%|t|w|h', line)
                if int(lin[4]) < 4:
                    pass
                elif int(lin[4]) > 412:
                    pass
                else:
                    if int(lin[6]) < 4:
                        pass
                    elif int(lin[6]) > 412:
                        pass
                    else:
                        classes = int(arry.index(lin[0]))
                        confidence = int((lin[1]))
                        if int(lin[4]) < 0:
                            left_x = 0
                        else:
                            left_x = int(lin[4])
                        if int(lin[6]) < 0:
                            top_y = 0
                        else:
                            top_y = int(lin[6])
                        width = int(lin[10])
                        height = int(lin[14][:-2])
                        bottom_y = top_y + height
                        right_x = left_x + width
                        if bottom_y < 0:
                            bottom_y = 0
                        if right_x > 416:
                            right_x = 416
                        if bottom_y < 4:
                            pass
                        elif bottom_y > 412:
                            pass
                        else:
                            if right_x > 412:
                                pass
                            elif right_x < 4:
                                pass
                            else:
                                res.write(image_name + ' ' + str(classes) + ' ' + str(left_x) + ' ' + str(top_y) + ' ' + str(right_x) + ' ' + str(bottom_y) + ' ' + str(confidence / 100) + ' \n')
            else:
                pass       

if __name__ == '__main__':
    path = '/home/as-hunt/fintest/n1/1/'
    data = path + 'data.txt'
    ai_folder = f'/home/as-hunt/Etra-Space/Diffy-10k/1/'
    obj_data = ai_folder + 'obj.data'
    yolo_cfg = ai_folder + 'yolov4.cfg'
    weights = ai_folder + 'backup/yolov4_final.weights'
    obj_names = ai_folder + 'obj.names'
    path_out = path + 'out/'
    out_file = path_out + 'results.txt'
    class_id = 'ERY'
    darknet_test(obj_data, yolo_cfg, weights, data , path_out+ 'result.txt')
    import_and_filter_result_neo(path_out+ 'result.txt' , out_file, obj_names)
    separate_rbcs(out_file, class_id, path_out, error_margin=int(margin_error_um))
    average_RBC_area = process_folder(path_out)
    print("Average area of RBCs:", average_RBC_area, " um^2")
    print("Margin error:", margin_error_um, " um^2")
