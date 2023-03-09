import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patheffects


def drawF(points, stepDistance):
    x = np.arange(-5, 5, 0.01)
    y = f(x)
    xPoints = [point[0] for point in points]
    y1 = [f(point) for point in xPoints]
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.scatter(points, y1, color="red", s=20)
    ax_name = f"Start: x={xPoints[0]}, Steps: {len(xPoints)}, Step distance: {stepDistance}"
    ax.set(xlabel="x", ylabel="y", title=ax_name, xticks=np.arange(-3, 4), yticks=[20, 40, 60, 80], xlim=(-3, 3), ylim=(0, 100))
    ax.grid()
    plt.show()

def F_value(xVec):
    pointVec = []
    for point in xVec:
        xVal = point[0]
        yVal = 0.25 * xVal**4
        pointVec.append([xVal, yVal])
    return pointVec

def f(x):
    return x**4