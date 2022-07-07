import os
import decimal
import tempfile
from shutil import copyfile

def modify_OTH_to_PLT_txt(file, path): 
    filoo = open(path + file, 'r')
    filetmp = open("temp.txt", 'w')
    for line in filoo:
        lin = line.split(' ')
        # print(line)
        classes = str(lin[0])
        x1 = round(decimal.Decimal(lin[1]), 6) 
        y1 = round(decimal.Decimal(lin[2]), 6)
        x2 = round(decimal.Decimal(lin[3]), 6)
        y2 = round(decimal.Decimal(lin[4]), 6)
        if classes == '0':
            # print('Changed OTH to PLT')
            classic = str('1')
            # write new line
            # sys.stdout.write(lnb)
            filetmp.write(classic + ' ' + str(x1) + ' ' + str(y1) + ' ' + str(x2) + ' ' + str(y2)+ '\n')
        elif classes != '0':
            # print('No change')
            filetmp.write(classes + ' ' + str(x1) + ' ' + str(y1) + ' ' + str(x2) + ' ' + str(y2)+ '\n')
            # pass
    filoo.close()
    # os.system('cat temp.txt')
    os.system('cat temp.txt >>' + path + file)
    filetmp.close()
    os.system('rm temp.txt')




def do_the_thing(path):
    for file in os.listdir(path):
        # print(file)
        if file.endswith("train.txt"):
            pass
        elif file.endswith("test.txt"):
            pass
        elif file.endswith("valid.txt"):
            pass
        elif file.endswith(".txt"):
            modify_OTH_to_PLT_txt(file, path)


path = '/mnt/c/Users/Alexander Hunt/data/train/'
do_the_thing(path)