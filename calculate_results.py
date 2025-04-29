import os
import numpy as np
import tqdm

def calculate_iou(bb1, bb2):
    """
    Calculate the Intersection over Union (IoU) of two bounding boxes.
    Automatically corrects coordinate ordering if necessary.

    Parameters
    ----------
    bb1 : list
        [x1, y1, x2, y2]
        The (x1, y1) position is at the top left corner,
        the (x2, y2) position is at the bottom right corner
    bb2 : list
        [x1, y1, x2, y2]
        The (x1, y1) position is at the top left corner,
        the (x2, y2) position is at the bottom right corner

    Returns
    -------
    float
        in [0, 1]
    """
    # Make copies to avoid modifying the original arrays
    bb1 = bb1.copy()
    bb2 = bb2.copy()
    
    # Ensure coordinates are in the correct order (x1 <= x2, y1 <= y2)
    if bb1[0] > bb1[2]:
        bb1[0], bb1[2] = bb1[2], bb1[0]
    if bb1[1] > bb1[3]:
        bb1[1], bb1[3] = bb1[3], bb1[1]
    
    if bb2[0] > bb2[2]:
        bb2[0], bb2[2] = bb2[2], bb2[0]
    if bb2[1] > bb2[3]:
        bb2[1], bb2[3] = bb2[3], bb2[1]

    # determine the coordinates of the intersection rectangle
    x_left = max(bb1[0], bb2[0])
    y_top = max(bb1[1], bb2[1])
    x_right = min(bb1[2], bb2[2])
    y_bottom = min(bb1[3], bb2[3])

    if x_right < x_left or y_bottom < y_top:
        return 0.0

    # The intersection of two axis-aligned bounding boxes is always an
    # axis-aligned bounding box.
    intersection_area = (x_right - x_left + 1) * (y_bottom - y_top + 1)

    # compute the area of both AABBs
    bb1_area = (bb1[2] - bb1[0] + 1) * (bb1[3] - bb1[1] + 1)
    bb2_area = (bb2[2] - bb2[0] + 1) * (bb2[3] - bb2[1] + 1)

    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the intersection area
    iou = intersection_area / float(bb1_area + bb2_area - intersection_area)
    
    # Sanity check
    if not (0.0 <= iou <= 1.0):
        iou = max(0.0, min(1.0, iou))
    
    return iou

def is_near_edge(box, image_size=(416, 416), threshold=6):
    """
    Check if a bounding box is near the edge of an image.
    
    Parameters:
    -----------
    box : list
        [x1, y1, x2, y2] bounding box coordinates
    image_size : tuple, optional
        (width, height) of the image
    threshold : int, optional
        Distance threshold in pixels
        
    Returns:
    --------
    bool
        True if the box is near the edge, False otherwise
    """
    x1, y1, x2, y2 = box
    width, height = image_size
    
    # Check if any part of the box is within threshold pixels of any edge
    if (x1 < threshold or  # Left edge
        y1 < threshold or  # Top edge
        x2 > width - threshold or  # Right edge
        y2 > height - threshold):  # Bottom edge
        return True
    
    return False

def calculate_results(pd_file, gt_file, edge_threshold=6):
    # Load the predicted and ground truth detections
    pd_detections = np.loadtxt(pd_file, delimiter=" ", dtype=str)
    gt_detections = np.loadtxt(gt_file, delimiter=" ", dtype=str)
    
    # Filter out detections near the edge
    pd_detections_filtered = []
    for pd_detection in pd_detections:
        pd_image_name, pd_class, pd_x1, pd_y1, pd_x2, pd_y2 = pd_detection[:6]
        pd_box = [float(pd_x1), float(pd_y1), float(pd_x2), float(pd_y2)]
        if not is_near_edge(pd_box, threshold=edge_threshold):
            pd_detections_filtered.append(pd_detection)
    
    gt_detections_filtered = []
    for gt_detection in gt_detections:
        gt_image_name, gt_class, gt_x1, gt_y1, gt_x2, gt_y2 = gt_detection[:6]
        gt_box = [float(gt_x1), float(gt_y1), float(gt_x2), float(gt_y2)]
        if not is_near_edge(gt_box, threshold=edge_threshold):
            gt_detections_filtered.append(gt_detection)
    
    # Use filtered detections for calculations
    pd_detections = np.array(pd_detections_filtered)
    gt_detections = np.array(gt_detections_filtered)
    
    # Track which ground truths have been matched
    gt_matched = [False] * len(gt_detections)
    
    # Calculate the number of true positives and false positives
    tp, fp = 0, 0
    for pd_detection in tqdm.tqdm(pd_detections, leave=False):
        pd_image_name, pd_class, pd_x1, pd_y1, pd_x2, pd_y2 = pd_detection[:6]
        pd_box = [float(pd_x1), float(pd_y1), float(pd_x2), float(pd_y2)]
        
        best_iou = 0
        best_gt_idx = -1
        for gt_idx, gt_detection in enumerate(gt_detections):
            # Skip already matched ground truths
            if gt_matched[gt_idx]:
                continue
                
            gt_image_name, gt_class, gt_x1, gt_y1, gt_x2, gt_y2 = gt_detection[:6]
            gt_box = [float(gt_x1), float(gt_y1), float(gt_x2), float(gt_y2)]
            
            iou = calculate_iou(pd_box, gt_box)
            if iou > best_iou:
                best_iou = iou
                best_gt_idx = gt_idx
        
        if best_iou > 0.5 and best_gt_idx >= 0:
            if pd_class == gt_detections[best_gt_idx][1]:
                tp += 1
                gt_matched[best_gt_idx] = True
            else:
                fp += 1
        else:
            fp += 1
    
    # False negatives are ground truths that weren't matched
    fn = len(gt_detections) - sum(gt_matched)
    
    # Calculate precision, recall, and F1 score
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    
    return precision, recall, f1_score

def calculate_results_per_class(pd_file, gt_file, edge_threshold=6):
    # Load the predicted and ground truth detections
    pd_detections = np.loadtxt(pd_file, delimiter=" ", dtype=str)
    gt_detections = np.loadtxt(gt_file, delimiter=" ", dtype=str)
    
    # Filter out detections near the edge
    pd_detections_filtered = []
    for pd_detection in pd_detections:
        pd_image_name, pd_class, pd_x1, pd_y1, pd_x2, pd_y2 = pd_detection[:6]
        pd_box = [float(pd_x1), float(pd_y1), float(pd_x2), float(pd_y2)]
        if not is_near_edge(pd_box, threshold=edge_threshold):
            pd_detections_filtered.append(pd_detection)
    
    gt_detections_filtered = []
    for gt_detection in gt_detections:
        gt_image_name, gt_class, gt_x1, gt_y1, gt_x2, gt_y2 = gt_detection[:6]
        gt_box = [float(gt_x1), float(gt_y1), float(gt_x2), float(gt_y2)]
        if not is_near_edge(gt_box, threshold=edge_threshold):
            gt_detections_filtered.append(gt_detection)
    
    # Use filtered detections for calculations
    pd_detections = np.array(pd_detections_filtered)
    gt_detections = np.array(gt_detections_filtered)
    
    # Track which ground truths have been matched
    gt_matched = [False] * len(gt_detections)
    
    # Calculate the number of true positives and false positives
    class_tp, class_fp = {}, {}
    for pd_detection in tqdm.tqdm(pd_detections, leave=False):
        pd_image_name, pd_class, pd_x1, pd_y1, pd_x2, pd_y2 = pd_detection[:6]
        pd_box = [float(pd_x1), float(pd_y1), float(pd_x2), float(pd_y2)]
        
        best_iou = 0
        best_gt_idx = -1
        for gt_idx, gt_detection in enumerate(gt_detections):
            # Skip already matched ground truths
            if gt_matched[gt_idx]:
                continue
                
            gt_image_name, gt_class, gt_x1, gt_y1, gt_x2, gt_y2 = gt_detection[:6]
            gt_box = [float(gt_x1), float(gt_y1), float(gt_x2), float(gt_y2)]
            
            iou = calculate_iou(pd_box, gt_box)
            if iou > best_iou:
                best_iou = iou
                best_gt_idx = gt_idx
        
        if best_iou > 0.5 and best_gt_idx >= 0:
            if pd_class == gt_detections[best_gt_idx][1]:
                class_tp[pd_class] = class_tp.get(pd_class, 0) + 1
                gt_matched[best_gt_idx] = True
            else:
                class_fp[pd_class] = class_fp.get(pd_class, 0) + 1
        else:
            class_fp[pd_class] = class_fp.get(pd_class, 0) + 1
    
    # Calculate false negatives based on unmatched ground truths
    class_fn = {}
    for gt_idx, gt_detection in enumerate(gt_detections):
        if not gt_matched[gt_idx]:
            gt_class = gt_detection[1]
            class_fn[gt_class] = class_fn.get(gt_class, 0) + 1
    
    # Calculate precision, recall, and F1 score for each class
    class_metrics = {}
    for cls in tqdm.tqdm(set(class_tp.keys()).union(class_fp.keys()).union(class_fn.keys()), leave=False):
        tp = class_tp.get(cls, 0)
        fp = class_fp.get(cls, 0)
        fn = class_fn.get(cls, 0)
        
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
        
        class_metrics[cls] = {
            'precision': precision,
            'recall': recall,
            'f1_score': f1_score
        }
    
    return class_metrics

def create_confusion_matrix(pd_file, gt_file, iou_threshold=0.5, edge_threshold=6):
    """
    Create a confusion matrix for object detection results.
    Includes an extra column for non-detected objects.
    Filters out detections near the edge of the image.
    
    Parameters:
    -----------
    pd_file : str
        Path to the predicted detections file.
    gt_file : str
        Path to the ground truth detections file.
    iou_threshold : float, optional
        IoU threshold for matching detections.
    edge_threshold : int, optional
        Distance threshold in pixels for filtering objects near edges.
        
    Returns:
    --------
    tuple
        (confusion_matrix, row_labels, column_labels)
    """
    # Load the predicted and ground truth detections
    pd_detections = np.loadtxt(pd_file, delimiter=" ", dtype=str)
    gt_detections = np.loadtxt(gt_file, delimiter=" ", dtype=str)
    
    # Filter out detections near the edge
    pd_detections_filtered = []
    for pd_detection in pd_detections:
        pd_image_name, pd_class, pd_x1, pd_y1, pd_x2, pd_y2 = pd_detection[:6]
        pd_box = [float(pd_x1), float(pd_y1), float(pd_x2), float(pd_y2)]
        if not is_near_edge(pd_box, threshold=edge_threshold):
            pd_detections_filtered.append(pd_detection)
    
    gt_detections_filtered = []
    for gt_detection in gt_detections:
        gt_image_name, gt_class, gt_x1, gt_y1, gt_x2, gt_y2 = gt_detection[:6]
        gt_box = [float(gt_x1), float(gt_y1), float(gt_x2), float(gt_y2)]
        if not is_near_edge(gt_box, threshold=edge_threshold):
            gt_detections_filtered.append(gt_detection)
    
    # Use filtered detections for calculations
    pd_detections = np.array(pd_detections_filtered)
    gt_detections = np.array(gt_detections_filtered)
    
    # Get all unique classes
    gt_classes = sorted(list(set([det[1] for det in gt_detections])))
    pd_classes = sorted(list(set([det[1] for det in pd_detections])))
    all_classes = sorted(list(set(gt_classes).union(set(pd_classes))))
    
    # Create class to index mapping
    class_to_idx = {cls: i for i, cls in enumerate(all_classes)}
    
    # Initialize confusion matrix
    # Rows = GT classes, Columns = PD classes + "Non-detected"
    n_classes = len(all_classes)
    confusion_mat = np.zeros((n_classes, n_classes + 1), dtype=int)
    
    # Track matched ground truths - same as in calculate_results_per_class
    gt_matched = [False] * len(gt_detections)
    
    # For each prediction, find best matching ground truth - using same logic as metrics calculation
    for pd_detection in tqdm.tqdm(pd_detections, leave=False):
        pd_image_name, pd_class, pd_x1, pd_y1, pd_x2, pd_y2 = pd_detection[:6]
        pd_box = [float(pd_x1), float(pd_y1), float(pd_x2), float(pd_y2)]
        pd_idx = class_to_idx[pd_class]
        
        best_iou = 0
        best_gt_idx = -1
        
        # Find best matching ground truth
        for gt_idx, gt_detection in enumerate(gt_detections):
            # Skip already matched ground truths - critical to match metrics calculation
            if gt_matched[gt_idx]:
                continue
                
            gt_image_name, gt_class, gt_x1, gt_y1, gt_x2, gt_y2 = gt_detection[:6]
            gt_box = [float(gt_x1), float(gt_y1), float(gt_x2), float(gt_y2)]
            
            iou = calculate_iou(pd_box, gt_box)
            if iou > best_iou:
                best_iou = iou
                best_gt_idx = gt_idx
        
        if best_iou > iou_threshold and best_gt_idx >= 0:
            # True detection with correct or incorrect class
            gt_class = gt_detections[best_gt_idx][1]
            gt_idx = class_to_idx[gt_class]
            confusion_mat[gt_idx][pd_idx] += 1
            gt_matched[best_gt_idx] = True
        else:
            # False positive without a matching ground truth
            # This is a prediction that didn't match any ground truth
            # We could log this separately, but it's not part of the confusion matrix
            pass
    
    # Process unmatched ground truths (non-detected objects)
    for gt_idx, gt_detection in enumerate(gt_detections):
        if not gt_matched[gt_idx]:
            gt_class = gt_detection[1]
            gt_idx = class_to_idx[gt_class]
            # Last column represents "Non-detected"
            confusion_mat[gt_idx][n_classes] += 1
    
    # Prepare labels
    row_labels = all_classes
    col_labels = all_classes + ["Non-detected"]
    
    return confusion_mat, row_labels, col_labels

def calculate_metrics_from_confusion_matrix(confusion_mat, row_labels):
    """
    Calculate precision, recall, and F1 score from a confusion matrix.
    
    Parameters:
    -----------
    confusion_mat : numpy.ndarray
        Confusion matrix with rows as true classes and columns as predicted classes + "Non-detected"
    row_labels : list
        Class labels corresponding to rows in the confusion matrix
        
    Returns:
    --------
    tuple
        (overall_metrics, per_class_metrics)
    """
    n_classes = len(row_labels)
    per_class_metrics = {}
    
    # Calculate metrics for each class
    total_tp = 0
    total_fp = 0
    total_fn = 0
    
    for i, cls in enumerate(row_labels):
        # True positives: diagonal element (correct predictions)
        tp = confusion_mat[i][i]
        
        # False positives: sum of column i (excluding the diagonal element)
        fp = sum(confusion_mat[j][i] for j in range(n_classes) if j != i)
        
        # False negatives: sum of row i (excluding diagonal) + non-detected
        fn = sum(confusion_mat[i][j] for j in range(n_classes) if j != i) + confusion_mat[i][n_classes]
        
        # Calculate metrics
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
        
        per_class_metrics[cls] = {
            'precision': precision,
            'recall': recall,
            'f1_score': f1_score
        }
        
        # Accumulate for macro average
        total_tp += tp
        total_fp += fp
        total_fn += fn
    
    # Calculate overall metrics (macro average)
    overall_precision = sum(m['precision'] for m in per_class_metrics.values()) / n_classes
    overall_recall = sum(m['recall'] for m in per_class_metrics.values()) / n_classes
    overall_f1 = sum(m['f1_score'] for m in per_class_metrics.values()) / n_classes
    
    overall_metrics = {
        'precision': overall_precision,
        'recall': overall_recall,
        'f1_score': overall_f1
    }
    
    return overall_metrics, per_class_metrics

def print_metrics(overall_metrics, per_class_metrics):
    """Print metrics in a readable format."""
    print(f"Precision: {overall_metrics['precision']}, Recall: {overall_metrics['recall']}, F1 Score: {overall_metrics['f1_score']}")
    print(per_class_metrics)

def print_confusion_matrix(confusion_mat, row_labels, col_labels):
    """Print the confusion matrix in a readable format."""
    # Calculate column widths for better alignment
    col_width = max(max(len(str(x)) for x in row_labels), max(len(str(x)) for x in col_labels)) + 2
    
    # Print header row
    print(" " * col_width, end="")
    for label in col_labels:
        print(f"{label:{col_width}}", end="")
    print()
    
    # Print each row
    for i, label in enumerate(row_labels):
        print(f"{label:{col_width}}", end="")
        for j in range(len(col_labels)):
            print(f"{confusion_mat[i][j]:{col_width}}", end="")
        print()    

def create_improved_confusion_matrix(pd_file, gt_file, iou_threshold=0.5, edge_threshold=6):
    """
    Create an improved confusion matrix for object detection results with better
    handling of class matching.
    
    Parameters:
    -----------
    pd_file : str
        Path to the predicted detections file.
    gt_file : str
        Path to the ground truth detections file.
    iou_threshold : float, optional
        IoU threshold for matching detections.
    edge_threshold : int, optional
        Distance threshold in pixels for filtering objects near edges.
        
    Returns:
    --------
    tuple
        (confusion_matrix, row_labels, column_labels)
    """
    # Load the predicted and ground truth detections
    pd_detections = np.loadtxt(pd_file, delimiter=" ", dtype=str)
    gt_detections = np.loadtxt(gt_file, delimiter=" ", dtype=str)
    
    # Ensure arrays are properly shaped
    if pd_detections.ndim == 1:
        pd_detections = pd_detections.reshape(1, -1)
    if gt_detections.ndim == 1:
        gt_detections = gt_detections.reshape(1, -1)
    
    # Filter out detections near the edge
    pd_detections_filtered = []
    for pd_detection in pd_detections:
        pd_image_name, pd_class, pd_x1, pd_y1, pd_x2, pd_y2 = pd_detection[:6]
        pd_box = [float(pd_x1), float(pd_y1), float(pd_x2), float(pd_y2)]
        if not is_near_edge(pd_box, threshold=edge_threshold):
            pd_detections_filtered.append(pd_detection)
    
    gt_detections_filtered = []
    for gt_detection in gt_detections:
        gt_image_name, gt_class, gt_x1, gt_y1, gt_x2, gt_y2 = gt_detection[:6]
        gt_box = [float(gt_x1), float(gt_y1), float(gt_x2), float(gt_y2)]
        if not is_near_edge(gt_box, threshold=edge_threshold):
            gt_detections_filtered.append(gt_detection)
    
    # Use filtered detections for calculations
    pd_detections = np.array(pd_detections_filtered)
    gt_detections = np.array(gt_detections_filtered)
    
    # Get all unique classes
    gt_classes = sorted(list(set([det[1] for det in gt_detections])))
    pd_classes = sorted(list(set([det[1] for det in pd_detections])))
    all_classes = sorted(list(set(gt_classes).union(set(pd_classes))))
    
    # Create class to index mapping
    class_to_idx = {cls: i for i, cls in enumerate(all_classes)}
    
    # Initialize confusion matrix
    # Rows = GT classes, Columns = PD classes + "Non-detected"
    n_classes = len(all_classes)
    confusion_mat = np.zeros((n_classes, n_classes + 1), dtype=int)
    
    # Group gt detections by image for more efficient matching
    gt_by_image = {}
    for gt_idx, gt_detection in enumerate(gt_detections):
        img_name = gt_detection[0]
        if img_name not in gt_by_image:
            gt_by_image[img_name] = []
        gt_by_image[img_name].append((gt_idx, gt_detection))
    
    # Track matched ground truths
    gt_matched = [False] * len(gt_detections)
    
    # For each prediction, find best matching ground truth
    for pd_detection in tqdm.tqdm(pd_detections, leave=False):
        pd_image_name, pd_class, pd_x1, pd_y1, pd_x2, pd_y2 = pd_detection[:6]
        pd_box = [float(pd_x1), float(pd_y1), float(pd_x2), float(pd_y2)]
        pd_idx = class_to_idx[pd_class]
        
        best_iou = 0
        best_gt_idx = -1
        
        # Only check ground truths from the same image
        if pd_image_name in gt_by_image:
            for gt_idx, gt_detection in gt_by_image[pd_image_name]:
                # Skip already matched ground truths
                if gt_matched[gt_idx]:
                    continue
                    
                gt_class = gt_detection[1]
                gt_x1, gt_y1, gt_x2, gt_y2 = (float(gt_detection[2]), float(gt_detection[3]), 
                                             float(gt_detection[4]), float(gt_detection[5]))
                gt_box = [gt_x1, gt_y1, gt_x2, gt_y2]
                
                iou = calculate_iou(pd_box, gt_box)
                
                # Prioritize matching with same class
                if iou > best_iou:
                    best_iou = iou
                    best_gt_idx = gt_idx
        
        if best_iou > iou_threshold and best_gt_idx >= 0:
            # True detection with correct or incorrect class
            gt_class = gt_detections[best_gt_idx][1]
            gt_idx = class_to_idx[gt_class]
            confusion_mat[gt_idx][pd_idx] += 1
            gt_matched[best_gt_idx] = True
        else:
            # False positive without a matching ground truth
            # We could count this as a separate category, but for now we'll skip it
            pass
    
    # Process unmatched ground truths (non-detected objects)
    for gt_idx, gt_detection in enumerate(gt_detections):
        if not gt_matched[gt_idx]:
            gt_class = gt_detection[1]
            gt_idx = class_to_idx[gt_class]
            # Last column represents "Non-detected"
            confusion_mat[gt_idx][n_classes] += 1
    
    # Prepare labels
    row_labels = all_classes
    col_labels = all_classes + ["Non-detected"]
    
    return confusion_mat, row_labels, col_labels

# Example usage in main
if __name__ == '__main__':
    path = '/home/as-hunt/Etra-Space/Mono/2/'
    pd_file = path + 'results.txt'
    gt_file = path + 'gt.txt'
    
    # Evaluate with original files
    precision, recall, f1_score = calculate_results(pd_file, gt_file)
    print(f'Precision: {precision}, Recall: {recall}, F1 Score: {f1_score}')
    
    class_metrics = calculate_results_per_class(pd_file, gt_file)
    print(class_metrics)
    
    # Create and print confusion matrix
    conf_mat, row_labels, col_labels = create_improved_confusion_matrix(pd_file, gt_file)
    
    # Calculate metrics from the confusion matrix
    overall_metrics, per_class_metrics = calculate_metrics_from_confusion_matrix(conf_mat, row_labels)
    
    # Print the metrics
    print_metrics(overall_metrics, per_class_metrics)
    
    # Print the confusion matrix
    print("\nConfusion Matrix:")
    print_confusion_matrix(conf_mat, row_labels, col_labels)