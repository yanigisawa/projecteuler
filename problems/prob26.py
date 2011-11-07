#!/usr/local/bin/python

from decimal import *
from time import sleep

decimalPrecision = 105000

def decimalRecurrence(x):
    s = str(x)[2:]
    if len(s) < decimalPrecision:
        return 0
    r = []
    prev = ''
    didRepeat = False
    #print(s)
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            l = j - i
            if s[i:i+l] == s[j:j+l]:
                return l

    return 0

def prob26():
    max = 0
    d = 0
    getcontext().prec = decimalPrecision
    for n in (range(1, 1001)):
        fraction = 1 / Decimal(n)
        recur = decimalRecurrence(fraction)
        if recur > max:
            max = recur
            d = n
        #print("1 / %s = %s - Recurrence: %s" % (n, fraction, recur))

    print("Max Recurrence: %s - d: %s" % (max, d))

prob26()
