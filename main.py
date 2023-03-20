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
    positionNormalized = []
    lightNormalized = []
    lightsInPosition = []

    lightsInPosition = (lightByPosition(lights, positions))
    for position in positions:
        maxPosition, maxPosition2 = maximunPosition(positions)
        minPosition, minPosition2 = minimunPosition(positions)
        positionNormalized.append(normalizePosition(position, maxPosition, maxPosition2, minPosition, minPosition2))
    for light in lights:
        maxLight = maximunLight(lights)
        minLight = minimunLight(lights)
        lightNormalized.append(normalizeLight(light, maxLight, minLight))
    
    graphLocalizationInOrder(positions[0])
    graphLocalization(positions)
    
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

main1()