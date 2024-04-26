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
"""
def lightGetSamplesLightY(lights):
    newArray = []
    
    for light in lights:
        for element in light:
            newArray.append(element[1])
    
    return newArray
"""
def lightsFittingSamples(lights):
    newArray = []
    array = []
    
    for light in lights:
        for element in light:
            array = []
            array.append(element[1])
            newArray.append(array)
    
    return newArray

def lightsTestSplit(lights, YSamples):
    newArraryXTrain = []
    newArraryXTest= []
    newArraryYTrain = []
    newArraryYTest= []
    
    newArraryXTrain, newArraryXTest, newArraryYTrain, newArraryYTest = train_test_split(lights, YSamples, test_size=0.30, shuffle=True) 
    """
    print(newArraryXTrain)
    print(newArraryXTest)
    print(newArraryYTrain)
    print(newArraryYTest)
    """
    return newArraryXTrain, newArraryXTest, newArraryYTrain, newArraryYTest

def printConfusionMatrix(matrix):
    
    for row in matrix:
        print(row)

def lightsConfusionMedia(ConfusionsMatrix):
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