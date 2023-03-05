from clases.classes import data
import numpy as np

def getArrayIndex(arg, index):
    aux=[]
    
    for a in arg:
        aux.append(a[index])
    return aux
    
def format(arg,type):
    for a in arg:
        index = arg.index(a)
        arg[index] = float(a)

    if type == data.position:
        arg.pop()
        arg.pop()
        arg.remove(arg[1])
        return arg
    if type == data.light:
        arg.remove(arg[3])
        arg.remove(arg[1])
        return arg

def lightFormat(lights):
    auxLight=[]
    for light in lights:
        auxLight.append(np.array(light) / np.array([1, 1000]))
    return auxLight