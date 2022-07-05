import os
import decimal

def modify_OTH_to_PLT_txt(file, path): 
    filoo = open(path + file, 'r+')
    lnb = 0
    for line in filoo:
        lin = line.split(' ')
        classes = str(lin[0])
        x1 = round(decimal.Decimal(lin[1]), 6) 
        y1 = round(decimal.Decimal(lin[2]), 6)
        x2 = round(decimal.Decimal(lin[3]), 6)
        y2 = round(decimal.Decimal(lin[4]), 6)
        if classes == '0':
            print('Changed OTH to PLT')
            classic = str('1')
            # delete current line from file
            filoo.seek(lnb)
            filoo.truncate()
            # write new line
            # sys.stdout.write(lnb)
            filoo.write(classic + ' ' + str(x1) + ' ' + str(y1) + ' ' + str(x2) + ' ' + str(y2)+ '\n')
        elif classes != '0':
            print('No change')
            pass
    filoo.close()



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


path = '/mnt/c/Users/Alexander Hunt/data/test/'
do_the_thing(path)