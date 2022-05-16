from math import sqrt
from typing import Callable, List
import matplotlib.pyplot as plt
import numpy as np
from gui import window

ALPHA = (sqrt(5)+1)/2   #Golden Ratio


def minimizePowell(func: Callable[[float, float, float, float, float], float], start: List[float],
                   eps1: float, eps2: float, gssRange: List[float], maxIter: int):
    dim = len(start)

    stepList = []
    dirVectors = np.identity(dim)
    currentIteration = 0

    points = np.zeros((dim+1, dim))
    startPoint = np.array(start)
    plt.plot(startPoint[0], startPoint[1], marker='o',
    markersize=8, markeredgecolor="red", markerfacecolor="red" )
    while(currentIteration < maxIter):
        currentIteration = currentIteration + 1
        # print(
        #     f'Iteration start: {currentIteration}\n{startPoint}')
        #print(f'start1 {startPoint}')
        points[0] = findMinimumByDir(func, dirVectors[0], startPoint, gssRange)
        for i in range(1, dim):
            points[i] = findMinimumByDir(
                func, dirVectors[i], points[i-1], gssRange)

        newDir = np.subtract(points[dim-1], startPoint)
        points[dim] = findMinimumByDir(func, newDir, points[dim-1], gssRange)
        #print(f'start2 {startPoint}')
        for i in range(dim-1):
            dirVectors[i] = np.copy(dirVectors[i+1])
        dirVectors[dim-1] = np.copy(newDir)
        if any([any(np.isnan(x)) for x in points]):
            return 'Error', *points
        if(dim == 2):
            #print(f'Line via {startPoint} {points[0]} {points[1]} {points[2]}')
            plt.plot([startPoint[0], points[0][0]], [
                     startPoint[1], points[0][1]], 'k-')
            plt.plot(startPoint[0], startPoint[1], marker='o',
                    markersize=3.5, markeredgecolor="red", markerfacecolor="red" )
            plt.plot([points[0][0], points[1][0]], [
                     points[0][1], points[1][1]], 'k-')
            plt.plot(points[0][0], points[0][1], marker='o',
                    markersize=3, markeredgecolor="gray", markerfacecolor="gray" )
            plt.plot([points[1][0], points[2][0]], [
                     points[1][1], points[2][1]], 'k-')
            plt.plot(points[1][0], points[1][1], marker='o',
                    markersize=3, markeredgecolor="gray", markerfacecolor="gray" )

        l = points
        stepList.append(np.copy(startPoint))
       # for i in range 
        #stepList.append(np.copy(np.delete(np.delete(points, -1),-1)))
        stepList.append(np.copy(l[:-1]))
       # stepList.append(np.copy(points))
       # print(points)
       # print(startPoint)
        #print(stepList)

        startPoint = np.copy(points[dim])
        diff = abs(func(*points[dim]) - func(*points[0]))
        # print(
        #     f'Iteration end: {currentIteration}\n{points}\nDiff: {diff}')

        if diff < eps2:
            return points[dim], func(*points[dim]), 'eps2', diff, stepList
        elif all([vectorLength(points[i],points[dim-1]) < eps1 for i in range(0,dim-1)]):
            return points[dim], func(*points[dim]), 'eps1', f'Value {[vectorLength(points[i],points[dim-1]) < eps1 for i in range(0,dim-1)]}', stepList
    return points[dim], func(*points[dim]), 'Max Iteration', f'Iteration count: {currentIteration}'


def findMinimumByDir(func: Callable[[float, float, float, float, float], float], direction: List[float],
                     startPoint: List[float], gssrange: List[float]) -> List[float]:
    normalizedDir = normalizeVector(direction)
    #print(f'{startPoint} {normalizedDir} {gssrange}')
    
    p0 = [startPoint[i] + gssrange[0]*normalizedDir[i] for i in range(len(direction))]
    p1 = [startPoint[i] + gssrange[1]*normalizedDir[i] for i in range(len(direction))]

    print(f'Minimize from {p0} to {p1}')
    return goldenSection(func, p0, p1)


def goldenSection(f: Callable[[float, float, float, float, float], float], a: List[float], b: List[float], tol=0.001, iter=100):
    c = np.subtract(b, np.divide(np.subtract(b, a), ALPHA))
    d = np.add(a, np.divide(np.subtract(b, a), ALPHA))
    i = 0
    while vectorLength(np.zeros(len(a)), np.subtract(a, b)) > tol and i < iter:
        i = i+1
        if f(*c) < f(*d):  # f(c) > f(d) to find the maximum
            b = np.copy(d)
        else:
            a = np.copy(c)

        c = np.subtract(b, np.divide(np.subtract(b, a), ALPHA))
        d = np.add(a, np.divide(np.subtract(b, a), ALPHA))
    return np.divide(np.add(a, b), 2)


def vectorLength(startPoint: List[float], endPoint: List[float]) -> float:
    assert(len(startPoint) == len(endPoint))
    sum = 0
    for x in range(len(startPoint)):
        sum = sum + pow((endPoint[x] - startPoint[x]), 2)
    l = sqrt(sum)
    return l


def normalizeVector(x: List[float]) -> List[float]:
    length = vectorLength(np.zeros(len(x)), x)
    if(length == 0):
        return [0 for v in x]
    return [v/length for v in x]
