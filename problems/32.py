#!/usr/bin/python

import sys
sys.path.append('../helpers/')
import mathHelper

def isProductPanDigital(x, y, p):
    s = "%s%s%s" % (str(x), str(y), str(p))
    if len(s) != 9: return False
    return mathHelper.isPandigital(s)

def prob32():
    products = []
    for i in range(1, 2000):
        for j in range(1, i + 1):
            prod = i * j
            if isProductPanDigital(i, j, prod):
                if prod not in products:
                    products.append(prod)
                print("%s * %s = %s - is Pandigital" % (i, j, prod))
    print("Products: %s" % products)
    print("Sum %s" % sum(products))

prob32()
