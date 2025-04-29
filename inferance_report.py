import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd   
import scienceplots

def inference_report(repot_txt, save_name='areas.png', labels=["Echinocyte", "Erythrocyte", "Lymphocyte", "Monocyte", "Neutrophil", "Platelet"]):
    
    '''Plots the areas of the bounding boxes in the ground truth and prediction from txt summary files'''
    pdchaart = []
    confi = []
    pd_array = []
    scatter = []
    cliss = []
    dfp = []
    classesp = []
    listed = open(repot_txt, 'r')
    for line in listed:
        li = line.split(' ')
        name = li[0]
        classes = li[1]
        bbox = [int(li[2]), int(li[3]), int(li[4]), int(li[5])]
        confidence = li[6]
        pd_array.append([name, bbox, classes, confidence])
    for item in pd_array:
        name = item[0]
        bbox = item[1]
        classes = item[2]
        confidence = item[3]
        pdchaart.append([classes, (abs(int(bbox[2]) - int(bbox[0])) * abs(int(bbox[3]) - int(bbox[1])))])
        classesp.append(labels[int(classes)])
        confi.append(confidence)
        cliss.append(classes)
        dfp.append(float(abs(int(bbox[2]) - int(bbox[0])) * abs(int(bbox[3]) - int(bbox[1]))))
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]
        scatter.append([int(width), int(height), str(labels[int(classes)]), float(confidence)])
    fig, axs = plt.subplots(3)        
    fig.set_size_inches(10, 16)

    

    confi = [float(i) for i in confi]
    plt.style.use(['science', 'no-latex'])
    df = pd.DataFrame({'Class':cliss, 'Area':dfp}, columns=["Class", "Area"])
    sns.violinplot(data=df, cut=0, x='Class', y='Area', inner='box', scale='count', split=True, ax=axs[0], order=["0", "1", "2", "3"], palette='muted')
    axs[0].set_xticklabels(["Lymphocytes", "Lymphocyte Activated", "Neutrophil", "Neutrohpils activated"])
    axs[0].set_title('Bbox Area Plotting per Class')
    axs[0].set(xlabel='Class', ylabel='Bbox Areas (pixels)')
    # classesp = [int(i) for i in classesp]
    du = pd.DataFrame({'Class':classesp, 'Area':dfp, 'Confidence':confi}, columns=["Class", "Area", "Confidence"])

    sns.scatterplot(data=du, x="Area", y="Confidence", ax=axs[1], hue='Class', palette='muted')
    # axs[1].legend(title='Cell type', labels=["Echinocyte", "Erythrocyte", "Lymphocyte", "Monocyte", "Neutrophil", "Platelet"])
    axs[1].set_title('Confidence by Bbox Areas coloured by Prediction Classes')
    axs[1].set(xlabel='Bbox Areas (pixels)', ylabel='Confidence')
    
    da = pd.DataFrame(scatter, columns=["Width", "Height", "Class", "Confidence"])
    sns.scatterplot(data=da, x="Width", y="Height",ax=axs[2], hue='Class', palette='muted')
    # sns.histplot(data=da, x='Width', y='Height', ax=axs[2], bins=50, pthresh=.1, cmap="mako")
    sns.kdeplot(data=da, x='Width', y='Height', ax=axs[2], levels=5, linewidths=1)
    # axs[2].legend(title='Cell type', labels=["Echinocyte", "Erythrocyte", "Lymphocyte", "Monocyte", "Neutrophil", "Platelet"])
    axs[2].set_title('Scatterplot')
    axs[2].set(xlabel='Width', ylabel='Height')
    print(da)
    plt.savefig(save_name+'_details.png', bbox_inches='tight')
    plt.clf()


def get_labels(obj_names):
    '''Returns a list of labels from the obj.names file'''
    labels = []
    with open(obj_names, 'r') as f:
        for line in f:
            labels.append(line.strip())
    return labels

if __name__ == '__main__':
#    print('2')
   labels = get_labels('/home/as-hunt/Etra-Space/LymNeu/1/obj.names')
   inference_report('/home/as-hunt/NEUStim/results.txt', 'NEU-stimmed', labels=labels)
