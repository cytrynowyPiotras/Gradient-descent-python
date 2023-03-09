from matplotlib import pyplot as plt
import numpy as np
from math import e


def drawG(pointsVec, stepDistance):
    xlist = np.linspace(-4.0, 3.0, 100)
    ylist = np.linspace(-3.0, 4.0, 100)
    X, Y = np.meshgrid(xlist, ylist)
    Z = (2-e**(-X**2-Y**2)-0.5*e**(-(X+1.5)**2-(Y-2)**2))
    fig,ax=plt.subplots(1,1)
    cp = ax.contourf(X, Y, Z)
    fig.colorbar(cp) # Add a colorbar to a plot
    ax.set_title(f"Starting Point: {pointsVec[0]}, Steps: {len(pointsVec)}, Step distance: {stepDistance}")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    for i in range(0, len(pointsVec)-1):
        xPos = pointsVec[i][0]
        yPos = pointsVec[i][1]
        xLen = pointsVec[i+1][0] - xPos
        yLen = pointsVec[i+1][1] - yPos
        plt.arrow(xPos, yPos, xLen, yLen)
    plt.show()


