from math import sqrt
from typing import Callable, List
import matplotlib.pyplot as plt
import numpy as np
ALPHA = (sqrt(5)-1)/2


def runGold(func: Callable[[float, float], float], startPoint: List[float], eps1: float, eps2: float, range: List[float], maxIter: int):
    currentIteration = 0
    minX = findMinimum(func, [startPoint[0] + range[0], startPoint[0] + range[1]],
                       [startPoint[1], startPoint[1]], maxIter)
    # print(minX)
    #plt.plot(minX[0], minX[1], "o")
    plt.plot([startPoint[0], minX[0]], [startPoint[1], minX[1]], 'k-')
    minY = findMinimum(func, [minX[0], minX[0]], [
                       minX[1]+range[0], minX[1]+range[1]])
    # print(minY)
    #plt.plot(minY[0], minY[1], "o")
    plt.plot([minX[0], minY[0]], [minX[1], minY[1]], 'k-')

    startPoint = np.array(startPoint)
    previousPoint = np.array([startPoint[0], startPoint[1]])
    currentPoint = np.array([minX[0], minY[1]])
    diff = abs(func(currentPoint[0], currentPoint[1]) -
               func(previousPoint[0], previousPoint[1]))
    while(currentIteration < maxIter and diff > eps2):
        currentIteration = currentIteration + 1
        print(
            f'Iteration: {currentIteration} \n Previous Point: {previousPoint} \n Current point: {currentPoint} \n Diff: {diff}')
        print(dir)
        previousPoint = currentPoint
        currentPoint = findMinimum(func, [previousPoint[0] - range[0], previousPoint[0] + range[0]],
                                   [previousPoint[1] - range[0], previousPoint[1] + range[1]])
        plt.plot([previousPoint[0], currentPoint[0]],
                 [previousPoint[1], currentPoint[1]])

        diff = abs(func(currentPoint[0], currentPoint[1]) -
                   func(previousPoint[0], previousPoint[1]))


def findMinimum(func: Callable[[float, float], float], xRange: List[float], yRange: List[float], iter=1000):
    tolerance = 1e-3
    #print(f'{xRange} {yRange}')
    a1 = xRange[0]
    b1 = xRange[1]

    a2 = yRange[0]
    b2 = yRange[1]

    x1 = a1+(1-ALPHA)*(b1 - a1)
    x2 = a1+(ALPHA)*(b1 - a1)
    y1 = a2+(1-ALPHA)*(b2 - a2)
    y2 = a2+(ALPHA)*(b2 - a2)

    fek = func(x1, y1)
    ffk = func(x1, y2)
    fhk = func(x2, y1)
    fgk = func(x2, y2)

    currentIteration = 1
    while(sqrt((b1-a1)**2+(b2-a2)**2) > tolerance and currentIteration < iter):
        currentIteration = currentIteration+1
        min1 = min([fek, ffk, fhk, fgk])

        if min1 == fek:
            b1 = x2
            b2 = y2
        elif min1 == ffk:
            b1 = x2
            a2 = y1
        elif min1 == fgk:
            a1 = x1
            a2 = y1
        elif min1 == fhk:
            a1 = x1
            b2 = y2

        x1 = a1+(1-ALPHA)*(b1 - a1)
        x2 = a1+(ALPHA)*(b1 - a1)
        y1 = a2+(1-ALPHA)*(b2 - a2)
        y2 = a2+(ALPHA)*(b2 - a2)
        fek = func(x1, y1)
        ffk = func(x1, y2)
        fhk = func(x2, y1)
        fgk = func(x2, y2)
    min1 = min([fek, ffk, fhk, fgk])
    #print(f'Minimum {min1} with iter: {currentIteration}')
    if min1 == fek:
        return (x1, y1)
    elif min1 == ffk:
        return (x1, y2)
    elif min1 == fgk:
        return (x2, y1)
    elif min1 == fhk:
        return (x2, y2)
