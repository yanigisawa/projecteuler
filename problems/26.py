#!/usr/local/bin/python

import sys
sys.path.append("../helpers")
from primes import getPrimes

decimalPrecision = 10

def decimalRecurrence(x):
    s = str(x)[2:]
    if x == 2 or x == 5:
        return 0

    i = 1
    # http://en.wikipedia.org/wiki/Cyclic_number#Form_of_cyclic_numbers
    while ((10 ** i) - 1) % x != 0:
        i = i + 1

    return i

def prob26():
    max = 0
    d = 0
    primes = getPrimes()
    for n in primes:
        if n > 1000: break
        recur = decimalRecurrence(n)
        if recur > max:
            max = recur
            d = n

    print("Max Recurrence: %s - d = %s" % (max, d))

prob26()
