import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.lines as mlines

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import preprocessing
from sklearn import svm

def lightML(lights, positions, lightsTest, positionsTest):
    XTrain = lights
    YTrain = positions
    XTest = lightsTest
    YTest = positionsTest
    
    fig, ax = plt.subplots()
    plt.xlabel('Lux (dBm)')
    plt.ylabel('Positions')

    clf = svm.SVC(kernel='poly')    #kernel{‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’} or callable, default=’rbf’
    clf.fit(XTrain, YTrain)       #SE HACE EL FIT SOLO CON LOS TRAINING DE LA X Y LA Y

    YPred = clf.predict(XTest)      #EL PREDICT SE HACE SOLO CON EL TEST
    
    """print(YPred)
    print(YTrain)"""
    
    """for element in XTrain:
        newX.append(element[0])"""
    
    print(classification_report(YTest, YPred, zero_division=0))      #MI CLASIFICATION REPORT Y LA MATRIZ DE CONFUSION UTILIZA LA YTEST CON LA Y DE LA PREDICCION
    print(confusion_matrix(YTest, YPred))
    
    return confusion_matrix(YTest, YPred)
    
    #print(confusion_matrix(YTest, YPred)[0][0])
