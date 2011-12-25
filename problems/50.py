#!/usr/bin/python

import sys
sys.path.append('../helpers')
import primes

allPrimes = [] #primes.getPrimesBelow(1000000)

def findConsecutivePrimeSum(x):
    runningAmount = x
    i = 0
    startingIndex = 0
    largestList = []
    runningList = []
    largest = 0
    while True:
        runningList = []
        runningAmount = x
        while runningAmount > 0:
            #print("Running Amount: %s - i: %s" % (runningAmount, i))
            runningAmount -= allPrimes[i]
            runningList.append(allPrimes[i])
            i += 1

        if runningAmount <= 0: 
            startingIndex += 1
            i = startingIndex

        if len(runningList) > largest and sum(runningList) == x:
            largest = len(runningList)
            largestList = runningList
            #print("New Largest %s" % largest)

        if allPrimes[i] > x:
           break 

    return largestList
            
def prob50():
    global allPrimes
    allPrimes = primes.getPrimesBelow(1000000)
    answer = 0
    largest = 0

    for p in allPrimes:
        if p < 990000:
            continue
        l = findConsecutivePrimeSum(p)
        if len(l) > largest:
            largest = len(l)
            answer = p
            print("new Largest found: %s - p: %s" % (largest, answer))
    print("Answer: %s" % answer)


prob50()
#l = findConsecutivePrimeSum(41)
#print("Length: %s - Sum: %s - %s " % (len(l), sum(l), l)) 
