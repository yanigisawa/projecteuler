#!/usr/bin/python

import sys
sys.path.append('../helpers')
from mathHelper import *

def prob44():
    maxI = 100000
    for i in range(1, maxI):
        for j in range(1, i):
            pi = getPentagonal(i)
            pj = getPentagonal(j)
            v1 = max(pi, pj)
            v2 = min(pi, pj)
            difference = v1 - v2
            sumation = v1 + v2
            #print("[%s, %s] - [%s, %s] - Difference: %s - Sum: %s" % (i, j, pi, pj, difference, sumation))
            if isPentagonal(difference) and isPentagonal(sumation):
                print("Answer: %s" % difference)
                return

prob44()
