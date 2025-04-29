import sys
import math
from collections import defaultdict

def calculate_total_cell_statistics(input_file):
    # Dictionary to count cells per image (needed for standard deviation)
    cells_per_image = defaultdict(int)
    total_cells = 0
    
    try:
        with open(input_file, 'r') as file:
            for line in file:
                # Skip empty lines
                if line.strip() == "":
                    continue
                
                # Parse line: image_name class top_x top_y bottom_x bottom_y
                parts = line.strip().split()
                
                # Ensure the line has the expected format
                if len(parts) >= 6:  # Make sure we have enough columns
                    image_name = parts[0]
                    # Increment the count for this image
                    cells_per_image[image_name] += 1
                    total_cells += 1
                else:
                    print(f"Warning: Skipping malformed line: {line.strip()}")
        
        # Calculate the average and standard deviation
        if cells_per_image:
            total_images = len(cells_per_image)
            average = total_cells / total_images
            
            # Calculate standard deviation 
            cell_counts = list(cells_per_image.values())
            variance = sum((x - average) ** 2 for x in cell_counts) / total_images
            std_dev = math.sqrt(variance)
            
            print(f"Total images: {total_images}")
            print(f"Total cells: {total_cells}")
            print(f"Average cells per image: {average:.2f} ± {std_dev:.2f}")
            
        else:
            print("No valid data found in the file.")
            
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_cells.py input_file.txt")
        # Default file if no argument provided
        input_file = "/home/as-hunt/Etra-Space/stim2/1/gt.txt"
        calculate_total_cell_statistics(input_file)
    else:
        calculate_total_cell_statistics(sys.argv[1])