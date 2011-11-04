from math import *

foundOne = False

x = "40586"
# 145, 40585

while not foundOne:
	y = 0
	for c in x:
		y += factorial(int(c))

	if int(x) % 10000 == 0:
		print "X: %s Y: %s" % (x, y)

	if y == int(x):
		print "Found one: %s" % (y)
		break
	x = str(int(x) + 1)


