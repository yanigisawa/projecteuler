#!/usr/bin/python

#Found 11 truncatable primes
#[23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
#Sum 748317: 
#
#real	15m16.034s
#user	15m14.801s
#sys	0m1.173s


import sys
sys.path.append('../helpers')
from primes import *
from mathHelper import *

allPrimes = getPrimes()
primes = getPrimesForTruncation()

def isTruncatablePrime(x):
    if x <= 7: return False

    xstr = str(x)

    for i in range(len(xstr)):
        y = int(xstr[i:])
        if y not in allPrimes:
            return False

    for i in range(1, len(xstr) + 1):
        y = int(xstr[0:i])
        if y not in allPrimes:
            return False

    return True

def prob37():
    count = 0
    trunc = []

    for p in primes:
        if p > 7 and isTruncatablePrime(p):
            count = count + 1
            trunc.append(p)

    print("Found %s truncatable primes" % count)
    print(trunc)
    print("Sum %s: " % sum(set(trunc)))

prob37()
