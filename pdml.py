from pandas_ml import ConfusionMatrix
import pandas as pd

prediction = pd.read_csv("/home/as-hunt/Mini/result_run_3.txt",
                        delimiter = ' ')

prediction.to_csv('/home/as-hunt/predictions.csv',
                index = None)

def get_stats(ground_truth_file, prediction_file):
    filoo = open( ground_truth_file, 'r')
    actual = []
    for line in filoo:
        lin = line.split(',')
        # print(lin)
        image = lin[0]
        classes = (lin[1])
        actual.append(classes)
    filoo.close()
    filoo = open( prediction_file, 'r')
    predicted = []
    for line in filoo:
        lin = line.split(',')
        # print(lin)
        image = lin[0]
        classes = (lin[1])
        predicted.append(classes)
    filoo.close()
    y_actu = pd.Series(actual, name='Actual')
    y_pred = pd.Series(predicted, name='Predicted')
    cm = ConfusionMatrix(y_actu, y_pred)
    cm.stats()

get_stats('/home/as-hunt/ground_truth.csv', '/home/as-hunt/predictions.csv')