from clases.classes import data

import numpy as np
from sklearn import preprocessing

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
            array.append(element[0][-1])
            newArray.append(array)
    
    return newArray