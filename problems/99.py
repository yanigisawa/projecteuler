#!/usr/local/bin/python

from math import log

def main():
    largest, largestLineNumber = 0, 0
    with open("../datafiles/base_exp.txt") as f:
        for lineNum, line in enumerate(f, start=1):
            base, exp = map(int, line.split(','))
            num = exp * log(base)
            if num > largest:
                largest, largestLineNumber = num, lineNum

    print "Largest Num: {0} - Line Number: {1}".format(largest, largestLineNumber)

main()
