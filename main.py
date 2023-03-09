from math import exp
from FfuncPlot import drawF
from GfuncFlatPlot import drawG
import copy

class Solver():
    def __init__(self, func, gradFunc, stepDistance=float, resultApprox=1e-10):
        self.func = func
        self.gradFunc = gradFunc
        self.stepDistance = stepDistance
        self.resultApprox = resultApprox

    def solve(self, pointsVector):
        direction = self.gradFunc(pointsVector)
        gradientWay = []
        gradientWay.append(copy.deepcopy(pointsVector))
        nextPointsVec=[0, 0]
        for i in range(0, len(pointsVector)):
            nextPointsVec[i] = pointsVector[i] - self.stepDistance*direction[i]
        while (abs(self.func(nextPointsVec)[0]-self.func(pointsVector)[0]) > self.resultApprox):
            for i in range(0, len(pointsVector)):
                pointsVector[i] = nextPointsVec[i]
            direction = self.gradFunc(pointsVector)
            for i in range(0, len(pointsVector)):
                nextPointsVec[i] = pointsVector[i] - self.stepDistance*direction[i]
            gradientWay.append(copy.deepcopy(pointsVector))
        return nextPointsVec, gradientWay

def F_value(point):
    """returns value of function f in x"""
    posX=point[0]
    return [0.25*posX**4]

def G_value(pointsVec):
    """returns value of function in point (x, y)"""
    x, y = pointsVec[0], pointsVec[1]
    value = 2-exp(-x**2-y**2)-0.5*exp(-(x+1.5)**2-(y-2)**2)
    return [value]

def F_gradient_value(point):
    """returns value of function f gradient in x"""
    xPos= point[0]
    return [xPos**3]

def G_gradient_value(pointsVec):
    x, y = pointsVec[0], pointsVec[1]
    """returns vector of values function g gradient in (x, y)"""
    X_value = 2*x*exp(-x**2-y**2)+(x+1.5)*exp(-(x+1.5)**2-(y-2)**2)
    Y_value = 2*y*exp(-x**2-y**2)+(y-2)*exp(-(x+1.5)**2-(y-2)**2)
    return [X_value, Y_value]

def main():
    stepDistance = 0.1
    startingPoint = [-0.2, 1.5]
    funcDict = {"f":{"FuncValue":F_value,"FuncGrad":F_gradient_value, "DrawFunc":drawF},
                "g":{"FuncValue":G_value, "FuncGrad":G_gradient_value, "DrawFunc":drawG}}
    solver = Solver(G_value, G_gradient_value, stepDistance)
    gradWay = solver.solve(startingPoint)[1]
    drawG(gradWay, 0.1)

if __name__ == "__main__":
    main()