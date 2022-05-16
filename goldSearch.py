from math import sqrt
from typing import Callable, List
import matplotlib.pyplot as plt
import numpy as np
import math
ALPHA = (sqrt(5)+1)/2


def minimizePowell(func: Callable[[float, float], float], start: List[float], eps1: float, eps2: float, range: List[float], maxIter: int):
    dirVectors = [
        [1, 0],
        [0, 1]
    ]
    currentIteration = 0

    startPoint = np.array([start[0], start[1]])
    x3 = [0,0]
    while(currentIteration < maxIter):
        currentIteration = currentIteration + 1

        x1 = findMinimumByDir(func, dirVectors[0], startPoint, range)

        x2 = findMinimumByDir(func, dirVectors[1], x1, range)
        dir = np.subtract(x2, startPoint)
        x3 = findMinimumByDir(func, dir, x2, range)
        dirVectors[0] = dirVectors[1]
        dirVectors[1] = dir
        if any(np.isnan(x1)) or any(np.isnan(x2)) or any(np.isnan(x3)):
            return 'Error',f'P1: {x1}',f'P2: {x2}',f'P3: {x3}'

        plt.plot([startPoint[0], x1[0]], [startPoint[1], x1[1]], 'k-')
        plt.plot([x1[0], x2[0]], [x1[1], x2[1]], 'k-')
        plt.plot([x2[0], x3[0]], [x2[1], x3[1]], 'k-')

        startPoint = x3

        diff = abs(func(x3[0], x3[1]) - func(x1[0], x1[1]))
        print(
            f'Iteration: {currentIteration} \n \
            P1: {x1} \n \
            P2: {x2} \n \
            P3: {x3} \n \
            Diff: {diff}')

        if diff < eps2:
            return x3, func(x3[0], x3[1]), 'eps2', f'Value difference: {diff}'
        elif vectorLength(x1,x3) < eps1 or vectorLength(x2,x3) < eps1:
            return x3, func(x3[0], x3[1]), 'eps1', f'P1->P3:{vectorLength(x1,x3)}\nP2->P3:{vectorLength(x2,x3)}'
    return x3, func(x3[0], x3[1]), 'Max Iteration', f'Iteration count: {currentIteration}'


def findMinimumByDir(func: Callable[[float, float], float], direction: tuple[float, float],
                     startPoint: tuple[float, float], range: tuple[float, float]) -> tuple[float, float]:
    dir = normalizeVector(direction[0], direction[1])

    p0 = [startPoint[0] + range[0]*dir[0],
          startPoint[1]+range[0]*dir[1]]
    p1 = [startPoint[0] + range[1]*dir[0],
          startPoint[1]+range[1]*dir[1]]
    #print(f'Minimize from {p0} to {p1}')
    return goldenSection(func, [p0[0], p0[1]], [p1[0], p1[1]])


def goldenSection(f: Callable[[float, float], float], a: tuple[float, float], b: tuple[float, float], tol=0.001, iter=100):
    c = np.subtract(b, np.divide(np.subtract(b, a), ALPHA))
    d = np.add(a, np.divide(np.subtract(b, a), ALPHA))
    i = 0
    while vectorLength([0, 0], np.subtract(a, b)) > tol and i < iter:
        i = i+1
        if f(c[0], c[1]) < f(d[0], d[1]):  # f(c) > f(d) to find the maximum
            b = d
        else:
            a = c

        c = np.subtract(b, np.divide(np.subtract(b, a), ALPHA))
        d = np.add(a, np.divide(np.subtract(b, a), ALPHA))
    return np.divide(np.add(a, b), 2)


def vectorLength(startPoint: tuple[float, float], endPoint: tuple[float, float]) -> float:
    l = sqrt((endPoint[0]-startPoint[0])**2+(endPoint[1]-startPoint[1])**2)
    return l


def normalizeVector(x: float, y: float) -> tuple[float, float]:
    length = vectorLength([0, 0], [x, y])
    return [x/length, y/length]
