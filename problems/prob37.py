#!/usr/bin/python

import sys
sys.path.append('../helpers')
from primes import *
from mathHelper import *

primes = getPrimes()

def isTruncatablePrime(x):
    if x <= 7: return False

    xstr = str(x)

    for i in range(len(xstr)):
        y = int(xstr[i:])
        if y not in primes: 
            return False

    for i in range(1, len(xstr) + 1):
        y = int(xstr[0:i])
        if y not in primes:
            return False

    return True

def test():
    count = 0
    trunc = []
    for p in primes:
        if p > 7 and isTruncatablePrime(p):
            count = count + 1
            trunc.append(p)

    print("Found %s truncatable primes" % count)
    print(trunc)

test()
#primes = getPrimes()
#print(isTruncatablePrime(7043))
