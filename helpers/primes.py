
def getPrimes():
    primes = []
    # Note: This will only return the first 1000 primes defined in the given text file
    with open("../datafiles/1000.txt") as f:
        for line in f:
            stringList = line.split()
            intList = [int(x) for x in stringList]
            for x in intList:
                primes.append(x)
    return primes


