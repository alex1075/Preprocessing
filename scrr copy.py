import numpy as np

coords = [0.0022507091346153,0.0003438197115384,0.0003987235576923,0.0003987115384615]
img_size = 416

transformed_coords = img_size * np.array(coords)
print(transformed_coords)
