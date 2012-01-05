#!/usr/bin/python

def prob63():
    count = 0
    for base in range(1, 100):
        for exp in range(1, 100):
            x = base ** exp
            if len(str(x)) == exp:
                count += 1
            elif len(str(x)) > exp:
                break

    print("Answer: %s" % count)

prob63()
