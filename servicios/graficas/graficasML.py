import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.lines as mlines
from sklearn import preprocessing
from sklearn import svm

def lightML(lights, positions):
    X = lights
    Y = positions
    
    fig, ax = plt.subplots()
    plt.xlabel('Lux (dBm)')
    plt.ylabel('Positions')
    
    x = []
    y = []
    
    for light in lights:
        x.append(light[0])
        y.append(float(light[1]))
    
    clf = svm.SVC(kernel='linear')
    clf.fit(X, Y)
    
    print(clf.predict([[96.0, 7.0]]))
    
    """
    w = clf.coef_[0]
    print(w)

    a = -w[0] / w[1]

    xx = np.linspace(0,7)
    yy = a * xx - clf.intercept_[0] / w[1]

    h0 = plt.plot(xx, yy, 'k-', label="non weighted div")
    """
    
    plt.grid()
    plt.scatter(x,y)
    plt.show()
    
