#!/usr/bin/python

import sys
sys.path.append('../helpers/')
import primes

def isPandigital(n):
    nstr = str(n)
    cpy = nstr
    for x in range(1, len(nstr) + 1):
        if str(x) in nstr:
            cpy = cpy.replace(str(x), "", 1) # replace only 1 character
        else:
            return False

    return cpy == ""

def prob41():
    p = primes.getPrimes()
    largest = 0
    for x in p:
        if isPandigital(x) and x > largest:
            largest = x
    return largest

print("Largest: %s" % prob41())
