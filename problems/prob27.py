#!/usr/local/bin/python

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

def prob27():
    maxPrimeCount = 0
    primeProduct = 0
    coefficientProduct = 0
    a = -999
    aEnd = 1000
    bEnd = 1000
    while a < aEnd:
        b = -999
        while b < bEnd:
            n = 0
            while True:
                x = quadratic(a, b, n)
                prime = isPrime(x)
                if not prime:
                    break
                n = n + 1
            if n > maxPrimeCount:
                coefficientProduct = a * b
                print("New Max found, a: %s, b: %s, n: %s, a*b: %s" % (a, b, n, (a*b)))
                maxPrimeCount = n

            b = b + 1
        if a % 100 == 0:
            print("a: %s" % a)
        a = a + 1

    print("Prime Count %s, Product %s" % (maxPrimeCount, coefficientProduct))

def test():
    a = -79
    b = 1601
    n = 0
    while True:
        x = quadratic(a, b, n)
        if not isPrime(x):
            break
        n = n + 1
    print("Number of Primes: %s; a: %s, b: %s" % (n, a, b))

#test()
prob27()

