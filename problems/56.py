#!/usr/bin/python

def sumOfDigits(x):
    s = 0
    for c in str(x):
        s += int(c)
    return s

def prob56():
    m = 0
    for a in range(1, 100):
        for b in range(1, 100):
            sod = sumOfDigits(a ** b)
            if sod > m:
                m = sod
    print("max sum: %s" % m)

prob56()
