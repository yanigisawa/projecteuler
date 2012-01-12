#!/usr/bin/python

import sys
# default recurssion limit is 1000
sys.setrecursionlimit(2000)

def reduceFraction(frac):
    twoNumerator = frac[1] * 2
    num = twoNumerator + frac[0]
    #invert fraction for 1 / fraction
    return [frac[1], num]

def solveFraction(i):
    if i < 0:
        return []
    if i == 0:
        return [1, 2]
    if i == 1:
        return reduceFraction([1, 2])

    frac = solveFraction(i - 1)
    return reduceFraction(frac)

def prob57():
    answer = 0
    for i in range(1001):
        f = solveFraction(i)
        numerator = f[1] + f[0]
        if len(str(numerator)) > len(str(f[1])):
            answer += 1
    print("Answer: %s" % answer)

prob57()
