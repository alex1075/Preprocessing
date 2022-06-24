import re
file = open('ground_truth.txt', 'r')
for line in file.readlines():
    if re.search('\S', line): print (line),
file.close()