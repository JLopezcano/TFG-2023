import matplotlib
import matplotlib.pyplot as plt
from servicios.mapeo.mapeos import getArrayIndex
import numpy as np

def graphLightByTime(lights):
    fig, ax = plt.subplots()
    ax.plot(getArrayIndex(lights,0),getArrayIndex(lights,1))
    #Agregamos las etiquetas y añadimos una leyenda.
    plt.xlabel('Time')
    plt.ylabel('Lux')
    plt.title("Light Intensity")
#    plt.legend()
    plt.savefig('grafica_lineal.png')
    plt.show()

def graphLocalization(positions):
    x = np.array(getArrayIndex(positions,2))
    y = np.array(getArrayIndex(positions,1))
    # Gráfico
    fig, ax = plt.subplots()
    
    plt.plot(x, y, "-ok", label = "Puntos")
    plt.legend(loc = "upper right")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("Localizations")
#    plt.legend()
    plt.savefig('grafica_lineal.png')
    plt.show()
    
def graphLatitudeByTime(positions):
    fig, ax = plt.subplots()
    ax.plot(getArrayIndex(positions,0),getArrayIndex(positions,1))
    #Agregamos las etiquetas y añadimos una leyenda.
    plt.xlabel('Time')
    plt.ylabel('Positions')
    plt.title("Laitutde in time")
#    plt.legend()
    plt.savefig('grafica_lineal.png')
    plt.show()

def graphLongitudeByTime(positions):
    fig, ax = plt.subplots()
    ax.plot(getArrayIndex(positions,0),getArrayIndex(positions,2))
    #Agregamos las etiquetas y añadimos una leyenda.
    plt.xlabel('Time')
    plt.ylabel('Positions')
    plt.title("Longitude in time")
#    plt.legend()
    plt.savefig('grafica_lineal.png')
    plt.show()