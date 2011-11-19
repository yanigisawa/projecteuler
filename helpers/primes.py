
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

