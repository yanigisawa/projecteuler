#!/usr/bin/python

import sys
sys.path.append('../helpers')
import mathHelper

def prob47():
    factorLists = []
    curr = []
    factorLength = 2
    prev = []
    for i in range(4, 17):
        print("i: %s" % i)
        if mathHelper.isPrime(i):
            factorLists.pop()
            continue

        curr = mathHelper.getPrimeFactors(i) 
        print("Prime Factors(%s) - %s" % (i, curr))


        if len(factorLists) > 1:
            prev = factorLists[-1]
            if prev == curr: 
                factorLists.pop(0)
        elif prev != curr:
            tmp = [i, curr]
            factorLists.append(tmp)

        if len(factorLists) == factorLength:
            break

    print("Factors: %s" % (factorLists))

prob47()
