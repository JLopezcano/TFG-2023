import sys
import os
from pathlib import Path

from servicios.rutas.rutas import *
from servicios.graficas.graficas import *
from servicios.graficas.graficasML import *
from clases.classes import colours
from servicios.mapeo.mapeos import *
from servicios.mapeo.mapeosWifi import *
from servicios.mapeo.mapeosWifiFilters import *
from servicios.mapeo.mapeosWifiSingle import *
from servicios.mapeo.mapeosML import *

def main():
    filePath = Path(sys.argv[1])
    positions = []
    lights = []
    extension = ".txt"
    files = []
    files = os.listdir(filePath)
    
    lights, positions = readFiles(files, extension, filePath)

    graphLightByTime(lights)
    graphLocalization(positions)
    graphLatitudeByTime(positions)
    graphLongitudeByTime(positions)
    
    graphPositionAndLightByTime(positions, lights)

def main1():
    filePath = Path(sys.argv[1])
    positions = []
    lights = []
    wifis = []
    extension = ".txt"
    files = []
    files = os.listdir(filePath)
    
    lights, positions, wifis = readFilesToLists(files, extension, filePath)
    
    lightsInPosition = []
    lightsInPosition = lightByPosition(lights, positions)
    positionNormalized, lightNormalized = normalization(positions, lights)
    positionBegining, positionEnd = positionsCapped(positions)
    
    graphLocalizationInList(positions[0])
    graphLocalizationsInOrder(positionBegining[0], positions[0])
    graphLocalizationsInOrder(positionEnd[0], positions[0])
    
    luxInPositions = luxesCappedByPos(lightsInPosition, positions)
    luxInPositionsMinusMean = []

    for light in luxInPositions:
        mean = meanLightSimpleTxt(light)
        luxInPositionsMinusMean.append(minusMeanLights(light, mean))
    
    graphLuxByLocalization(luxInPositionsMinusMean)
    
    lightsOrdered = groupLightsMinusMean(luxInPositions)
    lightsOrderedMean = arrayWithLightMeans(lightsOrdered)
        
    graphLuxByLocalizationMean(luxInPositions, lightsOrderedMean)
    
    lightsOrderedMinusMean = groupLightsMinusMean(luxInPositionsMinusMean)
    lightsOrderedMeanMinusMean = arrayWithLightMeans(lightsOrderedMinusMean)
    
    graphLuxByLocalizationMean(luxInPositionsMinusMean, lightsOrderedMeanMinusMean)
    
    graphLuxByLocalizationMeanBoxplots(lightsOrderedMeanMinusMean)

    graphLuxByLocalizationPositionsBoxplots(lightsOrdered)
    
    graphLuxByLocalizationPositionsBoxplots(lightsOrderedMinusMean)
    
    """
    luxInPositionsMinusThreash = []

    for light in luxInPositions:
        maxLux = maximunLightSimpleTxt(light)
        minLux = minimunLightSimpleTxt(light)
        luxInPositionsMinusThreash.append(minusThreshLights(light, maxLux, minLux))
    
    graphLuxByLocalization(luxInPositions)
    graphLuxByLocalization(luxInPositionsMinusThreash)
    
    
    means = []
    
    for light in luxInPositionsMinusMean:
        means.append(lightMeanPosition(light))
    
    graphLuxByLocalizationMean(luxInPositionsMinusMean, means)
    """
    
    """
    graphLightByTimeToList(lightNormalized)
    graphLatitudeByTimeToList(positions)
    graphLongitudeByTimeToList(positions)

    graphLightByTimeToList(lights)
    graphPositionAndLightByTimeToList(positionNormalized, lightNormalized)
    graphLightByTimeToList(lightsInPosition)
    
    lightsInPositionNormalized = []
    
    for light in lightsInPosition:
        maxLight = maximunLight(lightsInPosition)
        minLight = minimunLight(lightsInPosition)
        lightsInPositionNormalized.append(normalizeLight(light, maxLight, minLight))

    maxLight = maximunLightSimpleTxt(lightsInPosition[0])
    minLight = minimunLightSimpleTxt(lightsInPosition[0])
    simpleLightNormalized = (normalizeLight(lightsInPosition[0], maxLight, minLight))
    
    graphPositionAndLightByTimeToList(positionNormalized, lightsInPositionNormalized)
    
    for position in positionNormalized:
        graphPositionAndLightByTime(positionNormalized[positionNormalized.index(position)], simpleLightNormalized)
"""

def mainLightML():
    filePath = Path(sys.argv[1])
    positions = []
    lights = []
    wifis = []
    extension = ".txt"
    files = []
    files = os.listdir(filePath)
    
    lights, positions, wifis = readFilesToLists(files, extension, filePath)
    
    lightsInPosition = []
    lightsInPosition = lightByPosition(lights, positions)
    positionNormalized, lightNormalized = normalization(positions, lights)
    positionBegining, positionEnd = positionsCapped(positions)
 
    luxInPositions = luxesCappedByPos(lightsInPosition, positions)
    luxInPositionsMinusMean = []

    for light in luxInPositions:
        mean = meanLightSimpleTxt(light)
        luxInPositionsMinusMean.append(minusMeanLights(light, mean))
 
    lightsOrdered = groupLightsMinusMean(luxInPositions)
    lightsOrderedMean = arrayWithLightMeans(lightsOrdered)
       
    lightsOrderedMinusMean = groupLightsMinusMean(luxInPositionsMinusMean)
    lightsOrderedMeanMinusMean = arrayWithLightMeans(lightsOrderedMinusMean)

    graphLuxByLocalizationPositionsBoxplots(lightsOrdered)
    
    graphLuxByLocalizationPositionsBoxplots(lightsOrderedMinusMean)
    
    #Parte del ML con los lights, se implementará un SVC
    
    lightSamplesY = lightGetSamplesY(lightsOrdered)
    #lightSamplesY = lightGetSamplesLightY(lightsOrdered)
    lightsOrderedFitted = lightsFittingSamples(lightsOrdered)
    lightML(lightsOrderedFitted, lightSamplesY)

def main2():
    
    filePath = Path(sys.argv[1])
    positions = []
    lights = []
    wifis = []
    extension = ".txt"
    files = []
    files = os.listdir(filePath)
    
    lights, positions, wifis = readFilesToLists(files, extension, filePath)

    wifisInPosition = []
    #wifisInPosition = wifiByPosition(wifis, positions)
    wifisInPosition = wifiCappedByPosition(wifis, positions)
    
    wifisCappedSSID1 = []
    wifisCappedSSID1 = wifiCapBySSID(wifisInPosition)
    wifisCappedFrequency = []
    wifisCappedFrequency = wifiCapByFrequency(wifisCappedSSID1)
    
    #print(wifisCappedSSID1)
    
    wifisOrderedPositions = wifisOrdered(wifisCappedFrequency)
    wifisOrderedsBoxplot = wifiOrderingPositionsForBoxplot(wifisCappedFrequency)
    
    wifisMeansByPosition = wifiGetMeanByPosition(wifisOrderedsBoxplot)
    
    """
    wifisMeanByPosition = wifiGetMeanByPosition(wifisOrderedsBoxplot)
    wifisMinusMeanPosition = wifiMinusPositionMeans(wifisCappedFrequency, wifisMeanByPosition)

    graphWifisByPositions(wifisOrderedPositions, wifisMeanByPosition)
    """
    wifisMinusMeanTxt = []
    
    for wifi in wifisOrderedPositions:
        mean = getMeanWifiSimpleTxt(wifi)
        wifisMinusMeanTxt.append(wifiMinusTxtMeans(wifi, mean))
        
    wifisOrderedsBoxplotMinusMeans = wifiOrderingPositionsForBoxplot(wifisMinusMeanTxt)
    wifisMeansMinusMeans = wifiGetMeanByPosition(wifisOrderedsBoxplotMinusMeans)
    
    graphWifisByPositions(wifisOrderedPositions, wifisMeansByPosition)
    
    graphWifisByPositions(wifisMinusMeanTxt, wifisMeansMinusMeans)
    
    graphWifisByPositionsBoxplots(wifisOrderedsBoxplot, 0)
    graphWifisByPositionsBoxplots(wifisOrderedsBoxplotMinusMeans, 1)
    
def main3():
    
    filePath = Path(sys.argv[1])
    positions = []
    lights = []
    wifis = []
    extension = ".txt"
    files = []
    files = os.listdir(filePath)
    
    lights, positions, wifis = readFilesToLists(files, extension, filePath)

    wifisInPosition = []
    #wifisInPosition = wifiByPosition(wifis, positions)
    wifisInPosition = wifiCappedByPosition(wifis, positions)
    
    wifisCappedSSID2 = []
    wifisCappedSSID2 = wifiCapBySSID2(wifisInPosition)
    
    wifisCappedFrequency = []
    wifisCappedFrequency = wifiCapByFrequency2(wifisCappedSSID2)
    
    print(wifisCappedSSID2)
        
    wifisOrderedPositions = wifisOrdered(wifisCappedFrequency)
    wifisOrderedsBoxplot = wifiOrderingPositionsForBoxplot(wifisCappedFrequency)
    
    wifisMeansByPosition = wifiGetMeanByPosition(wifisOrderedsBoxplot)

    wifisMinusMeanTxt = []
    
    for wifi in wifisOrderedPositions:
        mean = getMeanWifiSimpleTxt(wifi)
        wifisMinusMeanTxt.append(wifiMinusTxtMeans(wifi, mean))
        
    wifisOrderedsBoxplotMinusMeans = wifiOrderingPositionsForBoxplot(wifisMinusMeanTxt)
    wifisMeansMinusMeans = wifiGetMeanByPosition(wifisOrderedsBoxplotMinusMeans)
    
    graphWifisByPositions(wifisOrderedPositions, wifisMeansByPosition)
    
    graphWifisByPositions(wifisMinusMeanTxt, wifisMeansMinusMeans)
    
    graphWifisByPositionsBoxplots(wifisOrderedsBoxplot, 0)
    graphWifisByPositionsBoxplots(wifisOrderedsBoxplotMinusMeans, 1)

def main4():
    
    filePath = Path(sys.argv[1])
    positions = []
    lights = []
    wifis = []
    extension = ".txt"
    files = []
    files = os.listdir(filePath)
    
    lights, positions, wifis = readFilesToLists(files, extension, filePath)

    wifisInPosition = []
    #wifisInPosition = wifiByPosition(wifis, positions)
    wifisInPosition = wifiCappedByPosition(wifis, positions)
    
    wifisCappedSSID3 = []
    wifisCappedSSID3 = wifiCapBySSID3(wifisInPosition)
        
    wifisCappedFrequency = []
    wifisCappedFrequency = wifiCapByFrequency3(wifisCappedSSID3)
    
    print(wifisCappedSSID3)
        
    wifisOrderedPositions = wifisOrdered(wifisCappedFrequency)
    wifisOrderedsBoxplot = wifiOrderingPositionsForBoxplot(wifisCappedFrequency)
    
    wifisMeansByPosition = wifiGetMeanByPosition(wifisOrderedsBoxplot)

    wifisMinusMeanTxt = []
    
    for wifi in wifisOrderedPositions:
        mean = getMeanWifiSimpleTxt(wifi)
        wifisMinusMeanTxt.append(wifiMinusTxtMeans(wifi, mean))
                
    wifisOrderedsBoxplotMinusMeans = wifiOrderingPositionsForBoxplot(wifisMinusMeanTxt)
    wifisMeansMinusMeans = wifiGetMeanByPosition(wifisOrderedsBoxplotMinusMeans)
    
    graphWifisByPositions(wifisOrderedPositions, wifisMeansByPosition)
    
    graphWifisByPositions(wifisMinusMeanTxt, wifisMeansMinusMeans)
    
    graphWifisByPositionsBoxplots(wifisOrderedsBoxplot, 0)
    graphWifisByPositionsBoxplots(wifisOrderedsBoxplotMinusMeans, 1)

def main5():
    
    filePath = Path(sys.argv[1])
    positions = []
    lights = []
    wifis = []
    extension = ".txt"
    files = []
    files = os.listdir(filePath)
    
    lights, positions, wifis = readFilesToLists(files, extension, filePath)

    wifisInPosition = []
    #wifisInPosition = wifiByPosition(wifis, positions)
    wifisInPosition = wifiCappedByPosition(wifis, positions)
    
    wifisCappedSSID4 = []
    wifisCappedSSID4 = wifiCapBySSID4(wifisInPosition)
            
    wifisCappedFrequency = []
    wifisCappedFrequency = wifiCapByFrequency4(wifisCappedSSID4)
    
    print(wifisCappedSSID4)
        
    wifisOrderedPositions = wifisOrdered(wifisCappedFrequency)
    wifisOrderedsBoxplot = wifiOrderingPositionsForBoxplot(wifisCappedFrequency)
    
    wifisMeansByPosition = wifiGetMeanByPosition(wifisOrderedsBoxplot)

    wifisMinusMeanTxt = []
    
    for wifi in wifisOrderedPositions:
        mean = getMeanWifiSimpleTxt(wifi)
        wifisMinusMeanTxt.append(wifiMinusTxtMeans(wifi, mean))
                
    wifisOrderedsBoxplotMinusMeans = wifiOrderingPositionsForBoxplot(wifisMinusMeanTxt)
    wifisMeansMinusMeans = wifiGetMeanByPosition(wifisOrderedsBoxplotMinusMeans)
    
    graphWifisByPositions(wifisOrderedPositions, wifisMeansByPosition)
    
    graphWifisByPositions(wifisMinusMeanTxt, wifisMeansMinusMeans)
    
    graphWifisByPositionsBoxplots(wifisOrderedsBoxplot, 0)
    graphWifisByPositionsBoxplots(wifisOrderedsBoxplotMinusMeans, 1)
    
def main6():
    
    filePath = Path(sys.argv[1])
    positions = []
    lights = []
    wifis = []
    extension = ".txt"
    files = []
    files = os.listdir(filePath)
    
    lights, positions, wifis = readFilesToLists(files, extension, filePath)

    wifisInPosition = []
    #wifisInPosition = wifiByPosition(wifis, positions)
    wifisInPosition = wifiCappedByPosition(wifis, positions)
    
    wifisCappedSSID5 = []
    wifisCappedSSID5 = wifiCapBySSID5(wifisInPosition)
            
    wifisCappedFrequency = []
    wifisCappedFrequency = wifiCapByFrequency5(wifisCappedSSID5)
    
    print(wifisCappedFrequency)
        
    wifisOrderedPositions = wifisOrdered(wifisCappedFrequency)
    wifisOrderedsBoxplot = wifiOrderingPositionsForBoxplot(wifisCappedFrequency)
    
    wifisMeansByPosition = wifiGetMeanByPosition(wifisOrderedsBoxplot)

    wifisMinusMeanTxt = []
    
    for wifi in wifisOrderedPositions:
        mean = getMeanWifiSimpleTxt(wifi)
        wifisMinusMeanTxt.append(wifiMinusTxtMeans(wifi, mean))
                
    wifisOrderedsBoxplotMinusMeans = wifiOrderingPositionsForBoxplot(wifisMinusMeanTxt)
    wifisMeansMinusMeans = wifiGetMeanByPosition(wifisOrderedsBoxplotMinusMeans)
    
    graphWifisByPositions(wifisOrderedPositions, wifisMeansByPosition)
    
    graphWifisByPositions(wifisMinusMeanTxt, wifisMeansMinusMeans)
    
    graphWifisByPositionsBoxplots(wifisOrderedsBoxplot, 0)
    graphWifisByPositionsBoxplots(wifisOrderedsBoxplotMinusMeans, 1)
    
def main7():
    
    filePath = Path(sys.argv[1])
    positions = []
    lights = []
    wifis = []
    extension = ".txt"
    files = []
    files = os.listdir(filePath)
    
    lights, positions, wifis = readFilesToLists(files, extension, filePath)

    wifisInPosition = []
    #wifisInPosition = wifiByPosition(wifis, positions)
    wifisInPosition = wifiCappedByPosition(wifis, positions)
    
    wifisCappedSSID6 = []
    wifisCappedSSID6 = wifiCapBySSID6(wifisInPosition)
            
    wifisCappedFrequency = []
    wifisCappedFrequency = wifiCapByFrequency6(wifisCappedSSID6)
    
    print(wifisCappedFrequency)
        
    wifisOrderedPositions = wifisOrdered(wifisCappedFrequency)
    wifisOrderedsBoxplot = wifiOrderingPositionsForBoxplot(wifisCappedFrequency)
    
    wifisMeansByPosition = wifiGetMeanByPosition(wifisOrderedsBoxplot)

    wifisMinusMeanTxt = []
    
    for wifi in wifisOrderedPositions:
        mean = getMeanWifiSimpleTxt(wifi)
        wifisMinusMeanTxt.append(wifiMinusTxtMeans(wifi, mean))
                
    wifisOrderedsBoxplotMinusMeans = wifiOrderingPositionsForBoxplot(wifisMinusMeanTxt)
    wifisMeansMinusMeans = wifiGetMeanByPosition(wifisOrderedsBoxplotMinusMeans)
    
    graphWifisByPositions(wifisOrderedPositions, wifisMeansByPosition)
    
    graphWifisByPositions(wifisMinusMeanTxt, wifisMeansMinusMeans)
    
    graphWifisByPositionsBoxplots(wifisOrderedsBoxplot, 0)
    graphWifisByPositionsBoxplots(wifisOrderedsBoxplotMinusMeans, 1)
    
def main8():
    
    filePath = Path(sys.argv[1])
    positions = []
    lights = []
    wifis = []
    extension = ".txt"
    files = []
    files = os.listdir(filePath)
    
    lights, positions, wifis = readFilesToLists(files, extension, filePath)

    wifisInPosition = []
    #wifisInPosition = wifiByPosition(wifis, positions)
    wifisInPosition = wifiCappedByPosition(wifis, positions)
    
    wifiCappedID = wifiCapID1(wifisInPosition)
    wifiCappedID1 = wifiCapID2(wifisInPosition)
    wifiCappedID2 = wifiCapID3(wifisInPosition)
    wifiCappedID3 = wifiCapID4(wifisInPosition)
    wifiCappedID4 = wifiCapID5(wifisInPosition)
    
    wifiCappedFreq = wifiCapFreq1(wifiCappedID)
    wifiCappedFreq1 = wifiCapFreq2(wifiCappedID1)
    wifiCappedFreq2 = wifiCapFreq3(wifiCappedID2)
    wifiCappedFreq3 = wifiCapFreq4(wifiCappedID3)
    wifiCappedFreq4 = wifiCapFreq5(wifiCappedID4)
    
    wifiOrderedPosi1 = wifiOrderingPositionsForBoxplot(wifiCappedFreq)
    wifiOrderedPosi2 = wifiOrderingPositionsForBoxplot(wifiCappedFreq1)
    wifiOrderedPosi3 = wifiOrderingPositionsForBoxplot(wifiCappedFreq2)
    wifiOrderedPosi4 = wifiOrderingPositionsForBoxplot(wifiCappedFreq3)
    wifiOrderedPosi5 = wifiOrderingPositionsForBoxplot(wifiCappedFreq4)
    
    #id1 frec 5600 -> 1-2-3-5-6-(+-7)
    #id1 frec 5560 -> 4-7-(+-3)
    #id2 frec 2447 -> 1-6-7 ó 1-5-6
    #id3 frec 2422 -> 1-4-6-7
    #id6 frec 2412 -> 1-2-4-5
    
    #wifiExample1 tiene:
        #id1 frec 5600 -> 2
        #id1 frec 5560 -> 4-7-3
        #id2 frec 2447 -> 5-6
        #id6 frec 2412 -> 1
    
    #wifiExample2 tiene:
        #id6 frec 2412 -> 1-5-7
        #id3 frec 2422 -> 6
        #id1 frec 5560 -> 3-2-4
    
    #wifiExample3 tiene:
        #id3 frec 2422 -> 4-6
        #id1 frec 5600 -> 2-3-5
        #id2 frec 2447 -> 1-7
    
    #wifiExample4 tiene:
        #id1 frec 5600 -> 5-6-7
        #id1 frec 5560 -> 2-4
        #id2 frec 2447 -> 1-3

    wifiExample1 = []
    wifiExample1 = rellenaWifi1(wifiOrderedPosi1, wifiOrderedPosi2, wifiOrderedPosi3, wifiOrderedPosi5)
    
    wifiExample2 = []
    wifiExample2 = rellenaWifi2(wifiOrderedPosi5, wifiOrderedPosi4, wifiOrderedPosi2)
    
    wifiExample3 = []
    wifiExample3 = rellenaWifi3(wifiOrderedPosi4, wifiOrderedPosi1, wifiOrderedPosi3)
    
    wifiExample4 = []
    wifiExample4 = rellenaWifi3(wifiOrderedPosi1, wifiOrderedPosi2, wifiOrderedPosi3)
    
    graphWifisByPositionsBoxplots(wifiExample1, 0)
    graphWifisByPositionsBoxplots(wifiExample2, 0)
    print(wifiExample3)
    graphWifisByPositionsBoxplots(wifiExample3, 0)
    graphWifisByPositionsBoxplots(wifiExample4, 0)    
    
mainLightML()