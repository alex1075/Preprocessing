import cv2
import glob
import tqdm
import numpy as np

def detect_objects(image_path, net, classes):
    # Load image and get its dimensions
    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    # Create a blob from the image and perform a forward pass
    blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    output_layers = net.getUnconnectedOutLayersNames()
    detections = net.forward(output_layers)

    # Process the detections
    results = []
    for detection in detections:
        for obj in detection:
            scores = obj[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5:  # Adjust confidence threshold as needed
                center_x = int(obj[0] * width)
                center_y = int(obj[1] * height)
                box_width = int(obj[2] * width)
                box_height = int(obj[3] * height)

                results.append([
                    image_path,
                    class_id,
                    center_x,
                    center_y,
                    box_width,
                    box_height,
                    confidence
                ])

    return results


def load_net(model_weights, model_config, names_path):
    # Load the pre-trained YOLO model and corresponding classes
    net = cv2.dnn.readNet(model_weights, model_config)
    classes = open(names_path).read().strip().split('\n')
    return net, classes


def test_folder(folder_path, net, classes):
    # Specify the image file path
    image_paths = glob.glob(folder_path + "/*.jpg")

    # Perform object detection
    detections = []
    for image_path in tqdm.tqdm(image_paths, desc="Detecting objects"):
        detections += detect_objects(image_path, net, classes)
    file = open("resulty.txt", "w")
    # Print the results
    for detection in detections:
        image_name, class_id, top_x, top_y, bottom_x, bottom_y, confidence = detection
        file.write(str(image_name) + ' ' + str(class_id) + ' ' + str(top_x) + ' ' + str(top_y) + ' ' + str(bottom_x) + ' ' + str(bottom_y) + ' ' + str(confidence) + '\n')
    file.close()    
        

# Example usage:
if __name__ == "__main__":
    # Load the pre-trained YOLO model and corresponding classes
    model_weights = "/home/as-hunt/Etra-Space/Diffy/3/backup/yolov4_10_pass_3_500.weights"
    model_config = "Etra-Space/Diffy/3/yolov4_10_pass_3.cfg"
    coco_names = "/home/as-hunt/Etra-Space/Diffy/3/obj.names"

    net = cv2.dnn.readNet(model_weights, model_config)
    classes = open(coco_names).read().strip().split('\n')

    # Specify the image file path
    # image_path = "/home/as-hunt/Etra-Space/diff-yolov4/test/1hr-HEPES_1_1248_2080_jpg.rf.16d2b4eb2d76ac8dd9d25c17573ae24a.jpg"

    # Perform object detection
    # detections = detect_objects(image_path, net, classes)
    test_folder("Etra-Space/PHA-leuko/valid", net, classes)


