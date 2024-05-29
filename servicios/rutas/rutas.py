from clases.classes import data
from servicios.mapeo.mapeos import *

def readFiles(files, extension, filePath):
    lights = []
    positions = []
    
    for file in files:
        fullPath = ""
        fullPath = filePath / file
        if file.endswith(extension):
            file = open(fullPath, "r")
            lines = file.readlines()
            
            for line in lines:
                if  line.startswith(data.LIGH):
                    formatted = format(line[5:-1].split(';'),data.light)
                    lights.append(formatted)  
                if line.startswith(data.POSI):
                    formatted = format(line[5:-1].split(';'),data.position)
                    positions.append(formatted) 
                    
    return (lights, positions) 

def readFilesToLists(files, extension, filePath):
    lights = []
    positions = []
    wifis = []
        
    for file in files:
        fullPath = ""
        fullPath = filePath / file
        if file.endswith(extension):
            file = open(fullPath, "r")
            lines = file.readlines()
            fileLight = []
            filePosition = []
            fileWifi = []

            for line in lines:
                if line.startswith(data.LIGH):
                    formatted = format(line[5:-1].split(';'),data.light,0)
                    fileLight.append(formatted) 
                    
                if line.startswith(data.POSI):
                    formatted = format(line[5:-1].split(';'),data.position,0)
                    filePosition.append(formatted)
                
                if line.startswith(data.WIFI):
                    formatted = format(line[5:-1].split(';'),data.wifi,1)
                    fileWifi.append(formatted)
            
            lights.append(fileLight)
            positions.append(filePosition)
            wifis.append(fileWifi)
    
    return lights, positions, wifis