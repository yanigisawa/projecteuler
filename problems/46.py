#!/usr/bin/python

import sys
sys.path.append('../helpers')
import mathHelper
import primes

def isSumOfSquare(x):
    allPrimes = primes.getPrimesBelow(x)
    for p in allPrimes:
        y =1
        sos = p + 2 * y ** 2
        while sos < x:
            y += 1
            sos = p + 2 * y ** 2
        if sos == x:
            return True

    return False

def prob46():
    for i in range(1, 500000, 2):
        if not mathHelper.isPrime(i) and not isSumOfSquare(i):
            print("Answer: %s" % i)
            return

prob46()
