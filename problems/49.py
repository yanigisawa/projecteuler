#!/usr/bin/python 

import sys
sys.path.append('../helpers')
import primes
import mathHelper
import itertools
import math

def findThreeSequence(primeList, x):
    primePermutations = list(itertools.permutations(primeList, 3))
    for l in primePermutations:
        diff1 = l[1] - l[0]
        diff2 = l[2] - l[1]
        if diff1 == diff2:
            return list(l)

    return []

def prob49():
    fourDigitPrimes = primes.getPrimeRange(1000, 10000)
    answers = []
    for d in fourDigitPrimes:
        charList = [c for c in str(d)]
        charPerms = list(itertools.permutations(charList))
        foundPrimes = [d]
        for d1 in charPerms:
            x = int(''.join(d1))
            if x in fourDigitPrimes and x not in foundPrimes: 
                foundPrimes.append(x)

        if len(foundPrimes) >= 3:
            a = findThreeSequence(foundPrimes, d)
            a.sort()
            if a != [] and a not in answers:
                print("Answer: %s - %s" % (a, ''.join([str(i) for i in a])))
                answers.append(a)

prob49()
