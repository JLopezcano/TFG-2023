import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.lines as mlines

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

from sklearn import preprocessing
from sklearn import svm

def rssML(lights, positions, lightsTest, positionsTest, kern):
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
        
    clf.fit(XTrain, YTrain)

    YPred = clf.predict(XTest)
    
    print(classification_report(YTest, YPred, zero_division=0))
    print(confusion_matrix(YTest, YPred))
    
    report = classification_report(YTest, YPred, zero_division=0, output_dict=True)
    
    accuracy = accuracy_score(YTest, YPred)
    macro_precision =  report['macro avg']['precision'] 
    macro_recall = report['macro avg']['recall']    
    macro_f1 = report['macro avg']['f1-score']
    
    return confusion_matrix(YTest, YPred), accuracy, macro_precision, macro_recall, macro_f1
