from clases.classes import data

import numpy as np

from sklearn import preprocessing
from sklearn.model_selection import train_test_split

def lightGetSamplesY(lights):
    newArray = []
    
    for light in lights:
        for element in light:
            newArray.append(element[0][-1])
    
    return newArray

def wifiGetSamplesY(wifis):
    newArray = []
    
    for wifi in wifis:
        for element in wifi:
            newArray.append(element[4][-1])
    
    return newArray

def lightsFittingSamples(lights):
    newArray = []
    array = []
    
    for light in lights:
        for element in light:
            array = []
            array.append(element[1])
            newArray.append(array)
    
    return newArray

def wifisFittingSamples(wifis):
    newArray = []
    array = []
    
    for wifi in wifis:
        for element in wifi:
            array = []
            array.append(element[3])
            newArray.append(array)
    
    return newArray

def testSplit(rss, YSamples):
    newArraryXTrain = []
    newArraryXTest= []
    newArraryYTrain = []
    newArraryYTest= []
    
    newArraryXTrain, newArraryXTest, newArraryYTrain, newArraryYTest = train_test_split(rss, YSamples, test_size=0.30, shuffle=True) 

    return newArraryXTrain, newArraryXTest, newArraryYTrain, newArraryYTest

def printConfusionMatrix(matrix):
    
    for row in matrix:
        print(row)

def rssConfusionMedia(ConfusionsMatrix):
    sumMatrix = []
    matrixRow = []
    
    for list in ConfusionsMatrix:
        if sumMatrix == []:
            sumMatrix = list
        else:
            indice = 0
            for row in list:
                aux = []
                matrixRow = []
                aux = sumMatrix[indice]
                rIndice = 0
                for element in row:
                    numberAux = (float(element) + float(aux[rIndice]))
                    matrixRow.append(numberAux)
                    rIndice = rIndice + 1
                sumMatrix[indice] = matrixRow
                indice = indice + 1
    
    mediaMatrix = []
    
    for sumRow in sumMatrix:
        mediaRow = []
        for element in sumRow:
            mediaRow.append(element / 10)
        mediaMatrix.append(mediaRow)   
         
    print()
    printConfusionMatrix(mediaMatrix)
    print()
    
    return mediaMatrix

def featureMean(featureList):
    mean = 0
    
    for feature in featureList:
        mean = mean + feature
    
    mean = mean / 10
    print(mean)
    
    return mean

def featureMeanWifi(featureList):
    mean = 0
    
    for feature in featureList:
        mean = mean + feature
    
    mean = mean / 2
    print(mean)
    
    return mean