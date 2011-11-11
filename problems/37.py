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

primes = getPrimes()

def isTruncatablePrime(x):
    if x <= 7: return False

    xstr = str(x)
    if int(xstr[0]) not in [2, 3, 5, 7]: return False
    elif int(xstr[-1]) not in [3, 7]: return False
    elif '2' in xstr[1:]: return False
    elif '4' in xstr[1:]: return False
    elif '6' in xstr[1:]: return False
    elif '8' in xstr[1:]: return False

    for i in range(len(xstr)):
        y = int(xstr[i:])
        if y not in primes:
            return False

    for i in range(1, len(xstr) + 1):
        y = int(xstr[0:i])
        if y not in primes:
            return False

    return True

def prob37():
    count = 0
    trunc = []

    for p in primes:
        if p > 7 and isTruncatablePrime(p):
            count = count + 1
            trunc.append(p)
        if len(trunc) == 11:
            break

    print("Found %s truncatable primes" % count)
    print(trunc)
    print("Sum: %s" % sum(set(trunc)))

prob37()
