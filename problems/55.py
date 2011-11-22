#!/usr/bin/python

import sys
sys.path.append('../helpers')
import mathHelper

def getReverseNumber(x):
    x = str(x)[::-1]
    return int(x)

def prob55():
    lychrel = range(1, 10000)
    n = 1
    while n < 10001:
        tmpn = n
        m = 1
        while m < 51:
            m += 1
            nr = getReverseNumber(tmpn)
            tmpn = tmpn + nr
            if mathHelper.isPalindrome(tmpn):
                if n in lychrel:
                    lychrel.remove(n)
                break

        n += 1

    print(lychrel)
    print("Lychrel numbers: %s" % len(lychrel))

prob55()
