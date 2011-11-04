import math

def quadratic(a, b, n):
    return (n * n) + a * n + b

def isPrime(x):
    y = 2
    x = math.fabs(x)
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

def isPerfectNumber(x):
    divisors = getDivisors(x)
    sum = 0
    for n in divisors:
        sum = sum + n
    return sum == x

def isAbundantNumber(x):
    divisors = getDivisors(x)
    sum = 0
    for n in divisors:
        sum = sum + n
    return sum > x

