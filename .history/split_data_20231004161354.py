import os
import tqdm
import pandas as pd
from sklearn.model_selection import train_test_split



def split_img_label(data_train,data_test, data_val, out):
    try:
        os.mkdir(out)
    except:
        pass
    folder_train = out + 'train'
    folder_test = out + 'test'
    folder_val = out + 'val'
    try:
        os.mkdir(out + 'train')
    except:
        pass
    try:
        os.mkdir(out + 'test')
    except:
        pass
    try:
        os.mkdir(out + 'val')
    except:
        pass
    train_ind=list(data_train.index)
    test_ind=list(data_test.index)
    val_ind=list(data_val.index)
    # Train folder
    print(train_ind)
    print(data_train)
    for i in tqdm.tqdm(range(len(train_ind))):
        os.system('cp '+data_train[train_ind[i]]+' '+ folder_train + '/'  +data_train[train_ind[i]].split('/')[-1])
        os.system('cp '+data_train[train_ind[i]].split('.jpg')[0]+'.txt'+'  '+ folder_train + '/'  +data_train[train_ind[i]].split('/')[-1].split('.jpg')[0]+'.txt')
    # Test folder
    for j in tqdm.tqdm(range(len(test_ind))):
        os.system('cp '+data_test[test_ind[j]]+' '+ folder_test + '/'  +data_test[test_ind[j]].split('/')[-1])
        os.system('cp '+data_test[test_ind[j]].split('.jpg')[0]+'.txt'+' ' + folder_test + '/'  +data_test[test_ind[j]].split('/')[-1].split('.jpg')[0]+'.txt')  
    # Val folder
    for k in tqdm.tqdm(range(len(val_ind))):
        os.system('cp '+data_val[val_ind[k]]+' '+ folder_val + '/'  +data_val[val_ind[k]].split('/')[-1])
        os.system('cp '+data_val[val_ind[k]].split('.jpg')[0]+'.txt'+'  '+ folder_val + '/'  +data_val[val_ind[k]].split('/')[-1].split('.jpg')[0]+'.txt')
    os.system('cp' + ' '+ PATH + '/'  +'classes.txt' + ' '+ folder_test + '/')
    os.system('cp' + ' '+ PATH + '/'  +'classes.txt' + ' '+ folder_train + '/')
    os.system('cp' + ' '+ PATH + '/'  +'classes.txt' + ' '+ folder_val + '/')

def prep_split(PATH = '/home/as-hunt/machine-code/temp/')
    list_img=[img for img in os.listdir(PATH) if img.endswith('.jpg')==True]
    list_txt=[img for img in os.listdir(PATH) if img.endswith('.txt')==True]
    path_img=[]
    for i in range (len(list_img)):
        path_img.append(PATH+list_img[i])       
    df=pd.DataFrame(path_img)
    # split 
    data_train, data_test, labels_train, labels_test = train_test_split(df[0], df.index, test_size=0.20, random_state=42)
    data_train, data_val, labels_train, labels_val = train_test_split(df[0], df.index, test_size=0.25, random_state=1) # 0.25 x 0.8 = 0.2
    # Function split 
    split_img_label(data_train,data_test,data_val,'/home/as-hunt/machine-code/temp3/')

i    