import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.lines as mlines
from sklearn import preprocessing

from servicios.mapeo.mapeos import getArrayIndex
#from servicios.mapeo.mapeos import lightFormat
from clases.classes import colours

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

def graphLightByTimeToList(lights):
    arrayLegend = []
    
    fig, ax = plt.subplots()
    for light in lights:
        ax.plot(getArrayIndex(light,0),getArrayIndex(light,1))
        arrayLegend.append("text"+ str(lights.index(light)+1))
    #Agregamos las etiquetas y añadimos una leyenda.
    plt.xlabel('Time')
    plt.ylabel('Lux')
    plt.title("Light Intensity")
    plt.legend(arrayLegend, loc="upper left")
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


def graphLocalizationsInOrder(position, positions):
    arrayLegend = []
    colourGraph = ['black', 'grey', 'yellow', 'green', 'purple', 'blue', 'pink', 'red', 'orange', 'gold',
                  'lime', 'brown', 'turquoise', 'olivedrab', 'darkkhaki', 'teal', 'sienna', 'peru', 'tan']
    
    for posi in position:
        x = np.array(posi[2])
        y = np.array(posi[1])
        arrayLegend.append(position.index(posi)+1)
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.title("Localizations")
        plt.plot(x, y, "-ok", label = str(position.index(posi)), color=colourGraph[position.index(posi)])
    plt.legend(arrayLegend, loc="upper center")
    
    # Gráfico
    x = np.array(getArrayIndex(positions,2))
    y = np.array(getArrayIndex(positions,1))
    #arrayLegend.append("text"+ str(position.index(position)+1))
    # Gráfico
    plt.plot(x, y, label = "pixel", color='grey')
    plt.grid()
    plt.show()

def graphLocalizationInList(positions):
    arrayLegend = []
    
   # for posi in position:
    x = np.array(getArrayIndex(positions,2))
    y = np.array(getArrayIndex(positions,1))
    #arrayLegend.append("text"+ str(position.index(position)+1))
    # Gráfico
    fig, ax = plt.subplots()
    
    plt.plot(x, y, "-ok", label = "Puntos")
    plt.grid()
    plt.legend(loc = "upper right")
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title("Localizations")
    plt.legend(arrayLegend, loc="upper left")
    plt.savefig('grafica_lineal.png')
    plt.show()

def graphLatitudeByTime(positions):
    fig, ax = plt.subplots()
    ax.plot(getArrayIndex(positions,0),getArrayIndex(positions,1))
    #Agregamos las etiquetas y añadimos una leyenda.
    plt.xlabel('Time')
    plt.ylabel('Positions')
    plt.title("Latitude in time")
#    plt.legend()
    plt.savefig('grafica_lineal.png')
    plt.show()
    
def graphLatitudeByTimeToList(positions):
    arrayLegend = []
    
    fig, ax = plt.subplots()
    for position in positions:
        ax.plot(getArrayIndex(position,0),getArrayIndex(position,1))
        arrayLegend.append("text"+ str(positions.index(position)+1))
    #Agregamos las etiquetas y añadimos una leyenda.
    plt.xlabel('Time')
    plt.ylabel('Positions')
    plt.title("Latitude in time")
    plt.legend(arrayLegend, loc="upper left")
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
    
def graphLongitudeByTimeToList(positions):
    arrayLegend = []
    
    fig, ax = plt.subplots()
    for position in positions:
        ax.plot(getArrayIndex(position,0),getArrayIndex(position,2))
        arrayLegend.append("text"+ str(positions.index(position)+1))
    #Agregamos las etiquetas y añadimos una leyenda.
    plt.xlabel('Time')
    plt.ylabel('Positions')
    plt.title("Longitude in time")
    plt.legend(arrayLegend, loc="upper left")
    plt.savefig('grafica_lineal.png')
    plt.show()

def graphPositionAndLightByTime(positions, lights):
    
    fig, ax = plt.subplots()
    ax.plot(getArrayIndex(lights,0),getArrayIndex(lights,1), marker='+', color='black')
    ax.plot(getArrayIndex(positions,0),getArrayIndex(positions,1), marker='*', color='green')
    ax.plot(getArrayIndex(positions,0),getArrayIndex(positions,2), marker='^', color='grey')
    #Agregamos las etiquetas y añadimos una leyenda.
    plt.xlabel('Time')
    plt.ylabel('Lux and Lat/Long')
    plt.title("Variation by time")
    plt.legend(["Light", "Latitude", "Longitude"], loc="upper left")
    plt.savefig('grafica_lineal.png')
    plt.show()
    
def graphPositionAndLightByTimeToList(positions, lights):

    LightMarker = mlines.Line2D([], [], color='blue', marker='+', linestyle='None', markersize=10, label='Light')
    LatitudeMarker = mlines.Line2D([], [], color='blue', marker='*', linestyle='None', markersize=10, label='Latitude')
    LongitudeMarker = mlines.Line2D([], [], color='blue', marker='^', linestyle='None', markersize=10, label='Longitude')
    #scaler = preprocessing.MinMaxScaler(feature_range=(0,1))
    
    fig, ax = plt.subplots()
    for light in lights:
        ax.plot(getArrayIndex(light,0),getArrayIndex(light,1), marker='+')
    for position in positions:
        ax.plot(getArrayIndex(position,0),getArrayIndex(position,1), marker='*')
    for position in positions:
        ax.plot(getArrayIndex(position,0),getArrayIndex(position,2), marker='^')
    #Agregamos las etiquetas y añadimos una leyenda.
    plt.xlabel('Time')
    plt.ylabel('Lux and Lat/Long')
    plt.title("Variation by time")
    plt.legend(handles=[LightMarker, LatitudeMarker, LongitudeMarker], loc="upper left")
    plt.savefig('grafica_lineal.png')
    plt.show()
    
def graphLuxByLocalization(lights):
    #LightMarker = mlines.Line2D([], [], color='blue', marker='+', linestyle='None', markersize=10, label='Light')
    arrayLegend = []
    
    fig, ax = plt.subplots()
    for light in lights:
        ax.scatter(getArrayIndex(light,0),getArrayIndex(light,1), marker='+')       #ax.plot
        arrayLegend.append("text"+ str(lights.index(light)+1))
    #Agregamos las etiquetas y añadimos una leyenda.
    plt.xlabel('Position')
    plt.ylabel('Lux')
    plt.title("Variation by time")
    plt.legend(arrayLegend, loc="upper left")
    plt.savefig('grafica_lineal.png')
    plt.grid()
    plt.show()

def graphLuxByLocalizationMean(lights, means):
    arrayLegend = []
    
    fig, ax = plt.subplots()
    for light in lights:
        ax.scatter(getArrayIndex(light,0),getArrayIndex(light,1), marker='+')
        arrayLegend.append("text"+ str(lights.index(light)+1))

    #Agregamos las etiquetas y añadimos una leyenda.
    
    x = np.array(getArrayIndex(means,0))
    y = np.array(getArrayIndex(means,1))
    # Gráfico
    plt.plot(x, y, label = "pixel", color='grey')
    plt.grid()
    plt.xlabel('Position')
    plt.ylabel('Lux')
    plt.title("Variation by Positions")
    plt.legend(arrayLegend, loc="upper left")
    plt.savefig('grafica_lineal.png')
    plt.show()
    
def graphLuxByLocalizationMeanBoxplots(ordereds):
    array = []
    newArray = []
    
    fig, ax = plt.subplots()

    positionArray=[]
    for ordered in ordereds:
            positionArray.append(ordered[0])
    
    for position in positionArray:
        for ordered in ordereds:
            if ordered[0]==position:
                array.append(ordered[1])
        newArray.append(array)
        array=[]

    bp = ax.boxplot(newArray) 
    
    #Agregamos las etiquetas y añadimos una leyenda.
    
    # Gráfico
    plt.xlabel('Position')
    plt.ylabel('Lux')
    plt.title("Aproximated Luxes in mean")
    plt.savefig('grafica_lineal.png')
    plt.grid()
    plt.show()
    
def graphLuxByLocalizationPositionsBoxplots(ordereds):
    array = []
    newArray = []
    
    fig, ax = plt.subplots()

    for ordered in ordereds:
        for positions in ordered:
            array.append(positions[1])
        newArray.append(array)
        array=[]
        
    bp = ax.boxplot(newArray) 
    
    #Agregamos las etiquetas y añadimos una leyenda.
    
    # Gráfico
    plt.xlabel('Position')
    plt.ylabel('Lux')
    plt.title("Aproximated Luxes minus mean")
    plt.savefig('grafica_lineal.png')
    plt.grid()
    plt.show()
    
def graphWifisByPositions(wifis, means):
    arrayLegend = []
    
    fig, ax = plt.subplots()
         
    x = np.array(getArrayIndex(means,1))
    y = np.array(getArrayIndex(means,0))
    arrayLegend.append("Txt de datos:")
    plt.plot(x, y, label = "pixel", color='white')
    
    for wifi in wifis:
        ax.scatter(getArrayIndex(wifi,-1),getArrayIndex(wifi,3), marker='+')       #ax.plot
        arrayLegend.append("text"+ str(wifis.index(wifi)+1))
    #Agregamos las etiquetas y añadimos una leyenda.
    plt.xlabel('Positions')
    plt.ylabel('Wifi RSS(dBm)')
    plt.title("Wifi RSS by Positions")
    plt.legend(arrayLegend, loc="upper left")
    plt.savefig('grafica_lineal.png')
    plt.grid()
    plt.show()
    
def graphWifisByPositionsBoxplots(wifis):
    array = []
    newArray = []
    
    fig, ax = plt.subplots()

    for wifi in wifis:
        for element in wifi:
            array.append(element[3])
        newArray.append(array)
        array=[]
        
    bp = ax.boxplot(newArray) 
    
    #Agregamos las etiquetas y añadimos una leyenda.
    
    # Gráfico
    plt.xlabel('Position')
    plt.ylabel('RSS (dBm)')
    plt.title("Aproximated RSS minus mean")
    plt.savefig('grafica_lineal.png')
    plt.grid()
    plt.show()