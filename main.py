import sys
import os
from pathlib import Path

from servicios.rutas.rutas import *
from servicios.graficas.graficas import *

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

    

main()