
def getPrimes():
    primes = []
    # Note: This will only return the first 1000 primes defined in the given text file
    with open("../datafiles/primes1.txt") as f:
    #with open("../datafiles/10000.txt") as f:
        for line in f:
            stringList = line.split()
            intList = [int(x) for x in stringList]
            primes.extend(intList)
    return primes

def getPrimesBelow(x):
    primes = []
    with open("../datafiles/primes1.txt") as f:
        for line in f:
            stringList = line.split()
            intList = [int(y) for y in stringList]
            for i in intList:
                if i > x:
                    return primes
                else:
                    primes.append(i)
    return primes

def getPrimeRange(x, y):
    tmpPrimes = getPrimesBelow(y)
    primeRange = []
    for p in tmpPrimes:
        if p > x:
            primeRange.append(p)

    return primeRange

