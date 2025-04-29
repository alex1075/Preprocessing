import os, re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def center_bbox(bbox):
    x1, y1, x2, y2 = bbox
    return str(round((x1 + x2) / 2)), str(round((y1 + y2) / 2))

def image_name_locator_2(image_name):
    i = -1
    j = i -1
    while image_name.split('_')[i].isnumeric() == True:
        while image_name.split('_')[j].isnumeric() == True:
            x = image_name.split('_')[i]
            y = image_name.split('_')[j]
            if int(x) >=3840 or int(y) >= 2160:
                x = image_name.split('_')[i+2]
                y = image_name.split('_')[j+2]
                break
            i -= 1
            j -= 1
    return x, y

def image_name_locator(image_name):
    x = image_name.split('_')[-1]
    y = image_name.split('_')[-2]
    if x == '0' and y == '0' and (image_name.split('_')[-3]).isnumeric() == True and (image_name.split('_')[-4]).isnumeric() == True:
        x = image_name.split('_')[-3]
        y = image_name.split('_')[-4]
        if x == '0' and y == '0' and (image_name.split('_')[-5]).isnumeric() == True and (image_name.split('_')[-6]).isnumeric() == True:
            x = image_name.split('_')[-5]
            y = image_name.split('_')[-6]
            if x == '0' and y == '0' and (image_name.split('_')[-7]).isnumeric() == True and (image_name.split('_')[-8]).isnumeric() == True:
                x = image_name.split('_')[-7]
                y = image_name.split('_')[-8]
                if x == '0' and y == '0' and (image_name.split('_')[-9]).isnumeric() == True and (image_name.split('_')[-10]).isnumeric() == True:
                    x = image_name.split('_')[-9]
                    y = image_name.split('_')[-10]
                    if x == '0' and y == '0' and (image_name.split('_')[-11]).isnumeric() == True and (image_name.split('_')[-12]).isnumeric() == True:
                        x = image_name.split('_')[-11]
                        y = image_name.split('_')[-12]
                        if x == '0' and y == '0' and (image_name.split('_')[-13]).isnumeric() == True and (image_name.split('_')[-14]).isnumeric() == True:
                            x = image_name.split('_')[-13]
                            y = image_name.split('_')[-14]
                            if x == '0' and y == '0' and (image_name.split('_')[-15]).isnumeric() == True and (image_name.split('_')[-16]).isnumeric() == True:
                                x = image_name.split('_')[-15]
                                y = image_name.split('_')[-16]
                                if x == '0' and y == '0' and (image_name.split('_')[-17]).isnumeric() == True and (image_name.split('_')[-18]).isnumeric() == True:
                                    x = image_name.split('_')[-17]
                                    y = image_name.split('_')[-18]
                                    if x == '0' and y == '0' and (image_name.split('_')[-19]).isnumeric() == True and (image_name.split('_')[-20]).isnumeric() == True:
                                        x = image_name.split('_')[-19]
                                        y = image_name.split('_')[-20]
                                        if x == '0' and y == '0' and (image_name.split('_')[-21]).isnumeric() == True and (image_name.split('_')[-22]).isnumeric() == True:
                                            x = image_name.split('_')[-21]
                                            y = image_name.split('_')[-22]
                                            if x == '0' and y == '0' and (image_name.split('_')[-23]).isnumeric() == True and (image_name.split('_')[-24]).isnumeric() == True:
                                                x = image_name.split('_')[-23]
                                                y = image_name.split('_')[-24]
                                                if x == '0' and y == '0' and (image_name.split('_')[-25]).isnumeric() == True and (image_name.split('_')[-26]).isnumeric() == True:
                                                    x = image_name.split('_')[-25]
                                                    y = image_name.split('_')[-26]
                                                    if x == '0' and y == '0' and (image_name.split('_')[-27]).isnumeric() == True and (image_name.split('_')[-28]).isnumeric() == True:
                                                        x = image_name.split('_')[-27]
                                                        y = image_name.split('_')[-28]
                                                        if x == '0' and y == '0' and (image_name.split('_')[-29]).isnumeric() == True and (image_name.split('_')[-30]).isnumeric() == True:
                                                            x = image_name.split('_')[-29]
                                                            y = image_name.split('_')[-30]
                                                            if x == '0' and y == '0' and (image_name.split('_')[-31]).isnumeric() == True and (image_name.split('_')[-32]).isnumeric() == True:
                                                                x = image_name.split('_')[-31]
                                                                y = image_name.split('_')[-32]
                                                                if x == '0' and y == '0' and (image_name.split('_')[-33]).isnumeric() == True and (image_name.split('_')[-34]).isnumeric() == True:
                                                                    x = image_name.split('_')[-33]
                                                                    y = image_name.split('_')[-34]
                                                                    if x == '0' and y == '0' and (image_name.split('_')[-35]).isnumeric() == True and (image_name.split('_')[-36]).isnumeric() == True:
                                                                        x = image_name.split('_')[-35]
                                                                        y = image_name.split('_')[-36]
                                                                        if x == '0' and y == '0' and (image_name.split('_')[-37]).isnumeric() == True and (image_name.split('_')[-38]).isnumeric() == True:
                                                                            x = image_name.split('_')[-37]
                                                                            y = image_name.split('_')[-38]
                                                                            if x == '0' and y == '0' and (image_name.split('_')[-39]).isnumeric() == True and (image_name.split('_')[-40]).isnumeric() == True:
                                                                                x = image_name.split('_')[-39]
                                                                                y = image_name.split('_')[-40]
                                                                                if x == '0' and y == '0' and (image_name.split('_')[-41]).isnumeric() == True and (image_name.split('_')[-42]).isnumeric() == True:
                                                                                    x = image_name.split('_')[-41]
                                                                                    y = image_name.split('_')[-42]
                                                                                    if x == '0' and y == '0' and (image_name.split('_')[-43]).isnumeric() == True and (image_name.split('_')[-44]).isnumeric() == True:
                                                                                        x = image_name.split('_')[-43]
                                                                                        y = image_name.split('_')[-44]
                                                                                        if x == '0' and y == '0' and (image_name.split('_')[-45]).isnumeric() == True and (image_name.split('_')[-46]).isnumeric() == True:
                                                                                            x = image_name.split('_')[-45]
                                                                                            y = image_name.split('_')[-46]
                                                                                            if x == '0' and y == '0' and (image_name.split('_')[-47]).isnumeric() == True and (image_name.split('_')[-48]).isnumeric() == True:
                                                                                                x = image_name.split('_')[-47]
                                                                                                y = image_name.split('_')[-48]
                                                                                                
    return x, y

def read_results(input_file='/home/as-hunt/result.txt', arry=['LYM', 'LYM-A']):
    res = []
    with open(input_file, 'r') as f:
        for line in f:
            if line[0:4] == '/hom':
                lin = re.split('/| ', line)
                li = filter(lambda a: '.jpg' in a, lin)
                l = list(li)[0][:-5]
                image_name = l
            elif (line[0:3] in arry) or (line[0:4] in arry ) == True:
                lin = re.split(':|%|t|w|h', line)
                if int(lin[4]) <= 0:
                    pass
                elif int(lin[4]) >= 416:
                    pass
                else:
                    if int(lin[6]) <= 0:
                        pass
                    elif int(lin[6]) >= 416:
                        pass
                    else:
                        if int(lin[4]) <= 0:
                            left_x = 0
                        else:
                            left_x = int(lin[4])
                        if int(lin[6]) <= 0:
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
                                bbox = (left_x, top_y, right_x, bottom_y)
                                res.append([image_name, bbox])
            else:
                pass  
    return res         

def cell_location(image_name, bbox):
    cent_x, cent_y = center_bbox(bbox)
    x, y = image_name_locator(image_name)
    # print(cent_x, cent_y, x, y)
    x = float(cent_x) + float(x)
    y = float(cent_y) + float(y)
    return str(x), str(y)

def calc_all_cell_locations(array):
    cell_locations = []
    for image_name, bbox in array:
        cell_locations.append(cell_location(image_name, bbox))
    return cell_locations

def save_cell_locations(cell_locations, output_file):
    df = pd.DataFrame(cell_locations, columns=['x', 'y'])
    # add to existing file
    if os.path.exists(output_file):
        df.to_csv(output_file, mode='a', header=False, index=False)
    else:
        df.to_csv(output_file, index=False)

def plot(cell_locations):
    df = pd.DataFrame(cell_locations, columns=['x', 'y'])
    plt.plot(df['x'], df['y'], 'ro')
    # set x0 to top left corner
    # set y to increase from top to bottom

    plt.savefig('cell_locations.png')

if __name__ == '__main__':
    # path_results = '/home/as-hunt/time_incubation_pannel/3h/ln/out/results.txt'
    # path_results = '/home/as-hunt/test2/out/results.txt'
    # path_results = '/home/as-hunt/test_1/temp/result.txt'
    # path_results = '/home/as-hunt/test/out/results.txt'
    # path_results = '/home/as-hunt/results/concentration_panel/100cfu/ln/out/results.txt'
    path_results = '/home/as-hunt/bact_test_1/out/results.txt'
    array = read_results(path_results, ['LYM', 'LYM-A', 'MON', 'MON-A', 'NEU', 'NEU-A', 'ECHY', 'ERY', 'PLT', 'WBC'])
    # print(array)
    cell_locations = calc_all_cell_locations(array)
    # print(cell_locations)
    save_cell_locations(cell_locations, 'cell_locations4.csv')
    plot(cell_locations)