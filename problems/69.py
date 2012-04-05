#!/usr/local/bin/python

import sys
sys.path.append("../helpers")
import mathHelper

def prob69():
    highest = 0
    highN = 0
    for n in xrange(2, 1000000):
        x = n / float(mathHelper.totient(n))
        if x > highest:
            highest = x
            highN = n


    print("Highest: %s - n: %s" % (highest, highN))


prob69()
    
