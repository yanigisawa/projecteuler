
def sqrt_list(n, precision):
    ndigits = []        # break n into list of digits
    n_int = int(n)
    n_fraction = n - n_int

    while n_int:                            # generate list of digits of integral part
        ndigits.append(n_int % 10)
        n_int /= 10
    if len(ndigits) % 2: ndigits.append(0)  # ndigits will be processed in groups of 2

    decimal_point_index = len(ndigits) / 2  # remember decimal point position
    while n_fraction:                       # insert digits from fractional part
        n_fraction *= 10
        ndigits.insert(0, int(n_fraction))
        n_fraction -= int(n_fraction)
    if len(ndigits) % 2: ndigits.insert(0, 0)  # ndigits will be processed in groups of 2

    rootlist = []
    root = carry = 0                        # the algorithm
    while root == 0 or (len(rootlist) < precision and (ndigits or carry != 0)):
        carry = carry * 100
        if ndigits: carry += ndigits.pop() * 10 + ndigits.pop()
        x = 9
        while (20 * root + x) * x > carry:
                x -= 1
        carry -= (20 * root + x) * x
        root = root * 10 + x
        rootlist.append(x)
    return rootlist, decimal_point_index

def getDec(numList):
    s = "{0}.".format(str(numList[1]))
    for x in numList[0]:
        s += str(x)
    return s

def problem80():
    totalSum = 0
    for x in range(1, 101):
        l = sqrt_list(x, 100)
        if len(l[0]) == 100:
            print "N: {0} - sqrt: {1}".format(x, getDec(l))
            for n in l[0]:
                totalSum += n
    print totalSum

problem80()

