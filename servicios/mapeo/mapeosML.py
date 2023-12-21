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
    