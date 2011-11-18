#!/usr/bin/python

coins = [200, 100, 50, 20, 10, 5, 2, 1]
combinations = 0

def findCombination(coinIndex, coinCount, purseTotal):
    global combinations
    if purseTotal == 200:
        combinations += 1
        return
    if coinIndex > (len(coins) - 1): return 

    while True: 
        coinValue = coins[coinIndex] * coinCount
        newPurseTotal = coinValue + purseTotal
        findCombination(coinIndex + 1, 1, newPurseTotal)

        if newPurseTotal >= 200:
            findCombination(coinIndex + 1, 1, purseTotal)
            break
        else:
            coinCount += 1

def prob31():
    findCombination(0, 1, 0)
    print("Found combinations: %s" % combinations)

prob31()

#  $ time ./31.py 
#  Found combinations: XXXXX
#  
#  real 0m2.142s
#  user 0m2.128s
#  sys  0m0.011s
#  $ 
#  
