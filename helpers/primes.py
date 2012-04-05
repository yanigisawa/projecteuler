import sys
import random 

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


# Code from: http://snippets.dzone.com/posts/show/4200
# Implements the Miller Rabin algorithm for primality testing

def toBinary(n):
  r = []
  while (n > 0):
    r.append(n % 2)
    n = n / 2
  return r

def test(a, n):
  """
  test(a, n) -> bool Tests whether n is complex.

  Returns:
    - True, if n is complex.
    - False, if n is probably prime.
  """
  b = toBinary(n - 1)
  d = 1
  for i in xrange(len(b) - 1, -1, -1):
    x = d
    d = (d * d) % n
    if d == 1 and x != 1 and x != n - 1:
      return True # Complex
    if b[i] == 1:
      d = (d * a) % n
  if d != 1:
    return True # Complex
  return False # Prime

def MillerRabin(n, s = 50):
  """
    MillerRabin(n, s = 1000) -> bool Checks whether n is prime or not

    Returns:
      - True, if n is probably prime.
      - False, if n is complex.
  """
  for j in xrange(1, s + 1):
    a = random.randint(1, n - 1)
    if (test(a, n)):
      return False # n is complex
  return True # n is prime

#def main(argv):
#  print MillerRabin(int(argv[0]), int(argv[1]))
#
#if __name__ == "__main__":
#  main(sys.argv[1:])

