#!/usr/bin/python

def containSameDigits(x, y):

    xchars = [c for c in str(x)]
    ychars = [c for c in str(y)]

    if len(xchars) != len(ychars):
        return False

    for i in range(len(xchars)):
        if xchars[i] not in ychars:
            return False

        ychars.remove(xchars[i])

    return True

def prob52():
    m = 10000000
    answer = -1
    for i in range(1, m):
        a = i * 2
        b = i * 3
        c = i * 4
        d = i * 5
        e = i * 6
        a_b = containSameDigits(a, b)
        b_c = containSameDigits(b, c)
        c_d = containSameDigits(c, d)
        d_e = containSameDigits(d, e)
        if a_b and b_c and c_d and d_e:
            answer = i
            break
    print("Answer: %s" % answer)

prob52()
