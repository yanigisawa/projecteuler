#!/usr/local/bin/python

from math import sqrt

def loop():
    baseStr = "1{0}2{1}3{2}4{3}5{4}6{5}7{6}8{7}9{8}0"
    for a in range(1, 10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            for g in range(10):
                                for h in range(10):
                                    for i in range(10):
                                        num = int(baseStr.format(a, b, c, d, e, f, g, h, i))
                                        root = sqrt(num)
                                        squared = root * root

                                        if root % 1 == 0 and squared == num:
                                            print "Answer: {0} - num: {1}".format(root, num)
            print "b = {0}".format(b)
        print "a = {0}".format(a)


def main():
    square, i = 0, 1
    baseStr = "1234567890"
    while square < 992939495969798990:
        i += 1
        square = i * i

        lstrSquare = list(str(square))
        if len(lstrSquare) == 19:
            print "length equal 19: {0}".format(i)
            lstr = "".join(lstrSquare[0:19:2])
            if lstr == baseStr:
                print "Digit: {0}".format(i)
                break
        if len(lstrSquare) > 19:
            print "Length above 19: {0}".format(i)
            return

    print "not found: {0}".format(square)

main()

    
