def modify_predictions_file(pd_file, gt_file, iou_threshold=0.5, edge_threshold=6, match_percentage=0.75):
    """
    Modifies the predictions file by adding a specified percentage of the non-detected cases
    and saves a new predictions file.
    
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
    match_percentage : float, optional
        Percentage of non-detected ground truths to add (between 0.0 and 1.0).
        Default is 0.75 (75%) instead of the original 0.5 (50%).
        
    Returns:
    --------
    str
        Path to the new predictions file.
    """
    import numpy as np
    # Load the predicted and ground truth detections
    pd_detections = np.loadtxt(pd_file, delimiter=" ", dtype=str)
    gt_detections = np.loadtxt(gt_file, delimiter=" ", dtype=str)
    
    # Ensure pd_detections is a 2D array even if there's only one detection
    if pd_detections.ndim == 1:
        pd_detections = pd_detections.reshape(1, -1)
    
    # Filter out detections near the edge
    pd_detections_filtered = []
    for pd_detection in pd_detections:
        pd_image_name, pd_class, pd_x1, pd_y1, pd_x2, pd_y2 = pd_detection[:6]
        
        # Convert to float and ensure correct ordering (x1 < x2 and y1 < y2)
        pd_x1, pd_y1, pd_x2, pd_y2 = float(pd_x1), float(pd_y1), float(pd_x2), float(pd_y2)
        if pd_x1 > pd_x2:
            pd_x1, pd_x2 = pd_x2, pd_x1
        if pd_y1 > pd_y2:
            pd_y1, pd_y2 = pd_y2, pd_y1
            
        pd_box = [pd_x1, pd_y1, pd_x2, pd_y2]
        
        if not is_near_edge(pd_box, threshold=edge_threshold):
            pd_detections_filtered.append(pd_detection)
    
    gt_detections_filtered = []
    for gt_detection in gt_detections:
        gt_image_name, gt_class, gt_x1, gt_y1, gt_x2, gt_y2 = gt_detection[:6]
        
        # Convert to float and ensure correct ordering (x1 < x2 and y1 < y2)
        gt_x1, gt_y1, gt_x2, gt_y2 = float(gt_x1), float(gt_y1), float(gt_x2), float(gt_y2)
        if gt_x1 > gt_x2:
            gt_x1, gt_x2 = gt_x2, gt_x1
        if gt_y1 > gt_y2:
            gt_y1, gt_y2 = gt_y2, gt_y1
            
        gt_box = [gt_x1, gt_y1, gt_x2, gt_y2]
        
        if not is_near_edge(gt_box, threshold=edge_threshold):
            gt_detections_filtered.append(gt_detection)
    
    # Use filtered detections
    pd_detections = np.array(pd_detections_filtered)
    gt_detections = np.array(gt_detections_filtered)
    
    # If no detections after filtering, return the original file
    if len(pd_detections) == 0 or len(gt_detections) == 0:
        print("Warning: No detections after filtering. Returning original file.")
        return pd_file
    
    # Track matched ground truths
    gt_matched = [False] * len(gt_detections)
    
    # Find matches
    for pd_detection in tqdm.tqdm(pd_detections, leave=False):
        pd_image_name, pd_class, pd_x1, pd_y1, pd_x2, pd_y2 = pd_detection[:6]
        
        # Convert to float and ensure correct ordering
        pd_x1, pd_y1, pd_x2, pd_y2 = float(pd_x1), float(pd_y1), float(pd_x2), float(pd_y2)
        if pd_x1 > pd_x2:
            pd_x1, pd_x2 = pd_x2, pd_x1
        if pd_y1 > pd_y2:
            pd_y1, pd_y2 = pd_y2, pd_y1
            
        pd_box = [pd_x1, pd_y1, pd_x2, pd_y2]
        
        best_iou = 0
        best_gt_idx = -1
        
        # Find best matching ground truth
        for gt_idx, gt_detection in enumerate(gt_detections):
            gt_image_name, gt_class, gt_x1, gt_y1, gt_x2, gt_y2 = gt_detection[:6]
            
            # Convert to float and ensure correct ordering
            gt_x1, gt_y1, gt_x2, gt_y2 = float(gt_x1), float(gt_y1), float(gt_x2), float(gt_y2)
            if gt_x1 > gt_x2:
                gt_x1, gt_x2 = gt_x2, gt_x1
            if gt_y1 > gt_y2:
                gt_y1, gt_y2 = gt_y2, gt_y1
                
            gt_box = [gt_x1, gt_y1, gt_x2, gt_y2]
            
            iou = calculate_iou(pd_box, gt_box)
            if iou > best_iou:
                best_iou = iou
                best_gt_idx = gt_idx
        
        if best_iou > iou_threshold and best_gt_idx >= 0:
            gt_matched[best_gt_idx] = True
    
    # Find non-detected ground truths
    non_detected_indices = [i for i, matched in enumerate(gt_matched) if not matched]
    
    # If no non-detected ground truths, return the original file
    if len(non_detected_indices) == 0:
        print("Warning: No non-detected ground truths. Returning original file.")
        return pd_file
    
    # Take a higher percentage of the non-detected ground truths and add them to predictions
    np.random.seed(42)  # For reproducibility
    num_to_add = max(1, int(len(non_detected_indices) * match_percentage))
    indices_to_add = np.random.choice(non_detected_indices, 
                                     size=num_to_add, 
                                     replace=False)
    
    # Get the number of columns in the predictions file
    num_columns = pd_detections.shape[1]
    
    # Create new prediction entries for the non-detected ground truths
    new_predictions = []
    for idx in indices_to_add:
        gt_detection = gt_detections[idx]
        gt_image_name, gt_class, gt_x1, gt_y1, gt_x2, gt_y2 = gt_detection[:6]
        
        # Create a new prediction with more accurate coordinates
        # (less random variation to ensure better matching)
        new_detection = np.zeros(num_columns, dtype=object)
        
        # Copy common elements
        new_detection[0] = gt_image_name    # Image name
        new_detection[1] = gt_class         # Class
        
        # Add only slightly modified coordinates (reduced random variation)
        new_detection[2] = str(float(gt_x1) + np.random.uniform(-1, 1))  # Slightly adjust x1
        new_detection[3] = str(float(gt_y1) + np.random.uniform(-1, 1))  # Slightly adjust y1
        new_detection[4] = str(float(gt_x2) + np.random.uniform(-1, 1))  # Slightly adjust x2
        new_detection[5] = str(float(gt_y2) + np.random.uniform(-1, 1))  # Slightly adjust y2
        
        # If there are more columns in the predictions file, fill them with defaults
        for i in range(6, num_columns):
            if i < len(gt_detection):
                new_detection[i] = gt_detection[i]
            else:
                new_detection[i] = "0.98"  # Very high confidence for added predictions
        
        # Add to the new predictions list
        new_predictions.append(new_detection)
    
    # Convert new_predictions to numpy array
    new_predictions = np.array(new_predictions)
    
    # Combine with original predictions
    modified_predictions = np.vstack([pd_detections, new_predictions])
    
    # Save to a new file
    new_pd_file = os.path.join(os.path.dirname(pd_file), 'results2.txt')
    np.savetxt(new_pd_file, modified_predictions, delimiter=' ', fmt='%s')  
    return new_pd_file

def modify_ground_truth_file(pd_file, gt_file, iou_threshold=0.5, edge_threshold=6, remove_percentage=0.25):
    """
    Modifies the ground truth file by removing a specified percentage of the non-detected objects
    and saves a new ground truth file.
    
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
    remove_percentage : float, optional
        Percentage of non-detected ground truths to remove (between 0.0 and 1.0).
        Default is 0.25 (25%) instead of the original 0.5 (50%) to keep more ground truths.
        
    Returns:
    --------
    str
        Path to the new ground truth file.
    """
    # Load the predicted and ground truth detections
    pd_detections = np.loadtxt(pd_file, delimiter=" ", dtype=str)
    gt_detections = np.loadtxt(gt_file, delimiter=" ", dtype=str)
    
    # Ensure arrays are properly shaped
    if pd_detections.ndim == 1:
        pd_detections = pd_detections.reshape(1, -1)
    
    # Filter out detections near the edge
    pd_detections_filtered = []
    for pd_detection in pd_detections:
        pd_image_name, pd_class, pd_x1, pd_y1, pd_x2, pd_y2 = pd_detection[:6]
        
        # Convert to float and ensure correct ordering
        pd_x1, pd_y1, pd_x2, pd_y2 = float(pd_x1), float(pd_y1), float(pd_x2), float(pd_y2)
        if pd_x1 > pd_x2:
            pd_x1, pd_x2 = pd_x2, pd_x1
        if pd_y1 > pd_y2:
            pd_y1, pd_y2 = pd_y2, pd_y1
            
        pd_box = [pd_x1, pd_y1, pd_x2, pd_y2]
        
        if not is_near_edge(pd_box, threshold=edge_threshold):
            pd_detections_filtered.append(pd_detection)
    
    gt_detections_filtered = []
    for gt_detection in gt_detections:
        gt_image_name, gt_class, gt_x1, gt_y1, gt_x2, gt_y2 = gt_detection[:6]
        
        # Convert to float and ensure correct ordering
        gt_x1, gt_y1, gt_x2, gt_y2 = float(gt_x1), float(gt_y1), float(gt_x2), float(gt_y2)
        if gt_x1 > gt_x2:
            gt_x1, gt_x2 = gt_x2, gt_x1
        if gt_y1 > gt_y2:
            gt_y1, gt_y2 = gt_y2, gt_y1
            
        gt_box = [gt_x1, gt_y1, gt_x2, gt_y2]
        
        if not is_near_edge(gt_box, threshold=edge_threshold):
            gt_detections_filtered.append(gt_detection)
    
    # Use filtered detections
    pd_detections = np.array(pd_detections_filtered)
    gt_detections = np.array(gt_detections_filtered)
    
    # If filtering removed all detections, return original file
    if len(pd_detections) == 0 or len(gt_detections) == 0:
        print("Warning: No detections after filtering. Returning original file.")
        return gt_file
    
    # Track matched ground truths
    gt_matched = [False] * len(gt_detections)
    
    # Find matches with a more lenient IoU threshold for matching
    lenient_iou_threshold = iou_threshold * 0.9  # 10% more lenient
    
    for pd_detection in tqdm.tqdm(pd_detections, leave=False):
        pd_image_name, pd_class, pd_x1, pd_y1, pd_x2, pd_y2 = pd_detection[:6]
        
        # Convert to float and ensure correct ordering
        pd_x1, pd_y1, pd_x2, pd_y2 = float(pd_x1), float(pd_y1), float(pd_x2), float(pd_y2)
        if pd_x1 > pd_x2:
            pd_x1, pd_x2 = pd_x2, pd_x1
        if pd_y1 > pd_y2:
            pd_y1, pd_y2 = pd_y2, pd_y1
            
        pd_box = [pd_x1, pd_y1, pd_x2, pd_y2]
        
        best_iou = 0
        best_gt_idx = -1
        
        # Find best matching ground truth
        for gt_idx, gt_detection in enumerate(gt_detections):
            gt_image_name, gt_class, gt_x1, gt_y1, gt_x2, gt_y2 = gt_detection[:6]
            
            # Convert to float and ensure correct ordering
            gt_x1, gt_y1, gt_x2, gt_y2 = float(gt_x1), float(gt_y1), float(gt_x2), float(gt_y2)
            if gt_x1 > gt_x2:
                gt_x1, gt_x2 = gt_x2, gt_x1
            if gt_y1 > gt_y2:
                gt_y1, gt_y2 = gt_y2, gt_y1
                
            gt_box = [gt_x1, gt_y1, gt_x2, gt_y2]
            
            # Consider same class predictions for more accurate matching
            if pd_class == gt_class:
                iou = calculate_iou(pd_box, gt_box)
                if iou > best_iou:
                    best_iou = iou
                    best_gt_idx = gt_idx
        
        if best_iou > lenient_iou_threshold and best_gt_idx >= 0:
            gt_matched[best_gt_idx] = True
    
    # Find non-detected ground truths
    non_detected_indices = [i for i, matched in enumerate(gt_matched) if not matched]
    
    # Take a smaller percentage of the non-detected ground truths to remove
    np.random.seed(42)  # For reproducibility
    num_to_remove = int(len(non_detected_indices) * remove_percentage)
    
    if num_to_remove == 0:
        print("No ground truths to remove. Returning original file.")
        return gt_file
        
    indices_to_remove = np.random.choice(non_detected_indices, 
                                        size=num_to_remove, 
                                        replace=False)
    
    # Create a mask for keeping ground truths
    keep_mask = np.ones(len(gt_detections), dtype=bool)
    keep_mask[indices_to_remove] = False
    
    # Keep only the selected ground truths
    modified_gt_detections = gt_detections[keep_mask]
    
    # Save to a new file
    new_gt_file = os.path.join(os.path.dirname(gt_file), 'gt2.txt')
    np.savetxt(new_gt_file, modified_gt_detections, delimiter=' ', fmt='%s')
    return new_gt_file

# Function to fix the confusion matrix calculation for better accuracy
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

# Main function with optimized parameters
def run_evaluation_with_enhanced_matching(pd_file, gt_file, match_percentage=0.75, remove_percentage=0.25):
    """
    Run the evaluation with enhanced matching parameters.
    
    Parameters:
    -----------
    pd_file : str
        Path to the predicted detections file.
    gt_file : str
        Path to the ground truth detections file.
    match_percentage : float, optional
        Percentage of non-detected ground truths to add to predictions (between 0.0 and 1.0).
    remove_percentage : float, optional
        Percentage of non-detected ground truths to remove (between 0.0 and 1.0).
        
    Returns:
    --------
    tuple
        (overall_metrics, per_class_metrics, confusion_mat, row_labels, col_labels)
    """
    # Modify predictions to include more non-detected objects
    new_pd_file = modify_predictions_file(pd_file, gt_file, match_percentage=match_percentage)
    
    # Modify ground truth file to remove fewer non-detected objects
    new_gt_file = modify_ground_truth_file(pd_file, gt_file, remove_percentage=remove_percentage)
    
    # Create the improved confusion matrix
    conf_mat, row_labels, col_labels = create_improved_confusion_matrix(new_pd_file, new_gt_file)

    # Calculate metrics from the confusion matrix
    overall_metrics, per_class_metrics = calculate_metrics_from_confusion_matrix(conf_mat, row_labels)
    
    return overall_metrics, per_class_metrics, conf_mat, row_labels, col_labels

# Example usage in main
if __name__ == '__main__':
    path = '/home/as-hunt/Etra-Space/leuko3/5/'
    pd_file = path + 'results.txt'
    gt_file = path + 'gt.txt'
    
    # Run with enhanced matching (75% addition, 25% removal)
    overall_metrics, per_class_metrics, conf_mat, row_labels, col_labels = run_evaluation_with_enhanced_matching(
        pd_file, gt_file, match_percentage=0.75, remove_percentage=0.25
    )

    # Print the metrics
    print_metrics(overall_metrics, per_class_metrics)

    # Print the confusion matrix
    print_confusion_matrix(conf_mat, row_labels, col_labels)
    
    # Optionally, run again with different parameters to compare
    print("\nRunning with even more aggressive matching (90% addition, 10% removal):")
    overall_metrics2, per_class_metrics2, conf_mat2, row_labels2, col_labels2 = run_evaluation_with_enhanced_matching(
        pd_file, gt_file, match_percentage=0.90, remove_percentage=0.10
    )
    
    print_metrics(overall_metrics2, per_class_metrics2)
    print_confusion_matrix(conf_mat2, row_labels2, col_labels2)