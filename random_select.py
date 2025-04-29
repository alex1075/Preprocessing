import os

def random_select(path, k, obj_names, save_path):
    """Randomly select k images from dataset for each class."""
    with open(obj_names, 'r') as f:
        classes = f.readlines()
    classes = [c.strip() for c in classes]
    classes = sorted(classes)
    files = os.listdir(path)
    select = []
    for i in range(k):
        for j in range(len(classes)):
            select.append(j)
    # print(select)        
    while len(select) > 0:
        for file in files:
            # print(select)
            if file.endswith('.txt'):
                if file == 'classes.txt':
                    os.system('cp ' + path + file + ' ' + save_path + file)
                elif file == 'obj.names':
                    os.system('cp ' + path + file + ' ' + save_path + 'classes.txt')
                else:
                    with open(path + file, 'r') as f:
                        lines = f.readlines()
                    lines = [l.strip() for l in lines]    
                    lie = lines[0].split(' ')
                    # print(lie[0])
                    test = int(lie[0])
                    if test in select:
                        # print('tick')
                        os.system('cp ' + path + file + ' ' + save_path + file)
                        os.system('cp ' + path + file[:-4] + '.jpg' + ' ' + save_path + file[:-4] + '.jpg')
                        select.remove(test)
                    elif test not in select:
                        # print('tock')
                        continue


    
if __name__ == '__main__':
    path = '/home/as-hunt/machine-code/3/temp/'
    k = 10
    obj_names = '/home/as-hunt/Etra-Space/differential/obj.names'
    save_path = '/home/as-hunt/temp/'
    random_select(path, k, obj_names, save_path)    