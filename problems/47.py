#!/usr/bin/python

import sys
sys.path.append('../helpers')
import mathHelper

def getDistinctPrimeFactors(factors):
    distinctFactors = []
    for f in factors:
        if f not in distinctFactors:
            distinctFactors.append(f)

    return distinctFactors

def prob47():
    factorLists = []
    curr = []
    factorLength = 4
    prev = []
    for i in range(100000, 1000000):
        if i % 1000 == 0: print("i: %s" % i)
        if mathHelper.isPrime(i):
            if len(factorLists) > 0: factorLists.pop()
            continue

        curr = getDistinctPrimeFactors(mathHelper.getPrimeFactors(i))

        if len(factorLists) >= 1:
            prev = factorLists[-1]

            if prev[0] < i - 1:
                factorLists = []
            elif prev[1] == curr: 
                factorLists.pop(0)

        if prev != curr and len(curr) == factorLength:
            tmp = [i, curr]
            factorLists.append(tmp)

        if len(factorLists) == factorLength:
            break

    print("Factors: %s" % (factorLists))

prob47()
