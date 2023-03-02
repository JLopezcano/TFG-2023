from clases.classes import data
from servicios.mapeo.mapeos import *

def readFiles(files, extension, filePath):
    lights = []
    positions = []
    
    for file in files:
        fullPath = ""
        fullPath = filePath / file
        if file.endswith(extension):   #falla el index, indicar que es el indice donde estoy, no el str que representa
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
