import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

class data:
    pos = 'position'
    lig = 'light'
    POSI = 'POSI'
    LIGH = 'LIGH'

def getArrPos(arg, pos):
    aux=[]
    
    for a in arg:
        aux.append(a[pos])
    return aux
    
def format(arg,type):
    for a in arg:
        index=arg.index(a)
        arg[index]=float(a)

    if type == data.pos:
        arg.pop()
        arg.pop()
        arg.remove(arg[1])
        return arg
    if type == data.lig:
        arg.remove(arg[3])
        arg.remove(arg[1])
        return arg

def main():
    ruta_Archivo = sys.argv[1]
    positions = []
    lights = []
    
    archivo = open(ruta_Archivo, "r")
    datos   = archivo.readlines()
    
    for element in datos:
        if  element.startswith(data.LIGH):
            formatted = format(element[5:-1].split(';'),data.lig)
            lights.append(formatted)  
        if element.startswith(data.POSI):
            print(element)
            formatted = format(element[5:-1].split(';'),data.pos)
            positions.append(formatted)  
        
    fig, ax = plt.subplots()
    ax.plot(getArrPos(lights,0),getArrPos(lights,1))
    #Agregamos las etiquetas y añadimos una leyenda.
    plt.xlabel('Time')
    plt.ylabel('Lux')
    plt.title("Light Intensity")
    plt.legend()
    plt.savefig('grafica_lineal.png')
    plt.show()

    x = np.array(getArrPos(positions,2))
    y = np.array(getArrPos(positions,1))
    # Gráfico
    fig, ax = plt.subplots()
    
    plt.plot(x, y, "-ok", label = "Puntos")
    plt.legend(loc = "upper right")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("Localizations")
    plt.legend()
    plt.savefig('grafica_lineal.png')
    plt.show()
    
    fig, ax = plt.subplots()
    ax.plot(getArrPos(positions,0),getArrPos(positions,1))
    #Agregamos las etiquetas y añadimos una leyenda.
    plt.xlabel('Time')
    plt.ylabel('Positions')
    plt.title("Laitutde in time")
    plt.legend()
    plt.savefig('grafica_lineal.png')
    plt.show()
            
main()
