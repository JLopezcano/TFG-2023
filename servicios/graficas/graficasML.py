import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.lines as mlines

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import preprocessing
from sklearn import svm

def lightML(lights, positions, data):
    X = lights
    Y = positions
    tipo = data
    
    fig, ax = plt.subplots()
    plt.xlabel('Lux (dBm)')
    plt.ylabel('Positions')

    clf = svm.SVC(kernel='poly')
    clf.fit(X, Y)       #SE HACE EL FIT SOLO CON LOS TRAINING DE LA X Y LA Y
    
    if (tipo == 1):
        print("TRAIN")
    else:
        print("TEST")
    
    YPred = clf.predict(X)      #EL PREDICT SE HACE SOLO CON EL TEST
    
    print(YPred)
    print(Y)
    
    newX = []
    
    for element in X:
        newX.append(element[0])
    
    print(classification_report(Y, YPred))      #MI CLASIFICATION REPORT Y LA MATRIZ DE CONFUSION UTILIZA LA YTEST CON LA Y DE LA PREDICCION
    print(confusion_matrix(Y, YPred))
    
    print(confusion_matrix(Y, YPred)[0][0])
