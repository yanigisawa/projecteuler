#!/usr/bin/python

import time
coins = [200, 100, 50, 20, 10, 5, 2, 1]
#coins = [200, 100, 50]
combinations = 0


def findCombination(coinIndex, coinCount, purseTotal):
    global combinations
    if purseTotal > 200: return
    if coinIndex > (len(coins) - 1): return
    if purseTotal == 200:
        combinations += 1
        return

    while purseTotal < 200:
        #time.sleep(1)
        tmp = coins[coinIndex] * coinCount
        #print("Coin Index: %s - Purse Total %s - tmp: %s - Coin Count %s" 
        #    % (coinIndex, purseTotal, tmp, coinCount))
        if tmp + purseTotal == 200:
            combinations += 1
            purseTotal += tmp
            findCombination(coinIndex + 1, 1, 0)
            #return
        elif tmp + purseTotal > 200:
            findCombination(coinIndex + 1, 1, purseTotal)
            #break
        else:
            findCombination(coinIndex + 1, 1, tmp + purseTotal)
            coinCount += 1




def prob31():
    findCombination(0, 1, 0)
    print("Found combinations: %s" % combinations)

prob31()
