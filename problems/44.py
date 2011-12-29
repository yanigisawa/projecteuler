#!/usr/bin/python

import sys
sys.path.append('../helpers')
from mathHelper import *

def prob44():
    maxI = 10000
    maxJ = 10000
    smallest = 5000
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
                if difference < smallest:
                    smallest = difference
                    print("New Smallest: %s" % smallest)
                print("[%s, %s] - [%s, %s] - Difference: %s - Sum: %s" % (i, j, v1, v2, difference, sumation))
                #return


prob44()
