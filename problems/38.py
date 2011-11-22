#!/usr/bin/python

import sys
sys.path.append('../helpers')
import mathHelper

def prob38():
    top = 0
    n = 1
    while n < 10000000:
        m = 1
        s = ""
        while len(s) < 9:
            p = n * m
            s += str(p)
            m += 1
        if len(s) == 9 and mathHelper.isPandigital(s) and int(s) > top:
            top = int(s)
        n += 1
    print("Found: %s" % top)


prob38()
