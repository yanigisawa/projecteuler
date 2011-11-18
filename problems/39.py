#!/usr/bin/python

import math

def isTriple(a, b, c):
    return ((a * a) + (b * b)) == (c * c)

def findSolutions(p):
    combinations = 0
    for a in range(p / 3):
        for b in range(a + 1, (p - a) / 2):
            c = (p - a) - b
            if isTriple(a, b, c):
                combinations += 1

    return combinations

def prob39():
    max = 0
    for n in range(1001):
        m = findSolutions(n)
        if m > max:
            max = m
            perim = n

    print("Max(%s): %s" % (perim, max))

prob39()
