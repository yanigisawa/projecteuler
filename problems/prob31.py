#!/usr/bin/python

coins = [200, 100, 50, 20, 10, 5, 2, 1]

def test():
    combinations = 0
    for c in coins:
        total = c
        while total < 200:
            for d in coins:
                tmp = d + total
                if tmp < 200:
                    total += d
                elif tmp == 200:
                    combinations += 1
                    break
                else:
                    break

    print("combinations: %s" % combinations)
        


test()
