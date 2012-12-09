#!/usr/local/bin/python

"""
Source code from: http://www.mathblog.dk/project-euler-51-eight-prime-family/
First of all we are looking for an 8 member family. And since we are looking
for the smallest member of the family our repeated digits has to be 0, 1 or 2. 
Otherwise we wont be able to make an eight member family.

Besides saying something about the size of the repeated digit we can also say
something about the number of repeated digits in the family. 
A number can be divided by 3 if the digit sum is is divisible by 3.  If we
calculate the digit sum mod 3 of the repeated digits we get the following
results with the number of repeated digits

Result	Number of repeated digits
-	1	2	3	4	5
0	4	4	10	4	4
1	3	3	0	3	3
2	3	3	0	3	3
If the number we have 1 repeated digit then the result n%3 will be 0 4 times,
namly for 0, 3, 6 and 9. It will be 1 a total of 3 times and 2 a total number
of 3 times.

That means that if we no matter what the digit sum of the non repeating digit
we will get at most 7 primes except if we use 3 repeating digits (or a
multiplum of three repeating digits). And the non repeating digits have a digit
sum mod 3 different from 0.

What more can be said is that a prime number always ends in 1,3, 7 or 9 for
primes larger than 10. This excludes the last digit from being a repeated
digit.

So now we know a bit more about the kind of prime we are looking for. I assume
that the prime will be 5 or 6 digits. It must have 3 digit being 0,1 or 2
excluding the last digit of the number.

So lets make some code.

"""

def get5digitPatterns():
    retVal = []

    retVal.append([ 1, 0, 0, 0, 1 ])
    retVal.append([ 0, 1, 0, 0, 1 ])
    retVal.append([ 0, 0, 1, 0, 1 ])
    retVal.append([ 0, 0, 0, 1, 1 ])

    return retVal

def get6digitPatterns():
    retVal = []

    retVal.append([ 1, 1, 0, 0, 0, 1 ]) 
    retVal.append([ 1, 0, 0, 1, 0, 1 ])
    retVal.append([ 1, 0, 0, 0, 1, 1 ])
    retVal.append([ 0, 1, 1, 0, 0, 1 ])
    retVal.append([ 0, 1, 0, 1, 0, 1 ])
    retVal.append([ 0, 1, 0, 0, 1, 1 ])
    retVal.append([ 0, 0, 1, 1, 0, 1 ])
    retVal.append([ 0, 0, 1, 0, 1, 1 ])
    retVal.append([ 0, 0, 0, 1, 1, 1 ])
    
    return retVal
    
def fillPattern(pattern, number):
    temp = number
    filledPattern = [0 for x in pattern]

    for i in range(len(pattern) - 1, -1, -1): # decrementing loop; -1 is step
        if (pattern[i] == 1): 
            filledPattern[i] = temp % 10
            temp = temp / 10
        else: 
            filledPattern[i] = -1
    return filledPattern

def generateNumber(repNumber, filledPattern):
    temp = 0
    for i in range(len(filledPattern)):
        temp = temp * 10

        if filledPattern[i] == -1: 
            temp += repNumber
        else:
            temp += filledPattern[i]
    return temp

def familySize(repeatingNumber, pattern):
    familySize = 1
    
    for i in range(repeatingNumber + 1, 10):
        if (isPrime(generateNumber(i, pattern))) : familySize += 1

    return familySize

def isPrime(n):
    if (n <= 1): return False
    if (n == 2): return True
    if (n % 2 == 0): return False
    if (n < 9): return True
    if (n % 3 == 0): return False
    
    counter = 5
    while ((counter * counter) <= n): 
        if (n % counter == 0): return False
        if (n % (counter + 2) == 0): return False
        counter += 6

    return True

"""
Since we will be replacing 3 digits in the number, we need to find the remaining
single digits. Looping from 11 to a max of 999 will generate at most a 3 digit
number to replace the 3 non-repeating digits in the resulting number; this number
is represented by 'i' in the following loop

'k' represents the possible repeating values of 0, 1, or 2, since all other 
possibilities have been excluded since we can't possibly achieve an 8 number
family with anything greater

'result' is initialized as a number greater than the largest possible 6 digit
value, since the resulting candidate number should be less than this value
"""
def problem51():

    fiveDigitPattern = get5digitPatterns()
    sixDigitPattern = get6digitPatterns()
    result = 1000000

    for i in range(11, 1000):

        # Only 1,3,7,9 are valid endings
        if (i % 5 == 0): continue

        if (i < 100):
            patterns = fiveDigitPattern
        else:
            patterns = sixDigitPattern

        for j in range(len(patterns)):
            for k in range(3):

                # Don't generate candidates with leading zero
                if (patterns[j][0] == 0 and k == 0): continue

                pattern = fillPattern(patterns[j], i)
                candidate = generateNumber(k, pattern)

                if (candidate < result and isPrime(candidate)):
                    if (familySize(k, pattern) == 8):
                        result = candidate                                                            
                break
    print result
            

problem51()
