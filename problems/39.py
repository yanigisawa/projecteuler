#!/usr/bin/python

def isTriple(a, b, c):
    return ((a * a) + (b * b)) == (c * c)

def test():
    print("Triple: %s" % isTriple(20, 48, 52))

test()
