#!/usr/local/bin/python

import math
import sys
sys.path.append("../helpers")
from mathHelper import *

def prob23():
    abundants = []
    max = 28123
    for n in range(1, max):
        if isAbundantNumber(n):
            abundants.append(n)

    abundantSums = []
    for i in abundants:
        for j in abundants:
            s = i + j
            if s > max:
                break
            abundantSums.append(s)

    diffs = set(range(1, max)) - set(abundantSums)
    answer = sum(diffs)
    print("Sum of non abundant ints: %s" % answer)

prob23()

