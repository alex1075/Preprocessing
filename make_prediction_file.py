import os
import decimal

file_weights = 'NoSidesNoBGNoBBoxTouchingSides_1.weights'
os.system('cd .. && ./darknet/darknet detector valid /home/as-hunt/Etra-Space/obj.data /home/as-hunt/Etra-Space/cfg/yolov4.cfg Saved_weights/'+file_weights+' -gpus 0')

p_file = open('predictons.txt', 'w')
results_folder = '/home/as-hunt/results/'
for file in os.listdir(results_folder):
    if file.endswith('.txt'):
        count = 0
        filoo = open(results_folder + file, 'r')
        if "OTR" in file:
                classes = 0
                for line in filoo:
                        print("OTR")
                        # print(file)
                        # print(line)
                        lin = line.split(' ')
                        # print(lin)
                        image = lin[0]
                        confidence = decimal.Decimal(lin[1])
                        x1 = decimal.Decimal(lin[2])
                        y1 = decimal.Decimal(lin[3])
                        x2 = decimal.Decimal(lin[4])
                        y2 = decimal.Decimal(lin[5])
                        x1 = decimal.Decimal(x1 / 416)
                        y1 = decimal.Decimal(y1 / 416)
                        x2 = decimal.Decimal(x2 / 416)
                        y2 = decimal.Decimal(y2 / 416)
                        p_file.write(image + ' ' + str(classes) + ' ' + str(x1) + ' ' + str(y1) + ' ' + str(x2) + ' ' + str(y2) + ' ' + str(confidence) + ' \n')
                        count += 1
                        print('Line ' + str(count) + ': ' + line)
                        # print(annotation) 
        elif "PLT" in file:
                classes = 1
                for line in filoo:
                        print("PLT")
                        # print(file)
                        # print(line)
                        lin = line.split(' ')
                        # print(lin)
                        image = lin[0]
                        confidence = decimal.Decimal(lin[1])
                        x1 = decimal.Decimal(lin[2])
                        y1 = decimal.Decimal(lin[3])
                        x2 = decimal.Decimal(lin[4])
                        y2 = decimal.Decimal(lin[5])
                        x1 = decimal.Decimal(x1 / 416)
                        y1 = decimal.Decimal(y1 / 416)
                        x2 = decimal.Decimal(x2 / 416)
                        y2 = decimal.Decimal(y2 / 416)
                        p_file.write(image + ' ' + str(classes) + ' ' + str(x1) + ' ' + str(y1) + ' ' + str(x2) + ' ' + str(y2) +  ' ' + str(confidence) + ' \n')
                        count += 1
                        print('Line ' + str(count) + ': ' + line)
                        # print(annotation) 
        elif "RBC.txt" in file:
                classes = 2
                for line in filoo:
                        print("RBC")
                        # print(file)
                        # print(line)
                        lin = line.split(' ')
                        # print(lin)
                        image = lin[0]
                        confidence = decimal.Decimal(lin[1])
                        x1 = decimal.Decimal(lin[2])
                        y1 = decimal.Decimal(lin[3])
                        x2 = decimal.Decimal(lin[4])
                        y2 = decimal.Decimal(lin[5])
                        x1 = decimal.Decimal(x1 / 416)
                        y1 = decimal.Decimal(y1 / 416)
                        x2 = decimal.Decimal(x2 / 416)
                        y2 = decimal.Decimal(y2 / 416)
                        p_file.write(image + ' ' + str(classes) + ' ' + str(x1) + ' ' + str(y1) + ' ' + str(x2) + ' ' + str(y2) + ' ' + str(confidence) + ' \n')
                        count += 1
                        print('Line ' + str(count) + ': ' + line)
                        # print(annotation) 
        elif "RBC_overlap" in file:
                classes = 3
                for line in filoo:
                        print("RBC_overlap")
                        # print(file)
                        # print(line)
                        lin = line.split(' ')
                        # print(lin)
                        image = lin[0]
                        confidence = decimal.Decimal(lin[1])
                        x1 = decimal.Decimal(lin[2])
                        y1 = decimal.Decimal(lin[3])
                        x2 = decimal.Decimal(lin[4])
                        y2 = decimal.Decimal(lin[5])
                        x1 = decimal.Decimal(x1 / 416)
                        y1 = decimal.Decimal(y1 / 416)
                        x2 = decimal.Decimal(x2 / 416)
                        y2 = decimal.Decimal(y2 / 416)
                        p_file.write(image + ' ' + str(classes) + ' ' + str(x1) + ' ' + str(y1) + ' ' + str(x2) + ' ' + str(y2) + ' ' + str(confidence) + ' \n')
                        count += 1
                        print('Line ' + str(count) + ': ' + line)
                        # print(annotation) 
        elif "RBC_sidew" in file:
                classes = 4
                for line in filoo:
                        print("RBC_sidew")
                        # print(file)
                        # print(line)
                        lin = line.split(' ')
                        # print(lin)
                        image = lin[0]
                        confidence = decimal.Decimal(lin[1])
                        x1 = decimal.Decimal(lin[2])
                        y1 = decimal.Decimal(lin[3])
                        x2 = decimal.Decimal(lin[4])
                        y2 = decimal.Decimal(lin[5])
                        x1 = decimal.Decimal(x1 / 416)
                        y1 = decimal.Decimal(y1 / 416)
                        x2 = decimal.Decimal(x2 / 416)
                        y2 = decimal.Decimal(y2 / 416)
                        p_file.write(image + ' ' + str(classes) + ' ' + str(x1) + ' ' + str(y1) + ' ' + str(x2) + ' ' + str(y2) + ' ' + str(confidence) + ' \n')
                        count += 1
                        print('Line ' + str(count) + ': ' + line)
                        # print(annotation) 
        filoo.close()  
p_file.close()
