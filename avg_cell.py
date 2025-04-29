def calculate_average_cells_per_image(file_path):
    with open(file_path, 'r') as file:
        image_counts = {}
        for line in file:
            parts = line.strip().split(',')
            image_name = parts[0]
            if image_name in image_counts:
                image_counts[image_name] += 1
            else:
                image_counts[image_name] = 1

        total_cells = sum(image_counts.values())
        number_of_images = len(image_counts)
        average_cells_per_image = total_cells / number_of_images

        return average_cells_per_image

# Replace 'your_file_path.txt' with the path to your actual file
file_path = '/home/as-hunt/time_incubation_pannel/3h/ln/out/results.txt'
# file_path = '/home/as-hunt/test2/out/results.txt'
# file_path = '/home/as-hunt/test_1/temp/result.txt'
# file_path = '/home/as-hunt/test/out/results.txt'
# file_path = '/home/as-hunt/results/concentration_panel/100cfu/ln/out/results.txt'
# file_path = '/home/as-hunt/bact_test_1/out/results.txt'
average = calculate_average_cells_per_image(file_path)
print(f'Average number of cells per image: {average:.2f}')
