import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.lines as mlines

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

from sklearn import preprocessing
from sklearn import svm

def lightML(lights, positions, lightsTest, positionsTest, kern):
    XTrain = lights
    YTrain = positions
    XTest = lightsTest
    YTest = positionsTest
    
    fig, ax = plt.subplots()
    plt.xlabel('Lux (dBm)')
    plt.ylabel('Positions')

    if kern == 1:
        clf = svm.SVC(kernel='poly')    #kernel{‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’} or callable, default=’rbf’
    else:
        clf = svm.SVC(kernel='rbf')
        
    clf.fit(XTrain, YTrain)       #SE HACE EL FIT SOLO CON LOS TRAINING DE LA X Y LA Y

    YPred = clf.predict(XTest)      #EL PREDICT SE HACE SOLO CON EL TEST
    
    print(classification_report(YTest, YPred, zero_division=0))      #MI CLASIFICATION REPORT Y LA MATRIZ DE CONFUSION UTILIZA LA YTEST CON LA Y DE LA PREDICCION
    print(confusion_matrix(YTest, YPred))
    
    report = classification_report(YTest, YPred, zero_division=0, output_dict=True)
    
    #Todo son un valor para la tabla
    accuracy = accuracy_score(YTest, YPred)
    macro_precision =  report['macro avg']['precision'] 
    macro_recall = report['macro avg']['recall']    
    macro_f1 = report['macro avg']['f1-score']
    
    return confusion_matrix(YTest, YPred), accuracy, macro_precision, macro_recall, macro_f1
