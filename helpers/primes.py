
def getPrimes():
    primes = []
    # Note: This will only return the first 1000 primes defined in the given text file
    with open("../datafiles/primes1.txt") as f:
    #with open("../datafiles/10000.txt") as f:
        for line in f:
            stringList = line.split()
            intList = [int(x) for x in stringList]
            for x in intList:
                primes.append(x)
    return primes

def getPrimesForTruncation():
    primes = getPrimes()
    sievePrimes = []
    for p in primes:
        pstr = str(p)
        if '0' in pstr:
            continue
        elif '5' in pstr[1:]:
            continue
        elif '2' in pstr[1:]:
            continue
        elif '1' == pstr[0:1]:
            continue
        elif int(pstr[0]) not in [2, 3, 5, 7]:
            continue
        elif int(pstr[-1]) not in [2, 3, 5, 7]:
            continue
        else:
            sievePrimes.append(p)
    return sievePrimes
