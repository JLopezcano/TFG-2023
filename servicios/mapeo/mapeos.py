from clases.classes import data

import numpy as np
from sklearn import preprocessing

def getArrayIndex(arg, index):
    aux=[]
    
    for a in arg:
        aux.append(a[index])
    return aux
    
def format(arg,type):
    for a in arg:
        index = arg.index(a)
        arg[index] = float(a)

    if type == data.position:
        arg.pop()
        arg.pop()
        arg.remove(arg[1])
        return arg
    if type == data.light:
        arg.remove(arg[3])
        arg.remove(arg[1])
        return arg

def lightFormat(lights):
    auxLight=[]
    for light in lights:
        auxLight.append(np.array(light) / np.array([1, 1000]))
    return auxLight

def lightByPosition(lights, positions):
    aux = []
    auxList = []
    
    for position in positions:
        aux = []
        indice = positions.index(position)
        for light in lights[indice]:
            for posi in position:
                auxTime1 = posi[0] - 0.5 #2.0
                auxTime2 = posi[0] + 0.5 #2.0
                if (light[0] <= auxTime2) and (light[0] >= auxTime1):
                    aux.append(light)
        auxList.append(aux)
            
    return auxList

def maximunLight(arrays):
    max = 0.0
    for array in arrays:
        for num in array:
            if num[1] > max:
                max = num[1]
    
    return max

def maximunPosition(arrays):
    max = 0.0
    max2 = -9.99*10**(99)
    
    for array in arrays:
        for num in array:
            if num[1] > max:
                max = num[1]
            if num[2] > max2:
                max2 = num[2]
    return [max, max2]

def minimunLight(arrays):
    min = 9.99*10**(99)
    
    for array in arrays:
        for num in array:
            if num[1] < min:
                min = num[1]
    
    return min

def minimunPosition(arrays):
    min = 9.99*10**(99)
    min2 = 9.99*10**(99)
    
    for array in arrays:
        for num in array:
            if num[1] < min:
                min = num[1]
            if num[2] < min2:
                min2 = num[2]
                
    return [min, min2]

def maximunLightSimpleTxt(array):
    max = 0.0
    for num in array:
        if num[1] > max:
            max = num[1]
    
    return max

def minimunLightSimpleTxt(array):
    min = 9.99*10**(99)
    
    for num in array:
        if num[1] < min:
            min = num[1]
    
    return min

def normalizeLight(array, max, min):
    newArray = []
    
    e2 = [1.0, min]
    for element in array:
        a = element[1] - min
        b = max - min
        auxNum = [element[0] / e2[0], a / b]
        newArray.append(auxNum)
    
    return newArray

def normalizePosition(array, max, max2, min, min2):
    newArray = []
    
    e2 = [1.0, min, min2]
    for element in array:
        a = element[1] - min
        b = max - min
        c = element[2] - min2
        d = max2 - min2
        auxNum = [element[0] / e2[0], a / b, c / d]
        newArray.append(auxNum)
    
    return newArray

def normalization(positions, lights):
    positionNormalized = []
    lightNormalized = []
    
    for position in positions:
        maxPosition, maxPosition2 = maximunPosition(positions)
        minPosition, minPosition2 = minimunPosition(positions)
        positionNormalized.append(normalizePosition(position, maxPosition, maxPosition2, minPosition, minPosition2))
    for light in lights:
        maxLight = maximunLight(lights)
        minLight = minimunLight(lights)
        lightNormalized.append(normalizeLight(light, maxLight, minLight))
        
    return positionNormalized, lightNormalized

def positionsCapped(positions):
    
    positionsCapped = []
    positionCapped = []
    positionsCappedEnd = []
    positionCappedEnd = []
    
    for position in positions:
        positionCapped = []
        positionCappedEnd = []
        a = len(position)
        contador = 0
        while(contador < int(a/2)):
            positionCapped.append(position[contador])
            positionCappedEnd.append(position[contador+int(a/2)])
            contador = contador + 1
        positionsCapped.append(positionCapped)
        positionsCappedEnd.append(positionCappedEnd)
    
    return positionsCapped, positionsCappedEnd

def luxesCappedByPos(lights, positions):
    aux = []
    auxList = []
    auxColumn = []
    
    for position in positions:
        aux = []
        indice = positions.index(position)
        for light in lights[indice]:
            for posi in position:
                auxColumn = []
                auxTime1 = posi[0] - 0.5 #2.0
                auxTime2 = posi[0] + 0.5 #2.0
                if (light[0] <= auxTime2) and (light[0] >= auxTime1):
                    if (position.index(posi) > int(len(position)/2)):
                         auxColumn.append("position" + (str(position.index(posi) - int(len(position)/2))))
                         auxColumn.append(light[1])
                    else:
                        auxColumn.append("position" + str(position.index(posi)+1))
                        auxColumn.append(light[1])
                    aux.append(auxColumn)
        auxList.append(aux)

    return auxList