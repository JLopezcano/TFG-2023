import sys
import os
from pathlib import Path

import signal
import sys
signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))

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
    wifis = []
    extension = ".txt"
    files = []
    files = os.listdir(filePath)
    
    lights, positions, wifis = readFilesToLists(files, extension, filePath)

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
    """
    lightSamplesY = lightGetSamplesY(lightsOrdered)
    lightsOrderedFitted = lightsFittingSamples(lightsOrdered)
    """
    lightSamplesY = lightGetSamplesY(lightsOrderedMinusMean)
    lightsOrderedFitted = lightsFittingSamples(lightsOrderedMinusMean)
    
    #lightML(lightsOrderedFitted, lightSamplesY)
    
    ConfusionMatrixList = []
    featureAccuracyAux = []
    featurePrecisionAux = []
    featureRecallAux = []
    featureF1Aux = []
    
    accuracyListPoly = []
    accuracyListRBF = []
    
    precisionListPoly = []
    precisionListRBF = []
    
    recallListPoly = []
    recallListRBF = []
    
    f1ListPoly = []
    f1ListRBF = []
    
    for kern in range(2):
        for i in range(10):
            Xtrain = []
            Xtest = []
            Ytrain = []
            Ytest = []
            ConfusionMatrix = []
            
            Xtrain, Xtest, Ytrain, Ytest = lightsTestSplit(lightsOrderedFitted, lightSamplesY)
            ConfusionMatrix, accuracy, precision, recall, f1 = lightML(Xtrain, Ytrain, Xtest, Ytest, kern)
            ConfusionMatrixList.append(ConfusionMatrix)
            featureAccuracyAux.append(accuracy)
            featurePrecisionAux.append(precision)
            featureRecallAux.append(recall)
            featureF1Aux.append(f1)
        if kern == 1:
            ConfusionMatrixListPoly = ConfusionMatrixList
            ConfusionMatrixListPoly = ConfusionMatrixList
            accuracyListPoly = featureAccuracyAux
            precisionListPoly = featurePrecisionAux
            recallListPoly = featureRecallAux
            f1ListPoly = featureF1Aux
        else:
            ConfusionMatrixListRBF = ConfusionMatrixList
            accuracyListRBF = featureAccuracyAux
            precisionListRBF = featurePrecisionAux
            recallListRBF = featureRecallAux
            f1ListRBF = featureF1Aux
            
        ConfusionMatrixList = []
        featureAccuracyAux = []
        featurePrecisionAux = []
        featureRecallAux = []
        featureF1Aux = []
    
    print()
    print("POLY")
    ConfusionMatrixPolyMedia = lightsConfusionMedia(ConfusionMatrixListPoly)
    print("accuracyListPoly")
    accuracyPolyMean = featureMean(accuracyListPoly)
    print("precisionListPoly")
    precisionPolyMean = featureMean(precisionListPoly)
    print("recallListPoly")
    recallPolyMean = featureMean(recallListPoly)
    print("f1ListPoly")
    f1PolyMean = featureMean(f1ListPoly)
    
    print()
    
    print("RBF")
    ConfusionMatrixRBFMedia = lightsConfusionMedia(ConfusionMatrixListRBF)
    print("accuracyListRBF")
    accuracyRBFMean = featureMean(accuracyListRBF)
    print("precisionListRBF")
    precisionRBFMean = featureMean(precisionListRBF)
    print("recallListRBF")
    recallRBFMean = featureMean(recallListRBF)
    print("f1ListRBF")
    f1RBFMean = featureMean(f1ListRBF)
    print()

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
    
    #Combinaciones totales:
        #id1 frec 5600
        #id1 frec 5560
        #id2 frec 2447
        #id3 frec 2422
        #id6 frec 2412
    
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
    
def selector(isFirstTime):
    
    if isFirstTime:
        print("State one Valid Number between [0-9].\nEXIT to end program.")
        print("0 To show light, latitude and longitude by time. Also shows a graph of the position \nand lux by time")
        print("1 To show graphs of the positions in space and order in the data collecting and lux \nby localization values, with and without its mean values, and boxplots for that data")
        print("2 To show wifi graphs in each positions ordered and minus their means for the SSID1")
        print("3 To show wifi graphs in each positions ordered and minus their means for the SSID2")
        print("4 To show wifi graphs in each positions ordered and minus their means for the SSID3")
        print("5 To show wifi graphs in each positions ordered and minus their means for the SSID4")
        print("6 To show wifi graphs in each positions ordered and minus their means for the SSID5")
        print("7 To show wifi graphs in each positions ordered and minus their means for the SSID6")
        print("8 To show wifi values in boxplots for 4 different examples, variating Freq and SSID")
        print("9 To show ML light results")
    
    x = input()
    if x == "EXIT":
        return
    
    if x == "0":
        main()
    elif x == "1":
        main1()
    elif x == "2":
        main2()
    elif x == "3":
        main3()
    elif x == "4":
        main4()
    elif x == "5":
        main5()
    elif x == "6":
        main6()
    elif x == "7":
        main7()
    elif x == "8":
        main8()
    elif x == "9":
        mainLightML()
    else: 
        print("State one Valid Number between [0-9]. EXIT to end program.")
        selector(False)
    
selector(True)
