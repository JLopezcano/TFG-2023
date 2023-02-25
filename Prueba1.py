import matplotlib
import matplotlib.pyplot as plt
import numpy as np


ruta_Archivo = "E:/mierdas estudios/mierdas uni/TFG/Primeras 4 trayectorias/01-Training/T01_01/T01_01.txt"

def cambiar_texto_en_posicion(ruta_archivo):
    archivo = open(ruta_archivo, "r")
    datos   = archivo.readlines()
    positions = []
    lights = []
    
    for element in datos:
        if  element.startswith('LIGH'):
            formatted = format(element[5:-1].split(';'),"light")
            lights.append(formatted)  
        if element.startswith('POSI'):
            print(element)
            formatted = format(element[5:-1].split(';'),"position")
            positions.append(formatted)  
    
    #print('datos: ', lights)
    
    fig, ax = plt.subplots()
    ax.plot(getArrPos(lights,0),getArrPos(lights,1))
    #Agregamos las etiquetas y añadimos una leyenda.
    plt.xlabel('Time')
    plt.ylabel('Lux')
    plt.title("Light Intensity")
    plt.legend()
    plt.savefig('grafica_lineal.png')
    plt.show()

    x = np.array(getArrPos(positions,1))
    y = np.array(getArrPos(positions,2))
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


def getArrPos(arg, pos):
    aux=[]
    for a in arg:
        aux.append(a[pos])
    return aux
    
def format(arg,type):
    for a in arg:
        index=arg.index(a)
        arg[index]=float(a)

    if type == 'position':
        arg.pop()
        arg.pop()
        arg.remove(arg[1])
        return arg
    if type == 'light':
        arg.remove(arg[3])
        arg.remove(arg[1])
        return arg
            
cambiar_texto_en_posicion(ruta_Archivo)
