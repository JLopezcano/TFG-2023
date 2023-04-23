import sys
import os
from pathlib import Path

from servicios.rutas.rutas import *
from servicios.graficas.graficas import *
from clases.classes import colours
from servicios.mapeo.mapeos import *

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
    extension = ".txt"
    files = []
    files = os.listdir(filePath)
    
    lights, positions = readFilesToLists(files, extension, filePath)
    lightsInPosition = []

    lightsInPosition = lightByPosition(lights, positions)
    positionNormalized, lightNormalized = normalization(positions, lights)
    positionBegining, positionEnd = positionsCapped(positions)
    
    graphLocalizationInList(positions[0])
    graphLocalizationsInOrder(positionBegining[0], positions[0])
    graphLocalizationsInOrder(positionEnd[0], positions[0])
    
    luxInPositions = luxesCappedByPos(lightsInPosition, positions)
    luxInPositionsMinusMean = []
    luxInPositionsMinusThreash = []

    for light in luxInPositions:
        maxLux = maximunLightSimpleTxt(light)
        minLux = minimunLightSimpleTxt(light)
        luxInPositionsMinusThreash.append(minusThreshLights(light, maxLux, minLux))
    
    graphLuxByLocalization(luxInPositions)
    graphLuxByLocalization(luxInPositionsMinusThreash)

    for light in luxInPositions:
        mean = meanLightSimpleTxt(light)
        luxInPositionsMinusMean.append(minusMeanLights(light, mean))
        
    graphLuxByLocalization(luxInPositionsMinusMean)
    
    """
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

main1()