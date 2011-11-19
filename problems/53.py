#!/usr/bin/python

import sys
sys.path.append('../helpers/')
import mathHelper

def prob53():
    count = 0
    for n in range(101):
        for r in range(n):
            if mathHelper.getCombinations(n, r) > 1000000:
                count += 1
                #print("New Over Million: C(%s, %s)" % (n, r))
    return count

print("Count: %s" % prob53())
