from clases.classes import data

import numpy as np
from sklearn import preprocessing

def wifiCapID1(wifis):
    newArray = []
    array = []
    
    for wifi in wifis:
        for element in wifi:
            if (element[1] == "SSID2021_0001"):
                array.append(element)
        newArray.append(array)
        array = []
        
    return newArray

def wifiCapFreq1(wifis):
    newArray = []
    array = []
    
    for wifi in wifis:
        for element in wifi:
            if (element[2] == float(5600)):
                array.append(element)
        newArray.append(array)
        array = []
        
    return newArray

def wifiCapID2(wifis):
    newArray = []
    array = []
    
    for wifi in wifis:
        for element in wifi:
            if (element[1] == "SSID2021_0001"):
                array.append(element)
        newArray.append(array)
        array = []
        
    return newArray

def wifiCapFreq2(wifis):
    newArray = []
    array = []
    
    for wifi in wifis:
        for element in wifi:
            if (element[2] == float(5560)):
                array.append(element)
        newArray.append(array)
        array = []
        
    return newArray

def wifiCapID3(wifis):
    newArray = []
    array = []
    
    for wifi in wifis:
        for element in wifi:
            if (element[1] == "SSID2021_0002"):
                array.append(element)
        newArray.append(array)
        array = []
        
    return newArray

def wifiCapFreq3(wifis):
    newArray = []
    array = []
    
    for wifi in wifis:
        for element in wifi:
            if (element[2] == float(2447)):
                array.append(element)
        newArray.append(array)
        array = []
        
    return newArray

def wifiCapID4(wifis):
    newArray = []
    array = []
    
    for wifi in wifis:
        for element in wifi:
            if (element[1] == "SSID2021_0003"):
                array.append(element)
        newArray.append(array)
        array = []
        
    return newArray

def wifiCapFreq4(wifis):
    newArray = []
    array = []
    
    for wifi in wifis:
        for element in wifi:
            if (element[2] == float(2422)):
                array.append(element)
        newArray.append(array)
        array = []
        
    return newArray

def wifiCapID5(wifis):
    newArray = []
    array = []
    
    for wifi in wifis:
        for element in wifi:
            if (element[1] == "SSID2021_0006"):
                array.append(element)
        newArray.append(array)
        array = []
        
    return newArray

def wifiCapFreq5(wifis):
    newArray = []
    array = []
    
    for wifi in wifis:
        for element in wifi:
            if (element[2] == float(2412)):
                array.append(element)
        newArray.append(array)
        array = []
        
    return newArray

def rellenaWifi1(wifis1, wifis2, wifis3, wifis6):
    wifis = []
    
    wifis.append(wifis6[0])
    
    wifis.append(wifis1[1])
    
    wifis.append(wifis2[2])
    wifis.append(wifis2[3])
    wifis.append(wifis2[4])
    
    wifis.append(wifis3[5])
    wifis.append(wifis3[6])
    
    return wifis

def rellenaWifi2(wifis6, wifis3, wifis1):
    wifis = []
    
    wifis.append(wifis6[0])
    
    wifis.append(wifis1[1])
    wifis.append(wifis1[2])
    wifis.append(wifis1[3])
    
    wifis.append(wifis6[4])
    
    wifis.append(wifis3[5])
    
    wifis.append(wifis6[6])
    
    return wifis

def rellenaWifi3(wifis1, wifis2, wifis3):
    wifis = []
    
    wifis.append(wifis3[0])
    
    wifis.append(wifis2[1])
    
    wifis.append(wifis3[2])
    
    wifis.append(wifis2[3])
    
    wifis.append(wifis1[4])
    wifis.append(wifis1[5])
    wifis.append(wifis1[6])
    
    return wifis
    