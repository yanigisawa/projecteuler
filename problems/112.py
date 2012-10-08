#!/usr/local/bin/python

from decimal import *
getcontext().prec = 10

def isIncreasing(num):
    strNum = str(num)

    prev = int(strNum[0])
    for c in strNum:
        if int(c) < prev:
            return False
        prev = int(c)

    return True

def isDecreasing(num):
    strNum = str(num)

    prev = int(strNum[0])
    for c in strNum:
        if int(c) > prev:
            return False
        prev = int(c)

    return True

def isBouncy(num):
    return not isIncreasing(num) and not isDecreasing(num)

#print "134468 - Inc: {0} - Dec: {1} - Bounce: {2}".format(isIncreasing(134468), isDecreasing(134468), isBouncy(134468))
#print "66420 - Inc: {0} - Dec: {1} - Bounce: {2}".format(isIncreasing(66420), isDecreasing(66420), isBouncy(66420))
#print "155349 - Inc: {0} - Dec: {1} - Bounce: {2}".format(isIncreasing(155349), isDecreasing(155349), isBouncy(155349))
#print "525 - Inc: {0} - Dec: {1} - Bounce: {2}".format(isIncreasing(525), isDecreasing(525), isBouncy(525))

isBouncyCount, total, proportion = 0, 1000000000, "0.99"
for i in xrange(1, total):
    if isBouncy(i):
        isBouncyCount += 1 

    #print "{3} - Inc: {0} - Dec: {1} - Bounce: {2}".format(isIncreasing(i), isDecreasing(i), isBouncy(i), i)
    if isBouncyCount > 0:
        if Decimal(isBouncyCount / Decimal(i)) == Decimal(proportion):
            print "Found it: {0} - ratio: {1}".format(i, isBouncyCount / Decimal(i))
            break
   
print isBouncyCount

