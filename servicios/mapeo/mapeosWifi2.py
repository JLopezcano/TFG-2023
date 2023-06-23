from clases.classes import data

import numpy as np
from sklearn import preprocessing

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

def wifiCapBySSID2(wifis):
    newArray = []
    array = []
    
    for wifi in wifis:
        for element in wifi:
            if (element[1] == "SSID2021_0002"):
                array.append(element)
        newArray.append(array)
        array = []
        
    return newArray

def wifiCapByFrequency2(wifis):
    newArray = []
    array = []
    
    for wifi in wifis:
        for element in wifi:
            if (element[2] == float(2447)):
                array.append(element)
        newArray.append(array)
        array = []
        
    return newArray

def wifiCapBySSID3(wifis):
    newArray = []
    array = []
    
    for wifi in wifis:
        for element in wifi:
            if (element[1] == "SSID2021_0003"):
                array.append(element)
        newArray.append(array)
        array = []
        
    return newArray

def wifiCapByFrequency3(wifis):
    newArray = []
    array = []
    
    for wifi in wifis:
        for element in wifi:
            if (element[2] == float(2422)):
                array.append(element)
        newArray.append(array)
        array = []
        
    return newArray

def wifiCapBySSID4(wifis):
    newArray = []
    array = []
    
    for wifi in wifis:
        for element in wifi:
            if (element[1] == "SSID2021_0006"):
                array.append(element)
        newArray.append(array)
        array = []
        
    return newArray

def wifiCapByFrequency4(wifis):
    newArray = []
    array = []
    
    for wifi in wifis:
        for element in wifi:
            if (element[2] == float(2412)):
                array.append(element)
        newArray.append(array)
        array = []
        
    return newArray