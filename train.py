import os
import subprocess
from tqdm import tqdm
import pandas as pd
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from add_bbox import *
from confusion import *
from import_results import *
warnings.filterwarnings("ignore")

def train_easy(obj_data="/home/as-hunt/Etra-Space/white-thirds/obj.data", cfg="/home/as-hunt/Etra-Space/white-thirds/yolov4.cfg", model="/home/as-hunt/Etra-Space/cfg/yolov4.conv.137", args=" -mjpeg_port 8090 -clear -dont_show"):
    os.system("darknet detector train " + obj_data + ' ' + cfg + ' ' + model + ' ' + args )

def train_fancy(dir="/home/as-hunt/Etra-Space/white-thirds/", upper_range=10000, model="/home/as-hunt/Etra-Space/cfg/yolov4.conv.137", args=" -mjpeg_port 8090 -clear -dont_show"):
    li = []
    epoch = 0
    warnings.filterwarnings("ignore")
    obj_data = dir + "obj.data"
    cfg_10 = dir + "yolov4_10.cfg"
    backup = dir + "backup/"
    if not os.path.exists(backup):
        os.makedirs(backup)
    temp = dir + "temp/"
    if not os.path.exists(temp):
        os.makedirs(temp)    
    new_weights = model
    test_dir = dir + "test/"
    test_file = test_dir + "test.txt"
    temp_file = temp + "temp.txt"
    make_groud_truth(temp + 'gt.txt', test_dir)
    print("Initiating training for " + str(upper_range) + " epochs")
    print("Using starting weights: " + new_weights)
    for i in tqdm(range(0, upper_range, 10), desc="Training", unit="epochs"):
        os.system("darknet detector train " + obj_data + ' ' + cfg_10 + ' ' + new_weights + ' ' + args )
        epoch = i + 10
        subprocess.run(['mv', backup + 'yolov4_10_final.weights', backup + 'yolov4_' + str(epoch) + '.weights'])
        new_weights = backup + "yolov4_" + str(epoch) + ".weights"
        os.system("darknet detector test " + obj_data + " " + cfg_10 + " " + new_weights + " -dont_show -ext_output < " + test_file + " > " + temp_file + " 2>&1")
        import_results_neo(temp_file, temp + 'results_' + str(epoch) + '.txt')
        F1w, F1m, acc, precision_score_weighted, precision_score_macro, recall_score_weighted, recall_score_macro, fbeta05_score_weighted, fbeta05_score_macro, fbeta2_score_weighted, fbeta2_score_macro, = do_math_leukall(temp + 'gt.txt', temp + 'results_' + str(epoch) + '.txt', 'export_' + str(epoch), False)
        li.append([epoch, F1w, F1m, acc, precision_score_weighted, precision_score_macro, recall_score_weighted, recall_score_macro, fbeta05_score_weighted, fbeta05_score_macro, fbeta2_score_weighted, fbeta2_score_macro])
        os.system("rm " + temp + "results_" + str(epoch) + ".txt")
        if (epoch-10) % 50 == 0:
            # print("Saving weights")
            pass
        else:
            subprocess.run(['rm', backup + 'yolov4_' + str(epoch - 10) + '.weights'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(['rm', backup + 'chart_yolov4_' + str(epoch) + '.png'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    df = pd.DataFrame(li, columns = ['Epoch', 'F1_score_weighted', 'F1_score_macro', 'Accuracy', 'Precision_score_weighted', 'Precision_score_macro', 'Recall_score_weighted', 'Recall_score_macro', 'Fbeta05_score_weighted', 'Fbeta05_score_macro', 'Fbeta2_score_weighted', 'Fbeta2_score_macro'])    
    print("Training complete. Epochs: " + str(epoch))    
    print(df)
    pd.DataFrame(df).to_csv(dir + 'output.csv', index=False)


def make_the_graphs(csv_file="/home/as-hunt/Etra-Space/white-thirds/output.csv", dir="/home/as-hunt/Etra-Space/white-thirds/"):
    df = pd.read_csv(csv_file)
    fig, axs = plt.subplots(2, 2)        
    fig.set_size_inches(16, 10)
    sns.lineplot(x="Epoch", y="Accuracy", data=df, ax=axs[0, 0])
    axs[0, 0].set_title("Accuracy over epochs")
    axs[0, 0].set(xlabel='Epoch', ylabel='Accuracy (in %)')

    sns.lineplot(x="Epoch", y="F1_score_weighted", data=df, ax=axs[0, 1])
    axs[0, 1].set_title("F1 score over epochs")
    axs[0, 1].set(xlabel='Epoch', ylabel='F1 score (weighted, in %)')

    sns.lineplot(x="Epoch", y="Precision_score_weighted", data=df, ax=axs[1, 0])
    axs[1, 0].set_title("Precision score over epochs")
    axs[1, 0].set(xlabel='Epoch', ylabel='Precision score (weighted, in %)')

    sns.lineplot(x="Epoch", y="Recall_score_weighted", data=df, ax=axs[1, 1])
    axs[1, 1].set_title("Recall score over epochs")
    axs[1, 1].set(xlabel='Epoch', ylabel='Recall score (weighted, in %)')

    plt.savefig(dir + "Training output.png", bbox_inches='tight')
    plt.clf()
    fig, axs = plt.subplots(1, 1)
    sns.set_theme(style="whitegrid")
    dfm=df.melt('Epoch', var_name='cols',  value_name='vals')
    fig.set_size_inches(16, 10)
    sns.lineplot(data=dfm, x="Epoch", y="vals", hue='cols')
    plt.savefig(dir + "Training output together.png", bbox_inches='tight')
    # print(dfm)



if __name__ == "__main__":
    train_fancy("/home/as-hunt/Etra-Space/differential/", 10000, "/home/as-hunt/Etra-Space/differential/backup/differential_final.weights", " -mjpeg_port 8090 -clear -dont_show")
    # print("train.py executed directly")
    make_the_graphs("/home/as-hunt/Etra-Space/differential/output.csv","/home/as-hunt/Etra-Space/differential/")