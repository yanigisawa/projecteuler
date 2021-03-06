import math
import primes
import itertools

def quadratic(a, b, n):
    return (n * n) + a * n + b

def isPrime(x):
    y = 2
    x = math.fabs(x)
    if x % y == 0:
        return False
    while y < (x / 2):
        if x % y == 0:
            #print("Divisor: %s", y)
            return False
        y = y + 1
    return True

def getDivisors(x):
    divs = []
    x = int(math.fabs(x))
    end = (x / 2) + 1
    for y in range(1, end):
        if x % y == 0:
            divs.append(y)
    return divs

def getPrimeFactors(x):
    if x == 0:
        return [0]
    if x == 1:
        return [1]
    allPrimes = primes.getPrimesBelow(x)

    factors = []
    workingx = x
    while 1:
        if workingx == 1:
            break

        for p in allPrimes:
            if workingx % p == 0:
                factors.append(p)
                workingx /= p
                break
    return factors

def getGCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def reduceFraction(n, d):
    gcd = getGCD(n, d)
    newN = n / gcd
    newD = d / gcd
    return [newN, newD]

def isPerfectNumber(x):
    divisors = getDivisors(x)
    sum = 0
    for n in divisors:
        sum = sum + n
    return sum == x

def isAbundantNumber(x):
    divisors = getDivisors(x)
    return sum(divisors) > x

def getCombinations(n, r):
    numerator = math.factorial(n)
    denominator = math.factorial(r) * math.factorial(n - r)
    return numerator / denominator

def isPandigital(n):
    nstr = str(n)
    cpy = nstr
    for x in range(1, len(nstr) + 1):
        if str(x) in nstr:
            cpy = cpy.replace(str(x), "", 1) # replace only 1 character
        else:
            return False

    return cpy == ""

def isPalindrome(n):
    n = str(n)
    # note [::-1] will reverse a string
    return n == n[::-1]

def getPentagonal(n):
    return n * (3 * n - 1) / 2

def isPentagonal(x):
    n = (math.sqrt(24 * x + 1) + 1) / float(6)
    return n % 1 == 0

def coprime(a, b):
    return getGCD(a, b) == 1

def phi(m):
    if m == 1:
        return 1
    else:
        r = [n for n in range(1,m) if coprime(m,n)]
        return len(r)

def prime_factors(value):
    if value > 3:
        for i in itertools.chain(iter([2]), xrange(3, int(value ** 0.5) + 1, 2)):
            if i * i > value: break
            while not (value % i):
                if value == i: break
                value /= i
                yield i
    yield value

def prime_factors_mult(n):
    res = list(prime_factors(n))
    return sorted([fact, res.count(fact)] for fact in set(res))

def totient(n):
    from operator import mul

    if n == 1: return 1

    return reduce(mul, [(p - 1) * p ** (m - 1) for p, m in prime_factors_mult(n)])
