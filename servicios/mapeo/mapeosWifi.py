from clases.classes import data

import numpy as np
from sklearn import preprocessing

"""
def wifiByPosition(wifis, positions):
    aux = []
    auxList = []
    
    for position in positions:
        aux = []
        indice = positions.index(position)
        for wifi in wifis[indice]:
            for posi in position:
                auxTime1 = posi[0] - 1.5 #2.0
                auxTime2 = posi[0] + 1.2 #2.0
                if (wifi[0] <= auxTime2) and (wifi[0] >= auxTime1):
                    aux.append(wifi)
        auxList.append(aux)
            
    return auxList
"""

def wifiCappedByPosition(wifis, positions):
    aux = []
    auxList = []
    auxColumn = []
    
    for position in positions:
        aux = []
        indice = positions.index(position)
        
        for wifi in wifis[indice]:
            for posi in position:
                auxColumn = []
                auxTime1 = posi[0] - 0.4 #2.0
                auxTime2 = posi[0] + 0.4 #2.0
                if (wifi[0] <= auxTime2) and (wifi[0] >= auxTime1):
                    if (position.index(posi) > int(len(position)/2)):
                        a = 0
                        for element in wifi:
                            auxColumn.append(element)
                        auxColumn.append("position" + (str(int(len(position)/2) + 1 - (position.index(posi) - int(len(position)/2)))))
                        
                    else:
                        for element in wifi:
                            auxColumn.append(element)
                        if ((position.index(posi) + 1) == 8):
                            auxColumn.append("position7")
                        else:
                            auxColumn.append("position" + str(position.index(posi) + 1))
                        aux.append(auxColumn)
        auxList.append(aux)
        
    return auxList

def wifiCapBySSID(wifis):
    newArray = []
    array = []
    
    for wifi in wifis:
        for element in wifi:
            if (element[1] == "SSID2021_0001"):
                array.append(element)
        newArray.append(array)
        array = []
        
    return newArray

def wifiCapByFrequency(wifis):
    newArray = []
    array = []
    
    for wifi in wifis:
        for element in wifi:
            if (element[2] == float(2437)):
                array.append(element)
        newArray.append(array)
        array = []
        
    return newArray

def wifisOrdered(wifis):
    newArray = []
    numeroMayor = 0
    
    for wifi in wifis:
        for element in wifi:
            pi = element[-1]
            if (int(pi.replace("position","")) > numeroMayor):
                numeroMayor = int(pi.replace("position",""))

    for wifi in wifis:
        count = 1
        array = []
        while count <= numeroMayor:
            for element in wifi:
               if "position" + str(count) == element[-1]:
                    array.append(element)
            count = count + 1
        newArray.append(array)

    return newArray

def wifiOrderingPositionsForBoxplot(wifis):
    newArray = []
    arrayPosition = []
    numeroMayor = 0
    
    for wifi in wifis:
        for element in wifi:
            pi = element[-1]
            if (int(pi.replace("position","")) > numeroMayor):
                numeroMayor = int(pi.replace("position",""))
                
    count = 1
    while count <= numeroMayor:
        arrayPosition = []
        for wifi in wifis:
            for element in wifi:
                if "position" + str(count) == element[-1]:
                    arrayPosition.append(element)
        newArray.append(arrayPosition)
        count = count + 1
        
    return newArray

def wifiGetMeanByPosition(wifis):
    newArray = []
    array = []
    value = 0
    
    for wifi in wifis:
        count = 0
        value = 0
        array = []
        for element in wifi:
            count = count + 1
            value = element[3] + value
        mean = value / count
        array.append(mean)
        array.append(element[-1])
        newArray.append(array)
            
    return newArray

def wifiMinusPositionMeans(wifis, means):
    newArray = []
    array = []
    aux = []
    
    for wifi in wifis:
        aux = []
        for element in wifi:
            array = []
            for mean in means:
                count = 0
                if (mean[1] == element[-1]):
                    for value in element:
                        if count == 3:
                            array.append(value - mean[0])
                        else:
                            array.append(value)
                        count = count + 1
            aux.append(array)
        newArray.append(aux)
        
    return newArray