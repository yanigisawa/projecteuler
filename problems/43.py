#!/usr/bin/python

import sys
sys.path.append('../helpers')
import itertools
import mathHelper

s = [2, 3, 5, 7, 11, 13, 17]

def isSubStringDivisor(x):
    xstr = x
    index = 0
    for i in range(1, 8):
        y = int(xstr[i:i+3])
        z = s[index]
        #print("y: %s - z: %s - y mod z: %s" % (y, z, (y % z)))
        if y % z != 0:
            return False
        index += 1

    return True

def prob43():
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    # Get a list of all permutations of the list above
    answer = []
    perms = list(itertools.permutations(digits))
    for p in perms:
        # Convert this permutation back into an integer
        num = ''.join(map(str, p))

        if isSubStringDivisor(num):
            print("found new divisor: %s" % num)
            answer.append(int(num))
        

    print("Answer List: %s" % answer)
    print("Sum: %s" % sum(answer))
    

#print("Is Divisor: %s" % isSubStringDivisor(1406357289))

prob43()


