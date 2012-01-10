#!/usr/bin/python

def getSumOfSquares(x):
    sumOfSquares = 0
    for c in str(x):
        d = int(c)
        sq = d * d
        sumOfSquares += sq
    return sumOfSquares

def getSquareNumberSequence(x):
    seq = [x]
    current = x
    while True:
        sumOfSquares = getSumOfSquares(current)
        if (sumOfSquares == 1 or sumOfSquares == 89) and sumOfSquares in seq:
            break
        seq.append(sumOfSquares)
        current = sumOfSquares

    return seq

def getFinalRepeatingSquare(x):
    l = getSquareNumberSequence(x)
    return getSumOfSquares(l[-1])

def prob92():
    count = 0
    for i in range(1, 10000000):
        x = getFinalRepeatingSquare(i)
        if x == 89:
            count += 1
    print("Answer: %s" % count)

prob92()
