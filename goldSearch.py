from math import sqrt
from typing import Callable, List
import matplotlib.pyplot as plt
import numpy as np
import math
ALPHA = (sqrt(5)+1)/2


def runGold(func: Callable[[float, float], float], start: List[float], eps1: float, eps2: float, range: List[float], maxIter: int):
    dirVectors = [
        [1, 0],
        [0, 1]
    ]
    currentIteration = 0

    startPoint = np.array([start[0], start[1]])

    diff = 999999

    while(currentIteration < maxIter and diff > eps2):
        currentIteration = currentIteration + 1

        x1 = findMinimumByDir(func, dirVectors[0], startPoint, range)

        x2 = findMinimumByDir(func, dirVectors[1], x1, range)
        dir = np.subtract(x2, startPoint)
        x3 = findMinimumByDir(func, dir, x2, range)
        dirVectors[0] = dirVectors[1]
        dirVectors[1] = dir

        plt.plot([startPoint[0], x1[0]], [startPoint[1], x1[1]], 'k-')
        plt.plot([x1[0], x2[0]], [x1[1], x2[1]], 'k-')
        plt.plot([x2[0], x3[0]], [x2[1], x3[1]], 'k-')

        startPoint = x3

        diff = abs(func(x3[0], x3[1]) - func(x1[0], x1[1]))
        print(
            f'Iteration: {currentIteration} \n  Point: {startPoint} \
            \n Diff: {diff}')


def getVectorLength(startPoint: tuple[float, float], endPoint: tuple[float, float]) -> float:
    return sqrt((endPoint[0]-startPoint[0])**2+(endPoint[1]-startPoint[1])**2)


def normalizeVector(x: float, y: float) -> tuple[float, float]:
    length = getVectorLength([0, 0], [x, y])
    print(f'length: {length}')
    return [x/length, y/length]


def findMinimumByDir(func: Callable[[float, float], float], direction: tuple[float, float],
                     startPoint: tuple[float, float], range: tuple[float, float]) -> tuple[float, float]:
    dir = normalizeVector(direction[0], direction[1])

    p0 = np.array(startPoint) + range[0] * np.array(dir)
    p1 = np.array(startPoint) + range[1] * np.array(dir)
    return gss(func, [p0[0], p0[1]], [p1[0], p1[1]], dir)


def gss(f: Callable[[float, float], float], a: tuple[float, float], b: tuple[float, float], normalized: tuple[float, float], tol=0.01, iter=100):
    """Golden-section search
    to find the minimum of f on [a,b]
    f: a strictly unimodal function on [a,b]

    Example:
    >>> f = lambda x: (x-2)**2
    >>> x = gss(f, 1, 5)
    >>> print("%.15f" % x)
    2.000009644875678

    """
    wspdir = 1
    if(normalized[0] != 0):
        wspdir = normalized[1]/normalized[0]
    wspb = a[1]-wspdir*a[0]
    ax = a[0]
    bx = b[0]
    cx = bx - (bx - ax) / ALPHA
    dx = ax + (bx - ax) / ALPHA
    i = 0
    while abs(bx-ax) > tol and i < iter:
        i = i+1

        # print(f'{ax}\n{bx}\n{cx}\n{dx}\n\n\n')
        if f(cx, cx*(wspdir)+wspb) < f(dx, dx*(wspdir)+wspb):  # f(c) > f(d) to find the maximum
            bx = dx
        else:
            ax = cx

        # We recompute both c and d here to avoid loss of precision which may lead to incorrect results or infinite loop
        cx = bx - (bx - ax) / ALPHA
        dx = ax + (bx - ax) / ALPHA

    returnx = (bx+ax)/2
    return [returnx, returnx*(wspdir)+wspb]
