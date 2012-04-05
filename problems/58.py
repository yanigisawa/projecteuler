#!/usr/bin/python

import sys
sys.path.append('../helpers')
import mathHelper
import primes

def prob58():
    # (di, dj) is a vector - direction in which we move right now
    di = 1
    dj = 0
    # length of current segment
    segment_length = 1

    # current position (i, j) and how much of current segment we passed
    i = 0
    j = 0
    segment_passed = 0
    primeCount = 0
    allDiagnals = 1
    corner = False 
    k = 1
    checkPoint = 1000
    while True:
        # make a step, add 'direction' vector (di, dj) to current position (i, j)
        i += di
        j += dj
        segment_passed += 1
        if corner:
            #print("%s is on a corner" % k)
            if primes.MillerRabin(k) and k > 2: 
                primeCount += 1
            allDiagnals += 1
            corner = False
            ratio = primeCount / float(allDiagnals)

            if k > checkPoint:
                print("k: %s - Ratio: %s / %s = %s" % (k, primeCount, allDiagnals, ratio))
                checkPoint += 100000000

        if segment_passed == segment_length:
            # done with current segment
            segment_passed = 0;

            # 'rotate' directions
            buff = di
            di = -dj
            dj = buff
            corner = True

            # increase segment length if necessary
            if dj == 0:
                segment_length += 1
                if ratio < 0.1 and ratio > 0:
                    break
        k += 1

    ratio = primeCount / float(allDiagnals)
    print("Prime Ratio: %s / %s = %s" % (primeCount, allDiagnals, ratio))
    print("Side Length: %s" % segment_length)

prob58()

#Tried: 
#Prime Ratio: 5249 / 52491 = 0.0999980949115
#Side Length: 26246

# 50 = 3m 31s
# 1000 = 5m 24s
# 10000 = 23m 10s
