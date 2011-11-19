#!/usr/bin/python

import sys
sys.path.append('../helpers/')
import mathHelper

def isUnorthodoxFraction(num, den):
    if num % 10 == 0 or den % 10 == 0: return False
    if num == den: return False
    numstr = str(num)
    denstr = str(den)
    c = numstr[0]
    c1 = denstr[1]
    if numstr[1] == denstr[0]:
        if float(numstr[0]) / int(denstr[1]) == num / float(den):
            return True

    return False

def prob33():
    fractions = []
    for n in range(10, 100):
        for d in range(10, 100):
            if isUnorthodoxFraction(n, d):
                fractions.append([n, d])

    denM = 1
    numM = 1
    for frac in fractions:
        red = mathHelper.reduceFraction(frac[0], frac[1])
        denM *= int(red[1])
        numM *= int(red[0])
    answer = mathHelper.reduceFraction(numM, denM)

    print("reduced fraction: %s" % answer)

prob33()
